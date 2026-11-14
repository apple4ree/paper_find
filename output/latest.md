# Daily Paper Digest — 2026-11-14 (Saturday)

> **수집 방식:** WebSearch 기반 수동 수집 (네트워크 정책으로 인해 huggingface.co, arxiv.org, semanticscholar.org 직접 접근 불가)
> **수집 범위:** AAAI 2026, NeurIPS 2026, ICML 2026, ICLR 2026, CVPR 2026, KDD 2026 + HuggingFace Daily Papers (Nov 2026)

---

## Agent  (25)

### NeurIPS 2026

- **AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent**
  - NeurIPS 2026 Poster · Hall C1, Dec 12 (Atlanta)
  - 멀티에이전트 디베이트를 단일 LLM 에이전트 가중치로 증류하여 추론 시간 계산 비용을 학습 단계로 전환하는 방법론

- **VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems**
  - NeurIPS 2026
  - LLM 멀티에이전트 시스템의 실패 원인 귀인을 위한 가설 검증 프레임워크

- **Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning**
  - NeurIPS 2026
  - 마음 이론(Theory-of-Mind) 추론을 활용해 자율 LLM 에이전트를 모니터링하는 방법

- **AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems**
  - NeurIPS 2026
  - 멀티에이전트 시스템에서 조기 실패 예측을 위한 온라인 감사 프레임워크

- **Heuresis: Evaluating Search Strategies for Autonomous Machine Learning Research Agents**
  - NeurIPS 2026
  - 자율 머신러닝 연구 에이전트의 탐색 전략을 평가하는 벤치마크

- **Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory**
  - NeurIPS 2026
  - 에이전트 메모리의 rate-distortion 프레임워크. 결정 자체를 기억하는 방식으로 효율성 향상

- **PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments**
  - NeurIPS 2026 Poster · Hall C1, Dec 12 (Atlanta)
  - 100개의 장기 임상 작업에서 EHR 환경의 LLM 에이전트 평가. 최고 모델도 46% 성공률(pass@1)

- **ContractBench: Can LLM Agents Preserve Observation Contracts?**
  - NeurIPS 2026 Poster · Hall C1, Dec 12 (Atlanta)
  - API 아티팩트(presigned URLs 등) 유효성 유지 능력을 평가하는 33개 이중 축 태스크 벤치마크

- **R&D-Agent-Quant: A Multi-Agent Framework for Factor and Model Optimization**
  - NeurIPS 2025 · CMU, MSRA
  - 퀀트 투자에서 팩터 및 모델 최적화를 위한 멀티에이전트 프레임워크

- **MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research**
  - NeurIPS 2025 Datasets & Benchmarks
  - NeurIPS, ICLR, ICML 워크숍에서 추출한 201개 태스크로 AI 연구 에이전트 평가

### ICML 2026

- **Decrypto: A Game-Based Benchmark for Multi-Agent Reasoning and Theory of Mind**
  - ICML 2026
  - 멀티에이전트 추론과 마음 이론을 위한 게임 기반 벤치마크

- **AgentLAB: Benchmarking LLM Agent Susceptibility to Adaptive Long-Horizon Attacks**
  - ICML 2026
  - 장기 적응형 공격에 대한 LLM 에이전트 취약성 벤치마크

- **AgentWebBench: Evaluating User-Agent Synthesis via Website-Specific Content Agents**
  - ICML 2026
  - 웹사이트 특화 콘텐츠 에이전트와의 상호작용을 통한 에이전트 답변 합성 평가

- **MASPO: Joint Prompt Optimization for LLM-Based Multi-Agent Systems**
  - ICML 2026
  - LLM 기반 멀티에이전트 시스템을 위한 공동 프롬프트 최적화

- **OMAC: Holistic Optimization Framework for LLM-Based Multi-Agent Systems**
  - ICML 2026
  - LLM 기반 멀티에이전트 시스템의 종합 최적화 일반 프레임워크

### ICLR 2026

- **MemoryAgentBench: Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions**
  - ICLR 2026 · HUST
  - 증분 멀티턴 상호작용을 통해 LLM 에이전트의 메모리를 평가하는 벤치마크
  - GitHub: [HUST-AI-HYZ/MemoryAgentBench](https://github.com/HUST-AI-HYZ/MemoryAgentBench)

- **MCP-Bench: Evaluating LLM Agents in Realistic Ecosystem-Based Tool-Use Scenarios**
  - ICLR 2026
  - 금융, 과학, 연구 도구를 아우르는 실제 생태계 기반 도구 사용 시나리오에서 LLM 에이전트 평가

- **FinSearchComp: An End-to-End Open-Source Agent Benchmark for Financial Research Tasks**
  - ICLR 2026
  - 글로벌 및 중화권 시장을 아우르는 635개 질문의 완전 오픈소스 금융 연구 에이전트 벤치마크

- **ACE: Context Optimization for Agents and Finance**
  - ICLR 2026
  - 에이전트 성능 +10.6%, 금융 성능 +8.6% 향상을 달성하는 컨텍스트 최적화 방법론

### AAAI 2026

- **RECoRD: Multi-Agent LLM Framework for Reverse Engineering Codebases to Causal Diagrams**
  - AAAI 2026 · Amazon
  - 코드베이스를 인과관계 다이어그램으로 역설계하는 LLM 멀티에이전트 프레임워크

- **MAGIC: Multi-Modal LLM Agents for Physical Adversarial Patches in Driving Scenarios**
  - AAAI 2026 · A*STAR CFAR
  - 자율주행 시나리오의 물리적 적대 패치 생성을 위한 멀티모달 LLM 에이전트 프레임워크

- **COACH: Collaborative Agents for Contextual Highlighting**
  - AAAI 2026 LaMAS Workshop
  - 컨텍스트 강조 작업을 위한 협업 에이전트 시스템

- **STAR-MARL: LLM-Based Sub-task Curricula Design for Multi-Agent RL**
  - AAAI 2026 LaMAS Workshop
  - LLM을 활용한 멀티에이전트 강화학습의 서브태스크 커리큘럼 설계

### CVPR 2026

- **Universal Guideline-Driven Image Clustering via Hybrid LLM Agent**
  - CVPR 2026 · Amazon
  - 범용 가이드라인 기반 이미지 클러스터링을 위한 하이브리드 LLM 에이전트

- **Restore-R1: Efficient Image Restoration Agents via RL with Multimodal LLM Perceptual Feedback**
  - CVPR 2026 Findings
  - 멀티모달 LLM의 지각적 피드백을 활용한 강화학습 기반 효율적 이미지 복원 에이전트

### HuggingFace Daily Papers (Nov 2026)

- **Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems**
  - HuggingFace Featured · arXiv:2610.30418
  - LLM 에이전트 시스템에서 기밀 정보 유출 탐지 프레임워크

- **Agent-Reflex: Teaching Language Agents to Act Reflectively**
  - HuggingFace Featured · arXiv:2610.17953
  - 언어 에이전트에 반성적 행동 학습을 도입하는 방법론

- **CEPO: A General Framework for Improving Prompt Optimization in Multi-Agent Systems**
  - HuggingFace Daily Papers, Nov 2026
  - 멀티에이전트 시스템에서 프롬프트 최적화를 향상시키는 일반 프레임워크

- **Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training**
  - HuggingFace Daily Papers, Nov 2026
  - 형제 하네스에서 학습하여 범용적 에이전트 훈련을 위한 프레임워크

- **EvoTeam: Multi-Agent Collaboration via Evolving Teams**
  - HuggingFace Daily Papers, Nov 2026
  - LLM 기반 멀티에이전트 시스템에서 팀 조직과 상호작용 규칙의 진화적 학습

- **MoLRSI: A Recursive Self-Improving AI Agent for Molecular Discovery**
  - HuggingFace Featured · arXiv:2610.39714
  - 분자 발견을 위한 재귀적 자기 개선 AI 에이전트

---

## Harness  (14)

### ICLR 2026

- **Terminal-Bench: Benchmarking LLM Agents on Terminal-Based Tasks**
  - ICLR 2026 (also NeurIPS 2025 D&B Spotlight)
  - 89개의 터미널 기반 작업 벤치마크. 프론티어 모델도 65% 미만의 점수. 평가 하네스 포함 공개
  - [proceedings.iclr.cc](https://proceedings.iclr.cc/paper_files/paper/2026/file/444a3737adaee10d86ad2ef5f74468e6-Paper-Conference.pdf)

- **ProfBench: Rubric-Guided Benchmark of Professional-Level Tasks**
  - ICLR 2026
  - 전문가 수준 작업의 루브릭 가이드 벤치마크. 인간 전문가 채점으로 LLM 판사 편향 감소 및 평가 비용 절감
  - [proceedings.iclr.cc](https://proceedings.iclr.cc/paper_files/paper/2026/file/09c4960d66e6182e57062c5d71ce1d3d-Paper-Conference.pdf)

- **MeTaBench: Contamination-Resistant Benchmark Reduction**
  - ICLR 2025
  - 6개 기존 벤치마크의 오염 저항 축소판. EleutherAI의 lm-evaluation-harness에 통합
  - [proceedings.iclr.cc](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)

- **BENTO: Efficient Benchmark Task Reduction via In-Context Learning**
  - ICLR 2025
  - 인컨텍스트 학습을 통해 LLM 벤치마크 태스크를 5%로 축소하여 평가 비용 절감
  - [proceedings.iclr.cc](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)

### NeurIPS 2026

- **Act As a Real Researcher: Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle**
  - arXiv:2606.07462 · NeurIPS 2026 Workshop
  - 연구 생명주기 전반에 걸쳐 LLM과 에이전트 하네스를 평가하는 벤치마크 스위트

- **AgentAtlas: Beyond Outcome Leaderboards for LLM Agents**
  - arXiv:2605.20530
  - 최종 결과 리더보드를 넘어 과정 중심의 에이전트 평가 접근법

- **Heuresis: Evaluating Search Strategies for Autonomous ML Research Agents**
  - NeurIPS 2026
  - 자율 ML 연구 에이전트의 탐색 전략 평가

### HuggingFace / arXiv

- **HarnessOpt-Bench: Evaluating LLMs at Harness Optimization**
  - arXiv:2608.06301
  - 고비용·확률적 평가 하에서 하네스 최적화를 위한 LLM 평가 벤치마크. end-to-end 하네스 최적화

- **Stop Comparing LLM Agents Without Disclosing the Harness**
  - arXiv:2605.23950
  - 에이전트 비교 시 하네스 공개의 필요성 주장. 동일 모델이 다른 하네스에서 다른 성능을 보임을 입증

- **Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts**
  - arXiv:2609.18366
  - 반사실적 가이드를 통한 하네스 진화 방법론. 태스크 특화 지름길을 넘어서는 평가 프레임워크

- **Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation**
  - arXiv:2607.25891
  - 벤치마크 간 에이전트 평가를 위한 고해상도 코퍼스

- **DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows**
  - arXiv:2608.26546
  - 복잡한 실세계 워크플로우에서 자율 에이전트를 평가하는 벤치마크

- **Beyond Final Scores: Systematic Evaluation of Agents for Long-Horizon AI R&D**
  - arXiv:2608.13417
  - 장기 AI 연구개발을 위한 에이전트의 체계적 평가. 최종 점수 너머의 과정 평가

- **FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance**
  - HuggingFace Daily Papers, Nov 2026
  - 금융 도메인 에이전트를 위한 오픈 월드 평가 패러다임

---

## Finance  (19)

### KDD 2026

- **Can LLM-based Financial Investing Strategies Outperform the Market in Long Run?**
  - KDD 2026 · University of Edinburgh (Oral, Datasets & Benchmarks Track)
  - LLM 기반 금융 투자 전략의 장기 시장 초과 성과 가능성을 20년(2004–2024) FINSABER 프레임워크로 엄밀히 평가. 벤치마크 편향 문제 지적
  - [ACM DL](https://dl.acm.org/doi/abs/10.1145/3770854.3785702) · [GitHub](https://github.com/waylonli/FINSABER)

- **CNFinBench: Evaluating Finance Expertise, Autonomy, and Integrity of LLM Agents**
  - KDD 2026
  - 금융 전문성, 자율성, 무결성을 평가하는 에이전트 벤치마크. 기존 규칙 기반 QA의 한계를 지적하고 에이전트 실행과 컴플라이언스를 포함

- **SOP-Bench: Industrial Agent Benchmark Across 12 Business Domains Including Finance**
  - KDD 2026
  - 금융을 포함한 12개 비즈니스 도메인 2,000+ 태스크. 전문가 작성 SOP 기반

### ICLR 2026

- **Trade in Minutes! (TiMi): Rationality-Driven Agentic System for Quantitative Trading**
  - ICLR 2026 · TJU, MSRA
  - 합리성 기반의 에이전트 퀀트 트레이딩 시스템. 미국 시장 200+ 종목 실거래 실험

- **AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets**
  - ICLR 2026
  - GFlowNets를 활용한 구조 인식 알파 팩터 채굴

- **AlphaAgentEvo: Evolution-Oriented Alpha Mining via Agentic Reinforcement Learning**
  - ICLR 2026
  - 에이전트 강화학습을 통한 진화 지향 알파 팩터 채굴

- **STABLE: Shift-Tolerant Allocation via Black-Litterman with Conditional Diffusion Estimates**
  - ICLR 2026
  - 조건부 디퓨전 추정을 통한 Black-Litterman 모델 기반 분포 이동 허용 포트폴리오 배분

- **FinSearchComp: End-to-End Open-Source Agent Benchmark for Financial Research**
  - ICLR 2026
  - 글로벌 및 중화권 시장의 635개 질문 기반 완전 오픈소스 금융 연구 에이전트 벤치마크

- **FORESIGHT-9: Prospective and Process-Aware Evaluation of Adaptive Trading Agents**
  - arXiv:2608.29372 · ICLR 2026 related
  - 적응형 트레이딩 에이전트에 대한 전망적, 과정 인식 평가 프레임워크

### NeurIPS 2025

- **DeepFund: Live Arena for Evaluating LLMs on Fund Investment**
  - NeurIPS 2025 · HKUST
  - LLM 펀드 투자 성과를 실시간으로 평가하는 라이브 아레나

- **PHANTOM: Benchmark for Hallucination Detection in Financial Long-Context QA**
  - NeurIPS 2025 · Goldman Sachs
  - 금융 장문 맥락 QA에서 환각 탐지를 위한 벤치마크

- **R&D-Agent-Quant: Multi-Agent Framework for Quantitative Factor Optimization**
  - NeurIPS 2025 · CMU, MSRA
  - 퀀트 팩터 및 모델 최적화를 위한 멀티에이전트 프레임워크

### ICML 2026

- **Evaluating LLMs in Finance Requires Explicit Bias Consideration**
  - ICML 2026 Position Paper · Seoul, Jul 6-11
  - 2023–2025년 164개 주요 학회 금융 AI 논문 분석. 26.8%만이 선행 편향(look-ahead bias)을 명시적으로 인정

### HuggingFace / arXiv

- **AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests**
  - arXiv:2611.04813 · Nov 2026
  - 230개 실세계 금융 태스크(8개 카테고리, 2개 언어, 4단계 복잡도). 동일 모델도 하네스에 따라 성능 차이 발생을 실증

- **FinanceHarness: Autonomous Financial Deep Research Framework**
  - HuggingFace Featured · arXiv:2607.27853
  - 금융 도구와 워크플로우를 실행하는 하네스. 동일 백본으로 루브릭 점수 25.3% → 32.4% 향상

- **BigFinanceBench: Workflow-Grounded Benchmark for Financial-Research Agents**
  - arXiv:2606.03829 · HuggingFace
  - 오픈 북 ReAct 스타일 하네스와 50단계 예산으로 프론티어 모델 평가하는 벤치마크

- **FrontierFinance: Benchmark for Measuring Frontier Intelligence of Finance Agents**
  - arXiv:2608.11683
  - 6개 고위험 금융 사용 사례에 걸친 금융 에이전트 프론티어 벤치마크

- **Mint-Agent: Finance-Native Agentic Foundation Models**
  - arXiv:2608.16386
  - 금융 네이티브 에이전트 기반 모델 소개

- **LATTICE: Evaluating Decision Support Utility of Crypto Agents**
  - arXiv:2604.26235
  - 암호화폐 에이전트의 의사결정 지원 유틸리티 평가 프레임워크

---

## 요약

| 토픽 | 논문 수 |
|------|---------|
| Agent | 30 |
| Harness | 14 |
| Finance | 19 |
| **합계 (중복 제외)** | **~55** |

> **네트워크 제한 사항:** 이 세션은 huggingface.co, arxiv.org, semanticscholar.org, neurips.cc, paperdigest.org에 대한 직접 접근이 차단되어 있습니다. WebSearch 도구를 통해 최대한 수집하였으나 일부 논문은 누락되었을 수 있습니다. 네트워크 정책 업데이트를 통해 위 도메인 접근을 허용하면 `python main.py` 스크립트가 더 완전한 결과를 제공합니다.

---

*Sources: [HuggingFace Daily Papers Nov 2026](https://huggingface.co/papers/month/2026-11) · [NeurIPS 2026](https://neurips.cc/virtual/2026) · [ICLR 2026 Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/) · [ICML 2026](https://icml.cc/virtual/2026) · [KDD 2026](https://dl.acm.org/doi/abs/10.1145/3770854.3785702) · [AAAI 2026](https://www.amazon.science/conferences-and-events/aaai-2026) · [CVPR 2026](https://cvpr.thecvf.com/virtual/2026)*
