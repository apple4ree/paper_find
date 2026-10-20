# Daily Paper Digest — 2026-10-20 (Tuesday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**430 unique papers** (543 topic-entries — cross-topic papers counted once per category)

---

## Agent  (290)

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


### KDD

- **[Bridging Concepts: Multi-Agent Reasoning over Scientific Concept Graphs for High-Impact Research Prediction](https://arxiv.org/abs/2610.25281v1)**
  - *Donggyu Yoon, Minsung Hwang, Juneha Baek et al.*
  - **KDD** · `2026-10-18`
  - Within a research community, new topics often emerge when previously unconnected concepts are first studied together. We construct scientific concept graphs (SCGs)--domain knowledge graphs whose nodes are fine-grained research concepts extracted from paper text by LLMs and whose…


### ACL

- **[Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models](https://arxiv.org/abs/2610.25659v1)**
  - *Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk et al.*
  - **ACL** · `2026-10-19`
  - Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized tes…

- **[PACT: Plan-Augmented Coordination via Trace-Graphs for Dynamic Multi-Agent Combinatorial Optimization](https://arxiv.org/abs/2610.26671v1)**
  - *Xiao Zhou, Alex Schutz, Victor-Alexandru Darvariu et al.*
  - **ACL** · `2026-10-19`
  - Multi-agent approaches have been investigated recently as a means of improving the scalability of reinforcement learning for neural combinatorial optimization. Existing methods assume that all problem instance information is known upfront. However, real-world problems are often d…

- **[Self-organizing reinforcement learning: a swarm approaches the explore-exploit optimum](https://arxiv.org/abs/2610.25113v1)**
  - *Galen J. Wilkerson*
  - **ACL** · `2026-10-18`
  - The explore/exploit trade-off is the core problem of reinforcement learning (RL). We show that a minimal foraging swarm approaches its optimum - the ideal-free / Nash allocation of a multi-agent resource-sharing game (an equilibrium, not a return maximum) - with no learner and no…

- **[CARVS: A Congestion-Aware Algorithm for Online Multi-Agent Pickup-and-Delivery in Human-Collaborative Warehouses](https://arxiv.org/abs/2610.24549v1)**
  - *Chaoran Li, Zeyuan Zhao, Shao Zhang*
  - **ACL** · `2026-10-17`
  - Intelligent warehouse systems have transformed logistics by integrating robots with minimal infrastructure changes, boosting efficiency and optimizing workflows compared to traditional human-only operations. However, human-robot collaboration introduces new challenges, particular…

- **[Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security](https://arxiv.org/abs/2610.24896v1)**
  - *Khushbu Pahwa, Yubin Ge, Daniele Bonadiman et al.*
  - **ACL** · `2026-10-17`
  - LLM code agents increasingly ship code with little oversight, yet defenders trained on static vulnerability datasets fall behind adapting adversaries. We co-train attacker and defender instead, and let execution decide every reward: an attacker (Red) edits a real repository and e…

- **[Do Conversational Agents Need Explicit Memory? A Controlled Comparison with Raw-History Retrieval](https://arxiv.org/abs/2610.24671v1)**
  - *Yongjie Zhou, Shuai Wang, Bevan Koopman et al.*
  - **ACL** · `2026-10-17`
  - Explicit memory systems transform conversation history into persistent representations intended to improve future access, often at substantial construction cost. Yet it remains unclear whether this added complexity yields better answer accuracy than retrieving directly from raw h…


### Other / arXiv

- **[MemT-1.0: Towards Memory-Native Evolution](https://arxiv.org/abs/2610.26825)**
  - *Zhiyu Li, Zeyu Zhang, Linyun Liu et al.*
  - 🤗 Featured · `2026-10-19`
  - Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of mod…

- **[OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory](https://arxiv.org/abs/2610.26860)**
  - *Yu Zhou, Cheng-Fu Yang, Rui Sun et al.*
  - 🤗 Featured · `2026-10-19`
  - Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base…

- **[AnyGoal: On World Model Generalization Beyond Expert Rollouts](https://arxiv.org/abs/2610.26844)**
  - *Heejeong Nam, Divyat Mahajan, Quentin Le Lidec et al.*
  - 🤗 Featured · `2026-10-19`
  - The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For these uses to be reliable, however, the learned dynamics must behave well beyond th…

- **[Manga2Animate: An Agentic Framework for Faithful Manga Animation with Script and Storyboard Planning](https://arxiv.org/abs/2610.26851)**
  - *Sheng-Wei Zhang, Hsi-An Chen, Yan-Ting Liou et al.*
  - 🤗 Featured · `2026-10-19`

- **[AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time Adaptation in Evolving Environments](https://arxiv.org/abs/2610.25950)**
  - *Rui Wang, Zishen Lai, Jiayu Liu et al.*
  - 🤗 Featured · `2026-10-19`
  - Large Language Model (LLM) agents are increasingly deployed in unfamiliar and evolving environments, requiring them to proactively explore, understand, and adapt to environmental dynamics. However, existing benchmarks rarely test whether agents can proactively discover how an env…

- **[Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy](https://arxiv.org/abs/2610.26848)**
  - *Zekai Li, Jiayi Yu, Jinlu Zhang et al.*
  - 🤗 Featured · `2026-10-19`
  - In this paper, we systematically investigate the mechanisms, scaling behavior, and generalization of physical Recursive self-improvement. We introduce PhysRSI-eval to quantify physical RSI through a five-axis metric: First-Attempt Performance, Efficiency, Success, Budget and Impr…

- **[HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs](https://arxiv.org/abs/2610.26770)**
  - *Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen et al.*
  - 🤗 Featured · `2026-10-19`
  - Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harn…

- **[Remembering Has a Price: Learning Memory Worth under Resource Constraints](https://arxiv.org/abs/2610.26453)**
  - *Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang et al.*
  - 🤗 Featured · `2026-10-19`
  - Lifelong agents continually accumulate and reuse experience to improve after deployment, yet in practice they often operate under tight generation, interaction, and memory budgets. Under such stringent joint constraints, we find that existing lifelong-memory methods can become in…

- **[CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents](https://arxiv.org/abs/2610.24960)**
  - *Zhongwei Xie, Yiming Du, Jiaxin Bai et al.*
  - 🤗 Featured · `2026-10-18`
  - AI coworkers must coordinate tools, communicate across turns, and act on changing workspace state while respecting workflow constraints. Constructing training experience for these capabilities requires coherent requests, service records, tool interfaces, and grading checks. We pr…

- **[HSPR: Recovering Software-Agent Benchmark Scores via Hierarchical Posterior Inference](https://arxiv.org/abs/2610.24611)**
  - *Wanyi Chen, Wanqin Shen, Yuanchen Shi et al.*
  - 🤗 Featured · `2026-10-17`
  - Evaluating software agents on a full benchmark is expensive. A small task subset can preserve agent rankings while yielding inaccurate scores. Historical responses provide useful structure, but tasks with identical source responses can have different outcomes for a new target age…

- **[OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners](https://arxiv.org/abs/2610.24087)**
  - *Peisong Wang, Feixue Liu, Yize Meng et al.*
  - 🤗 Featured · `2026-10-16`

- **[Self-Evolving Coding Agents via Harness-Policy Optimization](https://arxiv.org/abs/2610.22791)**
  - *Zhepei Wei, Wenlin Yao, Baolin Peng et al.*
  - 🤗 Featured · `2026-10-16`

- **[Interlock: From Local Correctness to Task Completion in Long-Horizon Agents](https://arxiv.org/abs/2610.19686)**
  - *Linji Hao, Yanji He, Zihan Wang et al.*
  - 🤗 Featured · `2026-10-14`

- **[BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References](https://arxiv.org/abs/2610.23986)**
  - *Xinyu Fang, Yuchi Wang, Weihao Yu et al.*
  - 🤗 Featured · `2026-10-14`

- **[Evidence-First Agentic Verification](https://arxiv.org/abs/2610.17724)**
  - *Reza Sanayei, Razvan-Gabriel Dumitru, Sunjie Hou et al.*
  - 🤗 Featured · `2026-10-13`

- **[MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents](https://arxiv.org/abs/2610.06830)**
  - *Haozhen Zhang, Haodong Yue, Quanyu Long et al.*
  - 🤗 Featured · `2026-10-05`

- **[Self-Evaluating Recursive Agents](https://arxiv.org/abs/2610.04902)**
  - *TianYi Lyu, Xiaozhe Li, Yang Li et al.*
  - 🤗 Featured · `2026-10-04`

- **[Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy](https://arxiv.org/abs/2610.26836)**
  - *Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu et al.*
  - 🤗 · `2026-10-19`
  - LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads on demand. We ask where this costs accuracy with a real scientific tool: PHREEQC…

- **[Agent World Model in the Wild: Computer-Use Agent Environment Synthesis](https://arxiv.org/abs/2610.26828)**
  - *Zhaoyang Wang, Qianhui Wu, Haorui Wang et al.*
  - 🤗 · `2026-10-19`
  - Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model…

- **[SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?](https://arxiv.org/abs/2610.26659)**
  - *Zhaoxi Zhang, Hao Liang, Linxuan Wu et al.*
  - 🤗 · `2026-10-19`
  - Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through a…

- **[The Control Layer Behind Rule-Following Agents Trading Across Market Conditions](https://arxiv.org/abs/2610.26324)**
  - *Saad Naja, Nasser Odtallah, Jake Van-Praag et al.*
  - 🤗 · `2026-10-19`
  - Trading discipline often fails people. Our study tested whether four AI trading agents followed their strategies and risk rules. Offering traders the evidence and an agent evaluation toolkit to separate luck from following the rules, before giving agents meaningful autonomy or ca…

- **[Focused Omni-Modal GUI Agents](https://arxiv.org/abs/2610.26203)**
  - *Fuyao Zhang, Wenwen He, Jiaming Zhang et al.*
  - 🤗 · `2026-10-19`

- **[ClueFlow: Learning Long-Horizon Search through Attributed Research-State Transitions](https://arxiv.org/abs/2610.25980)**
  - *Yicheng Wang, Wentao Tan, Yidan Huang et al.*
  - 🤗 · `2026-10-19`
  - Long-horizon search requires agents to acquire relevant evidence and integrate it into an evolving research state. Existing methods maintain research states to guide exploration or assign turn-level progress signals, yet grounding these signals in explicit, attributable state cha…

- **[MASIF: Implicit Failures for Process Observability in Multi-Agent Systems](https://arxiv.org/abs/2610.25852)**
  - *Yanwei Huang, Arpit Narechania, Atanu Sinha*
  - 🤗 · `2026-10-19`
  - Multi-agent systems (MAS) can complete a task despite local execution errors that are corrected, bypassed, or carried forward without individually determining its outcome. We call these implicit failures (IFs) and study them as signals for process observability beyond final task…

- **[CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting](https://arxiv.org/abs/2610.26852v1)**
  - *Zehao Wang, Jianpeng Yao, Yuping Wang et al.*
  - `2026-10-19`
  - Reinforcement learning enables mobile robots to make fast and scalable navigation decisions in constrained human-shared environments. However, directly extending single-robot approaches to multi-robot settings often fails to ensure safety and efficiency, especially under occlusio…

- **[WeAct: Dynamic Weight Switching as Agent Actions](https://arxiv.org/abs/2610.26847v1)**
  - *Rui Shi, Xunjian Yin, Jiacheng Sang et al.*
  - `2026-10-19`
  - Long-horizon agents must learn heterogeneous capabilities from interleaved trajectories. Updating shared parameters to learn new capabilities can degrade previously acquired ones, resulting in catastrophic forgetting. As a trajectory unfolds, different stages may require differen…

- **[Train An Imaginative Agent](https://arxiv.org/abs/2610.26845v1)**
  - *Jiaxin Ge, Junyi Zhang, Tianning Chai et al.*
  - `2026-10-19`
  - A seemingly reasonable push in Sokoban can make the puzzle unsolvable. To avoid such mistakes, an agent has to anticipate the consequences of its actions before execution, especially when feedback from the real environment is sparse or actions are irreversible. We introduce Agent…

- **[ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry](https://arxiv.org/abs/2610.26829v1)**
  - *Matt Turk, Brandon L. Neel, Diana M. Lopez et al.*
  - `2026-10-19`
  - Frontier agents retrieve structural metadata well and compute geometry from coordinates less reliably. We ask how much of a benchmark score reflects that gap and how much reflects the evaluation configuration around the model. We study ProteinGeoBench, a suite of 131 protein-stru…

- **[RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through Web Development](https://arxiv.org/abs/2610.26826v1)**
  - *Yuchi Wang, Rongyao Fang, Weihao Yu et al.*
  - `2026-10-19`
  - Beyond basic tool use and coding skills, effectively incorporating visual references into agentic generation is equally essential for applying AI agents to real-world productivity tasks. We study this crucial capability through webpage development, a practical and readily evaluab…

- **[Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams](https://arxiv.org/abs/2610.26781v1)**
  - *Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao et al.*
  - `2026-10-19`
  - Phone scams impose substantial and growing costs on individuals and financial systems worldwide, yet existing countermeasures impose no resource cost on perpetrators. Strategic scam-baiting, in which automated agents engage scammers to deplete their operational capacity, offers a…

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

- **[Revision-Based Learning from Interactive Experience and Feedback](https://arxiv.org/abs/2610.26636v1)**
  - *Jiawen Li, Chenming Ge, Alice Gao et al.*
  - `2026-10-19`
  - Code generation models are increasingly used to produce interactive artifacts, such as websites and user interfaces. Many properties that determine whether these interfaces are useful only become apparent through realistic interaction, making them difficult to incorporate into mo…

- **[When the harness decides success: state that cannot be re-observed](https://arxiv.org/abs/2610.26632v1)**
  - *Raimondas Lencevicius*
  - `2026-10-19`
  - Agent harnesses decide what a language model sees across turns: they drop old turns, summarize them, or replay the model's own earlier reasoning. We ask when these choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registe…

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

- **[VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement](https://arxiv.org/abs/2610.26342v1)**
  - *Ruotian Peng, Yuanyi Ren, Shuaiqi Liu et al.*
  - `2026-10-19`
  - Recursive self-improvement (RSI) requires agents to diagnose system bottlenecks and coordinate improvements across training and inference. We refer to the agents' capability to jointly optimize training data, the trainer, and the inference harness as cross-component co-design. We…

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

- **[Claim Laundering: When Agent Decision Models Trust Records Over Reality](https://arxiv.org/abs/2610.25947v1)**
  - *Tina Khezresmaeilzadeh, Seyedarmin Azizi, Erfan Baghaei Potraghloo et al.*
  - `2026-10-19`
  - Agent decision models select actions in a single forward pass from inputs that combine environmental observations with the agent's own record of previous actions. When an action fails silently, these sources can conflict: the record reports success, but the environment shows that…

- **[Policy Search in Code Space for Multi-Agent Pathfinding](https://arxiv.org/abs/2610.25946v1)**
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

- **[Secure Agentic Coding through Counterexample-Grounded Feedback](https://arxiv.org/abs/2610.25916v1)**
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

- **[Cooperative Multi-Agent Reinforcement Learning for Market Making on Prediction-Market Order Books](https://arxiv.org/abs/2610.26789v1)**
  - *Skander Lejmi*
  - `2026-10-19`
  - A market maker provides liquidity by quoting prices to buy and sell an asset, earning the spread while managing inventory risk. We study market makers trained with multi-agent reinforcement learning on prediction markets, specifically Polymarket, whose thin order books pose disti…

- **[Topological Sheaves of Irreducibility: A Theoretical Framework for Multi-Agent Task Obstructions](https://arxiv.org/abs/2610.26777v1)**
  - *Steven Motta, Davide Mambelli, Alessandro Rozza*
  - `2026-10-19`
  - Multi-agent systems can differ under identical agents and communication budgets when they support different forms of joint interaction. We introduce Topological Sheaves of Irreducibility (TSI), a sheaf-theoretic framework separating task-level compatibility obstructions from syst…

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

- **[Zephyrus-R1: Agentic Reinforcement Learning for Weather Reporting](https://arxiv.org/abs/2610.25625v1)**
  - *Fengfei Yu, Marshall Fisher, Isadora White et al.*
  - `2026-10-19`
  - Reinforcement learning (RL) has emerged as a key method for training AI models in scientific applications, but RL remains difficult when outputs cannot easily be verified against a known ground-truth answer. Natural-language weather forecast reports are one such domain: they tran…

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

- **[Design and Cross-Domain Evaluation of an Agent Execution Harness](https://arxiv.org/abs/2610.25568v1)**
  - *Saurav Joshi, Manas Gupta, Ashwin Venkatesh Raman et al.*
  - `2026-10-18`
  - Completing complex tasks with language-model agents requires coordinating planning, execution, and review so the final result addresses the user's original objective. We present an agent execution harness that keeps the original objective separate from a revisable plan and an exe…

- **[Learning Which Device to Call: Online Tool Grounding for LLM Agents in IoT](https://arxiv.org/abs/2610.25563v1)**
  - *Yichen Liu, Xiaochong Jiang, Haoran Yu et al.*
  - `2026-10-18`
  - The Internet of Things (IoT) gives large language model (LLM) agents access to physical observations, but one requested capability is usually offered by several devices, and the agent's plan does not say which one to call. Existing work retrieves relevant tools and checks plan fe…

- **[Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors](https://arxiv.org/abs/2610.25552v1)**
  - *Jinu Lee, Shraddha Barke*
  - `2026-10-18`
  - Symbolic constraints (programmatic, deterministic checks for tool calls) enable deterministic verification of LLM agents' tool calls, but existing approaches primarily enforce predefined safety policies rather than tool dependencies in complex tool environments. We explore whethe…

- **[Editing as Language: Teaching LLM Agents a Grammar for Native Context Editing](https://arxiv.org/abs/2610.25550v1)**
  - *Yunlong Deng, Yan Li, Xing Hu et al.*
  - `2026-10-18`
  - A synopsis in novels folds a story into a few lines; a function in code gathers many steps with a single execution. Context editing is native to language itself. In this paper, we propose the Native Context Editing (NCE) framework, which gives language model agents a grammar for…

- **[Auditing Tool Traces in Agentic LLMs: Source Localization and Counterfactual Dependence Testing](https://arxiv.org/abs/2610.25540v1)**
  - *Junhao Liu, Tianxiao Li, Yongxian Wu et al.*
  - `2026-10-18`
  - Agentic LLMs increasingly support scientific prediction by grounding decisions in external evidence. In biology, they promise accurate, interpretable predictions for important problems by integrating complex experimental and computational evidence. However, serialized tool result…

- **[StopLoss: Teaching Agents to Predict Failure and Stop Early](https://arxiv.org/abs/2610.25525v1)**
  - *Jiarong Liang, Xueguang Ma, Dongfu Jiang et al.*
  - `2026-10-18`
  - Coding agents keep working on runs that will fail verification, and asking a frontier model to watch for this is expensive in its own right. We introduce StopLoss, a small external monitor that learns failure recognition from completed trajectories and their verifier outcomes. Th…

- **[Bud ContextCompact 2.0: Context Compaction for Agent Success and Accuracy with Small Language Models and Constrained Context Windows](https://arxiv.org/abs/2610.25516v1)**
  - *Jithin VG, Ditto PS*
  - `2026-10-18`
  - Agents that work for many turns outgrow the context window of the model that serves them, and on small language models (SLMs) and constrained inference systems that window is small. Context compaction replaces older turns with a summary so a session can continue, but it is lossy,…

- **[System X: An LLM Decision Model That Replies from Its Own KV Cache](https://arxiv.org/abs/2610.25456v1)**
  - *Syed Usama Khalid Bukhari, Syed Safwan Khalid, Muhammad Aamir*
  - `2026-10-18`
  - Decision models return probabilities over supplied options, but a deployed agent may also need to reply in words. The present study introduces System X, a large language model (LLM) decision model that adds a text-reply option to the LLM-as-Jev readout. When this option wins, or…

- **[Outcome-Anchored Credit Reallocation for Agentic Knowledge Graph Question Answering](https://arxiv.org/abs/2610.25384v1)**
  - *Mingyuan Li, Yucheng Li, Xiaxia Wang et al.*
  - `2026-10-18`
  - Agentic knowledge graph question answering (KGQA) requires large language models (LLMs) to solve complex questions through multi-turn interactions with a knowledge graph (KG). Outcome-supervised reinforcement learning derives verifiable outcome rewards from final answers but unif…

- **[MemDerive: A Diagnostic Benchmark for Agent Memory over Evolving Data](https://arxiv.org/abs/2610.25373v1)**
  - *Sen Gao, Yongan Li, Han Chen et al.*
  - `2026-10-18`
  - Long-running agents rely on memory of their past interactions for task state, such as what has been completed and which conditions still hold. Such state is usually a derived state. No record states it, and it must be computed by rules from multiple records of an evolving history…

- **[Formally Verified Autoresearch for Analyzing the Expressivity of Multi-Head Attention](https://arxiv.org/abs/2610.25341v1)**
  - *Karthik Viswanathan, Plamen Dimitrov, Stefano Rocca et al.*
  - `2026-10-18`
  - Multi-head attention is a central component of the transformer architecture, yet how its expressivity depends on the number of heads remains poorly understood. We study a one-layer, attention-only transformer with additive positional embeddings and define the head complexity $H^\…

- **[EG-GRPO: Evidence-Guided Step-level Credit Assignment for Deep Search Agents](https://arxiv.org/abs/2610.25269v1)**
  - *Sijia Luo, Mengjie Gao, Yuxiao He et al.*
  - `2026-10-18`
  - LLM-based search agents demonstrate strong capabilities in long-horizon information seeking and reasoning, typically trained via reinforcement learning. However, existing approaches predominantly rely on trajectory-level outcome rewards, providing limited supervision for complex…

- **[BatchParScale: Sparse Batch-Mixing for Sequence Models](https://arxiv.org/abs/2610.25254v1)**
  - *Hans Peter Lyngsøe Raaschou-jensen, M. Onurcan Kaya, Desmond Elliott*
  - `2026-10-18`
  - Recent test-time scaling methods improve model performance by increasing inference-time compute. One practical form of this is parallel scaling, where a model samples multiple independent reasoning streams and aggregates their answers using methods like voting, reranking, or veri…

- **[Assessing the Empirical Evidence for Loss of Control from Agentic General-Purpose AI](https://arxiv.org/abs/2610.25241v1)**
  - *Risto Uuk, Santeri Koivula, Lorenzo Pacchiardi et al.*
  - `2026-10-18`
  - Theoretical literature warns that advanced generalist agentic systems might pursue instrumental goals that are misaligned with human preferences, thus posing risks of irreversible loss of human control. The EU's Code of Practice for General-Purpose AI lists loss of control as a s…

- **[NeuroAct: Advancing EEG Analysis and Decoding via Dual-Loop Autonomous Research](https://arxiv.org/abs/2610.25211v1)**
  - *Wei Xiong, Jiangtong Li, Han Zhao et al.*
  - `2026-10-18`
  - EEG analysis and decoding underpin brain-computer interfaces, cognitive assessment, and sleep monitoring. Fixed pipelines and reward-driven search do not explicitly determine how signal structure, representations, predictor behavior, and training dynamics contribute to performanc…

- **[BrandEval: A Two-Track Multi-Agent Benchmark for Risk-Sensitive LLM Crisis Communication](https://arxiv.org/abs/2610.25208v1)**
  - *Haotian Gan, Weidong Tang, Hanbin Sun et al.*
  - `2026-10-18`
  - Evaluating LLMs for crisis communication requires more than judging isolated responses, because public feedback and competitor actions can reshape trust over time. Existing benchmarks remain largely static and single-turn, offering limited evidence about long-horizon risk-sensiti…

- **[Dialogue Generation for Conversational Recommendation Using User Search Interactions and Knowledge Graphs](https://arxiv.org/abs/2610.25182v1)**
  - *Minsung Hwang, Donggyu Yoon, Gowoon Hwang et al.*
  - `2026-10-18`
  - Large-scale conversational recommendation datasets typically require manual dialogue construction or annotation. We propose SearCl, which automatically generates conversational recommendation dialogues grounded in user search and click behaviors. SearCl segments user interactions…

- **[Memory, Know Your PLACE: Governing Lifecycle State and Query-Time Eligibility in Persistent-Memory Agents](https://arxiv.org/abs/2610.25179v1)**
  - *Chen-Fang Hu, Hong-Han Shuai, Woan-Shiuan Chien*
  - `2026-10-18`
  - Persistent memory turns prior interactions into durable agent state, but existing systems provide limited control over whether that state remains valid and whether it should influence a later query. We argue that reliable memory requires governance over both state formation and q…

- **[Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds](https://arxiv.org/abs/2610.25114v1)**
  - *Jingwen Bai, Guochao Bai, Canbo Zhang et al.*
  - `2026-10-18`
  - Embodied AI lacks the data-rich pretraining that gave language models their agents and skills, so new manipulation capability costs demonstrations per task or a frontier model in every episode. We study a third route: a strong general model acts only as an offline author that wri…

- **[Explore or Confirm? LLM Agents Misallocate Measurements Under Noise](https://arxiv.org/abs/2610.25111v1)**
  - *Abdul Karim, Matt Keon*
  - `2026-10-18`
  - As model reasoning gets cheaper, the physical experiment becomes the slow and costly step in discovery. Each experiment returns a noisy reading: a high value can mean a good candidate or a lucky draw. With a fixed budget, an AI agent must keep choosing between exploring a new can…

- **[Pre-Query Retention with Bounded Bit and Word Retrieval](https://arxiv.org/abs/2610.25098v1)**
  - *Pranav Singh, Prashant Singh*
  - `2026-10-18`
  - An agent can retain information before receiving a future question and later retrieve evidence from an archive. Evaluating this arrangement requires accounting for both retained information and the width of each retrieval response. Decision-tree capacity bounds describe individua…

- **[Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources](https://arxiv.org/abs/2610.25096v1)**
  - *Jeonghwan Choi, Jibin Hwang, Hayoon Park et al.*
  - `2026-10-18`
  - Enterprise retail workflows require agents to chain evidence across heterogeneous sources, from structured product and order records to unstructured inquiries and reviews, yet existing agentic RAG benchmarks rarely capture this challenge. To enable controlled evaluation of such w…

- **[DAGLoop: Aligning Method Design with Experimental Feedback in Automated AI Research](https://arxiv.org/abs/2610.25089v1)**
  - *Dengyuxing Wang, Yonggang Zhang, Qianshu Cai et al.*
  - `2026-10-18`
  - Automated AI research agents aim to improve machine learning methods by iteratively proposing, implementing, and evaluating candidate methods. Existing work uses the outcome of each evaluation to determine how the next candidate should be revised for performance improvement. Howe…

- **[Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks](https://arxiv.org/abs/2610.25069v1)**
  - *Shenqi Zhou, Qiran Zou, Wenhao Zhao et al.*
  - `2026-10-18`
  - Autonomous agents are increasingly capable of developing machine learning (ML) models end to end. In medical practice, however, strong performance on the target metric does not fully characterize how good the models are in real-world use cases. For example, medical ML models shou…

- **[One Skill Takes Over: Clashing Agent Skills and a One-File Fix](https://arxiv.org/abs/2610.25064v1)**
  - *Parsa Razmara, Seyedarmin Azizi, Ardalan Aryashad*
  - `2026-10-18`
  - Agent Skills are instruction files that tell a coding agent how to do one job. Users install skills from many authors, so two skills for the same job can be active at the same time. We ask what a model does when both skill files are in its context: does it combine their compatibl…

- **[LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica](https://arxiv.org/abs/2610.25019v1)**
  - *Jörg Frochte, Herbert Schmidt*
  - `2026-10-18`
  - To procure a model of a device, a client hands a supplier a description, sometimes with recorded data or a target response, and accepts the model against this handover. We let LLM coding agents act as the supplier on handovers with data, building Modelica models from library comp…

- **[IECLA: Interpretable Emotion Contribution Learning for Affective Image Editing](https://arxiv.org/abs/2610.25015v1)**
  - *Yijie Guo, Dexiang Hong, Weidong Chen et al.*
  - `2026-10-18`
  - Affective image editing (AIE) aims to evoke a target emotion while preserving the content and structure of a source image. Existing methods improve emotional expression or visual fidelity, but the target emotion alone does not reveal which source regions should be changed and whi…

- **[CorrectRTL: Boost RTL Generation Quality Through Automated Self-Correction with Instruction Decomposition](https://arxiv.org/abs/2610.24977v1)**
  - *Jing Wang, Shang Liu, Hangan Zhou et al.*
  - `2026-10-18`
  - Large language models (LLMs) have shown strong promise in specification-to-RTL generation. Among the explorations, the self-correction paradigm has significantly advanced LLM-based RTL generation. However, two challenges limit further progress. Existing benchmarks are saturated b…

- **[MemPrice: Online Memory Allocation via Adaptive Pricing for Long-Horizon Agents](https://arxiv.org/abs/2610.24955v1)**
  - *Yiming Zong, Shiyuan Piao, Jiashuo Jiang et al.*
  - `2026-10-18`
  - Long-horizon LLM agents face a fundamental allocation problem as interaction histories grow: which information to retain, how much context to devote to it, and at what granularity. Existing memory mechanisms largely focus on relevance, retrieval, or compression, leaving this allo…

- **[Epi: Towards a Persistent, Self-Improving Agent for Autonomous Research](https://arxiv.org/abs/2610.24944v1)**
  - *Yue Huang, Zhangchen Xu, Xiaonan Luo et al.*
  - `2026-10-18`
  - We present Épi, an autonomous research agent that sustains investigations across model sessions and evolves its methods through accumulated experience. Épi combines persistent research history, hierarchical memory, branching and independent review to maintain research continuity,…

- **[TrustAgent-RFF: Agentic Diagnostic Planning for Reliable RF Fingerprinting under Domain Shift](https://arxiv.org/abs/2610.24930v1)**
  - *Chuan Liu, Tianya Zhao, Xuyu Wang*
  - `2026-10-18`
  - Radio frequency fingerprinting (RFF) models can achieve accuracy under source domain conditions but become unreliable when the receiver, distance, collection day, or environment changes. Incorrect predictions in unseen domains may receive high softmax confidence, making confidenc…

- **[What Can't Jev Decide? Probing the Limits of One-Pass Decision Models](https://arxiv.org/abs/2610.24929v1)**
  - *Wang Yang, Xinpeng Li, Yanyan Zhang et al.*
  - `2026-10-18`
  - Jev and its open replicas choose among the options a caller supplies with a single forward pass, fast enough to decide inside an agent loop. We ask what such a model cannot decide, and find a simple limit: Jev cannot make a decision that an LLM makes only by writing out intermedi…

- **[Reinforcement learning on the EPRI AI-ccelerating Unit Commitment benchmark: diagnosing over-commitment and guiding MILP with learned policies](https://arxiv.org/abs/2610.25544v1)**
  - *Maharani Devira Pramita, Aidan O'Sullivan*
  - `2026-10-18`
  - Reinforcement learning (RL) is increasingly proposed as a fast solver for unit commitment (UC), but standalone agents remain far more expensive than mixed-integer linear programming (MILP). In the first study of RL on the 51-generator, 72-hour benchmark of the Electric Power Rese…

- **[Mining the Self-Rewriting System: A Vision for Data Mining on AI-Native Infrastructure](https://arxiv.org/abs/2610.25374v1)**
  - *Mayank Darbari, Chiman Salavati, Liang Wu et al.*
  - `2026-10-18`
  - Classical data mining treats data as generated outside the learner. Emerging AI-native infrastructure invalidates this assumption: as agents observe system state, act, update retrieval stores and models, and promote new artifacts into the serving path, their own decisions reshape…

- **[Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence](https://arxiv.org/abs/2610.25360v1)**
  - *One Octadion, Firmansyah Sundana, Novanto Yudistira*
  - `2026-10-18`
  - World models are increasingly judged by how well they rank plausible futures, yet plausibility alone is the wrong target. The same scene can evolve under many latent rules, and a future that is smooth and physically valid under one rule can be incoherent under the rule actually i…

- **[Indistinguishable Agents: Training Agent Privacy as Twin-World Indistinguishability](https://arxiv.org/abs/2610.25161v1)**
  - *Jiaming He, Guanyu Hou, Yi Yu et al.*
  - `2026-10-18`
  - LLM agents search, shop and send messages for their users, and every action is seen by some party. Existing privacy training rewards agents for not mentioning protected items, yet an observer can infer a private fact from what the agent does. Since an observer learns a fact only…

- **[Trackable Skill Library Lifecycle Management for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.25126v1)**
  - *Xi Zhu, Yuanlin Duan, Changyi Yang et al.*
  - `2026-10-18`
  - Skill-augmented agentic RL has emerged as an effective approach to improving LLM agents on long-horizon tasks. Despite this progress, individual skills may follow distinct trajectories as the policy evolves, with some becoming redundant after the model internalizes their capabili…

- **[Memory as Belief: Bayesian Evolution of Memory for Self-Evolving LLM Agents](https://arxiv.org/abs/2610.25119v1)**
  - *Yiming Xu, Qian Yang, Zihan Chen et al.*
  - `2026-10-18`
  - Large language model (LLM) agents increasingly rely on external memory to accumulate past experiences for continual adaptation. However, effectively reusing memory requires accurately assessing its value, as retrieved experiences may become unreliable when transferred across task…

- **[CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?](https://arxiv.org/abs/2610.25078v1)**
  - *Jiaqi Su, Guibin Zhang, Jie-Jing Shao et al.*
  - `2026-10-18`
  - Model--harness co-evolution has emerged as a prominent paradigm for recursive self-improving (RSI) agents, jointly evolving their execution scaffolds and intrinsic capabilities. We study the persistent yet often overlooked brain--body mismatch problem in this paradigm, where an e…

- **[Beyond the Teacher: Understanding and Preserving Distillation Overshoot in Agentic On-Policy Distillation](https://arxiv.org/abs/2610.25034v1)**
  - *Jike Zhong, Ming Li, Yuxiang Lai et al.*
  - `2026-10-18`
  - On-policy distillation (OPD) trains agents on their own trajectories using supervision from a stronger teacher. We uncover a counterintuitive phenomenon in multi-turn agentic tasks: a smaller, initially weaker student can substantially outperform its teacher during training, only…

- **[Decentralized Online Exp-Concave Optimization](https://arxiv.org/abs/2610.25017v1)**
  - *Hao Qiu, Mengxiao Zhang, Yuanyu Wan*
  - `2026-10-18`
  - Decentralized Online Convex Optimization (D-OCO) is a fundamental framework in which a set of local agents aims to minimize a sequence of global loss functions using only local computations and communications. While recent work has established near-optimal regret guarantees for c…

- **[Conjugate Compilation: Self-Improving Agentic Co-Compilation for Speculative Decoding](https://arxiv.org/abs/2610.25012v1)**
  - *Annabelle Sujun Tang, Rohan Mahapatra, Christopher Priebe et al.*
  - `2026-10-18`
  - As LLM adoption surges, scaling model serving requires unlocking stranded GPU capacity alongside deploying more GPUs. Speculative decoding brings two models into the serving process: a small draft model proposes tokens that a larger target model verifies. Yet compiling these mode…

- **[SoK: PIAtlas: Decomposing the Unbounded Prompt Injection Attack Space](https://arxiv.org/abs/2610.24999v1)**
  - *Stavros Damianakis, Konstantinos Psounis*
  - `2026-10-18`
  - Prompt injection is the dominant security risk for large-language-model (LLM) applications and agents, yet the field still lacks a coherent map of how these attacks are constructed. More than twenty public datasets describe prompt injection using incompatible vocabularies, often…

- **[Over-Defense in Coding Agents Begins at Silent Forks](https://arxiv.org/abs/2610.24949v1)**
  - *Hanjun Luo, Xuecheng Liu, Xiucheng Zhang et al.*
  - `2026-10-18`
  - Language models behind coding agents are post-trained with outcome rewards, and recent methods concentrate credit on the turns that decide the outcome. We find that defensive actions beyond what a task requires escape both. They begin at silent forks, the turns where every next a…

- **[Quality-Controlled Reply and Summary Data for Post-Training Small Language Models in AI Call-Screening Agents](https://arxiv.org/abs/2610.25458v1)**
  - *Jiaqi Gan, Tsang Ng, Ankit Raj et al.*
  - `2026-10-18`
  - Small language models have improved to the point where a phone can plausibly screen its own calls, answering on an absent owner's behalf without sending call content off the device, a privacy-respecting alternative to cloud call handling. Realizing that promise takes a model that…

- **[MemBubble: Benchmarking How Agent Memory Shapes LLM Response Diversity](https://arxiv.org/abs/2610.25127v1)**
  - *Jiajun Tan, Fei Sun, Xinyu Ma et al.*
  - `2026-10-18`
  - Memory serves as the core component of LLM-based agents, enabling personalized responses via extracting and using user preferences from past interactions. However, its use may reduce response diversity, thereby narrowing the range of information available to users. Existing evalu…

- **[Memories That Outlive Their Reasons: Dependency-Tethered Memory for Tool-Using LLM Agents](https://arxiv.org/abs/2610.25123v1)**
  - *Yiqi Wang, Jinqian Ju, Jiaqi Zhang et al.*
  - `2026-10-18`
  - Agents now act on the Web, publishing packages, models and datasets through registry APIs, and remembering past verifications spares them the work. But a verdict rests on premises. When a signing key is revoked, everything built on it stops passing, yet the advisory names only th…

- **[P2N: Reusing Deep Representations for Greater Effective Depth](https://arxiv.org/abs/2610.25076v1)**
  - *Yiqin Hao, Boyi Zeng, Zitong Wang et al.*
  - `2026-10-18`
  - Mathematical problem solving and autonomous agents are increasingly important applications of language models, demanding stronger reasoning capabilities. Computational depth is a key resource for such reasoning, but adding model layers increases both training and inference costs,…

- **[How Far Can an Agent Push? Trust-Safety Margins in Live Language-Based Economic Games](https://arxiv.org/abs/2610.25508v1)**
  - *Dima Galat, Marian-Andrei Rizoiu*
  - `2026-10-18`
  - The previous version contained Unicode em dashes. Paste this ASCII-only version:   Game theory identifies when a strategic action should be accepted, but not how long a live, language-based counterpart will continue to accept it. We entered the GLEE competition in its final week…

- **[Same Data, Different Bytes: Serialization-Invariant Integrity Checks for Agent-Published Datasets](https://arxiv.org/abs/2610.24916v1)**
  - *Jin Gao, Maura Clark*
  - `2026-10-17`
  - Agent networks require reliable ways for requesting agents to verify where data is located, how it can be accessed, and whether the data received matches what the data owner made available. Checksum mismatches can reflect either altered content or serialization differences that p…

- **[Arctic-SWE: Revisiting the Long Horizon Agent Training by Modeling-System Co-Design](https://arxiv.org/abs/2610.24914v1)**
  - *Boyi Liu, Yite Wang, Xinyu Lian et al.*
  - `2026-10-17`
  - Long-horizon agent training, including software engineering, is advancing rapidly, but the recipe and infrastructure needed for a strong reinforcement-learning baseline remain difficult to reproduce. This makes gains from new algorithms or data hard to distinguish from improvemen…

- **[HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents](https://arxiv.org/abs/2610.24899v1)**
  - *Soyoung Yoon, Peiran Xu, Han Wang et al.*
  - `2026-10-17`
  - While LLM agents are increasingly capable of gathering and synthesizing evidence from a single homogeneous source, such as structured tables or unstructured data, real-world analytical questions frequently span heterogeneous sources. For example, answering one enterprise question…

- **[The One-Pixel of Reasoning: One Truthful Relation Is Enough to Mislead LLM Agents](https://arxiv.org/abs/2610.24873v1)**
  - *Jinwei Hu, Youcheng Sun, Yi Dong et al.*
  - `2026-10-17`
  - Can one sentence manipulate an agent's belief by targeting a single implicit warrant linking evidence to a conclusion? In this paper, we introduce the one-relation attack (ORA), a novel cognitive attack on this inferential relation. ORA localizes a critical implicit warrant and p…

- **[Bellman Language Models: Solving the Recurring Decisions of LLM Agents](https://arxiv.org/abs/2610.24871v1)**
  - *Adarsh Vatsa, William Eiers*
  - `2026-10-17`
  - A general observation in agentic workflows, especially bounded ones, is that the decision space of the LLM, when we separate a decision from generation, starts approaching saturation: the agent meets the same states again and again, and after enough conversations it stops meeting…

- **[Teaching Code Agents to Ask Without Leaking Private Code](https://arxiv.org/abs/2610.24824v1)**
  - *Wenjia Jiang, Jieke Shi, Zhensu Sun et al.*
  - `2026-10-17`
  - Local coding agents can extend their reach by consulting a stronger cloud model. Such consultations, however, often expose the repository's private identifiers, file paths, and source code. Host-side masking hides recognized identifiers but leaves the surrounding code and the age…

- **[Pair-Aware Optimization: Coordinating Exploration and Refinement for Jailbreaking LLM Agents](https://arxiv.org/abs/2610.24823v1)**
  - *Juanyang Xu, Zheng Wang, Xingyu Zhao et al.*
  - `2026-10-17`
  - Large Language Model (LLM) agents are vulnerable to adversarial inputs that induce attacker-specified malicious behaviors, commonly referred to as jailbreaking. Existing optimization-based jailbreak attacks primarily employ first-order (FO) methods that leverage gradient informat…

- **[Cooperation Without Shared Rewards via Reciprocal Q-Augmentation](https://arxiv.org/abs/2610.24793v1)**
  - *Francesco Morri, Adel Abusitta, Quentin Cappart et al.*
  - `2026-10-17`
  - General-sum games are more challenging than fully cooperative or adversarial settings because agents may deceive or exploit one another. Achieving high social welfare requires sustained cooperation, while a single defection can drive agents toward a welfare suboptimal Nash equili…

- **[When LLM-Generated Refactorings Ripple: An Empirical Study of Repository Adoption Readiness](https://arxiv.org/abs/2610.24790v1)**
  - *Muhammad Waseem, Aakash Ahmad, Pekka Abrahamsson*
  - `2026-10-17`
  - Large Language Models (LLMs) are increasingly used to refactor source files, but file-local evaluations do not reveal changes to contracts, dependencies, or caller assumptions affecting repository adoption. To address this gap, we conduct 1,500 generation attempts across 150 prod…

- **[DialogMem: Evaluating Dialogue-Grounded Embodied Memory in 3D Environments](https://arxiv.org/abs/2610.24767v1)**
  - *SeongJun Jeong, Junghyun Kim, Gi-Cheon Kang et al.*
  - `2026-10-17`
  - Embodied agents in human-centered environments require memory that integrates what they observe with what humans tell them over time. However, existing embodied memories are built primarily from visual experience, leaving open how dialogue with humans can be grounded in the objec…

- **[ReTRACE: Feedback-Guided LLM Agent in a Chemistry Harness for Retrosynthesis Planning](https://arxiv.org/abs/2610.24744v1)**
  - *Jinxiang Xie, Yijian Zhang, Qingyuan Yi et al.*
  - `2026-10-17`
  - Computer-aided retrosynthesis has advanced through single-step prediction, tree search and route scoring, but complex targets still require judgement over the whole route, where stereochemistry, functional-group compatibility, cost and greenness interact. Here we present \textbf{…

- **[Can LLM Agents Resolve Service Failures? Simulating Multi-Turn Complaint Handling under Information Asymmetry](https://arxiv.org/abs/2610.24733v1)**
  - *Wailing Ng, Mengze Hong, Chen Jason Zhang et al.*
  - `2026-10-17`
  - LLM agents are widely adopted in service chatbots for rule-guided support and information access, yet emotionally demanding complaint handling still relies heavily on human agents. We introduce ServiceBench, to our knowledge the first benchmark dedicated to complaint handling, wi…

- **[Where Natural Language Ends in Agents: Executable Skill Composition with MetaSkill](https://arxiv.org/abs/2610.24723v1)**
  - *Meng Shu, Wei He, Hang Zhou et al.*
  - `2026-10-17`
  - Agent Skills express open-ended task knowledge in natural language, but composing them requires persistent execution order and upstream-output handoffs. We propose selective formalization at Skill boundaries: coordination relations with stable references and machine-checkable con…

- **[Neuro-Inspired Inhibitory Message Passing for Accurate and Token-Efficient Multi-Agent Reasoning](https://arxiv.org/abs/2610.24718v1)**
  - *Nima H. Siboni, Magdalena Springer, Vahid Rostami*
  - `2026-10-17`
  - Multi-agent systems promise to solve problems by bringing together information beyond the reach of any individual agent. Retrieval and tool use can distribute this information across agents, making communication essential to collaboration. A central challenge is keeping crucial e…

- **[DiffuPlan: Editable Planning State for Diffusion Language Model Agents](https://arxiv.org/abs/2610.24717v1)**
  - *Qisheng Zhou, Zhen Xiong, Qiaoyu Tan*
  - `2026-10-17`
  - Diffusion language models (dLLMs) are emerging as an alternative to autoregressive (AR) language models, yet dLLM agents largely inherit an interaction protocol designed for AR generation: once intermediate state is written, later observations can only be incorporated by appendin…

- **[Can AI agents make law? Evaluating AI legal relevance and creativity](https://arxiv.org/abs/2610.24661v1)**
  - *Benjamin Ricaud, Artem Galushko*
  - `2026-10-17`
  - Large language models, the artificial intelligence (AI) systems behind modern chatbots, are trained on vast amounts of legal text, but can they build on it to write law for situations that text never anticipated? In this study, we analyse AI agents' ability to draft a hypothetica…

- **[Good Judgment, Bad Advice: Decision-Model Controllers Raise Agent Cost Without Improving Success](https://arxiv.org/abs/2610.24649v1)**
  - *Naman Vats*
  - `2026-10-17`
  - Agent scaffolds increasingly delegate small decisions (whether to stop, verify, or change approach) to cheaper models. We ask whether a typed decision model, Jev 1.13, consulted only at deterministic decision points, makes a Claude Sonnet 5.5 terminal agent cheaper without making…

- **[Selm: Self-Evolving Library Management for Multi-Skill Agent Optimization](https://arxiv.org/abs/2610.24630v1)**
  - *Mengxi Hu, Yuxuan Hu, Jinbo Su et al.*
  - `2026-10-17`
  - Large language model (LLM) agents increasingly use skills as a lightweight way to acquire task-specific knowledge. Recent work enables skills to evolve from task trajectories. However, these methods often lack systematic management of evolved skills, making it difficult for agent…

- **[Muse Glimmer 30B: An On-Device Agentic Model](https://arxiv.org/abs/2610.24628v1)**
  - *Arash Ebrahim Abtahizadeh, Muna Aghamelu, Adil Ahmed et al.*
  - `2026-10-17`
  - We introduce Muse Glimmer, an open-source 30B parameter causal language model with perception encoder, purpose-built for autonomous agentic tasks on consumer hardware. Muse Glimmer integrates multi-step reasoning, reliable tool use and failure recovery into a single model that ru…

- **[CADS: Measuring the Incremental Contribution of LLM Proposers in Sequential Biological Screens](https://arxiv.org/abs/2610.24597v1)**
  - *Guanxing Chen, Nihui Shao, Haohuai He et al.*
  - `2026-10-17`
  - Large language models are increasingly used to guide sequential biological screens, yet standard evaluations rely on raw hit counts that conflate a proposer's value with the discovery capacity of the underlying algorithmic harness. Adaptive sampling and corrupted experimental rea…

- **[From Stories to Features: Scaling Concept Vectors for AI Alignment & Interpretability](https://arxiv.org/abs/2610.24556v1)**
  - *Dmitry Scherbakov, Oleg Chernikov, Victoria Khamash et al.*
  - `2026-10-17`
  - We study feature vectors: directions in a language model's activation space that correspond to human-interpretable concepts, such as honesty or deception. Existing unsupervised methods like sparse autoencoders attempt to recover the whole feature space, often at the cost of featu…

- **[When Code Becomes an LLM Call: An Empirical Study of Call-Site Contracts in Agentic Systems](https://arxiv.org/abs/2610.24545v1)**
  - *Shihao Weng, Longtian Wang, Yang Feng et al.*
  - `2026-10-17`
  - Software quality has long rested on specifications that state what code must do, and on testing and verification that check that the code does it. Agentic systems change this foundation: they replace parts of their logic, such as choosing the next tool, judging whether an action…

- **[HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory](https://arxiv.org/abs/2610.24520v1)**
  - *Junming Zhang, Rubin Wei, Xu Cheng et al.*
  - `2026-10-17`
  - In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions. These habits capture implicit user information that agents must infer across conversations. However, individual observations may provide only partial evidence…

- **[Write Once, Check Many: Reusable Ledgers for Post-Hoc Policy Compliance Auditing of Agent Trajectories](https://arxiv.org/abs/2610.24483v1)**
  - *Ashwin Nagarajan, Gursimran Panesar, Alicia Yang et al.*
  - `2026-10-17`
  - Auditing LLM agents against policies is critical to ensure safety but requires rereading long trajectories once per policy. Can we instead record each trajectory once and reuse that record for policies not known in advance? We propose write once, check many, a framework in which…

- **[MELD: Recursive Self-Improvement via Hierarchical Coordination for Multi-Agent Scientific Discovery](https://arxiv.org/abs/2610.24454v1)**
  - *Sizhe Tang, Zuyuan Zhang, Zeyu Fang et al.*
  - `2026-10-17`
  - Multi-agent scientific discovery with large language models raises a coupled learning problem: research assignments determine both which experiments are pursued and the experiences from which agents adapt. We introduce MELD, a unified hierarchical test-time training framework tha…

- **[Hippo: Training-Free Agent Self-Evolution via Hippocampal Replay](https://arxiv.org/abs/2610.24453v1)**
  - *Yutong Song, Jiang Wu, Yuxuan Ren et al.*
  - `2026-10-17`
  - Motivated by recursive self-improvement (RSI), we study how LLM agents can learn through external memory without updating model parameters. Extracting useful experience from a single attempt is difficult: flawed reasoning can produce success, while poor execution can obscure a so…

- **[Bridging Exploration and Persona: Information-Directed Dueling for Test-Time Agent Personalization](https://arxiv.org/abs/2610.24385v1)**
  - *Jie Mao, Pingchen Lu, Xiangyi Wang et al.*
  - `2026-10-17`
  - Effective test-time personalization requires LLM agents to adapt to query-dependent user preferences from lightweight interaction. We study persona selection with binary comparisons between candidate responses as the online signal. We present ID-TAP, a scalable, IDS-inspired neur…

- **[IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems](https://arxiv.org/abs/2610.24383v1)**
  - *Jie Mao, Pingchen Lu, Zikun Qu et al.*
  - `2026-10-17`
  - Improving every agent in an LLM-based multi-agent system can be prohibitively costly, making it important to identify which agent should be prioritized to achieve the greatest system-level gain with limited resources. Failure attribution can inform this decision, but an agent's r…

- **[Is This Your Agent? Identity Watermarking for Agent Systems in Dynamic Environments](https://arxiv.org/abs/2610.24382v1)**
  - *Yuwei Zhong, Yu Cheng, Jiuan Zhou et al.*
  - `2026-10-17`
  - Agent systems deployed in dynamic environments continuously update their memories, skills, and runtime configurations, leading to evolving trajectories and challenges for persistent identity authentication. Existing text and agent watermarking methods struggle to achieve stable w…

- **[Train Locally, Learn Together: Distributed Multi-Agent Training via ADMM](https://arxiv.org/abs/2610.24380v1)**
  - *Yiwei Chen, Changsheng Wang, Yicheng Lang et al.*
  - `2026-10-17`
  - Multi-agent systems (MAS) can outperform individual language-model agents by combining specialized roles, diverse reasoning processes, and collaborative decision-making. However, collaborative MAS training is typically centralized, requiring a common trainer to aggregate role-loc…

- **[fxBench: Evaluating and Understanding Formula Suggestions in Spreadsheets](https://arxiv.org/abs/2610.24729v1)**
  - *Sanket Mhatre, Sumit Gulwani, Vu Le et al.*
  - `2026-10-17`
  - Spreadsheets are among the most widely used tools for computations, and formulas are their core building blocks. Besides agentic spreadsheet tools, proactive formula suggestions enable significant productivity gains and are now available in popular spreadsheet software (Microsoft…

- **[EdgeKernelBench: Unified LLM-Driven Kernel Generation for Edge Backends](https://arxiv.org/abs/2610.24648v1)**
  - *Yuhua Zheng, Xueyi Chen, Xinze Zou et al.*
  - `2026-10-17`
  - Recent works show that LLMs can generate kernels with strong performance on server GPUs. Edge deployment presents distinct challenges because the hardware is heterogeneous, the software stacks are fragmented, and the resource budgets are tight. LLM kernel generation across divers…

- **[TCMScience: An Autonomous Scientist for Traditional Chinese Medicine](https://arxiv.org/abs/2610.24601v1)**
  - *Yanlan Kang, Ruiqi Liu, Xinpei Gu et al.*
  - `2026-10-17`
  - Traditional Chinese medicine (TCM) research connects classical texts, medicinal entities, molecular assays, computational predictions, and clinical studies. An autonomous research agent must preserve the inferential boundaries between these evidence types while coordinating analy…

- **[Write Once, Query Many: Evolving Compact Reusable Memory for Long Videos](https://arxiv.org/abs/2610.24537v1)**
  - *Kerui Chen, Jinglu Wang, Yun Wang et al.*
  - `2026-10-17`
  - Long videos often exceed the context capacity of multimodal large language models (MLLMs), while agentic search repeats costly video processing and grounding for each query. Reusable memory can amortize this cost, but must preserve information for questions unknown during constru…

- **[Measuring Empowerment from Offline Data for Intrinsically Motivated Exploration](https://arxiv.org/abs/2610.24461v1)**
  - *Ishir Garg, Vivek Myers, Qiyang Li et al.*
  - `2026-10-17`
  - Large, unlabeled datasets of prior experience have become increasingly available for agentic tasks in domains such as robotics and coding. A common recipe for these tasks is to train a policy using the prior data, and then further improve it with online rollouts. But while much w…

- **[Can Agents Keep Secrets They Were Never Told? Benchmarking Latent Privacy Risks Across Sessions with MemJoin](https://arxiv.org/abs/2610.24359v1)**
  - *Qishun Yang, Shu Yang, Difei Xu et al.*
  - `2026-10-17`
  - To support sustained interactions and personalized assistance, agents use long-term memory to retain and combine user information across sessions. Reusing such memories can lead an agent to state a sensitive relation while completing an ordinary task that does not require it. The…

- **[Measuring the Task Value of Precision Upgrades in Closed-Loop Agents](https://arxiv.org/abs/2610.24346v1)**
  - *Sicheng Lyu, Xinyu Wang, Yu Gu et al.*
  - `2026-10-17`
  - A low-precision agent can call its full-precision (BF16) model at selected decisions as a fallback. A learned precision router chooses where to call it from the disagreement between the two models and is judged by end-to-end success. An inserted BF16 action, however, can rescue a…

- **[Learning to Program Retrievals: Composing Search Primitives via Reinforcement Learning](https://arxiv.org/abs/2610.24854v1)**
  - *Kyuyoung Kim, Zilin Xiao, Zhiyuan Wang et al.*
  - `2026-10-17`
  - Retrieval-augmented language models increasingly use multi-step search to solve knowledge-intensive tasks, yet existing systems typically expose retrieval through fixed pipelines or collections of atomic tools. We introduce Retrieval Program Learning (RPL), a programmable search…

- **[EGIP: An Evidence-Grounded Interaction Protocol for Clinical Agents](https://arxiv.org/abs/2610.24539v1)**
  - *Zecheng Ren, Ruichen Cong, Yi Min Chen et al.*
  - `2026-10-17`
  - Interactive clinical agents acquire evidence through patient dialogue and diagnostic examinations, yet their performance also depends on how the interaction environment exposes information, available actions, and examination results. When these conditions are implicit or inconsis…

- **[Modeling Discourse Profiles in Climate Misinformation Discourse](https://arxiv.org/abs/2610.24489v1)**
  - *Ge Gao, Zhengyang Shan, Bryan A. Plummer et al.*
  - `2026-10-17`
  - Prior work on climate misinformation detection typically classifies individual comments or claims using text alone. This framing overlooks a key property of online climate discourse: misinformation is often produced, reinforced, and sustained through recurring rhetorical patterns…

- **[Ask Less, Ask Better: Allocating User Attention in Proactive LLM Agents with Interruption Budgets](https://arxiv.org/abs/2610.24411v1)**
  - *Xuanming Zhang, Amir H. Rezaeian, Miguel Ballesteros et al.*
  - `2026-10-17`
  - LLM agents can ask clarifying questions to complete tasks, but answering each question demands users' time and effort. Existing evaluations typically measure this burden by counting questions, treating necessary and avoidable questions equally. We propose an evaluation protocol t…

- **[Defending Against Dormant Poisoning Attacks Across Language and Multimodal Agents](https://arxiv.org/abs/2610.24379v1)**
  - *Wonjun Lee, Vaidehi Patil, Zaid Khan et al.*
  - `2026-10-17`
  - Recent work shows that attackers can implant dormant malicious behaviors that remain hidden at release but emerge after benign fine-tuning. As foundation models are used as agents, whether dormant poisoning extends to harmful agent actions and multimodal settings remains unclear.…

- **[AgentSoV: Virtual Sensing for LLM Multi-Agent Systems via Stream of Variation](https://arxiv.org/abs/2610.24845v1)**
  - *Congjing Zhang, Siyuan Xu, Yunfei Bai et al.*
  - `2026-10-17`
  - Large language model (LLM) multi-agent systems (MASs) solve complex tasks through interacting agents, yet their reliability is difficult to analyze because failures depend on both individual agents and how information and errors propagate across the system. Existing approaches la…

- **[Measuring Consensus in AI Agent Networks](https://arxiv.org/abs/2610.24833v1)**
  - *Jin Gao*
  - `2026-10-17`
  - As AI agents become increasingly connected through networks and take on tasks that require negotiation and joint decision-making, a systematic approach is needed to assess how their views converge and what information supports their decisions. We present an evaluation framework t…

- **[Low-Bit Distributed Constrained Optimization with Application to Optimal Scheduling and Allocation](https://arxiv.org/abs/2610.24431v1)**
  - *Mohammadreza Doostmohammadian, Sergio Pequito*
  - `2026-10-17`
  - This paper proposes a distributed resource allocation algorithm in which each agent communicates only the sign of its local cost gradient, a single bit per directed link per iteration. The algorithm is based on Laplacian-gradient dynamics and preserves the equality (demand) const…


## Harness  (98)

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


### Other / arXiv

- **[OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory](https://arxiv.org/abs/2610.26860)**
  - *Yu Zhou, Cheng-Fu Yang, Rui Sun et al.*
  - 🤗 Featured · `2026-10-19`
  - Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base…

- **[HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs](https://arxiv.org/abs/2610.26770)**
  - *Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen et al.*
  - 🤗 Featured · `2026-10-19`
  - Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harn…

- **[Self-Evolving Coding Agents via Harness-Policy Optimization](https://arxiv.org/abs/2610.22791)**
  - *Zhepei Wei, Wenlin Yao, Baolin Peng et al.*
  - 🤗 Featured · `2026-10-16`

- **[Harnessing Textual Refusal Directions for Multimodal Safety](https://arxiv.org/abs/2606.31876)**
  - *Moreno D&#39;Incà, Nicu Sebe, Massimiliano Mancini*
  - 🤗 Featured · `2026-10-16`

- **[Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy](https://arxiv.org/abs/2610.26836)**
  - *Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu et al.*
  - 🤗 · `2026-10-19`
  - LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads on demand. We ask where this costs accuracy with a real scientific tool: PHREEQC…

- **[ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry](https://arxiv.org/abs/2610.26829v1)**
  - *Matt Turk, Brandon L. Neel, Diana M. Lopez et al.*
  - `2026-10-19`
  - Frontier agents retrieve structural metadata well and compute geometry from coordinates less reliably. We ask how much of a benchmark score reflects that gap and how much reflects the evaluation configuration around the model. We study ProteinGeoBench, a suite of 131 protein-stru…

- **[Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams](https://arxiv.org/abs/2610.26781v1)**
  - *Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao et al.*
  - `2026-10-19`
  - Phone scams impose substantial and growing costs on individuals and financial systems worldwide, yet existing countermeasures impose no resource cost on perpetrators. Strategic scam-baiting, in which automated agents engage scammers to deplete their operational capacity, offers a…

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

- **[VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement](https://arxiv.org/abs/2610.26342v1)**
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

- **[Secure Agentic Coding through Counterexample-Grounded Feedback](https://arxiv.org/abs/2610.25916v1)**
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

- **[Maestro: Agentic Formal Proof Development by Coordination](https://arxiv.org/abs/2610.25920v1)**
  - *Haoyu Li, Zeren Shui, Yuhao Zhang et al.*
  - `2026-10-19`
  - Lean is increasingly used to verify mathematical proofs and software produced by LLM agents, but writing formal proofs remains hard. Existing prover systems take a divide-and-conquer approach that recursively decomposes hard proof obligations into easier lemmas and splits again a…

- **[Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments](https://arxiv.org/abs/2610.25747v1)**
  - *JooKyung Yuh, Byungmin Park, Eunseo Choi et al.*
  - `2026-10-19`
  - Scientific model discovery requires proposing candidate models of an unknown system and designing experiments that discriminate among them. However, LLM-based approaches typically rely on in-context learning to predict outcomes and select experiments, lacking explicit model evalu…

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

- **[From Outcomes to Components: A Counterfactual Evaluation Framework for LLM-Proposed Repairs](https://arxiv.org/abs/2610.26650v1)**
  - *Hengyu Ye, Songhua Hu*
  - `2026-10-19`
  - An LLM-generated repair action specifies which records to change and by how much. A failed action may still contain a useful target set or numerical update, depending on how the two are paired. We evaluate this problem in traffic networks and databases, where aggregate observatio…

- **[When to Stop Asking: Factor Coverage Bias and LLM Determinability Judgments with Underspecified Information in Medicine](https://arxiv.org/abs/2610.25819v1)**
  - *Yusuke Watanabe, Yohei Kobashi, Taisei Tosaki et al.*
  - `2026-10-19`
  - Clinical decision-making often begins with underspecified information and requires not only gathering missing information but also knowing when to stop. This calls for judging determinability (whether the available information is sufficient for a decision) by considering whether…

- **[ActTime: Action-Conditioned World Modeling for Time Series](https://arxiv.org/abs/2610.25764v1)**
  - *Xinxing Zhou, Xiaojie Yuan, Yanlong Wen et al.*
  - `2026-10-19`
  - Time-series models increasingly condition on known future inputs. In controlled systems, some of these inputs are actions that can be changed, compared, and optimized before execution. A model must therefore do more than predict the realized future: it must predict how outcomes c…

- **[Design and Cross-Domain Evaluation of an Agent Execution Harness](https://arxiv.org/abs/2610.25568v1)**
  - *Saurav Joshi, Manas Gupta, Ashwin Venkatesh Raman et al.*
  - `2026-10-18`
  - Completing complex tasks with language-model agents requires coordinating planning, execution, and review so the final result addresses the user's original objective. We present an agent execution harness that keeps the original objective separate from a revisable plan and an exe…

- **[Editing as Language: Teaching LLM Agents a Grammar for Native Context Editing](https://arxiv.org/abs/2610.25550v1)**
  - *Yunlong Deng, Yan Li, Xing Hu et al.*
  - `2026-10-18`
  - A synopsis in novels folds a story into a few lines; a function in code gathers many steps with a single execution. Context editing is native to language itself. In this paper, we propose the Native Context Editing (NCE) framework, which gives language model agents a grammar for…

- **[CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?](https://arxiv.org/abs/2610.25078v1)**
  - *Jiaqi Su, Guibin Zhang, Jie-Jing Shao et al.*
  - `2026-10-18`
  - Model--harness co-evolution has emerged as a prominent paradigm for recursive self-improving (RSI) agents, jointly evolving their execution scaffolds and intrinsic capabilities. We study the persistent yet often overlooked brain--body mismatch problem in this paradigm, where an e…

- **[ReTRACE: Feedback-Guided LLM Agent in a Chemistry Harness for Retrosynthesis Planning](https://arxiv.org/abs/2610.24744v1)**
  - *Jinxiang Xie, Yijian Zhang, Qingyuan Yi et al.*
  - `2026-10-17`
  - Computer-aided retrosynthesis has advanced through single-step prediction, tree search and route scoring, but complex targets still require judgement over the whole route, where stereochemistry, functional-group compatibility, cost and greenness interact. Here we present \textbf{…

- **[Can LLM Agents Resolve Service Failures? Simulating Multi-Turn Complaint Handling under Information Asymmetry](https://arxiv.org/abs/2610.24733v1)**
  - *Wailing Ng, Mengze Hong, Chen Jason Zhang et al.*
  - `2026-10-17`
  - LLM agents are widely adopted in service chatbots for rule-guided support and information access, yet emotionally demanding complaint handling still relies heavily on human agents. We introduce ServiceBench, to our knowledge the first benchmark dedicated to complaint handling, wi…

- **[CADS: Measuring the Incremental Contribution of LLM Proposers in Sequential Biological Screens](https://arxiv.org/abs/2610.24597v1)**
  - *Guanxing Chen, Nihui Shao, Haohuai He et al.*
  - `2026-10-17`
  - Large language models are increasingly used to guide sequential biological screens, yet standard evaluations rely on raw hit counts that conflate a proposer's value with the discovery capacity of the underlying algorithmic harness. Adaptive sampling and corrupted experimental rea…

- **[Write Once, Query Many: Evolving Compact Reusable Memory for Long Videos](https://arxiv.org/abs/2610.24537v1)**
  - *Kerui Chen, Jinglu Wang, Yun Wang et al.*
  - `2026-10-17`
  - Long videos often exceed the context capacity of multimodal large language models (MLLMs), while agentic search repeats costly video processing and grounding for each query. Reusable memory can amortize this cost, but must preserve information for questions unknown during constru…

- **[Learning to Program Retrievals: Composing Search Primitives via Reinforcement Learning](https://arxiv.org/abs/2610.24854v1)**
  - *Kyuyoung Kim, Zilin Xiao, Zhiyuan Wang et al.*
  - `2026-10-17`
  - Retrieval-augmented language models increasingly use multi-step search to solve knowledge-intensive tasks, yet existing systems typically expose retrieval through fixed pipelines or collections of atomic tools. We introduce Retrieval Program Learning (RPL), a programmable search…

- **[Measuring Consensus in AI Agent Networks](https://arxiv.org/abs/2610.24833v1)**
  - *Jin Gao*
  - `2026-10-17`
  - As AI agents become increasingly connected through networks and take on tasks that require negotiation and joint decision-making, a systematic approach is needed to assess how their views converge and what information supports their decisions. We present an evaluation framework t…

- **[Uncovering Semantic Hierarchies in Text-Attributed Graphs via Variational EM-based LLM-GNN Synergy](https://arxiv.org/abs/2610.24624v1)**
  - *Yunhui Liu, Xudong Jin, Qizhuo Xie et al.*
  - `2026-10-17`
  - While hierarchical structures are intrinsic to organizing human knowledge, current representation learning on text-attributed graphs predominantly operates on flat semantic spaces, overlooking the rich coarse-to-fine granularity inherent in real-world data. To bridge this gap, we…

- **[Medical Fine-Tuning Reshapes, Not Reduces, Patient-Facing AI Risk: A Rubric-Based, LLM-Judge Evaluation Framework](https://arxiv.org/abs/2610.24807v1)**
  - *Savan Doshi*
  - `2026-10-17`
  - Patient-facing medical question answering with large language models (LLMs) is moving from research demonstrations to production deployments, yet evaluation remains anchored on factual correctness. Factuality is necessary but not sufficient: a response can be factually grounded a…

- **[Are We Evaluating VLM Token Pruning Right? Looking Beyond Accuracy and Token Count](https://arxiv.org/abs/2610.24740v1)**
  - *Geng Li, Guohao Chen, Shilin Shan et al.*
  - `2026-10-17`
  - Visual token pruning aims to reduce inference cost while preserving the capabilities of the original VLM. Yet existing evaluations rely on aggregate task accuracy and retained token count as proxies for pruning quality and actual efficiency. We reveal two limitations: 1) Aggregat…

- **[Pluralistic Alignment in Language Models: Objectives, Human References, and Preference Representations](https://arxiv.org/abs/2610.24471v1)**
  - *Meng-Chen Wu, Umesh Bodhwani*
  - `2026-10-17`
  - Pluralistic alignment aims to represent meaningful variation in human preferences rather than collapse heterogeneous judgments into a single target. Yet existing work often mixes three distinct questions: what pluralistic behavior a model should exhibit, whose preferences define…


## Finance  (155)

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


### ACL

- **[Shallow Probes Are Sufficient for Near-Oracle Personalization Depth Allocation in Federated Learning](https://arxiv.org/abs/2610.25193v1)**
  - *Beyazit Bestami Yuksel, Emrah Dikbiyik, Ayse Yilmazer Metin*
  - **ACL** · `2026-10-18`
  - Rather than proposing a new federated optimizer, we study whether a small client-specific measurement budget can support cost-aware personalization-depth decisions under a utility that trades Macro-F1 against deployment cost. Exhaustive evaluation of six depths defines an offline…


### Other / arXiv

- **[Policy Is Not Capability: Some Safety Benchmarks Measure Which Definition of "Unsafe" You Trained On](https://arxiv.org/abs/2610.25060)**
  - *Vahid Jebraeeli, Jonathon Romero, Yijin Wang et al.*
  - 🤗 Featured · `2026-10-18`

- **[The Control Layer Behind Rule-Following Agents Trading Across Market Conditions](https://arxiv.org/abs/2610.26324)**
  - *Saad Naja, Nasser Odtallah, Jake Van-Praag et al.*
  - 🤗 · `2026-10-19`
  - Trading discipline often fails people. Our study tested whether four AI trading agents followed their strategies and risk rules. Offering traders the evidence and an agent evaluation toolkit to separate luck from following the rules, before giving agents meaningful autonomy or ca…

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

- **[Adversarial Post-Training of Foundation Models for High-Frequency Trading](https://arxiv.org/abs/2610.25604v1)**
  - *Alexandre Bismuth, Kang Li, Aramis Marti-Shahandeh et al.*
  - `2026-10-19`
  - While autoregressive foundation models trained on limit order book (LOB) data show state-of-the-art performance for market simulation, pre-training with cross-entropy neither penalizes the compounding of sampling errors over free-running rollouts nor targets desired market proper…

- **[Amortized Neural Filtering for Calibrated Posteriors in Statistical Arbitrage](https://arxiv.org/abs/2610.25802v1)**
  - *Minkey Chang*
  - `2026-10-19`
  - Statistical arbitrage trades on an estimate of the state of a residual spread, and conventional practice discards the uncertainty of that estimate. We keep the uncertainty and use it in the trading decision. A Neural Filter Estimator (NFE) is trained on simulated paths of a mean-…

- **[Regime-Aware Interpretable Ranking for Sector Rotation](https://arxiv.org/abs/2610.26456v1)**
  - *Kelvin J. L. Koa, Ziling Liu, Xinyang Li et al.*
  - `2026-10-19`
  - Sector rotation is a common decision in benchmark-relative portfolio management, where portfolio managers rank sectors for overweight and underweight positions. We formulate this task as ranking sector actions by expected future risk-adjusted active performance, measured with for…

- **[Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors](https://arxiv.org/abs/2610.25552v1)**
  - *Jinu Lee, Shraddha Barke*
  - `2026-10-18`
  - Symbolic constraints (programmatic, deterministic checks for tool calls) enable deterministic verification of LLM agents' tool calls, but existing approaches primarily enforce predefined safety policies rather than tool dependencies in complex tool environments. We explore whethe…

- **[StopLoss: Teaching Agents to Predict Failure and Stop Early](https://arxiv.org/abs/2610.25525v1)**
  - *Jiarong Liang, Xueguang Ma, Dongfu Jiang et al.*
  - `2026-10-18`
  - Coding agents keep working on runs that will fail verification, and asking a frontier model to watch for this is expensive in its own right. We introduce StopLoss, a small external monitor that learns failure recognition from completed trajectories and their verifier outcomes. Th…

- **[Formally Verified Autoresearch for Analyzing the Expressivity of Multi-Head Attention](https://arxiv.org/abs/2610.25341v1)**
  - *Karthik Viswanathan, Plamen Dimitrov, Stefano Rocca et al.*
  - `2026-10-18`
  - Multi-head attention is a central component of the transformer architecture, yet how its expressivity depends on the number of heads remains poorly understood. We study a one-layer, attention-only transformer with additive positional embeddings and define the head complexity $H^\…

- **[Assessing the Empirical Evidence for Loss of Control from Agentic General-Purpose AI](https://arxiv.org/abs/2610.25241v1)**
  - *Risto Uuk, Santeri Koivula, Lorenzo Pacchiardi et al.*
  - `2026-10-18`
  - Theoretical literature warns that advanced generalist agentic systems might pursue instrumental goals that are misaligned with human preferences, thus posing risks of irreversible loss of human control. The EU's Code of Practice for General-Purpose AI lists loss of control as a s…

- **[Mining the Self-Rewriting System: A Vision for Data Mining on AI-Native Infrastructure](https://arxiv.org/abs/2610.25374v1)**
  - *Mayank Darbari, Chiman Salavati, Liang Wu et al.*
  - `2026-10-18`
  - Classical data mining treats data as generated outside the learner. Emerging AI-native infrastructure invalidates this assumption: as agents observe system state, act, update retrieval stores and models, and promote new artifacts into the serving path, their own decisions reshape…

- **[World Models, Trees and Foundation Models for Retail Forecasting: Evidence from Four Public Data Sets](https://arxiv.org/abs/2610.25170v1)**
  - *Karthik Iyer, Madan Dabbeeru*
  - `2026-10-18`
  - A retailer makes different decisions at different grains of the product, store and time hierarchy: store orders for an item in a store, supplier funding for an item across stores, category performance by store, and the financial plan for the chain. Which forecasting model to use…

- **[The Hidden Look-Ahead: Point-in-Time Leakage in Electricity Market Data](https://arxiv.org/abs/2610.25389v1)**
  - *Abdelkrim Alfalah*
  - `2026-10-18`
  - Empirical studies of electricity prices routinely state that their models use only information available at the time of the trading decision. For weather-driven forecasts drawn from commercial archives, this condition is harder to meet than it appears, and whether it holds can ch…

- **[DiffuPlan: Editable Planning State for Diffusion Language Model Agents](https://arxiv.org/abs/2610.24717v1)**
  - *Qisheng Zhou, Zhen Xiong, Qiaoyu Tan*
  - `2026-10-17`
  - Diffusion language models (dLLMs) are emerging as an alternative to autoregressive (AR) language models, yet dLLM agents largely inherit an interaction protocol designed for AR generation: once intermediate state is written, later observations can only be incorporated by appendin…

- **[HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory](https://arxiv.org/abs/2610.24520v1)**
  - *Junming Zhang, Rubin Wei, Xu Cheng et al.*
  - `2026-10-17`
  - In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions. These habits capture implicit user information that agents must infer across conversations. However, individual observations may provide only partial evidence…

- **[MELD: Recursive Self-Improvement via Hierarchical Coordination for Multi-Agent Scientific Discovery](https://arxiv.org/abs/2610.24454v1)**
  - *Sizhe Tang, Zuyuan Zhang, Zeyu Fang et al.*
  - `2026-10-17`
  - Multi-agent scientific discovery with large language models raises a coupled learning problem: research assignments determine both which experiments are pursued and the experiences from which agents adapt. We introduce MELD, a unified hierarchical test-time training framework tha…

- **[Measuring Empowerment from Offline Data for Intrinsically Motivated Exploration](https://arxiv.org/abs/2610.24461v1)**
  - *Ishir Garg, Vivek Myers, Qiyang Li et al.*
  - `2026-10-17`
  - Large, unlabeled datasets of prior experience have become increasingly available for agentic tasks in domains such as robotics and coding. A common recipe for these tasks is to train a policy using the prior data, and then further improve it with online rollouts. But while much w…

- **[Pluralistic Alignment in Language Models: Objectives, Human References, and Preference Representations](https://arxiv.org/abs/2610.24471v1)**
  - *Meng-Chen Wu, Umesh Bodhwani*
  - `2026-10-17`
  - Pluralistic alignment aims to represent meaningful variation in human preferences rather than collapse heterogeneous judgments into a single target. Yet existing work often mixes three distinct questions: what pluralistic behavior a model should exhibit, whose preferences define…

- **[A Symmetry-Matching Approach to Blind-Spot Reduction in Sparse Autoencoders](https://arxiv.org/abs/2610.24908v1)**
  - *Csaba Balogh*
  - `2026-10-17`
  - Language models can treat semantically distinct inputs as interchangeable at the representation level, creating blind spots that standard sparse autoencoder (SAE) objectives do not target. In safety-critical settings such as clinical dosage extraction, legal clause interpretation…

- **[Learning volatility-adaptive forgetting via GARCH-modulated LSTM for stock price forecasting](https://arxiv.org/abs/2610.24386v1)**
  - *Xin-Rui Lu, Da-Qing Zhang*
  - `2026-10-17`
  - Stock price forecasting is hindered by the heteroscedastic nature of financial time series, in which turbulent and tranquil regimes alternate. Although the Long Short-Term Memory (LSTM) network is widely used for this task, its gates are oblivious to such volatility variation, so…

- **[A decomposition-integration framework coupling singular spectrum analysis with a volatility-adaptive LSTM for stock price forecasting](https://arxiv.org/abs/2610.24384v1)**
  - *Xin-Rui Lu, Da-Qing Zhang*
  - `2026-10-17`
  - Financial time series exhibit multi-scale, high-noise, and non-stationary volatility dynamics. Decomposition--integration frameworks built on complete ensemble empirical mode decomposition with adaptive noise (CEEMDAN) have advanced this field, yet existing CEEMDAN hybrids remain…

- **[Rachev-Ratio Portfolio Optimization with TimeGAN Scenarios: Replacement versus Supplementation](https://arxiv.org/abs/2610.24544v1)**
  - *Yifan He*
  - `2026-10-17`
  - This study evaluates the reliability and investment consequences of scenarios from a specified time-series generative adversarial network (TimeGAN) in Rachev-ratio portfolio allocation. Using 12 exchange-traded funds, we compare historical, replacement and hybrid policies across…

- **[Compose the Horizon: Parameter-Shared Blockwise Forecasting under a Sequential-Compute Trade-off](https://arxiv.org/abs/2610.24826v1)**
  - *Zeyan Li, Weiheng Li, Shengda Zhuo et al.*
  - `2026-10-17`
  - Most long-horizon forecasters emit the complete future in one pass. We ask whether a compact operator can instead be reused to emit contiguous future blocks, trading stored parameters for sequential computation. Recursive Functional Decomposition (RFD) factorizes the horizon mapp…

- **[No-Regret Revenue Maximization in Sequential Market Making Under Inventory Constraints](https://arxiv.org/abs/2610.24562v1)**
  - *Davide Maran, Marcello Restelli, Francesco Emanuele Stradi*
  - `2026-10-17`
  - Market makers keep trading efficient by setting bid and ask prices for buyers and sellers. In sequential market making, trades happen independently based on price thresholds, requiring the market maker to maintain balanced, low-risk inventory over T rounds. This paper studies how…

- **[Optimal Trading Filters and the Value of Predictive Signals](https://arxiv.org/abs/2610.24558v1)**
  - *Matteo Smerlak*
  - `2026-10-17`
  - The value of a forecast depends on its accuracy, but also on its actionability. In trading, an investor must translate return forecasts into positions while accounting for trading costs and the lingering impact of earlier trades. We solve the stationary quadratic trading problem…


---
*Generated 2026-10-20 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
