# A Dynamic Evolution Model of Call Center Service Processes through AI Contact Centers: A Bottleneck Shifting Perspective

**Draft v1.0 | 2026-05-20**
*Integrative Literature Review + Multiple Case Synthesis*

---

## TABLE OF CONTENTS

1. Abstract
2. Introduction
3. Literature Review
   - 3.1 Dynamic Innovation Model and Service Process Evolution
   - 3.2 Evolution of Call Centers and Contact Centers
   - 3.3 AI Contact Center and AI-based Service Innovation
   - 3.4 Employee Experience, Emotional Labor, and Learning Burden
   - 3.5 Bottleneck Shifting in AICC-based Service Systems
   - 3.6 Synthesis: Toward an Evolutionary Model of AICC-based Call Centers
4. Methodology
   - 4.1 Research Design
   - 4.2 Literature Search Strategy
   - 4.3 Integrative Literature Review Procedure
   - 4.4 Case Search and Selection Procedure
   - 4.5 Multiple Case Synthesis
   - 4.6 Analytical Framework
   - 4.7 Coding Procedure and Reliability
   - 4.8 Pattern Matching and Cross-case Comparison
   - 4.9 Development of Propositions
   - 4.10 Ensuring Methodological Rigor
   - 4.11 Scope and Limitations of the Method
5. Proposed Evolutionary Model of AICC-based Call Centers
   - 5.1 Overview of the Evolutionary Model
   - 5.2 Theoretical Justification of the Five Stages
   - 5.3 Transition Conditions across the Five Stages
   - 5.4 Bottleneck Shifting across the Five Stages
   - 5.5 Figure 1: AICC-based Call Center Evolution Model
   - 5.6 Conceptual Framework: Three-Layer Structure
   - 5.7 Summary
6. Case Synthesis
   - 6.1 Case Selection and Source Verification
   - 6.2 Insurance Industry: Compliance-driven Modularization
   - 6.3 Telecommunication Industry: From Modularization to Intelligentization
   - 6.4 Platform-based AICC: CCaaS and Smart Customer Centers
   - 6.5 Public Sector: AI-based Civil Service and Digital Inclusion
   - 6.6 Cross-case Comparison
   - 6.7 Summary
7. Propositions and Conceptual Framework
   - 7.1–7.8
8. Discussion
   - 8.1–8.8
9. Conclusion
10. References

---

## 1. ABSTRACT

The rapid proliferation of AI Contact Centers (AICC) has fundamentally altered the operational architecture of call centers. Yet existing scholarship tends to treat this transformation as a discrete technological adoption event rather than as a staged evolutionary process with complex, dynamic consequences for service operations, employee experience, and customer experience. This study addresses that gap by developing a dynamic evolution model of call center service processes through AICC adoption, grounded in the Dynamic Innovation Model (Utterback & Abernathy, 1975) and the Reverse Product Cycle framework (Barras, 1986).

Employing an integrative literature review of peer-reviewed scholarship on dynamic innovation models, call center operations management, AI service innovation, emotional labor, and automation trust, complemented by a multiple case synthesis of publicly documented AICC implementations in the insurance, telecommunications, platform-based AICC, and public sectors in South Korea, this study proposes a five-stage evolutionary model: Standardization, Simplification, Modularization, Intelligentization, and Convergence.

The central theoretical claim of this study is that AICC-driven transformation constitutes a process of bottleneck shifting rather than simple automation. AICC relieves lower-order operational bottlenecks—including quality variance, waiting time, information retrieval latency, and after-call work burden—while simultaneously generating higher-order cognitive, emotional, and organizational bottlenecks, such as AI trust deficits, accountability ambiguity, data quality failures, automation fatigue, escalated emotional labor, and governance complexity. Accordingly, the true performance of AICC is determined not solely by the degree of automation achieved, but by the organization's capacity to manage the bottlenecks it creates.

This study makes three theoretical contributions: (1) it extends the Dynamic Innovation Model to an AI-driven service process context; (2) it reconceptualizes AICC adoption as service process evolution rather than technology implementation; and (3) it introduces bottleneck shifting as a core explanatory mechanism for AI service innovation. Practical implications address AICC readiness diagnosis, human-AI role delineation, AI trust and accountability design, and digital inclusion in public sector contexts.

**Keywords:** AI Contact Center; Dynamic Innovation Model; Bottleneck Shifting; Service Process Evolution; Emotional Labor; Call Center Automation

---

## 2. INTRODUCTION

### 2.1 The Transforming Landscape of Contact Center Operations

Contact centers occupy a structurally pivotal position in the service economy. As the primary interface between service organizations and their customers, they handle high volumes of heterogeneous interactions, operate under intense performance scrutiny, and employ frontline workers in demanding emotional and cognitive conditions (Holman, 2002; Gans et al., 2003). For decades, operational improvement in contact centers followed a familiar logic: more agents, better scripts, tighter scheduling, and incremental investments in telephony infrastructure.

The emergence of AI Contact Centers (AICC)—integrated platforms combining speech recognition, natural language processing, large language models, and generative AI within the contact center environment—has disrupted this logic fundamentally. AICC represents not merely an upgrade to existing tools but a reorganization of the core service process: how interactions are routed, how agents are supported, how after-call work is handled, and ultimately how the contact center relates to the broader customer experience ecosystem (Huang & Rust, 2018; Wirtz et al., 2018).

A systematic Scopus database search conducted for this study (query: TITLE-ABS-KEY(("call center" OR "contact center" OR "AICC") AND ("artificial intelligence" OR "machine learning" OR "natural language processing")), search date: May 2025) identified that AI-related contact center publications grew from 71 to 75 studies annually between 2023 and 2025, reflecting accelerating scholarly attention to this domain. Within this set, publications addressing operational efficiency concerns grew from 5 to 15 studies in the same period, suggesting that practitioners and researchers alike are grappling with how AI changes what it means to run a contact center efficiently. Yet despite this momentum, the theoretical frameworks available to explain AICC-driven transformation remain underdeveloped.

### 2.2 Limitations of Existing Research

Existing scholarship on AICC and AI-enabled contact centers can be broadly organized into four streams, each of which, while valuable, addresses only a partial dimension of the phenomenon.

**First**, the *operational management stream* (Gans et al., 2003; Aksin et al., 2007) [verify bibliographic details] conceptualizes contact centers as queuing systems in which efficiency is defined by metrics such as first-call resolution (FCR), average handle time (AHT), and agent utilization. This literature provides a rigorous operational vocabulary but largely treats technology as a parameter input rather than a process-transforming force.

**Second**, the *AI service automation stream* (Huang & Rust, 2018; Wirtz et al., 2018; Flavián et al., 2022) [verify bibliographic details] examines how AI reconfigures service encounters and human-machine role division. While theoretically sophisticated, this literature tends to focus on the service encounter level—the moment of customer interaction—rather than on the organizational and process-level transformation that AICC entails.

**Third**, the *employee experience and emotional labor stream* (Grandey, 2000; Holman, 2002; Bakker & Demerouti, 2007) addresses the wellbeing and psychological demands of frontline contact center workers. This literature has documented how scripting, monitoring, and performance pressure intensify emotional labor; however, it has not yet systematically addressed how AI assistance reshapes the *structure* of labor demands rather than merely their intensity.

**Fourth**, the *AICC adoption and case study stream* documents specific implementations in industry and public sector contexts. However, this literature is heavily shaped by vendor-produced documentation and practitioner reports, which, while informative, are prone to positive reporting bias and rarely situate individual implementations within a coherent theoretical framework.

The critical gap that emerges across these four streams is the absence of an integrative, theoretically grounded model that explains *how* AICC adoption transforms call center service processes *dynamically over time*, and *what mechanisms drive and constrain* that transformation. Specifically, no existing study has applied a dynamic innovation lens to explain AICC-driven service process evolution as a staged, path-dependent process with predictable bottleneck-shifting consequences.

### 2.3 Research Questions

This study is organized around four research questions:

**RQ1.** From the perspective of the Dynamic Innovation Model, what staged evolutionary trajectory do call center service processes follow through AICC adoption?

**RQ2.** Does AICC shift call center bottlenecks from repetitive, physical service tasks toward cognitive, emotional, and exception-handling tasks?

**RQ3.** What tensions or equilibria does AICC-driven evolution create between employee experience and customer experience in call centers?

**RQ4.** Among documented AICC implementation cases, which evolutionary stages are represented, and what common patterns of bottleneck shifting are observable across cases?

### 2.4 Contributions

This study makes the following contributions to theory and practice.

*Theoretically*, it (1) extends Utterback and Abernathy's (1975) Dynamic Innovation Model from manufacturing to AI-enabled service process contexts; (2) proposes a five-stage evolutionary model of AICC-based call centers—Standardization, Simplification, Modularization, Intelligentization, and Convergence—grounded in dynamic innovation logic; and (3) introduces the concept of *bottleneck shifting* as a core explanatory mechanism that distinguishes AICC-driven transformation from simple automation.

*Practically*, the model provides a diagnostic framework with which organizations can assess their current evolutionary stage, anticipate the bottlenecks associated with the next stage, and design human-AI role delineation, accountability structures, and change management strategies accordingly.

---

## 3. LITERATURE REVIEW

### 3.1 Dynamic Innovation Model and Service Process Evolution

The foundation of this study rests on Utterback and Abernathy's (1975) dynamic model of product and process innovation, which proposes that innovation within an industry or organization follows a predictable trajectory. In early, fluid phases of an industry's development, innovation is predominantly *product-oriented*: firms experiment with designs, features, and configurations to attract market demand. As a dominant design emerges and the market stabilizes, innovation progressively shifts toward *process-oriented* improvement: firms compete on efficiency, cost, and reliability rather than novelty.

This transition from product to process innovation is accompanied by a structural change in how organizations manage production: operations become more specialized, standardized, and routinized. Utterback and Abernathy (1975) identify this movement as fundamental to understanding competitive dynamics in industrial settings. Although the model was developed in a manufacturing context, its core logic—that organizational and technological systems evolve through identifiable stages characterized by different innovation logics—has proven broadly applicable.

Barras (1986) adapted and extended this logic specifically to service industries through what he termed the *reverse product cycle*. Barras argued that in services, information technology-driven innovation proceeds in the reverse sequence compared to manufacturing. The first stage involves using new technology to improve the *efficiency* of existing services—doing the same things faster and cheaper. The second stage involves using technology to improve the *quality* of existing services—doing the same things better. The third stage involves using technology to generate *new services* altogether—doing things that were previously impossible. This reversal reflects the nature of service production, in which the process *is* the product: improving how services are delivered simultaneously changes what services are.

Together, these frameworks establish a theoretical basis for understanding AICC adoption not as a discrete technology event but as a stage in a broader evolutionary process. The question is not whether AICC changes how contact centers operate, but *which stage of process-innovation logic* AICC represents in any given organizational context—and what bottlenecks that stage creates and resolves.

Despite the explanatory power of these frameworks, their application to AI-enabled service systems remains limited. Prior applications of dynamic innovation models in service contexts have examined banking automation (Barras, 1986, 1990), software development [citation needed], and healthcare digitalization [citation needed], but have not been systematically extended to AI-driven contact center environments. This gap motivates the central theoretical move of the present study.

### 3.2 Evolution of Call Centers and Contact Centers

Call centers emerged as a distinct organizational form in the 1970s and 1980s, driven by the diffusion of automatic call distribution (ACD) systems and toll-free telephony infrastructure (Batt & Moynihan, 2002) [verify bibliographic details]. Their organizational logic was from the outset deeply shaped by industrial efficiency principles: work was standardized, monitored, and measured according to metrics borrowed from manufacturing (average handle time, calls per hour, queue length).

Gans et al. (2003) provide the foundational analytical treatment of call center operations as queuing systems, in which service outcomes are jointly determined by arrival rates, service rates, staffing levels, and routing rules. Within this framework, improvement is achieved by optimizing these parameters—hiring more agents, scheduling more precisely, routing calls more intelligently—rather than by changing the fundamental structure of the service process itself.

The transition from call centers to *contact centers* in the 2000s marked the first significant structural shift: the addition of email, web chat, and later social media channels required organizations to coordinate heterogeneous interaction types within a single operational unit. This shift, driven by customer channel preferences, can be understood in Barras's terms as a quality-improvement phase: the same services were now offered across more channels, reducing friction for customers without fundamentally changing what those services were.

The arrival of AI-enabled tools—first rudimentary chatbots and interactive voice response (IVR) upgrades, later sophisticated natural language processing, speech analytics, and generative AI—represents a qualitatively different kind of transformation. Rather than adding channels or optimizing staffing, AICC changes the *internal architecture* of the service process itself: which tasks are performed by humans, which by machines, and how the outputs of human and machine labor are combined to produce service outcomes. This is what Barras's model would predict as a third-stage innovation: not merely improved efficiency or quality, but the creation of fundamentally new service production structures.

### 3.3 AI Contact Center and AI-based Service Innovation

Huang and Rust (2018) distinguish among four types of intelligence that AI brings to service: mechanical (performing repetitive tasks), analytical (processing large datasets), intuitive (recognizing patterns from experience), and empathetic (understanding human emotions and context). Contact center AI currently spans the first three types with varying degrees of maturity: mechanical intelligence is highly developed (IVR, chatbots for routine queries); analytical intelligence is maturing rapidly (speech analytics, sentiment analysis, after-call summarization); intuitive intelligence is advancing through large language models; empathetic intelligence remains contested.

Wirtz et al. (2018) argue that service robots and AI systems are most effectively deployed when they occupy a position of *complementarity* with human agents rather than direct substitution. This complementarity principle is central to understanding AICC: the question is not whether AI replaces human agents, but how the division of labor between AI and human agents is designed, and how that design affects the quality and sustainability of both customer experience and employee experience.

Flavián et al. (2022) [verify bibliographic details] document how AI-mediated service encounters alter the psychological dynamics of customer interaction, including trust formation, attribution of service failures, and willingness to engage with automated systems. Their findings suggest that customers do not uniformly prefer automated service: the degree of customer acceptance of AI varies systematically with the complexity of the inquiry, the customer's prior experience with AI, and the presence of human oversight mechanisms.

Within the contact center literature specifically, recent empirical work has examined the effects of chatbot deployment on customer satisfaction (Chung et al., 2020) [verify bibliographic details], the role of speech analytics in quality monitoring [citation needed], and the integration of large language models in agent-assist systems [citation needed]. While these studies document effects at the level of individual technology deployments, they do not situate these deployments within a cumulative evolutionary model. Each study examines a snapshot; none explains the trajectory.

### 3.4 Employee Experience, Emotional Labor, and Learning Burden

Grandey (2000) defines emotional labor as the management of feeling to create a publicly observable facial and bodily display, drawing on Hochschild's (1983) foundational work. In contact centers, emotional labor is institutionalized: agents are required to maintain a pleasant, patient, and helpful demeanor regardless of their private emotional state or the behavior of the customer they serve (Holman, 2002; Zapf et al., 2003) [verify bibliographic details]. This structural demand has been consistently associated with emotional exhaustion, depersonalization, and reduced job satisfaction (Maslach et al., 2001) [verify bibliographic details].

The introduction of AI tools into the contact center environment alters the emotional labor landscape in two directions simultaneously. On one hand, AI automation of routine, high-volume queries reduces the sheer quantity of emotionally taxing interactions that human agents must handle, potentially providing relief from the monotony that characterizes burnout (Bakker & Demerouti, 2007). On the other hand, as AI handles routine queries, the interactions that reach human agents are increasingly complex, high-stakes, or emotionally charged—escalations, complaints, vulnerable customers, nuanced inquiries. This concentration of demanding interactions may intensify rather than reduce the qualitative emotional burden on agents, even as the quantitative workload decreases.

Bakker and Demerouti's (2007) Job Demands-Resources (JD-R) model provides a useful framework for understanding this dual dynamic. In the JD-R model, job demands (physical, cognitive, emotional) deplete psychological energy, while job resources (autonomy, support, feedback) buffer against depletion. AICC introduces a new class of cognitive demands—AI verification burden, learning burden for new AI tools, exception-handling responsibility—that must be understood alongside traditional contact center demands. Simultaneously, AI-generated information and decision support may function as job resources, providing agents with more accurate information faster and reducing the cognitive effort required for information retrieval.

This tension—AI as both source of relief and source of new demands—has not been adequately theorized in existing contact center scholarship. The present study addresses this through the proposition of a *dual effect* of AICC on employee experience, linked to the bottleneck-shifting mechanism described below.

### 3.5 Bottleneck Shifting in AICC-based Service Systems

The concept of the bottleneck—the constraint that limits the throughput of a system—has a rigorous theoretical basis in Goldratt's (1984) Theory of Constraints (TOC), which holds that every system has at least one bottleneck, and that the goal of management is to identify and exploit constraints rather than to optimize non-constraint elements. TOC has been applied extensively in manufacturing operations management and has more recently been explored in healthcare [citation needed] and service operations [citation needed].

Lee and See (2004) provide the foundational theoretical treatment of trust in automation systems, distinguishing between the calibration of trust (whether trust matches the actual capability of the system) and the dynamics of trust (how trust develops over time through experience). In contact center AI contexts, trust calibration is particularly challenging: AI systems perform reliably on certain query types and unreliably on others, and frontline agents must develop accurate mental models of AI reliability across different conditions. Where AI reliability is overestimated, agents may rely inappropriately on AI outputs, generating service errors. Where AI reliability is underestimated, agents may duplicate effort by manually verifying all AI outputs, negating efficiency gains.

The concept of bottleneck shifting, as applied in this study, integrates these perspectives. We propose that AICC-driven transformation does not eliminate bottlenecks from the contact center service process; rather, it *relocates* them. Bottlenecks shift from lower-order operational constraints—queue length, handle time, after-call work volume, information retrieval latency—to higher-order cognitive, emotional, and organizational constraints—AI trust calibration, accountability for AI errors, exception-handling capacity, emotional labor intensity, data governance complexity. This relocation has profound implications for how organizational performance is measured and managed: the performance metrics appropriate to lower-order bottlenecks (efficiency metrics) are largely inappropriate for measuring the higher-order bottlenecks that AICC creates.

### 3.6 Synthesis: Toward an Evolutionary Model of AICC-based Call Centers

The review above identifies a convergent set of theoretical resources—dynamic innovation models, contact center operations management, AI service innovation, employee experience and emotional labor, automation trust, and bottleneck theory—that have not been previously integrated. Each stream captures a dimension of AICC-driven transformation but lacks the integrative scope to explain the full trajectory of change.

The synthesis that this study proposes rests on three interconnected claims. *First*, AICC adoption follows a staged evolutionary logic, consistent with dynamic innovation models, in which each stage is characterized by a distinct process logic, dominant technology configuration, and performance focus. *Second*, the transition between stages is governed by predictable enabling conditions—demand pressure, data accumulation, technology maturity, organizational AI capability, customer acceptance, and regulatory requirements. *Third*, and most distinctively, each stage both relieves the bottlenecks characteristic of the preceding stage and generates new bottlenecks characteristic of the next stage, such that the total challenge of contact center management does not decrease with AICC adoption but shifts in kind.

This three-part synthesis generates the evolutionary model developed in Section 5 and the propositions elaborated in Section 7.

---

## 4. METHODOLOGY

### 4.1 Research Design

This study adopts an integrative literature review combined with multiple case synthesis as its research design. This approach is appropriate when the phenomenon of interest—in this case, AICC-driven call center service process evolution—is (1) emergent and rapidly evolving, making large-scale primary data collection difficult; (2) theoretically underspecified, requiring conceptual development prior to hypothesis testing; and (3) manifested in diverse organizational contexts that resist reduction to a single comparative analysis.

The goal of this study is not to test pre-specified hypotheses through statistical inference but to develop and justify a theoretically grounded evolutionary model through systematic synthesis of existing literature and documented cases. This is consistent with what Christensen and Carlile (2009) term *theory-building research* [verify bibliographic details], which proceeds by identifying anomalies in existing theory, articulating a new explanatory framework, and grounding that framework in carefully selected and analyzed empirical instances.

### 4.2 Literature Search Strategy

The literature search was conducted across the following databases: Web of Science, Scopus, ScienceDirect, EBSCO Business Source Premier, Emerald Insight, Google Scholar, RISS, DBpia, KCI, and KISS. The inclusion of Korean academic databases (RISS, DBpia, KCI, KISS) reflects the study's particular interest in AICC implementations in the South Korean context, where contact center AI adoption has been especially rapid and extensively documented.

Search terms were organized around the following conceptual clusters:

- **Dynamic innovation:** "dynamic model of innovation," "product-process innovation," "Utterback Abernathy model," "reverse product cycle," "service innovation," "service process innovation"
- **Contact center operations:** "call center operations," "contact center management," "call center performance," "queuing theory service"
- **AICC and AI service:** "AI contact center," "artificial intelligence in service," "service robots," "frontline service technology," "chatbot customer service," "AI service automation," "generative AI customer service," "voicebot," "speech recognition contact center"
- **Employee experience:** "call center employee wellbeing," "emotional labor," "job demands resources model," "frontline worker burnout," "AI learning burden"
- **Automation trust and bottlenecks:** "trust in automation," "human-AI collaboration," "theory of constraints," "bottleneck service operations," "accountability AI"

A preliminary search on Scopus using the query `TITLE-ABS-KEY("call center" OR "contact center" OR "AICC") AND PUBYEAR > 2022 AND PUBYEAR < 2026` returned 1,415 records. Filtering for AI-related terms within this set yielded 204 records. Filtering for operational efficiency terms yielded 27 records, and filtering for emotional labor terms yielded 28 records. These figures indicate a research landscape that has expanded rapidly in volume but remains fragmented across topical silos, reinforcing the need for integrative synthesis.

### 4.3 Integrative Literature Review Procedure

The integrative literature review followed the procedure recommended by Torraco (2005) and Whittemore and Knafl (2005) [verify bibliographic details], which involves five phases: (1) problem identification, (2) literature search, (3) data evaluation, (4) data analysis, and (5) presentation of findings.

**Inclusion criteria:** Peer-reviewed articles and book chapters in English or Korean; published between 2000 and 2025 (with priority given to 2018–2025 for AI-specific topics); directly addressing at least one of the five conceptual clusters identified above. Foundational theoretical sources (Utterback & Abernathy, 1975; Barras, 1986; Goldratt, 1984; Grandey, 2000; Bakker & Demerouti, 2007; Lee & See, 2004) were retained regardless of publication date in recognition of their status as constitutive references for the theoretical framework.

**Exclusion criteria:** Conference abstracts without full-text availability; purely technical papers without theoretical or managerial framing; vendor white papers and industry reports (retained only as supplementary case evidence, not as theoretical sources).

**Data evaluation:** Included sources were assessed for methodological rigor, theoretical clarity, and relevance to the research questions. Foundational theoretical sources (Utterback & Abernathy, 1975; Barras, 1986; Gans et al., 2003; Grandey, 2000; Bakker & Demerouti, 2007; Lee & See, 2004) were retained regardless of publication date.

### 4.4 Case Search and Selection Procedure

Case evidence was drawn from publicly available sources including: corporate official announcements and press releases, independent journalism (business press and technology media), public sector annual reports and procurement documents, and academic case studies where available.

Cases were included if they met all of the following criteria:

1. The organization's core service process involves customer contact or civil inquiry handling.
2. At least one AI-based contact technology (chatbot, voicebot, STT, TTS, speech analytics, generative AI agent-assist, AI Human, or omnichannel AICC) is confirmed as deployed.
3. Process-level changes—in interaction routing, agent workflow, after-call procedures, or channel integration—are documentable from public sources.
4. The case can be mapped to at least one of the five proposed evolutionary stages.
5. Core factual claims can be cross-verified from a minimum of two independent public sources.

Seven cases met these criteria and were selected for analysis: Kyobo Life Insurance (교보생명), KB Non-Life Insurance (KB손해보험), KT Corporation (KT), LG Uplus (LG유플러스), SK Telecom and SK Rental Car (SKT/SK렌터카), Seoul Talk (서울톡 / 120 Dasan Call Foundation), and National Health Insurance Service (국민건강보험공단).

### 4.5 Multiple Case Synthesis

Multiple case synthesis was conducted following the logic of *replication* proposed by Yin (2018): each case serves as an independent test of the proposed model, and convergent findings across cases strengthen theoretical confidence while divergent findings prompt refinement. The seven cases were analyzed along eight dimensions: (1) implementation background, (2) technologies deployed, (3) process changes, (4) reported outcomes, (5) employee experience changes, (6) customer experience changes, (7) bottleneck shifting patterns, and (8) evolutionary stage classification.

### 4.6 Analytical Framework

Cases were coded against a two-dimensional analytical framework: (a) evolutionary stage (Standardization, Simplification, Modularization, Intelligentization, Convergence) and (b) bottleneck type (operational, cognitive, emotional, organizational). Coding was guided by the theoretical definitions developed in the literature review rather than by prior case categorizations.

### 4.7 Coding Procedure and Reliability

Initial coding was performed by the primary investigator. Each case was coded independently against the two-dimensional analytical framework (evolutionary stage × bottleneck type), with coding decisions documented with explicit source references to enable transparency and replication.

This study is a conceptual theory-building work and does not report formal inter-rater reliability statistics. Instead, coding reliability is established through three procedural safeguards: (1) all coding decisions are grounded in theoretically defined criteria established prior to case examination, rather than inferred post hoc; (2) coding rationales are documented and traceable to specific source passages; and (3) cases classified at transitional positions between stages are explicitly flagged and the boundary conditions discussed, rather than assigned to a single stage by fiat. Future empirical validation studies applying this framework are encouraged to establish inter-rater reliability using Cohen's kappa (κ ≥ 0.70) with independent coders.

### 4.8 Pattern Matching and Cross-case Comparison

Pattern matching (Yin, 2018) was used to compare the observed characteristics of each case against the theoretically predicted characteristics of each evolutionary stage. A case was classified at a given stage if the majority of its observable characteristics matched the theoretical description of that stage. Cases that spanned two stages were classified as *transitional* and analyzed for the conditions associated with their stage transition.

Cross-case comparison followed a matrix structure in which rows represent cases and columns represent analytical dimensions, enabling systematic identification of common patterns and divergences across cases.

### 4.9 Development of Propositions

Propositions were developed inductively from the cross-case comparison and deductively from the theoretical framework. Each proposition connects a theoretical claim (derived from the literature review and the evolutionary model) to empirical support (from case evidence), and specifies operationalizable variables for future hypothesis-testing research. This follows the logic of Weick's (1989) theory construction as disciplined imagination [verify bibliographic details], in which propositions function as bridges between conceptual frameworks and empirical investigation.

### 4.10 Ensuring Methodological Rigor

Rigor in integrative conceptual research is established through four criteria adapted from Lincoln and Guba (1985) [verify bibliographic details]: (1) *credibility*—the theoretical model is grounded in well-established foundational theories and cross-verified case evidence; (2) *transferability*—the evolutionary model is designed to apply across contact center types and industries, with scope conditions specified; (3) *dependability*—the literature search and case selection procedures are documented in sufficient detail to permit replication; and (4) *confirmability*—all case claims are traced to public sources, and uncertain claims are marked with [citation needed] or [case evidence needed].

### 4.11 Scope and Limitations of the Method

This study acknowledges three principal limitations of its method. *First*, the integrative literature review cannot provide causal evidence for the relationships between evolutionary stages or bottleneck-shifting dynamics; these are theoretically proposed and require future empirical validation. *Second*, case evidence drawn from public documentation reflects the information that organizations choose to make available, which is subject to selection and positive reporting bias. Accordingly, all performance claims from case sources are treated as *reported outcomes* rather than verified causal effects. *Third*, the case base is drawn primarily from the South Korean AICC context, which is among the world's most advanced in contact center AI adoption; generalization to other national contexts should be approached with appropriate caution.

---

## 5. PROPOSED EVOLUTIONARY MODEL OF AICC-BASED CALL CENTERS

### 5.1 Overview of the Evolutionary Model

The proposed model holds that call center service processes evolve through five stages under the impetus of AICC adoption: **Standardization**, **Simplification**, **Modularization**, **Intelligentization**, and **Convergence**. These stages are not strictly sequential in the sense that all organizations pass through them in the same order or at the same pace; in practice, stages may overlap, and organizations may maintain different processes at different stages simultaneously. However, each stage has a distinct *dominant process logic*, a characteristic *technological configuration*, a primary *bottleneck it relieves*, and a characteristic set of *bottlenecks it creates*.

The model is informed by two theoretical architectures. From Utterback and Abernathy (1975), it derives the principle that innovation logic shifts predictably over time from fluid experimentation to process standardization. From Barras (1986), it derives the principle that in services, technology adoption proceeds first through efficiency improvement, then quality improvement, then new service creation. Together, these frameworks predict a trajectory that moves from stabilization through efficiency toward architectural transformation and finally platform integration—precisely the trajectory described by the five stages.

### 5.2 Theoretical Justification of the Five Stages

**Stage 1: Standardization — Process Stabilization**

In the Utterback-Abernathy framework, process stabilization corresponds to the consolidation of a dominant design around which operational routines can be organized. In the contact center context, this is the stage at which organizations establish the fundamental architecture of the service interaction: standardized scripts, FAQ libraries, quality assessment rubrics, and VOC (voice of customer) classification systems. The dominant logic is variance reduction: the goal is to ensure that all agents deliver a consistent level of service quality regardless of individual skill variation.

This stage addresses the bottleneck of quality variance and agent skill dependency—the risk that service quality fluctuates based on who handles an interaction. The new bottlenecks it creates are characteristic of standardization itself: reduced agent discretion, over-reliance on scripted procedures, and insufficient flexibility to handle edge cases and novel situations.

**Stage 2: Simplification — Process Efficiency**

The Simplification stage corresponds to Barras's first phase of the reverse product cycle: using technology to improve the efficiency of existing service delivery. Here, organizations deploy automated response systems—ARS, IVR, visual IVR, basic FAQ chatbots, and voicebots—to intercept and resolve routine, high-volume queries before they reach human agents. The dominant logic is query segregation: separate what can be automated from what requires human judgment.

The primary bottleneck relieved is simple query volume, which in high-demand contact centers can absorb the majority of agent time without requiring sophisticated judgment. The bottlenecks created are characteristic of automation encounters: automation fatigue for customers who prefer human contact, avoidance of automated systems leading to increased transfer demands, and a concentration of genuinely complex queries in the human-agent queue.

**Stage 3: Modularization — Architectural Decomposition**

Modularization marks the transition to a qualitatively different structural configuration. Rather than routing different query types to different handling mechanisms (as in Simplification), Modularization decomposes the internal structure of the interaction handling process itself into functionally distinct AI-assisted modules: speech-to-text (STT), text-to-speech (TTS), interaction analytics (TA), after-call summarization, interaction classification, knowledge retrieval, recommended response generation, and sentiment analysis.

This architectural decomposition corresponds to what Utterback and Abernathy (1975) describe as the transition from a fluid to a segmental process structure, in which distinct functional modules can be independently developed, optimized, and reconfigured. The primary bottleneck relieved is the cognitive burden of information retrieval and documentation: agents no longer need to manually search knowledge bases or write post-call summaries. The new bottlenecks are architectural: data quality failures within any module can cascade across the system; functional disconnection between modules can create inconsistent outputs; agents face an AI verification burden—the responsibility to check that AI-generated summaries, classifications, and recommendations are accurate.

**Stage 4: Intelligentization — Decision Augmentation**

The Intelligentization stage deploys generative AI and agent-assist systems (Copilot architectures) to provide real-time decision support throughout the interaction. Rather than merely assisting with pre- and post-interaction tasks, AI now accompanies the agent through the interaction itself: generating response recommendations in real time, synthesizing customer context, escalating risk flags, and automating post-interaction processing. Architecturally, this corresponds to what Barras (1986) describes as the quality-improvement phase: the service process is fundamentally the same, but AI augmentation makes it substantially more effective.

The primary bottleneck relieved is agent judgment burden under time pressure: with AI-generated recommendations, agents can respond more quickly and accurately to complex queries without needing to hold all relevant information in working memory simultaneously. The new bottlenecks are distinctively cognitive and organizational: AI trust calibration (does the agent trust the AI recommendation appropriately?), hallucination risk (does the AI generate plausible but incorrect information?), accountability ambiguity (who bears responsibility when an AI-supported decision proves incorrect?), and a heightened final-verification burden on agents who must serve as the last line of defense against AI errors.

**Stage 5: Convergence — Platform Integration**

The Convergence stage represents the most advanced phase of AICC evolution, in which the contact center transforms from a dedicated interaction-handling unit into a node within a broader AI-driven customer experience platform. AICC is integrated with CRM systems, omnichannel infrastructure, AI Human technologies, mobile applications, kiosks, and enterprise data platforms. The dominant logic is context continuity: the customer's history, preferences, current context, and emotional state are maintained and utilized across all touchpoints, and the contact center's role is to orchestrate this integrated experience rather than to handle discrete interactions.

This stage corresponds to Barras's (1986) third phase—the creation of genuinely new service structures that could not exist without the enabling technology. The new organizational form is not a better contact center; it is a different kind of organization. The bottlenecks relieved are the channel fragmentation and customer context discontinuity that characterize multi-channel but non-integrated service environments. The new bottlenecks are platform-level: data governance complexity, personal data protection obligations, cross-functional organizational alignment, the challenge of maintaining human warmth and empathy within a system optimized for consistency and efficiency.

### 5.3 Transition Conditions across the Five Stages

The model proposes that stage transitions are facilitated when the following conditions are sufficiently developed:

| Condition | Description | Most Critical For |
|-----------|-------------|-------------------|
| **Demand Pressure** | Sustained increase in query volume, waiting times, or complexity | Simplification, Modularization |
| **Data Accumulation** | Sufficient accumulation of FAQ, VOC, interaction logs, knowledge documents | Modularization, Intelligentization |
| **Technology Maturity** | Adequate performance of STT, NLP, summarization, generative AI, system integration | Modularization, Intelligentization |
| **Organizational AI Capability** | Internal capacity for AI operations, agent training, data quality management, error response | All transitions |
| **Customer Acceptance** | Customer willingness to engage with chatbots, voicebots, AI Human systems | Simplification, Convergence |
| **Regulatory & Accountability Requirements** | Legal requirements for explanation, personal data protection, accountability in regulated sectors | Intelligentization, Convergence |

Importantly, these conditions are not binary; they exist on continua, and insufficient development of any condition can stall a stage transition or generate transition-associated bottlenecks. This is why some organizations remain at the Modularization stage despite having deployed the technologies nominally associated with Intelligentization: organizational AI capability has not matured to the point where the transition can be managed effectively.

### 5.4 Bottleneck Shifting across the Five Stages

**Table 1: Bottleneck Shifting across Evolutionary Stages**

| Stage | Process Logic | Primary Technology | Bottleneck Relieved | Bottleneck Created |
|-------|--------------|-------------------|--------------------|--------------------|
| Standardization | Process Stabilization | Scripts, FAQs, QA rubrics | Quality variance, skill dependency | Reduced discretion, script rigidity, poor edge-case handling |
| Simplification | Process Efficiency | ARS, IVR, basic chatbot, voicebot | Simple query volume, waiting time, agent overload | Automation fatigue, transfer avoidance, complex query concentration |
| Modularization | Architectural Decomposition | STT, TTS, TA, summarization, knowledge retrieval, recommended response | Information retrieval time, documentation burden | Data quality failures, functional disconnection, AI verification burden |
| Intelligentization | Decision Augmentation | Generative AI, Copilot, Agentic RAG | Judgment burden under time pressure, response latency | AI trust calibration, hallucination, accountability ambiguity, final-verification burden |
| Convergence | Platform Integration | Omnichannel AICC, CRM, AI Human, data platform | Channel fragmentation, context discontinuity | Data governance, privacy obligations, organizational alignment, empathy management |

### 5.5 Figure 1: AICC-based Call Center Evolution Model

```
╔══════════════════════════════════════════════════════════════════════╗
║          Dynamic Innovation Logic (Utterback & Abernathy, 1975;      ║
║                            Barras, 1986)                             ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  AICC-Based Call Center Evolution                                    ║
║                                                                      ║
║  [Standard-] → [Simplifi-] → [Modular-] → [Intelligent-] → [Conver-]║
║  [ization  ]   [cation   ]   [ization ]   [ization     ]   [gence  ]║
║  Process      Process       Architectural  Decision        Platform  ║
║  Stabiliz.    Efficiency    Decomposition  Augmentation    Integration║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Bottleneck Shifting Mechanism                                       ║
║  ─────────────────────────────────────────────────────────────────  ║
║  Lower-order operational bottlenecks are RELIEVED                   ║
║  Higher-order cognitive / emotional / organizational                 ║
║  bottlenecks EMERGE                                                  ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  CX – EX Reconfiguration                                             ║
║  Customer experience and employee experience are reconfigured        ║
║  at each stage; the balance between them shifts.                     ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  AI-driven Customer Experience Platform                              ║
║  (Contact center as ecosystem node, not queue handler)              ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

*Figure 1.* The proposed AICC-based Call Center Evolution Model. Innovation proceeds through five stages, each governed by a distinct process logic. The central mechanism is bottleneck shifting: as AICC resolves lower-order operational bottlenecks, it generates higher-order cognitive, emotional, and organizational bottlenecks. The cumulative effect is a reconfiguration of customer experience and employee experience, culminating in the transformation of the contact center into an AI-driven customer experience platform.

> **[Production note: The ASCII diagram above is a working draft schematic for manuscript purposes. Prior to journal submission, Figure 1 must be replaced with a professionally rendered vector or high-resolution raster graphic (minimum 300 dpi; TIFF or EPS format per target journal specifications). The figure should clearly render the five-stage sequence, the bottleneck-shifting layer, the CX–EX reconfiguration layer, and the theoretical underpinning annotations.]**

### 5.6 Conceptual Framework: Three-Layer Structure

The model operates across three analytical layers:

**Layer 1 — Process Architecture Layer:** The configuration of tasks, technologies, and interaction flows that constitute the service process at each evolutionary stage.

**Layer 2 — Bottleneck Layer:** The constraints that determine operational throughput and service quality at each stage, including both the constraints relieved by AICC and those newly created.

**Layer 3 — Experience Layer:** The consequences of process architecture and bottleneck configuration for customer experience (CX) and employee experience (EX), including their points of tension and alignment.

The three layers interact: changes in process architecture alter the bottleneck profile, which in turn shapes the experience landscape. This interaction is not unidirectional—experience failures (customer dissatisfaction, agent burnout) can feed back into pressure for process architectural change, driving further evolution.

### 5.7 Summary

The five-stage evolutionary model proposes that AICC adoption transforms call center service processes through a progression from process stabilization to platform integration, governed by predictable enabling conditions and characterized at each stage by a distinctive bottleneck-shifting pattern. This model integrates dynamic innovation theory, service innovation theory, and bottleneck concepts into a unified explanatory framework applicable to the AICC context.

---

## 6. CASE SYNTHESIS

### 6.1 Case Selection and Source Verification

Seven cases were selected for synthesis, covering four industry sectors: insurance (Kyobo Life, KB Non-Life), telecommunications (KT, LG Uplus), platform-based AICC (SK Telecom / SK Rental Car), and public sector (Seoul Talk / 120 Dasan Call Foundation, National Health Insurance Service).

Source verification levels are classified as follows:

| Level | Description |
|-------|-------------|
| A | Core facts cross-verified from official organizational sources and independent journalistic sources |
| A– | Core facts confirmed from multiple official sources or reliable industry press |
| B+ | Verified from vendor documentation plus journalistic or regulatory sources |
| B | Multiple sources available but with high vendor dependence or limited official documentation |
| C | Single source or primarily promotional material |

As stated in the methodology, all performance outcomes reported by organizations or vendors are treated as *reported outcomes* or *claimed outcomes* rather than verified causal effects. The purpose of case analysis is not to validate individual organizational performance claims but to identify process change patterns, evolutionary stage characteristics, and bottleneck-shifting dynamics.

"To mitigate the limitations inherent in public-document-based case analysis, this study applied a cross-verification procedure to each case. Core factual claims were confirmed from a minimum of two independent sources—organizational official documentation, solution vendor documentation, press coverage, or public sector reports. Performance figures cited by corporate press releases or vendor materials are presented exclusively as reported or claimed outcomes and are not interpreted as confirmed causal evidence. The analytical focus is the identification of process change patterns, evolutionary stage positioning, and bottleneck-shifting dynamics, not the validation of individual organizational performance."

### 6.2 Insurance Industry: Compliance-driven Modularization

**Case 1: Kyobo Life Insurance (교보생명) AI Contact Center**
*Source Verification Level: A–*

*Background.* Kyobo Life Insurance operates one of South Korea's largest life insurance contact centers, handling high volumes of policy inquiries, claims guidance, and regulatory compliance interactions. The insurance sector's regulatory environment—requiring comprehensive documentation of sales processes and customer consent—creates distinctive compliance-related process demands that generic contact center AI deployments do not address.

*Technologies Deployed.* The organization is reported to have deployed AI-based voice analytics (TA: Talk Analytics), automated quality monitoring for complete-sale verification (완전판매 모니터링), and a standardized script delivery verification system. Outbound delinquency notification processes are reported to utilize automated voicebot capabilities.

*Process Changes.* Prior to AI deployment, quality monitoring relied on sampling-based human review of a small fraction of total interactions. AI-based TA reportedly enables full interaction monitoring, shifting quality assurance from a sampling logic to a comprehensive surveillance logic. Scripted disclosures required by insurance regulations are automatically verified for completeness.

*Reported Outcomes.* The organization reports [case evidence needed for specific figures] improved compliance monitoring coverage and reduced manual QA burden. Specific quantitative performance improvements, where cited in vendor or company materials, are treated as claimed outcomes and not reproduced here without independent verification.

*Bottleneck Shifting.* The primary operational bottlenecks relieved are the labor intensity of sampling-based quality monitoring and the risk of regulatory non-compliance from incomplete scripted disclosures. The new bottlenecks are characteristically cognitive and organizational: the reliability of AI monitoring output must itself be verified; the detection of nuanced compliance failures (customer understanding, emotional pressure, ambiguous consent) remains beyond current AI capability; accountability for mis-detected violations requires clear organizational protocols.

*Evolutionary Stage.* Modularization. The deployment of TA and automated quality monitoring constitutes architectural decomposition of the QA process into AI-assisted functional modules, consistent with Stage 3 characteristics.

---

**Case 2: KB Non-Life Insurance (KB손해보험) Future Contact Center (FCC)**
*Source Verification Level: B+*

*Background.* KB Non-Life Insurance's Future Contact Center (FCC) initiative focused specifically on emergency assistance services—particularly vehicle breakdown and accident response—which require 24-hour availability, rapid response, and location-sensitive information processing.

*Technologies Deployed.* The FCC is reported to incorporate voicebot and automated call handling capabilities integrated with GPS location data for emergency dispatch routing, with STT and TTS components supporting 24-hour voice-based interaction handling.

*Process Changes.* Emergency assistance intake processes that previously required human agents during all hours were partially automated, with AI systems handling initial intake, location verification, and dispatch routing for categorized emergency types.

*Reported Outcomes.* 24-hour automated intake capability for designated emergency categories is reported as a core operational outcome [case evidence needed for performance metrics].

*Bottleneck Shifting.* The operational bottleneck of emergency-hour staffing and intake delay is partially relieved. New bottlenecks include: intent recognition accuracy for distressed callers (whose speech patterns differ from normal), location data accuracy and privacy obligations, and the determination of appropriate thresholds for transfer to human agents when automated handling fails or the situation escalates beyond categorized types.

*Evolutionary Stage.* Simplification transitioning to Modularization. The deployment covers both automated query routing (Simplification) and modular AI components (STT/TTS with GPS integration), suggesting a transitional position.

### 6.3 Telecommunication Industry: From Modularization to Intelligentization

**Case 3: KT Corporation — AI Counseling Assistant and Voice Bot Genie**
*Source Verification Level: A–*

*Background.* KT Corporation operates a large-scale consumer telecommunications contact center serving millions of subscribers across broadband, mobile, and enterprise services. The volume and complexity of subscriber interactions creates significant pressure for AI-assisted efficiency.

*Technologies Deployed.* KT has publicly documented the deployment of an LLM-based AI counseling assistant system for agents, including real-time interaction summarization, automatic interaction classification, and recommended response generation. A consumer-facing voicebot (Genie) handles inbound queries on specific service categories.

*Process Changes.* Agent-side AI assistance shifts the cognitive structure of interaction handling: rather than holding all relevant customer information and service knowledge in working memory, agents receive AI-generated contextual summaries and recommended responses, with the agent's role shifting from information retrieval to evaluation and delivery. Post-interaction documentation, previously a manual after-call work task, is reportedly automated through AI summarization.

*Reported Outcomes.* The organization reports [case evidence needed for specific figures] reductions in after-call work duration and improvements in response consistency. Specific performance figures cited in company communications are treated as claimed outcomes.

*Bottleneck Shifting.* Operational bottlenecks relieved include summarization time, manual classification effort, and information retrieval latency. New bottlenecks include: calibration of agent trust in AI recommendations (over-reliance risk versus under-reliance risk), accuracy of AI classification for routing and analytics purposes, and accountability when AI-recommended responses lead to customer complaints or errors.

*Evolutionary Stage.* Modularization to Intelligentization transition. The combination of modular AI functions (STT, summarization, classification) with real-time agent-assist (recommended response) spans the boundary between Stage 3 and Stage 4.

---

**Case 4: LG Uplus — AI Counseling Advisor (Agentic RAG Architecture)**
*Source Verification Level: A–*

*Background.* LG Uplus, the third-largest telecommunications carrier in South Korea, has publicly described an advanced AI agent-assist architecture incorporating Retrieval-Augmented Generation (RAG) and agentic AI design principles.

*Technologies Deployed.* The system, described as an "AI In The Loop" architecture, deploys generative AI to support agents from interaction initiation through post-interaction classification. Agentic RAG enables the AI to retrieve, synthesize, and present relevant knowledge from internal documents in response to the specific content of each interaction.

*Process Changes.* The AI system participates in the interaction alongside the agent, generating contextually relevant knowledge retrievals and response suggestions in real time. Post-interaction classification and routing are automated. This constitutes a shift from AI as a pre/post-interaction tool to AI as an active participant in the interaction process.

*Reported Outcomes.* The organization reports [case evidence needed for specific figures] reductions in handle time and after-call work, with improvements in first-interaction resolution rates cited in company communications as claimed outcomes.

*Bottleneck Shifting.* This case most clearly illustrates the Intelligentization bottleneck profile. The operational bottlenecks of response latency and information synthesis are substantially relieved. The new bottlenecks are those characteristic of generative AI deployment in high-accountability contexts: hallucination risk (the AI may generate plausible but factually incorrect content from its knowledge base), source attribution and traceability requirements (can the agent verify and cite the source of AI-generated information?), and final accountability (who bears responsibility for a service outcome shaped by AI-generated advice?).

*Evolutionary Stage.* Intelligentization. This case represents the most advanced stage observed among the insurance and telecommunications cases analyzed.

### 6.4 Platform-based AICC: CCaaS and Smart Customer Centers

**Case 5: SK Telecom AI CCaaS / SK Rental Car Smart Customer Center**
*Source Verification Level: B+*

*Background.* SK Telecom has developed an AI Contact Center as a Service (CCaaS) offering that enables organizations to deploy AICC capabilities through a cloud-based subscription model rather than through on-premises infrastructure investment. SK Rental Car has deployed a Smart Customer Center built on this platform.

*Technologies Deployed.* The CCaaS platform integrates chatbot, voicebot, interaction summarization, interaction analytics, and omnichannel coordination within a managed cloud architecture. The SK Rental Car implementation combines these capabilities with vehicle service-specific workflows.

*Process Changes.* For organizations adopting CCaaS, the transition involves not only deploying AI capabilities but shifting from infrastructure ownership to platform dependency—a significant organizational and governance change. For SK Rental Car, process changes include integration of customer interaction data across channels and automation of routine service inquiries.

*Reported Outcomes.* Claimed outcomes associated with the CCaaS model include reduced capital expenditure for AICC deployment and faster capability deployment timelines [case evidence needed for specific figures].

*Bottleneck Shifting.* The CCaaS model shifts the operational bottleneck of AICC infrastructure investment and maintenance to a platform subscription relationship. New bottlenecks characteristic of platform dependency include: vendor lock-in risk, data sovereignty and security obligations, and the challenge of domain-specific customization within a generalist platform architecture.

*Evolutionary Stage.* Simplification to Modularization, with early Convergence characteristics in the omnichannel integration dimension.

### 6.5 Public Sector: AI-based Civil Service and Digital Inclusion

**Case 6: Seoul Talk and 120 Dasan Call Foundation (서울톡 / 120다산콜재단)**
*Source Verification Level: A–*

*Background.* The City of Seoul's 120 Dasan Call Foundation operates one of South Korea's highest-volume public sector contact centers, handling citizen inquiries across administrative services, emergency information, and civil complaints. The Seoul Talk initiative extends this service through a messaging-based channel.

*Technologies Deployed.* The platform integrates a chatbot for FAQ-type administrative inquiries, a visual IVR for common service requests, and integration pathways to human agents for complex or escalated interactions.

*Process Changes.* Routine administrative inquiries—hours of operation, document requirements, appointment scheduling—are handled by automated systems 24 hours per day. Complex civil complaints and nuanced inquiries are routed to human agents.

*Reported Outcomes.* 24-hour automated service availability and reduced queue times for voice channel inquiries are cited as operational outcomes [case evidence needed for specific figures]. Citizen satisfaction metrics are reported to have been maintained or improved, though causal attribution requires methodological caution.

*Bottleneck Shifting.* The operational bottleneck of after-hours service unavailability and routine inquiry volume is substantially relieved. Critical new bottlenecks are: *digital inclusion* (citizens who are elderly, disabled, or digitally inexperienced may not be able to access automated channels effectively, concentrating their interactions in the human voice channel under conditions that may be more demanding for agents); *complex complaint handling* (as simple queries are diverted, the remaining human-handled interactions disproportionately involve distressed or frustrated citizens); and *channel transfer quality* (the quality of transition from automated to human channels is critical and difficult to manage consistently).

*Evolutionary Stage.* Simplification. The primary focus remains on automated handling of routine queries, without the modular AI decomposition characteristic of Stage 3.

---

**Case 7: National Health Insurance Service (국민건강보험공단) — AI Counseling and NHIS-MATE**
*Source Verification Level: A–*

*Background.* The National Health Insurance Service (NHIS) operates a large-scale public contact center handling citizen inquiries related to health insurance eligibility, premium calculation, benefit claims, and healthcare provider information. The NHIS-MATE system provides an AI-based internal knowledge management and decision-support tool for staff.

*Technologies Deployed.* Customer-facing AI services include a chatbot for common health insurance inquiries. Internal-facing, the NHIS-MATE system employs generative AI to support staff in retrieving and applying internal policy knowledge, reducing the burden of navigating complex regulatory documentation.

*Process Changes.* External: routine eligibility and premium inquiries are partially diverted to automated channels. Internal: agents handling complex policy inquiries have AI-assisted access to synthesized knowledge from internal regulatory documents.

*Reported Outcomes.* Reductions in routine inquiry volume reaching human agents and improved staff information retrieval efficiency are reported as operational outcomes [case evidence needed for specific figures].

*Bottleneck Shifting.* External bottlenecks relieved include routine inquiry volume and after-hours service gaps. Internal bottlenecks relieved include knowledge retrieval latency for complex policy questions. New bottlenecks are distinctively public-sector in character: *personal data protection obligations* (health insurance data is among the most sensitive personal data categories); *administrative accountability* (policy interpretations generated or supported by AI systems must be defensible under administrative law); *knowledge currency* (the NHIS-MATE system's value depends on the currency and accuracy of its underlying knowledge base, which must be continuously updated to reflect regulatory changes); and *digital access equity* (elderly citizens who account for a substantial proportion of NHIS interactions may face greater difficulty with automated service channels).

*Evolutionary Stage.* Simplification to Intelligentization. The external customer-facing service is at Stage 2 (Simplification), while the internal NHIS-MATE system exhibits Stage 4 (Intelligentization) characteristics in its application to internal knowledge work.

### 6.6 Cross-case Comparison

**Table 2: Cross-case Comparison of AICC Implementations**

| Case | Sector | Stage | Primary Bottleneck Relieved | Primary New Bottleneck | Source Level |
|------|--------|-------|---------------------------|----------------------|-------------|
| Kyobo Life | Insurance | Modularization | Manual QA sampling burden | AI monitoring reliability, compliance accountability | A– |
| KB Non-Life | Insurance | Simplification → Modularization | Emergency staffing hours, intake delay | Intent recognition accuracy, location data privacy | B+ |
| KT | Telecom | Modularization → Intelligentization | After-call work, information retrieval | AI trust calibration, classification accuracy, accountability | A– |
| LG Uplus | Telecom | Intelligentization | Response latency, knowledge synthesis | Hallucination risk, source traceability, final accountability | A– |
| SKT / SK Rental | Platform | Simplification → Convergence | Infrastructure investment, routine inquiry | Platform dependency, data governance, domain customization | B+ |
| Seoul Talk | Public | Simplification | After-hours unavailability, routine volume | Digital inclusion, complex complaint intensity, transfer quality | A– |
| NHIS | Public | Simplification → Intelligentization | Routine volume, knowledge retrieval | Data protection, administrative accountability, knowledge currency | A– |

**Cross-case patterns:**

*Pattern 1: Universal emergence of accountability bottlenecks at Stage 3+.* Across all cases at or beyond the Modularization stage, accountability-related bottlenecks emerge as significant new constraints. This is consistent with the theoretical prediction that as AI generates and mediates consequential outputs, the question of who bears responsibility for errors becomes organizationally acute.

*Pattern 2: Public sector cases show distinct digital inclusion bottlenecks.* Both public sector cases (Seoul Talk, NHIS) exhibit digital inclusion challenges as significant new bottlenecks, reflecting the public sector's obligation to serve all citizens regardless of digital capability. Private sector cases do not feature this bottleneck prominently, suggesting a sector-specific bottleneck profile.

*Pattern 3: Stage advancement does not uniformly correlate with organizational size.* The NHIS case, a large public organization, operates customer-facing services at Stage 2 (Simplification) while its internal knowledge management is at Stage 4 (Intelligentization)—illustrating that evolutionary stage is process-specific rather than organization-wide.

*Pattern 4: Telecommunications cases are more advanced than insurance cases.* This is consistent with the telecommunications sector's higher data accumulation, technology maturity, and organizational AI capability, as well as the relatively lower regulatory constraint compared to insurance.

### 6.7 Summary

The seven cases collectively support the proposed evolutionary model. Each case is mappable to one or more evolutionary stages, and in every case the bottleneck-shifting pattern is consistent with theoretical predictions: operational bottlenecks are relieved while cognitive, emotional, or organizational bottlenecks emerge. The sector-specific variations—particularly the accountability and data protection intensity of insurance cases and the digital inclusion challenges of public sector cases—suggest that bottleneck profiles are shaped not only by evolutionary stage but by sector-specific regulatory and social contexts.

---

## 7. PROPOSITIONS AND CONCEPTUAL FRAMEWORK

### 7.1 Overview

Based on the theoretical framework and case synthesis, this study advances six propositions. Each proposition is stated formally, accompanied by its theoretical grounding and case-based support, and followed by specification of operationalizable variables for future empirical testing. The propositions function as bridge hypotheses that connect the conceptual evolutionary model to testable empirical claims.

### 7.2 Proposition 1: Dynamic Evolution of AICC-based Call Centers

**P1.** *Call center service processes evolve through five stages—Standardization, Simplification, Modularization, Intelligentization, and Convergence—driven by the progressive adoption of AI Contact Center technologies.*

*Theoretical grounding.* This proposition is directly derived from the synthesis of Utterback and Abernathy's (1975) dynamic innovation model and Barras's (1986) reverse product cycle. Both frameworks predict staged, path-dependent evolution of production processes under technological pressure; this proposition applies that logic to the contact center service context.

*Case-based support.* The seven analyzed cases are mappable to distinct stages or stage transitions, with no case exhibiting characteristics that contradict the five-stage structure. Telecommunication cases (KT, LG Uplus) are observed at Stages 3–4; insurance cases (Kyobo, KB) at Stages 2–3; public sector cases at Stages 2–4; and the platform CCaaS case at Stages 2–5.

*Operationalizable variables for future testing.* Stage classification instrument based on technology deployment and process architecture; longitudinal tracking of stage transitions in panel data; survey measure of organizational readiness for next-stage transition.

### 7.3 Proposition 2: Bottleneck Shifting

**P2.** *AICC adoption relieves lower-order operational bottlenecks—including quality variance, query volume, information retrieval latency, and after-call work burden—while simultaneously generating higher-order cognitive, emotional, and organizational bottlenecks.*

*Theoretical grounding.* This proposition integrates the Theory of Constraints (Goldratt, 1984) with Lee and See's (2004) automation trust framework. TOC establishes that bottleneck elimination generates new bottlenecks elsewhere in the system; automation trust theory specifies the cognitive demands that AI-mediated processes impose on human operators.

*Case-based support.* In all seven cases, the primary operational bottleneck targeted by AICC deployment is at least partially relieved (routine query volume, after-call documentation, monitoring coverage, emergency intake), while in all cases at Stage 3 or above, new bottlenecks emerge at the cognitive (AI verification, trust calibration), emotional (intensified emotional labor on exception handling), or organizational (accountability, data governance) level.

*Operationalizable variables.* Pre/post measurement of operational metrics (FCR, AHT, queue time); simultaneous measurement of cognitive burden (NASA-TLX or adapted instrument [citation needed]), emotional exhaustion (Maslach Burnout Inventory [citation needed]), and perceived accountability clarity; stage as a moderating variable.

### 7.4 Proposition 3: Dual Effect on Employee Experience

**P3.** *AICC exerts a dual effect on employee experience: reducing repetitive task burden while simultaneously increasing AI verification burden, learning burden, and exception-handling intensity.*

*Theoretical grounding.* Bakker and Demerouti's (2007) JD-R model provides the explanatory structure: AICC reduces certain job demands (repetitive query handling, manual documentation) while introducing new demands (AI verification, tool learning, exception escalation). The net effect on employee wellbeing is therefore not straightforwardly positive or negative but depends on the relative magnitude of demands reduced and demands introduced.

*Case-based support.* The KT and LG Uplus cases document reductions in post-interaction documentation burden as claimed outcomes, while simultaneously indicating that agents bear responsibility for verifying AI-generated summaries and recommendations—a new cognitive demand. The Seoul Talk and NHIS cases suggest that as simple queries are automated, human agents handle a higher proportion of emotionally demanding interactions.

*Operationalizable variables.* Job demands survey items specific to AI contact center contexts (AI verification load, learning burden, exception handling frequency); job resources items (AI decision support quality, feedback clarity); wellbeing outcomes (emotional exhaustion, job satisfaction, turnover intention).

### 7.5 Proposition 4: AI Trust and Accountability as Moderators

**P4.** *The performance outcomes of AICC-based call centers are moderated by the degree of AI trust calibration and accountability clarity within the organization.*

*Theoretical grounding.* Lee and See (2004) establish that the performance consequences of automation depend not on automation capability alone but on the correspondence between operator trust and actual system reliability. When trust is miscalibrated—either excessive or insufficient—performance degradation occurs even when the underlying AI system is capable. Accountability clarity (the degree to which responsibility for AI-influenced decisions is clearly assigned) determines whether errors are surfaced, addressed, and corrected.

*Case-based support.* The LG Uplus case most explicitly illustrates accountability as a bottleneck: the Agentic RAG architecture generates responses from internal documents, requiring clear organizational protocols for what happens when those responses prove incorrect. The insurance cases illustrate regulatory accountability as a structuring condition for technology deployment.

*Operationalizable variables.* AI trust calibration (comparing agent-reported confidence in AI outputs with AI output accuracy metrics); accountability clarity (organizational survey measure); performance outcomes (service error rate, complaint rate, escalation rate).

### 7.6 Proposition 5: Transformation from Contact Handling to Customer Experience Platform

**P5.** *As AICC maturity increases, the organizational role of the contact center shifts from interaction processing toward customer experience management and orchestration.*

*Theoretical grounding.* This proposition reflects Barras's (1986) third-phase logic—the creation of genuinely new service structures—applied to the Convergence stage of the evolutionary model. It is also consistent with Huang and Rust's (2018) argument that AI progressively expands the scope of what service organizations can do, not merely how efficiently they do it.

*Case-based support.* The SKT CCaaS case illustrates the organizational restructuring associated with platform-model AICC, which changes the contact center's relationship to its technology infrastructure (from owner to subscriber) and to its service delivery role (from interaction handler to platform participant).

*Operationalizable variables.* Organizational self-classification of contact center role (survey); scope of CRM and cross-channel integration; percentage of interactions handled through non-voice, non-agent channels.

### 7.7 Proposition 6: Human Empathy Reallocation

**P6.** *AICC does not replace human empathy in service interactions but reallocates it: as routine interactions are automated, human empathy is concentrated in high-complexity, high-stakes, and emotionally demanding interactions.*

*Theoretical grounding.* This proposition draws on Grandey's (2000) emotional labor theory, which distinguishes between the surface acting required by scripted routine interactions and the deep acting required by genuine emotional engagement in complex situations. As AICC automates surface acting at scale, the remaining human-handled interactions disproportionately require deep acting—a qualitatively more demanding form of emotional labor.

*Case-based support.* The Seoul Talk and NHIS cases both document the concentration of complex and distressed-citizen interactions in the human-agent queue as simple queries are automated. The Kyobo Life case implicitly illustrates this dynamic: AI monitoring handles the routine compliance verification that previously occupied a significant portion of QA effort, freeing (and concentrating) human attention on nuanced compliance signals.

*Operationalizable variables.* Complexity distribution of human-handled interactions (pre/post AICC); emotional exhaustion trajectory by agent cohort; deep acting frequency (surface acting vs. deep acting item ratio in emotional labor survey).

### 7.8 Proposition Summary Table

**Table 3: Summary of Propositions**

| Proposition | Core Claim | Theoretical Basis | Key Future Variables |
|-------------|-----------|-------------------|---------------------|
| P1 | Five-stage evolutionary path | Utterback & Abernathy (1975); Barras (1986) | Stage classification; transition timing |
| P2 | Bottleneck shifting | Goldratt (1984); Lee & See (2004) | Operational metrics; cognitive/emotional burden |
| P3 | Dual EX effect | Bakker & Demerouti (2007); Grandey (2000) | JD-R variables; wellbeing outcomes |
| P4 | Trust and accountability as moderators | Lee & See (2004) | Trust calibration; accountability clarity |
| P5 | CX platform transformation | Barras (1986); Huang & Rust (2018) | Organizational role; integration scope |
| P6 | Human empathy reallocation | Grandey (2000); Holman (2002) | Interaction complexity distribution; deep acting |

---

## 8. DISCUSSION

### 8.1 Overview

This study has proposed a five-stage evolutionary model of call center service processes under AICC adoption and has advanced six propositions connecting the model to theoretical foundations in dynamic innovation, operations management, AI service innovation, emotional labor, and automation trust. This discussion section elaborates the theoretical and practical implications of the model, addresses its limitations, and identifies directions for future research.

### 8.2 Theoretical Implications

**Extending the Dynamic Innovation Model to AI-driven Service Contexts**

The primary theoretical contribution of this study is the extension of Utterback and Abernathy's (1975) dynamic innovation model—originally developed in manufacturing—to an AI-driven service process context. This extension is not merely analogical; it is substantive. The five stages proposed in this study are not simply relabeled versions of the Utterback-Abernathy stages; they reflect the specific architectural characteristics of service production in which process and product are co-produced in real time. The shift from Process Stabilization through Process Efficiency and Architectural Decomposition to Decision Augmentation and Platform Integration captures the distinctive logic of AI innovation in high-contact service environments.

This extension adds to a developing body of scholarship that applies dynamic innovation models to digital and AI-enabled industries [citation needed], contributing a service-specific evolutionary model grounded in empirical case evidence.

**Reconceptualizing AICC as Service Process Evolution**

A second theoretical contribution lies in the reconceptualization of AICC adoption as service process evolution rather than technology implementation. The dominant frame in practitioner and much scholarly discourse treats AICC as a technology investment decision: deploy the technology, measure the efficiency gain, calculate the ROI. The evolutionary model proposed here challenges this frame by insisting that AICC deployment is intelligible only in the context of the organization's prior evolutionary stage and the bottleneck-shifting consequences that the next stage will produce. Organizations that deploy Intelligentization-stage technologies (generative AI agent-assist) without having developed the organizational AI capability associated with Stage 3 (Modularization) are likely to encounter bottlenecks characteristic of Stage 4 without the operational foundation necessary to manage them.

**Bottleneck Shifting as a Core Explanatory Mechanism**

The concept of bottleneck shifting, as developed in this study, offers a new analytical lens for understanding AI service innovation dynamics. Unlike efficiency-focused frameworks that evaluate AICC in terms of the bottlenecks it removes, the bottleneck-shifting framework insists on evaluating AICC in terms of the bottlenecks it creates alongside those it removes. This dual accounting has implications not only for AICC specifically but for AI service innovation more broadly: any AI deployment that removes an existing bottleneck without attending to the bottlenecks it creates is likely to generate unexpected performance degradation in the medium term.

### 8.3 Practical Implications

**Stage Diagnosis before AICC Investment**

The most direct practical implication of the evolutionary model is that organizations should diagnose their current evolutionary stage before making AICC investment decisions. An organization at the Standardization stage that attempts to deploy Intelligentization-level AI will encounter not only the technical challenges of integration but the organizational bottlenecks of Stage 4—AI trust calibration, accountability ambiguity, hallucination management—without the data accumulation, technology maturity, and organizational AI capability that characterize Stage 3. The result is likely to be technology deployment failure or, worse, deployment that appears successful on operational metrics while generating significant unmanaged employee and customer experience costs.

**Human-AI Role Delineation Design**

Proposition 6 (Human Empathy Reallocation) suggests that AICC deployment decisions are simultaneously decisions about what kind of emotional and cognitive demands are placed on human agents. Organizations that automate routine query handling without designing the resulting human-handled interaction environment—its training implications, its supervision structure, its workload management—are likely to experience agent burnout and attrition as a delayed consequence of apparently successful automation.

**AI Trust and Accountability Frameworks**

Proposition 4 (AI Trust and Accountability as Moderators) implies that AICC deployment requires explicit organizational design of trust calibration and accountability structures, not merely technical deployment. Agents must understand the reliability profile of their AI systems—which outputs to trust, which to verify, which to override—and must have clear organizational protocols for handling situations in which AI outputs are incorrect or contested.

### 8.4 Implications for AI Service Business Development

For organizations developing or selling AICC solutions, the bottleneck-shifting framework offers a more honest and strategically useful value proposition than simple efficiency metrics. Vendors who help clients understand the full bottleneck profile of each evolutionary stage—not only the operational improvements but the new organizational requirements they create—are better positioned to support sustained adoption and to differentiate from competitors offering narrow point solutions.

### 8.5 Public Sector Implications

The public sector cases analyzed in this study highlight a set of implications specific to government and quasi-governmental contact center operations. Digital inclusion—the obligation to serve citizens regardless of digital capability—creates bottleneck profiles that differ significantly from private sector contexts. Public sector AICC deployments that succeed in automating simple queries may inadvertently concentrate the most difficult and emotionally demanding citizen interactions in the human-agent queue while simultaneously creating barriers for digitally underserved populations. Public sector AICC strategy must explicitly address these distributional effects.

### 8.6 Limitations

**Absence of primary empirical data.** The model is developed through literature review and public-document case analysis. Causal relationships between evolutionary stages, bottleneck profiles, and performance outcomes are proposed as theoretically motivated hypotheses rather than empirically verified findings.

**Case base scope.** Seven cases from the South Korean market, while diverse in sector, represent a single national context characterized by among the world's highest AICC adoption rates. Generalization to other contexts requires empirical validation.

**Positive reporting bias.** Despite cross-verification procedures, public case documentation is systematically subject to positive reporting bias. Cases in which AICC deployment generated significant operational failures are underrepresented in public documentation and therefore in this analysis.

**Stage classification subjectivity.** Classification of cases to evolutionary stages, while theory-guided, involves interpretive judgment. Inter-rater reliability procedures are specified but cannot be fully reported in the context of a conceptual study.

### 8.7 Future Research Directions

**AICC Maturity Index.** Developing a validated instrument for measuring an organization's position within the five-stage evolutionary model would enable large-scale survey research on the determinants and consequences of stage advancement.

**Agent experience studies.** Longitudinal survey research on the dual effect of AICC on agent job demands, resources, and wellbeing (P3) would provide the empirical foundation for evidence-based agent experience design.

**Customer experience investigation.** The relationship between evolutionary stage, bottleneck profile, and customer experience outcomes is theoretically proposed but empirically unexamined. Research combining AICC stage classification with customer satisfaction data (e.g., KSQI or equivalent) would test P5 directly.

**Interaction log analysis.** Where organizations permit access, analysis of interaction log data (query complexity distribution, escalation patterns, handle time) would provide objective evidence for the bottleneck-shifting dynamics proposed in P2.

### 8.8 Summary

This study makes a three-part theoretical contribution—extending dynamic innovation models to AI-driven service contexts, reconceptualizing AICC as service process evolution, and introducing bottleneck shifting as a core explanatory mechanism—with practical implications for AICC investment strategy, human-AI role design, accountability framework development, and public sector digital inclusion. The evolutionary model and six propositions advanced here provide a foundation for a program of empirical research on AICC-driven call center transformation.

---

## 9. CONCLUSION

This study set out to address a fundamental gap in the scholarly understanding of AI Contact Centers: the absence of an integrative, theoretically grounded model that explains how AICC adoption transforms call center service processes dynamically over time, and what mechanisms drive and constrain that transformation.

### Answers to Research Questions

**RQ1** asked: From the perspective of the Dynamic Innovation Model, what staged evolutionary trajectory do call center service processes follow through AICC adoption? The proposed AICC-based Call Center Evolution Model answers this question by identifying five sequential stages—Standardization, Simplification, Modularization, Intelligentization, and Convergence—each governed by a distinct process logic (process stabilization → process efficiency → architectural decomposition → decision augmentation → platform integration) that maps directly onto the efficiency–quality–new-service progression predicted by Barras's (1986) reverse product cycle and the fluid-to-specific process transition of Utterback and Abernathy (1975).

**RQ2** asked: Does AICC shift call center bottlenecks from repetitive, physical service tasks toward cognitive, emotional, and exception-handling tasks? The cross-case synthesis confirms this shift across all seven cases examined. In every case at Stage 3 (Modularization) or above, the operational bottlenecks targeted by AICC deployment were at least partially relieved, while new bottlenecks emerged at the cognitive (AI verification, trust calibration), emotional (intensified exception-handling emotional labor), and organizational (accountability, data governance) levels. The bottleneck-shifting mechanism is thus empirically supported by the case evidence, consistent with P2.

**RQ3** asked: What tensions or equilibria does AICC-driven evolution create between employee experience and customer experience in call centers? The analysis reveals a dual-effect pattern (P3): AICC reduces repetitive task burden for agents while simultaneously concentrating the most demanding interactions—complex escalations, distressed customers, nuanced complaints—in the human-handled queue. This concentration intensifies the qualitative emotional labor demands on agents even as quantitative workload decreases, creating a structural tension between operational efficiency gains (a customer experience improvement) and escalating agent emotional exhaustion (an employee experience cost). P6 (Human Empathy Reallocation) further specifies that this tension does not disappear at higher stages but transforms: as automation scope expands, human empathy becomes increasingly concentrated in high-stakes interactions that require deep acting rather than surface acting.

**RQ4** asked: Among documented AICC implementation cases, which evolutionary stages are represented, and what common patterns of bottleneck shifting are observable? The seven analyzed cases span Stages 2 through 5, with telecommunications cases (KT, LG Uplus) at Stages 3–4, insurance cases at Stages 2–3, public sector cases at Stages 2–4, and the CCaaS platform case exhibiting early Stage 5 characteristics. Three cross-case patterns are consistently observable: (1) accountability bottlenecks emerge universally at Stage 3 and above; (2) public sector cases generate distinct digital inclusion bottlenecks absent from private sector cases; and (3) evolutionary stage is process-specific rather than organization-wide, with some organizations simultaneously operating at different stages for customer-facing and internal processes.

### Summary of Contributions

Six propositions connect the evolutionary model to testable empirical claims regarding the staged trajectory of AICC evolution, the dual effects of AICC on employee experience, the moderating roles of AI trust and accountability, the organizational transformation of the contact center toward a customer experience platform, and the reallocation of human empathy to high-complexity interactions. Collectively, these propositions provide a research agenda for empirical validation of the model across diverse organizational and national contexts.

For practitioners, the model's most important implication is diagnostic: before investing in AICC technologies, organizations should assess their current evolutionary stage, anticipate the bottlenecks that the next stage will create, and design organizational structures—human-AI role delineation, accountability frameworks, agent experience management, data governance—that are adequate to those bottlenecks. The performance of AICC is determined not by the degree of automation achieved but by the organization's capacity to manage the bottlenecks that automation creates.

---

## 10. REFERENCES

Aksin, Z., Armony, M., & Mehrotra, V. (2007). The modern call center: A multi-disciplinary perspective on operations management research. *Production and Operations Management, 16*(6), 665–688. [verify bibliographic details]

Bakker, A. B., & Demerouti, E. (2007). The job demands-resources model: State of the art. *Journal of Managerial Psychology, 22*(3), 309–328.

Barras, R. (1986). Towards a theory of innovation in services. *Research Policy, 15*(4), 161–173.

Barras, R. (1990). Interactive innovation in financial and business services: The vanguard of the service revolution. *Research Policy, 19*(3), 215–237.

Batt, R., & Moynihan, L. (2002). The viability of alternative call centre production models. *Human Resource Management Journal, 12*(4), 14–34. [verify bibliographic details]

Christensen, C. M., & Carlile, P. R. (2009). Course research: Using the case method to build and teach management theory. *Academy of Management Learning & Education, 8*(2), 240–251. [verify bibliographic details]

Chung, M., Ko, E., Joung, H., & Kim, S. J. (2020). Chatbot e-service and customer satisfaction regarding luxury brands. *Journal of Business Research, 117*, 587–595. [verify bibliographic details]

Flavián, C., Pérez-Rueda, A., Belanche, D., & Casaló, L. V. (2022). Intentional and unintentional side-effects of AI-assistant recommendations. *Journal of Business Research, 152*, 487–497. [verify bibliographic details]

Gans, N., Koole, G., & Mandelbaum, A. (2003). Telephone call centers: Tutorial, review, and research prospects. *Manufacturing & Service Operations Management, 5*(2), 79–141.

Goldratt, E. M. (1984). *The goal: A process of ongoing improvement*. North River Press.

Grandey, A. A. (2000). Emotional regulation in the workplace: A new way to conceptualize emotional labor. *Journal of Occupational Health Psychology, 5*(1), 95–110.

Hochschild, A. R. (1983). *The managed heart: Commercialization of human feeling*. University of California Press.

Holman, D. (2002). Employee wellbeing in call centres. *Human Resource Management Journal, 12*(4), 35–50.

Huang, M. H., & Rust, R. T. (2018). Artificial intelligence in service. *Journal of Service Research, 21*(2), 155–172.

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80.

Lincoln, Y. S., & Guba, E. G. (1985). *Naturalistic inquiry*. Sage.

Maslach, C., Schaufeli, W. B., & Leiter, M. P. (2001). Job burnout. *Annual Review of Psychology, 52*(1), 397–422.

Torraco, R. J. (2005). Writing integrative literature reviews: Guidelines and examples. *Human Resource Development Review, 4*(3), 356–367. [verify bibliographic details]

Utterback, J. M., & Abernathy, W. J. (1975). A dynamic model of process and product innovation. *Omega, 3*(6), 639–656.

Weick, K. E. (1989). Theory construction as disciplined imagination. *Academy of Management Review, 14*(4), 516–531. [verify bibliographic details]

Whittemore, R., & Knafl, K. (2005). The integrative review: Updated methodology. *Journal of Advanced Nursing, 52*(5), 546–553. [verify bibliographic details]

Wirtz, J., Patterson, P. G., Kunz, W. H., Gruber, T., Lu, V. N., Paluch, S., & Martins, A. (2018). Brave new world: Service robots in the frontline. *Journal of Service Management, 29*(5), 907–931.

Yin, R. K. (2018). *Case study research and design: Methods* (6th ed.). Sage.

Zapf, D., Isic, A., Bechtoldt, M., & Blau, P. (2003). What is typical for call centre jobs? Job characteristics, and service interactions in different call centres. *European Journal of Work and Organizational Psychology, 12*(4), 311–340. [verify bibliographic details]

---

*[verify bibliographic details] = Bibliographic information requires independent verification prior to submission.*
*[citation needed] = A supporting citation is required; the theoretical claim is established but the specific reference has not been confirmed.*
*[case evidence needed] = Specific quantitative claims require independent source verification before inclusion.*

---

## SUBMISSION METADATA (for journal submission — complete before submitting)

### Author Information
**Corresponding Author:**
- Name: [Author Name]
- Affiliation: [Department, Institution, City, Country]
- Email: [email address]
- ORCID: [https://orcid.org/XXXX-XXXX-XXXX-XXXX]

**Co-Author(s):**
- Name: [Co-author Name]
- Affiliation: [Department, Institution, City, Country]
- ORCID: [https://orcid.org/XXXX-XXXX-XXXX-XXXX]

### Acknowledgments
[Acknowledge funding agencies, research assistants, or institutional support here. If none, write: "The authors received no specific funding for this work."]

### Funding Statement
This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.
*[Update if funding was received: include grant number, funder name, and role of funder.]*

### Conflict of Interest Statement
The authors declare no conflict of interest.

### Data Availability Statement
This study is a conceptual integrative review and multiple case synthesis. No primary empirical data were collected. All case evidence was derived from publicly available sources cited in the references. Secondary data used for bibliometric context were obtained through the Scopus database (search conducted May 2025). These sources are available via the cited databases subject to institutional access rights.

### Ethics Statement
This study involved no collection of primary data from human participants. All case evidence was drawn from publicly available organizational documents, press releases, and public sector reports. Formal ethics review was not required.

---

**Draft v1.1 | Word count: approximately 13,200 words (body text, revised)**
**Target journal (primary): Telematics and Informatics (IF 7.6, Elsevier)**
**Target journal (secondary): Information & Management (IF 8.2) / Computers in Human Behavior (IF 9.9)**
**Submission checklist:**
- [ ] Figure 1 replaced with professional vector graphic (300 dpi TIFF/EPS)
- [ ] All [verify bibliographic details] references independently confirmed
- [ ] All [citation needed] items resolved or removed
- [ ] All [case evidence needed] items verified or qualified further
- [ ] Author information completed
- [ ] Word count confirmed against target journal limit
- [ ] Reference format verified against target journal style guide (APA 7th / Vancouver)
- [ ] Cover letter prepared
- [ ] English language proofread by native speaker or professional service
