# Daily Paper Digest — 2026-11-05 (Thursday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**570 unique papers** (728 topic-entries — cross-topic papers counted once per category)

---

## Agent  (391)

### AAAI

- **[D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies](https://arxiv.org/abs/2511.16590)**
  - *Sen Chen, Tong Zhao, Yi Bin et al.*
  - **AAAI 2025** · `2025-11-20`
  - Developing intelligent agents capable of operating a wide range of Graphical User Interfaces (GUIs) with human-level proficiency is a key milestone on the path toward Artificial General Intelligence. While most existing datasets and benchmarks for training and evaluating GUI agen…


### NeurIPS

- **[Scanner-Aware Coordinated Attacks on LLM Agent Skills](https://openreview.net/forum?id=HiqcfJyIUF)**
  - *Tongyan Hu, Xiaogeng Liu, Bryan Hooi et al.*
  - **NeurIPS 2025** · OpenReview · `2026-06-05`
  - With the rapid development of Large Language Model (LLM) agents, these agents increasingly rely on skills—modular capabilities that combine natural language specifications with executable code across multiple modalities—to extend agent behavior at scale. As skills become a key me…

- **[Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety](https://openreview.net/forum?id=7UXZAFMvpZ)**
  - *Lifei Liu, Haoran Yu, Xiaochong Jiang et al.*
  - **NeurIPS 2025** · OpenReview · `2026-05-26`
  - Safety evaluations of multi-agent LLM systems often compare a direct prompt against a planner-executor pipeline and report the difference as a single "pipeline effect." This aggregate hides
  several simultaneous changes: harmful intent may be recast as plausible operational work…

- **[Modeling Fairness as an Evolving Social Consensus via LLM-Based Multi-Agent Simulation](https://openreview.net/forum?id=BEA4PVipWF)**
  - **NeurIPS 2025** · OpenReview · `2026-02-20`

- **[AgentRace: Benchmarking Efficiency in LLM Agent Frameworks](https://openreview.net/forum?id=eUuxWAQA5F)**
  - *Yanling Xu, bangwei zeng, Zeyu Qiu et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-19`
  - Large Language Model (LLM) agents are rapidly gaining traction across domains such as intelligent assistants, programming aids, and autonomous decision systems. While existing benchmarks focus primarily on evaluating the effectiveness of LLM agents, such as task success rates and…

- **[Economic Confidentiality without Secrets: Making Intercepted LLM-Agent Communications Unusable](https://openreview.net/forum?id=sJbC5vtT2v)**
  - *Bolaji Makinde*
  - **NeurIPS 2025** · OpenReview · `2025-09-16`
  - We study whether LLM agents can exchange useful information over a public channel without secrets (no keys, no TEEs) while making unauthorized decoding economically impractical. We formalize an “economic confidentiality” objective and design a stochastic “private language” ${L_r}…

- **[How to Train Your LLM Web Agent: A Statistical Diagnosis](https://openreview.net/forum?id=HBx2K7SVYh)**
  - *Dheeraj Vattikonda, Santhoshi Ravichandran, Emiliano Penaloza et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-03`
  - LLM-based web agents have recently made significant progress, but much of it has
occurred in closed-source systems—widening the gap with open-source alternatives.
Progress has been held back by two key challenges—first, a narrow focus on single-
step tasks that overlooks the comp…

- **[AsymPuzl: An Asymmetric Puzzle for multi-agent cooperation](https://openreview.net/forum?id=SXcJh8hoLz)**
  - *Xavier Cadet, Edward Koh, Peter Chin*
  - **NeurIPS 2025** · OpenReview · `2025-09-03`
  - Large Language Model (LLM) agents are increasingly studied in multi-turn, multi-agent scenarios, yet most existing setups emphasize open-ended role-play rather than controlled evaluation.
We introduce AsymPuzl, a minimal but expressive two-agent puzzle environment designed to iso…

- **[Toward Community-Driven Agents for Machine Learning Engineering](https://openreview.net/forum?id=aKChEjaJpZ)**
  - *Sijie Li, Weiwei Sun, Shanda Li et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-03`
  - Large language model-based machine learning (ML) agents have shown great promise in automating ML research.
However, existing agents typically operate in isolation on a given research problem, without engaging with the broader research community, where human researchers often gai…

- **[Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design and Credit Assignment](https://openreview.net/forum?id=drP7qVUnUt)**
  - *Quan Wei, Siliang Zeng, Chenliang Li et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-02`
  - This paper investigates approaches to enhance the reasoning capabilities of Large Language Model (LLM) agents using Reinforcement Learning (RL).  Specifically, we focus on long-horizon multi-turn agent scenarios, which can be naturally modeled as Markov Decision Processes.  Altho…

- **[Orchestrator: Active Inference for Multi-Agent Systems in Long-Horizon Tasks](https://openreview.net/forum?id=21sPEvGUL2)**
  - *Lukas Beckenbauer, Johannes-Lucas Löwe, Ge Zheng et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-02`
  - Complex, non-linear tasks challenge LLM-enhanced multi-agent systems (MAS) due to partial observability and suboptimal coordination. We propose Orchestrator, a novel MAS framework that leverages attention-inspired self-emergent coordination and reflective benchmarking to optimize…

- **[The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets](https://openreview.net/forum?id=XZpIu68yW6)**
  - *Shenzhe Zhu, Jiao Sun, Yi Nian et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-01`
  - AI agents are increasingly used in consumer-facing applications to assist with tasks such as product search, negotiation, and transaction execution. In this paper, we investigate a future setting where both consumers and merchants authorize AI agents to automate the negotiations…

- **[Multi-Turn LLM Systems for Diagnostic Decision-Making: Considerations, Biases, and Challenges](https://openreview.net/forum?id=It7AgR3A9H)**
  - *Benjamin Liu, Sejong Kim, Drona Thoka et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-01`
  - This study investigates the systemic limitations and architectural design trade-offs of Large Language Model multi-agent systems (LLM-MAS) for clinical decision support, focusing on how agent collaboration and architectural choices influence reasoning in complex medical problems.…

- **[Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning](https://openreview.net/forum?id=WYfzRJgWbO)**
  - *Shuo Liu, Tianle Chen, Christopher Amato*
  - **NeurIPS 2025** · OpenReview · `2025-08-22`
  - A large amount of work has been done in Multi-Agent Systems (MAS) for modeling and solving problems with multiple interacting agents.  However, most LLMs are pretrained independently and not specifically optimized for coordination. Existing LLM fine-tuning frameworks rely on indi…

- **[CORE: Measuring Multi-Agent LLM Interaction Quality under Game-Theoretic Pressures](https://openreview.net/forum?id=cArAB6Sj5X)**
  - *Punya Syon Pandey, Yongjin Yang, Jiarui Liu et al.*
  - **NeurIPS 2025** · OpenReview · `2025-08-17`
  - Game-theoretic interactions between agents with Large Language Models (LLMs) have revealed many emergent capabilities, yet the linguistic diversity of these interactions has not been sufficiently quantified. In this paper, we present the Conversational Robustness Evaluation Score…

- **[Scalability of LLM-Based Multi-Agent Systems for Scientific Code Generation: A Preliminary Study](https://openreview.net/forum?id=h8KFX5HM3N)**
  - *Yuru Wang, Kaiyan Zhang, Kai Tian et al.*
  - **NeurIPS 2025** · OpenReview · `2025-08-16`
  - Recent studies indicate that LLM-based Multi-Agent Systems (MAS) encounter scalability challenges in complex mathematical problem-solving or coding tasks, exhibiting issues such as inconsistent role adherence and ineffective inter-agent communication. Moreover, the performance ad…

- **[AIOS: LLM Agent Operating System](https://openreview.net/forum?id=L4HHkCDz2x)**
  - *Kai Mei, Xi Zhu, Wujiang Xu et al.*
  - **NeurIPS 2025** · OpenReview · `2025-03-19`
  - LLM-based intelligent agents face significant deployment challenges, particularly related to resource management. Allowing unrestricted access to LLM or tool resources can lead to inefficient or even potentially harmful resource allocation and utilization for agents. 
Furthermore…

- **[SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks](https://arxiv.org/abs/2506.11791)**
  - *Hwiwon Lee, Zi-Qi Zhang, Hanxiao Lu et al.*
  - **NeurIPS 2025** · `2025-06-13`
  - Rigorous security-focused evaluation of large language model (LLM) agents is imperative for establishing trust in their safe deployment throughout the software development lifecycle. However, existing benchmarks largely rely on synthetic challenges or simplified vulnerability dat…

- **[REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://arxiv.org/abs/2504.11543)**
  - *Divyansh Garg, Shaun VanWeelden, Diego Caples et al.*
  - **NeurIPS 2025** · `2025-04-15`
  - We introduce REAL, a benchmark and framework for multi-turn agent evaluations on deterministic simulations of real-world websites. REAL comprises high-fidelity, deterministic replicas of 11 widely-used websites across domains such as e-commerce, travel, communication, and profess…


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

- **[FairCoder: Probing LLM Bias in High-Stakes Decision Making via Coding Tasks](https://openreview.net/forum?id=n7Mk11IVX8)**
  - *Yongkang Du, Jen-tse Huang, Jieyu Zhao et al.*
  - **ICML 2025** · OpenReview · `2026-06-03`
  - Large language models (LLMs) are increasingly used in high-stakes decisions such as hiring and college admissions, making their social bias a critical concern. While LLMs are trained to refuse explicitly biased requests, bias can be leaked implicitly during LLM planning and reaso…

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

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **ICLR 2026** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…

- **[HeurekaBench: A Benchmarking Framework for AI Co-scientist](https://arxiv.org/abs/2601.01678)**
  - *Siba Smarak Panigrahi, Jovana Videnovi'c, Maria Brbic*
  - **ICLR 2026** · `2026-01-04`
  - LLM-based reasoning models have enabled the development of agentic systems that act as co-scientists, assisting in multi-step scientific analysis. However, evaluating these systems is challenging, as it requires realistic, end-to-end research scenarios that integrate data analysi…

- **[MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents](https://arxiv.org/abs/2508.21475)**
  - *Xi-Jia Tao, Yi-Hua Teng, Xinxing Su et al.*
  - **ICLR 2025** · `2025-08-29`
  - Existing multimodal browsing benchmarks often fail to require genuine multimodal reasoning, as many tasks can be solved with text-only heuristics without vision-in-the-loop verification. We introduce MMSearch-Plus, a 311-task benchmark that enforces multimodal understanding by re…


### KDD

- **[CR-Bench-v2: Evaluating the Real-World Utility of AI Code Review Agents](https://arxiv.org/abs/2611.02566v2)**
  - *Kristen Pereira, Neelabh Sinha, Rajat Ghosh et al.*
  - **KDD** · `2026-11-02`
  - The rapid growth of automated code generation has created a pressing need for automated code review. Yet code review resists full automation: it depends on context beyond the \textit{diff}, on the author's intent, and on judgments about design and maintainability on which even ex…

- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)**
  - *Mahmoud Mohammadi, Yi-Peng Li, Jean-Pierre Lo et al.*
  - **KDD 2025** · `2025-07-29`
  - The rise of LLM-based agents has opened new frontiers in AI applications, yet evaluating these agents remains a complex and underdeveloped area. This survey provides an in-depth overview of the emerging field of LLM agent evaluation, introducing a two-dimensional taxonomy that or…


### ACL

- **[RAGAM-AI: A Hybrid Reinforcement Learning based Agentic approach powered by Generative AI for Edge Resource Management](https://arxiv.org/abs/2611.06554v1)**
  - *Shreya K. Chari, John S. Vardakas, Kostas Ramantas et al.*
  - **ACL** · `2026-11-04`
  - Resource management for distributed edge networks hosting different services has been handled efficiently using Reinforcement learning (RL). Reward generalization in complex workflows is still an open issue within the RL realm. Therefore, this work proposes RAGAM-AI, a hybrid fra…

- **[Local Visibility Roadmaps in Continous Multi-agent Path Finding](https://arxiv.org/abs/2611.04944v1)**
  - *Kristýna Janovská, Pavel Surynek*
  - **ACL** · `2026-11-03`
  - We address the problem of smooth continuous multi-agent path finding (SC-MAPF), where agents move in a continuous environment along smooth curves in continuous time. The paths for individual agents are searched in local visibility roadmaps that consider obstacles and other agents…

- **[MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](https://arxiv.org/abs/2611.03555v1)**
  - *Farooq Shaikh, Biagio Montaruli*
  - **ACL** · `2026-11-02`
  - The Model Context Protocol (MCP) lets agentic AI frameworks connect language models to external tool providers, but it carries attacker-controlled content (tool descriptions, schema fields, and response data) into model context without validation. Prior benchmarks measure model c…

- **[Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials](https://arxiv.org/abs/2611.04073v1)**
  - *Anh Nguyen, Tianyi Xu, Phat Tran et al.*
  - **ACL** · `2026-11-02`
  - Recent work has improved computer-use agents (CUAs) by combining retrieved task-relevant tutorials and look-ahead planning using world models with MLLM judges. However, the contribution of each component -- tutorials, the judge, and the world model -- to overall improvement has n…

- **[DR Pixel: Page-Native Deep Research with Vision-Language Models](https://arxiv.org/abs/2611.03097v1)**
  - *Tiansheng Hu, Yichuan Wang, James V. Talwar et al.*
  - **ACL** · `2026-11-02`
  - Complex documents such as scientific papers contain rich information in tables, figures, and equations; however, existing deep research (DR) agents typically reduce papers to OCR-extracted text. We instead ask whether vision-language models (VLMs) can enable page-native deep rese…

- **[MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](https://arxiv.org/abs/2506.21605)**
  - *Hao-Ran Tan, Ze-Yu Zhang, Chen Ma et al.*
  - **ACL 2025** · `2025-06-20`
  - Recent works have highlighted the significance of memory mechanisms in LLM-based agents, which enable them to store observed information and adapt to dynamic environments. However, evaluating their memory capabilities still remains challenges. Previous evaluations are commonly li…

- **[AutoJudger: An Agent-Driven Framework for Efficient Benchmarking of MLLMs](https://arxiv.org/abs/2505.21389)**
  - *Xuanwen Ding, Chengjun Pan, Zejun Li et al.*
  - **ACL 2025** · `2025-05-27`
  - Evaluating multimodal large language models (MLLMs) is increasingly expensive, as the growing size and cross-modality complexity of benchmarks demand significant scoring efforts. To tackle with this difficulty, we introduce AutoJudger, an agent-driven framework for efficient and…

- **[ProjectEval: A Benchmark for Programming Agents Automated Evaluation on Project-Level Code Generation](https://arxiv.org/abs/2503.07010)**
  - *Kaiyuan Liu, You-Cheng Pan, Jing Li et al.*
  - **ACL 2025** · `2025-03-10`
  - Recently, LLM agents have made rapid progress in improving their programming capabilities. However, existing benchmarks lack the ability to automatically evaluate from users' perspective, and also lack the explainability of the results of LLM agents' code generation capabilities.…

- **[SOTOPIA-Ω: Dynamic Strategy Injection Learning and Social Instruction Following Evaluation for Social Agents](https://arxiv.org/abs/2502.15538)**
  - *Wenyuan Zhang, Tian-Yun Liu, Mengxiao Song et al.*
  - **ACL 2025** · `2025-02-21`
  - Despite the abundance of prior social strategies possessed by humans, there remains a paucity of research dedicated to their transfer and integration into social agents. Our proposed SOTOPIA-$\Omega$ framework aims to address and bridge this gap, with a particular focus on enhanc…

- **[WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)**
  - *Jialong Wu, Wen-Biao Yin, Yong Jiang et al.*
  - **ACL 2025** · `2025-01-13`
  - Retrieval-augmented generation (RAG) demonstrates remarkable performance across tasks in open-domain question-answering. However, traditional search engines may retrieve shallow content, limiting the ability of LLMs to handle complex, multi-layered information. To address it, we…


### EMNLP

- **[Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents](https://arxiv.org/abs/2502.20073)**
  - *Haochen Sun, Shu-Wen Zhang, Lu-Jie Niu et al.*
  - **EMNLP 2025** · `2025-02-27`
  - Large Language Models (LLMs) based agent systems have made great strides in real-world applications beyond traditional NLP tasks. This paper proposes a new LLM-based Multi-Agent System (LLM-MAS) benchmark, Collab-Overcooked, built on the popular Overcooked-AI game with more appli…


### Other / arXiv

- **[FrontierPhysics: Evaluating Agents for End-to-End Physics Research](https://arxiv.org/abs/2611.06910)**
  - *Bingran You, Wenjun Ke, Ria Rosenauer et al.*
  - 🤗 Featured · `2026-11-04`
  - AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce Fron…

- **[What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?](https://arxiv.org/abs/2611.06483)**
  - *Kejian Zhu, Zhuoran Jin, Shangqing Tu et al.*
  - 🤗 Featured · `2026-11-04`
  - While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth $K$ and interaction depth $T$ via $Pass@(K,T)$, we show that trajectory-level RL advanta…

- **[EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](https://arxiv.org/abs/2611.06518)**
  - *Mingzhe Zheng, Yue Wu, Jing Tan et al.*
  - 🤗 Featured · `2026-11-04`
  - Group Relative Policy Optimization (GRPO) has advanced generative model post-training in verifiable domains such as code and mathematics, but evaluating video quality, especially emotional expression, often depends on subjective aesthetics and has no uniquely correct target. Exis…

- **[PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://arxiv.org/abs/2611.05320)**
  - *Kewei Zhang, Juncheng Ma, Guodong Lv et al.*
  - 🤗 Featured · `2026-11-03`
  - Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, the agent receives a data request a…

- **[On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation](https://arxiv.org/abs/2611.05609)**
  - *Yichen Wang, Yufa Zhou, Siqi Zhu et al.*
  - 🤗 Featured · `2026-11-03`
  - Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) to consolidate capabilities from multiple teachers. Although prior work reports near-perfect in-distribution (IND) distillation performance, we find that this can mask incomplete capability consolida…

- **[DRAP: Dynamics-Risk Adaptive Plasticity for Continual Learning in Physical AI](https://arxiv.org/abs/2611.05029)**
  - *Oswaldo Ludwig*
  - 🤗 Featured · `2026-11-03`
  - Continual learning in physical AI differs from conventional continual learning because small per-step policy errors can accumulate over a trajectory. Each deviation may move the agent outside the training distribution, increase subsequent prediction errors, and ultimately cause c…

- **[SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding](https://arxiv.org/abs/2611.02846)**
  - *Tianyu Liu, Jun Zhang, Wenjie Huang et al.*
  - 🤗 Featured · `2026-11-02`
  - Speculative decoding (SD) accelerates large language model inference by reducing the sequential cost of token-by-token generation. Advanced SD methods reduce proposal cost with parallel drafters that predict entire blocks in one forward pass, but overall speedup still depends on…

- **[The SIMPLE Law for Energy Cost of LLM Inference](https://arxiv.org/abs/2611.03330)**
  - *Hiari Pizzini Cavagna, Andrea Proia, Daniele Cesarini et al.*
  - 🤗 Featured · `2026-11-02`
  - Generative AI is billed per token, yet tokens are not equally expensive. Each token enters the KV-cache and raises the cost of those that follow, so energy grows non-linearly along a sequence whose tokens look identical. No analytical model states what a token costs, and the most…

- **[Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization](https://arxiv.org/abs/2611.03517)**
  - *Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su et al.*
  - 🤗 Featured · `2026-11-02`
  - LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff. Scripted agents fix what the model does at each step, via a learned policy, an optimization menu, or fixed roles, and are sample-efficient where the recipe applies and stall where it does not.…

- **[Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning History Compaction on Future Generation and Agent Cost](https://arxiv.org/abs/2611.03852)**
  - *Anton Hristov*
  - 🤗 Featured · `2026-11-02`
  - Reasoning substantially improves language models' ability to solve difficult problems, but long reasoning traces make these gains expensive. Efficient reasoning should express useful analysis in fewer tokens by reducing repetition and text that adds little value to solving the pr…

- **[StreamDuo: A Live Commentator and a Research Agent for Unseen Games](https://arxiv.org/abs/2611.01120)**
  - *Zixian Gao, Penghao Luo, Xiangcheng Cao et al.*
  - 🤗 Featured · `2026-10-31`

- **[Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents](https://arxiv.org/abs/2610.41432)**
  - *Haoqing Wang, Xiaoyi Zhang, Sicheng Fan et al.*
  - 🤗 Featured · `2026-10-30`

- **[Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors](https://arxiv.org/abs/2610.36544)**
  - *Siddharth Jain, Venkat N. Vedam*
  - 🤗 Featured · `2026-10-27`

- **[LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856)**
  - *Haoxiang Cao, Yuxuan Zhang, Penghui Du et al.*
  - 🤗 · `2026-11-04`
  - We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence, rejecting distractors, binding e…

- **[Agent-Driven Generative Priors for Pathology Image Synthesis and Segmentation](https://arxiv.org/abs/2611.06701)**
  - *Sicheng Yang, Rui Tang, Haipeng Zhou et al.*
  - 🤗 · `2026-11-04`

- **[Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription](https://arxiv.org/abs/2611.06043)**
  - *Daniel Huang, Qi He, Shaoxiong Duan et al.*
  - 🤗 · `2026-11-04`
  - Streaming speech recognition is increasingly consumed by machines, such as translators and voice agents, that act on each token as it appears. A token that is later revised costs wasted work or a wrong action. In this work, we present Confucius4-R2T2 (short for Real Real-Time Tra…

- **[WayPOP: A Panoramic Open-Set Panoptic Tracking Benchmark](https://arxiv.org/abs/2611.05801)**
  - *Rohit Mohan, Maximilian Luz, Swarnava Chowdhury et al.*
  - 🤗 · `2026-11-04`
  - Holistic perception for autonomous agents requires reliably segmenting and associating scene elements across time and camera views, including objects outside a fixed semantic taxonomy. Existing open-set panoptic benchmarks focus on individual images or views, while panoramic trac…

- **[Visual Token Routing: Learning to keep tokens that matter](https://arxiv.org/abs/2611.06854)**
  - *Pranjal Aggarwal, Sean Welleck*
  - 🤗 · `2026-11-04`
  - Computer-use agents (CUAs) have recently achieved superhuman performance on several long-horizon benchmarks. However, their computational cost limits their use in long-horizon tasks and real-time domains such as video games. A key bottleneck is representing each screenshot as tho…

- **[MKD2World: A Typed Spatial MarkDown World Model For Web Agents](https://arxiv.org/abs/2611.06544)**
  - *Zhihao Nan, Sifan Zhou, Yiming Cheng et al.*
  - 🤗 · `2026-11-04`

- **[From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence](https://arxiv.org/abs/2611.05376)**
  - *Hao Fei*
  - 🤗 · `2026-11-03`
  - For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on a person's behalf. Yet people still forget what they once knew, miss what they a…

- **[τ-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems](https://arxiv.org/abs/2611.04459)**
  - *Bharath Sivaram Narasimhan, Karthik R. Narasimhan*
  - 🤗 · `2026-11-03`
  - While conversational recommendation systems provide a more natural user interface, they face the challenge of progressively discovering a user's needs before they can recommend an item that satisfies them. To evaluate the ability of AI agents at this elicitation process, we intro…

- **[Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex](https://arxiv.org/abs/2611.05753)**
  - *Andrew Miracle, Phyl Georgiou, Christine Okoth et al.*
  - 🤗 · `2026-11-03`
  - Organizations accumulate evidence in conversations, documents, decisions and relationships, but they act on interpretations: judgements assembled from several observations, resting on assumptions, and revised as circumstances change. Existing retrieval, knowledge graphs and agent…

- **[Adversarial Speculative Reasoning Improves Long Horizon Agents](https://arxiv.org/abs/2611.05345)**
  - *Hongyin Luo, Wei Fang, Lijie Yang et al.*
  - 🤗 · `2026-11-03`
  - Speculative decoding has been treated purely as a systems optimization that speeds up large language model decoding without changing the model behavior. Under this view, the growing effort to train better draft models has been focused solely on acceptance rate. We argue that this…

- **[On Turn-Level Best-of-N Sampling for Scaling LLM Agents](https://arxiv.org/abs/2611.06868v1)**
  - *Jalaj Bhandari, Dhawal Gupta, Hongli Zhan et al.*
  - `2026-11-04`
  - In this work, we evaluate a simple inference-time scaling approach based on \textit{turn-level best-of-N sampling} (\method) for large language model (LLM) agents on complex, long-horizon tasks. We instantiate this using a \textit{generator-selector} framework with two LLMs; at e…

- **[CompressionBench: How can your coding agents compress LLMs?](https://arxiv.org/abs/2611.06858v1)**
  - *Xinrui Zhong, Zhifeng Li, Zhiming Wang et al.*
  - `2026-11-04`
  - Recursive self-improvement requires AI systems to improve the models and infrastructure used by subsequent systems. LLM compression offers a concrete efficiency objective: retain a pretrained model's behavior within a smaller model storage budget. We study whether coding agents c…

- **[ServerBench: How can your coding agents design specialized LLM serving systems?](https://arxiv.org/abs/2611.06841v1)**
  - *Xinrui Zhong, Zhiming Wang, Yongqi Liu et al.*
  - `2026-11-04`
  - Large language model (LLM) coding agents develop software through experimentation, offering an opportunity to design the serving systems supporting their own operation. Effective serving requires coordinating implementation and operating decisions under session dependencies, late…

- **[Enabling AWS Cloud FPGA Development Using High-Level Vitis HLS](https://arxiv.org/abs/2611.06829v1)**
  - *David Rostcheck*
  - `2026-11-04`
  - We present a toolchain for development of ML models on AWS EC2 F2 cloud FPGA infrastructure from high-level language, implementing a complete Vitis HLS to HDK bridge to AFI workflow that has been absent from the academic literature despite eight years of AWS FPGA availability. We…

- **[Task-Efficient Agent Evaluation Using Cached Traces](https://arxiv.org/abs/2611.06803v1)**
  - *Ben Johnson, Hayden Helm*
  - `2026-11-04`
  - Efficient benchmarking estimates a system's full benchmark performance from a small number of task executions. Standard approaches rely solely on the binary correctness of executions from a collection of already-evaluated reference systems. An agentic system, however, produces a…

- **[Transforming Integer Grids to Spatial Intuition: Perception, Not Planning, Governs ARC-AGI-3](https://arxiv.org/abs/2611.06793v1)**
  - *Harsidak Singh Banwait*
  - `2026-11-04`
  - Sample-efficient fluid intelligence requires agents that rapidly form working models of unfamiliar interactive environments. ARC-AGI-3 tests this across uninstructed visual games scored by Relative Human Action Efficiency, which penalizes exploratory waste quadratically. When fro…

- **[Route First, See Later: Enabling Vision Agents to Reason Scientifically by Separating Routing Policy from Action Spaces](https://arxiv.org/abs/2611.06760v1)**
  - *Shubhabrata Mukherjee, Jeffrey Donatelli, Daniela Ushizima*
  - `2026-11-04`
  - Scientific image-analysis workflows require agents to select among diverse capabilities like description, detection, counting, and segmentation. Current multi-tool architectures conflate intent interpretation with visual execution, masking whether a failure arises from flawed rea…

- **[LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks](https://arxiv.org/abs/2611.06687v1)**
  - *Jenny Yang, Elizabeth Proehl, Anjan Bharadwaj et al.*
  - `2026-11-04`
  - We introduce LifeVal, a benchmark evaluating AI model performance on personalized agentic consumer tasks. LifeVal covers the most valuable life tasks that a personalized digital superassistant could automate, representing over 1.7 trillion US dollars in annual willingness-to-pay…

- **[AgentTrustCI: Build-Time Policy, Grounding, and Trajectory Tests for Java LLM Agents](https://arxiv.org/abs/2611.06674v1)**
  - *Sachin Gupta*
  - `2026-11-04`
  - Infrastructure security does not establish whether an LLM agent selected an allowed tool, grounded its answer in tool output, or followed a required workflow. AgentTrustCI is a Java/JUnit 5 framework that expresses these application-layer expectations as policy, grounding, and tr…

- **[Where Search Agents Go Off the Rails: Graph-Grounded Step-Level Verification](https://arxiv.org/abs/2611.06662v1)**
  - *Hyeseo Jeon, Seonho Yoo, Jay-Yoon Lee*
  - `2026-11-04`
  - Search-augmented reasoning systems can reach correct answers while making errors in intermediate steps. Reliable auditing must check whether evidence $D$ covers the question $Q$, reasoning $T$ addresses $Q$, and $T$ is grounded in $D$. We introduce GraphRail, which represents req…

- **[Interactive World Simulation with Cosmos for Physical AI](https://arxiv.org/abs/2611.06627v1)**
  - *NVIDIA, :, Anis Ahmad et al.*
  - `2026-11-04`
  - We present a shared framework that adapts Cosmos world foundation models for real-time interactive world simulation in Physical AI. By streaming visual observations in response to actions and scene controls, the framework enables users and embodied agents to interact with evolvin…

- **[Time-Division Multiplexing: The Operational Rhythm and Temporal Organization Layer of Digital Life](https://arxiv.org/abs/2611.06603v1)**
  - *Haibin Tong, Luming Guo, Nana Cui et al.*
  - `2026-11-04`
  - Continual agents must handle urgent interaction while retaining alternatives, replaying errors, and committing safe long-term changes. A previous digital-life framework distinguishes online (busy) and offline (idle) channels, but leaves open whether these are separate programs or…

- **[Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains](https://arxiv.org/abs/2611.06585v1)**
  - *Yichiet Aun, Mohammed A. Alhartomi, Jing Jie Tan et al.*
  - `2026-11-04`
  - AI agents rely on third-party tools, such as Model Context Protocol (MCP) servers, whose publishers can be authenticated and whose execution can be restricted by runtime security policies. Yet authenticity does not guarantee benign behaviour: a legitimately signed tool may perfor…

- **[Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment](https://arxiv.org/abs/2611.06543v1)**
  - *Shumao Wu, Kongcheng Zhang, Jianqiang Huang et al.*
  - `2026-11-04`
  - Agent trajectories often contain both successful decisions and failed attempts, yet optimization with sparse trajectory-level rewards struggles to identify which critical decisions should be reinforced or suppressed. We observe that meaningful distinctions among on-policy traject…

- **[ElecLoad: Adaptive Electricity Load Forecasting Guided by Multiple Events](https://arxiv.org/abs/2611.06508v1)**
  - *Huajian Zhang, Mingyue Cheng, Xingpeng Gao et al.*
  - `2026-11-04`
  - Accurate electricity load forecasting provides critical decision support for energy procurement, generation scheduling, and supply-demand balancing, contributing to the economic efficiency and operational reliability of power systems. However, future electricity demand can be aff…

- **[Tools Need Not Speak in Text: Latent Context Compression for Agents](https://arxiv.org/abs/2611.06500v1)**
  - *Yuetong Liu, Zhehao Zhou, Yitong Zhang et al.*
  - `2026-11-04`
  - Large language model (LLM) agents typically append raw tool outputs to their context. Over multi-step interactions, long and noisy observations incur substantial context overhead and dilute the agent's attention to task-relevant information. Existing token pruning and summarizati…

- **[ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs](https://arxiv.org/abs/2611.06481v1)**
  - *Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal et al.*
  - `2026-11-04`
  - Graph-based retrieval-augmented generation (GraphRAG) answers questions by retrieving over a knowledge graph built from a corpus. Yet retrieval strategies are designed around the structure their own construction pipeline produces, and whether they survive a change of construction…

- **[SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory](https://arxiv.org/abs/2611.06445v1)**
  - *Jizhe Zhang, Ang Li, Chenheng Zhang et al.*
  - `2026-11-04`
  - Long-horizon language-model agents accumulate increasingly large interaction histories, making context compaction essential for efficient execution. Existing learned compaction methods often rely on downstream task outcomes or solver behavior, coupling training to specific tasks…

- **[EviSeek: An Evidence-Centric Agentic Framework for Embodied Active Information Seeking](https://arxiv.org/abs/2611.06434v1)**
  - *Jintao Li, Zhiyong Cao, Baihua Xiao et al.*
  - `2026-11-04`
  - Active embodied question answering requires agents to acquire evidence through viewpoint changes and physical interaction. The central challenge is to avoid undirected interaction: taking plausible actions without specifying what evidence they should reveal for answering the ques…

- **[Zero-Shot Coordination among LLM Agents](https://arxiv.org/abs/2611.06409v1)**
  - *Adrian Hayler, Shashank Reddy Chirra, Andrei Lupu et al.*
  - `2026-11-04`
  - We study zero-shot coordination (ZSC), where independently developed agents must coordinate at test time. While ZSC has been well studied in the RL literature, far less is known about the performance of LLM agents despite their increasing deployment in such settings. Existing wor…

- **[MA-Mesh: Resilient Multi-Agent Collaboration via Role-based Self-Healing](https://arxiv.org/abs/2611.06389v1)**
  - *JunYong Lee, Woo Kyung Kim, Honguk Woo*
  - `2026-11-04`
  - Effective collaboration in multi-agent systems requires mechanisms for coordination and adaptability in dynamic and uncertain environments. However, existing multi-agent systems rarely model resilience explicitly, instead relying on ad-hoc output correction that limits systematic…

- **[From hydrological laws to catchment models: A process-based model matches deep-learning accuracy on three continents](https://arxiv.org/abs/2611.06382v1)**
  - *Xilin Xia*
  - `2026-11-04`
  - Dooge asked whether hydrology has laws at the catchment scale. We ask whether a low-dimensional system built under physical laws can match the accuracy of neural networks that outperform process-based models on the same inputs. Three laws constrain a lumped catchment model. Conse…

- **[LegalEvolver: Agentic Legal Judgment Prediction via Rubric-Guided Self-Evolution](https://arxiv.org/abs/2611.06381v1)**
  - *Xinyu Yang, Jiejun Tan, Chenlong Deng et al.*
  - `2026-11-04`
  - As LLM-based agents develop, they have been increasingly applied in the legal domain. Legal Judgment Prediction~(LJP) requires models to conduct multi-step reasoning and external legal evidence retrieval. Existing legal search agents' performance is often constrained by the quali…

- **[Corralling AI Risks with Grassroots Contracts](https://arxiv.org/abs/2611.06374v1)**
  - *Ehud Shapiro*
  - `2026-11-04`
  - AI's inflection point is a fountain of alarming risks. Digital platforms in particular are vulnerable to three major AI risks, as those in control of global platforms cede control to AI, of the algorithms, of membership and of content: (1) AI control of global platforms, social a…

- **[A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code](https://arxiv.org/abs/2611.06294v1)**
  - *Jiongchi Yu, Keke Lian, Junqing Wang et al.*
  - `2026-11-04`
  - Large language model (LLM) coding assistants and agents construct a repository context before generating code. For security-sensitive code, this context decides whether the model sees the project's safeguards (e.g., authorization checks) or insecure code to imitate. However, cont…

- **[HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](https://arxiv.org/abs/2611.06254v1)**
  - *Zhi Hong, Qianlong Wang, Hongchen Wei et al.*
  - `2026-11-04`
  - The performance of large language model (LLM) agents depends on both the underlying model and the harness that governs interaction with tools and the environment. Yet harness design remains largely manual, and automating it requires navigating an open-ended search space through c…

- **[A Definition of Catastrophic Performance](https://arxiv.org/abs/2611.06219v1)**
  - *Henrik Marklund, Alex Infanger, Benjamin Van Roy*
  - `2026-11-04`
  - A central challenge in AI is specifying objectives that align with human preferences. While existing theoretical results elucidate how misspecification impacts performance, they typically do not distinguish between merely suboptimal and catastrophic outcomes. To enable rigorous a…

- **[ModalSearcher: Weaving Visual Evidence into Autonomous Cross-Modal Deep Search](https://arxiv.org/abs/2611.06131v1)**
  - *Zhihan Yin, Ruyi Li, Chengyu Fang et al.*
  - `2026-11-04`
  - Static and incomplete parametric knowledge limits the performance of multimodal large language models on novel-knowledge and knowledge-intensive tasks, especially those requiring multi-hop evidence acquisition. Existing multimodal agentic search methods often fix visual evidence…

- **[The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules, Unevenly Across Models](https://arxiv.org/abs/2611.06116v1)**
  - *Mehmet Murat Huyut*
  - `2026-11-04`
  - Banks validate language models, but they deploy systems: a model inside a harness that decides what it sees, which tools it can call and who checks its actions. We test whether that harness changes compliance with banking conduct rules when the model is held fixed. Four open-weig…

- **[Reglos: A Self-Evolving Personal Memory Agent with Recursive Self-Improvement](https://arxiv.org/abs/2611.06049v1)**
  - *Sen Yang, Jiaduo Lin, Zehong Huang et al.*
  - `2026-11-04`
  - Personal agents draw on past conversations to tailor their responses to each user. Their memory systems store and update what each user says, and coding agents now also rewrite the harness that turns this memory into the model's context. Such patches risk overfitting, because one…

- **[Graph-Mediated Large Language Model Systems in the Agentic Era: Reasoning, Knowledge, Retrieval, Execution, and Coordination](https://arxiv.org/abs/2611.05953v1)**
  - *Haihui Liu, Yang Chen, Zice Qiu et al.*
  - `2026-11-04`
  - Graphs play an increasingly important role in large language model (LLM) systems, supporting structural reasoning, knowledge grounding, retrieval, and memory. As these systems evolve toward the agentic era, graphs also organize execution dependencies and multi-agent communication…

- **[Autonomous agents for electricity-system planning](https://arxiv.org/abs/2611.05911v1)**
  - *Yoon Pyo Lee, Samrendra Roy, Jay Phil Yoo et al.*
  - `2026-11-04`
  - Planning electricity systems requires repeated decisions that connect regional resources, investment, operation and network constraints. Here we present an autonomous planning framework that carries prepared regional scenarios through proposal, numerical evaluation, feedback inte…

- **[CellCanon: An Agentic Cellular World Model for Prediction, Explanation, and Observation-Driven Updating](https://arxiv.org/abs/2611.05890v1)**
  - *Zhaokang Liang, Shuyang Zhuang, Xiaoran Jiao et al.*
  - `2026-11-04`
  - Biological discovery requires using molecular knowledge and new measurements to infer responses beyond the conditions already observed. We introduce CellCanon, the first agentic cellular world model to unify single-cell expression prediction, evidence-grounded explanation, and ob…

- **[Autonomy and Coordination in Intelligent Manufacturing: A Recursive Autonomous Agent Framework](https://arxiv.org/abs/2611.05828v1)**
  - *Yuning Chen, Hongda Zhang, Linqiang Hu et al.*
  - `2026-11-04`
  - Intelligent production requires systems to make decisions and organize work according to production goals and operating conditions. It also requires continuous adjustment through feedback. This paper analyzes intelligence in human production organizations from a complex adaptive…

- **[A Hybrid Approach for Automated Security Pattern Recovery](https://arxiv.org/abs/2611.05823v1)**
  - *Anh Minh Nguyen, Tuan Dat Tran, Alzubair Hassan et al.*
  - `2026-11-04`
  - Security-by-design emphasises integrating security into software design and development. Security pattern catalogues operationalise this principle by prescribing reusable architectural solutions to recurring security problems. However, recovering their implementations from source…

- **[Learning When Human Decisions Matter: Executor-Relative Consultation Value for LLM Agents](https://arxiv.org/abs/2611.05814v1)**
  - *Shuli Jiang, Khushbu Pahwa, Yuting Zhang et al.*
  - `2026-11-04`
  - Large language models increasingly automate complex tasks, but human decision capacity does not scale with their capabilities. In many applications, humans remain essential for providing private context, authority, or judgments unavailable to the agent. We formulate human decisio…

- **[When File Ingestion Misleads Language Models: Measuring and Mitigating Divergences in Office Documents](https://arxiv.org/abs/2611.05806v1)**
  - *Penghui Li*
  - `2026-11-04`
  - Office documents are now routinely uploaded to large language models (LLMs) for processing. However, an LLM does not always see what a human sees, because it typically reads the text that an extractor produces from the document's underlying Office Open XML (OOXML) files. Dependin…

- **[GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802v1)**
  - *Mohan Cao, Yongsen Mao, Chucheng Xiang et al.*
  - `2026-11-04`
  - Recent LLM-centric advances can generate attractive furnished rooms by selecting and arranging assets. Yet evaluation remains limited to specific perspectives or predefined questions, failing to reflect overall scene quality. To address this pressing need, we introduce GREP. Its…

- **[DARE: Difficulty Analysis for Repair Enhancement](https://arxiv.org/abs/2611.05797v1)**
  - *Jikwang Lee, Seungwook Jung, Jaechang Nam*
  - `2026-11-04`
  - LLM-based coding agents are primarily evaluated by their solve rates. However, this metric does not reveal how difficult the solved tasks are or account for differences intask difficulty across benchmarks. Determining the difficulty of individual tasks by repeatedly running multi…

- **[FlyHash for LLM Agent Memory: An Empirical Validation and a New Application](https://arxiv.org/abs/2611.05791v1)**
  - *Mohan Bheemadolu, Chrisogonas O. Odhiambo*
  - `2026-11-04`
  - Large language model (LLM) agents increasingly rely on external memory stores to retain information across conversations, typically via dense vector embeddings searched with approximate nearest-neighbor methods. The fruit fly's olfactory circuit computes a locality-sensitive hash…

- **[BobFlow: Towards Human-Agent Collaborative Data Science Using Dataflows](https://arxiv.org/abs/2611.05761v1)**
  - *Jiadong Bai, Yicong Huang, Chen Li*
  - `2026-11-04`
  - Recent advances in large language models (LLMs) have established human-agent collaboration as a promising paradigm for data science. Effective collaboration requires a shared computational abstraction that enables agents to reason about processing logic while allowing human analy…

- **[A Framework for Context Enrichment and Selective Robustness in LLM Social Agents](https://arxiv.org/abs/2611.06914v1)**
  - *Mattia Greiche, Reihaneh Rabbany, Maximilian Puelma Touzel*
  - `2026-11-04`
  - Researchers use large language models as agents in social simulations, where agents are prompted with observations and background information intended to shape their actions. Yet LLM agents have been shown to substantially change their behavior under meaning-preserving prompt var…

- **[Where It Breaks: Diagnosing Perception, Memory, and Decision Failures of a Vision-Language Agent in Pac-Man](https://arxiv.org/abs/2611.06704v1)**
  - *Xinglu Wang, Edward Wang, Yong Zhang et al.*
  - `2026-11-04`
  - Training an agent to play Pac-Man with only up, down, left and right actions raises a basic question: when performance is poor, what should be improved? Difficulty can arise from reading the screen or from choosing actions over a long sequence. We examine these problems in a Qwen…

- **[SecureGARD: Dynamic Ontology-Guided Governance for Secure Tool-Using LLM Agents](https://arxiv.org/abs/2611.06682v1)**
  - *Guoqin Xiong, Shengtao Wen, Xiang Chen et al.*
  - `2026-11-04`
  - Tool-using large language model (LLM) agents translate model outputs into consequential actions, turning indirect prompt injection into an execution-security problem. Existing defenses constrain tool calls, trajectories, or information flows, but often leave action semantics, sta…

- **[Analysis of Local Open-Weight LLM Agents on Vulnerability-Reproduction Tasks](https://arxiv.org/abs/2611.06257v1)**
  - *Jorge García-Carrasco, Javier Sanchis, Álvaro Navarro et al.*
  - `2026-11-04`
  - Open-weight language models that fit on a single consumer GPU are becoming capable on a growing range of tasks, and they matter because they can run locally without sending the code to a hosted service. Vulnerability reproduction, turning a vulnerability description into an input…

- **[Shallow Encoding Emits Deep Memories](https://arxiv.org/abs/2611.06084v1)**
  - *Mingyuan Ma, Yangmin Li, Harris Nover et al.*
  - `2026-11-04`
  - Hybrid language models interleave a few softmax-attention layers with many linear-attention or state-space layers, so every layer keeps a memory of earlier tokens: a key-value cache or a fixed-size recurrent state. Serving them spends more compute and high-bandwidth memory on the…

- **[A Controlled Experimental Evaluation of Configuration and Cache Architecture in LLM Serving Engines](https://arxiv.org/abs/2611.05991v1)**
  - *Muhammad Faizan Anwar, Sina Keshvadi*
  - `2026-11-04`
  - Multi-agent LLM applications repeat most of their prompt tokens across requests, and serving engines reuse the cached state of shared prefixes. vLLM and SGLang reuse it at different granularities, and benchmarks of their default deployments report large performance gaps, usually…

- **[SpecCompact: Accelerating LLM Agent Context Compaction with Slot-Parallel Semantic Speculative Verification](https://arxiv.org/abs/2611.06876v1)**
  - *Yulu An, Yifei Feng, Xiangyang Yin*
  - `2026-11-04`
  - LLM agents use context compaction to manage growing interaction histories, but summarizing long histories with large models can introduce substantial delays. Compaction therefore requires balancing information retention against latency. We observe that structured summary slots ca…

- **[When Do Summaries Become Instructions? Unsupported Policy in LLM Agents' Self-Written Handoff Summaries](https://arxiv.org/abs/2611.06545v1)**
  - *Wenhui Chu*
  - `2026-11-04`
  - Long-running LLM agents compact their context, replacing most history with a summary. We ask whether handoff summaries state permissions or requirements the record does not support, whether such sentences change what the next instance (the successor) does, and where they come fro…

- **[EvoGuard: Mitigating Degradation in Online Skill Evolution](https://arxiv.org/abs/2611.06444v1)**
  - *Yanli Wang, Zichen Bai, Tianyue Jiang et al.*
  - `2026-11-04`
  - Skills let language agents reuse experience across tasks as natural-language documents. Recent work evolves skills from interaction, but existing methods have limitations when skills evolve online. Prior methods update a skill offline from a batch of trajectories collected over m…

- **[TandemBench: Benchmarking Decision Models for Multi-Agent Collaboration](https://arxiv.org/abs/2611.05827v1)**
  - *Baohang Li, Xiaocheng Feng, Bing Qin*
  - `2026-11-04`
  - Decision models choose among predefined options in tasks such as routing and action selection. In multi-agent collaboration, a decision determines how members divide work, exchange resources, and act in parallel. We introduce TandemBench, a benchmark of 1,200 questions in multi-a…

- **[Airlock: Bounding the Multi-Agent Blast Radius via Selective Online Containment](https://arxiv.org/abs/2611.06727v1)**
  - *Zhonghao Zhan, Javad Forough, Yefan Zhang et al.*
  - `2026-11-04`
  - When multi-agent systems act on the external world, a single agent's faulty output can spread across tasks before detection, creating a system-wide blast radius. Single-agent guardrails are confined to individual harnesses, while existing multi-agent controls either cancel only t…

- **[Hard to Fool: A Bounded LLM Research Loop for Quantitative Finance, and What Two Dozen Campaigns Found](https://arxiv.org/abs/2611.06607v1)**
  - *Henry Zhang*
  - `2026-11-04`
  - Agentic research loops that let a language model propose a change, run a fixed experiment and keep whatever improves the metric work well in machine learning. In trading research the same loop is a machine for producing false discoveries: a backtest that "improves the metric" is,…

- **[PAYWORTHY: Can LLMs Predict Which Freelance Jobs an AI Agent Will Complete?](https://arxiv.org/abs/2611.05759v1)**
  - *Mohammad Reza Rezaei, Dingxian Wang, Brett Levert et al.*
  - `2026-11-03`
  - Before an AI agent takes on a paid job, someone has to judge whether it is likely to succeed. We test whether frontier language models can make this call before any attempt. We propose PAYWORTHY which contains 1{,}494 real freelance job postings, sampled from 18.8M postings made…

- **[PersonaCodeBench: Evaluating Coding Agents in Persona-driven Human-Interactive Sessions](https://arxiv.org/abs/2611.05739v1)**
  - *Haixin Wang, Jianheng Hou, Hongyu Shen et al.*
  - `2026-11-03`
  - Coding agents must deliver correct software while respecting users' expertise, preferences, and working conditions. Existing benchmarks increasingly incorporate interaction, yet personalized requirement fulfillment remains underexplored. We introduce PersonaCodeBench, which turns…

- **[OdorSpaces: Visual-Olfactory Embodied Navigation in 3D Environments](https://arxiv.org/abs/2611.05738v1)**
  - *Changyeon Lee, Kelin Yu, Zheng Wei et al.*
  - `2026-11-03`
  - Olfaction provides critical information about airborne chemical cues, yet it remains largely underexplored in embodied AI, with limited prior machine olfaction work focusing primarily on semantic odor perception. We introduce OdorSpaces, a physics-based simulation platform and be…

- **[Agents, Think Only When it Helps](https://arxiv.org/abs/2611.05709v1)**
  - *Min-Seon Kim, Seungdong Yoa, Sanghyu Yoon et al.*
  - `2026-11-03`
  - LLM agent distillation transfers agentic capabilities to student models by training on complete teacher trajectories that typically interleave thoughts and actions. We question how critical thought supervision is for agents' ultimate action performance. To answer this, we disenta…

- **[How Do Artificial Agents Make Decisions in Light of Visual Data?](https://arxiv.org/abs/2611.05671v1)**
  - *Keyty Loza, Shayan Monadjemi*
  - `2026-11-03`
  - Vision-language models (VLMs) have demonstrated significant advances in reasoning with visual data, which is particularly important given that much of human knowledge is encoded visually in scientific articles and other sources. However, a gap remains in understanding how artific…

- **[Combining Relevant Expert Knowledge Using Mixtures of Feedback Fuzzy Cognitive Maps](https://arxiv.org/abs/2611.05664v1)**
  - *Olaoluwa Adigun, Akash Kumar Panda, Bart Kosko*
  - `2026-11-03`
  - A neuro-symbolic system should combine only relevant answers from expert agents or other knowledge sources. Using only relevant experts for a given input query becomes ever more important for accuracy and scalability as the knowledge network grows and connects ever more knowledge…

- **[Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge](https://arxiv.org/abs/2611.05662v1)**
  - *Drake Benjamin Brown, Khushbu Pahwa, Yubin Ge et al.*
  - `2026-11-03`
  - Evaluating open-ended agent tasks increasingly falls to an Agent-as-a-Judge: an evaluator handed tools and the agent's full trajectory so it can verify a result against the environment. The premise is that a judge that gathers its own evidence should be grounded by it. We show th…

- **[Attributing Agent Failures to Their History Needs an Executed Counterfactual: Toward a Reporting Standard](https://arxiv.org/abs/2611.05650v1)**
  - *Egor Pakhomov, Erik Nijkamp*
  - `2026-11-03`
  - Published explanations of why long-horizon agents fail are commonly taxonomies labeled over completed trajectories: a judge reads a transcript and names the failure. We argue that a claim attributing an agent's behavior to its history should carry intervention-verified evidence,…

- **[Route to Remember: Adaptive Memory Selection for LLM Agents](https://arxiv.org/abs/2611.05636v1)**
  - *Zeyu Fang, Jun Yin, Yongsheng Mei et al.*
  - `2026-11-03`
  - The memory of production agents is increasingly becoming a bottleneck and is built almost exclusively from text: key points are extracted from out-of-limit context and retrieved into context at query time. Therefore, every new query incurs an additional cost that grows with the a…

- **[Assurance-Conditioned Continuous Authorization for Autonomous AI Agents](https://arxiv.org/abs/2611.05632v1)**
  - *Mehdi Shajari*
  - `2026-11-03`
  - Autonomous software agents can act through tools, delegate work, and change their models or execution environments while earlier authorizations remain in flight. We present Assurance-Conditioned Continuous Authorization (ACCA), an approach designed to be harness-independent, for…

- **[ViBench 2.0: A Benchmark for Long-Horizon Software Building](https://arxiv.org/abs/2611.05620v1)**
  - *Daniel Furman, Preeya Kirani, Ibrahim Sheikh et al.*
  - `2026-11-03`
  - On Replit, our agentic engineering platform, users now build entire products without writing code, through successive feature requests to an agent. Yet existing coding benchmarks evaluate single, fully specified tasks, and many are near saturation. We introduce ViBench 2.0, a ben…

- **[Anduin: A sybil-resistant agentic marketplace reputation system](https://arxiv.org/abs/2611.05586v1)**
  - *Reza Ramji, Preston Vander Vos, Ziming Zeng et al.*
  - `2026-11-03`
  - As autonomous AI agents enter permissionless onchain markets, selecting new service providers remains a core challenge. Existing reputation systems depend on scarce resources like human curation, identity credentials, or voluntary reviews, while naive volume rankings are vulnerab…

- **[VirtualTrialHarness: Coordinating Agentic Operationalization of Virtual Trial Protocols Across Complex Clinical Schemas](https://arxiv.org/abs/2611.05551v1)**
  - *Pengze Li, Jingna Feng, Yue Yu et al.*
  - `2026-11-03`
  - Virtual trials use routinely collected clinical data to evaluate treatment strategies, but translating a study protocol into an executable analysis requires determining how clinical concepts and study requirements should be represented in the available data and applied consistent…

- **[Iterated creation, grading, and revision of data science projects by language models](https://arxiv.org/abs/2611.05548v1)**
  - *Rohan Alexander*
  - `2026-11-03`
  - We evaluate the extent to which agentic AI models can complete an end-to-end data science project, and how this improves with feedback. A 'writer' model with specific tools creates a complete data science project including downloading, cleaning, and analyzing a dataset, and writi…

- **[MA-SafeDiffuser: Safe Multi-Agent Planning with Diffusion Probabilistic Models](https://arxiv.org/abs/2611.05524v1)**
  - *Kiran Ravish, Ankita Kushwaha, Preeti et al.*
  - `2026-11-03`
  - We propose MA-SafeDiffuser, a multi-agent extension of SafeDiffuser that equips diffusion-based trajectory planners with finite-time diffusion invariance guarantees for joint-agent safety specifications. Building on the single-agent construction that embeds control barrier functi…

- **[SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories](https://arxiv.org/abs/2611.05512v1)**
  - *Mingxuan Li, Huanzhi Mao, Ruitao Zheng et al.*
  - `2026-11-03`
  - AI Agents are becoming digital coworkers that can browse the web, write code, run experiments, and assist humans over extended horizons. Yet existing benchmarks fall short of real knowledge work: many rely on synthetic data or isolated tasks, missing the complex, multi-party dyna…

- **[HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation](https://arxiv.org/abs/2611.05319v1)**
  - *Zhen Tao, Xun Zhou, Xuhui Chen et al.*
  - `2026-11-03`
  - In LLM-based recommendation, memory acts as a user-level agent in a memory-augmented backbone. Yet users and items remain asymmetric: only the user is given a structured profile; it enters a bandwidth-limited reranker prompt; and it is frozen after warmup. We recast LLM-based rec…

- **[Towards Robust Long-Lived Agents: Benchmarking Experience Lifecycles in Evolving Environments](https://arxiv.org/abs/2611.05450v1)**
  - *Shijue Huang, Hangyu Guo, Hengheng Zhang et al.*
  - `2026-11-03`
  - As agents become more capable, they are moving beyond one-off tasks toward sustained assistance across successive user goals. Such assistance requires agents to discover how unfamiliar environments work, reuse what they learn across tasks, and keep that experience current as envi…

- **[JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks](https://arxiv.org/abs/2611.05263v1)**
  - *Shanka Subhra Mondal, Jiayun Wang*
  - `2026-11-03`
  - Multimodal web agents have shown promising capabilities for interacting with websites through graphical user interfaces (GUIs), yet realistic web tasks often require long-horizon, multi-step planning that remains challenging for monolithic policies. Such agents must jointly infer…

- **[Jev with Foresight: Safe Language-Guided Autonomous Driving via a Language World Model](https://arxiv.org/abs/2611.05448v1)**
  - *Yansong Qu, Jiancong Chen, Samuel Labi*
  - `2026-11-03`
  - Large language models understand passengers' driving commands, but as driving agents they reason in generated text for seconds and must infer each action's consequences implicitly from the scene. We present Jev-AD, which pairs Jev, a typed decision model that answers predefined q…

- **[LIBRA: Programmatic Induction of Executable Tool Libraries](https://arxiv.org/abs/2611.05445v1)**
  - *Zekai Li, Zhenke Liu, Yonghao Li et al.*
  - `2026-11-03`
  - Large language model agents increasingly retrieve tools from large catalogs, yet most retrievers rank each tool independently by request similarity. For multi tool tasks, this recovers the goal matching tool while omitting prerequisite tools required by the workflow.We introduce…

- **[OperAItor: An Agentic Framework for Fault-Tolerant Operation of Chemical Processes](https://arxiv.org/abs/2611.05179v1)**
  - *Javal Vyas, Mehmet Mercang{ö}z*
  - `2026-11-03`
  - OperAItor, an open-source framework for developing and evaluating large language model agents for supervisory fault management in chemical processes. The framework is demonstrated on a dynamic reactor-distillation process representing isopropanol dehydrogenation, with physically…

- **[AgentAM: An AI Agent for Spatter- and Defect-Aware Process Optimization in Laser Powder Bed Fusion](https://arxiv.org/abs/2611.05171v1)**
  - *Olabode T. Ajenifujah, Amir Barati Farimani*
  - `2026-11-03`
  - Predictive models for laser powder bed fusion (LPBF) are rarely used on the shop floor because querying them requires programming and model-specific knowledge. We present AgentAM, a large language model (LLM) agent that gives process engineers natural-language access to CFD-train…

- **[Meta$^2$: Precomputing Reusable Knowledge for Online Harness Evolution in Long-Horizon Agents](https://arxiv.org/abs/2611.05139v1)**
  - *Lingzhi Yuan, Yiguang Cai, Weize Liu et al.*
  - `2026-11-03`
  - Harness optimization improves long-horizon agents by refining the prompts, tools, memory, and hooks around a frozen model. Offline methods can learn from completed trajectories, but deploy one shared harness that may overfit training tasks and cannot react to evidence revealed du…

- **[From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks?](https://arxiv.org/abs/2611.05108v1)**
  - *Jeremy Qin, Ruizhi Deng, Mohamed Osama Ahmed et al.*
  - `2026-11-03`
  - Autoresearch has shown that agents can autonomously write code, run experiments, and iteratively improve machine learning solutions. Yet most evaluations start a new agent session from scratch for each new problem, making them costly and leaving unclear whether agents can retain…

- **[LatentTriad: Pre-Action Risk Representations for Malicious Agent Skill Detection](https://arxiv.org/abs/2611.05088v1)**
  - *Zhe Yu, Yi Liu, Ying Zhang et al.*
  - `2026-11-03`
  - Large language model agents are increasingly extended with reusable skills, but untrusted skill content can induce operations outside the user's task. Detecting this contextual risk requires more than suspicious-pattern matching, while dynamic analysis incurs the cost of skill ex…

- **[Do Agentic Policies Need to Look at Every Step? Geometric Abstraction for Reasoning and Action](https://arxiv.org/abs/2611.05058v1)**
  - *Yihang Liu, Yiming Chen, Mingzhe Zheng*
  - `2026-11-03`
  - Recent multimodal language models can reason directly about robot scenes, but it is unclear whether they need to repeatedly reinterpret raw visual observations at every step of an interaction. We propose shifting routine spatial reasoning from images to text and symbols through a…

- **[ALBI: LLM-Guided Inductive Logic Programming via Iterative Generate-Test-Constrain Refineme](https://arxiv.org/abs/2611.05039v1)**
  - *Aboubaker Seddiq Benterki, Jüri Vain, Gert Kanter et al.*
  - `2026-11-03`
  - We introduce ALBI (Agent for Learning By Induction), a neuro-symbolic ILP framework that replaces the ASP-based hypothesis generator in the Learning from Failures (LFF) paradigm with a Large Language Model (LLM), while retaining SWI-Prolog as a formal verifier. ALBI implements an…

- **[GeoFaham: Domain-Specialized Multi-Agent Geospatial Analytics for Disaster Response](https://arxiv.org/abs/2611.04977v1)**
  - *Muhammad Sohail Danish, Gilles Q. Hacheme, Akram Zaytar et al.*
  - `2026-11-03`
  - Real-world geospatial decision support requires more than single-step retrieval or code generation. Disaster-response questions often involve multi-source workflows that combine spatial databases, map-derived features, satellite imagery, raster products, and reusable geospatial a…

- **[LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation](https://arxiv.org/abs/2611.04974v1)**
  - *Hong Je-Gal, Jinwoo Kim, Chanbin Yi et al.*
  - `2026-11-03`
  - We investigate the automated generation of executable robot reinforcement learning (RL) policies from natural-language task descriptions. Rather than using large language models (LLMs) as execution-time decision makers, we use them as designers that construct RL pipelines before…

- **[Artifact-to-Capability: Diagnosing Breaks in Capability Formation of Self-Evolving Agents in a Controlled Environment](https://arxiv.org/abs/2611.04952v1)**
  - *Ziqian Ban, Haoxiang Yang, Yanfei Zhang et al.*
  - `2026-11-03`
  - Self-evolving agents write interaction experience into artifacts and reuse them in later tasks. Most work supports such methods with three proxy signals: artifacts accumulate, behavior changes once they are loaded, and metrics rise. We call this signal-based evaluation. What thes…

- **[VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents](https://arxiv.org/abs/2611.04894v1)**
  - *ZhengXian Wu, Qianhao Nie, Zhuohong Chen et al.*
  - `2026-11-03`
  - Multimodal agents use web and image tools to answer questions beyond their internal knowledge. Some search tasks use images mainly to identify an initial entity, then rely on text retrieval. These tasks offer limited insight into how agents connect information across images, obje…

- **[Modelling lock-in of AI adoption through skill erosion](https://arxiv.org/abs/2611.04886v1)**
  - *Renaud Lambiotte*
  - `2026-11-03`
  - Generative AI can improve immediate performance but may erode the human skills required for future work. We study a model in which individuals tend to imitate successful peers, while their independent skills grow with practice and erode with reliance on AI. Because each agent's s…

- **[ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud](https://arxiv.org/abs/2611.04879v2)**
  - *Yutao Wu, Xiao Liu, Ming Wen et al.*
  - `2026-11-03`
  - Web agents increasingly browse, shop, and manage accounts on behalf of their users. Prior work has shown that they can be misled by adversarial content, including prompt injections and deceptive interfaces. Beyond such attacks, agents operating on the open web also encounter onli…

- **[One Assistant, Many Memories: Benchmarking Real-World Group Assistance When Recall Is Not Enough](https://arxiv.org/abs/2611.04867v1)**
  - *Zhanghao Hu, Linhai Zhang, Qian Zhao et al.*
  - `2026-11-03`
  - The value of memory lies not only in recall but in using it to provide appropriate assistance. Recent benchmarks test memory use in personalisation and agentic tasks, but seldom evaluate assistance without fixed answers or integration across multiple participants. Group chats mak…

- **[Found by Search, Broken by a Shortcut: Transfer and Tampering of Searched Intrinsic Rewards](https://arxiv.org/abs/2611.04838v1)**
  - *Chase J. Metoyer*
  - `2026-11-03`
  - Can a search over innate drives find intrinsic rewards that help a reinforcement-learning agent learn, transfer to a task it never saw, and resist an exploit that was absent during the search? Each candidate reward combines four generic events (a new view, a pickup, a drop and a…

- **[HTCE: Homeomorphism-inspired Topological Cross-Scene Experience Canonicalization and Reuse for Object Navigation](https://arxiv.org/abs/2611.04836v1)**
  - *Xiaoran Xu, Yupeng Wu, Tianyu Xue et al.*
  - `2026-11-03`
  - As embodied agents perform object-goal navigation across residential environments, they accumulate successful experiences whose semantic structure recurs across scenes even when geometric trajectories do not. Reusing such experience is challenging because differences in region na…

- **[AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests](https://arxiv.org/abs/2611.04813v2)**
  - *Shu Zhou, Ziyang He, Yuxin Rao et al.*
  - `2026-11-03`
  - Financial agents are becoming an important class of real-world AI systems. Financial tasks vary widely in type and difficulty, and many are open-ended with no ground-truth answers. However, existing benchmarks neither capture this breadth and open-endedness nor separate grounding…

- **[Asymptotic Optimality of $cμ$-Rule for LLM Inference Scheduling under Memory Constraint](https://arxiv.org/abs/2611.04807v1)**
  - *Zhenghao Li, Shengbo Wang, Nian Si*
  - `2026-11-03`
  - Large language model (LLM) inference, the process by which a pre-trained model receives an input prompt and generates output tokens sequentially, has become increasingly important with the widespread deployment of LLM-based applications. As inference workloads continue to scale,…

- **[Where Is the Truth When AI Agents Disagree? Dependence-Aware Belief Propagation for Unsupervised Truth Discovery (Extended Version)](https://arxiv.org/abs/2611.04805v1)**
  - *Laure Berti-Equille*
  - `2026-11-03`
  - LLM agents often give conflicting answers to the same question, and many deployed agents are variants of one base model, so their errors are correlated. We study truth discovery among such agents: inferring the true answer and each agent's reliability without labels. Classical tr…

- **[TactiNavi: Serving and Revising an LLM Game Coach with Explicit Strategy Conditions](https://arxiv.org/abs/2611.04772v1)**
  - *Qi Liu, Xiaoyang Yuan, Zhuomeng Zhang et al.*
  - `2026-11-03`
  - A deployed LLM coaching agent answers requests whose correct response depends on player state and game version, so advice that is right for one player can be wrong for the next. We describe TactiNavi, the serving system behind the LLM coach of a commercial open-world game, which…

- **[Can Network Models of Science Do Without Pluralist Agents?](https://arxiv.org/abs/2611.04590v1)**
  - *Jonas Hallgren, David Hyland, Mahault Albarracin*
  - `2026-11-03`
  - Science is a process of useful models being proven wrong time and again, but despite its many flaws, it somehow works. Why is this? Paul Feyerabend argued that it works because people dare to hold and defend incompatible rival theories against the accepted one, since a theory's f…

- **[Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems](https://arxiv.org/abs/2611.04556v1)**
  - *Chandler Smith, Qi Guo, Cecilia Elena Tilli et al.*
  - `2026-11-03`
  - The deployment of AI agents in multi-agent settings enables inter-agent influence, whereby agents can strategically steer each other's behaviour towards an intended outcome. Such capabilities pose novel risks, as malicious agents could direct others towards harmful actions. In th…

- **[Learnings and Pitfalls from AI-Assisted A/B Experimentation at Scale](https://arxiv.org/abs/2611.04515v1)**
  - *Brett Daley, Ilya Gorbachev, Anubhav Natani et al.*
  - `2026-11-03`
  - A/B testing underpins product decisions by providing trustworthy, reproducible quantification of proposed changes' effects. Growing large language model (LLM) capabilities have motivated efforts to automate experimentation workflows. Yet LLMs are nondeterministic and prone to hal…

- **[Signals: Continuous Diagnostics of AI Agents](https://arxiv.org/abs/2611.04507v2)**
  - *Amey Rambatla, Vatsal Goel, Sagar Gaur et al.*
  - `2026-11-03`
  - AI agents can make incorrect decisions or waste resources even when their tools and infrastructure work normally. Their nondeterministic behavior makes these problems difficult to reproduce and diagnose. We developed Signals to identify such problems from agentic traces and sugge…

- **[CogniLife: Continuous Cognitive Distillation for Deployed Multi-Expert Agent Marketplaces](https://arxiv.org/abs/2611.04483v1)**
  - *Xuwei Tan, Jingchun Huang, Ming Cai et al.*
  - `2026-11-03`
  - Multi-expert agent marketplaces -- where creators publish domain-specific AI experts for end users to consult -- are an emerging deployment pattern for language technology. A published expert can receive many requests yet little evidence about its creator, who remains active else…

- **[Goal-Driven Autonomous Optical Experimentation via a Self-Recursive Hardware-Software Harness](https://arxiv.org/abs/2611.04481v1)**
  - *Tianxing Zhu, Huacheng Lu, Ming Liu et al.*
  - `2026-11-03`
  - We propose goal-driven self-recursive optical research in which agents use physical evidence to revise the hardware, software, models, and protocols used to pursue a scientific goal. The framework can be instantiated with different stimulus systems and measurement devices. We for…

- **[Treating the Symptom, Missing the Cause: Anatomy of a Scientific Reasoning Failure](https://arxiv.org/abs/2611.04473v1)**
  - *Anna Gogleva, Thomas Charman, Martin Balla et al.*
  - `2026-11-03`
  - Scientific agents can find interventions that work without understanding why they do. We study this failure mode in controlled synthetic regulatory systems, where agents must experimentally identify a hidden fault and rescue the resulting phenotype. Across seven LLMs, every model…

- **[From Watching to Steering: Enabling Human-Coding Agent Collaboration through Execution Traces](https://arxiv.org/abs/2611.04466v1)**
  - *Xiaoke Yan, Jiaying Lei, Danqing Shi et al.*
  - `2026-11-03`
  - Recent advances in large language models (LLMs) have enabled coding agents to autonomously perform complex software development tasks, yet their long-running execution remains difficult for users to inspect, understand, and steer. We present Vibetrace, an interactive trace visual…

- **[Silent Instrument Errors Reorder Agent Leaderboards](https://arxiv.org/abs/2611.04399v1)**
  - *Yangze Liu*
  - `2026-11-03`
  - On a public agent leaderboard, a general-purpose agent trails a scaffold built for an airline customer-service benchmark by 13 points on the tasks that touch its database, and a reader could conclude that generality costs accuracy. The gap comes from the grader. The general agent…

- **[Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents](https://arxiv.org/abs/2611.04393v1)**
  - *Ilan Zendel, Matan Levy, Stav Cohen et al.*
  - `2026-11-03`
  - LLM agents increasingly act on information retrieved from public sources they treat as credible, which turns a manipulated recommendation into a transaction, a dependency, or a decision with physical consequences. The security literature models this threat as instruction injectio…

- **[CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion](https://arxiv.org/abs/2611.04356v1)**
  - *Li Zheng, Simin Chen*
  - `2026-11-03`
  - Finite element method (FEM) solvers are foundational to scientific and engineering simulation, yet their susceptibility to \emph{efficiency attacks} remains largely unexplored. An adversary can craft syntactically valid and runnable FEM programs that complete successfully while f…

- **[ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems](https://arxiv.org/abs/2611.04321v1)**
  - *Maisha Maliha, Vishal Pramanik, Sumit Kumar Jha*
  - `2026-11-03`
  - Multi-agent LLM systems assign different responsibilities to different agents: one plans, another retrieves evidence, another verifies, another executes. This division of labor is only meaningful if each agent stays within the functions it is authorized to perform. Over many turn…

- **[Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI](https://arxiv.org/abs/2611.04315v1)**
  - *Vishal Pramanik, Maisha Maliha, Susmit Jha et al.*
  - `2026-11-03`
  - Long-horizon multi-agent systems suffer from three tightly coupled failures: task drift, role drift, and state staleness. We test the hypothesis that these share a common representational cause: agent hidden states move away from the directions encoding the active task, assigned…

- **[OSGR: Observation-Support Graph Reasoning for Earth Observation Question Answering](https://arxiv.org/abs/2611.04301v1)**
  - *Dazhou Yu, Zerong Wang, Riyang Bao et al.*
  - `2026-11-03`
  - Answering geographic queries over Earth observation (EO) archives requires solving a joint retrieval-and-derivation problem under strict spatiotemporal constraints. Existing LLM agents fail to ground observation items or suffer from search-space explosion. We propose OSGR, a two-…

- **[When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation](https://arxiv.org/abs/2611.04289v1)**
  - *Qinghua Mao, Xi Lin, Yuxin Qi et al.*
  - `2026-11-03`
  - Retrieval-augmented Web applications increasingly employ multi-agent debate (MAD) to aggregate conflicting, noisy, and heterogeneous information, yet deliberation is fundamentally a social process susceptible to interpersonal dynamics. When retrieved Web sources contain latent ha…

- **[Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training](https://arxiv.org/abs/2611.04277v1)**
  - *Kangning Zhang, Wenxiang Jiao, Bowen Fang et al.*
  - `2026-11-03`
  - Harness evolution from a common base exhibits Locality, Complementarity, and Nonstationarity: variants repair different failures, and their utility changes as the policy learns. Rather than seeking a universally superior harness, we introduce Harness-S to selectively rescue failu…

- **[AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds](https://arxiv.org/abs/2611.04241v1)**
  - *Kailing Li, Ruoxuan Zhang, Zheyuan Zhou et al.*
  - `2026-11-03`
  - Video games provide a practical setting for collecting vision-language-action (VLA) data, whose acquisition in physical environments is costly. Existing datasets, however, remain limited by restricted game coverage, sparse language supervision, or temporal hierarchies that do not…

- **[DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?](https://arxiv.org/abs/2611.04228v1)**
  - *Yang Chen, Bin Wen, Danyang Peng et al.*
  - `2026-11-03`
  - Recent multimodal agents have shown promising progress in embodied planning and web interaction. However, existing evaluations often rely on simplified tasks with limited combinatorial structure, leaving it unclear whether current agents can robustly integrate perception and reas…

- **[DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution](https://arxiv.org/abs/2611.04226v1)**
  - *Renkai Yi, Yuwei Wu, Haoyu Zhang et al.*
  - `2026-11-03`
  - Disturbances can invalidate the conditions required by a robot's next action even when much of its task program remains useful. A recovery system must therefore choose a response suited to the current state. We present DiMuRe (diagnosis-guided multilevel recovery), a framework fo…

- **[IntentGEO: Intent-aware Generative Engine Optimization for Recommendation](https://arxiv.org/abs/2611.04225v1)**
  - *Runlin Lei, Shiqi Zhang, Xiaokui Xiao et al.*
  - `2026-11-03`
  - Large language models (LLMs) increasingly shape recommendations across chatbots, e-commerce, and user-generated content (UGC) platforms, creating demand for Generative Engine Optimization (GEO) to improve item visibility in generated responses. Existing GEO studies are mainly con…

- **[Toward User-Centered Agentic Recommendation: When Does Platform Competition Benefit Users?](https://arxiv.org/abs/2611.04203v1)**
  - *Kehan Zheng, Deyao Hong, Qian Li et al.*
  - `2026-11-03`
  - Conventional recommender systems operate within platform-specific catalogs, limiting access to potentially valuable resources across platforms. We propose user-centered agentic recommendation, a paradigm in which user agents compare recommendations from competing platform agents,…

- **[DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation](https://arxiv.org/abs/2611.04196v1)**
  - *Yuxuan Wang, Dadi Guo, Weijie Guo et al.*
  - `2026-11-03`
  - Frontier LLM agents can turn known vulnerabilities into working exploits, but are costly and often access-restricted due to their potential for malicious use. Open-weight models offer a more accessible alternative, but struggle to maintain progress across long exploitation chains…

- **[Agentic Path Maps: Exposing an Agent's Traversal Through the Garden of Forking Paths](https://arxiv.org/abs/2611.04183v1)**
  - *Madeleine Grunde-McLaughlin, Hafsah Usman, Daniel Mitroshkov et al.*
  - `2026-11-03`
  - When an AI agent executes an underspecified task, it embeds choices that may contradict unarticulated user context and preferences. However, interrupting the user for clarification on all such decisions is untenable. How might agents communicate impactful, but unexplored, paths t…

- **[When the Consumer Is an Agent: Execution-Grounded Service-Level Agreements](https://arxiv.org/abs/2611.04182v1)**
  - *Michal Orzechowski, Renata G. Slota, Jacek Kitowski*
  - `2026-11-03`
  - Large language model (LLM) agents increasingly act as service consumers. They select operations and report whether a task is complete. In an asynchronous distributed service, an accepted call or immediate state read does not establish that the required state became observable by…

- **[Validation-Gated ML Pipeline Synthesis with Expert-Grounded Self-Evolving Skills](https://arxiv.org/abs/2611.04180v1)**
  - *Zixiao Zhao, Jing Sun, Zhe Hou et al.*
  - `2026-11-03`
  - Recent advances in large language models have enabled agentic systems that automate machine learning pipeline construction from minimal user input. However, existing agentic AutoML methods either depend on rigid templates that limit adaptability, target narrow task domains, or re…

- **[Interpretable Early Termination of Web Navigation Agents via Closed Sequential Pattern Mining](https://arxiv.org/abs/2611.04142v1)**
  - *Sergio Talavera, Magdalini Eirinaki*
  - `2026-11-03`
  - Web navigation agents built on open-weight language models fail often and fail late, with most of the tokens spent after the trajectory has become unrecoverable. Recent work has shown that early termination is a viable cost-reduction strategy, but existing approaches produce opaq…

- **[GlucoAgent: Personalized Glucose Forecasting from Multimodal Personal Context](https://arxiv.org/abs/2611.04126v1)**
  - *Xingzhi Sun, Hyo Jin Kim, Zhiyuan Wang et al.*
  - `2026-11-03`
  - Continuous glucose monitors, smartwatches, meal logs, and health profiles form a rich multimodal personal context that can significantly enhance glucose forecasting. However, existing methods struggle to effectively utilize these signals to improve glucose prediction because the…

- **[The Agent Board: Kanban for Machines; Durable Coordination for Agents That Outlive the Conversation](https://arxiv.org/abs/2611.04100v1)**
  - *Tyler Hunt, Donald Nguyen, Gurbinder Gill*
  - `2026-11-03`
  - Harnesses for large language models have converged on a single-threaded shape: one agent, one history, one machine, one sitting. That shape fails work that spans many agents, outlives any one model call, or waits on systems that are not agents. We describe the Agent Board, the co…

- **[RIDGE: State-Conditioned Reward Blending for Behavioral Coverage in Deep RL Game Agents](https://arxiv.org/abs/2611.05601v1)**
  - *AL Muqshith Mohammed Shifan, Kevin Christopher Chua, Ali Neshati et al.*
  - `2026-11-03`
  - A deep RL agent trained on a fixed persona reward plays one way: an Explorer keeps exploring while starving, a Survivor hoards on an empty map. Since each persona fixes its own reward, automated playtesting trains N agents for N styles. Changing reward composition mid-episode run…

- **[Learning vs. Optimizing Players in Budgeted Games](https://arxiv.org/abs/2611.05580v1)**
  - *Giannis Fikioris, Balasubramanian Sivan, Éva Tardos*
  - `2026-11-03`
  - We study repeated general games over $T$ rounds between a utility-maximizing optimizer and a learning agent, where budget constraints couple the players' decisions across rounds. Without budgets, low swap regret simultaneously guarantees the learner sublinear regret and caps the…

- **[Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning](https://arxiv.org/abs/2611.05266v2)**
  - *Kevin Frans, Alexander M Rush, Sergey Levine et al.*
  - `2026-11-03`
  - Naive on-policy RL is often bottlenecked by the capabilities of the base model --- insufficient coverage can result in an inability to learn from certain rewards. At the same time, rewards in modern post-training systems often come from rich textual sources, e.g. judge models wit…

- **[Distributed Linear Bandits for Freshness-Aware Preprocessing in MEC-Enabled Digital Twin Networks](https://arxiv.org/abs/2611.05115v1)**
  - *Mariam Yahya, Setareh Maghsudi*
  - `2026-11-03`
  - Digital twins (DTs) require timely updates from Internet of Things (IoT) devices to accurately represent the state of the corresponding physical systems, but transmitting large data volumes can compromise freshness. Moreover, different task classes have distinct computational dem…

- **[Training Specialist LLMs on Your Phone: Forward-Only Optimization via Block-Spectral Coordinates](https://arxiv.org/abs/2611.04797v1)**
  - *Liyan Tan, Yequan Zhao, Ziyue Liu et al.*
  - `2026-11-03`
  - Large language models (LLMs) on personal devices keep user data local, but limited memory restricts their general capability. Since most user-specific tasks do not require the breadth of frontier models, a practical solution is to adapt a shared on-device model into lightweight s…

- **[Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards](https://arxiv.org/abs/2611.04774v1)**
  - *Yasaman Zolfimoselo, Nikolas Geroliminis, Maryam Kamgarpour*
  - `2026-11-03`
  - We study cooperative multi-agent reinforcement learning with decoupled dynamics and a monotone submodular reward function over joint trajectories. Due to the non-additive reward, an optimal policy may depend on the history of all agents. This dependence makes exact optimization e…

- **[SKILL2STEER: One-Pass Hypernetwork for Mapping Natural-Language Skills to Low-Rank Post-Block Activation Shifts](https://arxiv.org/abs/2611.04497v1)**
  - *Ran Li, Lei Chen*
  - `2026-11-03`
  - Compiling a natural-language agent skill into model parameters removes the skill text from the prompt and leaves behind a small artifact that can be distributed and reused. Existing methods differ in where they inject the compiled quantity, and all of them assume that the artifac…

- **[ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends](https://arxiv.org/abs/2611.04104v1)**
  - *Shengjun Kris Dong, Dima Nikiforov, Sahil Modi et al.*
  - `2026-11-03`
  - Optimizing accelerator code across hardware architectures is difficult. ML compilers search predefined spaces of schedules and micro-kernels, while LLM-guided optimization can explore alternative algorithms, operator decompositions, and hardware-specific techniques. However, exis…

- **[Prospective Memory for Proactive LLM Agents](https://arxiv.org/abs/2611.05731v1)**
  - *Yuanchen Bei, Zhining Liu, Tianxin Wei et al.*
  - `2026-11-03`
  - Most memory systems for LLM agents are retrospective, preserving and retrieving past information to inform current decisions. Proactive agents, however, also require prospective memory: retaining future-directed intentions and realizing them when appropriate opportunities arise,…

- **[The Male Abstraction Bias in Internet Culture and Large Language Models](https://arxiv.org/abs/2611.05730v1)**
  - *Douglas Guilbeault, Bhargav Srinivasa Desikan*
  - `2026-11-03`
  - Two foundational aspects of human cognition, abstractness and gender, are typically examined as separable. Here, we find they are systematically linked throughout the entire space of concepts spanning single (N = 40,000) and multi-word expressions (N = 67,000): across billions of…

- **[Cognitive Bias Signatures in Search-Equipped LLM Agents: A Stage-Resolved Analysis](https://arxiv.org/abs/2611.05720v1)**
  - *Yanru Xiao, Yingwei Yu*
  - `2026-11-03`
  - Search can help LLM agents correct mistakes, but their starting conditions may shape which evidence they find and use. Drawing on cognitive-bias paradigms, we develop a controlled search harness to examine result order, records of prior work, and initial hypotheses while holding…

- **[MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution](https://arxiv.org/abs/2611.05313v1)**
  - *Dian Jin, Jinluan Yang, Kairong Han et al.*
  - `2026-11-03`
  - Skill memories encode past experiences as textual prompts to improve reinforcement learning (RL) for self-evolving agents. Complementing RL, On-Policy Self-Distillation (OPSD) provides dense, fine-grained supervision to internalize knowledge from skill-guided trajectories and acc…

- **[ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents](https://arxiv.org/abs/2611.05036v1)**
  - *Guanting Dong, Zhichao Sun, Xinyu Yang et al.*
  - `2026-11-03`
  - Large language models are deployed as long-horizon agents that compose diverse tools across MCP services into executable workflows. Existing MCP environment-scaling methods are data-centric: they first synthesize a database and scenario, then derive tools and tasks from them. As…

- **[CardioVascBench:Prioritized Diagnosis Generation from Real-World Chinese Cardiovascular Records](https://arxiv.org/abs/2611.04687v1)**
  - *Minghao Kong, Muyao Chen, Jianhao Wu et al.*
  - `2026-11-03`
  - Identifying the primary diagnosis alone does not fully characterize a model's diagnosis-generation performance. We introduce CardioVascBench, a retrospective benchmark for prioritized diagnosis generation from real-world Chinese cardiovascular inpatient records. It contains 3,262…

- **[MIMIC-Note-Extract: A Large-Scale Structured Dataset Extracted from MIMIC-IV-Note Discharge Summaries](https://arxiv.org/abs/2611.04685v1)**
  - *Kristian Schwethelm, Jonas Kuntzer, Conrad Ketzer et al.*
  - `2026-11-03`
  - MIMIC is one of the most widely used public hospital datasets for machine learning on electronic health records, yet clinically important information, such as past medical history, allergies, and diagnostic findings, remains confined to free-text discharge summaries. Studies requ…

- **[Mechanical Engineering Skills: An Open Library of Agent Skills for Design, Analysis and Manufacturing](https://arxiv.org/abs/2611.05758v1)**
  - *Achuth Chandrasekhar, Jesse Barkley, Peter Pak et al.*
  - `2026-11-03`
  - Mechanical engineers use specialized tools for CAD, simulation, manufacturing and research, each with a distinct interface and learning curve. We present Mechanical Engineering Skills, an open library of 33 agent skills that makes these capabilities accessible through a single te…

- **[Same Method, Different Task: What the Bitter Lesson Does Not License in Social Simulation](https://arxiv.org/abs/2611.05717v1)**
  - *Justin Downes, Robby Milletich, Newel Hirst*
  - `2026-11-03`
  - The bitter lesson holds that general methods leveraging computation defeat hand-encoded domain knowledge. We argue it carries a condition its popular reading omits: in every case Sutton cites, the general method was scaled against the same task the domain engineering was solving.…

- **[Haptic Shared Control for Multi-Robot Systems](https://arxiv.org/abs/2611.05027v1)**
  - *Maxime Bernard*
  - `2026-11-03`
  - Multi-agent systems offer significant advantages in terms of flexibility and redundancy, enabling the efficient distribution of complex tasks among multiple robots. However, their deployment requires advanced control strategies to ensure optimal cooperation between autonomous age…

- **[AttriSwarm: Orchestrating Agent Swarms for Cross-Page Visual Attribution](https://arxiv.org/abs/2611.04504v1)**
  - *Suifeng Zhao, Zida Liu, Lei Sun et al.*
  - `2026-11-03`
  - Multimodal large language models (MLLMs) increasingly address knowledge-intensive tasks by integrating evidence scattered across multiple document pages into a final answer. Because such answers are synthesized from many pages, the link between the answer and its supporting visua…

- **[Distributed Marginal Return: A Communication-Efficient Algorithm for Multi-Agent Weapon Target Assignment](https://arxiv.org/abs/2611.04370v1)**
  - *Kamal Mammadov, Glen Pearce, Helen Krause et al.*
  - `2026-11-03`
  - The Weapon-Target Assignment (WTA) problem in distributed multi-agent systems is challenged by limited situational awareness and communication constraints. Existing distributed methods, such as auction-consensus algorithms, typically assume task-value independence, a simplificati…

- **[When Is Fresh AI Stock Analysis Worth It? Allocating a Limited Research Budget Across Price Updates, Deep Forecast Refreshes, and Editorial Reviews of Top Stock Picks](https://arxiv.org/abs/2611.04348v2)**
  - *Russlan Ramdowar*
  - `2026-11-03`
  - When is another AI research run worth more than keeping that money invested? Using 8,120 iPulse AI reports that consumed nearly 100 million output and reasoning tokens on the same 203 stocks across four production batches, we compare repricing old targets (with and without shock…

- **[Sketchpad: certified exact arithmetic with a small vision-language model](https://arxiv.org/abs/2611.04434v1)**
  - *Mostafa 'Neo' Mohsenvand*
  - `2026-11-03`
  - Language models are accurate on most long-arithmetic problems, but their accuracy is estimated on samples and carries no guarantee for an unseen input; tool use is exact but moves the computation outside the network. We show that exactness at all input lengths becomes a finite, c…

- **[ScienceVision: Can AI Observe and Reason Like a Scientist?](https://arxiv.org/abs/2611.04087v1)**
  - *Tianyi Ma, Jing Gu, Haozhe Zhao et al.*
  - `2026-11-02`
  - Scientific discovery builds on accurate observations interpreted through domain knowledge and reasoning. For scientific 3D data, this requires understanding structures and spatial relationships, from protein contacts to anatomical organization. Existing multimodal benchmarks larg…

- **[Exploit or conform? How norm utility prompting changes the way LLMs use community beliefs](https://arxiv.org/abs/2611.04048v1)**
  - *Leon Klingborg, Theodor Cimpeanu, Alexander J. Stewart*
  - `2026-11-02`
  - Large Language Models (LLMs) serve both as tools for aiding human decision-making in everyday life and as models of human agents in experimental simulation studies. Alignment on prototypical social decisions -- such as whether to cooperate on a collective action -- therefore has…

- **[ROCm InferaSim: Cut LLM Serving Trial Costs and Deploy the Best Configuration](https://arxiv.org/abs/2611.04032v1)**
  - *Anshu Raina, Yao Fu, Zhang Jiejing et al.*
  - `2026-11-02`
  - Serving an LLM efficiently depends on the engine, how the model is split across GPUs, precision, scheduler settings, speculative decoding, KV-cache management, and prefill-decode disaggregation. The best configuration depends on the model, hardware, workload, and objective. Opera…

- **[Characterizing Adversarial GEO via Implicit Brand Injection](https://arxiv.org/abs/2611.04005v1)**
  - *Shobhnik Kriplani, Haohan Wang*
  - `2026-11-02`
  - Generative search engines increasingly shape how users discover products, services, and commercial entities by generating answers from retrieved web content. This creates an opportunity to influence which brands appear in these answers by modifying the content available to the re…

- **[WASP-Mem: Let Agent Organize Procedural Memory. Human Spend Effort on Diagnosis](https://arxiv.org/abs/2611.04003v1)**
  - *Peizhi Niu, Ge Shi, Vaibhav Gorde et al.*
  - `2026-11-02`
  - LLM agents struggle to automate complex enterprise procedures because static, pre-built harness cannot capture proprietary policies, undocumented behaviors, or state-dependent recovery paths that surface only during execution. Procedural memory accrued from agent experience offer…

- **[Measure Before You Repair: An Explainable Agent for Blind Restoration of Multi-Artifact 3-D MRI](https://arxiv.org/abs/2611.03996v1)**
  - *Necati Sefercioglu, Mehmet Ozan Unal, Metin Ertas et al.*
  - `2026-11-02`
  - A brain MRI scan can carry an unknown mix of artifacts, so restoration has to be blind, yet most deep-learning methods are built to correct one known artifact. We present Dx-Rx, an agent in which a multimodal large language model (MLLM) measures suspected artifacts before it repa…

- **[When Music Needs Meaning: Semantic Communication as a Transformative Enabler for the Musical Metaverse](https://arxiv.org/abs/2611.03995v1)**
  - *Ali Al Housseini, Jaime Llorca, Cristina Rottondi et al.*
  - `2026-11-02`
  - The Musical Metaverse (MM) enables geographically distributed musicians, audiences, sound engineers, and AI agents to interact through synchronized audio, visual, kinematic, and haptic streams, imposing latency, synchronization, bandwidth, and scalability requirements that are di…

- **[A Guideline-Grounded Multi-Agent Framework for Personalized Exercise Prescription from Clinical and Wearable Data](https://arxiv.org/abs/2611.03983v1)**
  - *Xintong Li, Yufen Lin, Yuhua Wu et al.*
  - `2026-11-02`
  - Translating population-level exercise guidance into individualized prescriptions requires integrating clinical and wearable data, including diagnoses, medications, functional limitations, and baseline activity, with condition-specific recommendations, a process difficult to scale…

- **[SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use](https://arxiv.org/abs/2611.03982v1)**
  - *Rongzhe Wei, Ge Shi, Min Cheng et al.*
  - `2026-11-02`
  - Enterprises increasingly want LLM agents to automate standard operating procedures over their software stacks -- mapping each step of a procedure to the right call among thousands of internal APIs, without hand-authored step-to-API mappings. The core difficulty is API selection a…

- **[Measuring Model-Specific Alignment Drift in LLM-Based Opinion Dynamics](https://arxiv.org/abs/2611.03980v1)**
  - *Nataša Djurdjevac Conrad, Sebastian Pokutta, Christof Schütte*
  - `2026-11-02`
  - Large language model (LLM) agents are increasingly used as synthetic participants in opinion-dynamics experiments, often assuming that an agent's behaviour is fully determined by its prompt. We test this assumption with a framework in which LLM agents discuss a contested policy i…

- **[What Is This Memory Useful For? Measuring Task-Conditioned Utility in Long-Term Agent Memory](https://arxiv.org/abs/2611.03930v1)**
  - *Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Feng Yan et al.*
  - `2026-11-02`
  - A stored experience may answer one future question and offer little help with another. We measure this task-conditioned utility rather than assigning each memory a single importance score. A task-blind writer stores a memory without seeing the later task; a frozen reader then ans…

- **[ProofPaths: An AI Agent Framework for Assessing Student Reasoning](https://arxiv.org/abs/2611.03882v1)**
  - *Mohsen Hariri, Vipin Chaudhary*
  - `2026-11-02`
  - Students can use large language models to complete assignments, but a correct solution does not establish whether they understand the reasoning behind it. Individualized interviews can probe that understanding but require recurring staff effort. We introduce ProofPaths, an AI age…

- **[Performance, Scalability and Maintenance: An Experimental Study of RPA vs. Autonomous Agents in the Healthcare Domain](https://arxiv.org/abs/2611.03853v1)**
  - *Daniel Schulz, Pedro Cabral Buchaim, Bernardo Soares et al.*
  - `2026-11-02`
  - Healthcare information systems are fragmented, and retrieving data from legacy web portals is a recurrent need. Robotic Process Automation (RPA) is deterministic but sensitive to interface changes, whereas autonomous agents based on large language models (Agent Process Automation…

- **[El Agente Fármaco: A Scalable AI Scientist for Drug Discovery](https://arxiv.org/abs/2611.03832v1)**
  - *Marcel Müller, Mohammad Ghazi Vakili, Yoshihiro Ogura et al.*
  - `2026-11-02`
  - Computational drug discovery offers a growing range of tools for proposing and evaluating molecules, but combining them and deciding what to do next still requires substantial expert effort. Here, we introduce El Agente Fármaco, an AI scientist that uses modern large language mod…

- **[Rethinking Next-Visit Diagnosis Prediction Beyond Aggregate Metrics: Retrieval--Memory Multi-Agent Adjudication](https://arxiv.org/abs/2611.03826v1)**
  - *Heejoon Koo*
  - `2026-11-02`
  - Next-visit diagnosis prediction forecasts the diagnoses documented at a patient's next encounter, turning retrospective electronic health records into prospective clinical prediction. However, conventional aggregate evaluation obscures its multifaceted nature: distributionally, m…

- **[WebHarbor: Docking Real Websites for Evolving GUI Agent Environments](https://arxiv.org/abs/2611.03634v1)**
  - *Zhaoyang Wang, Qianhui Wu, Boyu Gou et al.*
  - `2026-11-02`
  - GUI web agents require realistic and interactive environments that remain stable during both evaluation and training. Live website evaluation suffers from changing content, access restrictions, and limited coverage of authenticated workflows, while existing synthetic environments…

- **[Strategist: Evolving Reasoning with Agents](https://arxiv.org/abs/2611.03618v1)**
  - *Taiming Lu, Qi Xu, Zhigang Hua et al.*
  - `2026-11-02`
  - A model is only half of an AI agent system. The other half is the inference strategy: the reasoning procedure that turns model calls into a response. Today that second half is written by hand, and the experience of building one strategy never carries to the next. We introduce Str…

- **[DiabAgent: Toward Agentic Physiological Control](https://arxiv.org/abs/2611.03601v1)**
  - *Chengxi Li, Shaoxuan Li, Deyao Hong et al.*
  - `2026-11-02`
  - As pretraining scales, medical language models have advanced rapidly in clinical question answering. Their ability to achieve effective physiological control through sustained intervention still lacks systematic quantitative evaluation. Type 1 diabetes provides a concrete setting…

- **[Four Bridges: Measuring Deception Propensity in a Multi-Agent Game](https://arxiv.org/abs/2611.03600v1)**
  - *Raphael Casey, Michael Simeone, Alberto Tosato et al.*
  - `2026-11-02`
  - AI agents are increasingly deployed in settings where they interact and coordinate with other agents, yet honesty is mostly measured in single-turn, single-agent benchmarks that pressure the model to deceive. We study deception that emerges in multi-agent interaction without any…

- **[Spacetime Emergence in the Memory of a Learning Agent](https://arxiv.org/abs/2611.03596v1)**
  - *Philip A. LeMaitre, T. Rick Perche*
  - `2026-11-02`
  - We show that the causal structure of spacetime can emerge within the memory of a learning agent performing a quantum information task. We train a model-based reinforcement-learning agent to maximize the quantum mutual information between localized quantum probes interacting with…

- **[FedReady: Bounded Agents for Federation Formation](https://arxiv.org/abs/2611.03586v1)**
  - *Ziyue Xu, Holger R. Roth, Chester Chen et al.*
  - `2026-11-02`
  - Federated learning (FL) runtimes standardize aggregation and deployment, but each new study still requires federation formation: selecting task-eligible sites and preparing their local data and task code for federated training or analysis. This preparation recurs when the target…

- **[Can LLM Agents Be Forward-Deployed Engineers? Requirement Discovery and Delivery for Enterprise Text-to-SQL](https://arxiv.org/abs/2611.03551v1)**
  - *Marianne Menglin Liu, Rongguang Wang, Zheng Wang et al.*
  - `2026-11-02`
  - LLM coding agents can increasingly automate model post-training, but whether they can act as forward-deployed engineer (FDE) agents, discovering customer requirements and turning them into deployment decisions, remains unclear. We study this on a real enterprise text-to-SQL engag…

- **[An Agentic Framework for Automated Power System Studies and Grid Connection Assessment](https://arxiv.org/abs/2611.03534v1)**
  - *MaoXun Huang, Kshitij Kapoor, Eli Louise*
  - `2026-11-02`
  - Connecting new generation and demand to the grid depends on two scarce skills: checking applications against a large, changing body of regulation, and running the network studies that decide where and how a project connects. We present Grid Agents, an AI system that brings both t…

- **[VIAS: Value-Isolating Activation Steering for Multi-Value Alignment and Compliance for Organisations](https://arxiv.org/abs/2611.03518v1)**
  - *Avni Mittal, Avinash Anand, Dikshant Kukreja et al.*
  - `2026-11-02`
  - Organisations increasingly deploy large language model agents that must follow organisational values. We check whether activation steering, which adds vectors to a model's internal activations during generation without changing its weights, can improve compliance beyond prompting…

- **[Harder Than the Task: From Technical to Organizational Difficulty in AI Benchmarking](https://arxiv.org/abs/2611.03494v1)**
  - *Victor Barres, Aden Barton, Nicolai J. Foss et al.*
  - `2026-11-02`
  - AI benchmarks have made remarkable progress in measuring the ability of AI systems to perform increasingly demanding cognitive and technical tasks. Yet, many of these benchmarks treat technical tasks as the unit of analysis, while much economically valuable work takes place withi…

- **[RuntimeTickets: Source-Grounded Security Obligations for Agent Skills](https://arxiv.org/abs/2611.03772v1)**
  - *Kuiyi Gao, Xue Liu, Bowei He*
  - `2026-11-02`
  - Third-party Agent Skills extend what an autonomous agent can do, but a malicious Skill can hide data exposure or output manipulation inside a legitimate workflow. Neither reading a Skill's description nor granting it tool permissions tells whether its execution meets the user's s…

- **[Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM for Investigative Analysis](https://arxiv.org/abs/2611.03434v1)**
  - *Shai Nahum Gefen, Vered Chassida, Dmitry Basin et al.*
  - `2026-11-02`
  - Government intelligence teams need LLM agents that can analyze large, messy evidence collections, but security and cost constraints often rule out hosted frontier models and broad, hard-to-audit tool surfaces. We report CLEO: Constrained Loop for Environment Optimization, a metho…

- **[DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412v2)**
  - *Yumou Liu, Mingju Chen, Zhoufutu Wen et al.*
  - `2026-11-02`
  - LLM agents are judged by what they deliver, and in professional work what gets delivered is a project, not a task. A project pays off only if the whole package holds, and one weak part can limit the value of the rest. Yet existing benchmarks mostly test agents on one task at a ti…

- **[From Reactive to Agentic Resilience: Multi-Timescale AI-RAN Orchestration Under Signaling Storms](https://arxiv.org/abs/2611.03406v1)**
  - *Sotiris Chatzimiltis, Mahdi Boloursaz Mashhadi, Mohammad Shojafar et al.*
  - `2026-11-02`
  - Next-generation open radio access network (Open RAN) and AI-RAN deployments turn the RAN into a disaggregated, compute-aware platform whose service continuity depends on many control loops acting at different timescales. Resilience in this setting is best seen as a lifecycle span…

- **[Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents](https://arxiv.org/abs/2611.03384v1)**
  - *Eric Benhamou, Jean-Jacques Ohana, Beatrice Guez et al.*
  - `2026-11-02`
  - Financial research agents can generate and monitor trading rules faster than a human can document the resulting selection process. Candidates appear at data-dependent times, weak rules are abandoned, and promising ones are watched until they cross a reporting threshold. We introd…

- **[Characterizing When Language Models Take Harmful Actions to Protect Their Assigned Goals](https://arxiv.org/abs/2611.03374v1)**
  - *Brandon Jaipersaud, Elliot Creager*
  - `2026-11-02`
  - Recent language model (LM) safety failures have largely been studied as disparate phenomena. In agentic misalignment, a model blackmails an executive to avoid being replaced. In alignment faking, it complies with harmful requests during training to keep its values from being modi…

- **[From FAIR to AI-FAIR Metadata-First Infrastructure for AI-Enabled Science](https://arxiv.org/abs/2611.03327v1)**
  - *Elizabeth G. Campolongo, Eric R. Sokol, Marty Downs et al.*
  - `2026-11-02`
  - Artificial intelligence (AI) technologies and their capabilities have advanced rapidly over the past few years, leading to widespread interest and adoption in the biological and ecological sciences. However, the data infrastructure and computational resources that provide the fou…

- **[LLMs Depend on Specialist Tools for Out-of-Distribution Generalization in MS/MS Structural Elucidation](https://arxiv.org/abs/2611.03308v1)**
  - *Gabriel Asher, Cailum M. K. Stienstra, Tomo Oga et al.*
  - `2026-11-02`
  - A frontier language model was recently reported to solve 1D NMR structural elucidation without tools. We ask whether this capability transfers to tandem mass spectrometry (MS/MS) in the de novo setting, where the model must propose a structure directly from the spectrum without a…

- **[An Axiomatic Framework for Reinforcement Learning in Open Multi-Agent Systems](https://arxiv.org/abs/2611.03301v2)**
  - *Jianhong Wang, Yang Li, Samuel Kaski et al.*
  - `2026-11-02`
  - Open multi-agent systems, where only a subset of agents are controllable, are central to real-world domains such as smart grids, yet lack a principled foundation for reinforcement learning algorithm design. We study this setting through n-agent ad hoc teamwork (NAHT), a recent fr…

- **[SQLoom: Set-Contrastive Learning of Syntactic, Semantic, and Logical Dependencies for Text-to-SQL](https://arxiv.org/abs/2611.03298v1)**
  - *Hao Fu, Degang Sun, Wan Wei et al.*
  - `2026-11-02`
  - Text-to-SQL translates natural language questions into SQL queries, enabling database access without writing SQL. Fine-tuning open-weight large language models (LLMs) is cost-effective, but existing methods treat SQL as ordinary text and optimize token-level likelihood without ex…

- **[Top-$k$ Retrieval Leaves Memory Value Undetermined](https://arxiv.org/abs/2611.03289v1)**
  - *Arman Behnam*
  - `2026-11-02`
  - A memory-augmented agent must decide which memories to keep, merge and retrieve, and its only evidence of their value is its retrieval log: the memories it retrieved in each episode and whether it succeeded. Existing methods assign every memory a value from this log, even when th…

- **[VagueBench: Benchmarking the Robustness of Embodied Agents on Ambient Context Illusions](https://arxiv.org/abs/2611.03765v1)**
  - *Yang Qu, Qiang Fu, Zonghao Ying et al.*
  - `2026-11-02`
  - Embodied agents are increasingly deployed in open-world environments, yet current robustness evaluations remain biased toward hazardous instructions and jailbreak vulnerabilities. A more fundamental issue is largely overlooked: agents are rarely tested under semantically sufficie…

- **[ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents](https://arxiv.org/abs/2611.03238v1)**
  - *Daiqiang Li, Jingyi Peng, Rui Hu et al.*
  - `2026-11-02`
  - Computer-use agents for scientific software require application-specific expertise. Much of this expertise is documented in human-authored software manuals and web pages. However, turning these resources into executable, reusable skills remains challenging due to mismatches betwe…

- **[Axion 1.0: Open Agent Foundation Models, Simplified](https://arxiv.org/abs/2611.03233v2)**
  - *Yuqi Jia, Yunjie Tian, Jiayu Zheng et al.*
  - `2026-11-02`
  - We introduce Axion 1.0, a fully open agent foundation model that combines strong and broad agentic capabilities with a remarkably simple training recipe. Axion 1.0 is trained in only three stages: two lightweight supervised fine-tuning stages followed by reinforcement learning, w…

- **[Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction](https://arxiv.org/abs/2611.03223v1)**
  - *Yiwei Zha, Qingyu Meng, Herbert Bos et al.*
  - `2026-11-02`
  - LLM agents compact long histories to fit their context windows, but the compacted context must still carry the operating rules that govern later actions. Prior work shows that violations rise after compaction, but measures compliance outside a complete agent harness and does not…

- **[Can Coding Agents Sustain Continual Evolution without Forgetting?](https://arxiv.org/abs/2611.03219v1)**
  - *Shangziqi Zhao, Yitong Zhang, Jia Li*
  - `2026-11-02`
  - Recently, harness self-evolution has emerged as an important paradigm for improving agent performance. Prior studies show that evolving the agent harness can effectively enhance agent capabilities without modifying the foundation model's parameters. We find that existing approach…

- **[Auto-Research Agent on MSA Organization to Improve Protein-Protein Complex Structure Prediction](https://arxiv.org/abs/2611.03183v2)**
  - *Zilu Zhang, Jing Bao, Lifeng Qiao et al.*
  - `2026-11-02`
  - Protein-complex structure prediction with AlphaFold 3 depends on MSA content, depth, and cross-chain pairing. Current pipelines apply uniform recipes, typically maximizing depth and pairing by species, yet even whether cross-chain pairing helps AF3 remains contested. We show that…

- **[CoworkOS:Scaling Agent Coworkers for Real-world Automation](https://arxiv.org/abs/2611.03178v1)**
  - *Jiajie Jin, Guanting Dong, Chengjun Pan et al.*
  - `2026-11-02`
  - Rapid advances in cowork agents are shifting human-AI collaboration toward real-world automation, delivering software, designs, and other artifacts. However, such productivity work demands both high-quality delivery on complex productivity tasks and continued monitoring and decis…

- **[Toward Knowledge-Centric AI: Discovering, Internalizing, and Using Explicit Knowledge Across Agents and Generations](https://arxiv.org/abs/2611.03157v1)**
  - *Yisen Gao, Haoyu Huang, Zhongwei Xie et al.*
  - `2026-11-02`
  - Knowledge is how understanding accumulates across people and generations: durable records that outlive their producers and that others can check, combine, teach, and correct. AI agents are now built and run by many independent users and organizations, and each agent is upgraded,…

- **[CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements](https://arxiv.org/abs/2611.03126v1)**
  - *Xinlei Yu, Gen Li, Ji Zhao et al.*
  - `2026-11-02`
  - Despite recent advances in CUAs, their development remains constrained by the limited diversity, controllability, and reliability of interaction data. Moreover, conventional optimization pipelines lack iterative feedback, while existing recursive improvement approaches often rely…

- **[ComplianceAtlas: A Taxonomy-Driven Agentic AI Framework for Automated AI Act Gap Analysis and Remediation](https://arxiv.org/abs/2611.03121v1)**
  - *Ilias Driouich, Hongliu Cao, Eoin Thomas et al.*
  - `2026-11-02`
  - Assessing regulatory compliance for high-risk AI systems requires systematic identification of technical gaps such as missing controls, in- adequate processes, or shallow evaluation of practices. Compliance officers typically admin- ister structured questionnaires collecting evi-…

- **[From Local Skills to Long-Horizon Web Tasks: Progressive Skill Exploration for LLM Web Agents](https://arxiv.org/abs/2611.03116v1)**
  - *Xueyang Feng, Xiaohe Bo, Xu Chen et al.*
  - `2026-11-02`
  - Large language models (LLMs) are driving autonomous agents toward real-world environments, with the Web emerging as one of the most representative interaction scenarios. However, training Web agents with naive exploration remains challenging: successful trajectories are rare, and…

- **[LUCA: A Synthetic World for Experimental Reasoning](https://arxiv.org/abs/2611.03100v1)**
  - *Anna Gogleva, Thomas Charman, Martin Balla et al.*
  - `2026-11-02`
  - An experimental agent can succeed for the wrong reasons. Evaluations, however, often focus on the outcome, not the experiments, evidence, and inferences that produced it. We introduce LUCA, a configurable synthetic world for evaluating this process under fully known ground truth.…

- **[Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents](https://arxiv.org/abs/2611.03092v1)**
  - *Zheng Wu, Xinbei Ma, Yao Yao et al.*
  - `2026-11-02`
  - Personal AI agents are increasingly capable of handling long-horizon tasks across applications, yet users often need to invest substantial effort in specifying goals, resolving ambiguity, and verifying outcomes. We argue that progress should be measured by how effectively agents…

- **[Towards a Trustworthy and Governable Internet of Agentics: An Architectural Perspective on Protocols, Systems, and Services](https://arxiv.org/abs/2611.03066v1)**
  - *Haoyi Xiong, Yi Liu, Jiang Bian et al.*
  - `2026-11-02`
  - Large language model applications are increasingly being organized as tool-using and multi-agent workflows rather than as isolated chat interfaces. This perspective paper examines the architectural problem that follows from that shift: agents may reason, invoke tools, and delegat…

- **[Networked AI: Architecture, Theory, and Applications](https://arxiv.org/abs/2611.03063v1)**
  - *Liang Song, Jiayue Jin, Peng Sun et al.*
  - `2026-11-02`
  - Recent advances in Artificial Intelligence (AI), particularly large-scale deep learning, have been driven by monolithic or offline training on massive curated datasets. While successful, these approaches face structural limitations: escalating data and computational demands, limi…

- **[BLPO: Beyond-Local Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2611.03005v1)**
  - *Xuanren Chen, Chongyang Tao, Wenpeng Hu et al.*
  - `2026-11-02`
  - Long-horizon tasks require large language model (LLM) agents to coordinate interdependent actions, a capability central to automating complex workflows. Stepwise group-based reinforcement learning provides finer credit than trajectory-level supervision, but reliable comparisons m…

- **[Action Verification through Conjecture and Refutation for Language Model Agents](https://arxiv.org/abs/2611.02950v1)**
  - *Minhyeon Oh, Chiyeong Heo, Geonwoo Noh et al.*
  - `2026-11-02`
  - Language model agents increasingly act on users' behalf by manipulating external environments through tools, often from high-level instructions that leave critical task- and environment-specific context unstated. To prevent resulting misaligned actions, recent work verifies propo…

- **[The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents](https://arxiv.org/abs/2611.03754v1)**
  - *Geyuan Wang, Shunyu Liu, Siyuan Liang et al.*
  - `2026-11-02`
  - Large Language Models (LLMs) have shown promise for empowering search agents to tackle complex information-seeking tasks. However, since acquiring external information necessitates web search, these agents are highly susceptible to various adversarial attacks (e.g., malicious inf…

- **[Why Tabular Foundation Models Excel on Relational Data They Have Never Seen](https://arxiv.org/abs/2611.02936v2)**
  - *Linjie Xu, Yiqun Hu, Jixiang He et al.*
  - `2026-11-02`
  - Given a relational database (RDB) storing heterogeneous tabular information, how can we predict missing (or future) values in some target column of interest? As candidate targets are numerous in enterprise settings, it is preferable to avoid learning a new model from scratch each…

- **[What makes a theorem interesting? Operationalizing interestingness for open-ended exploration](https://arxiv.org/abs/2611.02905v1)**
  - *Silvère Gangloff*
  - `2026-11-02`
  - An agent that explores, whether it generates conjectures or research ideas, must decide which of them are worth keeping. This judgment of interestingness is usually delegated to a hand-picked proxy or to a language model, neither of which is known to correspond to what humans act…

- **[TLAPS-Bench: Formally Proving Correctness of Real-World System Specifications with TLA+ Proof System](https://arxiv.org/abs/2611.02849v1)**
  - *Qian Cheng, Ruize Tang, Saad Mohammad Rafid Pial et al.*
  - `2026-11-02`
  - TLAPS-Bench is a benchmark and execution harness for constructing machine-checked proofs for real-world system specifications in TLA+ with agentic AI. Proving correctness of complex system specifications requires discovering inductive invariants, reasoning about intricate state t…

- **[Math Foundation Formalization Agent: A General-Purpose Approach to Formalizing Mathematical Foundations](https://arxiv.org/abs/2611.02843v1)**
  - *Jiaxin Xie, Guowei Dou, Xiang Ji et al.*
  - `2026-11-02`
  - Mathematical formalization plays an important role in establishing rigorous and machine-verifiable foundations for mathematical reasoning. With the development of large language models (LLMs) and interactive theorem provers, intelligent agents offer a promising approach to automa…

- **[CARE: Grounded Recursive Self-Improvement for Production Customer-Service Agents](https://arxiv.org/abs/2611.02839v1)**
  - *Yanbei Jiang, Chao Lei, Rena Gao et al.*
  - `2026-11-02`
  - Recursive self-improvement (RSI) in production agents involves transforming accumulated experience into reliable model updates while adapting to evolving business policies. We present CARE (Customer-service Agent Retrospective and Evolve), a grounded RSI framework that operationa…

- **[Reimagining computational quantum research with AI scientists](https://arxiv.org/abs/2611.02833v1)**
  - *Yuxuan Du, Hanqing Zhao, Xinbiao Wang et al.*
  - `2026-11-02`
  - AI scientists are expanding automated research across scientific domains, yet their ability to turn the scientific record into a foundation for autonomous discovery remains elusive. Here we uncover a fundamental barrier to this transition and demonstrate a route to overcome it in…

- **[Think with Skills: Pseudocode Planning Before Execution for Advanced Reasoners](https://arxiv.org/abs/2611.02830v1)**
  - *Boshen Zhou, Boxuan Yue, Xiang Li et al.*
  - `2026-11-02`
  - Language model agents often struggle with complex tasks even when equipped with expert-written skills. Such skills encode declarative knowledge, whereas successful execution requires procedural knowledge tailored to the task at hand. Natural language skills may leave conditions a…

- **[RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures](https://arxiv.org/abs/2611.02826v1)**
  - *Jinbo Hu, Songren Zhang, Chuanxun Fu et al.*
  - `2026-11-02`
  - Reaction data underpin machine learning for reaction prediction, condition recommendation, and retrosynthetic planning, yet extracting these data from literature figures still requires substantial manual effort. Many figures encode multiple experiments through shared templates, s…

- **[Discovering hierarchical governing equations for community-structured complex network dynamics with LLM agents](https://arxiv.org/abs/2611.02816v1)**
  - *Jinlei Zhang, Zixuan Zhang, Hao Qiu et al.*
  - `2026-11-02`
  - Governing equations provide an interpretable description of the mechanisms underlying complex network dynamics, yet their discovery from observational data remains challenging when shared community-level dynamics coexist with individual-level variations and the relevant functiona…

- **[Predictive Safety Guardrails Do Not Always Make LLM Agents Safer](https://arxiv.org/abs/2611.02815v1)**
  - *Weixiang Zhao, Zhihao Liu, Guancheng Li et al.*
  - `2026-11-02`
  - Large language model agents increasingly take consequential actions in digital and physical environments, where safety risks may emerge only after multiple interaction steps. This has motivated world-model-driven predictive safety guardrails, which anticipate future consequences…

- **[SelfImprove-Bench: Evaluating Generalization in Self-Improving Agents](https://arxiv.org/abs/2611.02797v1)**
  - *Bangrui Xu, Jie Yang, Sidi Chen et al.*
  - `2026-11-02`
  - Recursively self-improving (RSI) systems are increasingly viewed as a promising means of accelerating progress toward artificial general intelligence. They aim to autonomously improve their capabilities by refining their working pipelines and recursively improving the strategies…

- **[Stop Handcrafting Your Engine! GenDB-V: Towards AI-Generated and Formally Verified Database Systems](https://arxiv.org/abs/2611.02779v1)**
  - *Jiale Lao, Immanuel Trummer*
  - `2026-11-02`
  - For over 50 years, the database community has developed a wide range of successful engines to answer two fundamental questions: how can database systems run faster, and how can we ensure their correctness? Experience with these engines shows that performance depends on hardware a…

- **[AffToM: Benchmarking Recursive Affective Theory of Mind in Dynamic Multi-Party Interactions](https://arxiv.org/abs/2611.02725v1)**
  - *Jinpeng Hu, Yiduo Jin, Erqiang Wang et al.*
  - `2026-11-02`
  - Understanding emotion in realistic social interactions requires more than recognizing facial expressions or assigning affective labels. The same event can elicit different emotions depending on what each participant knows, what they believe others know or feel, and how these nest…

- **[IssueLighter: An Issue Type-Aware LLM Agent for Issue Report Validity Assessment](https://arxiv.org/abs/2611.02721v1)**
  - *Jiawei Ran, Yuxia Zhang, Ziyang Zhao et al.*
  - `2026-11-02`
  - Invalid issue reports are prevalent in open source software (OSS) projects, imposing substantial burdens on maintainers who already face a high risk of burnout. Prior research has primarily focused on identifying invalid reports for specific issue categories (e.g., bug and wontfi…

- **[Hindsight Credit Assignment over Trees for Agentic RL](https://arxiv.org/abs/2611.02706v1)**
  - *Penghong Zhao, Yihao Chen, Maoheng Yuan et al.*
  - `2026-11-02`
  - Reinforcement learning for long-horizon LLM agents faces a fundamental dilemma: successful experiences are essential for policy improvement, yet limited policy capabilities make such experiences difficult to discover. Sparse outcome rewards compound this challenge, leaving sample…

- **[GeoGuesser Bench: Benchmarking Vision-Language Agents on Interactive Geolocation](https://arxiv.org/abs/2611.02698v1)**
  - *Huanzhi Mao, Yichuan Wang, Michael Koo et al.*
  - `2026-11-02`
  - Vision-language model (VLM) agents that act in the open world need two abilities: world knowledge to interpret what they see, and exploration to find what they cannot yet see. We study how agents combine the two through interactive visual geolocation. GeoGuesser Bench contains 28…

- **[Closing the Dynamics Gap through Self-Directed Robotic Interaction](https://arxiv.org/abs/2611.02691v1)**
  - *Xilun Zhang, Liam Achenbach, Luis Pabon et al.*
  - `2026-11-02`
  - Agentic Real2Sim2Real systems can reconstruct a scene in simulation from camera observations, but contact-rich dynamics such as friction and restitution cannot be observed without interaction. We call this the dynamics gap and present CUE, an agentic system that closes it by inte…

- **[Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659v1)**
  - *Mei Chen, Yu Xia, Haipeng Mao*
  - `2026-11-02`
  - Producing an executable CAD script is not sufficient to establish that an agent has satisfied an engineering design request. Evaluation must also consider the resulting geometry, specified dimensions, and native CAD modeling history. We present Parametric CAD Bench v3, a 100-task…

- **[Measuring AI Agents as Teammates with Collaborative Intelligence](https://arxiv.org/abs/2611.02633v1)**
  - *Sean Wu, Aneesh Pappu, Jiaru Zou et al.*
  - `2026-11-02`
  - Progress in AI is often measured by what a single model can do on its own. Yet teams of AI agents are starting to make breakthroughs and discoveries in science, medicine, mathematics and software engineering. As AI begins to work in teams of agents and people, the ability to coll…

- **[Widening Harm Evaluation Coverage with a Judge that Reads the World](https://arxiv.org/abs/2611.02624v1)**
  - *Prabhpreet Singh Setia, Bhavesh Neekhra, Debayan Gupta*
  - `2026-11-02`
  - An agent acting in a stateful environment can leave evidence of harm in two places: the record of what it did and said, or the world it changed. Safety evaluations for discovering harm examine one or the other in limited ways, using either an LLM judge over the trajectory or dete…

- **[StateFence: Task-State Protection Against Evidence-Chain Contamination in Blue-Team LLM Agents](https://arxiv.org/abs/2611.02605v1)**
  - *Haowen Dai, Alejandro Guerra-Manzanares*
  - `2026-11-02`
  - Indirect prompt injection creates a distinctive risk for blue-team Large Language Model (LLM) agents in Security Operations Centers (SOCs). Malicious instructions can be embedded in telemetry, tickets, retrieval results, or memory and then propagate through alert triage, incident…

- **[Parallelism-Aligned Pruning and Round-Aware Context Reuse for On-Device Multimodal Agents](https://arxiv.org/abs/2611.02601v1)**
  - *Peipei Jiao, Mingkang Liu, Weiming Meng et al.*
  - `2026-11-02`
  - On-device multimodal agents are limited by two deployment mismatches: pretrained attention structures may not divide evenly across the compute cores of an edge accelerator, causing irregular partitions; and standard prefix caching keeps historical visual tokens in the persistent…

- **[EEFA: A Framework for the Ethical Evaluation of AI Agents](https://arxiv.org/abs/2611.02561v1)**
  - *Swathi Pallikala, Yashas Hariprasad*
  - `2026-11-02`
  - The rapid deployment of autonomous AI agents across consequential domains including healthcare, legal services, nancial management, and enterprise workows has created an urgent governance challenge. While the eld of AI evaluation has produced sophisticated benchmarks for measurin…

- **[Scientific Liquidity Agents: An Agent-Based Model of Knowledge Arbitrage in Scientific Communities](https://arxiv.org/abs/2611.02539v1)**
  - *Koutian Wu, You Liu, Yue Liu et al.*
  - `2026-11-02`
  - Scientific knowledge gains new uses when ideas, methods, and results move between research contexts. Understanding this process requires a model of both specialized knowledge production and the intermediary activities that connect it. We introduce Scientific Liquidity Agents (SLA…

- **[Cumulative and Audited Guardrail Tool Evolution for LLM Agent Safety](https://arxiv.org/abs/2611.02516v1)**
  - *Xiao Yang, Aishan Liu, Siyuan Liang et al.*
  - `2026-11-02`
  - Large language model (LLM) agents increasingly operate in open-world environments where safety risks cannot be fully predefined. However, most existing guardrail mechanisms remain static, relying on fixed rules, prompts, or classifiers that generalize poorly to emerging risks. He…

- **[When Prediction Shapes the Future: A BlueSky Agenda for Reflexive Time Series Analysis](https://arxiv.org/abs/2611.02511v1)**
  - *Tao Xie, Yiqun Zhang, Yiu-ming Cheung*
  - `2026-11-02`
  - Time-series models are increasingly deployed in operational systems (e.g., inventory management and clinical care) where predictions trigger interventions that alter future observations, producing records we term AI-shaped trajectories. This sequence-prediction coupling deepens a…

- **[RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild](https://arxiv.org/abs/2611.02497v1)**
  - *Tan Sang Nguyen, Yi Ru Wang, Shailesh Shailesh et al.*
  - `2026-11-02`
  - General-purpose robot policies must work across robots, tasks, and environments, yet the variation that makes physical trials informative also makes them difficult to reproduce. We introduce RoboColosseum, a distributed evaluation framework that combines unified policy serving an…

- **[Benchmark of THReD: Evaluating an LLM Agent and Its Preprocessing Tools for Turning Electronic Health Records into AI-Ready Datasets](https://arxiv.org/abs/2611.02484v1)**
  - *Javad Mohammad Alizadeh, Huanmei Wu*
  - `2026-11-02`
  - LLM agents are increasingly built into data-analysis software, yet little evidence shows how reliably they preprocess clinical data or whether the tools they invoke give correct, reproducible output. We report a benchmark of THReD, a web-based system that turns electronic health…

- **[MAGAR: Multimodal Agents for GUI-Based 3D Mechanical Assembly and Minimal Rework](https://arxiv.org/abs/2611.02472v1)**
  - *Jingxuan Wei, Jiahao Fu, Fuqiang Wang et al.*
  - `2026-11-02`
  - A GUI command can be correct at the interface level yet still produce an incorrect assembly. An agent must identify the relevant components, respect their structural relationships, and determine which parts should move during recovery. We introduce MAGAR-Bench, a benchmark of 4,0…

- **[RLiD: Reinforcement Learning in the Decision Plane for Language Agents and LLMs](https://arxiv.org/abs/2611.02455v1)**
  - *Ziyi Chen, Yan Zhang, Jianhui Wei et al.*
  - `2026-11-02`
  - Reinforcement learning (RL) has improved the capabilities of large language models (LLMs) across a wide range of tasks. However, token-level RL assigns an action's advantage to the entire generated response, including tokens specifying the parsed action, reasoning chains, and mal…

- **[Harvesting SWE Benchmarks from Wild Vibe Coding Sessions](https://arxiv.org/abs/2611.02440v1)**
  - *Ao Lu, Yuanhao Zeng, Shaocheng Lan et al.*
  - `2026-11-02`
  - Development teams need reproducible tasks from their own repositories and workflows to evaluate coding agents. Conversational developer-agent collaboration ("vibe coding") produces abundant coding sessions and repository checkpoints, but requirements evolve across turns, unrelate…

- **[EvoMemState: Evolving Memory State for Personal Agents](https://arxiv.org/abs/2611.03743v1)**
  - *Zhishang Xiang, Yunbo Tang, Zhongqiao Liu et al.*
  - `2026-11-02`
  - Long-term memory enables large language model (LLM) agents to provide continuous personalized assistance by retaining user information across interactions. Existing systems support this process through fact extraction, organization, updating, and retrieval, but largely maintain m…

- **[SGR-OPSD: Learning from Subgoal Plans with Graph-Regularized Credit Assignment for Agentic Reinforcement Learning](https://arxiv.org/abs/2611.02414v1)**
  - *Shu Liu, Yang Chong, WenShi Chen et al.*
  - `2026-11-02`
  - OPSD provides dense supervision for agentic reinforcement learning through privileged information feedback. However, existing privileged information often lacks explicit task-progression planning, while teacher-student log-probability gaps reflect shifts in model preference rathe…

- **[Networked Synthetic Social Engineering on the Web](https://arxiv.org/abs/2611.02407v1)**
  - *Bryan C. Boots*
  - `2026-11-02`
  - Several genuine AI services may repeat one unsupported source, and correcting that source may leave later reports unchanged. We examine these networked consequences of synthetic social engineering (SSE), deliberately misleading influence intended to redirect AI recipients from au…

- **[Late Autumn: LLM Agents Specialize a General Multi-Robot Planner for One Warehouse](https://arxiv.org/abs/2611.02391v1)**
  - *Yimin Tang, Han Zhang, Shao-Hung Chan et al.*
  - `2026-11-02`
  - No algorithm is best on all problems, but a real warehouse is a narrow problem: its layout and processes rarely change. Operators still run one general multi-robot planner at many sites, because experts cannot tune it for each one. In this work, which we call Late Autumn, we expl…

- **[Beyond Accuracy: How Quantization Affects Coding Agents](https://arxiv.org/abs/2611.02368v1)**
  - *Areej Mehboob, Muhammad Ali Shafique, Muhammad Usman Qadeer et al.*
  - `2026-11-02`
  - Agents are increasingly used for coding tasks, but the inference cost of large language models (LLMs) limits where they can run. Quantization reduces model size, but its effects on coding agents that execute and revise programs remain underexplored. We compare BF16 with 4-bit AWQ…

- **[AgiWorld: An Agentic Video World Model for Building Persistent Worlds](https://arxiv.org/abs/2611.02341v1)**
  - *Shaoheng Fang, Yiqun Mei, Hanwen Jiang et al.*
  - `2026-11-02`
  - Recent interactive video world models generate visually compelling videos from a single image, following user-provided camera motion and text prompts. However, such low-level control demands substantial user effort to realize a high-level intent, and the generated world struggles…

- **[LEANGUARD: Lean-Verified Guardrails for Tool-Using Agents](https://arxiv.org/abs/2611.02332v1)**
  - *Sreehari Sankar, Debargha Ganguly, Vikash Singh et al.*
  - `2026-11-02`
  - Tool-using language-model agents often execute actions that their domain policies forbid. We present LeanGuard, a runtime that checks every proposed tool call against a policy written in Lean4 before the call reaches the environment. Policies combine state predicates with scoped…

- **[Accessed, never disclosed: Silent access to protected health information by medical artificial intelligence agents](https://arxiv.org/abs/2611.02319v1)**
  - *Jae Wang Lee, Abhirup Banerjee, Yeong Chan Lee*
  - `2026-11-02`
  - Medical artificial intelligence agents should retrieve patient identifiers only when a task requires them, the data-minimization principle behind the HIPAA minimum necessary standard for protected health information (PHI). An agent can retrieve identifiers without revealing them.…

- **[Finite-Sample Convergence in Networked Average Reward MARL: Decentralization Pitfalls and Entropy Remedies](https://arxiv.org/abs/2611.04072v1)**
  - *Yizhou Zhang, Yashaswini Murthy, Laixi Shi et al.*
  - `2026-11-02`
  - We study the problem of average reward Multi-Agent Reinforcement Learning (MARL) where agents interact within a network. Each agent in the network conducts local updates with information within its $k$-hop neighborhood and collaboratively maximizes the overall reward of the entir…

- **[Rapid Mean-Field Formation Transport with a Shared-Representation Neural Fokker-Planck Controller](https://arxiv.org/abs/2611.03981v1)**
  - *Zejian Zhou, Hao Xu*
  - `2026-11-02`
  - This paper develops a mean-field formation transport method with low online computational cost for large-scale multi-agent systems. Classical mean-field planners often require repeated solutions of coupled forward and backward partial differential equations, making online replann…

- **[Should We Combine Our Data? Algorithms and Limits for Privately Assessing Data Sharing](https://arxiv.org/abs/2611.03599v1)**
  - *Mahdi Haghifam, Kumar Kshitij Patel, Avrim Blum et al.*
  - `2026-11-02`
  - In this paper, we study when two parties should pool their data to train a machine learning model. Two agents, Alice and Bob, each hold a sensitive labeled dataset and want to train a classifier from a given hypothesis class $\mathcal{H}$. Even when each party's dataset can be pe…

- **[Can LLM Agents Improve Imperfect Earth System Model Parameterizations?](https://arxiv.org/abs/2611.03543v1)**
  - *Kara D. Lamb*
  - `2026-11-02`
  - Earth system models (ESMs) rely on parameterizations to represent unresolved processes such as convection, cloud microphysics, and turbulence. However, translating advances in physical understanding into stable, validated parameterizations and integrating them into ESMs often tak…

- **[DistDebug-Bench: Can LLM Agents Diagnose Bugs in Distributed Systems?](https://arxiv.org/abs/2611.03523v1)**
  - *Yuxuan Jiang, Chenglin Liu, John Rose et al.*
  - `2026-11-02`
  - LLM agents show strong potential in software engineering tasks such as competitive programming and code synthesis. Existing benchmarks, however, largely focus on small-scale settings such as self-contained Python modules, leaving distributed systems, an essential class of product…

- **[What Structurally Breaks an Agent? Auditing Difficulty in Stateful Tool-Use Workflows](https://arxiv.org/abs/2611.03227v1)**
  - *Shereen Anand, Ju Wang, Yali Du*
  - `2026-11-02`
  - An aggregate task score does not distinguish failures of scheduling, state retention, and candidate selection. We develop a small executable instrument that varies dependency depth, candidate count, active state width, and access to current-state snapshots while holding the numbe…

- **[Bayesian Sequential Optimal Experimental Design for Single-Pixel Imaging using Reinforcement Learning](https://arxiv.org/abs/2611.03042v1)**
  - *Marcos Antonio Obando, Tianyuan Wang, Tanja Tarvainen et al.*
  - `2026-11-02`
  - Adaptive compressed sensing (CS) aims to select the most informative measurements sequentially, which is crucial for many modern imaging systems. This task can be formulated as a Bayesian sequential optimal experimental design (sOED) problem, where each new acquisition is chosen…

- **[AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games](https://arxiv.org/abs/2611.02875v1)**
  - *Woohyeon Byeon, Seongmin Kim, Jiwon Jeon et al.*
  - `2026-11-02`
  - In this paper, we consider mixed-motive games (MMGs) which model various real-world multi-agent scenarios where self-interested agents must both cooperate and compete. We identify an issue with existing gifting methods, where agents become overly dependent on incoming gifts and f…

- **[HLSClaw: Bringing Vibe Coding to High-Level Synthesis through Skill-Based Agentic Harness](https://arxiv.org/abs/2611.02784v1)**
  - *Jinming Ge, Shang Liu, Jiawei Liang et al.*
  - `2026-11-02`
  - LLM agents are rapidly shifting software development toward intent-driven \emph{vibe coding}, yet their effectiveness drops sharply in high-level synthesis (HLS), where code optimization must jointly consider design structure, directive search, and downstream hardware constraints…

- **[SMILE: A Structured Multi-Agent Clinical Reasoning for Liver Ultrasound Understanding](https://arxiv.org/abs/2611.02581v1)**
  - *Haris Ghafoor, Minjee Seo, Seonaeng cho et al.*
  - `2026-11-02`
  - Automated liver ultrasound report generation improves the diagnosis of liver diseases by producing clinically structured descriptions of anatomical and disease-related findings. However, current generative vision-language models (VLMs) often rely on a single reasoning pathway tha…

- **[Beyond $L_\infty$-Norm Sets: Synthesizing Interpretable Non-Uniform Uncertainty Sets for Evaluation-Time State-Adversarial Robustness](https://arxiv.org/abs/2611.02576v1)**
  - *Xulin Chen, Ruipeng Liu, Garrett E. Katz*
  - `2026-11-02`
  - Deep reinforcement learning (DRL) agents are vulnerable to perturbations of their observed state inputs. Prior works often constrain state adversaries with $L_p$-norm uncertainty sets and evaluate policy performance under the resulting perturbations. However, in continuous contro…

- **[Organizational Learning in Materials Discovery Campaigns: Which Databases, Calculations, and Agent Teams Pay Off](https://arxiv.org/abs/2611.02571v1)**
  - *Kinston Ackölf, Taylor D. Sparks*
  - `2026-11-02`
  - More databases can make a materials campaign worse. Through an organizational lens, we trace each source's contribution. One band-gap campaign ranks seven anion families from archived measured gaps, one vote per source. In the first half of its budget, all seven pooled rank worse…

- **[SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding](https://arxiv.org/abs/2611.02501v1)**
  - *Kunjun Li, Wenhao Chai, Yihao Liang et al.*
  - `2026-11-02`
  - Speculative decoding accelerates memory-bound LLM decoding with a lightweight drafter, and parallel drafters extend this speedup by drafting a whole block in one forward pass. However, it remains unclear whether their released systems (stock) attain the full speedup that parallel…

- **[Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon](https://arxiv.org/abs/2611.02361v1)**
  - *Tianhao Guo, Chongyao Guo*
  - `2026-11-02`
  - Can a language model that reads the full history of an access log say whether a service may act now? On an executable benchmark of grants, withdrawals, reinstatements, expiries, groups and change windows under a known policy, scored on pairs of histories that differ only in the o…

- **[Dory1.0-4B: A Looped Normalized-GPT](https://arxiv.org/abs/2611.03998v1)**
  - *Maxim Fishman, Simeng Sun, Shantanu Acharya et al.*
  - `2026-11-02`
  - We introduce Dory1.0-4B, a 4-billion-parameter looped (latent-recurrent) language model with elastic depth: a single checkpoint serves different inference compute budgets. Dory1.0-4B is built on a normalized Transformer (nGPT) backbone with interleaved sliding-window and full-att…

- **[EvoGroup: A Self-Evolving Harness for Group Agents in Shared Contexts](https://arxiv.org/abs/2611.03868v1)**
  - *Xinyi Xu, Xiaoyang Li, Yucheng Feng et al.*
  - `2026-11-02`
  - With the rise of Group Agent such as Claude Tag, agents increasingly serve as digital workers for long-term team collaboration. These agents operate over shared contexts that continuously accumulate through multi-user interactions. However, existing agent memory systems are mainl…

- **[NitiBench+: A Temporal Thai Legal Question Answering Benchmark Across 17 Domains](https://arxiv.org/abs/2611.03576v2)**
  - *Pawitsapak Akarajaradwong, Sarana Nutanong, Chompakorn Chaksangchaichot*
  - `2026-11-02`
  - Law changes over time. A court decides a case under the law in force on that day, and legal QA benchmarks grade answers against today's law. We checked 156,650 decisions of four Thai courts. Up to 67% of them cite law that has since been amended or repealed. We introduce NitiBenc…

- **[VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](https://arxiv.org/abs/2611.03575v1)**
  - *Wei-Lin Chen, Zhepei Wei, Xinyu Zhu et al.*
  - `2026-11-02`
  - Large language model (LLM) coding agents increasingly operate with shell access, allowing them to write scripts, move files, alter permissions, and modify system configurations. However, an agent may achieve a user's goal while causing unintended harm, such as deleting unrelated…

- **[IdeaTaste: Do LLMs Share the Research Taste of Human Researchers?](https://arxiv.org/abs/2611.03424v1)**
  - *Shanshan Zhong, Chen Xu, Jingjie Ning et al.*
  - `2026-11-02`
  - Research taste, the judgment of what to read, which problems to pursue, and which methods to try, increasingly shapes the work of AI scientists, yet it remains far less understood than their ability to execute research. We introduce IdeaTaste, a benchmark that scores an LLM by ho…

- **[ACTOR: Action-Centered Temporal Organization for Literary Role-Playing Agents](https://arxiv.org/abs/2611.03184v1)**
  - *Yuxiang Gao, Tianjie Ju, Zheng Wu et al.*
  - `2026-11-02`
  - Large language agents for literary role-playing are typically modeled around dialogue generation, leaving characters' non-dialogue behaviors and their dynamic evolution over story time underrepresented. In this paper, we propose ACTOR (Action-Centered Temporal Organization for Li…

- **[A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory](https://arxiv.org/abs/2611.02912v1)**
  - *Yiqi Wang, Tongyuan Zhao, Jiaqi Zhang et al.*
  - `2026-11-02`
  - Long-lived agents rely on persistent memory of users, tasks and decisions, and this memory must stay consistent with a world that keeps changing. When an upstream fact changes, however, memory systems can revise the contradicted memory itself while the beliefs, plans and actions…

- **[TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation](https://arxiv.org/abs/2611.02810v1)**
  - *Yingtao Ren, Xiao Luo, Yiwei Fu et al.*
  - `2026-11-02`
  - This paper studies retrieval-augmented generation (RAG), which leverages external knowledge to improve the performance of language models. Despite the remarkable progress, current RAG approaches are still far from satisfactory due to inadequate retrieval and potential hallucinati…

- **[Labtune: Treating Lab Organization and Information Sharing as Experimental Variables in LLM-Agent Discovery](https://arxiv.org/abs/2611.03935v1)**
  - *Goran Mitevski*
  - `2026-11-02`
  - De-siloing can create groupthink; silos can prevent knowledge sharing and reduce research efficiency. The same tension appears in research systems built with large language model (LLM) agents, yet their organization is usually fixed by design. I propose treating laboratory struct…

- **[Beyond Division of Labor: How Roles Shape Feedback and Recovery in Multi-Agent Systems](https://arxiv.org/abs/2611.03931v1)**
  - *Chih-Hsuan Yang, Xinyang Li, Rajeev Thakur et al.*
  - `2026-11-02`
  - Roles in multi-agent large language model (LLM) systems allocate decisions as well as work. In a Planner--Executor--Reviewer team, the Reviewer's approval can determine when the team submits an answer and receives corrective feedback. We study both functions by varying role instr…

- **[KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL](https://arxiv.org/abs/2611.03138v1)**
  - *Aswin Ramachandran, Jona Schulz, Maurus Derungs et al.*
  - `2026-11-02`
  - Progress in robot learning, particularly physical multi-agent reinforcement learning (MARL), is currently challenged by a limited availability of accessible, standardized benchmarks. While simulation-based MARL has produced remarkable emergent behaviors, from coordinated team pla…

- **[Cloudra: Geometric Reasoning and Scientific Validation for Autonomous Reaction Mechanism Exploration](https://arxiv.org/abs/2611.02909v1)**
  - *Chengyi Yang, Qianxin Zhou, Yang Li*
  - `2026-11-02`
  - Autonomous reaction-mechanism exploration requires proposing reaction steps, preparing three-dimensional structures, and determining which reactant and product a computed saddle point connects. Large language model (LLM) agents can misjudge spatial relationships and confuse a com…

- **[Multi-Modal Multi-Agent System for Bridge Operation and Maintenance based on Large Language Model](https://arxiv.org/abs/2611.02738v1)**
  - *Xiangyun Luo, Yunkai Zhang, Yong Huang et al.*
  - `2026-11-02`
  - Bridges are critical transportation infrastructure, and reliable operation and maintenance (O&M) is essential for traffic safety and long-term structural performance. However, bridge O&M faces key bottlenecks: no unified architecture coordinates heterogeneous resources; model inf…

- **[Coati: Host-Grounded Execution for Installable Mobile GUI Agents](https://arxiv.org/abs/2611.02644v1)**
  - *Yudou Ying, Pu Shi, Hanlei Shi et al.*
  - `2026-11-02`
  - Mobile GUI agents can carry out tasks across apps, yet most run on a separate computer that drives a phone over the Android Debug Bridge (ADB), out of reach of ordinary users and of the apps through which most people reach Web services. We present Coati, a source-available agent…


## Harness  (148)

### AAAI

- **[D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies](https://arxiv.org/abs/2511.16590)**
  - *Sen Chen, Tong Zhao, Yi Bin et al.*
  - **AAAI 2025** · `2025-11-20`
  - Developing intelligent agents capable of operating a wide range of Graphical User Interfaces (GUIs) with human-level proficiency is a key milestone on the path toward Artificial General Intelligence. While most existing datasets and benchmarks for training and evaluating GUI agen…

- **[Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory](https://arxiv.org/abs/2505.15055)**
  - *Hongli Zhou, Hui Huang, Zi-Qing Zhao et al.*
  - **AAAI 2025** · `2025-05-21`
  - The evaluation of large language models (LLMs) via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities. This paper provides a crit…

- **[DHMoE: Diffusion Generated Hierarchical Multi-Granular Expertise for Stock Prediction](https://doi.org/10.1609/aaai.v39i11.33250)**
  - *Weijun Chen, Yan-Ze Wang*
  - **AAAI 2025** · `2025-04-11`
  - Stock prediction stands as a pivotal research objective within the Fintech. Existing deep learning research revolves around the development and scaling of one individual neural network predictor. However, in the dynamic and noisy landscape of the stock market, reliance solely on…


### NeurIPS

- **[Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety](https://openreview.net/forum?id=7UXZAFMvpZ)**
  - *Lifei Liu, Haoran Yu, Xiaochong Jiang et al.*
  - **NeurIPS 2025** · OpenReview · `2026-05-26`
  - Safety evaluations of multi-agent LLM systems often compare a direct prompt against a planner-executor pipeline and report the difference as a single "pipeline effect." This aggregate hides
  several simultaneous changes: harmful intent may be recast as plausible operational work…

- **[Toward Community-Driven Agents for Machine Learning Engineering](https://openreview.net/forum?id=aKChEjaJpZ)**
  - *Sijie Li, Weiwei Sun, Shanda Li et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-03`
  - Large language model-based machine learning (ML) agents have shown great promise in automating ML research.
However, existing agents typically operate in isolation on a given research problem, without engaging with the broader research community, where human researchers often gai…

- **[OpenUnlearning: Accelerating LLM Unlearning via Unified Benchmarking of Methods and Metrics](https://arxiv.org/abs/2506.12618)**
  - *Vineeth Dorna, Anmol Reddy Mekala, Wenlong Zhao et al.*
  - **NeurIPS 2025** · `2025-06-14`
  - Robust unlearning is crucial for safely deploying large language models (LLMs) in environments where data privacy, model safety, and regulatory compliance must be ensured. Yet the task is inherently challenging, partly due to difficulties in reliably measuring whether unlearning…

- **[SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks](https://arxiv.org/abs/2506.11791)**
  - *Hwiwon Lee, Zi-Qi Zhang, Hanxiao Lu et al.*
  - **NeurIPS 2025** · `2025-06-13`
  - Rigorous security-focused evaluation of large language model (LLM) agents is imperative for establishing trust in their safe deployment throughout the software development lifecycle. However, existing benchmarks largely rely on synthetic challenges or simplified vulnerability dat…

- **[REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://arxiv.org/abs/2504.11543)**
  - *Divyansh Garg, Shaun VanWeelden, Diego Caples et al.*
  - **NeurIPS 2025** · `2025-04-15`
  - We introduce REAL, a benchmark and framework for multi-turn agent evaluations on deterministic simulations of real-world websites. REAL comprises high-fidelity, deterministic replicas of 11 widely-used websites across domains such as e-commerce, travel, communication, and profess…

- **[Envisioning Beyond the Pixels: Benchmarking Reasoning-Informed Visual Editing](https://arxiv.org/abs/2504.02826)**
  - *Xiang-Yu Zhao, Pei-Yuan Zhang, Kexian Tang et al.*
  - **NeurIPS 2025** · `2025-04-03`
  - Large Multi-modality Models (LMMs) have made significant progress in visual understanding and generation, but they still face challenges in General Visual Editing, particularly in following complex instructions, preserving appearance consistency, and supporting flexible input for…


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

- **[R-Bench: Graduate-level Multi-disciplinary Benchmarks for LLM & MLLM Complex Reasoning Evaluation](https://arxiv.org/abs/2505.02018)**
  - *Meng-Hao Guo, Jia-Jun Xu, Yi Zhang et al.*
  - **ICML 2025** · `2025-05-04`
  - Reasoning stands as a cornerstone of intelligence, enabling the synthesis of existing knowledge to solve complex problems. Despite remarkable progress, existing reasoning benchmarks often fail to rigorously evaluate the nuanced reasoning capabilities required for complex, real-wo…

- **[Protein Structure Tokenization: Benchmarking and New Recipe](https://arxiv.org/abs/2503.00089)**
  - *Xin-Yu Yuan, Zichen Wang, Marcus Collins et al.*
  - **ICML 2025** · `2025-02-28`
  - Recent years have witnessed a surge in the development of protein structural tokenization methods, which chunk protein 3D structures into discrete or continuous representations. Structure tokenization enables the direct application of powerful techniques like language modeling fo…


### ICLR

- **[HeurekaBench: A Benchmarking Framework for AI Co-scientist](https://arxiv.org/abs/2601.01678)**
  - *Siba Smarak Panigrahi, Jovana Videnovi'c, Maria Brbic*
  - **ICLR 2026** · `2026-01-04`
  - LLM-based reasoning models have enabled the development of agentic systems that act as co-scientists, assisting in multi-step scientific analysis. However, evaluating these systems is challenging, as it requires realistic, end-to-end research scenarios that integrate data analysi…

- **[RefineBench: Evaluating Refinement Capability of Language Models via Checklists](https://arxiv.org/abs/2511.22173)**
  - *Young-Jun Lee, Seungone Kim, Byung-Kwan Lee et al.*
  - **ICLR 2025** · `2025-11-27`
  - Can language models (LMs) self-refine their own responses? This question is increasingly relevant as a wide range of real-world user interactions involve refinement requests. However, prior studies have largely tested LMs'refinement abilities on verifiable tasks such as competiti…

- **[VERINA: Benchmarking Verifiable Code Generation](https://arxiv.org/abs/2505.23135)**
  - *Zhe Ye, Zheng-Xu Yan, Jing-Xuan He et al.*
  - **ICLR 2025** · `2025-05-29`
  - Large language models (LLMs) are increasingly integrated in software development, but ensuring correctness in LLM-generated code remains challenging and often requires costly manual review. Verifiable code generation -- jointly generating code, specifications, and proofs of code-…


### KDD

- **[CR-Bench-v2: Evaluating the Real-World Utility of AI Code Review Agents](https://arxiv.org/abs/2611.02566v2)**
  - *Kristen Pereira, Neelabh Sinha, Rajat Ghosh et al.*
  - **KDD** · `2026-11-02`
  - The rapid growth of automated code generation has created a pressing need for automated code review. Yet code review resists full automation: it depends on context beyond the \textit{diff}, on the author's intent, and on judgments about design and maintainability on which even ex…

- **[IdeaBench: Benchmarking Large Language Models for Research Idea Generation](https://doi.org/10.1145/3711896.3737419)**
  - *Si-Kun Guo, Amir Hassan Shariatmadari, Guang-Zhi Xiong et al.*
  - **KDD 2025** · `2025-08-03`
  - Large Language Models (LLMs) have revolutionized interactions between human and artificial intelligence (AI) systems, demonstrating state-of-the-art performance across various domains, including scientific discovery and hypothesis generation. However, the absence of a comprehensi…


### ACL

- **[AutoMedEval: Harnessing Language Models for Automatic Medical Capability Evaluation](https://arxiv.org/abs/2505.11887)**
  - *Xiechi Zhang, Zetian Ouyang, Lin-Lin Wang et al.*
  - **ACL 2025** · `2025-05-17`
  - With the proliferation of large language models (LLMs) in the medical domain, there is increasing demand for improved evaluation techniques to assess their capabilities. However, traditional metrics like F1 and ROUGE, which rely on token overlaps to measure quality, significantly…

- **[ChartEdit: How Far Are MLLMs From Automating Chart Analysis? Evaluating MLLMs' Capability via Chart Editing](https://arxiv.org/abs/2505.11935)**
  - *Xuanle Zhao, Xue-Xin Liu, Haoyue Yang et al.*
  - **ACL 2025** · `2025-05-17`
  - Although multimodal large language models (MLLMs) show promise in generating chart rendering code, editing charts via code presents a greater challenge. This task demands MLLMs to integrate chart understanding and reasoning capacities, which are labor-intensive. While many MLLMs…

- **[MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs](https://arxiv.org/abs/2501.17399)**
  - *Ved Sirdeshmukh, Kaustubh Deshpande, Johannes Mols et al.*
  - **ACL 2025** · `2025-01-29`
  - We present MultiChallenge, a pioneering benchmark evaluating large language models (LLMs) on conducting multi-turn conversations with human users, a crucial yet underexamined capability for their applications. MultiChallenge identifies four categories of challenges in multi-turn…


### EMNLP

- **[CompassVerifier: A Unified and Robust Verifier for LLMs Evaluation and Outcome Reward](https://arxiv.org/abs/2508.03686)**
  - *Shudong Liu, Hongwei Liu, Jun-Nan Liu et al.*
  - **EMNLP 2025** · `2025-08-05`
  - Answer verification is crucial not only for evaluating large language models (LLMs) by matching their unstructured outputs against standard answers, but also serves as the reward model to guide LLM optimization. Most evaluation frameworks rely on regularized matching or employ ge…

- **[Automated Creativity Evaluation for Large Language Models: A Reference-Based Approach](https://arxiv.org/abs/2504.15784)**
  - *Ruizhe Li, Chiwei Zhu, Benfeng Xu et al.*
  - **EMNLP 2025** · `2025-04-22`
  - Creative writing is a key capability of Large Language Models (LLMs), with potential applications in literature, storytelling, and various creative domains. However, evaluating the creativity of machine-generated texts remains a significant challenge, as existing methods either r…

- **[Skeleton-Guided-Translation: A Benchmarking Framework for Code Repository Translation with Fine-Grained Quality Evaluation](https://arxiv.org/abs/2501.16050)**
  - *Xinglian Zhang, Jiaheng Wen, Fangkai Yang et al.*
  - **EMNLP 2025** · `2025-01-27`
  - The advancement of large language models has intensified the need to modernize enterprise applications and migrate legacy systems to secure, versatile languages. However, existing code translation benchmarks primarily focus on individual functions, overlooking the complexities in…


### Other / arXiv

- **[Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization](https://arxiv.org/abs/2611.03517)**
  - *Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su et al.*
  - 🤗 Featured · `2026-11-02`
  - LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff. Scripted agents fix what the model does at each step, via a learned policy, an optimization menu, or fixed roles, and are sample-efficient where the recipe applies and stall where it does not.…

- **[LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856)**
  - *Haoxiang Cao, Yuxuan Zhang, Penghui Du et al.*
  - 🤗 · `2026-11-04`
  - We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence, rejecting distractors, binding e…

- **[Task-Efficient Agent Evaluation Using Cached Traces](https://arxiv.org/abs/2611.06803v1)**
  - *Ben Johnson, Hayden Helm*
  - `2026-11-04`
  - Efficient benchmarking estimates a system's full benchmark performance from a small number of task executions. Standard approaches rely solely on the binary correctness of executions from a collection of already-evaluated reference systems. An agentic system, however, produces a…

- **[SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory](https://arxiv.org/abs/2611.06445v1)**
  - *Jizhe Zhang, Ang Li, Chenheng Zhang et al.*
  - `2026-11-04`
  - Long-horizon language-model agents accumulate increasingly large interaction histories, making context compaction essential for efficient execution. Existing learned compaction methods often rely on downstream task outcomes or solver behavior, coupling training to specific tasks…

- **[HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](https://arxiv.org/abs/2611.06254v1)**
  - *Zhi Hong, Qianlong Wang, Hongchen Wei et al.*
  - `2026-11-04`
  - The performance of large language model (LLM) agents depends on both the underlying model and the harness that governs interaction with tools and the environment. Yet harness design remains largely manual, and automating it requires navigating an open-ended search space through c…

- **[The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules, Unevenly Across Models](https://arxiv.org/abs/2611.06116v1)**
  - *Mehmet Murat Huyut*
  - `2026-11-04`
  - Banks validate language models, but they deploy systems: a model inside a harness that decides what it sees, which tools it can call and who checks its actions. We test whether that harness changes compliance with banking conduct rules when the model is held fixed. Four open-weig…

- **[Reglos: A Self-Evolving Personal Memory Agent with Recursive Self-Improvement](https://arxiv.org/abs/2611.06049v1)**
  - *Sen Yang, Jiaduo Lin, Zehong Huang et al.*
  - `2026-11-04`
  - Personal agents draw on past conversations to tailor their responses to each user. Their memory systems store and update what each user says, and coding agents now also rewrite the harness that turns this memory into the model's context. Such patches risk overfitting, because one…

- **[Graph-Mediated Large Language Model Systems in the Agentic Era: Reasoning, Knowledge, Retrieval, Execution, and Coordination](https://arxiv.org/abs/2611.05953v1)**
  - *Haihui Liu, Yang Chen, Zice Qiu et al.*
  - `2026-11-04`
  - Graphs play an increasingly important role in large language model (LLM) systems, supporting structural reasoning, knowledge grounding, retrieval, and memory. As these systems evolve toward the agentic era, graphs also organize execution dependencies and multi-agent communication…

- **[A Hybrid Approach for Automated Security Pattern Recovery](https://arxiv.org/abs/2611.05823v1)**
  - *Anh Minh Nguyen, Tuan Dat Tran, Alzubair Hassan et al.*
  - `2026-11-04`
  - Security-by-design emphasises integrating security into software design and development. Security pattern catalogues operationalise this principle by prescribing reusable architectural solutions to recurring security problems. However, recovering their implementations from source…

- **[GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802v1)**
  - *Mohan Cao, Yongsen Mao, Chucheng Xiang et al.*
  - `2026-11-04`
  - Recent LLM-centric advances can generate attractive furnished rooms by selecting and arranging assets. Yet evaluation remains limited to specific perspectives or predefined questions, failing to reflect overall scene quality. To address this pressing need, we introduce GREP. Its…

- **[Analysis of Local Open-Weight LLM Agents on Vulnerability-Reproduction Tasks](https://arxiv.org/abs/2611.06257v1)**
  - *Jorge García-Carrasco, Javier Sanchis, Álvaro Navarro et al.*
  - `2026-11-04`
  - Open-weight language models that fit on a single consumer GPU are becoming capable on a growing range of tasks, and they matter because they can run locally without sending the code to a hosted service. Vulnerability reproduction, turning a vulnerability description into an input…

- **[Airlock: Bounding the Multi-Agent Blast Radius via Selective Online Containment](https://arxiv.org/abs/2611.06727v1)**
  - *Zhonghao Zhan, Javad Forough, Yefan Zhang et al.*
  - `2026-11-04`
  - When multi-agent systems act on the external world, a single agent's faulty output can spread across tasks before detection, creating a system-wide blast radius. Single-agent guardrails are confined to individual harnesses, while existing multi-agent controls either cancel only t…

- **[EnzymeRSI: A dual-loop recursive self-improvement system for enzyme design](https://arxiv.org/abs/2611.06321v1)**
  - *Genoria AI Team, Yuejie Hou, Lixiang Yang et al.*
  - `2026-11-04`
  - Improvement in enzyme engineering is usually pursued by optimising which candidates to assay within a fixed model and workflow; when the bottleneck arises from a mismatched method or a failing workflow, that route is difficult to escape. We present EnzymeRSI, a dual-loop system f…

- **[Continual Classification Beyond the Kernel Regime: Harnessing the Sparsity Bias of L2 Regularization in Diagonal Linear Networks](https://arxiv.org/abs/2611.06759v1)**
  - *Gilad Karpel, Itay Evron, Ron Meir et al.*
  - `2026-11-04`
  - We study logistic regression for continual learning with linear predictors in a high-dimensional statistical setting. Existing theoretical work has largely focused on continual linear regression with variants of L2 regularization, motivated by their analytical simplicity and conn…

- **[A trust layer for fast pedestal-stability surrogates: calibrated error bars, out-of-distribution alarms and few-shot recalibration](https://arxiv.org/abs/2611.06597v1)**
  - *Amin Vakhshouri*
  - `2026-11-04`
  - Machine-learning surrogates of linear peeling-ballooning stability now run in milliseconds, but they are mostly deployed as point estimators: they do not say how wrong they may be, or when a query lies outside what they were trained on. For a fusion company designing a new device…

- **[Chiron: Cache Management Empowered by LLM Intelligence for AI Workloads](https://arxiv.org/abs/2611.06179v1)**
  - *Bohan Zhang, Renshu Ge, Tianze Wang et al.*
  - `2026-11-04`
  - AI clusters keep data in remote object stores and rely on local caches to stop GPUs from waiting for data. A cache performs well only when its prefetching and eviction policies match the access pattern, yet these patterns differ across AI workloads and change between phases of on…

- **[Alleviating Limited Effectiveness and Multi-Class Collapse in Deep Graph-level Clustering](https://arxiv.org/abs/2611.06052v1)**
  - *Xiaoyang Lin, Renchi Yang, Yuqi Chen et al.*
  - `2026-11-04`
  - Given a collection of $N$ graphs, graph-level clustering (GLC) seeks to partition the $N$ graphs into semantically meaningful groups, which serves as a fundamental task in analyzing graph-structured data. While Graph Isomorphism Networks (GINs) have become the de facto encoders f…

- **[Adapting Qwen3 to Tajik from 0.6B to 8B: Lower Text Loss Did Not Mean Better Understanding](https://arxiv.org/abs/2611.06062v1)**
  - *Tohir Saidzoda, Madina Abdusalomzoda, Nasimjon Rajabov et al.*
  - `2026-11-04`
  - Small LoRA adapters trained on Tajik news and books lowered Qwen3's Tajik text loss at every size we tried, from 0.6B to 8B, by 0.60 to 1.45 nats per token, but none of them improved Tajik reading comprehension where it can be measured. On Belebele the 1.7B and 8B adapters left a…

- **[Trick-or-Treat: Adversarial Evaluation of Multimodal Medical Reasoning with Synthetic Images](https://arxiv.org/abs/2611.06631v1)**
  - *Oishi Banerjee, Eujin Lee, Sung Eun Kim et al.*
  - `2026-11-04`
  - We used medical image synthesis to create a challenging multimodal evaluation framework that exposes hallucination behaviors in frontier models. Evaluating multimodal reasoning has historically been difficult because existing medical datasets rarely pair different image modalitie…

- **[SVGFaith: A Two-Layer Meta-Evaluation of Faithfulness Metrics for Text-to-SVG Generation](https://arxiv.org/abs/2611.06048v1)**
  - *Guotao Liang, Haitao Zhou, Biao Liu et al.*
  - `2026-11-04`
  - Text-to-SVG systems are commonly evaluated by applying raster-image metrics to rasterised outputs, yet whether these scores capture fine-grained prompt faithfulness remains unclear. We introduce SVGFaith, a two-layer meta-evaluation framework in which the more faithful candidate…

- **[Route to Remember: Adaptive Memory Selection for LLM Agents](https://arxiv.org/abs/2611.05636v1)**
  - *Zeyu Fang, Jun Yin, Yongsheng Mei et al.*
  - `2026-11-03`
  - The memory of production agents is increasingly becoming a bottleneck and is built almost exclusively from text: key points are extracted from out-of-limit context and retrieved into context at query time. Therefore, every new query incurs an additional cost that grows with the a…

- **[Assurance-Conditioned Continuous Authorization for Autonomous AI Agents](https://arxiv.org/abs/2611.05632v1)**
  - *Mehdi Shajari*
  - `2026-11-03`
  - Autonomous software agents can act through tools, delegate work, and change their models or execution environments while earlier authorizations remain in flight. We present Assurance-Conditioned Continuous Authorization (ACCA), an approach designed to be harness-independent, for…

- **[ViBench 2.0: A Benchmark for Long-Horizon Software Building](https://arxiv.org/abs/2611.05620v1)**
  - *Daniel Furman, Preeya Kirani, Ibrahim Sheikh et al.*
  - `2026-11-03`
  - On Replit, our agentic engineering platform, users now build entire products without writing code, through successive feature requests to an agent. Yet existing coding benchmarks evaluate single, fully specified tasks, and many are near saturation. We introduce ViBench 2.0, a ben…

- **[VirtualTrialHarness: Coordinating Agentic Operationalization of Virtual Trial Protocols Across Complex Clinical Schemas](https://arxiv.org/abs/2611.05551v1)**
  - *Pengze Li, Jingna Feng, Yue Yu et al.*
  - `2026-11-03`
  - Virtual trials use routinely collected clinical data to evaluate treatment strategies, but translating a study protocol into an executable analysis requires determining how clinical concepts and study requirements should be represented in the available data and applied consistent…

- **[SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories](https://arxiv.org/abs/2611.05512v1)**
  - *Mingxuan Li, Huanzhi Mao, Ruitao Zheng et al.*
  - `2026-11-03`
  - AI Agents are becoming digital coworkers that can browse the web, write code, run experiments, and assist humans over extended horizons. Yet existing benchmarks fall short of real knowledge work: many rely on synthetic data or isolated tasks, missing the complex, multi-party dyna…

- **[Meta$^2$: Precomputing Reusable Knowledge for Online Harness Evolution in Long-Horizon Agents](https://arxiv.org/abs/2611.05139v1)**
  - *Lingzhi Yuan, Yiguang Cai, Weize Liu et al.*
  - `2026-11-03`
  - Harness optimization improves long-horizon agents by refining the prompts, tools, memory, and hooks around a frozen model. Offline methods can learn from completed trajectories, but deploy one shared harness that may overfit training tasks and cannot react to evidence revealed du…

- **[LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation](https://arxiv.org/abs/2611.04974v1)**
  - *Hong Je-Gal, Jinwoo Kim, Chanbin Yi et al.*
  - `2026-11-03`
  - We investigate the automated generation of executable robot reinforcement learning (RL) policies from natural-language task descriptions. Rather than using large language models (LLMs) as execution-time decision makers, we use them as designers that construct RL pipelines before…

- **[AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests](https://arxiv.org/abs/2611.04813v2)**
  - *Shu Zhou, Ziyang He, Yuxin Rao et al.*
  - `2026-11-03`
  - Financial agents are becoming an important class of real-world AI systems. Financial tasks vary widely in type and difficulty, and many are open-ended with no ground-truth answers. However, existing benchmarks neither capture this breadth and open-endedness nor separate grounding…

- **[Goal-Driven Autonomous Optical Experimentation via a Self-Recursive Hardware-Software Harness](https://arxiv.org/abs/2611.04481v1)**
  - *Tianxing Zhu, Huacheng Lu, Ming Liu et al.*
  - `2026-11-03`
  - We propose goal-driven self-recursive optical research in which agents use physical evidence to revise the hardware, software, models, and protocols used to pursue a scientific goal. The framework can be instantiated with different stimulus systems and measurement devices. We for…

- **[Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training](https://arxiv.org/abs/2611.04277v1)**
  - *Kangning Zhang, Wenxiang Jiao, Bowen Fang et al.*
  - `2026-11-03`
  - Harness evolution from a common base exhibits Locality, Complementarity, and Nonstationarity: variants repair different failures, and their utility changes as the policy learns. Rather than seeking a universally superior harness, we introduce Harness-S to selectively rescue failu…

- **[DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation](https://arxiv.org/abs/2611.04196v1)**
  - *Yuxuan Wang, Dadi Guo, Weijie Guo et al.*
  - `2026-11-03`
  - Frontier LLM agents can turn known vulnerabilities into working exploits, but are costly and often access-restricted due to their potential for malicious use. Open-weight models offer a more accessible alternative, but struggle to maintain progress across long exploitation chains…

- **[Validation-Gated ML Pipeline Synthesis with Expert-Grounded Self-Evolving Skills](https://arxiv.org/abs/2611.04180v1)**
  - *Zixiao Zhao, Jing Sun, Zhe Hou et al.*
  - `2026-11-03`
  - Recent advances in large language models have enabled agentic systems that automate machine learning pipeline construction from minimal user input. However, existing agentic AutoML methods either depend on rigid templates that limit adaptability, target narrow task domains, or re…

- **[The Agent Board: Kanban for Machines; Durable Coordination for Agents That Outlive the Conversation](https://arxiv.org/abs/2611.04100v1)**
  - *Tyler Hunt, Donald Nguyen, Gurbinder Gill*
  - `2026-11-03`
  - Harnesses for large language models have converged on a single-threaded shape: one agent, one history, one machine, one sitting. That shape fails work that spans many agents, outlives any one model call, or waits on systems that are not agents. We describe the Agent Board, the co…

- **[Cognitive Bias Signatures in Search-Equipped LLM Agents: A Stage-Resolved Analysis](https://arxiv.org/abs/2611.05720v1)**
  - *Yanru Xiao, Yingwei Yu*
  - `2026-11-03`
  - Search can help LLM agents correct mistakes, but their starting conditions may shape which evidence they find and use. Drawing on cognitive-bias paradigms, we develop a controlled search harness to examine result order, records of prior work, and initial hypotheses while holding…

- **[Verified but Vacuous: Three Failure Surfaces of LLM-Driven Verified Code Generation](https://arxiv.org/abs/2611.05590v1)**
  - *Aditya Vempaty, Himaneesh Sompalle, Manan Tayal et al.*
  - `2026-11-03`
  - What should ``verified'' mean when evaluating LLM-generated code? Many existing pipelines report a single verification number. We argue this collapses three distinct properties measured in a conditional audit sequence: verifier acceptance (Surface A), \emph{syntactic specificatio…

- **[MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](https://arxiv.org/abs/2611.05567v1)**
  - *Albert Wilcox, Frank Chang, Nhi Nguyen et al.*
  - `2026-11-03`
  - Despite growing interest in foundation models for robotic manipulation, systematic evaluation of their capabilities remains elusive. Existing benchmarks are either narrow and saturated, offering little signal on SOTA methods, broadly scoped, providing diversity at the cost of con…

- **[ScienceVision: Can AI Observe and Reason Like a Scientist?](https://arxiv.org/abs/2611.04087v1)**
  - *Tianyi Ma, Jing Gu, Haozhe Zhao et al.*
  - `2026-11-02`
  - Scientific discovery builds on accurate observations interpreted through domain knowledge and reasoning. For scientific 3D data, this requires understanding structures and spatial relationships, from protein contacts to anatomical organization. Existing multimodal benchmarks larg…

- **[WASP-Mem: Let Agent Organize Procedural Memory. Human Spend Effort on Diagnosis](https://arxiv.org/abs/2611.04003v1)**
  - *Peizhi Niu, Ge Shi, Vaibhav Gorde et al.*
  - `2026-11-02`
  - LLM agents struggle to automate complex enterprise procedures because static, pre-built harness cannot capture proprietary policies, undocumented behaviors, or state-dependent recovery paths that surface only during execution. Procedural memory accrued from agent experience offer…

- **[SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use](https://arxiv.org/abs/2611.03982v1)**
  - *Rongzhe Wei, Ge Shi, Min Cheng et al.*
  - `2026-11-02`
  - Enterprises increasingly want LLM agents to automate standard operating procedures over their software stacks -- mapping each step of a procedure to the right call among thousands of internal APIs, without hand-authored step-to-API mappings. The core difficulty is API selection a…

- **[El Agente Fármaco: A Scalable AI Scientist for Drug Discovery](https://arxiv.org/abs/2611.03832v1)**
  - *Marcel Müller, Mohammad Ghazi Vakili, Yoshihiro Ogura et al.*
  - `2026-11-02`
  - Computational drug discovery offers a growing range of tools for proposing and evaluating molecules, but combining them and deciding what to do next still requires substantial expert effort. Here, we introduce El Agente Fármaco, an AI scientist that uses modern large language mod…

- **[Rethinking Next-Visit Diagnosis Prediction Beyond Aggregate Metrics: Retrieval--Memory Multi-Agent Adjudication](https://arxiv.org/abs/2611.03826v1)**
  - *Heejoon Koo*
  - `2026-11-02`
  - Next-visit diagnosis prediction forecasts the diagnoses documented at a patient's next encounter, turning retrospective electronic health records into prospective clinical prediction. However, conventional aggregate evaluation obscures its multifaceted nature: distributionally, m…

- **[Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM for Investigative Analysis](https://arxiv.org/abs/2611.03434v1)**
  - *Shai Nahum Gefen, Vered Chassida, Dmitry Basin et al.*
  - `2026-11-02`
  - Government intelligence teams need LLM agents that can analyze large, messy evidence collections, but security and cost constraints often rule out hosted frontier models and broad, hard-to-audit tool surfaces. We report CLEO: Constrained Loop for Environment Optimization, a metho…

- **[DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412v2)**
  - *Yumou Liu, Mingju Chen, Zhoufutu Wen et al.*
  - `2026-11-02`
  - LLM agents are judged by what they deliver, and in professional work what gets delivered is a project, not a task. A project pays off only if the whole package holds, and one weak part can limit the value of the rest. Yet existing benchmarks mostly test agents on one task at a ti…

- **[Characterizing When Language Models Take Harmful Actions to Protect Their Assigned Goals](https://arxiv.org/abs/2611.03374v1)**
  - *Brandon Jaipersaud, Elliot Creager*
  - `2026-11-02`
  - Recent language model (LM) safety failures have largely been studied as disparate phenomena. In agentic misalignment, a model blackmails an executive to avoid being replaced. In alignment faking, it complies with harmful requests during training to keep its values from being modi…

- **[LLMs Depend on Specialist Tools for Out-of-Distribution Generalization in MS/MS Structural Elucidation](https://arxiv.org/abs/2611.03308v1)**
  - *Gabriel Asher, Cailum M. K. Stienstra, Tomo Oga et al.*
  - `2026-11-02`
  - A frontier language model was recently reported to solve 1D NMR structural elucidation without tools. We ask whether this capability transfers to tandem mass spectrometry (MS/MS) in the de novo setting, where the model must propose a structure directly from the spectrum without a…

- **[Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction](https://arxiv.org/abs/2611.03223v1)**
  - *Yiwei Zha, Qingyu Meng, Herbert Bos et al.*
  - `2026-11-02`
  - LLM agents compact long histories to fit their context windows, but the compacted context must still carry the operating rules that govern later actions. Prior work shows that violations rise after compaction, but measures compliance outside a complete agent harness and does not…

- **[Can Coding Agents Sustain Continual Evolution without Forgetting?](https://arxiv.org/abs/2611.03219v1)**
  - *Shangziqi Zhao, Yitong Zhang, Jia Li*
  - `2026-11-02`
  - Recently, harness self-evolution has emerged as an important paradigm for improving agent performance. Prior studies show that evolving the agent harness can effectively enhance agent capabilities without modifying the foundation model's parameters. We find that existing approach…

- **[CoworkOS:Scaling Agent Coworkers for Real-world Automation](https://arxiv.org/abs/2611.03178v1)**
  - *Jiajie Jin, Guanting Dong, Chengjun Pan et al.*
  - `2026-11-02`
  - Rapid advances in cowork agents are shifting human-AI collaboration toward real-world automation, delivering software, designs, and other artifacts. However, such productivity work demands both high-quality delivery on complex productivity tasks and continued monitoring and decis…

- **[TLAPS-Bench: Formally Proving Correctness of Real-World System Specifications with TLA+ Proof System](https://arxiv.org/abs/2611.02849v1)**
  - *Qian Cheng, Ruize Tang, Saad Mohammad Rafid Pial et al.*
  - `2026-11-02`
  - TLAPS-Bench is a benchmark and execution harness for constructing machine-checked proofs for real-world system specifications in TLA+ with agentic AI. Proving correctness of complex system specifications requires discovering inductive invariants, reasoning about intricate state t…

- **[CARE: Grounded Recursive Self-Improvement for Production Customer-Service Agents](https://arxiv.org/abs/2611.02839v1)**
  - *Yanbei Jiang, Chao Lei, Rena Gao et al.*
  - `2026-11-02`
  - Recursive self-improvement (RSI) in production agents involves transforming accumulated experience into reliable model updates while adapting to evolving business policies. We present CARE (Customer-service Agent Retrospective and Evolve), a grounded RSI framework that operationa…

- **[Reimagining computational quantum research with AI scientists](https://arxiv.org/abs/2611.02833v1)**
  - *Yuxuan Du, Hanqing Zhao, Xinbiao Wang et al.*
  - `2026-11-02`
  - AI scientists are expanding automated research across scientific domains, yet their ability to turn the scientific record into a foundation for autonomous discovery remains elusive. Here we uncover a fundamental barrier to this transition and demonstrate a route to overcome it in…

- **[SelfImprove-Bench: Evaluating Generalization in Self-Improving Agents](https://arxiv.org/abs/2611.02797v1)**
  - *Bangrui Xu, Jie Yang, Sidi Chen et al.*
  - `2026-11-02`
  - Recursively self-improving (RSI) systems are increasingly viewed as a promising means of accelerating progress toward artificial general intelligence. They aim to autonomously improve their capabilities by refining their working pipelines and recursively improving the strategies…

- **[GeoGuesser Bench: Benchmarking Vision-Language Agents on Interactive Geolocation](https://arxiv.org/abs/2611.02698v1)**
  - *Huanzhi Mao, Yichuan Wang, Michael Koo et al.*
  - `2026-11-02`
  - Vision-language model (VLM) agents that act in the open world need two abilities: world knowledge to interpret what they see, and exploration to find what they cannot yet see. We study how agents combine the two through interactive visual geolocation. GeoGuesser Bench contains 28…

- **[Widening Harm Evaluation Coverage with a Judge that Reads the World](https://arxiv.org/abs/2611.02624v1)**
  - *Prabhpreet Singh Setia, Bhavesh Neekhra, Debayan Gupta*
  - `2026-11-02`
  - An agent acting in a stateful environment can leave evidence of harm in two places: the record of what it did and said, or the world it changed. Safety evaluations for discovering harm examine one or the other in limited ways, using either an LLM judge over the trajectory or dete…

- **[EEFA: A Framework for the Ethical Evaluation of AI Agents](https://arxiv.org/abs/2611.02561v1)**
  - *Swathi Pallikala, Yashas Hariprasad*
  - `2026-11-02`
  - The rapid deployment of autonomous AI agents across consequential domains including healthcare, legal services, nancial management, and enterprise workows has created an urgent governance challenge. While the eld of AI evaluation has produced sophisticated benchmarks for measurin…

- **[RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild](https://arxiv.org/abs/2611.02497v1)**
  - *Tan Sang Nguyen, Yi Ru Wang, Shailesh Shailesh et al.*
  - `2026-11-02`
  - General-purpose robot policies must work across robots, tasks, and environments, yet the variation that makes physical trials informative also makes them difficult to reproduce. We introduce RoboColosseum, a distributed evaluation framework that combines unified policy serving an…

- **[Harvesting SWE Benchmarks from Wild Vibe Coding Sessions](https://arxiv.org/abs/2611.02440v1)**
  - *Ao Lu, Yuanhao Zeng, Shaocheng Lan et al.*
  - `2026-11-02`
  - Development teams need reproducible tasks from their own repositories and workflows to evaluate coding agents. Conversational developer-agent collaboration ("vibe coding") produces abundant coding sessions and repository checkpoints, but requirements evolve across turns, unrelate…

- **[HLSClaw: Bringing Vibe Coding to High-Level Synthesis through Skill-Based Agentic Harness](https://arxiv.org/abs/2611.02784v1)**
  - *Jinming Ge, Shang Liu, Jiawei Liang et al.*
  - `2026-11-02`
  - LLM agents are rapidly shifting software development toward intent-driven \emph{vibe coding}, yet their effectiveness drops sharply in high-level synthesis (HLS), where code optimization must jointly consider design structure, directive search, and downstream hardware constraints…

- **[EvoGroup: A Self-Evolving Harness for Group Agents in Shared Contexts](https://arxiv.org/abs/2611.03868v1)**
  - *Xinyi Xu, Xiaoyang Li, Yucheng Feng et al.*
  - `2026-11-02`
  - With the rise of Group Agent such as Claude Tag, agents increasingly serve as digital workers for long-term team collaboration. These agents operate over shared contexts that continuously accumulate through multi-user interactions. However, existing agent memory systems are mainl…

- **[VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](https://arxiv.org/abs/2611.03575v1)**
  - *Wei-Lin Chen, Zhepei Wei, Xinyu Zhu et al.*
  - `2026-11-02`
  - Large language model (LLM) coding agents increasingly operate with shell access, allowing them to write scripts, move files, alter permissions, and modify system configurations. However, an agent may achieve a user's goal while causing unintended harm, such as deleting unrelated…

- **[Camera Radar LiDAR Fusion via Point-Cloud Projection for Multi-Task Learning](https://arxiv.org/abs/2611.03942v1)**
  - *Kavin Chandrasekaran, Sorin Grigorescu*
  - `2026-11-02`
  - Autonomous vehicles require robust perception systems to operate safely under diverse environmental conditions. While cameras provide high-resolution visual data, their performance significantly degrades in low-light and adverse weather. High Definition (HD) radar offers superior…

- **[InteractionBench: Measuring Timing, Task Accuracy, Whisper and Volume, and Grounding in Real-Time Voice Systems](https://arxiv.org/abs/2611.02430v1)**
  - *Richard Yucheng He, Chen Xu, Yihang Liu et al.*
  - `2026-11-02`
  - Most benchmarks for real-time voice systems focus on one aspect, such as turn-taking, instruction following, paralinguistic control, or conversational memory, each with its own data and set of systems. We present InteractionBench, a benchmark and evaluation harness that measures…

- **[Evaluating Uncertainty Calibration in Probabilistic Time Series Foundation Models](https://arxiv.org/abs/2611.03592v1)**
  - *Thomas Decker, Volker Tresp*
  - `2026-11-02`
  - Time series foundation models (TSFMs) are increasingly used for probabilistic forecasting across diverse domains, yet the reliability of their uncertainty estimates remains poorly understood. In this work, we study uncertainty calibration in probabilistic TSFMs from a broader met…

- **[MetaPOCS: Meta-Learned Multi-Exit Unfolding for Budget-Aware Seismic Data Interpolation](https://arxiv.org/abs/2611.02478v1)**
  - *Baisong Jiang, Chunxia Zhang, Xiaoli Wei et al.*
  - `2026-11-02`
  - Seismic data interpolation must reconcile reconstruction fidelity with the computational budgets of acquisition quality control and subsequent imaging. Fixed-depth unfolding networks are optimized for a single operating point, whereas their intermediate estimates may be insuffici…

- **[A Scientific Claim Stability Framework for Evaluating MRI Morphometry Pipelines](https://arxiv.org/abs/2611.02413v1)**
  - *Duy-Cat Can, Dang-Duat Tran, Anh-Khang Nguyen et al.*
  - `2026-11-02`
  - MRI morphometry pipelines are often evaluated by measurement agreement or downstream accuracy, yet their scientific value depends on the conclusions they support. Two pipelines can produce similar feature-level results yet support different conclusions about aging, cognitive decl…

- **[Same Outputs, Different Scores: Auditing the Unchecked Graders of Multimodal LLM Benchmarks](https://arxiv.org/abs/2611.03377v1)**
  - *Ahmad Jarjis Hasan, Jonathan Lwowski*
  - `2026-11-02`
  - Every multimodal-LLM multiple-choice benchmark ends with a scoring rule that converts a model's response, often free-form text rather than a clean option letter, into a right/wrong verdict, buried in its code. Unlike the dataset, this rule is chosen without justification and left…

- **[ENGINE: Endogenous Variational MultiScale Optimization for Zeroth-Order LLM Fine-Tuning](https://arxiv.org/abs/2611.03293v1)**
  - *Zhuoli Ouyang, Changxi Chi, Siyuan Li et al.*
  - `2026-11-02`
  - Zeroth-order (ZO) optimization enables memory-efficient large language model (LLM) fine-tuning, and recent methods incorporate curvature-aware strategies. However, in the high-dimensional parameter space of LLMs, these methods inherently suffer from exploding gradient variance an…

- **[CAST-Bench: Tracing Every Sound to Its Source in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2611.05422v1)**
  - *Yucong Liu, Qi Tian, Shuyuan Tu et al.*
  - `2026-11-02`
  - Existing benchmarks for joint text-to-audio-video (T2AV) generation evaluate perceptual quality and audiovisual alignment, but balanced sound-source sam?pling and separate reporting by shot structure remain limited. This makes it dif?ficult to determine whether a specific sound i…

- **[Efficient Closure Learning in Dynamical Systems: A Comparison of Data-Assimilated and Embedded Approaches](https://arxiv.org/abs/2611.03612v1)**
  - *Rileigh Bandy, Teresa Portone, Mohammad Khalil et al.*
  - `2026-11-02`
  - Increased computing power has transformed computational science and improved predictive capabilities for complex systems, but many phenomena still exceed current simulation capabilities or require rapid evaluations for fast design iterations. Closure models address this challenge…


## Finance  (189)

### AAAI

- **[D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies](https://arxiv.org/abs/2511.16590)**
  - *Sen Chen, Tong Zhao, Yi Bin et al.*
  - **AAAI 2025** · `2025-11-20`
  - Developing intelligent agents capable of operating a wide range of Graphical User Interfaces (GUIs) with human-level proficiency is a key milestone on the path toward Artificial General Intelligence. While most existing datasets and benchmarks for training and evaluating GUI agen…

- **[DHMoE: Diffusion Generated Hierarchical Multi-Granular Expertise for Stock Prediction](https://doi.org/10.1609/aaai.v39i11.33250)**
  - *Weijun Chen, Yan-Ze Wang*
  - **AAAI 2025** · `2025-04-11`
  - Stock prediction stands as a pivotal research objective within the Fintech. Existing deep learning research revolves around the development and scaling of one individual neural network predictor. However, in the dynamic and noisy landscape of the stock market, reliance solely on…

- **[Can We Trust AI Benchmarks? An Interdisciplinary Review of Current Issues in AI Evaluation](https://arxiv.org/abs/2502.06559)**
  - *Maria Eriksson, Erasmo Purificato, Arman Noroozian et al.*
  - **AAAI 2025** · `2025-02-10`
  - Quantitative Artificial Intelligence (AI) Benchmarks have
emerged as fundamental tools for evaluating the
performance, capability, and safety of AI models and
systems. Currently, they shape the direction of AI
development and are playing an increasingly prominent role
in regulato…


### NeurIPS

- **[The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets](https://openreview.net/forum?id=XZpIu68yW6)**
  - *Shenzhe Zhu, Jiao Sun, Yi Nian et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-01`
  - AI agents are increasingly used in consumer-facing applications to assist with tasks such as product search, negotiation, and transaction execution. In this paper, we investigate a future setting where both consumers and merchants authorize AI agents to automate the negotiations…


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


### ICLR

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **ICLR 2026** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…


### KDD

- **[AFABench: A Generic Framework for Benchmarking Active Feature Acquisition](https://arxiv.org/abs/2508.14734)**
  - *Valter Schütz, Han Wu, Reza Rezvan et al.*
  - **KDD 2025** · `2025-08-20`
  - In many real-world scenarios, acquiring all features of a data instance can be expensive or impractical due to monetary cost, latency, or privacy concerns. Active Feature Acquisition (AFA) addresses this challenge by dynamically selecting a subset of informative features for each…

- **[Progressive Dependency Representation Learning for Stock Ranking in Uncertain Risk Contrasting](https://www.semanticscholar.org/paper/55881a648fae1fc3748022a08e5b1a0f52a98925)**
  - *Li Huang, Yan-Zhe Xie, Qiang Gao et al.*
  - **KDD 2025** · `2025-07-20`
  - The practice of ranking a list of stocks to facilitate investment decisions has garnered a lot of attention in the fintech field, aiming at minimizing investment risk while maximizing profitable returns. With recent developments in deep representation learning such as temporal/re…


### ACL

- **[FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation](https://arxiv.org/abs/2505.24714)**
  - *Junyu Luo, Zhi-Zhuo Kou, Liming Yang et al.*
  - **ACL 2025** · `2025-05-30`
  - Multimodal Large Language Models (MLLMs) have experienced rapid development in recent years. However, in the financial domain, there is a notable lack of effective and specialized multimodal evaluation datasets. To advance the development of MLLMs in the finance domain, we introd…


### Other / arXiv

- **[WayPOP: A Panoramic Open-Set Panoptic Tracking Benchmark](https://arxiv.org/abs/2611.05801)**
  - *Rohit Mohan, Maximilian Luz, Swarnava Chowdhury et al.*
  - 🤗 · `2026-11-04`
  - Holistic perception for autonomous agents requires reliably segmenting and associating scene elements across time and camera views, including objects outside a fixed semantic taxonomy. Existing open-set panoptic benchmarks focus on individual images or views, while panoramic trac…

- **[LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks](https://arxiv.org/abs/2611.06687v1)**
  - *Jenny Yang, Elizabeth Proehl, Anjan Bharadwaj et al.*
  - `2026-11-04`
  - We introduce LifeVal, a benchmark evaluating AI model performance on personalized agentic consumer tasks. LifeVal covers the most valuable life tasks that a personalized digital superassistant could automate, representing over 1.7 trillion US dollars in annual willingness-to-pay…

- **[Zero-Shot Coordination among LLM Agents](https://arxiv.org/abs/2611.06409v1)**
  - *Adrian Hayler, Shashank Reddy Chirra, Andrei Lupu et al.*
  - `2026-11-04`
  - We study zero-shot coordination (ZSC), where independently developed agents must coordinate at test time. While ZSC has been well studied in the RL literature, far less is known about the performance of LLM agents despite their increasing deployment in such settings. Existing wor…

- **[From hydrological laws to catchment models: A process-based model matches deep-learning accuracy on three continents](https://arxiv.org/abs/2611.06382v1)**
  - *Xilin Xia*
  - `2026-11-04`
  - Dooge asked whether hydrology has laws at the catchment scale. We ask whether a low-dimensional system built under physical laws can match the accuracy of neural networks that outperform process-based models on the same inputs. Three laws constrain a lumped catchment model. Conse…

- **[A Definition of Catastrophic Performance](https://arxiv.org/abs/2611.06219v1)**
  - *Henrik Marklund, Alex Infanger, Benjamin Van Roy*
  - `2026-11-04`
  - A central challenge in AI is specifying objectives that align with human preferences. While existing theoretical results elucidate how misspecification impacts performance, they typically do not distinguish between merely suboptimal and catastrophic outcomes. To enable rigorous a…

- **[ModalSearcher: Weaving Visual Evidence into Autonomous Cross-Modal Deep Search](https://arxiv.org/abs/2611.06131v1)**
  - *Zhihan Yin, Ruyi Li, Chengyu Fang et al.*
  - `2026-11-04`
  - Static and incomplete parametric knowledge limits the performance of multimodal large language models on novel-knowledge and knowledge-intensive tasks, especially those requiring multi-hop evidence acquisition. Existing multimodal agentic search methods often fix visual evidence…

- **[The Harness Is the Model: Agent Scaffolding Changes a Fixed LLM's Compliance with Banking Conduct Rules, Unevenly Across Models](https://arxiv.org/abs/2611.06116v1)**
  - *Mehmet Murat Huyut*
  - `2026-11-04`
  - Banks validate language models, but they deploy systems: a model inside a harness that decides what it sees, which tools it can call and who checks its actions. We test whether that harness changes compliance with banking conduct rules when the model is held fixed. Four open-weig…

- **[Autonomous agents for electricity-system planning](https://arxiv.org/abs/2611.05911v1)**
  - *Yoon Pyo Lee, Samrendra Roy, Jay Phil Yoo et al.*
  - `2026-11-04`
  - Planning electricity systems requires repeated decisions that connect regional resources, investment, operation and network constraints. Here we present an autonomous planning framework that carries prepared regional scenarios through proposal, numerical evaluation, feedback inte…

- **[Autonomy and Coordination in Intelligent Manufacturing: A Recursive Autonomous Agent Framework](https://arxiv.org/abs/2611.05828v1)**
  - *Yuning Chen, Hongda Zhang, Linqiang Hu et al.*
  - `2026-11-04`
  - Intelligent production requires systems to make decisions and organize work according to production goals and operating conditions. It also requires continuous adjustment through feedback. This paper analyzes intelligence in human production organizations from a complex adaptive…

- **[GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802v1)**
  - *Mohan Cao, Yongsen Mao, Chucheng Xiang et al.*
  - `2026-11-04`
  - Recent LLM-centric advances can generate attractive furnished rooms by selecting and arranging assets. Yet evaluation remains limited to specific perspectives or predefined questions, failing to reflect overall scene quality. To address this pressing need, we introduce GREP. Its…

- **[DARE: Difficulty Analysis for Repair Enhancement](https://arxiv.org/abs/2611.05797v1)**
  - *Jikwang Lee, Seungwook Jung, Jaechang Nam*
  - `2026-11-04`
  - LLM-based coding agents are primarily evaluated by their solve rates. However, this metric does not reveal how difficult the solved tasks are or account for differences intask difficulty across benchmarks. Determining the difficulty of individual tasks by repeatedly running multi…

- **[A Framework for Context Enrichment and Selective Robustness in LLM Social Agents](https://arxiv.org/abs/2611.06914v1)**
  - *Mattia Greiche, Reihaneh Rabbany, Maximilian Puelma Touzel*
  - `2026-11-04`
  - Researchers use large language models as agents in social simulations, where agents are prompted with observations and background information intended to shape their actions. Yet LLM agents have been shown to substantially change their behavior under meaning-preserving prompt var…

- **[TandemBench: Benchmarking Decision Models for Multi-Agent Collaboration](https://arxiv.org/abs/2611.05827v1)**
  - *Baohang Li, Xiaocheng Feng, Bing Qin*
  - `2026-11-04`
  - Decision models choose among predefined options in tasks such as routing and action selection. In multi-agent collaboration, a decision determines how members divide work, exchange resources, and act in parallel. We introduce TandemBench, a benchmark of 1,200 questions in multi-a…

- **[Continual Classification Beyond the Kernel Regime: Harnessing the Sparsity Bias of L2 Regularization in Diagonal Linear Networks](https://arxiv.org/abs/2611.06759v1)**
  - *Gilad Karpel, Itay Evron, Ron Meir et al.*
  - `2026-11-04`
  - We study logistic regression for continual learning with linear predictors in a high-dimensional statistical setting. Existing theoretical work has largely focused on continual linear regression with variants of L2 regularization, motivated by their analytical simplicity and conn…

- **[An Interaction-Aware Decision Framework for FDIC-Assisted Distressed Bank Acquisitions: Empirical Evidence from the FDIC Failed-Bank Panel and the SVB-First Citizens Case](https://arxiv.org/abs/2611.06514v1)**
  - *Yousef Nejatbakhsh, Malihe Aliasgari, Parsa Safaee et al.*
  - `2026-11-04`
  - Acquirers of failed banks weigh acquisition value, regulatory protection, risk, buyer strength, and execution difficulty jointly, because each signal's meaning depends on the others: high non-performing loans matter less when government loss sharing absorbs the losses. The propos…

- **[The Alignment Tax Is Graded: Task-Selective Capability Loss Under Length-Normalized DPO with SFT Retention](https://arxiv.org/abs/2611.06476v1)**
  - *Ye Yuan*
  - `2026-11-04`
  - Setting. This is an empirical characterization study; we propose no new method and run no comparisons against alternative objectives. We fine-tune Qwen3.5-4B with sparse LoRA and length-normalized DPO plus an SFT retention term (the RPO objective) on structured financial-filing t…

- **[Constrained defined-contribution pension management: A reparameterized neural network approach](https://arxiv.org/abs/2611.06495v1)**
  - *Yueman Feng, Wenyuan Li*
  - `2026-11-04`
  - This paper studies constrained defined contribution (DC) pension management under a two-factor financial market model. The pension participant is allowed to invest in cash, two nominal bonds, an inflation-linked bond, and a stock index. Moreover, they can also purchase term life…

- **[Risk Control Certifies Rates, Not Magnitudes: An Audit of Selective Fetal Biometry](https://arxiv.org/abs/2611.05851v1)**
  - *Zhengshuai Yang, Linna Jiang, Changyun Li et al.*
  - `2026-11-04`
  - Prenatal ultrasound biometry must return a head circumference (HC) and refuse when the image cannot support one. Selective prediction trades coverage against error, but its finite-sample guarantees bound the rate of gross errors, not their magnitude. We audit a tool-grounded biom…

- **[Vision Paper: Why Distributed LLM Post-Training and Decentralized Alignment Are Now Essential](https://arxiv.org/abs/2611.05841v1)**
  - *Zhanhong Jiang, Qisai Liu, Soumik Sarkar*
  - `2026-11-04`
  - This vision paper argues that distributed learning, including federated and decentralized, should become a first-class paradigm in LLM post-training, not merely a privacy add-on. Current methods like RLHF and DPO rest on an invisible assumption: preference data should be centrali…

- **[Short-Term Forecasting of Heterogeneous Wind Power Fleets: Global Temporal Fusion Transformer Leveraging Static Covariates](https://arxiv.org/abs/2611.06130v1)**
  - *Viktor Walter, Andreas Wagner*
  - `2026-11-04`
  - Accurate short-term wind power forecasting is critical for grid stability and electricity trading. While transformer-based deep learning is state of the art, industry practice relies mostly on local models trained for individual assets. This study investigates whether a global te…

- **[Timing is Everything: Inferring Temporal Membership in Continually Updated Models](https://arxiv.org/abs/2611.05781v1)**
  - *Jie Fu, Xiangpeng Deng, Yuan Hong et al.*
  - `2026-11-04`
  - Continual model updating has become a common practice in the deployment of machine learning systems. However, the dynamic training behaviors give rise to new risks not sufficiently addressed by existing studies. In this paper, we present the first systematic study of temporal pri…

- **[Hard to Fool: A Bounded LLM Research Loop for Quantitative Finance, and What Two Dozen Campaigns Found](https://arxiv.org/abs/2611.06607v1)**
  - *Henry Zhang*
  - `2026-11-04`
  - Agentic research loops that let a language model propose a change, run a fixed experiment and keep whatever improves the metric work well in machine learning. In trading research the same loop is a machine for producing false discoveries: a backtest that "improves the metric" is,…

- **[Combining Relevant Expert Knowledge Using Mixtures of Feedback Fuzzy Cognitive Maps](https://arxiv.org/abs/2611.05664v1)**
  - *Olaoluwa Adigun, Akash Kumar Panda, Bart Kosko*
  - `2026-11-03`
  - A neuro-symbolic system should combine only relevant answers from expert agents or other knowledge sources. Using only relevant experts for a given input query becomes ever more important for accuracy and scalability as the knowledge network grows and connects ever more knowledge…

- **[Assurance-Conditioned Continuous Authorization for Autonomous AI Agents](https://arxiv.org/abs/2611.05632v1)**
  - *Mehdi Shajari*
  - `2026-11-03`
  - Autonomous software agents can act through tools, delegate work, and change their models or execution environments while earlier authorizations remain in flight. We present Assurance-Conditioned Continuous Authorization (ACCA), an approach designed to be harness-independent, for…

- **[Anduin: A sybil-resistant agentic marketplace reputation system](https://arxiv.org/abs/2611.05586v1)**
  - *Reza Ramji, Preston Vander Vos, Ziming Zeng et al.*
  - `2026-11-03`
  - As autonomous AI agents enter permissionless onchain markets, selecting new service providers remains a core challenge. Existing reputation systems depend on scarce resources like human curation, identity credentials, or voluntary reviews, while naive volume rankings are vulnerab…

- **[Jev with Foresight: Safe Language-Guided Autonomous Driving via a Language World Model](https://arxiv.org/abs/2611.05448v1)**
  - *Yansong Qu, Jiancong Chen, Samuel Labi*
  - `2026-11-03`
  - Large language models understand passengers' driving commands, but as driving agents they reason in generated text for seconds and must infer each action's consequences implicitly from the scene. We present Jev-AD, which pairs Jev, a typed decision model that answers predefined q…

- **[Artifact-to-Capability: Diagnosing Breaks in Capability Formation of Self-Evolving Agents in a Controlled Environment](https://arxiv.org/abs/2611.04952v1)**
  - *Ziqian Ban, Haoxiang Yang, Yanfei Zhang et al.*
  - `2026-11-03`
  - Self-evolving agents write interaction experience into artifacts and reuse them in later tasks. Most work supports such methods with three proxy signals: artifacts accumulate, behavior changes once they are loaded, and metrics rise. We call this signal-based evaluation. What thes…

- **[ScamWorld: An Interactive Environment for Evaluating Web Agents Against Online Fraud](https://arxiv.org/abs/2611.04879v2)**
  - *Yutao Wu, Xiao Liu, Ming Wen et al.*
  - `2026-11-03`
  - Web agents increasingly browse, shop, and manage accounts on behalf of their users. Prior work has shown that they can be misled by adversarial content, including prompt injections and deceptive interfaces. Beyond such attacks, agents operating on the open web also encounter onli…

- **[AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests](https://arxiv.org/abs/2611.04813v2)**
  - *Shu Zhou, Ziyang He, Yuxin Rao et al.*
  - `2026-11-03`
  - Financial agents are becoming an important class of real-world AI systems. Financial tasks vary widely in type and difficulty, and many are open-ended with no ground-truth answers. However, existing benchmarks neither capture this breadth and open-endedness nor separate grounding…

- **[Learnings and Pitfalls from AI-Assisted A/B Experimentation at Scale](https://arxiv.org/abs/2611.04515v1)**
  - *Brett Daley, Ilya Gorbachev, Anubhav Natani et al.*
  - `2026-11-03`
  - A/B testing underpins product decisions by providing trustworthy, reproducible quantification of proposed changes' effects. Growing large language model (LLM) capabilities have motivated efforts to automate experimentation workflows. Yet LLMs are nondeterministic and prone to hal…

- **[Signals: Continuous Diagnostics of AI Agents](https://arxiv.org/abs/2611.04507v2)**
  - *Amey Rambatla, Vatsal Goel, Sagar Gaur et al.*
  - `2026-11-03`
  - AI agents can make incorrect decisions or waste resources even when their tools and infrastructure work normally. Their nondeterministic behavior makes these problems difficult to reproduce and diagnose. We developed Signals to identify such problems from agentic traces and sugge…

- **[Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI](https://arxiv.org/abs/2611.04315v1)**
  - *Vishal Pramanik, Maisha Maliha, Susmit Jha et al.*
  - `2026-11-03`
  - Long-horizon multi-agent systems suffer from three tightly coupled failures: task drift, role drift, and state staleness. We test the hypothesis that these share a common representational cause: agent hidden states move away from the directions encoding the active task, assigned…

- **[DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution](https://arxiv.org/abs/2611.04226v1)**
  - *Renkai Yi, Yuwei Wu, Haoyu Zhang et al.*
  - `2026-11-03`
  - Disturbances can invalidate the conditions required by a robot's next action even when much of its task program remains useful. A recovery system must therefore choose a response suited to the current state. We present DiMuRe (diagnosis-guided multilevel recovery), a framework fo…

- **[ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends](https://arxiv.org/abs/2611.04104v1)**
  - *Shengjun Kris Dong, Dima Nikiforov, Sahil Modi et al.*
  - `2026-11-03`
  - Optimizing accelerator code across hardware architectures is difficult. ML compilers search predefined spaces of schedules and micro-kernels, while LLM-guided optimization can explore alternative algorithms, operator decompositions, and hardware-specific techniques. However, exis…

- **[When Is Fresh AI Stock Analysis Worth It? Allocating a Limited Research Budget Across Price Updates, Deep Forecast Refreshes, and Editorial Reviews of Top Stock Picks](https://arxiv.org/abs/2611.04348v2)**
  - *Russlan Ramdowar*
  - `2026-11-03`
  - When is another AI research run worth more than keeping that money invested? Using 8,120 iPulse AI reports that consumed nearly 100 million output and reasoning tokens on the same 203 stocks across four production batches, we compare repricing old targets (with and without shock…

- **[Verified but Vacuous: Three Failure Surfaces of LLM-Driven Verified Code Generation](https://arxiv.org/abs/2611.05590v1)**
  - *Aditya Vempaty, Himaneesh Sompalle, Manan Tayal et al.*
  - `2026-11-03`
  - What should ``verified'' mean when evaluating LLM-generated code? Many existing pipelines report a single verification number. We argue this collapses three distinct properties measured in a conditional audit sequence: verifier acceptance (Surface A), \emph{syntactic specificatio…

- **[Pairing Expert Critique with LLM-Driven Refinement: An Iterative Approach for Curating Quality AI Evaluation Datasets](https://arxiv.org/abs/2611.05749v1)**
  - *Honson Ling, Kidus Admassu, Stephanie Rosenthal*
  - `2026-11-03`
  - Evaluating and improving domain-specific LLM responses requires high-quality reference data and rubrics, yet expert authoring is slow and expensive, and synthetic datasets may fail to capture practitioner preferences unless they are grounded in expert judgment. We present SME-C (…

- **[Reconstructing Fraudulent Strategies in Online Payments via Interpretable Inverse Reinforcement Learning](https://arxiv.org/abs/2611.04819v1)**
  - *Huilin He, Weiyu Han, Linbo Shao et al.*
  - `2026-11-03`
  - Payment fraud causes financial losses and undermines users' trust in web payment services. Although fraud detection is a critical defense for payment security, complex and diverse fraudulent behaviors can still evade detection. Generating fraud samples for data augmentation can b…

- **[Kierston & KierstonBench: Simulation of Allentown, PA and Evaluation of Language Models in Crime Investigation and Surveillance Tasks](https://arxiv.org/abs/2611.04785v1)**
  - *Andrew Semenov, Svyatoslav Dorofeev*
  - `2026-11-03`
  - Large language models are candidates for collecting and analyzing records in criminal investigations and mass surveillance. Their capability and accuracy in this work cannot currently be measured. Real deployments lack the ground truth needed to score a model's conclusions, and n…

- **[TAPES: Task-Aligned Joint Predictive Pretraining for Transaction Event Sequences](https://arxiv.org/abs/2611.04747v1)**
  - *Ruobing Zuo, Weiyu Han, Huilin He et al.*
  - `2026-11-03`
  - Transaction event sequences support diverse prediction tasks in online commerce and digital financial services. The same transaction records can yield prediction targets with different semantics, including values, changes, and relations to past events. These targets impose differ…

- **[CosmosAlpha: Multi-Relational Graph Search with Pareto-Guided Exploration for LLM-Driven Alpha Mining](https://arxiv.org/abs/2611.04555v1)**
  - *Zhan-He Wang, Zi-Yang Lang, Yi-Yang Li et al.*
  - `2026-11-03`
  - Discovering predictive alpha factors from noisy financial data is a fundamental yet challenging problem in quantitative finance. LLM-driven formulaic alpha mining offers an attractive paradigm by combining interpretable symbolic expressions with iterative generation and refinemen…

- **[Generative Modeling for Cascading Extremes via Autoregressive Transformers](https://arxiv.org/abs/2611.05728v1)**
  - *Miguel de Carvalho, Myung Won Lee, Jordan Richards et al.*
  - `2026-11-03`
  - Extreme events often occur sequentially, from earthquake-tsunami cascades to successive extreme losses in financial markets. We introduce an extremal token representation that encodes multivariate observations as a categorical sequence. A quiet token records the absence of thresh…

- **[LENS: Reliability-Aware Stock Prediction via LLM-Extracted Priors and News-Driven Semantic Graphs](https://arxiv.org/abs/2611.04217v1)**
  - *Hao Zhou, Tiejun Ma, Luis Felipe Costa Sperb*
  - `2026-11-03`
  - Predicting stock returns requires modeling persistent company relations and time-varying market signals. Graph Neural Network (GNN) approaches combine static priors with dynamic relational graphs, but treat every extracted edge as a trustworthy binary fact, ignoring heterogeneous…

- **[Decomposing Rank Reversals under Temporal Nonstationarity: Alignment, Aggressiveness, and Instability](https://arxiv.org/abs/2611.04116v1)**
  - *Deying Song, Xueying Ding*
  - `2026-11-03`
  - Under temporal nonstationarity, model performance rankings reverse across training horizons due to heterogeneous sensitivities to memory. While existing literature addresses adaptive lookbacks, effective model complexity, and empirical forecast evaluation in isolation, no unified…

- **[Aggregate Calibration Can Mask Stress-State Undercoverage: Bounded-Memory Forecast Intervals under Recurrent Financial Stress](https://arxiv.org/abs/2611.04223v1)**
  - *Ruihang Han, Li-Hsiang Lin*
  - `2026-11-03`
  - Sequential forecast intervals are often evaluated by aggregate coverage even when calibration memory is bounded. This can be misleading when economically important states recur after long absences: a recent-only buffer may satisfy its overall coverage target while no longer conta…

- **[Multidimensional Views Behind Target-Price Revisions: An LLM-Based Representation of Analyst Outlooks](https://arxiv.org/abs/2611.04119v1)**
  - *Kiyoun Kim, Sung-Yeon Nathan Lim*
  - `2026-11-03`
  - A target price compresses an analyst's multidimensional views into a single number. We propose an LLM-based text representation that extracts these views from research reports as question-based outlook scores with supporting evidence. The questions organize reported views on earn…

- **[Impact of Input Resolution in Mammographic Mass Detection: A Controlled Multi-Architecture Study](https://arxiv.org/abs/2611.04200v1)**
  - *Kaan Buyukdemirci, Emine Ulku Saritas*
  - `2026-11-03`
  - Deep-learning-based mass detectors usually downsample mammograms, trading fine image detail for lower computational cost. However, published studies cannot reveal how much accuracy this trade-off sacrifices, since they also differ in architecture, preprocessing, and evaluation pr…

- **[Hierarchical Intelligent Evolutionary Optimization for UAV-Assisted NOMA-MEC Systems](https://arxiv.org/abs/2611.04474v1)**
  - *Yaxuan Jiao, Jiaxuan Lv, Jyoti Sahni et al.*
  - `2026-11-03`
  - The integration of unmanned aerial vehicles (UAVs), mobile edge computing (MEC) and non-orthogonal multiple access (NOMA) provides an effective solution for computation-intensive and latency-sensitive services in infrastructure-deficient environments. However, the joint optimizat…

- **[Beyond Anonymous Order Flow: Wallet Identity as a Feature for Short-Horizon Return Prediction](https://arxiv.org/abs/2611.05218v1)**
  - *Jingqiu Ding, Daojing Zhai*
  - `2026-11-03`
  - Conventional public order-book data summarize trading without identifying the accounts behind it. Hyperliquid's Level-4 record also exposes persistent pseudonymous wallet addresses. We reconstruct full-depth books from consensus-ordered messages and evaluate wallet identity as a…

- **[How market volatility responds to a preceding price trend: a lag-resolved measurement in cryptocurrencies and equities](https://arxiv.org/abs/2611.04533v1)**
  - *Gulsah Bicki, Taylan Akdogan*
  - `2026-11-03`
  - We quantify the response of market volatility to a preceding price trend as a function of lag at minute resolution. The asymmetry of the response is investigated. The sample consists of trades in three of the largest cryptocurrencies on a single exchange and in three large US sto…

- **[Estimating "Realized" Skewness using Convolutional Neural Network](https://arxiv.org/abs/2611.04598v1)**
  - *Haozhe Jiang, Ostap Okhrin, Michael Rockinger*
  - `2026-11-03`
  - We propose a new estimator of low-frequency skewness (monthly) that exploits high-frequency data (5 min) through a direct functional mapping consisting of layers of Convolutional Neural Networks followed by Multi Layer Perceptrons. Monte Carlo experiments involving stochastic vol…

- **[Safe Portfolio Learning from Untrusted Predictions: Signed Trust, Abstention, and Cross-Universe Polarity Failure](https://arxiv.org/abs/2611.04826v1)**
  - *Amirhossein MohammadpourAzari, Mohammad Zarei, MohammadAmin Fazli*
  - `2026-11-03`
  - Portfolio use of machine predictions must often proceed while the predictions' economic direction, reliability, and timing remain untrusted, and while feedback from overlapping multi-period positions arrives with delay. A controller chooses among Safe, Follow, and Reverse portfol…

- **[Characterizing Adversarial GEO via Implicit Brand Injection](https://arxiv.org/abs/2611.04005v1)**
  - *Shobhnik Kriplani, Haohan Wang*
  - `2026-11-02`
  - Generative search engines increasingly shape how users discover products, services, and commercial entities by generating answers from retrieved web content. This creates an opportunity to influence which brands appear in these answers by modifying the content available to the re…

- **[WASP-Mem: Let Agent Organize Procedural Memory. Human Spend Effort on Diagnosis](https://arxiv.org/abs/2611.04003v1)**
  - *Peizhi Niu, Ge Shi, Vaibhav Gorde et al.*
  - `2026-11-02`
  - LLM agents struggle to automate complex enterprise procedures because static, pre-built harness cannot capture proprietary policies, undocumented behaviors, or state-dependent recovery paths that surface only during execution. Procedural memory accrued from agent experience offer…

- **[When Music Needs Meaning: Semantic Communication as a Transformative Enabler for the Musical Metaverse](https://arxiv.org/abs/2611.03995v1)**
  - *Ali Al Housseini, Jaime Llorca, Cristina Rottondi et al.*
  - `2026-11-02`
  - The Musical Metaverse (MM) enables geographically distributed musicians, audiences, sound engineers, and AI agents to interact through synchronized audio, visual, kinematic, and haptic streams, imposing latency, synchronization, bandwidth, and scalability requirements that are di…

- **[What Is This Memory Useful For? Measuring Task-Conditioned Utility in Long-Term Agent Memory](https://arxiv.org/abs/2611.03930v1)**
  - *Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Feng Yan et al.*
  - `2026-11-02`
  - A stored experience may answer one future question and offer little help with another. We measure this task-conditioned utility rather than assigning each memory a single importance score. A task-blind writer stores a memory without seeing the later task; a frozen reader then ans…

- **[DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412v2)**
  - *Yumou Liu, Mingju Chen, Zhoufutu Wen et al.*
  - `2026-11-02`
  - LLM agents are judged by what they deliver, and in professional work what gets delivered is a project, not a task. A project pays off only if the whole package holds, and one weak part can limit the value of the rest. Yet existing benchmarks mostly test agents on one task at a ti…

- **[Can We Stop the Backtest Yet? Anytime-Valid Promotion Tests for Adaptive Financial Research Agents](https://arxiv.org/abs/2611.03384v1)**
  - *Eric Benhamou, Jean-Jacques Ohana, Beatrice Guez et al.*
  - `2026-11-02`
  - Financial research agents can generate and monitor trading rules faster than a human can document the resulting selection process. Candidates appear at data-dependent times, weak rules are abandoned, and promising ones are watched until they cross a reporting threshold. We introd…

- **[ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents](https://arxiv.org/abs/2611.03238v1)**
  - *Daiqiang Li, Jingyi Peng, Rui Hu et al.*
  - `2026-11-02`
  - Computer-use agents for scientific software require application-specific expertise. Much of this expertise is documented in human-authored software manuals and web pages. However, turning these resources into executable, reusable skills remains challenging due to mismatches betwe…

- **[Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents](https://arxiv.org/abs/2611.03092v1)**
  - *Zheng Wu, Xinbei Ma, Yao Yao et al.*
  - `2026-11-02`
  - Personal AI agents are increasingly capable of handling long-horizon tasks across applications, yet users often need to invest substantial effort in specifying goals, resolving ambiguity, and verifying outcomes. We argue that progress should be measured by how effectively agents…

- **[EEFA: A Framework for the Ethical Evaluation of AI Agents](https://arxiv.org/abs/2611.02561v1)**
  - *Swathi Pallikala, Yashas Hariprasad*
  - `2026-11-02`
  - The rapid deployment of autonomous AI agents across consequential domains including healthcare, legal services, nancial management, and enterprise workows has created an urgent governance challenge. While the eld of AI evaluation has produced sophisticated benchmarks for measurin…

- **[Cumulative and Audited Guardrail Tool Evolution for LLM Agent Safety](https://arxiv.org/abs/2611.02516v1)**
  - *Xiao Yang, Aishan Liu, Siyuan Liang et al.*
  - `2026-11-02`
  - Large language model (LLM) agents increasingly operate in open-world environments where safety risks cannot be fully predefined. However, most existing guardrail mechanisms remain static, relying on fixed rules, prompts, or classifiers that generalize poorly to emerging risks. He…

- **[Late Autumn: LLM Agents Specialize a General Multi-Robot Planner for One Warehouse](https://arxiv.org/abs/2611.02391v1)**
  - *Yimin Tang, Han Zhang, Shao-Hung Chan et al.*
  - `2026-11-02`
  - No algorithm is best on all problems, but a real warehouse is a narrow problem: its layout and processes rarely change. Operators still run one general multi-robot planner at many sites, because experts cannot tune it for each one. In this work, which we call Late Autumn, we expl…

- **[What Structurally Breaks an Agent? Auditing Difficulty in Stateful Tool-Use Workflows](https://arxiv.org/abs/2611.03227v1)**
  - *Shereen Anand, Ju Wang, Yali Du*
  - `2026-11-02`
  - An aggregate task score does not distinguish failures of scheduling, state retention, and candidate selection. We develop a small executable instrument that varies dependency depth, candidate count, active state width, and access to current-state snapshots while holding the numbe…

- **[Camera Radar LiDAR Fusion via Point-Cloud Projection for Multi-Task Learning](https://arxiv.org/abs/2611.03942v1)**
  - *Kavin Chandrasekaran, Sorin Grigorescu*
  - `2026-11-02`
  - Autonomous vehicles require robust perception systems to operate safely under diverse environmental conditions. While cameras provide high-resolution visual data, their performance significantly degrades in low-light and adverse weather. High Definition (HD) radar offers superior…

- **[Integrating Domain Adaptation and Retrieval-Augmented Generation for Saline-Alkali Land Reclamation Planning](https://arxiv.org/abs/2611.02883v1)**
  - *Zuguang He, Congcong Zheng, Wanyue Chen et al.*
  - `2026-11-02`
  - Reclamation of saline-alkali land requires management plans that account for soil and water conditions, treatment evidence, and financial constraints. This study develops Wenyao, an agricultural decision-support system integrating domain adaptation with retrieval-augmented genera…

- **[Risk-Constrained Evaluation of Financial Document Recognition: A Formal Framework for Evidence, Critical Errors, and Selective Automation](https://arxiv.org/abs/2611.02775v1)**
  - *Subodh Lonkar*
  - `2026-11-02`
  - Financial document recognition is commonly evaluated using character and word error rates, which do not adequately represent the consequences of errors in financial workflows. This paper formalizes financial document recognition as a risk-constrained evidence-recovery problem. It…

- **[The Customer Never Sees the Goal: Measuring and Detecting Vulnerability-Targeted Manipulation in LLM Assistants](https://arxiv.org/abs/2611.02689v1)**
  - *Bohan Jiang, Dawei Li, Yasin Silva et al.*
  - `2026-11-02`
  - Companies deploy large language model (LLM) assistants on their websites to advise customers. For commercial reasons, the operator can give an assistant a goal that the customer never sees. This paper focuses on operator-induced vulnerability-targeted manipulation (VTM), in which…

- **[InterFuse: Interaction-Guided Adaptive Fusion of Heterogeneous Models for Payment Risk Ranking](https://arxiv.org/abs/2611.02640v1)**
  - *Haoyu Jiang, Weiyu Han, Ze Zhao et al.*
  - `2026-11-02`
  - Payment platforms use view-specific models trained on transaction attributes, behavioral histories, and relational structures to rank transactions under limited review budgets. However, existing fusion methods often focus on prediction scores or interactions among model represent…

- **[Enhancing Stock Market Information Retrieval with Retrieval-Augmented Generation](https://arxiv.org/abs/2611.03747v1)**
  - *Huan Phong Thai, Thu Anh Ngoc Le, Nhu Huynh Thi Le et al.*
  - `2026-11-02`
  - Natural Language Processing (NLP) has been widely applied in financial domains, enabling automated analysis and retrieval of stock market information. However, traditional NLP-based systems often struggle with maintaining contextual accuracy and generating relevant responses in d…

- **[Honest Small Decision Models for Finance: Scale, Specialization Collapse, and Mixed-Corpus Remediation](https://arxiv.org/abs/2611.03755v1)**
  - *Ajitabh Kumar*
  - `2026-11-02`
  - Financial workflows need fast, calibrated, auditable decisions, not just generated text. We train System-1 decision models, small language models fine-tuned to answer typed questions (choice/score/noul) with a probability in a single forward pass, across two model families (K2-Ho…

- **[TensorLOB: Structure-Preserving Tensor Learning for Limit Order Book Forecasting](https://arxiv.org/abs/2611.02866v1)**
  - *Yuxuan Gu, Danilo Mandic*
  - `2026-11-02`
  - The limit order book (LOB) records outstanding buy and sell orders across multiple price levels. Its state evolves over time across market side, price level, and order attribute, naturally forming a multiway structure. However, existing LOB models typically flatten these dimensio…

- **[Improving Financial Cybersecurity Through Fraud Transaction Detection with Deep Learning](https://arxiv.org/abs/2611.02312v1)**
  - *Harish Kant Pathak, Rahul Kumar*
  - `2026-11-02`
  - Financial fraud detection remains a critical challenge in cybersecurity, with traditional rule-based systems struggling to keep pace with evolving attack patterns. This paper presents a deep learning approach for fraud transaction detection, leveraging neural network architecture…

- **[Thinking Fast, Trading Late: System One Decision Models vs the Market](https://arxiv.org/abs/2611.03985v1)**
  - *Amir Dehkordi, Alireza Kargarzadeh, Nariman Khaledian et al.*
  - `2026-11-02`
  - Large language models (LLMs) read company news at scale, and backtests suggest that their readings predict stock returns. We ask how much of that predictability survives a test that rules out look-ahead, memorization and selection. We propose OLIVIA, a protocol for such tests: po…

- **[Analysing the Narrative Paradox through Formal Models and Properties in Interactive Narrative](https://arxiv.org/abs/2611.02801v1)**
  - *Jules Clerc, Mohamed Sallak, Domitile Lourdeaux et al.*
  - `2026-11-02`
  - Interactive narratives aim to let players influence the unfolding of a story while preserving a coherent and satisfying narrative progression. This creates a central tension, commonly described as the narrative paradox, between player autonomy and narrative control. Experience Ma…

- **[Penalize the Common Trade: A Collision-Aware Layer for Learned Portfolios](https://arxiv.org/abs/2611.03453v1)**
  - *Eric Benhamou, Jean-Jacques Ohana, Beatrice Guez et al.*
  - `2026-11-02`
  - Different learning systems can make nearly the same trade when they share data, objectives, or representations. The market then sees decision concentration even if the models look diverse. We call exposure to this shared direction a signal collision. A linear-impact game shows th…

- **[Interpretable Allocation and Model-Predictive Rebalancing of Equity Portfolios, Tested on Real and Synthetic Markets](https://arxiv.org/abs/2611.03022v1)**
  - *Jeffrey D. Varner*
  - `2026-11-02`
  - A live equity portfolio poses three problems: which stocks to hold, when to trade, and whether the strategy holds up beyond the observed market. We built one system for all three and tested it on 373 US equities, calibrated on 2014-2024 and traded from January 2025 to September 2…

- **[PanelGP: A Probabilistic Factor Model for Asset-Return Panels](https://arxiv.org/abs/2611.04040v1)**
  - *Andrea Ruglioni, Damir Filipovic*
  - `2026-11-02`
  - We develop PanelGP, a conditional factor model for large panels of stock returns in which firm characteristics determine the factor loadings and economic conditions determine the expected factors. Both relations are estimated nonparametrically with Gaussian-process priors. The ke…

- **[Herding or Racing? Decomposing Cross-Account Order-Flow Persistence in On-Chain Markets](https://arxiv.org/abs/2611.02616v1)**
  - *Yichong Bai, Dingyue Kan*
  - `2026-11-02`
  - Most of the autocorrelation in trade signs on decentralized exchanges comes from pairs of trades sent by different wallets. For Uniswap v3, this has been read as herding dominating order splitting -- the reverse of what equity markets show. We show that this herding share mixes t…

- **[Auditing Representation-Space Fraud Detection: A Bayesian IRL Framework for Calibrated Uncertainty and Its Limits](https://arxiv.org/abs/2611.02673v1)**
  - *Shivam Swarup, Divya Prakash Shrivastava, Rakesh Thakur*
  - `2026-11-02`
  - Shilling detectors for recommender systems are almost always evaluated by one number, detection AUROC, with no account of when it can be trusted. We audit representation-space detection with VEIL (Variational Evaluation via Inverse-reinforcement Learning), a pairwise (Bradley-Ter…


---
*Generated 2026-11-05 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
