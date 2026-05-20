# SSCI 투고용 연구 설계 (재설계안)
# Comparative Competitive Advantage of Generative AI Services:
# Focusing on "Turing-Test"-Based Human-Likeness and "Agentic AI Attributes"
# across ChatGPT, Claude, and Gemini

---

## 1. 왜 현재 초안이 SSCI에 부족한가

| 요건 | 현재 초안 | SSCI 요건 |
|------|----------|----------|
| 가설 | 없음 | 이론 기반 가설 H1~Hn 필수 |
| 통계 분석 | 평균 비교 | 회귀/SEM/ANOVA + 유의성 검증 |
| 이론 기여 | 벤치마크 비교 | 기존 이론 확장·검증·반박 |
| 데이터 | 벤치마크만 | 원칙적으로 사용자 인식 데이터 필요 |
| 표본 | 없음 | 명확한 표본 정의·크기·특성 |

---

## 2. 혼합연구 설계 (Mixed-Methods)

### 2.1 연구의 핵심 기여

> **"객관적 AI 성능(벤치마크)과 사용자의 주관적 인식은 얼마나 일치하는가?"**
> 이 괴리(perception gap)를 TAM + 신뢰 이론으로 설명하고,
> ChatGPT·Claude·Gemini 간 차이를 실증한다.

이 질문은 다음 이유로 SSCI 기여가 명확합니다.
- 기존 연구는 벤치마크 또는 설문 중 하나만 사용
- 객관적 성능과 주관적 인식의 괴리는 IS 분야의 핵심 미해결 문제
- 세 서비스를 동일 프레임으로 비교한 선례 없음

---

## 3. 연구 모형 (Research Model)

```
[2차 데이터 — 벤치마크]          [1차 데이터 — 설문]
                                                      
 Obj. Human-Likeness ──H1──→ Perceived Human-Likeness ──H3──→ Trust ──────────────→ Adoption
    (벤치마크 점수)                (사용자 인식)                                         Intention
                                          │                                              ↑
                                          └──────────────────H5(-)──→ Creepiness ───────┘(-)
                                                                                         
 Obj. Agentic Score  ──H2──→ Perceived Agentic Attrs  ──H4──→ Perceived Usefulness ───→(위와 연결)
    (벤치마크 점수)                (사용자 인식)                                              
                                                                                         
 AI Service Type (ChatGPT / Claude / Gemini)          ← Moderating Variable (다집단 분석)
```

---

## 4. 가설 (Hypotheses)

### Phase 1: 벤치마크 → 사용자 인식 (객관 → 주관 연결)

**H1.** 객관적 인간 유사성 벤치마크 점수가 높은 AI 서비스를 사용한 사용자는
       인지된 인간 유사성(Perceived Human-Likeness)이 더 높다.
       *(비교 집단: ChatGPT vs Claude vs Gemini 사용자 간 ANOVA)*

**H2.** 객관적 에이전틱 벤치마크 점수가 높은 AI 서비스를 사용한 사용자는
       인지된 에이전틱 속성(Perceived Agentic Attributes)이 더 높다.

### Phase 2: 인지된 인간 유사성의 이중 효과

**H3.** 인지된 인간 유사성은 사용자 신뢰(Trust)에 정(+)의 영향을 미친다.

**H4.** 인지된 인간 유사성은 불쾌감(Creepiness)에 정(+)의 영향을 미친다.
       *(Uncanny Valley 효과 — Schermer & Thies, 2023)*

**H5.** 불쾌감(Creepiness)은 수용 의도(Adoption Intention)에 부(-)의 영향을 미친다.

### Phase 3: 에이전틱 속성의 효용 경로

**H6.** 인지된 에이전틱 속성은 인지된 유용성(Perceived Usefulness)에 정(+)의 영향을 미친다.

**H7.** 인지된 유용성은 수용 의도(Adoption Intention)에 정(+)의 영향을 미친다.

**H8.** 신뢰(Trust)는 수용 의도(Adoption Intention)에 정(+)의 영향을 미친다.

### Phase 4: 조절 효과 (AI 서비스 유형)

**H9.** AI 서비스 유형(ChatGPT/Claude/Gemini)은 인지된 인간 유사성 → 신뢰
       경로를 조절한다. *(다집단 분석)*

**H10.** AI 서비스 유형은 인지된 에이전틱 속성 → 인지된 유용성 경로를 조절한다.

---

## 5. 변수 정의 및 측정 문항 (Survey Instrument)

### 5.1 인지된 인간 유사성 (Perceived Human-Likeness, PHL) — 4문항
*(Turing, 1950; Elyoseph et al., 2023 기반 개발)*

| 코드 | 문항 |
|------|------|
| PHL1 | 이 AI는 인간처럼 자연스러운 대화를 한다. |
| PHL2 | 이 AI의 응답은 인간 전문가의 수준과 유사하다. |
| PHL3 | 이 AI는 내 감정과 맥락을 인간처럼 이해한다. |
| PHL4 | 이 AI와 대화할 때 인간과 대화하는 느낌을 받는다. |
*5점 Likert (1=전혀 그렇지 않다 ~ 5=매우 그렇다)*

### 5.2 인지된 에이전틱 속성 (Perceived Agentic Attributes, PAA) — 4문항
*(Wang et al., 2024; Yao et al., 2023 기반 개발)*

| 코드 | 문항 |
|------|------|
| PAA1 | 이 AI는 복잡한 과업을 스스로 계획하고 실행한다. |
| PAA2 | 이 AI는 내가 제시한 목표를 자율적으로 달성한다. |
| PAA3 | 이 AI는 필요한 도구나 정보를 스스로 찾아 활용한다. |
| PAA4 | 이 AI는 나의 개입 없이도 과업을 완수한다. |

### 5.3 신뢰 (Trust, TR) — 3문항
*(McKnight et al., 2002)*

| 코드 | 문항 |
|------|------|
| TR1 | 나는 이 AI 서비스가 정확하고 신뢰할 수 있다고 생각한다. |
| TR2 | 나는 이 AI 서비스가 나의 이익을 위해 행동한다고 믿는다. |
| TR3 | 나는 이 AI 서비스를 믿고 중요한 과업을 맡길 수 있다. |

### 5.4 불쾌감 (Creepiness, CR) — 3문항
*(Schermer & Thies, 2023)*

| 코드 | 문항 |
|------|------|
| CR1 | 이 AI가 인간처럼 행동할 때 불편함을 느낀다. |
| CR2 | 이 AI의 반응이 지나치게 인간 같아서 어색하다. |
| CR3 | 이 AI와 상호작용할 때 묘한 불쾌감을 느낀다. |

### 5.5 인지된 유용성 (Perceived Usefulness, PU) — 3문항
*(Davis, 1989)*

| 코드 | 문항 |
|------|------|
| PU1 | 이 AI는 나의 업무 생산성을 향상시킨다. |
| PU2 | 이 AI는 복잡한 과업을 더 쉽게 처리하도록 돕는다. |
| PU3 | 이 AI를 사용하면 더 나은 결과물을 만들 수 있다. |

### 5.6 수용 의도 (Adoption Intention, AI_INT) — 3문항
*(Venkatesh et al., 2003)*

| 코드 | 문항 |
|------|------|
| AI1 | 나는 앞으로도 이 AI 서비스를 계속 사용할 것이다. |
| AI2 | 나는 이 AI 서비스를 주변에 추천할 의향이 있다. |
| AI3 | 나는 이 AI 서비스에 비용을 지불할 의향이 있다. |

### 5.7 통제 변수 (Control Variables)

| 변수 | 측정 |
|------|------|
| AI 서비스 유형 | ChatGPT / Claude / Gemini (집단 변수) |
| 사용 빈도 | 1=거의 안 씀 ~ 5=매일 |
| AI 경험 기간 | 개월 수 |
| 직군 | 학생/연구자/직장인/기타 |
| 연령·성별 | 인구통계 |

---

## 6. 표본 및 자료 수집

### 6.1 표본 크기
- PLS-SEM 기준: 최대 경로 수 × 10 = 약 150명 이상 권장
- **목표 표본: 각 서비스 100명씩 × 3 = 300명**
- 조건: 해당 AI 서비스를 최근 3개월 내 사용 경험자

### 6.2 수집 방법 (선택)

| 방법 | 비용 | 속도 | 적합성 |
|------|------|------|--------|
| Prolific/MTurk (해외 패널) | 유료 | 빠름 | ✅ 권장 |
| Google Forms + SNS 배포 | 무료 | 느림 | △ 가능 |
| 대학 내 설문 | 무료 | 중간 | △ 편의 표본 한계 |

---

## 7. 분석 방법

### 7.1 1단계: 집단 간 차이 검증 (ANOVA)
- 3개 서비스 사용자 집단 간 PHL, PAA 점수 차이 검증
- 사후 검정: Tukey HSD
- → H1, H2 검증

### 7.2 2단계: 측정 모형 검증 (CFA / PLS-SEM)
- 신뢰도: Cronbach's α > 0.70, CR > 0.70
- 타당도: AVE > 0.50 (수렴 타당도), HTMT < 0.85 (판별 타당도)

### 7.3 3단계: 구조 모형 검증 (PLS-SEM)
- 경로 계수 유의성: Bootstrapping (5,000회)
- 설명력: R², Q² (예측 정확도)
- → H3~H8 검증

### 7.4 4단계: 다집단 분석 (MGA)
- ChatGPT vs Claude vs Gemini 집단 간 경로 계수 차이 검증
- SmartPLS 또는 R(lavaan) 활용
- → H9, H10 검증

### 7.5 추가: 객관-주관 괴리 분석
- 벤치마크 순위(객관)와 PHL/PAA 평균(주관) 간 Spearman 상관
- 괴리가 큰 서비스·지표 식별 → 이론적 해석

---

## 8. 투고 대상 저널 추천

| 저널 | IF | 분야 | 적합도 |
|------|-----|------|--------|
| **Telematics and Informatics** | 7.6 | IS/HCI | ★★★★★ |
| **Computers in Human Behavior** | 9.9 | HCI | ★★★★★ |
| **Information & Management** | 8.2 | IS | ★★★★☆ |
| **Internet Research** | 5.9 | IS | ★★★★☆ |
| **Journal of Retailing and Consumer Services** | 11.0 | 마케팅 | ★★★☆☆ |

*Telematics and Informatics*는 Schermer & Thies(2023) 논문이 게재된 저널로 주제 적합성 최상.

---

## 9. 보강된 논문 구조

| 섹션 | 내용 | 분량 |
|------|------|------|
| Abstract | 목적·방법·결과·기여 | 250단어 |
| 1. Introduction | 배경·갭·목적·기여 | 2,000단어 |
| 2. Theoretical Background | 튜링/에이전틱/TAM/신뢰/Uncanny Valley | 3,000단어 |
| 3. Research Model & Hypotheses | 모형도 + H1~H10 | 1,500단어 |
| 4. Methodology | 2차+1차 데이터, 측정도구, 분석방법 | 2,000단어 |
| 5. Results | ANOVA + PLS-SEM + MGA | 2,500단어 |
| 6. Discussion | 가설 결과 해석, 괴리 분석 | 2,000단어 |
| 7. Conclusion | 기여, 함의, 한계, 향후과제 | 1,500단어 |
| References | APA 7th | 40~60편 |
| **합계** | | **~15,000단어** |

---

## 10. 다음 단계 (Action Plan)

| 단계 | 내용 | 우선순위 |
|------|------|---------|
| ① | 설문 도구 완성 및 파일럿 테스트 (10명) | 즉시 |
| ② | IRB(기관생명윤리위원회) 승인 신청 | 즉시 |
| ③ | 표본 수집 (Prolific 또는 SNS) | 2~4주 |
| ④ | PLS-SEM 분석 (SmartPLS 4.0) | 데이터 수집 후 |
| ⑤ | 논문 최종 작성 및 영문 교정 | 분석 후 |
| ⑥ | *Telematics and Informatics* 투고 | 최종 |

---

*재설계일: 2026-05-20*
