# Daily Paper Digest — 2026-11-08 (Sunday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · HuggingFace · arXiv | Agent · Harness · Finance |

**50 unique papers** (cross-topic papers counted once per category)

---

## Agent  (25)

### NeurIPS 2026

- **AgentArk**
  - **NeurIPS 2026** · Main Track
  - Agent safety and self-correction in multi-step agentic workflows.

- **AgentAbstain**
  - **NeurIPS 2026** · Main Track
  - When and how agents should decline tasks beyond their reliable capability.

- **AgentForesight**
  - **NeurIPS 2026** · Main Track
  - Anticipatory planning in LLM agents for long-horizon task completion.

- **AgentWeave**
  - **NeurIPS 2026** · Main Track
  - Compositional agent architectures for multi-skill task execution.

- **[When and Why Does Multi-Agent Debate Fail and Does It Really Underperform?](https://openreview.net/)**
  - **NeurIPS 2026** · Main Track (RIKEN AIP accepted)
  - Systematic analysis of conditions under which multi-agent debate fails and comparison against single-agent baselines.

- **FINCOSMOS** (arXiv:2611.07464)
  - **NeurIPS 2026** · Submission (cs.AI Nov 6, 2026)
  - Open-world evaluation paradigm for finance agents: agent acquires data from the web, builds its own backtest under a data cutoff, and delivers verifiable results with no pre-provided data.

### ICML 2026

- **[Towards Professional-Grade Financial Agents: Benchmarking, Tooling, and Structured Reasoning](https://openreview.net/)**
  - **ICML 2026** · Main Track
  - Proposes a comprehensive benchmark and reasoning framework for financial agents aimed at professional-level performance.

- **[MarketSim: Simulating Stock Markets with Large-Scale Generative Agents](https://openreview.net/)**
  - **ICML 2026** · Main Track
  - Large-scale generative agent simulation of stock markets for studying emergent market phenomena and AI-driven trading.

- **[Position: Collusion Risks Among AI Reasoning Agents Justify Certification Requirements for Making Market Decisions](https://openreview.net/)**
  - **ICML 2026** · Position Paper
  - Argues that AI agents making market decisions pose systemic collusion risks and advocates for formal certification requirements.

- **[Evolving Quantitative Reasoning through Self-Play in Digital Twin Markets](https://openreview.net/)**
  - **ICML 2026** · Main Track
  - Applies self-play in simulated digital twin market environments to evolve quantitative reasoning capabilities in LLM agents.

- **[VeRO: An Evaluation Harness for Agents to Optimize Agents](https://openreview.net/)**
  - **ICML 2026** · Main Track
  - Meta-evaluation framework where an agent harness is used to optimize other agent harnesses, enabling recursive improvement.

- **[MARS: Modular Agent with Reflective Search for Automated AI Research](https://openreview.net/)**
  - **ICML 2026** · Main Track (Microsoft)
  - Modular LLM agent with reflective self-search for automated scientific research workflows.

### ICLR 2026

- **[AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite](https://openreview.net/)**
  - **ICLR 2026** · Oral
  - A scientific research benchmark for rigorously evaluating AI agents across diverse scientific tasks.

- **[Speculative Actions: A Lossless Framework for Faster AI Agents](https://openreview.net/)**
  - **ICLR 2026** · Oral
  - Introduces speculative action execution that improves agent throughput without loss of task quality.

- **[MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science](https://openreview.net/)**
  - **ICLR 2026** · Main Track
  - Scalable gym environment for training LLM agents on code-centric biomedical data science tasks.

- **[AgentFlow: Trainable Multi-Agent Planning with Tool Use](https://openreview.net/)**
  - **ICLR 2026** · Main Track (Lambda AI highlight)
  - Multi-agent system where a team of agents learns to collaboratively plan and use tools in complex task flows.

- **[Agent Data Protocol: A Unified Dataset for Fine-Tuning LLM Agents](https://openreview.net/)**
  - **ICLR 2026** · Oral
  - Proposes a unified dataset protocol and format for fine-tuning agents across diverse agentic tasks.

- **[FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning](https://openreview.net/)**
  - **ICLR 2026** · Main Track
  - Expert-level benchmark for financial search and multi-step reasoning by LLM agents.

- **[When AI Agents Collude Online: Financial Fraud Risks by Collaborative LLM Agents on Social Platforms](https://openreview.net/)**
  - **ICLR 2026** · Main Track
  - Investigates how collaborative LLM agents on social platforms can be weaponized for coordinated financial fraud.

### CVPR 2026

- **[Agent4FaceForgery: Multi-Agent LLM Framework for Realistic Face Forgery Detection](https://openaccess.thecvf.com/content/CVPR2026/)**
  - **CVPR 2026** · Main Track
  - LLM-powered multi-agent framework with profile and memory modules that simulates forgery creation to detect deepfakes.

- **[VULCAN: Tool-Augmented Multi-Agents for Iterative 3D Object Arrangement](https://ai.stanford.edu/blog/cvpr-2026/)**
  - **CVPR 2026** · Main Track (Stanford)
  - Multi-agent system with specialized tools for iterative spatial arrangement of 3D objects.

- **[VTOS: Learning to Orchestrate Vision Tools by Co-Searching Solutions and Observers](https://arxiv.org/abs/2606.20728)**
  - **CVPR 2026** · Main Track
  - Vision-language agent that co-searches optimal tool orchestration sequences and observer strategies.

### KDD 2026

- **[SOP-Bench: Benchmarking LLM Agents on Industrial Standard Operating Procedures](https://www.amazon.science/conferences-and-events/kdd-2026)**
  - **KDD 2026** · Main Track (Amazon)
  - Benchmark evaluating LLM agents on enterprise-grade standard operating procedure adherence.

- **[Can LLM-based Financial Investing Strategies Outperform the Market in Long Run?](https://researchr.org/publication/LiKCM26)**
  - **KDD 2026** · Main Track
  - Empirical study evaluating the long-run alpha generation capability of LLM-driven investment strategies.

---

## Harness  (12)

### ICML 2026

- **[VeRO: An Evaluation Harness for Agents to Optimize Agents](https://openreview.net/)**
  - **ICML 2026** · Main Track
  - *(also listed in Agent section)* Meta-evaluation harness for recursive agent optimization.

### HuggingFace / arXiv

- **[FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents](https://huggingface.co/papers/2605.27333)**
  - arXiv:2605.27333 · `2026-05-27`
  - Inline safety harness monitoring queries and tool calls during the full agent lifecycle with a cascade verification module.

- **[Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents](https://arxiv.org/abs/2606.01886)**
  - arXiv:2606.01886 · `2026-06-03` · ICLR 2026 FinAI Workshop (accepted)
  - Knowledge harness for finance agents: reduces latency by 82.95%, token cost by 82.29%, stale-knowledge usage by 96.58%.

- **[FinanceHarness: Autonomous Financial Deep Research Framework](https://huggingface.co/papers/2607.27853)**
  - arXiv:2607.27853 · `2026-08-07`
  - Expert-knowledge-guided harness with layered services (LLM-facing tools, APIs, execution workflows, evaluation rubrics) + FinanceGym benchmark. Frontier models score 44.9% on its leaderboard.

- **[The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules, Unevenly Across Models](https://arxiv.org/abs/2611.06116)**
  - arXiv:2611.06116 · `2026-11-06` · **Very Recent**
  - Shows that harness design (not just the base LLM) significantly and unevenly affects compliance with banking regulatory conduct rules.

- **[QuantHarness: Governing Financial Strategy Development with LLM Agents](https://arxiv.org/abs/2610.26101)**
  - arXiv:2610.26101 · `2026-10-26`
  - Two-layer harness for governing LLM-driven quantitative strategy development, paired with FinRelBench.

- **[Replayable Financial Agents: A Determinism-Faithfulness Assurance Harness (DFAH)](https://arxiv.org/abs/2601.15322)**
  - arXiv:2601.15322 · `2026-01-15` · **ICLR 2026 Workshop on Advances in Financial AI (accepted)**
  - Determinism-faithfulness assurance harness for tool-using LLM agents in finance, ensuring replay consistency.

- **[Code as Agent Harness](https://huggingface.co/papers/2605.18747)**
  - arXiv:2605.18747 · `2026-05-18`
  - Survey framing code as the foundational infrastructure for agent harnesses; reviews 100+ agent systems.

- **[Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850)**
  - arXiv:2604.25850 · `2026-04-25`
  - Closed-loop method for automatically evolving coding-agent harnesses using runtime observability signals.

- **[Harness as an Asset: Enforcing Determinism via CAAF (Convergent AI Agent Framework)](https://arxiv.org/abs/2604.17025)**
  - arXiv:2604.17025 · `2026-04-17`
  - Framework for deterministic agent execution by treating the harness as a first-class software asset.

- **[Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974)**
  - arXiv:2609.24974 · `2026-09-24`
  - Distillation method where an agent itself serves as the harness, enabling zero-shot harness generation.

- **[Co-Evolving Harnesses and Models](https://clea-neurips.github.io/)**
  - **NeurIPS 2026** · CLEA Workshop
  - Joint co-evolution of model weights and agent harnesses for improved agentic capability.

---

## Finance  (22)

### ICML 2026

- **[Towards Professional-Grade Financial Agents: Benchmarking, Tooling, and Structured Reasoning](https://openreview.net/)**
  - **ICML 2026** · Main Track
  - *(also in Agent section)*

- **[MarketSim: Simulating Stock Markets with Large-Scale Generative Agents](https://openreview.net/)**
  - **ICML 2026** · Main Track
  - *(also in Agent section)*

- **[Evolving Quantitative Reasoning through Self-Play in Digital Twin Markets](https://openreview.net/)**
  - **ICML 2026** · Main Track
  - *(also in Agent section)*

- **[FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors](https://openreview.net/)**
  - **ICML 2026** · Main Track (OpenReview confirmed)
  - Privacy-preserving benchmark for auditing AI agent deployments in financial services.

- **[ParaFusionBench: A Unified Benchmark for Cross-Paradigm Fusion in Factor Mining and Trading Decision-Making](https://openreview.net/)**
  - **ICML 2026** · Main Track (OpenReview confirmed)
  - Bridges conventional factor mining and LLM/agent-based trading across four paradigms.

- **[PortfolioRouter: Consequence-Aware Multi-Task Routing for Portfolio Agents](https://openreview.net/)**
  - **ICML 2026** · Main Track (OpenReview confirmed)
  - Cost-sensitive routing framework for portfolio agents weighted by financial consequences, not classification error.

### ICLR 2026

- **[FinSearchComp: Towards a Realistic, Expert-Level Evaluation of Financial Search and Reasoning](https://openreview.net/)**
  - **ICLR 2026** · Main Track
  - *(also in Agent section)*

- **[When AI Agents Collude Online: Financial Fraud Risks by Collaborative LLM Agents on Social Platforms](https://openreview.net/)**
  - **ICLR 2026** · Main Track
  - *(also in Agent section)*

- **[Trade in Minutes! Rationality-Driven Agentic System for Quantitative Financial Trading](https://openreview.net/)**
  - **ICLR 2026** · Main Track
  - Agentic system leveraging rational planning for sub-minute quantitative trading execution.

- **[AI Fundamentals: Valuing AI Agents & Data Assets](https://openreview.net/)**
  - **ICLR 2026** · Main Track
  - Provides theoretical foundations for valuing AI agents and their associated data assets in financial/enterprise contexts.

### KDD 2026

- **[Can LLM-based Financial Investing Strategies Outperform the Market in Long Run?](https://researchr.org/publication/LiKCM26)**
  - **KDD 2026** · Main Track
  - *(also in Agent section)*

- **[FinTexTS: Financial Text-Paired Time-Series Dataset](https://kr.linkedin.com/in/junhyeokkang)**
  - **KDD 2026** · Main Track / Workshop (LG EXAONE BI team)
  - Financial text paired with time-series data for joint modeling of market signals and language.

### NeurIPS 2026

- **[FinGovBench: Evaluating Governance Contracts for Financial AI Agents](https://www.agenthon.net/)**
  - **NeurIPS 2026** · Agenthon Workshop
  - Benchmark for evaluating governance and compliance contracts applied to financial AI agents.

- **[QuantitativeFinance-Bench: Benchmarking AI Agents on Real-World Quantitative Finance Tasks](https://www.agenthon.net/)**
  - **NeurIPS 2026** · Agenthon Workshop
  - Real-world quantitative finance benchmark for AI agents covering strategy research and execution.

- **[Bound Together: Composing Finance Agent Harnesses from Best-of-Breed Parts](https://www.agenthon.net/)**
  - **NeurIPS 2026** · Agenthon Workshop
  - Modular approach to composing finance agent harnesses from interchangeable components.

- **[PRISM: Prompt-Refined In-Context System Modeling for Financial Retrieval](https://clea-neurips.github.io/)**
  - **NeurIPS 2026** · CLEA Workshop
  - Prompt engineering method optimized for financial document retrieval in enterprise LLM agents.

- **[Beyond Leaderboards: Continual, Task-Specific LLM Evaluation for Enterprise Finance](https://clea-neurips.github.io/)**
  - **NeurIPS 2026** · CLEA Workshop
  - Framework for ongoing, task-specific evaluation of LLMs deployed in enterprise finance environments.

### HuggingFace / arXiv

- **[Agentic Trading: When LLM Agents Meet Financial Markets](https://arxiv.org/abs/2605.19337)**
  - arXiv:2605.19337 · `2026-05-19` (revised Oct 2026)
  - Survey of LLM agent trading systems via Architecture–Capability–Adaptation framework; covers 77 studies.

- **[Agentic Quantitative Trading: A Survey of Workflows, Systems, and Evaluation](https://arxiv.org/abs/2608.31041)**
  - arXiv:2608.31041 · `2026-08-31`
  - Comprehensive survey of agentic quantitative trading pipelines and evaluation methodologies.

- **[FrontierFinance: A Challenging Benchmark for Measuring Frontier Intelligence of Finance Agents](https://arxiv.org/abs/2608.11683)**
  - arXiv:2608.11683 · `2026-08-11`
  - Difficult expert-level benchmark testing frontier LLM agents on financial analysis tasks.

- **[Mint-Agent: Introducing Finance-Native Agentic Foundation Models](https://arxiv.org/abs/2608.16386)**
  - arXiv:2608.16386 · `2026-08-16`
  - Finance-native foundation model designed from the ground up for agentic workflows in financial services.

- **[Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113)**
  - arXiv:2610.30113 · `2026-10-30`
  - End-to-end benchmark for LLM agents doing quantitative research on real A-share data beyond formula/code scoring.

---

*보고서 생성: 2026-11-08 | 주요 소스: AAAI·NeurIPS·ICML·ICLR·CVPR·KDD 공식 사이트, HuggingFace Daily Papers, arXiv cs.AI/cs.CL*

*Note: NeurIPS 2026 개최: 2026년 12월 6–12일 시드니 (위성 행사: 애틀랜타·파리)*
*CVPR 2026 개최: 2026년 6월 3–7일 덴버 | ICML 2026 개최: 2026년 7월 6–11일 서울 | KDD 2026 개최: 2026년 8월 9–13일 제주*
