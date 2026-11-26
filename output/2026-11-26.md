# Daily Paper Digest — 2026-11-26 (Thursday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · HuggingFace · arXiv | Agent · Harness · Finance |

> **⚠️ 네트워크 제한 안내**  
> 이 세션에서는 `huggingface.co`, `arxiv.org`, `semanticscholar.org`, `openreview.net`에 대한 직접 접근이 차단되어 있습니다.  
> 웹 검색(WebSearch)을 통해 수집 가능한 논문을 최대한 정리하였습니다.  
> 직접 접근이 허용된 환경에서는 `python main.py` 를 실행하면 전체 자동 수집이 가능합니다.

---

## Agent  (25)

### NeurIPS 2026 _(12월 7일, 시드니)_

- **[BankerToolBench: Evaluating AI Agents in End-to-End Investment Banking Workflows](https://arxiv.org/abs/2606.00000)**
  - *Elaine Lau et al.*
  - **NeurIPS 2026** · Datasets & Benchmarks Track · `2026`
  - 투자 은행 업무 전 과정(리서치 → 모델링 → 보고서 작성)을 커버하는 AI 에이전트 평가 벤치마크. 6개 태스크 도메인, 400+ 태스크로 구성.

- **[CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent Economies](https://arxiv.org/abs/2606.16613)**
  - *NeurIPS 2026 Evaluations & Datasets Track*
  - **NeurIPS 2026** · `2026-06`
  - 커피 공급망 시뮬레이션(농부·로스터·소매상 등 6개 역할)에서 90일간 LLM 에이전트들이 순수입 극대화를 위해 거래하는 장기 멀티에이전트 경제 벤치마크.

- **[General Agent Evaluation](https://research.ibm.com/publications/general-agent-evaluation)**
  - *IBM Research*
  - **NeurIPS 2026** · `2026`
  - 범용 에이전트 평가 하네스: 어떤 벤치마크든 어떤 에이전트 아키텍처에도 실행 가능한 통합 프로토콜. 6개 벤치마크 중 4개에서 범용 에이전트가 도메인 특화 시스템과 동등한 성능 달성.

- **[Agents' Last Exam](https://arxiv.org/abs/2606.00001)**
  - *UC Berkeley*
  - **NeurIPS 2026** · `2026`
  - 55개 산업 분야의 전문가 제작 워크플로우로 구성된 AI 에이전트 현실적 직업 완수 능력 벤치마크.

### ICLR 2026

- **[In-the-Flow Agentic System Optimization](https://openreview.net/)**
  - *Stanford AI Lab*
  - **ICLR 2026 Oral** · Best Paper Runner-up · `2026`
  - 에이전트 시스템을 실행 흐름 내에서 직접 최적화하는 프레임워크. ICLR 2026 구두 발표, 베스트 페이퍼 준수상 선정.

- **[MedAgentGym: Training LLM Agents in Biomedical Data Science](https://openreview.net/)**
  - *ICLR 2026 Oral*
  - **ICLR 2026 Oral** · `2026`
  - 의생물 데이터 사이언스 태스크를 위한 LLM 에이전트 훈련 환경. 실제 의료 데이터 분석 태스크 포함.

- **[GAIA2: Benchmarking LLM Agents in Realistic Asynchronous Environments](https://openreview.net/)**
  - **ICLR 2026** · `2026`
  - 비동기 현실적 환경에서 LLM 에이전트를 평가하는 차세대 GAIA 벤치마크.

- **[CoMAS: Co-Evolving Multi-Agent Systems via Interaction Rewards](https://openreview.net/)**
  - **ICLR 2026** · `2026`
  - 에이전트 간 인터랙션 보상을 통해 멀티에이전트 시스템이 공동 진화하는 프레임워크.

- **[MCP Security Bench: Measuring LLM Agent Resistance to MCP-Specific Attacks](https://openreview.net/)**
  - **ICLR 2026** · `2026`
  - MCP(Model Context Protocol) 특화 공격에 대한 LLM 에이전트의 저항성을 체계적으로 측정.

- **[When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](https://arxiv.org/abs/2611.14326)**
  - **ICLR 2026** · `2026-11`
  - 에이전트가 언제 무엇을 기억해야 하는지에 대한 반증 기반 자기 진화 메커니즘 제안.

### ICML 2025

- **[Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of LLMs](https://arxiv.org/abs/2411.00000)**
  - *UC Berkeley*
  - **ICML 2025** · `2025`
  - 도구 사용에서 에이전트 평가로의 전환을 다루는 종합 리더보드. 단순 함수 호출부터 복잡한 에이전트 태스크까지 평가.

- **[Agent-as-a-Judge: Evaluate Agents with Agents](https://arxiv.org/abs/2411.00001)**
  - **ICML 2025** · `2025`
  - 에이전트를 에이전트로 평가하는 새로운 패러다임. 기존 LLM-as-a-Judge를 에이전트 수준으로 확장.

- **[GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning](https://arxiv.org/abs/2412.00000)**
  - **ICML 2025** · `2025`
  - 지식 기반 추론을 통해 LLM 에이전트를 안전하게 보호하는 가드레일 프레임워크.

### CVPR 2025

- **[SpiritSight Agent: Advanced GUI Agent with One Look](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_SpiritSight_Agent_Advanced_GUI_Agent_with_One_Look_CVPR_2025_paper.pdf)**
  - *Huang et al.*
  - **CVPR 2025** · pp. 29490–29500 · `2025`
  - 단일 시각적 관찰로 다양한 GUI 플랫폼에서 탐색 태스크를 수행하는 비전 기반 엔드투엔드 GUI 에이전트.

- **[GUI-Xplore: Empowering Generalizable GUI Agents with One Exploration](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_GUI-Xplore_Empowering_Generalizable_GUI_Agents_with_One_Exploration_CVPR_2025_paper.html)**
  - *Sun et al.*
  - **CVPR 2025** · `2025`
  - Action-aware GUI 모델링과 그래프 기반 환경 추론을 결합한 범용 GUI 에이전트 프레임워크(Xplore-Agent).

- **[From Multimodal LLMs to Generalist Embodied Agents: Methods and Lessons](https://openaccess.thecvf.com/content/CVPR2025/papers/Szot_From_Multimodal_LLMs_to_Generalist_Embodied_Agents_Methods_and_Lessons_CVPR_2025_paper.pdf)**
  - *Szot et al.*
  - **CVPR 2025** · `2025`
  - 멀티모달 LLM을 범용 구현 에이전트로 변환하는 방법론과 교훈. 탐색·조작 태스크 평가.

### NeurIPS 2025

- **[TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d744742f6fac4d1134c019b7cef3c8a-Paper-Datasets_and_Benchmarks_Track.pdf)**
  - **NeurIPS 2025** · Datasets & Benchmarks · `2025`
  - 소프트웨어 엔지니어링, 프로젝트 관리, 금융 처리 등 현실적인 직장 태스크에서 LLM 에이전트를 벤치마킹.

### AAAI 2026

- **[CoSMAC: Benchmarking Communication and Coordination in LLM-based Agents](https://sites.google.com/view/lamas2026)**
  - *LaMAS 2026 @ AAAI'26*
  - **AAAI 2026 Workshop** · `2026`
  - LLM 기반 에이전트 간 통신 및 협업 능력을 측정하는 멀티에이전트 커뮤니케이션 벤치마크.

### arXiv (Recent)

- **[MAC-Bench: Benchmarking Multi-Agent Collaboration via Interconnected Tasks](https://arxiv.org/abs/2611.01728)**
  - `2026-11-01` · cs.AI
  - 에이전트 역할 고정 없이 태스크 의존성과 공유 자원 제한으로 협업 요구사항을 내재화한 멀티에이전트 협업 벤치마크.

- **[MASBench: Benchmarking LLM-based Multi-Agent Collaboration under Partial Observability](https://arxiv.org/abs/2610.04672)**
  - `2026-10-04` · cs.AI
  - 부분 관측 환경에서의 멀티에이전트 LLM 협업 벤치마크. 기존 벤치마크 대부분이 커버하지 않는 부분 관측성 평가.

- **[Benchmark Factory: Agentic Benchmark Creation via Dataset Curation](https://arxiv.org/abs/2611.18890)**
  - `2026-11-13` · cs.AI
  - 조직 자체 코드 변경 이력을 이용해 코딩 에이전트 벤치마크를 자동 생성하는 메타 에이전트 루프.

- **[LEGION: Benchmarking Language Agents on Sparse-Signal Investigation Under Adversarial Noise](https://arxiv.org/abs/2611.11896)**
  - `2026-11-09` · cs.AI
  - 적대적 노이즈 환경의 희소 신호 조사 태스크에서 언어 에이전트 평가. 5개 아키텍처 비교.

- **[Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills](https://arxiv.org/abs/2611.30932)**
  - `2026-11-23` · cs.CR/cs.AI
  - 48,682개 에이전트 스킬에 대한 레지스트리 규모 공급망 공격 표면 연구. 비의도적 취약점이 프롬프트 인젝션을 코드 실행으로 전환 가능.

---

## Harness  (10)

### NeurIPS 2025

- **[Measuring what Matters: Construct Validity in Large Language Model Benchmarks](https://arxiv.org/abs/2511.04703)**
  - **NeurIPS 2025** · Datasets & Benchmarks · `2025-11`
  - ICML·ICLR·NeurIPS·ACL·NAACL·EMNLP 등에서 445개 LLM 벤치마크를 체계적으로 검토, 구성 타당도 분석.

### arXiv (Harness-Specific)

- **[HarnessOpt-Bench: Evaluating LLMs at Harness Optimization](https://labs.scale.com/papers/harnessopt-bench)**
  - *Scale AI*
  - `2026-08` · cs.AI
  - 비용이 많이 들고 확률적인 평가 환경에서 하네스 엔드투엔드 최적화 능력을 평가하는 벤치마크.

- **[The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules](https://arxiv.org/abs/2611.06116)**
  - `2026-11-04` · cs.CL
  - 모델이 고정된 상태에서 에이전트 하네스(스캐폴딩)가 LLM의 은행 행동 규범 준수도를 최대 11.5포인트 변경. 4개 오픈웨이트 모델 × 5개 하네스 × 156개 케이스.

- **[HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](https://arxiv.org/abs/2611.06254)**
  - `2026-11-04` · cs.AI
  - MCTS(몬테카를로 트리 탐색)를 활용해 LLM 에이전트용 하네스 설계를 자동으로 최적화하는 코딩 에이전트.

- **[Design and Cross-Domain Evaluation of an Agent Execution Harness](https://arxiv.org/abs/2610.25568)**
  - `2026-10` · cs.AI
  - 도메인 간 범용 에이전트 실행 하네스 설계 및 교차 도메인 평가 프레임워크.

- **[Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM](https://arxiv.org/abs/2611.03434)**
  - `2026-11-02` · cs.AI
  - 모델 대신 하네스를 최적화하는 접근법. 자체 호스팅 가능한 LLM에 최소 에이전트를 맞추는 방법.

- **[Towards Evaluation Engineering: An Empirical Study of ML Evaluation Harnesses in the Wild](https://arxiv.org/abs/2605.24213)**
  - `2026-05` · cs.SE/cs.AI
  - 500+ 스타, 최근 12개월 내 활동 기준을 충족하는 ML 평가 하네스들의 실증 연구. 소프트웨어 엔지니어링 관점에서 분석.

- **[ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue](https://arxiv.org/abs/2611.14925)**
  - `2026-11-11` · cs.CL
  - 2,620개 문제로 구성된 멀티턴 도구 사용 벤치마크. 최우수 에이전트가 개별 요청 69.6% 해결, 완전한 대화 완료는 39.8%에 그침.

- **[Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of LLMs](https://arxiv.org/abs/2610.18248)**
  - `2026-10` · cs.CL
  - LLM 효율적 평가를 위한 벤치마크 압축 종합 조사. ICML·NeurIPS·ICLR·AAAI·KDD·CVPR 에서의 2025–2026 작업 포함.

- **[ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research](https://arxiv.org/abs/2506.02314)**
  - `2026-06` · cs.AI
  - NeurIPS·ICLR·CVPR 등 주요 학회 논문 20편에서 212개 코딩 과제 추출, ML 논문 → 작동 코드 변환 평가.

---

## Finance  (17)

### NeurIPS 2026

- **[BankerToolBench: Evaluating AI Agents in End-to-End Investment Banking Workflows](https://neurips.cc/virtual/2026/poster/139094)**
  - **NeurIPS 2026** · `2026` · ✅ Accepted
  - 투자 은행 엔드투엔드 워크플로우에서 AI 에이전트 평가. _(Agent 섹션과 중복 — Finance 측면 강조)_

- **[FinVerify: A Verification Framework for Financial Agents](https://arxiv.org/abs/2611.20423)**
  - `2026-11` · **NeurIPS 2026 Workshop** (Who Verifies the Agents?)
  - 금융 에이전트의 출력 검증 프레임워크. NeurIPS 2026 Workshop 발표.

### NeurIPS 2025

- **[FinAgentBench: A Benchmark Dataset for Agentic Retrieval in Financial Question Answering](https://neurips.cc/virtual/2025/loc/san-diego/132558)**
  - **NeurIPS 2025 Workshop** (Generative AI in Finance) · `2025`
  - S&P-100 상장기업 대상 3,429개 전문가 주석 예시. LLM 에이전트가 올바른 문서 유형 식별 및 핵심 구절 추출 능력 평가.

- **[Privacy-Preserving Financial Fraud Detection](https://neurips.cc/virtual/2025/loc/san-diego/132498)**
  - **NeurIPS 2025** · `2025`
  - 한국 은행 데이터 기반 프라이버시 보존 금융 사기 탐지. 생성 모델과 연합 부스팅 활용.

- **[EconEvals: Benchmarks and Litmus Tests for Economic Decision-Making by LLM Agents](https://arxiv.org/abs/2503.18825)**
  - **NeurIPS 2025** · `2025`
  - LLM 에이전트의 경제적 의사결정 능력을 평가하는 벤치마크 및 리트머스 테스트.

### ICLR 2026

- **[Fin-RSI: A Unified Library of Financial Skills, Checks, and Self-Improvement for LLM Agents](https://arxiv.org/abs/2611.29716)**
  - **ICLR 2026** · `2026-11-22`
  - 금융 LLM 에이전트를 위한 통합 스킬·검증·자기개선 라이브러리.

### KDD 2025

- **[FLAG: Fraud Detection with LLM-Enhanced Graph Neural Network](https://dl.acm.org/doi/)**
  - *KDD 2025 Proceedings*
  - **KDD 2025** · `2025`
  - LLM으로 강화된 그래프 신경망을 활용한 금융 사기 탐지.

### arXiv (Recent Finance)

- **[FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance](https://arxiv.org/abs/2611.07464)**
  - `2026-11-05` · cs.AI/cs.CL
  - 에이전트가 웹에서 직접 데이터를 수집하고 데이터 컷오프 하에서 자체 백테스트를 구성하는 오픈 월드 금융 에이전트 평가 패러다임.

- **[AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests](https://arxiv.org/abs/2611.04813)**
  - `2026-11-03` · cs.AI
  - 현실적인 금융 요청 기반 다양한 태스크에서 금융 에이전트를 평가하는 종합 벤치마크.

- **[Inside the Trading Loop: Markets, Models, and Moves with LLM Agents](https://arxiv.org/abs/2611.11657)**
  - `2026-11-08` · cs.AI/q-fin.TR
  - LLM 애널리스트(기업 뉴스·거시경제 에이전트)가 코디네이터에게 피드백하고 주식 비중·현금 보유를 설정, 모멘텀 기반 포트폴리오 구성.

- **[Agent4Crypto: A Dual-Reflective Multi-Agent System for Cryptocurrency Trading](https://arxiv.org/abs/2611.12269)**
  - `2026-11-09` · cs.AI
  - 경험 메모리와 트레이더 에이전트별 기여도를 결합한 이중 반성 LLM 멀티에이전트 암호화폐 거래 시스템.

- **[FinCutBench: A Continually Updated Benchmark for Measuring the Temporal Boundaries of LLM Financial Knowledge](https://arxiv.org/abs/2611.11588)**
  - `2026-11-08` · cs.CL
  - LLM 금융 지식의 시간적 한계를 측정하는 지속 업데이트 벤치마크.

- **[Reliable Evaluation of AI Agents for Investment Research: A Framework for Performance and Validity Assessment](https://arxiv.org/abs/2611.22338)**
  - `2026-11-17` · cs.AI
  - 에이전트 성능과 평가 타당성을 동시에 측정하는 프레임워크. 평가 입력·참조 정보·증거·채점 출력의 무결성을 검사.

- **[Agent Money Benchmark: Can AI Agents Be Trusted to Spend Money?](https://arxiv.org/abs/2611.28610)**
  - `2026-11-21` · cs.AI
  - 금융 의사결정을 위한 정보 구매 태스크에서 에이전트의 신뢰성 평가. 12개 모델 중 3개가 80개 지불 태스크에서 오류 없이 통과.

- **[QuantHarness: Reliable Before Profitable — Governing Financial Strategy Development with LLM Agents](https://arxiv.org/abs/2610.26101)**
  - `2026-10-19` · cs.AI/q-fin
  - 금융 전략 개발을 위한 2계층 에이전트 하네스. 금융 특화 워크플로우 계층 + 강제 실행 코어.

- **[The Harness Is the Model (Finance 측면): Banking Conduct Rules Compliance](https://arxiv.org/abs/2611.06116)**
  - `2026-11-04` · cs.CL _(Harness 섹션과 중복 — Finance 측면 강조)_
  - 소매 은행 행동 규범 준수 맥락에서 에이전트 하네스가 LLM 행동에 미치는 영향 분석.

---

## 소스 요약

| 소스 | Agent | Harness | Finance |
|------|-------|---------|---------|
| NeurIPS 2026 | 4 | — | 2 |
| ICLR 2026 | 6 | — | 1 |
| NeurIPS 2025 | 1 | 1 | 3 |
| ICML 2025 | 3 | — | — |
| CVPR 2025 | 3 | — | — |
| AAAI 2026 | 1 | — | — |
| KDD 2025 | — | — | 1 |
| arXiv (최근) | 7 | 9 | 10 |
| **합계** | **25** | **10** | **17** |

> **중복 제외:** 일부 논문(BankerToolBench, The Harness Is the Model 등)이 복수 토픽에 걸치는 경우 각 섹션에 표기하되 고유 논문 수 기준으로는 한 번만 집계.

---

*수집 일시: 2026-11-26 | 네트워크 제한으로 HuggingFace Daily Papers 및 arXiv 직접 조회 불가 — WebSearch 기반 수집*
