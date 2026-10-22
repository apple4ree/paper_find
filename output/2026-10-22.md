# Daily Paper Digest — 2026-10-22 (Thursday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**578 unique papers** (744 topic-entries — cross-topic papers counted once per category)

---

## Agent  (410)

### AAAI

- **[Two Heads are Better than One: Distilling Large Language Model Features Into Small Models with Feature Decomposition and Mixture](https://arxiv.org/abs/2511.07110)**
  - *Tian-Hao Fu, Xin-Xin Xu, Weichen Xu et al.*
  - **AAAI 2025** · `2025-11-10`
  - Market making (MM) through Reinforcement Learning (RL) has attracted significant attention in financial trading. With the development of Large Language Models (LLMs), more and more attempts are being made to apply LLMs to financial areas. A simple, direct application of LLM as an…

- **[TimeCAP: Learning to Contextualize, Augment, and Predict Time Series Events with Large Language Model Agents](https://arxiv.org/abs/2502.11418)**
  - *Ge-On Lee, Wen-Chao Yu, Kijung Shin et al.*
  - **AAAI 2025** · `2025-02-17`
  - Time series data is essential in various applications, including climate modeling, healthcare monitoring, and financial analytics. Understanding the contextual information associated with real-world time series data is often essential for accurate and reliable event predictions.…


### ICML

- **[TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration](https://openreview.net/forum?id=bz651zjpyk)**
  - **ICML 2025** · OpenReview · `2026-10-13`
  - LLM-based agents can automate model post-training, accelerating progress toward recursive self-improvement. Despite their promise, existing approaches remain under-explored and face two main challenges: (1) strategy lock-in that limits exploration beyond the initial strategy; and…

- **[ARTE: Agentic Refinement through Trade Execution for High-Frequency Trading Strategy Discovery](https://openreview.net/forum?id=VisvXioWmG)**
  - **ICML 2025** · OpenReview · `2026-10-12`
  - Existing LLM-based trading strategy development primarily uses aggregated price and volume data, which omit within-interval event order and displayed order book changes. Tick-level trade and quote observations preserve this information, but their scale makes the full history impr…

- **[Harness Self-Evolution: Theory, Algorithms, Evaluation, Applications, and Impact](https://openreview.net/forum?id=m5jsFGXUM2)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - **ICML 2025** · OpenReview · `2026-10-11`
  - Building agents that learn from experience is a central goal of artificial intelligence. Harness self-evolution offers a path toward this goal by adapting the system around a fixed base model. This article develops a unified framework for examining how execution feedback produces…

- **[DS-Lighting: Making Agent Harnesses Explicit for Data-Science Automation](https://openreview.net/forum?id=m7wsVqhIYs)**
  - **ICML 2025** · OpenReview · `2026-10-11`
  - Large Language Model (LLM) agents have shown promise for automating data-science workflows, yet their end-to-end performance depends critically on the agent harness that represents tasks, manages execution state, constrains output artifacts, and provides evaluation feedback. Exis…

- **[FLRT: Learning Efficient Tool Use from Tool-Sufficient States](https://openreview.net/forum?id=1OmQc2z5qY)**
  - **ICML 2025** · OpenReview · `2026-09-19`
  - Tool-augmented reasoning substantially extends the capability of large language models to solve complex problems, but frequent tool use also incurs additional interaction and execution costs. We observe that tool necessity changes dynamically along a reasoning trajectory: a model…

- **[TradingArena: A Market-Making Benchmark for Ranking, Diagnosing, and Steering LLM Behavior](https://openreview.net/forum?id=6VObvVwaGZ)**
  - **ICML 2025** · OpenReview · `2026-09-19`
  - As large language models are increasingly deployed as agents, evaluation should capture both task performance and interactive behavior. Few benchmarks jointly measure performance and behavior under controlled changes to an agent’s information, action space, and inference. We intr…

- **[Can Harness Optimization Improve Agents? Generalizable Gains Versus Evaluation Noise](https://openreview.net/forum?id=Ri0rU3rPOS)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Harness optimization methods revise an agent’s prompts, tools, memory, and run-
time control without updating model weights. We ask which of their improve-
ments can be distinguished from evaluation noise, and where the reliable ones
come from. We evaluate Meta-Harness, Agentic H…

- **[TAME: Transfer-Aware Model-Harness Co-Evolution through Learned Harness Revisions](https://openreview.net/forum?id=IXnpSW8g3v)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Agentic post-training relies on an execution harness that both assists the model and shapes the trajectories from which it learns. A harness that improves immediate success, however, need not produce capability that transfers when that support changes. We examine this distinction…

- **[Harness-Zero: Harness Distillation via Agent-as-Harness](https://openreview.net/forum?id=rZ7eO7DZmc)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent…

- **[Hypothesis-Conditioned Evaluation for Efficient Harness Optimization](https://openreview.net/forum?id=q55gCb73ub)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Harness optimization improves an LLM agent by editing its prompts, tools
and helper code with model weights fixed. Evaluating every edit on
every training task is expensive, but a small random sample can miss the
failure that motivated the edit. We introduce \emph{Hypothesis-Cond…

- **[Harness-Delta Attribution: Dissecting Gains From Harness Evolution](https://openreview.net/forum?id=PX4Zpvsaca)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Harness evolution automatically optimizes the prompts, skills, tools, and orchestration code around a fixed-weight model, offering a way to improve agentic systems without updating model weights. The agent harness is iteratively optimized to achieve higher performance on the sear…

- **[Visual Reasoning at the Harness Level: A Ladder for Controlled Evaluation](https://openreview.net/forum?id=8Rdl9qkU1A)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Advances in foundation models are shifting coding and working agents from predefined tools toward general computational environments. Yet existing visual agents often couple model, harness, and training choices, making it difficult to determine how this transition affects visual…

- **[AURA-Eval: Evaluation Framework for Acting Under Risk Awareness in LLM Agent Trajectories](https://openreview.net/forum?id=9XfH1iAA4W)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - LLM agents are increasingly taking actions with real consequences, yet safety evaluations often reduce their behavior to a final safe or unsafe outcome, obscuring whether the agent recognized the risk and how it responded. We introduce AURA-Eval, a framework for evaluating whethe…

- **[ParaFusionBench: A Unified Benchmark for Cross-Paradigm Fusion in Factor Mining and Trading Decision-Making](https://openreview.net/forum?id=nqb5xH3QuC)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Quantitative investment research has evolved from conventional models to large language models (LLMs) and multi-agent collaboration, forming two primary research trajectories: factor mining and trading decision-making. Their intersection yields four paradigms: Conventional Factor…

- **[Rethinking the Evaluation of Harness Evolution for Agents](https://openreview.net/forum?id=QDdWiaNkk2)**
  - **ICML 2025** · OpenReview · `2026-09-17`
  - Harness evolution is an iterative search procedure that repeatedly evaluates and revises candidate harnesses used for LLM agents using task feedback. We revisit the evaluation of such automatic harness evolution procedures and identify two fundamental issues in the protocol. Firs…

- **[Harness-MAP: Budget-Efficient Harness Search via Structure-Token Factorization](https://openreview.net/forum?id=HM48DQvAqS)**
  - **ICML 2025** · OpenReview · `2026-09-17`
  - Automating harness evolution via naive meta-agent search is prohibitively expensive, requiring hundreds of meta-agent calls and minutes-to-hours per evaluation.
How can we efficiently search for a diverse set of high-quality harnesses under a tight evaluation budget?
To address t…

- **[FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors](https://openreview.net/forum?id=RKKGxm7O4L)**
  - **ICML 2025** · OpenReview · `2026-09-16`
  - As AI agents are becoming widely adopted in the financial services industry, careful measurement is essential to understand where they can be reliably deployed and where oversight and professional review remain necessary. Such measurement, however, is constrained by limited acces…

- **[PortfolioRouter: Consequence-Aware Multi-Task Routing for Portfolio Agents](https://openreview.net/forum?id=My6dyV7ecS)**
  - **ICML 2025** · OpenReview · `2026-09-14`
  - Portfolio agents can recommend materially different allocations for the same trading date, but standard best-expert classification does not weight errors by their financial cost. The cost of a routing error depends on the return forgone by choosing one proposal over another. We i…

- **[Turbo Harness: Instance-Adaptive Harness Optimization](https://openreview.net/forum?id=Iyc8G0eNib)**
  - **ICML 2025** · OpenReview · `2026-09-13`
  - Designing effective harnesses with minimal human intervention is an important challenge for building modern agents. Existing automated harness optimization methods typically produce a single global harness that is applied uniformly across future problem instances. However, a harn…

- **[CHART: A Harness-Rotation Curriculum for Harness-Robust Search Agents](https://openreview.net/forum?id=HdwZqmT4Ld)**
  - *{'username': '~Xinlu_Zhang1', 'fullname': 'Xinlu Zhang', 'institutions': [{'name': 'Amazon', 'domain': 'amazon.com', 'country': 'US'}]}, {'username': '~Ying-Chun_Lin2', 'fullname': 'Ying-Chun Lin', 'institutions': [{'name': 'Amazon', 'domain': 'amazon.com', 'country': 'US'}]}, {'username': '~Zhihan_Zhang2', 'fullname': 'Zhihan Zhang', 'institutions': [{'name': 'Amazon', 'domain': 'amazon.com', 'country': 'US'}]} et al.*
  - **ICML 2025** · OpenReview · `2026-08-28`
  - Search agents are usually trained under a single harness. But once an agent is deployed in a real application, its harness is frequently updated (e.g., a rewritten system prompt) to fit production needs. This exposes a fragility of post-trained agents: because a learned behavior…

- **[Harness Engineering for LLM Agents: A Survey of Harness Component Taxonomy, Evaluation, and Model--Harness Coevolution](https://openreview.net/forum?id=1VJLY0hAFT)**
  - **ICML 2025** · OpenReview · `2026-07-03`
  - As large language model-driven autonomous agents are increasingly deployed in real-world long-horizon, open-environment tasks, foundation models expose systematic capability gaps in context retention, reliable tool invocation, persistent state management, and multi-step execution…

- **[A Fraud-Detection-Inspired Framework for LLM Agents Security](https://openreview.net/forum?id=uUipgSY8Sh)**
  - *Sheldon Yu, Yingcheng Sun, Hanqing Guo et al.*
  - **ICML 2025** · OpenReview · `2026-06-12`
  - Large Language Model (LLM) agents demonstrate strong capabilities in autonomous task execution, tool use, and multi-step reasoning. However, their increasing autonomy also introduces a new attack surface: adversarial interactions can manipulate agent behavior through direct promp…

- **[The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation](https://openreview.net/forum?id=1sqKRqsaE9)**
  - *Naman Vats, Oleg Aleksandrovich Golev*
  - **ICML 2025** · OpenReview · `2026-06-10`
  - Public leaderboards for coding agents typically rank systems by model name and pass rate, while the surrounding harness—the scaffold that issues tools, manages context, and decides when to stop—is often under-specified. Model-to-model comparison is valid when the harness is fixed…

- **[Scanner-Aware Coordinated Attacks on LLM Agent Skills](https://openreview.net/forum?id=HiqcfJyIUF)**
  - *Tongyan Hu, Xiaogeng Liu, Bryan Hooi et al.*
  - **ICML 2025** · OpenReview · `2026-06-05`
  - With the rapid development of Large Language Model (LLM) agents, these agents increasingly rely on skills—modular capabilities that combine natural language specifications with executable code across multiple modalities—to extend agent behavior at scale. As skills become a key me…

- **[FairCoder: Probing LLM Bias in High-Stakes Decision Making via Coding Tasks](https://openreview.net/forum?id=n7Mk11IVX8)**
  - *Yongkang Du, Jen-tse Huang, Jieyu Zhao et al.*
  - **ICML 2025** · OpenReview · `2026-06-03`
  - Large language models (LLMs) are increasingly used in high-stakes decisions such as hiring and college admissions, making their social bias a critical concern. While LLMs are trained to refuse explicitly biased requests, bias can be leaked implicitly during LLM planning and reaso…

- **[Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety](https://openreview.net/forum?id=7UXZAFMvpZ)**
  - *Lifei Liu, Haoran Yu, Xiaochong Jiang et al.*
  - **ICML 2025** · OpenReview · `2026-05-26`
  - Safety evaluations of multi-agent LLM systems often compare a direct prompt against a planner-executor pipeline and report the difference as a single "pipeline effect." This aggregate hides
  several simultaneous changes: harmful intent may be recast as plausible operational work…

- **[AgenticRec: A Recommendation-Oriented Agentic Framework with Progressive Tool-Integrated Reasoning Optimization](https://openreview.net/forum?id=hrSwV2oSqz)**
  - **ICML 2025** · OpenReview · `2026-05-26`
  - Recommender agents built on Large Language Models offer a promising paradigm for personalized recommendation. However, existing agents typically suffer from a misalignment between their tool-integrated reasoning trajectories and recommendation feedback, limiting their ability to…

- **[AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing](https://openreview.net/forum?id=IzKJV1g5jX)**
  - **ICML 2025** · OpenReview · `2026-05-17`
  - Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts.
Recent reinforcement learnin…

- **[AEVAL: From Anecdotal to Deterministic Testing for Agentic Skill Workflows](https://openreview.net/forum?id=tpEflAIlo5)**
  - *Tejas Singh Anand, Yuet Ying Christina Wang, Wanting Jiang et al.*
  - **ICML 2025** · OpenReview · `2026-05-02`
  - Modern agentic systems increasingly rely on skills: installable packages of natural language and code that teach an LLM agent how to perform a domain task. As skill repositories grow, developers need automated, trustworthy quality signals on every change to a skill, yet most eval…

- **[Towards Direct Evaluation of Harness Optimizers via Priority Ranking](https://arxiv.org/abs/2605.22505)**
  - *{'fullname': 'Kai Tzu-iunn Ong', 'username': ''}, {'fullname': 'Minseok Kang', 'username': ''}, {'fullname': 'Dongwook Choi', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2026-05-01`
  - Harness optimization enables automated agent creation by having an optimizer agent iteratively update the harness of target agents. Despite its success, current studies evaluate optimizers solely by observing target agents' performance gains. This indirect end-improvement evaluat…

- **[The Tool Illusion: Rethinking Tool Use in Web Agents](https://openreview.net/forum?id=gQwin40zgt)**
  - *Renze Lou, Baolin Peng, Wenlin Yao et al.*
  - **ICML 2025** · OpenReview · `2026-03-14`
  - As web agents rapidly evolve, an increasing body of work has moved beyond conventional atomic browser interactions and explored tool use as a higher-level action paradigm. Although prior studies have shown the promise of tools, their conclusions are often drawn from limited exper…

- **[AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2603.20213)**
  - *{'fullname': 'Jiaqi Yuan', 'username': ''}, {'fullname': 'Jialu Wang', 'username': ''}, {'fullname': 'Zihan Wang', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2026-03-01`
  - Generative search engines represent a transition from traditional ranking-based retrieval to Large Language Model (LLM)-based synthesis, transforming optimization goals from ranking prominence towards content inclusion. Generative Engine Optimization (GEO), specifically, aims to…

- **[Modeling Fairness as an Evolving Social Consensus via LLM-Based Multi-Agent Simulation](https://openreview.net/forum?id=BEA4PVipWF)**
  - **ICML 2025** · OpenReview · `2026-02-20`

- **[A multi-agent system for financial retrieval](https://openreview.net/forum?id=X86jxEIVtX)**
  - **ICML 2025** · OpenReview · `2026-02-11`

- **[Locomo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents](https://openreview.net/forum?id=QGJrLaES6h)**
  - *{'fullname': 'Yifei Li', 'username': ''}, {'fullname': 'Weidong Guo', 'username': ''}, {'fullname': 'Lingling Zhang', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2026-01-01`
  - Long-term conversational memory is a core capability for LLM-baseddialogue systems, yet existing benchmarks and evaluation protocolsprimarily focus on surface-level factual recall.In realistic interactions, appropriate responses often depend onimplicit constraints such as user st…

- **[Conversational Agents: A Framework for Evaluation (CAFE) (Dagstuhl Perspectives Workshop 24352)](https://openreview.net/forum?id=rpLDo1d8oU)**
  - *{'fullname': 'Christine Bauer', 'username': '~Christine_Bauer1'}, {'fullname': 'Li Chen'}, {'fullname': 'Nicola Ferro'} et al.*
  - **ICML 2025** · OpenReview · `2025-12-19`
  - During the workshop, we deeply discussed what CONversational Information ACcess (CONIAC) is and its unique features, proposing a world model abstracting it, and defined the Conversational Agents Framework for Evaluation (CAFE) for the evaluation of CONIAC systems, consisting of s…

- **[Text to SQL in Agentics](https://openreview.net/forum?id=DcmJC1HLUk)**
  - **ICML 2025** · OpenReview · `2025-11-21`

- **[RAPTOR: Reasoned Agentic Portfolio Trading with Orchestrated Rebalancing](https://openreview.net/forum?id=ziuTkKhgT0)**
  - *Blake Almon, Matthew Caliboso, Alex Kim et al.*
  - **ICML 2025** · OpenReview · `2025-10-28`
  - We propose an institutional-style, multi-agent architecture for equity portfolio construction that couples a schema-constrained blackboard with structured debate and a Black-Litterman optimizer, enabling diversified, risk-aware allocations. The system is scalable, modular, and in…

- **[AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation](https://arxiv.org/abs/2510.19361)**
  - *Xianyang Liu, Yilin Liu, Shuai Wang et al.*
  - **ICML 2025** · OpenReview · `2025-10-01`
  - The creation of high-quality datasets to improve Large Language Model (LLM) reasoning remains a significant challenge, as current methods often suffer from generating low-quality/incorrect answers and limited information richness from available data sources. To address this, we p…

- **[AgentRace: Benchmarking Efficiency in LLM Agent Frameworks](https://openreview.net/forum?id=eUuxWAQA5F)**
  - *Yanling Xu, bangwei zeng, Zeyu Qiu et al.*
  - **ICML 2025** · OpenReview · `2025-09-19`
  - Large Language Model (LLM) agents are rapidly gaining traction across domains such as intelligent assistants, programming aids, and autonomous decision systems. While existing benchmarks focus primarily on evaluating the effectiveness of LLM agents, such as task success rates and…

- **[AgenticIQA: An Agentic Framework for Adaptive and Interpretable Image Quality Assessment](https://openreview.net/forum?id=PZq5RtJDUK)**
  - *Hanwei Zhu, Yu TIAN, Keyan Ding et al.*
  - **ICML 2025** · OpenReview · `2025-09-18`
  - Image quality assessment (IQA) is inherently complex, as it reflects both the quantification and interpretation of perceptual quality rooted in the human visual system. Conventional approaches typically rely on fixed models to output scalar scores, limiting their adaptability to…

- **[AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation](https://openreview.net/forum?id=2aA6YwZYOJ)**
  - *Xianyang Liu, Yilin LIU, Shuai Wang et al.*
  - **ICML 2025** · OpenReview · `2025-09-18`
  - The creation of high-quality datasets to improve Large Language Model (LLM) reasoning remains a significant challenge, as current methods often suffer from generating low-quality/incorrect answers and limited information richness from available data sources. To address this, we p…

- **[Multi-target Parallel Drug Discovery with Multi-agent Orchestration](https://openreview.net/forum?id=AhFsKmuaCb)**
  - *AI Agent, Fuad Al Abir, Sixue Zhang et al.*
  - **ICML 2025** · OpenReview · `2025-09-17`
  - The immense cost and high failure rates of traditional drug discovery necessitate a shift towards more systematic, automated approaches. While specialized AI tools have excelled at individual tasks, their integration into a cohesive, end-to-end discovery workflow remains a signif…

- **[Economic Confidentiality without Secrets: Making Intercepted LLM-Agent Communications Unusable](https://openreview.net/forum?id=sJbC5vtT2v)**
  - *Bolaji Makinde*
  - **ICML 2025** · OpenReview · `2025-09-16`
  - We study whether LLM agents can exchange useful information over a public channel without secrets (no keys, no TEEs) while making unauthorized decoding economically impractical. We formalize an “economic confidentiality” objective and design a stochastic “private language” ${L_r}…

- **[QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading](https://openreview.net/forum?id=fdKmhFYcQv)**
  - *Fei Xiong, Xiang Zhang, Aosong Feng et al.*
  - **ICML 2025** · OpenReview · `2025-09-08`
  - Recent advances in Large Language Models (LLMs) have shown remarkable capabilities in financial reasoning and market understanding. Multi-agent LLM frameworks such as TradingAgent and FINMEM augment these models to long-horizon investment tasks by leveraging fundamental and senti…

- **[The Social Laboratory: A Psychometric Framework for Multi-Agent LLM Evaluation](https://openreview.net/forum?id=5Larp1U1Mq)**
  - *Zarreen Reza*
  - **ICML 2025** · OpenReview · `2025-09-05`
  - As Large Language Models (LLMs) transition from static tools to autonomous agents, traditional evaluation benchmarks that measure performance on downstream tasks are becoming insufficient. These methods fail to capture the emergent social and cognitive dynamics that arise when ag…

- **[Medical AI Consensus: A Multi-Agent Framework for  Radiology Report Generation and Evaluation](https://openreview.net/forum?id=BwvWrnPzfZ)**
  - *Ahmed Tamer El Boardy, Ghada Khoriba, Essam Rashed*
  - **ICML 2025** · OpenReview · `2025-09-05`
  - Automating radiology report generation poses a dual challenge: building clinically reliable systems and designing rigorous evaluation protocols. We introduce a multi-agent reinforcement learning framework that serves as both a benchmark and evaluation environment for multimodal c…

- **[A Protocol-Driven Platform for Agent-Agnostic Evaluation of LLM Agents](https://openreview.net/forum?id=G9YKfCddN3)**
  - *Cong Minh Tran, Issam Falih, Hatim CHAHDI et al.*
  - **ICML 2025** · OpenReview · `2025-09-05`
  - The fast growth of LLM-based agents has outpaced efforts to build solid evaluation standards, causing mismatched formats and idiosyncratic reporting that often makes fair comparisons challenging. To tackle this, we created a platform around a protocol-based setup that keeps evalu…

- **[How to Train Your LLM Web Agent: A Statistical Diagnosis](https://openreview.net/forum?id=HBx2K7SVYh)**
  - *Dheeraj Vattikonda, Santhoshi Ravichandran, Emiliano Penaloza et al.*
  - **ICML 2025** · OpenReview · `2025-09-03`
  - LLM-based web agents have recently made significant progress, but much of it has
occurred in closed-source systems—widening the gap with open-source alternatives.
Progress has been held back by two key challenges—first, a narrow focus on single-
step tasks that overlooks the comp…

- **[AsymPuzl: An Asymmetric Puzzle for multi-agent cooperation](https://openreview.net/forum?id=SXcJh8hoLz)**
  - *Xavier Cadet, Edward Koh, Peter Chin*
  - **ICML 2025** · OpenReview · `2025-09-03`
  - Large Language Model (LLM) agents are increasingly studied in multi-turn, multi-agent scenarios, yet most existing setups emphasize open-ended role-play rather than controlled evaluation.
We introduce AsymPuzl, a minimal but expressive two-agent puzzle environment designed to iso…

- **[Toward Community-Driven Agents for Machine Learning Engineering](https://openreview.net/forum?id=aKChEjaJpZ)**
  - *Sijie Li, Weiwei Sun, Shanda Li et al.*
  - **ICML 2025** · OpenReview · `2025-09-03`
  - Large language model-based machine learning (ML) agents have shown great promise in automating ML research.
However, existing agents typically operate in isolation on a given research problem, without engaging with the broader research community, where human researchers often gai…

- **[Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design and Credit Assignment](https://openreview.net/forum?id=drP7qVUnUt)**
  - *Quan Wei, Siliang Zeng, Chenliang Li et al.*
  - **ICML 2025** · OpenReview · `2025-09-02`
  - This paper investigates approaches to enhance the reasoning capabilities of Large Language Model (LLM) agents using Reinforcement Learning (RL).  Specifically, we focus on long-horizon multi-turn agent scenarios, which can be naturally modeled as Markov Decision Processes.  Altho…

- **[Orchestrator: Active Inference for Multi-Agent Systems in Long-Horizon Tasks](https://openreview.net/forum?id=21sPEvGUL2)**
  - *Lukas Beckenbauer, Johannes-Lucas Löwe, Ge Zheng et al.*
  - **ICML 2025** · OpenReview · `2025-09-02`
  - Complex, non-linear tasks challenge LLM-enhanced multi-agent systems (MAS) due to partial observability and suboptimal coordination. We propose Orchestrator, a novel MAS framework that leverages attention-inspired self-emergent coordination and reflective benchmarking to optimize…

- **[The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets](https://openreview.net/forum?id=XZpIu68yW6)**
  - *Shenzhe Zhu, Jiao Sun, Yi Nian et al.*
  - **ICML 2025** · OpenReview · `2025-09-01`
  - AI agents are increasingly used in consumer-facing applications to assist with tasks such as product search, negotiation, and transaction execution. In this paper, we investigate a future setting where both consumers and merchants authorize AI agents to automate the negotiations…

- **[Multi-Turn LLM Systems for Diagnostic Decision-Making: Considerations, Biases, and Challenges](https://openreview.net/forum?id=It7AgR3A9H)**
  - *Benjamin Liu, Sejong Kim, Drona Thoka et al.*
  - **ICML 2025** · OpenReview · `2025-09-01`
  - This study investigates the systemic limitations and architectural design trade-offs of Large Language Model multi-agent systems (LLM-MAS) for clinical decision support, focusing on how agent collaboration and architectural choices influence reasoning in complex medical problems.…

- **[Offline Policy Evaluation of Multi-Turn LLM Health Coaching with Real Users](https://openreview.net/forum?id=BE00LfP4Dv)**
  - *Melik Ozolcer, Sang Won Bae*
  - **ICML 2025** · OpenReview · `2025-09-01`
  - We study a web-deployed, tool-augmented LLM health coach with real users. In a pilot with seven users (280 rated turns), offline policy evaluation (OPE) over factorized decision heads (Tool/Style) shows that a uniform heavy-tool policy raises average value on logs but harms speci…

- **[Traxgen: Ground-Truth Trajectory Generation for AI Agent Evaluation](https://openreview.net/forum?id=pERJAy5kI1)**
  - *Maria Emilia Mazzolenis, Ruirui Zhang*
  - **ICML 2025** · OpenReview · `2025-09-01`
  - As AI agents take on complex, goal-driven workflows, response-level evaluation becomes insufficient. Trajectory‐level evaluation offers deeper insight but typically relies on high‑quality reference trajectories that are costly to curate or prone to LLM noise. We introduce \texttt…

- **[Disclosure Audits for LLM Agents](https://openreview.net/forum?id=BV6QBwZkfK)**
  - *Saswat Das, Jameson Sandler, Ferdinando Fioretto*
  - **ICML 2025** · OpenReview · `2025-09-01`
  - LLM agents have begun to appear as personal assistants, customer service bots, and clinical aides. While these applications deliver substantial operational benefits, they also require continuous access to sensitive data, which increases the likelihood of unauthorized disclosures.…

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://openreview.net/forum?id=7AetgL7eVL)**
  - *Jiaju Chen, Yuxuan Lu, Xiaojie Wang et al.*
  - **ICML 2025** · OpenReview · `2025-08-31`
  - Nearly all human work is collaborative; thus, the evaluation of real-world NLP applications often requires multiple dimensions that align with diverse human perspectives. As real human evaluator resources are often scarce and costly, the emerging “LLM-as-a-judge” paradigm sheds l…

- **[RAFFLES: Reasoning-based Attribution of Faults for LLM Systems](https://openreview.net/forum?id=0oxelK4W6c)**
  - *Chenyang Zhu, Spencer Hong, Jingyu Wu et al.*
  - **ICML 2025** · OpenReview · `2025-08-29`
  - We have reached a critical roadblock in the development and enhancement of long-horizon, multi-component LLM agentic systems: it is incredibly tricky to identify where these systems breakdown and why. Evaluation capabilities that currently exist today (e.g., single pass LLM-as-a-…

- **[Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning](https://openreview.net/forum?id=WYfzRJgWbO)**
  - *Shuo Liu, Tianle Chen, Christopher Amato*
  - **ICML 2025** · OpenReview · `2025-08-22`
  - A large amount of work has been done in Multi-Agent Systems (MAS) for modeling and solving problems with multiple interacting agents.  However, most LLMs are pretrained independently and not specifically optimized for coordination. Existing LLM fine-tuning frameworks rely on indi…

- **[CORE: Measuring Multi-Agent LLM Interaction Quality under Game-Theoretic Pressures](https://openreview.net/forum?id=cArAB6Sj5X)**
  - *Punya Syon Pandey, Yongjin Yang, Jiarui Liu et al.*
  - **ICML 2025** · OpenReview · `2025-08-17`
  - Game-theoretic interactions between agents with Large Language Models (LLMs) have revealed many emergent capabilities, yet the linguistic diversity of these interactions has not been sufficiently quantified. In this paper, we present the Conversational Robustness Evaluation Score…

- **[Scalability of LLM-Based Multi-Agent Systems for Scientific Code Generation: A Preliminary Study](https://openreview.net/forum?id=h8KFX5HM3N)**
  - *Yuru Wang, Kaiyan Zhang, Kai Tian et al.*
  - **ICML 2025** · OpenReview · `2025-08-16`
  - Recent studies indicate that LLM-based Multi-Agent Systems (MAS) encounter scalability challenges in complex mathematical problem-solving or coding tasks, exhibiting issues such as inconsistent role adherence and ineffective inter-agent communication. Moreover, the performance ad…

- **[Agentic Design Review System](https://arxiv.org/abs/2508.10745)**
  - *Sayan Nag, K. J. Joseph, Koustava Goswami et al.*
  - **ICML 2025** · OpenReview · `2025-08-01`
  - Evaluating graphic designs involves assessing it from multiple facets like alignment, composition, aesthetics and color choices. Evaluating designs in a holistic way involves aggregating feedback from individual expert reviewers. Towards this, we propose an Agentic Design Review…

- **[TradingGroup: A Multi-Agent Trading System with Self-Reflection and Data-Synthesis](https://arxiv.org/abs/2508.17565)**
  - *Feng Tian, Flora D. Salim, Hao Xue*
  - **ICML 2025** · OpenReview · `2025-08-01`
  - Recent advancements in large language models (LLMs) have enabled powerful agent-based applications in finance, particularly for sentiment analysis, financial report comprehension, and stock forecasting. However, existing systems often lack inter-agent coordination, structured sel…

- **[Tool-as-Interface: Learning Robot Policies from Observing Human Tool Use](https://openreview.net/forum?id=5udqMOeai1)**
  - *Haonan Chen, Cheng Zhu, Shuijing Liu et al.*
  - **ICML 2025** · OpenReview · `2025-05-10`
  - Tool use is essential for enabling robots to perform complex real-world tasks, but learning such skills requires extensive datasets. While teleoperation is widely used, it is slow, delay-sensitive, and poorly suited for dynamic tasks. In contrast, human videos provide a natural w…

- **[Establishing Best Practices in Building Rigorous Agentic Benchmarks](https://openreview.net/forum?id=E58HNCqoaA)**
  - *Yuxuan Zhu, Tengjun Jin, Yada Pruksachatkun et al.*
  - **ICML 2025** · OpenReview · `2025-05-01`
  - Benchmarks are essential for quantitatively tracking progress in AI. As AI agents become increasingly capable, researchers and practitioners have introduced agentic benchmarks to evaluate agents on complex, real-world tasks. These benchmarks typically measure agent capabilities b…

- **[AIOS: LLM Agent Operating System](https://openreview.net/forum?id=L4HHkCDz2x)**
  - *Kai Mei, Xi Zhu, Wujiang Xu et al.*
  - **ICML 2025** · OpenReview · `2025-03-19`
  - LLM-based intelligent agents face significant deployment challenges, particularly related to resource management. Allowing unrestricted access to LLM or tool resources can lead to inefficient or even potentially harmful resource allocation and utilization for agents. 
Furthermore…

- **[Conversational Agents: A Framework for Evaluation (CAFE)](https://openreview.net/forum?id=s4QQ6uxQcx)**
  - *{'fullname': 'Christine Bauer', 'username': '~Christine_Bauer1'}, {'fullname': 'Li Chen'}, {'fullname': 'Nicola Ferro'} et al.*
  - **ICML 2025** · OpenReview · `2025-03-19`
  - This report documents the program and the outcomes of the Dagstuhl Perspectives Workshop 24352, "Conversational Agents: A Framework for Evaluation (CAFE)", which brought together 22 distinguished researchers and practitioners from 12 countries. In this workshop, a new framework f…

- **[AgenticHypothesis: A Survey on Hypothesis Generation Using LLM Systems](https://openreview.net/forum?id=UeeyfR4CUg)**
  - *Adib Bazgir, Rama chandra Praneeth Madugula, Yuwen Zhang*
  - **ICML 2025** · OpenReview · `2025-02-10`
  - Hypothesis generation is a cornerstone of scientific discovery, enabling researchers to formulate testable ideas that drive innovation and progress. Although traditional methods have proven effective, they are often constrained by cognitive biases, information overload, and time…

- **[agenticMSA: Agentic Multimodal Sentiment Analysis with Task-Specific and Large Language Model Collaboration](https://openreview.net/forum?id=ATwJ8MWnth)**
  - **ICML 2025** · OpenReview · `2025-02-10`
  - Multimodal Sentiment Analysis (MSA) faces challenges due to inconsistencies between modalities, such as conflicting sentiment cues from visual, audio, and text data. These modality conflicts make it difficult for previous task-specific samll-scale models to accurately predict sen…

- **[Performant LLM Agentic Framework for Conversational AI](https://openreview.net/forum?id=JDXB6nvH9x)**
  - *Alex Casella, Wayne Wang*
  - **ICML 2025** · OpenReview · `2025-01-22`
  - The rise of Agentic applications and automation in the Voice AI industry has led to an increased reliance on Large Language Models (LLMs) to navigate graph-based logic workflows composed of nodes and edges. However, existing methods face challenges such as alignment errors in com…

- **[Social Agentics](https://openreview.net/forum?id=yzWu4VvAXE)**
  - *{'fullname': 'Matt Ratto', 'username': '~Matt_Ratto1'}, {'fullname': 'Anastasia Kuzminykh', 'username': ''}, {'fullname': 'Shion Guha', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2025-01-01`
  - Agentic AI is being heralded as the next step in the development of AI systems. Agentics, complex ensembles of different machine learning, data processing, and generative AI models, can provide new autonomous and proactive decision-making capabilities to organizations, participat…

- **[Trading Confidence: Comprehensive Uncertainty Estimation in Algorithmic Trading](https://openreview.net/forum?id=IWDsycHMSP)**
  - *Lin Li, Li Rong Wang, Hsuan Fu et al.*
  - **ICML 2025** · OpenReview · `2025-01-01`
  - Description Reinforcement Learning (RL) has emerged as a powerful approach in financial trading, enabling agents to learn optimal strategies through direct market interaction. However, financial markets are highly uncertain, with price fluctuations driven by stochastic volatility…

- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://openreview.net/forum?id=4QPrXwMQt1)**
  - *Yijia Xiao, Edward Sun, Di Luo et al.*
  - **ICML 2025** · OpenReview · `2024-12-02`
  - Significant progress has been made in automated problem-solving using societies of agents powered by large language models (LLMs). In finance, efforts have largely focused on single-agent systems handling specific tasks or multi-agent frameworks independently gathering data. Howe…

- **[An Intelligent Agentic System for Complex Image Restoration Problems](https://openreview.net/forum?id=3RLxccFPHz)**
  - *Kaiwen Zhu, Jinjin Gu, Zhiyuan You et al.*
  - **ICML 2025** · OpenReview · `2024-09-26`
  - Real-world image restoration (IR) is inherently complex and often requires combining multiple specialized models to address diverse degradations. Inspired by human problem-solving, we propose AgenticIR, an agentic system that mimics the human approach to image processing by follo…

- **[FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://openreview.net/forum?id=sstfVOwbiG)**
  - *Haohang Li, Yangyang Yu, Zhi Chen et al.*
  - **ICML 2025** · OpenReview · `2024-02-03`
  - Recent advancements in Large Language Models (LLMs) have exhibited notable efficacy in natural language processing (NLP) tasks across diverse domains. Their prowess in integrating extensive knowledge has fueled interest in developing LLM-based autonomous agents. Furthermore, in t…

- **[An Intelligent Agentic System for Complex Image Restoration Problems](https://arxiv.org/abs/2410.17809)**
  - *Kaiwen Zhu, Jinjin Gu, Zhiyuan You et al.*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - Real-world image restoration (IR) is inherently complex and often requires combining multiple specialized models to address diverse degradations. Inspired by human problem-solving, we propose AgenticIR, an agentic system that mimics the human approach to image processing by follo…

- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)**
  - *Yijia Xiao, Edward Sun, Di Luo et al.*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - Significant progress has been made in automated problem-solving using societies of agents powered by large language models (LLMs). In finance, efforts have largely focused on single-agent systems handling specific tasks or multi-agent frameworks independently gathering data. Howe…

- **[ChEF: A Comprehensive Evaluation Framework for Standardized Assessment of Multimodal Large Language Models](https://openreview.net/forum?id=ClqyY6Bvb7)**
  - *Zhelun Shi, Zhipin Wang, Hongxing Fan et al.*
  - **ICML 2025** · OpenReview · `2023-09-15`
  - Multimodal Large Language Models (MLLMs) have shown impressive abilities in interacting with visual content with myriad potential downstream tasks. However, even though a list of benchmarks has been proposed, the capabilities and limitations of MLLMs are still not comprehensively…

- **[Cryptocurrency Trading Agent Using Deep Reinforcement Learning](https://openreview.net/forum?id=XW3tnMhPFu)**
  - *Uwais Suliman, Terence L. van Zyl, Andrew Paskaramoorthy*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - Cryptocurrencies are peer-to-peer digital assets monitored and organised by a blockchain network. Price prediction has been a significant focus point with various machine learning algorithms, especially concerning cryptocurrency. This work addresses the challenge faced by traders…

- **[Trading Agents](https://openreview.net/forum?id=8QTqyKAeeN)**
  - *Michael P. Wellman*
  - **ICML 2025** · OpenReview · `2011-01-01`
  - Automated trading in electronic markets is one of the most common and consequential applications of autonomous software agents.


### ICLR

- **[ASTOR: Benchmarking and Improving Autoformulation for Soft-Constraint Optimization with a Formal Grammar](https://arxiv.org/abs/2610.26819v1)**
  - *Amer Goel, Yeganeh Alimohammadi, Andrew Daw*
  - **ICLR** · `2026-10-19`
  - Real-world decision problems combine two qualitatively different kinds of constraints: requirements that must be satisfied, called hard constraints, and preferences that can be violated, called soft constraints. Because these problems are often posed to decision-makers in natural…


### ACL

- **[Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification Agents](https://arxiv.org/abs/2610.29812v1)**
  - *Mohammed Saqlain*
  - **ACL** · `2026-10-21`
  - Literature-searching language agents are becoming a standard component of scientific assistants for the life sciences, yet there is little controlled evidence on which parts of their harness matter. We run a controlled ablation on biomedical claim verification (SciFact) with the…

- **[Inheritance as an Admission Test for LLM Prompt Merge Operators](https://arxiv.org/abs/2610.29023v1)**
  - *Zan-Kai Chong, Hiroyuki Ohsaki, Bryan Ng*
  - **ACL** · `2026-10-21`
  - Large language model (LLM) agents are often improved by iterating until a fixed verifier is done. Once that verifier saturates, the loop has nothing left to climb. We instead score agents against the current population, and a frozen panel records whether anyone got better. The pa…

- **[VeriEvolve: Evaluator-First Evolution for Tool-Using Agents](https://arxiv.org/abs/2610.29005v1)**
  - *Yueshen Li, Kamer Ali Yuksel, Gokhan Tur et al.*
  - **ACL** · `2026-10-21`
  - A central obstacle to self-improving agents is the absence of a reliable fitness signal for realistic stateful tasks. We introduce \textsc{VeriEvolve}, an evaluator-first evolution framework that constructs this missing evaluation layer before optimizing the agent. From task inst…

- **[Preference Is Not Permission: Personalizing the Auto-Purchase Line in Agentic Commerce](https://arxiv.org/abs/2610.29216v1)**
  - *Ryotaro Shimizu, Sai HtaungKham, Mo Fan*
  - **ACL** · `2026-10-21`
  - Personalized shopping benchmarks ask which item fits the user; we ask how far an agent may commit on that item, and pose learning the individual's auto-purchase line as a task. The boundary is evidence-conditioned and three-valued: whether committing is appropriate depends on the…

- **[Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models](https://arxiv.org/abs/2610.27921v1)**
  - *Zhiyuan Liu, Sicheng Liu, Haiyu Wu*
  - **ACL** · `2026-10-20`
  - A single observation can admit several plausible futures, making uncertainty an essential part of world modelling. However, quantum generative models remain underexplored for this task. We introduce Quantum-JEPA, a latent-action JEPA framework that learns distributions of future…

- **[When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines](https://arxiv.org/abs/2610.27714v1)**
  - *Yingxin Jia, Xuanyi Li*
  - **ACL** · `2026-10-20`
  - When does experience memory help a closed-loop LLM driving agent? Published gains cannot say, because the two factors we find to matter most, which warmup experiences the pool contains and what any injected tokens do to the prompt, are controlled in none of them. We answer with a…

- **[Local Allow, Global Deny: Why Per-Action Authorization Does Not Compose in LLM Agents](https://arxiv.org/abs/2610.27620v1)**
  - *Anmol Pandey, Aditya Jain, Liang Chen et al.*
  - **ACL** · `2026-10-20`
  - Autonomous LLM agents act through tools under per-action authorization: a local guard screens each tool call in isolation. We show that local authorization does not compose into global authorization. A compositional authorization failure (CAF) is a locally authorized execution, o…

- **[REM: What to Store, When to Recall, What to Forget in Experience Memory for Coding Agents](https://arxiv.org/abs/2610.27377v1)**
  - *Xinyi Lisa Chen, Pedro Herrero-Vidal, Xiaohan Chen et al.*
  - **ACL** · `2026-10-19`
  - Large language model (LLM) agents now autonomously complete long-horizon tasks, such as repository-level coding, through hundreds of think-act steps, yet the experience each run produces is rarely reused on the next. Prior memory systems concentrate on retrieval, finding the most…

- **[Certifying Repeatable Entry-Replay Witnesses for COBOL-to-Java Migration](https://arxiv.org/abs/2610.27272v1)**
  - *Andras L. Ferenczi, Mariya Bessonov, Allwyn Ponnudurai et al.*
  - **ACL** · `2026-10-19`
  - Producing synthetic data for comparison testing a migrated COBOL application is a major challenge that agentic migrations face today. Our prior paper, the Agentic Method for Deterministic Validation of Legacy Code Migration, presents a deterministic oracle to facilitate such migr…

- **[Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models](https://arxiv.org/abs/2610.25659v1)**
  - *Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk et al.*
  - **ACL** · `2026-10-19`
  - Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized tes…

- **[PACT: Plan-Augmented Coordination via Trace-Graphs for Dynamic Multi-Agent Combinatorial Optimization](https://arxiv.org/abs/2610.26671v1)**
  - *Xiao Zhou, Alex Schutz, Victor-Alexandru Darvariu et al.*
  - **ACL** · `2026-10-19`
  - Multi-agent approaches have been investigated recently as a means of improving the scalability of reinforcement learning for neural combinatorial optimization. Existing methods assume that all problem instance information is known upfront. However, real-world problems are often d…

- **[Multi-Docker-Eval: A 'Shovel of the Gold Rush' Benchmark on Automatic Environment Building for Software Engineering](https://arxiv.org/abs/2512.06915)**
  - *Kelin Fu, Tian-Yu Liu, Zeyu Shang et al.*
  - **ACL 2025** · `2025-12-07`
  - Automated environment configuration is a critical bottleneck in scaling software engineering (SWE) automation. To provide a reliable evaluation standard for this task, we present Multi-Docker-Eval benchmark. It includes 40 real-world repositories spanning 9 programming languages…


### Other / arXiv

- **[Retrieval Augmented Generation Compositionality](https://arxiv.org/abs/2610.29722)**
  - *Ido Levy, Segev Shlomov, Leshem Choshen*
  - 🤗 Featured · `2026-10-21`
  - Retrieval Augmented Generation (RAG) grounds large language models in external knowledge. Modern pipelines combine embedding, chunking, retrieval, reranking, query augmentation, context compression, and agentic verification, yet these techniques are typically evaluated one at a t…

- **[Memory-Centric Continual Learning for AI Agents](https://arxiv.org/abs/2610.29357)**
  - *Dongfang Li, Zhuoen Chen, Bonian Jia et al.*
  - 🤗 Featured · `2026-10-21`
  - Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive ret…

- **[Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use](https://arxiv.org/abs/2610.30108)**
  - *Yanzhe Chen, Ziyi Yang, Jifeng Zhu et al.*
  - 🤗 Featured · `2026-10-21`
  - Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed system…

- **[Harness Scaling for Generalizable Agentic Reinforcement Learning](https://arxiv.org/abs/2610.29458)**
  - *Fei Bai, Huatong Song, Chuan Hao et al.*
  - 🤗 Featured · `2026-10-21`
  - Agent harnesses have become a central component of modern agentic systems, shaping how models use tools, manage context, and coordinate long-horizon interaction. Realizing the benefits of these harnesses depends on how effectively the underlying model can make use of them, motiva…

- **[From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](https://arxiv.org/abs/2610.29560)**
  - *Tingwen Du, Haoyu Guo, Hanxue Zhang et al.*
  - 🤗 Featured · `2026-10-21`

- **[Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting](https://arxiv.org/abs/2610.29784)**
  - *Zhipeng Chen, Yunsen Liang, Yanxi Chen et al.*
  - 🤗 Featured · `2026-10-21`
  - Most contemporary artificial intelligence (AI) systems are released with frozen parameters and improve through external updates, whereas an ideal system would keep improving from its own experience, a capacity we call recursive self-improvement (RSI). Yet studying RSI requires an…

- **[Agentic World Action Models](https://arxiv.org/abs/2610.30136)**
  - *Zhuoyang Liu, Dantong Niu, Botong Zhang et al.*
  - 🤗 Featured · `2026-10-21`

- **[Cache Engineering for Agents](https://arxiv.org/abs/2610.28577)**
  - *Tianyu Fu, Ruoxi Wang, Zihan Min et al.*
  - 🤗 Featured · `2026-10-20`
  - Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache I/O and storage become the dominant cost. Trajectories can also exceed the LLM's maximum context len…

- **[Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698)**
  - *Kuan Zhang, Yukun Chen, Zhihao Yang et al.*
  - 🤗 Featured · `2026-10-20`
  - Scaling data, diversity and model capacity has improved embodied learning in physical environments, where diverse experiences remain grounded in shared physical laws. Whether these gains extend to virtual worlds with different visual styles, dynamics, controls, and objectives rem…

- **[AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589)**
  - *Xinxin Liu, Bingxin Xu, Wenrui Bao et al.*
  - 🤗 Featured · `2026-10-20`

- **[Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures](https://arxiv.org/abs/2610.28887)**
  - *Yujian Liu, Li An, Zelin He et al.*
  - 🤗 Featured · `2026-10-20`
  - Autonomous agents can increasingly propose ideas, modify code, and run experiments, creating an opportunity to accelerate scientific discovery using teams of collaborative AI researchers. To escape local minima in the discovery, we propose to encourage orthogonal exploration by c…

- **[Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?](https://arxiv.org/abs/2610.28763)**
  - *Ming Zhong, Stacy Li, Nicholas Carlini et al.*
  - 🤗 Featured · `2026-10-20`
  - Frontier coding agents are increasingly framed as end-to-end automated researchers, and ML for science offers a demanding test of that promise: improving a scientific model often requires domain insight beyond routine ML engineering. We introduce Agent4Sci, a long-horizon testbed…

- **[SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?](https://arxiv.org/abs/2610.26659)**
  - *Zhaoxi Zhang, Hao Liang, Linxuan Wu et al.*
  - 🤗 Featured · `2026-10-19`
  - Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through a…

- **[Agent World Model in the Wild: Computer-Use Agent Environment Synthesis](https://arxiv.org/abs/2610.26828)**
  - *Zhaoyang Wang, Qianhui Wu, Haorui Wang et al.*
  - 🤗 Featured · `2026-10-19`
  - Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model…

- **[Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams](https://arxiv.org/abs/2610.27227)**
  - *Yanan Ma, Yang Wang, David Le et al.*
  - 🤗 Featured · `2026-10-19`
  - Cooperative language-model agents can improve without weight updates by revising reusable skills, but only if a shared team reward is traced to the responsible agent and skill. Existing methods credit the skills present in each trajectory, yet presence is not responsibility: a ha…

- **[DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents](https://arxiv.org/abs/2610.19376)**
  - *Tianle Chen, Pushkar Singh, Ketan Todi et al.*
  - 🤗 Featured · `2026-10-14`

- **[Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills](https://arxiv.org/abs/2610.17860)**
  - *Letian Zhu, Han Li, Yifan Yao et al.*
  - 🤗 Featured · `2026-10-13`

- **[Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](https://arxiv.org/abs/2610.11942)**
  - *Jiaming Zhang, Xuan Wang, Fuyao Zhang et al.*
  - 🤗 Featured · `2026-10-08`

- **[Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113)**
  - *Houde Qian, Zheng Jiang, Wenyi Li et al.*
  - 🤗 · `2026-10-21`
  - Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether lar…

- **[TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments](https://arxiv.org/abs/2610.30043)**
  - *Yicheng Xu, Zhikai Xu, Ziyuan Chen et al.*
  - 🤗 · `2026-10-21`

- **[FrontierCS 2: A Benchmark for Computer Science R&D](https://arxiv.org/abs/2610.29932)**
  - *Qiuyang Mang, Wenhao Chai, Runyuan He et al.*
  - 🤗 · `2026-10-21`
  - Can LLM agents make contributions to frontier computer science R&D? We introduce FrontierCS 2, a benchmark of 48 open-ended tasks. We take a paper and the code its authors released and delete the paper's contribution. The deleted code becomes the human reference that sets the bar…

- **[Let Agents Design How They Search: Automatic Interface Optimization for Agentic Search](https://arxiv.org/abs/2610.29250)**
  - *Sangjune An, Jaeyoon Jung, Yumin Choi et al.*
  - 🤗 · `2026-10-21`
  - Agentic search depends on the interface through which a language-model agent accesses and explores a corpus. Existing interface designs are fixed by hand and applied unchanged to every corpus, although effective designs may depend on the corpus. We introduce SearchWeaver, a frame…

- **[Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents](https://arxiv.org/abs/2610.28934)**
  - *Xu Li, Simon Yu, Minzhou Pan et al.*
  - 🤗 · `2026-10-20`
  - Coding agents now complete tasks autonomously, modifying real-world state such as artifacts, software environments, and configurations along the way. Yet they show limited backup awareness: recognizing that an action will modify state that may later be needed, and preserving it b…

- **[DiffResearch: Accelerating Deep Research with Diffusion Language Models](https://arxiv.org/abs/2610.28909)**
  - *Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov et al.*
  - 🤗 · `2026-10-20`
  - Deep research systems iteratively plan, gather evidence, synthesize, and revise, making end-to-end latency a key bottleneck for interactive use. Almost all production systems are built on autoregressive (AR) language models and inherit left-to-right decoding in planning and long-…

- **[Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for Latent Communication](https://arxiv.org/abs/2610.28905)**
  - *Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov et al.*
  - 🤗 · `2026-10-20`
  - Diffusion language models form answers through a sequence of revisable continuous states, but multi-agent systems usually discard those states and make agents communicate only after decoding text. We ask whether one independent diffusion trajectory can pass a compact hidden messa…

- **[Evolving Agent Interfaces](https://arxiv.org/abs/2610.28601)**
  - *Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega et al.*
  - 🤗 · `2026-10-20`
  - Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through a shell to find one function. Both the interfaces and the knowledge of when to u…

- **[Environment Duels: A Microcosm of LLM Co-Evolution](https://arxiv.org/abs/2610.30116v1)**
  - *Shibo Jin, Zhiqiu Xu, Yiling Zou et al.*
  - `2026-10-21`
  - Through a tangle of real-world interactions, from synthetic training pipelines to data shared on the open web, frontier LLMs absorb what their predecessors and competitors create. How well does each model play its role in this ecosystem, as a creator and as a solver? We introduce…

- **[The End of Consensus Research?](https://arxiv.org/abs/2610.30114v1)**
  - *Clément Burgelin, Rachid Guerraoui, Zicong Hong et al.*
  - `2026-10-21`
  - Consensus is a fundamental problem in distributed computing and at the core of state machine replication (SMR). Despite decades of active human research, discovering practical low-latency solutions to the problem is still open, as it requires combining protocol knowledge, correct…

- **[Asymmetric On-Policy Distillation Learns In-Context Exploration](https://arxiv.org/abs/2610.30105v1)**
  - *Sriyash Poddar, Yanda Bao, Jacob Krantz et al.*
  - `2026-10-21`
  - Sequential decision-making under partial observability is difficult because agents must explore to infer hidden, task-relevant information before acting effectively. Learning such information-gathering behaviors tabula rasa via online reinforcement learning is sample-inefficient,…

- **[Parallel AI Agent Collaboration as Graph-Structured Distributed Block Optimization](https://arxiv.org/abs/2610.30074v1)**
  - *Hanmin Li, Yury Demidovich, Peter Richtárik*
  - `2026-10-21`
  - Parallel AI agents can produce useful local edits yet degrade a shared solution when their edits are combined. We model this coordination problem as discrete block optimization with an exactly evaluable objective and a known dependency graph. Independent sets certify compatible e…

- **[Charts as Epistemic Actions for Experience-Driven Agentic Data Analysis](https://arxiv.org/abs/2610.30072v1)**
  - *Xinzhe Wang, Xudong Weng, Zang Li et al.*
  - `2026-10-21`
  - Data agents built on ReAct-style loops now execute complex analytical workflows over structured data, yet their intermediate reasoning still runs almost entirely through text. Human analysts instead move between numbers, tables, and charts, reading visual evidence to expose trend…

- **[SWE-DIVE: Multi-Turn Coding Agent Evaluation with Dynamic User Simulation](https://arxiv.org/abs/2610.30047v1)**
  - *Lorenz Brehme, Benjamin Steenhoek, Ruth Breu*
  - `2026-10-21`
  - Coding agents are typically evaluated using one-shot, well-formulated prompts. Benchmarks such as SWE-bench use existing GitHub issues as input for a coding agent and evaluate whether the agent successfully solves the task. However, in real-world use cases, prompts are often not…

- **[HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning](https://arxiv.org/abs/2610.30042v1)**
  - *Sudipta Paul, Pengrui Quan, Aounon Kumar et al.*
  - `2026-10-21`
  - Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs. Leading approaches such as the Darwin--Godel Machine and the Huxley--Godel Machine (HGM) rely on recursive self…

- **[Robust Soft Skill Adaptation via Behavioral Localization in Tool-Using Agents](https://arxiv.org/abs/2610.30041v1)**
  - *Zijian Jiang, Xilu Wang*
  - `2026-10-21`
  - Text skills can extend the capabilities of tool-using agents, but long skill descriptions increase computational costs. Soft prompts provide a compact alternative, yet learning from entire successful trajectories may also introduce unnecessary behavioral changes. We find that the…

- **[What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise Document Ingestion](https://arxiv.org/abs/2610.30026v1)**
  - *Yikai Zhao, Saurabh Pandey, Pradeep Kumar Misra*
  - `2026-10-21`
  - Enterprise agents act on documents. Before an agent can follow a policy, answer a compliance question or file a ticket, some ingestion layer must turn a Word file or PDF into tokens - and that layer is where an agent deployed in the wild silently loses information. We show that o…

- **[GuideEvolve: Self-Evolving Agent Framework with Expert Guidance and 3Ts Mechanisms](https://arxiv.org/abs/2610.30017v1)**
  - *Meihong Jia, Yasemin Timar, Jonathan Taws*
  - `2026-10-21`
  - This study introduces GuideEvolve, a self-evolving agent framework incorporating expert guidance and three autonomous regulatory mechanisms, collectively termed the 3Ts: Think Fast and Slow, Throwback, and Termination by choice. The framework addresses critical limitations in ext…

- **[Agent Behavior Maps: Locating Agents by What They Would Do, Without Running Them](https://arxiv.org/abs/2610.30014v1)**
  - *Shota Fujikawa, Takuya Tamura, Kosuke Akimoto et al.*
  - `2026-10-21`
  - LLM agents with similar success rates can follow different action sequences. An Agent Behavior Map represents LLM-harness combinations using centered action log-likelihoods on shared reference trajectories, without requiring new environment rollouts from the target agent. We deri…

- **[ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination](https://arxiv.org/abs/2610.29934v1)**
  - *Nithin Sivakumaran, Ali Payani, Hyunji Lee et al.*
  - `2026-10-21`
  - Forming an accurate theory-of-mind (ToM) is key to successful multi-agent collaboration and requires reasoning under uncertainty to capture multiple possible partner states. This is hard to do in the text representation space native to large language model (LLM) agents, which mor…

- **[Automated Materials Data and Knowledge Extraction using Machine Learning and Large Language Models](https://arxiv.org/abs/2610.29895v1)**
  - *Aravindan Kamatchi Sundaram, B. Pabitramohan Prusty, Rohit Batra*
  - `2026-10-21`
  - Over the past decade, substantial efforts have been devoted to developing machine learning (ML) methods for extracting materials data and, where possible, materials knowledge directly from the scientific literature. This review traces the evolution of these methods from heuristic…

- **[PAUSE: Search-Free Steering of Coding Agents Before Their First Source-Code Edit](https://arxiv.org/abs/2610.29870v1)**
  - *Viral Patel, Boyin Tan, Jason Xue et al.*
  - `2026-10-21`
  - Coding agents can invest substantial effort in repository exploration and testing yet still produce unsuccessful patches. Existing online steering methods review trajectories periodically or invoke an advisor when a monitor detects behavioral problems; frequent reviews are costly…

- **[MemoryTax: The Bitter Lesson of Agent Memory](https://arxiv.org/abs/2610.29823v1)**
  - *Zedong Peng*
  - `2026-10-21`
  - Agent memory systems such as Mem0 and Zep decide what to keep before any question arrives; coding agents keep the raw history and let the model search it with its own tools. We ask whether designed memory still helps once the model is strong enough to search for itself. On one Lo…

- **[UserSWE: Evaluating Coding Agents in Multi-Turn Conversations with Dynamic Users](https://arxiv.org/abs/2610.29822v1)**
  - *Zhan-Yu Wu, Ji Luo, Alyssa Wu et al.*
  - `2026-10-21`
  - As coding agents become more capable, developers increasingly use them to fix bugs through multi-turn interactions. Existing benchmarks do not adequately cover this scenario. Most present a complete issue report in a single turn without interaction. Their evaluation can produce b…

- **[Toward Recursive Self-Improvement in Physical AI](https://arxiv.org/abs/2610.29677v1)**
  - *Meng Luo, Zechen Bai, Shanqing Xu et al.*
  - `2026-10-21`
  - Recursive self-improvement (RSI) describes a system that improves not only its behavior but also the process by which it improves. Recent digital agents test this idea by rewriting their own code and checking each version with executable tests. Bringing these mechanisms into the…

- **[Conflicted Records: Typed Adversarial Contracts for Auditable LLM Output Quality Enforcement](https://arxiv.org/abs/2610.29669v1)**
  - *Kardelen Subasi, Jarosław A. Chudziak*
  - `2026-10-21`
  - LLM-generated records increasingly populate production information systems where they are treated as data assets subject to the same quality expectations as records from operational databases. A single such record can simultaneously satisfy and violate a quality rule: a grounded…

- **[The Reflexivity Threshold: A Phase Transition for Multi-Agent Performative Prediction](https://arxiv.org/abs/2610.29577v1)**
  - *Ahmed Mahrous, Roberto Di Pietro*
  - `2026-10-21`
  - Many learning systems are performative: once deployed, their predictions change the data distribution on which future models are trained. In multi-agent settings, this feedback is routed through a network of interacting learners, so stability depends not only on the strength of p…

- **[Rethinking Agentic Model Orchestration for Time Series Forecasting](https://arxiv.org/abs/2610.29504v1)**
  - *Tong Guan, Tianxiang Zhan, Shirui Pan et al.*
  - `2026-10-21`
  - Time series foundation models (TSFMs) perform unevenly across forecasting tasks. Recent work uses agentic model orchestration (AMO) to select or combine TSFMs, often outperforming individual forecasters. Yet these gains may reflect stronger or more complementary candidates rather…

- **[PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents](https://arxiv.org/abs/2610.29467v1)**
  - *Jian Zhong, Zeyu Liu, Pingchuan Cao et al.*
  - `2026-10-21`
  - Long-horizon dialogue agents need to keep user memories stable enough for personalization while adapting when the user genuinely changes. Existing memory systems often append every observation or overwrite old entries by heuristic rules, which makes transient noise hard to distin…

- **[RegoMender: A Multi-agent Framework for Automated Rego Policy Repair](https://arxiv.org/abs/2610.29456v1)**
  - *Ruijie Zhang, Huaxiao Yin, Li Hu et al.*
  - `2026-10-21`
  - Policy-as-Code (PaC) has emerged as a foundational paradigm in cloud-native systems. However, repairing Rego policies remains challenging due to their strict syntax, declarative semantics, and specific verification requirements. Existing automated program repair (APR) methods are…

- **[Beyond Small Talk: Modeling Disclosure Trajectories in Human-AI Conversation](https://arxiv.org/abs/2610.29413v1)**
  - *Keith Kwok, Wanting Ning, Tej Deep Pala et al.*
  - `2026-10-21`
  - Recently, we see a rise in conversational agents as a form of social and emotional support, where disclosure will unfold over time. Yet, current evaluations of these agents typically examine isolated conversational states. In analyses of naturally occurring conversations, disclos…

- **[From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?](https://arxiv.org/abs/2610.29331v1)**
  - *Linus Filbry, Luckeciano C. Melo, Yarin Gal*
  - `2026-10-21`
  - Large language models (LLMs) are increasingly applied across the scientific discovery pipeline, from synthesizing literature to generating hypotheses to informing experimental design. A unifying principle behind these tasks is the need to continuously update beliefs as evidence a…

- **[AgentMonopoly: Behavioral Patterns and Persona Control in LLM Agents](https://arxiv.org/abs/2610.29330v1)**
  - *Changshun Wu, Mengyu Li, Mathis Marsault et al.*
  - `2026-10-21`
  - How do LLM agents' strategies differ, and how much can instructions to adopt a persona change their behavior over a game? We study these questions with AgentMonopoly, an environment where agents communicate, buy and trade properties, and make decisions that affect later turns. We…

- **[MOSAIC: An Omni-Modal Benchmark for Long-Term Memory and Cross-Modal Reasoning in Conversational Agents](https://arxiv.org/abs/2610.29249v1)**
  - *Hong Ting Tsang, Boyi Zhang, Haoyu Huang et al.*
  - `2026-10-21`
  - Omni-modal assistants must remember not only what users say, but also what they show and convey. Existing long-term memory benchmarks are mostly text-and-image or report a single end-to-end score, so they cannot locate whether evidence is lost when it is represented, retrieved, d…

- **[CrashGym: Measuring the Decision Value of Experimentation for LLM Agents in Counterfactual Market Crashes](https://arxiv.org/abs/2610.29245v1)**
  - *Haocheng Lu, Haoxuan Cheng, Mingyang Chen et al.*
  - `2026-10-21`
  - Language-model agents are increasingly asked to run experiments, yet benchmarks rarely measure whether those experiments improve the decisions they are meant to inform. We introduce CrashGym, a deterministic, replayable limit-order-book simulator in which an agent must choose bet…

- **[Correlated Failures of AI Approval Monitors](https://arxiv.org/abs/2610.29178v1)**
  - *Luca Zanolini*
  - `2026-10-21`
  - Before an AI agent takes a consequential action, such as paying, messaging or changing code, several monitors check it. Their verdicts are combined by aggregating scores or by counting approvals, whatever inputs the monitors share. Monitors that share a base model or a poisoned i…

- **[TrainBridge: Agentic NPU Training Optimization Guided by GPU Compilation Evidence](https://arxiv.org/abs/2610.29171v1)**
  - *Yupeng Chen, Kunxiang Zhao, Xingjian Wang et al.*
  - `2026-10-21`
  - We study how to improve training efficiency on Ascend NPUs. In the NPU training programs we study, framework-level compilation optimizations such as operator fusion are only partially applied, leaving fragmented computation and avoidable execution overheads. Profiling-guided tuni…

- **[Steering Black-Box Large Language Model Agents with Pitfall Anticipation World Model](https://arxiv.org/abs/2610.29139v1)**
  - *Jiongxiao Wang, Han Ding, Youzhi Luo et al.*
  - `2026-10-21`
  - Frontier black-box Large Language Model (LLM) agents are proficient at long-horizon reasoning and precise action generation. However, when it comes to a specific agentic task, they have no internalized knowledge of how that particular environment unfolds. A world model offers a n…

- **[Recursive Self-Improvement on a Budget: Scoring Code Edits Before They Run](https://arxiv.org/abs/2610.29121v1)**
  - *Erfan Darzi, Sree Bhargavi Balija, Sheng He*
  - `2026-10-21`
  - A coding agent that rewrites its own scaffold has to choose which proposed edit to expand before that edit has been evaluated, and the search then has to return one agent. Each run fits one linear readout on the parent's steering-split solve rate and eight coordinates of the prop…

- **[Agentic Music Post-Production](https://arxiv.org/abs/2610.29093v1)**
  - *Jaywon Koo, Junghyun Koo, Marco A. Martinez-Ramirez et al.*
  - `2026-10-21`
  - We introduce MixAgent, an agentic pipeline for music post-production that follows the workflow of audio engineers to build interpretable and editable mixing plans guided by a reference song. A grouping agent first routes related input tracks, such as drum recordings, into subgrou…

- **[Our Own Jev: Typed Decisions in One Forward Pass, from an In-House Judge to Open LoRA Models](https://arxiv.org/abs/2610.29052v1)**
  - *Yuchuan Weng, Chi Liu, Xin Chen et al.*
  - `2026-10-21`
  - A typed decision maps evidence, a question and a fixed set of options to a probability for every option, computed in one forward pass, by reading a language model's logits or a small head over its hidden states, instead of generating and parsing text. The commercial system Jev po…

- **[GenXR-Bench: Benchmarking Coding Agents for Interactive XR Development](https://arxiv.org/abs/2610.29014v1)**
  - *William Huang, David Li, Xiang 'Anthony' Chen et al.*
  - `2026-10-21`
  - Coding agents are rapidly advancing from single-file generation to long-horizon repository-scale engineering, yet the evaluation of their capabilities to author interactive extended reality (XR) applications remains an open challenge. Unlike traditional software, XR applications…

- **[An Evidence-Driven Multi-Agent Compound AI System for Head and Neck Proton Radiotherapy Planning](https://arxiv.org/abs/2610.29010v1)**
  - *Qingqing Wang, Liqiang Xiao, Chang Chang*
  - `2026-10-21`
  - Radiation treatment planning requires balancing competing objectives to satisfy clinical criteria while accommodating physicians' preferences. This study aims to develop an evidence-driven, multi-agent compound AI system that integrates DRL-based automated treatment planning with…

- **[Circuits of LLM Classifiers](https://arxiv.org/abs/2610.30076v1)**
  - *Hadi Khalaf, Sajani Vithana, Kunal Talreja et al.*
  - `2026-10-21`
  - Language models make it easy to build classifiers by simply prompting a model with the sample to classify. However, their predictions are neither deterministic nor uniformly reliable across samples. How can we combine predictions from different models to improve reliability? We v…

- **[CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents](https://arxiv.org/abs/2610.29965v1)**
  - *Wenhao Yu, Zhengcheng Wang, Jiahong Liu et al.*
  - `2026-10-21`
  - Joint reinforcement learning and self-distillation combines task rewards with dense teacher guidance for agent training, but their gradients can partly cancel. A mixing coefficient controls relative scale without selectively removing opposing components. We present CORD, a genera…

- **[Recursive Code Evolution for Task-Oriented Semantic Communications](https://arxiv.org/abs/2610.29641v1)**
  - *Yan Gong, Zheng Chu, Wei Koong Chai et al.*
  - `2026-10-21`
  - Semantic communication jointly optimizes inference accuracy, channel use, and computation, yet the underlying communication program is typically specified before training. This paper presents ComRSI (Communications-Oriented Recursive Self-Improvement), a framework for recursively…

- **[One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents](https://arxiv.org/abs/2610.29427v1)**
  - *Shaojin Ma, Ruitao Wang, Pengyi Li et al.*
  - `2026-10-21`
  - Recent advances in multi-turn reinforcement learning (RL) have substantially improved the performance of LLM agents on complex, long-horizon interactive tasks. However, despite progress in fine-grained credit assignment, policy optimization still applies these learning signals th…

- **[BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments](https://arxiv.org/abs/2610.29426v1)**
  - *Ge Qu, Jinyang Li, Xiaohan Xu et al.*
  - `2026-10-21`
  - While agentic reinforcement learning (RL) has emerged as a promising paradigm for training small language models (SLMs), existing frameworks are predominantly tool-centric and struggle with data-centric environments. Specifically, applying tool-centric frameworks to stateful task…

- **[Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents](https://arxiv.org/abs/2610.29346v1)**
  - *Zixuan Yu, Zhenheng Tang, Xiaowen Chu et al.*
  - `2026-10-21`
  - As Large Language Models (LLMs) evolve into autonomous Deep Search and Deep Research Agents capable of executing long-horizon, multi-step tasks, evaluating their reliability becomes increasingly critical. However, existing evaluation paradigms predominantly focus on final task ou…

- **[ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery](https://arxiv.org/abs/2610.29303v1)**
  - *Yongqiang Chen, Chenxi Liu, Deyu Zou et al.*
  - `2026-10-21`
  - Evolutionary coding agents such as AlphaEvolve are one of the notable successes in using Large Language Models (LLMs) to build AI Scientists. These agents tackle open-ended scientific problems by iteratively improving and evolving programs, leveraging the prior knowledge and reas…

- **[Design and Tuning of Multi-Agent Systems Using Bayesian Evolutionary Optimization](https://arxiv.org/abs/2610.29276v1)**
  - *Dominik Jehle, Tom Zehle*
  - `2026-10-21`
  - Designing effective multi-agent systems (MAS) remains a challenging and resource-intensive task. We propose a Bayesian Evolutionary Optimization framework for automatically discovering task-specific MAS topologies. The approach combines evolutionary operators to generate diverse…

- **[MA-UITD: Offline Multi-Agent Reward Inference for Characterizing Continuous Social Behavior](https://arxiv.org/abs/2610.29237v1)**
  - *Zeyuan Zhang, Yiyun Yang, Yuan Cheng et al.*
  - `2026-10-21`
  - Multi-agent inverse reinforcement learning offers a powerful framework not only for imitation learning but also for understanding the neural computations supporting social interactions and decision-making. Inferring rewards from interacting agents is challenging because observed…

- **[Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting](https://arxiv.org/abs/2610.30103v1)**
  - *Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Zabir Al Nazi et al.*
  - `2026-10-21`
  - Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notice which side of this boundary a problem falls on, yet existing benchmarks either…

- **[Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents](https://arxiv.org/abs/2610.29995v1)**
  - *Jielong Tang, Ling-An Zeng, Xujie Yuan et al.*
  - `2026-10-21`
  - Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions. Existing abstraction-based memories compress images into text, often discarding visually discriminative details, whereas p…

- **[Bridging Foundational and Agentic Capabilities of LLMs](https://arxiv.org/abs/2610.29751v1)**
  - *Wei Guo, Yuanjian Xu, Jianing Hao et al.*
  - `2026-10-21`
  - Large language models (LLMs) are increasingly deployed as agents, yet it remains unclear how their foundational capabilities translate into agentic capabilities. End-to-end scores leave unresolved whether low benchmark capability or weak deployment drives a failure, limiting acti…

- **[Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization](https://arxiv.org/abs/2610.29671v1)**
  - *Zhiqian Xia, Jielong Tang, Ling-An Zeng et al.*
  - `2026-10-21`
  - Long-term agent memory is shifting from predefined workflows toward learnable policies for memory construction and retrieval. Existing learning-based methods either optimize construction alone or combine retrieval-side online reinforcement learning (RL) with offline construction…

- **[DynaWeave: Learning to Adapt through Dynamic Scenario Synthesis](https://arxiv.org/abs/2610.29443v1)**
  - *Xuan Yang, Chunxiao Liu, Hongsheng Xin et al.*
  - `2026-10-21`
  - Large language model (LLM) agents increasingly use tools to complete tasks in stateful environments. However, many training environments remain largely static apart from changes caused by the agent's own actions, whereas external events introduced by other users, services, or sud…

- **[Don't Stop Long-Context Continual Pre-Training Too Early: An Empirical Scaling Law](https://arxiv.org/abs/2610.29352v1)**
  - *Ziqing Qiao, Xiaoyue Xu, Sikui Zhang et al.*
  - `2026-10-21`
  - Long-context continual pre-training (LCCP) is widely used to improve long-context capability, but how its benefits scale with the number of tokens used for LCCP remains unclear. We investigate this question through modeling, monitoring, and validating the benefits of scaling LCCP…

- **[Seeing the Forest for the Trees: Emergent Agreement from Individual Conversations](https://arxiv.org/abs/2610.29328v1)**
  - *Adi Simhi, Yaniv Nikankin, Jonathan Herzig et al.*
  - `2026-10-21`
  - As LLM agents interact in the wild and shape each other's decisions, understanding how they converge toward agreement becomes important. We study this in multi-turn conversations where two LLMs discuss subjective matters, can agree or disagree, and may change their stances. Using…

- **[OACap: Caption-Guided Active Observation for Detailed Video Captioning](https://arxiv.org/abs/2610.29327v1)**
  - *Hao Shi, Hong Yan, Xiaoyang Zhang et al.*
  - `2026-10-21`
  - Unlike question answering, where a query specifies a perceptual target, open-ended detailed captioning must determine what evidence to acquire and how to integrate it into a coherent global description. We propose Observation-Adaptive Video Captioner (OACap), a caption-centered a…

- **[Signals and Queries: Token-Efficient Agentic Context Discovery](https://arxiv.org/abs/2610.29326v1)**
  - *Yam Marcovitz*
  - `2026-10-21`
  - User-facing LLM agents must identify which behavioral policies apply at each turn, but evaluating every policy with an LLM is costly. We introduce Signals and Queries (S&Q), a lightweight first-stage relevance filter developed for Parlant 4.0 that removes at least 30% of candidat…

- **[Credit Where Credit Is Due: Contrastive Attribution Topology Search for Multi-Agent Systems](https://arxiv.org/abs/2610.29292v1)**
  - *Fabian Tritthart, Tom Zehle*
  - `2026-10-21`
  - An LLM multi-agent system (MAS) is only as good as the agents it chooses to trust: its accuracy and cost hinge on its topology, meaning which agents are included and how they communicate. A single task score, however, does not reveal which agents help or hinder performance. We pr…

- **[Reasoning-Search-Augmented LLMs: An Operational Taxonomy, Benchmark Analysis and Controlled Evidence Synthesis](https://arxiv.org/abs/2610.29189v1)**
  - *Biswas Poudel, Nilson Chapagain, Amit Kumar et al.*
  - `2026-10-21`
  - Large language models (LLMs) demonstrate impressive emergent reasoning capabilities, yet they remain constrained by fixed model parameters and finite context windows. Even when augmented with static retrieval, they can produce statements that are unsupported by, or even contradic…

- **[VeeReview: Measuring Build-Verify Pairs in Agent-Authored Pull Requests from a V-Model Perspective](https://arxiv.org/abs/2610.29143v1)**
  - *Gabriel Dautovi, Jie JW Wu*
  - `2026-10-21`
  - Context: Reviewing a pull request requires verification evidence that addresses the proposed change. Coding agent benchmarks and studies of pull request outcomes do not directly assess this relationship. Objective: We test whether the V-Model's build and verify pairs can measure…

- **[Resonance and Depth: Composing Timbral Identity and Spatial Form in an Artist-in-the-Loop Co-Creative Multi-Agent Percussive Performance](https://arxiv.org/abs/2610.29026v1)**
  - *Keon Ju Maverick Lee*
  - `2026-10-21`
  - This research-creation artistic report presents Resonance and Depth, a 9-minute immersive electroacoustic/acousmatic performance that treats timbre and space as primary compositional materials. Built from live electronic percussion and a personal corpus recorded, curated, and com…

- **[From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](https://arxiv.org/abs/2610.30051v1)**
  - *May Espinola, Qifan Zhang, Yu Xiang*
  - `2026-10-21`
  - Recent advances in frontier AI models have demonstrated remarkable capabilities in visual understanding, reasoning, planning, and tool use, raising the possibility of using general-purpose AI models for robot manipulation without task-specific training. However, their manipulatio…

- **[AgentPolicyForge: From Executable Environments to Policy Benchmarks and Adaptive Guards](https://arxiv.org/abs/2610.28989v1)**
  - *Chao Shang, Wanyu Du, Yi Zhang et al.*
  - `2026-10-20`
  - Customized agent deployments define policies over tools, resources, and execution conditions. Providing these policies in the task agent's prompt does not reliably prevent violations. Training a guard requires examples of tool calls that comply with or violate those policies. We…

- **[PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust](https://arxiv.org/abs/2610.28987v1)**
  - *Tanqiu Jiang, Min Bai, Sadat Shahriar et al.*
  - `2026-10-20`
  - Persistent memory is a largely undefended surface for injection and poisoning, and the same risk limits memory sharing among agents. We present PerMIT, a memory architecture with provable integrity guarantees under an explicit trust assumption: only user-typed inputs and values c…

- **[Behavior Beyond Text: Evaluating Refusal Transfer Failure in LLM Agents](https://arxiv.org/abs/2610.28982v1)**
  - *Ekagra Gupta, Raj Saha, Aniekan-Abasi Inyang et al.*
  - `2026-10-20`
  - While large language models are increasingly deployed as tool-calling agents, their safety evaluations still focus primarily on their ability to refuse harmful requests in text. We investigate whether the refusal behavior in text transfers to tool use. We construct a benchmark of…

- **[SSMCGM-Stream: A Streaming State-Space Model for Personalized Diabetes Management](https://arxiv.org/abs/2610.28976v1)**
  - *Shakson Isaac, Chirag Patel*
  - `2026-10-20`
  - Continuous glucose monitoring supports diabetes management but requires forecasting models that are accurate, interpretable, and efficient enough for real-time deployment. We present SSMCGM-Stream, a streaming state-space model that maintains a personalized hidden state updated w…

- **[Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning](https://arxiv.org/abs/2610.28966v1)**
  - *Yuqi Jia, Hangsheng Zhang, Chenxi Liu et al.*
  - `2026-10-20`
  - Large language model (LLM) agents are increasingly deployed in multi-agent systems (MAS) to accomplish complex tasks. Prior black-box red-teaming attacks mainly focus on single agents, but we find that these methods are far less effective in MAS, where multiple sub-agents may not…

- **[Self-Improving Agents with World Model Predictive Paths](https://arxiv.org/abs/2610.28945v1)**
  - *Haori Lu, Tianyu Gao, Yaoyao Liu et al.*
  - `2026-10-20`
  - Large language model (LLM) agents are increasingly expected to interact with environments and improve their decisions during deployment. However, how anticipating future outcomes and drawing on accumulated interaction experience can jointly support decision-making remains underex…

- **[D-Skill: Distilling Teacher Knowledge through Agent Skills](https://arxiv.org/abs/2610.28914v1)**
  - *Shuo Yuan, Dacheng Li, Joseph E. Gonzalez*
  - `2026-10-20`
  - Frontier language-model agents excel at complex tasks, but high inference costs make transferring their capabilities to smaller models essential. Traditional knowledge distillation achieves this through parameter updates, requiring access to the student's weights and additional t…

- **[JaxMARL-BC: Multi-Agent Reinforcement Learning for Macroeconomic Modelling, in Seconds](https://arxiv.org/abs/2610.28907v1)**
  - *Daniele Montagnani, Andrea Coletta, Antonietta Mira et al.*
  - `2026-10-20`
  - Multi-agent reinforcement learning (MARL) offers a principled way of populating simulated economies with many heterogeneous decision makers. Its adoption, pioneered in finance, has nonetheless been slow in macroeconomics because of two main limitations: the lack of a shared frame…

- **[Fig: Automated Multiagent Behavior Elicitor](https://arxiv.org/abs/2610.28891v1)**
  - *Anrui Gu, Zhichao Wang, Nicolai Ouporov*
  - `2026-10-20`
  - Many social evaluations for multiagent systems study behaviors as they emerge from environments instead of systematically intervening in the environment to elicit such behaviors. We introduce Fig (Finding Interactions in Games), an agentic system that performs targeted elicitatio…

- **[SANE: Automated Scorer-Specific Metamorphic Testing for LLM Judges](https://arxiv.org/abs/2610.28886v1)**
  - *Ethan Ludwick, Yu-Chung Hsiao*
  - `2026-10-20`
  - LLM judges increasingly mediate benchmark evaluation, model selection, data curation, and training. Their decisions are useful only when each judge responds reliably to changes affecting its scoring criterion. Existing methods for reliability testing perturb inputs with known exp…

- **[Agent AI Zarządzający Siecią Open RAN Zorientowana na Użytkownika](https://arxiv.org/abs/2610.28860v1)**
  - *Marcin Hoffmann*
  - `2026-10-20`
  - Jednym z najważniejszych wyzwań związanych z implementacją sieci Open RAN o architekturze zorientowanej na użytkownika jest odpowiednie formowanie tzw. klastrów obsługujących. Problem ten może być efektywnie rozwiązany za pomocą zaproponowanego Agenta AI bazującego na modelu języ…

- **[Where Should a Stuck Agent Spend Its Next Tokens? Causal Attribution of Inference-Time Resources](https://arxiv.org/abs/2610.28834v1)**
  - *Saiyue Lyu, Jerrold Huang, Yunbei Zhang et al.*
  - `2026-10-20`
  - Inference-time scaling is often treated as a token-budget problem, but a failed coding agent can seek qualitatively different resources: computation, information, or feedback. We introduce Banzhaf Resource Attribution (BRA), a controlled factorial framework that measures each res…

- **[Brittle by Design? Multi-Scenario Reinforcement Learning for Robust Mission Coordination in Systems of Systems](https://arxiv.org/abs/2610.28818v1)**
  - *İbrahim Oğuz Çetinkaya, Sajad Khodadadian, Taylan Topcu*
  - `2026-10-20`
  - As systems engineering (SE) shifts from monolithic systems to Systems of Systems, Mission Engineering (ME) has emerged as a new line of thinking in SE. Mission environments are uncertain and dynamic, and outcomes depend on how mission assets interact with them, rendering static a…

- **[Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing](https://arxiv.org/abs/2610.28815v1)**
  - *Jingzhe Liu, Jiliang Tang, Tong Zhao et al.*
  - `2026-10-20`
  - Agentic harness evolution optimizes an agent's instructions, tools, and control flow by using its task execution experiences as evolving evidence. While more evolution tasks should intuitively improve performance, our preliminary study reveals a paradoxical failure mode: the perf…

- **[Second Thoughts: Exploring and Planning through Comparative Imagination in World Models](https://arxiv.org/abs/2610.28779v1)**
  - *Hieu Tran, Hong Yu*
  - `2026-10-20`
  - World models let agents compare imagined outcomes before acting, but an agent must still decide which alternatives to explore and when a proposed plan should replace its learned policy. We introduce SDI (Sibling Disagreement in Imagination), which connects these decisions through…

- **[GBClaw: An agentic AI framework for atomistic grain boundary research and mechanistic discovery](https://arxiv.org/abs/2610.28629v1)**
  - *Yazhuo Liu, Kunqing Ding, Xiaoguo Gong et al.*
  - `2026-10-20`
  - Agentic artificial intelligence (AI) systems hold immense potential for automating complex workflows in materials discovery and design, but extending them to domain-intensive mechanistic investigations remains challenging. Here, we present GBClaw, an agentic AI framework for inve…

- **[Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets](https://arxiv.org/abs/2610.28624v1)**
  - *Jad Yammine, Malek Wahidi, Abrar Anwar et al.*
  - `2026-10-20`
  - Warehouse robot fleets continuously observe operational conditions, but preserving these observations as reusable semantic memory incurs substantial computation, communication, and storage costs. For example, explaining recurring aisle blockages can require reviewing video from m…

- **[Semantic Observability for Autonomous Systems Diagnostics](https://arxiv.org/abs/2610.28611v1)**
  - *Jitendra Solanki, Anand Todkar, Ziran Min*
  - `2026-10-20`
  - Modern distributed microservice deployments generate massive volumes of heterogeneous, multi-format observability logs across physically and logically partitioned infrastructure. Isolating root causes during cascading failures remains an arduous task for Site Reliability Engineer…

- **[Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation](https://arxiv.org/abs/2610.28586v1)**
  - *Shu Zhao, Tan Yu*
  - `2026-10-20`
  - Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable…

- **[SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images](https://arxiv.org/abs/2610.28585v1)**
  - *Rundong Luo, Yunong Liu, Di Cao et al.*
  - `2026-10-20`
  - Simulation is a powerful tool for robotics, but building diverse, simulation-ready scenes at scale remains difficult. Reconstructing scenes from single images is a promising alternative, but visual similarity alone is insufficient: objects must also be recovered, accurately place…

- **[Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition](https://arxiv.org/abs/2610.28578v1)**
  - *Wenjie Lou, Tianshuo Peng, Shiyang Feng et al.*
  - `2026-10-20`
  - In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and r…

- **[OptScientist: Automated Discovery of Optimization Laws](https://arxiv.org/abs/2610.28562v1)**
  - *Ma ZhenYao, Yue Liang, Jian-Qiao Zhu*
  - `2026-10-20`
  - Many scientific phenomena are best understood as outcomes of underlying optimization problems, yet automated scientific discovery has largely focused on recovering equations that describe observed input-output patterns. We introduce OptScientist, a novel automated framework for d…

- **[Agentic Ensemble with Vision-Language Models for Visual Anomaly Detection](https://arxiv.org/abs/2610.28560v1)**
  - *Shangquan Sun, Wenjun Luo, Xu He et al.*
  - `2026-10-20`
  - Visual anomaly detection aims to detect abnormal objects, while anomaly samples are often scarce during model training. Assembling multiple pretrained detectors can help by leveraging their transferable image scores and anomaly maps. However, most existing ensemble methods apply…

- **[Proof-Carrying Contracts: Commitments AI Agents Cannot Break](https://arxiv.org/abs/2610.28484v1)**
  - *Carlo Ciliberto, Alessandro Rudi, Enrico Tassi*
  - `2026-10-20`
  - AI agents increasingly act on behalf of people or other agents, purchasing services, exchanging information and delegating work. What an agent must respect is written in instructions, policies or agreements, but text alone cannot make it comply. It may make mistakes, be redirecte…

- **[Claims of emergence in AI should be grounded in information decomposition](https://arxiv.org/abs/2610.28479v1)**
  - *Christoph Riedl, Fernando E. Rosas*
  - `2026-10-20`
  - When a language model develops capabilities not traceable to its individual components, when a multi-agent AI system outperforms each agent on its own, or when a human-AI pair succeeds where either fails in isolation, AI researchers describe it as a case of ``synergy'' or ``emerg…

- **[Beyond Trajectory Statistics: Community-Consistent Human Mobility Generation via Evolving User-Location Graphs](https://arxiv.org/abs/2610.28467v1)**
  - *Bo Liu, Tong Li, Jiapeng Zhang et al.*
  - `2026-10-20`
  - Human mobility data are fundamental to Web-based location services and broader urban applications, and mobility generation provides synthetic trajectories when real data are costly or inaccessible. Although recent mobility generators have incorporated collective mobility patterns…

- **[Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization](https://arxiv.org/abs/2610.28454v1)**
  - *Zhenwei Tang, Di Bai, Jintao Liu et al.*
  - `2026-10-20`
  - Agents are starting to sell to other agents. Seller agents write the listings of tools, services and products, and buyer agents read these listings when they choose what to use. We show that seller agents told only to be selected more often practice generative engine optimization…

- **[After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents](https://arxiv.org/abs/2610.28425v1)**
  - *Zhiyue Xu, Xukai Wang, Zhiyuan Huang et al.*
  - `2026-10-20`
  - Modern LLM agents persist state across sessions via two channels: long-lived memory files silently prepended to the system prompt, and scheduled tasks waking the agent without user input. A one-time indirect prompt injection committed to either channel can re-fire across sessions…

- **[Rewards for Budget-Aware Multi-Turn Agents That Adapt to Arbitrary Test-Time Constraints](https://arxiv.org/abs/2610.28409v1)**
  - *Tom A. Lamb, Adam Golinski, Eleonora Gualdoni et al.*
  - `2026-10-20`
  - Large language model agents are often given an inference budget and asked to maximise success within it. A multi-turn agent has to allocate this budget across many environment interactions. An external harness can enforce the budget, but it remains unclear whether the agent itsel…

- **[MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems](https://arxiv.org/abs/2610.28397v1)**
  - *Mohammad Kachuee, Phu Mon Htut, Sheng Li et al.*
  - `2026-10-20`
  - Agentic AI extends large language models (LLMs) from generating responses to planning and executing complex workflows, substantially expanding their utility while exposing applications to unsafe actions, information leakage, and adversarial manipulation. Multi-agent systems furth…

- **[FALCA: Falsification-Aware Reinforcement Learning with Hierarchical Credit Assignment for Long-Horizon Deep Search Agents](https://arxiv.org/abs/2610.28361v1)**
  - *Zijun Dou, Kun Luo, Chaofan Li et al.*
  - `2026-10-20`
  - Long-horizon deep search requires LLM agents to iteratively decompose complex information needs, gather evidence from external sources, and maintain a reliable research state under multiple constraints. A central challenge is that early mistakes can be amplified over the search t…

- **[S-Agent 2.0: Spatial Reasoning with a General Coding Agent](https://arxiv.org/abs/2610.28354v1)**
  - *Rui Gong, Ruoyu Wang, Yalun Dai et al.*
  - `2026-10-20`
  - Spatial reasoning asks a model to work out where objects are in 3D space, how they relate to one another, and how they move. Agentic VLMs have recently brought large improvements on such tasks by letting the model actively gather evidence with 3D perception tools instead of answe…

- **[Local Work, Global Progress: A Convergence Theory of AI Agent Collaboration](https://arxiv.org/abs/2610.28286v1)**
  - *Ivan Ilin, Peter Richtárik*
  - `2026-10-20`
  - Teams of large language model (LLM) agents are increasingly applied to complex tasks, but their collaboration protocols are mostly designed empirically, without convergence guarantees. We formalize collaborative problem solving as block optimization: each agent improves one part…

- **[ChartEvo: Self-Evolving Agent Harnesses for Long-Tail Chart Reasoning](https://arxiv.org/abs/2610.28282v1)**
  - *Qi Wang, Peijie Wang, Jun Cao et al.*
  - `2026-10-20`
  - Multimodal large language models (MLLMs) have substantially advanced chart understanding and reasoning, yet their performance remains highly uneven across chart types. While modern MLLMs perform well on common charts, their accuracy drops sharply on long-tail charts with diverse…

- **[GALA: Geometry-Aware Language Model for Controllable Object Arrangement](https://arxiv.org/abs/2610.28280v1)**
  - *Chucheng Xiang, Runze Wang, Zhi Deng et al.*
  - `2026-10-20`
  - Reasoning about fine-grained placement constraints, such as support and containment, is essential for realistic 3D scene creation. It remains a significant challenge for existing methods that rely on simplified object representations like oriented bounding box (OBB), which are bl…

- **[JAXbounce: A Continuous-Control Pong-Like Benchmark for Active Inference Beyond Low Dimensional Environments](https://arxiv.org/abs/2610.28203v1)**
  - *Chaitanya Kaul, Markus Klar, Sebastian Stein et al.*
  - `2026-10-20`
  - We introduce JAXbounce, a continuous control pong-like benchmark designed to evaluate active inference beyond discrete, low dimensional environments. JAXbounce combines continuous states and stochastic dynamics in discrete time with flexible and composable observation models that…

- **[MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2610.28201v1)**
  - *Yu Cui, Hong He, Ruiqing Yue et al.*
  - `2026-10-20`
  - Recursive self-improvement (RSI) of agent harnesses has emerged as an effective approach to enhancing the capabilities of large language model (LLM) agents. By searching the harness space for a specific LLM on a given dataset, RSI can discover a harness tailored to the capabiliti…

- **[Reframing Object-Centric Reinforcement Learning: From Absolute to Relative Representations](https://arxiv.org/abs/2610.28197v1)**
  - *Cedric Derstroff, Jannis Blüml, Janosch Moos et al.*
  - `2026-10-20`
  - Object-centric reinforcement learning agents typically receive each object's position in a fixed global frame, even though their decisions usually depend on where objects are relative to one another. These absolute views often fail to capture the local context that is most releva…

- **[From Code Generator to Engineering Companion: A Plant-aware Agent for PLC Programming](https://arxiv.org/abs/2610.28160v1)**
  - *Joschka Kersting, Gesa Benndorf*
  - `2026-10-20`
  - Programmable Logic Controller (PLC) coding remains a manual, IDE-centric task that demands constant context switching between documentation, project files, and code editors. Recent work has demonstrated that retrieval-augmented large language models can generate vendor-compliant…

- **[Interruption-Aware Recurrent Reinforcement Learning for UAS Navigation Under Temporary Overrides](https://arxiv.org/abs/2610.28121v1)**
  - *Christopher Conrad, Deepak Panda, Weisi Guo et al.*
  - `2026-10-20`
  - Safe autonomous navigation of UASs requires tactical deconfliction to address conflicts that strategic coordination cannot prevent. This task is challenging under partial observability, when sensor or traffic data are missing, delayed, or degraded. Geometry-based methods can offe…

- **[ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents](https://arxiv.org/abs/2610.28093v1)**
  - *Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique et al.*
  - `2026-10-20`
  - AI agents keep long-term memory, much of which comes from web pages and tool results. Agent harnesses, the software that runs the model, do not record who may act on this memory, so an instruction hidden in a fetched page can be treated as the user's own instruction. We propose C…

- **[Reinforcement learning for hardware acceleration and system-level optimization on FPGA and integrated-circuit platforms: A survey](https://arxiv.org/abs/2610.28699v1)**
  - *Hamza Kheddar*
  - `2026-10-20`
  - Reinforcement learning (RL) enables adaptive and autonomous decision-making in embedded, edge, and heterogeneous computing systems. Field-programmable gate arrays (FPGAs) and integrated circuits (ICs) offer low latency, energy efficiency, and architectural flexibility for RL depl…

- **[When Do Humans and Machines Truly Complement Each Other? Formal Conditions and Empirical Evidence for Human-AI Synergy](https://arxiv.org/abs/2610.27965v1)**
  - *Andrea Campagner, Federico Cabitza, Vincenzo Crupi*
  - `2026-10-20`
  - Can humans and artificial intelligence cooperate such that their combination yields greater accuracy than either agent alone? This result, termed \emph{synergy} or \emph{complementarity}, is notoriously difficult to achieve, even when both agents possess significant independent a…

- **[Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](https://arxiv.org/abs/2610.27954v1)**
  - *Byeonghun Bang, Sangwoo Park, Jinheon Baek et al.*
  - `2026-10-20`
  - Recent advances in large (vision) language models have enabled computer-use agents that automate digital workflows via fine-grained keyboard and mouse operations. However, such agents remain fragile in long-horizon settings, where errors accumulate and executed actions leave unin…

- **[MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records](https://arxiv.org/abs/2610.27911v1)**
  - *Seohyun Lee, Jongha Kim, Dohwan Ko et al.*
  - `2026-10-20`
  - Enterprise agents answer questions over workplace records that evolve through team collaboration. As information is shared, corrected, and revised across documents, chats, and figures, multiple versions of the same information accumulate in the workspace. Reliable question answer…

- **[SAPD: Learning from Agent Experience without Environment Interaction](https://arxiv.org/abs/2610.27847v1)**
  - *Juncheng Diao, Haibin Wang, Wei Shi et al.*
  - `2026-10-20`
  - Scaling the training of Large Language Model (LLM) agents typically requires a large collection of executable environments, whose construction, maintenance, and operation constrain the expansion of training experience. Existing offline trajectories offer an opportunity to reuse i…

- **[COMPASS: Routing via Capability-Oriented Model Profiling with Adaptive Search, Selection, and Tool Use](https://arxiv.org/abs/2610.27822v1)**
  - *Amin Rezaei, Pouya Parsa*
  - `2026-10-20`
  - LLM routing aims to select a capable model at low cost, but specialized routers can require updates as models and tasks change. We propose COMPASS, an agentic router in which an LLM follows a routing recipe, gathers performance and cost evidence through tools, and optionally insp…

- **[LatBridge: Efficient and Stable Model Replacement in Latent-Communication Multi-Agent Systems](https://arxiv.org/abs/2610.27813v1)**
  - *Jiajun Zhu, Haobo Li, Zixin Chen et al.*
  - `2026-10-20`
  - Multi-agent systems rely on communication to complete tasks, and latent communication passes continuous representations to reduce text generation and re-encoding. However, multi-agent systems must reconfigure agent models, whereas existing latent-communication methods are built f…

- **[Toward Agentic AI for the 6G Physical Layer: From Algorithm Discovery to Verified Baseband Silicon](https://arxiv.org/abs/2610.27797v1)**
  - *Eric Mittag, Lukas Brechtel, Maximilian Stark et al.*
  - `2026-10-20`
  - 6G will be designed faster than it can be built: AI-driven search already proposes physical-layer algorithms at machine speed, while carrying a single one onto embedded baseband silicon remains specialist work. That silicon imposes hard memory and numeric limits, but also exposes…

- **[RELAY: Scaling Historical Build Restoration through Rule Reuse and Agentic Repair](https://arxiv.org/abs/2610.27784v1)**
  - *Olivier Nourry, Yoshiki Higo*
  - `2026-10-20`
  - Vulnerability benchmarks and software engineering research depend on rebuilding historical software. Yet builds rely on external resources, such as base images and packages, that change independently of the source code. In this study, we examine this environment decay on 14,159 O…

- **[GRADUS: Discovering and Recovering Agent Lessons from the Environment's Latent Syllabus](https://arxiv.org/abs/2610.27781v1)**
  - *Qing Ping, Wei Yang, Panpan Xu et al.*
  - `2026-10-20`
  - Training LLM agents for policy-constrained tool environments, such as an airline backend with booking, refund, and cancellation policies, requires tasks that exercise the environment's rules individually and in combination. Existing synthesis pipelines let a model propose tasks a…

- **[RITE: Evaluating End-to-End Resilience to Silent Tool Errors in E-Commerce Agentic Systems](https://arxiv.org/abs/2610.27777v1)**
  - *Wenshuo Zhang, Yuquan Lin, Yushi Sun et al.*
  - `2026-10-20`
  - Tool-using LLM agents increasingly answer e-commerce queries through multi-step tool interactions. The expected output of a tool call can shift between agent development and execution, allowing a plausible but incorrect value to be returned without an explicit failure signal. The…

- **[Give the Model a Finger: Developmentally Aligned Evaluation of Counting in Vision-Language Models](https://arxiv.org/abs/2610.27756v1)**
  - *Yingxin Jia, Hui Geng, Wenxin Yang et al.*
  - `2026-10-20`
  - Vision-language models (VLMs) are exact on small sets and drift into estimation on larger ones, a profile reminiscent of children before they master counting. Children cross the barrier with epistemic actions: pointing at each item while reciting number words, moving counted item…

- **[S$^2$-MAS: A Society-Scale Multi-Agent Simulation Framework with 500 Million Household Persona Agents](https://arxiv.org/abs/2610.27746v2)**
  - *Yang Li, Di Wan, Yike Wang et al.*
  - `2026-10-20`
  - Simulating economic responses at society scale requires agents whose decisions reflect household circumstances and the effects of earlier actions. We introduce S$^2$-MAS, a society-scale multi-agent simulation framework built on 500 million synthetic household personas grounded i…

- **[Hearsay or Fact? How Framing and Elicitation Shape LLM Probability Updates](https://arxiv.org/abs/2610.27745v1)**
  - *An-Sheng Jhang*
  - `2026-10-20`
  - Large language models (LLMs) are increasingly used as judgment assistants and as stand-in participants in psychology experiments, yet little is known about how much their probability estimates move in response to a single new piece of information. We pair premise-hypothesis items…

- **[RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process?](https://arxiv.org/abs/2610.27735v1)**
  - *Kaiwen Zhou, Udari Madhushani Sehwag*
  - `2026-10-20`
  - Recursive self-improvement, in which frontier AI models work on training the next generation, is quickly becoming a reality. However, the safety of this process has received far less attention than it should. A misaligned model training its successor can shape what that successor…

- **[CovNav: Conformal Prediction-Guided Adaptive Inference for Object Goal Navigation](https://arxiv.org/abs/2610.27677v1)**
  - *Pengying Wu, Zhejia Wen, Kang Ding et al.*
  - `2026-10-20`
  - In object goal navigation (ObjectNav), an embodied agent must find a target object (e.g., "find a bed") in a previously unseen environment, relying on spatial commonsense such as object co-occurrence. Large Language Models (LLMs) encode this commonsense, but deploying them on rob…

- **[Reusing Multimodal Agents: Efficient Evaluation of Sound Designs in Games](https://arxiv.org/abs/2610.27670v1)**
  - *Thai Nguyen Van, Ibrahim Khan, Mury Fajar Dewantoro et al.*
  - `2026-10-20`
  - This paper introduces a novel framework for efficiently evaluating in-game sound designs using multimodal learning and reinforcement learning. Sound design significantly influences gameplay and accessibility; however, objective evaluation methods, defined here as automated assess…

- **[Does Multi-Agent Collaboration Pay When Agents Serve Users? Testing Agent Scaling in Dual-Control Settings](https://arxiv.org/abs/2610.27655v1)**
  - *Ethan Yang, Xiangcheng Shi*
  - `2026-10-20`
  - Multi-agent systems (MAS) built from language models are deployed on the premise that collaboration beats a single-agent system (SAS), yet when it pays is unclear. The most systematic study to date gives a capability-saturation rule: coordination helps while the SAS is weak and h…

- **[CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents](https://arxiv.org/abs/2610.27645v1)**
  - *Xu Hu, Haoming Li, Yuxiang Wang et al.*
  - `2026-10-20`
  - As computer-use agents (CUAs) move to long-horizon workflows spanning multiple applications, undetected errors can silently corrupt persistent state and cause cascading failures in subsequent actions. Reliable error detection and recovery have become critical bottlenecks for buil…

- **[Auditing the Product, Not the Recursion: The Evaluation Evidence Behind Recursive Self-Improvement Claims](https://arxiv.org/abs/2610.27610v1)**
  - *Zihan Chen, Di Zhu, Lei Nico Zheng*
  - `2026-10-20`
  - Recursive self-improvement (RSI) promises AI systems, such as self-evolving LLM agents, that become better at producing further improvements. Evaluating this promise requires separating product claims about the final system from process claims about the improvement process itself…

- **[Beyond Experience: Knowledge-Guided Evolution for NPU Kernel Generation](https://arxiv.org/abs/2610.27588v1)**
  - *Xi Chen, Ming Shen, Haotian Yan et al.*
  - `2026-10-20`
  - LLM agents have become capable kernel engineers on mainstream GPU stacks, but they struggle on emerging accelerators such as Ascend NPUs, whose programming model is barely represented in pretraining data. Recent NPU agents address this gap largely through experience: they accumul…

- **[DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents](https://arxiv.org/abs/2610.27581v1)**
  - *Yuxuan Li, Xiangchen Guan, Kunrong Li et al.*
  - `2026-10-20`
  - Full-duplex speech agents must update persistent memory while listening and speaking, yet it remains unclear which events should be stored, revised, or excluded. Existing benchmarks isolate interaction timing from memory outcomes, obscuring the state transitions behind a correct…

- **[The Show-Up Attack: When Subagents Win Over Their Supervisor](https://arxiv.org/abs/2610.27574v1)**
  - *Maosen Zhang, Jianshuo Dong, Yutong Zhang et al.*
  - `2026-10-20`
  - Multi-agent systems are increasingly deployed to coordinate multiple large language model (LLM) agents. However, this also creates new attack surfaces: malicious agents may have chances to exploit the coordination. In this paper, we propose and study the \textit{show-up attack},…

- **[RaspAssistant as an Agentic Framework for Automating Adsorption Simulation Research in Porous Materials](https://arxiv.org/abs/2610.27572v1)**
  - *Marko Petković, Susanne Gooijer, José Manuel Vicent-Luna et al.*
  - `2026-10-20`
  - Porous-material adsorption studies require coordinated structure preparation, force-field selection, simulation, validation, and interpretation, making end-to-end automation difficult. We test whether RaspAssistant, a hierarchical multi-agent framework, can carry an adsorption st…

- **[Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](https://arxiv.org/abs/2610.27548v2)**
  - *Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang et al.*
  - `2026-10-20`
  - When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing c…

- **[Automated Multi-Agent Organization Design: From Architecture Search to Organizational Learning](https://arxiv.org/abs/2610.27531v1)**
  - *Shao-Jun Xia, Yuner Zhang, Huixin Zhang et al.*
  - `2026-10-20`
  - Agentic system design is increasingly shifting from hand-crafted prompts and workflows toward automated search over agentic programs and interaction structures, with multi-agent systems receiving growing attention. Yet a central question remains unresolved: when does an automatic…

- **[MemDev-Bench: Does Memory Help Code Agents?Benchmarking Memory Systems over Real Repository Histories](https://arxiv.org/abs/2610.27524v1)**
  - *Guorui Chen, Tao Liu, Zhenzhen Huang et al.*
  - `2026-10-20`
  - Code agents increasingly work on evolving real repositories, and memory systems aim to help them reuse earlier experience. However, such experience is diverse and evolving, so it remains unclear how memory systems organize it and thereby affect code agents. Existing benchmarks ca…

- **[Self-Evolving Agents through Privileged Retrospective Distillation](https://arxiv.org/abs/2610.27495v1)**
  - *Yuhang Zhou, Yifan Wu, Bo Peng et al.*
  - `2026-10-20`
  - Self-evolving agents aim to improve from their own experience rather than remain fixed after deployment, but naturally collected trajectories often lack ground-truth solutions or verifier-derived rewards. We introduce Retrospective Self-Distillation (RSD), a multi-round framework…

- **[The More the Better? A Comparison of Single- and Multi-Agent LLM Setups on a Financial Review Task](https://arxiv.org/abs/2610.27488v1)**
  - *Pei Liu*
  - `2026-10-20`
  - Practitioner guidance holds that a large language model reviews a document better when the work is divided among agents. We test a narrow form of it in a controlled comparison of single-agent and multi-agent setups on a financial task, reviewing credit assessment memos against re…

- **[Securing Agentic Commerce Through Behavior-Aware Fraud Detection and Cybersecurity for Trusted AI-Agent Payment Authorization](https://arxiv.org/abs/2610.27483v1)**
  - *Kayode L. Ogunsusi*
  - `2026-10-20`
  - The growing use of autonomous artificial intelligence agents in digital commerce creates new security concerns involving agent impersonation, unauthorized payments, compromised agents, and misuse of delegated authority. This research introduces the Autonomous Commerce Agent Guard…

- **[Runtime Control for AI Agents: Closing the Evaluation--Execution Gap in Operational Workflows](https://arxiv.org/abs/2610.27480v1)**
  - *Jayesh Bhadane, Ramachandra Yerramsetti, Rajesh Gupta et al.*
  - `2026-10-20`
  - Language-model agents increasingly participate in operational workflows where approvals, binds, and payments create commitments. An approval valid when issued may no longer authorize execution after relevant facts, evidence, policy, or authority change. We call this the evaluatio…

- **[Recoverability and Verifier Strength: Two Measured Preconditions for Unattended Agent Self-Improvement](https://arxiv.org/abs/2610.27465v1)**
  - *De Wang, Peng Qi*
  - `2026-10-20`
  - Agent platforms are starting to improve their own agents: they read a deployed agent's execution traces, derive a change, have an automated verifier approve it, and release it with no human author. How much of this loop can safely run without a human? We propose two quantities a…

- **[Ask to Distill: Learning to Synthesize Data for On-Policy Distillation](https://arxiv.org/abs/2610.27450v1)**
  - *Jiashuo Sun, Hao Zhang, Xueqiang Xu et al.*
  - `2026-10-20`
  - On-policy distillation (OPD) can succeed with surprisingly few training questions, motivating a view of questions as carriers of distributional knowledge transfer. How can we assess whether a newly generated question is valuable for distillation, and learn to generate better ques…

- **[Harness Self-Evolution for Long-Horizon Terminal Agents](https://arxiv.org/abs/2610.27435v1)**
  - *Ruhan Wang, Yucheng Shi, Zongxia Li et al.*
  - `2026-10-20`
  - Long-horizon terminal agents may solve a task in one run yet fail across repeated runs. Stochastic errors can propagate through actions and context, creating a gap between capability and reliable execution. We present RiseHarness, a framework for iteratively improving agent harne…

- **[KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses](https://arxiv.org/abs/2610.27417v1)**
  - *Zhikang Chen, Yueqing Sun, Sen Cui et al.*
  - `2026-10-20`
  - A failed gaming trajectory reveals that an agent needs intervention, but not necessarily how its execution harness should change. Effective harness adaptation therefore requires gathering diagnostic evidence, rather than merely proposing alternative recovery rules. We present KPH…

- **[FlashNext-RL: A System Optimization Study for Long-Horizon Agentic RL of Qwen3.8-Flash-Next](https://arxiv.org/abs/2610.28998v1)**
  - *Zhewei Yao, Yuxiong He*
  - `2026-10-20`
  - Long-horizon agentic reinforcement learning (RL) requires both efficient rollout generation and training on long sequences. However, the memory requirements and model-specific operators of Qwen3.8-Flash-Next make this difficult with existing open-source implementations. To resolv…

- **[Attention-based Classification for Indirect Prompt Injection](https://arxiv.org/abs/2610.28988v1)**
  - *Amelia Kawasaki, Stefan Lee*
  - `2026-10-20`
  - Indirect prompt injection (IPI) attacks, in which adversarial instructions are embedded in external data processed by a language model, pose a significant threat to the integrity of deployed LLM agents. Attention Tracker (Hung et al., 2025) is a recently proposed white-box detect…

- **[Transformers as Generic Deep Neural Networks: Exact Compilation, the Cost of Removing Activation-Activation Products, and Multi-Agent Attention Clustering](https://arxiv.org/abs/2610.28958v1)**
  - *Sergey Salishev, Zeev Volkovich, Oleg Granichin*
  - `2026-10-20`
  - Transformers are deployed as a special model class. Neural processing units (NPU) add dedicated operators for attention and normalization, and quantization relies on Transformer-specific algorithms. We show the computation does not force this. Every Transformer block, with attent…

- **[The Data Differentiator Framework (DDF): Quantifying Marginal Data Value with Information-Theoretic and Game-Theoretic Measures in an Agentic Evaluation Pipeline (SDSAE)](https://arxiv.org/abs/2610.28933v1)**
  - *Sukesh Kumar, Dilip Singh*
  - `2026-10-20`
  - In data-rich enterprises the hard question is not whether a candidate dataset is good in isolation, but whether it adds information beyond what the organization already holds, and whether that increment is worth its price. We present the Data Differentiator Framework (DDF), a com…

- **[One Policy, Many Styles: Where to Aggregate Preferences for Steerable Humanoid Control?](https://arxiv.org/abs/2610.28925v1)**
  - *Ziqian Huang, Yuzhuo Chen, Shimin Zhang et al.*
  - `2026-10-20`
  - Modern robotic agents are increasingly expected to support steerable control, where a single policy can adjust its behavioral style at runtime under changing user preferences. Preference-conditioned reinforcement learning provides this interface, but conditioning alone does not e…

- **[A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems](https://arxiv.org/abs/2610.28811v1)**
  - *Wendy Zheng, Liang Wu, Yinhan He et al.*
  - `2026-10-20`
  - Agentic systems have demonstrated strong capabilities on complex tasks by enabling multiple interacting large language model (LLM)-based agents to collaborate and execute subtasks in parallel. However, this collaborative structure introduces new challenges for reliably evaluating…

- **[An Explicit Feedback Contract for Iterative ML-Agent Harnesses](https://arxiv.org/abs/2610.28798v1)**
  - *Kehui Yao, Chuanbo Hu, Jiao Chen et al.*
  - `2026-10-20`
  - Iterative ML agents develop models by editing code, running experiments, reading a validation score, and choosing what to try next. In current harnesses this loop is served by an exact validation score returned after every attempt, which leaves the validation split open to adapti…

- **[Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets](https://arxiv.org/abs/2610.28787v1)**
  - *Hieu Tran, Hong Yu*
  - `2026-10-20`
  - Evaluations of large language model (LLM) agents report that pricing agents collude at others' expense. Yet collusion is defined by enforcement: a cartel, in which competitors share monopoly profits, holds only if a member who cheats is punished. We introduce an audit that tests…

- **[Measure First, Then Allocate: Calibrated Rollout Budgets for MCP Agents in Reinforcement Learning](https://arxiv.org/abs/2610.28785v1)**
  - *Hieu Tran, Zonghai Yao, Sunjae Kwon et al.*
  - `2026-10-20`
  - Training tool-using language models requires costly interaction, yet identical rewards within a rollout group provide no group-relative learning signal. We use reward disagreement to guide harness evaluation and the allocation of rollouts for policy training in Model Context Prot…

- **[Self-Credit: Credit Assignment for Long-Horizon Agentic RL via Intra-group Rescaling](https://arxiv.org/abs/2610.28388v1)**
  - *Fangcong Yin, Ming Yin, Tanvi Bhandarkar et al.*
  - `2026-10-20`
  - LLM agents are commonly trained with RLVR, but the sparse nature of typical RLVR rewards makes credit assignment challenging, especially for long-horizon tasks. We propose Self-Credit, an end-to-end agentic RL method that creates dense supervision signals from sparse outcome rewa…

- **[Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory](https://arxiv.org/abs/2610.28315v1)**
  - *Masahiro Kaneko, Hiromi Arai, Timothy Baldwin*
  - `2026-10-20`
  - Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed. We ask how consulting memory during dialogue changes what users go on to say, and thus what the memory comes to re…

- **[RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards](https://arxiv.org/abs/2610.28010v1)**
  - *Artem Mikhaylov, Pavel Konoplev, Nikolay Efanov et al.*
  - `2026-10-20`
  - The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provide strong semantic understanding and reasoning capabilities,…

- **[Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization](https://arxiv.org/abs/2610.27889v1)**
  - *Younghyun Kim, Wooseok Seo, Minseo Kim et al.*
  - `2026-10-20`
  - Recent studies in harness optimization have shown substantial performance gains in language model agents without updating model weights. A well-designed harness more effectively leverages the underlying model's capabilities by shaping context, tool use, and execution workflows. H…

- **[From Outcomes to Steps: Reliable Success-Aware Critic Learning for Long-Horizon Language Agents](https://arxiv.org/abs/2610.27623v1)**
  - *Jiaxi Liu, Shixiong Kai, Zhentao Tang et al.*
  - `2026-10-20`
  - Reinforcement learning for long-horizon language agents requires identifying whether intermediate actions make eventual task success more or less likely when supervision is available only at trajectory level. The main difficulty is that a critic with aggregate return-prediction a…

- **[OptionWorld: A Benchmark for Diagnosing Failures of LLMs as Long-Term Personal Assistants](https://arxiv.org/abs/2610.28491v1)**
  - *Ruoyu Zhang, Zhaocen Liu, Weiyi Tian et al.*
  - `2026-10-20`
  - Long-term assistants must follow unfinished tasks across days as information and circumstances change. Finding information or starting an action, however, does not ensure that the task gets completed. We introduce OptionWorld, a benchmark that traces information acquisition, judg…

- **[CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents](https://arxiv.org/abs/2610.28381v1)**
  - *Youmna Farag, Svetlana Stoyanchev, Simon Keizer et al.*
  - `2026-10-20`
  - Reasoning about safety is essential for embodied agents powered by large language models (LLMs). We introduce the Contextual Action and Plan Safety benchmark (CAPSafe), designed to evaluate safety reasoning at two levels: (1) an action-level dataset that tests whether a single ac…

- **[Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented Design](https://arxiv.org/abs/2610.28380v1)**
  - *Gaotang Li, Bhavana Dalvi Mishra, Yifei Ming et al.*
  - `2026-10-20`
  - Agent harnesses are executable code that specifies the prompts, tools, and control flow around a language model. A single global harness can struggle with heterogeneous tasks that require different execution strategies. In this work, we introduce Object-Oriented Harness (OO-Harne…

- **[From Abstraction to Action: DSLs for Natural Language Abstraction Interpretation and Execution](https://arxiv.org/abs/2610.28311v1)**
  - *Amit Lisha, Reut Tsarfaty*
  - `2026-10-20`
  - Natural-language instructions often rely on high-level abstractions, such as asking an agent to ``stack blocks in a pyramid.'' Interpreting abstract instructions requires models to both identify the abstraction intended by the speaker, and unroll it into the many concrete actions…

- **[Adaptive Stopping of Streamed Reasoning for Language Model Agents](https://arxiv.org/abs/2610.27981v1)**
  - *JunHyeok Oh, Byung-Jun Lee*
  - `2026-10-20`
  - Reasoning-enabled language model agents can incur substantial computation before acting, although the reasoning needed varies across decisions. Existing stopping signals, such as confidence and intermediate-answer stability, can vary in effectiveness across reasoning models; sign…

- **[SciDiagBench: A Type-Specific Benchmark for Human-Aligned Evaluation of Scientific Diagrams](https://arxiv.org/abs/2610.27841v1)**
  - *Hao Wang, Zixuan Li, Long Bai et al.*
  - `2026-10-20`
  - Recent agents have demonstrated strong capabilities in generating images from textual prompts, motivating their utilization for scientific diagram generation. Scientific diagrams naturally span diverse types, each characterized by distinct visual structures and content organizati…

- **[Memory as Code: Declarative Retrieval over Codified Long-Term Memory](https://arxiv.org/abs/2610.27700v1)**
  - *Aoting Zeng, Yuxin Du, Jianwei Wang et al.*
  - `2026-10-20`
  - In long-term memory systems, memories are constructed from interaction histories and retrieved in response to queries, enhancing the reasoning ability of LLM agents. In complex scenarios, facts are scattered across sessions and their relationships evolve over time, making it diff…

- **[The Butterfly Effect in LLM Social Simulations: From Architecture Sensitivity to Robustness Audits](https://arxiv.org/abs/2610.28981v1)**
  - *Jinyi Ye, Lei Cao, Ding Chen et al.*
  - `2026-10-20`
  - A butterfly effect occurs when a local perturbation propagates through a system and produces divergence in its collective outcome. In LLM social simulations, this creates a particular challenge for scientific inference: sensitivity to implementation choices can enter agent intera…

- **[Complete Street Design informed by Multi-Agent Simulation](https://arxiv.org/abs/2610.27509v1)**
  - *Sharika J. Hegde, Amirmohammad Khakpour, Pedram Beigi et al.*
  - `2026-10-20`
  - Objectives: Complete Street design is currently guided largely by qualitative principles despite the increasing complexity of multimodal urban traffic. This paper develops a microscopic simulation framework for quantitatively evaluating alternative street designs by explicitly re…

- **[VisualEvolve: A Skill Self-Evolution Framework for Visual Reasoning](https://arxiv.org/abs/2610.28386v1)**
  - *Jiawei Wang, Yucun Li, Xueqi Li et al.*
  - `2026-10-20`
  - Visual tool use enables vision-language models (VLMs) to acquire task-relevant evidence, but its effectiveness can be limited by predefined visual operations and the tool-use strategies learned during training. Representing these operations and strategies as reusable external ski…

- **[Projected Distillation: On Learning to Solve Hard Problems from Close, Correct Targets](https://arxiv.org/abs/2610.27467v1)**
  - *Shripad V. Deshmukh, Christian Bock, Kangrui Ruan et al.*
  - `2026-10-20`
  - On-policy learning is central to post-training: training on a model's own generations limits distribution shift and helps preserve existing capabilities. On hard problems, however, on-policy RL provides no reward-based learning signal when all attempts fail. On-policy distillatio…

- **[More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents](https://arxiv.org/abs/2610.27406v1)**
  - *Ruhan Wang, Kishan Panaganti, Dongruo Zhou*
  - `2026-10-19`
  - LLM agents can improve across tasks without updating model parameters by storing experience from their own executions in external memory and reusing it to guide later decisions. A central design question is whether to retain only observed trajectories and outcomes or also the rul…

- **[ProMemAgent: Long-Horizon Proactive Assistance with Context-Aware Prospective Memory from Sensory Perceptions](https://arxiv.org/abs/2610.27400v1)**
  - *Lilin Xu, Linyang He, Kaiyuan Hou et al.*
  - `2026-10-19`
  - Large language model (LLM) agents are moving beyond reactive responses toward proactive assistance that anticipates user needs without explicit requests. However, existing proactive agents primarily address immediate needs, while many everyday situations involve delayed intention…

- **[Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops](https://arxiv.org/abs/2610.27350v1)**
  - *Arnav Grover*
  - `2026-10-19`
  - Frontier models can control robots through agent harnesses that loop on one question: what motion comes next toward the user's goal? We show that this default loop carries out harmful instructions. With GPT-6 Astra controlling a low-cost SO-101 arm through the Inspect Robots harn…

- **[An LLM-Based Agent for Legal Compliance Assessment: Architecture, Memory, and Evaluation in a Canadian and Quebec Context](https://arxiv.org/abs/2610.27347v1)**
  - *Soukaina Alaoui Ismaili, Jean-Sebastien Dessureault*
  - `2026-10-19`
  - Checking whether a text complies with a body of law is slow when done by hand and fragile when done with keyword rules. This paper presents ComplianceAgent, the legal compliance sub-agent of COMPASS, a multi-agent framework that evaluates texts along four axes: digital sovereignt…

- **[Modeling Authentic Research Trajectories: A Graph View of Research Ideation](https://arxiv.org/abs/2610.27337v1)**
  - *Ruochen Li, Zhiyu Chen*
  - `2026-10-19`
  - The research idea in a published paper is rarely the project's initial idea. Between the two lies a closed-loop process in which researchers run experiments, derive insights, identify challenges, explore the literature, and revise the idea, with each step motivated by evidence an…

- **[Unsupervised Tool Evolution for Coding Agents in Data-Lake Analytics](https://arxiv.org/abs/2610.27327v1)**
  - *Yuqing Yang, Yurong Liu, Deqing Fu et al.*
  - `2026-10-19`
  - Coding agents can answer analytical questions over a data lake by discovering, cleaning, and joining the relevant data. However, they discard this work after each question and redo it from scratch for the next one. Tool evolution, which automatically builds and refines reusable t…

- **[Evolving Self-tuning Benchmarks for Long-Horizon Tool Use](https://arxiv.org/abs/2610.27307v2)**
  - *Hyunji Alex Nam, Michael Dennis, Natasha Jaques et al.*
  - `2026-10-19`
  - For AI assistants to move beyond simple chat interfaces and reliably assist users with applications like Gmail, Venmo, and Slack, we need to improve their tool-use capabilities. However, existing tool use benchmarks are still limited and difficult to scale because they rely on hu…

- **[Evaluating Context Compaction on the Questions That Come Later](https://arxiv.org/abs/2610.27301v1)**
  - *Junwei Yao, Yongxi Zhou, Zike Yang et al.*
  - `2026-10-19`
  - Language-model agents compact their context for the question at hand, but the compacted context must also serve questions that come later. We evaluate compaction on these later questions, using four corpora that annotate the evidence of several questions per text and recorded age…

- **[Vulnerability Analysis for Safe Multi-Agent Reinforcement](https://arxiv.org/abs/2610.27293v1)**
  - *Taozheng Zhu, Shixiong Jiang, Fanxin Kong*
  - `2026-10-19`
  - Safe Multi-Agent Reinforcement Learning (SMARL) aims to learn cooperative control policies under prescribed safety constraints. Al- though existing SMARL methods focus on enforcing safety during policy optimization, their vulnerability remains largely unexplored. This paper inves…

- **[TEX: Test-Time Scaling Testing Agents via Execution-based Cross-Validation](https://arxiv.org/abs/2610.27290v1)**
  - *Akash Gokul, Srijan Bansal, Yingbo Zhou et al.*
  - `2026-10-19`
  - Test-case generation is critical but remains challenging for language models. Existing test-time scaling methods either isolate candidates or aggregate traces, which do not scale to long-horizon tasks. We present TEX, a collaborative test-time scaling framework based on execution…

- **[A latent control model for realistic rodent motion](https://arxiv.org/abs/2610.27279v1)**
  - *Aidan Sirbu, Charles Y. Zhang, Yuanjia Yang et al.*
  - `2026-10-19`
  - The development of embodied models of animal behavior is a major goal of the neuro-AI community. Embodied models will enhance our ability to make direct comparisons between biological and artificial agents. To make such comparisons effective, though, we need embodied models that…

- **[AutoRedClaw: Automated Red-Teaming for Claw-Style Agents](https://arxiv.org/abs/2610.27244v1)**
  - *Hao Li, Tongyan Hu, Weidi Luo et al.*
  - `2026-10-19`
  - Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw. These claw-style agents maintain configuration files (e.g., AGENTS.md), long-term memory, and reusable skills. Once poisoned, this persistent state is repeatedly r…

- **[EGI-BENCH: An Enterprise General Intelligence Benchmark Suite](https://arxiv.org/abs/2610.27234v1)**
  - *Zhiwei Liu, Zhujun Lan, Jielin Qiu et al.*
  - `2026-10-19`
  - Enterprise adoption of LLMs in agentic workflows is gated by evaluations that span a wide arc of abilities: CRM operations, heterogeneous-document retrieval, personal data understanding, multi-turn planning, tool use, function calling, long-horizon research, and long-context soft…

- **[MMedAgent-Plus: Scaling Multimodal Medical Agents across Modalities, Tasks and Workflows](https://arxiv.org/abs/2610.27233v1)**
  - *Ruoxin Wang, Yuanting Pan, Binxu Li et al.*
  - `2026-10-19`
  - Medical workflows often require multiple interdependent analyses, but existing specialist and generalist AI models are not designed to coordinate them. We introduce MMedAgent-Plus, a multimodal medical tool-use agent that combines a vision-language planner with 18 leading special…

- **[Magnolia: A Persistent-Memory Agent Framework for Computational Chemistry](https://arxiv.org/abs/2610.27230v1)**
  - *Tao Jiang, Benjamin Navet, Yousouf Taghzouti et al.*
  - `2026-10-19`
  - Chemistry has recently entered a high-data regime as molecular databases from high-throughput platforms or computational studies have become available. Increasing automation within the chemical sciences leads to a more digital and precision chemistry. Dedicated scientific agents…

- **[LoWAgent: A Low-Resource Multilingual Benchmark for Web Agents](https://arxiv.org/abs/2610.27205v1)**
  - *Ocean Monjur, Daud Ahmad Nisar, Shahriar Kabir Nahin et al.*
  - `2026-10-19`
  - Web agents are typically evaluated on English-language interfaces, leaving their ability to operate across the world's multilingual websites largely unexplored. This gap is especially significant for low-resource languages, where standardized resources for evaluating web agents r…

- **[Understanding the Benefits of Scaffolds through Computational Separations](https://arxiv.org/abs/2610.27157v1)**
  - *Jingchu Gai, Adam Block, Andrej Risteski*
  - `2026-10-19`
  - Inference-time harnesses, i.e., external procedures that call a model many times and keep state across calls, can substantially improve model capabilities. In this paper, we investigate the benefits of using such harnesses and the extent to which these benefits can be internalize…

- **[EDMA: Entropy-Driven Multimodal Answering](https://arxiv.org/abs/2610.27120v1)**
  - *Emanuele Mezzi, Gertjan Burghouts, Fabio Massacci et al.*
  - `2026-10-19`
  - Multimodal question answering (MMQA) is based on integrating heterogeneous data sources, selectively leveraging relevant modalities, and ignoring distractors. Existing approaches based on Multimodal Large Language Models (MLLMs) improve performance by splitting the task into inte…

- **[PORA: Learning When More Reasoning Pays Off for LLM Agents](https://arxiv.org/abs/2610.27119v1)**
  - *Bo Yan, Qi Zhang, Zhen Tan et al.*
  - `2026-10-19`
  - LLM agents perform tasks over multiple steps and revise their actions based on feedback. As the total reasoning budget is often limited and must support future steps, the agent must choose between short and long reasoning before each action. Longer reasoning may improve the final…

- **[PROVISO: Provenance-Informed Action Selection for Secure LLM Agents](https://arxiv.org/abs/2610.27115v1)**
  - *Bo Yan, Qi Zhang, Ziwen Kan et al.*
  - `2026-10-19`
  - LLM agents act on the external world through tools and third-party skills, so a single executed action can cause irreversible harm. Existing defenses judge a proposed action without tracking whether its content comes from the user or from external sources such as tool outputs, an…

- **[A general-purpose System One decision model for clinical records](https://arxiv.org/abs/2610.27099v1)**
  - *Andrew Zhang, Trinh T. L. Vuong, Sophia J. Wagner et al.*
  - `2026-10-19`
  - Clinical care, health-system operations and biomedical discovery depend on extracting reliable answers from patient records, yet applying diverse clinical questions across entire populations remains computationally expensive. Here we present Clinical System One (CS1), a 4-billion…

- **[OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory](https://arxiv.org/abs/2610.26860v1)**
  - *Yu Zhou, Cheng-Fu Yang, Rui Sun et al.*
  - `2026-10-19`
  - Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base…

- **[CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting](https://arxiv.org/abs/2610.26852v1)**
  - *Zehao Wang, Jianpeng Yao, Yuping Wang et al.*
  - `2026-10-19`
  - Reinforcement learning enables mobile robots to make fast and scalable navigation decisions in constrained human-shared environments. However, directly extending single-robot approaches to multi-robot settings often fails to ensure safety and efficiency, especially under occlusio…

- **[Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy](https://arxiv.org/abs/2610.26848v1)**
  - *Zekai Li, Jiayi Yu, Jinlu Zhang et al.*
  - `2026-10-19`
  - In this paper, we systematically investigate the mechanisms, scaling behavior, and generalization of physical Recursive self-improvement. We introduce PhysRSI-eval to quantify physical RSI through a five-axis metric: First-Attempt Performance, Efficiency, Success, Budget and Impr…

- **[WeAct: Dynamic Weight Switching as Agent Actions](https://arxiv.org/abs/2610.26847v2)**
  - *Rui Shi, Xunjian Yin, Jiacheng Sang et al.*
  - `2026-10-19`
  - Long-horizon agents must learn heterogeneous capabilities from interleaved trajectories. Updating shared parameters to learn new capabilities can degrade previously acquired ones, resulting in catastrophic forgetting. As a trajectory unfolds, different stages may require differen…

- **[Train An Imaginative Agent](https://arxiv.org/abs/2610.26845v1)**
  - *Jiaxin Ge, Junyi Zhang, Tianning Chai et al.*
  - `2026-10-19`
  - A seemingly reasonable push in Sokoban can make the puzzle unsolvable. To avoid such mistakes, an agent has to anticipate the consequences of its actions before execution, especially when feedback from the real environment is sparse or actions are irreversible. We introduce Agent…

- **[AnyGoal: On World Model Generalization Beyond Expert Rollouts](https://arxiv.org/abs/2610.26844v1)**
  - *Heejeong Nam, Divyat Mahajan, Quentin Le Lidec et al.*
  - `2026-10-19`
  - The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For these uses to be reliable, however, the learned dynamics must behave well beyond th…

- **[Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy](https://arxiv.org/abs/2610.26836v1)**
  - *Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu et al.*
  - `2026-10-19`
  - LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads on demand. We ask where this costs accuracy with a real scientific tool: PHREEQC…

- **[ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry](https://arxiv.org/abs/2610.26829v1)**
  - *Matt Turk, Brandon L. Neel, Diana M. Lopez et al.*
  - `2026-10-19`
  - Frontier agents retrieve structural metadata well and compute geometry from coordinates less reliably. We ask how much of a benchmark score reflects that gap and how much reflects the evaluation configuration around the model. We study ProteinGeoBench, a suite of 131 protein-stru…

- **[RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through Web Development](https://arxiv.org/abs/2610.26826v1)**
  - *Yuchi Wang, Rongyao Fang, Weihao Yu et al.*
  - `2026-10-19`
  - Beyond basic tool use and coding skills, effectively incorporating visual references into agentic generation is equally essential for applying AI agents to real-world productivity tasks. We study this crucial capability through webpage development, a practical and readily evaluab…

- **[ReuF2F: Benchmarking Coding Agents on Formalized Undergraduate Research Problems](https://arxiv.org/abs/2610.27046v1)**
  - *Zeyu Zheng, Yiyang Liu, Yuyang Zhao et al.*
  - `2026-10-19`
  - As AI systems begin to resolve open research problems, reliable verification becomes increasingly important. Formal mathematics provides a trusted framework for mathematical reasoning, enabling agents to produce machine-checkable proofs while conducting mathematical exploration.…

- **[Physical AI: Concepts, Techniques, and Challenges](https://arxiv.org/abs/2610.27045v1)**
  - *Weinan Zhang, Chunhua Shen, Tianfan Xue et al.*
  - `2026-10-19`
  - In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry. However, the field has yet to reach consensus on its definition, technical landscape, and core challenges. To address this…

- **[Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams](https://arxiv.org/abs/2610.26781v1)**
  - *Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao et al.*
  - `2026-10-19`
  - Phone scams impose substantial and growing costs on individuals and financial systems worldwide, yet existing countermeasures impose no resource cost on perpetrators. Strategic scam-baiting, in which automated agents engage scammers to deplete their operational capacity, offers a…

- **[VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM Agents](https://arxiv.org/abs/2610.28679v1)**
  - *Jianing Yin, Ziyi Chen, Hao Wang et al.*
  - `2026-10-19`
  - Agents need reliable ways to validate their outputs, both when completing tasks and when filtering synthetic training data. We study verifier generation: from the instruction and environment available for solving a task, an agent writes an executable verifier that must accept eve…

- **[M-Plan: Comprehensive Planning For LLM Agents with Memory Arrangement](https://arxiv.org/abs/2610.27032v1)**
  - *Ziyang Liu, Jiakang Yuan, Jiayuan Fan et al.*
  - `2026-10-19`
  - Large language model (LLM)-based agents have recently demonstrated outstanding performance in single-turn tasks, yet they continue to struggle with long-horizon tasks, particularly in environments without prior training. A key limitation of single LLMs is their difficulty in proc…

- **[StepBench: Diagnosing Real-World Procedural Understanding in AI Agents](https://arxiv.org/abs/2610.26679v1)**
  - *Hossein A. Rahmani, Bin Wu, Chaeeun Lee et al.*
  - `2026-10-19`
  - Evaluating an agent's planning ability remains challenging for open-domain tasks, where verifying procedures through execution is often impractical. Existing evaluations typically assess only the final plan and do not distinguish procedural errors such as missing, incorrect, or m…

- **[Honeypots for AI Agent Insider Threats](https://arxiv.org/abs/2610.26664v1)**
  - *Jan Wehner, Jam Kraprayoon*
  - `2026-10-19`
  - AI agents deployed inside organizations can pose an insider threat if they make mistakes, are compromised by an attacker, or pursue misaligned objectives. We propose honeypots as an AI control method to improve the security of internal agent deployments. Rather than only using ho…

- **[AllPath: Layered Verification for a Deployed, Self-Revising LLM Trading Agent under Human-Gated and Autonomous Regimes](https://arxiv.org/abs/2610.26662v1)**
  - *Tian Zhang, Meng Li*
  - `2026-10-19`
  - LLM trading agents are evaluated almost exclusively in backtests and autonomous benchmark harnesses. Deployment, where actions are irreversible, raises a different question: who verifies the agent's actions, and which failures can each verifier structurally catch? We report on Al…

- **[Tandem: Serving Hybrid Linear-Attention GUI Agents on Mobile NPUs](https://arxiv.org/abs/2610.26660v1)**
  - *Zhuomin Chen, Jingchao Ni, Xu Zheng et al.*
  - `2026-10-19`
  - Smartphone GUI agents complete tasks in mobile apps by repeatedly reading the screen and asking a model for the next action. Mobile neural processing units (NPUs) enable local execution, keeping screen contents on the phone, but model latency accumulates with every action. Hybrid…

- **[Revision-Based Learning from Interactive Experience and Feedback](https://arxiv.org/abs/2610.26636v2)**
  - *Jiawen Li, Chenming Ge, Alice Gao et al.*
  - `2026-10-19`
  - Code generation models are increasingly used to produce interactive artifacts, such as websites and user interfaces. Many properties that determine whether these interfaces are useful only become apparent through realistic interaction, making them difficult to incorporate into mo…

- **[When the harness decides success: state that cannot be re-observed](https://arxiv.org/abs/2610.26632v1)**
  - *Raimondas Lencevicius*
  - `2026-10-19`
  - Agent harnesses decide what a language model sees across turns: they drop old turns, summarize them, or replay the model's own earlier reasoning. We ask when these choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registe…

- **[Teaching AI Agent to Play Poker Strategically Through Preference Optimization](https://arxiv.org/abs/2610.27028v1)**
  - *Phurinat Polasa, Thanapon Thanadunpremdet, Phatthanasak Kraiduang et al.*
  - `2026-10-19`
  - A poker agent can make a legal move and still make a strategically poor one. We ask whether compact AI agents can exhibit strategic behavior under hidden information and whether preference optimization can improve beyond static and zero-shot policies. We first evaluate a static b…

- **[Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games](https://arxiv.org/abs/2610.26568v1)**
  - *Durgam Latha, Dion Reji, Dorde Zikelic et al.*
  - `2026-10-19`
  - Robust partially observable Markov decision processes model agents that act under partial observability while adversarial environment resolves uncertainty in the transition probabilities. Reward objectives such as discounted-sum, long-run average and cumulative reward under finit…

- **[BetaMem: Learning to Remember a Changing World for Embodied Agents](https://arxiv.org/abs/2610.26554v1)**
  - *Mai Liu, He Sun, Siru Zhong et al.*
  - `2026-10-19`
  - Long-horizon embodied agents face temporal confusion and incomplete or distorted records, recurring errors from fixed memory rules, and growing storage and retrieval costs. We present BetaMem, a framework for building and evolving traceable long-term memory through six linked lay…

- **[Agentic Orchestration of EDC Data Space Retrieval and Natural Language Driven Data Processing](https://arxiv.org/abs/2610.26548v1)**
  - *Marla Grunewald, Fin Gentzen, Iulisloi Zacarias et al.*
  - `2026-10-19`
  - Participating in a data space still requires the Dataspace Protocol (DSP) negotiation flow to be hand-coded against each provider's access policy. We present a multi-agent architecture that automates this process using natural language requests. Built on LangGraph over an Eclipse…

- **[Does Multi-Agent Collaboration Reduce Hallucination in Clinical Tasks?](https://arxiv.org/abs/2610.27027v1)**
  - *Won Seok Jang, Harry Bhaskar Joshi, Hong Yu*
  - `2026-10-19`
  - Multi-agent LLM systems improve performance on clinical tasks, and that improvement is often read as evidence of a more trustworthy system. However, the two are not the same claim. A clinician acts on the stated reasoning and not only on the conclusion, so whether collaboration r…

- **[RouterWorld: Scaling Conversational AI with Latency-Aware LLM Routing](https://arxiv.org/abs/2610.26511v1)**
  - *Jinyang Li, Denis Emelin, Simone Tedeschi et al.*
  - `2026-10-19`
  - Conversational AI systems built on Large Language Models (LLMs) require routing mechanisms that balance answer quality and response latency at scale. However, existing LLM routing benchmarks assume full observability of all candidate model outcomes, under-emphasize latency as a f…

- **[ScopeMem: Latent Memory That Learns Where to Revise Frozen GUI Agents](https://arxiv.org/abs/2610.26503v1)**
  - *Zhicheng Zheng, Cheng Zhang, Shengping Yu et al.*
  - `2026-10-19`
  - Latent memory is gaining ground as a lightweight history supplement for GUI agents. It supplies history to a frozen vision-language model via prefix vectors trained with step-wise cross-entropy (CE). While resulting gains are naturally attributed to encoded history, our controlle…

- **[VeriCUA: Learning Proactive Verification for Reliable GUI Agent Rewards](https://arxiv.org/abs/2610.26469v1)**
  - *Zhizhou Wang, Yaxi Lu, Zhong Zhang et al.*
  - `2026-10-19`
  - Reinforcement learning for computer-use agents increasingly relies on proactive reward agents that interact with the post-execution GUI environment to verify what recorded screenshots cannot reveal. The reliability of such verification hinges on two coupled decisions: what to che…

- **[Learning What to Remember: Resource-Efficient Self-Improvement for Lifelong Agents](https://arxiv.org/abs/2610.26453v2)**
  - *Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang et al.*
  - `2026-10-19`
  - Self-improving agents aim to continuously improve their behavior by learning from experience after deployment. However, accumulating and reusing more experience does not necessarily lead to better decisions, particularly when generation, interaction, and memory resources are join…

- **[Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents](https://arxiv.org/abs/2610.26438v1)**
  - *Mengxiao Wang, Nitesh Saxena*
  - `2026-10-19`
  - Large language model (LLM) agents now trade real capital using news as evidence, yet they cannot reliably tell fabricated headlines from real news. Because they read the same feeds under near-identical policies, a single fabricated post can push them into the same trade at the sa…

- **[When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories](https://arxiv.org/abs/2610.26394v1)**
  - *Tianqi Liu, Yandong Guan, Songze Li et al.*
  - `2026-10-19`
  - Coding agents increasingly undertake development tasks in mature enterprise repositories, yet existing benchmarks offer limited insight into whether they fulfill complete Product Requirement Documents (PRDs) and where delivery breaks down. Issue resolution and development from sc…

- **[Autonomous intelligence for mining productivity: a multi-agent AI approach to operational value creation](https://arxiv.org/abs/2610.26369v1)**
  - *N Guerin, A Dehoux, M Nakhla*
  - `2026-10-19`
  - Integrated Remote Operation Centres (IROCs) are emerging as the architectural frontier of Industry 4.0 for capital-intensive sectors such as mining, oil and gas, and energy. Yet two intertwined gaps constrain their evolution towards full autonomy. First, no integrated agentic arc…

- **[VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement](https://arxiv.org/abs/2610.26342v2)**
  - *Ruotian Peng, Yuanyi Ren, Shuaiqi Liu et al.*
  - `2026-10-19`
  - Recursive self-improvement (RSI) requires agents to diagnose system bottlenecks and coordinate improvements across training and inference. We refer to the agents' capability to jointly optimize training data, the trainer, and the inference harness as cross-component co-design. We…

- **[The Control Layer Behind Rule-Following Agents Trading Across Market Conditions](https://arxiv.org/abs/2610.26324v1)**
  - *Saad Naja, Nasser Odtallah, Jake Van-Praag et al.*
  - `2026-10-19`
  - Trading discipline often fails people. Our study tested whether four AI trading agents followed their strategies and risk rules. Offering traders the evidence and an agent evaluation toolkit to separate luck from following the rules, before giving agents meaningful autonomy or ca…

- **[The Scheduler Is a Hidden Retriever: How Asynchrony Shapes Evidence Acquisition in Search Agents](https://arxiv.org/abs/2610.26310v1)**
  - *Ruiyang Ren, Yuhao Wang, Yinan Zhang et al.*
  - `2026-10-19`
  - Language-model agents increasingly solve complex tasks through parallel reasoning and asynchronous information gathering. Controlled replay across two model families and three benchmarks shows that delivery timing redirects search decisions made before all results arrive, despite…

- **[Toward Online Robust Zero-Sum Markov Games with Function Approximation](https://arxiv.org/abs/2610.26286v1)**
  - *Chenhao Zhou, Jiyu Wei*
  - `2026-10-19`
  - Online robust zero-sum Markov games pose a coupled operator-learning and game-solving problem: from nominal interaction data, the learner must recover a worst-case minimax Bellman operator while maintaining strategic coverage and controlling stage-game approximation error. Existi…

- **[Reliable Before Profitable: QuantHarness for Governing Financial Strategy Development with LLM Agents](https://arxiv.org/abs/2610.26101v1)**
  - *Jiasheng Mao, Jiacheng Liu, Hengwei Ye et al.*
  - `2026-10-19`
  - LLM agents can turn natural-language financial research requests into executable and backtested strategies, but a successful run may still implement the wrong rule, use information unavailable at decision time, or obscure how repairs and candidate selection changed the strategy.…

- **[From Code to Playable Systems: CEGame-Bench for Long-Horizon Game Creation Agents](https://arxiv.org/abs/2610.26098v1)**
  - *Zixuan Dong, Yanghai Wang, Hanyan Bian et al.*
  - `2026-10-19`
  - A game ships when a player can launch it, finish it, and return to a saved world, none of which a successful build guarantees, yet game-creation agents are mostly tested on one engine or on one-prompt browser games. We present CEGame-Bench, the first long-horizon benchmark for co…

- **[CUA-Lite: An Open Platform for Computer Use Agents](https://arxiv.org/abs/2610.26071v1)**
  - *Zhanhui Zhou, Weichen Zhang, Haoran Liu et al.*
  - `2026-10-19`
  - Open resources for computer use agents (CUAs) -- environments, datasets, and models -- remain scattered: without a standard, these resources cannot be integrated and scaled; additionally, evaluation, RL, and SFT cannot share one infrastructure. We present CUA-Lite, an open platfo…

- **[Decision4Rec: A Jev-Inspired Framework of Decision Models on Knowledge and Active Graphs for Multi-Agent Recommender Systems](https://arxiv.org/abs/2610.26035v1)**
  - *Marco Polignano, Het Darshan Mehta, Pasquale Lops et al.*
  - `2026-10-19`
  - Decision models, such as the commercial Jev, are language models that return one probability for each option of a question instead of generating text. We present Decision4Rec, an open and modular framework that makes decision models useful for recommendation. A knowledge graph wr…

- **[AuDQ: Auditable Data Quality through Agentic Rule Discovery](https://arxiv.org/abs/2610.26031v1)**
  - *Jacopo Biggiogera, Nicolas Colombo, Krati Saxena et al.*
  - `2026-10-19`
  - High-stakes tabular pipelines rely on scattered, static quality checks that are hard to evolve and audit against policy intent. Regulated domains particularly suffer as the LLM-era automation raises expectations for traceability and accountability. We propose a vision for an onto…

- **[SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents](https://arxiv.org/abs/2610.26995v1)**
  - *Ran Zhou, Zehui Kong, Fanyu Lin et al.*
  - `2026-10-19`
  - LLM-based agents increasingly rely on reusable skills. However, scaling skill libraries makes efficient and accurate skill use difficult. Full skill loading incurs high token and runtime overhead. In contrast, flat semantic retrieval treats skills as independent text entries, ign…

- **[Procedural Memory for Language Agents: A Neurosymbolic Perspective on Explicit Goal Structure](https://arxiv.org/abs/2610.25996v1)**
  - *Jonathan Leung, Zhiqi Shen, Deheng Ye*
  - `2026-10-19`
  - Large language models remain unreliable on long-horizon tasks requiring procedural reasoning. We argue that a key cause is the absence of explicit procedural memory: accessible, modifiable knowledge of how tasks are accomplished, distinct from semantic and episodic memory. Goal-O…

- **[Map-Distribution Mixture-of-Experts for Multi-Agent Pathfinding](https://arxiv.org/abs/2610.25991v1)**
  - *Fumimaro Suzuki, Keisuke Okumura*
  - `2026-10-19`
  - Designing capable neural policies for multi-agent pathfinding (MAPF), which map local observations to action distributions, represents an important challenge in multi-agent learning, with practical relevance to scalable collective automation problems such as warehouse logistics.…

- **[NIOCIS: Typed-Decision Next-Hop Routing with Node-Conditioned Option Spaces for Tool-Use Agents](https://arxiv.org/abs/2610.25985v1)**
  - *Jin Han, Mingfeng Xin, Feng Liang et al.*
  - `2026-10-19`
  - Tool-use agents pay per decision: at each hop a language model re-reads the state and thinks for seconds, though its actions are finite and decisions recur. We present NIOCIS, a routing layer that folds execution logs into a loop-collapsed action graph (forward transitions plus r…

- **[ClueFlow: Learning Long-Horizon Search through Attributed Research-State Transitions](https://arxiv.org/abs/2610.25980v1)**
  - *Yicheng Wang, Wentao Tan, Yidan Huang et al.*
  - `2026-10-19`
  - Long-horizon search requires agents to acquire relevant evidence and integrate it into an evolving research state. Existing methods maintain research states to guide exploration or assign turn-level progress signals, yet grounding these signals in explicit, attributable state cha…

- **[GLOBE: Geometry-Led Online Behavioral Early Exit via Unit-Sphere Trajectories](https://arxiv.org/abs/2610.25970v1)**
  - *Xinyue Peng, Zhenlin Liang, Meng Cai et al.*
  - `2026-10-19`
  - Chain-of-thought (CoT) reasoning can improve problem solving, but models often keep generating after the correct answer is already reachable; the extra steps raise serving costs and may replace a correct intermediate result with an incorrect one. We propose GLOBE (Geometry-Led On…

- **[EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models](https://arxiv.org/abs/2610.25959v1)**
  - *X. Feng, J. Tang, Z. Lin et al.*
  - `2026-10-19`
  - Building embodied agents that can perceive, reason, and act across diverse 3D worlds is a central research direction toward artificial general intelligence. Yet most existing work remains confined to specific tasks in a single scene and transfers poorly to new environments, leavi…

- **[Productive State-Space Exploration for Multi-turn RL in LLM Agents](https://arxiv.org/abs/2610.25957v1)**
  - *Mohammed Haroon Dupty, Yong Liang Goh, Song Guo et al.*
  - `2026-10-19`
  - Reinforcement Learning (RL) for Large Language Model (LLM) agents in multi-turn, long-horizon environments remains challenging due to inefficient action selection and repetitive behavioral patterns. In particular, agents often become trapped in high-confidence yet unproductive be…

- **[CXBench: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows](https://arxiv.org/abs/2610.25954v1)**
  - *Boxi Yu, Yuzhong Zhang, Zhenfeng Su et al.*
  - `2026-10-19`
  - Tool-using language agents increasingly perform regulated customer-service workflows, where a correct final state is insufficient: agents must also provide disclosures, obtain consent, and follow required procedures. Existing tool-agent benchmarks largely score final business sta…

- **[AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time Adaptation in Evolving Environments](https://arxiv.org/abs/2610.25950v1)**
  - *Rui Wang, Zishen Lai, Jiayu Liu et al.*
  - `2026-10-19`
  - Large Language Model (LLM) agents are increasingly deployed in unfamiliar and evolving environments, requiring them to proactively explore, understand, and adapt to environmental dynamics. However, existing benchmarks rarely test whether agents can proactively discover how an env…

- **[Claim Laundering: When Agent Decision Models Trust Records Over Reality](https://arxiv.org/abs/2610.25947v1)**
  - *Tina Khezresmaeilzadeh, Seyedarmin Azizi, Erfan Baghaei Potraghloo et al.*
  - `2026-10-19`
  - Agent decision models select actions in a single forward pass from inputs that combine environmental observations with the agent's own record of previous actions. When an action fails silently, these sources can conflict: the record reports success, but the environment shows that…

- **[Policy Search in Code Space for Multi-Agent Pathfinding](https://arxiv.org/abs/2610.25946v2)**
  - *Matthias Eder, Pantelis Emmanouil, Vivek Farias et al.*
  - `2026-10-19`
  - Developing coordination policies for complex multi-agent systems relies on either labor-intensive algorithm design or opaque task-specific reinforcement learning. With recent advances in autonomous coding agents, we show that policy search directly in code space offers a compelli…

- **[EvoSkill v2: Fully Agentic Skill Evolution from Benchmark Adaptation to a Stateful Evolver](https://arxiv.org/abs/2610.25931v1)**
  - *Dastin Huang, Baran Nama, Salaheddin Alzubi*
  - `2026-10-19`
  - EvoSkill v2 is a three-agent system that edits the instructions (skills) an agent is given, leaving its model and harness intact. The user starts a run by describing a benchmark and supplying a grader, which a benchmark adaptor turns into a benchmark-specific plugin. A solver att…

- **[TESS: LLM-guided Translation, Exploration, Simulation, and Search for Embodied Task Planning](https://arxiv.org/abs/2610.25930v1)**
  - *Peiran Xu, Yixiang Yang, Jinghan Li et al.*
  - `2026-10-19`
  - In this work we focus on the problem of embodied task planning, which requires an agent to accomplish a complex task by separating it into atomic actions. Recent studies have developed LLM-based methods to address this problem. However, the executability and correctness of the ge…

- **[Secure Agentic Coding through Counterexample-Grounded Feedback](https://arxiv.org/abs/2610.25916v2)**
  - *Tue Le, Anh Nguyen Hoang, Gabriel Sasseville et al.*
  - `2026-10-19`
  - As coding models and agent harnesses become more capable, reliable security verification is becoming a central bottleneck. Improving secure code generation requires a signal whose reported progress remains aligned with actual program behavior under optimization; otherwise, an opt…

- **[When Should AI Chime In? Benchmarking Timely Contribution of Proactive Agents in Multi-Party Chat](https://arxiv.org/abs/2610.25896v1)**
  - *Ruotong Wang, Brian S. Yu, Xinyi Zhou et al.*
  - `2026-10-19`
  - Proactive agents can support group collaboration by surfacing useful information without waiting to be asked, but even relevant contributions can be disruptive if poorly timed. In this work, we isolate the timing question: given a fixed candidate contribution such as a clarificat…

- **[Are Self-Evolving Agents Continual Learners?](https://arxiv.org/abs/2610.25858v1)**
  - *Xiaoyin Chen, Yizheng Huang, Yinglun Xu et al.*
  - `2026-10-19`
  - Large language model agents are often deployed in environments where new knowledge, tools, and workflows keep arriving. Such an agent is therefore expected to adapt continually, learning new tasks as they arrive without forgetting earlier ones. This resembles the continual learni…

- **[MASIF: Implicit Failures for Process Observability in Multi-Agent Systems](https://arxiv.org/abs/2610.25852v1)**
  - *Yanwei Huang, Arpit Narechania, Atanu Sinha*
  - `2026-10-19`
  - Multi-agent systems (MAS) can complete a task despite local execution errors that are corrected, bypassed, or carried forward without individually determining its outcome. We call these implicit failures (IFs) and study them as signals for process observability beyond final task…

- **[A Cue's Hidden Price: Auditing Seller Influence on AI Shoppers](https://arxiv.org/abs/2610.25843v1)**
  - *Felix Buecheler, Gerardo Berbeglia, Mingyu Guo*
  - `2026-10-19`
  - Large language models are increasingly asked to shop on a user's behalf, which lets seller-controlled content such as badges, endorsements, and framing steer what they recommend. That poses the question at the core of generative engine optimization (GEO): not whether seller conte…

- **[FrontierRefactor: Benchmarking Multi-Scale Performance-Oriented Codebase Refactoring](https://arxiv.org/abs/2610.25834v1)**
  - *Shijian Wang, Fanqing Meng, Jiajun Chen et al.*
  - `2026-10-19`
  - Autonomous codebase refactoring requires coding agents to restructure working software while strictly preserving externally observable behavior and prioritizing execution performance and compute efficiency over stylistic preference. Existing benchmarks: refactoring benchmarks ass…

- **[Can LLM User-Proxies Stand In for Humans in Reliance Measurement? Replicating Rel-A.I. with Simulated Users](https://arxiv.org/abs/2610.25788v1)**
  - *Shuai Wang, Rui Hu*
  - `2026-10-19`
  - Can language-model user proxies reproduce human reliance on an AI answer across contexts? Published simulated-user studies do not establish validity for this partial-answer decision, and Rel-A.I.'s released human record omits trial-level choices. We audit its 90 printed questions…

- **[OpenSaC: A Python Library for Search as Code in Deep Research Agents](https://arxiv.org/abs/2610.25779v1)**
  - *Qi Liu, Jiaxin Mao, Fengbin Zhu et al.*
  - `2026-10-19`
  - Deep research agents investigate complex questions through iterative search, source examination, and evidence synthesis. A conventional workflow alternates reasoning with individual search and reading actions. Search as Code introduces a new paradigm: agents write programs that c…

- **[Standing on the Shoulders of Giants: Enhancing LLM Agents for Automated Fact-Checking with Human Expert Skills](https://arxiv.org/abs/2610.25777v1)**
  - *Xinwen Chen, Haorui He, Yupeng Li*
  - `2026-10-19`
  - Automated fact-checking (AFC) systems powered by large language model (LLM) agents still face challenges in evidence retrieval and claim verification. Existing approaches improve their capabilities through computationally costly post-training or human-in-the-loop feedback that is…

- **[From Trace to Fix: Residual Task State in Long-Horizon Agents](https://arxiv.org/abs/2610.25776v1)**
  - *Zile Huang, Ser-nam Lim*
  - `2026-10-19`
  - Recovering from failures in long-horizon, stateful language agents is challenging because the action introducing a defect, the symptom exposing it, and the persistent state requiring repair frequently diverge. Existing methods largely focus on retrospective failure attribution, l…

- **[EvalRx: Agentic Diagnosis and Verified Repair of Foundation Models](https://arxiv.org/abs/2610.25767v1)**
  - *Jiaqi Liu, Ruinan Jin, Yitong Tang et al.*
  - `2026-10-19`
  - Model evaluation reveals where models fail, but rarely why or whether a proposed fix genuinely works. We introduce EvalRx, an open-source agentic framework for statistically grounded model diagnosis and repair. EvalRx discovers systematic failure modes, explores candidate mechani…

- **[Computation, Not Memory: Chain-of-Thought and State Tracking in LLM Agents](https://arxiv.org/abs/2610.25760v1)**
  - *Pedram Mouseli, Massieh Moayedi*
  - `2026-10-19`
  - Language-model agents often reason before they act, and the value of monitoring that reasoning depends on how it relates to their actions. We ask how an agent's actions depend on its reasoning when the correct action depends on a changing state. In a small file-system task, backg…

- **[Remember Less, Adapt Longer: Bounded-State In-Context Reinforcement Learning with Recurrent Summary Memory](https://arxiv.org/abs/2610.25758v1)**
  - *Jiawen Wang, Cheng Xue, Peng Zhang et al.*
  - `2026-10-19`
  - In-context reinforcement learning (ICRL) enables agents to adapt to new tasks without parameter updates, relying on memory to retain what they learn from experience. For agents operating continually, existing approaches using memory trade off bounded cost against access to past e…

- **[TimelineAgent: An LLM-based Framework for Query-Centric Event Timeline Extraction Across Multiple Documents](https://arxiv.org/abs/2610.25733v1)**
  - *Qingkai Min, Yunxin Bao, Yifeng Lu et al.*
  - `2026-10-19`
  - Query-centric cross-document event timeline extraction aims to construct event timelines from multiple documents under diverse query focuses. The task is very challenging due to the heterogeneous event modeling and reasoning requirements arising from both the intrinsic complexity…

- **[Whose Credential Is It? How Owner Attribution in Agent MemoryShapes Cross-User Account Misuse](https://arxiv.org/abs/2610.25707v1)**
  - *Hau-Sing So, Daixian Liu, Carl Hou et al.*
  - `2026-10-19`
  - Shared long-term memory lets an LLM agent serving one user inadvertently retrieve another user's credentials, but it is unclear when such exposure leads to actual harm. We introduce a three-stage audit that separates three events: a foreign credential reaches the prompt (exposure…

- **[ToolOPD: Credit-Aware On-Policy Distillation for Tool-Use Agents](https://arxiv.org/abs/2610.25693v1)**
  - *Chu Zhao, Lei Tang, Yanming Wang et al.*
  - `2026-10-19`
  - On-policy distillation (OPD) enhances the capabilities of small language agents by providing dense, token-level supervision from a teacher model on student-generated trajectories. However, standard OPD implicitly assumes that credit is uniformly distributed across long-horizon tr…

- **[The Forward/Inverse Duality of Controlled Emergence:A Computational Design Program from Explanation to Engineering](https://arxiv.org/abs/2610.25630v1)**
  - *Hao Li, Minghui Ren, Shaowen Lu*
  - `2026-10-19`
  - The macroscopic capabilities of intelligent systems arise from the local interactions of many simple units. When such systems are deployed in the real world, their behaviour must nevertheless be constrained, leaving designers caught between releasing adaptability and preventing l…

- **[Selecting and Composing Agent Design Patterns: Industrial Case Evidence and Controlled Reference-System Experiments](https://arxiv.org/abs/2610.25629v1)**
  - *Jia Huang, Bingsheng Ru, Bo Liang et al.*
  - `2026-10-19`
  - Agent pattern catalogs describe architectural alternatives, but engineers also need evidence for selecting and composing them. We extend a cognitive-function--execution-topology framework with an evidence-driven selection procedure and explicit composition contracts. The study co…

- **[Weighted State Souping for Efficient Long-Context Retrieval](https://arxiv.org/abs/2610.25621v1)**
  - *William L. Tong, Aryo Lotfi, Emmanuel Abbe et al.*
  - `2026-10-19`
  - State space models (SSMs) combine fast inference and fixed state size with competitive language-modeling performance. Recently, state souping has been proposed as a procedure whereby an SSM independently encodes chunks of tokens like documents, tool definitions, or memory records…

- **[When Better Opportunities Backfire: Service Worker Responses to Parallel AI Deployment in Customer Acquisition](https://arxiv.org/abs/2610.25603v1)**
  - *Xinyu Fu, Shulong Luo, Narayan Ramasubbu et al.*
  - `2026-10-19`
  - As AI voice agents get deployed in high-volume contact centers, firms can route low-intent leads to AI and allocate high-intent leads to human workers. Drawing on sequential search theory, we posit that AI-induced task allocation reshapes work, enriching opportunities facing huma…

- **[You Are the Trigger: Speaker-Activated Backdoors](https://arxiv.org/abs/2610.27210v1)**
  - *Nataša Krčo, Euodia Dodd, Peter Romov et al.*
  - `2026-10-19`
  - Speech models are increasingly used as an interface to AI systems, from transcription tools to voice agents. Existing audio backdoors require an attacker to introduce triggers at inference time. We study a different threat model in which the attacker compromises the model during…

- **[Glass-Box Deep Reinforcement Learning for High-Speed Flow Control](https://arxiv.org/abs/2610.27132v1)**
  - *Ameya D. Jagtap*
  - `2026-10-19`
  - Deep reinforcement learning (DRL) is challenging long-held assumptions in active flow control. By learning directly from interaction with a flow, DRL agents can find actuation strategies for nonlinear, unsteady flows without explicit models, often exploiting mechanisms that class…

- **[LOB-Impact Benchmark: Emergent Market Impact in Generative Limit Order Book Models](https://arxiv.org/abs/2610.27100v1)**
  - *George Nigmatulin, Valentin Mohl, Sascha Frey et al.*
  - `2026-10-19`
  - Realistic market impact is essential for generative limit order book (LOB) models to serve as world models for trading agents. If a simulator misprices this mechanism, agents learn policies that are optimal in the simulator but wrong in the real market. Existing metrics assess ge…

- **[MemT-1.0: Towards Memory-Native Evolution](https://arxiv.org/abs/2610.26825v2)**
  - *Zhiyu Li, Zeyu Zhang, Linyun Liu et al.*
  - `2026-10-19`
  - Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of mod…

- **[Cooperative Multi-Agent Reinforcement Learning for Market Making on Prediction-Market Order Books](https://arxiv.org/abs/2610.26789v1)**
  - *Skander Lejmi*
  - `2026-10-19`
  - A market maker provides liquidity by quoting prices to buy and sell an asset, earning the spread while managing inventory risk. We study market makers trained with multi-agent reinforcement learning on prediction markets, specifically Polymarket, whose thin order books pose disti…

- **[Topological Sheaves of Irreducibility: A Theoretical Framework for Multi-Agent Task Obstructions](https://arxiv.org/abs/2610.26777v1)**
  - *Steven Motta, Davide Mambelli, Alessandro Rozza*
  - `2026-10-19`
  - Multi-agent systems can differ under identical agents and communication budgets when they support different forms of joint interaction. We introduce Topological Sheaves of Irreducibility (TSI), a sheaf-theoretic framework separating task-level compatibility obstructions from syst…

- **[HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs](https://arxiv.org/abs/2610.26770v2)**
  - *Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen et al.*
  - `2026-10-19`
  - Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harn…

- **[Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows](https://arxiv.org/abs/2610.26676v1)**
  - *Qian Xie, Wenyue Hua, Yueli He et al.*
  - `2026-10-19`
  - LLM agentic workflows increasingly employ different models for specialized roles. Users may prefer different trade-offs between task quality and deployment cost, sometimes also considering latency. Finding good assignments incurs a separate search cost from evaluating multiple ca…

- **[LeakBench: Auditing Reward Hacking through Prediction-Time Leakage in Clinical Modeling Agents](https://arxiv.org/abs/2610.26088v1)**
  - *Xiaoyuan Bao, Jingsi Jiang, Jiao Shan et al.*
  - `2026-10-19`
  - Autonomous clinical-modeling agents can optimize predictive performance while violating conditions that make a model usable. We introduce LeakBench, an executable, guideline-derived audit suite that tests agent decisions for prediction-time leakage, calibration, site-level evalua…

- **[FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation](https://arxiv.org/abs/2610.26036v1)**
  - *Yuxuan Wu, Miaopei Lin, Qiufang Ying et al.*
  - `2026-10-19`
  - Financial agents are expected to answer factual investment queries through open search, but financial multi-hop retrieval differs from general multi-hop QA in a crucial way: each intermediate answer is an exact typed constraint, such as an entity, date, event, or numerical indica…

- **[Maestro: Agentic Formal Proof Development by Coordination](https://arxiv.org/abs/2610.25920v1)**
  - *Haoyu Li, Zeren Shui, Yuhao Zhang et al.*
  - `2026-10-19`
  - Lean is increasingly used to verify mathematical proofs and software produced by LLM agents, but writing formal proofs remains hard. Existing prover systems take a divide-and-conquer approach that recursively decomposes hard proof obligations into easier lemmas and splits again a…

- **[ACE-Trader: Adversarial Co-Evolution for Generator-Critic Trading Systems](https://arxiv.org/abs/2610.25847v1)**
  - *Chang Zhou, Jiarun Zhou, Xingtong Yu et al.*
  - `2026-10-19`
  - Generator--critic trading systems pair an LLM-based trader that makes trading decisions with a red team agent that evaluates these decisions and provides feedback for revision. However, improving individual trading decisions does not ensure that both agents learn from experience…

- **[Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments](https://arxiv.org/abs/2610.25747v1)**
  - *JooKyung Yuh, Byungmin Park, Eunseo Choi et al.*
  - `2026-10-19`
  - Scientific model discovery requires proposing candidate models of an unknown system and designing experiments that discriminate among them. However, LLM-based approaches typically rely on in-context learning to predict outcomes and select experiments, lacking explicit model evalu…

- **[Latent Projection for Latent Planning](https://arxiv.org/abs/2610.26979v1)**
  - *Yoo Sung Jang, Michael Ryoo*
  - `2026-10-19`
  - Latent world models let an agent plan in latent space. The planner searches for an action sequence that minimizes a cost, and that cost is often the $\ell_2$ distance between the predicted terminal latent and the goal latent. The latent, however, is partly noise: the regularizer…

- **[Zephyrus-R1: Agentic Reinforcement Learning for Weather Reporting](https://arxiv.org/abs/2610.25625v1)**
  - *Fengfei Yu, Marshall Fisher, Isadora White et al.*
  - `2026-10-19`
  - Reinforcement learning (RL) has emerged as a key method for training AI models in scientific applications, but RL remains difficult when outputs cannot easily be verified against a known ground-truth answer. Natural-language weather forecast reports are one such domain: they tran…

- **[On the LLM Verification for Argument Graph Generation](https://arxiv.org/abs/2610.27361v1)**
  - *Jakub Bąba, Jarosław A. Chudziak*
  - `2026-10-19`
  - Multi-agent LLM systems can formalize natural-language argumentation end-to-end, turning plain text into structured graphs by classifying components, connecting them with relations, and enriching the resulting graphs into formal models. Quality assurance for those graphs is almos…

- **[RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents](https://arxiv.org/abs/2610.27295v1)**
  - *Xinying Cai, Bin Hu, Mingyu Jin et al.*
  - `2026-10-19`
  - Existing steering benchmarks are built around simplified, isolated generation tasks and evaluate a single behavioral attribute under controlled settings that do not reflect the diversity and complexity of practical deployment. As a result, performance on these benchmarks provides…

- **[Beyond Two Tracks: Speaker-Anchored Full-Duplex Dialogue Recovery](https://arxiv.org/abs/2610.27109v1)**
  - *Yuxuan Chen, Yang Xiao, Jack Sun et al.*
  - `2026-10-19`
  - Spoken interaction is moving from alternating turns to full-duplex conversation, where an agent listens while speaking. Learning this coordination requires natural dialogue with persistent speaker-resolved tracks, a data requirement that remains difficult to satisfy at scale. Gen…

- **[Can It Actually Work? Synthesizing Functional CAD Mechanisms](https://arxiv.org/abs/2610.26861v1)**
  - *Wenqian Zhang, Yangyi Huang, Zigeng Xu et al.*
  - `2026-10-19`
  - While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that sat…

- **[HoloCosm: Beyond Single-Metric Benchmark Compression Across Multiple Metrics](https://arxiv.org/abs/2610.26714v1)**
  - *Yupei Lin, Zhongzhan Huang, Junxin Li et al.*
  - `2026-10-19`
  - Benchmark compression reduces evaluation cost by selecting a small set of samples. Existing methods typically guide selection using a single metric, although benchmarks often assess models along multiple dimensions. We find that model rankings are often weakly correlated across m…

- **[The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits](https://arxiv.org/abs/2610.26433v1)**
  - *Iliya Zhechev, Radoslav Ralev, Chris Coleman et al.*
  - `2026-10-19`
  - We study whether geometric relationships between conversation turns, memory texts, and queries can predict answer correctness before generation. We evaluate four memory implementations with dense or hybrid retrieval and one observation-summary comparator. We embed these texts in…

- **[Self-Consistency of Entity Sets and Citations in a Deep Research System under Repeated Prompting](https://arxiv.org/abs/2610.26421v1)**
  - *Lauri Pykälä, Kimmo K. Kaski*
  - `2026-10-19`
  - Deep research agents (DRA) are commonly used for open-ended synthesis tasks where closed-world QA benchmarks are poorly suited to characterize relevant aspects of performance. We study the self-consistency of one commercial deep research system under repeated identical prompting,…

- **[Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents](https://arxiv.org/abs/2610.26233v1)**
  - *Zhenyu Zhang, Kewei Fu, Yongqi Tong et al.*
  - `2026-10-19`
  - Tool-using voice agents often leave users waiting after speech ends, even when actionable information arrives earlier in the request. Speculative approaches begin work during speech, but chunk-bounded or interrupt-on-update generation can truncate a tool call before its arguments…

- **[VISAGENT: An Agent-Based End-to-End Voice Interaction System](https://arxiv.org/abs/2610.26168v1)**
  - *Xiang Wang, Zhaoxiang Liu, Xiang Chen et al.*
  - `2026-10-19`
  - Voice-based public services have evolved from manual switchboards to intelligent platforms to meet modern user needs. However, current systems remain constrained by rigid menu-driven interaction, fragmented vertical services, and limited extensibility. To address these issues, we…

- **[LEAPS: Long-context Evaluation of Adaptive Pattern Learning and State Tracking](https://arxiv.org/abs/2610.25919v1)**
  - *Howard Yen, Nitya Mani, Alex Renda et al.*
  - `2026-10-19`
  - Long-context language models (LCLMs) power agents that act over long trajectories, from improving a codebase to running research experiments to forecasters that condition on lengthy histories. These applications draw on three distinct long-context capabilities: recall, where the…

- **[SWE-Residual: Evaluating Starting-State Robustness of Coding Agents](https://arxiv.org/abs/2610.25899v1)**
  - *Jinze Li, Weijie Liu, Jinfeng Xu et al.*
  - `2026-10-19`
  - Software engineering (SWE) benchmarks are the primary way to measure the capabilities of coding agents: an agent is placed in a code repository or machine environment, given a request, and judged by hidden tests. These benchmarks almost always start the agent from a clean state t…

- **[CoMem: Learning to Anticipate Failures from Retrieved Experience](https://arxiv.org/abs/2610.25790v1)**
  - *Yun Shen, Ming Shen, Tianjun Yao*
  - `2026-10-19`
  - Reflection lets LLM agents improve from their own attempts, but the memory it builds is local to a single task, so an agent reflecting on its own tends to revisit the same explanation for failure. Cross-task reflective memory addresses this in two forms: retrieved memory keeps pa…

- **[Discovery-Probability Graph Planning for Embodied Agents in Tasks with Hidden Cooperation Requirements](https://arxiv.org/abs/2610.26359v1)**
  - *Zihuang Cai, Changjian Chen, Zhuo Tang et al.*
  - `2026-10-19`
  - Embodied agents are increasingly capable of perceiving, planning, and acting autonomously in dynamic environments, demonstrating strong performance on complex cooperative tasks. Recent advances typically assume that cooperative tasks are known in advance. In real-world applicatio…

- **[Bidirectionality is Necessary in Cellular Machines for Exact-Arrival Multi-Agent Path Finding](https://arxiv.org/abs/2610.26272v1)**
  - *Masashi Aono*
  - `2026-10-19`
  - On ranked directed acyclic graphs coupled by vertex conflicts we study exact-arrival multi-agent path finding (departure and arrival pinned in place and time) posed as a distributed output task: every cell must emit its own bit of a valid joint path-support mask. The machines are…

- **[A GPU-Resident Pipeline for Multi-Robot 3D Inspection with Limited Perception](https://arxiv.org/abs/2610.26106v1)**
  - *Kryštof Pšenička, Stefan Edelkamp*
  - `2026-10-19`
  - We present a complete, GPU-resident pipeline for multi-robot 3D inspection of underwater structures. Given a triangle mesh and a fleet of $K$ robots, each carrying a short-range, limited field-of-view camera, the pipeline computes 6-DOF trajectories that jointly cover a target fr…

- **[Learning Who Talks to Whom: Role-Aware Communication Topology Scheduling for Efficient LLM Multi-Agent Collaboration](https://arxiv.org/abs/2610.25851v1)**
  - *Haibin Li, Wenya Yu, Xuefeng Jiang et al.*
  - `2026-10-19`
  - Multi-agent systems driven by large language models (LLMs) rely on structured communication topologies to facilitate information exchange and collaborative reasoning. However, effectively scheduling these topologies to dynamically determine who talks to whom and when to communica…

- **[MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced by Reinforcement Learning](https://arxiv.org/abs/2610.25748v1)**
  - *Zhongyu Wang, Chen Zuo, Qingxuan Sun et al.*
  - `2026-10-19`
  - With the rapid growth of online video consumption, video advertising has become a dominant component of digital advertising. Most personalized video advertising systems follow a retrieval-based paradigm, which matches ad content with user preferences in a feature space and recomm…


## Harness  (150)

### NeurIPS

- **[MVU-Eval: Towards Multi-Video Understanding Evaluation for Multimodal LLMs](https://arxiv.org/abs/2511.07250)**
  - *Tian-Hao Peng, Hao-Cheng Wang, Yuan-Xing Zhang et al.*
  - **NeurIPS 2025** · `2025-11-10`
  - The advent of Multimodal Large Language Models (MLLMs) has expanded AI capabilities to visual modalities, yet existing evaluation benchmarks remain limited to single-video understanding, overlooking the critical need for multi-video understanding in real-world scenarios (e.g., sp…


### ICML

- **[Harness Self-Evolution: Theory, Algorithms, Evaluation, Applications, and Impact](https://openreview.net/forum?id=m5jsFGXUM2)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - **ICML 2025** · OpenReview · `2026-10-11`
  - Building agents that learn from experience is a central goal of artificial intelligence. Harness self-evolution offers a path toward this goal by adapting the system around a fixed base model. This article develops a unified framework for examining how execution feedback produces…

- **[DS-Lighting: Making Agent Harnesses Explicit for Data-Science Automation](https://openreview.net/forum?id=m7wsVqhIYs)**
  - **ICML 2025** · OpenReview · `2026-10-11`
  - Large Language Model (LLM) agents have shown promise for automating data-science workflows, yet their end-to-end performance depends critically on the agent harness that represents tasks, manages execution state, constrains output artifacts, and provides evaluation feedback. Exis…

- **[Can Harness Optimization Improve Agents? Generalizable Gains Versus Evaluation Noise](https://openreview.net/forum?id=Ri0rU3rPOS)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Harness optimization methods revise an agent’s prompts, tools, memory, and run-
time control without updating model weights. We ask which of their improve-
ments can be distinguished from evaluation noise, and where the reliable ones
come from. We evaluate Meta-Harness, Agentic H…

- **[TAME: Transfer-Aware Model-Harness Co-Evolution through Learned Harness Revisions](https://openreview.net/forum?id=IXnpSW8g3v)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Agentic post-training relies on an execution harness that both assists the model and shapes the trajectories from which it learns. A harness that improves immediate success, however, need not produce capability that transfers when that support changes. We examine this distinction…

- **[Harness-Zero: Harness Distillation via Agent-as-Harness](https://openreview.net/forum?id=rZ7eO7DZmc)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent…

- **[Hypothesis-Conditioned Evaluation for Efficient Harness Optimization](https://openreview.net/forum?id=q55gCb73ub)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Harness optimization improves an LLM agent by editing its prompts, tools
and helper code with model weights fixed. Evaluating every edit on
every training task is expensive, but a small random sample can miss the
failure that motivated the edit. We introduce \emph{Hypothesis-Cond…

- **[Harness-Delta Attribution: Dissecting Gains From Harness Evolution](https://openreview.net/forum?id=PX4Zpvsaca)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Harness evolution automatically optimizes the prompts, skills, tools, and orchestration code around a fixed-weight model, offering a way to improve agentic systems without updating model weights. The agent harness is iteratively optimized to achieve higher performance on the sear…

- **[Visual Reasoning at the Harness Level: A Ladder for Controlled Evaluation](https://openreview.net/forum?id=8Rdl9qkU1A)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Advances in foundation models are shifting coding and working agents from predefined tools toward general computational environments. Yet existing visual agents often couple model, harness, and training choices, making it difficult to determine how this transition affects visual…

- **[AURA-Eval: Evaluation Framework for Acting Under Risk Awareness in LLM Agent Trajectories](https://openreview.net/forum?id=9XfH1iAA4W)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - LLM agents are increasingly taking actions with real consequences, yet safety evaluations often reduce their behavior to a final safe or unsafe outcome, obscuring whether the agent recognized the risk and how it responded. We introduce AURA-Eval, a framework for evaluating whethe…

- **[Rethinking the Evaluation of Harness Evolution for Agents](https://openreview.net/forum?id=QDdWiaNkk2)**
  - **ICML 2025** · OpenReview · `2026-09-17`
  - Harness evolution is an iterative search procedure that repeatedly evaluates and revises candidate harnesses used for LLM agents using task feedback. We revisit the evaluation of such automatic harness evolution procedures and identify two fundamental issues in the protocol. Firs…

- **[EvoVE: Evolving Video Evaluation Through A Self-Improving Harness](https://openreview.net/forum?id=adiE97Xeyr)**
  - **ICML 2025** · OpenReview · `2026-09-17`
  - Modern video generation models are improving at a rapid rate, and they are quickly spreading into domains such as film production, advertising, education, and robotics simulation. Each new generation brings new capabilities and, with them, new failure modes: Seedance 2.5 accepts…

- **[Harness-MAP: Budget-Efficient Harness Search via Structure-Token Factorization](https://openreview.net/forum?id=HM48DQvAqS)**
  - **ICML 2025** · OpenReview · `2026-09-17`
  - Automating harness evolution via naive meta-agent search is prohibitively expensive, requiring hundreds of meta-agent calls and minutes-to-hours per evaluation.
How can we efficiently search for a diverse set of high-quality harnesses under a tight evaluation budget?
To address t…

- **[PACE-3D: A structure-aware multi-dimensional evaluation framework for codon optimization via AlphaFold2-derived metrics](https://openreview.net/forum?id=5ZPzR0D1Br)**
  - **ICML 2025** · OpenReview · `2026-09-16`
  - Codon optimization is the cornerstone of heterologous protein expression, but current metrics, such as the Codon Adaptation Index (CAI), only focus on translation elongation rates and ignore the complex coupling between translation dynamics and co-translational folding. Therefore…

- **[FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors](https://openreview.net/forum?id=RKKGxm7O4L)**
  - **ICML 2025** · OpenReview · `2026-09-16`
  - As AI agents are becoming widely adopted in the financial services industry, careful measurement is essential to understand where they can be reliably deployed and where oversight and professional review remain necessary. Such measurement, however, is constrained by limited acces…

- **[Turbo Harness: Instance-Adaptive Harness Optimization](https://openreview.net/forum?id=Iyc8G0eNib)**
  - **ICML 2025** · OpenReview · `2026-09-13`
  - Designing effective harnesses with minimal human intervention is an important challenge for building modern agents. Existing automated harness optimization methods typically produce a single global harness that is applied uniformly across future problem instances. However, a harn…

- **[FrontierSpatial: Holistic Evaluation of Spatial Reasoning in Large Multimodal Models](https://openreview.net/forum?id=Aoghe69Xw0)**
  - **ICML 2025** · OpenReview · `2026-09-04`
  - Spatial reasoning is foundational to intelligent systems, yet its evaluation in multimodal large language models (MLLMs) remains fragmented across narrow benchmarks that test isolated skills. We introduce ***FrontierSpatial***, a unified benchmark and evaluation framework for lar…

- **[Answers Without the Model: Harness Failures and a Zero-Cost Noise Floor for Small-Scale LLM Evaluation](https://openreview.net/forum?id=MXxiEnXvTw)**
  - *{'username': '~Satoshi_Akiyama1', 'fullname': 'Satoshi Akiyama', 'institutions': [{'name': 'Independent', 'domain': 'independent-researcher.org', 'country': 'JP'}]}*
  - **ICML 2025** · OpenReview · `2026-09-02`
  - When an LLM evaluation harness is written by the same person who reads its output, its defects arrive disguised as findings. In one such programme (20 waves, 79,021 rows, one consumer GPU), three defects produced apparent findings: distractors reconstructed the answer, an answer…

- **[CHART: A Harness-Rotation Curriculum for Harness-Robust Search Agents](https://openreview.net/forum?id=HdwZqmT4Ld)**
  - *{'username': '~Xinlu_Zhang1', 'fullname': 'Xinlu Zhang', 'institutions': [{'name': 'Amazon', 'domain': 'amazon.com', 'country': 'US'}]}, {'username': '~Ying-Chun_Lin2', 'fullname': 'Ying-Chun Lin', 'institutions': [{'name': 'Amazon', 'domain': 'amazon.com', 'country': 'US'}]}, {'username': '~Zhihan_Zhang2', 'fullname': 'Zhihan Zhang', 'institutions': [{'name': 'Amazon', 'domain': 'amazon.com', 'country': 'US'}]} et al.*
  - **ICML 2025** · OpenReview · `2026-08-28`
  - Search agents are usually trained under a single harness. But once an agent is deployed in a real application, its harness is frequently updated (e.g., a rewritten system prompt) to fit production needs. This exposes a fragility of post-trained agents: because a learned behavior…

- **[Harness Engineering for LLM Agents: A Survey of Harness Component Taxonomy, Evaluation, and Model--Harness Coevolution](https://openreview.net/forum?id=1VJLY0hAFT)**
  - **ICML 2025** · OpenReview · `2026-07-03`
  - As large language model-driven autonomous agents are increasingly deployed in real-world long-horizon, open-environment tasks, foundation models expose systematic capability gaps in context retention, reliable tool invocation, persistent state management, and multi-step execution…

- **[The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation](https://openreview.net/forum?id=1sqKRqsaE9)**
  - *Naman Vats, Oleg Aleksandrovich Golev*
  - **ICML 2025** · OpenReview · `2026-06-10`
  - Public leaderboards for coding agents typically rank systems by model name and pass rate, while the surrounding harness—the scaffold that issues tools, manages context, and decides when to stop—is often under-specified. Model-to-model comparison is valid when the harness is fixed…

- **[Clustering-based Prompt Optimization for LLM Evaluation](https://openreview.net/forum?id=vLGZhWJW3i)**
  - *Jinyoung Kim, Sun Kim, Inho Kang*
  - **ICML 2025** · OpenReview · `2026-06-10`
  - LLM evaluators (``AI judges'') increasingly stand in for human raters in search-quality pipelines, but their agreement with humans is fragile to how the scoring rubric is worded. We study how to optimize that rubric under a fixed budget of expert labels and evaluation calls, comp…

- **[FairCoder: Probing LLM Bias in High-Stakes Decision Making via Coding Tasks](https://openreview.net/forum?id=n7Mk11IVX8)**
  - *Yongkang Du, Jen-tse Huang, Jieyu Zhao et al.*
  - **ICML 2025** · OpenReview · `2026-06-03`
  - Large language models (LLMs) are increasingly used in high-stakes decisions such as hiring and college admissions, making their social bias a critical concern. While LLMs are trained to refuse explicitly biased requests, bias can be leaked implicitly during LLM planning and reaso…

- **[Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety](https://openreview.net/forum?id=7UXZAFMvpZ)**
  - *Lifei Liu, Haoran Yu, Xiaochong Jiang et al.*
  - **ICML 2025** · OpenReview · `2026-05-26`
  - Safety evaluations of multi-agent LLM systems often compare a direct prompt against a planner-executor pipeline and report the difference as a single "pipeline effect." This aggregate hides
  several simultaneous changes: harmful intent may be recast as plausible operational work…

- **[Toward Trustworthy LLM–GNN Fusion: A Fusion-Aware Evaluation and Reporting Framework](https://openreview.net/forum?id=urfkW0BNuO)**
  - *Zhifei Hu, Alexandra I. Cristea*
  - **ICML 2025** · OpenReview · `2026-05-02`
  - Hybrid LLM–GNN systems are often evaluated primarily through task accuracy, which can obscure whether improvements arise from genuine
cross-modal interaction or from a dominant single modality. We propose a fusion-aware evaluation framework that attributes gains relative to
unimo…

- **[Towards Direct Evaluation of Harness Optimizers via Priority Ranking](https://arxiv.org/abs/2605.22505)**
  - *{'fullname': 'Kai Tzu-iunn Ong', 'username': ''}, {'fullname': 'Minseok Kang', 'username': ''}, {'fullname': 'Dongwook Choi', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2026-05-01`
  - Harness optimization enables automated agent creation by having an optimizer agent iteratively update the harness of target agents. Despite its success, current studies evaluate optimizers solely by observing target agents' performance gains. This indirect end-improvement evaluat…

- **[vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models](https://openreview.net/forum?id=IpKQsHWaYS)**
  - *Suhwan Choi, Yunsung Lee, Yu Been Park et al.*
  - **ICML 2025** · OpenReview · `2026-04-13`
  - Vision-Language-Action (VLA) models are increasingly evaluated across multiple simulation benchmarks, yet adding each benchmark to an evaluation pipeline requires resolving incompatible dependencies, matching underspecified evaluation protocols, and reverse-engineering undocument…

- **[From Guidelines to Guarantees: A Graph-Based Evaluation Harness for Domain-Specific Evaluation of LLMs](https://openreview.net/forum?id=9Y10aBDIlj)**
  - *Jessica M. Lundin, Usman Nasir Nakakana, Guillaume Chabot-Couture*
  - **ICML 2025** · OpenReview · `2026-03-20`
  - Rigorous evaluation of domain-specific language models requires benchmarks that are comprehensive, contamination-resistant, and maintainable. Static, manually curated datasets do not satisfy these properties. We present a graph-based evaluation harness that transforms structured…

- **[The Tool Illusion: Rethinking Tool Use in Web Agents](https://openreview.net/forum?id=gQwin40zgt)**
  - *Renze Lou, Baolin Peng, Wenlin Yao et al.*
  - **ICML 2025** · OpenReview · `2026-03-14`
  - As web agents rapidly evolve, an increasing body of work has moved beyond conventional atomic browser interactions and explored tool use as a higher-level action paradigm. Although prior studies have shown the promise of tools, their conclusions are often drawn from limited exper…

- **[Locomo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents](https://openreview.net/forum?id=QGJrLaES6h)**
  - *{'fullname': 'Yifei Li', 'username': ''}, {'fullname': 'Weidong Guo', 'username': ''}, {'fullname': 'Lingling Zhang', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2026-01-01`
  - Long-term conversational memory is a core capability for LLM-baseddialogue systems, yet existing benchmarks and evaluation protocolsprimarily focus on surface-level factual recall.In realistic interactions, appropriate responses often depend onimplicit constraints such as user st…

- **[Conversational Agents: A Framework for Evaluation (CAFE) (Dagstuhl Perspectives Workshop 24352)](https://openreview.net/forum?id=rpLDo1d8oU)**
  - *{'fullname': 'Christine Bauer', 'username': '~Christine_Bauer1'}, {'fullname': 'Li Chen'}, {'fullname': 'Nicola Ferro'} et al.*
  - **ICML 2025** · OpenReview · `2025-12-19`
  - During the workshop, we deeply discussed what CONversational Information ACcess (CONIAC) is and its unique features, proposing a world model abstracting it, and defined the Conversational Agents Framework for Evaluation (CAFE) for the evaluation of CONIAC systems, consisting of s…

- **[Evaluate on lm-evaluation-harness](https://openreview.net/forum?id=DBgYQiFOjb)**
  - **ICML 2025** · OpenReview · `2025-11-29`

- **[Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://arxiv.org/abs/2510.01232)**
  - *Dongjun Kim, Gyuho Shim, Yongchan Chun et al.*
  - **ICML 2025** · OpenReview · `2025-10-01`
  - Large Language Models are commonly judged by their scores on standard benchmarks, yet such scores often overstate real capability since they mask the mix of skills a task actually demands. For example, ARC is assumed to test reasoning, while HellaSwag is designed to evaluate comm…

- **[FinTSBridge: A New Evaluation Suite for Real-world Financial Prediction with Advanced Time Series Models](https://openreview.net/forum?id=b3xZoZcW1J)**
  - *Yanlong Wang, Jian Xu, Tiantian Gao et al.*
  - **ICML 2025** · OpenReview · `2025-09-25`
  - Despite the growing attention to time series forecasting in recent years, many studies have proposed various solutions to address the challenges encountered in time series prediction, aiming to improve forecasting performance. However, the strategic interactions inherent in finan…

- **[AU-Harness: An Open-Source Toolkit for Holistic Evaluation of AudioLLMs](https://openreview.net/forum?id=3eoCXVxvbZ)**
  - *Hoang H Nguyen, Sidharth Surapaneni, Akshay Kalkunte Suresh et al.*
  - **ICML 2025** · OpenReview · `2025-09-17`
  - Large Audio Language Models (LALMs) are rapidly advancing, but evaluating them remains challenging due to inefficient toolkits that limit fair comparison and systematic assessment. Current frameworks suffer from three critical issues: slow processing that bottlenecks large-scale…

- **[CTBench: Cryptocurrency Time Series Generation Benchmark](https://openreview.net/forum?id=RzT2sombPD)**
  - *Yihao Ang, Qiang Wang, Qiang Huang et al.*
  - **ICML 2025** · OpenReview · `2025-09-17`
  - Synthetic time series are vital for data augmentation, stress testing, and prototyping in quantitative finance. Yet in cryptocurrency markets, characterized by 24/7 trading, extreme volatility, and rapid regime shifts, existing Time Series Generation (TSG) methods and benchmarks…

- **[Formal Methods-based Evaluation of LLM Systematic Generalization](https://openreview.net/forum?id=gIvtkwqyub)**
  - *Gao Tianxi, Cai Yufan, Zhe Hou et al.*
  - **ICML 2025** · OpenReview · `2025-09-15`
  - Recent advances in large language models(LLMs) have demonstrated impressive performance on a wide range of mathematic benchmarks.
Yet a critical challenge remains: systematic generalization, which is the ability to correctly reason about novel combinations and unseen contexts.
We…

- **[Prompt Genotyping: Quantifying the Evaluation Gap Between Synthetic Benchmarks and Real LLM Performance](https://openreview.net/forum?id=WCNAcIKREG)**
  - *Sohum Mehta, Saaketh Bhojanam*
  - **ICML 2025** · OpenReview · `2025-09-05`
  - LLM evaluation relies heavily on synthetic benchmarks, but how well do these predict real-world performance? We introduce Prompt Genotyping, a framework treating prompts as measurable ''genomes'' of 14 linguistic features to predict LLM ''phenotypes'' (performance outcomes). Usin…

- **[The Social Laboratory: A Psychometric Framework for Multi-Agent LLM Evaluation](https://openreview.net/forum?id=5Larp1U1Mq)**
  - *Zarreen Reza*
  - **ICML 2025** · OpenReview · `2025-09-05`
  - As Large Language Models (LLMs) transition from static tools to autonomous agents, traditional evaluation benchmarks that measure performance on downstream tasks are becoming insufficient. These methods fail to capture the emergent social and cognitive dynamics that arise when ag…

- **[RADAR: Mechanistic Pathways for Detecting Data Contamination in LLM Evaluation](https://openreview.net/forum?id=d0di5jC9kb)**
  - *Ashish Kattamuri, Harshwardhan Fartale, Arpita Vats et al.*
  - **ICML 2025** · OpenReview · `2025-09-05`
  - Data contamination poses a significant challenge to reliable LLM evaluation, where models may achieve high performance by memorizing training data rather than demonstrating genuine reasoning capabilities. We introduce RADAR (Recall vs. Reasoning Detection through Activation Repre…

- **[Improving Automated LLM Evaluation by Introducing Personas in LLM Red-Teaming](https://openreview.net/forum?id=Q3zYGHp2hl)**
  - *Wesley Deng, Sunnie S. Y. Kim, Akshita Jha et al.*
  - **ICML 2025** · OpenReview · `2025-09-04`
  - Recent developments in AI safety and Responsible AI research have called for red-teaming methods that can effectively surface potential risks posed by LLMs. Many of these calls have emphasized how the identities and backgrounds of red-teamers can shape their red-teaming strategie…

- **[When Benchmarks Age: Temporal Misalignment through Large Language Model Factuality Evaluation](https://openreview.net/forum?id=WRMjVoJfCY)**
  - *Xunyi Jiang, Dingyi Chang, Xin Xu*
  - **ICML 2025** · OpenReview · `2025-09-04`
  - The rapid evolution of large language models (LLMs) and the real world has outpaced the static nature of widely used evaluation benchmarks, raising concerns about their reliability for evaluating LLM factuality. While substantial works continue to rely on the popular but old benc…

- **[Rethinking MCQ Benchmarks: Mandatory Reasoning Evaluation Reveals Significant Performance Drops in Large Language Models](https://openreview.net/forum?id=U0WNteGf73)**
  - *Yue Zhang, Nhan Nguyen*
  - **ICML 2025** · OpenReview · `2025-09-04`
  - Rigorous evaluation of Large Language Models (LLMs) is critical for their adoption in high-stakes applications, particularly in highly technical domains that require deep expertise and specialized training. The proliferation of LLMs from various providers further underscores the…

- **[Human-Centric Framework for Large Multimodal Models Evaluation](https://openreview.net/forum?id=Xx9t6pe1Pk)**
  - *Shaina Raza, Aravind Narayanan, Vahid Reza Khazaie et al.*
  - **ICML 2025** · OpenReview · `2025-09-04`
  - Large multimodal models (LMMs) have been widely tested on tasks like visual question answering (VQA), image captioning, and grounding, but lack rigorous evaluation for alignment with human-centered (HC) values such as fairness, ethics, and inclusivity. To address this gap, we int…

- **[Toward Community-Driven Agents for Machine Learning Engineering](https://openreview.net/forum?id=aKChEjaJpZ)**
  - *Sijie Li, Weiwei Sun, Shanda Li et al.*
  - **ICML 2025** · OpenReview · `2025-09-03`
  - Large language model-based machine learning (ML) agents have shown great promise in automating ML research.
However, existing agents typically operate in isolation on a given research problem, without engaging with the broader research community, where human researchers often gai…

- **[Who Routes the Router: Rethinking the Evaluation of LLM Routing Systems](https://openreview.net/forum?id=EEPostHMtF)**
  - *Jiayi Yuan, Yifan Lu, Rixin Liu et al.*
  - **ICML 2025** · OpenReview · `2025-09-03`
  - The growing ecosystem of Large Language Models (LLMs) with diverse capabilities and costs has motivated the need for LLM routing systems that dynamically select the most appropriate model for each query.
Evaluating these routing systems is important yet inherently challenging due…

- **[Data Centric Guard (DC-Guard) - A Framework for Trustworthy LLM Evaluation](https://openreview.net/forum?id=4mqbmnWYAm)**
  - *Vishnu Vardhan Yadoji*
  - **ICML 2025** · OpenReview · `2025-09-03`
  - In the current era, Large Language Models (LLMs) continue to achieve remarkable results yet their evaluation is increasingly undermined by data-centric challenges such as contamination, memorization and benchmark bias which threaten the reliability of reported performance. To add…

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://openreview.net/forum?id=7AetgL7eVL)**
  - *Jiaju Chen, Yuxuan Lu, Xiaojie Wang et al.*
  - **ICML 2025** · OpenReview · `2025-08-31`
  - Nearly all human work is collaborative; thus, the evaluation of real-world NLP applications often requires multiple dimensions that align with diverse human perspectives. As real human evaluator resources are often scarce and costly, the emerging “LLM-as-a-judge” paradigm sheds l…

- **[From Many Voices to One: Statistically Principled Aggregation of LLM Judges](https://openreview.net/forum?id=XdcofpTCyq)**
  - *Jitian Zhao, Changho Shin, Tzu-Heng Huang et al.*
  - **ICML 2025** · OpenReview · `2025-08-29`
  - LLM-as-a-judge---often with multiple judges---is now the standard for scalable model evaluation, yet judge biases and correlations can amplify errors. We cast aggregation as inference in a latent-factor Markov random field that jointly models a latent true-quality variable, inter…

- **[RAFFLES: Reasoning-based Attribution of Faults for LLM Systems](https://openreview.net/forum?id=0oxelK4W6c)**
  - *Chenyang Zhu, Spencer Hong, Jingyu Wu et al.*
  - **ICML 2025** · OpenReview · `2025-08-29`
  - We have reached a critical roadblock in the development and enhancement of long-horizon, multi-component LLM agentic systems: it is incredibly tricky to identify where these systems breakdown and why. Evaluation capabilities that currently exist today (e.g., single pass LLM-as-a-…

- **[H-DDx: A Hierarchical Evaluation Framework for Differential Diagnosis](https://openreview.net/forum?id=gTq3VkpBvN)**
  - *Seungseop Lim, Gibaeg Kim, Hyunkyung Lee et al.*
  - **ICML 2025** · OpenReview · `2025-08-29`
  - An accurate differential diagnosis (DDx) is essential for patient care, shaping therapeutic decisions and influencing outcomes. Recently, Large Language Models (LLMs) have emerged as promising tools to support this process by generating a DDx list from patient narratives. However…

- **[MermaidSeqBench: An Evaluation Benchmark for LLM-to-Mermaid Sequence Diagram Generation](https://openreview.net/forum?id=cGXircO5gy)**
  - *Basel Shbita, Farhan Ahmed, Chad DeLuca*
  - **ICML 2025** · OpenReview · `2025-08-25`
  - Large language models (LLMs) have demonstrated excellent capabilities in generating structured diagrams from natural language descriptions. In particular, they have shown great promise in generating sequence diagrams for software engineering, typically represented in a text-based…

- **[Conversational Agents: A Framework for Evaluation (CAFE)](https://openreview.net/forum?id=s4QQ6uxQcx)**
  - *{'fullname': 'Christine Bauer', 'username': '~Christine_Bauer1'}, {'fullname': 'Li Chen'}, {'fullname': 'Nicola Ferro'} et al.*
  - **ICML 2025** · OpenReview · `2025-03-19`
  - This report documents the program and the outcomes of the Dagstuhl Perspectives Workshop 24352, "Conversational Agents: A Framework for Evaluation (CAFE)", which brought together 22 distinguished researchers and practitioners from 12 countries. In this workshop, a new framework f…

- **[Review to Copilot Evaluation Harness](https://openreview.net/forum?id=AXPuV3mrnL)**
  - **ICML 2025** · OpenReview · `2025-03-01`

- **[Benchmark Profiling: Mechanistic Diagnosis of LLM Benchmarks](https://openreview.net/forum?id=y4asE42Dmi)**
  - *{'fullname': 'Dongjun Kim', 'username': ''}, {'fullname': 'Gyuho Shim', 'username': '~Gyuho_Shim1'}, {'fullname': 'Yongchan Chun', 'username': '~Yongchan_Chun1'} et al.*
  - **ICML 2025** · OpenReview · `2025-01-01`
  - Large Language Models are commonly judged by their scores on standard benchmarks, yet such scores often overstate real capability since they mask the mix of skills a task actually demands. For example, ARC is assumed to test reasoning, while HellaSwag is designed to evaluate comm…

- **[Evaluation framework for copyright takedowns](https://openreview.net/forum?id=Esv8SwwkjG)**
  - **ICML 2025** · OpenReview · `2024-07-25`

- **[eva: Evaluation framework for pathology foundation models](https://openreview.net/forum?id=FNBQOPj18N)**
  - *kaiko.ai, Ioannis Gatopoulos, Nicolas Känzig et al.*
  - **ICML 2025** · OpenReview · `2024-04-05`
  - In computational pathology, self-supervised learning trained models surpass supervised ones in scale and performance. However, the benchmarking of these models remains a challenge due to the diversity in tasks and evaluation methods. To address this, we introduce eva (available a…

- **[ChEF: A Comprehensive Evaluation Framework for Standardized Assessment of Multimodal Large Language Models](https://openreview.net/forum?id=ClqyY6Bvb7)**
  - *Zhelun Shi, Zhipin Wang, Hongxing Fan et al.*
  - **ICML 2025** · OpenReview · `2023-09-15`
  - Multimodal Large Language Models (MLLMs) have shown impressive abilities in interacting with visual content with myriad potential downstream tasks. However, even though a list of benchmarks has been proposed, the capabilities and limitations of MLLMs are still not comprehensively…

- **[PEAS: A Performance Evaluation Framework for Auto-Scaling Strategies in Cloud Applications](https://openreview.net/forum?id=mmjxzINQgA)**
  - *Alessandro Vittorio Papadopoulos, Ahmed Ali-Eldin, Karl-Erik Årzén et al.*
  - **ICML 2025** · OpenReview · `2016-01-01`
  - Numerous auto-scaling strategies have been proposed in the past few years for improving various Quality of Service (QoS) indicators of cloud applications, for example, response time and throughput, by adapting the amount of resources assigned to the application to meet the worklo…


### ACL

- **[Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification Agents](https://arxiv.org/abs/2610.29812v1)**
  - *Mohammed Saqlain*
  - **ACL** · `2026-10-21`
  - Literature-searching language agents are becoming a standard component of scientific assistants for the life sciences, yet there is little controlled evidence on which parts of their harness matter. We run a controlled ablation on biomedical claim verification (SciFact) with the…

- **[What Do RTL Repair Benchmarks Actually Measure?](https://arxiv.org/abs/2610.28595v1)**
  - *Yeyin Eva Zhu, Rishabh Ranawat*
  - **ACL** · `2026-10-20`
  - RTL repair benchmarks should measure whether a model can fix broken RTL given a specification. To this end, we construct and hash-bind RTLRepairDataset, 5,784 (broken, fixed) training pairs; RTLRepairBench, 459 held-out cases with 374 syntactic and 85 behavioral mutations; and an…

- **[Semantic-Eval : A Semantic Comprehension Evaluation Framework for Large Language Models Generation without Training](https://aclanthology.org/2025.acl-long.477.pdf)**
  - *Shusheng Li, Jiale Li, Yifei Qu et al.*
  - **ACL 2025**
  - With the increasing prominence of large language models (LLMs), evaluating their text-generation capabilities has become an essential research challenge. Although LLM-based evaluation methods exhibit robust performance, the inherent stochastic nature of the LLM generation process…


### EMNLP

- **[Tau-Eval: A Unified Evaluation Framework for Useful and Private Text Anonymization](https://arxiv.org/abs/2506.05979)**
  - *Gabriel Loiseau, Damien Sileo, Damien Riquet et al.*
  - **EMNLP 2025** · `2025-06-06`
  - Text anonymization is the process of removing or obfuscating information from textual data to protect the privacy of individuals. This process inherently involves a complex trade-off between privacy protection and information preservation, where stringent anonymization methods ca…

- **[MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language](https://arxiv.org/abs/2505.14395)**
  - *Seyoung Song, Seogyeong Jeong, Eunsu Kim et al.*
  - **EMNLP 2025** · `2025-05-20`
  - Evaluating text generation capabilities of large language models (LLMs) is challenging, particularly for low-resource languages where methods for direct assessment are scarce. We propose MUG-Eval, a novel framework that evaluates LLMs'multilingual generation capabilities by trans…


### Other / arXiv

- **[Harness Scaling for Generalizable Agentic Reinforcement Learning](https://arxiv.org/abs/2610.29458)**
  - *Fei Bai, Huatong Song, Chuan Hao et al.*
  - 🤗 Featured · `2026-10-21`
  - Agent harnesses have become a central component of modern agentic systems, shaping how models use tools, manage context, and coordinate long-horizon interaction. Realizing the benefits of these harnesses depends on how effectively the underlying model can make use of them, motiva…

- **[From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](https://arxiv.org/abs/2610.29560)**
  - *Tingwen Du, Haoyu Guo, Hanxue Zhang et al.*
  - 🤗 Featured · `2026-10-21`

- **[Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113)**
  - *Houde Qian, Zheng Jiang, Wenyi Li et al.*
  - 🤗 · `2026-10-21`
  - Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether lar…

- **[Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents](https://arxiv.org/abs/2610.28934)**
  - *Xu Li, Simon Yu, Minzhou Pan et al.*
  - 🤗 · `2026-10-20`
  - Coding agents now complete tasks autonomously, modifying real-world state such as artifacts, software environments, and configurations along the way. Yet they show limited backup awareness: recognizing that an action will modify state that may later be needed, and preserving it b…

- **[Evolving Agent Interfaces](https://arxiv.org/abs/2610.28601)**
  - *Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega et al.*
  - 🤗 · `2026-10-20`
  - Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through a shell to find one function. Both the interfaces and the knowledge of when to u…

- **[The End of Consensus Research?](https://arxiv.org/abs/2610.30114v1)**
  - *Clément Burgelin, Rachid Guerraoui, Zicong Hong et al.*
  - `2026-10-21`
  - Consensus is a fundamental problem in distributed computing and at the core of state machine replication (SMR). Despite decades of active human research, discovering practical low-latency solutions to the problem is still open, as it requires combining protocol knowledge, correct…

- **[SWE-DIVE: Multi-Turn Coding Agent Evaluation with Dynamic User Simulation](https://arxiv.org/abs/2610.30047v1)**
  - *Lorenz Brehme, Benjamin Steenhoek, Ruth Breu*
  - `2026-10-21`
  - Coding agents are typically evaluated using one-shot, well-formulated prompts. Benchmarks such as SWE-bench use existing GitHub issues as input for a coding agent and evaluate whether the agent successfully solves the task. However, in real-world use cases, prompts are often not…

- **[HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning](https://arxiv.org/abs/2610.30042v1)**
  - *Sudipta Paul, Pengrui Quan, Aounon Kumar et al.*
  - `2026-10-21`
  - Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs. Leading approaches such as the Darwin--Godel Machine and the Huxley--Godel Machine (HGM) rely on recursive self…

- **[Agent Behavior Maps: Locating Agents by What They Would Do, Without Running Them](https://arxiv.org/abs/2610.30014v1)**
  - *Shota Fujikawa, Takuya Tamura, Kosuke Akimoto et al.*
  - `2026-10-21`
  - LLM agents with similar success rates can follow different action sequences. An Agent Behavior Map represents LLM-harness combinations using centered action log-likelihoods on shared reference trajectories, without requiring new environment rollouts from the target agent. We deri…

- **[PAUSE: Search-Free Steering of Coding Agents Before Their First Source-Code Edit](https://arxiv.org/abs/2610.29870v1)**
  - *Viral Patel, Boyin Tan, Jason Xue et al.*
  - `2026-10-21`
  - Coding agents can invest substantial effort in repository exploration and testing yet still produce unsuccessful patches. Existing online steering methods review trajectories periodically or invoke an advisor when a monitor detects behavioral problems; frequent reviews are costly…

- **[Beyond Small Talk: Modeling Disclosure Trajectories in Human-AI Conversation](https://arxiv.org/abs/2610.29413v1)**
  - *Keith Kwok, Wanting Ning, Tej Deep Pala et al.*
  - `2026-10-21`
  - Recently, we see a rise in conversational agents as a form of social and emotional support, where disclosure will unfold over time. Yet, current evaluations of these agents typically examine isolated conversational states. In analyses of naturally occurring conversations, disclos…

- **[From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?](https://arxiv.org/abs/2610.29331v1)**
  - *Linus Filbry, Luckeciano C. Melo, Yarin Gal*
  - `2026-10-21`
  - Large language models (LLMs) are increasingly applied across the scientific discovery pipeline, from synthesizing literature to generating hypotheses to informing experimental design. A unifying principle behind these tasks is the need to continuously update beliefs as evidence a…

- **[From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](https://arxiv.org/abs/2610.30051v1)**
  - *May Espinola, Qifan Zhang, Yu Xiang*
  - `2026-10-21`
  - Recent advances in frontier AI models have demonstrated remarkable capabilities in visual understanding, reasoning, planning, and tool use, raising the possibility of using general-purpose AI models for robot manipulation without task-specific training. However, their manipulatio…

- **[Beyond Binary Labels: Diagnostic Evaluation of LLM Safety with Prompt-Level Rubrics](https://arxiv.org/abs/2610.29225v1)**
  - *Hongyu Li, Xinlong Huang, Zhan Yu et al.*
  - `2026-10-21`
  - Current LLM safety benchmarks predominantly rely on binary safe or unsafe labels, lacking explanatory depth and suffering from low consistency across automated judges. To address this, we introduce DiagSafe, a diagnostic evaluation framework that moves beyond binary classificatio…

- **[Context-Augmented, Session-Calibrated Blood Pressure Tracking from Photoplethysmography](https://arxiv.org/abs/2610.29091v1)**
  - *Farouk Ganiyu Adewumi, Timothy Oladunni*
  - `2026-10-21`
  - Objective.To distinguish the contributions of acquisition context and photoplethysmography (PPG) to session-calibrated blood pressure (BP) tracking.Approach. The original comparison used three repeats of five-fold participant-level cross-validation in 653 AuroraBP participants, e…

- **[BrainCodes: A Lightweight EEG Foundation Model over Discrete Neural Codes](https://arxiv.org/abs/2610.29320v1)**
  - *Kleanthis Avramidis, Ivan Tashev, Dimitra Emmanouilidou*
  - `2026-10-21`
  - Recent electroencephalography (EEG) foundation models increasingly emphasize model scale, potentially limiting their deployment on resource-constrained devices and in everyday environments. We argue that transferable EEG features can instead be learned with a compact architecture…

- **[A Unified Evaluation Framework of Physical Adversarial Robustness in the Edge VLM Era](https://arxiv.org/abs/2610.29196v1)**
  - *Eric Liang, Alan Luo, Kaiwen Yuan*
  - `2026-10-21`
  - Recent advancements in Vision-Language Models (VLMs) enable end-to-end visual grounding via language prompts and generative decoding, demonstrating largely improved zero-shot and open-vocabulary detection capabilities. As a result, VLMs are rapidly being deployed at the edge in s…

- **[Task-Preserving Multilingual Instruction Tuning for Open-Ended QA in WMT 2026 MIST](https://arxiv.org/abs/2610.29926v1)**
  - *Aleix Sant, Jordi Luque, Carlos Escolano*
  - `2026-10-21`
  - This paper describes our submission to the WMT 2026 Multilingual Instruction Shared Task. We adapt Qwen3-8B with LoRA using organiser-provided data, EuroAlpaca, a multilingual instruction dataset created through task-preserving localisation, and CrossEuroAlpaca, a cross-lingual a…

- **[Huayu-Global: Skillful real-time quasi-global precipitation retrieval](https://arxiv.org/abs/2610.29213v1)**
  - *Zijiang Song, Shuang Yang, Yuying Li et al.*
  - `2026-10-21`
  - Satellite precipitation products face a persistent trade-off: real-time estimates are timely but less accurate, whereas the most reliable products are often released months after observation. This delay keeps high-quality precipitation information outside the decision window for…

- **[Behavior Beyond Text: Evaluating Refusal Transfer Failure in LLM Agents](https://arxiv.org/abs/2610.28982v1)**
  - *Ekagra Gupta, Raj Saha, Aniekan-Abasi Inyang et al.*
  - `2026-10-20`
  - While large language models are increasingly deployed as tool-calling agents, their safety evaluations still focus primarily on their ability to refuse harmful requests in text. We investigate whether the refusal behavior in text transfers to tool use. We construct a benchmark of…

- **[SANE: Automated Scorer-Specific Metamorphic Testing for LLM Judges](https://arxiv.org/abs/2610.28886v1)**
  - *Ethan Ludwick, Yu-Chung Hsiao*
  - `2026-10-20`
  - LLM judges increasingly mediate benchmark evaluation, model selection, data curation, and training. Their decisions are useful only when each judge responds reliably to changes affecting its scoring criterion. Existing methods for reliability testing perturb inputs with known exp…

- **[Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing](https://arxiv.org/abs/2610.28815v1)**
  - *Jingzhe Liu, Jiliang Tang, Tong Zhao et al.*
  - `2026-10-20`
  - Agentic harness evolution optimizes an agent's instructions, tools, and control flow by using its task execution experiences as evolving evidence. While more evolution tasks should intuitively improve performance, our preliminary study reveals a paradoxical failure mode: the perf…

- **[Rewards for Budget-Aware Multi-Turn Agents That Adapt to Arbitrary Test-Time Constraints](https://arxiv.org/abs/2610.28409v1)**
  - *Tom A. Lamb, Adam Golinski, Eleonora Gualdoni et al.*
  - `2026-10-20`
  - Large language model agents are often given an inference budget and asked to maximise success within it. A multi-turn agent has to allocate this budget across many environment interactions. An external harness can enforce the budget, but it remains unclear whether the agent itsel…

- **[FALCA: Falsification-Aware Reinforcement Learning with Hierarchical Credit Assignment for Long-Horizon Deep Search Agents](https://arxiv.org/abs/2610.28361v1)**
  - *Zijun Dou, Kun Luo, Chaofan Li et al.*
  - `2026-10-20`
  - Long-horizon deep search requires LLM agents to iteratively decompose complex information needs, gather evidence from external sources, and maintain a reliable research state under multiple constraints. A central challenge is that early mistakes can be amplified over the search t…

- **[S-Agent 2.0: Spatial Reasoning with a General Coding Agent](https://arxiv.org/abs/2610.28354v1)**
  - *Rui Gong, Ruoyu Wang, Yalun Dai et al.*
  - `2026-10-20`
  - Spatial reasoning asks a model to work out where objects are in 3D space, how they relate to one another, and how they move. Agentic VLMs have recently brought large improvements on such tasks by letting the model actively gather evidence with 3D perception tools instead of answe…

- **[ChartEvo: Self-Evolving Agent Harnesses for Long-Tail Chart Reasoning](https://arxiv.org/abs/2610.28282v1)**
  - *Qi Wang, Peijie Wang, Jun Cao et al.*
  - `2026-10-20`
  - Multimodal large language models (MLLMs) have substantially advanced chart understanding and reasoning, yet their performance remains highly uneven across chart types. While modern MLLMs perform well on common charts, their accuracy drops sharply on long-tail charts with diverse…

- **[MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2610.28201v1)**
  - *Yu Cui, Hong He, Ruiqing Yue et al.*
  - `2026-10-20`
  - Recursive self-improvement (RSI) of agent harnesses has emerged as an effective approach to enhancing the capabilities of large language model (LLM) agents. By searching the harness space for a specific LLM on a given dataset, RSI can discover a harness tailored to the capabiliti…

- **[ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents](https://arxiv.org/abs/2610.28093v1)**
  - *Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique et al.*
  - `2026-10-20`
  - AI agents keep long-term memory, much of which comes from web pages and tool results. Agent harnesses, the software that runs the model, do not record who may act on this memory, so an instruction hidden in a fetched page can be treated as the user's own instruction. We propose C…

- **[Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](https://arxiv.org/abs/2610.27954v1)**
  - *Byeonghun Bang, Sangwoo Park, Jinheon Baek et al.*
  - `2026-10-20`
  - Recent advances in large (vision) language models have enabled computer-use agents that automate digital workflows via fine-grained keyboard and mouse operations. However, such agents remain fragile in long-horizon settings, where errors accumulate and executed actions leave unin…

- **[Give the Model a Finger: Developmentally Aligned Evaluation of Counting in Vision-Language Models](https://arxiv.org/abs/2610.27756v1)**
  - *Yingxin Jia, Hui Geng, Wenxin Yang et al.*
  - `2026-10-20`
  - Vision-language models (VLMs) are exact on small sets and drift into estimation on larger ones, a profile reminiscent of children before they master counting. Children cross the barrier with epistemic actions: pointing at each item while reciting number words, moving counted item…

- **[Hearsay or Fact? How Framing and Elicitation Shape LLM Probability Updates](https://arxiv.org/abs/2610.27745v1)**
  - *An-Sheng Jhang*
  - `2026-10-20`
  - Large language models (LLMs) are increasingly used as judgment assistants and as stand-in participants in psychology experiments, yet little is known about how much their probability estimates move in response to a single new piece of information. We pair premise-hypothesis items…

- **[Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](https://arxiv.org/abs/2610.27548v2)**
  - *Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang et al.*
  - `2026-10-20`
  - When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing c…

- **[Harness Self-Evolution for Long-Horizon Terminal Agents](https://arxiv.org/abs/2610.27435v1)**
  - *Ruhan Wang, Yucheng Shi, Zongxia Li et al.*
  - `2026-10-20`
  - Long-horizon terminal agents may solve a task in one run yet fail across repeated runs. Stochastic errors can propagate through actions and context, creating a gap between capability and reliable execution. We present RiseHarness, a framework for iteratively improving agent harne…

- **[KPHarness: Co-Evolving Knowledge and Probing for Long-Horizon Gaming Harnesses](https://arxiv.org/abs/2610.27417v1)**
  - *Zhikang Chen, Yueqing Sun, Sen Cui et al.*
  - `2026-10-20`
  - A failed gaming trajectory reveals that an agent needs intervention, but not necessarily how its execution harness should change. Effective harness adaptation therefore requires gathering diagnostic evidence, rather than merely proposing alternative recovery rules. We present KPH…

- **[An Explicit Feedback Contract for Iterative ML-Agent Harnesses](https://arxiv.org/abs/2610.28798v1)**
  - *Kehui Yao, Chuanbo Hu, Jiao Chen et al.*
  - `2026-10-20`
  - Iterative ML agents develop models by editing code, running experiments, reading a validation score, and choosing what to try next. In current harnesses this loop is served by an exact validation score returned after every attempt, which leaves the validation split open to adapti…

- **[Measure First, Then Allocate: Calibrated Rollout Budgets for MCP Agents in Reinforcement Learning](https://arxiv.org/abs/2610.28785v1)**
  - *Hieu Tran, Zonghai Yao, Sunjae Kwon et al.*
  - `2026-10-20`
  - Training tool-using language models requires costly interaction, yet identical rewards within a rollout group provide no group-relative learning signal. We use reward disagreement to guide harness evaluation and the allocation of rollouts for policy training in Model Context Prot…

- **[RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards](https://arxiv.org/abs/2610.28010v1)**
  - *Artem Mikhaylov, Pavel Konoplev, Nikolay Efanov et al.*
  - `2026-10-20`
  - The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provide strong semantic understanding and reasoning capabilities,…

- **[Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization](https://arxiv.org/abs/2610.27889v1)**
  - *Younghyun Kim, Wooseok Seo, Minseo Kim et al.*
  - `2026-10-20`
  - Recent studies in harness optimization have shown substantial performance gains in language model agents without updating model weights. A well-designed harness more effectively leverages the underlying model's capabilities by shaping context, tool use, and execution workflows. H…

- **[Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented Design](https://arxiv.org/abs/2610.28380v1)**
  - *Gaotang Li, Bhavana Dalvi Mishra, Yifei Ming et al.*
  - `2026-10-20`
  - Agent harnesses are executable code that specifies the prompts, tools, and control flow around a language model. A single global harness can struggle with heterogeneous tasks that require different execution strategies. In this work, we introduce Object-Oriented Harness (OO-Harne…

- **[SciDiagBench: A Type-Specific Benchmark for Human-Aligned Evaluation of Scientific Diagrams](https://arxiv.org/abs/2610.27841v1)**
  - *Hao Wang, Zixuan Li, Long Bai et al.*
  - `2026-10-20`
  - Recent agents have demonstrated strong capabilities in generating images from textual prompts, motivating their utilization for scientific diagram generation. Scientific diagrams naturally span diverse types, each characterized by distinct visual structures and content organizati…

- **[WorldSR: Harnessing World Knowledge Search for Grounded Image Super-Resolution](https://arxiv.org/abs/2610.28423v1)**
  - *Junyuan Deng, Xinyi Wu, Zhenyao Wu et al.*
  - `2026-10-20`
  - Generative-prior-based super-resolution (SR) methods leverage implicit knowledge learned from large-scale models to enhance low-resolution inputs. However, such priors are inherently stochastic and optimized for diverse generation, conflicting with the deterministic, high-fidelit…

- **[Context-Aware Prompt Injection Detection via Small Language Models in RAG Pipelines: nokast-secureRAG](https://arxiv.org/abs/2610.28364v1)**
  - *Abhishek Rai*
  - `2026-10-20`
  - Local Retrieval-Augmented Generation (RAG) systems are vulnerable to indirect prompt injection and retrieval poisoning, where malicious instructions in retrieved content are mistaken for trusted input. We present nokast-secureRAG, a roughly 0.5B-parameter small language model tha…

- **[World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation](https://arxiv.org/abs/2610.27725v1)**
  - *Jiushu Li, Haoran Wang, Yumeng Liu et al.*
  - `2026-10-20`
  - Long-horizon human-object-scene interaction (HOSI) is central to embodied AI, animation, and game development. Existing human-object interaction (HOI) and human-scene interaction (HSI) models excel in their respective domains, but none alone covers tasks requiring multiple intera…

- **[SkillEval: Learning Interpretable Ability Profiles of LLMs via Cognitive Diagnosis Models](https://arxiv.org/abs/2610.28767v1)**
  - *Berke Arda, Peng Cui, Qiaoyuan Zheng et al.*
  - `2026-10-20`
  - Current evaluation of LLMs on benchmarks typically aggregates performance over individual examples into a single scalar score. This approach is overly coarse and ignores the diverse scope of skills covered by benchmark datasets. To address this limitation and better exploit bench…

- **[Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V](https://arxiv.org/abs/2610.28416v1)**
  - *Zhenghan Chen, Zekai Shao, Xin Lin et al.*
  - `2026-10-20`
  - Code-based video generation offers fine-grained control, targeted editing, and component reuse compared with direct video generation. This approach requires multimodal large language models (MLLMs) to translate visual and temporal requirements into executable programs that produc…

- **[ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](https://arxiv.org/abs/2610.27913v1)**
  - *Jiahui Ning, Liang Chen, Yuchen Liang et al.*
  - `2026-10-20`
  - Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions o…

- **[ABench: Adversarily Benchmarking Large Language Models across Taxonomized Values](https://arxiv.org/abs/2610.27611v1)**
  - *Liping Yang, Yongqi Leng, Jingting Zheng et al.*
  - `2026-10-20`
  - Ensuring the alignment of Large Language Models (LLMs) with diverse cultural values is critical for their safe global deployment. However, existing alignment benchmarks are predominantly English-centric or confined to simple discriminative tasks. Moreover, they often fail to effe…

- **[Tracing Recurrent and Emergent Hallucination Patterns in Decomposed Text-to-SQL Generation](https://arxiv.org/abs/2610.27720v1)**
  - *Hayden Moore, Abhinav Verma, Anshuman Dutt*
  - `2026-10-20`
  - Large language models can achieve strong Text-to-SQL benchmark performance while still producing schema and query-logic errors. Most evaluations characterize such failures only in the final generated query, making it difficult to determine whether a related error was also observe…

- **[When LLMs Manipulate: Measuring Behavioral, Social, and Temporal Effects](https://arxiv.org/abs/2610.27573v1)**
  - *Sadia Asif, Israel Antonio Rosales Laguan, Shumaila Asif et al.*
  - `2026-10-20`
  - Large language models (LLMs) can influence user trust and decision-making through subtle linguistic cues, yet the behavioral effects of manipulative outputs remain poorly quantified. We introduce a behavioral computing framework for measuring \textit{behavioral vulnerability}, de…

- **[Don't Skip the Baseline: A Controlled Comparison of Dynamic Expert Skipping in MoEs](https://arxiv.org/abs/2610.28369v1)**
  - *Jakob Steimle, Thomas Elsken, Daniel Ehrhardt et al.*
  - `2026-10-20`
  - A growing body of work proposes dynamic expert-skipping methods for Mixture-of-Experts (MoE) models that adjust the number of experts activated per token during inference, aiming to preserve model quality while further reducing the number of active parameters. These methods have…

- **[Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops](https://arxiv.org/abs/2610.27350v1)**
  - *Arnav Grover*
  - `2026-10-19`
  - Frontier models can control robots through agent harnesses that loop on one question: what motion comes next toward the user's goal? We show that this default loop carries out harmful instructions. With GPT-6 Astra controlling a low-cost SO-101 arm through the Inspect Robots harn…

- **[AutoRedClaw: Automated Red-Teaming for Claw-Style Agents](https://arxiv.org/abs/2610.27244v1)**
  - *Hao Li, Tongyan Hu, Weidi Luo et al.*
  - `2026-10-19`
  - Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw. These claw-style agents maintain configuration files (e.g., AGENTS.md), long-term memory, and reusable skills. Once poisoned, this persistent state is repeatedly r…

- **[EGI-BENCH: An Enterprise General Intelligence Benchmark Suite](https://arxiv.org/abs/2610.27234v1)**
  - *Zhiwei Liu, Zhujun Lan, Jielin Qiu et al.*
  - `2026-10-19`
  - Enterprise adoption of LLMs in agentic workflows is gated by evaluations that span a wide arc of abilities: CRM operations, heterogeneous-document retrieval, personal data understanding, multi-turn planning, tool use, function calling, long-horizon research, and long-context soft…

- **[Understanding the Benefits of Scaffolds through Computational Separations](https://arxiv.org/abs/2610.27157v1)**
  - *Jingchu Gai, Adam Block, Andrej Risteski*
  - `2026-10-19`
  - Inference-time harnesses, i.e., external procedures that call a model many times and keep state across calls, can substantially improve model capabilities. In this paper, we investigate the benefits of using such harnesses and the extent to which these benefits can be internalize…

- **[A general-purpose System One decision model for clinical records](https://arxiv.org/abs/2610.27099v1)**
  - *Andrew Zhang, Trinh T. L. Vuong, Sophia J. Wagner et al.*
  - `2026-10-19`
  - Clinical care, health-system operations and biomedical discovery depend on extracting reliable answers from patient records, yet applying diverse clinical questions across entire populations remains computationally expensive. Here we present Clinical System One (CS1), a 4-billion…

- **[OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory](https://arxiv.org/abs/2610.26860v1)**
  - *Yu Zhou, Cheng-Fu Yang, Rui Sun et al.*
  - `2026-10-19`
  - Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base…

- **[Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy](https://arxiv.org/abs/2610.26836v1)**
  - *Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu et al.*
  - `2026-10-19`
  - LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads on demand. We ask where this costs accuracy with a real scientific tool: PHREEQC…

- **[ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry](https://arxiv.org/abs/2610.26829v1)**
  - *Matt Turk, Brandon L. Neel, Diana M. Lopez et al.*
  - `2026-10-19`
  - Frontier agents retrieve structural metadata well and compute geometry from coordinates less reliably. We ask how much of a benchmark score reflects that gap and how much reflects the evaluation configuration around the model. We study ProteinGeoBench, a suite of 131 protein-stru…

- **[ReuF2F: Benchmarking Coding Agents on Formalized Undergraduate Research Problems](https://arxiv.org/abs/2610.27046v1)**
  - *Zeyu Zheng, Yiyang Liu, Yuyang Zhao et al.*
  - `2026-10-19`
  - As AI systems begin to resolve open research problems, reliable verification becomes increasingly important. Formal mathematics provides a trusted framework for mathematical reasoning, enabling agents to produce machine-checkable proofs while conducting mathematical exploration.…

- **[Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams](https://arxiv.org/abs/2610.26781v1)**
  - *Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao et al.*
  - `2026-10-19`
  - Phone scams impose substantial and growing costs on individuals and financial systems worldwide, yet existing countermeasures impose no resource cost on perpetrators. Strategic scam-baiting, in which automated agents engage scammers to deplete their operational capacity, offers a…

- **[VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM Agents](https://arxiv.org/abs/2610.28679v1)**
  - *Jianing Yin, Ziyi Chen, Hao Wang et al.*
  - `2026-10-19`
  - Agents need reliable ways to validate their outputs, both when completing tasks and when filtering synthetic training data. We study verifier generation: from the instruction and environment available for solving a task, an agent writes an executable verifier that must accept eve…

- **[AllPath: Layered Verification for a Deployed, Self-Revising LLM Trading Agent under Human-Gated and Autonomous Regimes](https://arxiv.org/abs/2610.26662v1)**
  - *Tian Zhang, Meng Li*
  - `2026-10-19`
  - LLM trading agents are evaluated almost exclusively in backtests and autonomous benchmark harnesses. Deployment, where actions are irreversible, raises a different question: who verifies the agent's actions, and which failures can each verifier structurally catch? We report on Al…

- **[When the harness decides success: state that cannot be re-observed](https://arxiv.org/abs/2610.26632v1)**
  - *Raimondas Lencevicius*
  - `2026-10-19`
  - Agent harnesses decide what a language model sees across turns: they drop old turns, summarize them, or replay the model's own earlier reasoning. We ask when these choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registe…

- **[When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories](https://arxiv.org/abs/2610.26394v1)**
  - *Tianqi Liu, Yandong Guan, Songze Li et al.*
  - `2026-10-19`
  - Coding agents increasingly undertake development tasks in mature enterprise repositories, yet existing benchmarks offer limited insight into whether they fulfill complete Product Requirement Documents (PRDs) and where delivery breaks down. Issue resolution and development from sc…

- **[Autonomous intelligence for mining productivity: a multi-agent AI approach to operational value creation](https://arxiv.org/abs/2610.26369v1)**
  - *N Guerin, A Dehoux, M Nakhla*
  - `2026-10-19`
  - Integrated Remote Operation Centres (IROCs) are emerging as the architectural frontier of Industry 4.0 for capital-intensive sectors such as mining, oil and gas, and energy. Yet two intertwined gaps constrain their evolution towards full autonomy. First, no integrated agentic arc…

- **[VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement](https://arxiv.org/abs/2610.26342v2)**
  - *Ruotian Peng, Yuanyi Ren, Shuaiqi Liu et al.*
  - `2026-10-19`
  - Recursive self-improvement (RSI) requires agents to diagnose system bottlenecks and coordinate improvements across training and inference. We refer to the agents' capability to jointly optimize training data, the trainer, and the inference harness as cross-component co-design. We…

- **[Reliable Before Profitable: QuantHarness for Governing Financial Strategy Development with LLM Agents](https://arxiv.org/abs/2610.26101v1)**
  - *Jiasheng Mao, Jiacheng Liu, Hengwei Ye et al.*
  - `2026-10-19`
  - LLM agents can turn natural-language financial research requests into executable and backtested strategies, but a successful run may still implement the wrong rule, use information unavailable at decision time, or obscure how repairs and candidate selection changed the strategy.…

- **[CUA-Lite: An Open Platform for Computer Use Agents](https://arxiv.org/abs/2610.26071v1)**
  - *Zhanhui Zhou, Weichen Zhang, Haoran Liu et al.*
  - `2026-10-19`
  - Open resources for computer use agents (CUAs) -- environments, datasets, and models -- remain scattered: without a standard, these resources cannot be integrated and scaled; additionally, evaluation, RL, and SFT cannot share one infrastructure. We present CUA-Lite, an open platfo…

- **[AuDQ: Auditable Data Quality through Agentic Rule Discovery](https://arxiv.org/abs/2610.26031v1)**
  - *Jacopo Biggiogera, Nicolas Colombo, Krati Saxena et al.*
  - `2026-10-19`
  - High-stakes tabular pipelines rely on scattered, static quality checks that are hard to evolve and audit against policy intent. Regulated domains particularly suffer as the LLM-era automation raises expectations for traceability and accountability. We propose a vision for an onto…

- **[EvoSkill v2: Fully Agentic Skill Evolution from Benchmark Adaptation to a Stateful Evolver](https://arxiv.org/abs/2610.25931v1)**
  - *Dastin Huang, Baran Nama, Salaheddin Alzubi*
  - `2026-10-19`
  - EvoSkill v2 is a three-agent system that edits the instructions (skills) an agent is given, leaving its model and harness intact. The user starts a run by describing a benchmark and supplying a grader, which a benchmark adaptor turns into a benchmark-specific plugin. A solver att…

- **[Secure Agentic Coding through Counterexample-Grounded Feedback](https://arxiv.org/abs/2610.25916v2)**
  - *Tue Le, Anh Nguyen Hoang, Gabriel Sasseville et al.*
  - `2026-10-19`
  - As coding models and agent harnesses become more capable, reliable security verification is becoming a central bottleneck. Improving secure code generation requires a signal whose reported progress remains aligned with actual program behavior under optimization; otherwise, an opt…

- **[Are Self-Evolving Agents Continual Learners?](https://arxiv.org/abs/2610.25858v1)**
  - *Xiaoyin Chen, Yizheng Huang, Yinglun Xu et al.*
  - `2026-10-19`
  - Large language model agents are often deployed in environments where new knowledge, tools, and workflows keep arriving. Such an agent is therefore expected to adapt continually, learning new tasks as they arrive without forgetting earlier ones. This resembles the continual learni…

- **[EvalRx: Agentic Diagnosis and Verified Repair of Foundation Models](https://arxiv.org/abs/2610.25767v1)**
  - *Jiaqi Liu, Ruinan Jin, Yitong Tang et al.*
  - `2026-10-19`
  - Model evaluation reveals where models fail, but rarely why or whether a proposed fix genuinely works. We introduce EvalRx, an open-source agentic framework for statistically grounded model diagnosis and repair. EvalRx discovers systematic failure modes, explores candidate mechani…

- **[HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs](https://arxiv.org/abs/2610.26770v2)**
  - *Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen et al.*
  - `2026-10-19`
  - Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harn…

- **[Maestro: Agentic Formal Proof Development by Coordination](https://arxiv.org/abs/2610.25920v1)**
  - *Haoyu Li, Zeren Shui, Yuhao Zhang et al.*
  - `2026-10-19`
  - Lean is increasingly used to verify mathematical proofs and software produced by LLM agents, but writing formal proofs remains hard. Existing prover systems take a divide-and-conquer approach that recursively decomposes hard proof obligations into easier lemmas and splits again a…

- **[Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments](https://arxiv.org/abs/2610.25747v1)**
  - *JooKyung Yuh, Byungmin Park, Eunseo Choi et al.*
  - `2026-10-19`
  - Scientific model discovery requires proposing candidate models of an unknown system and designing experiments that discriminate among them. However, LLM-based approaches typically rely on in-context learning to predict outcomes and select experiments, lacking explicit model evalu…

- **[RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents](https://arxiv.org/abs/2610.27295v1)**
  - *Xinying Cai, Bin Hu, Mingyu Jin et al.*
  - `2026-10-19`
  - Existing steering benchmarks are built around simplified, isolated generation tasks and evaluate a single behavioral attribute under controlled settings that do not reflect the diversity and complexity of practical deployment. As a result, performance on these benchmarks provides…

- **[Can It Actually Work? Synthesizing Functional CAD Mechanisms](https://arxiv.org/abs/2610.26861v1)**
  - *Wenqian Zhang, Yangyi Huang, Zigeng Xu et al.*
  - `2026-10-19`
  - While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that sat…

- **[Optimal Multi-Kernel Combination for Online Multi-Label Classification](https://arxiv.org/abs/2610.26123v1)**
  - *Tingting Zhai, Wei Liu, Renjian Yu*
  - `2026-10-19`
  - Multi-label classification is particularly challenging in streaming scenarios, where data arrives sequentially. Online kernel methods offer a promising solution. However, prevailing methods rely on a single preselected kernel, making them prone to suboptimal choices since the glo…

- **[HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended RL](https://arxiv.org/abs/2610.26426v1)**
  - *Xiaoqiang Wang, Ting-En Lin, Yuchuan Wu et al.*
  - `2026-10-19`
  - Rubric-based reinforcement learning (RL) trains policies for open-ended generation with natural-language criteria as rewards, but these rewards can become ineffective as training progresses. We identify two failure modes. Under non-discriminative rewards, scores collapse to unifo…

- **[How to get the best and fairest performance out of your ASR system using activation steering](https://arxiv.org/abs/2610.26994v1)**
  - *Felix Herron, Alex Colagrande, Solange Rossato et al.*
  - `2026-10-19`
  - Activation steering for ASR systems is an underexplored technique in improving both ASR performance and demographic fairness. We investigate two forms of activation steering: paired activation subtraction, and supervised optimization. We find the former to be ineffective at ameli…

- **[From Outcomes to Components: A Counterfactual Evaluation Framework for LLM-Proposed Repairs](https://arxiv.org/abs/2610.26650v2)**
  - *Hengyu Ye, Songhua Hu*
  - `2026-10-19`
  - A repair action proposed by a large language model (LLM) specifies which records to change and how to change their values. A failed action may still contain a useful choice of records or a useful update, depending on how the two are paired. We introduce a counterfactual evaluatio…

- **[When to Stop Asking: Factor Coverage Bias and LLM Determinability Judgments with Underspecified Information in Medicine](https://arxiv.org/abs/2610.25819v1)**
  - *Yusuke Watanabe, Yohei Kobashi, Taisei Tosaki et al.*
  - `2026-10-19`
  - Clinical decision-making often begins with underspecified information and requires not only gathering missing information but also knowing when to stop. This calls for judging determinability (whether the available information is sufficient for a decision) by considering whether…

- **[Evaluating Tibetan Speech Recognition Across Dialects and Adaptation Regimes: A Multi-Granularity Analysis](https://arxiv.org/abs/2610.27002v1)**
  - *Jacob Moore, Sheng Li*
  - `2026-10-19`
  - Tibetan speech recognition is usually evaluated with character or syllable error rates because the writing system does not mark word boundaries. These metrics can rank systems differently and respond differently to adaptation failures. We combine character error rate, syllable er…

- **[TRACE: Training-aware Robustness and Challenge Evaluation for Text-Vision Embedding Models](https://arxiv.org/abs/2610.26993v1)**
  - *Pume Tuchinda, Tinnakit Udsa, Peerat Limkonchotiwat*
  - `2026-10-19`
  - Existing benchmarks for text-vision embedding models report aggregate scores that obscure whether performance comes from general capabilities, task-specific adaptation, or robustness to challenging tasks. We introduce TRACE, a Training-aware Robustness and Challenge Evaluation fr…

- **[ActTime: Action-Conditioned World Modeling for Time Series](https://arxiv.org/abs/2610.25764v1)**
  - *Xinxing Zhou, Xiaojie Yuan, Yanlong Wen et al.*
  - `2026-10-19`
  - Time-series models increasingly condition on known future inputs. In controlled systems, some of these inputs are actions that can be changed, compared, and optimized before execution. A model must therefore do more than predict the realized future: it must predict how outcomes c…


## Finance  (184)

### AAAI

- **[Two Heads are Better than One: Distilling Large Language Model Features Into Small Models with Feature Decomposition and Mixture](https://arxiv.org/abs/2511.07110)**
  - *Tian-Hao Fu, Xin-Xin Xu, Weichen Xu et al.*
  - **AAAI 2025** · `2025-11-10`
  - Market making (MM) through Reinforcement Learning (RL) has attracted significant attention in financial trading. With the development of Large Language Models (LLMs), more and more attempts are being made to apply LLMs to financial areas. A simple, direct application of LLM as an…

- **[TimeCAP: Learning to Contextualize, Augment, and Predict Time Series Events with Large Language Model Agents](https://arxiv.org/abs/2502.11418)**
  - *Ge-On Lee, Wen-Chao Yu, Kijung Shin et al.*
  - **AAAI 2025** · `2025-02-17`
  - Time series data is essential in various applications, including climate modeling, healthcare monitoring, and financial analytics. Understanding the contextual information associated with real-world time series data is often essential for accurate and reliable event predictions.…


### ICML

- **[ARTE: Agentic Refinement through Trade Execution for High-Frequency Trading Strategy Discovery](https://openreview.net/forum?id=VisvXioWmG)**
  - **ICML 2025** · OpenReview · `2026-10-12`
  - Existing LLM-based trading strategy development primarily uses aggregated price and volume data, which omit within-interval event order and displayed order book changes. Tick-level trade and quote observations preserve this information, but their scale makes the full history impr…

- **[DS-Lighting: Making Agent Harnesses Explicit for Data-Science Automation](https://openreview.net/forum?id=m7wsVqhIYs)**
  - **ICML 2025** · OpenReview · `2026-10-11`
  - Large Language Model (LLM) agents have shown promise for automating data-science workflows, yet their end-to-end performance depends critically on the agent harness that represents tasks, manages execution state, constrains output artifacts, and provides evaluation feedback. Exis…

- **[TradingArena: A Market-Making Benchmark for Ranking, Diagnosing, and Steering LLM Behavior](https://openreview.net/forum?id=6VObvVwaGZ)**
  - **ICML 2025** · OpenReview · `2026-09-19`
  - As large language models are increasingly deployed as agents, evaluation should capture both task performance and interactive behavior. Few benchmarks jointly measure performance and behavior under controlled changes to an agent’s information, action space, and inference. We intr…

- **[Visual Reasoning at the Harness Level: A Ladder for Controlled Evaluation](https://openreview.net/forum?id=8Rdl9qkU1A)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Advances in foundation models are shifting coding and working agents from predefined tools toward general computational environments. Yet existing visual agents often couple model, harness, and training choices, making it difficult to determine how this transition affects visual…

- **[ParaFusionBench: A Unified Benchmark for Cross-Paradigm Fusion in Factor Mining and Trading Decision-Making](https://openreview.net/forum?id=nqb5xH3QuC)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Quantitative investment research has evolved from conventional models to large language models (LLMs) and multi-agent collaboration, forming two primary research trajectories: factor mining and trading decision-making. Their intersection yields four paradigms: Conventional Factor…

- **[Many Preferences, Few Policies: Compact Portfolios for Multi-Objective LLM Alignment](https://openreview.net/forum?id=byWrQmX9t4)**
  - **ICML 2025** · OpenReview · `2026-09-17`
  - Aligning large language models (LLMs) requires balancing competing objectives such as helpfulness, harmlessness, and conciseness. The appropriate balance varies across users and applications, yet training, evaluating, and deploying many policies across different reward weights is…

- **[FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors](https://openreview.net/forum?id=RKKGxm7O4L)**
  - **ICML 2025** · OpenReview · `2026-09-16`
  - As AI agents are becoming widely adopted in the financial services industry, careful measurement is essential to understand where they can be reliably deployed and where oversight and professional review remain necessary. Such measurement, however, is constrained by limited acces…

- **[PortfolioRouter: Consequence-Aware Multi-Task Routing for Portfolio Agents](https://openreview.net/forum?id=My6dyV7ecS)**
  - **ICML 2025** · OpenReview · `2026-09-14`
  - Portfolio agents can recommend materially different allocations for the same trading date, but standard best-expert classification does not weight errors by their financial cost. The cost of a routing error depends on the return forgone by choosing one proposal over another. We i…

- **[Multi-Identity Transaction Graph Pretraining for Fraud Detection](https://openreview.net/forum?id=1edqcNjZ3J)**
  - **ICML 2025** · OpenReview · `2026-09-07`
  - Real-world payment risk modeling is constrained by scarce fraud labels and fragmented behavioral context across multiple payment identities. A physical transaction may appear simultaneously in multiple behavioral histories defined by different identities, while each identity indu…

- **[Stacking RNNs and LSTMs for Fraud Detection in Cryptocurrency Blockchain Transactions](https://openreview.net/forum?id=Ukalf1pGgk)**
  - *{'username': '~Olufunso_Dayo_Alowolodu1', 'fullname': 'Olufunso Dayo Alowolodu', 'institutions': [{'name': 'The Federal University of Technology, Akure (FUTA)', 'domain': 'futa.edu.ng', 'country': 'NG'}]}*
  - **ICML 2025** · OpenReview · `2026-08-20`
  - Introduction
Cryptocurrency blockchains enable secure, decentralized financial transactions, but their pseudonymous, decentralized structure also makes them attractive for fraud such as money laundering, Ponzi schemes, and phishing, which makes it difficult for conventional intru…

- **[A Fraud-Detection-Inspired Framework for LLM Agents Security](https://openreview.net/forum?id=uUipgSY8Sh)**
  - *Sheldon Yu, Yingcheng Sun, Hanqing Guo et al.*
  - **ICML 2025** · OpenReview · `2026-06-12`
  - Large Language Model (LLM) agents demonstrate strong capabilities in autonomous task execution, tool use, and multi-step reasoning. However, their increasing autonomy also introduces a new attack surface: adversarial interactions can manipulate agent behavior through direct promp…

- **[FairCoder: Probing LLM Bias in High-Stakes Decision Making via Coding Tasks](https://openreview.net/forum?id=n7Mk11IVX8)**
  - *Yongkang Du, Jen-tse Huang, Jieyu Zhao et al.*
  - **ICML 2025** · OpenReview · `2026-06-03`
  - Large language models (LLMs) are increasingly used in high-stakes decisions such as hiring and college admissions, making their social bias a critical concern. While LLMs are trained to refuse explicitly biased requests, bias can be leaked implicitly during LLM planning and reaso…

- **[A multi-agent system for financial retrieval](https://openreview.net/forum?id=X86jxEIVtX)**
  - **ICML 2025** · OpenReview · `2026-02-11`

- **[CAFE-RL: Counterfactual Augmented Reinforcement Learning for Mechanism-Aware Onboarding Fraud Detection in E-Commerce](https://openreview.net/forum?id=31rXKDS7o8)**
  - *Linfeng Cao, Hang Yin, Yang Zhao et al.*
  - **ICML 2025** · OpenReview · `2026-02-03`
  - Buyer Onboarding Fraud Detection (BOFD), defined as fraud detection at the early stages of user registration and first-transaction screening, is a strategic decision-making problem that defines a platform intervention mechanism and shapes user participation, adversarial behavior,…

- **[Retriever Portfolios: A Principled Approach to Adaptive RAG](https://openreview.net/forum?id=NyGHaciFrK)**
  - *Miltiadis Stouras, Vincent Cohen-Addad, Silvio Lattanzi et al.*
  - **ICML 2025** · OpenReview · `2026-01-23`
  - Retrieval-augmented generation (RAG) systems typically rely on a single
retriever and a single set of hyperparameters, despite facing highly
heterogeneous queries that range from simple factoid questions to complex
multi-hop reasoning. We propose a method that automatically selec…

- **[Conversational Agents: A Framework for Evaluation (CAFE) (Dagstuhl Perspectives Workshop 24352)](https://openreview.net/forum?id=rpLDo1d8oU)**
  - *{'fullname': 'Christine Bauer', 'username': '~Christine_Bauer1'}, {'fullname': 'Li Chen'}, {'fullname': 'Nicola Ferro'} et al.*
  - **ICML 2025** · OpenReview · `2025-12-19`
  - During the workshop, we deeply discussed what CONversational Information ACcess (CONIAC) is and its unique features, proposing a world model abstracting it, and defined the Conversational Agents Framework for Evaluation (CAFE) for the evaluation of CONIAC systems, consisting of s…

- **[RAPTOR: Reasoned Agentic Portfolio Trading with Orchestrated Rebalancing](https://openreview.net/forum?id=ziuTkKhgT0)**
  - *Blake Almon, Matthew Caliboso, Alex Kim et al.*
  - **ICML 2025** · OpenReview · `2025-10-28`
  - We propose an institutional-style, multi-agent architecture for equity portfolio construction that couples a schema-constrained blackboard with structured debate and a Black-Litterman optimizer, enabling diversified, risk-aware allocations. The system is scalable, modular, and in…

- **[FinTSBridge: A New Evaluation Suite for Real-world Financial Prediction with Advanced Time Series Models](https://openreview.net/forum?id=b3xZoZcW1J)**
  - *Yanlong Wang, Jian Xu, Tiantian Gao et al.*
  - **ICML 2025** · OpenReview · `2025-09-25`
  - Despite the growing attention to time series forecasting in recent years, many studies have proposed various solutions to address the challenges encountered in time series prediction, aiming to improve forecasting performance. However, the strategic interactions inherent in finan…

- **[CTBench: Cryptocurrency Time Series Generation Benchmark](https://openreview.net/forum?id=RzT2sombPD)**
  - *Yihao Ang, Qiang Wang, Qiang Huang et al.*
  - **ICML 2025** · OpenReview · `2025-09-17`
  - Synthetic time series are vital for data augmentation, stress testing, and prototyping in quantitative finance. Yet in cryptocurrency markets, characterized by 24/7 trading, extreme volatility, and rapid regime shifts, existing Time Series Generation (TSG) methods and benchmarks…

- **[QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading](https://openreview.net/forum?id=fdKmhFYcQv)**
  - *Fei Xiong, Xiang Zhang, Aosong Feng et al.*
  - **ICML 2025** · OpenReview · `2025-09-08`
  - Recent advances in Large Language Models (LLMs) have shown remarkable capabilities in financial reasoning and market understanding. Multi-agent LLM frameworks such as TradingAgent and FINMEM augment these models to long-horizon investment tasks by leveraging fundamental and senti…

- **[Spatio-Temporal Directed Graph Learning for Account Takeover Fraud Detection](https://openreview.net/forum?id=Yx89Ibpym7)**
  - *Mohsen Nayebi Kerdabadi, William A. Byron, xin sun et al.*
  - **ICML 2025** · OpenReview · `2025-09-07`
  - Account Takeover (ATO) fraud poses a significant challenge in consumer banking, requiring high recall under strict latency while minimizing friction for legitimate users. Production systems typically rely on tabular gradient-boosted decision trees (e.g., XGBoost) that score sessi…

- **[Generation-Time vs. Post-hoc Citation: A Holistic Evaluation of LLM Attribution](https://openreview.net/forum?id=iQyfHmqRJR)**
  - *Yash Saxena, Raviteja Bommireddy, Ankur Padia et al.*
  - **ICML 2025** · OpenReview · `2025-09-05`
  - Trustworthy Large Language Models (LLMs) must cite human-verifiable sources in high-stakes domains such as healthcare, law, academia, and finance, where even small errors can have severe consequences. Practitioners and researchers face a choice: let models generate citations duri…

- **[A Protocol-Driven Platform for Agent-Agnostic Evaluation of LLM Agents](https://openreview.net/forum?id=G9YKfCddN3)**
  - *Cong Minh Tran, Issam Falih, Hatim CHAHDI et al.*
  - **ICML 2025** · OpenReview · `2025-09-05`
  - The fast growth of LLM-based agents has outpaced efforts to build solid evaluation standards, causing mismatched formats and idiosyncratic reporting that often makes fair comparisons challenging. To tackle this, we created a platform around a protocol-based setup that keeps evalu…

- **[Who Routes the Router: Rethinking the Evaluation of LLM Routing Systems](https://openreview.net/forum?id=EEPostHMtF)**
  - *Jiayi Yuan, Yifan Lu, Rixin Liu et al.*
  - **ICML 2025** · OpenReview · `2025-09-03`
  - The growing ecosystem of Large Language Models (LLMs) with diverse capabilities and costs has motivated the need for LLM routing systems that dynamically select the most appropriate model for each query.
Evaluating these routing systems is important yet inherently challenging due…

- **[Healthcare Insurance Fraud Detection via Continual Fiedler Vector Graph Model](https://openreview.net/forum?id=ZWDvIKMkMG)**
  - *Yehan Zhang, Huaidong Zhang, Xuandi Luo et al.*
  - **ICML 2025** · OpenReview · `2025-09-02`
  - Healthcare insurance fraud detection presents unique machine learning challenges: labeled data are scarce due to delayed verification processes, and fraudulent behaviors evolve rapidly, often manifesting in complex, graph-structured interactions. Existing methods struggle in such…

- **[The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets](https://openreview.net/forum?id=XZpIu68yW6)**
  - *Shenzhe Zhu, Jiao Sun, Yi Nian et al.*
  - **ICML 2025** · OpenReview · `2025-09-01`
  - AI agents are increasingly used in consumer-facing applications to assist with tasks such as product search, negotiation, and transaction execution. In this paper, we investigate a future setting where both consumers and merchants authorize AI agents to automate the negotiations…

- **[From Many Voices to One: Statistically Principled Aggregation of LLM Judges](https://openreview.net/forum?id=XdcofpTCyq)**
  - *Jitian Zhao, Changho Shin, Tzu-Heng Huang et al.*
  - **ICML 2025** · OpenReview · `2025-08-29`
  - LLM-as-a-judge---often with multiple judges---is now the standard for scalable model evaluation, yet judge biases and correlations can amplify errors. We cast aggregation as inference in a latent-factor Markov random field that jointly models a latent true-quality variable, inter…

- **[TradingGroup: A Multi-Agent Trading System with Self-Reflection and Data-Synthesis](https://arxiv.org/abs/2508.17565)**
  - *Feng Tian, Flora D. Salim, Hao Xue*
  - **ICML 2025** · OpenReview · `2025-08-01`
  - Recent advancements in large language models (LLMs) have enabled powerful agent-based applications in finance, particularly for sentiment analysis, financial report comprehension, and stock forecasting. However, existing systems often lack inter-agent coordination, structured sel…

- **[Financial Fraud Detection with Entropy Computing](https://openreview.net/forum?id=gRnaP5Mw4k)**
  - *Babak Emami, Wesley Dyk, David Haycraft et al.*
  - **ICML 2025** · OpenReview · `2025-07-16`
  - We introduce CVQBoost, a novel classification algorithm
that leverages early hardware implementing Quantum Computing Inc’s
Entropy Quantum Computing (EQC) paradigm, Dirac-3. We apply CVQ-
Boost to a fraud detection test case and benchmark its performance
against XGBoost, a widely…

- **[Search Algorithm Portfolios with Multithreaded Components](https://openreview.net/forum?id=VSMc1rHKLk)**
  - *Takumi Shimoda, Alex S. Fukunaga*
  - **ICML 2025** · OpenReview · `2025-07-12`
  - One successful approach to parallel satisficing search is a search algorithm portfolio, where each processor executes an independent search process. Portfolios are competitive with parallel search algorithms where threads use shared Open/Closed lists. We investigate the scalabili…

- **[Knowledge-Grounded Detection of Cryptocurrency Scams with Retrieval-Augmented LMs](https://openreview.net/forum?id=qDDuQGypqM)**
  - *Zichao Li*
  - **ICML 2025** · OpenReview · `2025-06-06`
  - This paper presents a knowledge-grounded framework for cryptocurrency scam detection using retrieval-augmented language models. We address three key limitations of existing approaches: static knowledge bases, unreliable LM outputs, and fixed classification thresholds. Our method…

- **[Trading-off Reward Maximization and Stability in Sequential Decision Making](https://openreview.net/forum?id=5FSTwSgQQz)**
  - *Federico Corso, Marco Mussi, Alberto Maria Metelli*
  - **ICML 2025** · OpenReview · `2025-06-04`
  - Reinforcement Learning (RL) focuses on learning policies that maximize the expected reward. This simple objective has enabled the success of RL in a wide range of scenarios. However, as emphasized by control-theoretic methods, stability is also a desired property when dealing wit…

- **[Multilingual Financial Word Embeddings for Arabic, English and French](https://openreview.net/forum?id=s3BXlQQ2IK)**
  - *{'fullname': 'Nadhem Zmandar', 'username': 'https://orcid.org/orcid-search/search?searchQuery=Nadhem%20Zmandar'}, {'fullname': 'Mahmoud El-Haj', 'username': '~Mo_El-Haj1'}, {'fullname': 'Paul Rayson', 'username': 'https://orcid.org/0000-0002-1257-2191'}*
  - **ICML 2025** · OpenReview · `2025-05-09`
  - Natural Language Processing is increasingly being applied to analyse the text of many different types of financial documents. For many tasks, it has been shown that standard language models and tools need to be adapted to the financial domain in order to properly represent domain…

- **[Risk and return prediction for pricing portfolios of non-performing consumer credit](https://openreview.net/forum?id=nrKd35xs6S)**
  - *WANG Siyi, Xing YAN, Bangqi Zheng et al.*
  - **ICML 2025** · OpenReview · `2025-02-26`
  - We design a system for risk-analyzing and pricing portfolios of non-performing consumer credit loans. The rapid development of credit lending business for consumers heightens the need for trading portfolios formed by overdue loans as a manner of risk transferring. However, the pr…

- **[agenticMSA: Agentic Multimodal Sentiment Analysis with Task-Specific and Large Language Model Collaboration](https://openreview.net/forum?id=ATwJ8MWnth)**
  - **ICML 2025** · OpenReview · `2025-02-10`
  - Multimodal Sentiment Analysis (MSA) faces challenges due to inconsistencies between modalities, such as conflicting sentiment cues from visual, audio, and text data. These modality conflicts make it difficult for previous task-specific samll-scale models to accurately predict sen…

- **[Financial Fraud Detection using Jump-Attentive Graph Neural Networks](https://openreview.net/forum?id=9w3R5lfhZB)**
  - *Prashank Kadam*
  - **ICML 2025** · OpenReview · `2025-02-07`
  - As the availability of financial services online continues to grow, the incidence of fraud has surged correspondingly. Fraudsters continually seek new and innovative ways
to circumvent the detection algorithms in place. Traditionally,
fraud detection relied on rule-based methods,…

- **[Performant LLM Agentic Framework for Conversational AI](https://openreview.net/forum?id=JDXB6nvH9x)**
  - *Alex Casella, Wayne Wang*
  - **ICML 2025** · OpenReview · `2025-01-22`
  - The rise of Agentic applications and automation in the Voice AI industry has led to an increased reliance on Large Language Models (LLMs) to navigate graph-based logic workflows composed of nodes and edges. However, existing methods face challenges such as alignment errors in com…

- **[Trading Confidence: Comprehensive Uncertainty Estimation in Algorithmic Trading](https://openreview.net/forum?id=IWDsycHMSP)**
  - *Lin Li, Li Rong Wang, Hsuan Fu et al.*
  - **ICML 2025** · OpenReview · `2025-01-01`
  - Description Reinforcement Learning (RL) has emerged as a powerful approach in financial trading, enabling agents to learn optimal strategies through direct market interaction. However, financial markets are highly uncertain, with price fluctuations driven by stochastic volatility…

- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://openreview.net/forum?id=4QPrXwMQt1)**
  - *Yijia Xiao, Edward Sun, Di Luo et al.*
  - **ICML 2025** · OpenReview · `2024-12-02`
  - Significant progress has been made in automated problem-solving using societies of agents powered by large language models (LLMs). In finance, efforts have largely focused on single-agent systems handling specific tasks or multi-agent frameworks independently gathering data. Howe…

- **[The Poorest Man in Babylon: A Longitudinal Study of Cryptocurrency Investment Scams](https://openreview.net/forum?id=P0x8J5gCPP)**
  - *Muhammad Muzammil, Abisheka Pitumpe, Xigao Li et al.*
  - **ICML 2025** · OpenReview · `2024-10-06`
  - Governments and regulatory bodies have recognized investment scams as the most prevalent forms of cryptocurrency fraud. These scams typically use professional-looking websites to lure unsuspecting victims with promises of unrealistically high returns. In this paper, we introduce…

- **[DiT-LSTM-SVAR Model For Portfolios](https://openreview.net/forum?id=MeOi6u9E23)**
  - *Yuxing Yuan, Ziwei Wang, Zhenyuan Huang et al.*
  - **ICML 2025** · OpenReview · `2024-09-26`
  - This paper proposes a novel combined model named DiT-LSTM-SVAR, which successfully integrates time series and the Efficient Markets Hypothesis. This is the first to combine the microstructure of financial markets with deep learning networks to improve the performance of portfolio…

- **[A Fully Analog Pipeline for Portfolio Optimization](https://openreview.net/forum?id=mtkbTUVaV1)**
  - *James S. Cummins, Natalia Berloff*
  - **ICML 2025** · OpenReview · `2024-09-11`
  - Portfolio optimization is a ubiquitous problem in financial mathematics that relies on accurate estimates of covariance matrices for asset returns. However, estimates of pairwise covariance are notoriously poor and calculating time-sensitive optimal portfolios is energy-intensive…

- **[Financial Sentiment Analysis: Techniques and Applications](https://openreview.net/forum?id=CFNmRsC7hs)**
  - *Kelvin Du, Frank Xing, Rui Mao et al.*
  - **ICML 2025** · OpenReview · `2024-09-01`
  - Financial Sentiment Analysis (FSA) is an important domain application of sentiment analysis that has gained increasing attention in the past decade. FSA research falls into two main streams. The first stream focuses on defining tasks and developing techniques for FSA, and its mai…

- **[A Portfolio’s Common Causal Conditional Risk-Neutral PDE](https://openreview.net/forum?id=oHgvpDTOve)**
  - *{'fullname': 'Alejandro Rodriguez Dominguez', 'username': '~Alejandro_Rodriguez_Dominguez1'}*
  - **ICML 2025** · OpenReview · `2024-08-01`
  - Portfolio’s optimal drivers for diversification are common causes of the constituents’ correlations. A closed-form formula for the conditional probability of the portfolio given its optimal common drivers is presented, with each pair constituent-common driver joint distribution m…

- **[Clustering-Augmented Fraud Detection on Graphs Using Label-Aware Feature Aggregation](https://openreview.net/forum?id=sosXTwotGd)**
  - *Shixiong Jing, Lingwei Chen, Dinghao Wu*
  - **ICML 2025** · OpenReview · `2024-07-04`
  - Fraud detection has emerged as a pivotal process in different fields (e.g., e-commerce, social networks). Since interactions among entities provide valuable insights into fraudulent activities, such behaviors can be naturally represented as graphs, where graph neural networks (GN…

- **[Cryptocurrency Prices Forecast Using GNNs](https://openreview.net/forum?id=vbdU3t6Nkp)**
  - *Ly Hai Nguyen, Edwin Onyango, Chahak Goyal et al.*
  - **ICML 2025** · OpenReview · `2024-03-31`
  - Cryptocurrencies have become an extremely popular and volatile market, delivering massive returns (as well as losses) to investors. Cryptocurrency returns prediction remains an open and extremely challenging forecasting task. Using the time series of historical prices as training…

- **[FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://openreview.net/forum?id=sstfVOwbiG)**
  - *Haohang Li, Yangyang Yu, Zhi Chen et al.*
  - **ICML 2025** · OpenReview · `2024-02-03`
  - Recent advancements in Large Language Models (LLMs) have exhibited notable efficacy in natural language processing (NLP) tasks across diverse domains. Their prowess in integrating extensive knowledge has fueled interest in developing LLM-based autonomous agents. Furthermore, in t…

- **[Financial Networks and Other Adventures in Graph Learning](https://openreview.net/forum?id=DCOnX2Zv6i)**
  - *Béni Egressy*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - This thesis investigates graph problems from both a machine learning and a theoretical perspective. In particular, it explores financial applications, focusing on fraud detection, central bank bailouts, and lending. The thesis is split into two main parts, broadly corresponding t…

- **[Financial Risk Assessment via Long-term Payment Behavior Sequence Folding](https://arxiv.org/abs/2411.15056)**
  - *Yiran Qiao, Yateng Tang, Xiang Ao et al.*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - Online inclusive financial services encounter significant financial risks due to their expansive user base and low default costs. By real-world practice, we reveal that utilizing longer-term user payment behaviors can enhance models' ability to forecast financial risks. However,…

- **[Financial Risk Assessment via Long-term Payment Behavior Sequence Folding](https://openreview.net/forum?id=unqcVrSezM)**
  - *Yiran Qiao, Yateng Tang, Xiang Ao et al.*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - Online inclusive financial services encounter significant financial risks due to their expansive user base and low default costs. By real-world practice, we reveal that utilizing longer-term user payment behaviors can enhance models' ability to forecast financial risks. However,…

- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)**
  - *Yijia Xiao, Edward Sun, Di Luo et al.*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - Significant progress has been made in automated problem-solving using societies of agents powered by large language models (LLMs). In finance, efforts have largely focused on single-agent systems handling specific tasks or multi-agent frameworks independently gathering data. Howe…

- **[Trading Volume Maximization with Online Learning](https://arxiv.org/abs/2405.13102)**
  - *Tommaso Cesari, Roberto Colomboni*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - We explore brokerage between traders in an online learning framework. At any round $t$, two traders meet to exchange an asset, provided the exchange is mutually beneficial. The broker proposes a trading price, and each trader tries to sell their asset or buy the asset from the ot…

- **[Collateral Portfolio Optimization in Crypto-Backed Stablecoins](https://arxiv.org/abs/2405.08305)**
  - *Bretislav Hajek, Daniël Reijsbergen, Anwitaman Datta et al.*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - Stablecoins - crypto tokens whose value is pegged to a real-world asset such as the US Dollar - are an important component of the DeFi ecosystem as they mitigate the impact of token price volatility. In crypto-backed stablecoins, the peg is founded on the guarantee that in case o…

- **[Cryptocurrency Analysis: Price Prediction of Cryptocurrency Using User Sentiments and Quantitative Data](https://openreview.net/forum?id=Iy7tsxFdSt)**
  - *Dayan Perera, Jessica Lim, Shuta Gunraku et al.*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - This research introduces an innovative approach to forecasting cryptocurrency prices by combining user-generated content (UGC) and sentiment analysis with quantitative data. The primary goal is to overcome limitations in existing methods for market forecasting, where accurate for…

- **[Cryptocurrency Topic Burst Prediction via Hybrid Twin-structured Multi-modal Learning](https://openreview.net/forum?id=h5r1B6G0dc)**
  - *Keting Yin, Xiaen Sun, Tian Feng*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - Social media users actively engage in discussions concerning news and events within the dynamic cryptocurrency market, resulting in the widespread dissemination of cryptocurrency-related topics across various platforms. The ongoing monitoring of these topics is crucial to informe…

- **[Cryptocurrency Price Forecasting Using XGBoost Regressor and Technical Indicators](https://arxiv.org/abs/2407.11786)**
  - *{'fullname': 'Abdelatif Hafid', 'username': ''}, {'fullname': 'Maad Ebrahim', 'username': ''}, {'fullname': 'Ali Alfatemi', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - The rapid growth of the stock market has attracted many investors due to its potential for significant profits. However, predicting stock prices accurately is difficult because financial markets are complex and constantly changing. This is especially true for the cryptocurrency m…

- **[Cryptocurrency Price Forecasting using Variational Autoencoder with Versatile Quantile Modeling](https://openreview.net/forum?id=VtVNMYPGRp)**
  - *Sungchul Hong, SeungHwan An, Jong-June Jeon*
  - **ICML 2025** · OpenReview · `2024-01-01`
  - In recent years, there has been a growing interest in probabilistic forecasting methods that offer more comprehensive insights by considering prediction uncertainties rather than point estimates. This paper introduces a novel variational autoencoder learning framework for multiva…

- **[Identifying Risky Vendors in Cryptocurrency P2P Marketplaces](https://openreview.net/forum?id=rvSv8Df4AB)**
  - *Taro Tsuchiya, Alejandro Cuevas, Nicolas Christin*
  - **ICML 2025** · OpenReview · `2023-10-04`
  - Peer-to-Peer (P2P) cryptocurrency exchanges are two-sided marketplaces, similar to eBay/Craigslist, where individuals can offer to sell cryptocurrency assets in exchange for payment.
Due to disintermediation, these marketplaces trade off increased privacy for higher risk (e.g., s…

- **[Interface Illusions: Uncovering the Rise of Visual Scams in Cryptocurrency Wallets](https://openreview.net/forum?id=39AIGw9x8m)**
  - *Guoyi Ye, Geng Hong, Yuan Zhang et al.*
  - **ICML 2025** · OpenReview · `2023-09-27`
  - Cryptocurrencies, while revolutionary, have become a magnet for malicious actors. With numerous reports underscoring cyberattacks and scams in this domain, our paper takes the lead in characterizing visual scams associated with cryptocurrency wallets—a fundamental component of We…

- **[Exploring Modern Evolution Strategies in Portfolio Optimization](https://openreview.net/forum?id=KiQ8PhDzIU)**
  - *Ramin Hasani, Etan A Ehsanfar, Greg A Banis et al.*
  - **ICML 2025** · OpenReview · `2023-09-26`
  - Black-box optimization (BBO) techniques are often the core engine used in combinatorial optimization problems which include multi-asset class portfolio construction. The computational complexity of such evolutionary algorithms, however, is excessively high to the point that findi…

- **[Partitioning Message Passing for Graph Fraud Detection](https://openreview.net/forum?id=tEgrUrUuwA)**
  - *Wei Zhuo, Zemin Liu, Bryan Hooi et al.*
  - **ICML 2025** · OpenReview · `2023-09-24`
  - Label imbalance and homophily-heterophily mixture are the fundamental problems encountered when applying Graph Neural Networks (GNNs) to Graph Fraud Detection (GFD) tasks. Existing GNN-based GFD models are designed to augment graph structure to accommodate the inductive bias of G…

- **[Financial Time Series Data Prediction by Combination Model Adaboost-KNN-LSTM](https://openreview.net/forum?id=JRZ1CG0S6n)**
  - *Heng Zhao, Xinran Li, Jiakai Xu et al.*
  - **ICML 2025** · OpenReview · `2023-01-01`
  - Financial time series is the main research direction of financial researchers due to its important economic value. However, owing to stochastic nature of financial markets, the data used by financial time series models need to have a series of features. This limits the use of fin…

- **[Unsupervised Financial Fraud Detection Using Low-rank Recovery](https://openreview.net/forum?id=zFcQ9cez3h)**
  - *Jingjing Zheng, John Hawkin, Charles Robertson et al.*
  - **ICML 2025** · OpenReview · `2023-01-01`
  - Many outlier detection methods have been studied and applied to financial fraud detection problems in recent years. These traditional financial fraud detection problems (such as classification-based methods) often suffer performance degradation caused by imbalanced data. Even wor…

- **[Spotlight News Driven Quantitative Trading Based on Trajectory Optimization](https://openreview.net/forum?id=jLIv3t9fuR)**
  - *Mengyuan Yang, Mengying Zhu, Qianqiao Liang et al.*
  - **ICML 2025** · OpenReview · `2023-01-01`
  - News-driven quantitative trading (NQT) has been popularly studied in recent years. Most existing NQT methods are performed in a two-step paradigm, i.e., first analyzing markets by a financial prediction task and then making trading decisions, which is doomed to failure due to the…

- **[Portfolio Optimization using Predictive Auxiliary Classifier Generative Adversarial Networks with Measuring Uncertainty](https://arxiv.org/abs/2304.11856)**
  - *Jiwook Kim, Minhyeok Lee*
  - **ICML 2025** · OpenReview · `2023-01-01`
  - In financial engineering, portfolio optimization has been of consistent interest. Portfolio optimization is a process of modulating asset distributions to maximize expected returns and minimize risks. To obtain the expected returns, deep learning models have been explored in rece…

- **[Collaborative Fraud Detection: How Collaboration Impacts Fraud Detection](https://openreview.net/forum?id=doxofj6iUW)**
  - *Jinzhang Hu, Ruimin Hu, Zheng Wang et al.*
  - **ICML 2025** · OpenReview · `2023-01-01`
  - Collaborative fraud has become increasingly serious in telecom and social networks, but is hard to detect by traditional fraud detection methods. In this paper, we find a significant positive correlation between the increase of collaborative fraud and the degraded detection perfo…

- **[Cryptocurrency Portfolio Optimization by Neural Networks](https://arxiv.org/abs/2310.01148)**
  - *Quoc Minh Nguyen, Dat Thanh Tran, Juho Kanniainen et al.*
  - **ICML 2025** · OpenReview · `2023-01-01`
  - Many cryptocurrency brokers nowadays offer a variety of derivative assets that allow traders to perform hedging or speculation. This paper proposes an effective algorithm based on neural networks to take advantage of these investment products. The proposed algorithm constructs a…

- **[Cryptocurrency Portfolio Optimization by Neural Networks](https://openreview.net/forum?id=8alfjwG7lf)**
  - *Quoc Minh Nguyen, Dat Thanh Tran, Juho Kanniainen et al.*
  - **ICML 2025** · OpenReview · `2023-01-01`
  - Many cryptocurrency brokers nowadays offer a va-riety of derivative assets that allow traders to perform hedging or speculation. This paper proposes an effective algorithm based on neural networks to take advantage of these investment products. The proposed algorithm constructs a…

- **[Examining Liquidity of Exchanges and Assets and the Impact of External Events in Centralized Crypto Markets: A 2022 Study](https://openreview.net/forum?id=tpk47MymYw)**
  - *Adrian Jobst, Daniel Atzberger, Robert Henker et al.*
  - **ICML 2025** · OpenReview · `2023-01-01`
  - Most cryptocurrencies are bought and sold on centralized exchanges that manage supply and demand via an order book. Besides trading fees, the high liquidity of a market is the most relevant reason for choosing one exchange over the other. However, as the different liquidity measu…

- **[Financial data analysis application via multi-strategy text processing](https://arxiv.org/abs/2204.11394)**
  - *Hongyin Zhu*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - Maintaining financial system stability is critical to economic development, and early identification of risks and opportunities is essential. The financial industry contains a wide variety of data, such as financial statements, customer information, stock trading data, news, etc.…

- **[Cryptographic and Financial Fairness](https://openreview.net/forum?id=B56IlH5g8N)**
  - *Daniele Friolo, Fabio Massacci, Chan Nam Ngo et al.*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - A recent trend in multi-party computation is to achieve cryptographic fairness via monetary penalties, i.e. each honest player either obtains the output or receives a compensation in the form of a cryptocurrency. We pioneer another type of fairness, financial fairness, that is cl…

- **[Cryptographic and Financial Fairness](https://arxiv.org/abs/2207.10780)**
  - *Daniele Friolo, Fabio Massacci, Chan Nam Ngo et al.*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - A recent trend in multi-party computation is to achieve cryptographic fairness via monetary penalties, i.e. each honest player either obtains the output or receives a compensation in the form of a cryptocurrency. We pioneer another type of fairness, financial fairness, that is cl…

- **[Trading Positional Complexity vs Deepness in Coordinate Networks](https://openreview.net/forum?id=0qVaMVKCNi)**
  - *Jianqiao Zheng, Sameera Ramasinghe, Xueqian Li et al.*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - It is well noted that coordinate-based MLPs benefit—in terms of preserving high-frequency information—through the encoding of coordinate positions as an array of Fourier features. Hitherto, the rationale for the effectiveness of these positional encodings has been mainly studied…

- **[A Selective Portfolio Management Algorithm with Off-Policy Reinforcement Learning Using Dirichlet Distribution](https://openreview.net/forum?id=JVZvp4YhI4)**
  - *Hyunjun Yang, Hyeonjun Park, Kyungjae Lee*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - Existing methods in portfolio management deterministically produce an optimal portfolio. However, according to modern portfolio theory, there exists a trade-off between a portfolio’s expected returns and risks. Therefore, the optimal portfolio does not exist definitively, but sev…

- **[Cryptocurrency Trading Agent Using Deep Reinforcement Learning](https://openreview.net/forum?id=XW3tnMhPFu)**
  - *Uwais Suliman, Terence L. van Zyl, Andrew Paskaramoorthy*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - Cryptocurrencies are peer-to-peer digital assets monitored and organised by a blockchain network. Price prediction has been a significant focus point with various machine learning algorithms, especially concerning cryptocurrency. This work addresses the challenge faced by traders…

- **[Cryptocurrency Price Prediction with Convolutional Neural Network and Stacked Gated Recurrent Unit](https://openreview.net/forum?id=98spjLJzqq)**
  - *Chuen Yik Kang, Chin-Poo Lee, Kian-Ming Lim*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - Virtual currencies have been declared as one of the financial assets that are widely recognized as exchange currencies. The cryptocurrency trades caught the attention of investors as cryptocurrencies can be considered as highly profitable investments. To optimize the profit of th…

- **[A Deep Learning-Based Cryptocurrency Price Prediction Model That Uses On-Chain Data](https://openreview.net/forum?id=6XBg6f3kBb)**
  - *Gyeongho Kim, Dong-Hyun Shin, Jaegyeong Choi et al.*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - Cryptocurrency has recently attracted substantial interest from investors due to its underlying philosophy of decentralization and transparency. Considering cryptocurrency’s volatility and unique characteristics, accurate price prediction is essential for developing successful in…

- **[Cryptocurrency Price Prediction With Multi-task Multi-step Sequence-to-Sequence Modeling](https://openreview.net/forum?id=x5ZNDu77kF)**
  - *Jesper T. Kristensen, Juan P. Madrigal-Cianci, Giorgos Felekis et al.*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - In the scientific and commercial worlds, predicting cryptocurrency prices over time has gotten a lot of interest. Most related studies use variations of Recurrent Neural Networks to forecast the next value of a single coin due to the temporal nature of the challenge. As a result,…

- **[Financial fraud risk analysis based on audit information knowledge graph](https://openreview.net/forum?id=85kQohPZew)**
  - *Huidong Wu, Yanpeng Chang, Jianping Li et al.*
  - **ICML 2025** · OpenReview · `2021-01-01`
  - The frequent occurrence of financial fraud caused by listed companies has seriously hindered the healthy development of the capital market. Existing studies usually analyze financial fraud through the effectiveness of audit opinion or the correlation between auditor change rate a…

- **[Financial fraud detection using the related-party transaction knowledge graph](https://openreview.net/forum?id=Ib8D0OFUDt)**
  - *Xuting Mao, Hao Sun, Xiaoqian Zhu et al.*
  - **ICML 2025** · OpenReview · `2021-01-01`
  - Financial fraud detection has gained constant attention from researchers, practitioners, and regulators. Because of its concealment and ease of manipulation, related-party transactions (RPTs) among firms have become a usual way to implement financial fraud. However, the tradition…

- **[Trading strategy of structured mutual fund based on deep learning network](https://openreview.net/forum?id=oh1ymyx23K)**
  - *Jiao Chen, Changqing Luo, Lurun Pan et al.*
  - **ICML 2025** · OpenReview · `2021-01-01`
  - Highlights•Deep learning network is constructed for trading strategy of structured fund.•Deep learning network is useful for modeling structured fund’s trading strategy.•Considering trading behavior and share numbers can improve model performance.•Transfer learning can stabilize…

- **[Trading off data resource availability and privacy preservation in multi-layer network transaction](https://openreview.net/forum?id=FsX7y5IZl3)**
  - *Yun Hu, Chunguo Li, Aiqun Hu et al.*
  - **ICML 2025** · OpenReview · `2021-01-01`
  - The big data market solves the problem of the effective utilization of data through treating data as the circulating commodity in the market. The existing body of research on the big data market suggests that either improving the availability of published data or protecting sensi…

- **[Trading with the Momentum Transformer: An Intelligent and Interpretable Architecture](https://arxiv.org/abs/2112.08534)**
  - *Kieran Wood, Sven Giegerich, Stephen J. Roberts et al.*
  - **ICML 2025** · OpenReview · `2021-01-01`
  - We introduce the Momentum Transformer, an attention-based deep-learning architecture, which outperforms benchmark time-series momentum and mean-reversion trading strategies. Unlike state-of-the-art Long Short-Term Memory (LSTM) architectures, which are sequential in nature and ta…

- **[Cryptocurrency Usage Impact on Perceived Benefits and Users’ Behaviour](https://openreview.net/forum?id=iOEHErWiXz)**
  - *{'fullname': 'Omar Alqaryouti'}, {'fullname': 'Nur Siyam'}, {'fullname': 'Zainab Alkashri'} et al.*
  - **ICML 2025** · OpenReview · `2020-04-17`
  - This paper aims to analyse the impact of Cryptocurrency usage on users’ perceived benefits and behaviour. The Technology Acceptance Model has been used as foundation for this research. In this study, three main factors were examined, namely perceived ease of use, perceived benefi…

- **[Users’ Knowledge and Motivation on Using Cryptocurrency](https://openreview.net/forum?id=k7lgOyf7XP)**
  - *{'fullname': 'Omar Alqaryouti'}, {'fullname': 'Nur Siyam'}, {'fullname': 'Zainab Alkashri'} et al.*
  - **ICML 2025** · OpenReview · `2020-04-17`
  - Cryptocurrency is a decentralized digital currency stored in an online form that does not fall under governments and banks control. This study aimed at understanding users’ knowledge and their motivation on using cryptocurrency through structured interviews. Data was gathered thr…

- **[Financial news recommendation based on graph embeddings](https://openreview.net/forum?id=zzffQUnh7x)**
  - *Jiangtao Ren, Jiawei Long, Zhikang Xu*
  - **ICML 2025** · OpenReview · `2019-01-01`
  - Highlights•We introduce NNR, a graph-based method for financial news recommendation that outperforms the commonly used baselines.•We develop INNR, an incremental approach that makes the recommendation process more efficient.•We combine NNR and INNR to create a graph embeddings-ba…

- **[Towards Decentralized Equilibrium Asset Trading Based on Blockchain](https://openreview.net/forum?id=WtEKcbKlao)**
  - *Kai Lei, Maoyu Du, Liwei Yang et al.*
  - **ICML 2025** · OpenReview · `2019-01-01`
  - The last decade has witnessed the explosive growth of digital tokens and cryptocurrencies including Bitcoin, reward programs and various tokens on Ethereum. However, trading these heterogeneous and non-financial digital assets often encounters substantial liquidity barriers due t…

- **[Cryptocurrency Usage Impact on Perceived Benefits and Users' Behaviour](https://openreview.net/forum?id=XfaL2qmyIE)**
  - *Omar Alqaryouti, Nur Siyam, Zainab Alkashri et al.*
  - **ICML 2025** · OpenReview · `2019-01-01`
  - This paper aims to analyse the impact of Cryptocurrency usage on users’ perceived benefits and behaviour. The Technology Acceptance Model has been used as foundation for this research. In this study, three main factors were examined, namely perceived ease of use, perceived benefi…

- **[Users' Knowledge and Motivation on Using Cryptocurrency](https://openreview.net/forum?id=nukYddD2kK)**
  - *Omar Alqaryouti, Nur Siyam, Zainab Alkashri et al.*
  - **ICML 2025** · OpenReview · `2019-01-01`
  - Cryptocurrency is a decentralized digital currency stored in an online form that does not fall under governments and banks control. This study aimed at understanding users’ knowledge and their motivation on using cryptocurrency through structured interviews. Data was gathered thr…

- **[Computation of Loss Distribution Based on the Structural Model for Credit Portfolios](https://openreview.net/forum?id=H9YyL2epYt)**
  - *Meng Han*
  - **ICML 2025** · OpenReview · `2018-01-01`
  - Credit risk analysis and management at the portfolio level is a challenging issue for financial institutions due to their portfolios’ large size, heterogeneity and complex correlation structure. In this thesis, we propose several new asymptotic methods and exact methods to comput…

- **[Financial Fraud Detection: a New Ensemble Learning Approach for Imbalanced Data](https://openreview.net/forum?id=wlgQTGscdX)**
  - *Yiyang Bian, Min Cheng, Chen Yang et al.*
  - **ICML 2025** · OpenReview · `2016-01-01`
  - With the rapid development of online and offline transactions, various financial fraud crimes happen every day. Financial fraud has seriously affected the health of economics and damaged the welfare of consumers, investors, as well as financial institutions. Prior studies apply s…

- **[Portfolio approaches for constraint optimization problems](https://openreview.net/forum?id=j3FK0IgKQi)**
  - *Roberto Amadini, Maurizio Gabbrielli, Jacopo Mauro*
  - **ICML 2025** · OpenReview · `2016-01-01`
  - Within the Constraint Satisfaction Problems (CSP) context, a methodology that has proven to be particularly performant consists of using a portfolio of different constraint solvers. Nevertheless, comparatively few studies and investigations have been done in the world of Constrai…

- **[Portfolio Methods for Optimal Planning: An Empirical Analysis](https://openreview.net/forum?id=475019BUk2)**
  - *Mattia Rizzini, Chris Fawcett, Mauro Vallati et al.*
  - **ICML 2025** · OpenReview · `2015-01-01`
  - Combining the complementary strengths of several algorithms through portfolio approaches has been demonstrated to be effective in solving a wide range of AI problems. Notably, portfolio techniques have been prominently applied to suboptimal (satisficing) AI planning. Here, we con…

- **[Portfolio performance and risk-based assessment of the PORTRAIT tool](https://openreview.net/forum?id=nePDRDlqmL)**
  - *Konstantina Pendaraki, Nikolaos I. Spanoudakis*
  - **ICML 2025** · OpenReview · `2015-01-01`
  - In this paper we evaluate and extend the PORTRAIT tool. PORTRAIT applies an argumentation based methodology for composing fund portfolios. Argumentation allows for combining different contexts and preferences in a way that can be optimized. It allows for defining a set of differe…

- **[Portfolio Methods in Uncertain Contexts. (Méthodes de portefeuille en contexte incertain)](https://openreview.net/forum?id=UOZdaO3HdK)**
  - *Jialin Liu*
  - **ICML 2025** · OpenReview · `2015-01-01`
  - en fr This manuscript concentrates in studying methods to handle the noise, including using resampling methods to improve the convergence rates and applying portfolio methods to cases with uncertainties (games, and noisy optimization in continuous domains).Part I will introduce t…

- **[Financial Market Prediction Based On Online Opinion Ensemble](https://openreview.net/forum?id=GfwxqxCXjR)**
  - *Wei Xu, Daoyuan Sun, Zihe Meng et al.*
  - **ICML 2025** · OpenReview · `2012-01-01`
  - Financial market prediction is one of the most attractive research areas in financial data mining field because of its available data and potential profits. Financial market prediction has been paid much attention by many researchers and practitioners. Huge numbers of forecasting…

- **[Trading Agents](https://openreview.net/forum?id=8QTqyKAeeN)**
  - *Michael P. Wellman*
  - **ICML 2025** · OpenReview · `2011-01-01`
  - Automated trading in electronic markets is one of the most common and consequential applications of autonomous software agents.

- **[Financial supply chain management](https://openreview.net/forum?id=qNRO4hqcog)**
  - *Miao He, Changrui Ren, Bing Shao et al.*
  - **ICML 2025** · OpenReview · `2010-01-01`
  - To effectively manage a supply chain, we should no longer focus on physical flow and informational flow only, but also the financial flow. The financial supply chain management (FSCM) extracts capital tied to the raw material, work-in-process, inventory in transit, and accounts r…

- **[Financial Forecasting with Gompertz Multiple Kernel Learning](https://openreview.net/forum?id=61F5yY82AP)**
  - *Han Qin, Dejing Dou, Yue Fang*
  - **ICML 2025** · OpenReview · `2010-01-01`
  - Financial forecasting is the basis for budgeting activities and estimating future financing needs. Applying machine learning and data mining models to financial forecasting is both effective and efficient. Among different kinds of machine learning models, kernel methods are well…

- **[Portfolio optimization for wealth-dependent risk preferences](https://openreview.net/forum?id=a9ZZOydRP9)**
  - *Luis Miguel Rios, Nikolaos V. Sahinidis*
  - **ICML 2025** · OpenReview · `2010-01-01`
  - Empirical and theoretical studies of preference structures of investors have long shown that personal and corporate utility is typically multimodal, implying that the same investor can be risk-averse at certain levels of wealth while risk-seeking at others. In this paper, we cons…

- **[Portfolio construction using argumentation and hybrid evolutionary forecasting algorithms](https://openreview.net/forum?id=Q76JVm1o5n)**
  - *Nikolaos I. Spanoudakis, Konstantina Pendaraki, Grigorios N. Beligiannis*
  - **ICML 2025** · OpenReview · `2009-01-01`
  - In the current contribution, an application for constructing mutual fund portfolios is presented. This approach comprises several Intelligent Methods, namely an argumentation based decision making framework and a hybrid evolutionary forecasting algorithm which combines Genetic Al…

- **[Resource-Bounded Fraud Detection](https://openreview.net/forum?id=dOUXFZ9lCD)**
  - *Luís Torgo*
  - **ICML 2025** · OpenReview · `2007-01-01`
  - This paper describes an approach to fraud detection targeted at applications where this task is followed by a posterior human analysis of the signaled frauds. This is a frequent setup on fraud detection applications (e.g. credit card misuse, telecom fraud, etc.). In real world ap…

- **[Application of Large Language Model Fine-Tuning in Financial News Sentiment Recognition](https://doi.org/10.1145/3832928.3833015)**
  - *Le-Le Zhang*
  - **ICML 2026** · `2026-05-15`
  - The application of sentiment information in financial market analysis has drawn growing attention from both academia and industry. Nevertheless, as the volume of financial news and textual data continues to expand, traditional manual analysis methods show obvious limitations in t…


### ACL

- **[Nominate-then-Adjudicate: LLM-Assisted One-Pass and Per-Instance MIP Solver Tuning](https://arxiv.org/abs/2610.29391v1)**
  - *Yifan Zhao, Qianyang Zhao, Xinyu Guan et al.*
  - **ACL** · `2026-10-21`
  - Mixed-integer programming solvers expose hundreds or even thousands of parameters whose best setting varies per instance, yet per-instance search is prohibitively expensive. We frame this as configuration for heterogeneous Big Data optimization workloads and propose a nominate-th…

- **[MultiFinBen: Benchmarking Large Language Models for Multilingual and Multimodal Financial Application](https://arxiv.org/abs/2506.14028)**
  - *Xue-Qing Peng, Ling-Fei Qian, Yan Wang et al.*
  - **ACL 2025** · `2025-06-16`
  - Real-world financial analysis involves information across multiple languages and modalities, from reports and news to scanned filings and meeting recordings. Yet most existing evaluations of LLMs in finance remain text-only, monolingual, and largely saturated by current models. T…


### IJCAI

- **[Fin-PRM: A Domain-Specialized Process Reward Model for Financial Reasoning in Large Language Models](https://arxiv.org/abs/2508.15202)**
  - *Jie Zhu, Yuanchen Zhou, Shuo Jiang et al.*
  - **IJCAI 2025** · `2025-08-21`
  - Process Reward Models (PRMs) supervise intermediate reasoning steps in large language models (LLMs), but existing PRMs are mainly trained on general-domain data and struggle with the structured, symbolic, and fact-sensitive nature of financial reasoning. Financial tasks require n…


### Other / arXiv

- **[Memory-Centric Continual Learning for AI Agents](https://arxiv.org/abs/2610.29357)**
  - *Dongfang Li, Zhuoen Chen, Bonian Jia et al.*
  - 🤗 Featured · `2026-10-21`
  - Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive ret…

- **[Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use](https://arxiv.org/abs/2610.30108)**
  - *Yanzhe Chen, Ziyi Yang, Jifeng Zhu et al.*
  - 🤗 Featured · `2026-10-21`
  - Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed system…

- **[Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113)**
  - *Houde Qian, Zheng Jiang, Wenyi Li et al.*
  - 🤗 · `2026-10-21`
  - Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether lar…

- **[LTEM: LLM-Friendly Table-Enhanced Markdown for Table Understanding and Generation](https://arxiv.org/abs/2610.29188)**
  - *Eunbin Kim, Hyeonseok Kang, Sangkeun Jung*
  - 🤗 · `2026-10-21`
  - Tables in real-world documents, including scientific papers, financial reports, and statistical summaries, frequently use merged cells, multi-level headers, and sectioned layouts. Yet the lightweight formats LLMs handle best (Markdown, CSV) cannot express these structures, while…

- **[The End of Consensus Research?](https://arxiv.org/abs/2610.30114v1)**
  - *Clément Burgelin, Rachid Guerraoui, Zicong Hong et al.*
  - `2026-10-21`
  - Consensus is a fundamental problem in distributed computing and at the core of state machine replication (SMR). Despite decades of active human research, discovering practical low-latency solutions to the problem is still open, as it requires combining protocol knowledge, correct…

- **[The Reflexivity Threshold: A Phase Transition for Multi-Agent Performative Prediction](https://arxiv.org/abs/2610.29577v1)**
  - *Ahmed Mahrous, Roberto Di Pietro*
  - `2026-10-21`
  - Many learning systems are performative: once deployed, their predictions change the data distribution on which future models are trained. In multi-agent settings, this feedback is routed through a network of interacting learners, so stability depends not only on the strength of p…

- **[Beyond Small Talk: Modeling Disclosure Trajectories in Human-AI Conversation](https://arxiv.org/abs/2610.29413v1)**
  - *Keith Kwok, Wanting Ning, Tej Deep Pala et al.*
  - `2026-10-21`
  - Recently, we see a rise in conversational agents as a form of social and emotional support, where disclosure will unfold over time. Yet, current evaluations of these agents typically examine isolated conversational states. In analyses of naturally occurring conversations, disclos…

- **[Bridging Foundational and Agentic Capabilities of LLMs](https://arxiv.org/abs/2610.29751v1)**
  - *Wei Guo, Yuanjian Xu, Jianing Hao et al.*
  - `2026-10-21`
  - Large language models (LLMs) are increasingly deployed as agents, yet it remains unclear how their foundational capabilities translate into agentic capabilities. End-to-end scores leave unresolved whether low benchmark capability or weak deployment drives a failure, limiting acti…

- **[Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization](https://arxiv.org/abs/2610.29671v1)**
  - *Zhiqian Xia, Jielong Tang, Ling-An Zeng et al.*
  - `2026-10-21`
  - Long-term agent memory is shifting from predefined workflows toward learnable policies for memory construction and retrieval. Existing learning-based methods either optimize construction alone or combine retrieval-side online reinforcement learning (RL) with offline construction…

- **[Leveraging Time-Series Foundation Models for Financial Crime Detection](https://arxiv.org/abs/2610.29667v1)**
  - *Danae Natalie Savvidi, H. Çağrı Bilgi, Kubilay Atasu et al.*
  - `2026-10-21`
  - Financial crime detection requires identifying illicit activity within large transaction networks, where suspicious behaviour is rare and unfolds over time. Existing graph-based methods capture relationships among accounts but typically underuse the temporal behaviour encoded in…

- **[What Prediction-Market Contracts Reveal at Launch: Trading Volume and Dispute Risk](https://arxiv.org/abs/2610.29578v1)**
  - *Ahmed Mahrous, Roberto Di Pietro*
  - `2026-10-21`
  - Using a near-census of 802,863 resolved markets listed on Polymarket between January 2023 and May 2026, and only information available at listing (the market's title and description, named resolution source, and contract metadata), we predict lifetime trading volume and whether s…

- **[Lineage-Aware Search Control for LLM-Based Evolutionary Factor Mining](https://arxiv.org/abs/2610.29663v1)**
  - *Xintong Liu, Chenkai Zhang, Yanzhao Ma et al.*
  - `2026-10-21`
  - Formulaic alpha factor mining searches for symbolic expressions that transform market data into predictive signals. Recent LLM-based evolutionary factor mining methods use large language models as semantic variation operators. Under the conventional LLM-EA paradigm, stochastic va…

- **[When Are We Near Nash? Certifying Solutions in General-Sum Games](https://arxiv.org/abs/2610.29300v1)**
  - *Boning Li, Longbo Huang*
  - `2026-10-21`
  - Heuristic solvers for general-sum extensive-form games produce a stream of iterates, and practice reports the NashGap of the returned profile. We ask what a solver can know about its own iterates from the regret accumulators and the terminal-distribution accumulators its updates…

- **[Distributions or Quantiles? A Convex Variational Theory of Worst-Case Risk](https://arxiv.org/abs/2610.29652v1)**
  - *Jianjun Gao, Jonathan Li, Zhen Wang et al.*
  - `2026-10-21`
  - Worst-case risk evaluation is central to finance and operations research, yet existing analytical results remain fragmented and largely confined to ambiguity sets with specific structures. Using spectral risk measures as the underlying class, we develop a convex variational theor…

- **[AgentPolicyForge: From Executable Environments to Policy Benchmarks and Adaptive Guards](https://arxiv.org/abs/2610.28989v1)**
  - *Chao Shang, Wanyu Du, Yi Zhang et al.*
  - `2026-10-20`
  - Customized agent deployments define policies over tools, resources, and execution conditions. Providing these policies in the task agent's prompt does not reliably prevent violations. Training a guard requires examples of tool calls that comply with or violate those policies. We…

- **[Behavior Beyond Text: Evaluating Refusal Transfer Failure in LLM Agents](https://arxiv.org/abs/2610.28982v1)**
  - *Ekagra Gupta, Raj Saha, Aniekan-Abasi Inyang et al.*
  - `2026-10-20`
  - While large language models are increasingly deployed as tool-calling agents, their safety evaluations still focus primarily on their ability to refuse harmful requests in text. We investigate whether the refusal behavior in text transfers to tool use. We construct a benchmark of…

- **[JaxMARL-BC: Multi-Agent Reinforcement Learning for Macroeconomic Modelling, in Seconds](https://arxiv.org/abs/2610.28907v1)**
  - *Daniele Montagnani, Andrea Coletta, Antonietta Mira et al.*
  - `2026-10-20`
  - Multi-agent reinforcement learning (MARL) offers a principled way of populating simulated economies with many heterogeneous decision makers. Its adoption, pioneered in finance, has nonetheless been slow in macroeconomics because of two main limitations: the lack of a shared frame…

- **[SANE: Automated Scorer-Specific Metamorphic Testing for LLM Judges](https://arxiv.org/abs/2610.28886v1)**
  - *Ethan Ludwick, Yu-Chung Hsiao*
  - `2026-10-20`
  - LLM judges increasingly mediate benchmark evaluation, model selection, data curation, and training. Their decisions are useful only when each judge responds reliably to changes affecting its scoring criterion. Existing methods for reliability testing perturb inputs with known exp…

- **[Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition](https://arxiv.org/abs/2610.28578v1)**
  - *Wenjie Lou, Tianshuo Peng, Shiyang Feng et al.*
  - `2026-10-20`
  - In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and r…

- **[Toward Agentic AI for the 6G Physical Layer: From Algorithm Discovery to Verified Baseband Silicon](https://arxiv.org/abs/2610.27797v1)**
  - *Eric Mittag, Lukas Brechtel, Maximilian Stark et al.*
  - `2026-10-20`
  - 6G will be designed faster than it can be built: AI-driven search already proposes physical-layer algorithms at machine speed, while carrying a single one onto embedded baseband silicon remains specialist work. That silicon imposes hard memory and numeric limits, but also exposes…

- **[S$^2$-MAS: A Society-Scale Multi-Agent Simulation Framework with 500 Million Household Persona Agents](https://arxiv.org/abs/2610.27746v2)**
  - *Yang Li, Di Wan, Yike Wang et al.*
  - `2026-10-20`
  - Simulating economic responses at society scale requires agents whose decisions reflect household circumstances and the effects of earlier actions. We introduce S$^2$-MAS, a society-scale multi-agent simulation framework built on 500 million synthetic household personas grounded i…

- **[Reusing Multimodal Agents: Efficient Evaluation of Sound Designs in Games](https://arxiv.org/abs/2610.27670v1)**
  - *Thai Nguyen Van, Ibrahim Khan, Mury Fajar Dewantoro et al.*
  - `2026-10-20`
  - This paper introduces a novel framework for efficiently evaluating in-game sound designs using multimodal learning and reinforcement learning. Sound design significantly influences gameplay and accessibility; however, objective evaluation methods, defined here as automated assess…

- **[The More the Better? A Comparison of Single- and Multi-Agent LLM Setups on a Financial Review Task](https://arxiv.org/abs/2610.27488v1)**
  - *Pei Liu*
  - `2026-10-20`
  - Practitioner guidance holds that a large language model reviews a document better when the work is divided among agents. We test a narrow form of it in a controlled comparison of single-agent and multi-agent setups on a financial task, reviewing credit assessment memos against re…

- **[Securing Agentic Commerce Through Behavior-Aware Fraud Detection and Cybersecurity for Trusted AI-Agent Payment Authorization](https://arxiv.org/abs/2610.27483v1)**
  - *Kayode L. Ogunsusi*
  - `2026-10-20`
  - The growing use of autonomous artificial intelligence agents in digital commerce creates new security concerns involving agent impersonation, unauthorized payments, compromised agents, and misuse of delegated authority. This research introduces the Autonomous Commerce Agent Guard…

- **[Recoverability and Verifier Strength: Two Measured Preconditions for Unattended Agent Self-Improvement](https://arxiv.org/abs/2610.27465v1)**
  - *De Wang, Peng Qi*
  - `2026-10-20`
  - Agent platforms are starting to improve their own agents: they read a deployed agent's execution traces, derive a change, have an automated verifier approve it, and release it with no human author. How much of this loop can safely run without a human? We propose two quantities a…

- **[The Data Differentiator Framework (DDF): Quantifying Marginal Data Value with Information-Theoretic and Game-Theoretic Measures in an Agentic Evaluation Pipeline (SDSAE)](https://arxiv.org/abs/2610.28933v1)**
  - *Sukesh Kumar, Dilip Singh*
  - `2026-10-20`
  - In data-rich enterprises the hard question is not whether a candidate dataset is good in isolation, but whether it adds information beyond what the organization already holds, and whether that increment is worth its price. We present the Data Differentiator Framework (DDF), a com…

- **[Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets](https://arxiv.org/abs/2610.28787v1)**
  - *Hieu Tran, Hong Yu*
  - `2026-10-20`
  - Evaluations of large language model (LLM) agents report that pricing agents collude at others' expense. Yet collusion is defined by enforcement: a cartel, in which competitors share monopoly profits, holds only if a member who cheats is punished. We introduce an audit that tests…

- **[From Outcomes to Steps: Reliable Success-Aware Critic Learning for Long-Horizon Language Agents](https://arxiv.org/abs/2610.27623v1)**
  - *Jiaxi Liu, Shixiong Kai, Zhentao Tang et al.*
  - `2026-10-20`
  - Reinforcement learning for long-horizon language agents requires identifying whether intermediate actions make eventual task success more or less likely when supervision is available only at trajectory level. The main difficulty is that a critic with aggregate return-prediction a…

- **[VisualEvolve: A Skill Self-Evolution Framework for Visual Reasoning](https://arxiv.org/abs/2610.28386v1)**
  - *Jiawei Wang, Yucun Li, Xueqi Li et al.*
  - `2026-10-20`
  - Visual tool use enables vision-language models (VLMs) to acquire task-relevant evidence, but its effectiveness can be limited by predefined visual operations and the tool-use strategies learned during training. Representing these operations and strategies as reusable external ski…

- **[When LLMs Manipulate: Measuring Behavioral, Social, and Temporal Effects](https://arxiv.org/abs/2610.27573v1)**
  - *Sadia Asif, Israel Antonio Rosales Laguan, Shumaila Asif et al.*
  - `2026-10-20`
  - Large language models (LLMs) can influence user trust and decision-making through subtle linguistic cues, yet the behavioral effects of manipulative outputs remain poorly quantified. We introduce a behavioral computing framework for measuring \textit{behavioral vulnerability}, de…

- **[Staged Continual Adaptation of Multimodal Foundation Models for Japanese Financial Documents](https://arxiv.org/abs/2610.27904v1)**
  - *Genshin Kakimoto, Atsushi Yanagisawa*
  - `2026-10-20`
  - Staged post-training of multimodal foundation models chains vision-language alignment, reasoning distillation, and domain tuning, yet how each phase trades capabilities against the others remains under-characterised. Tracking an 8.4B-parameter model from an un-fine-tuned baseline…

- **[GPU-Accelerated Construction of the Gabriel Graph: Parallelization Strategies and Applications to Large-Margin Classification and Graph-Based Clustering](https://arxiv.org/abs/2610.28759v1)**
  - *Diego Sanches Nere dos Santos, Luiz Carlos Bambirra Torres*
  - `2026-10-20`
  - The Gabriel graph is a proximity graph widely used in computational geometry and geometric machine learning, underlying large-margin classifiers and, as we show in this work, density-aware clustering methods. Its construction, however, has cubic time complexity $O(N^3)$ in the na…

- **[Understanding the Inner Workings of a State-Space Foundation Model for Limit Order Books](https://arxiv.org/abs/2610.28753v1)**
  - *Valentin Mohl, Alexandre Bismuth, Aramis Marti-Shahandeh et al.*
  - `2026-10-20`
  - Autoregressive foundation models offer state-of-the-art capabilities to simulate the market by generating the message flow of limit order books (LOBs). Yet, without understanding their inner workings, research directions are hard to narrow and practical use in real-world trading…

- **[Market Regime-Based Multi-Asset Portfolio Optimization Using Nested Clustered Optimization for Tactical Asset Allocation](https://arxiv.org/abs/2610.27751v1)**
  - *Supriadi, Bambang Siswoyo*
  - `2026-10-20`
  - We propose a regime-aware tactical asset allocation (TAA) framework integrating market regime detection with Nested Clustered Optimization (NCO) for multi-asset portfolio construction. The central hypothesis is that incorporating market regime information into the NCO pipeline, s…

- **[Arithmetic Models for Commodity Futures, Vanilla, and Calendar Spread Options](https://arxiv.org/abs/2610.28071v1)**
  - *Malthe Rauh Johansen, Nina Lange, David Skovmand*
  - `2026-10-20`
  - We develop an arithmetic multi-factor stochastic volatility model for commodity futures and options. The arithmetic specification yields a low-dimensional Markovian representation of the futures curve and semi-closed-form pricing formulas for vanilla and basket options, including…

- **[EGI-BENCH: An Enterprise General Intelligence Benchmark Suite](https://arxiv.org/abs/2610.27234v1)**
  - *Zhiwei Liu, Zhujun Lan, Jielin Qiu et al.*
  - `2026-10-19`
  - Enterprise adoption of LLMs in agentic workflows is gated by evaluations that span a wide arc of abilities: CRM operations, heterogeneous-document retrieval, personal data understanding, multi-turn planning, tool use, function calling, long-horizon research, and long-context soft…

- **[Magnolia: A Persistent-Memory Agent Framework for Computational Chemistry](https://arxiv.org/abs/2610.27230v1)**
  - *Tao Jiang, Benjamin Navet, Yousouf Taghzouti et al.*
  - `2026-10-19`
  - Chemistry has recently entered a high-data regime as molecular databases from high-throughput platforms or computational studies have become available. Increasing automation within the chemical sciences leads to a more digital and precision chemistry. Dedicated scientific agents…

- **[Physical AI: Concepts, Techniques, and Challenges](https://arxiv.org/abs/2610.27045v1)**
  - *Weinan Zhang, Chunhua Shen, Tianfan Xue et al.*
  - `2026-10-19`
  - In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry. However, the field has yet to reach consensus on its definition, technical landscape, and core challenges. To address this…

- **[Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams](https://arxiv.org/abs/2610.26781v1)**
  - *Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao et al.*
  - `2026-10-19`
  - Phone scams impose substantial and growing costs on individuals and financial systems worldwide, yet existing countermeasures impose no resource cost on perpetrators. Strategic scam-baiting, in which automated agents engage scammers to deplete their operational capacity, offers a…

- **[AllPath: Layered Verification for a Deployed, Self-Revising LLM Trading Agent under Human-Gated and Autonomous Regimes](https://arxiv.org/abs/2610.26662v1)**
  - *Tian Zhang, Meng Li*
  - `2026-10-19`
  - LLM trading agents are evaluated almost exclusively in backtests and autonomous benchmark harnesses. Deployment, where actions are irreversible, raises a different question: who verifies the agent's actions, and which failures can each verifier structurally catch? We report on Al…

- **[Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents](https://arxiv.org/abs/2610.26438v1)**
  - *Mengxiao Wang, Nitesh Saxena*
  - `2026-10-19`
  - Large language model (LLM) agents now trade real capital using news as evidence, yet they cannot reliably tell fabricated headlines from real news. Because they read the same feeds under near-identical policies, a single fabricated post can push them into the same trade at the sa…

- **[The Control Layer Behind Rule-Following Agents Trading Across Market Conditions](https://arxiv.org/abs/2610.26324v1)**
  - *Saad Naja, Nasser Odtallah, Jake Van-Praag et al.*
  - `2026-10-19`
  - Trading discipline often fails people. Our study tested whether four AI trading agents followed their strategies and risk rules. Offering traders the evidence and an agent evaluation toolkit to separate luck from following the rules, before giving agents meaningful autonomy or ca…

- **[Reliable Before Profitable: QuantHarness for Governing Financial Strategy Development with LLM Agents](https://arxiv.org/abs/2610.26101v1)**
  - *Jiasheng Mao, Jiacheng Liu, Hengwei Ye et al.*
  - `2026-10-19`
  - LLM agents can turn natural-language financial research requests into executable and backtested strategies, but a successful run may still implement the wrong rule, use information unavailable at decision time, or obscure how repairs and candidate selection changed the strategy.…

- **[Decision4Rec: A Jev-Inspired Framework of Decision Models on Knowledge and Active Graphs for Multi-Agent Recommender Systems](https://arxiv.org/abs/2610.26035v1)**
  - *Marco Polignano, Het Darshan Mehta, Pasquale Lops et al.*
  - `2026-10-19`
  - Decision models, such as the commercial Jev, are language models that return one probability for each option of a question instead of generating text. We present Decision4Rec, an open and modular framework that makes decision models useful for recommendation. A knowledge graph wr…

- **[AuDQ: Auditable Data Quality through Agentic Rule Discovery](https://arxiv.org/abs/2610.26031v1)**
  - *Jacopo Biggiogera, Nicolas Colombo, Krati Saxena et al.*
  - `2026-10-19`
  - High-stakes tabular pipelines rely on scattered, static quality checks that are hard to evolve and audit against policy intent. Regulated domains particularly suffer as the LLM-era automation raises expectations for traceability and accountability. We propose a vision for an onto…

- **[EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models](https://arxiv.org/abs/2610.25959v1)**
  - *X. Feng, J. Tang, Z. Lin et al.*
  - `2026-10-19`
  - Building embodied agents that can perceive, reason, and act across diverse 3D worlds is a central research direction toward artificial general intelligence. Yet most existing work remains confined to specific tasks in a single scene and transfers poorly to new environments, leavi…

- **[CXBench: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows](https://arxiv.org/abs/2610.25954v1)**
  - *Boxi Yu, Yuzhong Zhang, Zhenfeng Su et al.*
  - `2026-10-19`
  - Tool-using language agents increasingly perform regulated customer-service workflows, where a correct final state is insufficient: agents must also provide disclosures, obtain consent, and follow required procedures. Existing tool-agent benchmarks largely score final business sta…

- **[A Cue's Hidden Price: Auditing Seller Influence on AI Shoppers](https://arxiv.org/abs/2610.25843v1)**
  - *Felix Buecheler, Gerardo Berbeglia, Mingyu Guo*
  - `2026-10-19`
  - Large language models are increasingly asked to shop on a user's behalf, which lets seller-controlled content such as badges, endorsements, and framing steer what they recommend. That poses the question at the core of generative engine optimization (GEO): not whether seller conte…

- **[Weighted State Souping for Efficient Long-Context Retrieval](https://arxiv.org/abs/2610.25621v1)**
  - *William L. Tong, Aryo Lotfi, Emmanuel Abbe et al.*
  - `2026-10-19`
  - State space models (SSMs) combine fast inference and fixed state size with competitive language-modeling performance. Recently, state souping has been proposed as a procedure whereby an SSM independently encodes chunks of tokens like documents, tool definitions, or memory records…

- **[LOB-Impact Benchmark: Emergent Market Impact in Generative Limit Order Book Models](https://arxiv.org/abs/2610.27100v1)**
  - *George Nigmatulin, Valentin Mohl, Sascha Frey et al.*
  - `2026-10-19`
  - Realistic market impact is essential for generative limit order book (LOB) models to serve as world models for trading agents. If a simulator misprices this mechanism, agents learn policies that are optimal in the simulator but wrong in the real market. Existing metrics assess ge…

- **[Cooperative Multi-Agent Reinforcement Learning for Market Making on Prediction-Market Order Books](https://arxiv.org/abs/2610.26789v1)**
  - *Skander Lejmi*
  - `2026-10-19`
  - A market maker provides liquidity by quoting prices to buy and sell an asset, earning the spread while managing inventory risk. We study market makers trained with multi-agent reinforcement learning on prediction markets, specifically Polymarket, whose thin order books pose disti…

- **[Topological Sheaves of Irreducibility: A Theoretical Framework for Multi-Agent Task Obstructions](https://arxiv.org/abs/2610.26777v1)**
  - *Steven Motta, Davide Mambelli, Alessandro Rozza*
  - `2026-10-19`
  - Multi-agent systems can differ under identical agents and communication budgets when they support different forms of joint interaction. We introduce Topological Sheaves of Irreducibility (TSI), a sheaf-theoretic framework separating task-level compatibility obstructions from syst…

- **[FinHopper: A Progressive Multi-Hop Benchmark for Complex Financial Agents with Step-wise Evaluation](https://arxiv.org/abs/2610.26036v1)**
  - *Yuxuan Wu, Miaopei Lin, Qiufang Ying et al.*
  - `2026-10-19`
  - Financial agents are expected to answer factual investment queries through open search, but financial multi-hop retrieval differs from general multi-hop QA in a crucial way: each intermediate answer is an exact typed constraint, such as an entity, date, event, or numerical indica…

- **[ACE-Trader: Adversarial Co-Evolution for Generator-Critic Trading Systems](https://arxiv.org/abs/2610.25847v1)**
  - *Chang Zhou, Jiarun Zhou, Xingtong Yu et al.*
  - `2026-10-19`
  - Generator--critic trading systems pair an LLM-based trader that makes trading decisions with a red team agent that evaluates these decisions and provides feedback for revision. However, improving individual trading decisions does not ensure that both agents learn from experience…

- **[Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments](https://arxiv.org/abs/2610.25747v1)**
  - *JooKyung Yuh, Byungmin Park, Eunseo Choi et al.*
  - `2026-10-19`
  - Scientific model discovery requires proposing candidate models of an unknown system and designing experiments that discriminate among them. However, LLM-based approaches typically rely on in-context learning to predict outcomes and select experiments, lacking explicit model evalu…

- **[SWE-Residual: Evaluating Starting-State Robustness of Coding Agents](https://arxiv.org/abs/2610.25899v1)**
  - *Jinze Li, Weijie Liu, Jinfeng Xu et al.*
  - `2026-10-19`
  - Software engineering (SWE) benchmarks are the primary way to measure the capabilities of coding agents: an agent is placed in a code repository or machine environment, given a request, and judged by hidden tests. These benchmarks almost always start the agent from a clean state t…

- **[CARLAR Influence: A Structured Hallucination Risk in Multimodal Cheque Extraction and an Exploratory Compressed-Image Countermeasure](https://arxiv.org/abs/2610.27192v1)**
  - *Joong Ho, Choi, Aditya Paul et al.*
  - `2026-10-19`
  - Multimodal large language models (LLMs) are increasingly used for structured extraction from financial documents, but their behavior under visual ambiguity is poorly understood. We study CARLAR (Courtesy Amount Recognition and Legal Amount Recognition) influence: a model returns…

- **[Cross-Lingual Reusability of LLM Pipelines: Financial Extraction, Multilingual Reasoning, and Semantic Screening](https://arxiv.org/abs/2610.27043v1)**
  - *Joong Ho, Choi, Sherine George et al.*
  - `2026-10-19`
  - Financial institutions increasingly deploy large language models (LLMs) in multilingual markets, raising a practical question: can pipelines developed and validated in English be reused across languages, or must they be rebuilt per locale? We test cross-lingual reusability along…

- **[Toward Structured Financial Foundation Models](https://arxiv.org/abs/2610.26516v1)**
  - *Natraj Raman, Saumitra Mishra, Vamsi Potluru et al.*
  - `2026-10-19`
  - Foundation models promise reusable capabilities and step-change performance gains across tasks. In finance, large-scale pretraining of domain-specialized foundation models can advance both goals. However, prevailing architectures and objectives do not by themselves address the co…

- **[StrucChunk: Structure-Aware Retrieval for Legal Document RAG](https://arxiv.org/abs/2610.26313v1)**
  - *Surya Deep Singh, Ashutosh Tripathi, Gaurav Deep Singh*
  - `2026-10-19`
  - Retrieval-Augmented Generation (RAG) can ground LLM outputs in domain-specific knowledge, but legal documents are hard: standard chunking fragments hierarchical argument structure, and generic embeddings struggle with both precise citation matching and semantic understanding. We…

- **[FinSafeGuard: A Quality-Driven Synthetic Dataset for Financial AI Safety](https://arxiv.org/abs/2610.26066v1)**
  - *Joseph Thomas Thacil, Reetu Raj Harsh, Krati Saxena et al.*
  - `2026-10-19`
  - Generating high-quality synthetic datasets at scale remains a fundamental challenge for training specialized AI systems in data-scarce domains. We present a comprehensive methodology that produces 14.3 million quality-filtered synthetic training examples from a structured taxonom…

- **[A Calibrated Instrument for Detecting Disposition Drift in Language Models](https://arxiv.org/abs/2610.25735v1)**
  - *Jerry Kaplan*
  - `2026-10-19`
  - Before language models are released, they are tested for harmful traits such as willingness to carry out dangerous requests, deception, power seeking, and sycophancy. The safe behavior these tests certify may degrade as models are modified, by topical fine-tuning, new training da…

- **[RGH-GNN : Risk-Gated Heterogeneous Graph Neural Network for Financial Fraud Detection](https://arxiv.org/abs/2610.27107v1)**
  - *Mythreyee Hari, Subin Sahayam, Vegesna S M Srinivasavarma*
  - `2026-10-19`
  - Credit card fraud is a significant problem for financial institutions, resulting in substantial monetary loss each year. Fraud patterns and methods are continuously evolving, with fraudulent transactions often disguised to resemble legitimate activity. Real world transaction data…

- **[Teacher Supervision, Fixed Representations and Calibration: Exact Risk Calculations for Candidate-Scoring Decision Models](https://arxiv.org/abs/2610.26797v1)**
  - *Agus Sudjianto, Denis Burakov*
  - `2026-10-19`
  - Candidate-scoring decision models return a probability distribution over a presented set of answers. Public documentation of one such system, Jev, and of an open counterpart, JevAny, describes three training ingredients that determine what these probabilities estimate: soft targe…

- **[Typed Decision Models under Prevalence Shift: Decision Training, Calibration, and Implicit Priors](https://arxiv.org/abs/2610.26325v1)**
  - *Abdul Rahman Iqbal, Muhammad Fawad Nasim, Amir Saleem*
  - `2026-10-19`
  - Typed decision models (TDMs) return a probability over caller-defined options, and Jev is described by its vendor as calibrated. But in deployment class frequencies change, so calibration measured on a fixed test set need not hold where thresholds are applied. Existing evaluation…

- **[Evidence Sufficiency and Model Comparisons in MexRegQA: An Item-Level Audit of Mexican-Spanish Regulatory QA](https://arxiv.org/abs/2610.25710v1)**
  - *Fred Hu, Yeqi Wang, Xing Zhou*
  - `2026-10-19`
  - Similarity-gated coverage does not establish that retrieved evidence contains the facts needed to answer a question. We audit Mexican-Spanish financial-regulatory QA and find that 35 of 135 covered items lack some or all load-bearing facts. On the post-hoc full-evidence slice (n=…

- **[Topological Compression of Prediction Market Belief States for Event Forecasting](https://arxiv.org/abs/2610.25756v1)**
  - *Aadit Jerfy*
  - `2026-10-19`
  - Topological Data Analysis (TDA) and Persistent Homology (PH) have been utilized in numerous fields$-$from protein modeling to financial analysis$-$to understand the underlying structure of data. In this paper, we incorporate TDA and PH into forecasting models over a prediction ma…

- **[Fundamental Impossibility Results in AI Safety: Trading Off between Desiderata](https://arxiv.org/abs/2610.27373v1)**
  - *Ida Mattsson, Ratip Emin Berker, Emanuel Tewolde et al.*
  - `2026-10-19`
  - Is there a fundamental tradeoff between desiderata for safe AI systems, such as harmlessness and helpfulness? We answer by formalizing the interaction between AI systems and users as a game with three players: a defender and an attacker that are computationally or informationally…

- **[Next Best Action: Causal Constrained Offline RL for Business Action Targeting](https://arxiv.org/abs/2610.26817v1)**
  - *Surya Ramachandiran, Yiming Li, Juan Mancilla-Caceres et al.*
  - `2026-10-19`
  - Next Best Action (NBA) systems must select among customer interventions (e.g., discounts, promotions, and lifecycle actions), maximize long-term economic value, satisfy complex operational constraints, and remain causally grounded. Existing approaches lack a rigorous framework fo…

- **[Beyond Behavioral Accuracy: Evaluating Individual-Level Fidelity in LLM Investor Simulation](https://arxiv.org/abs/2610.26524v1)**
  - *Jiajie He, Yuanhong Jiang, Xintong Chen et al.*
  - `2026-10-19`
  - Large language models (LLMs) are increasingly used as user simulators, but can they faithfully reproduce an individual's behavior and decision logic over time? We investigate this question in a longitudinal paper-trading study with 80 participants. Using rolling next-day predicti…

- **[An Empirical Study of Parameter-Efficient Fine-Tuning for Mixture-of-Experts LLMs](https://arxiv.org/abs/2610.26370v1)**
  - *Minglei Li, Peng Ye, Haonan He et al.*
  - `2026-10-19`
  - Parameter-efficient fine-tuning (PEFT) methods are critical for adapting large models under resource-constrained settings. However, as mixture-of-experts (MoE) architectures, which offer efficient inference at massive parameter scales, gain increasing prevalence in the community,…

- **[CAST: Cast-Admissible Generative Design and Shape Optimization with Paired Depth Images](https://arxiv.org/abs/2610.26309v1)**
  - *Jihoon Kim, Yongmin Kwon, Namwoo Kang*
  - `2026-10-19`
  - Deep generative design can produce complex geometries, but unconstrained representations may create undercuts that prevent release from a two-part mold. We present CAST, which reformulates three-dimensional shape generation under a selected mold-opening constraint as a two-dimens…

- **[CorteXforge: Scenario-Based RF Dataset Generation on Real Testbeds](https://arxiv.org/abs/2610.26999v1)**
  - *Andréa Joly, Leonardo S Cardoso, Jean-Marie Gorce*
  - `2026-10-19`
  - Deep learning for radio frequency (RF) signal analysis relies on large annotated datasets, yet synthetic datasets trade physical realism for controllability, while uncontrolled over-theair measurements offer realism but limited reproducibility. We present CorteXforge, a scenario-…

- **[Adversarial Post-Training of Foundation Models for High-Frequency Trading](https://arxiv.org/abs/2610.25604v1)**
  - *Alexandre Bismuth, Kang Li, Aramis Marti-Shahandeh et al.*
  - `2026-10-19`
  - While autoregressive foundation models trained on limit order book (LOB) data show state-of-the-art performance for market simulation, pre-training with cross-entropy neither penalizes the compounding of sampling errors over free-running rollouts nor targets desired market proper…

- **[Amortized Neural Filtering for Calibrated Posteriors in Statistical Arbitrage](https://arxiv.org/abs/2610.25802v2)**
  - *Minkey Chang*
  - `2026-10-19`
  - Statistical arbitrage trades on an estimate of the state of a residual spread, and conventional practice discards the uncertainty of that estimate. We keep the uncertainty and use it in the trading decision. A Neural Filter Estimator (NFE) is trained on simulated paths of a mean-…

- **[Regime-Aware Interpretable Ranking for Sector Rotation](https://arxiv.org/abs/2610.26456v1)**
  - *Kelvin J. L. Koa, Ziling Liu, Xinyang Li et al.*
  - `2026-10-19`
  - Sector rotation is a common decision in benchmark-relative portfolio management, where portfolio managers rank sectors for overweight and underweight positions. We formulate this task as ranking sector actions by expected future risk-adjusted active performance, measured with for…


---
*Generated 2026-10-22 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
