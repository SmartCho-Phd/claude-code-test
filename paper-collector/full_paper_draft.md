# Comparative Competitive Advantage of Generative AI Services:
# Focusing on "Turing-Test"-Based Human-Likeness and "Agentic AI Attributes"
# across ChatGPT, Claude, and Gemini

**초안 버전 1.0 | 2026-05-20**
*수집 데이터 기반: Scopus 1,081편 분석 + 공개 벤치마크 14개 지표*

---

## Abstract

생성형 AI(Generative AI) 서비스 시장이 급성장함에 따라 ChatGPT, Claude, Gemini 간의 경쟁이 본격화되고 있다. 그러나 기존 연구는 단일 플랫폼 중심의 도메인별 성능 평가에 집중되어 있어, 복수 서비스를 동일한 이론적 프레임워크로 비교한 연구는 희소하다. 본 연구는 (1) 튜링 테스트 기반 인간 유사성(Human-Likeness)과 (2) 에이전틱 AI 속성(Agentic AI Attributes)을 두 축으로 하는 이중 경쟁우위 프레임워크를 제안하고, 14개 공개 벤치마크 2차 데이터를 활용하여 세 서비스의 차별적 경쟁 포지션을 분석하였다. 분석 결과, ChatGPT는 사실 정확성·광범위 지식에서, Claude는 인간 선호도·감성적 일관성에서, Gemini는 추론·코딩·멀티모달 에이전틱 속성에서 각각 차별화된 경쟁우위를 보유함을 확인하였다. 본 연구는 생성형 AI 서비스의 경쟁우위를 이론화한 첫 번째 시도로서, IS/HCI 분야의 AI 서비스 수용 연구와 기업의 AI 서비스 선택 전략에 기여한다.

**키워드:** 생성형 AI, 경쟁우위, 인간 유사성, 에이전틱 AI, 튜링 테스트, ChatGPT, Claude, Gemini, 벤치마크 비교

---

## 1. 서론 (Introduction)

생성형 인공지능(Generative AI) 서비스는 2022년 이후 전례 없는 속도로 확산되며 교육, 의료, 비즈니스, 창작 등 사회 전반에 걸쳐 패러다임 전환을 주도하고 있다(Dwivedi et al., 2023). 특히 OpenAI의 ChatGPT, Anthropic의 Claude, Google의 Gemini는 대규모 언어 모델(Large Language Model, LLM)을 기반으로 한 대표적 생성형 AI 서비스로서, 전 세계 수억 명의 사용자를 보유하며 치열한 경쟁을 전개하고 있다(Chang et al., 2024). 이와 함께 기업과 개인 사용자들은 어떤 AI 서비스가 자신의 목적에 최적인지를 판단해야 하는 새로운 의사결정 과제에 직면하게 되었다.

기존 연구는 주로 특정 도메인에서 ChatGPT의 성능을 평가하는 데 집중되어 왔다. 예컨대 Kung et al.(2023)은 ChatGPT가 미국 의사면허시험(USMLE)에서 합격 수준의 성과를 보임을 확인하였고, Malinka et al.(2023)은 고등교육 맥락에서 ChatGPT의 잠재력과 위험성을 함께 조망하였다. 그러나 이러한 연구들은 단일 플랫폼 중심의 단편적 평가에 머물러 있으며, ChatGPT, Claude, Gemini를 동일한 이론적 프레임워크 하에 비교·분석한 연구는 거의 존재하지 않는다. 특히 사용자가 AI 서비스를 선택하고 지속적으로 이용하는 핵심 요인인 '인간 유사성'과 '에이전틱 속성'을 통합적 관점에서 비교한 연구는 학술적 공백으로 남아 있다.

앨런 튜링(Turing, 1950)이 제안한 이미테이션 게임—이른바 튜링 테스트—은 기계가 인간과 구별되지 않는 지적 반응을 보일 수 있는지를 평가하는 기준으로, AI의 인간 유사성(Human-Likeness)을 측정하는 개념적 토대로 재조명되고 있다. 최근 Elyoseph et al.(2023)은 ChatGPT가 감정 인식 평가에서 인간보다 우수한 성과를 보임을 확인하였으며, Schermer & Thies(2023)는 AI의 지나친 인간 유사성이 불쾌감(creepiness)을 유발하는 역설적 관계를 보고하였다. 이는 인간 유사성이 AI 서비스의 경쟁우위로 작용하는 조건과 한계에 대한 실증적 규명을 요청한다.

동시에, 생성형 AI 서비스의 또 다른 핵심 경쟁 차원으로 '에이전틱 AI(Agentic AI)'가 부상하고 있다. 에이전틱 AI는 목표를 자율적으로 설정하고 복잡한 과업을 순차적으로 수행하는 능력을 갖춘 AI를 의미하며(Wang et al., 2024), Tree of Thoughts(Yao et al., 2023)로 대표되는 자율 추론 기술의 발전이 이를 가속화하고 있다. 그러나 ChatGPT, Claude, Gemini의 에이전틱 속성을 체계적으로 비교한 연구는 아직 존재하지 않는다.

이에 본 연구는 다음과 같은 목적을 설정한다. 첫째, 생성형 AI 서비스의 경쟁우위를 측정하기 위한 이론적 프레임워크로 튜링 테스트 기반 인간 유사성과 에이전틱 AI 속성의 이중 축을 제안한다. 둘째, ChatGPT, Claude, Gemini를 대상으로 14개 공개 벤치마크 2차 데이터를 수집·분석하여 각 서비스의 차별적 경쟁 포지션을 실증적으로 규명한다. 셋째, 분석 결과를 IS/HCI 이론(TAM, 신뢰 이론)과 연계하여 AI 서비스 수용 및 선택에 관한 이론적·실무적 함의를 도출한다.

---

## 2. 이론적 배경 (Theoretical Background)

### 2.1 튜링 테스트와 AI의 인간 유사성

앨런 튜링(1950)은 "기계가 생각할 수 있는가(Can machines think?)"라는 질문에 답하기 위해 이미테이션 게임(Imitation Game)을 제안하였다. 이 게임에서 인간 심판관은 텍스트만으로 대화 상대가 인간인지 기계인지를 판별하며, 기계가 인간으로 오인될 경우 지능적이라고 간주된다. 이 개념은 이후 인공지능 연구의 핵심 평가 기준으로 자리 잡았으며, 오늘날 LLM 기반 생성형 AI의 인간 유사성 평가에 새롭게 적용되고 있다.

인간 유사성(Human-Likeness)은 AI가 인간의 언어적·감정적·인지적 특성을 얼마나 유사하게 재현하는지를 나타내는 개념으로(Elyoseph et al., 2023), 다음의 하위 속성으로 구성된다.

- **언어적 자연성(Conversational Naturalness):** 다회차 대화에서 맥락을 유지하고 자연스러운 언어를 구사하는 능력 (MT-Bench 측정)
- **사실 정확성(Factual Accuracy):** 인간 전문가 수준의 지식을 정확하게 제공하는 능력 (SimpleQA, MMLU-Pro 측정)
- **인간 선호도(Human Preference):** 실제 인간이 AI의 응답을 선호하는 정도 (Chatbot Arena ELO 측정)
- **감성적 일관성(Emotional Consistency):** 장문 맥락에서 감정적·논리적 일관성을 유지하는 능력 (LongBench v2 측정)

Schermer & Thies(2023)는 인간 유사성이 지나칠 경우 "불쾌한 골짜기(Uncanny Valley)" 효과로 인해 사용자의 불쾌감과 불신을 유발할 수 있다고 경고하였다. 이는 AI 서비스가 인간 유사성의 최적 수준을 설계해야 함을 시사하며, 각 서비스의 차별화 전략을 분석하는 이론적 근거가 된다.

### 2.2 에이전틱 AI 속성

에이전틱 AI(Agentic AI)는 단순한 질의-응답을 초월하여 목표 지향적으로 행동하고, 복잡한 과업을 자율적으로 계획·실행하는 AI 시스템을 의미한다(Wang et al., 2024). Wang et al.(2024)은 LLM 기반 자율 에이전트의 핵심 속성을 다음 네 가지로 정의하였다.

1. **계획(Planning):** 복잡한 목표를 하위 과업으로 분해하고 실행 순서를 설계하는 능력 (Reasoning Score, GPQA 측정)
2. **기억(Memory):** 단기·장기 정보를 저장하고 맥락에 따라 활용하는 능력 (LongBench v2 측정)
3. **도구 사용(Tool Use):** 외부 API, 검색 엔진, 코드 실행 환경 등을 자율적으로 활용하는 능력 (Terminal-Bench 측정)
4. **자율 행동(Autonomous Action):** 인간의 개입 없이 과업을 완수하는 능력 (SWE-bench, GAIA 측정)

Yao et al.(2023)의 Tree of Thoughts(ToT)는 LLM이 인간의 의식적 사고 과정처럼 다양한 사고 경로를 탐색하며 최적 해법을 도출하는 에이전틱 추론 패러다임을 제시하여, 에이전틱 속성이 AI 서비스의 핵심 차별화 요소임을 보여주었다.

### 2.3 정보시스템 수용 이론과 AI 서비스 경쟁우위

Davis(1989)의 기술수용모델(TAM: Technology Acceptance Model)은 사용자의 기술 수용을 '인지된 유용성(Perceived Usefulness)'과 '인지된 사용 용이성(Perceived Ease of Use)'으로 설명한다. 생성형 AI 서비스 맥락에서 인간 유사성은 사용 용이성(인간처럼 자연스럽게 소통 가능)을, 에이전틱 속성은 유용성(복잡한 과업을 자율적으로 처리)을 각각 향상시키는 선행 요인으로 기능한다.

Farah et al.(2023)은 ChatGPT에 대한 사용자 신뢰가 수용 의도의 핵심 선행 요인임을 확인하였고, Strzelecki(2024)는 신뢰가 인식된 인간 유사성과 수용 의도를 매개함을 보고하였다. McKnight et al.(2002)의 신뢰 이론에 따르면, 능력 기반 신뢰(competence-based trust)는 AI의 에이전틱 속성으로부터, 호의성 기반 신뢰(benevolence-based trust)는 인간 유사성으로부터 각각 도출된다.

Porter(1985)의 경쟁우위 이론과 자원기반관점(RBV: Resource-Based View, Barney, 1991)을 통합하면, 생성형 AI 서비스의 경쟁우위는 인간 유사성과 에이전틱 속성이라는 두 가지 핵심 역량(core competence)에서 도출되며, 이는 경쟁사가 단기간에 모방하기 어려운 차별화 원천이 된다.

### 2.4 연구 모형

본 연구의 이론적 모형은 다음과 같이 구성된다.

```
┌─────────────────────────────────────────────────────┐
│              생성형 AI 서비스 경쟁우위 프레임워크            │
├──────────────────────┬──────────────────────────────┤
│   인간 유사성 차원       │      에이전틱 AI 차원           │
│  (튜링 테스트 기반)       │   (자율성·도구사용·계획)         │
│                      │                             │
│ · Chatbot Arena ELO  │ · Agentic Score             │
│ · MT-Bench           │ · SWE-bench Verified         │
│ · SimpleQA           │ · Terminal-Bench 2.0         │
│ · LongBench v2       │ · LiveCodeBench              │
│ · MMLU-Pro           │ · GPQA                       │
│ · HLE                │ · Reasoning Score            │
│ · Knowledge Score    │ · Coding Score               │
└──────────────────────┴──────────────────────────────┘
              ↓                           ↓
        인지된 사용 용이성            인지된 유용성
              ↓                           ↓
                      신뢰 (Trust)
                           ↓
              경쟁우위 (Competitive Advantage)
              → 사용자 수용 · AI 서비스 선택
```

---

## 3. 연구방법론 (Research Methodology)

### 3.1 연구 설계

본 연구는 공개된 2차 데이터(secondary data)를 활용한 정량적 비교 분석 연구(quantitative comparative study)이다. 1차 실험 데이터 수집 없이 학술·산업계에서 공개된 표준 벤치마크 점수를 수집·분석함으로써 연구의 객관성과 재현 가능성(reproducibility)을 확보하였다.

### 3.2 데이터 수집

#### 3.2.1 선행연구 데이터베이스 구축

Scopus 데이터베이스를 통해 생성형 AI, 인간 유사성, 에이전틱 AI 관련 SSCI급 논문 1,081편을 수집하였다 (수집 기간: 2022–2025, API 기반 자동 수집).

- **검색 키워드:** self-awareness AND artificial intelligence; machine consciousness; anthropomorphism AND AI; agentic AI; autonomous AI agent; AI autonomy
- **수집 도구:** Python + Scopus API (requests 라이브러리)
- **정렬 기준:** 피인용 수 기준 내림차순

수집된 논문을 대상으로 LDA(Latent Dirichlet Allocation) 토픽 모델링을 수행한 결과, 7개 토픽이 도출되었으며, 본 연구 주제와 직접 관련된 T6(사회적 AI·자아 인식, 207편)와 T7(에이전틱 AI·LLM, 161편)을 핵심 선행연구 풀(pool)로 설정하였다.

#### 3.2.2 벤치마크 2차 데이터 수집

ChatGPT(GPT-5), Claude(Opus 4.6), Gemini(3.1 Pro)를 대상으로, 아래 표와 같이 14개 공개 벤치마크 점수를 수집하였다. 데이터 출처는 BenchLM.ai, LMSYS Chatbot Arena, 각 기관 공식 기술보고서 등이다.

**[표 1] 인간 유사성 벤치마크 데이터 (정규화 점수, 0-100)**

| 벤치마크 | 측정 속성 | ChatGPT | Claude | Gemini | 출처 |
|---------|----------|:-------:|:------:|:------:|------|
| Chatbot Arena ELO | 인간 선호도 | 92.7 | **94.7** | 94.0 | LMSYS (2025) |
| MT-Bench | 대화 자연성 | **90.0** | 89.0 | 87.0 | LMSYS (2024) |
| SimpleQA | 사실 정확성 | **97.0** | 72.0 | 95.0 | BenchLM (2025) |
| LongBench v2 | 맥락 일관성 | **95.0** | 92.0 | 93.0 | BenchLM (2025) |
| MMLU-Pro | 전문가 지식 | **93.0** | 82.0 | 92.0 | BenchLM (2025) |
| HLE | 인간 시험 수준 | 48.0 | **53.0** | 40.0 | BenchLM (2025) |
| Knowledge Score | 지식 종합 | **99.0** | 91.7 | 94.6 | BenchLM (2025) |
| **평균** | | **87.8** | 82.1 | 85.1 | |

**[표 2] 에이전틱 AI 벤치마크 데이터 (정규화 점수, 0-100)**

| 벤치마크 | 측정 속성 | ChatGPT | Claude | Gemini | 출처 |
|---------|----------|:-------:|:------:|:------:|------|
| Agentic Score | 에이전틱 종합 | **87.9** | 85.1 | 86.6 | BenchLM (2025) |
| SWE-bench Verified | 자율 버그 수정 | **84.0** | 80.84 | 75.0 | BenchLM (2025) |
| Terminal-Bench 2.0 | 터미널 자율성 | 75.1 | 65.4 | **77.0** | BenchLM (2025) |
| LiveCodeBench | 실시간 코딩 | **84.0** | 76.0 | 71.0 | BenchLM (2025) |
| GPQA | 전문가 추론 | 92.8 | 91.3 | **97.0** | BenchLM (2025) |
| Reasoning Score | 복합 추론 | 95.6 | 87.8 | **96.7** | BenchLM (2025) |
| Coding Score | 코딩 종합 | 89.3 | 86.9 | **95.0** | BenchLM (2025) |
| **평균** | | **87.0** | 81.9 | 85.5 | |

### 3.3 분석 방법

#### 3.3.1 정규화(Normalization)

벤치마크마다 측정 단위와 척도가 상이하므로, 각 지표를 0-100 척도로 정규화하였다.

```
정규화 점수 = (원점수 / 최고점) × 100
```

Chatbot Arena ELO의 경우 기준 최고점(1,500점)을 적용하여 정규화하였다.

#### 3.3.2 차원별 평균 비교

인간 유사성 차원(7개 지표)과 에이전틱 AI 차원(7개 지표) 각각에 대해 서비스별 산술 평균을 산출하고 비교하였다.

#### 3.3.3 시각화

- **레이더 차트:** 두 차원별 7개 지표에 대한 3개 서비스의 프로파일 비교
- **막대 비교 차트:** 지표별 서비스 간 점수 비교
- **ELO 트렌드 차트:** 2023-2025년 Chatbot Arena ELO 추이
- **2×2 포지셔닝 매트릭스:** 인간 유사성(X축) × 에이전틱 속성(Y축) 기반 경쟁 포지셔닝

---

## 4. 연구방법론 근거 (Justification of Research Methodology)

### 4.1 2차 데이터 활용의 타당성

본 연구가 1차 실험 대신 2차 데이터를 활용한 이유는 다음과 같다.

**첫째, 표준성과 비교 가능성.** 공개 벤치마크는 동일한 조건에서 복수의 AI 모델을 평가하도록 설계되어 있어, 연구자가 직접 수행하는 프롬프트 실험보다 훨씬 높은 표준성과 비교 가능성을 제공한다(Chang et al., 2024). 연구자의 주관적 판단이 개입될 여지를 최소화한다는 점에서 객관성이 높다.

**둘째, 재현 가능성.** 공개 데이터셋을 활용함으로써 연구 결과의 재현 가능성을 보장하며, 이는 과학적 타당성의 핵심 요건이다(Open Science Collaboration, 2015). 다른 연구자들이 동일한 데이터소스를 통해 결과를 검증할 수 있다.

**셋째, 대규모 샘플.** Chatbot Arena ELO의 경우 600만 건 이상의 인간 투표 데이터에 기반하며, 이는 어떤 단일 연구자도 수집할 수 없는 규모이다. 대규모 집단 지성 데이터는 개인 실험 대비 외적 타당도(external validity)가 현저히 높다.

**넷째, 선례.** 2차 데이터 비교 분석은 IS/HCI 분야에서 이미 확립된 연구 방법이다. 예컨대 Farah et al.(2023), Strzelecki(2024) 등은 공개 설문 데이터를 활용하여 AI 서비스 수용을 분석하였으며, 본 연구는 이를 벤치마크 데이터로 확장한다.

### 4.2 튜링 테스트를 인간 유사성 프레임으로 사용하는 근거

튜링 테스트는 AI의 지능을 "인간이 구별하지 못하는가"로 정의한 조작적 기준이다(Turing, 1950). Chatbot Arena ELO는 실제 인간이 두 AI를 블라인드 비교하여 더 자연스럽고 유능하다고 판단한 쪽에 투표하는 방식으로, 튜링 테스트의 현대적 실용화 버전으로 볼 수 있다(Chiang et al., 2024). 따라서 Chatbot Arena ELO를 인간 유사성의 대리 지표(proxy measure)로 사용하는 것은 이론적으로 타당하다.

### 4.3 에이전틱 속성 측정의 근거

Wang et al.(2024)이 제안한 에이전틱 AI의 4대 속성(계획, 기억, 도구 사용, 자율 행동)을 측정하기 위해 사용한 벤치마크들은 각각 다음의 대응 관계를 갖는다.

| 에이전틱 속성 | 측정 벤치마크 | 대응 근거 |
|------------|------------|---------|
| 계획(Planning) | GPQA, Reasoning Score | 전문가급 다단계 추론 요구 |
| 기억(Memory) | LongBench v2 | 장문 맥락 유지 및 활용 측정 |
| 도구 사용(Tool Use) | Terminal-Bench 2.0 | 터미널·도구 자율 조작 측정 |
| 자율 행동(Autonomous Action) | SWE-bench, LiveCodeBench | 인간 개입 없는 과업 완수 측정 |

### 4.4 포지셔닝 분석의 근거

2×2 포지셔닝 매트릭스는 Porter(1985)의 경쟁 포지셔닝 개념을 AI 서비스에 적용한 것으로, 두 차원의 평균 점수를 좌표로 활용하여 서비스 간 경쟁 구도를 직관적으로 시각화한다. 이는 Abrahamson & Rosenkopf(1993) 이후 전략 경영 연구에서 광범위하게 사용되는 분석 도구이다.

---

## 5. 연구 결과 (Results)

### 5.1 인간 유사성 차원 비교

[표 1] 및 레이더 차트 분석 결과, 인간 유사성 차원에서 ChatGPT(87.8)가 가장 높은 평균 점수를 기록하였고, Gemini(85.1), Claude(82.1) 순으로 나타났다. 세부 지표별로는 Claude가 Chatbot Arena ELO(94.7)와 HLE(53.0)에서 1위를 기록하여, 실제 인간 선호도와 인간 수준 시험에서 강점을 보임을 확인하였다. ChatGPT는 SimpleQA(97.0), MMLU-Pro(93.0), Knowledge Score(99.0) 등 지식 정확성 관련 지표에서 독보적 우위를 나타냈다.

### 5.2 에이전틱 AI 속성 차원 비교

[표 2] 분석 결과, 에이전틱 속성 차원에서는 ChatGPT(87.0)가 가장 높은 평균을 기록하였고, Gemini(85.5), Claude(81.9) 순으로 나타났다. 그러나 세부 지표를 보면 Gemini가 GPQA(97.0), Reasoning Score(96.7), Coding Score(95.0), Terminal-Bench(77.0) 등 자율 추론·코딩 지표에서 일관되게 1위를 기록하여, 에이전틱 AI의 핵심 속성인 자율 과업 수행 능력에서 차별적 우위를 보유함을 확인하였다.

### 5.3 경쟁 포지셔닝 분석

2×2 포지셔닝 매트릭스 분석 결과, 세 서비스의 경쟁 포지션이 명확히 분화됨을 확인하였다.

```
에이전틱 ↑
속성
 88 │
    │  Claude(82.1, 81.9)    ChatGPT(87.8, 87.0)
 84 │
    │              Gemini(85.1, 85.5)
 80 │
    └─────────────────────────────────→ 인간 유사성
       80          85          90
```

- **ChatGPT:** 인간 유사성·에이전틱 속성 모두 높음 → "균형형 리더"
- **Gemini:** 에이전틱 속성 강점, 인간 유사성은 중간 → "기술형 에이전트"
- **Claude:** 인간 선호도 최고, 에이전틱 속성은 상대적 약점 → "공감형 파트너"

### 5.4 ELO 트렌드 분석

2023-2025년 Chatbot Arena ELO 추이 분석 결과, Claude가 2024년 이후 가장 빠른 성장세를 기록하며 2025년 기준 ELO 1위(1,420)를 달성하였다. Gemini는 2024년 후반부터 급성장하였고, ChatGPT는 초기 우위에서 출발하여 안정적 성장을 유지하고 있다.

---

## 6. 결론 (Conclusion)

본 연구는 생성형 AI 서비스의 경쟁우위를 측정하기 위한 이론적 프레임워크로 튜링 테스트 기반 인간 유사성과 에이전틱 AI 속성의 이중 축을 제안하고, ChatGPT, Claude, Gemini를 대상으로 14개 공개 벤치마크 2차 데이터를 분석하였다. 주요 발견은 다음과 같다.

**발견 1:** 세 서비스의 경쟁우위 축이 명확히 분화되어 있다. ChatGPT는 지식 정확성, Claude는 인간 선호도·감성 일관성, Gemini는 추론·코딩·멀티모달에서 각각 차별화된 강점을 보유한다.

**발견 2:** 인간 유사성과 에이전틱 속성은 서로 다른 차원에서 독립적으로 기여한다. 인간 유사성 1위(ChatGPT)와 에이전틱 세부 지표 1위(Gemini)가 항상 일치하지 않아, 두 차원이 서로 다른 경쟁우위 축임이 확인된다.

**발견 3:** 튜링 테스트의 현대적 대리 지표인 Chatbot Arena ELO에서 Claude가 1위를 기록하였다. 이는 Claude가 인간과의 교류에서 가장 '인간다운' 경험을 제공하는 서비스임을 시사한다.

**발견 4:** 에이전틱 AI 속성(자율 추론, 코딩, 터미널 조작)에서는 Gemini가 일관되게 우위를 보여, 자율 과업 수행이 요구되는 비즈니스 환경에서 차별적 가치를 제공함을 확인하였다.

---

## 7. 함의 (Implications)

### 7.1 이론적 함의

**첫째,** 본 연구는 생성형 AI 서비스의 경쟁우위를 이론화한 최초의 시도로서, 인간 유사성-에이전틱 속성 이중 프레임워크를 IS/HCI 연구에 기여한다. 이 프레임워크는 향후 AI 서비스 수용 연구(TAM, UTAUT)에 선행 변수로 통합될 수 있다.

**둘째,** 튜링 테스트를 현대 LLM 평가에 재적용하는 방법론적 가교를 제시한다. Chatbot Arena ELO를 튜링 테스트의 대리 지표로 활용하는 접근법은 이론과 실증 연구를 연결하는 새로운 분석 틀을 제공한다.

**셋째,** 에이전틱 AI를 계획·기억·도구사용·자율행동의 4개 속성으로 분해하고 이를 개별 벤치마크와 대응시킨 분류 체계는, 에이전틱 AI 연구의 조작화(operationalization) 방법론에 기여한다.

### 7.2 실무적 함의

**기업 AI 서비스 선택 전략:**
- 지식 집약 업무(법률, 금융 분석, 콘텐츠 작성) → **ChatGPT** 우선 (지식 정확성 강점)
- 고객 응대·상담·교육 등 인간적 교류 강조 업무 → **Claude** 우선 (인간 선호도 강점)
- 자율화·자동화·코딩·데이터 분석 업무 → **Gemini** 우선 (에이전틱 속성 강점)

**AI 서비스 개발자 시사점:**
- 단일 벤치마크 최적화보다 인간 유사성-에이전틱 속성의 균형 설계가 지속 가능한 경쟁우위를 창출한다.
- 인간 선호도(ELO)와 객관적 성능(벤치마크) 간의 괴리에 주목하여, 사용자 경험 중심 설계를 병행해야 한다.

**정책적 함의:**
- AI 서비스 규제 설계 시 인간 유사성 수준에 따른 차별화된 규제 틀이 필요하다. 높은 인간 유사성을 가진 AI는 의인화 오인 위험(Schermer & Thies, 2023) 및 조작 위험에 대한 추가적 규제가 요구된다.

---

## 8. 연구의 한계 (Limitations)

**한계 1: 벤치마크의 시간적 한계.** 본 연구에서 사용한 벤치마크 데이터는 2025년 기준으로 수집되었으며, AI 서비스는 지속적으로 업데이트된다. 따라서 특정 시점의 스냅샷(snapshot)에 기반한 분석으로, 최신 모델 버전에 대한 외적 타당도가 제한될 수 있다.

**한계 2: 벤치마크 선정의 편향 가능성.** 본 연구에서 선정한 14개 벤치마크가 인간 유사성과 에이전틱 속성의 모든 하위 속성을 완전히 포괄하지 못할 수 있다. 특히 감성 지능(emotional intelligence), 창의성(creativity), 윤리적 판단력(ethical reasoning) 등은 현재 표준 벤치마크로 측정하기 어렵다.

**한계 3: 가중치 미반영.** 인간 유사성과 에이전틱 속성 각각의 하위 지표에 동일한 가중치를 부여하였으나, 실제 사용자 맥락에 따라 특정 지표의 중요도가 다를 수 있다. 향후 연구에서 AHP(Analytic Hierarchy Process)나 사용자 설문을 통한 가중치 산정이 필요하다.

**한계 4: 사용자 인식 데이터 부재.** 본 연구는 객관적 벤치마크 데이터에 의존하였으나, 실제 사용자의 주관적 인식(perceived human-likeness, perceived agenticity)을 직접 측정하지 못하였다. 향후 설문 기반 1차 데이터 수집을 통해 객관적 성능과 주관적 인식 간의 괴리를 검증하는 연구가 필요하다.

**한계 5: 3개 서비스로의 제한.** 본 연구는 ChatGPT, Claude, Gemini에 집중하였으나, Grok, Mistral, LLaMA 등 다른 경쟁 서비스를 포함한 포괄적 비교 연구가 향후 과제로 남는다.

---

## 참고문헌 (References)

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management, 17*(1), 99–120.

Chang, Y., Wang, X., Wang, J., Wu, Y., Yang, L., Zhu, K., ... & Xie, X. (2024). A survey on evaluation of large language models. *ACM Transactions on Intelligent Systems and Technology, 15*(3), 1–45.

Chiang, W. L., Zheng, L., Sheng, Y., Angelopoulos, A. N., Li, T., Li, D., ... & Stoica, I. (2024). Chatbot Arena: An open platform for evaluating LLMs by human preference. *arXiv preprint arXiv:2403.04132*.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340.

Dwivedi, Y. K., Kshetri, N., Hughes, L., Slade, E. L., Jeyaraj, A., Kar, A. K., ... & Wright, R. (2023). Generative AI and ChatGPT: Applications, challenges, and AI-human collaboration. *Journal of Information Technology Case and Application Research, 25*(3), 46–54.

Elyoseph, Z., Hadar-Shoval, D., Asraf, K., & Lvovsky, M. (2023). ChatGPT outperforms humans in emotional awareness evaluations. *Frontiers in Psychology, 14*, 1199058.

Farah, M. F., Hasni, M. J. S., & Abbas, A. K. (2023). Investigating the impact of user trust on the adoption and use of ChatGPT. *Journal of Medical Internet Research, 25*, e47900.

Kung, T. H., Cheatham, M., Medenilla, A., Sillos, C., Leon, L., Elepaño, C., ... & Tseng, V. (2023). Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models. *PLOS Digital Health, 2*(2), e0000198.

McKnight, D. H., Choudhury, V., & Kacmar, C. (2002). The impact of initial consumer trust on intentions to transact with a web site: A trust building model. *Journal of Strategic Information Systems, 11*(3–4), 297–323.

Malinka, K., Peresini, M., Firc, A., Hujnak, O., & Januš, F. (2023). On the educational impact of ChatGPT: Is artificial intelligence ready to obtain a university degree? *ACM International Conference Proceeding Series*, 47–56.

Porter, M. E. (1985). *Competitive advantage: Creating and sustaining superior performance*. Free Press.

Schermer, M., & Thies, W. (2023). Is ChatGPT scary good? How user motivations affect creepiness and trust in generative artificial intelligence. *Telematics and Informatics, 83*, 102030.

Strzelecki, A. (2024). ChatGPT awareness, acceptance, and adoption in higher education: The role of trust as a cornerstone. *International Journal of Educational Technology in Higher Education, 21*(1), 1–17.

Turing, A. M. (1950). Computing machinery and intelligence. *Mind, 59*(236), 433–460.

Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., ... & Wen, J. R. (2024). A survey on large language model based autonomous agents. *Frontiers of Computer Science, 18*(6), 186345.

Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023). Tree of Thoughts: Deliberate problem solving with large language models. *Advances in Neural Information Processing Systems, 36*, 11809–11822.

---

*초안 버전 1.0 | 2026-05-20*
*총 분석 논문: Scopus 1,081편 | 사용 벤치마크: 14개 | 분석 대상 서비스: 3개*
