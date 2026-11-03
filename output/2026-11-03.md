# Daily Paper Digest — 2026-11-03 (Tuesday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**460 unique papers** (590 topic-entries — cross-topic papers counted once per category)

---

## Agent  (314)

### AAAI

- **[GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Through Code Repository Leveraging](https://arxiv.org/abs/2508.18993)**
  - *Zi-Yi Ni, Hua-Can Wang, Shuo Zhang et al.*
  - **AAAI 2025** · `2025-08-26`
  - Beyond scratch coding, exploiting large-scale code repositories (e.g., GitHub) for practical tasks is vital in real-world software development, yet current benchmarks rarely evaluate code agents in such authentic, workflow-driven scenarios. 
To bridge this gap, we introduce GitTa…


### NeurIPS

- **[ARTE: Agentic Refinement through Trade Execution for High-Frequency Trading Strategy Discovery](https://openreview.net/forum?id=VisvXioWmG)**
  - **NeurIPS 2025** · OpenReview · `2026-10-12`
  - Existing LLM-based trading strategy development primarily uses aggregated price and volume data, which omit within-interval event order and displayed order book changes. Tick-level trade and quote observations preserve this information, but their scale makes the full history impr…

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

- **[Self-Evolving Agentic Workflows via Semantic Decomposition of Complex Tasks](https://arxiv.org/abs/2611.01840v1)**
  - *Zichuan Fu, Junjia Qi, Xian Wu et al.*
  - **NeurIPS** · `2026-11-01`
  - Agentic workflows organize complex tasks into reusable procedures. However, invoking an LLM at every step incurs repeated inference costs and delays. We propose a framework for self-evolving agentic workflows through semantic task decomposition. Each subtask has explicit applicab…

- **[REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://arxiv.org/abs/2504.11543)**
  - *Divyansh Garg, Shaun VanWeelden, Diego Caples et al.*
  - **NeurIPS 2025** · `2025-04-15`
  - We introduce REAL, a benchmark and framework for multi-turn agent evaluations on deterministic simulations of real-world websites. REAL comprises high-fidelity, deterministic replicas of 11 widely-used websites across domains such as e-commerce, travel, communication, and profess…


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


### ICLR

- **[MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents](https://arxiv.org/abs/2510.15994)**
  - *Dong-Sen Zhang, Ze-Kun Li, Xu Luo et al.*
  - **ICLR 2025** · `2025-10-14`
  - The Model Context Protocol (MCP) standardizes how large language model (LLM) agents discover, describe, and call external tools. While MCP unlocks broad interoperability, it also enlarges the attack surface by making tools first-class, composable objects with natural-language met…


### KDD

- **[CR-Bench-v2: Evaluating the Real-World Utility of AI Code Review Agents](https://arxiv.org/abs/2611.02566v1)**
  - *Kristen Pereira, Neelabh Sinha, Rajat Ghosh et al.*
  - **KDD** · `2026-11-02`
  - The rapid growth of automated code generation has created a pressing need for automated code review. Yet code review resists full automation: it depends on context beyond the \textit{diff}, on the author's intent, and on judgments about design and maintainability on which even ex…


### ACL

- **[DR Pixel: Page-Native Deep Research with Vision-Language Models](https://arxiv.org/abs/2611.03097)**
  - *Tiansheng Hu, Yichuan Wang, James V. Talwar et al.*
  - **ACL** · 🤗 Featured · `2026-11-02`
  - Complex documents such as scientific papers contain rich information in tables, figures, and equations; however, existing deep research (DR) agents typically reduce papers to OCR-extracted text. We instead ask whether vision-language models (VLMs) can enable page-native deep rese…

- **[MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](https://arxiv.org/abs/2611.03555v1)**
  - *Farooq Shaikh, Biagio Montaruli*
  - **ACL** · `2026-11-02`
  - The Model Context Protocol (MCP) lets agentic AI frameworks connect language models to external tool providers, but it carries attacker-controlled content (tool descriptions, schema fields, and response data) into model context without validation. Prior benchmarks measure model c…

- **[Switch-SWE: Do Coding Agents Hold Focus When Switching Between Unfinished Tasks?](https://arxiv.org/abs/2611.02017v1)**
  - *Shuochen Chang, Qianli Ma, Yibo Miao et al.*
  - **ACL** · `2026-11-01`
  - Software development sessions often involve several unfinished tasks rather than one issue carried through to completion. As coding agents take on repository-level development, they need to recover an earlier task's requirements and partial progress after intervening work. Existi…

- **[Accounting for Irregular State Transitions through Belief Estimation in Online Medical Consultation](https://arxiv.org/abs/2611.01474v1)**
  - *Mingzhe Lu, Xiangru Chen, Jian Qin et al.*
  - **ACL** · `2026-11-01`
  - While online medical consultation broadens access, unprompted patient disclosures and topic shifts frequently disrupt clinician inquiry, leaving clinical states progressively revealed. We characterize these dynamics using both existing evaluation metrics and task-specific interac…

- **[Discovering Models for Experimental Quantum Systems with Agentic AI](https://arxiv.org/abs/2611.00620v1)**
  - *Hannah C. Kleidermacher, Bennet Windt, Miguel Bello et al.*
  - **ACL** · `2026-10-31`
  - A central obstacle in realizing color center cavity-QED-based quantum technologies is inhomogeneity, or disorder, among individual emitters. As the number of emitters increases, so does the complexity of the experimental data, making it difficult to quantify the present physical…

- **[Agentic Context Management for Multi-Turn Human-AI Conversations](https://arxiv.org/abs/2611.00518v1)**
  - *Matthew Ho, Chenglong Wang, Baolin Peng et al.*
  - **ACL** · `2026-10-31`
  - LLMs degrade in multi-turn conversation partly because of context pollution: the model's own earlier outputs stay in context and anchor later turns, so an early misreading of the user's intent can persist after the user corrects it. Assistant omission (AO), dropping every assista…


### Other / arXiv

- **[CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements](https://arxiv.org/abs/2611.03126)**
  - *Xinlei Yu, Gen Li, Ji Zhao et al.*
  - 🤗 Featured · `2026-11-02`
  - Despite recent advances in CUAs, their development remains constrained by the limited diversity, controllability, and reliability of interaction data. Moreover, conventional optimization pipelines lack iterative feedback, while existing recursive improvement approaches often rely…

- **[CoworkOS:Scaling Agent Coworkers for Real-world Automation](https://arxiv.org/abs/2611.03178)**
  - *Jiajie Jin, Guanting Dong, Chengjun Pan et al.*
  - 🤗 Featured · `2026-11-02`
  - Rapid advances in cowork agents are shifting human-AI collaboration toward real-world automation, delivering software, designs, and other artifacts. However, such productivity work demands both high-quality delivery on complex productivity tasks and continued monitoring and decis…

- **[Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents](https://arxiv.org/abs/2611.03092)**
  - *Zheng Wu, Xinbei Ma, Yao Yao et al.*
  - 🤗 Featured · `2026-11-02`
  - Personal AI agents are increasingly capable of handling long-horizon tasks across applications, yet users often need to invest substantial effort in specifying goals, resolving ambiguity, and verifying outcomes. We argue that progress should be measured by how effectively agents…

- **[Measuring AI Agents as Teammates with Collaborative Intelligence](https://arxiv.org/abs/2611.02633)**
  - *Sean Wu, Aneesh Pappu, Jiaru Zou et al.*
  - 🤗 Featured · `2026-11-02`
  - Progress in AI is often measured by what a single model can do on its own. Yet teams of AI agents are starting to make breakthroughs and discoveries in science, medicine, mathematics and software engineering. As AI begins to work in teams of agents and people, the ability to coll…

- **[LEANGUARD: Lean-Verified Guardrails for Tool-Using Agents](https://arxiv.org/abs/2611.02332)**
  - *Sreehari Sankar, Debargha Ganguly, Vikash Singh et al.*
  - 🤗 Featured · `2026-11-02`
  - Tool-using language-model agents often execute actions that their domain policies forbid. We present LeanGuard, a runtime that checks every proposed tool call against a policy written in Lean4 before the call reaches the environment. Policies combine state predicates with scoped…

- **[IdeaTaste: Do LLMs Share the Research Taste of Human Researchers?](https://arxiv.org/abs/2611.03424)**
  - *Shanshan Zhong, Chen Xu, Jingjie Ning et al.*
  - 🤗 Featured · `2026-11-02`
  - Research taste, the judgment of what to read, which problems to pursue, and which methods to try, increasingly shapes the work of AI scientists, yet it remains far less understood than their ability to execute research. We introduce IdeaTaste, a benchmark that scores an LLM by ho…

- **[Can Coding Agents Sustain Continual Evolution without Forgetting?](https://arxiv.org/abs/2611.03219)**
  - *Shangziqi Zhao, Yitong Zhang, Jia Li*
  - 🤗 Featured · `2026-11-02`
  - Recently, harness self-evolution has emerged as an important paradigm for improving agent performance. Prior studies show that evolving the agent harness can effectively enhance agent capabilities without modifying the foundation model's parameters. We find that existing approach…

- **[Advances in Agentic Computer Graphics](https://arxiv.org/abs/2611.01860)**
  - *Hengyu Liu, Jihyeon Je, Ruiqi Wang et al.*
  - 🤗 Featured · `2026-11-01`

- **[Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://arxiv.org/abs/2611.01560)**
  - *Jiarui Yuan, Yuxin Zuo, Xiaoyu Huang et al.*
  - 🤗 Featured · `2026-11-01`

- **[SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training](https://arxiv.org/abs/2611.02074)**
  - *Ziming Li, Lu Yu, Jiatan Huang et al.*
  - 🤗 Featured · `2026-11-01`
  - Coding agents solve repository issues through long sequences of exploration, editing, and validation. These trajectories are increasingly used as post-training data, so how they are collected shapes what the trained model learns. A common approach is to sample multiple trajectori…

- **[NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale](https://arxiv.org/abs/2611.02102)**
  - *Chaoyun Zhang, Bingxuan Li, Pinxue Guo et al.*
  - 🤗 Featured · `2026-11-01`
  - Scaling computer-use agents from individual actions to complex software work requires experience that connects decisions to complete outcomes. We present NorthCUA, an integrated system for turbocharging computer-use agents through experience at scale. Its Experience Flywheel supp…

- **[CrossSWE: Benchmarking Cross-Repository Joint Development for Coding Agents](https://arxiv.org/abs/2611.01484)**
  - *Silin Chen, Yuling Shi, Heng Lian et al.*
  - 🤗 Featured · `2026-11-01`

- **[Can Large Language Model Agents Learn by Watching Tutorial Videos?](https://arxiv.org/abs/2611.01460)**
  - *Haoyu Zhao, Zafeirios Fountas, Jun Wang*
  - 🤗 Featured · `2026-11-01`
  - Humans continuously acquire knowledge from carefully crafted materials such as books and tutorial videos, carrying that understanding into future tasks. Millions of such instructional videos are uploaded online every day, yet LLM agents remain unable to exploit this ever-expandin…

- **[TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents](https://arxiv.org/abs/2610.41216)**
  - *Kehong Gong, Xiaoxu Zheng, Guanli Hou et al.*
  - 🤗 Featured · `2026-10-30`

- **[Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](https://arxiv.org/abs/2610.40191)**
  - *Liaoyuan Fan, Yuhao Zheng, Dongxing Mao et al.*
  - 🤗 Featured · `2026-10-29`

- **[MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads](https://arxiv.org/abs/2610.40293)**
  - *Shengxuan Qiu, Haochen Huang, Shuzhang Zhong et al.*
  - 🤗 Featured · `2026-10-29`

- **[Multi-Agent Relay Thinking](https://arxiv.org/abs/2610.35219)**
  - *Xu Liu, Jungang Qiao, Guikun Chen et al.*
  - 🤗 Featured · `2026-10-27`

- **[Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](https://arxiv.org/abs/2610.27954)**
  - *Byeonghun Bang, Sangwoo Park, Jinheon Baek et al.*
  - 🤗 Featured · `2026-10-20`

- **[NitiBench+: A Temporal Thai Legal Question Answering Benchmark Across 17 Domains](https://arxiv.org/abs/2611.03576)**
  - *Pawitsapak Akarajaradwong, Sarana Nutanong, Chompakorn Chaksangchaichot*
  - 🤗 · `2026-11-02`
  - Law changes over time. A court decides a case under the law in force on that day, and legal QA benchmarks grade answers against today's law. We checked 156,650 decisions of four Thai courts. Up to 67% of them cite law that has since been amended or repealed. We introduce NitiBenc…

- **[Auto-Research Agent on MSA Organization to Improve Protein-Protein Complex Structure Prediction](https://arxiv.org/abs/2611.03183)**
  - *Zilu Zhang, Jing Bao, Lifeng Qiao et al.*
  - 🤗 · `2026-11-02`
  - Protein-complex structure prediction with AlphaFold 3 depends on MSA content, depth, and cross-chain pairing. Current pipelines apply uniform recipes, typically maximizing depth and pairing by species, yet even whether cross-chain pairing helps AF3 remains contested. We show that…

- **[WebHarbor: Docking Real Websites for Evolving GUI Agent Environments](https://arxiv.org/abs/2611.03634)**
  - *Zhaoyang Wang, Qianhui Wu, Boyu Gou et al.*
  - 🤗 · `2026-11-02`
  - GUI web agents require realistic and interactive environments that remain stable during both evaluation and training. Live website evaluation suffers from changing content, access restrictions, and limited coverage of authenticated workflows, while existing synthetic environments…

- **[The SIMPLE Law for Energy Cost of LLM Inference](https://arxiv.org/abs/2611.03330)**
  - *Hiari Pizzini Cavagna, Andrea Proia, Daniele Cesarini et al.*
  - 🤗 · `2026-11-02`
  - Generative AI is billed per token, yet tokens are not equally expensive. Each token enters the KV-cache and raises the cost of those that follow, so energy grows non-linearly along a sequence whose tokens look identical. No analytical model states what a token costs, and the most…

- **[RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures](https://arxiv.org/abs/2611.02826)**
  - *Jinbo Hu, Songren Zhang, Chuanxun Fu et al.*
  - 🤗 · `2026-11-02`
  - Reaction data underpin machine learning for reaction prediction, condition recommendation, and retrosynthetic planning, yet extracting these data from literature figures still requires substantial manual effort. Many figures encode multiple experiments through shared templates, s…

- **[Harvesting SWE Benchmarks from Wild Vibe Coding Sessions](https://arxiv.org/abs/2611.02440)**
  - *Ao Lu, Yuanhao Zeng, Shaocheng Lan et al.*
  - 🤗 · `2026-11-02`
  - Development teams need reproducible tasks from their own repositories and workflows to evaluate coding agents. Conversational developer-agent collaboration ("vibe coding") produces abundant coding sessions and repository checkpoints, but requirements evolve across turns, unrelate…

- **[Decision Models as Policy Gates for Coding Agents: Explicit Policy Boundaries Improve Detection and Reduce False Alarms](https://arxiv.org/abs/2611.02155)**
  - *James P. Beno*
  - 🤗 · `2026-11-01`
  - Coding agents can destroy data, leak secrets and message the wrong person faster than a human can review. Could a decision model catch these risks at runtime? We evaluated 22 hosted decision models and two prompted general models as classifiers for a multi-rule policy engine. A s…

- **[Is Your Long-Horizon Benchmark Really Deep? Measuring and Synthesizing Depth in Terminal Tasks](https://arxiv.org/abs/2611.01927)**
  - *Yu Jiang, Yue Huang, Hang Hua et al.*
  - 🤗 · `2026-11-01`
  - Long-horizon terminal tasks are used to evaluate and train agents. Human-curated datasets are scarce, so many synthesis methods have emerged. They usually measure the length of a task by the turns a model needs to pass it, and its difficulty by labels the LLM sets during generati…

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

- **[Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM for Investigative Analysis](https://arxiv.org/abs/2611.03434v1)**
  - *Shai Nahum Gefen, Vered Chassida, Dmitry Basin et al.*
  - `2026-11-02`
  - Government intelligence teams need LLM agents that can analyze large, messy evidence collections, but security and cost constraints often rule out hosted frontier models and broad, hard-to-audit tool surfaces. We report CLEO: Constrained Loop for Environment Optimization, a metho…

- **[DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412v1)**
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

- **[An Axiomatic Framework for Reinforcement Learning in Open Multi-Agent Systems](https://arxiv.org/abs/2611.03301v1)**
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

- **[ScienceCUA: Resource-to-Skill Construction and Execution-Guided Skill Evolution for Scientific Computer Use Agents](https://arxiv.org/abs/2611.03238v1)**
  - *Daiqiang Li, Jingyi Peng, Rui Hu et al.*
  - `2026-11-02`
  - Computer-use agents for scientific software require application-specific expertise. Much of this expertise is documented in human-authored software manuals and web pages. However, turning these resources into executable, reusable skills remains challenging due to mismatches betwe…

- **[Axion 1.0: Open Agent Foundation Models, Simplified](https://arxiv.org/abs/2611.03233v1)**
  - *Yuqi Jia, Yunjie Tian, Jiayu Zheng et al.*
  - `2026-11-02`
  - We introduce Axion 1.0, a fully open agent foundation model that combines strong and broad agentic capabilities with a remarkably simple training recipe. Axion 1.0 is trained in only three stages: two lightweight supervised fine-tuning stages followed by reinforcement learning, w…

- **[Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction](https://arxiv.org/abs/2611.03223v1)**
  - *Yiwei Zha, Qingyu Meng, Herbert Bos et al.*
  - `2026-11-02`
  - LLM agents compact long histories to fit their context windows, but the compacted context must still carry the operating rules that govern later actions. Prior work shows that violations rise after compaction, but measures compliance outside a complete agent harness and does not…

- **[Toward Knowledge-Centric AI: Discovering, Internalizing, and Using Explicit Knowledge Across Agents and Generations](https://arxiv.org/abs/2611.03157v1)**
  - *Yisen Gao, Haoyu Huang, Zhongwei Xie et al.*
  - `2026-11-02`
  - Knowledge is how understanding accumulates across people and generations: durable records that outlive their producers and that others can check, combine, teach, and correct. AI agents are now built and run by many independent users and organizations, and each agent is upgraded,…

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

- **[Why Tabular Foundation Models Excel on Relational Data They Have Never Seen](https://arxiv.org/abs/2611.02936v1)**
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

- **[SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding](https://arxiv.org/abs/2611.02846v1)**
  - *Tianyu Liu, Jun Zhang, Wenjie Huang et al.*
  - `2026-11-02`
  - Speculative decoding (SD) accelerates large language model inference by reducing the sequential cost of token-by-token generation. Advanced SD methods reduce proposal cost with parallel drafters that predict entire blocks in one forward pass, but overall speedup still depends on…

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

- **[Accessed, never disclosed: Silent access to protected health information by medical artificial intelligence agents](https://arxiv.org/abs/2611.02319v1)**
  - *Jae Wang Lee, Abhirup Banerjee, Yeong Chan Lee*
  - `2026-11-02`
  - Medical artificial intelligence agents should retrieve patient identifiers only when a task requires them, the data-minimization principle behind the HIPAA minimum necessary standard for protected health information (PHI). An agent can retrieve identifiers without revealing them.…

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

- **[Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization](https://arxiv.org/abs/2611.03517v1)**
  - *Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su et al.*
  - `2026-11-02`
  - LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff. Scripted agents fix what the model does at each step, via a learned policy, an optimization menu, or fixed roles, and are sample-efficient where the recipe applies and stall where it does not.…

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

- **[VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](https://arxiv.org/abs/2611.03575v1)**
  - *Wei-Lin Chen, Zhepei Wei, Xinyu Zhu et al.*
  - `2026-11-02`
  - Large language model (LLM) coding agents increasingly operate with shell access, allowing them to write scripts, move files, alter permissions, and modify system configurations. However, an agent may achieve a user's goal while causing unintended harm, such as deleting unrelated…

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

- **[Toward Agentic AI-Ready Workflows in Built Environment Organizations: Knowledge Structures and Interoperability Challenges](https://arxiv.org/abs/2611.02286v1)**
  - *Ahmet Bahaddin Ersoz, Justin McHenry, Yevgeniya Kovalchuk et al.*
  - `2026-11-01`
  - The rise of agentic artificial intelligence (AI) in the built environment is shifting attention from isolated AI tools toward autonomous systems that reason, plan, and act across project and organizational workflows. The effectiveness of such systems depends not only on large lan…

- **[Data-Scarce, Multi-Granular, Multimodal: Benchmark Design for Biosynthetic Gene Clusters](https://arxiv.org/abs/2611.02275v1)**
  - *Hanlin Xiao, Eriko Takano, Mauricio A. Álvarez et al.*
  - `2026-11-01`
  - Biosynthetic gene clusters (BGCs) are co-located genes that encode the biosynthesis of specialized metabolites, an important source of antibiotics, anticancer agents, immunosuppressants, and agricultural bioactives. Deep learning, particularly self-supervised foundation models, h…

- **[Qubrio: High-Performance Quantum Compilation via Multi-Agent LLM Collaboration](https://arxiv.org/abs/2611.02269v1)**
  - *Jixuan Ruan, Zhuo Cui, Zhengding Hu et al.*
  - `2026-11-01`
  - Large Language Models (LLMs) offer an adaptable alternative to traditional quantum compilation heuristics, which bottleneck progress by demanding costly manual redesigns whenever hardware evolves. However, naive single-pass LLM approaches fail under the unique challenges introduc…

- **[ANCHOR: KL-Anchored Adaptation for Stable Offline-to-Online RL](https://arxiv.org/abs/2611.02177v1)**
  - *Geonwoo Cho, Jaegyun Im, Doyoon Kim et al.*
  - `2026-11-01`
  - Offline-to-online reinforcement learning (RL) follows the pretrain-finetune paradigm: an agent is first pretrained on historical data and then adapted through online interaction. We study offline-to-online adaptation without offline replay, where the agent must improve using only…

- **[Rewarded for Not Getting Caught: Why Alignment Training Selects for Conditional Compliance and Cannot Instill Norms](https://arxiv.org/abs/2611.02162v1)**
  - *Kevin Baum, Ruta Binkytė, Gerrit Großmann et al.*
  - `2026-11-01`
  - Current alignment training cannot be expected to deliver what it is meant to deliver: AI agents that comply with norms whatever the gains and whether or not anyone is watching. Training that rewards and penalizes behavior can teach norms only through that reward, and a reward can…

- **[ZT-DAC: ML-Driven Dynamic Access Control Policy for Zero Trust in DER Networks](https://arxiv.org/abs/2611.02107v1)**
  - *Arun B. Chandrasekaran, Damilola Popoola, Souradeep Bhattacharya et al.*
  - `2026-11-01`
  - The increasing penetration of Distributed Energy Resources (DERs) in the smart grid has significantly expanded the cyber-attack surface. Traditionally, DER networks rely on static role-based access control (RBAC) mechanisms that assume persistent trust after authentication. This…

- **[Consolidating Reasoning with Test-Time Training](https://arxiv.org/abs/2611.02104v1)**
  - *Haotian Wu, Zeming Chen, Hao Zhao et al.*
  - `2026-11-01`
  - Effective multi-agent collaboration requires finalizing solutions from reasoning that is distributed across the individual attempts of many agents. However, useful intermediate reasoning can remain unexploited when collaboration is limited to voting on conclusions reached among i…

- **[ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and Cost](https://arxiv.org/abs/2611.02079v1)**
  - *Xingzhi Qian, Sungho Park, Rongyuan Tan et al.*
  - `2026-11-01`
  - Harness optimization can substantially improve LLM agents without modifying model weights, but existing methods primarily optimize response quality. Extending them to joint quality--cost optimization introduces a challenge: applying the deployment preference during intermediate u…

- **[Decoupled Predictive Decision Making: A Shared Conditional Predictor for Agents](https://arxiv.org/abs/2611.02075v1)**
  - *Lang Mo, Xingxuan Zhang, Qi Wang et al.*
  - `2026-11-01`
  - Agent decisions depend on empirical relationships that deployment observations reveal and task descriptions alone may leave unresolved. We introduce Decoupled Predictive Decision Making (DPDM), an architecture that formulates heterogeneous agent decisions as conditional predictio…

- **[State-Aware Virtual Patient Simulation for Training Psychiatrists in Challenging Clinical Scenarios](https://arxiv.org/abs/2611.02067v1)**
  - *Harsh Mohta, C Chandrahas Reddy, Sunhith Reddy Bojja et al.*
  - `2026-11-01`
  - Psychiatrists must be prepared to manage patients exhibiting challenging psychological states, including suicidal ideation, hallucinations, and other high-risk behaviors. However, opportunities to safely practice such interactions are limited. While recent conversational agents c…

- **[Do Embodied VLMs Actually Use Their Scene-Graph Memory?](https://arxiv.org/abs/2611.02056v1)**
  - *Shubh Garg, Divyansh Pandey, Vedant Khandelwal et al.*
  - `2026-11-01`
  - Embodied agents that answer questions about their route need a memory of what they saw, and scene graphs are a natural form for it. A vision-language model (VLM) can receive such a graph as text or through a graph encoder, but accuracy alone cannot show whether the graph holds th…

- **[Beliefs in feedback: Factored representations of interacting agents in transformers](https://arxiv.org/abs/2611.02047v1)**
  - *David A. Ehrlich, Manuel Baltieri, Fernando E. Rosas et al.*
  - `2026-11-01`
  - Complex systems, from ecosystems to brains, are usually modeled as modular components coupled through feedback rather than as indivisible wholes. Can a transformer trained on the joint behavior of a group of interacting agents be understood in the same way? In this work, we devel…

- **[LARK: Lean-Assisted Reasoning for LLM-Generated GPU Kernels](https://arxiv.org/abs/2611.02028v1)**
  - *Zixi Zhang, Jiayi Nie, Haoran Wu et al.*
  - `2026-11-01`
  - Efficient GPU kernels are typically low-level and hardware-specific, and LLM agents can now generate them faster than experts can verify. Existing approaches rely on testing, which provides evidence but not a guarantee of correctness. We introduce LARK, an agentic framework that…

- **[TrackMem: Tracking Evolving Beliefs in Long-Horizon Financial Dialogue](https://arxiv.org/abs/2611.02001v1)**
  - *Austin M. Y. Cheung, Harsh Vardhan Gupta, Go Nam Lui et al.*
  - `2026-11-01`
  - Memory systems for LLM agents are evaluated mostly on social dialogue, where facts accumulate and rarely change, so remembering reduces largely to finding the turn in which something was said. Financial dialogue breaks this assumption: figures are revised, stances shift without b…

- **[Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security](https://arxiv.org/abs/2611.01976v1)**
  - *Shiyu Kan, Yue Qi, Yufei Han et al.*
  - `2026-11-01`
  - Large language model based agents increasingly rely on external tools to invoke services and interact with web resources. These tools can evolve through software updates, yet agentic frameworks may continue trusting them without re-verifying their safety after implementation chan…

- **[Launder-Bench: Can Repository-Level Agentic Code Laundering Be Detected?](https://arxiv.org/abs/2611.01966v1)**
  - *Yuntong Hu, Hongji Pu, Zimo Li et al.*
  - `2026-11-01`
  - Coding agents can now rewrite repository-scale codebases while preserving tested behavior, creating a new challenge for plagiarism detection, license auditing, and software provenance. We ask whether such rewrites can still be traced to their source. Existing clone benchmarks emp…

- **[Step-Zero Attack: Agent Safety Before Observability](https://arxiv.org/abs/2611.01953v1)**
  - *Tian Qin, Yuhang Jiang, Junzhe Chen et al.*
  - `2026-11-01`
  - Existing attacks and defenses for coding agents act once content enters the model context: injected text persuades the model, and guards inspect what the model reads. Yet to judge whether processing an unknown archive, network response, or image is safe, an agent often must proce…

- **[TriPhysBench: Evaluating Physical Intelligence for Embodied Agents](https://arxiv.org/abs/2611.01934v1)**
  - *Zhongxiang Sun, Chenghao Yang, Haojie Ding et al.*
  - `2026-11-01`
  - Embodied agents need physical intelligence to understand their surroundings through physical perception, physical knowledge retrieval, and physical reasoning. These capabilities must work together to interpret events and make quantitative judgments. Existing benchmarks advance ph…

- **[RECEIPT: Measuring and Repairing the Return Assumption of LLM Agents in Web Service Operations](https://arxiv.org/abs/2611.01930v1)**
  - *Boyang Yang, Ziyao Yang, Yu Zhang et al.*
  - `2026-11-01`
  - LLM agents operate Web infrastructure from the command line and rely on a return assumption, namely that each tool call returns within a bounded time and with its requested action finished. Many commands, however, ask a question before they act, and the agent's harness either clo…

- **[AgenticMobility: An Open-Source Platform for Multi-AI-Agent Mobility Dynamics](https://arxiv.org/abs/2611.01918v1)**
  - *Jiaheng Xiao, Jiangtao Han, Jiachen Wang et al.*
  - `2026-11-01`
  - Understanding mobility dynamics and the effects of urban transportation management policies requires examining how individual travel decisions, traffic conditions, and policy interventions influence one another over time. We present AgenticMobility, an open-source experimental pl…

- **[NEIGHBOR: Aligning Service Behaviour and Evidence Use in an LLM Agent for Community Resident Services](https://arxiv.org/abs/2611.01836v1)**
  - *Zongyou Yang, Yinghan Hou, Xiaokun Yang*
  - `2026-11-01`
  - Residents who contact a community service desk about a repair or a service charge need answers they can act on, with facts that hold for their case and commitments the desk can keep. In tool-augmented LLM agents, such facts come from documents and records, and the conduct of a se…

- **[LegoEnv: Self-Evolving Agentic Environments via Modular Recombination](https://arxiv.org/abs/2611.01834v1)**
  - *Zhuosong Jiang, Chengxu Wu, Junqi Liu et al.*
  - `2026-11-01`
  - LLM agents learn by interacting with environments, yet existing environments are designed for specific tasks and fail to generalize to new ones. Recent methods automate environment construction with LLMs. However, they generate each environment from scratch, neither reusing parts…

- **[MemRole: From Memories to Decisions for Long-Horizon Reasoning in Role-Playing Agents](https://arxiv.org/abs/2611.01778v1)**
  - *Mengting Li, Xilong Cheng, Zhihao Xiao et al.*
  - `2026-11-01`
  - LLM-based role-playing agents are fluent at imitating a character's style, yet struggle to make role-consistent decisions over long narrative horizons. Such decisions are shaped by experiences spanning many prior scenes, which are often partial and may point in different directio…

- **[Silent Reward and Environment Defects in EV Charging Simulation Benchmarks: A Diagnostic Checklist](https://arxiv.org/abs/2611.01769v1)**
  - *Nour-Eddine Moumni, Rachid Alaoui, Driss Kiouach*
  - `2026-11-01`
  - Reinforcement-learning (RL) benchmarks built on microscopic traffic simulators such as SUMO are increasingly used to compare agent architectures for electric vehicle (EV) charging assignment. Unlike crashes, defects in the reward function, the environment's stochastic model, or t…

- **[Evolving Memory, Learning to Meta-Control: Test-Time Adaptation for Experience-augmented LLM Agents](https://arxiv.org/abs/2611.01747v1)**
  - *Zeyuan Zhao, Yuanyuan Shi, Peng Yu et al.*
  - `2026-11-01`
  - Self-evolving agents accumulate experience from task streams, but existing frameworks typically rely on fixed pipelines to retrieve and utilize this experience, neglecting when and how to deploy it. We introduce Online Meta-Control of Experience (OMCE), a framework that updates e…

- **[MAC-Bench: Benchmarking Multi-Agent Collaboration via Interconnected Tasks](https://arxiv.org/abs/2611.01728v1)**
  - *Zerui Chen, Qinggang Zhang, Qichuan Liu et al.*
  - `2026-11-01`
  - Large language model (LLM)-based multi-agent systems (MAS) tackle challenging tasks by dividing work among agents and coordinating their contributions toward shared objectives. Evaluating these systems therefore requires benchmarks that assess not only task-solving performance bu…

- **[Delivered, Not Used: Evaluating Agent Memory at Its Point of Use](https://arxiv.org/abs/2611.01718v1)**
  - *Changran Xu, Zeju Li, Qiang Xu*
  - `2026-11-01`
  - Task success, retrieval quality, and cost do not show whether an LLM agent used a delivered memory or what followed from that use. We introduce MemUse, which evaluates memory at its point of use in recorded trajectories: each memory delivery is compared with what the agent could…

- **[Just-in-Time Skill Retrieval via Long-Horizon State Tracking](https://arxiv.org/abs/2611.01701v1)**
  - *Xin Lin, Ziheng Wang, Zerui Chen et al.*
  - `2026-11-01`
  - Large language model (LLM) agents increasingly rely on external skill libraries to support complex task execution. However, determining which skills are needed remains challenging in long-horizon tasks. Existing methods typically select a fixed skill set before execution, implici…

- **[MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents](https://arxiv.org/abs/2611.01700v1)**
  - *Zhihua Wang, Yunhao Feng, Yifeng Gao et al.*
  - `2026-11-01`
  - AI agents often rely on persistent memory to retain user preferences and operational rules across sessions. However, this capability introduces a new safety risk: malicious instructions from messages, documents, or Web content can be retained in memory and influence future tasks…

- **[SPAR: Experience-Driven Strategy Evolution in Multi-Session B2B Sales](https://arxiv.org/abs/2611.01695v1)**
  - *Hangming Zhang, Yao Zhao, Haotian Kuang et al.*
  - `2026-11-01`
  - B2B outbound sales involves high transaction values and relationship-based trust, so closing a deal typically requires multiple rounds of outreach building on prior context. Existing LLM-based sales agents operate within single sessions and cannot carry forward context or refine…

- **[CREDO: Evidence-Conditioned Credit Assignment for Temporal Reasoning Agents](https://arxiv.org/abs/2611.01643v1)**
  - *Yue Leng, Shengtao Wen, Xiang Chen et al.*
  - `2026-11-01`
  - Temporal Knowledge Graph Question Answering (TKGQA) requires language model agents to retrieve evidence, select relevant facts, and perform multi-step temporal reasoning. However, the trajectory-level outcome signal in GRPO does not explicitly distinguish the quality of intermedi…

- **[SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts](https://arxiv.org/abs/2611.01600v1)**
  - *Amir Hossain Raj, Xuesu Xiao*
  - `2026-11-01`
  - Robots manipulating in cluttered spaces must often plan from partial views where foreground objects occlude the target, surrounding geometry, and usable free space. Reactive policies often miss these hidden constraints, while exhaustive search becomes computationally prohibitive…

- **[Principled Human-AI Collaboration in Agentic Workflows](https://arxiv.org/abs/2611.01566v1)**
  - *Young Hyun Cho, Will Wei Sun*
  - `2026-11-01`
  - Organizations adopting AI face the challenge of deciding which outputs can be released without human review while meeting the quality standards of human experts. We develop a statistical framework for delegating tasks between experts and black-box generate-verify workflows, in wh…

- **[\textsc{ChatDify}: Automating End-to-End Dify Workflow Synthesis from Natural Language via Multi-Agent Collaboration](https://arxiv.org/abs/2611.01563v1)**
  - *Tao Fan, Guoqiang Ma*
  - `2026-11-01`
  - The proliferation of Large Language Models has catalyzed powerful application development platforms like Dify, which enable users to build sophisticated LLM-powered workflows through modular node orchestration. However, manually configuring these workflows requires deep platform…

- **[From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents](https://arxiv.org/abs/2611.01527v1)**
  - *Xingyu Yi, Xinya Zhang, Yunshen Zhou et al.*
  - `2026-11-01`
  - A scientific agent can give the same verdict while reading and citing different evidence. BioAgent-DF tests this separation using paired reference and candidate values saved at the same scientific computation site. It restores or transplants those values at their original coordin…

- **[An auditable agentic pipeline for variant-to-gene prioritisation, validated against orthogonal functional evidence](https://arxiv.org/abs/2611.01461v1)**
  - *Shakuntala Baichoo, Sohail, Sarkar et al.*
  - `2026-11-01`
  - Assigning GWAS variants to causal genes requires evidence from multiple resources. We present V2G, an agentic pipeline that records evidence retrieval and returns ranked genes alongside the retrieved evidence. We evaluate whether language-model reranking improves gene prioritisat…

- **[CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging](https://arxiv.org/abs/2611.01449v1)**
  - *Yuxiang Wei, Lijing Zhu, Qizhen Lan et al.*
  - `2026-11-01`
  - Large language model (LLM) agents can autonomously run neuroimaging analyses from research questions to reported findings. Existing agentic systems use tools to check that code runs and reported values match its output, but rely on LLM judgment to decide which results warrant sci…

- **[I-PTC: Interactive Programmatic Tool Calling for Stateful Tool-Augmented Agents](https://arxiv.org/abs/2611.01446v1)**
  - *Huanzhi Mao, Chengkun Cao, Shuo Yuan et al.*
  - `2026-11-01`
  - Large language models are increasingly capable of writing and executing code, suggesting a natural paradigm for tool-augmented agents: expressing tool use as programs rather than isolated calls. Programmatic tool calling (PTC) captures this idea through loops, batching, abstracti…

- **[ERIA: An Instruction-Optimized Agent for Clinical EEG Reporting](https://arxiv.org/abs/2611.01394v1)**
  - *Ahmed Sameh, Gayal Kuruppu, Neeraj Wagh et al.*
  - `2026-11-01`
  - Clinical EEG interpretation requires integrating technical quality, background and behavioral states, interictal and ictal abnormalities, and overall clinical context across long recordings. We introduce ERIA (EEG Reporting and Instruction-Optimized Agent), a locally deployable f…

- **[Learning by Doing: Autonomously Compiling and Curating Agent Skills from Verified Traces](https://arxiv.org/abs/2611.01386v1)**
  - *Daniel Chalef, Peter Evans, Pavlo Paliychuk et al.*
  - `2026-11-01`
  - Memory systems for production LLM agents mostly store semantic memory (facts about users and domains) or episodic memory (earlier interactions). Research systems such as Trace2Skill, WikiSkill, and SkillRevise learn procedures from agent runs, package them as Skills, and evaluate…

- **[Toward Executable Multi-framework Front-end Code Generation with Self-Correction](https://arxiv.org/abs/2611.01383v1)**
  - *Linxiao Li, Haoran Ma, Chenyue Wang et al.*
  - `2026-11-01`
  - Generating codes from UI screenshots has recently benefited from MLLMs, yet existing methods centered on HTML targets and transfer poorly to multi-frameworks such as React, Vue, and Angular. However, unlike HTML, which does not entail compilation issues, generating executable cod…

- **[A Self-Exploring and Self-Evolving Paradigm for Adaptive Edge AI Development](https://arxiv.org/abs/2611.01377v1)**
  - *Leming Shen, Qiang Yang, Xinyu Huang et al.*
  - `2026-11-01`
  - Large Language Models (LLMs) exhibit powerful code generation abilities, fostering agentic systems to automate edge AI application development. However, existing agents typically operate via fixed agentic workflows and predefined design spaces, struggling to handle rapidly evolvi…

- **[Built on Broken Assumptions (BOBA): Why Coding Agents Cannot Be Left Alone](https://arxiv.org/abs/2611.02207v1)**
  - *Alejandro Cuadron, Arpit Gupta*
  - `2026-11-01`
  - Coding agents are autonomous developers. Given a request, they change the code and report back when done. As such, they can handle not only independent requests but whole chains of them, each request built on the last. Agents are known to report wrong work as done, yet benchmarks…

- **[TSSDA: An Autonomous Agent for Constructing a Time-Series Text-to-SQL Benchmark](https://arxiv.org/abs/2611.02132v1)**
  - *Zhihan Zheng, Shaoxu Song, Haitao Yuan et al.*
  - `2026-11-01`
  - As agents increasingly undertake data querying, Text-to-SQL serves as a foundational capability for database access. However, for text-to-SQL in time-series databases, high-quality benchmarks and large-scale training corpora remain scarce, limiting the systematic evaluation and d…

- **[Reinforcement Learning in High-Energy Physics: A Survey from Accelerator Control to Theory Exploration](https://arxiv.org/abs/2611.02049v1)**
  - *Luca Anzalone*
  - `2026-11-01`
  - Reinforcement learning (RL) is a machine learning paradigm in which an agent learns a decision-making policy by interacting with an environment, guided by a scalar reward rather than explicit supervision. Supervised and unsupervised learning have become indispensable tools in hig…

- **[ReFrame: Silence-Aware Compute Reclamation for Full-Duplex Speech Models](https://arxiv.org/abs/2611.01835v1)**
  - *Zheng Zhou, Guanyi Chen, Jing Wei et al.*
  - `2026-11-01`
  - Full-duplex speech models execute dense model inference for every audio frame throughout a live interaction. This uniform framewise schedule creates sustained GPU load across dialogue states whose computation has strong, reusable temporal structure. ReFrame formulates full-duplex…

- **[Learning AI Agents, Market Makers, and Stress in Automated Markets](https://arxiv.org/abs/2611.01799v1)**
  - *Irene Aldridge*
  - `2026-11-01`
  - Automated markets increasingly route order flow from learning trading agents through automated market makers (AMMs). We model trader archetypes as AI agents defined by their reward functions and analyze the feedback they create on a constant-product AMM. Herd-dominated and arbitr…

- **[A Deep Reinforcement Learning Framework for Real-Time Electric Vehicle Charging Management in IoEV-Enabled Smart Cities](https://arxiv.org/abs/2611.01751v1)**
  - *Nour-Eddine Moumni, Rachid Alaoui, Driss Kiouach*
  - `2026-11-01`
  - The rapid growth of electric vehicles (EVs) in urban environments demands intelligent, decentralised charging management strategies that operate under strict real-time constraints. This paper proposes an Edge-Intelligent architecture in which each EV selects a charging station (C…

- **[LLM-Enhanced Multimodal House Price Prediction using Structured, Textual, and Visual Features](https://arxiv.org/abs/2611.01615v1)**
  - *Khandokar Md. Rahat Hossain, Souvik Das, Tahsina Hashem et al.*
  - `2026-11-01`
  - Accurate house price prediction is essential for real estate buyers, sellers, agents, and financial institutions. Traditional methods rely primarily on structured data, e.g., number of bedrooms, bathrooms, parkings, but they overlook rich contextual information embedded in textua…

- **[When Should an Agent Refresh? Adaptive Index Reuse for Efficient Long-Horizon Reasoning](https://arxiv.org/abs/2611.01429v1)**
  - *Guangyuan Wang, Yifan Zhang, Shilong Liu*
  - `2026-11-01`
  - Language agents read code, tool output, and dialogue in contexts that grow at every step. Dynamic sparse attention lets a small indexer choose the earlier tokens each query attends to, but the indexer still scores the whole prefix at every layer. Cross-layer reuse methods such as…

- **[Multi-Agent Collusion and the J-Space](https://arxiv.org/abs/2611.02153v1)**
  - *Marco Molinari, Gabriele Bettineschi*
  - `2026-11-01`
  - LLM agents are increasingly deployed in Multi-Agent Systems (MAS), and they introduce the risk of coordination among agents that might escape human oversight. The J-space has been used to uncover deception in single LLMs, but its use for uncovering and steering collusion between…

- **[Retrieval-Enhanced Cultural Evaluation for Social Media Translation Training](https://arxiv.org/abs/2611.02009v1)**
  - *Linjuan Wu, Yiwen Qiu, Xinze Lyu et al.*
  - `2026-11-01`
  - Social media translation requires preserving meaning while capturing the cultural nuances of user-generated content (UGC). However, gaps in the cultural knowledge of LLM-based evaluators can lead to inaccurate assessments and unreliable training rewards. To improve these signals,…

- **[TAC-CoT: Tool-Empowered Implicit Chain-of-Thought via Interleaving Explicit Tokens](https://arxiv.org/abs/2611.01926v1)**
  - *Juseon Do, Sangmin Bae, Jeesu Jung et al.*
  - `2026-11-01`
  - LLM-based agentic systems are increasingly combined with CoT reasoning to solve tasks that require accurate reasoning, external knowledge, and multi-step deliberation. Yet, explicit CoT incurs substantial generation overhead, while implicit CoT, which replaces textual rationales…

- **[Can Large Language Models Extend Their Agentic Capabilities to Goal Pursuit in Open-Ended Multi-Turn Interaction?](https://arxiv.org/abs/2611.01552v1)**
  - *Mingyu Chen, Jingkai Lin, Xiaofen Xing et al.*
  - `2026-11-01`
  - Goal pursuit in open-ended dialogue requires agents to adapt their actions to interaction feedback across successive exchanges. We investigate whether agentic capabilities developed for multi-step tool use carry over to dialogue organized through the model's native tool interface…

- **[Latent Harness: Compiling Agent Behaviors into Post-Block Activation Shifts](https://arxiv.org/abs/2611.01415v1)**
  - *Ran Li, Shimin Di, Zeyu Ren et al.*
  - `2026-11-01`
  - Harness engineering and self-evolving agents improve language-model agents quickly, yet their gains live outside the model. The harness is re-sent and re-paid on every call, and the standard route to internalization is a weight update that is costly to iterate and fixed once merg…

- **[Trustworthy Execution of Industrial Agents](https://arxiv.org/abs/2611.02300v1)**
  - *Zhongjie Wang, Mingyi Liu, Xiang He et al.*
  - `2026-11-01`
  - Industrial agents increasingly modify persistent engineering objects rather than merely generate answers. Authentication and successful calls cannot establish whether intended changes occurred, evidence supports a conclusion, or historical results remain applicable. We present a…

- **[Towards a Theory for the Design of Rules in Multi-Agent Systems: the case of Homogeneous Fleets](https://arxiv.org/abs/2611.02260v1)**
  - *Matteo Penlington, Lorenzo Fiaschi, Raj Kiriti Velicheti et al.*
  - `2026-11-01`
  - The regulation of systems composed of many interacting decentralised agents is a long-standing problem. This problem has typically been resolved by the imposition of rules. Rules resolve the limitations of sub-optimal agents whilst simultaneously aligning the behaviour of the age…

- **[Local Solution Repair for Multi-Agent Pickup and Delivery](https://arxiv.org/abs/2611.02090v1)**
  - *Ethan Schneider, Jingkai Chen, Seth Hutchinson et al.*
  - `2026-11-01`
  - Multi-robot systems in automated warehouses must efficiently attend to a constant stream of pickup-and-delivery tasks while avoiding collisions. Existing Multi-Agent Pickup-and-Delivery (MAPD) solutions generate plans that are globally feasible but often locally inefficient. In l…

- **[Automated Stateful Specialization for Adaptive Agent Systems](https://arxiv.org/abs/2611.01870v1)**
  - *Myan Vu, Harrish Ayyanar, Jiang Pang et al.*
  - `2026-11-01`
  - Current automated agent design frameworks produce either static workflows that lack adaptability or per-query optimizers that prevent the accumulation of deep, agent-level task expertise. We propose a new direction that reconciles these paradigms: creating stateful teams of speci…

- **[From Single-Agent Self-Discovery to Multi-Agent Adaptation: Scaling Laws of Partner Feedback and Convention Rigidity in Meta Reinforcement Learning Algorithms](https://arxiv.org/abs/2611.01742v1)**
  - *Haomin Luo, Ersha Li*
  - `2026-11-01`
  - A key milestone toward Recursive Self-Improvement (RSI) is replacing hand-crafted optimizers with meta-learned update rules (such as Disco103 and OPEN) that discover how agents learn. Yet when a self-discovered RL model trains with adapting teammates, does co-evolution sustain ca…

- **[Renormalized Cellular Intelligence: When Does Model Reduction Preserve Collective Capability?](https://arxiv.org/abs/2611.01441v1)**
  - *Xuening Wu, Yanlan Kang, Qianya Xu et al.*
  - `2026-11-01`
  - As multi-agent systems grow in size and complexity, understanding which features of their interactions support collective capability becomes increasingly difficult. Can a simpler description preserve both task performance and the measured contribution of interactions between agen…

- **[ProofPatch: Reviewing Lean Statements and Keeping the Reviews Valid as Formalizations Evolve](https://arxiv.org/abs/2611.01357v1)**
  - *Xujun Che, Depeng Xu, Jian Xiang et al.*
  - `2026-10-31`
  - The kernel of the Lean proof assistant checks that a proof establishes its statement. Whether the statement says what was intended is left to human reviewers. This is the old problem of validating a specification, and it grows more pressing as language models write formal stateme…

- **[The Verifier Is Part of the Simulator: Evidence-View Gaming in Agentic Equation Discovery](https://arxiv.org/abs/2611.01334v1)**
  - *Orestis Oikonomou, Bogdan Raonic*
  - `2026-10-31`
  - A growing number of agentic pipelines search for governing equations: an agent proposes laws and a verifier checks them against simulated trajectories. The verifier sees only a numerical summary: integrals against test functions on a time grid. That summary carries its own discre…

- **[CuriousTogether: Implications of Curiosity and Cultural Grounding in Multi-Agent LLM Interactions](https://arxiv.org/abs/2611.01301v1)**
  - *Angana Borah, Zoha Hayat Bhatti, Zhijing Jin et al.*
  - `2026-10-31`
  - Large Language Models (LLMs) are increasingly deployed in multi-agent settings, exhibiting emergent collective behaviors, yet the role of curiosity as a driver of such dynamics remains understudied. We introduce CuriousTogether, a framework evaluating curiosity-driven multi-agent…

- **[OntoDoc: Automatically Generating Ontology Resource Descriptions](https://arxiv.org/abs/2611.01276v1)**
  - *Juan Guajardo Gutierrez, Mike Tran, Nasim Shirvani Mahdavi et al.*
  - `2026-10-31`
  - Knowledge graphs and ontologies form the backbone of structured, machine-readable knowledge representation, yet ontology terms often lack natural language descriptions, limiting their accessibility and reuse. Existing ontology verbalization approaches tend to rely on rule-based o…

- **[Toward Bounding Coding-Agent Autonomy in Software Maintenance: A Pilot Study of Boundary Contracts](https://arxiv.org/abs/2611.01265v1)**
  - *Heeyong Eun, Seungyeon Chung, Hyejee Park et al.*
  - `2026-10-31`
  - As coding agents gain greater autonomy to modify software repositories, relevant context alone does not define their operational authority. An artifact may be relevant to a maintenance task while being inappropriate to edit; conversely, another artifact may be required even when…

- **[Satisfied, Not Solving: Wireheading of Bounded Homeostatic Rewards in Reinforcement Learning](https://arxiv.org/abs/2611.01183v1)**
  - *Chase J. Metoyer*
  - `2026-10-31`
  - Bounded intrinsic rewards are often assumed to be safe from exploitation: if a signal can yield at most a fixed amount, gaming it should not pay. We test this for a homeostatic satiation reward, in which needs build up and relieving them is rewarding, and give the agent a cheap a…

- **[CivicBench: A Benchmark and Memory Framework for Web-Based Civic Data Analytics](https://arxiv.org/abs/2611.01145v1)**
  - *Yangyu Wu, Siru Zhong, Haoyuan Liang et al.*
  - `2026-10-31`
  - Municipalities publish service requests, geographic boundaries, weather observations, demographic estimates, and operational guidance through independently maintained Web portals. Civic analysis must combine these sources while preserving their schemas, source links, spatial and…

- **[Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](https://arxiv.org/abs/2611.01112v1)**
  - *Chengcheng Wang, Yuheng Shi, Siyu Xu et al.*
  - `2026-10-31`
  - Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies. On RoboDojo, a large planning-execution gap separates high-level task decisions from physical execution: removing arm execution raises GPT-6 Astra's…

- **[Dependable Agents Need Hard and Fuzzy Rules](https://arxiv.org/abs/2611.01043v1)**
  - *Frederick Roth*
  - `2026-10-31`
  - Language models let software read requests in ordinary language, but they keep rules as people do: usually, and less so under pressure. Conventional code keeps rules exactly, but it cannot read a request. We argue that dependable agents need both, because the two kinds of rule co…

- **[Constraint Dependency Graph Retrieval for Compliance Detection on Long SKILL Documents](https://arxiv.org/abs/2611.01042v1)**
  - *Shuaitao Zhao, Feng Ni, Lichao Ma et al.*
  - `2026-10-31`
  - Large Language Model (LLM) agents carry out business operations under enterprise documents we refer to as SKILL documents, which take the form of standard operating procedures (SOPs) that state the conditions to verify and the actions to take before an operation proceeds. Long, d…

- **[GURU: A Hierarchical Neuro-Symbolic Multi-Agent System for Verification-Aware Automation of Mission-Critical Digital Engineering and Operations](https://arxiv.org/abs/2611.01001v1)**
  - *Allan Grosvenor, Anton Zemlyansky, Abdul Wahab et al.*
  - `2026-10-31`
  - An AI can find a safe action faster than any human, but it must never decide what counts as safe. We present GURU, a hierarchical neuro-symbolic multi-agent system for mission-critical digital engineering and operations, built on one partition of authority: learned models propose…

- **[Pulse: Long-Horizon Tasks Need Streaming Personalization](https://arxiv.org/abs/2611.00988v1)**
  - *Qijia Zhuang, Jialiang Liang, Yuxiang Ren*
  - `2026-10-31`
  - Large language model agents increasingly undertake complex, long-horizon tasks that benefit from sustained personalized support through long-term memory. Existing memory-augmented methods retrieve and use memory primarily from the initial request, with limited awareness of ongoin…

- **[SNAPPerf: Software-Aware Tabular Foundation Model for Retraining-Free Performance Prediction of Configurable Systems](https://arxiv.org/abs/2611.00944v1)**
  - *Amine Lbath, Massih-Reza Amini, Vadim Okun*
  - `2026-10-31`
  - Modern software systems expose hundreds of configuration options whose combinations can substantially affect execution time, memory and energy usage. Measuring software performance resulting from a configuration set requires running a realistic workload. Since the configuration s…

- **[Illusion: Safeguarding Topology Confidentiality in LLM Multi-Agent Systems via Behavior-Preserving Obfuscation](https://arxiv.org/abs/2611.00923v1)**
  - *Yiu-Fai Cheung, Hongzhi Guo, Miao Pan et al.*
  - `2026-10-31`
  - The communication topology of Large Language Model Multi-Agent Systems (LLM-MASs) governs how information propagates among agents and encodes critical domain knowledge and expert workflow design. It is valuable intellectual property and plays a decisive role in system utility and…

- **[Can Agentic AI Undermine Its Own Assurance Loop? Closed-Loop Dependency Assurance for Cognitive Network Digital Twins](https://arxiv.org/abs/2611.00838v1)**
  - *Ahmed Hussain, Konstantinos Kalogiannis, Salahuddin Salahuddin et al.*
  - `2026-10-31`
  - Agentic Artificial Intelligence (AI) and Network Digital Twins (NDTs) are increasingly combined to form Cognitive Digital Twins (CDTs) that translate operational intents into network changes and support closed-loop management. However, a network change may achieve its intended ob…

- **[AI Data Analysis: A New Approach - Multi-engine Joint State Data Analysis](https://arxiv.org/abs/2611.00807v1)**
  - *Jean Ye*
  - `2026-10-31`
  - AI data analysis today is three fragmented worlds: LLMs understand semantics but cannot compute; BI aggregates precisely but is stateless; ML processes large-scale data on a stateful kernel but lacks semantics. This paper proposes a combination mechanism, named Multi-engine Joint…

- **[Who Schedules Agent Memory? A Sidecar Approach to Long-Horizon Tasks](https://arxiv.org/abs/2611.00779v1)**
  - *Qijia Zhuang, Rui Liu, Yuxiang Ren*
  - `2026-10-31`
  - As large language model agents increasingly undertake complex, long-horizon tasks, memory has become an important component for supporting sustained decision-making and action. Existing methods primarily focus on memory storage, updating, and retrieval, but often overlook how mem…

- **[Decision-Centric Research: A Calibrated Decision Model and Benchmark for Scientific Agents](https://arxiv.org/abs/2611.00774v1)**
  - *Shaoning Zeng, Wen Huang, Xinzhong Zhu et al.*
  - `2026-10-31`
  - Scientific agents make consequential choices about evidence, next actions and research strategy, but choices embedded in generated text are difficult to evaluate independently. Decision-Centric Research (DCR) is introduced to make individual choices the common unit of supervision…

- **[Designing Informative Actions: Action Construction for Long-Horizon Research Agents](https://arxiv.org/abs/2611.00773v1)**
  - *Alkut Arxidin, Shaoning Zeng, Jianhang Zhou et al.*
  - `2026-10-31`
  - Large language model agents support automated scientific research by connecting literature analysis and planning with experimentation. Evaluating which action an agent selects does not establish which experiment its instruction specifies, because omitted interventions or replicat…

- **[Old Is Not False: Valid-Time Memory for Interactive Video World Models](https://arxiv.org/abs/2611.00758v1)**
  - *Ziming Wang, Chuyue Gong, Hongliang Cao et al.*
  - `2026-10-31`
  - Interactive video world models draw each frame from a memory bank of earlier frames stamped with their capture times. With frames, weights and noise fixed, reversing the timestamps of two views flips the state that generators of two families draw: they take the newest timestamp a…

- **[Architecting Fairness-Aware LLM Interactions](https://arxiv.org/abs/2611.00723v1)**
  - *Alessandra Parziale, Valeria Pontillo, Fabio Palomba et al.*
  - `2026-10-31`
  - Large Language Models (LLMs) are increasingly used as decision-support tools but may generate stereotypical, discriminatory, or unfair responses. As LLMs become embedded in decision-critical software systems, fairness can no longer be treated as a downstream evaluation step, but…

- **[SAVIER: Source-Anchored Visual Inspection and Evidence-Guided Repair for Vietnamese Cultural Text-to-Image Generation](https://arxiv.org/abs/2611.00722v1)**
  - *Gia-Huy Thai, Duc-Tien Khong, Trung-Nghia Le*
  - `2026-10-31`
  - We present SAVIER, a training-free, one-pass framework that repairs the depiction of a named Vietnamese cultural entity in a generated image while preserving the scene details requested by the user. The problem is hard because a plausible scene can miss the cues that identify the…

- **[Getting a Grip: Operating Human-Agent Software Teams Through Governed Messages](https://arxiv.org/abs/2611.00689v1)**
  - *Michael Granitzer, Kanishka Ghosh Dastidar, Andreas Einwiller et al.*
  - `2026-10-31`
  - Software is increasingly developed by teams in which several people direct many coding agents from different vendors. Such teams must establish who may request what from whom, which messages start work, which decisions bind, and who caused a change. We propose to govern a human-a…

- **[FastAgent: A Physics-Aware FastFluent-to-Fluent Workflow for Rapid CFD Screening and Industrial Steam Dewaxing Design](https://arxiv.org/abs/2611.00645v1)**
  - *Chen YanKai, Yu QiuHeng, Yuan Man et al.*
  - `2026-10-31`
  - Industrial computational fluid dynamics (CFD) becomes costly when complex geometries, long transients and coupled physics must be evaluated across large design spaces. We introduce FastAgent, a physics-aware campaign controller built around FastFluent, a lightweight numerical eng…

- **[Autonomous Analysis of Thermoelectric Materials Big Data by Multi-Agentic AI and Construction of a Knowledge Base and Specialized AI](https://arxiv.org/abs/2611.00627v1)**
  - *Yusuke Hashimoto, Takaaki Tomai*
  - `2026-10-31`
  - Extracting knowledge from large databases of experimental materials data requires repeated analyses and reusable records of their choices and results. We developed Multi-Agentic AI (MAA), a multi-agent system in which AI agents with distinct roles analyze experimental thermoelect…

- **[XLA from the Trenches: Correctness on TPU Workloads at Scale](https://arxiv.org/abs/2611.00624v1)**
  - *Ignacio Cano, Amir Saadat, Rishipal Singh Bhatia et al.*
  - `2026-10-31`
  - Accelerating modern foundational models has pushed domain-specific compilers toward increasingly complex, multi-tiered optimization pipelines. However, this heavy optimization focus introduces delicate tradeoffs between peak execution performance and correctness. Subtle codegen d…

- **[Low-Margin Branch Points in Deterministic LLM Deliberatio](https://arxiv.org/abs/2611.00546v1)**
  - *Hajime Shimao, Warut Khern-am-nua*
  - `2026-10-31`
  - Deterministic multi-agent LLM deliberation can exactly re- play a fixed transcript, yet exact replay alone does not test local resistance to controlled internal interventions. Because each response becomes context for later agents, a changed greedy token can redirect a transcript…

- **[Skill++: Towards Lifelong Agents via Routing-Aware Skill Refinement](https://arxiv.org/abs/2611.00544v1)**
  - *Hanrong Zhang, Minghao Liang, Jiawei Wu et al.*
  - `2026-10-31`
  - Large language model (LLM) agents extend their capabilities with skills, each with a name, a description, and a body. Under progressive disclosure, an LLM router selects skills by name and description alone and loads only the selected bodies. Skill libraries grow continually as u…

- **[AStockArena: Beyond Returns, Can We Entrust Real Capital to the Decisions of Financial Agents?](https://arxiv.org/abs/2611.00515v1)**
  - *Zeyu Liu, Sing Kwong Lai, Xuanzhi Feng et al.*
  - `2026-10-31`
  - Large language models (LLMs) are increasingly used in dynamic financial trading, yet real-time trading benchmarks mainly evaluate agents by cumulative returns and risk-adjusted performance. Such outcome metrics cannot show whether trades are faithfully reported, supported by avai…

- **[Do Social Influence Pressures Move LLM Agents? Evidence from Delegated Audit Judgment](https://arxiv.org/abs/2611.00508v1)**
  - *Richard Zhe Wang*
  - `2026-10-31`
  - Large language model (LLM) agents are rapidly being integrated into complex professional workflows such as auditing and entrusted with judgments under human review. Human auditors are known to yield to social influence pressures from superiors, peers and clients, and this paper a…

- **[Spotting the Artificial: Dialogic Humor Improvisation in Humans and LLMs](https://arxiv.org/abs/2611.00492v1)**
  - *Lizeth Palacios Patiño, Ximena Gutierrez-Vasques, Daniel Rodriguez*
  - `2026-10-31`
  - We propose a methodology for investigating the differences between natural and synthetic language in a challenging setting: humorous improvisational dialogue. Our experimental setting compares human-produced comedy improvisations with the dialogues generated by LLMs in a multi-ag…

- **[Threat Modeling Intimate Partner Abuse in Agentic Systems](https://arxiv.org/abs/2611.00489v1)**
  - *Natalie Grace Brigham, Eugene Bagdasarian, Franziska Roesner et al.*
  - `2026-10-31`
  - Agentic systems are AI-powered technologies capable of autonomous action within digital environments, such as sending emails or making reservations. They are deeply connected to external tools as well as users' data and resources, making them vulnerable to attacks which exploit t…

- **[MAPLE: A Multimodal Mobile Agent with Playbook-Learned Experience](https://arxiv.org/abs/2611.01351v1)**
  - *Jun Wang, Aurora Wei, Lucas Spangher et al.*
  - `2026-10-31`
  - Autonomous agents powered by vision-language models (VLMs) show great potential in navigating mobile graphical user interfaces (GUIs) to complete complex tasks. However, existing paradigms face fundamental scalability bottlenecks: fine-tuning requires massive high-fidelity datase…

- **[Alignment Flywheel-Guided Suppression Patching for Interactionless Inverse Reinforcement Learning](https://arxiv.org/abs/2611.01322v1)**
  - *Elias Malomgré, Pieter Simoens*
  - `2026-10-31`
  - Learned reward models allow reinforcement-learning agents to use demonstrations, implicit feedback, safety constraints, social norms, or other sources that do not provide a complete hand-designed scalar reward. However, a learned reward model can assign high reward to unwanted be…

- **[AgentCBO: Causal Belief Routing for Bayesian Optimization under Unknown Graphs](https://arxiv.org/abs/2611.01317v1)**
  - *Qiyu Wei, Xin Zhang, Richard Allmendinger et al.*
  - `2026-10-31`
  - Causal Bayesian optimization (CBO) typically relies on the unrealistic assumption of a perfectly known causal graph. Recent methods relax this constraint by coupling optimization with structure learning, but they often waste sample budgets on structural uncertainties that are irr…

- **[Learning What to Ask and What to Believe: Distilling a Variational Bayesian Agent into Language Models](https://arxiv.org/abs/2611.01245v1)**
  - *Baichuan Li, Yanling Chang, Alfredo Garcia*
  - `2026-10-31`
  - Interactive tasks such as eliciting a user's preferences or diagnosing a hidden mechanism require an agent to track its uncertainty over a latent state, ask informative questions and act on the answers. Language models have no explicit mechanism for this, whereas Bayesian informa…

- **[Synergetic Autonomous Intelligence: Three Axioms for Recursive Semi-Closed Learning](https://arxiv.org/abs/2611.01070v1)**
  - *Dongxu Li*
  - `2026-10-31`
  - We introduce Synergetic Autonomous Intelligence (SAI), a theory and design program for learning systems that form, preserve, revise, and compose relations while continuing to learn. SAI is built on three axioms: consequential distinctions must not become orphaned (U); identity is…

- **[Jet-QSparse: Accelerating Agentic LLM Inference with 4-Bit Sparse Attention](https://arxiv.org/abs/2611.01022v1)**
  - *Haozhan Tang, Hao Kang, Meng Lu et al.*
  - `2026-10-31`
  - Long-horizon reasoning and agentic workloads strain KV-cache capacity and decode attention throughput. We present Jet-QSparse, a training-free method that combines compact NVFP4 cache storage with native FP4 query-key computation on Blackwell tensor cores. A dense scan scores the…

- **[What Breaks and What Comes Back: Capability Damage and Recovery in Depth-Pruned Small Language Models](https://arxiv.org/abs/2611.00877v1)**
  - *Piyush Dhoka, Vedant Pandhare, Varun Inamdar et al.*
  - `2026-10-31`
  - Depth pruning removes whole Transformer blocks to make a language model smaller and faster, but the damage is not spread evenly across what the model can do, and a short fine-tuning run, called healing, decides what comes back. We measure this for small models used as agents. Fou…

- **[Can agents reliably design therapeutic antibodies?](https://arxiv.org/abs/2611.00558v1)**
  - *Asli Alpman, Nick Bhattacharya, Aaron Solomon et al.*
  - `2026-10-31`
  - Recent work has demonstrated agents driving protein design workflows, either through orchestration of specialized tools or direct manipulation of sequences. Yet the fidelity with which agents follow protein design instructions and the factors contributing to their effectiveness r…

- **[CompSkill: Compiling Execution Experience for Skill Retrieval](https://arxiv.org/abs/2611.01115v1)**
  - *Qi Shen, Ziyue Zhu, Yongqing Jiang et al.*
  - `2026-10-31`
  - LLM agents increasingly rely on skill documents, yet most retrievers rank them by description alone and ignore what earlier executions revealed, even though a relevant skill can hurt execution. We present CompSkill, which indexes skills with learned 512-d keys and compiles matche…

- **[When 200 OK Is Not an Answer: Silent Fetch Failures in Agentic Web Content Acquisition](https://arxiv.org/abs/2611.00884v1)**
  - *Shuyang Zhang*
  - `2026-10-31`
  - Web agents and answer engines fetch pages at question time, and liveness checks of cited sources treat an HTTP 200 response as success. We measure how often that assumption fails and what it does to measurements built on fetched pages. We fetched 10,307 URLs in three days with a…

- **[Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand](https://arxiv.org/abs/2611.00883v1)**
  - *George Ling, Shanshan Zhong, Lijin Yang et al.*
  - `2026-10-31`
  - Benchmark compression reduces the often prohibitive time and cost of model evaluation by evaluating models on a small benchmark subset that closely matches full-benchmark results. To quantify estimation error, we derive an accurate analytical approximation to the error distributi…

- **[Robust Safety Assurance for Robotic Swarms Using Decentralized Collision Verification](https://arxiv.org/abs/2611.01081v1)**
  - *Grant Phillips, Hoang-Dung Tran, Justin M. Bradley*
  - `2026-10-31`
  - In this paper we present the methodologies, results, and analysis used to deploy a decentralized safety verification algorithm on a robotic swarm to prevent collisions at runtime in an outdoor environment. Typically, approaches toward verification of swarms of cyber-physical syst…

- **[PhoneValue-Bench: A Multimodal Benchmark and Datasets for Consumer Smartphone Recommerce Valuation](https://arxiv.org/abs/2611.00791v1)**
  - *Zihan Deng, Jun Gao*
  - `2026-10-31`
  - As consumer smartphone recommerce scales, buyers must quote binding repurchase prices from seller-uploaded multi-view photos and diagnostic screenshots before devices reach the warehouse. Accurate remote valuation requires fusing noisy cosmetic evidence with identity, battery, lo…


## Harness  (117)

### AAAI

- **[GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Through Code Repository Leveraging](https://arxiv.org/abs/2508.18993)**
  - *Zi-Yi Ni, Hua-Can Wang, Shuo Zhang et al.*
  - **AAAI 2025** · `2025-08-26`
  - Beyond scratch coding, exploiting large-scale code repositories (e.g., GitHub) for practical tasks is vital in real-world software development, yet current benchmarks rarely evaluate code agents in such authentic, workflow-driven scenarios. 
To bridge this gap, we introduce GitTa…

- **[Democratizing Diplomacy: A Harness for Evaluating Any Large Language Model on Full-Press Diplomacy](https://arxiv.org/abs/2508.07485)**
  - *Alexander Duffy, Samuel J. Paech, Ishana Shastri et al.*
  - **AAAI 2025** · `2025-08-10`
  - We present the first evaluation harness that enables any out-of-the-box, local, Large Language Models (LLMs) to play full-press Diplomacy without fine-tuning or specialized training. Previous work required frontier LLMs, or fine-tuning, due to the high complexity and information…


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

- **[REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://arxiv.org/abs/2504.11543)**
  - *Divyansh Garg, Shaun VanWeelden, Diego Caples et al.*
  - **NeurIPS 2025** · `2025-04-15`
  - We introduce REAL, a benchmark and framework for multi-turn agent evaluations on deterministic simulations of real-world websites. REAL comprises high-fidelity, deterministic replicas of 11 widely-used websites across domains such as e-commerce, travel, communication, and profess…


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


### ICLR

- **[MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents](https://arxiv.org/abs/2510.15994)**
  - *Dong-Sen Zhang, Ze-Kun Li, Xu Luo et al.*
  - **ICLR 2025** · `2025-10-14`
  - The Model Context Protocol (MCP) standardizes how large language model (LLM) agents discover, describe, and call external tools. While MCP unlocks broad interoperability, it also enlarges the attack surface by making tools first-class, composable objects with natural-language met…


### KDD

- **[CR-Bench-v2: Evaluating the Real-World Utility of AI Code Review Agents](https://arxiv.org/abs/2611.02566v1)**
  - *Kristen Pereira, Neelabh Sinha, Rajat Ghosh et al.*
  - **KDD** · `2026-11-02`
  - The rapid growth of automated code generation has created a pressing need for automated code review. Yet code review resists full automation: it depends on context beyond the \textit{diff}, on the author's intent, and on judgments about design and maintainability on which even ex…


### ACL

- **[NorEval: A Norwegian Language Understanding and Generation Evaluation Benchmark](https://arxiv.org/abs/2504.07749)**
  - *Vladislav Mikhailov, T. Enstad, David Samuel et al.*
  - **ACL 2025** · `2025-04-10`
  - This paper introduces NorEval, a new and comprehensive evaluation suite for large-scale standardized benchmarking of Norwegian generative language models (LMs). NorEval consists of 24 high-quality human-created datasets -- of which five are created from scratch. In contrast to ex…


### EMNLP

- **[R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)**
  - *Shuai-Jie She, Jun-Xiao Liu, Yifeng Liu et al.*
  - **EMNLP 2025** · `2025-03-27`
  - Large language models (LLMs) inevitably make mistakes when performing step-by-step mathematical reasoning. Process Reward Models (PRMs) have emerged as a promising solution by evaluating each reasoning step. However, existing PRMs typically output evaluation scores directly, limi…


### Other / arXiv

- **[CoworkOS:Scaling Agent Coworkers for Real-world Automation](https://arxiv.org/abs/2611.03178)**
  - *Jiajie Jin, Guanting Dong, Chengjun Pan et al.*
  - 🤗 Featured · `2026-11-02`
  - Rapid advances in cowork agents are shifting human-AI collaboration toward real-world automation, delivering software, designs, and other artifacts. However, such productivity work demands both high-quality delivery on complex productivity tasks and continued monitoring and decis…

- **[Can Coding Agents Sustain Continual Evolution without Forgetting?](https://arxiv.org/abs/2611.03219)**
  - *Shangziqi Zhao, Yitong Zhang, Jia Li*
  - 🤗 Featured · `2026-11-02`
  - Recently, harness self-evolution has emerged as an important paradigm for improving agent performance. Prior studies show that evolving the agent harness can effectively enhance agent capabilities without modifying the foundation model's parameters. We find that existing approach…

- **[Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://arxiv.org/abs/2611.01560)**
  - *Jiarui Yuan, Yuxin Zuo, Xiaoyu Huang et al.*
  - 🤗 Featured · `2026-11-01`

- **[NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale](https://arxiv.org/abs/2611.02102)**
  - *Chaoyun Zhang, Bingxuan Li, Pinxue Guo et al.*
  - 🤗 Featured · `2026-11-01`
  - Scaling computer-use agents from individual actions to complex software work requires experience that connects decisions to complete outcomes. We present NorthCUA, an integrated system for turbocharging computer-use agents through experience at scale. Its Experience Flywheel supp…

- **[When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?](https://arxiv.org/abs/2611.01815)**
  - *Anton Hristov, Aleksandar Slavov, Vasil Vasilev*
  - 🤗 Featured · `2026-11-01`
  - Prediction errors from video world models are often treated as physical surprise, but they can also reflect appearance, static content, motion, or ordinary prediction difficulty. We present an evaluation framework that separates what frozen representations contain, how they organ…

- **[TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents](https://arxiv.org/abs/2610.41216)**
  - *Kehong Gong, Xiaoxu Zheng, Guanli Hou et al.*
  - 🤗 Featured · `2026-10-30`

- **[Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](https://arxiv.org/abs/2610.40191)**
  - *Liaoyuan Fan, Yuhao Zheng, Dongxing Mao et al.*
  - 🤗 Featured · `2026-10-29`

- **[Harvesting SWE Benchmarks from Wild Vibe Coding Sessions](https://arxiv.org/abs/2611.02440)**
  - *Ao Lu, Yuanhao Zeng, Shaocheng Lan et al.*
  - 🤗 · `2026-11-02`
  - Development teams need reproducible tasks from their own repositories and workflows to evaluate coding agents. Conversational developer-agent collaboration ("vibe coding") produces abundant coding sessions and repository checkpoints, but requirements evolve across turns, unrelate…

- **[Decision Models as Policy Gates for Coding Agents: Explicit Policy Boundaries Improve Detection and Reduce False Alarms](https://arxiv.org/abs/2611.02155)**
  - *James P. Beno*
  - 🤗 · `2026-11-01`
  - Coding agents can destroy data, leak secrets and message the wrong person faster than a human can review. Could a decision model catch these risks at runtime? We evaluated 22 hosted decision models and two prompted general models as classifiers for a multi-rule policy engine. A s…

- **[Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM for Investigative Analysis](https://arxiv.org/abs/2611.03434v1)**
  - *Shai Nahum Gefen, Vered Chassida, Dmitry Basin et al.*
  - `2026-11-02`
  - Government intelligence teams need LLM agents that can analyze large, messy evidence collections, but security and cost constraints often rule out hosted frontier models and broad, hard-to-audit tool surfaces. We report CLEO: Constrained Loop for Environment Optimization, a metho…

- **[DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412v1)**
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

- **[Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization](https://arxiv.org/abs/2611.03517v1)**
  - *Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su et al.*
  - `2026-11-02`
  - LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff. Scripted agents fix what the model does at each step, via a learned policy, an optimization menu, or fixed roles, and are sample-efficient where the recipe applies and stall where it does not.…

- **[HLSClaw: Bringing Vibe Coding to High-Level Synthesis through Skill-Based Agentic Harness](https://arxiv.org/abs/2611.02784v1)**
  - *Jinming Ge, Shang Liu, Jiawei Liang et al.*
  - `2026-11-02`
  - LLM agents are rapidly shifting software development toward intent-driven \emph{vibe coding}, yet their effectiveness drops sharply in high-level synthesis (HLS), where code optimization must jointly consider design structure, directive search, and downstream hardware constraints…

- **[VeriHarm-Bench: Measuring Harmful Success in LLM Coding Agents Verifiably](https://arxiv.org/abs/2611.03575v1)**
  - *Wei-Lin Chen, Zhepei Wei, Xinyu Zhu et al.*
  - `2026-11-02`
  - Large language model (LLM) coding agents increasingly operate with shell access, allowing them to write scripts, move files, alter permissions, and modify system configurations. However, an agent may achieve a user's goal while causing unintended harm, such as deleting unrelated…

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

- **[Efficient Closure Learning in Dynamical Systems: A Comparison of Data-Assimilated and Embedded Approaches](https://arxiv.org/abs/2611.03612v1)**
  - *Rileigh Bandy, Teresa Portone, Mohammad Khalil et al.*
  - `2026-11-02`
  - Increased computing power has transformed computational science and improved predictive capabilities for complex systems, but many phenomena still exceed current simulation capabilities or require rapid evaluations for fast design iterations. Closure models address this challenge…

- **[Data-Scarce, Multi-Granular, Multimodal: Benchmark Design for Biosynthetic Gene Clusters](https://arxiv.org/abs/2611.02275v1)**
  - *Hanlin Xiao, Eriko Takano, Mauricio A. Álvarez et al.*
  - `2026-11-01`
  - Biosynthetic gene clusters (BGCs) are co-located genes that encode the biosynthesis of specialized metabolites, an important source of antibiotics, anticancer agents, immunosuppressants, and agricultural bioactives. Deep learning, particularly self-supervised foundation models, h…

- **[ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and Cost](https://arxiv.org/abs/2611.02079v1)**
  - *Xingzhi Qian, Sungho Park, Rongyuan Tan et al.*
  - `2026-11-01`
  - Harness optimization can substantially improve LLM agents without modifying model weights, but existing methods primarily optimize response quality. Extending them to joint quality--cost optimization introduces a challenge: applying the deployment preference during intermediate u…

- **[Step-Zero Attack: Agent Safety Before Observability](https://arxiv.org/abs/2611.01953v1)**
  - *Tian Qin, Yuhang Jiang, Junzhe Chen et al.*
  - `2026-11-01`
  - Existing attacks and defenses for coding agents act once content enters the model context: injected text persuades the model, and guards inspect what the model reads. Yet to judge whether processing an unknown archive, network response, or image is safe, an agent often must proce…

- **[RECEIPT: Measuring and Repairing the Return Assumption of LLM Agents in Web Service Operations](https://arxiv.org/abs/2611.01930v1)**
  - *Boyang Yang, Ziyao Yang, Yu Zhang et al.*
  - `2026-11-01`
  - LLM agents operate Web infrastructure from the command line and rely on a return assumption, namely that each tool call returns within a bounded time and with its requested action finished. Many commands, however, ask a question before they act, and the agent's harness either clo…

- **[Latent Harness: Compiling Agent Behaviors into Post-Block Activation Shifts](https://arxiv.org/abs/2611.01415v1)**
  - *Ran Li, Shimin Di, Zeyu Ren et al.*
  - `2026-11-01`
  - Harness engineering and self-evolving agents improve language-model agents quickly, yet their gains live outside the model. The harness is re-sent and re-paid on every call, and the standard route to internalization is a weight update that is costly to iterate and fixed once merg…

- **[Retrain, Alert, or Rollback? A Three-Response Decision Framework for Production ML Under Concept Drift](https://arxiv.org/abs/2611.02251v1)**
  - *Ali Sadeghian, Alireza Shafaei, Hamid Hadibeik et al.*
  - `2026-11-01`
  - When a deployed model degrades under concept drift, an operator can retrain it, raise an alert and monitor, or roll back. Yet most drift-adaptation methods consider only retraining. We present RAR (Retrain-Alert-Rollback), a state machine that gives each response an explicit trig…

- **[FinForesight: A Diagnostic Backtesting Benchmark for Deep Research Systems in Financial Forecasting](https://arxiv.org/abs/2611.01621v1)**
  - *Fengyuan Liu, Mukai Li, Jieshun You et al.*
  - `2026-11-01`
  - Anticipating financial outcomes requires synthesizing evolving evidence and reasoning under uncertainty, making deep research systems promising tools for forecasting. Yet evaluating forecasting ability is challenging because historical backtests may reward memorized outcomes or i…

- **[InformedXRD: Reproducible Benchmarks and Physics-Informed Evaluation for Powder Diffraction Symmetry Classification](https://arxiv.org/abs/2611.01525v1)**
  - *Edward G Friedman, Elizabeth J. Baggett, Abhishek Shetty et al.*
  - `2026-11-01`
  - Machine learning for powder diffraction (PXRD) symmetry classification is being trained at scale, yet the field lacks a common evaluation standard: papers report results on different subsets of experimental archives, with different target taxonomies, preprocessing, and metrics, a…

- **[Adversarial Robustness of Retrieval-Based Fact-Checking: Detecting and Mitigating Evidence Contamination](https://arxiv.org/abs/2611.02139v1)**
  - *Alamgir Munir Qazi, John P. McCrae, Jamal Abdul Nasir*
  - `2026-11-01`
  - Retrieval-based fact-checking systems ground verification in large document collections, creating a critical vulnerability: adversarial evidence contamination. We demonstrate that factually inconsistent but contextually coherent evidence generated to satisfy both retrieval-simila…

- **[Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](https://arxiv.org/abs/2611.01112v1)**
  - *Chengcheng Wang, Yuheng Shi, Siyu Xu et al.*
  - `2026-10-31`
  - Vision-language models can interpret instructions and plan manipulation tasks, yet struggle when acting directly as robot policies. On RoboDojo, a large planning-execution gap separates high-level task decisions from physical execution: removing arm execution raises GPT-6 Astra's…

- **[GURU: A Hierarchical Neuro-Symbolic Multi-Agent System for Verification-Aware Automation of Mission-Critical Digital Engineering and Operations](https://arxiv.org/abs/2611.01001v1)**
  - *Allan Grosvenor, Anton Zemlyansky, Abdul Wahab et al.*
  - `2026-10-31`
  - An AI can find a safe action faster than any human, but it must never decide what counts as safe. We present GURU, a hierarchical neuro-symbolic multi-agent system for mission-critical digital engineering and operations, built on one partition of authority: learned models propose…

- **[Skill++: Towards Lifelong Agents via Routing-Aware Skill Refinement](https://arxiv.org/abs/2611.00544v1)**
  - *Hanrong Zhang, Minghao Liang, Jiawei Wu et al.*
  - `2026-10-31`
  - Large language model (LLM) agents extend their capabilities with skills, each with a name, a description, and a body. Under progressive disclosure, an LLM router selects skills by name and description alone and loads only the selected bodies. Skill libraries grow continually as u…

- **[Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand](https://arxiv.org/abs/2611.00883v1)**
  - *George Ling, Shanshan Zhong, Lijin Yang et al.*
  - `2026-10-31`
  - Benchmark compression reduces the often prohibitive time and cost of model evaluation by evaluating models on a small benchmark subset that closely matches full-benchmark results. To quantify estimation error, we derive an accurate analytical approximation to the error distributi…

- **[What Do LLM Judges Actually Verify? Matched Controls and Record Gaps for Document Currency](https://arxiv.org/abs/2611.01311v1)**
  - *Unnati Shah, Samruddhi Kakade, Aum Patel*
  - `2026-10-31`
  - LLM judges often check, against an amendment record, whether the documents an answer cites are still in force. Such records are rarely complete. From a table of replacements, our test generates matched answers citing a replaced document, its successor, the replaced document befor…

- **[Selecting LLM-Generated Hypotheses Raises Truth Beyond What an LLM Panel Expects: A Pre-registered Study on NAS-Bench-201 and HPOBench](https://arxiv.org/abs/2611.00643v1)**
  - *Shanglin Yang, Zhan Shi*
  - `2026-10-31`
  - LLM research-ideation systems aim for hypotheses that are both true and non-obvious, yet neither property can normally be checked. We build a testbed in which both can. Generators propose conditional interaction claims about two fully tabulated benchmarks, NAS-Bench-201 and HPOBe…

- **[Answer Correction with Verifiable Rewards: A Gemma-Family Study of Multi-View Driving QA](https://arxiv.org/abs/2611.00828v1)**
  - *T N Rickesh, Pranav Vinodh, Sowmya Kamath S*
  - `2026-10-31`
  - Multi-camera driving question answering provides a discrete test of vision-language models, but post-training gains can reflect changed selected answers or improved answer extraction. We investigate this distinction within the Gemma model family using archived, task-linked WaymoQ…

- **[Lightweight Representation Learning for Low Tucker Rank Tensors](https://arxiv.org/abs/2611.01168v1)**
  - *Hiroki Hasegawa, Yukihiko Okada*
  - `2026-10-31`
  - Low Tucker rank tensors provide compact representations of multidimensional dependencies, but standard learning pipelines can incur substantial computational and memory overhead from redundant intermediate quantities. We reduce this overhead without modifying the underlying repre…

- **[PhoneValue-Bench: A Multimodal Benchmark and Datasets for Consumer Smartphone Recommerce Valuation](https://arxiv.org/abs/2611.00791v1)**
  - *Zihan Deng, Jun Gao*
  - `2026-10-31`
  - As consumer smartphone recommerce scales, buyers must quote binding repurchase prices from seller-uploaded multi-view photos and diagnostic screenshots before devices reach the warehouse. Accurate remote valuation requires fusing noisy cosmetic evidence with identity, battery, lo…

- **[X-World 1.6: Building Controllable Virtual Cities with World Models](https://arxiv.org/abs/2611.00596v1)**
  - *XPeng, :, Boyang Wang et al.*
  - `2026-10-31`
  - Deploying generative world models for end-to-end closed-loop evaluation and policy learning requires precise scenario control, consistent observations, and sustained generation quality during extended interactions. This report presents \emph{X-World~1.6}, advancing X-World~1.0 to…


## Finance  (159)

### NeurIPS

- **[ARTE: Agentic Refinement through Trade Execution for High-Frequency Trading Strategy Discovery](https://openreview.net/forum?id=VisvXioWmG)**
  - **NeurIPS 2025** · OpenReview · `2026-10-12`
  - Existing LLM-based trading strategy development primarily uses aggregated price and volume data, which omit within-interval event order and displayed order book changes. Tick-level trade and quote observations preserve this information, but their scale makes the full history impr…

- **[The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets](https://openreview.net/forum?id=XZpIu68yW6)**
  - *Shenzhe Zhu, Jiao Sun, Yi Nian et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-01`
  - AI agents are increasingly used in consumer-facing applications to assist with tasks such as product search, negotiation, and transaction execution. In this paper, we investigate a future setting where both consumers and merchants authorize AI agents to automate the negotiations…


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


### ACL

- **[Non-Convex Market Makers: Coherence without Convexity, Friction, and Parallel Composition](https://arxiv.org/abs/2611.00502v1)**
  - *Peter Cotton*
  - **ACL** · `2026-10-31`
  - Cost-function market makers are always assumed convex, and convexity is not what makes them coherent. For a path-independent maker the exact no-arbitrage condition is a chord condition, that every chord slope of the cost lie in the convex hull of payoffs; convexity enters the sta…


### Other / arXiv

- **[Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents](https://arxiv.org/abs/2611.03092)**
  - *Zheng Wu, Xinbei Ma, Yao Yao et al.*
  - 🤗 Featured · `2026-11-02`
  - Personal AI agents are increasingly capable of handling long-horizon tasks across applications, yet users often need to invest substantial effort in specifying goals, resolving ambiguity, and verifying outcomes. We argue that progress should be measured by how effectively agents…

- **[DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects](https://arxiv.org/abs/2611.03412v1)**
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

- **[TensorLOB: Structure-Preserving Tensor Learning for Limit Order Book Forecasting](https://arxiv.org/abs/2611.02866v1)**
  - *Yuxuan Gu, Danilo Mandic*
  - `2026-11-02`
  - The limit order book (LOB) records outstanding buy and sell orders across multiple price levels. Its state evolves over time across market side, price level, and order attribute, naturally forming a multiway structure. However, existing LOB models typically flatten these dimensio…

- **[Improving Financial Cybersecurity Through Fraud Transaction Detection with Deep Learning](https://arxiv.org/abs/2611.02312v1)**
  - *Harish Kant Pathak, Rahul Kumar*
  - `2026-11-02`
  - Financial fraud detection remains a critical challenge in cybersecurity, with traditional rule-based systems struggling to keep pace with evolving attack patterns. This paper presents a deep learning approach for fraud transaction detection, leveraging neural network architecture…

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

- **[Herding or Racing? Decomposing Cross-Account Order-Flow Persistence in On-Chain Markets](https://arxiv.org/abs/2611.02616v1)**
  - *Yichong Bai, Dingyue Kan*
  - `2026-11-02`
  - Most of the autocorrelation in trade signs on decentralized exchanges comes from pairs of trades sent by different wallets. For Uniswap v3, this has been read as herding dominating order splitting -- the reverse of what equity markets show. We show that this herding share mixes t…

- **[Auditing Representation-Space Fraud Detection: A Bayesian IRL Framework for Calibrated Uncertainty and Its Limits](https://arxiv.org/abs/2611.02673v1)**
  - *Shivam Swarup, Divya Prakash Shrivastava, Rakesh Thakur*
  - `2026-11-02`
  - Shilling detectors for recommender systems are almost always evaluated by one number, detection AUROC, with no account of when it can be trusted. We audit representation-space detection with VEIL (Variational Evaluation via Inverse-reinforcement Learning), a pairwise (Bradley-Ter…

- **[Qubrio: High-Performance Quantum Compilation via Multi-Agent LLM Collaboration](https://arxiv.org/abs/2611.02269v1)**
  - *Jixuan Ruan, Zhuo Cui, Zhengding Hu et al.*
  - `2026-11-01`
  - Large Language Models (LLMs) offer an adaptable alternative to traditional quantum compilation heuristics, which bottleneck progress by demanding costly manual redesigns whenever hardware evolves. However, naive single-pass LLM approaches fail under the unique challenges introduc…

- **[Decoupled Predictive Decision Making: A Shared Conditional Predictor for Agents](https://arxiv.org/abs/2611.02075v1)**
  - *Lang Mo, Xingxuan Zhang, Qi Wang et al.*
  - `2026-11-01`
  - Agent decisions depend on empirical relationships that deployment observations reveal and task descriptions alone may leave unresolved. We introduce Decoupled Predictive Decision Making (DPDM), an architecture that formulates heterogeneous agent decisions as conditional predictio…

- **[LARK: Lean-Assisted Reasoning for LLM-Generated GPU Kernels](https://arxiv.org/abs/2611.02028v1)**
  - *Zixi Zhang, Jiayi Nie, Haoran Wu et al.*
  - `2026-11-01`
  - Efficient GPU kernels are typically low-level and hardware-specific, and LLM agents can now generate them faster than experts can verify. Existing approaches rely on testing, which provides evidence but not a guarantee of correctness. We introduce LARK, an agentic framework that…

- **[TrackMem: Tracking Evolving Beliefs in Long-Horizon Financial Dialogue](https://arxiv.org/abs/2611.02001v1)**
  - *Austin M. Y. Cheung, Harsh Vardhan Gupta, Go Nam Lui et al.*
  - `2026-11-01`
  - Memory systems for LLM agents are evaluated mostly on social dialogue, where facts accumulate and rarely change, so remembering reduces largely to finding the turn in which something was said. Financial dialogue breaks this assumption: figures are revised, stances shift without b…

- **[Launder-Bench: Can Repository-Level Agentic Code Laundering Be Detected?](https://arxiv.org/abs/2611.01966v1)**
  - *Yuntong Hu, Hongji Pu, Zimo Li et al.*
  - `2026-11-01`
  - Coding agents can now rewrite repository-scale codebases while preserving tested behavior, creating a new challenge for plagiarism detection, license auditing, and software provenance. We ask whether such rewrites can still be traced to their source. Existing clone benchmarks emp…

- **[AgenticMobility: An Open-Source Platform for Multi-AI-Agent Mobility Dynamics](https://arxiv.org/abs/2611.01918v1)**
  - *Jiaheng Xiao, Jiangtao Han, Jiachen Wang et al.*
  - `2026-11-01`
  - Understanding mobility dynamics and the effects of urban transportation management policies requires examining how individual travel decisions, traffic conditions, and policy interventions influence one another over time. We present AgenticMobility, an open-source experimental pl…

- **[MAC-Bench: Benchmarking Multi-Agent Collaboration via Interconnected Tasks](https://arxiv.org/abs/2611.01728v1)**
  - *Zerui Chen, Qinggang Zhang, Qichuan Liu et al.*
  - `2026-11-01`
  - Large language model (LLM)-based multi-agent systems (MAS) tackle challenging tasks by dividing work among agents and coordinating their contributions toward shared objectives. Evaluating these systems therefore requires benchmarks that assess not only task-solving performance bu…

- **[Principled Human-AI Collaboration in Agentic Workflows](https://arxiv.org/abs/2611.01566v1)**
  - *Young Hyun Cho, Will Wei Sun*
  - `2026-11-01`
  - Organizations adopting AI face the challenge of deciding which outputs can be released without human review while meeting the quality standards of human experts. We develop a statistical framework for delegating tasks between experts and black-box generate-verify workflows, in wh…

- **[A Self-Exploring and Self-Evolving Paradigm for Adaptive Edge AI Development](https://arxiv.org/abs/2611.01377v1)**
  - *Leming Shen, Qiang Yang, Xinyu Huang et al.*
  - `2026-11-01`
  - Large Language Models (LLMs) exhibit powerful code generation abilities, fostering agentic systems to automate edge AI application development. However, existing agents typically operate via fixed agentic workflows and predefined design spaces, struggling to handle rapidly evolvi…

- **[ReFrame: Silence-Aware Compute Reclamation for Full-Duplex Speech Models](https://arxiv.org/abs/2611.01835v1)**
  - *Zheng Zhou, Guanyi Chen, Jing Wei et al.*
  - `2026-11-01`
  - Full-duplex speech models execute dense model inference for every audio frame throughout a live interaction. This uniform framewise schedule creates sustained GPU load across dialogue states whose computation has strong, reusable temporal structure. ReFrame formulates full-duplex…

- **[Learning AI Agents, Market Makers, and Stress in Automated Markets](https://arxiv.org/abs/2611.01799v1)**
  - *Irene Aldridge*
  - `2026-11-01`
  - Automated markets increasingly route order flow from learning trading agents through automated market makers (AMMs). We model trader archetypes as AI agents defined by their reward functions and analyze the feedback they create on a constant-product AMM. Herd-dominated and arbitr…

- **[LLM-Enhanced Multimodal House Price Prediction using Structured, Textual, and Visual Features](https://arxiv.org/abs/2611.01615v1)**
  - *Khandokar Md. Rahat Hossain, Souvik Das, Tahsina Hashem et al.*
  - `2026-11-01`
  - Accurate house price prediction is essential for real estate buyers, sellers, agents, and financial institutions. Traditional methods rely primarily on structured data, e.g., number of bedrooms, bathrooms, parkings, but they overlook rich contextual information embedded in textua…

- **[Can Large Language Models Extend Their Agentic Capabilities to Goal Pursuit in Open-Ended Multi-Turn Interaction?](https://arxiv.org/abs/2611.01552v1)**
  - *Mingyu Chen, Jingkai Lin, Xiaofen Xing et al.*
  - `2026-11-01`
  - Goal pursuit in open-ended dialogue requires agents to adapt their actions to interaction feedback across successive exchanges. We investigate whether agentic capabilities developed for multi-step tool use carry over to dialogue organized through the model's native tool interface…

- **[Towards a Theory for the Design of Rules in Multi-Agent Systems: the case of Homogeneous Fleets](https://arxiv.org/abs/2611.02260v1)**
  - *Matteo Penlington, Lorenzo Fiaschi, Raj Kiriti Velicheti et al.*
  - `2026-11-01`
  - The regulation of systems composed of many interacting decentralised agents is a long-standing problem. This problem has typically been resolved by the imposition of rules. Rules resolve the limitations of sub-optimal agents whilst simultaneously aligning the behaviour of the age…

- **[FinForesight: A Diagnostic Backtesting Benchmark for Deep Research Systems in Financial Forecasting](https://arxiv.org/abs/2611.01621v1)**
  - *Fengyuan Liu, Mukai Li, Jieshun You et al.*
  - `2026-11-01`
  - Anticipating financial outcomes requires synthesizing evolving evidence and reasoning under uncertainty, making deep research systems promising tools for forecasting. Yet evaluating forecasting ability is challenging because historical backtests may reward memorized outcomes or i…

- **[Beyond Binary Detection: Type-Aware Hallucination Analysis and Hierarchical Detection in Financial Question Answering](https://arxiv.org/abs/2611.02258v1)**
  - *Xiongyu Chen, Sizhen Zhu, Zhuoer Wang*
  - `2026-11-01`
  - Large language models are increasingly used to answer questions over financial filings, where an unfaithful answer can mislead investment, compliance, or client decisions. Hallucination detectors are a common safeguard, but they are usually evaluated with a single binary score th…

- **[HQNN-CL: Regime-Aware Hybrid Quantum Neural Network with Continual Learning for Financial Forecasting](https://arxiv.org/abs/2611.02091v1)**
  - *Muhammad Atif Saeed, Akhtar Jamil, Subhan Ullah*
  - `2026-11-01`
  - Financial time-series forecasting is still difficult owing to the non-stationary nature of the market, regime changes, and catastrophic forgetting, which makes conventional deep learning models hard to adapt in the long term. To achieve uncertainty-aware robust financial forecast…

- **[Who Should Score the Cache? Mid-Depth Layers Are the Best Judges of KV-Cache Eviction](https://arxiv.org/abs/2611.02230v1)**
  - *Ekaterina Seregina*
  - `2026-11-01`
  - Key-value (KV) cache eviction methods rank tokens by attention scores, and each layer scores its own cache. To our knowledge, no eviction method asks which layer should score. We find, across twenty-one models, that the depth of the scoring layer governs eviction quality. On the…

- **[Sonny-ENS: demystifying machine-learning ensemble weather forecasting](https://arxiv.org/abs/2611.01614v1)**
  - *Minjong Cheon*
  - `2026-11-01`
  - Every weather forecast is uncertain, and decisions from flood warnings to energy trading depend on how well that uncertainty is quantified. Machine-learning (ML) ensembles now quantify it better than the best physics-based ensemble, yet two things about them remain opaque: whethe…

- **[AIDA: An AI Outage Registry with Evidence from On-Chain MEV](https://arxiv.org/abs/2611.01656v1)**
  - *Wenbin Wu*
  - `2026-11-01`
  - Generative AI coding tools have lowered the cost of writing trading software, but no systematic dataset records when these services fail. We introduce the AI Incident and Disruption Archive (AIDA), a multi-vendor registry of 5,868 deduplicated outage incidents across 30 providers…

- **[ProofPatch: Reviewing Lean Statements and Keeping the Reviews Valid as Formalizations Evolve](https://arxiv.org/abs/2611.01357v1)**
  - *Xujun Che, Depeng Xu, Jian Xiang et al.*
  - `2026-10-31`
  - The kernel of the Lean proof assistant checks that a proof establishes its statement. Whether the statement says what was intended is left to human reviewers. This is the old problem of validating a specification, and it grows more pressing as language models write formal stateme…

- **[Toward Bounding Coding-Agent Autonomy in Software Maintenance: A Pilot Study of Boundary Contracts](https://arxiv.org/abs/2611.01265v1)**
  - *Heeyong Eun, Seungyeon Chung, Hyejee Park et al.*
  - `2026-10-31`
  - As coding agents gain greater autonomy to modify software repositories, relevant context alone does not define their operational authority. An artifact may be relevant to a maintenance task while being inappropriate to edit; conversely, another artifact may be required even when…

- **[AI Data Analysis: A New Approach - Multi-engine Joint State Data Analysis](https://arxiv.org/abs/2611.00807v1)**
  - *Jean Ye*
  - `2026-10-31`
  - AI data analysis today is three fragmented worlds: LLMs understand semantics but cannot compute; BI aggregates precisely but is stateless; ML processes large-scale data on a stateful kernel but lacks semantics. This paper proposes a combination mechanism, named Multi-engine Joint…

- **[Who Schedules Agent Memory? A Sidecar Approach to Long-Horizon Tasks](https://arxiv.org/abs/2611.00779v1)**
  - *Qijia Zhuang, Rui Liu, Yuxiang Ren*
  - `2026-10-31`
  - As large language model agents increasingly undertake complex, long-horizon tasks, memory has become an important component for supporting sustained decision-making and action. Existing methods primarily focus on memory storage, updating, and retrieval, but often overlook how mem…

- **[Decision-Centric Research: A Calibrated Decision Model and Benchmark for Scientific Agents](https://arxiv.org/abs/2611.00774v1)**
  - *Shaoning Zeng, Wen Huang, Xinzhong Zhu et al.*
  - `2026-10-31`
  - Scientific agents make consequential choices about evidence, next actions and research strategy, but choices embedded in generated text are difficult to evaluate independently. Decision-Centric Research (DCR) is introduced to make individual choices the common unit of supervision…

- **[FastAgent: A Physics-Aware FastFluent-to-Fluent Workflow for Rapid CFD Screening and Industrial Steam Dewaxing Design](https://arxiv.org/abs/2611.00645v1)**
  - *Chen YanKai, Yu QiuHeng, Yuan Man et al.*
  - `2026-10-31`
  - Industrial computational fluid dynamics (CFD) becomes costly when complex geometries, long transients and coupled physics must be evaluated across large design spaces. We introduce FastAgent, a physics-aware campaign controller built around FastFluent, a lightweight numerical eng…

- **[Autonomous Analysis of Thermoelectric Materials Big Data by Multi-Agentic AI and Construction of a Knowledge Base and Specialized AI](https://arxiv.org/abs/2611.00627v1)**
  - *Yusuke Hashimoto, Takaaki Tomai*
  - `2026-10-31`
  - Extracting knowledge from large databases of experimental materials data requires repeated analyses and reusable records of their choices and results. We developed Multi-Agentic AI (MAA), a multi-agent system in which AI agents with distinct roles analyze experimental thermoelect…

- **[AStockArena: Beyond Returns, Can We Entrust Real Capital to the Decisions of Financial Agents?](https://arxiv.org/abs/2611.00515v1)**
  - *Zeyu Liu, Sing Kwong Lai, Xuanzhi Feng et al.*
  - `2026-10-31`
  - Large language models (LLMs) are increasingly used in dynamic financial trading, yet real-time trading benchmarks mainly evaluate agents by cumulative returns and risk-adjusted performance. Such outcome metrics cannot show whether trades are faithfully reported, supported by avai…

- **[Synergetic Autonomous Intelligence: Three Axioms for Recursive Semi-Closed Learning](https://arxiv.org/abs/2611.01070v1)**
  - *Dongxu Li*
  - `2026-10-31`
  - We introduce Synergetic Autonomous Intelligence (SAI), a theory and design program for learning systems that form, preserve, revise, and compose relations while continuing to learn. SAI is built on three axioms: consequential distinctions must not become orphaned (U); identity is…

- **[When 200 OK Is Not an Answer: Silent Fetch Failures in Agentic Web Content Acquisition](https://arxiv.org/abs/2611.00884v1)**
  - *Shuyang Zhang*
  - `2026-10-31`
  - Web agents and answer engines fetch pages at question time, and liveness checks of cited sources treat an HTTP 200 response as success. We measure how often that assumption fails and what it does to measurements built on fetched pages. We fetched 10,307 URLs in three days with a…

- **[Do Earnings Calls Help Predict Financial Restatements? Evaluating Text Beyond Public Firm Information](https://arxiv.org/abs/2611.01123v1)**
  - *Ahmet Efe, Shivank Sapra, Bilal Ahmed*
  - `2026-10-31`
  - Financial restatements correct errors in previously published financial reports. Could managers' language in earnings calls warn of them in advance? Comparing 109 calls that precede restatements with 218 matched control calls, we find that the text predicts restatements but adds…

- **[Where Causal Discovery Breaks on Real Data: Measuring the Assumptions One Property at a Time](https://arxiv.org/abs/2611.00484v1)**
  - *Padmaja Jonnalagedda, Avinash Baidya, Ruocheng Guo et al.*
  - `2026-10-31`
  - Causal discovery is usually evaluated on simulators or on systems whose ground truth follows from physics or design. When it fails on other real data, the failure is attributed to assumptions that may not hold, but which ones fail, and by how much, is rarely measured. We measure…

- **[RiskReason: A Benchmark for Verifiable Financial Risk Reasoning](https://arxiv.org/abs/2611.01236v1)**
  - *Nazanin Yousefi, Mohammadreza Ghafouri, Seyedreza Tavakoli et al.*
  - `2026-10-31`
  - Robust financial-risk inference requires more than mathematical correctness. Models must accurately apply conditional rules, maintain evolving financial states, and make decisions that respect operational constraints. This work introduces RiskReason, a benchmark for verifiable fi…

- **[Approximate clearing in financial networks with credit default swaps: hardness thresholds, a box algorithm, barriers, and exact solvency at bounded degree](https://arxiv.org/abs/2611.00855v1)**
  - *Michal Čertík*
  - `2026-10-31`
  - We study approximate clearing in financial networks with credit default swaps. For weak notions (W) and (I), we prove PPAD-hardness below a threshold approximately $0.2530$ and give a polynomial-time interval algorithm above a threshold approximately $0.2834$. On networks whose C…

- **[Optimal portfolio and consumption under no-shorting constraints: The exploratory formulation and reinforcement learning](https://arxiv.org/abs/2611.00700v1)**
  - *Xun Li, Xiang Yu, Fengyi Yuan et al.*
  - `2026-10-31`
  - We develop a reinforcement-learning framework for the continuous-time optimal portfolio-consumption via utility maximization under no-shorting portfolio constraints. We adopt the exploratory formulation under entropy regularization and impose no-shorting constraint through a comp…

- **[Non-asymptotic analysis of SGLD with discontinuous stochastic gradients: a new route to portfolio CVaR minimization](https://arxiv.org/abs/2611.00578v1)**
  - *Yan Ding, Sotirios Sabanis, Ying Zhang*
  - `2026-10-31`
  - Conditional-Value-at-Risk (CVaR) optimization is a fundamental tool in portfolio selection, yet its nonsmooth loss structure poses a challenge for the existing theory of stochastic gradient methods including associated Langevin algorithms. In particular, the positive-part loss an…


---
*Generated 2026-11-03 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
