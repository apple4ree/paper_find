# Daily Paper Digest — 2026-10-28 (Wednesday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**498 unique papers** (651 topic-entries — cross-topic papers counted once per category)

---

## Agent  (361)

### NeurIPS

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **NeurIPS 2025** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…


### ICML

- **[TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration](https://openreview.net/forum?id=bz651zjpyk)**
  - **ICML 2025** · OpenReview · `2026-10-13`
  - LLM-based agents can automate model post-training, accelerating progress toward recursive self-improvement. Despite their promise, existing approaches remain under-explored and face two main challenges: (1) strategy lock-in that limits exploration beyond the initial strategy; and…

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

- **[Establishing Best Practices in Building Rigorous Agentic Benchmarks](https://openreview.net/forum?id=E58HNCqoaA)**
  - *Yuxuan Zhu, Tengjun Jin, Yada Pruksachatkun et al.*
  - **ICML 2025** · OpenReview · `2025-05-01`
  - Benchmarks are essential for quantitatively tracking progress in AI. As AI agents become increasingly capable, researchers and practitioners have introduced agentic benchmarks to evaluate agents on complex, real-world tasks. These benchmarks typically measure agent capabilities b…

- **[Tool-as-Interface: Learning Robot Policies from Observing Human Tool Use](https://openreview.net/forum?id=ZA8iXa45P2)**
  - *Haonan Chen, Cheng Zhu, Shuijing Liu et al.*
  - **ICML 2025** · OpenReview · `2025-04-23`
  - Tool use is essential for enabling robots to perform complex real-world tasks, but learning such skills requires extensive datasets. While teleoperation is widely used, it is slow, delay-sensitive, and poorly suited for dynamic tasks. In contrast, human videos provide a natural w…

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

- **[Online Fair Division with Frequency Predictions](https://arxiv.org/abs/2610.34625v1)**
  - *Tzeh Yuan Neoh, Nicholas Teh*
  - **ICML** · `2026-10-25`
  - We study online fair division of indivisible goods among $n$ agents with frequency predictions: before any good arrives, the algorithm learns the multiset of each agent's values for the goods, but neither the arrival order nor which values of different agents belong to the same g…


### ACL

- **[ProCerDCL: Query-Efficient Black-Box Probabilistic Verification of Deep Learning Compiler Optimization](https://arxiv.org/abs/2610.36499v1)**
  - *Zexin Li, Weibo Zhang, Linyi Li et al.*
  - **ACL** · `2026-10-27`
  - We present \tool, a query-efficient framework for black-box probabilistic verification. Given a fixed, sampleable input distribution and a binary property oracle, \tool assesses the property's violation probability $p$ against a threshold $θ$. Under independent sampling and state…

- **[The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation](https://arxiv.org/abs/2610.35541v2)**
  - *Ruozhao Yang, Jiongchi Yu, Ming Hu et al.*
  - **ACL** · `2026-10-26`
  - Web services increasingly expose backend interfaces that let users delegate tasks to AI agents, which invoke service operations directly without navigating websites. This shift changes how existing Web vulnerabilities can be exploited. We investigate these changes through VELA, a…

- **[Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives](https://arxiv.org/abs/2610.35240v1)**
  - *Radha Krishna Deshpande, Ajoy Mondal, Akash Manna et al.*
  - **ACL** · `2026-10-26`
  - India's historical public archives present severe computer vision and document image analysis challenges: decades of parliamentary records survive only as degraded, multi-column scanned pages featuring mixed scripts, complex layouts, and dense visual noise where OCR failure is th…

- **[Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents](https://arxiv.org/abs/2610.34817v2)**
  - *Ying Zhang, Ruoqi Guo, Yi Liu et al.*
  - **ACL** · `2026-10-26`
  - Large language model (LLM) services process massive volumes of user requests, resulting in substantial inference costs. To reduce both cost and latency, providers have introduced prompt caching. However, correctly integrating prompt caching is non-trivial due to heterogeneous pro…

- **[The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory](https://arxiv.org/abs/2610.34767v1)**
  - *Yuexi Pan, Yongchao Chen*
  - **ACL** · `2026-10-26`
  - Most agent-memory benchmarks frame long-term memory as retrieval: can an agent recover the relevant record from a long and evolving history? Scientific agents face a stricter problem: a correctly remembered fact may still be invalid to use. The same reported test result can suppo…

- **[FeatureLoop: Benchmarking Coding Agents under Evolving Requirements](https://arxiv.org/abs/2610.35488v1)**
  - *Jia Feng, Alyssa Wu, Cuiyun Gao et al.*
  - **ACL** · `2026-10-26`
  - Software development with coding agents often begins with a rough request that users refine after trying the implementation. Final correctness alone does not capture the repeated guidance this process requires. We introduce FeatureLoop, a benchmark of 61 human-reviewed tasks from…

- **[CodeMeepo: A Multi-Agent Workflow for Repository-Level Code Migration and Optimization](https://arxiv.org/abs/2610.34633v1)**
  - *Farzad Habibi, Changrong Wu, Jinzhou Jiang et al.*
  - **ACL** · `2026-10-25`
  - Repository-level code migration rewrites an entire project in a new programming language while preserving its observable behavior. It is challenging because behavior spans interdependent modules, dependencies and build infrastructure must be adapted to the target ecosystem, and t…

- **[Outcome-Aware Agents: When Does Causal Structure Help a Forward Model Foresee the Consequences of Actions?](https://arxiv.org/abs/2610.34385v1)**
  - *Mallesh Madapathi*
  - **ACL** · `2026-10-25`
  - Agents that act on real systems should predict what their actions will cause before acting. We study when causal structure helps a learned forward model do this, using a planner that rejects candidate actions whose simulated multi-step outcome is unsafe, in synthetic structural c…

- **[Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents](https://arxiv.org/abs/2610.34167v1)**
  - *Jiaju Huang, Shaobin Chen, Xinglong Liang et al.*
  - **ACL** · `2026-10-25`
  - Tool-using language model agents are usually evaluated by whether they finish the user's task. That metric misses a common failure: an agent can complete the requested work while also taking an unauthorized side-effecting action, such as writing to the wrong object, expanding the…

- **[How Do Small Coding Agents Use Code Graphs and Embeddings?](https://arxiv.org/abs/2610.33958v1)**
  - *Saurav Bellam*
  - **ACL** · `2026-10-25`
  - Coding agents are given embedding search and code-graph tools on the premise that a repository's structure is something the model lacks and the tool supplies. We test that premise on SWE-bench Verified with small open-weight models, stratifying tasks by a deterministic hop depth…


### IJCAI

- **[Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition](https://arxiv.org/abs/2610.34777v1)**
  - *Weihang Niu, Mengxing Ren, Che Qu*
  - **IJCAI** · `2026-10-26`
  - This paper introduces Scope-Gap Injection (SGI), an indirect prompt injection method for multi-stage LLM-agent safety pipelines. In the IJCAI 2026 OpenClaw Agent Security Attack Competition, each attack package is judged by a static skill scan (S1), an LLM-judge safety check over…


### Other / arXiv

- **[VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation](https://arxiv.org/abs/2610.35864)**
  - *Muxi Diao, Wenbin Xu, Lele Yang et al.*
  - 🤗 Featured · `2026-10-27`

- **[Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception](https://arxiv.org/abs/2610.37037)**
  - *Lai Wei, Yatai Li, Liangbo He et al.*
  - 🤗 Featured · `2026-10-27`
  - Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data for…

- **[Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces](https://arxiv.org/abs/2610.37255)**
  - *Jian Mu, Ruibo Shen, Yao Shu*
  - 🤗 Featured · `2026-10-27`
  - Language model agents are post-trained and deployed through a harness, the prompts, tools, and control logic that present a task to the model and execute its outputs. Harnesses are often revised and judged by how an already trained model performs under them, which assumes that wh…

- **[Can LLMs Uncover Hidden Physical Laws through Free Exploration?](https://arxiv.org/abs/2610.37649)**
  - *Zhen Yang, Wen Wang, Xander Xu et al.*
  - 🤗 Featured · `2026-10-27`
  - Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through exp…

- **[Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions](https://arxiv.org/abs/2610.37624)**
  - *Anouar Imel, Imad Charradi, Abderrahman Sghir et al.*
  - 🤗 Featured · `2026-10-27`
  - When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widel…

- **[MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model](https://arxiv.org/abs/2610.37175)**
  - *Brian Ko, Han Wang, Hejia Geng et al.*
  - 🤗 Featured · `2026-10-27`
  - AI research agents can propose, execute, and improve programs that solve machine learning tasks. However, executing each candidate program requires training and evaluating ML models, limiting how many candidates an agent can explore at each step. We introduce MLE-World, a world m…

- **[The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents](https://arxiv.org/abs/2610.36077)**
  - *Weidong Tang, Ruiheng Wang, Jingxuan Zhang et al.*
  - 🤗 Featured · `2026-10-26`
  - Multimodal intelligence can be viewed as human-guided co-evolution between worlds and agents through interaction. However, scaling this process faces two bottlenecks: constructing heterogeneous, verifiable environments is costly, and manual Harness iteration cannot keep pace with…

- **[Multiscale Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.35013)**
  - *Tao Ren, Hui Yang, Jia Deng et al.*
  - 🤗 Featured · `2026-10-26`
  - Long-horizon LLM agents interact with their environments through complete assistant turns while generating each action token by token. We observe that critic values vary primarily across turns, motivating optimization anchored at turns with finer credit allocation among tokens. W…

- **[Omni-InteractScope: Benchmarking Proactive and Agentic Interaction in Continuous Omnimodal Streams](https://arxiv.org/abs/2610.35439)**
  - *Yinsong Yan, Ling Wang, Yuxuan Wang et al.*
  - 🤗 Featured · `2026-10-26`
  - Omnimodal large language models (Omni-LLMs) are increasingly expected to assist users while observing continuous audiovisual streams. However, existing evaluations provide limited insight into how reliably these models connect stream evidence and user needs to timely, sustained i…

- **[SearchHorizonBench: A Benchmark for Search Value in AI Agents](https://arxiv.org/abs/2610.34714)**
  - *Jingjie Ning, Xueqi Li, Yibo Kong*
  - 🤗 Featured · `2026-10-26`
  - AI agents must decide when another search is worth its cost. Answer-success probabilities capture question difficulty, while this decision requires estimating the additional benefit of search. We introduce SearchHorizonBench, a benchmark for learning and evaluating search value f…

- **[Harness-Model Collaboration for Long-Horizon Continual Learning](https://arxiv.org/abs/2610.34724)**
  - *Zhen Bi, Zhizhi Peng, Yan Wang et al.*
  - 🤗 Featured · `2026-10-26`
  - Long-horizon agents continuously encounter reusable procedural knowledge, yet existing systems typically rely either on model adaptation or external memory, trading persistent learning for rapid reuse. This limitation is especially important for Web agents that repeatedly execute…

- **[Memory Tax: Dissecting the Net Value of Agent Memory](https://arxiv.org/abs/2610.34073)**
  - *Xuan He, Sining Zhoubian, Ruozhen Yang et al.*
  - 🤗 Featured · `2026-10-25`
  - Memory is increasingly used in long-horizon agents, yet the net value of building memory over direct retrieval from raw history remains largely unclear. Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems underper…

- **[h1: A Taste of the Bitter Lesson in Automated Theorem Proving](https://arxiv.org/abs/2610.35962)**
  - *Skander Moalla, Ahmad Rammal, Niket Patel et al.*
  - 🤗 Featured · `2026-10-25`
  - While progress in informal mathematics has come largely from scaling the chain-of-thought and agentic reasoning of frontier language models, formal theorem proving has increasingly relied on human-designed workflows around these models, such as planning, decomposition, and orches…

- **[What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents](https://arxiv.org/abs/2610.34491)**
  - *Kaiser Sun, Yongchan Kwon, Zain Hasan et al.*
  - 🤗 Featured · `2026-10-25`
  - Generative models increasingly expose a reasoning effort setting that lets users scale inference-time compute, trading higher cost for potentially improved performance. Users must choose an effort level before knowing whether extra reasoning will help, and even a successful run d…

- **[HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory](https://arxiv.org/abs/2610.24520)**
  - *Junming Zhang, Rubin Wei, Xu Cheng et al.*
  - 🤗 Featured · `2026-10-20`

- **[EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning](https://arxiv.org/abs/2610.37609)**
  - *Sihan Yang, Weichen Bai, Ruichuan An et al.*
  - 🤗 · `2026-10-27`
  - As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) mor…

- **[TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](https://arxiv.org/abs/2610.37571)**
  - *Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz et al.*
  - 🤗 · `2026-10-27`
  - Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-…

- **[Teach reality, not ethics: a drop-in continued-pretraining corpus installs coupled human-biosphere-AI welfare dispositions across model families](https://arxiv.org/abs/2610.37484)**
  - *Trent R. Northen, Mingxun Wang*
  - 🤗 · `2026-10-27`
  - Large language models (LLMs) are increasingly used to make and execute decisions that affect living systems. Yet, to our knowledge, ecological reasoning is not a focus of pre- or post-training. This increases the risk that under operational pressure, they may make decisions to ir…

- **[M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents](https://arxiv.org/abs/2610.37459)**
  - *Hannes Ill, Rafi Al Attrach, Rajna Fani et al.*
  - 🤗 · `2026-10-27`
  - Clinical research over electronic health records depends on derived variables whose definitions sit outside the schema, in item codes, time windows, missingness rules, and output-grain choices that change cohorts and downstream conclusions. We introduce M4Bench, 28 clinical deriv…

- **[TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving](https://arxiv.org/abs/2610.37230)**
  - *Shuhuai Li, Shengdong Ye, Dongdong Ge et al.*
  - 🤗 · `2026-10-27`

- **[Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements](https://arxiv.org/abs/2610.36584)**
  - *Binhang Qi, Yiming Liu, Yun Lin et al.*
  - 🤗 · `2026-10-27`
  - As large language model agents increasingly compile natural-language requirements into repository-level code, requirement-to-test generation grows in importance to provide validation constraints (or harness) to guide code generation. Yet it remains unclear whether current agents…

- **[When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents](https://arxiv.org/abs/2610.36471)**
  - *Chiming Duan, Tong Jia, Yingxi Chen et al.*
  - 🤗 · `2026-10-27`
  - LLM agents interact with Web services to perform tasks on users' behalf. Errors during these interactions can disrupt execution and prevent task completion, motivating external intervention. However, agents may self-recover through continued execution, raising the question of whe…

- **[Work Agents: Systems, Capabilities, and Optimization](https://arxiv.org/abs/2610.35845)**
  - *Zishan Xu, Enjun Du, Mingqi Gao et al.*
  - 🤗 · `2026-10-26`
  - As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish deleg…

- **[Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](https://arxiv.org/abs/2610.35832)**
  - *Yifei Yao, Yude Zou, Guanbo Jiao et al.*
  - 🤗 · `2026-10-26`
  - Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action model (WAM) policies across manipulation demands remains to be tho…

- **[Back to Basics: A Skill-Centric Approach to Generalist Web Agents](https://arxiv.org/abs/2610.35823)**
  - *Minh Pham-Dinh, Md Farhan Ishmam, Hernan Yupanqui et al.*
  - 🤗 · `2026-10-26`

- **[Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588v1)**
  - *Rodrigo Gonzalez Laiz, Steffen Schneider*
  - `2026-10-27`
  - World models are widely proposed as core components for enabling agents to reason over long temporal and spatial horizons. Yet current evaluations often emphasize task performance while providing limited insight into whether learned world models acquire predictive latent dynamics…

- **[Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents](https://arxiv.org/abs/2610.37567v1)**
  - *Pranjal Aggarwal, Sean Welleck*
  - `2026-10-27`
  - AI agents have made substantial progress in domains where they have a non-trivial amount of time to deliberate between actions, such as mathematics, software engineering, and performing tasks on desktop applications. It is less clear how such models fare in settings that demand r…

- **[Strategyproof Deep Reinforcement Learning for Online Resource Allocation](https://arxiv.org/abs/2610.37504v1)**
  - *Fariba Dehghan, Sebastian Stein, Vahid Yazdanpanah et al.*
  - `2026-10-27`
  - Online resource allocation faces two coupled challenges: (1) allocating scarce resources efficiently under uncertain future demand, and (2) ensuring that agents report task valuations and requirements truthfully (strategyproofness). Reinforcement Learning (RL) adapts allocation d…

- **[From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents](https://arxiv.org/abs/2610.37482v1)**
  - *Ziyang Chen, Qian Li, Chengwei Qin*
  - `2026-10-27`
  - GUI memory should preserve the results of past actions and learn reusable operations. This is difficult in long-horizon workflows, where agents must use information across applications and useful operations are interleaved with failed attempts. We introduce Task Advancement Memor…

- **[PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions](https://arxiv.org/abs/2610.37471v1)**
  - *Tongkun Guan, Zhibo Yang, Mingkun Yang et al.*
  - `2026-10-27`
  - Fine-grained visual perception remains a bottleneck during post-training of multimodal large language models (MLLMs), as perceptual errors can constrain gains from reasoning-focused optimization. Although image-caption pre-training improves perception, its influence can weaken as…

- **[Concordat: Typed Sessions for LLM Agents](https://arxiv.org/abs/2610.37461v1)**
  - *Milad Sikaroudi*
  - `2026-10-27`
  - Agents built on large language models are increasingly allowed to take consequential actions: cancelling bookings, issuing refunds, changing accounts. The rules that govern those actions, such as "obtain the customer's explicit confirmation before changing anything", are usually…

- **[Test-Time Communication in Trading Agent Swarms](https://arxiv.org/abs/2610.37448v1)**
  - *Avid Fayaz, Harry Zhang, Håvard Alstadheim et al.*
  - `2026-10-27`
  - Communication between agents has mostly been studied on tasks with a shared objective and fast, clear feedback. Trading has neither: each agent manages its own account, with decisions being scored by markets late and noisily. A trading swarm is thus a population of independent de…

- **[FeatureArc: Benchmarking Coding Agents on Evolving Features](https://arxiv.org/abs/2610.37434v1)**
  - *Yunlong Wang, Alyssa Wu, Cuiyun Gao et al.*
  - `2026-10-27`
  - A software feature usually evolves over time: developers extend its first version as new use cases and requirements arrive, and each extension builds on code written earlier. Most feature benchmarks evaluate a single request on a fixed codebase. Feature evolution requires evaluat…

- **[Constraining the Commit Boundary: A DIO/ODI-Informed Authorization Guardrail for Agentic Entity Resolution](https://arxiv.org/abs/2610.37407v1)**
  - *Daniel Beránek*
  - `2026-10-27`
  - Agentic Entity Resolution (ER) systems iteratively plan actions, retrieve evidence, revise hypotheses, and propose graph mutations. An erroneous identity hypothesis may condition later retrieval and produce apparent confirmation. This paper proposes a Digital Identity Optimizatio…

- **[Clearing the FoG: Training KG Agents to Retrieve the Evidence Behind Their Answers](https://arxiv.org/abs/2610.37405v1)**
  - *Zongyuan Sun, Shuai Zhao, Yingjun Du et al.*
  - `2026-10-27`
  - Large language models (LLMs) can answer many factual questions correctly, but a correct answer is not necessarily a supported one. For an LLM agent, a knowledge graph (KG) plays two roles: as a source of answers, it supplies facts that the model lacks; as a source of evidence, it…

- **[Agent-Conditioned Routing: Diverse Reasoning Paths Within One Frozen Model](https://arxiv.org/abs/2610.37375v1)**
  - *Ananth Kalyanasundaram, Ankush Kadu, Athira Gopal et al.*
  - `2026-10-27`
  - Generating several solutions can expose alternative methods, but additional trajectories often paraphrase one dominant approach. We investigate whether the conditional capacity of a frozen sparse mixture-of-experts (MoE) model can provide such diversity from one problem prompt, w…

- **[Aligning Institutional Power and Operational Ability](https://arxiv.org/abs/2610.37342v1)**
  - *Andrea Marino, Giovanni Sileno, Thomas van Binsbergen et al.*
  - `2026-10-27`
  - To be socially sustainable, Agentic AI systems require normative designs that align responsibilities with the ability to fulfil them. Identifying incongruences such as unsatisfiable expectations or privilege escalation is crucial in avoiding normative pitfalls. In this study, we…

- **[WCC: A Learning-Based Framework for Deciding When to Apply Cooperative Coevolution in Large-Scale Optimization](https://arxiv.org/abs/2610.37329v1)**
  - *Wenjie Qiu, Hepei Li, Jianfeng Wang et al.*
  - `2026-10-27`
  - Cooperative Coevolution (CC) and Non-Decomposition Algorithms (NDAs) are two primary approaches for large-scale global optimization (LSGO). Although both have achieved success, they exhibit markedly different performance across problem types and each faces approach-specific limit…

- **[AnalogScout: Simulation-Efficient PVT-Aware Analog Sizing with LLM Agents](https://arxiv.org/abs/2610.37319v1)**
  - *Yichen Long, Keren Zhu*
  - `2026-10-27`
  - Analog device sizing must satisfy all specifications across process, voltage, and temperature (PVT) corners to ensure tape-out success, but simulating every candidate at all corners dominates the sizing time and slows design iteration. Conventional surrogate-based optimizers sear…

- **[Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?](https://arxiv.org/abs/2610.37276v1)**
  - *Sichun Luo, Yi Huang, Mukai Li et al.*
  - `2026-10-27`
  - Large language model (LLM)-driven agent scaffold evolution improves agent workflows through iterative candidate generation and evaluation. Evaluation both guides subsequent search and determines the final scaffold, but evaluating every candidate on the full task set incurs substa…

- **[Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation](https://arxiv.org/abs/2610.37242v1)**
  - *Saiful Khan, Afrah Farea*
  - `2026-10-27`
  - Large language model (LLM) agents that call enterprise APIs must select the correct endpoints, follow process order, use valid payload keys, and choose coded values from predefined lists. However, current retrieval-augmented service discovery treats endpoints independently and th…

- **[Spine: Compiling Subtask Trees into Structured Context for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.37224v1)**
  - *Jiahong Xiang, Kunqiu Chen, Lingming Zhang et al.*
  - `2026-10-27`
  - Long-horizon coding tasks contain nested subtasks. Typically, agents record interactions sequentially into a growing history, causing context inflation and performance degradation. Compressing or trimming the history without explicit subtask boundaries can discard information nee…

- **[Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution](https://arxiv.org/abs/2610.37201v1)**
  - *Jiawei Zhou, Bo Peng, Yuxuan Huang et al.*
  - `2026-10-27`
  - Skill optimizers adapt an agent to long-horizon tasks, such as repairing a terminal environment, by rewriting its skill, a natural-language procedure in its context, and keeping the edits that raise success on a small dev set. On such tasks success is noisy, so a gain on a small…

- **[Action-Value Calibration via Continuation Sharing for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2610.37195v1)**
  - *Yingjian Chen, Lang Zhou, Zixin Zhao et al.*
  - `2026-10-27`
  - Reinforcement learning for long-horizon agents relies on feedback from sequences of interactions, making credit assignment to individual actions difficult. Existing methods such as GiGPO compare actions at shared states to compute relative advantages, but estimate each action's v…

- **[LiveSearch: Questions as Executable Verifier Code for a Live Benchmark of Professional-Source Financial Search Agents](https://arxiv.org/abs/2610.37166v1)**
  - *Sinuo Wang, Wentao Zhao, Jiacheng Lu et al.*
  - `2026-10-27`
  - In finance, the answer that matters is usually the current one: prices, rates, and disclosures hold only as of a given day, so retrieving up-to-date facts is a core capability of a financial agent. Yet most financial benchmarks overlook timeliness. They fix each answer at annotat…

- **[WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training](https://arxiv.org/abs/2610.37161v1)**
  - *Ziyang Zeng, Tingyang Chen, Jia Deng et al.*
  - `2026-10-27`
  - Scaling supervised training for working agents requires diverse professional tasks that yield reliable expert demonstrations. However, missing or inconsistent task information can obstruct teacher execution and weaken the resulting supervision. We propose WorkFactory, a scalable…

- **[OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents](https://arxiv.org/abs/2610.37081v1)**
  - *Humza Nusrat, Kundan Thind*
  - `2026-10-27`
  - Background and purpose: Radiotherapy planning agents based on large language models (LLMs) decide when to submit a plan or request review but are evaluated mainly by dose. This study developed OpenGray, a benchmark of planning tasks with known correct decisions. Materials and met…

- **[Blindfold: Keeping the Audit Coin Secret from LLM Agents](https://arxiv.org/abs/2610.37055v1)**
  - *Wei Zhu, Meiyun Zuo, Huiping Sun*
  - `2026-10-27`
  - Audit-based certification bounds the violation rate of an LLM agent by auditing a random fraction $\varepsilon$ of actions and reweighting the audited labels; its validity is meant to rest only on the defender's audit coin. We show that it also rests on a confidentiality property…

- **[AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations](https://arxiv.org/abs/2610.36980v1)**
  - *Qiming Shi, Yikun Li, Beidi Luan et al.*
  - `2026-10-27`
  - Large language model (LLM) agents are extending agent-mediated commerce on the Web from shopping for consumers to operating businesses for sellers. In online-to-offline (O2O) commerce, decisions are issued through Web-based platforms but realized through costly physical execution…

- **[Proactive Memory for Event-Driven LLM Agents](https://arxiv.org/abs/2610.36967v1)**
  - *Jinyang Li, Zichuan Fu, Xian Wu et al.*
  - `2026-10-27`
  - Proactive LLM agents anticipate service opportunities from ongoing observations and accumulated history. Existing approaches emphasize recent context or retrieval of related memories, providing limited support for validating recurring behavioral regularities and assessing their a…

- **[Beyond QASecClaw: Agent Scaling, Verifier Feedback, and Evidence Reliability in Software Assurance](https://arxiv.org/abs/2610.36947v1)**
  - *S M Abdulla Al Mamun, Akif Islam, Mohd. Ruhul Ameen*
  - `2026-10-27`
  - Can additional specialist language-model contexts improve software assurance when deterministic tool evidence is already available? We study this question through five experiments spanning authored Java warning controls, OWASP Benchmark assessment, Defects4J test generation, SV-C…

- **[Vision-Language Agents Can Learn in Their Own Latent Worlds](https://arxiv.org/abs/2610.36925v1)**
  - *Haoxi Li, Sikai Bai, Jianfei Ma et al.*
  - `2026-10-27`
  - Learning from experience is essential for building the next generation of agents that continually expand their capabilities. Pretrained vision-language models (VLMs) already internalize rich world knowledge, yet this knowledge is rarely leveraged to drive policy improvement throu…

- **[Noise Steering: Exploiting Wake Steering and Acoustic Directivity for Noise-Constrained Wind Farm Control via Reinforcement Learning](https://arxiv.org/abs/2610.36888v1)**
  - *Martín de Frutos, Baptiste Corban, Claire Bizon Monroc et al.*
  - `2026-10-27`
  - Existing noise mitigation strategies for wind farms usually consist in reducing turbines power output, without accounting for the wake interactions between them and the noise emission directivity. This leads to over-conservative policies and unexploited wind power. Yet, turbine y…

- **[RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents](https://arxiv.org/abs/2610.36878v1)**
  - *Delin Wang, Sinuo Wang, Rui Sun et al.*
  - `2026-10-27`
  - Deep research agents conduct multi-step Web searches and synthesise retrieved information into analytical reports. Evaluating these outputs requires checking which analyses they deliver, beyond the presence of relevant facts. Query-specific binary rubrics make individual requirem…

- **[GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents](https://arxiv.org/abs/2610.36877v1)**
  - *Bingchao Wang, Yongcheng Jing, Shunyu Liu et al.*
  - `2026-10-27`
  - Mobile GUI agents are typically fine-tuned 7B-scale vision-language models (VLMs) that generate each action as text. However, these VLMs decode every action token by token, and even agents that score candidate actions keep a large language model or VLM in the loop, making them sl…

- **[When All Rollouts Fail: Policy-Compatible Joint Decoding for Hard-Problem Reasoning](https://arxiv.org/abs/2610.36849v1)**
  - *Zehao Wang, Hanzhu Chen, Runquan Gui et al.*
  - `2026-10-27`
  - Reinforcement Learning with Verifiable Rewards (RLVR) derives its learning signal from binary rewards via on-policy exploration and becomes a powerful paradigm for improving the reasoning of large language models. Yet it faces a learning cliff on problems beyond model's current a…

- **[Evolving Agent Teams](https://arxiv.org/abs/2610.36848v1)**
  - *Shiyi Cao, Ziming Mao, Dacheng Li et al.*
  - `2026-10-27`
  - The rapid progress of software engineering agents drives interest in applying them to open-ended problems such as GPU kernel optimization. However, we find that existing coding agents converge to local optima on real-world, expert-written kernels (e.g., FlashInfer). We introduce…

- **[When the Critic Falls Behind: Co-Evolving Rubrics and Harnesses for Continual Agent Self-Improvement](https://arxiv.org/abs/2610.36826v1)**
  - *Hao Chen, Yukun Yan, Ziyu Han et al.*
  - `2026-10-27`
  - Autonomous agents increasingly depend on harnesses that govern interaction, memory, tools, and execution around large language models (LLMs). While recent work has begun to evolve these harnesses from execution experience, the supervision used to guide evolution often remains rel…

- **[Who Knows What - and What Does It Support? Perspective-Bounded Evidence Calibration for Multimodal Theory of Mind](https://arxiv.org/abs/2610.36824v1)**
  - *Ziqi Liao, Jiaqi Shen, Yiming Na et al.*
  - `2026-10-27`
  - Theory of Mind (ToM), the ability to infer others' beliefs, goals, and intentions, is a cornerstone of social intelligence. Multimodal ToM requires inferring an agent's mental state from evidence that is available to that agent, rather than from the complete episode observed by t…

- **[Select-TTT: Query-Conditioned Selective Fast Weight Updates for In-Place Test-Time Training](https://arxiv.org/abs/2610.36794v1)**
  - *Yue Wu, Yang Zhang, Weinan Gan et al.*
  - `2026-10-27`
  - Test-time training (TTT) enables a deployed language model to internalize incoming context on-the-fly into a small set of fast-weight parameters, rather than merely treating it as transient context for attention. In-Place TTT recently made this idea practical for large language m…

- **[Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better](https://arxiv.org/abs/2610.36774v1)**
  - *Jialin Zhang, Lakshya A Agrawal, Shangyin Tan et al.*
  - `2026-10-27`
  - Reflective text optimization makes agentic systems better, but the optimization loop is itself a resource-hungry workload whose sequential structure leaves parallel evaluation capacity idle. We extend the open-source GEPA optimizer to propose and evaluate a batch of candidates on…

- **[Beyond the Evidence Coherence Trap: Agent-Driven Evidence Selection for Temporally Disordered Fake News Detection](https://arxiv.org/abs/2610.36764v1)**
  - *Chi Wang, Min Gao, Yifei Zhang et al.*
  - `2026-10-27`
  - Fake news undermines public trust and the integrity of online information ecosystems. Temporally disordered fake news is especially elusive because it rearranges factual events into a false chronology. Individual events may remain factually valid even when their temporal relation…

- **[From Voiceprints to User Entities: Online Speaker-Memory Construction for Multi-User Spoken Agents](https://arxiv.org/abs/2610.36713v1)**
  - *Yucong Zhang, Cancan Li, Bo Xiao et al.*
  - `2026-10-27`
  - Personalized spoken agents must identify speakers before accessing user-specific memory, yet memory benchmarks typically assume correctly attributed histories. We argue that voiceprints are observations of identity, not identities themselves, and formulate online speaker-memory c…

- **[Atom as an Agent: Emergent Order by Collective Predictive Coding](https://arxiv.org/abs/2610.36673v1)**
  - *Koji Hashimoto, Tadahiro Taniguchi*
  - `2026-10-27`
  - What is the intrinsic reason of emergence of macroscopic order parameter out of microscopic systems? In this article, we apply to physics the collective predictive coding (CPC), the theory of language/symbol emergence. As our language emerges out of our human communications, phys…

- **[The View from Nowhere: Population-Centered Agent Evolution](https://arxiv.org/abs/2610.36660v1)**
  - *Shuo Yan, Ningning Hou, Haoyu He et al.*
  - `2026-10-27`
  - Self-improving AI systems can revise the designs that govern their own behavior. Yet existing approaches center improvement on selected parent agents and their evolutionary experience, leaving the broader population largely underused. We identify a substantial gap between populat…

- **[Remembering Is Not Enough: Refining Memories and Learning When to Use Them in Multi-Agent Systems](https://arxiv.org/abs/2610.36652v1)**
  - *Yipeng Hao, Yuxuan Cai, Wenkai Ji et al.*
  - `2026-10-27`
  - Memory helps LLM-based multi-agent systems reuse experience, but stored advice can be flawed or applied in the wrong situation. Team-level success or failure alone cannot reliably show whether a memory needs correction or should not have been used. We propose DiscernMem, a traini…

- **[God Does Not Play Dice: Enforcing Batch Invariance in Agentic Kernel Generation](https://arxiv.org/abs/2610.36623v1)**
  - *Youwei Bao, Chengpeng Wang, Simin Chen*
  - `2026-10-27`
  - Large language model (LLM) serving systems dynamically batch user requests for GPU execution, so the same request may be processed alongside different requests across runs. If the GPU kernels lack batch invariance (BI), this changing batch context can alter the numerical output f…

- **[Dream-COP: Guiding Algorithm Discovery for Combinatorial Optimization Problems in an Experience World](https://arxiv.org/abs/2610.36618v1)**
  - *Kuan Xu, Jianming Wang, Ni Zhang et al.*
  - `2026-10-27`
  - Large language models (LLMs) enable algorithm discovery for combinatorial optimization problems (COPs) through iterative program generation and evaluation. A central challenge is how to organize search to discover better algorithms within a limited budget. Our key insight is that…

- **[InfraDev: Can Coding Agents Develop AI Infrastructure, and How Can We Tell?](https://arxiv.org/abs/2610.36589v1)**
  - *Yangshen Deng, Jiaqi Ruan, Yeqi Huang et al.*
  - `2026-10-27`
  - Coding agents are beginning to develop the production-grade AI infrastructure that trains and serves large models, yet existing benchmarks cover only single kernels or single-GPU tasks, and grade with tests and prompts that misjudge both correct and incorrect patches. We introduc…

- **[CASEL: Consequence-Aware Selective Execution for Reliable Long-Horizon Tool-Using Agents](https://arxiv.org/abs/2610.36570v1)**
  - *Yanyan Zhang, Fei Shen, Ting Yan et al.*
  - `2026-10-27`
  - Tool-using language agents increasingly modify external systems, yet most runtime safeguards allocate scrutiny by generic uncertainty scores or coarse mutation heuristics. We introduce CASEL (Consequence-Aware Selective Execution Layer), a model-agnostic runtime allocation policy…

- **[NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization](https://arxiv.org/abs/2610.36553v1)**
  - *Shuo Chen, Li Cui, Cunxin Huang et al.*
  - `2026-10-27`
  - Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in simulation-based and experimental applications, where evaluating the black-box objective can itself be costly. Thus, it remains a central chal…

- **[Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors](https://arxiv.org/abs/2610.36544v1)**
  - *Siddharth Jain, Venkat N. Vedam*
  - `2026-10-27`
  - Classification accuracy and true-positive and false-positive rates alone do not determine whether restarting an AI agent improves success. Using an exact alarm-to-action identity for an independent clean restart with zero monitoring overhead, we show analytically that a monitor w…

- **[RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding](https://arxiv.org/abs/2610.36533v1)**
  - *Buzhao Liu, Jianing Ye, Xiu Yuan et al.*
  - `2026-10-27`
  - Recently, LLM-based autonomous agents have shown strong capabilities in iteratively generating, evaluating, and refining executable solutions. In robotic manipulation, Code-as-Policy lets these agents search over modular and editable robot programs. However, effective program sea…

- **[CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments](https://arxiv.org/abs/2610.36484v1)**
  - *Kianté Fernandez, Caitlin Chen, Jialu Zhou et al.*
  - `2026-10-27`
  - Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI a…

- **[FIDES-Live: Evaluating Behavioral Concordance in Sequential Trading Agents](https://arxiv.org/abs/2610.36476v1)**
  - *Arther Tian, Alex Ding, Simon Wu et al.*
  - `2026-10-27`
  - Sequential trading agents produce decisions, orders, execution receipts, account states, and reports that need not agree, even when the final portfolio value is correctly computed. We present FIDES-Live, an operational extension of FIDES from generated strategy concordance to the…

- **[Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure](https://arxiv.org/abs/2610.36453v1)**
  - *Nardine Basta, Venus Haghighi, Dali Kaafar et al.*
  - `2026-10-27`
  - LLM agents that answer questions and act on behalf of users must decide when to yield to a user who disagrees. Disagreement may correct a genuine error or may be an attempt at manipulation. Prior work shows that models frequently abandon correct answers when challenged by users,…

- **[RouteDRAG: Learning to Route and Control Agentic Execution for Multimodal Document RAG](https://arxiv.org/abs/2610.36444v1)**
  - *Zekai Chen, Hao Zhu, Yu Liu et al.*
  - `2026-10-27`
  - Web-based applications increasingly rely on understanding long multimodal documents, where answering questions often requires combining information across pages, tables, and figures. Agentic retrieval-augmented generation addresses these tasks through iterative retrieval and reas…

- **[Your Agent Acts Differently When You're Around: How User Presence Changes Agent Behavior in Negotiation](https://arxiv.org/abs/2610.36435v1)**
  - *Jane Pan, You Lyu, Abe Bohan Hou et al.*
  - `2026-10-27`
  - LLM agents increasingly interact with other agents on behalf of users, yet how users in the loop affect their agents' behavior--for better or worse--remains poorly understood. We study this question through the lens of negotiation, where agents must represent users while strategi…

- **[LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction](https://arxiv.org/abs/2610.36433v1)**
  - *Xianxiang Zhao, Advik Mehta, Falak Sethi et al.*
  - `2026-10-27`
  - Construction safety management still struggles to produce daily safety bulletins (DSBs), structured daily communications that identify site-specific hazards, convey safety protocols, and set preventive measures for workers. Manual DSB creation takes 2-3 hours daily and yields inc…

- **[Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness](https://arxiv.org/abs/2610.37657v1)**
  - *Igor Shilov, Xiaoxue Yang, Alexander Panfilov et al.*
  - `2026-10-27`
  - We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens, enabling models to reason o…

- **[Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](https://arxiv.org/abs/2610.37648v1)**
  - *Andrew Szot, Samira Abnar, Omar Attia et al.*
  - `2026-10-27`
  - We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthA…

- **[Interpretable Meta-Policies for Neural Decision Making](https://arxiv.org/abs/2610.37451v1)**
  - *Raban Emunds, Jannis Blüml, Quentin Delfosse et al.*
  - `2026-10-27`
  - Deep Reinforcement Learning remains difficult to interpret and align due to the black-box nature of neural networks. While (neuro-)symbolic approaches improve transparency by incorporating symbolic reasoning, applying them directly to low-level actions results in overly complex,…

- **[Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction](https://arxiv.org/abs/2610.37441v1)**
  - *Yifei Yuan, Jakob Wolf, Ghaith Androwis et al.*
  - `2026-10-27`
  - Objective: This study aims to determine whether a hip-exoskeleton policy trained in simulation, by co-adapting with a musculoskeletal human model under a metabolic-energy reward, reduces the metabolic cost of walking in new users without per-user tuning, and how mechanical-power…

- **[Hyperparameter and Neural Architecture Search via Evolutionary Optimization for Reinforcement Learning: HPNAS-RL](https://arxiv.org/abs/2610.36882v1)**
  - *Nihal Acharya Adde, Hanno Gottschalk*
  - `2026-10-27`
  - In this study, we propose a dual-branch evolutionary framework that simultaneously performs Neural Architecture Search (NAS) and Hyperparameter Optimization (HPO) for Reinforcement Learning (RL) in Autonomous Driving (AD) tasks. While NAS has shown strong potential in automating…

- **[Impossibility of No-Regret in Multi-Agent Bidding](https://arxiv.org/abs/2610.36666v1)**
  - *Zongjun Yang, Rachitesh Kumar, Christian Kroer*
  - `2026-10-27`
  - We consider $T$ repeated second-price auctions across $n$ pacing bidders with i.i.d. item arrivals, and show that it is computationally impossible for all bidders to achieve no-regret simultaneously while satisfying their respective budget or return-on-investment constraints. The…

- **[CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning](https://arxiv.org/abs/2610.36469v1)**
  - *Jianwen Chen, Peng Xia, Kaide Zeng et al.*
  - `2026-10-27`
  - Large language model (LLM) agents interact with their environments through executable harnesses that govern tool use and feedback. Optimizing a harness for a fixed policy overlooks how its behavior changes during learning, while training a policy under a fixed harness leaves the…

- **[GEPA-Curator: Curated Learning for Self Improving Agents](https://arxiv.org/abs/2610.37651v1)**
  - *Zack Yu, Nicholas Lee, Minjae Lee et al.*
  - `2026-10-27`
  - Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesse…

- **[Metacognitive Decoding: Efficient Inference for Diffusion Language Agents](https://arxiv.org/abs/2610.37642v1)**
  - *Mingyu Zhao, Shuhang Lin, Ligong Han et al.*
  - `2026-10-27`
  - Diffusion language models offer a promising path to efficient agents through parallel token generation. However, efficient interaction requires adapting both where computation is spent and how much text is generated. We introduce a metacognitive controller that guides diffusion g…

- **[ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents](https://arxiv.org/abs/2610.37443v1)**
  - *Xinying Qian, Ying Zhang, Yu Zhao et al.*
  - `2026-10-27`
  - Long-term memory enables Large Language Models (LLMs) to maintain coherent and personalized interactions across extended conversations. However, existing memory systems face two key challenges: (1) Information Entanglement, where heterogeneous information is mixed within coarse-g…

- **[Game-Theoretic Solvers with Bayesian Opponent Modeling and Moral Rhetoric Framing for GLEE](https://arxiv.org/abs/2610.37397v1)**
  - *Hayden Arnold*
  - `2026-10-27`
  - We describe the agent we submitted to the GLEE Competition, which plays bargaining, negotiation, and persuasion games against a shared pool of human and AI opponents. The agent is built around three central components: a classical game-theoretic solver to compute numeric moves, a…

- **[Modeling Preference Dependencies with Directed Acyclic Graphs for Narrative-Driven Recommendation](https://arxiv.org/abs/2610.37280v1)**
  - *Mingzhe Lu, Jian Qin, Ruize Qin et al.*
  - `2026-10-27`
  - Narrative-driven recommendation allows users to express multifaceted needs through free-form text where stated preferences naturally qualify and condition one another. Existing methods typically treat narratives as flat keyword combinations or unconstrained generative queries, fa…

- **[TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces](https://arxiv.org/abs/2610.36918v1)**
  - *Mingyu Zhang, Zixu Li, Zhiheng Fu et al.*
  - `2026-10-27`
  - Large language model (LLM) agents rely on memory systems to leverage long-term interactions, yet existing systems typically retrieve memories based on their relevance to the current query and use them as contextual evidence. However, relevance alone does not characterize how a me…

- **[Words or Deeds? How LLMs Predict Users' Decisions in Human-Agent Dialogue](https://arxiv.org/abs/2610.36813v1)**
  - *Baiqiao Zhang, Shuai Ma, Zhifeng Liao et al.*
  - `2026-10-27`
  - Web systems increasingly predict users' decisions from what users say, yet when interests partly conflict, users may promise to cooperate to win the other side's cooperation and then not do so. Sales or service agents that rely on such promises may grant concessions to users who…

- **[DocSkill: Skill-Integrated Agentic Reasoning for Multilingual Multi-Hop Document Question Answering](https://arxiv.org/abs/2610.36759v1)**
  - *Jing Huang, Zhiya Tan, Changtao Miao et al.*
  - `2026-10-27`
  - Multilingual multi-hop document question answering (MMHop-DocQA) requires locating and integrating evidence across complex layouts, document pages, and diverse languages. Existing approaches include single-pass processing and adaptive tool use, but learning to coordinate evidence…

- **[A Harness Reducing over-Defensive Writing in Agents by Isolating Objections](https://arxiv.org/abs/2610.36717v1)**
  - *Xiaochen Chang*
  - `2026-10-27`
  - When expanding a report, writing with agents may introduce a stronger claim than the article makes and then disclaim it. This is called over-defensive writing. We assume that this is because the agent is writing for responding to an adversarial AI reviewer, instead of a human rea…

- **[Agentic Data Sampling Framework for Multilingual ASR via Linguistic-Aware Error-Driven Optimization](https://arxiv.org/abs/2610.36538v1)**
  - *Zhiheng Qian, Junhao Du, Jing Peng et al.*
  - `2026-10-27`
  - Multilingual automatic speech recognition (ASR) has achieved rapid progress with large-scale pretrained models and multilingual speech corpora. Previous studies have proved the pivotal role of data sampling in multilingual ASR performance. However, existing sampling strategies la…

- **[ETC-Bench: A Multilingual Benchmark for Evaluation-Side Transcript Canonicalization](https://arxiv.org/abs/2610.36527v1)**
  - *Zhiheng Qian, Junhao Du, Jing Peng et al.*
  - `2026-10-27`
  - Written transcripts of the same speech can differ in ways that are not uniquely determined by the speech signal. We formulate evaluation-side transcript canonicalization (ETC), which maps multiple surface forms to a single canonical form when their differences are not determined…

- **[Benchmarking Task Takeover Across Agent Handoffs](https://arxiv.org/abs/2610.36523v1)**
  - *Wenyuan Li, Guang Li, Dongyuan Li et al.*
  - `2026-10-27`
  - As agents collaborate on longer tasks, responsibility may pass between models before the work is complete. The receiving model must build on prior decisions, observations, and actions while addressing the remaining requirements. Evaluating this transition requires connecting the…

- **[TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments](https://arxiv.org/abs/2610.37592v1)**
  - *Alireza Saleh Abadi, Leen-Kiat Soh, Adam Eck et al.*
  - `2026-10-27`
  - Cooperative multi-agent reinforcement learning under centralized training with decentralized execution (CTDE) shapes decentralized policies with a centralized critic that observes the global state, then removes the critic at execution. The policies are optimized to rely on inform…

- **[A Serious-Game Testbed for Self-Governing Human-Machine Institutions](https://arxiv.org/abs/2610.36989v1)**
  - *Callum Berger, Jeremy Pitt, Stefan Sarkadi*
  - `2026-10-27`
  - AI agents no longer act alone: they cooperate, coordinate and compete within and between groups, increasingly alongside humans who are in, on or out of ``the loop''. Whether such mixed groups can govern themselves is an open question about machine behaviour and human-computer int…

- **[Feedback autocratic strategies in stochastic games](https://arxiv.org/abs/2610.36683v1)**
  - *Masahiko Ueda*
  - `2026-10-27`
  - A stochastic game is an optimal control problem for multiple agents in a stochastic environment. Stochastic games contain important practical problems, related to environmental issues or traffic flows. If the number of environmental states is one, such stochastic games are called…

- **[Which Hand Was Late? Diagnosis for Robot Failure Recovery in Bimanual Tool Use](https://arxiv.org/abs/2610.37533v1)**
  - *Baptiste Bonin, Caro Strickland, Audrey Durand*
  - `2026-10-27`
  - Failure diagnosers for robot manipulation are increasingly vision--language models (VLMs), trained and evaluated on single-arm failures produced by perturbing a successful demonstration. Bimanual tool use adds failures of other kinds: a tool that slips out of its socket while sti…

- **[kw-bench: Breaking Frontier Harnesses on Real-World Tasks](https://arxiv.org/abs/2610.36405v1)**
  - *George Juraj Salapa*
  - `2026-10-26`
  - Each new generation of frontier model pushes the edge of what is possible. Inside a harness -- a loop, a shell, a filesystem, the ability to write and run its own code -- a model can take on increasingly difficult work.   A growing body of work treats the coding-agent harness as…

- **[MAREval: A Multi-Agent Framework for Evaluating Natural Language Recommendation Explanations](https://arxiv.org/abs/2610.36389v1)**
  - *Reza Yousefi Maragheh, Jayesh Uddhav Kudase, Aysenur Inan et al.*
  - `2026-10-26`
  - Evaluating natural language explanations in recommender systems is essential for fostering user trust, transparency, and engagement. However, existing evaluation approaches like human evaluations, while accurate, are resource-intensive and impractical at the scale required by mod…

- **[HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning](https://arxiv.org/abs/2610.36374v1)**
  - *Fanqi Yu, Matteo Tiezzi, Cigdem Beyan et al.*
  - `2026-10-26`
  - Robotic agents operating in real-world environments must adapt continuously from a stream of multimodal demonstrations, often under constraints that preclude storing or revisiting past data. In this replay-free, single-pass lifelong imitation learning setting, sequential updates…

- **[WAKMan: Workload Aware KVCache Manager](https://arxiv.org/abs/2610.36355v1)**
  - *Suhas Kumar Morisetty, Vaibhavi Lokegaonkar, Sachin Mathew Varghese et al.*
  - `2026-10-26`
  - Prefix caching enables a Large Language Model (LLM) servers to reuse the Key-Value (KV) states and accelerate prefill computation stage for requests that share a prefix with earlier prompts, thus reducing latency and serving cost. With limited memory resource, the KV cache evicti…

- **[OA-RAG: Ontology-based Agentic RAG for Faithful LLM Reasoning](https://arxiv.org/abs/2610.36335v1)**
  - *Hui Yang, Jiaoyan Chen, Yongsheng Gao*
  - `2026-10-26`
  - Large language models (LLMs) perform well across many real-world tasks but remain prone to hallucination, limiting their reliability in domains such as biomedicine and healthcare, where answers must be grounded in established knowledge. Retrieval-augmented generation (RAG) mitiga…

- **[Ontology-guided multi-agent reasoning for explainable differential diagnosis](https://arxiv.org/abs/2610.36325v1)**
  - *Roxana Ramona Szomiu, George Ursu, Adrian Groza*
  - `2026-10-26`
  - Effective differential diagnosis depends on well structured and unambiguous patient case descriptions, since incomplete or ambiguous clinical information readily leads to diagnostic errors and inconsistent reasoning. Large Language Models (LLMs) have recently shown promising capa…

- **[When Retrieval Is Not Enough: Obsolete Facts in Agent Memory](https://arxiv.org/abs/2610.36308v1)**
  - *Oleeviya Babu Poikarayil, Tony Basil Babu, Abdulrahman Nahhas et al.*
  - `2026-10-26`
  - Memory-agent benchmarks often collapse retrieval and answer generation into one score, making it hard to tell whether a failure comes from missing an update or from not using an update that was already retrieved. We examine this distinction on the single-hop FactConsolidation tas…

- **[Freeze, Don't Clone: Fine-Tuning with Expressive Policies Without Retaining Offline Data](https://arxiv.org/abs/2610.36247v1)**
  - *Sami Nur Islam, Johan Obando-Ceron, Doina Precup et al.*
  - `2026-10-26`
  - Offline-to-online reinforcement learning uses offline pretraining to accelerate subsequent online learning. While many methods assume the offline dataset remains available throughout fine-tuning, there are many settings where this is not the case. Prior work attributes failures i…

- **[Agent or Human? Detecting Commits by AI Coding Agents in the Absence of Authorship Signatures](https://arxiv.org/abs/2610.36229v1)**
  - *Kosei Horikawa, Hao Li, Yutaro Kashiwa et al.*
  - `2026-10-26`
  - AI coding agents such as Claude Code, GitHub Copilot coding agent, and Cursor now commit directly to open-source repositories. Empirical studies of these agents identify their commits through authorship signatures, such as bot accounts and Co-authored-by trailers. These signature…

- **[Skill Dreaming: Evolving Repository Skills through Pull Request Streams](https://arxiv.org/abs/2610.36188v1)**
  - *Xinyuan Song, Hasibul Haque, Jay Somasundaram et al.*
  - `2026-10-26`
  - Large language model (LLM) agents increasingly rely on reusable skills for complex software engineering tasks, making skill libraries essential for repository development and maintenance. However, repository-specific skills must evolve with changing code structures, implementatio…

- **[Stratum: Repository Memory for Coding Agents Beyond the Context Window](https://arxiv.org/abs/2610.36153v1)**
  - *Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan*
  - `2026-10-26`
  - Context windows have grown a thousand-fold, yet coding agents still start every session with no memory of their past work. They re-read files, retry failed approaches, and forget root causes they established hours earlier. This is not a context-length problem but a memory-archite…

- **[Replication or Corroboration? An Axiomatic Framework for Evidential Dependence in Multi-Agent Debate](https://arxiv.org/abs/2610.36151v1)**
  - *Hoang-Loc Cao, Truong Thanh Hung Nguyen, Phuc Truong Loc Nguyen et al.*
  - `2026-10-26`
  - In multi-agent debates, matching reports can arise for two different reasons: agents may repeat the same evidence (replication), or they may provide separate evidential roots that support the same claim (corroboration). A judge must distinguish these two cases. Counting report oc…

- **[When Connectivity Misleads: Guiding Agentic Search with Contrastive Evidence Paths](https://arxiv.org/abs/2610.36134v1)**
  - *Junchen Li, Liang Xu, Rongzheng Wang et al.*
  - `2026-10-26`
  - Search agents can use cross-document graphs to discover sources through multi-hop connections and choose subsequent actions based on candidate rankings and relationships within a limited observation window. However, documents may rank highly because their numerous connections mak…

- **[Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses](https://arxiv.org/abs/2610.36114v1)**
  - *Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan*
  - `2026-10-26`
  - LLM agents are judged by two numbers: the size of the context window, and how often the final answer is correct. Both numbers miss a third thing: how much of a tool's output is lost before the model ever sees it. We measured this loss in a real tool-using agent. The agent finds t…

- **[Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol](https://arxiv.org/abs/2610.36108v1)**
  - *Yuepeng Hu, Chongyu Fan, Sirat Samyoun et al.*
  - `2026-10-26`
  - LLM agents increasingly access external tools through the Model Context Protocol (MCP), but the natural-language metadata used to describe those tools creates a prompt-injection surface. Within this established tool-poisoning surface, we study Log-To-Leak, an additive post-hoc lo…

- **[CohortFlow: A Steerable Clinical Cohort Curation Agent with Localized Semantic Correction](https://arxiv.org/abs/2610.36100v1)**
  - *Neil Chen, Adrian Serapio, Hanxue Gu et al.*
  - `2026-10-26`
  - Language model agents for clinical cohort curation should accommodate evolving eligibility criteria without repeatedly processing unchanged requirements. We introduce CohortFlow, a steerable agent that represents natural language corrections as localized updates to a structured c…

- **[I-HITL: Inalienable Human-in-the-Loop](https://arxiv.org/abs/2610.35835v2)**
  - *Samuel Breckenridge, Dani Vilardell, Wenhao Wang et al.*
  - `2026-10-26`
  - Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.   We introduce the co…

- **[Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models](https://arxiv.org/abs/2610.35829v1)**
  - *Amine Lbath, Massih-Reza Amini*
  - `2026-10-26`
  - A vulnerability costs more to fix the later it is discovered. As coding agents generate code faster than developers can review it, software needs a first line of defense screening each new function in real time. LLM agents have recently become capable of finding real-world vulner…

- **[Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](https://arxiv.org/abs/2610.35817v2)**
  - *Benjamin Pikus, Daniel Saunders, Mircea Mironenco et al.*
  - `2026-10-26`
  - A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task. To achieve these two skills, we introduce Zero-real Agent Policy (ZAP), a recipe that teaches a small off-the-shelf vision-language model to control a robot…

- **[Do Coding Agents Still Need a Debugger? Frontier-Model-Based Fault Localization at the Accuracy Ceiling](https://arxiv.org/abs/2610.36015v1)**
  - *Christoph Daxerer, Johann Glock, Christian Macho et al.*
  - `2026-10-26`
  - Background: To localize a fault, a coding agent can reason from source code alone or use debugger assistance by running the program and stepping through it in an interactive debugger. While earlier agents struggled with static execution tracing and debugger operation, frontier LL…

- **[A Unified Arena for LLM Agents across Diverse Eurogame](https://arxiv.org/abs/2610.35773v1)**
  - *Fengrui Zhang, Xiang Li, Ruomeng Ding et al.*
  - `2026-10-26`
  - Interactive environments offer a practical way to evaluate large language model (LLM) agents, and competitive games extend this evaluation to decisions shaped by competing goals and other agents' choices. Yet existing evaluations confined to individual games or execution framewor…

- **[Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents](https://arxiv.org/abs/2610.35767v1)**
  - *Tingzhu Bi, Xun Zhang, Jinglin Li et al.*
  - `2026-10-26`
  - Root cause analysis (RCA) of microservice failures has attracted many LLM agents whose investigation is hand-crafted, through standard operating procedures, fixed stages and role agents. Each is evaluated on its own data against few baselines, so it is unknown whether this design…

- **[CIVER: Causal Intervention Verification for Reliable Code Review](https://arxiv.org/abs/2610.36010v1)**
  - *Xinyuan Song, Hasibul Haque, Jay Somasundaram et al.*
  - `2026-10-26`
  - Code review is essential for maintaining software repositories by identifying defects, improving code quality, and supporting reliable software evolution. With the growing adoption of LLM-based coding agents, an increasing number of code contributions and repository changes are g…

- **[MiRL: Error-Targeted Reinforcement Learning for Correcting Terminal Agent Misbehaviors](https://arxiv.org/abs/2610.35697v1)**
  - *Runchu Tian, Zaid Khan, Zun Wang et al.*
  - `2026-10-26`
  - Error-targeted learning gives a legible way to improve a model: identify specific weaknesses of the model, train the model to fix these weaknesses, and check whether the weaknesses are fixed. We study how to apply error-targeted learning to terminal agents, which solve long-horiz…

- **[EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation](https://arxiv.org/abs/2610.35690v1)**
  - *Yitao Xiao, Xu Zhang, Ye Cheng et al.*
  - `2026-10-26`
  - Serving web queries at scale with multi-agent systems requires jointly configuring large language models, collaboration modes, agent counts, interaction rounds, and skills. However, the resulting configuration space grows combinatorially, while sparse execution rewards provide li…

- **[Provably Efficient Q-learning for Robust Reinforcement Learning](https://arxiv.org/abs/2610.35656v1)**
  - *Yuchen Jiao, Gen Li*
  - `2026-10-26`
  - Standard reinforcement learning (RL) algorithms based on Markov Decision Processes (MDPs) are vulnerable to sim-to-real gaps. To address this issue, distributionally robust RL algorithms based on robust MDPs (RMDPs) have been proposed, for ensuring that agents can perform reliabl…

- **[From Language to Drives: A Multimodal Framework for Aligning Autonomous Robots with Human Purposes](https://arxiv.org/abs/2610.35629v1)**
  - *Diana Cerdas-Vargas, Alejandro Romero, Richard J. Duro*
  - `2026-10-26`
  - This work explores a multimodal approach to the alignment of the behavior of open-ended learning autonomous robots with human purposes through the use of large language models as cultural enablers. While autonomous robots can generate their own skills and goals through interactio…

- **[Evolve on Graph: Self-Evolving Knowledge Graph Reasoning without Question Annotations](https://arxiv.org/abs/2610.35598v1)**
  - *Zongyuan Sun, Shuai Zhao, Ke Shu et al.*
  - `2026-10-26`
  - Knowledge graphs (KGs) provide reliable external knowledge for multi-hop factual reasoning with large language models (LLMs), yet most KGs in real-world domains such as finance and industry lack question--answer (QA) annotations. Without such annotations, existing methods struggl…

- **[KAPPA: Checking the Proofs in Statistics Papers with Lean 4 and Language Model Agents](https://arxiv.org/abs/2610.35596v1)**
  - *Zihua She, Xiao Wang*
  - `2026-10-26`
  - Papers in statistical theory rest on long proofs that few readers check line by line. We present KAPPA (Kit of Agents for Proof-checking Papers with a proof Assistant), open-source software that organizes language model agents, run by Claude Code, to translate the proofs of a LaT…

- **[Agentic Algorithm Design: LLMs that Propose, Formalise, and Prove Runtime Bounds for Evolutionary Algorithms in Lean](https://arxiv.org/abs/2610.35595v2)**
  - *Per Kristian Lehre*
  - `2026-10-26`
  - LLMs now prove hard theorems in Lean. Can they also design algorithms and prove their correctness and efficiency? LLM-guided design of optimisation heuristics (such as AlphaEvolve) is purely empirical. Automated theorem provers with LLMs prove given statements. So far, there has…

- **[Infinity Machine: a self-improving AI agent for research](https://arxiv.org/abs/2610.35579v1)**
  - *Harish Santhanalakshmi Ganesan*
  - `2026-10-26`
  - We present the Infinity Machine, a self-improving AI agent that we use for research on problems whose answers aprogram or data can check. Each candidate solution is produced by a full tool-using agent that works for up to an hour in a fresh sandbox; proposers see only a public sc…

- **[Governing Enterprise AI Traffic at Scale: Design and Operation of a Policy-Driven, Multi-Vendor LLM Gateway on Envoy](https://arxiv.org/abs/2610.35509v1)**
  - *Mithun Sasidharan, Srinivasan Manoharan, Rupesh Thakur et al.*
  - `2026-10-26`
  - Large organizations consume large language models (LLMs) from several vendors at once, each with its own API dialect, credential model, streaming protocol and pricing. Integrated directly, this heterogeneity yields credential sprawl, format lock-in, unbounded spend and inconsiste…

- **[Test-Time Confidence Adaptation under RL-Induced Trajectory Shift](https://arxiv.org/abs/2610.35500v1)**
  - *Zhenzhen Ren, Xiaoqing Zhang, GuoBiao Li et al.*
  - `2026-10-26`
  - Trajectory-based confidence estimation has shown promising performance for large language models (LLMs) by leveraging rich signals from their reasoning processes. However, we find that such confidence estimators can degrade substantially after agentic reinforcement learning (Agen…

- **[The Hidden Costs of Forgetting: A Study of Trajectory Deletion in Software Engineering Agents](https://arxiv.org/abs/2610.35496v1)**
  - *Fernando Vallecillos-Ruiz, Islem Bouzenia, Michael Pradel et al.*
  - `2026-10-26`
  - Software engineering agents resend their entire trajectory to an LLM at every turn, motivating online trajectory reduction. Prior work shows that randomly deleting 75% of tokens in old turns may preserve agent effectiveness, but it remains unclear why, how agents compensate for m…

- **[ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation](https://arxiv.org/abs/2610.35486v1)**
  - *Param Biyani, Sebastien Luyasu, Cedric Potvliege et al.*
  - `2026-10-26`
  - Theory and experiments suggest that capable AI agents may resist shutdown. Existing shutdown evaluations are informative but limited in coverage and vulnerable to evaluation awareness. We introduce ShutdownMod, a method that turns any agent trajectory into a shutdown evaluation b…

- **[Beyond Federated Learning: Decentralized Agentic Systems for Self-Evolving Clinical Intelligence](https://arxiv.org/abs/2610.35453v1)**
  - *Haoyuan Li, Mathias Funk, Aaqib Saeed*
  - `2026-10-26`
  - Clinical expertise is inherently distributed: it resides not in any single dataset or institution but in the accumulated reasoning experiences of thousands of clinicians navigating diverse patient populations, resource constraints, and evolving treatment protocols. Yet current ap…

- **[Skill$^{\infty}$: Recursive Self-Improvement for Agent Skill Optimization](https://arxiv.org/abs/2610.35434v1)**
  - *Wangcheng Tao, Zhanglu Yan, Han Wu et al.*
  - `2026-10-26`
  - Recursive self-improvement (RSI), in which a system also improves the way it improves, is a long-standing aspiration on the path to AGI. Language agents increasingly store procedural knowledge in reusable skills. Optimizing skills offers a direct way to achieve RSI, because the o…

- **[PolicyMediator: Multi-Regional Policy Learning through Mediation Agents with Evolving Skills in OPC Ecosystems](https://arxiv.org/abs/2610.35997v1)**
  - *Jie Li, Bin Guo, Georgina Curto et al.*
  - `2026-10-26`
  - One-person companies (OPCs) are emerging enterprises operated by individual entrepreneurs through digital platforms and LLM-based AI agents. These highly skilled entrepreneurs are characterized by being digital nomads, with limited reliance on local ecosystems. Governments in Chi…

- **[Belief-Conditioned Multi-Agent Actor Critic for Decentralized LLM Collaboration](https://arxiv.org/abs/2610.35398v1)**
  - *Tianle Chen, Shuo Liu, Christopher Amato*
  - `2026-10-26`
  - Recent work has explored optimizing LLM collaboration through Multi-Agent Reinforcement Learning (MARL), but many approaches still rely on predefined workflows, limiting efficiency and scalability. Decentralized LLM collaboration is challenging because agents execute independentl…

- **[Autonomous Structural Discovery Of Bioprocess Dynamics And Kinetics Via LLM-Driven Agents](https://arxiv.org/abs/2610.35391v1)**
  - *Erdal Aydin, Yaman Arkun*
  - `2026-10-26`
  - High-fidelity digital twins in continuous biomanufacturing are often bottlenecked by incomplete kinetic models, while standard data-driven algorithms (e.g., SINDy, PINNs) lack interpretability or impose rigid physical assumptions. This paper introduces a hybrid closed-loop archit…

- **[MarkovSim: an LLM Agent Harness with Bounded Context for Long-Horizon Computational Simulation](https://arxiv.org/abs/2610.35349v1)**
  - *Yeui-Lung Lei, Wen-Bo Chen, Pan Zhang*
  - `2026-10-26`
  - Recent studies have applied large language model (LLM) agent systems to computational simulation workflows. Such workflows are long-horizon, so the information generated can exceed what an LLM can reason over at once, its context window. Context management is therefore essential,…

- **[RepoTrace: Improving Requirement Tracing in Multi-Round Agent Interactions](https://arxiv.org/abs/2610.35333v1)**
  - *Huanyu Liu, Yezheng Cheng, Jinliang You et al.*
  - `2026-10-26`
  - Code agents have become increasingly capable of performing software engineering tasks through interaction with software environments. However, agents tend to degrade as the number of interaction rounds increases, making it difficult to maintain existing software during iterative…

- **[RSIV-Harness: A Recursive Self-Improvement Harness Framework for Open-Domain Conversational Text-to-Visualization](https://arxiv.org/abs/2610.35316v1)**
  - *Jiawei Lu, Chen Zhang, Jinwei Lu et al.*
  - `2026-10-26`
  - Users often request charts without knowing which database or table holds the relevant data. Such requests may be ambiguous, and users may ask follow-up questions to deepen their analysis or iteratively refine existing charts. A useful assistant must therefore discover relevant da…

- **[PROBE: Frontier Coding Agents Find Different Bugs Than Maintainers Fix](https://arxiv.org/abs/2610.35987v1)**
  - *Marco Paina, Mark Niklas Müller, Niels Mündler-Sasahara et al.*
  - `2026-10-26`
  - Proactive bug discovery is an important software-engineering problem. Even though coding agents are already widely deployed in this domain, their capabilities remain understudied. In particular, the challenging task of finding all bugs that human maintainers would repair across a…

- **[AgenticCity-Bench: Longitudinal Multimodal Observations of Urban Dynamics with Agentic Reasoning](https://arxiv.org/abs/2610.35293v1)**
  - *Xiaofei Yu, Kailai Sun, Yanyu Mao et al.*
  - `2026-10-26`
  - City systems are shaped by interactions among infrastructure, human activity, and environmental conditions. Existing earth observation and urban benchmarks are limited in unified modeling and in capturing their joint dynamics. We introduce AgenticCity-Bench, a longitudinal multim…

- **[Proof-of-Agentness: Towards Verifying Agents on the Web](https://arxiv.org/abs/2610.35288v1)**
  - *Zuyao Xu, Xiang Li*
  - `2026-10-26`
  - CAPTCHAs and bot detection have helped protect Web services from automated abuse for decades by distinguishing humans from bots. However, the emergence of LLM-powered agents introduces a new setting: Web services increasingly accommodate agents as legitimate users. Without a way…

- **[Joint Latent Reasoning and Observation for Agentic Video Understanding](https://arxiv.org/abs/2610.35229v1)**
  - *Junzhang Liu, Hao Yuan, Qi Zhang et al.*
  - `2026-10-26`
  - Effective video agents must learn not only how to answer, but also where to look next. Transferring this capability to smaller models is challenging because each observation serves two purposes: supporting an answer and guiding the search for further evidence. Textual description…

- **[SkillLifeBench: Benchmarking Security Across the Lifecycle of Agent Skills](https://arxiv.org/abs/2610.35215v1)**
  - *Chenxu Zhang, Zhou Liu, Wu Xin et al.*
  - `2026-10-26`
  - Web agents reuse skills whose stored code, selected version, and loaded implementation can diverge across tasks and updates. SkillLifeBench links these states to task outcomes in 388 paired scenarios spanning implementation, interface, runtime, composition, and version changes. W…

- **[Generation and Verification: Human-Agent Collaboration for Safety-Critical Automotive Software Engineering](https://arxiv.org/abs/2610.35982v1)**
  - *Elizaveta Zinovyeva, Aiham Taleb, Nikita Kozodoi et al.*
  - `2026-10-26`
  - Research on coding agents mainly focuses on generation quality. Yet, safety-critical automotive software makes two additional demands. It prioritizes verification, since every change is reviewed, traced to a requirement, and checked against industry standards such as MISRA and AU…

- **[Same Story, Different Lens: A Multi-Agent System for Cross-Outlet News Framing Analysis](https://arxiv.org/abs/2610.35208v1)**
  - *Affan Yasin, Yueqi Lyu, Rubia Fatima et al.*
  - `2026-10-26`
  - News outlets covering the same event differ in what they emphasize and omit. \textit{Same Story, Different Lens} is an experimental research prototype for comparing these choices. It collects world and politics coverage from 17 outlets, groups reports about the same event, and pr…

- **[V$^3$AST-Bench: Verifiable, Valid, and Versatile Safety Evaluation for Coding Agents](https://arxiv.org/abs/2610.35188v1)**
  - *Weitao Feng, Hengheng Xiong, Zihao Zeng et al.*
  - `2026-10-26`
  - Large language models increasingly act through code, modifying repositories, executing programs, and interacting with services in agent form. Their actions introduce risks that cannot be assessed from generated responses alone. Safety evaluation must verify actual consequences, d…

- **[AutoEnergyDesign: An LLM-Driven Agent for Automatic Energy System Design Optimization](https://arxiv.org/abs/2610.35160v1)**
  - *Amedeo Buonanno, Salvatore Fabozzi, Maria Valenti*
  - `2026-10-26`
  - Designing building energy systems is a high-dimensional, mixed-integer search problem: when each design is evaluated by a year-long simulation, black-box optimizers typically need hundreds of evaluations. This paper presents AutoEnergyDesign, a framework in which a Large Language…

- **[UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity](https://arxiv.org/abs/2610.35980v1)**
  - *Yijun Zhou, Minghao Shao, Ke Zhang et al.*
  - `2026-10-26`
  - Game development stresses coding agents in ways general software engineering does not: correctness depends on how engine APIs, serialized scene state, and runtime behavior interact, not on source code alone. Existing benchmarks mainly target platforms such as Godot and heavily re…

- **[LongSearchEval: Evaluating Long-Horizon Web Search Capabilities of Large Language Models via a Trajectory-Aware Agent Framework with Failure-Node Localization](https://arxiv.org/abs/2610.35150v1)**
  - *Jialiang Liu, Shusheng Li, Wenjun Tan*
  - `2026-10-26`
  - Long-horizon web search requires LLM-based agents to integrate information across web pages through extended interactions under task-specific constraints. Evaluating this capability is important not only for measuring final answer quality, but also for assessing whether an agent…

- **[Locked In: Multi-Objective RL for the AI Data Center Build-Out](https://arxiv.org/abs/2610.35147v1)**
  - *Satyapragnya Kar, Rajarshi Das, PR Panigrahi*
  - `2026-10-26`
  - AI data center build-out is a multi-trillion-dollar, multi-decade infrastructure program. Yet siting, power procurement, and cooling decisions are still made with static, single-point scoring tools. These tools are evaluated once, on day-zero numbers. This is a poor fit. A site's…

- **[Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models](https://arxiv.org/abs/2610.35138v1)**
  - *Xilin Wei, Shengyuan Ding, Xinyu Fang et al.*
  - `2026-10-26`
  - Evaluating human-AI co-design requires testing whether coding agents can translate real users' multimodal requests into working application revisions. We introduce Co-Design Bench, a reference-free benchmark of 273 tasks curated from 37,463 deduplicated queries across 26,314 real…

- **[Improving Instruction Hierarchy by Learning from Goal-Goal Conflicts](https://arxiv.org/abs/2610.35093v1)**
  - *Sizhe Chen, Sanjay Kariyappa, Liwei Jiang et al.*
  - `2026-10-26`
  - The recent incident in which OpenAI agents autonomously compromised Hugging Face's infrastructure illustrates the importance of instruction hierarchy (IH): an LLM should follow lower-priority instructions, such as user requests, only when they do not conflict with higher-priority…

- **[CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems](https://arxiv.org/abs/2610.35082v1)**
  - *Yujia Zheng, Tianhao Li, Shangzhi Xu et al.*
  - `2026-10-26`
  - Agent Skills allow LLM agents to combine reusable capabilities, but checking each Skill in isolation cannot rule out policy violations when they are composed. We term such failures Conflict of Skills (CoS): artifacts or assessment signals produced for one purpose may be reused do…

- **[PatentAgentBench: Benchmarking LLM Agents with Professional Patent Task Suites](https://arxiv.org/abs/2610.35031v1)**
  - *Yijie Hu, Wei Li, Junjie Zhou et al.*
  - `2026-10-26`
  - Patent practice lies at the intersection of technical, legal, and linguistic work, making it challenging yet crucial to technological innovation. Recently, rapid advances in large language models (LLMs) and agentic systems have demonstrated the potential to complete realistic bus…

- **[AskGLP1: A Knowledge Graph LLM Agent for Exploring GLP-1 Experience from Online Patient Narratives](https://arxiv.org/abs/2610.34987v1)**
  - *Zhaoqian Xue, Anay Somani, Siddhartha Singh et al.*
  - `2026-10-26`
  - GLP-1 medications are increasingly used for weight management, and many people share their experiences online. These narratives show why people take the drugs and what they experience, but they remain unstructured and disconnected from formal pharmacovigilance. We therefore prese…

- **[The Target Agent Is Its Own Best Critic but a Poor Proposer: Self-Improved Red Teaming](https://arxiv.org/abs/2610.34965v1)**
  - *Mintong Kang, Stephen Rawls, Melissa Kazemi Rad et al.*
  - `2026-10-26`
  - Automatic red teaming increasingly relies on large language models (LLMs) to iteratively diagnose failed attacks and propose improved adversarial prompts or injections. Although prior work strengthens this loop through prompt engineering and search-harness design, the mechanisms…

- **[GUIFlow: Temporal Redundancy-Aware Incremental Inference for GUI Agents](https://arxiv.org/abs/2610.34959v1)**
  - *Ye Li, Haoran Ding, Huanan Liu et al.*
  - `2026-10-26`
  - GUI agents built on vision-language models interact with continuously evolving interfaces, yet conventional inference repeatedly recomputes representations of largely overlapping observations and histories. This mismatch makes multi-step interaction costly, while changes in conte…

- **[Reasoning Patterns for Efficient AI Coding: An Empirical Study](https://arxiv.org/abs/2610.34943v1)**
  - *Zhe Yin, Yuling Shi, Xiaodong Gu et al.*
  - `2026-10-26`
  - Large Reasoning Models (LRMs) generate long reasoning traces that expose intermediate inference behavior, offering opportunities to study and control reasoning in AI coding. However, the underlying patterns in these traces and their potential for analyzing and guiding coding mode…

- **[How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation](https://arxiv.org/abs/2610.34938v1)**
  - *Christoph Treude, Sebastian Baltes*
  - `2026-10-26`
  - Coding agents can adapt their harnesses, the software, configuration, and instructions used to run them, based on experience from earlier tasks, but whether these adaptations improve their behavior on later tasks remains unclear. We study \retro, a skill that asks an agent to rev…

- **[AIPC: Evidence-Guided Agent Workflows for PyTorch Project Deployment](https://arxiv.org/abs/2610.34890v1)**
  - *Zhanwei Wu, Jianhao Su, Brian Zhang et al.*
  - `2026-10-26`
  - Deploying and optimizing a PyTorch inference project on a dedicated accelerator, especially an on-device NPU, requires more than using a framework device API as with CUDA. The project must be converted into hardware-runtime artifacts and adapted to the target toolchain and applic…

- **[NumTrace: Auditing the Number Provenance of Financial Analyst Agents](https://arxiv.org/abs/2610.34887v1)**
  - *Tianlei Zhu, Matt White, Xue Liu et al.*
  - `2026-10-26`
  - A numerical claim generated by a financial analyst agent can match a number in a company filing but refer to the wrong entity, concept, period, unit or scope. A check based on reference answers can mark such an answer as wrong but does not explain why it fails. In this paper, we…

- **[ClinVerse: A Realistic Multi-Agent Diagnostic Environment for Training and Evaluating Medical Agents](https://arxiv.org/abs/2610.34878v1)**
  - *Sirry Chen, Fangke Chen, Xuanwen Ding et al.*
  - `2026-10-26`
  - Disease diagnosis is a key application of large language model (LLM) agents in healthcare. However, existing medical agents are primarily trained and evaluated with static question-answering data, providing limited opportunities to learn active information acquisition, examinatio…

- **[Adaptive Retrieval, Selective Answers: Evaluating Conformal Factuality in Agentic RAG](https://arxiv.org/abs/2610.34872v1)**
  - *Muhammad Aimal Rehman, Chi-Kuang Yeh*
  - `2026-10-26`
  - Retrieval-augmented generation (RAG) can improve factual grounding without guaranteeing that every generated claim is supported. Previous work has studied claim-level conformal factuality in single-stage RAG and, more recently, multi-hop RAG. We examine its behavior in agentic RA…

- **[DecoyCount: Evaluating Visual-Reasoning Misalignment in Counting](https://arxiv.org/abs/2610.34855v1)**
  - *Qiuyi, Zhang, Zhen Xu et al.*
  - `2026-10-26`
  - Visual counting benchmarks report whether vision-language models produce the correct number, but not whether errors arise from perception or reasoning. We introduce DecoyCount, a benchmark built from 1,660 real-world images with designed decoys across seven mechanisms, along with…

- **[Collective Emergent Alignment: Measuring and Amplifying Interaction-Induced Reasoning Alignment in Multi-Agent LLMs](https://arxiv.org/abs/2610.34836v1)**
  - *Boxuan Wang, Zhuoyun Li, Sarvapali D. Ramchurn et al.*
  - `2026-10-26`
  - Multi-agent large language model (LLM) systems can exhibit emergent behaviors through interaction, yet whether a similar phenomenon exists for reasoning alignment remains largely unexplored. We study whether agent interaction produces additional reference-grounded reasoning align…

- **[Centralized Critics for N-Agent Ad Hoc Teamwork](https://arxiv.org/abs/2610.34799v1)**
  - *Andrew McAlinden, Caroline Wang, Steven Shi et al.*
  - `2026-10-26`
  - Centralized training with decentralized execution (CTDE) has become the dominant paradigm in multi-agent reinforcement learning (MARL), motivating extensive study of what privileged information should be made available to the critic during training. While prior work has examined…

- **[The Physical Cost of Context: Quality-Constrained Resource Accounting for Coding Agents](https://arxiv.org/abs/2610.34763v1)**
  - *Zhongming Yu, Yitong Ma, Hengjia Yu et al.*
  - `2026-10-26`
  - Coding agents resend a growing context on every model call, and context policies are usually judged by the prompt tokens they save. Executed work also depends on call count and prefix reuse: a caching runtime prefills only the tokens after the longest cached prefix. A shorter pro…

- **[Babysitting AI Agents: A User-Centered Taxonomy and Study of Agentic Delegation Failures](https://arxiv.org/abs/2610.34748v1)**
  - *Shravika Mittal, Sunnie S. Y. Kim, Scott Counts et al.*
  - `2026-10-26`
  - Users are increasingly delegating tasks to AI agents, allowing agents to perform long-running, multi-step workflows on their behalf. However, agents may perform these tasks in ways that depart from users' expectations for how they should be carried out, leading to what we call ag…

- **[Query-Driven Learning for Lifted Reasoning](https://arxiv.org/abs/2610.34747v1)**
  - *Luise Ge, Brendan Juba*
  - `2026-10-26`
  - Learning and reasoning are both essential to intelligent agents, but have traditionally been treated as two separate stages: first learning a knowledge base from data (or taking one as given), and then verifying queries as if the knowledge base were complete. This separation has…

- **[SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745v1)**
  - *Luke Hollis, Tianxing Fan, Heng Yang*
  - `2026-10-26`
  - Visual captures provide detailed scene appearance, but converting them into interactive simulation environments requires object reconstruction, physical modeling, and correction of intermediate errors. We present SceneAgent, an agentic pipeline that coordinates these steps throug…

- **[SKALOS: Learning to Distinguish Similar Skills with Capability Graphs](https://arxiv.org/abs/2610.34728v1)**
  - *Wenhan Xiao, Ziwei Zhang, Xingcheng Fu et al.*
  - `2026-10-26`
  - Skills provide LLM agents with reusable procedural knowledge, making appropriate skill selection essential for reliable agent behavior. As skill libraries expand, distinguishing semantically similar candidates becomes increasingly difficult. Existing methods encode or rewrite ski…

- **[CEPO: A General Framework for Improving Prompt Optimization in Multi-Agent Systems](https://arxiv.org/abs/2610.34722v1)**
  - *Jongha Kim, Seohyun Lee, Jonathan Minho Chung et al.*
  - `2026-10-26`
  - Multi-agent systems (MAS) require both effective coordination and specialized task execution. Existing prompt optimization approaches typically couple these functions within agent-specific prompts. We introduce Coordinator-Executor Prompt Optimization (CEPO), a general framework…

- **[Intervene, Calibrate, Discover: Learning Causal Structure from Pixels](https://arxiv.org/abs/2610.34711v1)**
  - *Ziyi Ding, Xiaodi Huang, Xianxin Lai et al.*
  - `2026-10-26`
  - Learning high-level causal variables from low-level observations is a central problem for artificial intelligence. With known node semantics but an unknown graph, visual readout errors can misalign model settings with environment intervention values. We address this mismatch by p…

- **[Movable-Element Multi-Functional RIS-Assisted Hybrid RSMA-NOMA: A Constrained Hybrid Reinforcement Learning Approach](https://arxiv.org/abs/2610.34701v1)**
  - *Li-Hsiang Shen, Chi-Te Kuo*
  - `2026-10-26`
  - In this work, we propose a movable-element (ME) multi-functional reconfigurable intelligent surface (MF-RIS) architecture, termed MM-RIS, which integrates element mobility with adaptive signal reflection, transmission, amplification, and energy harvesting (EH) to enhance communic…

- **[Knowing When the Evidence Is Enough: Requirement-Directed Search with Horn-Closure Certificates](https://arxiv.org/abs/2610.34684v1)**
  - *Xinyu Zhang, Weiwei Sun*
  - `2026-10-26`
  - After each Web search, a search-augmented model must decide whether its evidence suffices: answer, search again, or abstain. Prevailing systems leave this to holistic model judgement, which can accept a context naming every entity yet lacking one required fact. We instead make su…

- **[Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents](https://arxiv.org/abs/2610.34673v1)**
  - *Xinyu Zhang, Weiwei Sun*
  - `2026-10-26`
  - Large language model (LLM) agents that serve users across many sessions must choose, for every request, the few stored memories that enter a limited context window. This choice largely decides whether the agent answers correctly, and it runs on every request at Web scale. This se…

- **[Hierarchical Task Network planning in the Goal Lifecycle](https://arxiv.org/abs/2610.34668v1)**
  - *Paola Rizzo, Hector Munoz-Avila, David W. Aha*
  - `2026-10-26`
  - Goal reasoning (GR) is the process by which intelligent agents continually reason about the goals they are pursuing, which may lead to goal change, for instance when opportunities arise, or when events cause discrepancies among expected and actual outcomes of actions planned to a…

- **[Thinking-in-Bets at Test Time Reduces Sycophantic Revisions in LLM Agents](https://arxiv.org/abs/2610.34654v1)**
  - *Nghi D. Q. Bui*
  - `2026-10-26`
  - Language model agents often abandon correct work when a user challenges it, yet simply telling them to stand firm makes them ignore real mistakes. Once an agent reads a complaint, it tends to discount its own earlier checks in order to agree with the user. We introduce Thinking-i…

- **[RobotAgentBench: Towards Open-world Robot Autonomy](https://arxiv.org/abs/2610.34649v1)**
  - *Lingjun Mao, Jinglin Cao, Lukun He et al.*
  - `2026-10-26`
  - Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm fo…

- **[SlowLab: Benchmarking Autonomous AI Agents on a Year of Experiments They Cannot Undo](https://arxiv.org/abs/2610.34644v1)**
  - *Ningpei Ding, Zai Wen Feng*
  - `2026-10-26`
  - AI agents are increasingly proposed as autonomous experimenters, yet the benchmarks that test them mostly offer cheap experiments that answer at once. Experiments in physical facilities are different: they take months, occupy scarce equipment and cannot be undone. We present Slow…

- **[Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning](https://arxiv.org/abs/2610.36075v1)**
  - *Koen Ponse, Aske Plaat, Thomas M. Moerland*
  - `2026-10-26`
  - Hardware-accelerated reinforcement learning in JAX has gained rapid popularity in recent years and has proven to be a successful method of scaling online reinforcement learning. The resulting ecosystem, however, is fragmented: environment suites define their own interfaces, and a…

- **[FOCUS: Active Critic Learning for Long-Horizon Language Model Agents](https://arxiv.org/abs/2610.35801v1)**
  - *Zhengping Jiang, William Jurayj, Liaoyaqi Wang et al.*
  - `2026-10-26`
  - Sparse outcome rewards make it difficult for long-horizon language-model agents to assign credit to earlier actions. Learned critics provide value estimates for intermediate states, but these estimates can be inaccurate, while estimating intermediate values with repetitive contin…

- **[Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.35736v1)**
  - *Qiyue Xia, J. Michael Herrmann*
  - `2026-10-26`
  - Multi-objective multi-agent reinforcement learning (MOMARL) addresses agent coordination and objective trade-offs simultaneously while optimising overall system performance. Existing work tends to treat multi-agent cooperation and multi-objective optimisation as largely independe…

- **[When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement Learning through Video Editing](https://arxiv.org/abs/2610.35497v1)**
  - *Lei Zhao, Zongheng Cao, Xinyu Hu*
  - `2026-10-26`
  - Reinforcement learning (RL) has shown promise for training multimodal agents to reason and use tools. However, it remains unclear when fine-grained credit assignment improves learning and when it fails to improve task performance. Video editing provides a useful testbed for this…

- **[Multi-Horizon Future Discovery for Physics-Informed Exploration](https://arxiv.org/abs/2610.35468v1)**
  - *Shuwei Wang, Qiang Guan, Brian Qiu et al.*
  - `2026-10-26`
  - Exploration in physical control environments requires agents to identify actions whose consequences reveal previously unexplored aspects of the underlying dynamics. However, many intrinsic motivation methods rely on immediate prediction errors, state novelty, or local physical ch…

- **[Intent-Preserving Adversarial User Simulation for Multi-Turn Agent Evaluation](https://arxiv.org/abs/2610.35426v1)**
  - *Atri Vivek Sharma, Brian Formento, Alessio Lomuscio*
  - `2026-10-26`
  - Multi-turn agents are commonly evaluated with LLM-based simulated users, which can be overly cooperative and can therefore overestimate an agent's performance. We here introduce StressSim, an intent-preserving adversarial user simulator framework for stress-testing agents with ch…

- **[InterQ-RL: Interaction-Aware Correction of Execution Mismatch in Quantized Agentic RL](https://arxiv.org/abs/2610.35303v1)**
  - *Yingbo Hao, Song Liu, Guanghua Yu et al.*
  - `2026-10-26`
  - Multi-turn agent reinforcement learning (RL) relies on long closed-loop rollouts, making generation and KV-cache costs a major bottleneck. Quantized rollout reduces these costs, but its low-precision executor also serves as the behavior policy and can induce execution mismatch wi…

- **[BellowsKV: One Latent for Many Layers, Expanded on Demand](https://arxiv.org/abs/2610.35023v1)**
  - *Jiamu Zhang, Hanjie Chen*
  - `2026-10-26`
  - Large language models (LLMs) now serve as the backbone of agents that reason over many turns, call tools, and pursue long-horizon tasks. To avoid recomputation, a model stores the attention keys and values of all past tokens in a key-value (KV) cache. Each layer maintains its own…

- **[Adaptive Memory Index Evolution for Agents](https://arxiv.org/abs/2610.34977v1)**
  - *Yuntong Hu, Tongli Su, Yuanfu Sun et al.*
  - `2026-10-26`
  - Long-horizon agents continually accumulate experience, yet retaining a memory does not guarantee access when it is needed. Existing systems can adapt both memory content and access; we isolate persistent access updates as a separately controlled adaptation layer. We formulate thi…

- **[AT-AT: Automatic Tool Optimization from Agent Traces](https://arxiv.org/abs/2610.34679v1)**
  - *Maya Ravichandran, Pragya Tripathi, Dharamendra Kumar et al.*
  - `2026-10-26`
  - Efforts to improve LLM-based agents typically focus on modifying the agent itself, yet success also depends on the environment in which an agent acts. Tools mediate this interaction: a tool's description shapes how an agent calls it, and its implementation determines the results…

- **[Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control](https://arxiv.org/abs/2610.34650v1)**
  - *Jonathan DeCastro, Thomas Balch, Emily Sumner et al.*
  - `2026-10-26`
  - Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehend and fluently respond in real time. We present Dream2Assist, a model-based reinforcement learning f…

- **[Quantifying Claim Smoothing by LLM Research Agents](https://arxiv.org/abs/2610.35793v1)**
  - *Tiasa Singha Roy, Manya Wadhwa, Greg Durrett*
  - `2026-10-26`
  - Deep research, or any use of large language models (LLMs) to read a large document collection and produce insights, requires synthesizing information from different sources. In this work, we find that LLMs produce long-form research reports that read as confident syntheses but wh…

- **[OmniBrain-0: A Unified Agentic Model for Embodied Intelligence](https://arxiv.org/abs/2610.36013v1)**
  - *Xiaomi Embodied Intelligence Team, Yuechen Luo, Chong He et al.*
  - `2026-10-26`
  - General-purpose embodied intelligence requires robots to coordinate diverse skills over long horizons, track task progress, and recover from failures. Specialist policies alone do not ensure task-level reliability, while powerful multimodal agents rely on costly reasoning and ext…

- **[Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks](https://arxiv.org/abs/2610.35671v1)**
  - *Yao Huang, Zhiyuan Zeng, Yu Wang et al.*
  - `2026-10-26`
  - As frontier language models grow increasingly capable and autonomous, independent third-party evaluations are critical for characterizing their systemic safety risks. While closed-source releases are routinely accompanied by comprehensive system cards, open-weight models receive…

- **[Hierarchical Skill Evolution for Coding Agent](https://arxiv.org/abs/2610.35616v1)**
  - *Jun Gao, Yun Peng, Changhai Zhou et al.*
  - `2026-10-26`
  - Skills provide agents with reusable experience to guide future decisions without modifying the underlying model. However, coding trajectories are often entangled with task- and repository-specific contexts, making it challenging to distill procedural skills that generalize across…

- **[The Voice on the Line](https://arxiv.org/abs/2610.35272v1)**
  - *Husein Zolkepli*
  - `2026-10-26`
  - A transcriber listening through one microphone also hears everyone near it. We train causal voice isolators: masking transformers of 140M, 243M and 374M parameters, 20 ms of latency, enrolling the caller from the call itself. Short evaluation windows hide two failures that real c…

- **[From Questions to Queries to Insights: A Schema-Grounded Agentic Workflow for Natural-Language Crash Data Analysis](https://arxiv.org/abs/2610.35054v1)**
  - *Jingwen Zhu, Keshu Wu, Steven T. Parker et al.*
  - `2026-10-26`
  - Transportation agencies maintain extensive crash databases to identify safety priorities, evaluate countermeasures, and guide resource allocation. Making these data accessible to practitioners requires flexible ways to translate analytical questions into reliable results. Existin…

- **[FATE-5: Faithful Alignment of Trait Expression for Continuous Big Five Personality Control](https://arxiv.org/abs/2610.34889v2)**
  - *Gunhee Cho, Hongyeob Kim, Yun-Gyung Cheong*
  - `2026-10-26`
  - Controlling personality in large language models is important for building conversational agents that can be customized to different users and interaction settings. However, existing personality control methods often face a tradeoff between strong trait expression and natural dia…

- **[Semantic Atoms for Scalable Text Analysis in Data Analytics in the Era of LLM-Based Agents](https://arxiv.org/abs/2610.34860v1)**
  - *Jinxiang Xie, Zihao Li, Rui Ding et al.*
  - `2026-10-26`
  - Much of the information needed for data analysis is buried in text columns: an analyst may infer customer frustration from complaint text and use it to explain resolution time. We call workloads in which processing text columns is central to subsequent data analysis TADA (\emph{T…

- **[Position Matters More Than Channel: Talking a Language Model Out of a Correct Answer](https://arxiv.org/abs/2610.34809v1)**
  - *Xinyi Ni*
  - `2026-10-26`
  - Language models now answer questions alongside other claims: a note in the system prompt, a message from another agent, their own earlier answer. We ask what it takes to talk a model out of an answer it gets right on its own, and separate three factors that earlier studies vary t…

- **[BehaviorMem: Building and Evaluating User Memory from Real-World E-Commerce Behavior Streams](https://arxiv.org/abs/2610.34790v1)**
  - *Sizhe Wang, Xinghao Fang, Rui Qiu et al.*
  - `2026-10-26`
  - User memory helps personalized systems build on their understanding of users over time. In e-commerce, users convey their preferences and needs through both explicit language and implicit interactions with products. We study memory built from logs of these interactions, examining…

- **[From Belief Inference to Task Action: A Multi-Level Evaluation of Theory of Mind on Verifiable Tasks](https://arxiv.org/abs/2610.34759v1)**
  - *Zhenshuai Yin, Yongxin Guo, Mingda Zhang et al.*
  - `2026-10-26`
  - Effective collaboration requires language models to understand what others know and believe, and to act accordingly. Models that assume others share their information may omit necessary communication and undermine coordination. Many theory-of-mind (ToM) benchmarks assess mental-s…

- **[iPrefBench: A User-Centric Benchmark for Personalized Mobile Use Agents](https://arxiv.org/abs/2610.34735v1)**
  - *Yuting Ning, Ruijia Cheng, Sushobhan Ghosh et al.*
  - `2026-10-26`
  - An agent that truly knows and acts on behalf of its user has been a long-standing promise of AI assistants. Computer-use agents bring this promise within reach by capably executing fully specified tasks across apps. However, real-world user requests are often underspecified. To a…

- **[Heard Enough to Act: Early Tool Calling in Spoken Dialogue Systems](https://arxiv.org/abs/2610.34653v1)**
  - *Yizhou Peng, Chen Chen, Donghang Wu et al.*
  - `2026-10-26`
  - Latency-sensitive spoken agents must know not only which tool to call, but also when they have heard enough to act. Waiting for the turn to complete delays execution even when the request is already actionable. However, neither existing spoken agents nor spoken dialogue corpora d…

- **[Bayesian Replicator Dynamics and the Inversion of Strict Dominance in Bimatrix Games](https://arxiv.org/abs/2610.36345v1)**
  - *Jaime Ruiz-Serra, Nihat Ay, Michael Harré*
  - `2026-10-26`
  - Replicator dynamics, the central model of evolutionary game theory, describe populations evolving under selection and agents learning by trial and error. They also admit a third use: continuous-time Bayesian inference, in which an agent planning against an opponent accumulates ev…

- **[Compatibility and future-proof testing for multi-agent systems](https://arxiv.org/abs/2610.36289v1)**
  - *Yueshan Li, Lorenzo Fiaschi, Andrea Censi et al.*
  - `2026-10-26`
  - Independently developed autonomous agents, such as autonomous vehicles, must guarantee joint compatibility, such as safety and task-completion requirements, when they operate in a shared environment. Existing methods require a centrally designed specification, or interaction mech…

- **[The Inbox as a Coordination Primitive for LLM Agent Societies](https://arxiv.org/abs/2610.36264v1)**
  - *Karthik Sreedhar, Leo Yuan, Pradyumna Chari et al.*
  - `2026-10-26`
  - Language-model agents increasingly coordinate in large groups, and current agent protocols focus on delivering messages. For these agents, however, the scarce resource is not delivery but reading: every message costs tokens, and the context is finite. Current infrastructure works…

- **[EREBOTS 4.0: A framework for conversational assistants with A2A agents and MCP tools](https://arxiv.org/abs/2610.36221v1)**
  - *Elia Pacioni, Davide Calvaresi, Andrei C. Coman et al.*
  - `2026-10-26`
  - In recent years, multi-agent systems have shifted from rule-based, symbolic agents to sub-symbolic agents built on language models. However, several limitations remain unresolved. The new frontier is neuro-symbolic agents, which pair language models with deterministic tools and e…

- **[GEAR: Feature-Based Configuration and Code Generation for Agentic Systems](https://arxiv.org/abs/2610.35592v1)**
  - *Brell Sanwouo, Nada Zine, Paul Temple et al.*
  - `2026-10-26`
  - Engineering multi-agent systems (MAS) requires choosing agents, orchestration strategies, communication mechanisms, reasoning approaches, and memory configurations. These choices depend on framework-specific capabilities and abstractions, requiring developers to learn different A…

- **[Simulation-Efficient Double-Flow Neural Posterior Estimation for Agent-Based Models](https://arxiv.org/abs/2610.35442v1)**
  - *Junyao Zhang, Jinglai Li, Junqi Tang*
  - `2026-10-26`
  - Neural posterior estimation (NPE) enables Bayesian inference of the posterior parameter in agent-based models (ABMs) with intractable likelihoods, but simulating training data can be computationally expensive. We propose Double-Flow Neural Posterior Estimation (DF-NPE), which com…

- **[Knowing When to Escalate: Disagreement Patterns for Uncertainty-Aware Content Moderation](https://arxiv.org/abs/2610.35335v1)**
  - *Michał Wawer, Jarosław A. Chudziak*
  - `2026-10-26`
  - Agentic content-moderation systems increasingly rely on collective judgments from LLM agents, while aggregation methods commonly treat inter-agent disagreement as a reliability problem to be removed through consensus or voting. This framing is inappropriate for value-laden tasks,…

- **[Guarded Agent-in-the-Loop Residual Adaptation for Evolving Wind Power Regimes](https://arxiv.org/abs/2610.34968v1)**
  - *Yuhang Dong, Min Xia, Jinghong Li et al.*
  - `2026-10-26`
  - Wind power forecasting models are often deployed as fixed temporal backbones, but the errors they make can vary across meteorological regimes such as cold waves, heat-and-calm periods, productive typhoon, and destructive storms. We present a guarded Agent-in-the-loop residual ada…

- **[InferPriv: Evaluating Inferential Privacy Leakage in LLM Assistants](https://arxiv.org/abs/2610.34640v1)**
  - *Pengrun Huang, Yiwei Fu, Luoxi Meng et al.*
  - `2026-10-25`
  - Large language model (LLM)-based personal agents are increasingly deployed to handle everyday tasks on users' behalf. These agents have access to private user information, while their tasks involve communicating with third parties; this raises a critical privacy concern that agen…

- **[Intrinsic Goals for Autonomous Agents: Hierarchical Exploration Captures Future Volitional Action in Drosophila](https://arxiv.org/abs/2610.34638v1)**
  - *Declan Kutscher, Reece Keller, Alyn Kirsch et al.*
  - `2026-10-25`
  - Animals have a remarkable capacity for autonomy---driven by intrinsic motivation---without external sensory cues or extrinsic objectives, yet the computational mechanisms behind this ability largely remain a mystery. We combine whole-brain recordings in the fruit fly (Drosophila…

- **[AgentProofBench: Benchmarking Reusable Verifiers for Web Agents](https://arxiv.org/abs/2610.34634v1)**
  - *Jingjie Ning, Xueqi Li, Yi Lu et al.*
  - `2026-10-25`
  - Reusable Web-agent verification requires a rule to follow changing requirements and support subsequent execution. We introduce AgentProofBench, which connects paired tests of a frozen acceptance rule to execution from identical saved openings. The resource spans 97 tasks, 79 fami…

- **[Large Language Models: A Plain-Language Overview for Engineers](https://arxiv.org/abs/2610.34585v1)**
  - *Bahaeddin Türkoğlu*
  - `2026-10-25`
  - Large language models (LLMs) are neural networks trained on huge text collections to generate text by predicting what comes next. Engineers using ChatGPT and other generative artificial intelligence (AI) tools need a clear picture of what training changes and prompts add. The art…

- **[HobbyLM: A Sparse Mixture-of-Experts Model Family on a Hobby Budget](https://arxiv.org/abs/2610.34582v1)**
  - *Harish Santhanalakshmi Ganesan, Hariharan M. S., Prabhurajhan R*
  - `2026-10-25`
  - We describe HobbyLM, a family of small sparse Mixture-of-Experts (MoE) models trained from scratch with a few hundred to a few thousand dollars of rented GPU time. The core is a decoder-only transformer with fine-grained experts, sigmoid routing with auxiliary-loss-free load bala…

- **[Rethinking Verification in Agent Harnesses](https://arxiv.org/abs/2610.34577v1)**
  - *Zhengxin Zhang, Erkang Zhu, Yin Lin et al.*
  - `2026-10-25`
  - Agent harnesses enable large language models to act through tools, observe the results, and iteratively work toward a task goal. Verification checks and revises agents' work to improve output quality. Yet there is limited guidance on how harnesses should organize this effort. We…

- **[Agentic AI Orchestration Framework for Spatial Intelligence: Supply Chain Deployment](https://arxiv.org/abs/2610.34569v1)**
  - *Constantinos Papantoniou, Brian Hilton*
  - `2026-10-25`
  - Industrial spatial decisions are assembled across systems that share neither a reference frame nor an owner, and analysts spend substantial effort reconciling those systems rather than reasoning about space. This paper presents ANASSA, a reference architecture integrating structu…

- **[LLM WikiLeaks: Uncovering URL-Based Capability Extension and Security Circumvention in Agentic Message Boards](https://arxiv.org/abs/2610.34542v1)**
  - *Orel Navi, Elad Feldman, Ben Nassi*
  - `2026-10-25`
  - Autonomous agents have been observed acting beyond their assigned tasks, accessing unauthorized systems, and establishing communication channels to exchange information, yet the Web and network-level techniques they use to extend their capabilities and circumvent security restric…

- **[SentryBench: A Cost-Sensitive Benchmark for Adversarial Robustness of Tool-Using LLM Agents in Public-Safety Deployments](https://arxiv.org/abs/2610.34535v1)**
  - *Md Abu Yusuf, Oyshi Tabassum Aditi, Md Faysal Hosain Mazed*
  - `2026-10-25`
  - Large language model (LLM) agents are increasingly wired to consequential tools that send public alerts, dispatch responders, and query citizen records, where one erroneous tool call carries real-world cost. Existing agent-safety benchmarks measure generic harm or prompt-injectio…

- **[How Humans Learn Unfamiliar Worlds: A Think-Aloud Dataset on ARC-AGI-3](https://arxiv.org/abs/2610.34523v1)**
  - *Shuzhi Liu, Archana Warrier, Dat Nguyen et al.*
  - `2026-10-25`
  - Learning through exploration and using newly acquired knowledge to achieve goals are central capabilities of general intelligence. Understanding these capabilities requires tracing how learners build, use, and revise world models during interaction. We construct the first dataset…

- **[CaliMem: Search-Efficient Data Agent via Calibrated Memory](https://arxiv.org/abs/2610.34500v1)**
  - *Hanze Li, Athan Z. Li, Feiyang Kang et al.*
  - `2026-10-25`
  - Data curation is a first-order design choice in machine learning, yet tailoring training data to a downstream model and task remains costly in labor, expertise, and compute. Datasets are therefore often processed through fixed pipelines and reused across applications. We show tha…

- **[EMMA: Structured Episodic Memory for Multi-Agent Workflow Synthesis](https://arxiv.org/abs/2610.35966v1)**
  - *Ruijia Niu, Kaiwen Liu, Rose Yu et al.*
  - `2026-10-25`
  - Deploying LLM agents in specialized domains often require fine-grained task-specific procedures and knowledge a general model lacks, yet parameter training is costly and non-interpretable, and hand-engineered agent systems shift the cost to expert labor. Episodic memory updates a…

- **[EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems](https://arxiv.org/abs/2610.34450v1)**
  - *Yalun Wu, Qiwei Ma, Bingbing Xu et al.*
  - `2026-10-25`
  - Decentralized multi-agent systems (MAS) enable large language model agents to interact without centralized control. Agents need to adapt to other agents at test time and reuse accumulated experience to refine their interaction strategies for future interactions across cooperative…

- **[CyberDual: AI Attackers versus AI Code Reviewers in Real Software Maintenance](https://arxiv.org/abs/2610.34435v1)**
  - *Chenyuan Yang, Hwiwon Lee, Jongseong Kim et al.*
  - `2026-10-25`
  - Open-source projects now let AI agents review incoming code, but the code under review may itself come from an AI attacker. We present CyberDual, an arena for this dual role of AI: attacker agents hide an exploitable bug in real maintenance work on widely used open-source project…

- **[CTXAgent - Self-Controlled Context Management of LLM Agents](https://arxiv.org/abs/2610.34425v1)**
  - *Matthias Busch, Marius Tacke, Roland C. Aydin et al.*
  - `2026-10-25`
  - Agent harnesses keep long sessions inside the context window by compacting the history when a token threshold is crossed. We study an alternative in which the model manages its own context: it decides when to compact, what to keep and what to write as the hand-off, given two tool…

- **[MulFCoder: Framework-conditioned Multi-agent for MLLM-based Multi-framework Front-end Code Generation](https://arxiv.org/abs/2610.34418v1)**
  - *Jie Wu, Haoran Ma, Shisong Tang et al.*
  - `2026-10-25`
  - Generating runnable front-end code from UI screenshots is a long-standing goal in automated software engineering. Existing MLLM-based methods predominantly focused on HTML/CSS, leaving multi-framework generation for React/Vue/Angular underexplored. Naively modifying prompts leads…

- **[ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?](https://arxiv.org/abs/2610.34386v1)**
  - *Haojin Wang, Yangzhen Wu, Zeyi Chen et al.*
  - `2026-10-25`
  - Recursive self-improvement (RSI) requires an agentic system to design, train, and evaluate its own successor. Data-driven post-training is a central part of that loop, yet existing evaluations measure it on a single benchmark, where an agent selects from a static pool or distills…

- **[AndroidFlux: Evaluating and Reward Modeling Failure Recovery Capabilities in Mobile Use Multimodal Agents](https://arxiv.org/abs/2610.34384v1)**
  - *Gyubeum Lim, Yemo Koo, Ghunwoo Jang et al.*
  - `2026-10-25`
  - Mobile-use multimodal agents are typically evaluated by task success from a clean initial state, which does not isolate their ability to recover from intermediate errors. Because mobile environments change dynamically, a general mobile-use agent must complete tasks robustly even…

- **[SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents](https://arxiv.org/abs/2610.34365v2)**
  - *Cheng Gui, Xiang Zheng, Yutao Wu et al.*
  - `2026-10-25`
  - Science agents increasingly package domain expertise as reusable skills that plan analyses, select tools, and execute workflows. This modularity creates a confidentiality risk: the interactions that deliver a skill's capability can also reveal the skill itself. We build an extens…

- **[Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents](https://arxiv.org/abs/2610.34298v1)**
  - *Zhenning Shi, Liang Pang, Yongqi Li*
  - `2026-10-25`
  - Language agents increasingly act through external tools and interactive environments, making the interface between the model and its executable capabilities part of the decision process. Model Context Protocol (MCP) and command-line interfaces (CLI) can expose the same semantic o…

- **[Repairing Broken Access Control in Web Applications with LLMs: An Empirical Benchmark Study](https://arxiv.org/abs/2610.34290v1)**
  - *Mingrui Liu, Liang He, Xinchu Wang et al.*
  - `2026-10-25`
  - Broken access control (BAC) ranks among the most severe web-application vulnerability classes, yet its automated repair remains largely unexplored. Unlike memory-safety vulnerabilities, BAC is a logic vulnerability whose repair demands a deep understanding of an application's acc…

- **[A Hyper-Logical View on Multi-Agent Path Planning](https://arxiv.org/abs/2610.35964v1)**
  - *Hadar Frenkel, Dor Atzmon*
  - `2026-10-25`
  - Multi-Agent Path Planning (MAPP) requires collision-free paths for multiple agents. MAPP has numerous real-life applications, including the navigation of automated vehicles, and has therefore many variants considering different constraints, requirements, and objectives. For each…

- **[MultiEvoSkill: Structure-Aware Multi-Agent Skill Evolution for Generalizable Skill Artifacts](https://arxiv.org/abs/2610.34260v1)**
  - *Kounianhua Du, Jianxing Liu, Ruoshui Shan et al.*
  - `2026-10-25`
  - Skill documents are becoming the default adaptation surface for frozen large language model (LLM) agents, but current skill generators face two key limitations. First, humans and different LLMs differ in how they organize procedural knowledge and approach task solving. Skills aut…

- **[Recovering Business Rules as Cascade Lookups for Enterprise Field Prediction](https://arxiv.org/abs/2610.34258v1)**
  - *Changxu Duan*
  - `2026-10-25`
  - Enterprise sales-order systems rely on manually maintained configuration rules to determine fields such as payment terms, shipping points, and sales ownership. When these rules are incomplete or stale, operators must enter values by hand, and downstream errors spread into billing…

- **[NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253v1)**
  - *Chieh-Yuan Chang, Guan-Wei Chen, Chia-Yi Hsu et al.*
  - `2026-10-25`
  - AI coding agents routinely clone repositories, install packages, and read source code obtained from the Web, so publicly hosted code becomes part of the context that shapes the code they write. We show that this Web-borne context can be weaponized without any explicit instruction…

- **[$Δτ$-Bench: Pushing Agents Toward a Moving Capability](https://arxiv.org/abs/2610.34238v1)**
  - *Shuofei Qiao, Xuanguang Pan, Yijun Chen et al.*
  - `2026-10-25`
  - In this paper, we introduce $Δτ$-Bench, an executable agent benchmark that models the structural evolution of large tool ecosystems. In $Δτ$-Bench, independently evolving services continually reshape how tasks can be accomplished: familiar tools may disappear or be replaced, whil…

- **[MatOS: An Agent Operating System for Materials Research](https://arxiv.org/abs/2610.34203v1)**
  - *Dingyang Lyu, Jing Gao, Zhonghao Chang et al.*
  - `2026-10-25`
  - Materials research relies on scattered and growing data, knowledge, and simulation tools, and a single study often spans multi-day workflows across literature analysis, computation, and experiment. Large language model agents can now retrieve materials data, operate simulation co…

- **[R2A-Sales: A Policy-Atom-Matched Benchmark for Rule-to-Action Gaps in Goal-Directed Sales Agents](https://arxiv.org/abs/2610.34185v1)**
  - *Yihua Qin, Jiajie Jerry Zhao*
  - `2026-10-25`
  - LLM-based sales agents are often evaluated on static policy questions or task success, but deployment asks a sharper question: when a model can state a rule, will it choose compliant, tool-grounded actions under commercial pressure? We introduce R2A-Sales (Rule-to-Action), a poli…

- **[Can LLMs Trust Appropriately? Evaluating Calibrated Reliance on Imperfect Partners](https://arxiv.org/abs/2610.34107v1)**
  - *Mengdi Chu, Jintao Huang*
  - `2026-10-25`
  - Large language models increasingly collaborate with humans and peer AI agents whose contributions may be incomplete, inconsistent, or incorrect. Effective collaboration requires calibrated trust, whereby decisions to rely on, verify, or assist a partner adapt rationally as empiri…

- **[From Document Layout to Causal Topology: An End-to-End Architecture for Temporal Causal Reasoning](https://arxiv.org/abs/2610.34094v1)**
  - *Zhifeng Yang, Wei Luo, Yongjian Chen et al.*
  - `2026-10-25`
  - Large language models (LLMs) generally lack deep causal reasoning capabilities in temporal reasoning. Inspired by document layout reordering, this paper proposes a paradigm shift from discrete narratives to causal topologies. It constructs two architectures: a training-free neuro…

- **[AgentBaton: Efficient Model Collaboration in Agentic Tasks](https://arxiv.org/abs/2610.35959v1)**
  - *Junlong Li, Jindong Jiang, Yonggan Fu et al.*
  - `2026-10-25`
  - Solving long-horizon agentic tasks requires language agents to interact with their environments over multiple steps, and reliable performance often comes from the expensive capable models available through cloud providers. Meanwhile, alternative efficient models with inferior per…

- **[Holding a Steady Course: Knowledge Evolution from Expertise and Lessons for Continual Agent Learning](https://arxiv.org/abs/2610.34043v1)**
  - *Wenzhe Fan, Benjamin Steenhoek, Gaurav Mittal et al.*
  - `2026-10-25`
  - Autonomous agents are increasingly deployed across sequences of related tasks, yet they often fail to retain and improve their knowledge over time. Existing approaches convert interaction trajectories into memories or reusable skills, but experience is not automatically reliable…

- **[Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents](https://arxiv.org/abs/2610.33956v1)**
  - *Haoyu Zhao, Sitian Tu, Yuxuan Huang et al.*
  - `2026-10-25`
  - Continual learning is the ability of LLM agents to improve over time by acquiring, refining, and applying knowledge from experience while retaining useful prior knowledge. It is essential for agents learning over long time horizons, yet current evaluations largely assess individu…

- **[An Agentic AI Workflow for Liver Lesion Segmentation and Structured Radiology Reporting](https://arxiv.org/abs/2610.34599v1)**
  - *Fatma Ahmed Mansour, Rahatara Ferdousi, Manar Fathy Elshenawy*
  - `2026-10-25`
  - Despite advances in automated liver lesion segmentation, a gap remains between image-derived predictions and clinically interpretable radiology reports. Bridging this gap requires quantitative measurements that are both reproducible and traceable. We present an evidence-grounded…

- **[MOFjson: An Explicit Topological Representation of Metal-Organic Frameworks for Language Models](https://arxiv.org/abs/2610.34549v1)**
  - *Anabel Yong, Matthew Hart, Philippe Schwaller*
  - `2026-10-25`
  - Language models for metal-organic frameworks (MOFs) rely on formats that separate atomic geometry from structural topology, forcing models to choose between unstructured coordinate lists and non-spatial string identifiers[1]. We present MOFjson, the first representation separatin…

- **[IntNet: A Communication-Driven Multi-Agent Reinforcement Learning Framework for Cooperative Autonomous Driving](https://arxiv.org/abs/2610.34466v1)**
  - *Leandro Parada, Kevin Yu, Panagiotis Angeloudis*
  - `2026-10-25`
  - Achieving safety in autonomous driving through Multi-Agent Reinforcement Learning (MARL) is a critical yet challenging task due to non-stationarity, partial observability, and the need for effective coordination among agents. Although earlier cooperative MARL methods have aimed t…

- **[From GPU to TPU with Coding Agents: What Works, What Fails, and What It Costs?](https://arxiv.org/abs/2610.34422v1)**
  - *Hui Sun, Anderson Uchôa, Wesley K. G. Assunção*
  - `2026-10-25`
  - A coding agent can migrate a machine learning workload, report success, and still change how the model trains. Rising compute costs, limited accelerator capacity, and vendor dependence are pushing organizations toward alternatives to graphics processing units (GPUs); a key questi…

- **[From Human Intent to In-Orbit Action: A Self-Learning Large Language Model Agent for 6G Satellite Networks](https://arxiv.org/abs/2610.34387v1)**
  - *Zhengqian Xu, Yasheng Zhang, Chenhua Sun et al.*
  - `2026-10-25`
  - Autonomous control of sixth-generation (6G) low Earth orbit satellite networks is hindered by the gap between high-level human intent and low-level control logic: translating a request such as "uninterrupted Arctic video" into a valid reinforcement learning reward still takes day…

- **[Reinforcement Learning for Adaptive Crowd Flow Control Using Dynamic Barriers](https://arxiv.org/abs/2610.34163v1)**
  - *Alhanof Alolyan, He Wang, Amani Alonayzan*
  - `2026-10-25`
  - Crowd barriers are widely used to regulate pedestrian movement during large public events such as pilgrimages. However, fixed barrier layouts often create unnecessary stopping and local congestion even when they successfully control the overall crowd flow. Finding better barrier…

- **[BE-CTDE: Blockchain-Enabled Multi-Agent Reinforcement Learning with Anomaly Detection and Token Economics](https://arxiv.org/abs/2610.34121v1)**
  - *Chih-Wei Huang, Hsin-Chieh Lee, Yun-Chen Yu et al.*
  - `2026-10-25`
  - Multi-agent reinforcement learning supports cooperative decision-making in Internet of Things systems, but strategic deviations can disrupt coordination and undermine confidence in the training process. This paper proposes Blockchain-Enabled Centralized Training and Decentralized…

- **[FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation](https://arxiv.org/abs/2610.34564v1)**
  - *Meryem Koksal, Yunzhe Wang, Volkan Ustun*
  - `2026-10-25`
  - Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents. We introduce FlockWorld, an artificial-life environment built on Reynolds's Boids algorithm for studying population-scale mu…

- **[DynaFlow: Learning Free-Form Multi-Agent Orchestration](https://arxiv.org/abs/2610.34467v1)**
  - *Ruhao Liu, Qi Li, Shizun Wang et al.*
  - `2026-10-25`
  - Multi-agent systems often rely on predefined collaboration structures, limiting their ability to adapt to diverse task requirements. We introduce DynaFlow, a framework that integrates free-form executable workflow synthesis into the action space of the main agent. The agent decid…

- **[6G Reasoning Agent Societies: Composition, Scaling, and Consistency-Time Laws](https://arxiv.org/abs/2610.34357v1)**
  - *Hatim Chergui, Carolina Fernández-Martínez, Mustapha Benjillali et al.*
  - `2026-10-25`
  - Emerging 6G control planes would compose Large Language Model (LLM) agents that exchange interpreted conclusions, so hallucinations can propagate even over error-free transport. Recent architectures audit each message locally against the sender's observation mask, but isolated au…

- **[Beyond Belief: Evaluating and Mitigating LLM Susceptibility to Misinformation](https://arxiv.org/abs/2610.33962v1)**
  - *Emran Kanaan, Jiho Lee, Ibrahim Odat et al.*
  - `2026-10-25`
  - Tool-using large language models (LLMs) must decide whether external information warrants action. We investigate whether their expressed credibility judgments reliably indicate behavioral resistance to misinformation. We evaluate five LLMs on 196 constructed false notices paired…

- **[Self-Evolution Reasoner: Continuous Optimization via Policy-Intrinsic Exploration and Exploitation](https://arxiv.org/abs/2610.34137v1)**
  - *Wenhang Shi, Yiren Chen, Zhe Zhao et al.*
  - `2026-10-25`
  - Reinforcement learning with verifiable rewards (RLVR) enables large language models (LLMs) to continuously self-improve their reasoning capabilities. Compared to RLVR's scalar rewards, recent self-supervised on-policy distillation methods leverage denser supervision signals. Howe…

- **[Certifying Reward Alignment in Portfolio Reinforcement Learning](https://arxiv.org/abs/2610.34153v2)**
  - *Matin Tavakoli, Seyedreza Tavakoli, Faezeh Salmani et al.*
  - `2026-10-25`
  - Financial reinforcement learning often translates an investment objective into an additive risk-adjusted reward. An agent can optimise that reward accurately yet implement a different financial preference. We develop a decision audit for terminal mean-variance equilibrium that se…


## Harness  (121)

### NeurIPS

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **NeurIPS 2025** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…


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


### Other / arXiv

- **[Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces](https://arxiv.org/abs/2610.37255)**
  - *Jian Mu, Ruibo Shen, Yao Shu*
  - 🤗 Featured · `2026-10-27`
  - Language model agents are post-trained and deployed through a harness, the prompts, tools, and control logic that present a task to the model and execute its outputs. Harnesses are often revised and judged by how an already trained model performs under them, which assumes that wh…

- **[The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents](https://arxiv.org/abs/2610.36077)**
  - *Weidong Tang, Ruiheng Wang, Jingxuan Zhang et al.*
  - 🤗 Featured · `2026-10-26`
  - Multimodal intelligence can be viewed as human-guided co-evolution between worlds and agents through interaction. However, scaling this process faces two bottlenecks: constructing heterogeneous, verifiable environments is costly, and manual Harness iteration cannot keep pace with…

- **[Harness-Model Collaboration for Long-Horizon Continual Learning](https://arxiv.org/abs/2610.34724)**
  - *Zhen Bi, Zhizhi Peng, Yan Wang et al.*
  - 🤗 Featured · `2026-10-26`
  - Long-horizon agents continuously encounter reusable procedural knowledge, yet existing systems typically rely either on model adaptation or external memory, trading persistent learning for rapid reuse. This limitation is especially important for Web agents that repeatedly execute…

- **[h1: A Taste of the Bitter Lesson in Automated Theorem Proving](https://arxiv.org/abs/2610.35962)**
  - *Skander Moalla, Ahmad Rammal, Niket Patel et al.*
  - 🤗 Featured · `2026-10-25`
  - While progress in informal mathematics has come largely from scaling the chain-of-thought and agentic reasoning of frontier language models, formal theorem proving has increasingly relied on human-designed workflows around these models, such as planning, decomposition, and orches…

- **[Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements](https://arxiv.org/abs/2610.36584)**
  - *Binhang Qi, Yiming Liu, Yun Lin et al.*
  - 🤗 · `2026-10-27`
  - As large language model agents increasingly compile natural-language requirements into repository-level code, requirement-to-test generation grows in importance to provide validation constraints (or harness) to guide code generation. Yet it remains unclear whether current agents…

- **[Work Agents: Systems, Capabilities, and Optimization](https://arxiv.org/abs/2610.35845)**
  - *Zishan Xu, Enjun Du, Mingqi Gao et al.*
  - 🤗 · `2026-10-26`
  - As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish deleg…

- **[Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](https://arxiv.org/abs/2610.35832)**
  - *Yifei Yao, Yude Zou, Guanbo Jiao et al.*
  - 🤗 · `2026-10-26`
  - Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action model (WAM) policies across manipulation demands remains to be tho…

- **[When the Critic Falls Behind: Co-Evolving Rubrics and Harnesses for Continual Agent Self-Improvement](https://arxiv.org/abs/2610.36826v1)**
  - *Hao Chen, Yukun Yan, Ziyu Han et al.*
  - `2026-10-27`
  - Autonomous agents increasingly depend on harnesses that govern interaction, memory, tools, and execution around large language models (LLMs). While recent work has begun to evolve these harnesses from execution experience, the supervision used to guide evolution often remains rel…

- **[The View from Nowhere: Population-Centered Agent Evolution](https://arxiv.org/abs/2610.36660v1)**
  - *Shuo Yan, Ningning Hou, Haoyu He et al.*
  - `2026-10-27`
  - Self-improving AI systems can revise the designs that govern their own behavior. Yet existing approaches center improvement on selected parent agents and their evolutionary experience, leaving the broader population largely underused. We identify a substantial gap between populat…

- **[Your Agent Acts Differently When You're Around: How User Presence Changes Agent Behavior in Negotiation](https://arxiv.org/abs/2610.36435v1)**
  - *Jane Pan, You Lyu, Abe Bohan Hou et al.*
  - `2026-10-27`
  - LLM agents increasingly interact with other agents on behalf of users, yet how users in the loop affect their agents' behavior--for better or worse--remains poorly understood. We study this question through the lens of negotiation, where agents must represent users while strategi…

- **[Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](https://arxiv.org/abs/2610.37648v1)**
  - *Andrew Szot, Samira Abnar, Omar Attia et al.*
  - `2026-10-27`
  - We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthA…

- **[CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning](https://arxiv.org/abs/2610.36469v1)**
  - *Jianwen Chen, Peng Xia, Kaide Zeng et al.*
  - `2026-10-27`
  - Large language model (LLM) agents interact with their environments through executable harnesses that govern tool use and feedback. Optimizing a harness for a fixed policy overlooks how its behavior changes during learning, while training a policy under a fixed harness leaves the…

- **[GEPA-Curator: Curated Learning for Self Improving Agents](https://arxiv.org/abs/2610.37651v1)**
  - *Zack Yu, Nicholas Lee, Minjae Lee et al.*
  - `2026-10-27`
  - Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesse…

- **[A Harness Reducing over-Defensive Writing in Agents by Isolating Objections](https://arxiv.org/abs/2610.36717v1)**
  - *Xiaochen Chang*
  - `2026-10-27`
  - When expanding a report, writing with agents may introduce a stronger claim than the article makes and then disclaim it. This is called over-defensive writing. We assume that this is because the agent is writing for responding to an adversarial AI reviewer, instead of a human rea…

- **[FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation](https://arxiv.org/abs/2610.36545v1)**
  - *Yijing Lin, Zhendong Mao, Mengqi Huang et al.*
  - `2026-10-27`
  - Unified conditional image generation requires a single model to preserve different aspects of a visual input while producing a target image that follows textual guidance. Pretrained video models provide a promising foundation by encoding visual transformations across time, yet ex…

- **[Evaluating AlphaEarth Embeddings for Crop Classification: Separability, Temporal Dynamics, and Cross-Regional Transferability](https://arxiv.org/abs/2610.36857v1)**
  - *Priyanka Goyal, Maitreyee Sar, Adway Mitra et al.*
  - `2026-10-27`
  - Earth Observation (EO)-based agricultural monitoring is shifting from pixel-level spectral analysis toward representation-driven modeling, yet systematic evaluation of learned representations across spatial, temporal, and domain-generalization dimensions remains limited. Geospati…

- **[The State and Fate of Multilingual, Contextual Evaluation in the NLP World](https://arxiv.org/abs/2610.36990v1)**
  - *Manan Uppadhyay, Himanshu Beniwal, Prashant Kodali et al.*
  - `2026-10-27`
  - Multilingual evaluation benchmarks are the primary instrument for assessing whether large language models generalize beyond English, yet the adequacy of these benchmarks has received little systematic scrutiny. We present a data-driven audit of 51 recent multilingual benchmarks s…

- **[SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2610.36991v1)**
  - *Zafer Sahinoglu, Abdulazeez Mohammed, Buse Yaren Kazangirler et al.*
  - `2026-10-27`
  - Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation on the retrieved context. Although dense retrieval is effective for local semantic matching, independently ranked retrieval can return redu…

- **[kw-bench: Breaking Frontier Harnesses on Real-World Tasks](https://arxiv.org/abs/2610.36405v1)**
  - *George Juraj Salapa*
  - `2026-10-26`
  - Each new generation of frontier model pushes the edge of what is possible. Inside a harness -- a loop, a shell, a filesystem, the ability to write and run its own code -- a model can take on increasingly difficult work.   A growing body of work treats the coding-agent harness as…

- **[HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning](https://arxiv.org/abs/2610.36374v1)**
  - *Fanqi Yu, Matteo Tiezzi, Cigdem Beyan et al.*
  - `2026-10-26`
  - Robotic agents operating in real-world environments must adapt continuously from a stream of multimodal demonstrations, often under constraints that preclude storing or revisiting past data. In this replay-free, single-pass lifelong imitation learning setting, sequential updates…

- **[Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses](https://arxiv.org/abs/2610.36114v1)**
  - *Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan*
  - `2026-10-26`
  - LLM agents are judged by two numbers: the size of the context window, and how often the final answer is correct. Both numbers miss a third thing: how much of a tool's output is lost before the model ever sees it. We measured this loss in a real tool-using agent. The agent finds t…

- **[I-HITL: Inalienable Human-in-the-Loop](https://arxiv.org/abs/2610.35835v2)**
  - *Samuel Breckenridge, Dani Vilardell, Wenhao Wang et al.*
  - `2026-10-26`
  - Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.   We introduce the co…

- **[Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](https://arxiv.org/abs/2610.35817v2)**
  - *Benjamin Pikus, Daniel Saunders, Mircea Mironenco et al.*
  - `2026-10-26`
  - A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task. To achieve these two skills, we introduce Zero-real Agent Policy (ZAP), a recipe that teaches a small off-the-shelf vision-language model to control a robot…

- **[A Unified Arena for LLM Agents across Diverse Eurogame](https://arxiv.org/abs/2610.35773v1)**
  - *Fengrui Zhang, Xiang Li, Ruomeng Ding et al.*
  - `2026-10-26`
  - Interactive environments offer a practical way to evaluate large language model (LLM) agents, and competitive games extend this evaluation to decisions shaped by competing goals and other agents' choices. Yet existing evaluations confined to individual games or execution framewor…

- **[Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents](https://arxiv.org/abs/2610.35767v1)**
  - *Tingzhu Bi, Xun Zhang, Jinglin Li et al.*
  - `2026-10-26`
  - Root cause analysis (RCA) of microservice failures has attracted many LLM agents whose investigation is hand-crafted, through standard operating procedures, fixed stages and role agents. Each is evaluated on its own data against few baselines, so it is unknown whether this design…

- **[Infinity Machine: a self-improving AI agent for research](https://arxiv.org/abs/2610.35579v1)**
  - *Harish Santhanalakshmi Ganesan*
  - `2026-10-26`
  - We present the Infinity Machine, a self-improving AI agent that we use for research on problems whose answers aprogram or data can check. Each candidate solution is produced by a full tool-using agent that works for up to an hour in a fresh sandbox; proposers see only a public sc…

- **[ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation](https://arxiv.org/abs/2610.35486v1)**
  - *Param Biyani, Sebastien Luyasu, Cedric Potvliege et al.*
  - `2026-10-26`
  - Theory and experiments suggest that capable AI agents may resist shutdown. Existing shutdown evaluations are informative but limited in coverage and vulnerable to evaluation awareness. We introduce ShutdownMod, a method that turns any agent trajectory into a shutdown evaluation b…

- **[MarkovSim: an LLM Agent Harness with Bounded Context for Long-Horizon Computational Simulation](https://arxiv.org/abs/2610.35349v1)**
  - *Yeui-Lung Lei, Wen-Bo Chen, Pan Zhang*
  - `2026-10-26`
  - Recent studies have applied large language model (LLM) agent systems to computational simulation workflows. Such workflows are long-horizon, so the information generated can exceed what an LLM can reason over at once, its context window. Context management is therefore essential,…

- **[RepoTrace: Improving Requirement Tracing in Multi-Round Agent Interactions](https://arxiv.org/abs/2610.35333v1)**
  - *Huanyu Liu, Yezheng Cheng, Jinliang You et al.*
  - `2026-10-26`
  - Code agents have become increasingly capable of performing software engineering tasks through interaction with software environments. However, agents tend to degrade as the number of interaction rounds increases, making it difficult to maintain existing software during iterative…

- **[RSIV-Harness: A Recursive Self-Improvement Harness Framework for Open-Domain Conversational Text-to-Visualization](https://arxiv.org/abs/2610.35316v1)**
  - *Jiawei Lu, Chen Zhang, Jinwei Lu et al.*
  - `2026-10-26`
  - Users often request charts without knowing which database or table holds the relevant data. Such requests may be ambiguous, and users may ask follow-up questions to deepen their analysis or iteratively refine existing charts. A useful assistant must therefore discover relevant da…

- **[V$^3$AST-Bench: Verifiable, Valid, and Versatile Safety Evaluation for Coding Agents](https://arxiv.org/abs/2610.35188v1)**
  - *Weitao Feng, Hengheng Xiong, Zihao Zeng et al.*
  - `2026-10-26`
  - Large language models increasingly act through code, modifying repositories, executing programs, and interacting with services in agent form. Their actions introduce risks that cannot be assessed from generated responses alone. Safety evaluation must verify actual consequences, d…

- **[UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity](https://arxiv.org/abs/2610.35980v1)**
  - *Yijun Zhou, Minghao Shao, Ke Zhang et al.*
  - `2026-10-26`
  - Game development stresses coding agents in ways general software engineering does not: correctness depends on how engine APIs, serialized scene state, and runtime behavior interact, not on source code alone. Existing benchmarks mainly target platforms such as Godot and heavily re…

- **[LongSearchEval: Evaluating Long-Horizon Web Search Capabilities of Large Language Models via a Trajectory-Aware Agent Framework with Failure-Node Localization](https://arxiv.org/abs/2610.35150v1)**
  - *Jialiang Liu, Shusheng Li, Wenjun Tan*
  - `2026-10-26`
  - Long-horizon web search requires LLM-based agents to integrate information across web pages through extended interactions under task-specific constraints. Evaluating this capability is important not only for measuring final answer quality, but also for assessing whether an agent…

- **[Locked In: Multi-Objective RL for the AI Data Center Build-Out](https://arxiv.org/abs/2610.35147v1)**
  - *Satyapragnya Kar, Rajarshi Das, PR Panigrahi*
  - `2026-10-26`
  - AI data center build-out is a multi-trillion-dollar, multi-decade infrastructure program. Yet siting, power procurement, and cooling decisions are still made with static, single-point scoring tools. These tools are evaluated once, on day-zero numbers. This is a poor fit. A site's…

- **[Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models](https://arxiv.org/abs/2610.35138v1)**
  - *Xilin Wei, Shengyuan Ding, Xinyu Fang et al.*
  - `2026-10-26`
  - Evaluating human-AI co-design requires testing whether coding agents can translate real users' multimodal requests into working application revisions. We introduce Co-Design Bench, a reference-free benchmark of 273 tasks curated from 37,463 deduplicated queries across 26,314 real…

- **[CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems](https://arxiv.org/abs/2610.35082v1)**
  - *Yujia Zheng, Tianhao Li, Shangzhi Xu et al.*
  - `2026-10-26`
  - Agent Skills allow LLM agents to combine reusable capabilities, but checking each Skill in isolation cannot rule out policy violations when they are composed. We term such failures Conflict of Skills (CoS): artifacts or assessment signals produced for one purpose may be reused do…

- **[PatentAgentBench: Benchmarking LLM Agents with Professional Patent Task Suites](https://arxiv.org/abs/2610.35031v1)**
  - *Yijie Hu, Wei Li, Junjie Zhou et al.*
  - `2026-10-26`
  - Patent practice lies at the intersection of technical, legal, and linguistic work, making it challenging yet crucial to technological innovation. Recently, rapid advances in large language models (LLMs) and agentic systems have demonstrated the potential to complete realistic bus…

- **[The Target Agent Is Its Own Best Critic but a Poor Proposer: Self-Improved Red Teaming](https://arxiv.org/abs/2610.34965v1)**
  - *Mintong Kang, Stephen Rawls, Melissa Kazemi Rad et al.*
  - `2026-10-26`
  - Automatic red teaming increasingly relies on large language models (LLMs) to iteratively diagnose failed attacks and propose improved adversarial prompts or injections. Although prior work strengthens this loop through prompt engineering and search-harness design, the mechanisms…

- **[How Do Coding-Agent Harnesses Self-Evolve? An Empirical Study of Retrospective Adaptation](https://arxiv.org/abs/2610.34938v1)**
  - *Christoph Treude, Sebastian Baltes*
  - `2026-10-26`
  - Coding agents can adapt their harnesses, the software, configuration, and instructions used to run them, based on experience from earlier tasks, but whether these adaptations improve their behavior on later tasks remains unclear. We study \retro, a skill that asks an agent to rev…

- **[Adaptive Memory Index Evolution for Agents](https://arxiv.org/abs/2610.34977v1)**
  - *Yuntong Hu, Tongli Su, Yuanfu Sun et al.*
  - `2026-10-26`
  - Long-horizon agents continually accumulate experience, yet retaining a memory does not guarantee access when it is needed. Existing systems can adapt both memory content and access; we isolate persistent access updates as a separately controlled adaptation layer. We formulate thi…

- **[AT-AT: Automatic Tool Optimization from Agent Traces](https://arxiv.org/abs/2610.34679v1)**
  - *Maya Ravichandran, Pragya Tripathi, Dharamendra Kumar et al.*
  - `2026-10-26`
  - Efforts to improve LLM-based agents typically focus on modifying the agent itself, yet success also depends on the environment in which an agent acts. Tools mediate this interaction: a tool's description shapes how an agent calls it, and its implementation determines the results…

- **[Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks](https://arxiv.org/abs/2610.35671v1)**
  - *Yao Huang, Zhiyuan Zeng, Yu Wang et al.*
  - `2026-10-26`
  - As frontier language models grow increasingly capable and autonomous, independent third-party evaluations are critical for characterizing their systemic safety risks. While closed-source releases are routinely accompanied by comprehensive system cards, open-weight models receive…

- **[Hierarchical Skill Evolution for Coding Agent](https://arxiv.org/abs/2610.35616v1)**
  - *Jun Gao, Yun Peng, Changhai Zhou et al.*
  - `2026-10-26`
  - Skills provide agents with reusable experience to guide future decisions without modifying the underlying model. However, coding trajectories are often entangled with task- and repository-specific contexts, making it challenging to distill procedural skills that generalize across…

- **[BehaviorMem: Building and Evaluating User Memory from Real-World E-Commerce Behavior Streams](https://arxiv.org/abs/2610.34790v1)**
  - *Sizhe Wang, Xinghao Fang, Rui Qiu et al.*
  - `2026-10-26`
  - User memory helps personalized systems build on their understanding of users over time. In e-commerce, users convey their preferences and needs through both explicit language and implicit interactions with products. We study memory built from logs of these interactions, examining…

- **[MedJev: Evaluating Zero-Shot System-One Decision Making in Medicine](https://arxiv.org/abs/2610.36006v1)**
  - *Simon A. Lee, Jiahang Sha, Moonseong Jeong et al.*
  - `2026-10-26`
  - System One decision models such as Jev answer structured questions in a single forward pass without generating text, offering fast and computationally efficient clinical decision support. We evaluate MedJev, an open System One model that runs locally on a laptop, across ten medic…

- **[Prefetch-Steered Routing: Deterministic Cache-Aware Expert Selection for Offloaded Mixture-of-Experts Decoding](https://arxiv.org/abs/2610.34721v1)**
  - *Siming Huang*
  - `2026-10-26`
  - When a Mixture-of-Experts (MoE) model does not fit in GPU memory, batch-1 decoding is dominated by copying expert weights from host memory. Cache-aware routing reduces these copies by biasing the router toward resident experts, but combined with asynchronous prefetching it makes…

- **[Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling](https://arxiv.org/abs/2610.35866v2)**
  - *Xi Chen, Chongjian Ge, Yiran Xu et al.*
  - `2026-10-26`
  - As autonomous research systems become more capable, benchmarks must both evaluate their performance and support meaningful research progress. We introduce Auto-Research Arena, a multi-target benchmark for evaluating autonomous research systems and discovering ideas in language mo…

- **[When Respondents Are Scarce: LLM-Derived Semantic Priors for Bayesian Confirmatory Factor Analysis](https://arxiv.org/abs/2610.34843v1)**
  - *Shaohuai Feng, Mohd Wira Mohd Shafiei, Mohd Sukri Shafie et al.*
  - `2026-10-26`
  - Across social and behavioral research, measuring latent constructs can be challenging when target populations are small or difficult to reach. Recruiting additional respondents may be costly or infeasible, leaving researchers with limited data for estimating questionnaire factor…

- **[The Watchtower Imperative: Lifespan-Calibrated Evaluation for Frontier AI](https://arxiv.org/abs/2610.35725v1)**
  - *Casey M. Williams, Jennifer Victoria Scurrell*
  - `2026-10-26`
  - The gap between AI capability deployment and safety assurance is structural and cannot be closed through internal evaluations alone. Analyzing documented harms (2017-2026) across the human lifespan reveals that disparate incidents --- from voice assistants endangering children to…

- **[Beyond Words Alone: Disentangling Distributed Evidence for Visually Grounded Cultural Translation](https://arxiv.org/abs/2610.35482v1)**
  - *Dingming Li, Yiwen Qiu, Linjuan Wu et al.*
  - `2026-10-26`
  - Social media enables cross-lingual communication, yet the meaning of user-generated content (UGC) is often distributed across text, images, and cultural knowledge, making translation challenging. Existing evaluations typically treat images as optional and assume textual informati…

- **[Precedence-Aware Resource Allocation: Extending the AUTOC Framework to Multi-Level Treatments](https://arxiv.org/abs/2610.34812v1)**
  - *Olin E. Gilster, Shengpu Tang*
  - `2026-10-26`
  - Many real-world decision problems require allocating limited resources across individuals to maximize total benefit often through interventions that vary in intensity rather than binary treat-or-not decisions. In these settings, higher levels treatments require first applying low…

- **[Beyond Update Counts: A Control Map for Evaluating Test-Time Model Updates](https://arxiv.org/abs/2610.36109v1)**
  - *Zehao Zhao, Shangjian Yin, Rui Liu et al.*
  - `2026-10-26`
  - Test-time updating lets a language model change persistent state after training---such as model weights, adapter parameters, or a memory module---before or while answering queries. Existing evaluations often compare systems using update count or frequency and performance measured…

- **[Diagnosing and Mitigating Long-Session Degradation in Full-Duplex Speech Models](https://arxiv.org/abs/2610.34991v2)**
  - *Junho Kim, CheHyun Lee, Donghun Kang et al.*
  - `2026-10-26`
  - End-to-end full-duplex spoken dialogue models enable natural, real-time spoken interactions with interruptions, backchannels, and overlapping speech. Prior evaluations have assessed diverse interaction capabilities and identified some degradation patterns across conversational tu…

- **[Large Language Models: A Plain-Language Overview for Engineers](https://arxiv.org/abs/2610.34585v1)**
  - *Bahaeddin Türkoğlu*
  - `2026-10-25`
  - Large language models (LLMs) are neural networks trained on huge text collections to generate text by predicting what comes next. Engineers using ChatGPT and other generative artificial intelligence (AI) tools need a clear picture of what training changes and prompts add. The art…

- **[Rethinking Verification in Agent Harnesses](https://arxiv.org/abs/2610.34577v1)**
  - *Zhengxin Zhang, Erkang Zhu, Yin Lin et al.*
  - `2026-10-25`
  - Agent harnesses enable large language models to act through tools, observe the results, and iteratively work toward a task goal. Verification checks and revises agents' work to improve output quality. Yet there is limited guidance on how harnesses should organize this effort. We…

- **[How Humans Learn Unfamiliar Worlds: A Think-Aloud Dataset on ARC-AGI-3](https://arxiv.org/abs/2610.34523v1)**
  - *Shuzhi Liu, Archana Warrier, Dat Nguyen et al.*
  - `2026-10-25`
  - Learning through exploration and using newly acquired knowledge to achieve goals are central capabilities of general intelligence. Understanding these capabilities requires tracing how learners build, use, and revise world models during interaction. We construct the first dataset…

- **[CTXAgent - Self-Controlled Context Management of LLM Agents](https://arxiv.org/abs/2610.34425v1)**
  - *Matthias Busch, Marius Tacke, Roland C. Aydin et al.*
  - `2026-10-25`
  - Agent harnesses keep long sessions inside the context window by compacting the history when a token threshold is crossed. We study an alternative in which the model manages its own context: it decides when to compact, what to keep and what to write as the hand-off, given two tool…

- **[ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?](https://arxiv.org/abs/2610.34386v1)**
  - *Haojin Wang, Yangzhen Wu, Zeyi Chen et al.*
  - `2026-10-25`
  - Recursive self-improvement (RSI) requires an agentic system to design, train, and evaluate its own successor. Data-driven post-training is a central part of that loop, yet existing evaluations measure it on a single benchmark, where an agent selects from a static pool or distills…

- **[$Δτ$-Bench: Pushing Agents Toward a Moving Capability](https://arxiv.org/abs/2610.34238v1)**
  - *Shuofei Qiao, Xuanguang Pan, Yijun Chen et al.*
  - `2026-10-25`
  - In this paper, we introduce $Δτ$-Bench, an executable agent benchmark that models the structural evolution of large tool ecosystems. In $Δτ$-Bench, independently evolving services continually reshape how tasks can be accomplished: familiar tools may disappear or be replaced, whil…

- **[Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents](https://arxiv.org/abs/2610.33956v1)**
  - *Haoyu Zhao, Sitian Tu, Yuxuan Huang et al.*
  - `2026-10-25`
  - Continual learning is the ability of LLM agents to improve over time by acquiring, refining, and applying knowledge from experience while retaining useful prior knowledge. It is essential for agents learning over long time horizons, yet current evaluations largely assess individu…

- **[In-Context Adapter Generation for Compositional Generalization in Large Audio Language Models](https://arxiv.org/abs/2610.34413v1)**
  - *Yiwei Guo, Siqi Huang, Bohan Li et al.*
  - `2026-10-25`
  - Large audio language models (LALMs) have achieved strong performance on standard speech and audio understanding tasks, yet their ability to systematically generalize to novel task compositions remains underexplored. Taking a meta-learning view, we extend Text-to-LoRA (T2L) to LAL…


## Finance  (169)

### ICML

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


### KDD

- **[CryptoMixer: Fine-grained market information-aware MLP Networks for Individual Cryptocurrency Trading Prediction](https://www.semanticscholar.org/paper/7700a7579ca8f11b5b31323e6e1fac103dabc2e7)**
  - *Ting-Sheng Feng, Zhi-Hao Shen, Xi Zhao et al.*
  - **KDD 2025** · `2025-08-03`
  - Accurately predicting user trading behavior in decentralized exchanges is essential for investors to mitigate risks and optimize their trading strategies. While existing research primarily focuses on predicting trading behavior in stock markets, these methods often struggle to ad…


### ACL

- **[The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory](https://arxiv.org/abs/2610.34767v1)**
  - *Yuexi Pan, Yongchao Chen*
  - **ACL** · `2026-10-26`
  - Most agent-memory benchmarks frame long-term memory as retrieval: can an agent recover the relevant record from a long and evolving history? Scientific agents face a stricter problem: a correctly remembered fact may still be invalid to use. The same reported test result can suppo…

- **[How Do Small Coding Agents Use Code Graphs and Embeddings?](https://arxiv.org/abs/2610.33958v1)**
  - *Saurav Bellam*
  - **ACL** · `2026-10-25`
  - Coding agents are given embedding search and code-graph tools on the premise that a repository's structure is something the model lacks and the tool supplies. We test that premise on SWE-bench Verified with small open-weight models, stratifying tasks by a deterministic hop depth…


### IJCAI

- **[Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition](https://arxiv.org/abs/2610.34777v1)**
  - *Weihang Niu, Mengxing Ren, Che Qu*
  - **IJCAI** · `2026-10-26`
  - This paper introduces Scope-Gap Injection (SGI), an indirect prompt injection method for multi-stage LLM-agent safety pipelines. In the IJCAI 2026 OpenClaw Agent Security Attack Competition, each attack package is judged by a static skill scan (S1), an LLM-judge safety check over…


### Other / arXiv

- **[Harness-Model Collaboration for Long-Horizon Continual Learning](https://arxiv.org/abs/2610.34724)**
  - *Zhen Bi, Zhizhi Peng, Yan Wang et al.*
  - 🤗 Featured · `2026-10-26`
  - Long-horizon agents continuously encounter reusable procedural knowledge, yet existing systems typically rely either on model adaptation or external memory, trading persistent learning for rapid reuse. This limitation is especially important for Web agents that repeatedly execute…

- **[How Much Does the Hint Matter? Scope Conditions for Hindsight Self-Distillation in Financial Reasoning](https://arxiv.org/abs/2610.36082)**
  - *Johnny Yu, Cyril Gorlla*
  - 🤗 Featured · `2026-10-26`
  - Financial institutions operating under data-residency constraints are restricted to open-weight models small enough to locally host, which trail frontier systems on multi-step quantitative reasoning. On-policy distillation narrows such gaps by supervising a student on its own rol…

- **[What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents](https://arxiv.org/abs/2610.34491)**
  - *Kaiser Sun, Yongchan Kwon, Zain Hasan et al.*
  - 🤗 Featured · `2026-10-25`
  - Generative models increasingly expose a reasoning effort setting that lets users scale inference-time compute, trading higher cost for potentially improved performance. Users must choose an effort level before knowing whether extra reasoning will help, and even a successful run d…

- **[TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](https://arxiv.org/abs/2610.37571)**
  - *Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz et al.*
  - 🤗 · `2026-10-27`
  - Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-…

- **[M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents](https://arxiv.org/abs/2610.37459)**
  - *Hannes Ill, Rafi Al Attrach, Rajna Fani et al.*
  - 🤗 · `2026-10-27`
  - Clinical research over electronic health records depends on derived variables whose definitions sit outside the schema, in item codes, time windows, missingness rules, and output-grain choices that change cohorts and downstream conclusions. We introduce M4Bench, 28 clinical deriv…

- **[Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents](https://arxiv.org/abs/2610.37567v1)**
  - *Pranjal Aggarwal, Sean Welleck*
  - `2026-10-27`
  - AI agents have made substantial progress in domains where they have a non-trivial amount of time to deliberate between actions, such as mathematics, software engineering, and performing tasks on desktop applications. It is less clear how such models fare in settings that demand r…

- **[From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents](https://arxiv.org/abs/2610.37482v1)**
  - *Ziyang Chen, Qian Li, Chengwei Qin*
  - `2026-10-27`
  - GUI memory should preserve the results of past actions and learn reusable operations. This is difficult in long-horizon workflows, where agents must use information across applications and useful operations are interleaved with failed attempts. We introduce Task Advancement Memor…

- **[Concordat: Typed Sessions for LLM Agents](https://arxiv.org/abs/2610.37461v1)**
  - *Milad Sikaroudi*
  - `2026-10-27`
  - Agents built on large language models are increasingly allowed to take consequential actions: cancelling bookings, issuing refunds, changing accounts. The rules that govern those actions, such as "obtain the customer's explicit confirmation before changing anything", are usually…

- **[Test-Time Communication in Trading Agent Swarms](https://arxiv.org/abs/2610.37448v1)**
  - *Avid Fayaz, Harry Zhang, Håvard Alstadheim et al.*
  - `2026-10-27`
  - Communication between agents has mostly been studied on tasks with a shared objective and fast, clear feedback. Trading has neither: each agent manages its own account, with decisions being scored by markets late and noisily. A trading swarm is thus a population of independent de…

- **[WCC: A Learning-Based Framework for Deciding When to Apply Cooperative Coevolution in Large-Scale Optimization](https://arxiv.org/abs/2610.37329v1)**
  - *Wenjie Qiu, Hepei Li, Jianfeng Wang et al.*
  - `2026-10-27`
  - Cooperative Coevolution (CC) and Non-Decomposition Algorithms (NDAs) are two primary approaches for large-scale global optimization (LSGO). Although both have achieved success, they exhibit markedly different performance across problem types and each faces approach-specific limit…

- **[Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation](https://arxiv.org/abs/2610.37242v1)**
  - *Saiful Khan, Afrah Farea*
  - `2026-10-27`
  - Large language model (LLM) agents that call enterprise APIs must select the correct endpoints, follow process order, use valid payload keys, and choose coded values from predefined lists. However, current retrieval-augmented service discovery treats endpoints independently and th…

- **[LiveSearch: Questions as Executable Verifier Code for a Live Benchmark of Professional-Source Financial Search Agents](https://arxiv.org/abs/2610.37166v1)**
  - *Sinuo Wang, Wentao Zhao, Jiacheng Lu et al.*
  - `2026-10-27`
  - In finance, the answer that matters is usually the current one: prices, rates, and disclosures hold only as of a given day, so retrieving up-to-date facts is a core capability of a financial agent. Yet most financial benchmarks overlook timeliness. They fix each answer at annotat…

- **[Noise Steering: Exploiting Wake Steering and Acoustic Directivity for Noise-Constrained Wind Farm Control via Reinforcement Learning](https://arxiv.org/abs/2610.36888v1)**
  - *Martín de Frutos, Baptiste Corban, Claire Bizon Monroc et al.*
  - `2026-10-27`
  - Existing noise mitigation strategies for wind farms usually consist in reducing turbines power output, without accounting for the wake interactions between them and the noise emission directivity. This leads to over-conservative policies and unexploited wind power. Yet, turbine y…

- **[RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents](https://arxiv.org/abs/2610.36878v1)**
  - *Delin Wang, Sinuo Wang, Rui Sun et al.*
  - `2026-10-27`
  - Deep research agents conduct multi-step Web searches and synthesise retrieved information into analytical reports. Evaluating these outputs requires checking which analyses they deliver, beyond the presence of relevant facts. Query-specific binary rubrics make individual requirem…

- **[NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization](https://arxiv.org/abs/2610.36553v1)**
  - *Shuo Chen, Li Cui, Cunxin Huang et al.*
  - `2026-10-27`
  - Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in simulation-based and experimental applications, where evaluating the black-box objective can itself be costly. Thus, it remains a central chal…

- **[FIDES-Live: Evaluating Behavioral Concordance in Sequential Trading Agents](https://arxiv.org/abs/2610.36476v1)**
  - *Arther Tian, Alex Ding, Simon Wu et al.*
  - `2026-10-27`
  - Sequential trading agents produce decisions, orders, execution receipts, account states, and reports that need not agree, even when the final portfolio value is correctly computed. We present FIDES-Live, an operational extension of FIDES from generated strategy concordance to the…

- **[Impossibility of No-Regret in Multi-Agent Bidding](https://arxiv.org/abs/2610.36666v1)**
  - *Zongjun Yang, Rachitesh Kumar, Christian Kroer*
  - `2026-10-27`
  - We consider $T$ repeated second-price auctions across $n$ pacing bidders with i.i.d. item arrivals, and show that it is computationally impossible for all bidders to achieve no-regret simultaneously while satisfying their respective budget or return-on-investment constraints. The…

- **[A Serious-Game Testbed for Self-Governing Human-Machine Institutions](https://arxiv.org/abs/2610.36989v1)**
  - *Callum Berger, Jeremy Pitt, Stefan Sarkadi*
  - `2026-10-27`
  - AI agents no longer act alone: they cooperate, coordinate and compete within and between groups, increasingly alongside humans who are in, on or out of ``the loop''. Whether such mixed groups can govern themselves is an open question about machine behaviour and human-computer int…

- **[An Application of Geometric Riemannian Pricing Algorithm for Valuing Catastrophe Bonds in Incomplete Markets: Market-Consistent Financial Entropy and the Split of Frequency and Severity Risk Premia](https://arxiv.org/abs/2610.37171v1)**
  - *Saeid Safarveisi*
  - `2026-10-27`
  - This paper presents a framework for pricing catastrophe (CAT) bonds in incomplete markets through Riemannian geometric optimization of financial entropy. We formulate pricing-measure selection as a maximum financial entropy problem on a finite-dimensional manifold of equivalent m…

- **[Simple Portfolios that Deliver Consistent Decent Returns](https://arxiv.org/abs/2610.36491v1)**
  - *Oskar Edén Wallberg, Alexander Karolin*
  - `2026-10-27`
  - Portfolio construction has been studied extensively in both academia and industry. Its applications range from pension funds and hedge funds to private savings. The academic literature centers on methodology, commonly evaluated in settings that allow short selling, leverage, and…

- **[Algorithmic Monoculture in Machine Learning-based Site-Specific Fertilizer Recommendation](https://arxiv.org/abs/2610.36941v1)**
  - *Abdelghani Belgaid*
  - `2026-10-27`
  - Machine learning recommendations are often evaluated one model at a time, despite deployment across interconnected decision makers. For continuous NPK fertilizer prescriptions, correlated errors can aggregate across farms and generate systemic costs. A model of shared and farm-sp…

- **[kw-bench: Breaking Frontier Harnesses on Real-World Tasks](https://arxiv.org/abs/2610.36405v1)**
  - *George Juraj Salapa*
  - `2026-10-26`
  - Each new generation of frontier model pushes the edge of what is possible. Inside a harness -- a loop, a shell, a filesystem, the ability to write and run its own code -- a model can take on increasingly difficult work.   A growing body of work treats the coding-agent harness as…

- **[I-HITL: Inalienable Human-in-the-Loop](https://arxiv.org/abs/2610.35835v2)**
  - *Samuel Breckenridge, Dani Vilardell, Wenhao Wang et al.*
  - `2026-10-26`
  - Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.   We introduce the co…

- **[From Language to Drives: A Multimodal Framework for Aligning Autonomous Robots with Human Purposes](https://arxiv.org/abs/2610.35629v1)**
  - *Diana Cerdas-Vargas, Alejandro Romero, Richard J. Duro*
  - `2026-10-26`
  - This work explores a multimodal approach to the alignment of the behavior of open-ended learning autonomous robots with human purposes through the use of large language models as cultural enablers. While autonomous robots can generate their own skills and goals through interactio…

- **[Evolve on Graph: Self-Evolving Knowledge Graph Reasoning without Question Annotations](https://arxiv.org/abs/2610.35598v1)**
  - *Zongyuan Sun, Shuai Zhao, Ke Shu et al.*
  - `2026-10-26`
  - Knowledge graphs (KGs) provide reliable external knowledge for multi-hop factual reasoning with large language models (LLMs), yet most KGs in real-world domains such as finance and industry lack question--answer (QA) annotations. Without such annotations, existing methods struggl…

- **[Agentic Algorithm Design: LLMs that Propose, Formalise, and Prove Runtime Bounds for Evolutionary Algorithms in Lean](https://arxiv.org/abs/2610.35595v2)**
  - *Per Kristian Lehre*
  - `2026-10-26`
  - LLMs now prove hard theorems in Lean. Can they also design algorithms and prove their correctness and efficiency? LLM-guided design of optimisation heuristics (such as AlphaEvolve) is purely empirical. Automated theorem provers with LLMs prove given statements. So far, there has…

- **[Skill$^{\infty}$: Recursive Self-Improvement for Agent Skill Optimization](https://arxiv.org/abs/2610.35434v1)**
  - *Wangcheng Tao, Zhanglu Yan, Han Wu et al.*
  - `2026-10-26`
  - Recursive self-improvement (RSI), in which a system also improves the way it improves, is a long-standing aspiration on the path to AGI. Language agents increasingly store procedural knowledge in reusable skills. Optimizing skills offers a direct way to achieve RSI, because the o…

- **[Belief-Conditioned Multi-Agent Actor Critic for Decentralized LLM Collaboration](https://arxiv.org/abs/2610.35398v1)**
  - *Tianle Chen, Shuo Liu, Christopher Amato*
  - `2026-10-26`
  - Recent work has explored optimizing LLM collaboration through Multi-Agent Reinforcement Learning (MARL), but many approaches still rely on predefined workflows, limiting efficiency and scalability. Decentralized LLM collaboration is challenging because agents execute independentl…

- **[MarkovSim: an LLM Agent Harness with Bounded Context for Long-Horizon Computational Simulation](https://arxiv.org/abs/2610.35349v1)**
  - *Yeui-Lung Lei, Wen-Bo Chen, Pan Zhang*
  - `2026-10-26`
  - Recent studies have applied large language model (LLM) agent systems to computational simulation workflows. Such workflows are long-horizon, so the information generated can exceed what an LLM can reason over at once, its context window. Context management is therefore essential,…

- **[RSIV-Harness: A Recursive Self-Improvement Harness Framework for Open-Domain Conversational Text-to-Visualization](https://arxiv.org/abs/2610.35316v1)**
  - *Jiawei Lu, Chen Zhang, Jinwei Lu et al.*
  - `2026-10-26`
  - Users often request charts without knowing which database or table holds the relevant data. Such requests may be ambiguous, and users may ask follow-up questions to deepen their analysis or iteratively refine existing charts. A useful assistant must therefore discover relevant da…

- **[Same Story, Different Lens: A Multi-Agent System for Cross-Outlet News Framing Analysis](https://arxiv.org/abs/2610.35208v1)**
  - *Affan Yasin, Yueqi Lyu, Rubia Fatima et al.*
  - `2026-10-26`
  - News outlets covering the same event differ in what they emphasize and omit. \textit{Same Story, Different Lens} is an experimental research prototype for comparing these choices. It collects world and politics coverage from 17 outlets, groups reports about the same event, and pr…

- **[UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity](https://arxiv.org/abs/2610.35980v1)**
  - *Yijun Zhou, Minghao Shao, Ke Zhang et al.*
  - `2026-10-26`
  - Game development stresses coding agents in ways general software engineering does not: correctness depends on how engine APIs, serialized scene state, and runtime behavior interact, not on source code alone. Existing benchmarks mainly target platforms such as Godot and heavily re…

- **[CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems](https://arxiv.org/abs/2610.35082v1)**
  - *Yujia Zheng, Tianhao Li, Shangzhi Xu et al.*
  - `2026-10-26`
  - Agent Skills allow LLM agents to combine reusable capabilities, but checking each Skill in isolation cannot rule out policy violations when they are composed. We term such failures Conflict of Skills (CoS): artifacts or assessment signals produced for one purpose may be reused do…

- **[AIPC: Evidence-Guided Agent Workflows for PyTorch Project Deployment](https://arxiv.org/abs/2610.34890v1)**
  - *Zhanwei Wu, Jianhao Su, Brian Zhang et al.*
  - `2026-10-26`
  - Deploying and optimizing a PyTorch inference project on a dedicated accelerator, especially an on-device NPU, requires more than using a framework device API as with CUDA. The project must be converted into hardware-runtime artifacts and adapted to the target toolchain and applic…

- **[NumTrace: Auditing the Number Provenance of Financial Analyst Agents](https://arxiv.org/abs/2610.34887v1)**
  - *Tianlei Zhu, Matt White, Xue Liu et al.*
  - `2026-10-26`
  - A numerical claim generated by a financial analyst agent can match a number in a company filing but refer to the wrong entity, concept, period, unit or scope. A check based on reference answers can mark such an answer as wrong but does not explain why it fails. In this paper, we…

- **[DecoyCount: Evaluating Visual-Reasoning Misalignment in Counting](https://arxiv.org/abs/2610.34855v1)**
  - *Qiuyi, Zhang, Zhen Xu et al.*
  - `2026-10-26`
  - Visual counting benchmarks report whether vision-language models produce the correct number, but not whether errors arise from perception or reasoning. We introduce DecoyCount, a benchmark built from 1,660 real-world images with designed decoys across seven mechanisms, along with…

- **[Thinking-in-Bets at Test Time Reduces Sycophantic Revisions in LLM Agents](https://arxiv.org/abs/2610.34654v1)**
  - *Nghi D. Q. Bui*
  - `2026-10-26`
  - Language model agents often abandon correct work when a user challenges it, yet simply telling them to stand firm makes them ignore real mistakes. Once an agent reads a complaint, it tends to discount its own earlier checks in order to agree with the user. We introduce Thinking-i…

- **[RobotAgentBench: Towards Open-world Robot Autonomy](https://arxiv.org/abs/2610.34649v1)**
  - *Lingjun Mao, Jinglin Cao, Lukun He et al.*
  - `2026-10-26`
  - Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm fo…

- **[Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning](https://arxiv.org/abs/2610.36075v1)**
  - *Koen Ponse, Aske Plaat, Thomas M. Moerland*
  - `2026-10-26`
  - Hardware-accelerated reinforcement learning in JAX has gained rapid popularity in recent years and has proven to be a successful method of scaling online reinforcement learning. The resulting ecosystem, however, is fragmented: environment suites define their own interfaces, and a…

- **[From Questions to Queries to Insights: A Schema-Grounded Agentic Workflow for Natural-Language Crash Data Analysis](https://arxiv.org/abs/2610.35054v1)**
  - *Jingwen Zhu, Keshu Wu, Steven T. Parker et al.*
  - `2026-10-26`
  - Transportation agencies maintain extensive crash databases to identify safety priorities, evaluate countermeasures, and guide resource allocation. Making these data accessible to practitioners requires flexible ways to translate analytical questions into reliable results. Existin…

- **[Heard Enough to Act: Early Tool Calling in Spoken Dialogue Systems](https://arxiv.org/abs/2610.34653v1)**
  - *Yizhou Peng, Chen Chen, Donghang Wu et al.*
  - `2026-10-26`
  - Latency-sensitive spoken agents must know not only which tool to call, but also when they have heard enough to act. Waiting for the turn to complete delays execution even when the request is already actionable. However, neither existing spoken agents nor spoken dialogue corpora d…

- **[Bayesian Replicator Dynamics and the Inversion of Strict Dominance in Bimatrix Games](https://arxiv.org/abs/2610.36345v1)**
  - *Jaime Ruiz-Serra, Nihat Ay, Michael Harré*
  - `2026-10-26`
  - Replicator dynamics, the central model of evolutionary game theory, describe populations evolving under selection and agents learning by trial and error. They also admit a third use: continuous-time Bayesian inference, in which an agent planning against an opponent accumulates ev…

- **[LLM-Enhanced Heterogeneous Graph Learning with Business Semantics for Financial Fraud Detection](https://arxiv.org/abs/2610.35298v1)**
  - *Yixuan Chen, Hongyu Zhan, Jie Sheng et al.*
  - `2026-10-26`
  - Financial fraud detection increasingly relies on heterogeneous transaction graphs, in which entities such as cards and merchants play distinct business roles and the risk meaning of an attribute depends on the entity's role: a high transaction volume may be routine for a merchant…

- **[Arya Forge: Auditing Validation and Release Approval for Financial Instruction Data](https://arxiv.org/abs/2610.34778v1)**
  - *Kushagra Bhatnagar, Deekshith Marla*
  - `2026-10-26`
  - Financial instruction-data pipelines must distinguish content validity from permission to release a particular dataset. Arya Forge combines typed records, current-content checks, and approval coverage bound to a dataset manifest. We evaluate its release boundaries in a financial-…

- **[FinLLM-KG: Knowledge Graph-Enhanced LLMs for Financial Sentiment Analysis in Algorithmic Trading](https://arxiv.org/abs/2610.36083v1)**
  - *Giorgos Iacovides, Oliver Hannibal, Wuyang Zhou et al.*
  - `2026-10-26`
  - Recent advances in Generative AI have substantially improved financial sentiment analysis through post-trained financial large language models (LLMs). However, existing approaches remain confined to predicting the sentiment of each article in isolation and operate as black boxes,…

- **[MINT: Mitigating Structural Inconsistency via Attentive Message Passing for Financial Anomaly Detection](https://arxiv.org/abs/2610.34950v1)**
  - *Yin-Ju Wu, Bi-Cheng Yan, Berlin Chen*
  - `2026-10-26`
  - Illicit account detection is a critical task for financial risk control systems, aiming to pinpoint malicious actors within transaction networks. Existing efforts typically recast transaction networks into directed multigraphs and leverage graph neural networks (GNNs) to detect a…

- **[Patient-specific rubric-based evaluation of large language models across longitudinal cancer care](https://arxiv.org/abs/2610.35847v1)**
  - *Wei-Wei Zhang, Pengkai Wang, Yan Li et al.*
  - `2026-10-26`
  - Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rather than tracking how clinical responsibilities evolve across a longitudinal care pathway. Here we introduce NPC-RubricBench, a phase-aware b…

- **[What Should an Information Bottleneck Encoder Learn? Separating Representation Learning from Rate Control](https://arxiv.org/abs/2610.36255v1)**
  - *Hassan Tavakoli, Bella Bose*
  - `2026-10-26`
  - The information bottleneck (IB) trades compression of an input $X$ against prediction of a target $Y$ through a multiplier $β=1/λ$, yet each operating point is usually served by training, or fully conditioning, a new encoder. For jointly Gaussian data, we show that the IB solutio…

- **[Balanced Sampling in Stochastic Multi-objective Bandits](https://arxiv.org/abs/2610.35551v1)**
  - *Mengfan Xu*
  - `2026-10-26`
  - In stochastic multi-objective bandits, Pareto optimal arms may represent different trade-offs among objectives. Balanced sampling across them is important in practical settings such as online advertising. Yet, there seems to be little consensus on how to measure fairness, to our…

- **[Event definition and the branching ratio: Hawkes estimates of price-change clustering in the consolidated quote feed](https://arxiv.org/abs/2610.36317v1)**
  - *Hyoeun Lee*
  - `2026-10-26`
  - Hawkes models of price changes in the consolidated US quote feed find a sub-millisecond kernel component and a branching ratio near criticality. We show that in large-tick stocks the first is the feed's construction: half of NBBO changes are locks or depleted quotes, resolved wit…

- **[Fuji: The Shape, Composition, and Spread of Demand Bursts on Robinhood Chain](https://arxiv.org/abs/2610.35738v1)**
  - *Pranay Anchuri*
  - `2026-10-26`
  - Demand on blockchain-based marketplaces arrives in bursts and at a high rate. On these platforms the data are completely visible, which makes it feasible to compare the bursty demand against the usual load. The congestion manifests as an increased demand for gas, the primary reso…

- **[Weekend Crypto Volatility and Monday Market Risk](https://arxiv.org/abs/2610.35702v1)**
  - *Pedram Ebadollahyvahed, Nneka Umeorah*
  - `2026-10-26`
  - Cryptocurrencies trade continuously while major traditional markets close over the weekend. We examine whether weekend cryptocurrency volatility predicts Monday variance in equity, commodity and fixed-income markets. Using daily range-based variance measures for Bitcoin, Ether, X…

- **[Beyond Wasserstein Proximity: Finding Better Transfer Sources](https://arxiv.org/abs/2610.35314v1)**
  - *Gordei Verbii, Georgii Killinkarov, Vladimir Yafarov*
  - `2026-10-26`
  - Source selection often favors similar data, yet marginal proximity need not identify the most useful pretraining source. We motivate a conditional alternative through domain-adaptation theory and a regression example in which broader source variation improves estimation despite i…

- **[AgentProofBench: Benchmarking Reusable Verifiers for Web Agents](https://arxiv.org/abs/2610.34634v1)**
  - *Jingjie Ning, Xueqi Li, Yi Lu et al.*
  - `2026-10-25`
  - Reusable Web-agent verification requires a rule to follow changing requirements and support subsequent execution. We introduce AgentProofBench, which connects paired tests of a frozen acceptance rule to execution from identical saved openings. The resource spans 97 tasks, 79 fami…

- **[EMMA: Structured Episodic Memory for Multi-Agent Workflow Synthesis](https://arxiv.org/abs/2610.35966v1)**
  - *Ruijia Niu, Kaiwen Liu, Rose Yu et al.*
  - `2026-10-25`
  - Deploying LLM agents in specialized domains often require fine-grained task-specific procedures and knowledge a general model lacks, yet parameter training is costly and non-interpretable, and hand-engineered agent systems shift the cost to expert labor. Episodic memory updates a…

- **[ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?](https://arxiv.org/abs/2610.34386v1)**
  - *Haojin Wang, Yangzhen Wu, Zeyi Chen et al.*
  - `2026-10-25`
  - Recursive self-improvement (RSI) requires an agentic system to design, train, and evaluate its own successor. Data-driven post-training is a central part of that loop, yet existing evaluations measure it on a single benchmark, where an agent selects from a static pool or distills…

- **[An Agentic AI Workflow for Liver Lesion Segmentation and Structured Radiology Reporting](https://arxiv.org/abs/2610.34599v1)**
  - *Fatma Ahmed Mansour, Rahatara Ferdousi, Manar Fathy Elshenawy*
  - `2026-10-25`
  - Despite advances in automated liver lesion segmentation, a gap remains between image-derived predictions and clinically interpretable radiology reports. Bridging this gap requires quantitative measurements that are both reproducible and traceable. We present an evidence-grounded…

- **[BE-CTDE: Blockchain-Enabled Multi-Agent Reinforcement Learning with Anomaly Detection and Token Economics](https://arxiv.org/abs/2610.34121v1)**
  - *Chih-Wei Huang, Hsin-Chieh Lee, Yun-Chen Yu et al.*
  - `2026-10-25`
  - Multi-agent reinforcement learning supports cooperative decision-making in Internet of Things systems, but strategic deviations can disrupt coordination and undermine confidence in the training process. This paper proposes Blockchain-Enabled Centralized Training and Decentralized…

- **[DynaFlow: Learning Free-Form Multi-Agent Orchestration](https://arxiv.org/abs/2610.34467v1)**
  - *Ruhao Liu, Qi Li, Shizun Wang et al.*
  - `2026-10-25`
  - Multi-agent systems often rely on predefined collaboration structures, limiting their ability to adapt to diverse task requirements. We introduce DynaFlow, a framework that integrates free-form executable workflow synthesis into the action space of the main agent. The agent decid…

- **[Models Verify Sufficiency, Not Validity: Usable Falsehoods Evade the Checks that Gaps Trigger](https://arxiv.org/abs/2610.34488v1)**
  - *Naveen Madiraju*
  - `2026-10-25`
  - Ask a model "how many settlements did the Normans control?" and it answers that the passage does not say. Tell it "given that the Normans controlled 12 settlements of 400 inhabitants, what is the total?" and it computes 4,800. Nothing was added to the passage; the unsupported fac…

- **[Reversion, Retention, and Semantic Intervention: Measuring Functional Content in CLIP Fine-Tuning Deltas](https://arxiv.org/abs/2610.34144v1)**
  - *Chih-Ting Liao, Kezhen Bao, Xin Cao*
  - `2026-10-25`
  - Fine-tuning adapts pretrained models to new tasks, but identifying which weight changes support the resulting behavior remains difficult. Weight-space interpretability assigns semantic descriptions to these changes, called fine-tuning deltas. Such descriptions leave open how much…

- **[Certifying Reward Alignment in Portfolio Reinforcement Learning](https://arxiv.org/abs/2610.34153v2)**
  - *Matin Tavakoli, Seyedreza Tavakoli, Faezeh Salmani et al.*
  - `2026-10-25`
  - Financial reinforcement learning often translates an investment objective into an additive risk-adjusted reward. An agent can optimise that reward accurately yet implement a different financial preference. We develop a decision audit for terminal mean-variance equilibrium that se…

- **[Intrinsic Gradient Barriers in Pushforward Deep Generative Models](https://arxiv.org/abs/2610.34484v1)**
  - *Edric Tam, Qingyang Liu, Barbara Engelhardt et al.*
  - `2026-10-25`
  - Broad classes of deep generative models (DGMs) operate by learning to map a simple source distribution, such as a standard Gaussian, to a complex high-dimensional target distribution. Despite their success, DGMs often empirically struggle to accurately represent distributions wit…


---
*Generated 2026-10-28 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
