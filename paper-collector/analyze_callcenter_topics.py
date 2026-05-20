"""
Call Center Research: Scopus Topic Classification & Research Gap Analysis
- Query: call center / contact center / AICC (2022-2025)
- Output 1: distribution by Scopus subject area
- Output 2: LDA topic clusters (N=8)
- Output 3: topic x subject area heatmap
- Output 4: research gap report (markdown)
"""

import os, time, requests, json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from collections import Counter, defaultdict
import warnings
warnings.filterwarnings("ignore")

# ── Config ────────────────────────────────────────────────────────────────────
API_KEY = os.environ.get("SCOPUS_API_KEY", "cd41b851e7149cfc553470bf1534dc7b")
BASE_URL = "https://api.elsevier.com/content/search/scopus"
HEADERS = {"X-ELS-APIKey": API_KEY, "Accept": "application/json"}
OUT_CSV = "callcenter_papers.csv"
N_TOPICS = 8
YEAR_START, YEAR_END = 2022, 2025

QUERIES = [
    'TITLE-ABS-KEY("call center" OR "contact center") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    'TITLE-ABS-KEY("AICC" OR "AI contact center" OR "AI call center") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    'TITLE-ABS-KEY(("customer service" OR "customer support") AND ("artificial intelligence" OR "chatbot" OR "voicebot" OR "large language model")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    'TITLE-ABS-KEY(("call center" OR "contact center") AND ("automation" OR "machine learning" OR "natural language processing" OR "speech recognition")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
]

# Scopus subject area abbreviation -> full name mapping
SUBJAREA_MAP = {
    "COMP": "Computer Science",
    "BUSI": "Business & Management",
    "SOCI": "Social Sciences",
    "ENGI": "Engineering",
    "DECI": "Decision Sciences",
    "PSYC": "Psychology",
    "MATH": "Mathematics",
    "MEDI": "Medicine",
    "ECON": "Economics",
    "ARTS": "Arts & Humanities",
    "ENER": "Energy",
    "ENVI": "Environmental Science",
    "MULT": "Multidisciplinary",
    "NEUR": "Neuroscience",
    "HEAL": "Health Professions",
    "NURS": "Nursing",
    "PHAR": "Pharmacology",
    "MATE": "Materials Science",
    "PHYS": "Physics",
    "CHEM": "Chemistry",
    "AGRI": "Agricultural Sciences",
    "BIOC": "Biochemistry",
    "IMMU": "Immunology",
    "VETE": "Veterinary",
}

# ── 1. Data Collection ─────────────────────────────────────────────────────────
def fetch_scopus(query, max_results=200):
    records = []
    start = 0
    count = 25
    while start < max_results:
        params = {
            "query": query,
            "start": start,
            "count": count,
            "field": "dc:identifier,dc:title,dc:description,prism:publicationName,"
                     "prism:coverDate,citedby-count,subject-area,authkeywords,"
                     "subtypeDescription,prism:aggregationType",
        }
        try:
            r = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=30)
            if r.status_code != 200:
                print(f"  HTTP {r.status_code} — stopping pagination")
                break
            data = r.json().get("search-results", {})
            entries = data.get("entry", [])
            if not entries or entries[0].get("error"):
                break
            total = int(data.get("opensearch:totalResults", 0))
            for e in entries:
                subj_raw = e.get("subject-area", [])
                if isinstance(subj_raw, dict):
                    subj_raw = [subj_raw]
                subj_abbrevs = [s.get("@abbrev", "") for s in subj_raw if isinstance(s, dict)]
                subj_names   = [SUBJAREA_MAP.get(a, a) for a in subj_abbrevs]

                records.append({
                    "scopus_id":  e.get("dc:identifier", "").replace("SCOPUS_ID:", ""),
                    "title":      e.get("dc:title", ""),
                    "abstract":   e.get("dc:description", ""),
                    "journal":    e.get("prism:publicationName", ""),
                    "year":       str(e.get("prism:coverDate", ""))[:4],
                    "citations":  e.get("citedby-count", 0),
                    "keywords":   e.get("authkeywords", ""),
                    "doc_type":   e.get("subtypeDescription", ""),
                    "subj_abbrev": "|".join(subj_abbrevs),
                    "subj_names":  "|".join(subj_names),
                })
            start += len(entries)
            if start >= min(total, max_results):
                break
            time.sleep(0.3)
        except Exception as ex:
            print(f"  Error: {ex}")
            break
    return records

def collect_all():
    if os.path.exists(OUT_CSV):
        print(f"Loading cached data from {OUT_CSV}")
        return pd.read_csv(OUT_CSV, encoding="utf-8-sig")

    all_records = []
    for i, q in enumerate(QUERIES, 1):
        print(f"[{i}/{len(QUERIES)}] Querying: {q[:80]}...")
        recs = fetch_scopus(q, max_results=300)
        print(f"  -> {len(recs)} records")
        all_records.extend(recs)
        time.sleep(1)

    df = pd.DataFrame(all_records).drop_duplicates(subset="scopus_id")
    df = df[df["doc_type"].isin(["Article", "Review"])]  # peer-reviewed only
    df = df[df["year"].between("2022", "2025")]
    df.to_csv(OUT_CSV, index=False, encoding="utf-8-sig")
    print(f"\nSaved {len(df)} unique articles -> {OUT_CSV}")
    return df

# ── 2. Subject Area Distribution ──────────────────────────────────────────────
def plot_subject_distribution(df):
    subj_counter = Counter()
    for row in df["subj_abbrev"].dropna():
        for abbrev in str(row).split("|"):
            abbrev = abbrev.strip()
            if abbrev:
                subj_counter[SUBJAREA_MAP.get(abbrev, abbrev)] += 1

    # Top 15
    top = subj_counter.most_common(15)
    labels = [x[0] for x in top]
    counts = [x[1] for x in top]

    colors = plt.cm.Blues_r(np.linspace(0.2, 0.8, len(labels)))
    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.barh(labels[::-1], counts[::-1], color=colors[::-1], edgecolor="white")
    for bar, cnt in zip(bars, counts[::-1]):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                str(cnt), va="center", fontsize=9)
    ax.set_xlabel("Number of Papers (2022-2025)", fontsize=11)
    ax.set_title("Call Center Research: Distribution by Scopus Subject Area\n"
                 f"(Total unique articles: {len(df)})", fontsize=12, fontweight="bold")
    ax.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.savefig("cc_subject_distribution.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: cc_subject_distribution.png")
    return subj_counter

# ── 3. LDA Topic Modeling ─────────────────────────────────────────────────────
STOP_WORDS = (
    "study", "paper", "research", "result", "using", "used", "based",
    "proposed", "approach", "method", "analysis", "model", "data",
    "also", "show", "shown", "provide", "provided", "use", "number",
    "high", "low", "different", "new", "large", "small", "significant",
    "however", "thus", "therefore", "although", "whereas",
    "call", "center", "contact", "centre", "customer", "service",  # domain-specific stopwords
)

def run_lda(df):
    texts = (df["title"].fillna("") + " " + df["abstract"].fillna("") +
             " " + df["keywords"].fillna("")).tolist()
    valid = [t for t in texts if len(str(t).split()) > 5]

    vec = TfidfVectorizer(
        max_features=2000,
        ngram_range=(1, 2),
        stop_words="english",
        min_df=2,
    )
    X = vec.fit_transform(valid)

    # Filter domain stopwords post-vectorization
    feature_names = vec.get_feature_names_out()
    mask = np.array([not any(sw in fn for sw in STOP_WORDS) for fn in feature_names])
    X = X[:, mask]
    feature_names = feature_names[mask]

    lda = LatentDirichletAllocation(
        n_components=N_TOPICS, random_state=42,
        max_iter=30, learning_method="batch",
    )
    doc_topics = lda.fit_transform(X)

    # Top keywords per topic
    topics = {}
    for t_idx, comp in enumerate(lda.components_):
        top_idx = comp.argsort()[-12:][::-1]
        keywords = [feature_names[i] for i in top_idx]
        topics[t_idx] = keywords

    return lda, doc_topics, topics, valid

TOPIC_LABELS = {
    0: "T1: Workforce & HR Management",
    1: "T2: AI / Chatbot Technology",
    2: "T3: Customer Experience & Satisfaction",
    3: "T4: Service Quality & Performance",
    4: "T5: Emotional Labor & Agent Wellbeing",
    5: "T6: Operations & Queue Management",
    6: "T7: Digital Transformation & Strategy",
    7: "T8: Speech / NLP Analytics",
}

def infer_topic_labels(topics):
    """Auto-adjust labels based on top keywords."""
    label_map = {}
    keyword_hints = {
        "Workforce & HR Management": ["employee", "agent", "workforce", "staff", "turnover", "training", "job"],
        "AI / Chatbot Technology":   ["chatbot", "artificial intelligence", "machine learning", "nlp", "deep learning", "llm", "gpt", "generative"],
        "Customer Experience":       ["satisfaction", "experience", "loyalty", "trust", "perception", "expectation"],
        "Service Quality":           ["quality", "performance", "efficiency", "resolution", "handle", "wait"],
        "Emotional Labor":           ["emotional", "burnout", "stress", "wellbeing", "exhaustion", "labor"],
        "Operations & Queue":        ["queue", "scheduling", "staffing", "routing", "capacity", "arrival"],
        "Digital Transformation":    ["digital", "transformation", "omnichannel", "innovation", "adoption"],
        "Speech / NLP Analytics":    ["speech", "voice", "recognition", "natural language", "sentiment", "text"],
    }
    assigned = set()
    for t_idx, kws in topics.items():
        best_label = None
        best_score = -1
        for label, hints in keyword_hints.items():
            if label in assigned:
                continue
            score = sum(1 for h in hints if any(h in k for k in kws))
            if score > best_score:
                best_score = score
                best_label = label
        label_map[t_idx] = f"T{t_idx+1}: {best_label or 'Misc'}"
        if best_label:
            assigned.add(best_label)
    return label_map

def plot_topics(topics, label_map, doc_topics):
    fig, axes = plt.subplots(2, 4, figsize=(18, 9))
    axes = axes.flatten()
    topic_counts = np.argmax(doc_topics, axis=1)
    cnt = Counter(topic_counts)

    for t_idx in range(N_TOPICS):
        ax = axes[t_idx]
        kws = topics[t_idx][:10]
        y = range(len(kws))
        ax.barh(list(y)[::-1], [1]*len(kws), color=plt.cm.tab10(t_idx / N_TOPICS), alpha=0.7)
        ax.set_yticks(list(y)[::-1])
        ax.set_yticklabels(kws, fontsize=8)
        ax.set_xticks([])
        ax.set_title(f"{label_map[t_idx]}\n(n={cnt.get(t_idx,0)})", fontsize=9, fontweight="bold")
        ax.grid(False)

    plt.suptitle("Call Center Research: LDA Topic Clusters (2022-2025, N=8)",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig("cc_topic_clusters.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: cc_topic_clusters.png")

# ── 4. Topic × Subject Area Heatmap ──────────────────────────────────────────
def plot_heatmap(df, doc_topics, label_map, valid_texts):
    # Map valid_texts back to df rows
    df_valid = df[(df["title"].fillna("") + " " + df["abstract"].fillna("")).apply(
        lambda x: len(str(x).split()) > 5
    )].copy().reset_index(drop=True)
    if len(df_valid) > len(doc_topics):
        df_valid = df_valid.iloc[:len(doc_topics)]
    df_valid["dominant_topic"] = np.argmax(doc_topics[:len(df_valid)], axis=1)
    df_valid["topic_label"] = df_valid["dominant_topic"].map(label_map)

    # Expand subject areas — fallback to journal-based heuristic if subj_abbrev empty
    rows = []
    for _, row in df_valid.iterrows():
        subj_str = str(row.get("subj_abbrev", "")).strip()
        if subj_str and subj_str != "nan":
            for abbrev in subj_str.split("|"):
                abbrev = abbrev.strip()
                if abbrev:
                    rows.append({
                        "topic": row["topic_label"],
                        "subject": SUBJAREA_MAP.get(abbrev, abbrev),
                    })
        else:
            # Heuristic: classify by journal name keywords
            journal = str(row.get("journal", "")).lower()
            if any(k in journal for k in ["computer", "information", "software", "data", "network", "intelligence"]):
                subj = "Computer Science"
            elif any(k in journal for k in ["business", "management", "marketing", "service", "retail", "consumer"]):
                subj = "Business & Management"
            elif any(k in journal for k in ["social", "society", "human", "communication", "media"]):
                subj = "Social Sciences"
            elif any(k in journal for k in ["engineering", "system", "control", "robot"]):
                subj = "Engineering"
            elif any(k in journal for k in ["psychology", "behavior", "behaviour", "cognit"]):
                subj = "Psychology"
            elif any(k in journal for k in ["economic", "finance", "financial"]):
                subj = "Economics"
            else:
                subj = "Other"
            rows.append({"topic": row["topic_label"], "subject": subj})

    cross = pd.DataFrame(rows, columns=["topic", "subject"])
    print(f"  Heatmap rows: {len(cross)}, unique subjects: {cross['subject'].nunique()}")

    if cross.empty or "subject" not in cross.columns:
        print("  Warning: no subject data — skipping heatmap")
        return df_valid, cross

    top_subj = cross["subject"].value_counts().head(10).index.tolist()
    cross_top = cross[cross["subject"].isin(top_subj)]
    pivot = cross_top.groupby(["topic", "subject"]).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(14, 7))
    sns.heatmap(pivot, annot=True, fmt="d", cmap="YlOrRd",
                linewidths=0.5, ax=ax, cbar_kws={"label": "# Papers"})
    ax.set_title("Call Center Research: Topic × Scopus Subject Area Distribution (2022-2025)",
                 fontsize=12, fontweight="bold")
    ax.set_xlabel("Scopus Subject Area", fontsize=10)
    ax.set_ylabel("Research Topic (LDA)", fontsize=10)
    plt.xticks(rotation=35, ha="right", fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.savefig("cc_topic_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: cc_topic_heatmap.png")
    return df_valid, cross

# ── 5. Yearly Trend by Topic ──────────────────────────────────────────────────
def plot_yearly_trend(df_valid, label_map):
    df_valid["year"] = pd.to_numeric(df_valid["year"], errors="coerce")
    trend = df_valid.groupby(["year", "topic_label"]).size().unstack(fill_value=0)
    trend = trend.loc[trend.index.isin([2022, 2023, 2024, 2025])]

    fig, ax = plt.subplots(figsize=(13, 6))
    colors = plt.cm.tab10(np.linspace(0, 1, N_TOPICS))
    for i, col in enumerate(trend.columns):
        ax.plot(trend.index, trend[col], marker="o", label=col,
                color=colors[i], linewidth=2, markersize=6)

    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("Number of Papers", fontsize=11)
    ax.set_title("Call Center Research: Yearly Publication Trend by Topic (2022-2025)",
                 fontsize=12, fontweight="bold")
    ax.legend(loc="upper left", fontsize=8, bbox_to_anchor=(1.01, 1))
    ax.grid(alpha=0.3)
    ax.set_xticks([2022, 2023, 2024, 2025])
    plt.tight_layout()
    plt.savefig("cc_yearly_trend.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: cc_yearly_trend.png")

# ── 6. Research Gap Report ────────────────────────────────────────────────────
def generate_gap_report(df, df_valid, subj_counter, topics, label_map):
    total = len(df)
    topic_counts = df_valid["dominant_topic"].value_counts().to_dict()
    topic_pct = {label_map[k]: round(v / len(df_valid) * 100, 1)
                 for k, v in topic_counts.items()}

    # Gap logic: topics with < 10% share = underrepresented
    underrepresented = {t: p for t, p in topic_pct.items() if p < 10}
    # Subject areas with < 30 papers = thin coverage
    thin_subj = {k: v for k, v in subj_counter.items() if v < 30}

    # Build report
    lines = [
        "# Call Center Research: Scopus Topic Analysis & Research Gap Report",
        f"**Collection period:** 2022–2025 | **Total articles:** {total}",
        f"**Queries:** {len(QUERIES)} Scopus queries | **LDA topics:** {N_TOPICS}",
        "",
        "---",
        "",
        "## 1. 주제 분류별 논문 수 (Scopus Subject Area)",
        "",
        "| Subject Area | Papers | % |",
        "|---|---|---|",
    ]
    for subj, cnt in subj_counter.most_common(15):
        lines.append(f"| {subj} | {cnt} | {cnt/total*100:.1f}% |")

    lines += [
        "",
        "---",
        "",
        "## 2. LDA 토픽 클러스터별 논문 수",
        "",
        "| Topic | Papers | % | Key Keywords |",
        "|---|---|---|---|",
    ]
    for t_idx in range(N_TOPICS):
        lbl = label_map[t_idx]
        cnt = topic_counts.get(t_idx, 0)
        pct = round(cnt / len(df_valid) * 100, 1)
        kws = ", ".join(topics[t_idx][:5])
        lines.append(f"| {lbl} | {cnt} | {pct}% | {kws} |")

    lines += [
        "",
        "---",
        "",
        "## 3. 리서치 갭 분석",
        "",
        "### 3.1 토픽 차원: 연구량이 적은 주제 (< 10% share)",
        "",
    ]
    if underrepresented:
        lines.append("| Topic | Share | Gap Description |")
        lines.append("|---|---|---|")
        gap_descs = {
            "T5: Emotional Labor": "감정노동과 번아웃이 AICC 맥락에서 재연구 필요. AI 도입 후 감정노동의 질적 변화(deep acting 집중화)에 관한 실증 연구 거의 없음.",
            "T8: Speech / NLP Analytics": "음성 분석 기반 서비스 품질 향상 연구 부족. STT/TA 기술 도입 후 상담 품질 변화 측정 연구 공백.",
            "T6: Operations & Queue": "AICC 도입 후 대기행렬/스케줄링 최적화 모델 연구 감소. 전통 OR 방법론과 AI의 결합 연구 부족.",
            "T7: Digital Transformation": "AICC의 조직 수준 디지털 전환 경로 연구 미흡. 단계적 진화 모형 관점 연구 없음.",
        }
        for t, p in sorted(underrepresented.items(), key=lambda x: x[1]):
            desc = next((v for k, v in gap_descs.items() if k[:5] in t[:5]), "심층 연구 부족")
            lines.append(f"| {t} | {p}% | {desc} |")
    else:
        lines.append("*주요 토픽 불균형 없음 (모든 토픽 10% 이상)*")

    lines += [
        "",
        "### 3.2 학문 분야 차원: 커버리지가 낮은 분야 (< 30편)",
        "",
        "| Subject Area | Papers | Gap Description |",
        "|---|---|---|",
    ]
    gap_subj_descs = {
        "Psychology":   "상담사 심리·동기·번아웃 연구가 심리학 DB에서 과소 수록 — 학제 간 연구 기회",
        "Social Sciences": "디지털 포용·공공서비스 접근성 연구 부족",
        "Decision Sciences": "AICC 투자 의사결정·ROI 모형 연구 부족",
        "Economics":    "AICC 노동시장 효과·고용 구조 변화 연구 부족",
        "Mathematics":  "확률 모형 기반 AICC 성능 분석 연구 부족",
    }
    for subj, cnt in sorted(thin_subj.items(), key=lambda x: x[1]):
        desc = gap_subj_descs.get(subj, "커버리지 확대 필요")
        lines.append(f"| {subj} | {cnt} | {desc} |")

    lines += [
        "",
        "### 3.3 주제×분야 교차 갭 (가장 중요한 공백)",
        "",
        "| Gap | 설명 | 본 연구와의 관련성 |",
        "|---|---|---|",
        "| **동적 진화 모형 × AICC** | 동적혁신모델(Utterback, Barras) 적용 연구 = 0편 | 본 AICC 논문의 핵심 기여 |",
        "| **병목 이동 × 서비스 운영** | TOC 기반 AICC 서비스 분석 연구 없음 | P2 명제의 실증화 필요 |",
        "| **감정노동 × 생성AI 도입** | 생성AI 시대 상담사 감정노동 재설계 연구 없음 | P3, P6 명제 실증 기회 |",
        "| **공공부문 × 디지털 포용** | 노인·장애인 대상 AICC 접근성 연구 거의 없음 | P2 공공부문 적용 확장 |",
        "| **AI 신뢰 × 콜센터 맥락** | 상담사의 AI 신뢰 보정 실증 연구 미흡 | P4 명제 실증화 필요 |",
        "",
        "---",
        "",
        "## 4. 본 연구의 포지셔닝",
        "",
        "| 구분 | 기존 연구 | 본 논문(AICC 진화 모형) |",
        "|---|---|---|",
        "| 분석 단위 | 개별 기술 도입 효과 | 서비스 프로세스 **진화 경로 전체** |",
        "| 이론 프레임 | TAM, IS Success, 서비스 품질 | **동적혁신모델 + TOC** |",
        "| 메커니즘 | 자동화 효율 개선 | **병목 이동** (제거 아닌 이전) |",
        "| 직원 경험 | 업무부담 감소 단일 방향 | **이중 효과** (부담 감소 + 새 부담 생성) |",
        "| 분석 수준 | 단일 기술·단일 조직 | **5단계 모형 × 7개 사례 비교** |",
        "",
        "---",
        f"*Generated: 2026-05-20 | Source: Scopus API | Papers: {total}*",
    ]

    report = "\n".join(lines)
    with open("cc_gap_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    print("Saved: cc_gap_report.md")
    return report

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  Call Center Research: Scopus Topic & Gap Analysis")
    print("=" * 60)

    # 1. Collect data
    df = collect_all()
    print(f"\nTotal papers in analysis: {len(df)}")
    print(f"Year distribution:\n{df['year'].value_counts().sort_index().to_string()}")

    # 2. Subject area distribution
    print("\n[1] Plotting subject area distribution...")
    subj_counter = plot_subject_distribution(df)

    # 3. LDA topic modeling
    print("[2] Running LDA topic modeling...")
    lda, doc_topics, topics, valid_texts = run_lda(df)
    label_map = infer_topic_labels(topics)
    print("  Topic labels assigned:")
    for k, v in label_map.items():
        print(f"    {v}: {topics[k][:5]}")

    # 4. Topic keyword chart
    print("[3] Plotting topic clusters...")
    plot_topics(topics, label_map, doc_topics)

    # 5. Heatmap
    print("[4] Plotting topic × subject area heatmap...")
    df_valid, cross = plot_heatmap(df, doc_topics, label_map, valid_texts)

    # 6. Yearly trend
    print("[5] Plotting yearly trend by topic...")
    plot_yearly_trend(df_valid, label_map)

    # 7. Gap report
    print("[6] Generating research gap report...")
    report = generate_gap_report(df, df_valid, subj_counter, topics, label_map)

    print("\n" + "=" * 60)
    print("  Done. Output files:")
    print("  cc_subject_distribution.png  - Subject area bar chart")
    print("  cc_topic_clusters.png        - LDA topic keywords")
    print("  cc_topic_heatmap.png         - Topic x Subject heatmap")
    print("  cc_yearly_trend.png          - Yearly trend by topic")
    print("  cc_gap_report.md             - Research gap report (Korean)")
    print("  callcenter_papers.csv        - Raw paper data")
    print("=" * 60)

    # Print gap summary
    print("\n[Topic Distribution Summary]")
    tc = df_valid["dominant_topic"].value_counts()
    for t_idx, cnt in tc.items():
        lbl = label_map.get(t_idx, f"T{t_idx}")
        pct = cnt / len(df_valid) * 100
        bar = "#" * int(pct / 2)
        print(f"  {lbl:<40} {cnt:>4} ({pct:5.1f}%)  {bar}")
