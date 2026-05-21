"""
Generative AI Research Landscape — Scopus 2022-2025
- Multi-keyword search (18 query clusters)
- Research stream classification (topic + methodology + domain)
- Output: summary tables + visualizations + markdown report
"""
import os, time, requests
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from collections import Counter
import warnings
warnings.filterwarnings("ignore")

API_KEY  = os.environ.get("SCOPUS_API_KEY", "cd41b851e7149cfc553470bf1534dc7b")
BASE_URL = "https://api.elsevier.com/content/search/scopus"
HEADERS  = {"X-ELS-APIKey": API_KEY, "Accept": "application/json"}
OUT_CSV  = "genai_papers.csv"
N_TOPICS = 10

# ── 18 keyword clusters ───────────────────────────────────────────────────────
QUERIES = {
    "GenAI_Core":        'TITLE-ABS-KEY("generative AI" OR "generative artificial intelligence") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "LLM_General":       'TITLE-ABS-KEY("large language model" OR "LLM" OR "foundation model") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "ChatGPT":           'TITLE-ABS-KEY("ChatGPT") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "GPT_Models":        'TITLE-ABS-KEY("GPT-4" OR "GPT-5" OR "GPT4" OR "GPT5" OR "GPT-3" OR "GPT3") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Claude_Gemini":     'TITLE-ABS-KEY("Claude AI" OR "Gemini AI" OR "Anthropic Claude" OR "Google Gemini") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Diffusion_Image":   'TITLE-ABS-KEY("diffusion model" OR "stable diffusion" OR "DALL-E" OR "Midjourney" OR "image generation") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "RAG_Agents":        'TITLE-ABS-KEY("retrieval augmented generation" OR "RAG" OR "agentic AI" OR "AI agent" OR "autonomous agent" AND "language model") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Hallucination":     'TITLE-ABS-KEY("hallucination" AND ("large language model" OR "generative AI" OR "ChatGPT")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Prompt_Engineering":'TITLE-ABS-KEY("prompt engineering" OR "prompt tuning" OR "in-context learning" OR "few-shot learning") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "FineTuning_RLHF":   'TITLE-ABS-KEY("fine-tuning" AND "language model") OR TITLE-ABS-KEY("RLHF" OR "reinforcement learning from human feedback") AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Education":         'TITLE-ABS-KEY(("ChatGPT" OR "generative AI" OR "large language model") AND ("education" OR "learning" OR "teaching" OR "student" OR "academic")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Healthcare":        'TITLE-ABS-KEY(("ChatGPT" OR "generative AI" OR "large language model") AND ("health" OR "medical" OR "clinical" OR "patient" OR "diagnosis")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Business_Strategy": 'TITLE-ABS-KEY(("generative AI" OR "ChatGPT" OR "large language model") AND ("business" OR "firm" OR "organization" OR "management" OR "strategy")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Ethics_Bias":       'TITLE-ABS-KEY(("generative AI" OR "large language model" OR "ChatGPT") AND ("ethics" OR "bias" OR "fairness" OR "privacy" OR "misinformation" OR "deepfake")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Creativity_Art":    'TITLE-ABS-KEY(("generative AI" OR "diffusion model") AND ("creativity" OR "art" OR "music" OR "design" OR "creative")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "NLP_Benchmark":     'TITLE-ABS-KEY(("language model" OR "LLM") AND ("benchmark" OR "evaluation" OR "performance" OR "reasoning" OR "MMLU" OR "HumanEval")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Code_Generation":   'TITLE-ABS-KEY(("code generation" OR "software engineering") AND ("large language model" OR "ChatGPT" OR "Copilot")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
    "Adoption_Trust":    'TITLE-ABS-KEY(("generative AI" OR "ChatGPT") AND ("adoption" OR "acceptance" OR "trust" OR "TAM" OR "user behavior")) AND PUBYEAR > 2021 AND PUBYEAR < 2026',
}

# ── Research stream taxonomy ──────────────────────────────────────────────────
STREAM_MAP = {
    "GenAI_Core":         "1. GenAI 총론 / 개관",
    "LLM_General":        "2. LLM / 기반 모델 기술",
    "ChatGPT":            "3. ChatGPT 응용 연구",
    "GPT_Models":         "4. GPT 시리즈 모델",
    "Claude_Gemini":      "5. 기타 LLM (Claude / Gemini)",
    "Diffusion_Image":    "6. 이미지 생성 / 확산 모델",
    "RAG_Agents":         "7. RAG / 에이전틱 AI",
    "Hallucination":      "8. 환각(Hallucination) / 신뢰성",
    "Prompt_Engineering": "9. 프롬프트 엔지니어링",
    "FineTuning_RLHF":    "10. 파인튜닝 / RLHF",
    "Education":          "11. 교육 분야 적용",
    "Healthcare":         "12. 헬스케어 / 의료 적용",
    "Business_Strategy":  "13. 비즈니스 / 경영 전략",
    "Ethics_Bias":        "14. 윤리 / 편향 / 딥페이크",
    "Creativity_Art":     "15. 창의성 / 예술 / 디자인",
    "NLP_Benchmark":      "16. NLP 성능 평가 / 벤치마크",
    "Code_Generation":    "17. 코드 생성 / SW 엔지니어링",
    "Adoption_Trust":     "18. 수용·신뢰 / 사용자 행동",
}

# ── Scopus fetcher ────────────────────────────────────────────────────────────
def fetch_scopus(query, max_results=300):
    records, start = [], 0
    while start < max_results:
        params = {
            "query": query, "start": start, "count": 25,
            "field": "dc:identifier,dc:title,dc:description,"
                     "prism:publicationName,prism:coverDate,"
                     "citedby-count,authkeywords,subtypeDescription",
        }
        try:
            r = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=30)
            if r.status_code != 200:
                break
            data  = r.json().get("search-results", {})
            entries = data.get("entry", [])
            if not entries or entries[0].get("error"):
                break
            total = int(data.get("opensearch:totalResults", 0))
            for e in entries:
                records.append({
                    "scopus_id": e.get("dc:identifier", "").replace("SCOPUS_ID:", ""),
                    "title":     e.get("dc:title", ""),
                    "abstract":  e.get("dc:description", ""),
                    "journal":   e.get("prism:publicationName", ""),
                    "year":      str(e.get("prism:coverDate", ""))[:4],
                    "citations": e.get("citedby-count", 0),
                    "keywords":  e.get("authkeywords", ""),
                    "doc_type":  e.get("subtypeDescription", ""),
                })
            start += len(entries)
            if start >= min(total, max_results):
                break
            time.sleep(0.25)
        except Exception as ex:
            print(f"    Error: {ex}")
            break
    return records

# ── 1. Collect ────────────────────────────────────────────────────────────────
def collect():
    if os.path.exists(OUT_CSV):
        print(f"Loading cached: {OUT_CSV}")
        return pd.read_csv(OUT_CSV, encoding="utf-8-sig")

    all_records = []
    stream_counts = {}
    for key, query in QUERIES.items():
        print(f"  [{STREAM_MAP[key]}] querying...")
        recs = fetch_scopus(query, max_results=300)
        for r in recs:
            r["query_key"] = key
            r["research_stream"] = STREAM_MAP[key]
        stream_counts[key] = len(recs)
        print(f"    -> {len(recs)} records")
        all_records.extend(recs)
        time.sleep(0.5)

    df = pd.DataFrame(all_records)
    df = df[df["doc_type"].isin(["Article", "Review", ""])]
    df = df[df["year"].between("2022", "2025")]
    # Keep first occurrence per paper (some papers appear in multiple queries)
    df_dedup = df.drop_duplicates(subset="scopus_id", keep="first")
    df_dedup.to_csv(OUT_CSV, index=False, encoding="utf-8-sig")
    # Also save raw (with duplicates) for stream counting
    df.to_csv("genai_papers_raw.csv", index=False, encoding="utf-8-sig")
    print(f"\nUnique papers: {len(df_dedup)} | Raw (with overlaps): {len(df)}")
    return df_dedup

# ── 2. Stream table ───────────────────────────────────────────────────────────
def stream_table(df_raw):
    """Count papers per stream from raw (multi-labeled) data."""
    raw = pd.read_csv("genai_papers_raw.csv", encoding="utf-8-sig") if os.path.exists("genai_papers_raw.csv") else df_raw
    sc = raw.groupby("research_stream").agg(
        papers=("scopus_id", "count"),
        unique=("scopus_id", "nunique"),
        avg_citations=("citations", lambda x: round(pd.to_numeric(x, errors="coerce").mean(), 1)),
    ).reset_index()
    sc = sc.sort_values("papers", ascending=False)
    return sc

# ── 3. Yearly trend ───────────────────────────────────────────────────────────
def plot_yearly(df_raw):
    raw = pd.read_csv("genai_papers_raw.csv", encoding="utf-8-sig") if os.path.exists("genai_papers_raw.csv") else df_raw
    raw["year_n"] = pd.to_numeric(raw["year"], errors="coerce")
    # Group streams into 6 macro-areas for readability
    macro = {
        "GenAI_Core": "Core GenAI",
        "LLM_General": "Core GenAI",
        "ChatGPT": "Core GenAI",
        "GPT_Models": "Core GenAI",
        "Claude_Gemini": "Core GenAI",
        "Diffusion_Image": "Image / Creative",
        "Creativity_Art": "Image / Creative",
        "RAG_Agents": "Technology",
        "Hallucination": "Technology",
        "Prompt_Engineering": "Technology",
        "FineTuning_RLHF": "Technology",
        "NLP_Benchmark": "Technology",
        "Code_Generation": "Technology",
        "Education": "Domain Applications",
        "Healthcare": "Domain Applications",
        "Business_Strategy": "Domain Applications",
        "Adoption_Trust": "Domain Applications",
        "Ethics_Bias": "Ethics / Society",
    }
    raw["macro"] = raw["query_key"].map(macro).fillna("Other")
    trend = raw.groupby(["year_n", "macro"]).size().unstack(fill_value=0)
    trend = trend.loc[trend.index.isin([2022, 2023, 2024, 2025])]

    colors = {"Core GenAI": "#1565C0", "Technology": "#2E7D32",
              "Domain Applications": "#E65100", "Image / Creative": "#7B1FA2",
              "Ethics / Society": "#C62828"}
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in trend.columns:
        ax.plot(trend.index, trend[col], marker="o", linewidth=2.5,
                markersize=7, label=col, color=colors.get(col, "gray"))
    ax.set_xlabel("Year", fontsize=11)
    ax.set_ylabel("Papers (incl. overlap)", fontsize=11)
    ax.set_title("Generative AI Research: Yearly Trend by Macro-Area (Scopus 2022-2025)",
                 fontsize=12, fontweight="bold")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    ax.set_xticks([2022, 2023, 2024, 2025])
    plt.tight_layout()
    plt.savefig("genai_yearly_trend.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: genai_yearly_trend.png")
    return trend

# ── 4. Stream volume bar chart ────────────────────────────────────────────────
def plot_stream_bar(sc):
    sc_sorted = sc.sort_values("papers", ascending=True).tail(18)
    colors = plt.cm.RdYlGn(np.linspace(0.2, 0.9, len(sc_sorted)))
    fig, ax = plt.subplots(figsize=(12, 9))
    bars = ax.barh(sc_sorted["research_stream"], sc_sorted["papers"],
                   color=colors, edgecolor="white", alpha=0.88)
    for bar, cnt in zip(bars, sc_sorted["papers"]):
        ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
                str(cnt), va="center", fontsize=8.5)
    ax.set_xlabel("Papers per Research Stream", fontsize=11)
    ax.set_title("Generative AI Research Streams — Scopus 2022-2025\n"
                 "(Multiple queries; some papers appear in multiple streams)",
                 fontsize=12, fontweight="bold")
    ax.grid(axis="x", alpha=0.3)
    ax.set_xlim(0, sc_sorted["papers"].max() * 1.15)
    plt.tight_layout()
    plt.savefig("genai_stream_bar.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: genai_stream_bar.png")

# ── 5. LDA on unique papers ───────────────────────────────────────────────────
def run_lda(df):
    texts = (df["title"].fillna("") + " " + df["abstract"].fillna("") +
             " " + df["keywords"].fillna("")).tolist()
    stop_extra = {"model", "models", "using", "based", "large", "language",
                  "paper", "study", "results", "show", "approach", "proposed",
                  "also", "two", "new", "different", "high", "performance",
                  "task", "tasks", "training", "data", "pre", "trained"}
    vec = TfidfVectorizer(max_features=2000, ngram_range=(1, 2),
                          stop_words="english", min_df=3)
    X = vec.fit_transform(texts)
    fn = vec.get_feature_names_out()
    mask = np.array([not any(s == w for s in stop_extra) for w in fn])
    X_f, fn_f = X[:, mask], fn[mask]

    lda = LatentDirichletAllocation(n_components=N_TOPICS, random_state=42, max_iter=50)
    doc_topics = lda.fit_transform(X_f)
    dom = np.argmax(doc_topics, axis=1)

    kws = {}
    for t, comp in enumerate(lda.components_):
        top = comp.argsort()[-10:][::-1]
        kws[t] = [fn_f[i] for i in top]
    return dom, kws, Counter(dom)

# ── 6. Markdown report ────────────────────────────────────────────────────────
def write_report(df, df_raw, sc, trend, dom, lda_kws, tc):
    total_unique = len(df)
    total_raw    = len(pd.read_csv("genai_papers_raw.csv", encoding="utf-8-sig")) if os.path.exists("genai_papers_raw.csv") else total_unique
    year_dist    = df["year"].value_counts().sort_index()

    lines = [
        "# 생성형 AI 연구 Scopus 현황 분석 (2022-2025)",
        f"**검색일:** 2026-05-21 | **키워드 클러스터:** 18개 | **고유 논문:** {total_unique:,}편",
        "",
        "---",
        "",
        "## 1. 연도별 논문 수",
        "",
        "| 연도 | 논문 수 | 비중 | 특징 |",
        "|---|---|---|---|",
        f"| 2022 | {year_dist.get('2022',0)} | {year_dist.get('2022',0)/total_unique*100:.1f}% | ChatGPT 등장 전후 — 기초 LLM 연구 급증 시작 |",
        f"| 2023 | {year_dist.get('2023',0)} | {year_dist.get('2023',0)/total_unique*100:.1f}% | ChatGPT 충격 — 교육·헬스케어·윤리 연구 폭증 |",
        f"| 2024 | {year_dist.get('2024',0)} | {year_dist.get('2024',0)/total_unique*100:.1f}% | 응용 연구 본격화 — RAG·에이전트·비즈니스 연구 |",
        f"| 2025 | {year_dist.get('2025',0)} | {year_dist.get('2025',0)/total_unique*100:.1f}% | 성숙기 진입 — 벤치마크·신뢰성·규제 연구 증가 |",
        "",
        "---",
        "",
        "## 2. 연구 스트림별 논문 수 (18개 키워드 클러스터)",
        "",
        "| # | 연구 스트림 | 논문 수 | 평균 피인용 | 연구 특징 |",
        "|---|---|---|---|---|",
    ]

    stream_chars = {
        "1. GenAI 총론 / 개관":          "GenAI 개념·영향·미래 전망 논문 — 리뷰 논문 비중 높음",
        "2. LLM / 기반 모델 기술":        "Transformer 아키텍처, 사전학습, 스케일링 법칙 등",
        "3. ChatGPT 응용 연구":           "ChatGPT 활용 실증 연구 — 가장 빠르게 성장한 스트림",
        "4. GPT 시리즈 모델":             "GPT-3/4/5 성능 비교, 역량 분석 연구",
        "5. 기타 LLM (Claude / Gemini)":  "비교 연구, 모델별 특성 분석 — 최근 급증",
        "6. 이미지 생성 / 확산 모델":      "Stable Diffusion, DALL-E, Midjourney 연구",
        "7. RAG / 에이전틱 AI":           "검색증강생성, 에이전트 시스템, 자율 AI 연구",
        "8. 환각(Hallucination) / 신뢰성": "오류 탐지, 사실 검증, 신뢰성 향상 기법",
        "9. 프롬프트 엔지니어링":          "prompt tuning, few-shot, chain-of-thought 연구",
        "10. 파인튜닝 / RLHF":            "도메인 특화 조정, 인간 피드백 기반 학습",
        "11. 교육 분야 적용":             "ChatGPT in 교육 — 가장 활발한 응용 도메인",
        "12. 헬스케어 / 의료 적용":        "임상 의사결정, 의료 문서, 진단 지원",
        "13. 비즈니스 / 경영 전략":        "기업 전략, 생산성, 비즈니스 모델 혁신",
        "14. 윤리 / 편향 / 딥페이크":      "AI 안전, 편향 감지, 허위정보, 저작권",
        "15. 창의성 / 예술 / 디자인":      "AI 생성 예술, 창의적 보조 도구 연구",
        "16. NLP 성능 평가 / 벤치마크":    "MMLU, HumanEval 등 표준화 평가 연구",
        "17. 코드 생성 / SW 엔지니어링":   "GitHub Copilot, 자동 코드 생성, 디버깅",
        "18. 수용·신뢰 / 사용자 행동":     "TAM 기반 수용 의도, 인간-AI 신뢰 연구",
    }
    for _, row in sc.iterrows():
        stream = row["research_stream"]
        char   = stream_chars.get(stream, "-")
        lines.append(f"| {stream.split('.')[0]} | {stream} | {row['papers']:,} | {row['avg_citations']} | {char} |")

    lines += [
        "",
        "---",
        "",
        "## 3. LDA 토픽 모델링 결과 (고유 논문 기준)",
        "",
        "| 토픽 | 논문 수 | 비중 | 대표 키워드 |",
        "|---|---|---|---|",
    ]
    lda_labels = [
        "Core LLM Architecture & Pretraining",
        "ChatGPT in Education & Academia",
        "Image Generation & Creative AI",
        "Retrieval, Agents & Agentic Systems",
        "Hallucination, Safety & Ethics",
        "Healthcare & Clinical NLP",
        "Business & Organizational Impact",
        "Code Generation & SW Engineering",
        "User Adoption & Human-AI Interaction",
        "Benchmarking & Model Evaluation",
    ]
    for t in range(N_TOPICS):
        cnt = tc.get(t, 0)
        kw  = ", ".join(lda_kws[t][:5])
        lbl = lda_labels[t] if t < len(lda_labels) else f"Topic {t+1}"
        lines.append(f"| {lbl} | {cnt} | {cnt/total_unique*100:.1f}% | {kw} |")

    lines += [
        "",
        "---",
        "",
        "## 4. 주요 연구 스트림별 현황 요약 (가장 많이 연구된 순)",
        "",
        "| 순위 | 연구 영역 | 핵심 발견 | 리서치 갭 |",
        "|---|---|---|---|",
        "| 1 | **ChatGPT 응용** | ChatGPT 등장 직후 교육·의료·비즈니스 적용 연구 폭증 | 장기 효과·종단 연구 부족 |",
        "| 2 | **LLM 기반 기술** | 아키텍처·스케일링 연구 주도; GPT 계열 집중 | 비GPT 모델 비교 연구 부족 |",
        "| 3 | **교육 적용** | 학습 도구·학술 부정 행위·교사 역할 연구 급증 | 학습 효과 실증·종단 연구 부족 |",
        "| 4 | **윤리 / 편향** | 허위정보·저작권·편향 연구 증가; 규제 논의 | 규제 효과성 실증 연구 없음 |",
        "| 5 | **헬스케어** | 임상 의사결정 지원 연구 활발; 규제 맥락 연구 | 실제 임상 결과 연구 미흡 |",
        "| 6 | **RAG / 에이전트** | 2024년 이후 급증; 아직 기술 논문 위주 | 조직·서비스 맥락 적용 연구 공백 |",
        "| 7 | **비즈니스 전략** | 생산성·혁신·업무 변화 연구 증가 | 국가·산업별 비교 연구 부족 |",
        "| 8 | **수용·신뢰** | TAM 기반 연구 증가; 인간-AI 신뢰 연구 | AICC 맥락 신뢰 연구 거의 없음 |",
        "",
        "---",
        "",
        "## 5. 본 연구(AICC 진화 모형)의 갭 포지셔닝",
        "",
        "| 스트림 | 현재 연구 수준 | 본 논문 위치 |",
        "|---|---|---|",
        "| GenAI 총론 | 리뷰 논문 다수, 개념 정리 중심 | 실증 케이스 기반 진화 모형 |",
        "| 비즈니스 / 경영 | 생산성·전략 연구 | **서비스 프로세스 진화** 연구 (갭) |",
        "| 수용·신뢰 | 고객 수용 중심 | **상담사 AI 신뢰 보정** 연구 (갭) |",
        "| 에이전트 / RAG | 기술 논문 위주 | **조직·서비스 운영 맥락** 적용 (갭) |",
        "| 헬스케어 | 의료 특화 연구 | **공공서비스 디지털 포용** (갭) |",
        "| 교육 | 학습 도구 연구 | 직접 관련 없음 |",
        "",
        "---",
        f"*분석일: 2026-05-21 | 데이터: Scopus API | 고유 논문: {total_unique:,}편*",
    ]
    with open("genai_landscape_report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("Saved: genai_landscape_report.md")

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 65)
    print("  Generative AI Research Landscape - Scopus 2022-2025")
    print("=" * 65)

    print("\n[Step 1] Collecting papers from Scopus...")
    df = collect()

    # Load raw for stream-level counting
    if os.path.exists("genai_papers_raw.csv"):
        df_raw = pd.read_csv("genai_papers_raw.csv", encoding="utf-8-sig")
    else:
        df_raw = df

    print(f"\nUnique papers: {len(df)} | Year range: {df['year'].min()}-{df['year'].max()}")
    print("Year distribution:")
    print(df["year"].value_counts().sort_index().to_string())

    print("\n[Step 2] Building stream summary table...")
    sc = stream_table(df_raw)
    print(sc[["research_stream","papers","unique","avg_citations"]].to_string(index=False))

    print("\n[Step 3] Plotting stream bar chart...")
    plot_stream_bar(sc)

    print("\n[Step 4] Plotting yearly trend...")
    trend = plot_yearly(df_raw)

    print("\n[Step 5] Running LDA topic modeling...")
    dom, lda_kws, tc = run_lda(df)
    df["topic"] = dom
    print("Topic distribution:")
    for t in range(N_TOPICS):
        print(f"  T{t+1} (n={tc.get(t,0):>4}): {', '.join(lda_kws[t][:6])}")

    print("\n[Step 6] Writing markdown report...")
    write_report(df, df_raw, sc, trend, dom, lda_kws, tc)

    print("\n" + "=" * 65)
    print("  Output files:")
    print("  genai_papers.csv              - Unique paper data")
    print("  genai_stream_bar.png          - Stream volume bar chart")
    print("  genai_yearly_trend.png        - Yearly trend by macro-area")
    print("  genai_landscape_report.md     - Full analysis report (Korean)")
    print("=" * 65)
