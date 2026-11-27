# Daily Paper Digest — 2026-11-27 (Friday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · HuggingFace | Agent · Harness · Finance |

> **주의**: 오늘(2026-11-27) 이 환경에서 HuggingFace, arXiv, OpenReview, Semantic Scholar API에 대한 직접 접근이 차단되어 있습니다.
> 웹 검색을 통해 수집된 논문 목록이며, 일부 논문은 arXiv 프리프린트 단계이거나 워크숍 논문일 수 있습니다.
> 각 논문의 최종 게재 상태는 공식 학회 사이트에서 확인해 주세요.

**43 papers** (Agent · Harness · Finance 카테고리별 정리, 중복 제외)

---

## Agent  (17)

### AAAI

- **[Think, Speak, Decide: Language-Augmented MARL for Economic Decision-Making](https://arxiv.org/search/?query=Think+Speak+Decide+MARL+Economic)**
  - **AAAI 2026**
  - 언어 모델을 강화학습 에이전트에 통합해 경제적 의사결정을 개선하는 멀티에이전트 강화학습 프레임워크.

### NeurIPS

- **[GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators](https://arxiv.org/search/?query=GenEnv+LLM+Agents+Environment+Simulators)**
  - **NeurIPS 2026**
  - LLM 에이전트와 환경 시뮬레이터가 난이도에 맞춰 함께 진화하는 공진화(co-evolution) 프레임워크.

- **[SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/search/?query=SkillsBench+Agent+Skills+Diverse+Tasks)**
  - **NeurIPS 2026**
  - 다양한 태스크에 걸쳐 에이전트 스킬의 범용성을 평가하는 벤치마크.

- **[ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](https://arxiv.org/abs/2609.19644)**
  - **NeurIPS 2026 Workshop**
  - 자율 AI를 통해 인간 지식의 프론티어를 개척하는 과학 에이전트 시스템.

### ICML

- **[Can Harness Optimization Improve Agents? Generalizable Gains Versus Evaluation Noise](https://openreview.net/forum?id=Ri0rU3rPOS)**
  - **ICML 2025** · OpenReview
  - 하니스 최적화 방법(프롬프트, 툴, 메모리, 런타임 제어 수정)의 성과가 평가 노이즈와 구별 가능한지 분석.

- **[AURA-Eval: Evaluation Framework for Acting Under Risk Awareness in LLM Agent Trajectories](https://openreview.net/forum?id=9XfH1iAA4W)**
  - **ICML 2025** · OpenReview
  - LLM 에이전트가 위험을 인지하고 어떻게 반응하는지 평가하는 프레임워크.

### ICLR

- **[Terminal-Bench: Benchmarking Terminal Tasks for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2026/file/444a3737adaee10d86ad2ef5f74468e6-Paper-Conference.pdf)**
  - **ICLR 2026**
  - Harbor 하니스 기반으로 Claude Code, Codex CLI, OpenHands 등 에이전트의 터미널 태스크 수행 능력 평가. 프론티어 모델도 65% 미만 달성.

- **[Agent Systems with Harness Engineering](https://github.com/RUCAIBox/awesome-agent-harness)**
  - **ICLR 2026**
  - 하니스 엔지니어링을 통한 에이전트 시스템 설계 원칙과 방법론 제시.

- **[When Agents Fail: Model or Harness--Who's to Blame?](https://arxiv.org/abs/2610.32483)**
  - **ICLR 2026** (관련 논문)
  - 에이전트 실패 시 기반 모델과 하니스 중 어느 쪽에 책임이 있는지 분석하는 귀인(attribution) 프레임워크.

- **[Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives](https://arxiv.org/abs/2609.38912)**
  - **ICLR 2026** (관련 논문)
  - 테스트 시점에 재사용 가능한 프리미티브로 태스크별 에이전트 하니스를 조합하는 방법.

### CVPR

- **[SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_SAGE_Scalable_Agentic_3D_Scene_Generation_for_Embodied_AI_CVPR_2026_paper.html)**
  - **CVPR 2026**
  - 체화 AI 훈련을 위해 레이아웃/오브젝트 생성기와 품질 비평기를 결합한 에이전트 기반 3D 씬 생성 프레임워크.

- **[Think Twice, Act Once: Verifier-Guided Action Selection For Embodied Agents](https://openaccess.thecvf.com/content/CVPR2026F/papers/Singhi_Think_Twice_Act_Once_Verifier-Guided_Action_Selection_For_Embodied_Agents_CVPRF_2026_paper.pdf)**
  - **CVPR 2026**
  - MLLM 기반 체화 에이전트가 행동 실행 전 검증 단계를 거쳐 최고 점수 행동만 실행하도록 하는 테스트 타임 검증 방법.

- **[AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://cvpr.thecvf.com/virtual/2026/poster/36429)**
  - **CVPR 2026**
  - 위험 지시에 대한 체화 에이전트의 안전성을 평가하는 벤치마크.

- **[RoboAgent: Chaining Basic Capabilities for Embodied Task Planning](https://cvpr.thecvf.com/virtual/2026/poster/39291)**
  - **CVPR 2026**
  - 기본 비전-언어 서브 캐퍼빌리티를 체인으로 연결하는 체화 태스크 플래닝 에이전트.

### KDD

- **[MALLES: Multi-Agent LLM Economic Sandbox with Consumer Preference Alignment](https://arxiv.org/search/?query=MALLES+Multi-Agent+LLM+Economic+Sandbox)**
  - **KDD 2026**
  - 소비자 선호도 정렬이 가능한 멀티에이전트 LLM 경제 샌드박스 플랫폼.

- **[FactorMiner: Self-Evolving Agent for Alpha Factor Discovery](https://arxiv.org/search/?query=FactorMiner+Self-Evolving+Agent+Alpha+Factor)**
  - **KDD 2026**
  - 알파 팩터 발굴을 위한 자기진화 에이전트 시스템.

### HuggingFace

- **[Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](https://huggingface.co/papers)**
  - **HuggingFace Daily Papers** · `2026-11-24`
  - 프론티어 모델을 정책으로 활용하는 체화 하니스의 동작 원리 이해를 위한 연구.

---

## Harness  (12)

### NeurIPS

- **[AutoSaddler: Automatic Harness Optimization](https://www.paperdigest.org/2026/10/neurips-2026-papers-highlights/)**
  - **NeurIPS 2026**
  - 에이전트 하니스를 자동으로 최적화하는 프레임워크. 금융 도메인에 특화되지는 않은 범용 접근.

### ICLR

- **[Harness-Bench: Evaluating Agent Harnesses across Models and Realistic Workflows](https://arxiv.org/abs/2605.27922)**
  - **ICLR 2026** (관련 논문)
  - 다양한 모델과 실제 워크플로우에 걸쳐 에이전트 하니스를 평가하는 종합 벤치마크.

- **[General Agent Evaluation (Exgentic)](https://iclr.cc/virtual/2026/10016363)**
  - **ICLR 2026**
  - 임의의 범용 에이전트가 임의의 백본 모델로 모든 벤치마크를 실행할 수 있는 통합 평가 하니스 + 오픈 리더보드 제공.

### ICML

- **[VeRO: A Harness for Agents to Optimize Agents](https://arxiv.org/abs/2602.22480)**
  - **ICML 2026**
  - 에이전트가 다른 에이전트를 최적화하기 위한 하니스 프레임워크.

- **[Rethinking the Evaluation of Harness Evolution for Agents](https://openreview.net/forum?id=QDdWiaNkk2)**
  - **ICML 2025** · OpenReview
  - 에이전트 하니스 진화의 평가 프로토콜에 존재하는 두 가지 근본적인 문제를 재검토.

- **[The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules](https://arxiv.org/abs/2611.06116)**
  - **arXiv 2026-11** (ICML/ICLR 관련)
  - 6개 모델을 대상으로 직접 API와 3개 스캐폴드 하에서 금융 규정 준수를 측정. 스캐폴드가 준수 분산의 단 0.5%만 설명한다는 발견.

### KDD

- **[Harness Choice as a Hidden Variable in Coding-Agent Evaluation](https://kdd-eval-workshop.github.io/agenticai-evaluation-kdd2026/)**
  - **KDD 2026 Workshop** (Agentic AI Evaluation)
  - 코딩 에이전트 평가에서 하니스 선택이 숨겨진 변수로 작용해 결과에 영향을 미침을 분석.

### HuggingFace

- **[QuantHarness: Reliable Before Profitable — Governing Financial Strategy Development with LLM Agents](https://arxiv.org/abs/2610.26101)**
  - **HuggingFace** · `2026-10`
  - 금융 전략 개발에서 수익성보다 신뢰성을 먼저 보장하기 위한 LLM 에이전트 거버넌스 하니스. NeurIPS 2026 Agenthon 워크숍 포스터.

- **[Code as Agent Harness](https://huggingface.co/papers/2605.18747)**
  - **HuggingFace Daily Papers** (Paper of the Day)
  - 코드 자체를 에이전트 하니스로 활용하는 패러다임 제안.

- **[HARBOR: Automated Harness Optimization](https://huggingface.co/papers)**
  - **HuggingFace**
  - 자동화된 하니스 최적화. ITBench SRE, EnterpriseOps-Gym ITSM, AutomationBench Finance에서 하니스 진화로 전체 성능 20-35%p 향상.

- **[Replayable Financial Agents: Determinism-Faithfulness Assurance Harness](https://huggingface.co/papers)**
  - **HuggingFace**
  - 툴 사용 LLM 금융 에이전트를 위한 결정론적 재현 가능성 보증 하니스.

- **[AutoPILOT: A Visual Agent Harness for Real-Time Gameplay](https://huggingface.co/papers)**
  - **HuggingFace Daily Papers** · `2026-11-24`
  - 실시간 게임플레이를 위한 시각적 에이전트 하니스.

- **[Bound Together: Composing Finance Agent Harnesses from Best-of-Breed Parts](https://www.agenthon.net/)**
  - **NeurIPS 2026 Agenthon Workshop**
  - 최고 성능 컴포넌트들을 조합해 금융 에이전트 하니스를 구성하는 방법론.

---

## Finance  (21)

### AAAI

- **[Language Models and Logic Programs for Trustworthy Tax Reasoning](https://arxiv.org/search/?query=Language+Models+Logic+Programs+Trustworthy+Tax+Reasoning)**
  - **AAAI 2026**
  - 세금 추론의 신뢰성을 높이기 위해 언어 모델과 논리 프로그래밍을 결합한 하이브리드 접근법.

### NeurIPS

- **[FinVerify: A Verification Framework for Financial Agents](https://arxiv.org/abs/2611.20423)**
  - **NeurIPS 2026 Workshop** (Who Verifies the Agents?)
  - 금융 에이전트의 수치 클레임 검증을 위한 증거 기반 검증 게이트. 5범주 오류 분류 체계 적용. Agent Finance Reasoning 풀에서 정밀도를 46.8% → 75.2%로 향상.

- **[BankerToolBench: Evaluating AI Agents in End-to-End Investment Banking Workflows](https://arxiv.org/search/?query=BankerToolBench+Investment+Banking+Workflows)**
  - **NeurIPS 2026**
  - 투자은행 엔드투엔드 워크플로우에서 AI 에이전트를 평가하는 벤치마크.

- **[PRISM: Prompt-Refined In-Context System Modeling for Financial Retrieval](https://scale-icml-2026.github.io/accepted_papers.html)**
  - **NeurIPS 2026 CLEA Workshop** (Continual Learning for Enterprise AI)
  - 금융 문서 검색을 위한 훈련 불필요 멀티에이전트 시스템. FinanceBench 등 평가.

### ICML

- **[Position: Evaluating LLMs in Finance Requires Explicit Bias Considerations](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)**
  - **ICML 2026** (Position Track)
  - 금융 분야 LLM 평가에서 편향(bias)을 명시적으로 고려해야 한다는 포지션 페이퍼. 유효성 프레임워크와 편향 진단 체크리스트 제안.

- **[Hybrid Financial Analysis Agent with RAG and Text Mining](https://openreview.net/forum?id=jGe6fFmsDg)**
  - **ICML 2025** · OpenReview
  - RAG, 금융 텍스트 마이닝, 실시간 시장 데이터, 뉴스 감성 분류기를 LangGraph 오케스트레이션으로 통합한 하이브리드 금융 분석 에이전트.

- **[ARTE: Agentic Refinement through Trade Execution for High-Frequency Trading Strategy Discovery](https://openreview.net/forum?id=VisvXioWmG)**
  - **ICML 2025** · OpenReview
  - 틱 단위 거래/호가 데이터를 활용한 고빈도 거래 전략 발굴을 위한 에이전트 기반 정제 시스템.

- **[TradingArena: A Market-Making Benchmark for Ranking, Diagnosing, and Steering LLM Behavior](https://openreview.net/forum?id=6VObvVwaGZ)**
  - **ICML 2025** · OpenReview
  - 에이전트 성능과 행동을 함께 측정하는 시장조성자(market-making) 벤치마크.

- **[ParaFusionBench: Unified Benchmark for Cross-Paradigm Fusion in Factor Mining and Trading Decision-Making](https://openreview.net/forum?id=nqb5xH3QuC)**
  - **ICML 2025** · OpenReview · *Xiaozhao Zeng, Fan Liu, Yang Ni et al.* (HKUST)
  - 팩터 마이닝과 트레이딩 의사결정의 4가지 패러다임 교차 융합을 위한 통합 벤치마크.

- **[FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors](https://openreview.net/forum?id=RKKGxm7O4L)**
  - **ICML 2025** · OpenReview
  - 차등 프라이버시 하에서 실세계 사전 지식을 활용해 금융 감사 벤치마크를 구축하는 방법론.

- **[PortfolioRouter: Consequence-Aware Multi-Task Routing for Portfolio Agents](https://openreview.net/forum?id=My6dyV7ecS)**
  - **ICML 2025** · OpenReview
  - 라우팅 오류의 금융 비용을 고려하는 결과 인식 멀티태스크 라우팅으로 포트폴리오 에이전트 의사결정 개선.

### ICLR

- **[FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning](https://github.com/jiaxianyan/icml-iclr-2026-agent-papers)**
  - **ICLR 2026**
  - 금융 검색 및 추론에 대한 현실적이고 전문가 수준의 평가 벤치마크.

### KDD

- **[FinWorld: Open-Source Platform for End-to-End Financial AI Research](https://arxiv.org/search/?query=FinWorld+Financial+AI+Research+Platform)**
  - **KDD 2026** · *Wentao Zhang, Yilei Zhao, Chuqiao Zong, Xinrun Wang, Bo An*
  - LLM 훈련 및 배포 지원을 포함한 엔드투엔드 금융 AI 연구 오픈소스 플랫폼.

- **[CNFinBench: Agentic Execution and Compliance Drift Benchmark for Finance](https://www.paperdigest.org/2026/08/kdd-2026-papers-highlights/)**
  - **KDD 2026**
  - 에이전트 실행과 규정 준수 드리프트를 평가하는 금융 벤치마크.

- **[Can LLM-based Financial Investing Strategies Outperform The Market in Long Run? (FINSABER)](https://www.paperdigest.org/2026/08/kdd-2026-papers-highlights/)**
  - **KDD 2026**
  - 타이밍 기반 LLM 투자 전략을 장기간, 더 넓은 종목 범위에서 평가하는 백테스팅 프레임워크 FINSABER 제안.

- **[Chat2Trade: Automating Financial RFQ Parsing with Fine-Tuned LLMs](https://github.com/EFundAI/Awesome-FinFMs)**
  - **KDD 2026**
  - 파인튜닝된 LLM으로 금융 RFQ(Request for Quote) 파싱을 자동화하는 시스템.

- **[AlphaMaster: Alpha Discovery with LLM Agents](https://github.com/EFundAI/Awesome-FinFMs)**
  - **KDD 2026**
  - LLM 에이전트를 활용한 알파 팩터 발굴 시스템.

- **[Compliance-to-Code: Enhancing Financial Compliance Checking via Code Generation](https://arxiv.org/search/?query=Compliance-to-Code+Financial+Compliance)**
  - **KDD 2026**
  - 코드 생성을 통해 금융 규정 준수 확인을 강화하는 방법론.

### HuggingFace

- **[FinanceHarness: Autonomous Financial Deep Research Framework](https://huggingface.co/papers/2607.27853)**
  - **HuggingFace** · arXiv:2607.27853
  - 금융 딥리서치를 자동화하는 프레임워크. FinanceGym(논문 주도 연구 질문 + 루브릭)과 결합된 에이전트 실행 루프 포함.

- **[Herculean: An Agentic Benchmark for Financial Intelligence](https://arxiv.org/abs/2605.14355)**
  - **HuggingFace** · arXiv:2605.14355
  - Claude Agent SDK를 하니스 어댑터로 활용하는 금융 인텔리전스 에이전트 벤치마크.

- **[AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests](https://arxiv.org/abs/2611.04813)**
  - **HuggingFace** · arXiv:2611.04813
  - 실세계 요청에서 다양한 태스크에 걸쳐 금융 에이전트를 평가하는 종합 벤치마크.

- **[BigFinanceBench: A Workflow-Grounded Benchmark for Financial-Research Agents](https://arxiv.org/abs/2606.03829)**
  - **HuggingFace** · arXiv:2606.03829
  - 금융 리서치 에이전트를 위한 워크플로우 기반 대규모 벤치마크.

- **[AStockArena: Beyond Returns — Can We Entrust Real Capital to Financial Agents?](https://arxiv.org/abs/2611.00515)**
  - **HuggingFace** · arXiv:2611.00515
  - 실제 자본을 금융 에이전트의 의사결정에 맡길 수 있는지 평가하는 아레나 스타일 벤치마크.

---

## 참고 출처

- [Paper Digest: NeurIPS 2026](https://www.paperdigest.org/2026/10/neurips-2026-papers-highlights/)
- [Paper Digest: ICML 2026](https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/)
- [Paper Digest: KDD 2026](https://www.paperdigest.org/2026/08/kdd-2026-papers-highlights/)
- [ICLR 2026 Oral Papers (GitHub)](https://github.com/XinyuLiuCs/iclr2026-oral-papers/blob/main/paper-list.md)
- [ICLR 2026 Agent Papers (GitHub)](https://github.com/jiaxianyan/icml-iclr-2026-agent-papers/blob/main/conferences/iclr-2026.zh-CN.md)
- [Awesome Agent Harness (RUCAIBox)](https://github.com/RUCAIBox/awesome-agent-harness)
- [Awesome FinFMs (EFundAI)](https://github.com/EFundAI/Awesome-FinFMs)
- [AI Agent Papers - Finance (GitHub)](https://github.com/masamasa59/ai-agent-papers/blob/main/applications/domain/finance-agents.md)
- [CVPR 2026 Open Access](https://openaccess.thecvf.com/CVPR2026)
- [NeurIPS 2026 Agenthon Workshop](https://www.agenthon.net/)
- [KDD Workshop on Agentic AI Evaluation](https://kdd-eval-workshop.github.io/agenticai-evaluation-kdd2026/)
- [FinVerify arXiv:2611.20423](https://arxiv.org/abs/2611.20423)
- [FinanceHarness arXiv:2607.27853](https://huggingface.co/papers/2607.27853)
- [AgenticFinBench arXiv:2611.04813](https://arxiv.org/abs/2611.04813)
- [BigFinanceBench arXiv:2606.03829](https://arxiv.org/abs/2606.03829)
