#!/usr/bin/env bash
#
# update_stars.sh — 用 gh api 批量刷新 ai-wiki 文档中的 GitHub star 数
#
# 用法
#   scripts/update_stars.sh               # 默认：只检查并输出差异，不写文件
#   scripts/update_stars.sh --apply       # 实际写入文件
#   scripts/update_stars.sh --check       # 同默认，但有差异时退出码 1（可用于 CI / pre-commit）
#   scripts/update_stars.sh --repo owner/name
#                                         # 只查单个仓库的实测值，不读 MANIFEST
#
# 依赖
#   gh（已登录）、python3
#
# 数字格式约定（由 fmt() 统一产出，与文档现有风格一致）
#   n < 1,000        -> 原样，如 842
#   1,000 ~ 999,999  -> 保留 1 位小数的 K，如 2.9K / 52.7K / 390.3K
#   n >= 1,000,000   -> 保留 1 位小数的 M，如 1.2M
#   替换时会去掉旧值里的 "+"（有了精确实测值后 "122K+" 这种保守写法不再需要）
#
# MANIFEST 格式（每行一条，字段用 :: 分隔）
#   <owner/repo>::<文档相对路径>::<该行唯一匹配片段>::<说明>
#
#   * 用「行级唯一片段」而不是仓库名定位，是因为同一仓库的星标常在同一章节
#     出现多次，且可能跨章节出现（如 openclaw 在 ch01 出现 4 次、
#     Claude Code 跨 ch04/ch08）。片段要能唯一定位到目标那一行。
#   * 若某处星标是「历史快照」（例如时间线里"仅 6 个月达到 370K star"
#     描述的是当时节点），不要加进 MANIFEST —— 它不该随最新值变动。
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

APPLY=0
CHECK=0
SINGLE_REPO=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --apply) APPLY=1; shift ;;
    --check) CHECK=1; shift ;;
    --repo)  SINGLE_REPO="${2:-}"; shift 2 ;;
    -h|--help) sed -n '2,32p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "未知参数: $1（用 --help 查看用法）" >&2; exit 2 ;;
  esac
done

if ! command -v gh >/dev/null 2>&1; then
  echo "❌ 找不到 gh 命令。请先安装 GitHub CLI 并执行 gh auth login" >&2
  exit 1
fi

# ---------------------------------------------------------------- 单仓库查询模式
if [[ -n "$SINGLE_REPO" ]]; then
  gh api "repos/$SINGLE_REPO" \
    --jq '"\(.full_name)  star=\(.stargazers_count)  forks=\(.forks_count)  pushed=\(.pushed_at[0:10])"' \
    || { echo "❌ 查询失败：$SINGLE_REPO" >&2; exit 1; }
  exit 0
fi

MANIFEST="$SCRIPT_DIR/stars.manifest"
[[ -f "$MANIFEST" ]] || { echo "❌ 找不到清单文件：$MANIFEST" >&2; exit 1; }

# ------------------------------------------------------- 1. 抽取 MANIFEST 中的仓库
REPOS="$(python3 - "$MANIFEST" <<'PY'
import sys
seen, out = set(), []
for raw in open(sys.argv[1], encoding="utf-8"):
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        continue
    repo = raw.split("::")[0].strip()
    if repo and repo not in seen:
        seen.add(repo)
        out.append(repo)
print("\n".join(out))
PY
)"

STARS_FILE="$(mktemp -t aiwiki-stars)"
trap 'rm -f "$STARS_FILE"' EXIT

echo "→ 正在用 gh api 拉取 $(printf '%s\n' "$REPOS" | grep -c . ) 个仓库的 star 数…"
FAILED=0
while IFS= read -r repo; do
  [[ -n "$repo" ]] || continue
  n="$(gh api "repos/$repo" --jq '.stargazers_count' 2>/dev/null)" || n=""
  if [[ -z "$n" ]]; then
    echo "  ⚠️  获取失败（仓库可能已改名/删除/无权限）：$repo" >&2
    FAILED=$((FAILED + 1))
    continue
  fi
  printf '%s\t%s\n' "$repo" "$n" >> "$STARS_FILE"
done <<< "$REPOS"

if [[ ! -s "$STARS_FILE" ]]; then
  echo "❌ 没有取到任何 star 数，终止。" >&2
  exit 1
fi

# ------------------------------------------------------------- 2. 比对并（可选）写入
MANIFEST="$MANIFEST" \
STARS_FILE="$STARS_FILE" \
REPO_ROOT="$REPO_ROOT" \
APPLY="$APPLY" \
CHECK="$CHECK" \
python3 <<'PY'
import collections
import os
import re
import sys

manifest_path = os.environ["MANIFEST"]
stars_path = os.environ["STARS_FILE"]
root = os.environ["REPO_ROOT"]
apply_ = os.environ["APPLY"] == "1"
check = os.environ["CHECK"] == "1"

stars = {}
for line in open(stars_path, encoding="utf-8"):
    line = line.rstrip("\n")
    if not line:
        continue
    repo, n = line.split("\t", 1)
    stars[repo] = int(n)


def fmt(n):
    """把原始 star 数格式化为文档里通用写法。"""
    if n < 1_000:
        return str(n)
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    return f"{n / 1_000:.1f}K"


# 匹配 "370K star" / "122K+ GitHub 星标" / "（23K+ star）" 里的数字部分
TOKEN = re.compile(r"\d[\d,.]*K?\+?(?=\s*(?:star|GitHub 星标|星标))")

entries = []
for raw in open(manifest_path, encoding="utf-8"):
    raw = raw.rstrip("\n")
    if not raw.strip() or raw.lstrip().startswith("#"):
        continue
    parts = raw.split("::")
    if len(parts) < 4:
        print(f"  ⚠️  MANIFEST 格式错误，已跳过：{raw}", file=sys.stderr)
        continue
    entries.append(tuple(p.strip() for p in parts[:4]))

cache = {}
changed_files = set()
changes = []
handled = collections.Counter()
sames = 0

for repo, rel, match, note in entries:
    path = os.path.join(root, rel)
    if rel not in cache:
        try:
            with open(path, encoding="utf-8") as fh:
                cache[rel] = fh.read().split("\n")
        except FileNotFoundError:
            print(f"  ⚠️  文件不存在，已跳过：{rel}", file=sys.stderr)
            cache[rel] = None
            continue
    lines = cache[rel]
    if lines is None:
        continue
    if repo not in stars:
        print(f"  ⚠️  未取得 {repo} 的 star 数，跳过该条目", file=sys.stderr)
        continue

    new = fmt(stars[repo])
    for idx, ln in enumerate(lines):
        if match not in ln:
            continue
        key = (rel, idx)
        if handled[key]:
            continue  # 该行已由更靠前的条目处理，避免重复替换
        handled[key] += 1
        m = TOKEN.search(ln)
        if not m:
            print(
                f"  ⚠️  {rel}:{idx + 1} 命中片段 “{match}” 但该行没有 star 数字，跳过",
                file=sys.stderr,
            )
            continue
        old = m.group(0)
        if old == new:
            sames += 1
            continue
        lines[idx] = TOKEN.sub(lambda _: new, ln, count=1)
        changed_files.add(rel)
        changes.append((rel, idx, old, new, repo))

if not changes:
    print(f"\n✅ 全部 {len(entries)} 条已是最新（{sames} 条值未变），无需修改。")
    sys.exit(0)

print(f"\n发现 {len(changes)} 处需要更新，涉及 {len(changed_files)} 个文件：\n")
print("| 位置 | 现状 | 实测 | 仓库 |")
print("| --- | --- | --- | --- |")
for rel, idx, old, new, repo in changes:
    print(f"| `{rel}:{idx + 1}` | {old} | **{new}** | `{repo}` |")

if apply_:
    for rel in sorted(changed_files):
        with open(os.path.join(root, rel), "w", encoding="utf-8") as fh:
            fh.write("\n".join(cache[rel]))
    print(f"\n✅ 已写入 {len(changed_files)} 个文件。")
    print("   下一步：检查 git diff，并同步在 log.md 记录本次刷新。")
else:
    print("\n（这是预演，未写入任何文件。确认无误后加 --apply 执行。）")

if check:
    sys.exit(1)
PY
