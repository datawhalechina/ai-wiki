#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成「二、Coding Plan」章节的两张对比图。

设计要点：
  - 图表由脚本生成而非截图，价格变更后重跑即可刷新，不会像旧截图那样迅速过期。
  - 数据集中在 DATA 区，修改价格只改这里。
  - 图内标注核查日期。

输出（写到 docs/chapter02/）：
  CodingPlan_Compare.png   入门档价格对比（横向条形图）
  CodingPlan_Compare2.png  各厂商价格带对比（对数刻度哑铃图）

用法：
  python3 scripts/gen_coding_plan_charts.py [--out DIR]
"""

import argparse
import os
import sys

try:
    import matplotlib
except ImportError:
    sys.exit("缺少 matplotlib，请先安装：pip install matplotlib")

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

# ---------------------------------------------------------------- 数据区


# 入门档价格（人民币/月）。key = 图例名，value = (显示名, 入门价, 厂商类型, 备注)
# 厂商类型：cn = 国产 / intl = 国际
ENTRY_PRICING = [
    ("huawei",   "华为云码道",      0,   "cn",   "体验版永久免费"),
    ("unicom",   "联通云元景",      15,  "cn",   "星罗 Token 服务"),
    ("tencent_hy", "腾讯云 Hy 线",   28,  "cn",   "混元专属"),
    ("tencent_gen", "腾讯云通用线",  39,  "cn",   "多模型"),
    ("xiaomi",   "小米 MiMo",      39,  "cn",   ""),
    ("volcano",  "方舟 Coding Plan", 40, "cn",   "限时 2.5 折至 ¥9.9"),
    ("kimi",     "Kimi 会员",      49,  "cn",   "四档均可调用 Kimi Code"),
    ("minimax",  "MiniMax Token Plan", 49, "cn", "国际站 $22"),
    ("glm",      "智谱 GLM",       118, "cn",   "自 49 元起上调"),
    ("xfyun",    "讯飞 Astron",    199, "cn",   "原 19 元档已下线"),
    ("aliyun",   "阿里云 Coding Plan", 200, "cn", "Lite 已停售，新客首月 ¥39.9"),
    ("opencode", "OpenCode Go",    72,  "intl", "$10/月，按 7.2 折算"),
]

# 各厂商完整价格带（人民币/月）。key = 显示名，value = [各档价格]
PRICE_BANDS = [
    ("智谱 GLM",            [118, 538, 1078]),
    ("Kimi 会员",           [49, 99, 199, 699]),
    ("小米 MiMo",           [39, 99, 329, 659]),
    ("腾讯云通用 Token Plan", [39, 99, 299, 599]),
    ("腾讯云 Hy Token Plan", [28, 78, 238, 468]),
    ("MiniMax Token Plan",  [49, 119, 469]),
    ("华为云码道",           [0, 98, 198, 498]),
    ("方舟 Coding Plan",     [40, 200]),
    ("联通云元景",           [15, 30, 45]),
    ("讯飞 Astron",         [199, 999]),
    ("阿里云 Coding Plan",   [200]),
]

USD_CNY = 7.2
VERIFIED_ON = "2026-09-23"

# ---------------------------------------------------------------- 字体

CJK_CANDIDATES = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
]


def setup_font():
    for path in CJK_CANDIDATES:
        if os.path.exists(path):
            font_manager.fontManager.addfont(path)
            name = font_manager.FontProperties(fname=path).get_name()
            plt.rcParams["font.family"] = name
            break
    else:
        print("⚠️  未找到中文字体，图中中文可能显示为方块", file=sys.stderr)
    plt.rcParams["axes.unicode_minus"] = False


# ---------------------------------------------------------------- 配色

BG = "#ffffff"
FG = "#1f2328"
MUTED = "#6b7280"
GRID = "#e6e9ee"
BAR = "#3f6fb5"
BAR_FREE = "#e08a2e"
BAR_INTL = "#8a63c9"


def style_axes(ax):
    ax.set_facecolor(BG)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0)


def draw_entry_chart(out_path):
    rows = sorted(ENTRY_PRICING, key=lambda r: r[2])
    labels = [r[1] for r in rows]
    values = [r[2] for r in rows]
    colors = []
    for r in rows:
        if r[2] == 0:
            colors.append(BAR_FREE)
        elif r[3] == "intl":
            colors.append(BAR_INTL)
        else:
            colors.append(BAR)

    fig, ax = plt.subplots(figsize=(14, 6.8), dpi=138)
    fig.patch.set_facecolor(BG)
    style_axes(ax)

    y = range(len(rows))
    # 免费档值 0，画一个极短的可见条示意
    plot_values = [v if v > 0 else 0.8 for v in values]
    ax.barh(y, plot_values, color=colors, height=0.62, zorder=3)

    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=11, color=FG)
    ax.invert_yaxis()
    ax.set_xlim(0, max(plot_values) * 1.28)
    ax.set_xlabel("入门档月费（人民币元）", fontsize=10.5, color=MUTED, labelpad=8)
    ax.xaxis.grid(True, color=GRID, linewidth=0.9, zorder=0)
    ax.set_axisbelow(True)

    for yi, (row, pv) in enumerate(zip(rows, plot_values)):
        val, note = row[2], row[4]
        label = "免费" if val == 0 else f"{val:g}"
        ax.text(pv + max(plot_values) * 0.012, yi, label,
                va="center", ha="left", fontsize=11, color=FG, fontweight="bold")
        if note:
            ax.text(pv + max(plot_values) * 0.085, yi, note,
                    va="center", ha="left", fontsize=8.6, color=MUTED)

    ax.set_title("主流 AI 编程订阅套餐 · 入门档价格对比",
                 fontsize=17, color=FG, fontweight="bold", pad=26, loc="left")
    fig.text(0.01, 0.945,
             f"价格核查于 {VERIFIED_ON} · 官方刊例价，未计限时折扣与新客优惠 · 仅横向比入门门槛，不代表单位价格高低",
             fontsize=9.2, color=MUTED, ha="left")
    fig.text(0.99, 0.02,
             "数据来源：各厂商官方定价页 / 帮助文档",
             fontsize=8.4, color=MUTED, ha="right")

    fig.tight_layout(rect=(0, 0.035, 1, 0.9))
    fig.savefig(out_path, facecolor=BG)
    plt.close(fig)
    print(f"✅ {out_path}")


def draw_band_chart(out_path):
    rows = sorted(PRICE_BANDS, key=lambda r: min(v for v in r[1] if v > 0))
    fig, ax = plt.subplots(figsize=(13.4, 6.9), dpi=138)
    fig.patch.set_facecolor(BG)
    style_axes(ax)

    floor = 8.0  # 对数轴下限，用于安置 0 元档的示意点
    for yi, (name, prices) in enumerate(rows):
        positive = [p for p in prices if p > 0]
        shifted = [p if p > 0 else floor for p in prices]
        ax.plot([min(shifted), max(shifted)], [yi, yi],
                color="#cfd8e3", linewidth=6, solid_capstyle="round", zorder=2)
        for p, s in zip(prices, shifted):
            free = p == 0
            ax.scatter([s], [yi], s=118, zorder=4,
                       color=BAR_FREE if free else "#ffffff",
                       edgecolors=BAR_FREE if free else BAR,
                       linewidths=2.1)
            txt = "免费" if free else f"{p:g}"
            ax.text(s, yi - 0.42, txt, ha="center", va="bottom",
                    fontsize=8.8, color=BAR_FREE if free else FG)

    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=11, color=FG)
    ax.invert_yaxis()
    ax.set_xscale("log")
    ax.set_xlim(floor * 0.82, 1750)
    ax.set_xticks([15, 50, 100, 200, 500, 1000])
    ax.set_xticklabels(["15", "50", "100", "200", "500", "1000"], fontsize=10)
    ax.xaxis.grid(True, color=GRID, linewidth=0.9, zorder=0)
    ax.set_axisbelow(True)
    ax.set_xlabel("月费（人民币元，对数刻度）", fontsize=10.5, color=MUTED, labelpad=8)
    ax.set_ylim(len(rows) - 0.45, -1.15)

    ax.set_title("各厂商 Coding / Token Plan 价格带（入门 → 顶配）",
                 fontsize=17, color=FG, fontweight="bold", pad=30, loc="left")
    fig.text(0.01, 0.935,
             f"价格核查于 {VERIFIED_ON} · 每点为一档套餐 · 对数刻度下等距＝倍率相同",
             fontsize=9.2, color=MUTED, ha="left")
    fig.text(0.99, 0.02,
             "「入门便宜、重度变贵」：最低门槛已下探至 0-15 元，最高档位则普遍上移至 500-1100 元",
             fontsize=8.8, color=MUTED, ha="right")

    fig.tight_layout(rect=(0, 0.035, 1, 0.9))
    fig.savefig(out_path, facecolor=BG)
    plt.close(fig)
    print(f"✅ {out_path}")


def main():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_out = os.path.join(here, "docs", "chapter02")
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=default_out, help="输出目录")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    setup_font()
    draw_entry_chart(os.path.join(args.out, "CodingPlan_Compare.png"))
    draw_band_chart(os.path.join(args.out, "CodingPlan_Compare2.png"))


if __name__ == "__main__":
    main()
