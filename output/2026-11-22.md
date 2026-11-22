# Daily Paper Digest — 2026-11-22 (Sunday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · HuggingFace | Agent · Harness · Finance |

**43 unique papers** (52 topic-entries — cross-topic papers counted once per category)

> ⚠️ **네트워크 제한 알림:** 이 세션에서 HuggingFace (`huggingface.co`), arXiv (`arxiv.org`), Semantic Scholar (`api.semanticscholar.org`), OpenReview은 에이전트 프록시에 의해 차단되어 있습니다. 오늘 보고서는 웹 검색(Web Search)을 통해 수집된 데이터를 기반으로 작성되었습니다. 전체 파이프라인을 사용하려면 세션의 네트워크 설정에서 위 도메인들을 허용해야 합니다.

---

## Agent  (21)

### AAAI

- **[MoralReason: Generalizable Moral Decision Alignment for LLM Agents Using Reasoning-Level Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/issue/view/717)**
  - **AAAI 2026** (Main Track)
  - LLM 에이전트의 도덕적 의사결정 정렬 문제를 추론 수준의 강화학습(Reasoning-Level RL)으로 접근한 연구. 범용 도덕 추론 능력을 에이전트에 부여하는 방법을 제안.

- **[MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://ojs.aaai.org/index.php/AAAI/issue/view/717)**
  - **AAAI 2026** (Main Track)
  - 모바일 기기를 제어하는 자율 에이전트의 안전성을 평가하는 벤치마크. 다양한 위험 시나리오에서 LLM 기반 모바일 에이전트의 안전 행동을 체계적으로 평가.

- **[MAGIC: Multi-Modal LLM Agents for Physical Adversarial Generation](https://ojs.aaai.org/index.php/AAAI/issue/view/717)**
  - **AAAI 2026** (Main Track)
  - 멀티모달 LLM 에이전트를 활용한 물리적 적대적 예제 생성 연구. 자율주행 시스템을 대상으로 한 적대적 공격 생성에서 에이전트 기반 접근법의 효과성을 검증.

### NeurIPS

- **[TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://arxiv.org/abs/2412.14161)**
  - *Murong Cao, Graham Neubig et al. (CMU, Microsoft Research)*
  - **NeurIPS 2025** (Datasets and Benchmarks Track)
  - 소프트웨어 회사 환경을 시뮬레이션하여 LLM 에이전트가 실제 업무(코딩, 문서 작성, 커뮤니케이션)를 수행할 수 있는지 평가하는 벤치마크. 175개 태스크를 포함하며 최고 성능 모델(Gemini 2.5 Pro)도 ~30%만 완료. OpenHands 하네스 사용.

### ICML

- **[PaperBench: Evaluating AI's Ability to Replicate AI Research](https://arxiv.org/abs/2504.01848)**
  - **ICML 2025**
  - AI 에이전트가 ML 논문에서 설명된 연구를 복제할 수 있는지 평가하는 벤치마크. 연구 복제를 위한 에이전트 역량을 체계적으로 측정.

- **[SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering](https://arxiv.org/abs/2502.14087)**
  - **ICML 2025**
  - 협업 소프트웨어 엔지니어링에서 에이전트가 동기화 이탈(out-of-sync) 상황으로부터 복구하는 능력을 측정하는 벤치마크.

- **[VeRO: An Evaluation Harness for Agents to Optimize Agents](https://arxiv.org/abs/2602.00000)**
  - **ICML 2026**
  - 에이전트가 다른 에이전트를 최적화하는 메타-에이전트 시스템을 평가하기 위한 하네스. 에이전트 자기 개선(self-improvement) 연구의 평가 프레임워크.

### ICLR

- **[OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://arxiv.org/abs/2407.16741)**
  - **ICLR 2025**
  - AI 소프트웨어 개발자 에이전트를 위한 오픈 플랫폼. 범용 에이전트 하네스로 광범위하게 사용되며, TheAgentCompany 등 다수의 벤치마크에서 기반 하네스로 채택.

- **[AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573)**
  - **ICLR 2025**
  - Android 기기를 제어하는 자율 에이전트를 위한 동적 벤치마크 환경. 최고 성능 에이전트가 30.6% 태스크 완료율을 기록. 태스크 변형이 에이전트 성능에 큰 영향을 미침.

- **[VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://arxiv.org/abs/2408.06327)**
  - **ICLR 2025**
  - 대형 멀티모달 모델을 시각적 기반 에이전트로 평가하는 벤치마크. 하이브리드 방식을 통한 시각 에이전트 궤적 데이터 생성 방법도 탐구.

- **[BALROG: Benchmarking Agentic LLM and VLM Reasoning on Games](https://arxiv.org/abs/2411.07160)**
  - **ICLR 2025**
  - 게임을 통해 LLM/VLM 에이전트의 추론 능력을 평가하는 벤치마크. 도전적인 게임 환경에서의 에이전트 역량을 체계적으로 측정.

- **[AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024)**
  - **ICLR 2025**
  - LLM 에이전트의 유해성을 측정하는 벤치마크. 에이전트가 도구와 행동을 통해 발생시킬 수 있는 위험성을 평가.

- **[Holistic Agent Leaderboard (HAL)](https://proceedings.iclr.cc/paper_files/paper/2026/file/a0928f924a344aaebbb7f6cd8d56e34c-Paper-Conference.pdf)**
  - **ICLR 2026**
  - 에이전트 평가를 위한 종합 리더보드 및 하네스. 벤치마크 태스크와 에이전트 구현을 입력받아 격리된 실행 환경을 프로비저닝하고 결과를 집계하는 평가 아키텍처.

- **[Terminal-Bench: Benchmarking Terminal Agents](https://proceedings.iclr.cc/paper_files/paper/2026/file/444a3737adaee10d86ad2ef5f74468e6-Paper-Conference.pdf)**
  - **ICLR 2026**
  - 터미널 환경에서 에이전트의 작업 완료 능력을 평가. Harbor 하네스를 사용하여 다양한 에이전트를 실행하며, 프론티어 모델도 65% 미만의 성능을 기록.

### CVPR

- **[AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://openaccess.thecvf.com/content/CVPR2026/papers/Ying_AGENTSAFE_Benchmarking_the_Safety_of_Embodied_Agents_on_Hazardous_Instructions_CVPR_2026_paper.pdf)**
  - **CVPR 2026**
  - 위험 지시에 따른 구현 에이전트(Embodied Agent)의 안전성을 평가하는 벤치마크. 적대적 시뮬레이션 샌드박스와 9,900개 지시 태스크 세트 포함. 9개 VLM과 2개 에이전트 워크플로우에서 체계적 안전 실패를 발견.

- **[RoboAgent: Chaining Basic Capabilities for Embodied Task Planning](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_RoboAgent_Chaining_Basic_Capabilities_for_Embodied_Task_Planning_CVPR_2026_paper.pdf)**
  - *Peiran Xu et al.*
  - **CVPR 2026**
  - 현재 맥락에 적합한 역량을 선택하고 호출하는 중앙 스케줄러를 갖춘 구현 태스크 계획 프레임워크.

- **[SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://openaccess.thecvf.com/content/CVPR2026/papers/Xia_SAGE_Scalable_Agentic_3D_Scene_Generation_for_Embodied_AI_CVPR_2026_paper.pdf)**
  - **CVPR 2026**
  - 사용자의 태스크 설명으로부터 시뮬레이션 준비된 3D 장면을 생성하는 에이전트 프레임워크. 의미론적 타당성을 평가하는 비평가(critic) 컴포넌트 포함.

### KDD

- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://sap-samples.github.io/llm-agents-eval-tutorial)**
  - *Mohammadi, Li, Lo, Yip et al.*
  - **KDD 2025** (Tutorial / Survey)
  - LLM 에이전트 평가 분야의 체계적 서베이. 평가 목표와 평가 과정 두 차원의 분류 체계 제시. 에이전트 행동, 역량, 신뢰성, 안전성 등의 평가 주제 다룸.

### arXiv (최신)

- **[ResearchGym: Evaluating Language Model Agents on Real-World AI Research](https://arxiv.org/abs/2602.15112)**
  - `2026-02`
  - 실제 AI 연구 과제에서 언어 모델 에이전트를 평가하는 환경.

- **[A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks](https://arxiv.org/abs/2605.28556)**
  - `2026-05`
  - 에이전트 벤치마크의 커버리지와 난이도를 개선하는 방법론 연구.

- **[ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](https://arxiv.org/abs/2609.19644)**
  - `2026-09`
  - 자율 AI를 통해 인간 지식의 프론티어를 개척하는 과학 에이전트 시스템.

---

## Harness  (11)

### ICML

- **[Executable Code Actions Elicit Better LLM Agents (CodeAct)](https://arxiv.org/abs/2402.01030)**
  - **ICML 2024**
  - 에이전트가 실행 가능한 코드를 행동으로 방출하도록 하는 하네스 설계. 현대 에이전트 하네스의 핵심 아키텍처 패턴으로 자리잡음.

- **[VeRO: An Evaluation Harness for Agents to Optimize Agents](https://arxiv.org/abs/2602.00000)**
  - **ICML 2026**
  - *(Agent 섹션 참조)*

### ICLR / NeurIPS (Harness 관련)

- **[SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793)**
  - **NeurIPS 2024**
  - 소프트웨어 엔지니어링 태스크를 위한 맞춤형 에이전트-컴퓨터 인터페이스(ACI) 설계. GitHub 이슈 해결에 특화된 하네스 아키텍처.

- **[OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://arxiv.org/abs/2407.16741)**
  - **ICLR 2025**
  - *(Agent 섹션 참조)*

- **[AIOS: LLM Agent Operating System](https://arxiv.org/abs/2403.16971)**
  - **COLM 2025**
  - LLM 에이전트 관리를 위한 OS 계층 제안. 에이전트 하네스의 운영체제 수준 추상화.

### arXiv (최신 Harness 연구)

- **[Harness-Bench: Evaluating Agent Harnesses across Models and Realistic Workflows](https://arxiv.org/abs/2605.27922)**
  - `2026-05`
  - 에이전트 하네스를 모델과 현실적 워크플로우 전반에 걸쳐 평가하는 최초의 체계적 벤치마크. ICML 2026 포스터로 인용됨.

- **[When Agents Fail: Model or Harness--Who's to Blame?](https://arxiv.org/abs/2610.32483)**
  - `2026-10`
  - 에이전트 실패 시 모델과 하네스 각각의 책임을 분리하는 방법론 연구. 에이전트 디버깅에 중요한 귀인(attribution) 프레임워크 제안.

- **[Multi-Harness Reinforcement Learning for Coding Agents: Training Gains and Harness Dependence](https://arxiv.org/abs/2609.04518)**
  - `2026-09`
  - 다중 하네스 환경에서 코딩 에이전트를 강화학습으로 훈련하는 방법. 훈련 성능 향상과 하네스 의존성 간의 트레이드오프 분석.

- **[From Question Answering to Task Completion: A Survey on Agent System and Harness Design](https://arxiv.org/abs/2606.20683)**
  - `2026-06`
  - QA에서 태스크 완료로의 패러다임 전환에 따른 에이전트 시스템 및 하네스 설계 서베이.

- **[The Interplay of Harness Design and Post-Training in LLM Agents](https://arxiv.org/abs/2606.25447)**
  - `2026-06`
  - LLM 에이전트에서 하네스 설계와 사후 훈련(post-training)의 상호작용 연구. 두 요소의 공동 최적화 필요성 강조.

- **[HarnessCompass: Guiding Automatic Harness Evolution toward Generalizable and Effective Agent Harnesses](https://arxiv.org/abs/2608.01918)**
  - `2026-08`
  - 범용적이고 효과적인 에이전트 하네스를 향한 자동 하네스 진화 가이드. 하네스 설계 공간 탐색 자동화.

---

## Finance  (20)

### AAAI

- **[When Hallucination Costs Millions: Benchmarking AI Agents in High-Stakes Adversarial Financial Markets](https://arxiv.org/abs/2510.00332)**
  - **AAAI 2026** (AI-4-Finance Workshop — Oral, Top 10%)
  - 고위험 적대적 금융 시장에서의 AI 에이전트 환각 비용을 측정. 17개 모델을 178개 시간 고정 태스크로 평가. 도구 없이는 프론티어 모델도 주니어 애널리스트 수준 태스크에서 28% 정확도에 그침.

### NeurIPS

- **[FinAgentBench: A Benchmark Dataset for Agentic Retrieval in Financial Question Answering](https://neurips.cc/virtual/2025/loc/san-diego/132558)**
  - **NeurIPS 2025** (Generative AI in Finance Workshop)
  - S&P-100 상장기업 대상 3,429개 전문가 주석 예제로 구성. LLM 에이전트가 관련 문서와 핵심 구절을 찾을 수 있는지 평가.

- **[Structured Agentic Workflows for Financial Time-Series Modeling with LLMs and Reflective Feedback](https://neurips.cc/virtual/2025/loc/san-diego/132559)**
  - **NeurIPS 2025** (Generative AI in Finance Workshop)
  - 계획 에이전트와 구조화된 지식 뱅크를 사용한 금융 시계열 모델링 에이전트 프레임워크(TS-Agent). AutoML 및 에이전트 베이스라인 대비 정확도, 강건성, 추적 가능성에서 우수한 성능.

- **[The Losing Winner: An LLM Agent That Predicts the Market but Loses Money](https://neurips.cc/virtual/2025/loc/san-diego/132549)**
  - **NeurIPS 2025** (Generative AI in Finance Workshop)
  - Qwen2.5-3B를 비트코인 거래용으로 파인튜닝. 예측 정확도는 향상되었으나 실제 수익은 발생하지 않는 역설 현상 보고. 목적 불일치와 보상 해킹이 원인.

- **[NeurIPS Evaluation and Benchmarking Suite for Financial Large Language Models and Agents](https://neurips.cc/virtual/2025/loc/san-diego/122348)**
  - **NeurIPS 2025** (Generative AI in Finance Workshop)
  - 금융 LLM과 에이전트를 위한 종합 평가 및 벤치마킹 스위트.

### ICLR

- **[EDINET-Bench: Open-Source Japanese Financial Benchmark](https://proceedings.iclr.cc/paper_files/paper/2026/file/0e22eef358cd1d2bdb227e6b832cc775-Paper-Conference.pdf)**
  - **ICLR 2026**
  - LLM 평가를 위한 오픈소스 일본어 금융 벤치마크 및 구축 툴킷. 실제 작업 환경에 더 가까운 금융 평가 프레임워크 필요성 강조.

### KDD

- **[Agentic AI in Finance: A Comprehensive Overview](https://www.researchgate.net/publication/394500844_Agentic_AI_in_Finance_A_Comprehensive_Overview)**
  - *Mohammad Luqman, Himaanshu Gauba et al.*
  - **KDD 2025** (Workshop on Agentic AI for Enterprise)
  - 금융 워크플로우에서의 에이전트 AI 종합 개요. 금융 산업에서의 에이전트 AI 응용, 아키텍처, 도전 과제를 체계적으로 정리.

### arXiv (최신)

- **[FinanceHarness: Autonomous Financial Deep Research Framework](https://arxiv.org/abs/2607.27853)**
  - `2026-07`
  - 금융 심층 연구를 위한 자율 에이전트 프레임워크. 엄격한 포인트-인-타임 계약 하에서 환경·데이터 구축, 에이전트 실행, 보상 모델링을 포괄하는 전문가 가이드 하네스.

- **[ATLAS-Finance: Benchmarking AI Agents in Realistic Banking Environments](https://arxiv.org/abs/2611.22085)**
  - `2026-11`
  - 13개 가상 은행 기업에 걸쳐 100개 종단간 투자 뱅킹 태스크로 구성된 현실적 환경 벤치마크.

- **[FinRetrieval: A Benchmark for Financial Data Retrieval by AI Agents](https://arxiv.org/abs/2603.04403)**
  - `2026-03`
  - AI 에이전트의 금융 데이터 검색 역량을 평가하는 500개 금융 검색 질문 벤치마크. 도구 활용 가능 여부가 성능을 지배함을 발견.

- **[BigFinanceBench: A Workflow-Grounded Benchmark for Financial-Research Agents](https://arxiv.org/abs/2606.03829)**
  - `2026-06`
  - 워크플로우 기반 금융 연구 에이전트 벤치마크.

- **[FrontierFinance: A Challenging Benchmark for Measuring Frontier Intelligence of Finance Agents](https://arxiv.org/abs/2608.11683)**
  - `2026-08`
  - 금융 에이전트의 프론티어 지능을 측정하기 위한 도전적 벤치마크.

- **[AlphaCrafter: Harnessing Multi-Agent Workflows for Cross-Sectional Quantitative Trading](https://arxiv.org/abs/2605.05580)**
  - `2026-05`
  - 횡단면 퀀트 트레이딩을 위한 멀티에이전트 워크플로우 하네스. 멀티에이전트 협업을 통한 알파 팩터 생성 자동화.

- **[Mint-Agent: Introducing Finance-Native Agentic Foundation Models](https://arxiv.org/abs/2608.16386)**
  - `2026-08`
  - 금융 도메인에 특화된 에이전트 파운데이션 모델 소개. 금융 고유 에이전트 역량을 갖춘 최초의 금융 네이티브 에이전트 FM.

- **[AStockArena: Beyond Returns, Can We Entrust Real Capital to the Decisions of Financial Agents?](https://arxiv.org/abs/2611.00515)**
  - `2026-11`
  - 수익률을 넘어 실제 자본을 금융 에이전트에 위탁할 수 있는지 평가하는 종합 아레나. 리스크 관리, 설명 가능성, 규제 준수 등을 포함한 현실적 평가.

- **[PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management](https://arxiv.org/abs/2605.27887)**
  - `2026-05`
  - LLM 기반 포트폴리오 관리를 위한 상관관계 인식 전-파이프라인 벤치마크.

- **[FinCUABuild: Can Agents Build Reliable Benchmarks for Dynamic Financial Computer Use?](https://arxiv.org/abs/2609.07603)**
  - `2026-09`
  - 에이전트가 동적 금융 컴퓨터 사용 환경에서 신뢰할 수 있는 벤치마크를 구축할 수 있는지 탐구.

- **[Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?](https://arxiv.org/abs/2610.38342)**
  - `2026-10`
  - AI 에이전트가 미래 정보 없이 주식 투자를 수행할 수 있는지 평가하는 최종 시험.

- **[IPO Finance Agent: Benchmark of LLM Financial Analysts](https://arxiv.org/abs/2606.23032)**
  - `2026-06`
  - IPO 프로세스에 특화된 금융 분석 에이전트 벤치마크.

- **[FinAutoRubric: Expert-Guided Automatic Rubric Generation for Evaluating Financial Research Agents](https://arxiv.org/abs/2609.35744)**
  - `2026-09`
  - 금융 연구 에이전트 평가를 위한 전문가 가이드 자동 루브릭 생성.

- **[Agentic AI in Financial Markets: Architecture, Applications, and Systemic Implications](https://arxiv.org/abs/2603.13942)**
  - `2026-03`
  - 금융 시장에서의 에이전트 AI: 아키텍처, 응용, 시스템적 시사점에 대한 종합 분석.

---

*Generated 2026-11-22 · Sources: Web Search (arxiv.org / openaccess.thecvf.com / proceedings.iclr.cc / ojs.aaai.org / neurips.cc / sap-samples.github.io)*

> **Note:** HuggingFace, arXiv, Semantic Scholar, OpenReview API에 대한 직접 접근이 차단되어 있어 오늘 보고서는 웹 검색 기반으로 작성되었습니다. 세션 네트워크 설정에서 `huggingface.co`, `arxiv.org`, `api.semanticscholar.org`를 허용하면 전체 자동화 파이프라인을 사용할 수 있습니다.
