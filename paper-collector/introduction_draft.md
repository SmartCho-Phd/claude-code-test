# Comparative Competitive Advantage of Generative AI Services:
# Focusing on "Turing-Test"-Based Human-Likeness and "Agentic AI Attributes"
# across ChatGPT, Claude, and Gemini

---

## 1. 서론 (Introduction)

생성형 인공지능(Generative AI) 서비스는 2022년 이후 급격한 성장세를 보이며 산업 및 학술 전반에 걸쳐 패러다임 전환을 주도하고 있다. 특히 OpenAI의 ChatGPT, Anthropic의 Claude, Google의 Gemini는 대규모 언어 모델(LLM)을 기반으로 한 대표적인 생성형 AI 서비스로서, 교육·의료·비즈니스·창작 등 다양한 영역에서 인간 전문가와 비견되는 수준의 성능을 시연하고 있다(Hua et al., 2023; Kung et al., 2023). 이와 함께 생성형 AI 서비스 간의 경쟁이 본격화됨에 따라, 각 서비스의 차별적 경쟁우위(competitive advantage)를 규명하려는 학문적·실무적 관심이 고조되고 있다.

기존 연구는 주로 특정 도메인(의료, 교육, 법률 등)에서의 ChatGPT 성능 평가에 집중되어 왔다(Kung et al., 2023; Malinka et al., 2023; Zhai, 2023). 그러나 이러한 연구들은 단일 플랫폼 중심의 평가에 머물러 있으며, 복수의 생성형 AI 서비스를 동일한 이론적 프레임워크 하에 비교하는 연구는 아직 희소하다. 더욱이, 사용자가 AI 서비스를 선택하고 지속적으로 이용하는 데 있어 핵심 요인으로 작용하는 '인간 유사성(human-likeness)'과 '에이전틱 속성(agentic attributes)'을 통합적 관점에서 분석한 연구는 거의 존재하지 않는다.

앨런 튜링(Turing, 1950)이 제안한 이미테이션 게임(Imitation Game), 즉 튜링 테스트(Turing Test)는 기계가 인간과 구별되지 않는 수준의 지적 반응을 보일 수 있는지를 평가하는 고전적 기준으로, AI의 인간 유사성을 측정하는 개념적 토대로 재조명되고 있다. 최근 연구에 따르면 ChatGPT는 감정 인식(emotional awareness) 평가에서 인간보다 우수한 성과를 보이는 등(Elyoseph et al., 2023), 생성형 AI의 인간 유사성은 이미 실질적인 차원에서 검토되고 있다. 동시에 사용자들은 AI가 인간을 지나치게 닮았을 때 불쾌감(creepiness)을 경험한다는 상충 관계(Schermer & Thies, 2023) 역시 보고되고 있어, 인간 유사성이 경쟁우위로 작용하는 구체적 조건에 대한 규명이 필요하다.

한편, 생성형 AI 서비스의 또 다른 핵심 경쟁 차원으로 '에이전틱 AI(Agentic AI)'가 부상하고 있다. 에이전틱 AI란 단순한 질의-응답 수준을 넘어, 목표를 자율적으로 설정하고 복잡한 과업을 순차적으로 수행하는 능력을 갖춘 AI를 의미한다(Wang et al., 2024). Tree of Thoughts(Yao et al., 2023), LLM 기반 자율 에이전트에 관한 연구(Wang et al., 2024)는 에이전틱 속성이 LLM의 질적 변별 요소로 기능할 수 있음을 보여준다. 그러나 ChatGPT, Claude, Gemini 각각의 에이전틱 속성을 비교 분석한 연구는 존재하지 않는다.

이에 본 연구는 생성형 AI 서비스의 경쟁우위를 규명하기 위한 이론적 프레임워크로 (1) 튜링 테스트 기반 인간 유사성과 (2) 에이전틱 AI 속성을 설정하고, ChatGPT·Claude·Gemini를 대상으로 비교 분석을 수행하고자 한다. 본 연구의 결과는 학술적으로 생성형 AI 서비스의 경쟁우위 평가 모형을 제시하는 한편, 실무적으로는 기업 및 개인 사용자의 AI 서비스 선택 기준을 마련하는 데 기여할 것으로 기대된다.

---

## 2. 선행연구 (Prior Literature)

### 2-1. LLM 평가 및 비교 프레임워크

생성형 AI 및 LLM의 성능 평가는 최근 급증하는 연구 관심 분야로, 다양한 평가 기준과 벤치마크가 제시되고 있다.

| # | 저자 | 연도 | 제목 | 저널 | 피인용 |
|---|------|------|------|------|--------|
| 1 | Chang et al. | 2024 | A Survey on Evaluation of Large Language Models | ACM Computing Surveys | 2,550 |
| 2 | Pan et al. | 2024 | Harnessing the Power of LLMs in Practice: A Survey on ChatGPT and Beyond | ACM Transactions on Knowledge Discovery from Data | 615 |
| 3 | Lund & Wang | 2023 | Chatting about ChatGPT: how may AI and GPT impact academia and libraries | Library Hi Tech News | - |

**시사점:** LLM 평가는 단일 지표가 아닌 다차원 프레임워크가 필요하며, 본 연구의 인간 유사성-에이전틱 속성 이중 프레임워크의 필요성을 지지한다.

---

### 2-2. 튜링 테스트 기반 인간 유사성 (Human-Likeness)

| # | 저자 | 연도 | 제목 | 저널 | 피인용 |
|---|------|------|------|------|--------|
| 4 | Elyoseph et al. | 2023 | ChatGPT outperforms humans in emotional awareness evaluations | Frontiers in Psychology | 246 |
| 5 | Schermer & Thies | 2023 | Is ChatGPT scary good? How user motivations affect creepiness and trust in generative AI | Telematics and Informatics | 262 |
| 6 | Hua et al. | 2023 | War and peace (waragent): Large language model-based multi-agent simulation of world wars | arXiv | - |
| 7 | Skjuve et al. | 2023 | The user experience of ChatGPT: findings from a questionnaire study | ACM CHI Conference | - |

**시사점:** ChatGPT는 감정 인식, 공감, 창의적 언어 생성에서 인간 수준에 근접하나, 과도한 인간 유사성은 불쾌감(uncanny valley)을 유발한다는 상충 관계가 존재한다. 이는 본 연구의 튜링 테스트 기반 인간 유사성 측정의 이론적 근거가 된다.

---

### 2-3. 에이전틱 AI 속성 (Agentic AI Attributes)

| # | 저자 | 연도 | 제목 | 저널 | 피인용 |
|---|------|------|------|------|--------|
| 8 | Wang et al. | 2024 | A survey on large language model based autonomous agents | Frontiers of Computer Science | 1,159 |
| 9 | Yao et al. | 2023 | Tree of Thoughts: Deliberate Problem Solving with Large Language Models | NeurIPS | 1,581 |
| 10 | Xi et al. | 2023 | The rise and potential of large language model based agents: A survey | arXiv | - |
| 11 | Sumers et al. | 2024 | Cognitive architectures for language agents | Transactions on Machine Learning Research | - |

**시사점:** 에이전틱 AI는 계획(planning), 기억(memory), 도구 사용(tool use), 자율 행동(autonomous action)의 4가지 속성으로 구성되며, 이는 ChatGPT·Claude·Gemini의 기능 차별화를 분석하는 분류 체계로 활용 가능하다.

---

### 2-4. 생성형 AI 서비스의 신뢰 및 수용

| # | 저자 | 연도 | 제목 | 저널 | 피인용 |
|---|------|------|------|------|--------|
| 12 | Sallam | 2023 | ChatGPT utility in healthcare education, research, and practice | Healthcare | 669 |
| 13 | Farah et al. | 2023 | Investigating the Impact of User Trust on the Adoption and Use of ChatGPT | Journal of Medical Internet Research | 361 |
| 14 | Strzelecki | 2024 | ChatGPT awareness, acceptance, and adoption in higher education: the role of trust | International Journal of Educational Technology in Higher Education | 151 |
| 15 | Cheng & Jiang | 2023 | Antecedents and consequences of travelers' trust towards personalized travel recommendations offered by ChatGPT | International Journal of Hospitality Management | 140 |

**시사점:** 생성형 AI 서비스의 사용자 신뢰는 수용과 지속 사용의 핵심 선행 요인으로, 인간 유사성과 에이전틱 속성은 신뢰 형성을 매개하는 경쟁우위 변수로 위치할 수 있다.

---

### 2-5. 생성형 AI의 경쟁 환경 및 산업적 함의

| # | 저자 | 연도 | 제목 | 저널 | 피인용 |
|---|------|------|------|------|--------|
| 16 | Dwivedi et al. | 2023 | Generative AI and ChatGPT: Applications, challenges, and AI-human collaboration | Journal of Information Technology Case and Application Research | 1,176 |
| 17 | Baidoo-Anu & Owusu Ansah | 2023 | Education in the era of generative AI: Understanding the potential benefits of ChatGPT | Journal of AI | 698 |
| 18 | Lo | 2023 | What is the impact of ChatGPT on education? A rapid review of the literature | Education Sciences | 669 |
| 19 | Tlili et al. | 2023 | What if the devil is my guardian angel: ChatGPT as a case study of using chatbots in education | Smart Learning Environments | - |
| 20 | Sun et al. | 2025 | When ChatGPT Gives Incorrect Answers: The Impact of Inaccurate Information by Generative AI on Tourism Decision-Making | Journal of Travel Research | 129 |

**시사점:** 생성형 AI 서비스들은 교육·의료·관광 등 여러 산업에서 경쟁하고 있으나, 서비스 간 차별적 경쟁우위를 이론화한 연구는 부재하다 — 본 연구의 핵심 기여 지점.

---

## 3. 연구 갭 요약 (Research Gap Summary)

| 구분 | 기존 연구 | 본 연구 |
|------|-----------|---------|
| 분석 대상 | 단일 플랫폼(주로 ChatGPT) | ChatGPT, Claude, Gemini 비교 |
| 평가 프레임 | 도메인별 성능(의료·교육 등) | 튜링 테스트 기반 인간 유사성 + 에이전틱 속성 |
| 경쟁우위 관점 | 부재 | 생성형 AI 서비스의 차별적 경쟁우위 규명 |
| 통합 프레임워크 | 부재 | 인간 유사성-에이전틱 속성 이중 분류 체계 |

---

*초안 작성일: 2026-05-20*
*수집 논문 기반: Scopus (2022–2025), 총 1,081편 분석*
