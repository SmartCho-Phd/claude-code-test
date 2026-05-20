import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation, NMF
from sklearn.cluster import KMeans
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import numpy as np
import warnings
warnings.filterwarnings('ignore')

nltk.download('stopwords', quiet=True)

INPUT_FILE = 'agentic_consciousness_papers.csv'

STOP_WORDS = list(stopwords.words('english')) + [
    'ai', 'artificial', 'intelligence', 'study', 'paper', 'research',
    'results', 'based', 'using', 'used', 'proposed', 'approach',
    'method', 'model', 'system', 'data', 'analysis', 'review',
    'new', 'also', 'however', 'thus', 'may', 'use', 'show',
    'provide', 'present', 'found', 'two', 'three', 'one',
]

N_TOPICS = 7

def load_data():
    df = pd.read_csv(INPUT_FILE, encoding='utf-8-sig')
    df['text'] = (df['title'].fillna('') + ' ' + df['abstract'].fillna('')).str.strip()
    df = df[df['text'].str.len() > 20]
    print(f"분석 대상: {len(df)}편")
    return df

def get_top_words(model, feature_names, n=10):
    topics = []
    for idx, topic in enumerate(model.components_):
        top_idx = topic.argsort()[:-n-1:-1]
        words = [feature_names[i] for i in top_idx]
        topics.append(words)
    return topics

def name_topic(words):
    mapping = {
        frozenset(['robot', 'human', 'interaction', 'social']): 'Human-Robot Interaction',
        frozenset(['agent', 'autonomous', 'task', 'decision']): 'Autonomous Agents',
        frozenset(['consciousness', 'aware', 'self', 'cognitive']): 'Machine Consciousness',
        frozenset(['ethical', 'trust', 'bias', 'fairness']): 'AI Ethics & Trust',
        frozenset(['language', 'llm', 'gpt', 'chatgpt']): 'Large Language Models',
        frozenset(['learning', 'reinforcement', 'reward', 'policy']): 'Reinforcement Learning',
        frozenset(['anthropomorph', 'perception', 'human-like', 'emotion']): 'Anthropomorphism',
    }
    word_set = set(words)
    for key, name in mapping.items():
        if len(key & word_set) >= 2:
            return name
    return f"Topic: {', '.join(words[:3])}"

def run_lda(df):
    vectorizer = TfidfVectorizer(
        max_features=1500,
        stop_words=STOP_WORDS,
        min_df=3,
        max_df=0.85,
        ngram_range=(1, 2),
    )
    X = vectorizer.fit_transform(df['text'])
    feature_names = vectorizer.get_feature_names_out()

    lda = LatentDirichletAllocation(
        n_components=N_TOPICS,
        random_state=42,
        max_iter=30,
    )
    lda.fit(X)

    topics = get_top_words(lda, feature_names)
    topic_dist = lda.transform(X)
    df['topic'] = topic_dist.argmax(axis=1)

    return lda, topics, feature_names, X, df

def plot_topic_keywords(topics, filename='topic_keywords.png'):
    fig, axes = plt.subplots(2, 4, figsize=(18, 8))
    axes = axes.flatten()
    colors = plt.cm.Set2(np.linspace(0, 1, N_TOPICS))

    for i, words in enumerate(topics):
        ax = axes[i]
        scores = np.arange(len(words), 0, -1)
        bars = ax.barh(words[::-1], scores[::-1], color=colors[i])
        ax.set_title(f'Topic {i+1}', fontsize=11, fontweight='bold')
        ax.set_xlabel('Relevance')
        ax.tick_params(labelsize=9)

    axes[-1].axis('off')
    plt.suptitle('LDA Topic Modeling — Top Keywords per Topic', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"저장: {filename}")

def plot_topic_distribution(df, topics, filename='topic_distribution.png'):
    counts = df['topic'].value_counts().sort_index()
    labels = [f"T{i+1}: {', '.join(topics[i][:2])}" for i in range(N_TOPICS)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    colors = plt.cm.Set2(np.linspace(0, 1, N_TOPICS))
    bars = ax1.bar(range(N_TOPICS), [counts.get(i, 0) for i in range(N_TOPICS)], color=colors)
    ax1.set_xticks(range(N_TOPICS))
    ax1.set_xticklabels([f'T{i+1}' for i in range(N_TOPICS)])
    ax1.set_title('Number of Papers per Topic', fontweight='bold')
    ax1.set_ylabel('Paper Count')
    for bar, count in zip(bars, [counts.get(i, 0) for i in range(N_TOPICS)]):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 str(count), ha='center', va='bottom', fontsize=10)

    wedges, texts, autotexts = ax2.pie(
        [counts.get(i, 0) for i in range(N_TOPICS)],
        labels=[f'T{i+1}' for i in range(N_TOPICS)],
        autopct='%1.1f%%', colors=colors, startangle=140
    )
    ax2.set_title('Topic Share', fontweight='bold')

    fig.text(0.5, -0.05, '\n'.join([f'T{i+1}: {labels[i]}' for i in range(N_TOPICS)]),
             ha='center', fontsize=9, style='italic')

    plt.suptitle('Topic Distribution across 1,081 Papers', fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"저장: {filename}")

def plot_yearly_trend(df, topics, filename='yearly_trend.png'):
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df_year = df.dropna(subset=['year'])
    df_year['year'] = df_year['year'].astype(int)

    pivot = df_year.groupby(['year', 'topic']).size().unstack(fill_value=0)
    pivot = pivot.reindex(columns=range(N_TOPICS), fill_value=0)

    fig, ax = plt.subplots(figsize=(12, 6))
    colors = plt.cm.Set2(np.linspace(0, 1, N_TOPICS))
    for i in range(N_TOPICS):
        if i in pivot.columns:
            ax.plot(pivot.index, pivot[i], marker='o', label=f'T{i+1}: {", ".join(topics[i][:2])}',
                    color=colors[i], linewidth=2)

    ax.set_title('Yearly Topic Trend (2022–2025)', fontsize=13, fontweight='bold')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Papers')
    ax.legend(loc='upper left', fontsize=8, bbox_to_anchor=(1, 1))
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"저장: {filename}")

def plot_wordcloud(df, filename='wordcloud.png'):
    all_text = ' '.join(df['text'].tolist())
    wc = WordCloud(
        width=1200, height=600,
        background_color='white',
        stopwords=set(STOP_WORDS),
        max_words=150,
        colormap='tab10',
    ).generate(all_text)

    plt.figure(figsize=(14, 7))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud — All 1,081 Papers', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"저장: {filename}")

def save_topic_summary(df, topics, filename='topic_summary.csv'):
    df['topic_label'] = df['topic'].apply(lambda i: f"T{i+1}: {', '.join(topics[i][:5])}")
    summary = df[['title', 'authors', 'journal', 'year', 'cited_by', 'doi', 'topic_label']]
    summary = summary.sort_values(['topic_label', 'cited_by'], ascending=[True, False])
    summary.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"저장: {filename}")

if __name__ == '__main__':
    print("=== 논문 토픽 분석 시작 ===\n")

    df = load_data()
    plot_wordcloud(df)

    print("\n[LDA 토픽 모델링 실행 중...]")
    lda, topics, feature_names, X, df = run_lda(df)

    print("\n=== 발견된 토픽 ===")
    for i, words in enumerate(topics):
        print(f"  Topic {i+1}: {', '.join(words)}")

    plot_topic_keywords(topics)
    plot_topic_distribution(df, topics)
    plot_yearly_trend(df, topics)
    save_topic_summary(df, topics)

    print("\n=== 분석 완료 ===")
    print("생성된 파일:")
    print("  - wordcloud.png         : 전체 키워드 워드클라우드")
    print("  - topic_keywords.png    : 토픽별 핵심 키워드")
    print("  - topic_distribution.png: 토픽 분포")
    print("  - yearly_trend.png      : 연도별 토픽 트렌드")
    print("  - topic_summary.csv     : 토픽 라벨이 붙은 논문 목록")
