import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import subprocess, sys

subprocess.run([sys.executable, "benchmark_data.py"], check=True, capture_output=True)

df_h = pd.read_csv("benchmark_human_likeness.csv", encoding="utf-8-sig")
df_a = pd.read_csv("benchmark_agentic.csv", encoding="utf-8-sig")
df_elo = pd.read_csv("benchmark_elo_trend.csv", encoding="utf-8-sig")

MODELS = ["ChatGPT_GPT5", "Claude_Opus46", "Gemini_31Pro"]
LABELS = {"ChatGPT_GPT5": "ChatGPT (GPT-5)", "Claude_Opus46": "Claude (Opus 4.6)", "Gemini_31Pro": "Gemini (3.1 Pro)"}
COLORS = {"ChatGPT_GPT5": "#10A37F", "Claude_Opus46": "#CC785C", "Gemini_31Pro": "#4285F4"}

def normalize(df):
    out = df.copy()
    for m in MODELS:
        out[m + "_norm"] = (df[m] / df["Max_Score"] * 100).round(1)
    return out

df_h = normalize(df_h)
df_a = normalize(df_a)

# ── 1. 레이더 차트 ────────────────────────────────────────────────────
def radar_chart():
    fig, axes = plt.subplots(1, 2, figsize=(16, 7), subplot_kw=dict(polar=True))

    for ax, df, title in [
        (axes[0], df_h, "Human-Likeness Benchmarks"),
        (axes[1], df_a, "Agentic AI Benchmarks"),
    ]:
        categories = df["Benchmark"].tolist()
        N = len(categories)
        angles = [n / N * 2 * np.pi for n in range(N)]
        angles += angles[:1]

        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, size=8)
        ax.set_ylim(0, 105)
        ax.set_yticks([25, 50, 75, 100])
        ax.set_yticklabels(["25", "50", "75", "100"], size=7, color="grey")
        ax.set_title(title, size=12, fontweight="bold", pad=20)

        for m in MODELS:
            vals = df[m + "_norm"].tolist()
            vals += vals[:1]
            ax.plot(angles, vals, linewidth=2, label=LABELS[m], color=COLORS[m])
            ax.fill(angles, vals, alpha=0.08, color=COLORS[m])

    axes[0].legend(loc="upper right", bbox_to_anchor=(1.4, 1.15), fontsize=9)
    plt.suptitle("ChatGPT vs Claude vs Gemini\nHuman-Likeness & Agentic AI Benchmark Comparison",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig("benchmark_radar.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("저장: benchmark_radar.png")

# ── 2. 막대 비교 차트 ─────────────────────────────────────────────────
def bar_comparison():
    fig, axes = plt.subplots(2, 1, figsize=(14, 12))

    for ax, df, title in [
        (axes[0], df_h, "Human-Likeness Benchmarks (Normalized Score)"),
        (axes[1], df_a, "Agentic AI Benchmarks (Normalized Score)"),
    ]:
        x = np.arange(len(df))
        width = 0.26
        for i, m in enumerate(MODELS):
            bars = ax.bar(x + i * width, df[m + "_norm"], width,
                          label=LABELS[m], color=COLORS[m], edgecolor="white", alpha=0.9)
            for bar in bars:
                h = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, h + 0.5,
                        f"{h:.0f}", ha="center", va="bottom", fontsize=7)

        ax.set_xticks(x + width)
        ax.set_xticklabels(df["Benchmark"], rotation=25, ha="right", fontsize=9)
        ax.set_ylim(0, 115)
        ax.set_ylabel("Normalized Score (0-100)")
        ax.set_title(title, fontweight="bold", fontsize=11)
        ax.legend(fontsize=9)
        ax.grid(axis="y", alpha=0.3)

    plt.suptitle("Competitive Benchmark Analysis: ChatGPT vs Claude vs Gemini",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig("benchmark_bars.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("저장: benchmark_bars.png")

# ── 3. ELO 트렌드 ────────────────────────────────────────────────────
def elo_trend_chart():
    fig, ax = plt.subplots(figsize=(12, 5))
    for m, label, color in [
        ("ChatGPT", "ChatGPT", "#10A37F"),
        ("Claude",  "Claude",  "#CC785C"),
        ("Gemini",  "Gemini",  "#4285F4"),
    ]:
        vals = df_elo[m].tolist()
        dates = df_elo["Date"].tolist()
        valid = [(d, v) for d, v in zip(dates, vals) if pd.notna(v)]
        ax.plot([v[0] for v in valid], [v[1] for v in valid],
                marker="o", label=label, color=color, linewidth=2.5, markersize=7)
        ax.annotate(f"{valid[-1][1]:.0f}", xy=(valid[-1][0], valid[-1][1]),
                    xytext=(5, 5), textcoords="offset points", color=color, fontsize=9)

    ax.set_title("Chatbot Arena ELO Score Trend (2023-2025)\n(Human Preference Voting — Proxy for Human-Likeness)",
                 fontweight="bold", fontsize=11)
    ax.set_xlabel("Date")
    ax.set_ylabel("ELO Score")
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("benchmark_elo_trend.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("저장: benchmark_elo_trend.png")

# ── 4. 2×2 포지셔닝 매트릭스 ─────────────────────────────────────────
def positioning_matrix():
    human_avg = {m: df_h[m + "_norm"].mean() for m in MODELS}
    agentic_avg = {m: df_a[m + "_norm"].mean() for m in MODELS}

    fig, ax = plt.subplots(figsize=(9, 8))
    ax.axhline(y=85, color="grey", linestyle="--", alpha=0.5)
    ax.axvline(x=85, color="grey", linestyle="--", alpha=0.5)

    for m in MODELS:
        ax.scatter(human_avg[m], agentic_avg[m], s=400,
                   color=COLORS[m], zorder=5, edgecolor="white", linewidth=2)
        ax.annotate(LABELS[m],
                    xy=(human_avg[m], agentic_avg[m]),
                    xytext=(8, 8), textcoords="offset points",
                    fontsize=11, fontweight="bold", color=COLORS[m])
        ax.annotate(f"({human_avg[m]:.1f}, {agentic_avg[m]:.1f})",
                    xy=(human_avg[m], agentic_avg[m]),
                    xytext=(8, -14), textcoords="offset points",
                    fontsize=9, color="grey")

    ax.set_xlabel("Human-Likeness Score (avg normalized)", fontsize=12)
    ax.set_ylabel("Agentic AI Score (avg normalized)", fontsize=12)
    ax.set_title("Competitive Positioning Matrix\nHuman-Likeness vs Agentic AI Attributes",
                 fontsize=13, fontweight="bold")

    ax.text(72, 87, "High Agentic\nLow Human-Like", fontsize=9, color="grey", alpha=0.6)
    ax.text(87, 87, "High Agentic\nHigh Human-Like", fontsize=9, color="grey", alpha=0.6)
    ax.text(72, 78, "Low Agentic\nLow Human-Like", fontsize=9, color="grey", alpha=0.6)
    ax.text(87, 78, "Low Agentic\nHigh Human-Like", fontsize=9, color="grey", alpha=0.6)

    ax.set_xlim(70, 100)
    ax.set_ylim(75, 95)
    ax.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig("benchmark_positioning.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("저장: benchmark_positioning.png")

# ── 5. 요약 테이블 출력 ──────────────────────────────────────────────
def print_summary():
    print("\n" + "="*65)
    print("  경쟁우위 분석 요약")
    print("="*65)

    for dim, df in [("Human-Likeness", df_h), ("Agentic AI", df_a)]:
        print(f"\n[{dim}] 평균 정규화 점수")
        avgs = {LABELS[m]: df[m + "_norm"].mean() for m in MODELS}
        for name, avg in sorted(avgs.items(), key=lambda x: -x[1]):
            bar = "=" * int(avg / 2)
            print(f"  {name:<25} {avg:5.1f}  {bar}")

    print("\n[벤치마크별 1위]")
    all_df = pd.concat([df_h, df_a])
    for _, row in all_df.iterrows():
        scores = {LABELS[m]: row[m + "_norm"] for m in MODELS}
        winner = max(scores, key=scores.get)
        print(f"  {row['Benchmark']:<30} -> {winner} ({scores[winner]:.1f})")

    print("\n[연구 시사점]")
    print("  ChatGPT: 사실 정확성·지식 강점 → 인간 유사성 우위")
    print("  Claude : 감성·맥락 일관성 강점 → 인간 유사성 차별화")
    print("  Gemini : 추론·코딩·멀티모달 강점 → 에이전틱 속성 우위")
    print("  → 3개 서비스의 경쟁우위 축이 명확히 분리됨")
    print("="*65)

if __name__ == "__main__":
    radar_chart()
    bar_comparison()
    elo_trend_chart()
    positioning_matrix()
    print_summary()
    print("\nDone. Generated files:")
    print("  benchmark_radar.png       - Radar chart")
    print("  benchmark_bars.png        - Bar comparison")
    print("  benchmark_elo_trend.png   - ELO trend")
    print("  benchmark_positioning.png - 2x2 Positioning matrix")
