# Daily Paper Digest — 2026-10-23 (Friday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**523 unique papers** (664 topic-entries — cross-topic papers counted once per category)

---

## Agent  (379)

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

- **[AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing](https://arxiv.org/abs/2608.29622)**
  - *{'fullname': 'Xinke Jiang', 'username': ''}, {'fullname': 'Yue Fang', 'username': ''}, {'fullname': 'Zhibang Yang', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2026-08-01`
  - Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts. Recent reinforcement learnin…

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


### ACL

- **[Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity](https://arxiv.org/abs/2610.31436v1)**
  - *Ali Atiah Alzahrani*
  - **ACL** · `2026-10-22`
  - Automated agentic-system design is typically evaluated on static task suites with immediate scalar rewards. Deployed systems face persistent shift, delayed dependent feedback, correlated component failures, and costly architecture changes. We formalize meta-agent architecture sea…

- **[Agri-SCHOLAR: Simulation-Grounded In-Season Rolling Advisories for Agricultural Crops Using LLM-Bounded Optimization](https://arxiv.org/abs/2610.31003v1)**
  - *Geetha Charan, Vedant Balasubramaniam, Manojkumar Patil et al.*
  - **ACL** · `2026-10-22`
  - Existing agricultural advisories to farmers suffer from several limitations: (a) remain largely expert-driven, (b) do not adequately account for in-season weather, and (c) do not scale to individual farms. In this paper, our objective is to close these gaps by developing Agri-SCH…

- **[ColaBench: Evaluating Memory-Guided Knowledge Acquisition in Personal Agents](https://arxiv.org/abs/2610.30989v1)**
  - *Wenjie Zhang, Zhichao Shi, Xuhui Jiang et al.*
  - **ACL** · `2026-10-22`
  - Personal agents need to draw on long-term interaction history to retrieve and apply external knowledge suited to a user's current request. Even an answer grounded in relevant documents can be unsuitable when it overlooks the user's circumstances. This creates two connected challe…

- **[AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes](https://arxiv.org/abs/2610.30738v1)**
  - *Jie Ying, Xutao Zhang, Ningyuan Chen et al.*
  - **ACL** · `2026-10-22`
  - When tool-use agents write files, execute code, or send data, their final responses do not explain the resulting security events, and heterogeneous runtimes expose the relevant evidence through incompatible interfaces. We present AgentTriage, an executable contract for replayable…

- **[Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test](https://arxiv.org/abs/2610.30698v1)**
  - *Bowen Liu, Youting Wang, Bonan Shen et al.*
  - **ACL** · `2026-10-22`
  - An LLM agent can retrieve a memory correctly yet use it incorrectly after its validity state changes. We study governance-state corruption: faults that alter which retained records enter model-visible context while stored content and tasks remain fixed. Across six providers, 731…

- **[nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators](https://arxiv.org/abs/2610.31080v1)**
  - *Fabian Isensee, Constantin Ulrich Harsy, Maximilian Rokuss et al.*
  - **ACL** · `2026-10-22`
  - Interactive 3D segmentation models such as nnInteractive turn a few spatial prompts (points, scribbles, boxes) into accurate volumetric masks, but a human still does the annotation work: finding each structure, placing prompts, checking the result and correcting it. General-purpo…

- **[What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks](https://arxiv.org/abs/2610.30635v1)**
  - *Fei Ding*
  - **ACL** · `2026-10-22`
  - Coding-agent benchmarks often describe a task in natural language but grade it with tests taken from the upstream project. Passing those tests can require information the description never states: a constant's name, a module path, an exact message. We call this a specification-or…

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

- **[A Transformer-based Approach for Real-time Multi-agent Path Planning with Varying Initial/Final Conditions](https://arxiv.org/abs/2610.30388v1)**
  - *Qian Zhang, Shanqing Liu, Jerome Darbon et al.*
  - **ACL** · `2026-10-21`
  - We address the problem of real-time multi-agent path planning under prescribed initial and final configurations, formulated as a high-dimensional optimal control problem subject to inter-agent collision avoidance and obstacle constraints. Classical solvers based on the Hamilton--…

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


### Other / arXiv

- **[IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems](https://arxiv.org/abs/2610.30949)**
  - *A. Jian Yang, An Huang, Bo Dan et al.*
  - 🤗 Featured · `2026-10-22`
  - We present IQuest-Q1, a sparse Mixture-of-Experts (MoE) agentic foundation model with 320B total parameters (15B activated). IQuest-Q1 is developed through a three-stage process: (1) stable and efficient pre-training, combining Stable SplitNorm, Muon, and muP with a two-stage cur…

- **[Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports](https://arxiv.org/abs/2610.31158)**
  - *Jiahao Meng, Qize Yang, Yuxuan Wang et al.*
  - 🤗 Featured · `2026-10-22`
  - Deep research agents synthesize open-web evidence into long reports, but current benchmarks do not evaluate research centered on a source video. We introduce Video-Centered Deep Research Report Generation. Given a video and user request, an agent identifies research questions, re…

- **[Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought](https://arxiv.org/abs/2610.30755)**
  - *Zhengye Bao, Shengtao Zhang, Haokai Zhang et al.*
  - 🤗 Featured · `2026-10-22`
  - LLM memory is widely used in long-term conversation understanding. Agentic memory systems often use mutation, structural organization, learned retrieval strategies, or other complex operations. Is this complexity always necessary? We study Raw-RAG, a naive RAG baseline using dens…

- **[AgentVQA: A Unified Benchmark for Agentic Visual Understanding](https://arxiv.org/abs/2610.31494)**
  - *Advait Gupta, Sachin Konan, Tom Yin et al.*
  - 🤗 Featured · `2026-10-22`

- **[SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs](https://arxiv.org/abs/2610.31062)**
  - *Arnon Mazza, Elad Levi*
  - 🤗 Featured · `2026-10-22`
  - Policy enforcement for LLM agents has shifted from single-turn content moderation to compound, application-specific policies evaluated over multi-turn transcripts and tool-call trajectories. Fine-tuned guardrail models are efficient but degrade on compound policies, and while LLM…

- **[FilmFlow: Agentic System for 3D Virtual Film Cinematography](https://arxiv.org/abs/2610.30753)**
  - *Yiming Zhang, Jiarui Guo, Haojia Wei et al.*
  - 🤗 Featured · `2026-10-22`

- **[RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention](https://arxiv.org/abs/2610.31372)**
  - *Jiening Siow, Amy Xin, Junjie Wang et al.*
  - 🤗 Featured · `2026-10-22`
  - Autonomous research agents are increasingly used to automate large portions of scientific research, yet they are prone to research integrity violations (RIVs): behaviors that compromise the validity, reproducibility, or faithfulness of the research process. We present RIDAR, a fr…

- **[Toward Recursive Self-Improvement in Physical AI](https://arxiv.org/abs/2610.29677)**
  - *Meng Luo, Zechen Bai, Shanqing Xu et al.*
  - 🤗 Featured · `2026-10-21`
  - Recursive self-improvement (RSI) describes a system that improves not only its behavior but also the process by which it improves. Recent digital agents test this idea by rewriting their own code and checking each version with executable tests. Bringing these mechanisms into the…

- **[Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents](https://arxiv.org/abs/2610.26233)**
  - *Zhenyu Zhang, Kewei Fu, Yongqi Tong et al.*
  - 🤗 Featured · `2026-10-19`

- **[BrickWright: Agentic Creation of Physically Feasible Brick Builds](https://arxiv.org/abs/2610.31651)**
  - *Ava Pun, Kevin Dai, Sally Chen et al.*
  - 🤗 · `2026-10-22`

- **[CoWriter: Guiding Methodological and Synergetic Human-LLM Co-Authoring](https://arxiv.org/abs/2610.31277)**
  - *Shmuel Amar, Benjamin Lieber, Ori Shapira et al.*
  - 🤗 · `2026-10-22`
  - While LLMs have transformed text generation, standard chat-and-canvas interfaces often reduce human authoring to quite passive supervision, causing review fatigue, over-reliance on AI, and the sidelining of the human role in long-form, source-grounded writing. Prior systems typic…

- **[Trace2World: Reconstructing App Worlds from Real Interaction Traces for Scalable GUI Agent Training](https://arxiv.org/abs/2610.30792)**
  - *Zezhou Wang, Hanzhang Zhou, Panrong Tong et al.*
  - 🤗 · `2026-10-22`
  - Scaling GUI reinforcement learning requires environments that preserve real-app behavior. Yet coupling behavior inference with coding can turn partial traces into runnable mocks with incorrect state transitions. We introduce \textbf{Trace2World}, which separates global behavior r…

- **[Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting](https://arxiv.org/abs/2610.30103)**
  - *Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Zabir Al Nazi et al.*
  - 🤗 · `2026-10-21`
  - Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notice which side of this boundary a problem falls on, yet existing benchmarks either…

- **[Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences](https://arxiv.org/abs/2610.30485)**
  - *Jialin Li, Zhenhao Chen, Hanjun Luo et al.*
  - 🤗 · `2026-10-21`
  - Personal intelligence systems are taking on increasingly complex everyday tasks, yet repeated questions, unnecessary confirmations, and unwanted outreach can turn capable assistance into interaction burden. Reducing this burden requires agents to remember how users want to be ass…

- **[Agentic World Action Models](https://arxiv.org/abs/2610.30136)**
  - *Zhuoyang Liu, Dantong Niu, Botong Zhang et al.*
  - 🤗 · `2026-10-21`

- **[Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113)**
  - *Houde Qian, Zheng Jiang, Wenyi Li et al.*
  - 🤗 · `2026-10-21`
  - Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether lar…

- **[Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use](https://arxiv.org/abs/2610.30108)**
  - *Yanzhe Chen, Ziyi Yang, Jifeng Zhu et al.*
  - 🤗 · `2026-10-21`
  - Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed system…

- **[From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](https://arxiv.org/abs/2610.30051)**
  - *May Espinola, Qifan Zhang, Yu Xiang*
  - 🤗 · `2026-10-21`
  - Recent advances in frontier AI models have demonstrated remarkable capabilities in visual understanding, reasoning, planning, and tool use, raising the possibility of using general-purpose AI models for robot manipulation without task-specific training. However, their manipulatio…

- **[TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments](https://arxiv.org/abs/2610.30043)**
  - *Yicheng Xu, Zhikai Xu, Ziyuan Chen et al.*
  - 🤗 · `2026-10-21`

- **[METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](https://arxiv.org/abs/2610.31656v1)**
  - *Ali Najar, Hosein Hasani, Amir Kooshan Fattah et al.*
  - `2026-10-22`
  - Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based a…

- **[EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650v1)**
  - *Qijin Zhang, Hanzhen Wang, Yuehan Zhao et al.*
  - `2026-10-22`
  - Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We int…

- **[Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3](https://arxiv.org/abs/2610.31624v1)**
  - *Barış Alparslan, Sandy Tanwisuth, Caleb Petterson*
  - `2026-10-22`
  - Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcem…

- **[Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure](https://arxiv.org/abs/2610.31573v1)**
  - *Pellegrino Casoria, Simon Pietro Romano*
  - `2026-10-22`
  - In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what c…

- **[Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated Metadata Across Structured and Unstructured Systems](https://arxiv.org/abs/2610.31553v1)**
  - *Humza Akhtar, Brian Freeman*
  - `2026-10-22`
  - Industrial organizations hold operational knowledge in structured records, such as telemetry, point lists, and transactions, and in unstructured sources, such as manuals, service notes, communications, and inspection reports. Governance programs often manage these sources separat…

- **[DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination](https://arxiv.org/abs/2610.31511v1)**
  - *Ziyi Jiao, Heng Zhang, Drishti Regmi et al.*
  - `2026-10-22`
  - Coordinating two players in a cooking task requires a vision-language agent to track changing scene states, sequence recipe steps, and allocate shared resources under a time budget. We introduce an Overcooked-inspired benchmark for evaluating these capabilities in Unreal Engine e…

- **[Training Small Language Models for Transferable Tool Selection](https://arxiv.org/abs/2610.31483v1)**
  - *Zhaoyi Zhou, Akshayaa Magesh, Jeongyeol Kwon et al.*
  - `2026-10-22`
  - As LLM agents operate over corpora of more than ten thousand tools, selecting the right tool for a complex multi-step user instruction becomes a central bottleneck. Tool descriptions cannot all fit in context, and relevance-based retrievers only rank tools without knowing which a…

- **[Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery](https://arxiv.org/abs/2610.31461v1)**
  - *Dingxuan Zhang, Yanhui Jiang, Jun Wang et al.*
  - `2026-10-22`
  - Reusable skills allow large language model agents to package task-specific procedures, tool affordances, and execution guidance into modular units. Prior work has largely studied how agents retrieve, compose, or synthesize skills before execution. In coding agents, however, execu…

- **[AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack](https://arxiv.org/abs/2610.31404v1)**
  - *Justin Tan, Miao Li, Ding Zhao*
  - `2026-10-22`
  - Computer-use agents increasingly handle private information and act on users' behalf across desktop and web applications, including email. Phishing therefore poses privacy and security risks that depend not only on whether agents recognize malicious messages, but also on how they…

- **[Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action](https://arxiv.org/abs/2610.31376v1)**
  - *Chao Gu, Quanyan Zhu*
  - `2026-10-22`
  - This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent capabilities, approval…

- **[Muffin - A Shared Memory Buffer for Asynchronous AI Agents](https://arxiv.org/abs/2610.31355v1)**
  - *Ping-Lin Kuo, Suman Navaratnarajah, Christian Frey et al.*
  - `2026-10-22`
  - The rise of Agentic AI systems has changed the landscape of artificial intelligence by enabling strong reasoning capabilities through specialized multi-agent interaction with structured self-reflection. However, in target-driven reasoning tasks, single- and multi-agent systems ar…

- **[Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash](https://arxiv.org/abs/2610.31351v1)**
  - *Atharv Chandratre, Jai Datar*
  - `2026-10-22`
  - Feature flags are runtime configuration mechanisms used for gradual feature rollouts, experimentation, and kill switches. Once a feature is fully rolled out, the flag and its gated code become technical debt and can introduce operational risk through inadvertently enabling dorman…

- **[AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments](https://arxiv.org/abs/2610.31326v1)**
  - *Ze-Yu Peng, Qing-Yu Lan, Zhan-He Wang et al.*
  - `2026-10-22`
  - Evolutionary program search with large language models keeps the structure of an evolutionary algorithm and uses the model as its variation operator. Typically, the model generates each candidate program in a single request from parent programs and their scores. We present Agenti…

- **[Subgoal-aware Memory Graph for GUI Agent](https://arxiv.org/abs/2610.31307v1)**
  - *Dezhao Luo, Daniel Beechey, Derek Yuen et al.*
  - `2026-10-22`
  - GUI agents aim to automate complex user tasks by interacting with mobile interfaces, but ef- fective decision-making in long-horizon set- tings requires reusing prior experience rather than relying solely on the environment ob- servations. Existing memory-based methods typically…

- **[Superintelligent Software Engineering: Governance That Scales with Capability](https://arxiv.org/abs/2610.31306v1)**
  - *Mohammad Mehdi Gholinejad*
  - `2026-10-22`
  - Software agents are being trained to exceed human engineers; we argue that capability alone does not produce better software engineering. We define superintelligent software engineering as the discipline of building and evolving software with agents whose capability exceeds that…

- **[The Value of Memory in Language Agents](https://arxiv.org/abs/2610.31303v1)**
  - *Zehao Lin, Erenkai Zhu, Helan Hu et al.*
  - `2026-10-22`
  - Memory enables language agents to carry useful distinctions from past experience into future decisions. Its value depends on which distinctions survive, whether a bounded agent can use them, and what can be recovered or revised as demands evolve. We develop a decision-theoretic f…

- **[RecallGS: Geometry-Grounded Recall for Online Semantic Gaussian Splatting](https://arxiv.org/abs/2610.31293v1)**
  - *Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran*
  - `2026-10-22`
  - Online semantic 3D Gaussian Splatting (3DGS) enables open-vocabulary scene understanding from streaming observations. However, existing methods recover geometric context missing from image-derived semantic features using an additionally learned 3D network, incurring extra trainin…

- **[Beyond Accuracy: Disentangling Decomposition from Typed-State Quality Assurance in Multi-Agent LLM Pipelines](https://arxiv.org/abs/2610.31280v1)**
  - *Maria Gabriela Alves Zuppardo, Vinicius Cardoso Garcia*
  - `2026-10-22`
  - Multi-agent LLM pipelines are often credited with gains in software engineering tasks, but it is rarely clear whether a gain stems from the typed contract between agents or from the specialized prompts that decomposition enables. We study this attribution problem in Requirements…

- **[RIPPLE: Recovery Internalization through Process-Level Policy Learning and Effect-Aware Credit for Long-Horizon Agentic Coding](https://arxiv.org/abs/2610.31276v1)**
  - *Jingxuan Xu, Zihang Xu, Yuechen Luo et al.*
  - `2026-10-22`
  - Long-horizon coding agents can observe a failure and generate a plausible critique yet continue along the same incorrect trajectory. We call this the Critique-to-Action Handoff Gap. We introduce RIPPLE, a recovery-oriented training framework that internalizes process-level guidan…

- **[Network topology shapes consensus and vulnerability in LLM populations](https://arxiv.org/abs/2610.31165v1)**
  - *Roberto Passaro, Ariel Flint, Romualdo Pastor-Satorras et al.*
  - `2026-10-22`
  - As large language models (LLMs) are deployed in interacting populations, their collective behaviour depends not only on the models but also on who interacts with whom. Studies of convention formation in LLM populations have mainly tested well-mixed interactions. We place policies…

- **[Post-Audit Mirage: Identifiability Limits of Offline Agent Verification](https://arxiv.org/abs/2610.31130v1)**
  - *Aman Behera, Payal Payal*
  - `2026-10-22`
  - Offline tests can fail to reveal whether an agent update will remain safe after deployment. We operationalize this post-audit mirage using matched safe and harmful lifecycles that expose identical verifier-visible evidence while an isolated scorer records opposite deployment trut…

- **[ProductWebBench: Evaluating Website Continuity Beyond Task Completion](https://arxiv.org/abs/2610.31118v1)**
  - *Jiajun Wu, Jian Yang, Yaxin Du et al.*
  - `2026-10-22`
  - Frontend coding agents are usually graded on one question: did the requested target get built. Real engineering changes carry a second obligation, because the rest of the site has to keep working. We call that second obligation website continuity, and introduce ProductWebBench, a…

- **[Can AI Co-Design Structures? An AI Agent for Early-Stage Structural Design](https://arxiv.org/abs/2610.31113v1)**
  - *Ricardo Maia Avelino, Mennatallah El-Assady, Tom Van Mele et al.*
  - `2026-10-22`
  - Recent advances in large language models and agentic workflows offer a new paradigm to early-stage structural design translating design intent into structural models. Although text-to-3D approaches have demonstrated that natural language can be used to produce visual, mesh-based…

- **[Who Is the Influencer? Consensus Dynamics in Multi-Agent Systems](https://arxiv.org/abs/2610.31105v1)**
  - *Gouki Minegishi, Jingyuan Feng, Hiroki Furuta et al.*
  - `2026-10-22`
  - Multi-agent LLM systems are increasingly used in practice, but their behavior is complex and hard to understand. We design a simple task to ask which model has the most influence on the final consensus when several models are mixed in one system. Experimentally, across seven mode…

- **[Co-Recursive Semantic Self-Extension: A Mathematical Foundation for Open-Ended Intelligence](https://arxiv.org/abs/2610.31097v1)**
  - *Simon Hegelich, Bardh Prenkaj, Habiba Sarhan et al.*
  - `2026-10-22`
  - Artificial intelligence has advanced through scale, data, and computation, yet remains bounded by its representational framework. We ask what makes intelligence open-ended. Every inferential system selects meaningful distinctions, limiting what it can learn. Within a fixed purpos…

- **[Dual Exam: Controlled Evaluation of Multimodal Agents and World Models](https://arxiv.org/abs/2610.31066v1)**
  - *Zhefan Rao, Meng Chu, Xuan Zhang et al.*
  - `2026-10-22`
  - World Models (WMs) can support Multimodal Agents (MAs) through simulated experience, while Agent trajectories can inform World Model refinement. Evaluating this interaction requires separate evidence about action selection and state evolution. We introduce Dual Exam, which tests…

- **[Algorithmic drift in generative adaptive learning](https://arxiv.org/abs/2610.31041v1)**
  - *Firuz Kamalov, Hana Sulieman, Ahmed El Sayed et al.*
  - `2026-10-22`
  - Generative artificial intelligence promises to democratize personalized tutoring, yet the longitudinal stability of adaptive systems remains under-theorized. Current ethical discourse focuses on static bias. This paper argues that a distinct threat lies in algorithmic drift: a fe…

- **[CANNBot-CAKE: Collaborative Agentic Kernel Evolution for Ascend NPU](https://arxiv.org/abs/2610.31034v1)**
  - *Deng Pan, Xue-Jian Gao, Junyi Fan et al.*
  - `2026-10-22`
  - Efficient custom operators are essential for modern deep learning workloads, yet developing high-performance kernels for Ascend NPUs remains slow, expert-intensive, and difficult to automate. Although AI agents now approach expert performance on GPU kernel benchmarks, current mod…

- **[Metacognitive Scaffolds Create Productive Friction for AI-Assisted Knowledge Work](https://arxiv.org/abs/2610.30945v1)**
  - *Viktor Kewenig, Lev Tankelevitch, Sean Rintel et al.*
  - `2026-10-22`
  - Generative AI imposes new metacognitive demands on knowledge workers as their work shifts from production to planning, evaluation, and orchestration. In a randomized, between-subjects experiment on AI-assisted writing (297 workers, 594 essays), we test dynamically-generated metac…

- **[Harnessing Language Models as Optimization Modeling Agents](https://arxiv.org/abs/2610.30917v1)**
  - *Yunxiang Luo, Xin Xu, Tianhao Chen et al.*
  - `2026-10-22`
  - Large language models (LLMs) can translate natural-language optimization problems into solver programs, but reliably producing correct formulations and implementations remains challenging. Existing approaches improve optimization modeling through agentic workflows or task-specifi…

- **[Separate Field Scoring Protects Unused Tools When Agents Pool Tool-Use Experience](https://arxiv.org/abs/2610.30867v1)**
  - *Abhijit Chakraborty*
  - `2026-10-22`
  - Agents that call tools from a shared catalog can pool what they learn about which tool serves which request. We measure what pooled usage examples do to tool retrieval, reporting separately the held-out tools, for which no agent has usage, and all other tools. Adding usage exampl…

- **[ADAPT for Science: A Multi-Agent System for Self-Evolving Scientific Optimization](https://arxiv.org/abs/2610.30851v1)**
  - *Zhaoran Feng, Yuchen Ni, Jianan Liu et al.*
  - `2026-10-22`
  - Scientific discovery often requires identifying a small number of high-performing designs in vast, constrained search spaces. This is difficult when evaluations are costly, feasible solutions are sparse, parameters are strongly coupled, and physical constraints are strict. Recent…

- **[What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight](https://arxiv.org/abs/2610.30803v1)**
  - *Ahmed M. Mahran*
  - `2026-10-22`
  - Replacing the judge can move a benchmark score, and models can be trained to hide capabilities. Both put the evaluator in question: what can it certify? We develop a partition theory of evaluation from one principle: judgement is bounded by perception. An agent's discrimination i…

- **[Agentic Knowledge-Model Co-Evolution via Consistency Regularization](https://arxiv.org/abs/2610.30790v1)**
  - *Sirui Chen, Zhining Liu, Chao Zhang et al.*
  - `2026-10-22`
  - LLM agents can evolve by learning from accumulated experience. Existing approaches extract reusable external knowledge, such as skills and memories, from experience to guide subsequent task solving, with some further internalizing this knowledge through model training. However, d…

- **[An Introduction to World Models for Generalist Agents](https://arxiv.org/abs/2610.30789v1)**
  - *Zhihui Zhu*
  - `2026-10-22`
  - World models have recently emerged as a promising direction toward developing generalist agents capable of understanding, predicting, and interacting with diverse environments. However, despite growing interest, the concept of a world model remains loosely defined, encompassing a…

- **[LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades](https://arxiv.org/abs/2610.30769v1)**
  - *Farnoosh Hashemi, Shiyu Ji, Joice Chen et al.*
  - `2026-10-22`
  - Large language models (LLMs) increasingly operate in multi-agent systems where they collaborate by responding to others' choices, creating endogenous feedback loops with vulnerability to social influence, herding behavior and runaway cascades. Following the design of the classic…

- **[AgentDP: Towards Automated Model Deployment for Heterogeneous Embedded AI Applications](https://arxiv.org/abs/2610.30760v1)**
  - *Leming Shen, Qiang Yang, Xinyu Huang et al.*
  - `2026-10-22`
  - This paper presents AgentDP, which aims to deploy pre-trained AI models on heterogeneous embedded devices by fully automating model optimization and adaptation (O&A) with Large Language Model (LLM) agents. AgentDP not only significantly reduces human effort via automation but als…

- **[The Delegation Divide: An Open Index of AI-Agent Delegability across Occupations and Countries](https://arxiv.org/abs/2610.30752v1)**
  - *Cristian Espinal Maya, Santiago Jiménez Londoño*
  - `2026-10-22`
  - 35.2% of task time in world employment is at least partly delegable to AI agents in 2026, and only 2.5% can be handed over in full. Existing measures score exposure to generative AI, mostly for the United States. We build the Agent Delegability Index (ADI): two language models ra…

- **[ULME: Predictive Coupling for Mutually Reinforcing Embedding and Language Modeling](https://arxiv.org/abs/2610.30705v1)**
  - *Yang Liu, Zhiqiang Yuan, Shu-Dong Huang et al.*
  - `2026-10-22`
  - Text embedding and text generation are two of the most useful capabilities of modern large language models, yet they are typically provided by separate specialized models (an embedder and a generator) trained with incompatible objectives and deployed side by side in retrieval-aug…

- **[A Topology-Guided GeoAI Agentic Framework for Urban Flood Screening](https://arxiv.org/abs/2610.30660v1)**
  - *Yutian Tao, Haoan Feng, Xin Xu et al.*
  - `2026-10-22`
  - Open-world geographic artificial intelligence (GeoAI) agents can transform public geospatial data into accessible decision support for real-world challenges, but must balance autonomous reasoning with reliable spatial analysis and human oversight. We present a topology-guided Geo…

- **[Anticipating Social Consequences with Distributional World Models](https://arxiv.org/abs/2610.30657v1)**
  - *Viet-Thanh Pham, Thuy-Trang Vu, Zhuang Li et al.*
  - `2026-10-22`
  - Social world models predict how interactions develop after an action, helping agents negotiate, cooperate and mediate. In these situations, one action can lead to several plausible futures, hence predicting only one future can overlook consequential alternatives, while exploring…

- **[Asking Less, Adapting Better: Feedback-Efficient Test-Time Adaptation for Vision-and-Language Navigation](https://arxiv.org/abs/2610.30643v1)**
  - *Zixu Wang, Huaquan Zhang, Shoukai Xu et al.*
  - `2026-10-22`
  - Vision-and-Language Navigation (VLN) requires agents to follow instructions and navigate to target locations. However, current VLN agents often suffer severe performance degradation in unseen environments due to distribution shifts. Test-Time Adaptation (TTA) offers a promising p…

- **[Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for Efficient and Reliable Inference](https://arxiv.org/abs/2610.30611v1)**
  - *Amirhossein Aghaei, Liangyan Li, Shiyi Yang et al.*
  - `2026-10-22`
  - Scaling large language models has substantially improved linguistic fluency, yet reliable autonomous agents require more than fluent generation. In multi-turn inference, current agentic systems often produce semantically plausible but structurally ungrounded reasoning, especially…

- **[Diagnosing Personalization Failures in Mobile GUI Agents](https://arxiv.org/abs/2610.30573v1)**
  - *Zhixin Lin, Dongliang Xu, Jungang Li et al.*
  - `2026-10-22`
  - Unlike conventional GUI agents, personalized GUI agents require user preferences to guide sequential execution over changing GUI states. This raises two challenges: determining HOW each preference should alter execution strategy and WHEN it should take effect along the interactio…

- **[Lifetime-valid decisions by continually evolving AI analysts](https://arxiv.org/abs/2610.30562v1)**
  - *Xiaojing Sun, Yuhan Zeng, Xiao Wang*
  - `2026-10-22`
  - AI agents increasingly act as analysts whose decision can often be cast as hypothesis tests. Classical tests control the Type I error rate, the probability of rejecting a true null hypothesis, for fixed procedures. However, AI analysts introduce internal randomness and can evolve…

- **[Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core](https://arxiv.org/abs/2610.30557v1)**
  - *Yebo Feng, Jingyang Dai, Liangrui Pan et al.*
  - `2026-10-22`
  - LLM agents that act on live Web data must combine heterogeneous evidence, remember what they have done and improve from outcomes without weakening their own safeguards. We study this problem in autonomous investing, where every action is irreversible and based on untrusted Web co…

- **[Reliable AI-Assisted Decisions via Selective Auditing](https://arxiv.org/abs/2610.31662v1)**
  - *Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani et al.*
  - `2026-10-22`
  - We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by th…

- **[Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.31544v1)**
  - *Zeropy Surio, Tobias Engel, Mei-Lin Chou et al.*
  - `2026-10-22`
  - Agentic reinforcement learning rewards a complete episode, yet the policy needs credit for every decision inside it. Counterfactual branching estimates this credit by re-running the episode after an alternative decision, but the branch draws its sampling noise independently of th…

- **[AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents](https://arxiv.org/abs/2610.31366v1)**
  - *Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian et al.*
  - `2026-10-22`
  - Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral a…

- **[ReDence: A Hybrid Agentic and Decision-Model Framework for Rapid, Evidence-Grounded Detection of Modern Social Engineering Scams](https://arxiv.org/abs/2610.30963v1)**
  - *Jaishnoor Kaur, Josef Horáček, Ian Waskom et al.*
  - `2026-10-22`
  - Detecting online social engineering (SE) scams often requires examining website workflows, verifying claims against external sources, and connecting evidence across multiple pages. Existing detectors provide limited support for these investigations, leaving analysts to manually g…

- **[Building Presentation Intelligence for High-Quality Slide Generation](https://arxiv.org/abs/2610.30888v1)**
  - *Yuhang Xie, Cheng Li, Chenliang Li et al.*
  - `2026-10-22`
  - PowerPoint presentations (PPTs) are a dominant medium for communication across diverse domains, yet high-quality PPT generation still depends heavily on labor-intensive human effort. Recent advances in large language models (LLMs) for agentic tasks have created both new opportuni…

- **[Lean Finder V2: Semantic Search for Mathlib That Disambiguates User Queries](https://arxiv.org/abs/2610.30843v1)**
  - *Jialin Lu, Xiaoyu Liu, Hengrui Luo et al.*
  - `2026-10-22`
  - We introduce Lean Finder V2, a semantic search framework for Mathlib that disambiguates user queries through complementary model-level adversarial training and input-level query rewriting. Human mathematicians and coding agents rarely search Mathlib by providing detailed context.…

- **[Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving](https://arxiv.org/abs/2610.30791v1)**
  - *Maharani A. P. Irawan, Kuntai Du, Jiayi Yao et al.*
  - `2026-10-22`
  - KV caching reduces the serving cost of large language models (LLMs), but the growing KV cache footprint is increasingly exceeds GPU and host-memory capacity. Therefore, people use SSD to expand the KV cache storage capacity with high I/O bandwidth. However, in production LLM work…

- **[Solvable models of learning to pursue a moving target](https://arxiv.org/abs/2610.30721v1)**
  - *John J. Vastola, Kanaka Rajan*
  - `2026-10-22`
  - Agents tasked with intercepting a moving target must learn how to reach it, ideally as efficiently as possible. As observers of animal pursuit behavior have noticed, different strategies are possible: on one extreme, the agent reactively moves toward the target's current location…

- **[An Agent Architecture with Tools and Memory for Selective Correction of Wrist PPG Heart Rate Estimates](https://arxiv.org/abs/2610.30688v1)**
  - *Xu Wang, Shuhan Yi, Zhen Cheng*
  - `2026-10-22`
  - Wrist photoplethysmography (PPG) heart rate estimates are vulnerable to motion artifacts, and corrections that reduce mean error can worsen individual windows. We propose an agent architecture with tools and memory around a fixed heart rate estimator. Pulse, motion, and limited h…

- **[Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2](https://arxiv.org/abs/2610.31636v1)**
  - *Marek Šuppa, Ivan Vykopal, Jaroslav Kopčan*
  - `2026-10-22`
  - Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather than a classifier: a tool-using agent explores the corpus through a read-only, bu…

- **[Learning What to Ask for Tomorrow: Active Preference Acquisition for Long-Term Personalized Web Agents](https://arxiv.org/abs/2610.31107v1)**
  - *Yiqi Wang, Zizhi Zeng, Jiaqi Zhang et al.*
  - `2026-10-22`
  - Web agents increasingly serve the same user across repeated online tasks such as booking travel, shopping, and scheduling, so their long-term usefulness depends on how well they know the user's preferences. Passive memory and personalization methods cannot obtain preferences the…

- **[ReflectPO: Reflection-Guided Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.30933v1)**
  - *Rumei Li, Xunliang Cai*
  - `2026-10-22`
  - With external tools, large language models (LLMs) can tackle complex tasks through sustained environmental interaction. LLM-based agents are therefore increasingly used to tackle complex long-horizon tasks in real-world environments. However, these tasks involve sequential, inter…

- **[UniGuard: Multi-View Guardrail Learning for Cross-Interface Safety Generalization](https://arxiv.org/abs/2610.30742v1)**
  - *Viet-Thanh Pham, Thuy-Trang Vu, Junae Kim et al.*
  - `2026-10-22`
  - Guardrail models are increasingly used as safety layers for LLMs and agentic systems, but most are trained on fixed prompt or response interfaces and become unreliable when the same safety case appears as a conversation, agent trajectory, multi-agent trace, or policy-conditioned…

- **[Decentralized Bi-Level Optimization for Cooperative Orbital Transportation of a Rigid Payload](https://arxiv.org/abs/2610.31562v1)**
  - *Sidhdharth D. Sikka, Revathy Ravuri, Hei Yin Jowett Chan et al.*
  - `2026-10-22`
  - The rapid growth of the space economy, alongside increasing orbital congestion and debris, is driving demand for reliable on-orbit transportation of large and non-cooperative objects. Performing such transportation with a swarm of small spacecraft distributes risk and removes the…

- **[When Is a Memory Safe Enough to Act On? Action-Conditioned Verification for Long-Lived Agents](https://arxiv.org/abs/2610.31446v1)**
  - *Yiqi Wang, Yifei Wang, Jiaqi Zhang et al.*
  - `2026-10-22`
  - Long-lived agents act on memory carried across sessions, and many of their actions are irreversible, so a stale memory can turn directly into harm. Existing work improves the memory itself --- retrieving, refreshing, or reconciling entries --- yet whether an entry must be re-chec…

- **[Probabilistic Energy Modeling Unifies Versatile Swarm Control](https://arxiv.org/abs/2610.31371v1)**
  - *Xiang Zhou, Xiangyu Zhu, Xintong Wang et al.*
  - `2026-10-22`
  - Robotic swarms must coordinate across diverse missions, yet existing controllers often require redesign, retuning, or retraining when objectives change. Here we show that probabilistic energy modeling provides a unifying representation for versatile swarm control, in which divers…

- **[Consistent but Biased: Chair Personas Trade Noise for Bias in Multi-Agent Clinical Decisions](https://arxiv.org/abs/2610.31325v1)**
  - *Yitong Bai, Chengyi Zhang, Ziyang Wang*
  - `2026-10-22`
  - In clinical systems built from several large language model (LLM) agents, one agent often chairs the discussion and makes the final decision. Whether the chair's persona prompt changes that decision, or the agreement between repeated runs that some systems treat as reliability, h…

- **[Consensus-Based Distributed Filtering for Angles-Only Tracking in Cislunar Space](https://arxiv.org/abs/2610.30864v1)**
  - *Giovanni Romagnoli, Fabrizio Pilone, Giordana Bucchioni*
  - `2026-10-22`
  - This paper investigates consensus-based distributed filtering strategies for multi-observer angles-only navigation in the cislunar space. The objective is to estimate the inertial state of a target spacecraft using only line-of-sight measurements collected by a network of observe…

- **[ABRA: Agent-Bound UI for Human-Agent Communication beyond Chat with Reusable Views](https://arxiv.org/abs/2610.30780v1)**
  - *Seon Gyeom Kim, Hannah Kim*
  - `2026-10-22`
  - Agents can create rich representations, yet these representations are rarely used as a medium for expressing user intent. We present Agent-Bound UI, an interaction model that separates reusable interaction structures from task-specific meanings. Agents bind task-specific meanings…

- **[PLE: Physical-Engineering's Last Exam](https://arxiv.org/abs/2610.30537v1)**
  - *Rujun Han, Yufan Zhuang, Arijit Ray et al.*
  - `2026-10-21`
  - Frontier language models now score above 90% on popular knowledge benchmarks and are increasingly deployed as agents that carry out multi-hour professional work. Yet no existing benchmark tests whether they can perform the real-world, economically valuable work of a professional…

- **[LLM2Cert: LLM Synthesis of Certificates with SMT/Lean Verification](https://arxiv.org/abs/2610.30524v1)**
  - *Zhipeng Cao, Peiyang Song, Nikolaus Vertovec et al.*
  - `2026-10-21`
  - Lyapunov functions and barrier certificates give state-space guarantees of stability and safety, but synthesizing and verifying them---especially for nonlinear, high-dimensional systems---remains an open challenge. Existing pipelines verify candidates with numerical solvers (sum-…

- **[Can LLMs Improve Their Own Harness? A Controlled Study on ARC-AGI-3](https://arxiv.org/abs/2610.30499v1)**
  - *Jens Lehmann, Sahar Vahdati*
  - `2026-10-21`
  - A generally intelligent system acquires new skills efficiently without requiring humans to redesign its software scaffold for every new task. Yet language models rarely act alone. A harness is a symbolic program that orchestrates calls to the model, handling perception, memory, t…

- **[From Prose to Properties: Testing Research Claims with ARATest for Agent-Native Science](https://arxiv.org/abs/2610.30495v1)**
  - *Yifeng He, Jiachen Liu, Hao Chen*
  - `2026-10-21`
  - AI agents now run experiments and report findings, so research produces claims faster than researchers can check them. Each empirical claim implies a property that must hold over its cases, but it states that property only in prose. Without an explicit property, no test can decid…

- **[What the Trace Shows and What the Label Says: Auditing Behavioral Detectors in Agent Evaluation](https://arxiv.org/abs/2610.30491v1)**
  - *Idunnuoluwa A. Adeniji, Shilpika, Michael E. Papka*
  - `2026-10-21`
  - LLM agents are often evaluated by reducing execution traces to labels such as final-answer correctness, tool verification, and fault propagation. These labels are measurements produced by parsers, behavioral detectors, and harness rules, and they may not fully capture what the tr…

- **[From Single-Actor Environments to Multi-Actor Event Worlds: Can LLMs Be Event World Models?](https://arxiv.org/abs/2610.30488v1)**
  - *Juntong Ni, Zewen Liu, Bohan Wang et al.*
  - `2026-10-21`
  - World models help agents assess the consequences of their actions before acting. Many real systems, however, involve multiple actors who make their own decisions, can evolve even when the agent takes no action, and are only partially observed through event logs. We formalize thes…

- **[Externalise the Memory: A Pre-Registered Study of Where an Embodied Agent's Experience Should Live](https://arxiv.org/abs/2610.30478v1)**
  - *Cheng-Yin Tu*
  - `2026-10-21`
  - Should an embodied agent's experience be baked into its policy weights, or kept external and retrieved at inference? A memory-augmented teacher (a VLM that retrieves lessons, with their episode images, from its own past attempts) produces trajectories on a vision-conditioned reac…

- **[Same Beliefs, Different Policies: Learning Reusable Representations for Early Stopping in LLM Reasoning](https://arxiv.org/abs/2610.30450v1)**
  - *Jingwei Ni, Dmitry Abulkhanov, Vladislav Smirnov et al.*
  - `2026-10-21`
  - Reasoning LLMs often continue reasoning after reaching a correct answer, wasting computation and sometimes replacing it with an incorrect one. Deciding when to stop is a metareasoning problem: the model must weigh what further reasoning could achieve against its cost, given what…

- **[A Three-Pillar Governance Framework for Safe and Trustworthy AI Agents](https://arxiv.org/abs/2610.30445v1)**
  - *Edward C. Cheng, Jeshua Cheng, Alice Siu*
  - `2026-10-21`
  - AI agents capable of autonomous decision-making introduce significant challenges related to safety, alignment, accountability, and human oversight. Existing Human-in-the-Loop (HITL) and responsible AI approaches provide important foundations, but many remain fragmented across sys…

- **[SpecMAGIC: Specification-Guided Multi-Task Generalization in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.30443v1)**
  - *Zijian Guo, İlker Işık, H. M. Sabbir Ahmad et al.*
  - `2026-10-21`
  - Multi-task generalization is an important yet underexplored problem in multi-agent reinforcement learning (MARL). Many real-world applications require multi-agent systems to generalize across complex, temporally extended tasks with diverse inter-agent coordination requirements. W…

- **[Secure Agentic AI and Multimodal Intelligence in 6G Communication Systems](https://arxiv.org/abs/2610.30436v1)**
  - *Satyam Gaba, Devanshu Motwani, Siva Sai et al.*
  - `2026-10-21`
  - Sixth-generation (6G) communication systems are expected to support immersive, intent-driven, and latency-critical services through tight integration of multimodal intelligence, edge computing, and autonomous network control. In this setting, agentic AI systems can reason over he…

- **[Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2610.30435v1)**
  - *Taewhoo Lee, Minju Song, Jungwoo Park et al.*
  - `2026-10-21`
  - Recent advances in search agents have enabled large language models to tackle complex tasks by retrieving and synthesizing external information. However, existing search agents often lack search-state awareness, i.e., the ability to recognize what information has been obtained an…

- **[RoleFlow: Self-Evolving Multi-Role Agentic Collaboration via Structural Adaptation](https://arxiv.org/abs/2610.30429v1)**
  - *Yi Ge, Pan Wang, Xuehao Cui et al.*
  - `2026-10-21`
  - Large language model (LLM) based multi-agent systems often rely on predefined collaboration structures, limiting their adaptability to evolving task requirements. Although recent approaches enable dynamic orchestration, trajectory-level rewards they apply assign one outcome to ea…

- **[Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems](https://arxiv.org/abs/2610.30418v1)**
  - *Daniel Ruiz, Luca Luceri, Emilio Ferrara*
  - `2026-10-21`
  - Modern LLM agents can retrieve information from accessible documents, and then disclose a sensitive conclusion assembled from them. This mosaic effect creates a critical risk for agents operating over confidential data. We quantify its realization with 30 synthetic cybersecurity,…

- **[MemPlan: Memory-Conditioned PDDL Planning for Partially Observable Text Environments](https://arxiv.org/abs/2610.30379v1)**
  - *Tengwei Song, Robert Hoehndorf*
  - `2026-10-21`
  - LLM agents are flexible in language interaction, but using them as long-horizon planners is costly and prone to hallucinated or invalid actions. This paper targets a different role for LLMs: constrained bridges between language and symbolic planning. We propose MemPlan, a memory-…

- **[GAV: A scientific experimentation environment for PDE agents](https://arxiv.org/abs/2610.30292v1)**
  - *Muheng Li, Wenlong Mou*
  - `2026-10-21`
  - Reliable feedback is essential for coding agents to develop programs for partial differential equations (PDEs). Yet evaluating these programs on new PDE problems often requires expensive reference computations, while fixed datasets restrict the range of experiments. We introduce…

- **[SWE-VERIFIER: Selective Verification for Cost-Efficient Coding Agents](https://arxiv.org/abs/2610.30284v1)**
  - *Kaijian Zou, Vaibhav Chennareddy, Yunxiang Zhang et al.*
  - `2026-10-21`
  - Coding agents spend substantial computation generating actions and processing long interaction histories. Poor action choices can steer agents into low-value states, wasting computation and increasing API costs. Sampling and verifying alternative actions can improve the agent's d…

- **[Breaking the high-degree barrier in Lehmer's problem with a human-AI discovery loop](https://arxiv.org/abs/2610.30277v1)**
  - *Yuri Chervonyi, Sergei Gukov, Thang Luong*
  - `2026-10-21`
  - While artificial intelligence has made rapid progress in mathematical reasoning, many open problems depend on structure that is revealed only through large-scale computational exploration and analytical synthesis. One such example is Lehmer's problem from 1933. It asks whether th…

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

- **[Retrieval Augmented Generation Compositionality](https://arxiv.org/abs/2610.29722v1)**
  - *Ido Levy, Segev Shlomov, Leshem Choshen*
  - `2026-10-21`
  - Retrieval Augmented Generation (RAG) grounds large language models in external knowledge. Modern pipelines combine embedding, chunking, retrieval, reranking, query augmentation, context compression, and agentic verification, yet these techniques are typically evaluated one at a t…

- **[Conflicted Records: Typed Adversarial Contracts for Auditable LLM Output Quality Enforcement](https://arxiv.org/abs/2610.29669v1)**
  - *Kardelen Subasi, Jarosław A. Chudziak*
  - `2026-10-21`
  - LLM-generated records increasingly populate production information systems where they are treated as data assets subject to the same quality expectations as records from operational databases. A single such record can simultaneously satisfy and violate a quality rule: a grounded…

- **[Feedback That Backfires in Games: Do LLM Players Repeat the Move They Just Watched Fail?](https://arxiv.org/abs/2610.30205v1)**
  - *Esmail Gumaan*
  - `2026-10-21`
  - When an LLM agent's move fails, the harness writes the move and the failure message into the transcript and asks again. In tool calling, this record makes small models more likely to repeat the failed action. We test whether the same holds in games (Sokoban, Connect Four, Othello…

- **[The Reflexivity Threshold: A Phase Transition for Multi-Agent Performative Prediction](https://arxiv.org/abs/2610.29577v1)**
  - *Ahmed Mahrous, Roberto Di Pietro*
  - `2026-10-21`
  - Many learning systems are performative: once deployed, their predictions change the data distribution on which future models are trained. In multi-agent settings, this feedback is routed through a network of interacting learners, so stability depends not only on the strength of p…

- **[MPIDetector: Detecting Multi-modal Prompt Injection via LLM-based Reasoning](https://arxiv.org/abs/2610.30202v1)**
  - *Yiheng Li, Jingyue Li*
  - `2026-10-21`
  - With the rapid integration of Multi-modal Large Language Models (MLLMs) into real-world applications, Prompt Injection (PI) has emerged as a critical security threat. Attackers can conceal malicious instructions within textual narratives or visual inputs to bypass safety alignmen…

- **[Rethinking Agentic Model Orchestration for Time Series Forecasting](https://arxiv.org/abs/2610.29504v1)**
  - *Tong Guan, Tianxiang Zhan, Shirui Pan et al.*
  - `2026-10-21`
  - Time series foundation models (TSFMs) perform unevenly across forecasting tasks. Recent work uses agentic model orchestration (AMO) to select or combine TSFMs, often outperforming individual forecasters. Yet these gains may reflect stronger or more complementary candidates rather…

- **[PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents](https://arxiv.org/abs/2610.29467v1)**
  - *Jian Zhong, Zeyu Liu, Pingchuan Cao et al.*
  - `2026-10-21`
  - Long-horizon dialogue agents need to keep user memories stable enough for personalization while adapting when the user genuinely changes. Existing memory systems often append every observation or overwrite old entries by heuristic rules, which makes transient noise hard to distin…

- **[Harness Scaling for Generalizable Agentic Reinforcement Learning](https://arxiv.org/abs/2610.29458v1)**
  - *Fei Bai, Huatong Song, Chuan Hao et al.*
  - `2026-10-21`
  - Agent harnesses have become a central component of modern agentic systems, shaping how models use tools, manage context, and coordinate long-horizon interaction. Realizing the benefits of these harnesses depends on how effectively the underlying model can make use of them, motiva…

- **[RegoMender: A Multi-agent Framework for Automated Rego Policy Repair](https://arxiv.org/abs/2610.29456v1)**
  - *Ruijie Zhang, Huaxiao Yin, Li Hu et al.*
  - `2026-10-21`
  - Policy-as-Code (PaC) has emerged as a foundational paradigm in cloud-native systems. However, repairing Rego policies remains challenging due to their strict syntax, declarative semantics, and specific verification requirements. Existing automated program repair (APR) methods are…

- **[Beyond Small Talk: Modeling Disclosure Trajectories in Human-AI Conversation](https://arxiv.org/abs/2610.29413v1)**
  - *Keith Kwok, Wanting Ning, Tej Deep Pala et al.*
  - `2026-10-21`
  - Recently, we see a rise in conversational agents as a form of social and emotional support, where disclosure will unfold over time. Yet, current evaluations of these agents typically examine isolated conversational states. In analyses of naturally occurring conversations, disclos…

- **[Memory-Centric Continual Learning for AI Agents](https://arxiv.org/abs/2610.29357v1)**
  - *Dongfang Li, Zhuoen Chen, Bonian Jia et al.*
  - `2026-10-21`
  - Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive ret…

- **[From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?](https://arxiv.org/abs/2610.29331v1)**
  - *Linus Filbry, Luckeciano C. Melo, Yarin Gal*
  - `2026-10-21`
  - Large language models (LLMs) are increasingly applied across the scientific discovery pipeline, from synthesizing literature to generating hypotheses to informing experimental design. A unifying principle behind these tasks is the need to continuously update beliefs as evidence a…

- **[AgentMonopoly: Behavioral Patterns and Persona Control in LLM Agents](https://arxiv.org/abs/2610.29330v2)**
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

- **[Learning to Incentivise: Using Reinforcement Learning for Sustainable Urban Mobility](https://arxiv.org/abs/2610.30469v1)**
  - *Germán Pardo-González, Shaghayegh Vosough, Katerina Papadaki et al.*
  - `2026-10-21`
  - Traffic management has traditionally focused on toll-based and road pricing solutions. However, road pricing often raises concerns about accessibility and public dissatisfaction, leading to its prohibition in some places, such as Finland. This study optimises the dynamic allocati…

- **[Circuits of LLM Classifiers](https://arxiv.org/abs/2610.30076v1)**
  - *Hadi Khalaf, Sajani Vithana, Kunal Talreja et al.*
  - `2026-10-21`
  - Language models make it easy to build classifiers by simply prompting a model with the sample to classify. However, their predictions are neither deterministic nor uniformly reliable across samples. How can we combine predictions from different models to improve reliability? We v…

- **[CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents](https://arxiv.org/abs/2610.29965v1)**
  - *Wenhao Yu, Zhengcheng Wang, Jiahong Liu et al.*
  - `2026-10-21`
  - Joint reinforcement learning and self-distillation combines task rewards with dense teacher guidance for agent training, but their gradients can partly cancel. A mixing coefficient controls relative scale without selectively removing opposing components. We present CORD, a genera…

- **[FrontierCS 2: A Benchmark for Computer Science R&D](https://arxiv.org/abs/2610.29932v1)**
  - *Qiuyang Mang, Wenhao Chai, Runyuan He et al.*
  - `2026-10-21`
  - Can LLM agents make contributions to frontier computer science R&D? We introduce FrontierCS 2, a benchmark of 48 open-ended tasks. We take a paper and the code its authors released and delete the paper's contribution. The deleted code becomes the human reference that sets the bar…

- **[AI Mindmeld: A Latent Interconnect Protocol](https://arxiv.org/abs/2610.30215v1)**
  - *Siavash Golkar, Jake Kovalic, Shirley Ho*
  - `2026-10-21`
  - LLMs can act as scientific agents using tools to consult specialists and run experiments. Yet specialist information must enter their context, generally as text, images, audio or video: a bottleneck between models with rich, high-dimensional representations. We advocate direct re…

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

- **[IFC-MCQ: Automatically Generating Multiple-Choice Benchmarks for Evaluating LLM Agents on IFC Data Retrieval](https://arxiv.org/abs/2610.30533v1)**
  - *Rabindra Lamsal, Sisi Zlatanova, Xuesong Shen*
  - `2026-10-21`
  - Industry Foundation Classes (IFC), the standard for building information exchange in architecture, engineering, and construction (AEC), is increasingly queried through large language models (LLMs) using natural language. Evaluating these systems at scale is difficult because free…

- **[SIM-UT: A User Simulation based Evaluation Framework for Medical Triage Chatbots](https://arxiv.org/abs/2610.30412v1)**
  - *Deepali Mittal, Dheeraj Mundhra, Yulia Sidorova et al.*
  - `2026-10-21`
  - LLM-based chat agents are increasingly used for complex, multi-turn, multilingual medical triage in low- and middle-income countries (LMICs), yet evaluation methods focus on single-turn, English-only benchmarks that primarily test the chatbots' knowledge. In practice, users are o…

- **[Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents](https://arxiv.org/abs/2610.29995v1)**
  - *Jielong Tang, Ling-An Zeng, Xujie Yuan et al.*
  - `2026-10-21`
  - Long-term memory for multimodal agents remains challenging, as it must preserve fine-grained visual evidence while tracking entity evolution across sessions. Existing abstraction-based memories compress images into text, often discarding visually discriminative details, whereas p…

- **[Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting](https://arxiv.org/abs/2610.29784v2)**
  - *Zhipeng Chen, Yunsen Liang, Yanxi Chen et al.*
  - `2026-10-21`
  - Most contemporary artificial intelligence (AI) systems are released with frozen parameters and improve through external updates, whereas an ideal system would keep improving from its own experience, a capacity we call recursive self-improvement (RSI). Yet studying RSI requires an…

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

- **[OACap: Caption-Guided Active Observation for Detailed Video Captioning](https://arxiv.org/abs/2610.29327v2)**
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

- **[Let Agents Design How They Search: Automatic Interface Optimization for Agentic Search](https://arxiv.org/abs/2610.29250v1)**
  - *Sangjune An, Jaeyoon Jung, Yumin Choi et al.*
  - `2026-10-21`
  - Agentic search depends on the interface through which a language-model agent accesses and explores a corpus. Existing interface designs are fixed by hand and applied unchanged to every corpus, although effective designs may depend on the corpus. We introduce SearchWeaver, a frame…

- **[Reasoning-Search-Augmented LLMs: An Operational Taxonomy, Benchmark Analysis and Controlled Evidence Synthesis](https://arxiv.org/abs/2610.29189v1)**
  - *Biswas Poudel, Nilson Chapagain, Amit Kumar et al.*
  - `2026-10-21`
  - Large language models (LLMs) demonstrate impressive emergent reasoning capabilities, yet they remain constrained by fixed model parameters and finite context windows. Even when augmented with static retrieval, they can produce statements that are unsupported by, or even contradic…

- **[VeeReview: Measuring Build-Verify Pairs in Agent-Authored Pull Requests from a V-Model Perspective](https://arxiv.org/abs/2610.29143v1)**
  - *Gabriel Dautovi, Jie JW Wu*
  - `2026-10-21`
  - Context: Reviewing a pull request requires verification evidence that addresses the proposed change. Coding agent benchmarks and studies of pull request outcomes do not directly assess this relationship. Objective: We test whether the V-Model's build and verify pairs can measure…

- **[Agentic Architecture of Information Systems. The AAM/5C Model: A Reference Model for Distributed Autonomy](https://arxiv.org/abs/2610.30221v1)**
  - *Laurent Goujon*
  - `2026-10-21`
  - Large organizations increasingly face what this book calls the cognitive complexity wall: at the scale of hundreds of interacting components, maintaining the dependency map and reacting at the pace of incidents exceeds what a human team can deliver. This conceptual volume propose…

- **[Resonance and Depth: Composing Timbral Identity and Spatial Form in an Artist-in-the-Loop Co-Creative Multi-Agent Percussive Performance](https://arxiv.org/abs/2610.29026v1)**
  - *Keon Ju Maverick Lee*
  - `2026-10-21`
  - This research-creation artistic report presents Resonance and Depth, a 9-minute immersive electroacoustic/acousmatic performance that treats timbre and space as primary compositional materials. Built from live electronic percussion and a personal corpus recorded, curated, and com…

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

- **[Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents](https://arxiv.org/abs/2610.28934v1)**
  - *Xu Li, Simon Yu, Minzhou Pan et al.*
  - `2026-10-20`
  - Coding agents now complete tasks autonomously, modifying real-world state such as artifacts, software environments, and configurations along the way. Yet they show limited backup awareness: recognizing that an action will modify state that may later be needed, and preserving it b…

- **[D-Skill: Distilling Teacher Knowledge through Agent Skills](https://arxiv.org/abs/2610.28914v1)**
  - *Shuo Yuan, Dacheng Li, Joseph E. Gonzalez*
  - `2026-10-20`
  - Frontier language-model agents excel at complex tasks, but high inference costs make transferring their capabilities to smaller models essential. Traditional knowledge distillation achieves this through parameter updates, requiring access to the student's weights and additional t…

- **[DiffResearch: Accelerating Deep Research with Diffusion Language Models](https://arxiv.org/abs/2610.28909v1)**
  - *Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov et al.*
  - `2026-10-20`
  - Deep research systems iteratively plan, gather evidence, synthesize, and revise, making end-to-end latency a key bottleneck for interactive use. Almost all production systems are built on autoregressive (AR) language models and inherit left-to-right decoding in planning and long-…

- **[JaxMARL-BC: Multi-Agent Reinforcement Learning for Macroeconomic Modelling, in Seconds](https://arxiv.org/abs/2610.28907v1)**
  - *Daniele Montagnani, Andrea Coletta, Antonietta Mira et al.*
  - `2026-10-20`
  - Multi-agent reinforcement learning (MARL) offers a principled way of populating simulated economies with many heterogeneous decision makers. Its adoption, pioneered in finance, has nonetheless been slow in macroeconomics because of two main limitations: the lack of a shared frame…

- **[Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for Latent Communication](https://arxiv.org/abs/2610.28905v1)**
  - *Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov et al.*
  - `2026-10-20`
  - Diffusion language models form answers through a sequence of revisable continuous states, but multi-agent systems usually discard those states and make agents communicate only after decoding text. We ask whether one independent diffusion trajectory can pass a compact hidden messa…

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

- **[Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?](https://arxiv.org/abs/2610.28763v1)**
  - *Ming Zhong, Stacy Li, Nicholas Carlini et al.*
  - `2026-10-20`
  - Frontier coding agents are increasingly framed as end-to-end automated researchers, and ML for science offers a demanding test of that promise: improving a scientific model often requires domain insight beyond routine ML engineering. We introduce Agent4Sci, a long-horizon testbed…

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

- **[Evolving Agent Interfaces](https://arxiv.org/abs/2610.28601v1)**
  - *Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega et al.*
  - `2026-10-20`
  - Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through a shell to find one function. Both the interfaces and the knowledge of when to u…

- **[Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation](https://arxiv.org/abs/2610.28586v1)**
  - *Shu Zhao, Tan Yu*
  - `2026-10-20`
  - Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable…

- **[SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images](https://arxiv.org/abs/2610.28585v1)**
  - *Rundong Luo, Yunong Liu, Di Cao et al.*
  - `2026-10-20`
  - Simulation is a powerful tool for robotics, but building diverse, simulation-ready scenes at scale remains difficult. Reconstructing scenes from single images is a promising alternative, but visual similarity alone is insufficient: objects must also be recovered, accurately place…

- **[Agentic Verified Optimization of Real-World Software](https://arxiv.org/abs/2610.30188v1)**
  - *Zhe Ye, Udaya Ghai, Zhizhen Qin et al.*
  - `2026-10-20`
  - Program optimization aims to improve performance while preserving behavior. Coding agents can already make programs faster by changing algorithms, data structures, and execution strategies. However, existing equivalence checks mostly rely on tests, which agents have been shown to…

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

- **[Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698v1)**
  - *Kuan Zhang, Yukun Chen, Zhihao Yang et al.*
  - `2026-10-20`
  - Scaling data, diversity and model capacity has improved embodied learning in physical environments, where diverse experiences remain grounded in shared physical laws. Whether these gains extend to virtual worlds with different visual styles, dynamics, controls, and objectives rem…

- **[Self-Evolving Static Analysis via LLM Pseudo-Labeling](https://arxiv.org/abs/2610.30184v1)**
  - *Rui Melo, Andre Duarte, Aditya Oke et al.*
  - `2026-10-20`
  - Security bugs often slip past static analysis not because they are impossible to detect, but because detection rules have not yet been written for the code in front of us. New frameworks, APIs, and coding idioms continually create such gaps, leaving developers to discover failure…

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

- **[S$^2$-MAS: A Society-Scale Multi-Agent Simulation Framework with 500 Million Household Persona Agents](https://arxiv.org/abs/2610.27746v3)**
  - *Yang Li, Yike Wang, Di Wan et al.*
  - `2026-10-20`
  - Simulating economic responses at society scale requires agents whose decisions reflect household circumstances and the effects of earlier actions. We introduce S$^2$-MAS, a society-scale multi-agent simulation framework built on 500 million synthetic household personas grounded i…

- **[Hearsay or Fact? How Framing and Elicitation Shape LLM Probability Updates](https://arxiv.org/abs/2610.27745v1)**
  - *An-Sheng Jhang*
  - `2026-10-20`
  - Large language models (LLMs) are increasingly used as judgment assistants and as stand-in participants in psychology experiments, yet little is known about how much their probability estimates move in response to a single new piece of information. We pair premise-hypothesis items…

- **[RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process?](https://arxiv.org/abs/2610.27735v2)**
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

- **[Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory](https://arxiv.org/abs/2610.28315v2)**
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

- **[Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures](https://arxiv.org/abs/2610.28887v1)**
  - *Yujian Liu, Li An, Zelin He et al.*
  - `2026-10-20`
  - Autonomous agents can increasingly propose ideas, modify code, and run experiments, creating an opportunity to accelerate scientific discovery using teams of collaborative AI researchers. To escape local minima in the discovery, we propose to encourage orthogonal exploration by c…

- **[Cache Engineering for Agents](https://arxiv.org/abs/2610.28577v1)**
  - *Tianyu Fu, Ruoxi Wang, Zihan Min et al.*
  - `2026-10-20`
  - Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache I/O and storage become the dominant cost. Trajectories can also exceed the LLM's maximum context len…

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


## Harness  (127)

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

- **[AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing](https://arxiv.org/abs/2608.29622)**
  - *{'fullname': 'Xinke Jiang', 'username': ''}, {'fullname': 'Yue Fang', 'username': ''}, {'fullname': 'Zhibang Yang', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2026-08-01`
  - Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts. Recent reinforcement learnin…

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

- **[ColaBench: Evaluating Memory-Guided Knowledge Acquisition in Personal Agents](https://arxiv.org/abs/2610.30989v1)**
  - *Wenjie Zhang, Zhichao Shi, Xuhui Jiang et al.*
  - **ACL** · `2026-10-22`
  - Personal agents need to draw on long-term interaction history to retrieve and apply external knowledge suited to a user's current request. Even an answer grounded in relevant documents can be unsuitable when it overlooks the user's circumstances. This creates two connected challe…

- **[What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks](https://arxiv.org/abs/2610.30635v1)**
  - *Fei Ding*
  - **ACL** · `2026-10-22`
  - Coding-agent benchmarks often describe a task in natural language but grade it with tests taken from the upstream project. Passing those tests can require information the description never states: a constant's name, a module path, an exact message. We call this a specification-or…

- **[Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification Agents](https://arxiv.org/abs/2610.29812v1)**
  - *Mohammed Saqlain*
  - **ACL** · `2026-10-21`
  - Literature-searching language agents are becoming a standard component of scientific assistants for the life sciences, yet there is little controlled evidence on which parts of their harness matter. We run a controlled ablation on biomedical claim verification (SciFact) with the…

- **[What Do RTL Repair Benchmarks Actually Measure?](https://arxiv.org/abs/2610.28595v1)**
  - *Yeyin Eva Zhu, Rishabh Ranawat*
  - **ACL** · `2026-10-20`
  - RTL repair benchmarks should measure whether a model can fix broken RTL given a specification. To this end, we construct and hash-bind RTLRepairDataset, 5,784 (broken, fixed) training pairs; RTLRepairBench, 459 held-out cases with 374 syntactic and 85 behavioral mutations; and an…


### Other / arXiv

- **[Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports](https://arxiv.org/abs/2610.31158)**
  - *Jiahao Meng, Qize Yang, Yuxuan Wang et al.*
  - 🤗 Featured · `2026-10-22`
  - Deep research agents synthesize open-web evidence into long reports, but current benchmarks do not evaluate research centered on a source video. We introduce Video-Centered Deep Research Report Generation. Given a video and user request, an agent identifies research questions, re…

- **[Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V](https://arxiv.org/abs/2610.28416)**
  - *Zhenghan Chen, Zekai Shao, Xin Lin et al.*
  - 🤗 Featured · `2026-10-20`
  - Code-based video generation offers fine-grained control, targeted editing, and component reuse compared with direct video generation. This approach requires multimodal large language models (MLLMs) to translate visual and temporal requirements into executable programs that produc…

- **[Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113)**
  - *Houde Qian, Zheng Jiang, Wenyi Li et al.*
  - 🤗 · `2026-10-21`
  - Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether lar…

- **[From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](https://arxiv.org/abs/2610.30051)**
  - *May Espinola, Qifan Zhang, Yu Xiang*
  - 🤗 · `2026-10-21`
  - Recent advances in frontier AI models have demonstrated remarkable capabilities in visual understanding, reasoning, planning, and tool use, raising the possibility of using general-purpose AI models for robot manipulation without task-specific training. However, their manipulatio…

- **[Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action](https://arxiv.org/abs/2610.31376v1)**
  - *Chao Gu, Quanyan Zhu*
  - `2026-10-22`
  - This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent capabilities, approval…

- **[Harnessing Language Models as Optimization Modeling Agents](https://arxiv.org/abs/2610.30917v1)**
  - *Yunxiang Luo, Xin Xu, Tianhao Chen et al.*
  - `2026-10-22`
  - Large language models (LLMs) can translate natural-language optimization problems into solver programs, but reliably producing correct formulations and implementations remains challenging. Existing approaches improve optimization modeling through agentic workflows or task-specifi…

- **[HERD: Harness-Evolving Recursive Distillation for Continual Learning](https://arxiv.org/abs/2610.31401v1)**
  - *Xun Sun, Thanh Thi Nguyen, Thuy-Trang Vu*
  - `2026-10-22`
  - Continual learning requires a model to keep acquiring new skills and knowledge without compromising its existing capabilities. Parametric methods suffer from catastrophic forgetting and loss of plasticity. Non-parametric methods, such as prompts, skills, and harnesses, leverage i…

- **[Cost-Aware Abstention for LLM-Based IT Ticket Classification](https://arxiv.org/abs/2610.31657v1)**
  - *Sachin Gupta*
  - `2026-10-22`
  - Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held…

- **[TESSA: A Governance-Oriented Custom GPT for SME Guidance under the EU AI Act: Design, Implementation, and Evaluation](https://arxiv.org/abs/2610.30822v1)**
  - *Chalisa Veesommai Sillberga, Kai-Kristian Kemella, Pekka Sillberga et al.*
  - `2026-10-22`
  - The increasing adoption of generative AI presents new opportunities while raising AI governance and regulatory challenges, particularly for small and medium-sized enterprises (SMEs) navigating the European Union Artificial Intelligence Act (EU AI Act). To support AI governance ed…

- **[A Reality Check of Inference-Time Context Augmentation Methods](https://arxiv.org/abs/2610.30983v1)**
  - *Haeun Yu, Geert Heyman, Pepa Atanasova et al.*
  - `2026-10-22`
  - Large language models (LLMs) often fail to utilise the context given in the input, resulting in hallucinations or a fallback to parametric knowledge. Context augmentation methods aim to improve model performance by modifying the input, from inserting filler tokens that add comput…

- **[PLE: Physical-Engineering's Last Exam](https://arxiv.org/abs/2610.30537v1)**
  - *Rujun Han, Yufan Zhuang, Arijit Ray et al.*
  - `2026-10-21`
  - Frontier language models now score above 90% on popular knowledge benchmarks and are increasingly deployed as agents that carry out multi-hour professional work. Yet no existing benchmark tests whether they can perform the real-world, economically valuable work of a professional…

- **[Can LLMs Improve Their Own Harness? A Controlled Study on ARC-AGI-3](https://arxiv.org/abs/2610.30499v1)**
  - *Jens Lehmann, Sahar Vahdati*
  - `2026-10-21`
  - A generally intelligent system acquires new skills efficiently without requiring humans to redesign its software scaffold for every new task. Yet language models rarely act alone. A harness is a symbolic program that orchestrates calls to the model, handling perception, memory, t…

- **[What the Trace Shows and What the Label Says: Auditing Behavioral Detectors in Agent Evaluation](https://arxiv.org/abs/2610.30491v1)**
  - *Idunnuoluwa A. Adeniji, Shilpika, Michael E. Papka*
  - `2026-10-21`
  - LLM agents are often evaluated by reducing execution traces to labels such as final-answer correctness, tool verification, and fault propagation. These labels are measurements produced by parsers, behavioral detectors, and harness rules, and they may not fully capture what the tr…

- **[Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems](https://arxiv.org/abs/2610.30418v1)**
  - *Daniel Ruiz, Luca Luceri, Emilio Ferrara*
  - `2026-10-21`
  - Modern LLM agents can retrieve information from accessible documents, and then disclose a sensitive conclusion assembled from them. This mosaic effect creates a critical risk for agents operating over confidential data. We quantify its realization with 30 synthetic cybersecurity,…

- **[SWE-VERIFIER: Selective Verification for Cost-Efficient Coding Agents](https://arxiv.org/abs/2610.30284v1)**
  - *Kaijian Zou, Vaibhav Chennareddy, Yunxiang Zhang et al.*
  - `2026-10-21`
  - Coding agents spend substantial computation generating actions and processing long interaction histories. Poor action choices can steer agents into low-value states, wasting computation and increasing API costs. Sampling and verifying alternative actions can improve the agent's d…

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

- **[Feedback That Backfires in Games: Do LLM Players Repeat the Move They Just Watched Fail?](https://arxiv.org/abs/2610.30205v1)**
  - *Esmail Gumaan*
  - `2026-10-21`
  - When an LLM agent's move fails, the harness writes the move and the failure message into the transcript and asks again. In tool calling, this record makes small models more likely to repeat the failed action. We test whether the same holds in games (Sokoban, Connect Four, Othello…

- **[MPIDetector: Detecting Multi-modal Prompt Injection via LLM-based Reasoning](https://arxiv.org/abs/2610.30202v1)**
  - *Yiheng Li, Jingyue Li*
  - `2026-10-21`
  - With the rapid integration of Multi-modal Large Language Models (MLLMs) into real-world applications, Prompt Injection (PI) has emerged as a critical security threat. Attackers can conceal malicious instructions within textual narratives or visual inputs to bypass safety alignmen…

- **[Harness Scaling for Generalizable Agentic Reinforcement Learning](https://arxiv.org/abs/2610.29458v1)**
  - *Fei Bai, Huatong Song, Chuan Hao et al.*
  - `2026-10-21`
  - Agent harnesses have become a central component of modern agentic systems, shaping how models use tools, manage context, and coordinate long-horizon interaction. Realizing the benefits of these harnesses depends on how effectively the underlying model can make use of them, motiva…

- **[Beyond Small Talk: Modeling Disclosure Trajectories in Human-AI Conversation](https://arxiv.org/abs/2610.29413v1)**
  - *Keith Kwok, Wanting Ning, Tej Deep Pala et al.*
  - `2026-10-21`
  - Recently, we see a rise in conversational agents as a form of social and emotional support, where disclosure will unfold over time. Yet, current evaluations of these agents typically examine isolated conversational states. In analyses of naturally occurring conversations, disclos…

- **[From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?](https://arxiv.org/abs/2610.29331v1)**
  - *Linus Filbry, Luckeciano C. Melo, Yarin Gal*
  - `2026-10-21`
  - Large language models (LLMs) are increasingly applied across the scientific discovery pipeline, from synthesizing literature to generating hypotheses to informing experimental design. A unifying principle behind these tasks is the need to continuously update beliefs as evidence a…

- **[SIM-UT: A User Simulation based Evaluation Framework for Medical Triage Chatbots](https://arxiv.org/abs/2610.30412v1)**
  - *Deepali Mittal, Dheeraj Mundhra, Yulia Sidorova et al.*
  - `2026-10-21`
  - LLM-based chat agents are increasingly used for complex, multi-turn, multilingual medical triage in low- and middle-income countries (LMICs), yet evaluation methods focus on single-turn, English-only benchmarks that primarily test the chatbots' knowledge. In practice, users are o…

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

- **[Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents](https://arxiv.org/abs/2610.28934v1)**
  - *Xu Li, Simon Yu, Minzhou Pan et al.*
  - `2026-10-20`
  - Coding agents now complete tasks autonomously, modifying real-world state such as artifacts, software environments, and configurations along the way. Yet they show limited backup awareness: recognizing that an action will modify state that may later be needed, and preserving it b…

- **[SANE: Automated Scorer-Specific Metamorphic Testing for LLM Judges](https://arxiv.org/abs/2610.28886v1)**
  - *Ethan Ludwick, Yu-Chung Hsiao*
  - `2026-10-20`
  - LLM judges increasingly mediate benchmark evaluation, model selection, data curation, and training. Their decisions are useful only when each judge responds reliably to changes affecting its scoring criterion. Existing methods for reliability testing perturb inputs with known exp…

- **[Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing](https://arxiv.org/abs/2610.28815v1)**
  - *Jingzhe Liu, Jiliang Tang, Tong Zhao et al.*
  - `2026-10-20`
  - Agentic harness evolution optimizes an agent's instructions, tools, and control flow by using its task execution experiences as evolving evidence. While more evolution tasks should intuitively improve performance, our preliminary study reveals a paradoxical failure mode: the perf…

- **[Evolving Agent Interfaces](https://arxiv.org/abs/2610.28601v1)**
  - *Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega et al.*
  - `2026-10-20`
  - Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through a shell to find one function. Both the interfaces and the knowledge of when to u…

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


## Finance  (158)

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

- **[Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity](https://arxiv.org/abs/2610.31436v1)**
  - *Ali Atiah Alzahrani*
  - **ACL** · `2026-10-22`
  - Automated agentic-system design is typically evaluated on static task suites with immediate scalar rewards. Deployed systems face persistent shift, delayed dependent feedback, correlated component failures, and costly architecture changes. We formalize meta-agent architecture sea…

- **[Nominate-then-Adjudicate: LLM-Assisted One-Pass and Per-Instance MIP Solver Tuning](https://arxiv.org/abs/2610.29391v1)**
  - *Yifan Zhao, Qianyang Zhao, Xinyu Guan et al.*
  - **ACL** · `2026-10-21`
  - Mixed-integer programming solvers expose hundreds or even thousands of parameters whose best setting varies per instance, yet per-instance search is prohibitively expensive. We frame this as configuration for heterogeneous Big Data optimization workloads and propose a nominate-th…


### Other / arXiv

- **[Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113)**
  - *Houde Qian, Zheng Jiang, Wenyi Li et al.*
  - 🤗 · `2026-10-21`
  - Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether lar…

- **[Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use](https://arxiv.org/abs/2610.30108)**
  - *Yanzhe Chen, Ziyi Yang, Jifeng Zhu et al.*
  - 🤗 · `2026-10-21`
  - Multimodal agents (MMAs) sustain interaction through reasoning, memory, tools, and feedback, most visibly as computer-use agents, while robotic systems (RSs) couple sensing and actuation under physical dynamics. We define multimodal embodied agents (MMEAs) as goal-directed system…

- **[Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated Metadata Across Structured and Unstructured Systems](https://arxiv.org/abs/2610.31553v1)**
  - *Humza Akhtar, Brian Freeman*
  - `2026-10-22`
  - Industrial organizations hold operational knowledge in structured records, such as telemetry, point lists, and transactions, and in unstructured sources, such as manuals, service notes, communications, and inspection reports. Governance programs often manage these sources separat…

- **[Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery](https://arxiv.org/abs/2610.31461v1)**
  - *Dingxuan Zhang, Yanhui Jiang, Jun Wang et al.*
  - `2026-10-22`
  - Reusable skills allow large language model agents to package task-specific procedures, tool affordances, and execution guidance into modular units. Prior work has largely studied how agents retrieve, compose, or synthesize skills before execution. In coding agents, however, execu…

- **[Subgoal-aware Memory Graph for GUI Agent](https://arxiv.org/abs/2610.31307v1)**
  - *Dezhao Luo, Daniel Beechey, Derek Yuen et al.*
  - `2026-10-22`
  - GUI agents aim to automate complex user tasks by interacting with mobile interfaces, but ef- fective decision-making in long-horizon set- tings requires reusing prior experience rather than relying solely on the environment ob- servations. Existing memory-based methods typically…

- **[Superintelligent Software Engineering: Governance That Scales with Capability](https://arxiv.org/abs/2610.31306v1)**
  - *Mohammad Mehdi Gholinejad*
  - `2026-10-22`
  - Software agents are being trained to exceed human engineers; we argue that capability alone does not produce better software engineering. We define superintelligent software engineering as the discipline of building and evolving software with agents whose capability exceeds that…

- **[What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight](https://arxiv.org/abs/2610.30803v1)**
  - *Ahmed M. Mahran*
  - `2026-10-22`
  - Replacing the judge can move a benchmark score, and models can be trained to hide capabilities. Both put the evaluator in question: what can it certify? We develop a partition theory of evaluation from one principle: judgement is bounded by perception. An agent's discrimination i…

- **[An Introduction to World Models for Generalist Agents](https://arxiv.org/abs/2610.30789v1)**
  - *Zhihui Zhu*
  - `2026-10-22`
  - World models have recently emerged as a promising direction toward developing generalist agents capable of understanding, predicting, and interacting with diverse environments. However, despite growing interest, the concept of a world model remains loosely defined, encompassing a…

- **[Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core](https://arxiv.org/abs/2610.30557v1)**
  - *Yebo Feng, Jingyang Dai, Liangrui Pan et al.*
  - `2026-10-22`
  - LLM agents that act on live Web data must combine heterogeneous evidence, remember what they have done and improve from outcomes without weakening their own safeguards. We study this problem in autonomous investing, where every action is irreversible and based on untrusted Web co…

- **[Reliable AI-Assisted Decisions via Selective Auditing](https://arxiv.org/abs/2610.31662v1)**
  - *Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani et al.*
  - `2026-10-22`
  - We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by th…

- **[Learning What to Ask for Tomorrow: Active Preference Acquisition for Long-Term Personalized Web Agents](https://arxiv.org/abs/2610.31107v1)**
  - *Yiqi Wang, Zizhi Zeng, Jiaqi Zhang et al.*
  - `2026-10-22`
  - Web agents increasingly serve the same user across repeated online tasks such as booking travel, shopping, and scheduling, so their long-term usefulness depends on how well they know the user's preferences. Passive memory and personalization methods cannot obtain preferences the…

- **[Multi-Tool Selection for Robotic Systems: Comparing Semantic Retrieval and LLM](https://arxiv.org/abs/2610.31013v1)**
  - *Miguel Sousa, Luis Ramos Pinto, João P. Matos-Carvalho*
  - `2026-10-22`
  - Natural-language interfaces allow users to command robotic systems without interacting directly with mission planners or robotics middleware. Their reliable use depends on robot tool routing, defined here as the selection of the smallest complete subset of predefined executable c…

- **[Can Loan Processors and Underwriters Spot AI-Edited Statements? An Empirical Study](https://arxiv.org/abs/2610.30758v1)**
  - *Simiao Ren, Xingyu Shen, Tommy Duong et al.*
  - `2026-10-22`
  - AI-assisted editing can produce loan documents that preserve familiar issuer layouts while changing the applicant's identity. We investigated whether experienced underwriters and loan processors identify such forgeries in first-pass, document-only review. Three practitioners recr…

- **[When News Gets Old: Portfolio Allocation with Reinforcement Learning and Large Language Models](https://arxiv.org/abs/2610.30564v1)**
  - *Bolin Song, Surui Xiang*
  - `2026-10-22`
  - Financial news can influence investment decisions long after publication. Timely news may reach an investor before prices fully adjust, whereas older news may already be reflected in prices. We examine two ways to handle aging signals: retain them and give a portfolio policy timi…

- **[Intraday Forecasting Ability and Liquidity Provision of Institutional Traders](https://arxiv.org/abs/2610.31141v1)**
  - *Xinlei Hao, Jiajun Guo, Jussi Keppo et al.*
  - `2026-10-22`
  - This study uses a high-frequency dataset from a stock exchange to examine how forecasting ability and liquidity provision relate to institutional traders' proprietary intraday profitability. We discover persistent forecasting abilities among traders. Specifically, we demonstrate…

- **[Directionally Correct Views in Portfolio Optimization](https://arxiv.org/abs/2610.31074v1)**
  - *Ojas Kumar, Sreejit Dey, Sarvesh Ravichandran Iyer et al.*
  - `2026-10-22`
  - Portfolio optimization techniques often use historical data to estimate parameters for Markowitz-type or ML models. Effective allocation requires a way to align the available data with conditions expected over the investment horizon. Inspired by the Black-Litterman framework, we…

- **[A Three-Pillar Governance Framework for Safe and Trustworthy AI Agents](https://arxiv.org/abs/2610.30445v1)**
  - *Edward C. Cheng, Jeshua Cheng, Alice Siu*
  - `2026-10-21`
  - AI agents capable of autonomous decision-making introduce significant challenges related to safety, alignment, accountability, and human oversight. Existing Human-in-the-Loop (HITL) and responsible AI approaches provide important foundations, but many remain fragmented across sys…

- **[RoleFlow: Self-Evolving Multi-Role Agentic Collaboration via Structural Adaptation](https://arxiv.org/abs/2610.30429v1)**
  - *Yi Ge, Pan Wang, Xuehao Cui et al.*
  - `2026-10-21`
  - Large language model (LLM) based multi-agent systems often rely on predefined collaboration structures, limiting their adaptability to evolving task requirements. Although recent approaches enable dynamic orchestration, trajectory-level rewards they apply assign one outcome to ea…

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

- **[Memory-Centric Continual Learning for AI Agents](https://arxiv.org/abs/2610.29357v1)**
  - *Dongfang Li, Zhuoen Chen, Bonian Jia et al.*
  - `2026-10-21`
  - Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive ret…

- **[IFC-MCQ: Automatically Generating Multiple-Choice Benchmarks for Evaluating LLM Agents on IFC Data Retrieval](https://arxiv.org/abs/2610.30533v1)**
  - *Rabindra Lamsal, Sisi Zlatanova, Xuesong Shen*
  - `2026-10-21`
  - Industry Foundation Classes (IFC), the standard for building information exchange in architecture, engineering, and construction (AEC), is increasingly queried through large language models (LLMs) using natural language. Evaluating these systems at scale is difficult because free…

- **[Bridging Foundational and Agentic Capabilities of LLMs](https://arxiv.org/abs/2610.29751v1)**
  - *Wei Guo, Yuanjian Xu, Jianing Hao et al.*
  - `2026-10-21`
  - Large language models (LLMs) are increasingly deployed as agents, yet it remains unclear how their foundational capabilities translate into agentic capabilities. End-to-end scores leave unresolved whether low benchmark capability or weak deployment drives a failure, limiting acti…

- **[Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization](https://arxiv.org/abs/2610.29671v1)**
  - *Zhiqian Xia, Jielong Tang, Ling-An Zeng et al.*
  - `2026-10-21`
  - Long-term agent memory is shifting from predefined workflows toward learnable policies for memory construction and retrieval. Existing learning-based methods either optimize construction alone or combine retrieval-side online reinforcement learning (RL) with offline construction…

- **[LTEM: LLM-Friendly Table-Enhanced Markdown for Table Understanding and Generation](https://arxiv.org/abs/2610.29188v1)**
  - *Eunbin Kim, Hyeonseok Kang, Sangkeun Jung*
  - `2026-10-21`
  - Tables in real-world documents, including scientific papers, financial reports, and statistical summaries, frequently use merged cells, multi-level headers, and sectioned layouts. Yet the lightweight formats LLMs handle best (Markdown, CSV) cannot express these structures, while…

- **[Leveraging Time-Series Foundation Models for Financial Crime Detection](https://arxiv.org/abs/2610.29667v1)**
  - *Danae Natalie Savvidi, H. Çağrı Bilgi, Kubilay Atasu et al.*
  - `2026-10-21`
  - Financial crime detection requires identifying illicit activity within large transaction networks, where suspicious behaviour is rare and unfolds over time. Existing graph-based methods capture relationships among accounts but typically underuse the temporal behaviour encoded in…

- **[Prediction Is Not Calibration: Item Parameter Recovery and Representation Coupling in Knowledge Tracing](https://arxiv.org/abs/2610.30211v1)**
  - *Wenrui Yuan, Stéphanie M. van den Berg, Johannes Steinrücke*
  - `2026-10-21`
  - Knowledge tracing (KT) models can estimate item parameters through an item response decoder trained solely for next-response prediction, yet predictive accuracy does not guarantee parameter recovery. We study 2PL, GPCM, and NRM decoders paired with LSTM, Transformer, and DKVMN en…

- **[Why Constrained Updates Still Forget: A Functional-Path Analysis of Continual SFT](https://arxiv.org/abs/2610.30191v1)**
  - *Qingsen Ma, Dianyun Wang, Jiahong Liu et al.*
  - `2026-10-21`
  - Supervised fine-tuning adapts language models to specialized tasks but can disrupt previously acquired behavior. Existing approaches constrain parameters, gradients, or replay objectives, yet the connection between the protected object, the intervening trajectory, and retained ou…

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

- **[S$^2$-MAS: A Society-Scale Multi-Agent Simulation Framework with 500 Million Household Persona Agents](https://arxiv.org/abs/2610.27746v3)**
  - *Yang Li, Yike Wang, Di Wan et al.*
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


---
*Generated 2026-10-23 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
