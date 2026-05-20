"""
2차 데이터: 공개 벤치마크 점수 데이터셋
출처: BenchLM.ai, LMSYS Chatbot Arena, GAIA Leaderboard, 공개 논문
수집 기준: ChatGPT(GPT-4o/GPT-5), Claude(Opus 4.6), Gemini(3.1 Pro) 최신 버전 기준
"""

import pandas as pd

# ── 1. 인간 유사성 (Human-Likeness) 관련 벤치마크 ─────────────────────
# 대화 자연성, 감정 인식, 다중 턴 일관성, 지식 정확성, 지시 따르기
human_likeness = {
    "Benchmark": [
        "Chatbot Arena ELO",       # 인간이 직접 투표한 선호도
        "MT-Bench",                 # 다회차 대화 자연성·일관성 (10점 만점)
        "SimpleQA",                 # 사실 정확성 (지식 유사성)
        "LongBench v2",             # 장문 맥락 이해·일관성
        "MMLU-Pro",                 # 광범위 지식 (인간 전문가 수준)
        "HLE",                      # Human-Level Exam (인간 시험 수준)
        "Knowledge Score",          # 종합 지식 점수 (BenchLM 집계)
    ],
    "Category": [
        "Human Preference",
        "Conversational Quality",
        "Factual Accuracy",
        "Context Consistency",
        "Expert Knowledge",
        "Human-Level Exam",
        "Composite Knowledge",
    ],
    "ChatGPT_GPT5": [1390, 9.0, 97.0, 95.0, 93.0, 48.0, 99.0],
    "Claude_Opus46": [1420, 8.9, 72.0, 92.0, 82.0, 53.0, 91.7],
    "Gemini_31Pro": [1410, 8.7, 95.0, 93.0, 92.0, 40.0, 94.6],
    "Max_Score":    [1500, 10,  100,   100,   100,  100,  100],
    "Source": [
        "LMSYS Chatbot Arena (2025)",
        "LMSYS MT-Bench (2024)",
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
    ]
}

# ── 2. 에이전틱 AI 속성 (Agentic AI Attributes) 관련 벤치마크 ──────────
# 자율 과업, 도구 사용, 코딩(자율 문제해결), 추론, 계획
agentic = {
    "Benchmark": [
        "Agentic Score",            # 에이전틱 종합 점수 (BenchLM 집계)
        "SWE-bench Verified",       # 실제 소프트웨어 버그 자율 수정
        "Terminal-Bench 2.0",       # 터미널 자율 조작 능력
        "LiveCodeBench",            # 실시간 코딩 과업 자율 수행
        "GPQA",                     # 전문가급 질의 자율 추론
        "Reasoning Score",          # 복합 추론 종합 (BenchLM 집계)
        "Coding Score",             # 코딩 자율 수행 종합 (BenchLM 집계)
    ],
    "Category": [
        "Composite Agentic",
        "Autonomous Bug Fix",
        "Terminal Autonomy",
        "Real-time Code Generation",
        "Expert Reasoning",
        "Composite Reasoning",
        "Composite Coding",
    ],
    "ChatGPT_GPT5": [87.9, 84.0, 75.1, 84.0, 92.8, 95.6, 89.3],
    "Claude_Opus46": [85.1, 80.84, 65.4, 76.0, 91.3, 87.8, 86.9],
    "Gemini_31Pro": [86.6, 75.0, 77.0, 71.0, 97.0, 96.7, 95.0],
    "Max_Score":    [100,  100,   100,  100,  100,  100,  100],
    "Source": [
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
        "BenchLM.ai (2025)",
    ]
}

# ── 3. Chatbot Arena ELO 연도별 추이 ─────────────────────────────────
elo_trend = {
    "Date": ["2023-12", "2024-02", "2024-04", "2024-06", "2024-09", "2025-03", "2025-07"],
    "ChatGPT": [1100, 1200, 1250, 1280, 1300, 1350, 1390],
    "Claude":  [None, None, 1190, 1220, 1250, 1350, 1420],
    "Gemini":  [None, None, 1080, 1150, 1200, 1300, 1410],
}

df_human = pd.DataFrame(human_likeness)
df_agentic = pd.DataFrame(agentic)
df_elo = pd.DataFrame(elo_trend)

df_human.to_csv("benchmark_human_likeness.csv", index=False, encoding="utf-8-sig")
df_agentic.to_csv("benchmark_agentic.csv", index=False, encoding="utf-8-sig")
df_elo.to_csv("benchmark_elo_trend.csv", index=False, encoding="utf-8-sig")

print("Dataset saved:")
print(f"  benchmark_human_likeness.csv: {len(df_human)} metrics")
print(f"  benchmark_agentic.csv:        {len(df_agentic)} metrics")
print(f"  benchmark_elo_trend.csv:      {len(df_elo)} timepoints")
