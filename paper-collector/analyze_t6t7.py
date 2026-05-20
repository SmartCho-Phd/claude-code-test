import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings('ignore')

INPUT_FILE = 'T6_T7_papers.csv'

STOP_WORDS = [
    'ai', 'artificial', 'intelligence', 'study', 'paper', 'research',
    'results', 'based', 'using', 'used', 'proposed', 'approach',
    'method', 'model', 'system', 'data', 'analysis', 'review',
    'new', 'also', 'however', 'thus', 'may', 'use', 'show',
    'provide', 'present', 'found', 'two', 'three', 'one', 'well',
    'large', 'language', 'models', 'llm', 'gpt', 'chatgpt',
]

def load():
    df = pd.read_csv(INPUT_FILE, encoding='utf-8-sig')
    orig = pd.read_csv('agentic_consciousness_papers.csv', encoding='utf-8-sig')
    df = df.merge(orig[['title', 'abstract']], on='title', how='left')
    df['abstract'] = df['abstract'].fillna('')
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['cited_by'] = pd.to_numeric(df['cited_by'], errors='coerce').fillna(0).astype(int)
    df['topic_group'] = df['topic_label'].str[:2]
    return df

# ── 1. 연도별 트렌드 ──────────────────────────────────────────
def plot_yearly_trend(df):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    yearly = df.groupby(['year', 'topic_group']).size().unstack(fill_value=0)
    yearly_total = df.groupby('year').size()

    colors = {'T6': '#4C9BE8', 'T7': '#E8834C'}
    for col in ['T6', 'T7']:
        if col in yearly.columns:
            axes[0].plot(yearly.index, yearly[col], marker='o', label=col,
                        color=colors.get(col), linewidth=2.5, markersize=7)

    axes[0].set_title('Yearly Paper Count by Topic (T6 vs T7)', fontweight='bold', fontsize=12)
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Number of Papers')
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    axes[0].set_xticks([2022, 2023, 2024, 2025])

    axes[1].bar(yearly_total.index, yearly_total.values, color='#6C8EBF', edgecolor='white')
    for x, y in zip(yearly_total.index, yearly_total.values):
        axes[1].text(x, y + 1, str(y), ha='center', fontsize=11, fontweight='bold')
    axes[1].set_title('Total T6+T7 Papers per Year', fontweight='bold', fontsize=12)
    axes[1].set_xlabel('Year')
    axes[1].set_ylabel('Number of Papers')
    axes[1].set_xticks([2022, 2023, 2024, 2025])
    axes[1].grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('t6t7_yearly_trend.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("저장: t6t7_yearly_trend.png")

# ── 2. 저널별 분포 ────────────────────────────────────────────
def plot_journal_distribution(df):
    top_journals = df['journal'].value_counts().head(15)

    fig, ax = plt.subplots(figsize=(13, 7))
    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(top_journals)))[::-1]
    bars = ax.barh(top_journals.index[::-1], top_journals.values[::-1], color=colors)

    for bar, val in zip(bars, top_journals.values[::-1]):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                str(val), va='center', fontsize=9)

    ax.set_title('Top 15 Journals — T6 + T7 Papers', fontweight='bold', fontsize=13)
    ax.set_xlabel('Number of Papers')
    ax.tick_params(axis='y', labelsize=9)
    plt.tight_layout()
    plt.savefig('t6t7_journals.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("저장: t6t7_journals.png")

# ── 3. 연구 갭 분석 ───────────────────────────────────────────
def analyze_gap(df):
    df['text'] = (df['title'].fillna('') + ' ' + df['abstract'].fillna('')).str.lower()

    t6 = df[df['topic_group'] == 'T6']['text']
    t7 = df[df['topic_group'] == 'T7']['text']

    vec = TfidfVectorizer(max_features=300, stop_words=STOP_WORDS, ngram_range=(1, 2), min_df=2)
    vec.fit(df['text'])

    def top_terms(corpus, n=20):
        mat = vec.transform(corpus)
        scores = mat.mean(axis=0).A1
        idx = scores.argsort()[::-1][:n]
        names = vec.get_feature_names_out()
        return [(names[i], round(scores[i], 4)) for i in idx]

    t6_terms = dict(top_terms(t6, 30))
    t7_terms = dict(top_terms(t7, 30))
    all_terms = set(t6_terms) | set(t7_terms)

    # T6에만 강한 키워드 (T7에 약한 것) → T7이 다루지 않는 T6 영역
    t6_unique = sorted([(k, t6_terms.get(k, 0) - t7_terms.get(k, 0))
                         for k in all_terms if t6_terms.get(k, 0) > 0],
                        key=lambda x: -x[1])[:10]

    # T7에만 강한 키워드
    t7_unique = sorted([(k, t7_terms.get(k, 0) - t6_terms.get(k, 0))
                         for k in all_terms if t7_terms.get(k, 0) > 0],
                        key=lambda x: -x[1])[:10]

    # 두 토픽이 공유하는 키워드 → 병합 접점
    shared = sorted([(k, min(t6_terms.get(k, 0), t7_terms.get(k, 0)))
                      for k in all_terms
                      if t6_terms.get(k, 0) > 0 and t7_terms.get(k, 0) > 0],
                     key=lambda x: -x[1])[:10]

    return t6_unique, t7_unique, shared

def plot_gap(t6_unique, t7_unique, shared):
    fig, axes = plt.subplots(1, 3, figsize=(17, 6))

    def hbar(ax, data, title, color):
        labels = [d[0] for d in data]
        values = [d[1] for d in data]
        bars = ax.barh(labels[::-1], values[::-1], color=color)
        ax.set_title(title, fontweight='bold', fontsize=11)
        ax.tick_params(labelsize=9)
        ax.set_xlabel('TF-IDF Score Difference')

    hbar(axes[0], t6_unique, 'T6 Unique Keywords\n(Self / Social AI)', '#4C9BE8')
    hbar(axes[1], t7_unique, 'T7 Unique Keywords\n(Agentic / LLM)', '#E8834C')
    hbar(axes[2], shared,    'Shared Keywords\n(Research Bridge)', '#6DBF67')

    plt.suptitle('Research Gap & Bridge Analysis — T6 vs T7', fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('t6t7_gap_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("저장: t6t7_gap_analysis.png")

# ── 4. 인사이트 텍스트 출력 ───────────────────────────────────
def print_insights(df, t6_unique, t7_unique, shared):
    print("\n" + "="*60)
    print("  T6 + T7 연구 인사이트 요약")
    print("="*60)

    total = len(df)
    t6_n = len(df[df['topic_group'] == 'T6'])
    t7_n = len(df[df['topic_group'] == 'T7'])
    yearly = df.groupby('year').size()

    print(f"\n[규모] 총 {total}편 | T6: {t6_n}편 | T7: {t7_n}편")
    print(f"[성장] {int(yearly.get(2022,0))}편(2022) → {int(yearly.get(2023,0))}편(2023) → {int(yearly.get(2024,0))}편(2024) → {int(yearly.get(2025,0))}편(2025)")

    top5 = df.nlargest(5, 'cited_by')[['title','cited_by','year']]
    print("\n[최다 피인용 5편]")
    for _, r in top5.iterrows():
        print(f"  {int(r['cited_by'])}회 ({int(r['year'])}) {r['title'][:65]}...")

    print("\n[T6 unique keywords - Social AI / Self-awareness]")
    print(" ", ", ".join([k for k, _ in t6_unique[:6]]))

    print("\n[T7 unique keywords - Agentic AI / LLM]")
    print(" ", ", ".join([k for k, _ in t7_unique[:6]]))

    print("\n[T6+T7 shared keywords - Research Bridge]")
    print(" ", ", ".join([k for k, _ in shared[:6]]))

    print("\n[Research Gap Insight]")
    print("  T6 covers social acceptance, trust, and self-awareness.")
    print("  T7 covers autonomous agents and LLM-based decision making.")
    print("  Bridging research on 'agentic AI with self-awareness and social trust'")
    print("  remains scarce -- a clear research gap exists.")
    print("="*60)

if __name__ == '__main__':
    df = load()
    print(f"T6+T7 논문 로드: {len(df)}편\n")

    plot_yearly_trend(df)
    plot_journal_distribution(df)
    t6_u, t7_u, shared = analyze_gap(df)
    plot_gap(t6_u, t7_u, shared)
    print_insights(df, t6_u, t7_u, shared)
