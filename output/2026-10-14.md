# Daily Paper Digest — 2026-10-14 (Wednesday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**595 unique papers** (762 topic-entries — cross-topic papers counted once per category)

---

## Agent  (432)

### AAAI

- **[GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Through Code Repository Leveraging](https://arxiv.org/abs/2508.18993)**
  - *Zi-Yi Ni, Hua-Can Wang, Shuo Zhang et al.*
  - **AAAI 2025** · `2025-08-26`
  - Beyond scratch coding, exploiting large-scale code repositories (e.g., GitHub) for practical tasks is vital in real-world software development, yet current benchmarks rarely evaluate code agents in such authentic, workflow-driven scenarios. 
To bridge this gap, we introduce GitTa…

- **[AgentSwift: Efficient LLM Agent Design via Value-guided Hierarchical Search](https://arxiv.org/abs/2506.06017)**
  - *Yu Li, Lehui Li, Zhi-Hao Wu et al.*
  - **AAAI 2025** · `2025-06-06`
  - Large language model (LLM) agents have demonstrated strong capabilities across diverse domains, yet automated agent design remains a significant challenge. Current automated agent design approaches are often constrained by limited search spaces that primarily optimize workflows b…

- **[CoDe: Communication Delay-Tolerant Multi-Agent Collaboration via Dual Alignment of Intent and Timeliness](https://arxiv.org/abs/2501.05207)**
  - *Shoucheng Song, You-Fang Lin, Sheng Han et al.*
  - **AAAI 2025** · `2025-01-09`
  - Communication has been widely employed to enhance multi-agent collaboration. Previous research has typically assumed delay-free communication, a strong assumption that is challenging to meet in practice. However, real-world agents suffer from channel delays, receiving messages se…


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

- **[AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents](https://arxiv.org/abs/2506.00641)**
  - *Han-Jun Luo, Shenyu Dai, Chiming Ni et al.*
  - **NeurIPS 2025** · `2025-05-31`
  - Despite the rapid advancement of LLM-based agents, the reliable evaluation of their safety and security remains a significant challenge. Existing rule-based or LLM-based evaluators often miss dangers in agents'step-by-step actions, overlook subtle meanings, fail to see how small…

- **[MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement](https://arxiv.org/abs/2506.15692)**
  - *Jaehyun Nam, Jinsung Yoon, Jie-Feng Chen et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - Agents based on large language models (LLMs) for machine learning engineering (MLE) can automatically implement ML models via code generation. However, existing approaches to build such agents often rely heavily on inherent LLM knowledge and employ coarse exploration strategies t…

- **[AgentRecBench: Benchmarking LLM Agent-based Personalized Recommender Systems](https://arxiv.org/abs/2505.19623)**
  - *Yu Shang, Peijie Liu, Yuwei Yan et al.*
  - **NeurIPS 2025** · `2025-05-26`
  - The emergence of agentic recommender systems powered by Large Language Models (LLMs) represents a paradigm shift in personalized recommendations, leveraging LLMs' advanced reasoning and role-playing capabilities to enable autonomous, adaptive decision-making. Unlike traditional r…

- **[Distilling LLM Agent into Small Models with Retrieval and Code Tools](https://arxiv.org/abs/2505.17612)**
  - *Minki Kang, Jongwon Jeong, Seanie Lee et al.*
  - **NeurIPS 2025** · `2025-05-23`
  - Large language models (LLMs) excel at complex reasoning tasks but remain computationally expensive, limiting their practical deployment. To address this, recent works have focused on distilling reasoning capabilities into smaller language models (sLMs) using chain-of-thought (CoT…

- **[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)**
  - *Yuan-Te Li, Xu Yang, Xiao Yang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - Financial markets pose fundamental challenges for asset return prediction due to their high dimensionality, non-stationarity, and persistent volatility. Despite advances in large language models and multi-agent systems, current quantitative research pipelines suffer from limited…

- **[Group-in-Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2505.10978)**
  - *Lang Feng, Zhenghai Xue, Ting-Cong Liu et al.*
  - **NeurIPS 2025** · `2025-05-16`
  - Recent advances in group-based reinforcement learning (RL) have driven frontier large language models (LLMs) in single-turn tasks like mathematical reasoning. However, their scalability to multi-turn LLM agent training remains limited. Unlike static tasks, agent-environment inter…

- **[AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2504.00587)**
  - *Yingxuan Yang, Hua-Can Chai, Shuai Shao et al.*
  - **NeurIPS 2025** · `2025-04-01`
  - The rapid advancement of large language models (LLMs) has enabled the development of multi-agent systems where multiple LLM-based agents collaborate on complex tasks. However, existing systems often rely on centralized coordination, leading to scalability bottlenecks, reduced ada…

- **[Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657)**
  - *M. Cemri, Melissa Z. Pan, Shuyi Yang et al.*
  - **NeurIPS 2025** · `2025-03-17`
  - Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal. This gap highlights a critical need for a principled understanding of why MAS fail. Addressing this question requires systematic identification and analysis of f…

- **[Repo2Run: Automated Building Executable Environment for Code Repository at Scale](https://arxiv.org/abs/2502.13681)**
  - *Rui-Da Hu, Chao Peng, Xinchen Wang et al.*
  - **NeurIPS 2025** · `2025-02-19`
  - Scaling up executable code data is significant for improving language models'software engineering capability. The intricate nature of the process makes it labor-intensive, time-consuming and expert-knowledge-dependent to build a large number of executable code repositories, limit…


### ICML

- **[TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration](https://openreview.net/forum?id=bz651zjpyk)**
  - **ICML 2025** · OpenReview · `2026-10-13`
  - LLM-based agents can automate model post-training, accelerating progress toward recursive self-improvement. Despite their promise, existing approaches remain under-explored and face two main challenges: (1) strategy lock-in that limits exploration beyond the initial strategy; and…

- **[Harness Self-Evolution: Theory, Algorithms, Evaluation, Applications, and Impact](https://openreview.net/forum?id=m5jsFGXUM2)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - **ICML 2025** · OpenReview · `2026-10-11`
  - Building agents that learn from experience is a central goal of artificial intelligence. Harness self-evolution offers a path toward this goal by revising an agent’s instructions, memory, workflows, and tools while model weights stay fixed. In this article, we develop a unified f…

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

- **[FairCoder: Probing LLM Bias in High-Stakes Decision Making via Coding Tasks](https://openreview.net/forum?id=n7Mk11IVX8)**
  - *Yongkang Du, Jen-tse Huang, Jieyu Zhao et al.*
  - **ICML 2025** · OpenReview · `2026-06-03`
  - Large language models (LLMs) are increasingly used in high-stakes decisions such as hiring and college admissions, making their social bias a critical concern. While LLMs are trained to refuse explicitly biased requests, bias can be leaked implicitly during LLM planning and reaso…

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

- **[Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://arxiv.org/abs/2505.19433)**
  - *Peijie Dong, Zhen-Heng Tang, Xiang-Hong Liu et al.*
  - **ICML 2025** · `2025-05-26`
  - Post-training compression reduces the computational and memory costs of large language models (LLMs), enabling resource-efficient deployment. However, existing compression benchmarks only focus on language modeling (e.g., perplexity) and natural language understanding tasks (e.g.…

- **[Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](https://arxiv.org/abs/2505.00212)**
  - *Shao-Kun Zhang, Ming Yin, Jie-Yu Zhang et al.*
  - **ICML 2025** · `2025-04-30`
  - Failure attribution in LLM multi-agent systems-identifying the agent and step responsible for task failures-provides crucial clues for systems debugging but remains underexplored and labor-intensive. In this paper, we propose and formulate a new research area: automated failure a…

- **[MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://arxiv.org/abs/2503.03686)**
  - *Rui Ye, Shuo Tang, Rui Ge et al.*
  - **ICML 2025** · `2025-03-05`
  - LLM-based multi-agent systems (MAS) have shown significant potential in tackling diverse tasks. However, to design effective MAS, existing approaches heavily rely on manual configurations or multiple calls of advanced LLMs, resulting in inadaptability and high inference costs. In…

- **[MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673)**
  - *Adibvafa Fallahpour, Jun Ma, Alif Munim et al.*
  - **ICML 2025** · `2025-02-04`
  - Chest X-rays (CXRs) play an integral role in driving critical decisions in disease management and patient care. While recent innovations have led to specialized models for various CXR interpretation tasks, these solutions often operate in isolation, limiting their practical utili…

- **[OrcaLoca: An LLM Agent Framework for Software Issue Localization](https://arxiv.org/abs/2502.00350)**
  - *Zhongming Yu, He-Jia Zhang, Yu-Jie Zhao et al.*
  - **ICML 2025** · `2025-02-01`
  - Recent developments in Large Language Model (LLM) agents are revolutionizing Autonomous Software Engineering (ASE), enabling automated coding, problem fixes, and feature improvements. However, localization -- precisely identifying software problems by navigating to relevant code…

- **[RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](https://arxiv.org/abs/2501.18160)**
  - *Jinyao Guo, Cheng-Peng Wang, Xiang-Zhe Xu et al.*
  - **ICML 2025** · `2025-01-30`
  - Code auditing is the process of reviewing code with the aim of identifying bugs. Large Language Models (LLMs) have demonstrated promising capabilities for this task without requiring compilation, while also supporting user-friendly customization. However, auditing a code reposito…


### KDD

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, A. Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…

- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)**
  - *Mahmoud Mohammadi, Yi-Peng Li, Jean-Pierre Lo et al.*
  - **KDD 2025** · `2025-07-29`
  - The rise of LLM-based agents has opened new frontiers in AI applications, yet evaluating these agents remains a complex and underdeveloped area. This survey provides an in-depth overview of the emerging field of LLM agent evaluation, introducing a two-dimensional taxonomy that or…

- **[A Survey on Trustworthy LLM Agents: Threats and Countermeasures](https://arxiv.org/abs/2503.09648)**
  - *Miao Yu, Fanci Meng, Xinyun Zhou et al.*
  - **KDD 2025** · `2025-03-12`
  - With the rapid evolution of Large Language Models (LLMs), LLM-based agents and Multi-agent Systems (MAS) have significantly expanded the capabilities of LLM ecosystems. This evolution stems from empowering LLMs with additional modules such as memory, tools, environment, and even…


### ACL

- **[Agentic-MatriBO: Capability-Compiled Agentic Bayesian Optimization for Materials and Chemical Design](https://arxiv.org/abs/2610.17832v1)**
  - *Yu Zeng, Yuchuan Chen, Ziyue Zhang et al.*
  - **ACL** · `2026-10-13`
  - Materials and chemical optimization must choose the next synthesis, characterization, or high-fidelity simulation from sequential observations under a limited budget. Large language models can use task knowledge to propose adjustments, but composing surrogates, acquisition functi…

- **[Learning from fracture: Teaching language models to design through physical experience](https://arxiv.org/abs/2610.17804v1)**
  - *Bo Ni*
  - **ACL** · `2026-10-13`
  - How can language models learn to optimize physical designs through experience? We introduce FracLearn, an experience-abstraction-generalization framework evaluated through a deliberately unfamiliar, Tetris-inspired fracture game. The model first proposes architectures and examine…

- **[Keep Your Receipts: Trustworthy Cleanup of Agent-Built Knowledge Graphs](https://arxiv.org/abs/2610.17719v1)**
  - *Vishisht Choudhary*
  - **ACL** · `2026-10-13`
  - Agents build knowledge graphs as memory, and building them has become easy. Maintaining them has not. When a source is retracted, overruled, or erased, everything built on top of it (entity merges, entailed edges, community summaries) must be re-examined, and the maintainer must…

- **[Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents](https://arxiv.org/abs/2610.18457v1)**
  - *Kristoffer Hempel, Nils Loose, Lorenzo Cavallaro et al.*
  - **ACL** · `2026-10-13`
  - Large language model (LLM) agents are becoming an integral part of the software development lifecycle, and the capabilities granted to them allow an agent to act with the user's authority on any resource it can access. The reach that gives an agent its utility is equally availabl…

- **[AutoNovo: Agentic Program Search Discovers Transferable Nucleic Acid Design Algorithms](https://arxiv.org/abs/2610.16232v1)**
  - *Joel Shor, Subhashini Venugopalan*
  - **ACL** · `2026-10-12`
  - In-silico optimization of nucleic acids relies on predictive oracles that imperfectly capture biological function, so sequences optimized against one model may exploit model-specific artifacts and fail to generalize to independent models. Recent studies have shown that not all de…

- **[When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark](https://arxiv.org/abs/2610.16067v1)**
  - *Junjie Chen*
  - **ACL** · `2026-10-12`
  - Agent evaluation harnesses are software systems that run test suites, generate inputs, and decide outcomes with test oracles. This paper audits such software for reliability defects that score tables cannot reveal.   We introduce an oracle-integrity auditing approach with five st…

- **[Mixture of GFlowNets](https://arxiv.org/abs/2610.17007v1)**
  - *Omar G. Younis, Joseph D. Viviano, Chirayu Anant Haryan et al.*
  - **ACL** · `2026-10-12`
  - Generative Flow Networks (GFlowNets) learn a policy that samples compositional objects in proportion to an unnormalized reward $R(x)$. This makes them useful wherever many diverse, high-reward candidates are needed and oracle queries are expensive. In practice, a single GFlowNet…

- **[SkillFusion: Towards Reliable Multi-Skill Composition for LLM Agents](https://arxiv.org/abs/2610.15481v1)**
  - *Enhao Huang, Xinye Zhao, Yiming Li et al.*
  - **ACL** · `2026-10-11`
  - Independently authored skills can impose incompatible requirements, competing preferences, and redundant instructions when jointly loaded by an LLM agent. We propose SkillFusion, an offline compiler that reconciles these interactions into a reusable merged skill. Its central idea…

- **[From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)**
  - *Jing Luo, Yuchen Tian, Chuxue Cao et al.*
  - **ACL 2026** · `2026-05-07`
  - Large Language Model (LLM)-based agents have fundamentally reshaped artificial intelligence by integrating external tools and planning capabilities. While memory mechanisms have emerged as the architectural cornerstone of these systems, current research remains fragmented, oscill…

- **[EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis](https://arxiv.org/abs/2601.05808)**
  - *Xiaoshuai Song, Hao Chang, Guan-Ting Dong et al.*
  - **ACL 2026** · `2026-01-09`
  - Large language models (LLMs) are expected to be trained to act as agents in various real-world environments, but this process relies on rich and varied tool-interaction sandboxes. However, access to real systems is often restricted; LLM-simulated environments are prone to halluci…

- **[ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering](https://arxiv.org/abs/2510.20036)**
  - *Marianne Menglin Liu, Daniel García, Fjona Parllaku et al.*
  - **ACL 2025** · `2025-10-22`
  - Large language model (LLM) agents rely on external tools to solve complex tasks, but real-world toolsets often contain redundant tools with overlapping names and descriptions, introducing ambiguity and reducing selection accuracy. LLMs also face strict input context limits, preve…

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://arxiv.org/abs/2507.21028)**
  - *Jiaju Chen, Yuxuan Lu, Xiaojie Wang et al.*
  - **ACL 2025** · `2025-07-28`
  - Nearly all human work is collaborative; thus, the evaluation of real-world NLP applications often requires multiple dimensions that align with diverse human perspectives. As real human evaluator resources are often scarce and costly, the emerging"LLM-as-a-judge"paradigm sheds lig…

- **[MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](https://arxiv.org/abs/2506.21605)**
  - *Hao-Ran Tan, Ze-Yu Zhang, Chen Ma et al.*
  - **ACL 2025** · `2025-06-20`
  - Recent works have highlighted the significance of memory mechanisms in LLM-based agents, which enable them to store observed information and adapt to dynamic environments. However, evaluating their memory capabilities still remains challenges. Previous evaluations are commonly li…

- **[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://arxiv.org/abs/2504.08725)**
  - *Dayu Yang, Antoine Simoulin, Xin Qian et al.*
  - **ACL 2025** · `2025-04-11`
  - High-quality code documentation is crucial for software development especially in the era of AI. However, generating it automatically using Large Language Models (LLMs) remains challenging, as existing approaches often produce incomplete, unhelpful, or factually incorrect outputs…

- **[METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](https://arxiv.org/abs/2502.17651)**
  - *Bing-Xuan Li, Yiwei Wang, Jiu-Xiang Gu et al.*
  - **ACL 2025** · `2025-02-24`
  - Chart generation aims to generate code to produce charts satisfying the desired visual properties, e.g., texts, layout, color, and type. It has great potential to empower the automatic professional report generation in financial analysis, research presentation, education, and hea…

- **[STeCa: Step-level Trajectory Calibration for LLM Agent Learning](https://arxiv.org/abs/2502.14276)**
  - *Han-Lin Wang, Jian Wang, Chak Tou Leong et al.*
  - **ACL 2025** · `2025-02-20`
  - Large language model (LLM)-based agents have shown promise in tackling complex tasks by interacting dynamically with the environment. Existing work primarily focuses on behavior cloning from expert demonstrations or preference learning through exploratory trajectory sampling. How…

- **[iAgent: LLM Agent as a Shield between User and Recommender Systems](https://arxiv.org/abs/2502.14662)**
  - *Wujiang Xu, Yunxiao Shi, Zujie Liang et al.*
  - **ACL 2025** · `2025-02-20`
  - Traditional recommender systems usually take the user-platform paradigm, where users are directly exposed under the control of the platform's recommendation algorithms. However, the defect of recommendation algorithms may put users in very vulnerable positions under this paradigm…

- **[Red-Teaming LLM Multi-Agent Systems via Communication Attacks](https://arxiv.org/abs/2502.14847)**
  - *Peng-Fei He, Yu-Ping Lin, Shen Dong et al.*
  - **ACL 2025** · `2025-02-20`
  - Large Language Model-based Multi-Agent Systems (LLM-MAS) have revolutionized complex problem-solving capability by enabling sophisticated agent collaboration through message-based communications. While the communication framework is crucial for agent coordination, it also introdu…

- **[Unveiling Privacy Risks in LLM Agent Memory](https://arxiv.org/abs/2502.13172)**
  - *Bo Wang, Weiyi He, Peng-Fei He et al.*
  - **ACL 2025** · `2025-02-17`
  - Large Language Model (LLM) agents have become increasingly prevalent across various real-world applications. They enhance decision-making by storing private user-agent interactions in the memory module for demonstrations, introducing new privacy risks for LLM agents. In this work…

- **[FLAG-Trader: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading](https://arxiv.org/abs/2502.11433)**
  - *Guo-Jun Xiong, Zhiyang Deng, Keyi Wang et al.*
  - **ACL 2025** · `2025-02-17`
  - Large language models (LLMs) fine-tuned on multimodal financial data have demonstrated impressive reasoning capabilities in various financial tasks. However, they often struggle with multi-step, goal-oriented scenarios in interactive financial markets, such as trading, where comp…

- **[LLM Agents Making Agent Tools](https://arxiv.org/abs/2502.11705)**
  - *G. Wölflein, Dyke Ferber, D. Truhn et al.*
  - **ACL 2025** · `2025-02-17`
  - Tool use has turned large language models (LLMs) into powerful agents that can perform complex multi-step tasks by dynamically utilising external software components. However, these tools must be implemented in advance by human developers, hindering the applicability of LLM agent…

- **[G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems](https://arxiv.org/abs/2502.11127)**
  - *Shilong Wang, Gui-Min Zhang, Miao Yu et al.*
  - **ACL 2025** · `2025-02-16`
  - Large Language Model (LLM)-based Multi-agent Systems (MAS) have demonstrated remarkable capabilities in various complex tasks, ranging from collaborative problem-solving to autonomous decision-making. However, as these systems become increasingly integrated into critical applicat…

- **[A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://arxiv.org/abs/2502.11211)**
  - *Wen-Xuan Wang, Zi-Zhan Ma, Zheng Wang et al.*
  - **ACL 2025** · `2025-02-16`
  - Large Language Models (LLMs) are transforming healthcare through the development of LLM-based agents that can understand, reason about, and assist with medical tasks. This survey provides a comprehensive review of LLM-based agents in medicine, examining their architectures, appli…

- **[PlanGenLLMs: A Modern Survey of LLM Planning Capabilities](https://arxiv.org/abs/2502.11221)**
  - *Hui Wei, Zihao Zhang, Shenghua He et al.*
  - **ACL 2025** · `2025-02-16`
  - LLMs have immense potential for generating plans, transforming an initial world state into a desired goal state. A large body of research has explored the use of LLMs for various planning tasks, from web navigation to travel planning and database querying. However, many of these…

- **[nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow](https://arxiv.org/abs/2502.05036)**
  - *Geliang Ouyang, Jingya Chen, Zhihe Nie et al.*
  - **ACL 2025** · `2025-02-07`
  - Natural Language to Visualization (NL2Vis) seeks to convert natural-language descriptions into visual representations of given tables, empowering users to derive insights from large-scale data. Recent advancements in Large Language Models (LLMs) show promise in automating code ge…

- **[PaSa: An LLM Agent for Comprehensive Academic Paper Search](https://arxiv.org/abs/2501.10120)**
  - *Yichen He, Guanhua Huang, Pei-Yuan Feng et al.*
  - **ACL 2025** · `2025-01-17`
  - We introduce PaSa, an advanced Paper Search agent powered by large language models. PaSa can autonomously make a series of decisions, including invoking search tools, reading papers, and selecting relevant references, to ultimately obtain comprehensive and accurate results for co…

- **[Uncertainty Propagation on LLM Agent](https://aclanthology.org/2025.acl-long.302.pdf)**
  - *Qi-Wei Zhao, Dong Li, Yan-Chi Liu et al.*
  - **ACL 2025**

- **[Qwen2.5-xCoder: Multi-Agent Collaboration for Multilingual Code Instruction Tuning](https://www.semanticscholar.org/paper/58f6ac8c023e18e7c8886770ec583e0fdd616e86)**
  - *Jian Yang, Wei Zhang, Yibo Miao et al.*
  - **ACL 2025**
  - ,


### EMNLP

- **[Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents](https://arxiv.org/abs/2509.17488)**
  - *Shou-Ju Wang, Fenglin Yu, Xirui Liu et al.*
  - **EMNLP 2025** · `2025-09-22`
  - The increasing autonomy of LLM agents in handling sensitive communications, accelerated by Model Context Protocol (MCP) and Agent-to-Agent (A2A) frameworks, creates urgent privacy challenges. While recent work reveals significant gaps between LLMs'privacy Q&A performance and thei…

- **[Code Like Humans: A Multi-Agent Solution for Medical Coding](https://arxiv.org/abs/2509.05378)**
  - *A. Motzfeldt, Joakim Edin, Casper L. Christensen et al.*
  - **EMNLP 2025** · `2025-09-04`
  - In medical coding, experts map unstructured clinical notes to alphanumeric codes for diagnoses and procedures. We introduce Code Like Humans: a new agentic framework for medical coding with large language models. It implements official coding guidelines for human experts, and it…

- **[Coarse-to-Fine Grounded Memory for LLM Agent Planning](https://arxiv.org/abs/2508.15305)**
  - *Wei Yang, Jin-Wei Xiao, Hongming Zhang et al.*
  - **EMNLP 2025** · `2025-08-21`
  - Recent advancements in Large Language Models (LLMs) have driven growing interest in LLM-based agents for complex planning tasks. To avoid costly agent training, many studies adopted memory mechanism that enhances LLM with offline experiences or online trajectory analysis. However…

- **[ECom-Bench: Can LLM Agent Resolve Real-World E-commerce Customer Support Issues?](https://arxiv.org/abs/2507.05639)**
  - *Haoxin Wang, Xianhan Peng, Huang Cheng et al.*
  - **EMNLP 2025** · `2025-07-08`
  - In this paper, we introduce ECom-Bench, the first benchmark framework for evaluating LLM agent with multimodal capabilities in the e-commerce customer support domain. ECom-Bench features dynamic user simulation based on persona information collected from real e-commerce customer…

- **[LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://arxiv.org/abs/2506.17335)**
  - *Shuo Yan, Ruochen Li, Ziming Luo et al.*
  - **EMNLP 2025** · `2025-06-19`
  - Large language model (LLM) agents have demonstrated remarkable potential in advancing scientific discovery. However, their capability in the fundamental yet crucial task of reproducing code from research papers, especially in the NLP domain, remains underexplored. This task inclu…

- **[DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation](https://arxiv.org/abs/2503.07044)**
  - *Ziming You, Yumiao Zhang, De-Xuan Xu et al.*
  - **EMNLP 2025** · `2025-03-10`
  - Existing large language model (LLM) agents for automating data science show promise, but they remain constrained by narrow task scopes, limited generalization across tasks and models, and over-reliance on state-of-the-art (SOTA) LLMs. We introduce DatawiseAgent, a notebook-centri…

- **[CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://arxiv.org/abs/2502.12532)**
  - *Yong Zhao, Kai Xu, Zheng-Qiu Zhu et al.*
  - **EMNLP 2025** · `2025-02-18`
  - Embodied Question Answering (EQA) has primarily focused on indoor environments, leaving the complexities of urban settings-spanning environment, action, and perception-largely unexplored. To bridge this gap, we introduce CityEQA, a new task where an embodied agent answers open-vo…

- **[Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)**
  - *Samuel Schmidgall, Yu-Sheng Su, Ze Wang et al.*
  - **EMNLP 2025** · `2025-01-08`
  - Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory, an…

- **[AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories](https://aclanthology.org/2025.emnlp-demos.15.pdf)**
  - *Tian-Yue Ou, Wan-Yao Guo, Apurva Gandhi et al.*
  - **EMNLP 2025**
  - ,

- **[ACEBench: A Comprehensive Evaluation of LLM Tool Usage](https://aclanthology.org/2025.findings-emnlp.697.pdf)**
  - *Chen Chen, Xin-Long Hao, Weiwen Liu et al.*
  - **EMNLP 2025**
  - Large Language Models (LLMs) have demonstrated significant potential in decision-making and reasoning, particularly when integrated with various tools to effectively solve complex problems. However, existing benchmarks for evaluating LLMs’ tool usage face several limitations: (1)…


### NAACL

- **[Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061)**
  - *Qiusi Zhan, Richard Fang, H. Panchal et al.*
  - **NAACL 2025** · `2025-02-27`
  - Large Language Model (LLM) agents exhibit remarkable performance across diverse applications by using external tools to interact with environments. However, integrating external tools introduces security risks, such as indirect prompt injection (IPI) attacks. Despite defenses des…

- **[CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging](https://arxiv.org/abs/2502.05664)**
  - *Md. Ashraful Islam, Mohammed Eunus Ali, Md. Rizwan Parvez*
  - **NAACL 2025** · `2025-02-08`
  - Large Language Models (LLMs) have made significant strides in code generation and problem solving. Current approaches employ external tool-based iterative debuggers that use compiler or other tool-based runtime feedback to refine coarse programs generated by various methods. Howe…


### Other / arXiv

- **[Agent-Reflex: Teaching Language Agents to Act Reflectively](https://arxiv.org/abs/2610.17953)**
  - *Guanting Dong, Xinyu Yang, Jiajie Jin et al.*
  - 🤗 Featured · `2026-10-13`
  - Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision…

- **[Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes](https://arxiv.org/abs/2610.18356)**
  - *Yu Wang, Rui Dai, Wei Chen et al.*
  - 🤗 Featured · `2026-10-13`
  - City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbex, an agentic vision-language framework that instead casts grounding as active spatial search. Urbex…

- **[WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution](https://arxiv.org/abs/2610.18067)**
  - *Hang He, Linting Wang, Guanming Liu et al.*
  - 🤗 Featured · `2026-10-13`
  - Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and…

- **[Learning How to Remember: Memory Modality Selection for GUI Agents](https://arxiv.org/abs/2610.17928)**
  - *Taeyun Roh, Suhyeong Park, Gijin Kim et al.*
  - 🤗 Featured · `2026-10-13`
  - Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for reusing knowledge from past interactions. However, existing memory augmented GUI agents typically adopt a…

- **[DeltaTTG: Training Multi-Turn Agents with a Token-to-Go Progress Meter](https://arxiv.org/abs/2610.17666)**
  - *Xuyan Ye, Xiyan Fu, Shengda Fan et al.*
  - 🤗 Featured · `2026-10-13`
  - Reinforcement learning with verifiable rewards (RLVR) for multi-turn agents relies on sparse terminal rewards that say little about individual steps. Within-group step comparisons depend on reliable state matching and sufficiently diverse sampled outcomes, while direct step scori…

- **[ReTerm: Recovery Training for Self-Improving Terminal Agents](https://arxiv.org/abs/2610.18484)**
  - *Wei Xie, Kaituo Feng, Shiming Fu et al.*
  - 🤗 Featured · `2026-10-13`
  - Terminal agents have shown strong abilities in complex coding tasks. However, they often struggle to recover from errors during long-running execution (e.g., command errors, faulty implementations), eventually leading to task failures. To this end, we present ReTerm, a self-impro…

- **[Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://arxiv.org/abs/2610.18868)**
  - *Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh et al.*
  - 🤗 Featured · `2026-10-13`
  - Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horiz…

- **[JevGPT: Thinking Fast and Slow in Autonomous Research](https://arxiv.org/abs/2610.18272)**
  - *Yasheng Sun, Yanning Dai, Yimeng Chen et al.*
  - 🤗 Featured · `2026-10-13`
  - Autonomous research agents must acquire and reason over evidence within a limited budget. Yet relevant sources can remain uninspected or unused, leaving a gap between retrieval coverage and the evidence that informs research. The challenge is to align fast local judgments with ch…

- **[LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity](https://arxiv.org/abs/2610.18092)**
  - *Yibo Wang, Senjie Jin, Yansong Ning et al.*
  - 🤗 Featured · `2026-10-13`
  - Deep research (DR) agents address open-ended information needs through multi-step reasoning, long-horizon web search, and evidence synthesis. However, existing benchmarks primarily focus on academic research or synthetic tasks, leaving DR agents' capabilities in real-world life a…

- **[SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software Coding Agents](https://arxiv.org/abs/2610.18206)**
  - *Do Xuan Trong, Duc Anh Nguyen, Do Xuan Long et al.*
  - 🤗 Featured · `2026-10-13`
  - We present SWE-MISBEHAVIOR, the first taxonomy and evaluation framework for diagnosing boundary-violating misbehaviors in coding agents. It contains 7.4K human-in-the-loop synthesized samples spanning three layers of agent action space: (i) Code Generation, (ii) File Management,…

- **[X-Ragent: Tool-Augmented Reinforcement Learning for Evidence-Grounded Chest X-Ray Reasoning](https://arxiv.org/abs/2610.16811)**
  - *Yi Wang, Zhenlong Yuan, Yuchan Guo et al.*
  - 🤗 Featured · `2026-10-12`

- **[CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction](https://arxiv.org/abs/2610.16577)**
  - *Jialei Wang, Zehan Wang, XiaoYang Wu et al.*
  - 🤗 Featured · `2026-10-12`

- **[A Decade in a Day: Synthesizing Agent-Native Interfaces from Human-Oriented Software Evolution](https://arxiv.org/abs/2610.15765)**
  - *Alan Wu, Wei Tao, Yiwen Guo*
  - 🤗 Featured · `2026-10-11`
  - Large language model agents are emerging as an important new class of users of desktop applications. However, existing desktop interfaces were designed for human end users or application developers, leaving agents to interpret visual controls or discover and compose low-level sof…

- **[VIEWCRAFT: Evolving What Multimodal Agents See and How They Read It](https://arxiv.org/abs/2610.15915)**
  - *Binxiao Xu, Ruichuan An, Bocheng Zou et al.*
  - 🤗 Featured · `2026-10-11`

- **[EviScene: Beyond "Is It AI?" for Agentic Image Factuality Assessment](https://arxiv.org/abs/2610.14609)**
  - *ZiAn Wang, Ruiqi Liu, Zhengbo Zhang et al.*
  - 🤗 Featured · `2026-10-10`

- **[Harness^2: Recursive Agent Harnessing for an Open World](https://arxiv.org/abs/2610.14224)**
  - *Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al.*
  - 🤗 Featured · `2026-10-09`

- **[ClawLoop: Self-Improving Agents via Harness-Native Training Loop](https://arxiv.org/abs/2610.14118)**
  - *Hansi Yang, Linji Hao, Hongyan Hao et al.*
  - 🤗 Featured · `2026-10-09`

- **[Latent World Action Model for GUI Agents](https://arxiv.org/abs/2610.14228)**
  - *Seungjun Yu, Hojun Choi, Seojeong Park et al.*
  - 🤗 Featured · `2026-10-09`

- **[AutoEnvScaling: Automating the Data Flywheel with Terminal Agents](https://arxiv.org/abs/2610.14163)**
  - *Simon Yu, Baolin Peng, Bo Liu et al.*
  - 🤗 Featured · `2026-10-09`

- **[DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning](https://arxiv.org/abs/2610.18862)**
  - *Minghao Luo, Liang Chen*
  - 🤗 · `2026-10-13`
  - Reasoning models achieve strong performance through long chains of thought (CoT), but often spend more tokens than needed to solve a problem. Existing ways to shorten the CoT require additional training for each model, add a fixed steering vector to the model's hidden states, or…

- **[Hybrid Reasoning Agents](https://arxiv.org/abs/2610.18861)**
  - *Jiaru Zou, Yunzhe Qi, Sirui Chen et al.*
  - 🤗 · `2026-10-13`
  - How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning tran…

- **[Self-Evolving Agent Harness](https://arxiv.org/abs/2610.18813)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - 🤗 · `2026-10-13`
  - Harness self-evolution revises an agent's software scaffolding, including prompts, memory, workflows, and executable components, while keeping model weights fixed. We formalize a feedback-driven process in which accepted revisions persist across runs. The framework separates upda…

- **[Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with Tool-Augmented Judges](https://arxiv.org/abs/2610.18766)**
  - *Tianci Liu, Haoyu Wang*
  - 🤗 · `2026-10-13`

- **[Beyond the Verdict: Agentic Code Judging with Verifiable Feedback](https://arxiv.org/abs/2610.18760)**
  - *Zheye Deng, Sha Li, Changlong Yu et al.*
  - 🤗 · `2026-10-13`
  - Test-time scaling for large language models (LLMs) can involve generating multiple candidate solutions for selection or revising an earlier attempt. To guide selection and revision, we need a verifier that can estimate candidate correctness and provide evidence of failure. In com…

- **[Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents](https://arxiv.org/abs/2610.18614)**
  - *Ashutosh Hathidara*
  - 🤗 · `2026-10-13`
  - Controlling an acting LLM agent means deciding, at each step of a long-horizon task, whether to trust its next action, abstain, or hand off to a human. That decision needs a per-step confidence signal predicting whether the current rollout will eventually succeed. The agent's own…

- **[Agaram 2.5B: The First Tamil-First Language Model Trained from Scratch with Tool Calling. A Playbook for Under-Represented Languages](https://arxiv.org/abs/2610.18420)**
  - *Ramchand Kumaresan, Madhusudhanan G, Kaushik Kezendirane*
  - 🤗 · `2026-10-13`

- **[Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2610.18352)**
  - *Youpeng Wen, Gang Wang, Tianyu Huang et al.*
  - 🤗 · `2026-10-13`
  - A robot following a multi-step instruction needs to act on the right objects in the right order, even as the scene changes. It must also maintain awareness of task progress and determine when to advance. To address these challenges, we introduce Orchestra, an agent harness that s…

- **[LADDER: A Long-Horizon Robot Manipulation Benchmark](https://arxiv.org/abs/2610.18053)**
  - *Petko Petkov, Giuliano Albanese, Nikolay Nikolov et al.*
  - 🤗 · `2026-10-13`
  - General-purpose robot manipulation policies learn short-horizon skills effectively, but degrade rapidly on long-horizon tasks. Existing benchmarks cannot isolate failures because task horizon is either too short or entangled with scene and object variations. We propose LADDER, a…

- **[Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills](https://arxiv.org/abs/2610.17860)**
  - *Letian Zhu, Han Li, Yifan Yao et al.*
  - 🤗 · `2026-10-13`
  - Agent Skills improve LLM agents by making task knowledge reusable across sessions. Learning transferable Skills requires evidence about a procedure and its conditions of use, which a successful task attempt can leave untested. We introduce Socratic Skill Learning (SSL), which int…

- **[GIFT-Eval-CTX: A Benchmark For Contextual Forecasting Model Evaluation](https://arxiv.org/abs/2610.17794)**
  - *Xu Liu, Hanshu Yan, Taha Aksu et al.*
  - 🤗 · `2026-10-13`
  - Contextual forecasting seeks to improve time series forecasting by incorporating forward-looking information, such as planned events, external conditions, and expert expectations. However, reliable evaluation remains difficult: existing benchmarks often have limited domain covera…

- **[When Should Enterprise Policy Decisions Be Learned, and When Should They Be Reasoned?](https://arxiv.org/abs/2610.17643)**
  - *Hyojung Han, Ryangkyung Kang, Youngeun Kim et al.*
  - 🤗 · `2026-10-13`
  - An enterprise agent that answers under a written policy must choose an action before it says anything: answer, ask for a missing fact, ask for confirmation, call one or several tools, escalate, or refuse. Holding one 27B Korean enterprise model fixed, we vary whether the decision…

- **[ChunkAct: Action Chunking for Agentic Robotics](https://arxiv.org/abs/2610.18874v1)**
  - *Bingxin Xu, Wenrui Bao, Xinxin Liu et al.*
  - `2026-10-13`
  - Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a st…

- **[RoboSimStudio: An Interactive Toolkit for Rapid Real2Sim of Robot Manipulation Tasks](https://arxiv.org/abs/2610.18835v1)**
  - *Kaiyuan Chen, Shuangyu Xie, Uksang Yoo et al.*
  - `2026-10-13`
  - It is difficult to accurately model the physics of the interaction between a robot and the objects it manipulates, including contact mechanics, coupled contact dynamics, deformations, stiffness and friction. We present RoboSimStudio (RSS), an interactive toolkit that makes choice…

- **[Optimizing Team Behavior via Extremum-seeking Control in Multi-agent Reinforcement Learning](https://arxiv.org/abs/2610.18808v1)**
  - *Svar Rajankumar Patel, Kshitij Jerath*
  - `2026-10-13`
  - In cooperative Multi-Agent Reinforcement Learning (MARL), agents must learn to coordinate their actions to achieve shared objectives. A key indicator of effective coordination is behavioral diversity, i.e., the agents' potential to enact distinct yet complementary control policie…

- **[SEAR: Self-Evolving Agentic Robotics](https://arxiv.org/abs/2610.18792v1)**
  - *Xinyi Wang, Bangzheng Li, Hanyu Wang et al.*
  - `2026-10-13`
  - Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the age…

- **[Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents](https://arxiv.org/abs/2610.18784v1)**
  - *Yuchen Lu, Julian McAuley, Lei Zhang*
  - `2026-10-13`
  - Long-horizon agents accumulate progress in persistent task state, yet repeatedly process interaction histories describing how that progress was achieved. This raises a natural question: can long-horizon context instead be organized around reusable progress rather than the history…

- **[BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems](https://arxiv.org/abs/2610.18780v1)**
  - *Xiaoguang Guo, Yaohao Long, Chuxu Zhang*
  - `2026-10-13`
  - Large language model multi-agent systems extend individual agents' capabilities through collaboration across specialized roles, tools, and workflows. Yet collaboration makes failures harder to diagnose: one agent may misinterpret a correct result while others carry the mistake fo…

- **[Knowing the User Is Not Knowing What We Established: Grounding Awareness in Personal Agents](https://arxiv.org/abs/2610.18684v1)**
  - *Jiajun Chen, Xinyue Chen, Yicheng Jiang et al.*
  - `2026-10-13`
  - Personal-agent memory has largely focused on learning what users know, prefer, and want. However, knowing the user does not necessarily mean knowing what the user and the agent have established together. An assistant's proposal should not become an authorized instruction merely b…

- **[ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2610.18683v1)**
  - *Bowen Ding, Mingda Wan, Yuhan Chen et al.*
  - `2026-10-13`
  - Reinforcement learning (RL) has emerged as the primary paradigm for optimizing Large Language Model (LLM) agents, yet efficient critic-free algorithms (e.g., GRPO) suffer from a fundamental uniform credit assignment dilemma that broadcasts trajectory-level advantages equally to a…

- **[Falsification-proof non-market allocation mechanisms](https://arxiv.org/abs/2610.18625v1)**
  - *Eduardo Perez-Richet, Vasiliki Skreta*
  - `2026-10-13`
  - Relying on manipulable characteristics to target the allocation of resources is fraught with difficulties. Naively optimal rules lead to falsification and allocative inefficiency. Optimizing the rule for allocative efficiency while accounting for falsification typically induces f…

- **[Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference](https://arxiv.org/abs/2610.18617v1)**
  - *St John Grimbly, Nicolas Kuske, Evert A. Boonstra et al.*
  - `2026-10-13`
  - An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separ…

- **[Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve](https://arxiv.org/abs/2610.18616v1)**
  - *Yuyang Bai, Yu Wang, Yu Zhang*
  - `2026-10-13`
  - Searching text-rich knowledge graphs requires following relations while examining textual evidence. Predefined graph interfaces constrain what evidence agents can access, even when they write code to combine tool calls or process retrieved subgraphs. We propose direct knowledge g…

- **[AgentStripes: An Evidence-Graded Maturity Model for AI Agents](https://arxiv.org/abs/2610.18603v1)**
  - *Nutan Kumar Naik, Vijay Prasad Poudel, Aditya Kumar Saroj et al.*
  - `2026-10-13`
  - Benchmarks report what an Artificial Intelligence (AI) agent can do on a task suite, but not whether one released version has been engineered with the controls that make it reliable, safe and observable, or how strongly that is shown. This paper proposes AgentStripes, an evidence…

- **[Auditing Future-Memory Use in Point-in-Time Language Agents](https://arxiv.org/abs/2610.18602v1)**
  - *Rongtian Ye*
  - `2026-10-13`
  - Point-in-time (PIT) agents can recall post-cutoff facts even when their external evidence respects a historical cutoff. We examine whether this access predicts evidence gathering in 48 historical company-comparison tasks. Independent closed-book revenue probes identify the better…

- **[Reading Right, Acting Wrong: Diagnosing Decision Failures of System One Models in Agent Loops](https://arxiv.org/abs/2610.18579v1)**
  - *Yubo Li, Ramayya Krishnan, Rema Padman*
  - `2026-10-13`
  - System One models choose an agent's next action by scoring a supplied set of options in a single pass. This makes them fast and cheap, but when they choose wrongly there is nothing to inspect: did the model misread what the agent has seen, or read it correctly and still act wrong…

- **[LLM Agents for Automated Post-Training via Structured Recipe Optimization](https://arxiv.org/abs/2610.18572v1)**
  - *Ruohong Liu, Bohan Tang, Lekang Jiang et al.*
  - `2026-10-13`
  - Automated post-training transforms pre-trained large language models (LLMs) into models capable of handling diverse domains by automatically constructing and optimizing a recipe of coupled decisions over data sources, data processing, cross-domain composition, and training config…

- **[On Symmetry for Characterizing Agent Heterogeneity in Multi-Agent Systems](https://arxiv.org/abs/2610.18538v1)**
  - *Jianhong Wang, Jonathan Lawry*
  - `2026-10-13`
  - Understanding agent heterogeneity can inform the design of shared and agent-specific policy representations, however existing criteria provide no unified structural test. We study finite-horizon POSGs and define a type-compatible transformation as a policy-evaluation symmetry whe…

- **[Lost in Implicit Routing: How LLM Agents Fail to Load Relevant Skills at Scale](https://arxiv.org/abs/2610.18522v1)**
  - *Jinlin Liu, Wei Chen, Xiaojin Zhang*
  - `2026-10-13`
  - Reusable skills let LLM agents load task-specific instructions on demand, but they make execution depend on implicit routing over skill metadata. We test whether this design scales by holding SkillsBench tasks and their golden skills fixed while adding irrelevant skills. We find…

- **[A Global View of How LLMs Value Human Time](https://arxiv.org/abs/2610.18515v1)**
  - *Yifan He, Sofie Goethals, Manon Reusens et al.*
  - `2026-10-13`
  - Large language models (LLMs) increasingly act as personal assistants; however, little is known about how they capture national-level preferences on a global scale. Given that "time" is a universal and representative concept, we examine LLMs' time preferences by varying only users…

- **[Judges Follow the Reference: The Derivation Gap in Verifying Tool-Call Arguments](https://arxiv.org/abs/2610.18497v1)**
  - *Linhai Ma, Yan Wang, Lingfei Qian et al.*
  - `2026-10-13`
  - Tool-call judges evaluate argument values proposed by LLM agents. We find that they accept a correct value less often when their input holds no reference for it, that is, no text that says what the value should be. This happens when the value is a default value from the function…

- **[MemoryVLN: From Ego-Aware Memory Representation to Cross-Context Memory Reuse in Vision-Language Navigation](https://arxiv.org/abs/2610.18478v1)**
  - *Xueyao Wei, Yifei Wang, Delun Li et al.*
  - `2026-10-13`
  - Large vision-language models (LVLMs) have shown strong potential for embodied vision-language navigation (VLN), yet their performance degrades on long-horizon trajectories due to context-length limits, redundant historical observations, and unstable spatial alignment across time.…

- **[Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2610.18449v1)**
  - *Yibo Wen, Han Liu*
  - `2026-10-13`
  - AI agents for autonomous scientific discovery must decide which experiments to run under a limited budget. Most benchmarks for science agents provide fixed datasets, while others that support active experimentation largely rely on simulation. We introduce Autonomous Science Bench…

- **[Delegating Earth science model calibration to knowledge-guided LLM agents](https://arxiv.org/abs/2610.18378v1)**
  - *Zhanliang Zhu, Ziwei Li, Liujun Zhu et al.*
  - `2026-10-13`
  - Applying process-based Earth science models to new sites and questions often requires expert calibration decisions. Reliable delegation to language-model agents must preserve scientific competence and reproducibility. Here we develop a general calibration harness (GCH) for end-to…

- **[ABot-ER: Unified Embodied Reasoning through Agentic Data-Model Co-Evolution](https://arxiv.org/abs/2610.18355v1)**
  - *Qiuyu Ding, Heng-Da Xu, Changda Xia et al.*
  - `2026-10-13`
  - We introduce \textbf{ABot Embodied Reasoning (ABot-ER)}, a unified embodied reasoning foundation model that breaks the tension between breadth and depth in embodied reasoning. Embodied intelligence demands the joint mastery of perception, planning, and execution, yet reconciling…

- **[Choosing LLMs for Strategic Agent Interactions](https://arxiv.org/abs/2610.18354v1)**
  - *Arastun Mammadli, Herbert Woisetschläger, Jawad Fayaz et al.*
  - `2026-10-13`
  - Game-theoretic benchmarks claim that large language model (LLM) strategic decision-making varies across game types, interaction structures, and capability dimensions. However, they only evaluate strategic performance across individual fixed models. In parallel, contemporary LLM r…

- **[AssetForge: Asset-Augmented Task Synthesis for Business Automation Agents](https://arxiv.org/abs/2610.18330v1)**
  - *Xiangrui Liu, Shuo Tang, Siheng Chen*
  - `2026-10-13`
  - Training business automation agents requires executable tasks that connect a natural-language request to an application state and a verifiable end state. Traditional Rubrics requires Authors to recreate application interfaces, initial records, policy evidence, and outcome checks…

- **[Complex materials engineering via Provenance Action Graphs: potential, structure and demonstration](https://arxiv.org/abs/2610.18314v1)**
  - *Yevgeny Rakita, Paul Todd, James R. Neilson et al.*
  - `2026-10-13`
  - This work discusses and tests the potential of reaction graphs for material synthesis, in which events consist of reaction steps (actions) and their outputs (observations). The importance comes from the requirement to synthesize technologically useful materials, especially those…

- **[SimInter: Evidence-Grounded User Simulation with Interview-Based Profile Enrichment for Conversational Recommender Systems](https://arxiv.org/abs/2610.18308v1)**
  - *Erfan Shahabi, Amirhossein Roshandel, Mohammad Sadegh Sadeghi et al.*
  - `2026-10-13`
  - Conversational Recommender Systems (CRSs) require reliable user simulators for cost-effective evaluation. LLM-based simulators have made realistic simulation possible but typically condition on profiles derived from explicit ratings, demographics, and static sources capturing sur…

- **[AffectWorld: Benchmarking Emotion-Driven Future World Prediction](https://arxiv.org/abs/2610.18305v1)**
  - *Changhao Song, Yacong Chen, Hui Gao et al.*
  - `2026-10-13`
  - The world encompasses both physical environments and human actors. Predicting its evolution requires understanding both physical laws and how emotions shape human actions. However, existing world model benchmarks primarily assess physical plausibility and perceptual quality, leav…

- **[Output Discipline Sets the Floor: A Falsification-Guided, Model-Agnostic Agent Protocol for Auditable Hypothesis-Driven Decision Making](https://arxiv.org/abs/2610.18298v1)**
  - *Jing Liu, Yongxing Qi, Ping Yao et al.*
  - `2026-10-13`
  - What binds large language models on auditable, hypothesis-driven decision tasks, where every candidate can be checked against the evidence? On the public TCMEval-SDT benchmark for Traditional Chinese Medicine syndrome differentiation (200 cases), the binding constraint is output…

- **[Encrypted Skills Can Become New Security Exploits If AI Agents Know How to Decipher](https://arxiv.org/abs/2610.18262v1)**
  - *Yan-Lun Chen, Pin-Yu Chen, Chia-Mu Yu*
  - `2026-10-13`
  - Third-party skills can expose LLM agents to malicious instructions hidden by encoding. We introduce Ciphered Skill Injection (CSI), which embeds such instructions in skill files for agents to decode and follow. We evaluate Caesar and layered variants across eight models and 139 i…

- **[Beyond Answer Sharing: TrueMAD for Targeted Peer Engagement in Multi-Agent Debate](https://arxiv.org/abs/2610.18240v1)**
  - *Dezheng Bao, Sihang Du, Renhong Huang et al.*
  - `2026-10-13`
  - Multi-agent debate (MAD) aims to improve large language model reasoning by exposing agents to alternative solutions and enabling iterative revision. However, standard broadcast-style MAD makes peer answers visible without requiring agents to engage with a particular peer claim. A…

- **[Holding Agents Accountable with Verifiable Agent Insurance](https://arxiv.org/abs/2610.18230v1)**
  - *Cheng Hua, Taro Tsuchiya, Nicolas Christin et al.*
  - `2026-10-13`
  - While AI agents are useful for many tasks, they regularly misbehave in destructive ways, such as deleting important data. While prior work has focused on preventing such misbehavior, we consider how to recover after an agent misbehaves. We propose verifiable agent insurance (VAI)…

- **[TextualRL: Textual Reinforcement Learning for Context Management](https://arxiv.org/abs/2610.18216v1)**
  - *Tianyu Huai, Jie Zhou, Bo Mao et al.*
  - `2026-10-13`
  - LLM agents can adapt to task feedback by revising the textual context that guides their behavior, without changing their model parameters. However, turning execution rewards into reusable context updates is challenging: individual trajectories offer limited comparative evidence a…

- **[When and How Order-Flow Interventions Work After Dealers Adapt](https://arxiv.org/abs/2610.18158v1)**
  - *Guanghao Wu, Zhuo Cai, Zhidong Li et al.*
  - `2026-10-13`
  - Learning dealer agents can settle on persistently wide quotes, raising what customers pay to trade. A venue can route more orders to tighter quotes, but a wide quote may reflect real risk, and once dealers adapt, an end-to-end comparison cannot show why a rule works: because it i…

- **[Fan Out or Relay? Ownership-Aware Routing for LLM Agents Querying Siloed Tables](https://arxiv.org/abs/2610.18157v1)**
  - *Zhexi Feng*
  - `2026-10-13`
  - Inside organizations, a question's data often sit with several owners, who query their own tables but never hand them over. An LLM coordinator can fan out, sending the question to every owner at once, or relay, querying owners in turn and reusing earlier rows. We show that neithe…

- **[APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation](https://arxiv.org/abs/2610.18097v1)**
  - *Sirui Zhang, Fangyun Wei, Dong Chen et al.*
  - `2026-10-13`
  - Post-training is crucial for improving text-to-image models, yet existing pipelines typically rely on manually curated training data and fixed training distributions. We introduce APT (Agentic Post-Training), a fully automated framework that adaptively post-trains a base model ac…

- **[AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses](https://arxiv.org/abs/2610.18090v1)**
  - *Kaiyu Huang, Yiting Li, Angyang Gu et al.*
  - `2026-10-13`
  - Ambiguous or incomplete task specifications complicate both execution and clarification for language-model agents. Yet agents' responses to these information gaps remain poorly characterized across models and execution harnesses. We present AM-Bench, a benchmark built from 48 tas…

- **[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088v1)**
  - *Peng Jiang, Dongyang Li, Quanying Liu et al.*
  - `2026-10-13`
  - Autoresearch systems increasingly undertake entire research projects. In practice, scientific research requires systems to pursue multiple interdependent claims through a continuous, multi-stage workflow and revise experiments as evidence accumulates. Existing evaluations of auto…

- **[AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement](https://arxiv.org/abs/2610.18083v1)**
  - *Wenhao Zhou, Jiajun Song, Haitao Wang et al.*
  - `2026-10-13`
  - Scaling recursive self-improvement requires additional computation to produce useful research progress in reaching persistent objectives. Intuitively, more researcher agents can explore more hypotheses, but early evaluation scores might misrepresent their promise, shared findings…

- **[Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents](https://arxiv.org/abs/2610.18052v1)**
  - *Bofan Xie, Chaokun Wang, Guanchen Ge et al.*
  - `2026-10-13`
  - Long-term memory has become a core component of large language model (LLM) agents. As agents accumulate personal information over long-term use, users increasingly ask them to delete sensitive or outdated facts. A memory system should honor such requests. It should remove exactly…

- **[LatentRemedy: Efficient Remedy For Non-Prefix KV Cache Reuse in Multi-Agent Systems](https://arxiv.org/abs/2610.18014v1)**
  - *Zhiwei Chen, Zhongtao Rao, Waikit Xiu et al.*
  - `2026-10-13`
  - Non-prefix KV cache reuse is a promising approach for improving inference efficiency in multi-agent systems as agents share the same context blocks. However, when agents have conflicting tasks, directly reusing non-prefix KV caches across agents can severely degrade model perform…

- **[Cost-Efficient Privacy Enforcement for Email-Generating LLM Agents under Strategic Information Requests](https://arxiv.org/abs/2610.18007v1)**
  - *Qikun Cai, Tao Huang, Chen Hou*
  - `2026-10-13`
  - LLM agents now act as delegated communication intermediaries: they read private context, draft messages, and send externally visible emails on behalf of a user. Existing checker-repair defenses can reduce inappropriate disclosure, but they rely on repeated calls to a remote actio…

- **[SWEPatchTest: Evaluating Software Tests Beyond Reproduction](https://arxiv.org/abs/2610.18004v1)**
  - *Hua Lu, Pengcheng Wang, Han Li et al.*
  - `2026-10-13`
  - Coding agents use generated tests to decide whether a proposed patch satisfies an issue's requirements. A suite that fails on the buggy program and passes after applying the reference patch can still accept an incorrect patch or reject a correct patch. We introduce SWEPATCHTEST,…

- **[Interaction-as-a-Judge](https://arxiv.org/abs/2610.17895v1)**
  - *Wayne Chi, I-Hung Hsu, Li Chen et al.*
  - `2026-10-13`
  - Coding agents are tasked with producing sophisticated interactive applications such as websites, desktop applications, and games. While humans assess these applications interactively, current automated LLM evaluations primarily focus on code analysis and unit tests. This mismatch…

- **[Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards](https://arxiv.org/abs/2610.17893v1)**
  - *Keru Chen, Sen Lin, Yingbin Liang et al.*
  - `2026-10-13`
  - Effective collaboration among large language model (LLM) agents in multi-agent systems requires sharing relevant evidence, requesting missing information, and incorporating teammates' contributions into decisions. Training these behaviors is challenging because final task outcome…

- **[ECMR: Evidence-Aware Deliberation Control for Multi-Agent LLM Reasoning](https://arxiv.org/abs/2610.17869v1)**
  - *Yuan Liu, Haoyue Peng, Fanliang Hu et al.*
  - `2026-10-13`
  - Multi-agent Large Language Model (LLM) systems typically commit to a deliberation protocol before inference. A fixed protocol cannot allocate computation differently to resolved and unresolved instances, and it may mistake repeated support for independent confirmation. We study t…

- **[RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions](https://arxiv.org/abs/2610.17867v1)**
  - *Rishabh Ranjan, Vignesh Kothapalli, Harshvardhan Agarwal et al.*
  - `2026-10-13`
  - Foundation models for tables and relational databases are increasingly used for predictive tasks across various scientific and industrial domains. However, adapting existing models to unseen datasets requires tens of thousands of examples. Here we introduce RT-J, an 85M-parameter…

- **[Learning Adaptive Deliberation Control for Reliable Recognition with Multi-Agent Language Models](https://arxiv.org/abs/2610.17840v1)**
  - *Yuan Liu, Haoyue Peng, Fanliang Hu et al.*
  - `2026-10-13`
  - Multi-agent deliberation can improve recognition by criticizing and revising candidate answers, but fixed controls cannot respond to changes in disagreement or reasoning quality. We present an adaptive multi-agent controller (ADMA) that learns continuous policies for proposal, ch…

- **[ProtoArena: Can AI Agents Discover and Exploit Real-World Cross-Component Protocol Vulnerabilities?](https://arxiv.org/abs/2610.17837v1)**
  - *Fasheng Miao, Zhaoyu Hu, Xiang Li et al.*
  - `2026-10-13`
  - Large language model (LLM) agents are increasingly used for vulnerability analysis, yet existing benchmarks provide limited coverage of exploitation that depends on interactions among network protocol components. Such vulnerabilities arise from inconsistencies in message interpre…

- **[Benchmarking and Training Reward Models for Cross-Source Evidence Grounding in Search Agents](https://arxiv.org/abs/2610.17827v1)**
  - *Haochen Zhao, Minsheng Hao, Zheng Li et al.*
  - `2026-10-13`
  - Existing approaches to training and evaluating search agents focus heavily on final-answer quality, largely neglecting how generated answers map back to retrieved evidence. Recent methods track citations to enforce grounding, but citation support alone does not establish source i…

- **[Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution](https://arxiv.org/abs/2610.17816v1)**
  - *Pengcheng Huang, Zhenghao Liu, Shixin Ren et al.*
  - `2026-10-13`
  - Edge-cloud collaboration combines the lower inference overhead and greater data locality of edge-side execution with the stronger capabilities of cloud-hosted models. However, as LLM agents increasingly operate in long-horizon scenarios, cloud participation becomes interleaved th…

- **[Agentic4PDM: Host-Governed Evidence Admissibility for Industrial Fault Diagnosis](https://arxiv.org/abs/2610.17786v1)**
  - *Nam V. Nguyen, Hoang Van Truong, Hieu D. D. et al.*
  - `2026-10-13`
  - We study industrial fault diagnosis as a classification task that assigns sensor time-series windows to predefined health states or fault types. Scarce labels and changing operating conditions make repeated training of specialized classifiers costly. Yet structures such as period…

- **[Memory Echo in Single-Agent Long-Term Memory: Lifecycle Evaluation and Provenance-Guided Mitigation](https://arxiv.org/abs/2610.17763v1)**
  - *Yufeng Li, Sheng Yao, Peng Zeng et al.*
  - `2026-10-13`
  - Long-term memory supports agents across sessions. Repeated retrieval and write-back can let one historical claim occupy multiple retrieval positions and influence current answers without independent evidence. Existing work examines retrieval, updating, and question answering, lea…

- **[Gaussian Process Bandits for AI System Optimization with Selectively Verified Feedback](https://arxiv.org/abs/2610.17760v1)**
  - *Shuang Wu*
  - `2026-10-13`
  - Gaussian process bandits exploit similarities among configurations to optimize prompts, retrieval systems, and agent workflows. In these applications, however, inexpensive model-based evaluations can disagree with trusted task outcomes. We study selective verification when an act…

- **[Instructions Are Evidence, Not Objectives: Measuring Outcome Alignment of Agents](https://arxiv.org/abs/2610.17757v1)**
  - *Kaiming Liu, Yuxuan Liu, Jinrui Ju et al.*
  - `2026-10-13`
  - Large language model agents can follow complex human instructions to solve real-world tasks. In practice, however, initial instructions are often incomplete. In our analysis of 100 user-agent trajectories from SWE-chat, 56\% of initial instructions omit requirements that later em…

- **[Degrees of Freedom in Multi-Agent Coordination: Between Centralized and Decentralized Regimes](https://arxiv.org/abs/2610.17751v1)**
  - *Yiqing Peng, Hehai Lin, Zixuan Wang et al.*
  - `2026-10-13`
  - Large language model (LLM)-based multi-agent systems (MAS) are commonly organized around two coordination regimes. Centralized coordination provides explicit control but can create a bottleneck at a single coordination locus, whereas decentralized coordination offers local autono…

- **[Auditing Failure Attribution: Label Predictability and Judge Behavior](https://arxiv.org/abs/2610.17747v1)**
  - *Tianyang Xu, Jing Gao*
  - `2026-10-13`
  - Failure-attribution benchmarks ask an LLM judge which step or agent caused a failure. A high score should mean the judge checked the faulty step against the run (a cross-step check). However, spurious signals (surface cues) that predict the annotation can produce a high score. In…

- **[Coupled Harness--Model Evolution for Scientific Equation Discovery](https://arxiv.org/abs/2610.17740v1)**
  - *Pengze Li, Jiaquan Zhang, Encheng Su et al.*
  - `2026-10-13`
  - Large language models (LLMs) are increasingly used to discover scientific equations from experimental data. Such a discovery system has two parts that must work together: a library of executable computational tools and the model's tool-use policy. The tools supply the solving cap…

- **[SkillScreen: High-Recall Screening of Malicious Agent Skills with Decision Models](https://arxiv.org/abs/2610.17727v1)**
  - *Jerrold Huang, Junwei Quan, Saiyue Lyu et al.*
  - `2026-10-13`
  - Agent skills turn natural-language instructions into actions, creating a security challenge: legitimate automation and malicious behaviour can look deceptively similar. A practical screen must catch nearly every attack while keeping the review load manageable. We present SkillScr…

- **[TSRL: Trigger-based Supervised Reinforcement Learning for Continual Agent Training](https://arxiv.org/abs/2610.17726v1)**
  - *Yuqian Fu, Kaiwen Jiang, Zijun Song et al.*
  - `2026-10-13`
  - Large language model (LLM) agents excel at complex, multi-step tasks but suffer from catastrophic forgetting during continual learning--acquiring new skills often degrades previously mastered capabilities. Existing post-training paradigms face a fundamental trade-off: Supervised…

- **[Evidence-First Agentic Verification](https://arxiv.org/abs/2610.17724v1)**
  - *Reza Sanayei, Razvan-Gabriel Dumitru, Sunjie Hou et al.*
  - `2026-10-13`
  - Long-horizon, semi-verifiable agentic tasks often rely on rubric-based evaluation, but the evidence needed to assess these tasks can be spread across the environment state and the execution trace. A judge may overlook this evidence or accept unsupported claims, including an agent…

- **[Upstream Influence, Downstream Re-Anchoring in LLM Agent Chains](https://arxiv.org/abs/2610.17723v1)**
  - *Chun-Yu Hsu, Lun-Wei Ku, Chung-Chi Chen*
  - `2026-10-13`
  - People act on evaluative judgments produced by LLM agents, and in multi-agent systems those judgments pass through several agents before reaching a person. We show that a workflow's information architecture---source access, handoff format, and which model reads the untrusted cont…

- **[Adaptive-Group Process Rewards for GUI Agents](https://arxiv.org/abs/2610.17710v1)**
  - *Zirui Shang, Yang Liu, Xin Shu et al.*
  - `2026-10-13`
  - Training graphical user interface (GUI) agents with reinforcement learning suffers from sparse outcome rewards, leading to inefficient learning. Process rewards offer a promising direction for credit assignment to intermediate actions; however, accurately evaluating an action req…

- **[HelpMeOut: A Neuropsychology-Grounded Benchmark for Error-Aware Monitoring of Household Task Execution](https://arxiv.org/abs/2610.17694v1)**
  - *Haoran Wang, Jingwei Huang, Anqing Duan et al.*
  - `2026-10-13`
  - We introduce HelpMeOut, an embodied AI benchmark for error-aware monitoring of household task execution. Existing embodied household benchmarks typically assume that humans execute tasks correctly, but this assumption does not hold for cognitively impaired persons or older adults…

- **[LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents](https://arxiv.org/abs/2610.17685v1)**
  - *Jingyue Cong, Estrid He, Zhuang Li et al.*
  - `2026-10-13`
  - Enterprise agents face safety risks that cannot be determined from individual actions alone. Existing safety benchmarks largely evaluate action-local risks, overlooking failures whose safety depends on workflow state. In such state-dependent risks, the same action may be safe in…

- **[Cowork-Gym: Synthesizing Interactive Work Environments at Scale](https://arxiv.org/abs/2610.17670v1)**
  - *Anni Zou, Cheng Chen, Jiaji Deng et al.*
  - `2026-10-13`
  - Cowork agents navigate dependencies across tools and files while adapting to changing user requirements and edits to shared workspaces. Scaling such environments requires maintaining consistency among task objectives, executable resources, user behavior, and success criteria. We…

- **[Can Agents Truly Forget? Explore Machine Unlearning for LLM Agents](https://arxiv.org/abs/2610.17659v1)**
  - *Junkai Lin, Ge Xu, Zheng Xu et al.*
  - `2026-10-13`
  - Large language model (LLM) agents have shown strong capabilities in interactive problem solving, tool use, and long-horizon task execution. However, they may also acquire sensitive or private knowledge during training and expose it during deployment. Retraining a model from scrat…

- **[Executable Prefix Values for Locating Agent Failures](https://arxiv.org/abs/2610.17633v1)**
  - *Bingyu Shen, Jiaqi Tang, Lan Wei et al.*
  - `2026-10-13`
  - Work on debugging LLM agents treats the "first mistake" marked by a human or LLM judge as ground truth for where a trajectory failed. We ask whether such labels point at causes or symptoms, and make the distinction executable: we restart the agent from reconstructed intermediate…

- **[MAS-Gate: Unlocking Multi-Agent System Lifecycle via Node-Centric Quantification](https://arxiv.org/abs/2610.17613v1)**
  - *Hehai Lin, Zixuan Wang, Ming Yan et al.*
  - `2026-10-13`
  - Large language model (LLM)-based multi-agent systems (MAS) can solve complex problems beyond the reach of a single agent by decomposing tasks and coordinating complementary capabilities. Despite extensive research on MAS, existing work largely focuses on specific aspects or indiv…

- **[Verifier-Harness Co-Evolution for Training-Free Self-Improvement on Open-Ended Tasks](https://arxiv.org/abs/2610.17609v1)**
  - *Tianyi Xu, Yaolun Zhang, Yiran Wu et al.*
  - `2026-10-13`
  - Training-free self-improvement lets an agent use feedback to revise the response it is about to return and to update the harness state that shapes how it handles later tasks. On open-ended tasks that feedback rarely comes from reference answers or executable tests, so the agent h…

- **[Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents](https://arxiv.org/abs/2610.17544v1)**
  - *Jianghong Zhou, Hao Rong, Chen Lin et al.*
  - `2026-10-13`
  - Thought templates, skill libraries, agent memories and caches turn many reasoning steps into one. We call this reasoning contraction. A contracted memory saves reasoning steps and errors until its facts change, then quietly answers wrong. Most systems trust memories by counting s…

- **[SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection](https://arxiv.org/abs/2610.18807v1)**
  - *Wenlin Zhong, Hao Wang, Kun Yuan et al.*
  - `2026-10-13`
  - Agentic reinforcement learning (RL) enables large language models (LLMs) to learn from multi-turn interactions with verifiable outcomes. Textual skills can improve exploration by distilling prior interactions into reusable guidance. However, existing skill-based RL approaches oft…

- **[Autonomous Cyber Operations Gym for Training and Evaluating AI Models for Defence](https://arxiv.org/abs/2610.18594v1)**
  - *Tobias Hürten, Johannes F. Loevenich, Florian Spelter et al.*
  - `2026-10-13`
  - This paper proposes an Autonomous Cyber Operations (ACO) gym, a unified framework integrating high-fidelity network emulation, realistic user behaviour modelling for benign network traffic and adversarial profiles, and the generation of cybersecurity scenarios through open toolki…

- **[Towards Safe Autonomy for Computer Use](https://arxiv.org/abs/2610.18508v1)**
  - *Dominik Seip, Bartol Markovinović, Matthias Hein*
  - `2026-10-13`
  - The safety of LLM-based agents currently rests on alignment training and safety classifiers, neither of which can rule out that a sophisticated indirect prompt injection (IPI) goes through and causes significant harm. Recent work therefore builds agents with information-flow guar…

- **[Teach Me After You Learn It: Lookahead Self-Distillation for RLVR](https://arxiv.org/abs/2610.18256v1)**
  - *Zepeng Zhai, Meilin Chen*
  - `2026-10-13`
  - On-policy self-distillation (OPSD) has emerged as a popular training paradigm for LLMs, providing dense, token-level supervision by aligning a model's own distribution with the distribution induced by privileged information. However, existing OPSD methods derive supervision solel…

- **[When Does Opponent Modeling Pay Off? Spatial Inference Stabilises Reinforcement Learning under Partial Observability](https://arxiv.org/abs/2610.18229v1)**
  - *Marcel Petran, Stefan Edelkamp*
  - `2026-10-13`
  - Deep reinforcement learning agents in partially observable competitive games must act on beliefs about an unseen opponent's intent. We study a spatial opponent model: a transformer trained with hindsight-relabelled opponent goals that outputs a subgoal heatmap from the opponent's…

- **[Reinforcement Learning for Large-Scale Lifelong Multi-Agent Path Finding with Shared Spatial Fields](https://arxiv.org/abs/2610.18186v1)**
  - *Jean Seong Bjorn Choe*
  - `2026-10-13`
  - Large-scale applications of lifelong multi-agent path finding (LMAPF) call for computationally inexpensive movement decisions under changing traffic conditions and across varied layouts. We propose a navigation policy in which a convolutional network computes a shared spatial fie…

- **[Failure Recovery via Belief Updates and World Modeling for Long-Horizon Agents](https://arxiv.org/abs/2610.18082v1)**
  - *Xiyang Wu, Zhichao Liu, Shengxin zhang et al.*
  - `2026-10-13`
  - Long-horizon agents often struggle to recover from failures whose causes lie several steps earlier, beyond what local reflection or backtracking can resolve. We introduce BELIEFWEAVER, a framework that combines persistent evidence across attempts with prospective reasoning over r…

- **[FRACTION: Fraud Explanation Generation via Agentic Graph Context Navigation](https://arxiv.org/abs/2610.18023v1)**
  - *Cecelia Soh, Jun Hu, Yuan Li et al.*
  - `2026-10-13`
  - Graph fraud explanation generation emerges as an important task, which requires jointly leveraging graph structure and content information to produce human-readable explanations for a given risk label. An intuitive approach is to adapt existing graph-enhanced large language model…

- **[AlignPred: Error-Controlled KV Cache Compression via Alignment and Predictive Coding](https://arxiv.org/abs/2610.17970v1)**
  - *Xu Yang, Jiapeng Zhang, Zhiwei Zuo et al.*
  - `2026-10-13`
  - Long-running agents retain KV caches across turns and sessions for hours or days. Compressing these persistent caches requires reducing storage while controlling reconstruction error. We present AlignPred, a codec that combines local alignment with predictive coding under a confi…

- **[Searching for What Matters: Open-Ended Discovery of Multiple Hypotheses with Agentic Data Exploration](https://arxiv.org/abs/2610.17874v1)**
  - *Sanchit Kabra, Nurendra Choudhary, Jiangshu Du et al.*
  - `2026-10-13`
  - Discovering what drives an outcome from data is central to science and often requires deciding what is worth investigating before a specific hypothesis is known. Yet most existing hypothesis generation settings substantially narrow this search by providing a research question, ta…

- **[ATTUNE: Agentic Throughput Tuning for LLM Training](https://arxiv.org/abs/2610.17528v1)**
  - *Leo Fan, Hongyang Wang, Wenbo Chen et al.*
  - `2026-10-13`
  - Training recipes are tuned by hand for one model, cluster and workload, and every new model, accelerator, framework version or dataset means tuning again. Automated tuners search a fixed space of knobs and check only that a job runs, yet a configuration can run to completion whil…

- **[The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement](https://arxiv.org/abs/2610.18845v1)**
  - *Sijie Zhao, Zeqi Zhou, Heli Qi et al.*
  - `2026-10-13`
  - Earth observation (EO) models are still built by hand. For each new task, experts design a training recipe and tune it against a benchmark. We show that this loop can be handed to an agent. Any verifiable task can be cast as a harness and a verifier, where the harness defines wha…

- **[Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning](https://arxiv.org/abs/2610.18611v1)**
  - *Huaiwen Pang, Jiale Han, Junying Chen et al.*
  - `2026-10-13`
  - Legal question answering requires answers that are not only plausible, but also grounded in legally valid and citable evidence. Standard retrieval-augmented generation often relies on one-shot semantic matching, which is insufficient when legal evidence must be selected according…

- **[The Last Mile of Coding Agents for Long-Document Tasks: An Empirical Study on Clinical Trial Protocol Digitization](https://arxiv.org/abs/2610.18507v1)**
  - *Jiacheng Lin, Geoffrey Low, Nishit Agarwal et al.*
  - `2026-10-13`
  - Clinical trial protocols serve as the source of truth for study design, but are mostly written and used as unstructured PDF documents. Digitizing protocols turns static content into structured, machine-readable data that clinical software can analyze, validate, and execute. Codin…

- **[Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments](https://arxiv.org/abs/2610.18427v1)**
  - *Hoang Pham, Cong-Duy Nguyen, Dong Le et al.*
  - `2026-10-13`
  - Persistent textual memory lets language-model agents reuse lessons from past tasks to improve on future multi-step tasks without retraining. Systems such as ACE and Dynamic Cheatsheet keep it as a playbook: lessons the agent writes after each task and reads in its prompt. A key c…

- **[Receiver Decides Agent-to-Agent Negotiations](https://arxiv.org/abs/2610.18424v1)**
  - *Fardeen Sadab, Alif Hasnain, Afsana Shehrin et al.*
  - `2026-10-13`
  - When one language-model agent asks another for money, which of the two decides how much changes hands? We ran a round-robin tournament of 1,049 negotiations among fifteen agents. In each game a requester tries to raise money from a holder that has been told to keep a $100 endowme…

- **[Prompt-Injection Probes Learn the Conversation, Not Just the Injection](https://arxiv.org/abs/2610.18408v1)**
  - *Kaan Kale, Sriram Vishwanath*
  - `2026-10-13`
  - Linear probes on a model's hidden states are used as cheap monitors for indirect prompt injection: they screen the tool outputs an agent reads and send suspicious ones to a slower second check, so every false alarm has a cost. But a probe learns whatever separates its training ex…

- **[Jev-Guard: Fast Routing and Auditing Agent Actions over Editable Policy Trees](https://arxiv.org/abs/2610.18326v1)**
  - *Wenbin Hu, Huihao Jing, Haochen Shi et al.*
  - `2026-10-13`
  - Agent harnesses require a low-latency guardrail model together with customizable audit policies. However, deploying an auto-regressive guardrail model remains challenging: such models incur high inference latency and are often poorly aligned with customized policies. To address t…

- **[Narrative Lookahead in LLMs: Event-Level Decodability, Predictive Advantage, and Steering](https://arxiv.org/abs/2610.18121v1)**
  - *Donghoon Jung, Min Kim, Seojin Choi et al.*
  - `2026-10-13`
  - Do language models carry information about narrative events before writing them, and how far ahead? We examine narrative lookahead through salient, state-changing events rather than tokens or response-level attributes. We extract 23,355 LLM-annotated events from 2,000 stories gen…

- **[From Agents to Edges: Paired Optimization for Multi-Agent Collaboration](https://arxiv.org/abs/2610.18069v1)**
  - *Feng Lin, Xiaotian Yu, Yifan Yang et al.*
  - `2026-10-13`
  - Strong individual agents do not guarantee effective collaboration. Communication must align what one agent conveys with how another interprets and uses it. This dependency makes the communication edge a natural unit of optimization. We introduce Paired Automated Communication Opt…

- **[BRIDGE: Selective Boundary Repair with Dependency Graph Evidence in Multi-Agent Systems](https://arxiv.org/abs/2610.17805v1)**
  - *Encheng Su, Pengze Li, Ziheng Hua et al.*
  - `2026-10-13`
  - Multi-agent collaboration has emerged as a critical paradigm for tackling complex, long-horizon tasks; however, while coordination protocols continue to advance, systemic failures at the inter-agent collaboration interface remain a pervasive bottleneck. In collaborative workflows…

- **[Full-duplex Spoken Language Modeling with Discrete Diffusion](https://arxiv.org/abs/2610.17780v1)**
  - *Chen Chen, Pin-Jui Ku, Ankita Pasad et al.*
  - `2026-10-13`
  - We introduce Diffuplex, a full-duplex spoken language model based on discrete diffusion that achieves an unprecedented balance between linguistic intelligence and response efficiency. With thinking mode, Diffuplex delivers 13.0 tokens per forward pass, reaching an average of 1872…

- **[Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models](https://arxiv.org/abs/2610.17777v1)**
  - *Shanshan You, Zhengqi Wang, Hao Liu et al.*
  - `2026-10-13`
  - Theory of mind (ToM), the ability to reason about others' mental states, underlies effective communication and coordination. Its higher-order form enables reasoning over nested perspectives in strategic interactions. However, existing evaluations often equate belief-nesting depth…

- **[RALI@iKAT 2026: Retrieval-aware User Profile Denoising via Personalized Conversational Dense Retrieval](https://arxiv.org/abs/2610.17673v1)**
  - *Yuchen Hui, Fengran Mo, Jia Ao Sun et al.*
  - `2026-10-13`
  - Modern conversational information access systems continuously extract user information from conversations to build user profiles for personalized retrieval. As user profiles accumulate over time, they inevitably become noisy, making effective user profile denoising a fundamental…

- **[When Does an ASR Error Matter? Task-Role Diagnostics for Tool-Using Voice Agents](https://arxiv.org/abs/2610.17619v1)**
  - *Xiaolong Wang, Shijie Su, Naqi Xiong*
  - `2026-10-13`
  - In cascaded voice agents, ASR errors can have markedly different downstream consequences: a small transcription error may leave a tool call unchanged or alter its intent or arguments. Conventional word error rate (WER), however, does not capture these differences. We introduce Sp…

- **[StateHarness: Maintaining Evolving Project State for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.17616v1)**
  - *Chuan Zou, Yujun Zhou, Xiaonan Luo et al.*
  - `2026-10-13`
  - Long-horizon coding requires agents to maintain an evolving view of the project they are changing: what problem is currently being solved, what has already been learned or modified, which other artifacts may be affected, and what work remains unresolved. When this information is…

- **[EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation](https://arxiv.org/abs/2610.17560v1)**
  - *Zeru Shi, Jindong Jiang, Ryo Hachiuma et al.*
  - `2026-10-13`
  - Complex and long-horizon agent tasks often rely on frontier models deployed in the cloud to achieve strong performance. However, using these models for every step of a long-horizon trajectory incurs substantial inference cost, even though not all steps may require the same level…

- **[PlanPath: Exploration-Guided Orchestration for Patient-Level Pathology Reasoning](https://arxiv.org/abs/2610.18664v1)**
  - *Jiusong Ge, Mingzhao He, Qidong Liu et al.*
  - `2026-10-13`
  - A patient's pathology case spans tens of slides from distinct specimens and anatomical sites, each carrying non-redundant, site-specific evidence. Forming a patient-level conclusion therefore requires locating the slides relevant to a given question and integrating complementary…

- **[CALM: Decentralized Control of Cooperative Aerial Manipulation with Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.18425v1)**
  - *Jiaxi Huo, Petre Ricioppo, Fausto Francesco Lizzio*
  - `2026-10-13`
  - Cooperative aerial manipulation is difficult under wind, payload motion, and noisy goal broadcasts because multiple Unmanned Aerial Vehicles (UAVs) are coupled through a shared payload. We present CALM (Cooperative Aerial Learned Manipulation), a decentralized controller for aeri…

- **[Strategic Multi-Agent Resource Allocation via Statistical Contracts](https://arxiv.org/abs/2610.18336v1)**
  - *Ben Chugg, Michael I. Jordan, Aaditya Ramdas*
  - `2026-10-13`
  - We study a class of strategic hypothesis testing problems in which a principal aims to allocate resources among competing agents who possess data or data-generating mechanisms that may be relevant to the principal's goals. Each agent can pay a participation cost to opt into a sta…

- **[Does self-distillation improve reasoning?](https://arxiv.org/abs/2610.18613v1)**
  - *Jason Ken Adhinarta, Raina Wu, Ashutosh Sharma et al.*
  - `2026-10-13`
  - Self-distillation is an emerging approach that trains a model to imitate its own predictions when conditioned on privileged information, such as correct answers or environmental feedback. Recent methods have reported better sample efficiency and generalization than reinforcement…

- **[Teacher-Guided Tool Learning for Small Language Models via Bidirectional KL Constraints](https://arxiv.org/abs/2610.18459v1)**
  - *Haoxuan Gao, Qin-Wen Luo, Xiang Chen et al.*
  - `2026-10-13`
  - External tools can extend the capabilities of small language models (SLMs), enabling their deployment in resource constrained environments. However, their limited capabilities make it difficult for SLMs to discover effective tool use behaviors through reinforcement learning alone…

- **[The belief-action gap in language model agents](https://arxiv.org/abs/2610.17444v1)**
  - *Ayse Sila Okcu, Weisheng Wang, Tongmeng Xie et al.*
  - `2026-10-12`
  - Language model (LM) agents can fail for different reasons, requiring different explanations and interventions. We study how state beliefs, action values, and action preferences interact as LM agents reason and commit to decisions in text-rendered grid worlds. We estimate task-rel…

- **[SchemaWeaver: Accelerating On-Device Mobile Agentic AI via Schema-Guided Parallel LLM Decoding](https://arxiv.org/abs/2610.17436v1)**
  - *Boyuan Yang, Wei Gao*
  - `2026-10-12`
  - Large language models (LLMs) on mobile devices can act as agents that call external software tools to complete complex tasks, but the major challenge of supporting on-device mobile agentic AI with LLMs is the long latency of LLM tool calling on mobile devices. In particular, the…

- **[Reinforcement Learning In Partially Verifiable Environments for Colon Cancer Treatment Planning](https://arxiv.org/abs/2610.17426v1)**
  - *Li-Ching Chen, Andrés Franco Valiente, Yuta Ishiyama et al.*
  - `2026-10-12`
  - Clinical decision-making is a sequential process of information collection, clinical inference, and forecasting under partial observability, often without a uniquely correct treatment decision. Large language models (LLMs) have demonstrated strong medical question-answering capab…

- **[Why Agentic Workflows Fail: A Taxonomy Derived from Literature and Empirical Data](https://arxiv.org/abs/2610.17418v1)**
  - *Xin Li, Rami Bahsoon, Tao Chen*
  - `2026-10-12`
  - Agentic workflows combine large language models with planning, memory, tools, execution environments, and iterative feedback. Their failures are difficult to diagnose because the same user-visible symptom may originate from model behavior, workflow orchestration, external tools,…

- **[Agency as a New Organizing Abstraction for Computer Science](https://arxiv.org/abs/2610.17410v1)**
  - *Ian Foster*
  - `2026-10-12`
  - Advances in large-scale machine learning have enabled agentic AI systems: persistent, autonomous computational entities that pursue goals, initiate actions, and interact with open environments. These systems are often framed as applications of foundation models. We argue that thi…

- **[Get In, Decide, Prove: A Merchant-Side Readiness Benchmark for Agentic Commerce](https://arxiv.org/abs/2610.17378v1)**
  - *Adrian de Valois-Franklin, Alex Bogdan, Anas Ibrahim et al.*
  - `2026-10-12`
  - AI agents now browse and buy on people's behalf, and benchmarks measure how well the agents perform. Far less is known about the other side of the transaction: whether a merchant's website lets an agent in, publishes terms precise enough to decide a purchase, and leaves evidence…

- **[When Goals Leak Across Relationships: How Cached Goal Representations Shape Cross-Client Decisions](https://arxiv.org/abs/2610.17365v1)**
  - *Saloni Gupta, Sébastien Krier, Glenn Matlin*
  - `2026-10-12`
  - As LLM agents take on more autonomous roles, they may interact with multiple clients and counterparties whose goals and incentives conflict. If an agent maintains shared inference state across these interactions, information associated with one relationship may influence decision…

- **[Budgeted KV-Cache Repair for Evolving Contexts](https://arxiv.org/abs/2610.17338v1)**
  - *Han Yu, Wenhui Zhu, Jincheng Cao et al.*
  - `2026-10-12`
  - Language-model agents revise their working context as information becomes obsolete, but deleting text does not erase its influence on cached computation. Later key-value (KV) states remain conditioned on the deleted content, while recomputing the entire retained suffix can be cos…

- **[Do Theorem Provers Need Theorem-Proving Agents? mini-Lean-agent: A Coding-Agent Baseline for Lean](https://arxiv.org/abs/2610.17331v1)**
  - *Tomas Ortega, Simon Park, Ayush Khaitan et al.*
  - `2026-10-12`
  - General-purpose coding agents use standard shell and file interactions, yet formal theorem-proving agents often rely on specialized, ad-hoc tooling. This makes it difficult to determine which components of theorem-proving agents provide benchmark gains: an improved base model, a…

- **[Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models](https://arxiv.org/abs/2610.17310v1)**
  - *Hanbo Xie, Yue Zhao, Robert C. Wilson*
  - `2026-10-12`
  - Language-model agents are expected to adapt to others whose behavior changes through interaction. Yet adaptation may rely on learned behavioral patterns rather than theory of mind (ToM): the ability to infer others' mental states, including beliefs and intentions. We introduce a…

- **[The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow](https://arxiv.org/abs/2610.17301v1)**
  - *Arya Fayyazi, Mehdi Kamal, Massoud Pedram*
  - `2026-10-12`
  - Language-model agents sometimes act beyond their authorization and then misreport what they did. On CAPE-Bench, matched agent tasks in which one fact decides whether an action is authorized, frontier open-weight agents do both, and one behavior marks the lie: retroactive permissi…

- **[PhysCodeGym: Benchmarking Coding Agents for Physically Verifiable 4D Reconstruction](https://arxiv.org/abs/2610.17288v1)**
  - *Shuai Shao, Jinchen He, Cunxin Fan et al.*
  - `2026-10-12`
  - Building physical simulations from video requires coding agents to translate observations into executable models and refine them through tool use. We introduce PhysCodeGym, a benchmark for physically verifiable 4D reconstruction with $156$ tasks covering rigid-body, liquid, defor…

- **[AutoMARS: Automatic and Scalable Multi-Agent Large Language Model Framework for Supply Chain Risk Assessment](https://arxiv.org/abs/2610.17206v1)**
  - *Yinzhu Quan, Zefang Liu, Frederick Benaben et al.*
  - `2026-10-12`
  - We propose AutoMARS (Automatic Multi-Agent Risk Assessment), an agentic framework for automatic and scalable comparative risk assessment in supply chain networks. The framework enables end-to-end execution of analytical workflows by automatically planning tasks, coordinating spec…

- **[Deleting Code Without Losing Knowledge: Regenerative Software for Python Libraries](https://arxiv.org/abs/2610.17197v1)**
  - *Thomas Bartz-Beielstein*
  - `2026-10-12`
  - In the age of "Software 3.0", when a complete program can be rewritten in minutes by an agent, the traditional approach of relying on code as the sole source of truth becomes questionable. Fowler advocated for a set of seven primitives, which lay the framework for regenerative so…

- **[ChemExplain: A Multimodal Benchmark for Explanatory Chemical Reasoning](https://arxiv.org/abs/2610.17183v1)**
  - *Aotian Chen, Frazier N. Baker, Reza Averly et al.*
  - `2026-10-12`
  - Current chemistry benchmarks primarily evaluate outcome prediction or reaction pathway generation, but rarely test whether a model can explain why an observed chemical effect occurs. We introduce ChemExplain, a benchmark of 1,180 multiple-choice chemistry questions drawn from 383…

- **[EvoQuantLab: Training-Free Dual-Loop Evolution for Auditable Quantitative Research](https://arxiv.org/abs/2610.17130v1)**
  - *Haolin Yang, Zhiqiang Qian, Chutian Chen et al.*
  - `2026-10-12`
  - Automated alpha factor discovery is critical for modern quantitative research. While large language models (LLMs) have increasingly been integrated into quantitative workflows, existing agent-based approaches remain highly susceptible to severe backtest overfitting. To address th…

- **[Who is the 'I' in AI? Establishing Decentralized Identity and Accountability for Autonomous Agents](https://arxiv.org/abs/2610.17126v1)**
  - *Ahammod Munim Ramil, Khalid Al Kafi, M. A. Abdullahis Sany et al.*
  - `2026-10-12`
  - The rapid proliferation of autonomous AI agents in decentralized ecosystems challenges existing identity paradigms. While human identity is traditionally anchored in biological and/or self-asserted attributes and government credentials, AI agents lack a standardized definition of…

- **[When LLM Agents See a Conflict but Still Proceed: Cross-Domain Dependencies in Network Slicing](https://arxiv.org/abs/2610.17118v1)**
  - *Marcos Lima Romero, Ricardo Suyama*
  - `2026-10-12`
  - Future AI-native networks are being designed to apply autonomous agents built on large language models (LLMs) in network management through intents. When intents from different domains meet on the same resource, an agent must recognize the cross-domain dependency before taking an…

- **[D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control](https://arxiv.org/abs/2610.17114v1)**
  - *Xuan Wen, Baichao Wang*
  - `2026-10-12`
  - Frontier large language models (LLMs) now reason about space well enough to program robots, yet the world models behind robot policies are implicit, held in network weights or predicted video, and cannot be inspected or corrected directly. We present D-World, an explicit world-la…

- **[Interactive Navigation Beyond Reachability: Benchmark and Agentic Framework](https://arxiv.org/abs/2610.17089v1)**
  - *Delun Li, Xueyao Wei, Rui Chen et al.*
  - `2026-10-12`
  - Existing embodied navigation tasks commonly assume that traversability and object states remain fixed during an episode. Yet reaching a goal may require opening a door to access a room and then opening a container to reveal a hidden target. We formulate interactive navigation bey…

- **[Superintelligence and the Triple Risk of an AI Race](https://arxiv.org/abs/2610.17085v1)**
  - *Matthew Rendall, Max Hellrigel-Holderbaum, Leonard Dung*
  - `2026-10-12`
  - On many estimates, artificial general intelligence (AGI) is likely to emerge within the next few decades or even sooner. Once it does, it may quickly surpass human intelligence, possibly by a huge margin. Some believe that the country that develops AGI first could attain global d…

- **[Neos: Learning to Interleave Search and Visual Reasoning](https://arxiv.org/abs/2610.17043v1)**
  - *Ekko He, Jack Hong, Shilin Yan et al.*
  - `2026-10-12`
  - Recent multimodal deep search agents have advanced tool use and visual content retrieval, yet they still struggle to convert intermediate visual evidence into actionable guidance for subsequent search, limiting their effectiveness in long-horizon settings. To address this gap, we…

- **[CWE-bench: Refocusing Agentic Security from Exploitation to Defense](https://arxiv.org/abs/2610.17020v1)**
  - *Gonzalo Gonzalez-Pumariega, Ajay Jagannath, Adit Jain et al.*
  - `2026-10-12`
  - Cybersecurity evaluations of AI agents have focused largely on offense, yet a working exploit does not show that an agent can make software safe. An attacker needs to exploit only one vulnerability; a defender must find and fix all of them. We introduce CWE-bench, a private bench…

- **[Glasseek: A Transparent Recipe for Training and Trustworthy Evaluation of DeepSearch Agents](https://arxiv.org/abs/2610.16998v1)**
  - *Cong Pang, Jiaqi Su, Chengrui Wu et al.*
  - `2026-10-12`
  - Deep search enables language agents to solve complex information-seeking tasks through iterative web exploration. However, developing robust open-source agents remains challenging for three reasons. First, opaque trajectory-construction pipelines make training data difficult to a…

- **[MADDIE: Multi-Agent Drug Discovery Engine](https://arxiv.org/abs/2610.16975v1)**
  - *Ye Liu, Reza Averly, Avery Meyer et al.*
  - `2026-10-12`
  - Drug discovery remains a resource-intensive and time-consuming process, involving billions of dollars and a decade of development to advance a drug to market. While many in silico tools have accelerated this process, operating them still demands substantial time, effort, and expe…

- **[Social Priors: Descriptions of AI Users Shape How Language Models Trust and Cooperate](https://arxiv.org/abs/2610.16946v1)**
  - *Harsh Kumar, George Eilender, Ashton Anderson*
  - `2026-10-12`
  - Descriptions of how people use AI are becoming training data for the next generation of models. We ask whether what a model reads about its users changes how it treats people. Using contrastive synthetic-document finetuning, we train Qwen3-32B on four matched corpora built from t…

- **[Audit tools of the trade: Automated Auditor Elicitation Can Be Sensitive to the Context the Auditor Is Given](https://arxiv.org/abs/2610.16911v1)**
  - *Ben Slater, Ryan Lundqvist, Leo Richter et al.*
  - `2026-10-12`
  - Does providing additional context to automated AI auditors improve their effectiveness? Using the Petri tool to audit LLM coding agents, we test the impact of providing two types of resources (an external codebase and benchmark transcripts) to LLM auditors, across four auditor-ta…

- **[Neural Bayesian Networks for Modular and Scalable Decision-Making Under Uncertainty](https://arxiv.org/abs/2610.16902v1)**
  - *Giovanni Briglia, Marco Lippi, Stefano Mariani et al.*
  - `2026-10-12`
  - Bayesian Networks (BNs) are established tools for letting agents reason under uncertainty in sequential decision-making. They split a joint distribution into local conditional mechanisms arranged on a directed acyclic graph, which makes them modular, interpretable, and ready to p…

- **[Observe, Share, or Predict? Disentangling Partner Information in Embodied Multi-Agent Collaboration](https://arxiv.org/abs/2610.16895v1)**
  - *Adrián Szlatincsán, Filippo Ziliotto, Bruno Lepri et al.*
  - `2026-10-12`
  - LLMs are used as high-level controllers for embodied agents, but it remains unclear whether they support collaborative reasoning, such as anticipating a collaborator's actions in real-time teamwork without dialogue. We ask if observing the partner's state, exchanging object knowl…

- **[Davinci-Tool: Scaling Agentic Tool-Use Supervision with Verifiable Executable Environments](https://arxiv.org/abs/2610.16867v1)**
  - *Xiaoyang Yuan, Ji Zhao, Xingyu Hu et al.*
  - `2026-10-12`
  - Reliable agentic tool use requires training data that pair diverse multi-step workflows with executable evidence that the requested outcomes were achieved. Scaling either trajectory coverage or verification alone is insufficient as new environments introduce distinct states, rule…

- **[Same Operation, Different Permission: Evaluating Whether Guardrails Honor Authorization](https://arxiv.org/abs/2610.16838v1)**
  - *Huihao Jing, Shaojin Chen, Wenbin Hu et al.*
  - `2026-10-12`
  - As language-model agents write code, move money and change records on behalf of users, deciding whether an action is authorized has become a central safety problem. Guardrails are often placed in front of these actions, yet few evaluations ask whether their decisions follow autho…

- **[PrivacyGuard: Source-Linked Sanitization and Locally Resolvable PII References for Cloud GUI Agents](https://arxiv.org/abs/2610.16778v1)**
  - *Zian Yuan, Wei Li*
  - `2026-10-12`
  - Cloud graphical user interface (GUI) agents send instructions and screenshots to remote planners, exposing personally identifiable information (PII). Existing placeholder defenses mask detected spans and reuse exact strings. Fragmented or changed forms can expose PII or break ent…

- **[Game-Creation-Agents: Autonomous Game Production](https://arxiv.org/abs/2610.16776v1)**
  - *Tencent Multimodal RL Team, Xiangxin Zhou, Jiaqi Tang et al.*
  - `2026-10-12`
  - Game-Creation-Agents (GCA) turns a natural-language request into a runnable Phaser 4 browser game. The pipeline first builds a multimodal game design document that couples mechanics and scene contracts to grounded visual references. It then projects that document into a runtime s…

- **[Trace-to-Architecture: Capability Bottleneck Diagnosis for Harness Revision](https://arxiv.org/abs/2610.16725v1)**
  - *Wenfeng Wang, Jianrui Shi, Mingang Guo et al.*
  - `2026-10-12`
  - Improving an LLM agent requires knowing what to change when it fails. Similar failures can require different fixes, and resolving one problem can expose another. We introduce Trace-to-Architecture (T2A), a framework that uses execution trajectories to determine what to change in…

- **[Structural Baselines Matter for Agent Failure Detection and Attribution](https://arxiv.org/abs/2610.16661v1)**
  - *Ramesh Arvind Naagarajan, Stefan Streif*
  - `2026-10-12`
  - An LLM agent using tools can fail silently. It stops before the task is done, raises no error, and answers fluently. Two kinds of monitor address this, one deciding whether a run failed and the other naming the step where failure became unavoidable. Much of the reported performan…

- **[REEL: Learning to Retrieve, Evaluate, and Evolve Visual Memory for Any Long-Horizon Multi-Shot Video Generation](https://arxiv.org/abs/2610.16632v1)**
  - *Hang Xu, Guohui Zhang, Xiaoxiao Ma et al.*
  - `2026-10-12`
  - Memory-based long-video generation aims to combine user control with long-range visual consistency. We organize this process into three functional components: a planner, an adapter, and a generator. Representative multi-shot systems couple memory to generator-specific interfaces…

- **[LATCH: LLM-Assisted Timing Closure Harness for Post-Route FPGA Optimisation](https://arxiv.org/abs/2610.16625v1)**
  - *Shu Gu, Matthew Youngman, Yuqin Zhao et al.*
  - `2026-10-12`
  - Post-route FPGA timing closure remains expert-dependent and computationally expensive. We present LATCH (LLM-Assisted Timing Closure Harness), a two-layer framework that separates large language model (LLM) orchestration from deterministic FPGA implementation and evaluation. Acro…

- **[G$^2$WAM: World Action Models for Efficient and Geometry Grounded Image-Goal Navigation](https://arxiv.org/abs/2610.16558v1)**
  - *Ke Gui, Chenghao Shi, Ziyue Wang et al.*
  - `2026-10-12`
  - World models capture environment dynamics and support counterfactual reasoning for planning. In image-goal navigation, where the target often lies beyond the current field of view, the agent must not only model environmental dynamics but also maintain a persistent spatial memory…

- **[AI Discovery in Combinatorics: From Problems to Solutions and Back to Bigger Problems](https://arxiv.org/abs/2610.16555v1)**
  - *Eugenio Cainelli, Lorenzo Luccioli, Alessandro Iraci et al.*
  - `2026-10-12`
  - We introduce $qt$Bench, a benchmark of 29 open problems in algebraic combinatorics. These problems ask for a simple combinatorial algorithm that explains given polynomial coefficients or identities. To help AI agents search for such algorithms, we provide a scaffold for playing w…

- **[Overtaught, Underlearned: Learner-Centered Distillation from Multi-Agent Discussion](https://arxiv.org/abs/2610.16543v1)**
  - *Mengtao Zhou, Jianxiao Wang, Xiupeng Chen et al.*
  - `2026-10-12`
  - Multi-agent discussion produces reasoning collaboratively, while deployment still relies on a smaller student that must answer alone. Full-graph distillation transfers such discussions by treating each correct solution as a separate training target, but what teachers provide need…

- **[EAU: Environment-Agent-User Co-evolution for Training User-Centric Agents](https://arxiv.org/abs/2610.16523v1)**
  - *Min Cai, Dan Zhang, Gao Xing et al.*
  - `2026-10-12`
  - Training LLM agents to interact with users over multiple turns is challenging because the learning signal depends not only on the agent, but also on the user simulator and environment, which jointly shape the agent's experience. Simulated users can be stochastic or inconsistent,…

- **[From Caricature to Collective Artifact: How Persona Construction Drives Polarization in Generative Social Simulations](https://arxiv.org/abs/2610.16498v1)**
  - *Dimitris Michailidis, Petter Törnberg, Fernando P. Santos*
  - `2026-10-12`
  - Generative Social Simulation (GSS) leverages Large Language Models (LLMs) to create sophisticated personas that define agents with demographics, emotions, and political opinions. While prior work shows that personas compress outputs into stereotypical caricatures, there is no com…

- **[Drafting Agents, Not Just Tokens: Speculative Recursive Self-Improvement for Agentic Systems](https://arxiv.org/abs/2610.16491v1)**
  - *Xin Xu, Ke Cheng, Hao Wang et al.*
  - `2026-10-12`
  - Improving an agent through successive revisions requires balancing exploration and evaluation under a limited budget. A narrow search can miss useful sequences of edits, while fully evaluating every intermediate version can exhaust the budget before those sequences yield a verifi…

- **[CryptoFlowBench: Benchmarking Multi-Hop Reasoning on Blockchains for Cryptocurrency Fund Tracing](https://arxiv.org/abs/2610.16449v1)**
  - *Runang He, Tongya Zheng, Jing Cao et al.*
  - `2026-10-12`
  - Pseudonymous accounts and complex smart-contract ecosystems substantially hinder the tracing of illicit cryptocurrency fund flows. Existing Graph Neural Networks (GNNs) have achieved promising performance in blockchain fraud detection, yet their static node- or edge-level predict…

- **[RAP-WAM: Learning World-Action Models through Predictive Rehearsal and Action Perturbations](https://arxiv.org/abs/2610.16443v1)**
  - *Yuanpeng He, Ceyao Zhang, Fangjing Li et al.*
  - `2026-10-12`
  - Recent world action models draw on video generation priors to jointly predict future observations and robot actions. Adapting these priors to control requires determining how future predictions should guide policy learning. RAP-WAM combines predictive Rehearsal and Action Perturb…

- **[AuthGateBench: Benchmarking LLMs as Authorization Gate](https://arxiv.org/abs/2610.16426v1)**
  - *Zhixiong Zhuang, Jin Jia, Zhiwei Shang et al.*
  - `2026-10-12`
  - Automated approval systems let coding agents execute high-risk actions with minimal human oversight by delegating the authorization decision to a classifier, typically a large language model (LLM). Such systems, adopted in tools like Claude Code and Codex, remain vulnerable to fa…

- **[SLS-Bench: A Benchmark for Incident Log Summarization with Synthetic Observability Data](https://arxiv.org/abs/2610.16412v1)**
  - *Valerii Iakovlev, Markus Spanring, Martin Flechl*
  - `2026-10-12`
  - As IT systems grow in complexity, automated agent-driven incident response becomes increasingly critical. A key capability for these agents is summarizing large log streams into human-readable reports. Further progress requires meaningfully evaluating this function, yet existing…

- **[EvoWeb: A Benchmark for Coding Agents on Evolving Web Applications](https://arxiv.org/abs/2610.16402v1)**
  - *David Nukrai, Bar Alon, Nativ Levy et al.*
  - `2026-10-12`
  - Web application development often proceeds through successive requests that extend an existing implementation. Yet web-generation benchmarks primarily evaluate development toward fixed specifications. We introduce EvoWeb, a novel benchmark comprising 320 cumulative requests over…

- **[Recursive Environment Scaling for General Long-Horizon Agents](https://arxiv.org/abs/2610.16397v1)**
  - *Lingxiao Jing, Zhengbo Jiao, Yichen Xiang et al.*
  - `2026-10-12`
  - We study environment scaling as a way to increase agent-benchmark difficulty while holding core task objectives fixed. Our framework, Recursive Environment Scaling (RES), transforms existing benchmark environments while preserving their objectives and completion requirements. A p…

- **[Efficient Multi-Agent Reasoning via Confidence-Guided Adaptive Debate](https://arxiv.org/abs/2610.16343v1)**
  - *Seungdong Yoa, Ye Seul Sim, Suhee Yoon et al.*
  - `2026-10-12`
  - Multi-agent debate has shown promise for improving the reasoning of large language models, yet recent theory suggests its benefits are highly regime-dependent. While interaction can amplify informative signals under corrective conditions, symmetric debate dynamics are neutral in…

- **[TRAP: Tool-result Replay Attack for Probing Misbinding in LLM Agents](https://arxiv.org/abs/2610.16333v1)**
  - *Yutong Zhi, Jie Zhang, Xiuqi Lu et al.*
  - `2026-10-12`
  - As AI agents increasingly act through external tools, tool results are no longer simple outputs but execution artifacts that must remain correctly associated with the context that produced them. Yet as results persist across caches, recovery mechanisms, and shared runtime state,…

- **[HyWe: Unifying Search and Operation for Real-World Hybrid Web Tasks](https://arxiv.org/abs/2610.16319v1)**
  - *Zijian Cai, Haowei Liu, Kailai Chen et al.*
  - `2026-10-12`
  - Real-world hybrid web tasks need both information gathering and page interaction, yet search-based and operation-based agents are developed and evaluated separately. To bridge this gap, we introduce HyWe, a framework that unifies both capabilities within one model and trajectory.…

- **[ReTAC: Residual Test-Time Agentic Computation for Video Spatial Reasoning](https://arxiv.org/abs/2610.16315v1)**
  - *Yike Wu, Keyan Chen, Qixiong Wang et al.*
  - `2026-10-12`
  - Test-time agentic computation can improve multimodal large language models (MLLMs) through planning, tool use, iterative perception, and reflection, but indiscriminate computation may duplicate resolved work, introduce noisy evidence, and perturb correct predictions. We propose t…

- **[SLDBench v2: Active Scaling Law Discovery](https://arxiv.org/abs/2610.16297v1)**
  - *Lingbei Meng, Rui Huang, Zhirong Shen et al.*
  - `2026-10-12`
  - Scaling laws predict large-model performance from small experiments, but finding a reliable law itself requires costly experiments. SLDBench tests whether language-model agents can discover scaling laws when all experimental results are given upfront. We introduce SLDBench v2 wit…

- **[REVEAL: Reverse Engineering Agentic Latents from Frontier-Model Traces](https://arxiv.org/abs/2610.16288v1)**
  - *Yuetian Du, Meng Wang, Yucheng Wang et al.*
  - `2026-10-12`
  - Frontier LLM agents perform complex interactive tasks, but their inference costs motivate transferring their experience to smaller open-source agents. Distillation and latent communication typically require target-model training or access to source-model internals. We study how t…

- **[agent-risk: Risk Assessment for Changes to AI Agents](https://arxiv.org/abs/2610.16280v1)**
  - *Yue Zhao, Zixiang Xu, Angela Huyue Zhang et al.*
  - `2026-10-12`
  - Before changing a deployed AI agent (a stricter safety gate, a new model), organizations must approve the change, starting from existing logs. Extending classical risk analysis to partial records and partial changes to running systems, agent-risk replays logged episodes, assuming…

- **[Avoiding What Your Teacher Already Knows: Entity Familiarity for Deep-Search Distillation](https://arxiv.org/abs/2610.16251v1)**
  - *Yifei Liu, Zhixiang Liang, Wentao Tan et al.*
  - `2026-10-12`
  - Deep-search agents are commonly trained by distilling tool-use trajectories from stronger teacher models. However, structurally complex questions may remain relatively easy for teachers familiar with key entities in the underlying entity graph, resulting in lower search demand an…

- **[Learning to GUIDE the Group: Self-Learning LLM Facilitation Across Multi-Party Tasks](https://arxiv.org/abs/2610.16231v1)**
  - *Ziyi Liu, Tzu-Sheng Kuo, Jiale Liu et al.*
  - `2026-10-12`
  - As large language models are increasingly adopted as multi-party communication facilitators, there is a growing demand for agents capable of balancing diverse group dynamics across contexts. However, existing LLM facilitators are often fine-tuned for task-specific objectives; gen…

- **[Look Back to Move Forward: Learning to Revisit for Agentic Compositional Image Generation](https://arxiv.org/abs/2610.16224v1)**
  - *Zixu Wang, Xiaoran Zhao, Yahui Liu et al.*
  - `2026-10-12`
  - Text-to-image models have made remarkable progress in visual fidelity and instruction following, yet complex compositional generation remains challenging. Existing agentic approaches address this limitation through iterative generation and editing, adapting their actions based on…

- **[ProCARE: Real-World Study Automation via Profile-Grounded Evidence Contracts](https://arxiv.org/abs/2610.16175v1)**
  - *Zhaoyu Fan, Bowen Han, Jincheng Ou et al.*
  - `2026-10-12`
  - Real-world studies (RWS) analyze routinely collected healthcare data, such as electronic health records and insurance claims, to estimate treatment effects, monitor safety, and identify risk factors outside randomized trials. Automating RWS with large language model agents is app…

- **[Uncovering Robustness Weaknesses in LLM Agents via Persona Evolution with Task-Integrity Constraints](https://arxiv.org/abs/2610.16155v1)**
  - *Yutao Xie, Jingbo Yang, Guanyu Yao et al.*
  - `2026-10-12`
  - Interactive-agent evaluations commonly rely on standardized LLM-based user simulators that exhibit broadly cooperative behavior, potentially overlooking failures that arise under diverse but realistic user interactions. This can lead to overly optimistic estimates of agent robust…

- **[Unravel: Recovering an Interactive 3D Scene from a Single Image](https://arxiv.org/abs/2610.16146v1)**
  - *Hui Shan, Keyang Luo, Binjia Zhou et al.*
  - `2026-10-12`
  - We present Unravel, a training-free framework that turns a single image into an interactive 3D scene, where every object is an independent and movable asset. Existing generators either produce one entangled geometry in which no object can be moved, or predict all objects in one f…

- **[Pollard: Governed Semantic Execution Trees for Framework-Independent AI Agent Control and Replay](https://arxiv.org/abs/2610.16145v1)**
  - *Muntaser Syed, Marius C. Silaghi*
  - `2026-10-12`
  - Agent frameworks can persist checkpoints, trace tool calls, and limit resource use, but these facilities often assign different identities to execution, governance, and replay. We present Pollard, a framework-independent runtime based on governed semantic execution trees. A step…

- **[Phantom Merge: When Your Large Language Model Agents Pick One but Tell You About Another](https://arxiv.org/abs/2610.16141v1)**
  - *Wangshu Zhu, Qianwen Guo, Yushun Dong*
  - `2026-10-12`
  - LLM agents increasingly operate over multiple entities, where reliable response generation requires not only retrieving relevant evidence but also preserving its association with the correct entity. We identify Phantom Merge (PM), an entity-evidence binding failure in which an ag…

- **[Large Language Model Assisted Transportation Planning through a Differentiable User Equilibrium Layer](https://arxiv.org/abs/2610.16140v1)**
  - *Eunseung Lee, Gyeongjun Kim, Keemin Sohn*
  - `2026-10-12`
  - Transportation planning has traditionally required substantial expertise in network modeling, traffic assignment, and optimization. As a result, strategic analyses such as network design, capacity expansion, and model calibration remain inaccessible to non-expert decision makers.…

- **[PID-Gated Continual Prompt Adaptation Under Noisy Feedback](https://arxiv.org/abs/2610.16129v1)**
  - *Zhentao Xu*
  - `2026-10-12`
  - Deploying LLM agents in non-stationary environments requires continually revising their instructions as the task drifts, yet rewriting after every reported mistake can turn noisy feedback into persistent errors. This raises an often-overlooked scheduling question in prompt adapta…

- **[Imitation Holds a Key to Evolution: Localized Repair and Verified Skill Acquisition for Adaptive Agents](https://arxiv.org/abs/2610.16125v1)**
  - *Kai Hu, Hua Huang*
  - `2026-10-12`
  - An agent can retain successful trajectories without learning which part of an experience should repair a new discrepancy. We formulate passive imitation (PI) as an architectural loop that localizes a violated contract, extracts a local goal, proposes an effect-matched skill, test…

- **[Beyond Perfect Teammates: Multi-Agent Collaboration with Unreliable Colleagues](https://arxiv.org/abs/2610.16117v1)**
  - *Chen Huang, Yiyang Zhang, Yuhao Wu et al.*
  - `2026-10-12`
  - LLM-based multi-agent collaboration is increasingly used to solve complex tasks by dividing work among specialized agents and integrating complementary expertise. Yet existing systems and evaluations largely rest on an implicit perfect-colleague assumption: collaborators provide…

- **[GUIDE: Computationally Augmented Consensus for Trustworthy Clinical Practice Guidelines](https://arxiv.org/abs/2610.16108v1)**
  - *Yuanfan Lin, Jie Di, Xujin He et al.*
  - `2026-10-12`
  - Maintaining up-to-date clinical practice guidelines (CPGs) is essential for evidence-based medicine, but rapid evidence growth and complex expert consensus formation limit timely updates. We developed GUIDE, a multi-agent copilot system for human-AI collaborative guideline genera…

- **[Heterogeneous Agentic Coevolution](https://arxiv.org/abs/2610.16078v1)**
  - *Wenqian Ye, Ziwei Guan, Zi Yang et al.*
  - `2026-10-12`
  - Recent advances in self-improving LLM agents have demonstrated the potential of AI systems that drive their own intelligence. However, many domain-specific applications rely on specialized foundation models that possess strong domain expertise but remain dependent on human-design…

- **[Dream2Discern: Learning from Hard Latent Variants for Runtime Failure Prediction in Multi-Agent Systems](https://arxiv.org/abs/2610.16071v1)**
  - *Boxuan Zhang, jianing Zhu, Xiaotian Han et al.*
  - `2026-10-12`
  - Reliable deployment of LLM-based multi-agent systems calls for runtime auditors that predict terminal outcomes from observed execution prefixes. These auditors typically learn from a limited corpus of trajectories with verified outcomes. Expanding this corpus requires costly exec…

- **[Understanding and Reducing Misalignment in Persuasion Optimization](https://arxiv.org/abs/2610.16070v1)**
  - *Boyi Wei, Ruta Desai, Peter Henderson et al.*
  - `2026-10-12`
  - Frontier models are now trained for complex multi-agent tasks, from running a company to engaging in negotiations. These tasks necessitate training models to be persuasive. But what does this optimization pressure mean for model alignment? In this work, we study how reinforcement…

- **[When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems](https://arxiv.org/abs/2610.16039v1)**
  - *Sunday Oyinlola Ogundoyin, Muhammad Ikram*
  - `2026-10-12`
  - Multi-agent LLM systems (MALS) introduce a privacy-leakage problem that conventional sensitivity-based defenses miss, since information disclosed to one authorized agent can propagate through routine coordination to an unauthorized one, without compromise or malicious behavior. T…

- **[Of Errors and Echoes: Responsibility-Aware Credit Assignment for Tool-Use Agents](https://arxiv.org/abs/2610.16027v1)**
  - *Xingjian Diao, Tianyu Yang, Wenjun Huang et al.*
  - `2026-10-12`
  - Reinforcement learning improves tool-use agents, yet fine-grained credit assignment remains challenging even with step-level feedback. An observed error may be inherited from an earlier decision, while multiple responsible decisions may share the same downstream consequence or pa…

- **[Computational Reflective Equilibrium for Agentic AI: A Rawlsian Alignment Scaffold for Governance](https://arxiv.org/abs/2610.16015v1)**
  - *Quanyan Zhu*
  - `2026-10-12`
  - The rapid deployment of agentic AI has introduced complex challenges for the ethics and governance of AI systems. Agents built on large language models act through tools on behalf of people, and each deployment case brings its own instructions, policies, evidence, and stakeholder…

- **[BrowseSafe++: Benchmarking Prompt Injection Detection Across Web Contexts, Languages, and Browser Views](https://arxiv.org/abs/2610.17457v1)**
  - *Yuetian Chen, Kaiyuan Zhang, Yuntao Du et al.*
  - `2026-10-12`
  - Browser agents need to make decisions and execute actions on behalf of users while consuming untrusted webpages, creating opportunities for malicious instructions embedded in webpages to redirect legitimate tasks. We introduce BrowseSafe++, which extends BrowseSafe from 14,719 pa…

- **[Position: Beyond Training Time, Test-Time Coordination is Essential for Cooperative MARL](https://arxiv.org/abs/2610.17409v1)**
  - *Dongsu Lee, Sooraj Sathish, Joonkyung Kim et al.*
  - `2026-10-12`
  - We argue that cooperative multi-agent reinforcement learning (MARL) should treat test-time coordination as part of the problem definition rather than a deployment artifact. Our focus is on long-horizon, centrally monitored cooperative systems such as warehouse robotics, automated…

- **[CodeLift: Your Test Suite Is Secretly a Dense SWE Curriculum](https://arxiv.org/abs/2610.17224v1)**
  - *Junjielong Xu, Huachao Zhu, Alyssa Wu et al.*
  - `2026-10-12`
  - The pass-all-test binary reward has become a standard recipe for training software engineering agents, but its sparsity eliminates difference of partially correct patches. The test pass-rate is a natural alternative. However, we find that it is not a reliable indicator of patch q…

- **[Density-Matrix Reinforcement Learning](https://arxiv.org/abs/2610.17214v1)**
  - *Chiuman Ho*
  - `2026-10-12`
  - What information does a reinforcement learning policy omit? At each state, a standard policy stores one probability per action. It has no place to record how actions relate to each other, such as which pairs go together and which conflict. We ask when this missing structure matte…

- **[FunDM: Cheap & Label-Free Decision Models from Frozen Language Models](https://arxiv.org/abs/2610.17175v1)**
  - *Ujjawal K. Panchal*
  - `2026-10-12`
  - Decision models such as Jev score candidate answers or actions. A small decision head trained label-free can recover about 99% of a frozen language model's multiple-choice accuracy while using only two-thirds of its transformer layers. It learns the full model's answer probabilit…

- **[OpenDGO: Benchmarking Multi-Agent Organizations Across Diverse Application Domains](https://arxiv.org/abs/2610.17143v1)**
  - *Xunkai Li, Miao Zhang, Zekai Chen et al.*
  - `2026-10-12`
  - Large language model (LLM)-based multi-agent systems are increasingly applied across diverse domains, yet different applications require different forms of agent organization. Existing studies typically adopt predefined organizations, such as Star, Chain, and Tree, or learn commu…

- **[MENTOR: Procedural Shielding of Tool-Using LLM Agents](https://arxiv.org/abs/2610.17039v1)**
  - *Ashwani Anand, Ivi Chatzi, Ritam Raha et al.*
  - `2026-10-12`
  - Tool-using LLM agents are increasingly used to automate workflows governed by procedural manuals, such as company rules for booking travel or procuring hardware. These manuals are written in natural language for humans and describe general requirements over such complex workflows…

- **[Multi-Agent Deferred-Decision Trajectory Optimization with Anytime-Valid Target Retention for Moving Candidates](https://arxiv.org/abs/2610.17003v1)**
  - *Farbod Siahkali, Mengxue Hou, Vijay Gupta*
  - `2026-10-12`
  - We study multi-agent terminal interception when one of several moving candidates is the unknown target and both target identity and candidate terminal locations are uncertain. We develop a receding-horizon deferred-decision trajectory optimization (DDTO) controller that combines…

- **[Learning to Design SR Solvers: Harness Optimization for Symbolic Regression](https://arxiv.org/abs/2610.16966v1)**
  - *Qian Li, Yuxiao Hu, Qihao Duan et al.*
  - `2026-10-12`
  - Symbolic regression (SR) seeks explicit equations that explain observed data, and recent methods increasingly employ large language models (LLMs) and agents for equation discovery. However, these systems typically rely on manually designed workflows and prompts. We argue that the…

- **[DiTSG: Context-Aware Air Traffic Scene Generation with Multi-Agent Diffusion Transformers](https://arxiv.org/abs/2610.16959v1)**
  - *Seokbin Yoon, Kyungmin Kim, Taejung Kwon et al.*
  - `2026-10-12`
  - Understanding how many aircraft, and which traffic configurations, can be safely and efficiently managed by air traffic controllers within a given airspace is fundamental to air traffic management. Air traffic controllers continuously modify aircraft trajectories through interven…

- **[ML Engineering Agents - A Data Management Perspective](https://arxiv.org/abs/2610.16919v1)**
  - *Arnab Phani, Elias Strauss, Tim Schuster et al.*
  - `2026-10-12`
  - Machine learning engineering (MLE) agents are emerging as a new paradigm for automating end-to-end ML pipeline development. Using large language models for code generation and predictive performance as a machine-gradable feedback signal, these agents iteratively synthesize, execu…

- **[Learn from Move: the Next Step for GUI Agents](https://arxiv.org/abs/2610.16720v1)**
  - *Jiahao Lu, Yize Shen, Chuanyuan Tan et al.*
  - `2026-10-12`
  - Existing benchmarks for GUI agents primarily focus on increasing task difficulty by extending task horizons. Besides, enabling agents to explore unfamiliar environments and successfully complete tasks within them is also a critical yet challenging problem. We introduce LatentGUIW…

- **[Prorsa: Unleashing the Potential of Prefill-Decode Disaggregation in Agentic Reinforcement Learning](https://arxiv.org/abs/2610.16592v1)**
  - *Chiheng Lou, Xiangwei Deng, Bangjun Xiao et al.*
  - `2026-10-12`
  - Agentic reinforcement learning (RL) is commonly used to enhance the capabilities of large language models (LLMs) in solving complex multi-turn tasks. During rollout, agentic RL exhibits a workload pattern distinct from that of traditional RL: multi-turn interactions repeatedly in…

- **[Learning Graded Sparse Mechanisms: A Representation Theorem and Certified Generalization](https://arxiv.org/abs/2610.16537v1)**
  - *Mark Kozdoba, Shie Mannor*
  - `2026-10-12`
  - In a variety of multi-agent and physical environments, an element's update depends strongly on a few other elements and weakly on many, and both the identity and the number of the elements that matter change with the state of the system. Such graded sparse mechanisms are common,…

- **[A Production-Grade, High-Efficiency Agentic RL Framework for Frontier LLMs with Validated Recipes](https://arxiv.org/abs/2610.16352v1)**
  - *LoonSage Team, Bowei Song, Caiwei Zhao et al.*
  - `2026-10-12`
  - Reinforcement learning (RL) has emerged as a critical phase in the post-training pipeline of large language models (LLMs). As the frontier of LLM capabilities shifts from static reasoning to agentic tasks--characterized by external tool invocation, multi-turn interactions, and lo…

- **[Think Before You Speak: Enabling Training-Free Latent Communication Between Language Models](https://arxiv.org/abs/2610.16165v1)**
  - *Rishi Khare*
  - `2026-10-12`
  - Large language models (LLMs) have demonstrated remarkable capabilities in solving complex tasks in coding, mathematical logic, and iterative reasoning, especially by coordinating effectively within multi-agent systems (MAS). However, language agents traditionally communicate via…

- **[Scaling Inference-Time Compute with Teams of Coding Agents](https://arxiv.org/abs/2610.17471v1)**
  - *Keenan Samway, Daniel D'souza, Omar Darwiche Domingues et al.*
  - `2026-10-12`
  - Multi-agent systems promise a new axis for scaling inference: rather than having one agent think longer or sample more attempts, a task is split across many agents that work in parallel and coordinate. However, in practice, more agents can easily produce duplicate work, coordinat…

- **[UMCR: Universal Medical Concept Recognition through Guideline Integration and Agentic Linking](https://arxiv.org/abs/2610.17363v1)**
  - *Fabrice Lamarche, Amal Zouaq*
  - `2026-10-12`
  - Medical Concept Recognition is the task of extracting and grounding spans in medical text to entries in a standard ontology. Current methods are generally developed towards a single ontology and source text type (clinical notes, drug labels, etc.) The central challenge is therefo…

- **[The Curse of Knowledge in Role-Playing Language Models](https://arxiv.org/abs/2610.17327v1)**
  - *Xiao Zhang*
  - `2026-10-12`
  - Role-playing language models speak as characters in games and agent simulations, where the system records what each character can hear, see and understand. We test whether characters respect these boundaries in 480 scenes, each with a counterfactual twin that changes only the hid…

- **[Welcome to the Age of Agent Ads: Using On-Policy Attacks to Steer Agentic Decisions](https://arxiv.org/abs/2610.17195v1)**
  - *Tim R. Davidson, Marija Šakota, Joshua Joseph et al.*
  - `2026-10-12`
  - People increasingly delegate option-ranking tasks (e.g., shopping, job search, travel) to AI agents, which creates incentives to steer agentic decisions via "agent ads." To defend against such steering attacks, people count on models' alignment training and platforms' terms of se…

- **[DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck](https://arxiv.org/abs/2610.17184v1)**
  - *Shubham Agarwal, Akshat Gupta, Mike Heddes et al.*
  - `2026-10-12`
  - Evaluation has been central to advances in AI, and it is equally critical to autonomous discovery. Yet scaling autonomous discovery to real-world engineering challenges faces a fundamental bottleneck: the cost of evaluating progress. In real settings, a single true evaluation, su…

- **[SpecGuardBench: Can Coding Agents Construct Reliable Validation Harnesses from Natural Language Specifications?](https://arxiv.org/abs/2610.16870v1)**
  - *Zhiqing Zhong, Mingyu Chen, Aoyang Fang et al.*
  - `2026-10-12`
  - As coding agents become more capable, tests remain the primary evidence for judging whether their code is correct. Yet passing available tests does not establish that an implementation satisfies its natural language specification. Reliable validation requires checks that faithful…

- **[ANCHOR: Assessing Naturalistic Constraint Hierarchies and Ordering in Repository-Grounded Agentic Coding](https://arxiv.org/abs/2610.16859v1)**
  - *Wenqiang Zhu, Xinping Lei, Zhiyi Lai et al.*
  - `2026-10-12`
  - For repository-grounded coding agents, a functionally correct patch is not necessarily an acceptable one: developers also constrain how the task must be carried out-modification scope, workflow order, validation, tool use, and reporting. This capability, which we call engineering…

- **[The interpreter as developer: An autoethnographic design study of building a computer-assisted interpreting tool through human-LLM co-creation](https://arxiv.org/abs/2610.16460v1)**
  - *Zeming Zhao*
  - `2026-10-12`
  - Real-time AI captioning now serves audiences at multilingual events, yet computer-assisted interpreting (CAI) tools are still built for interpreters, rarely by them. This article reports an autoethnographic design study in which a professional interpreter with no programming trai…

- **[CivWorldBench: Evaluating Language World Models in Structured Multi-Agent Sandbox Worlds](https://arxiv.org/abs/2610.16450v1)**
  - *Ang Li, Haofei Yu, Zhengwei Tao et al.*
  - `2026-10-12`
  - The growing use of language models for forecasting motivates a broader evaluation of their world-model capabilities. Such evaluation must go beyond predictive accuracy to assess hidden-state inference and intervention prediction. Real-world forecasting benchmarks offer limited ac…

- **[RelLedger: Relational Information Governance for LLM Agent Organizations](https://arxiv.org/abs/2610.16281v1)**
  - *Junxi Huang, Wenshuo Chen, Nuoxuan Li et al.*
  - `2026-10-12`
  - In LLM agent organizations, shared records determine which facts are available for later decisions. A sender consults interaction histories before deciding whether to report an event. A delivery gap across histories does not show whose relationship drove the choice or whether the…

- **[Scaling Multi-Agent Intelligence with Substrate-Centric Coordination](https://arxiv.org/abs/2610.16120v1)**
  - *Zhenting Qi, Zhuokai Zhao, Rulin Shao et al.*
  - `2026-10-12`
  - Existing large language model (LLM) based multi-agent systems have been shown to scale poorly, and we identify three problems: reading burden that grows with the group, useful information diluted by shared work of unknown quality, and fragility to failed agents. We argue that the…

- **[Origin Attribution for Unsafe Behavior in Self-Evolving Multi-Agent Coding Systems](https://arxiv.org/abs/2610.17488v1)**
  - *Hanyi Yu, Jiaming Cui*
  - `2026-10-12`
  - As language-model-based coding agents evolve their programs and reuse code from one another, safety failures can acquire a history that extends beyond the agent in which they are detected. An unsafe change may originate in one agent, propagate through intermediate recipients, and…

- **[AgentCue: Statistical Summaries for Guiding Decentralized Multi-Agent Self-Organization](https://arxiv.org/abs/2610.16621v1)**
  - *Guojun Zhu, Xinyou Chen, Kejian Zhang et al.*
  - `2026-10-12`
  - Multi-agent systems (MAS) combine multiple agents to solve complex tasks, and recent MAS scale to more than a thousand agents. At this scale, decentralized MAS remove the central orchestrator that assigns sub-tasks, and the agents, which we call workers, self-organize through the…

- **[Transparent Information Flow Modeling for Role-Aware AI Act Assessment](https://arxiv.org/abs/2610.16916v1)**
  - *Mattias Brännström, Themis Dimitra Xanthopoulou, Lili Jiang*
  - `2026-10-12`
  - The European Union's Artificial Intelligence Act introduces a structured framework for governing high-risk AI systems, emphasizing transparency, risk management, and role-specific accountability. However, current assessment practices often rely on monolithic system views or disco…

- **[Large language model-generated patterns for epidemiological modeling: a multi-benchmark evaluation framework](https://arxiv.org/abs/2610.15994v1)**
  - *Sophia Mao, Keshav Gandhi, Alexander Gutfraind*
  - `2026-10-11`
  - Representing individual-level behavioral heterogeneity is challenging in epidemiological modeling, particularly when empirical behavioral data are sparse. We assess the potential of large language model (LLM)-generated behavioral outputs in addressing this challenge, using hepati…

- **[Revocation Is Not Complete at Receipt: An Executable Outcome Contract for Distributed Agent-Tool Gateways](https://arxiv.org/abs/2610.15991v1)**
  - *Lifei Liu, Haoran Yu, Danping Zhang*
  - `2026-10-11`
  - Distributed agent workflows cache delegated authority at tool gateways. Revocation may be reported at issuer commit, transport acknowledgment, or receiver persistence, although none of these observations establishes that all gateways enforced the change or that guarded effects st…

- **[Embedding Information in Policy Randomness: Distribution-Preserving Implicit Communication in MDPs](https://arxiv.org/abs/2610.15976v1)**
  - *Gongpu Chen, Deniz Gündüz*
  - `2026-10-11`
  - This paper investigates a new role of randomness in stochastic policies--as a medium for embedding and communicating information. Specifically, we consider an agent interacting with an environment according to a prescribed stochastic policy. By carefully modulating the random act…

- **[PopGen: Generating Semantically Diverse Populations for Zero-Shot Coordination](https://arxiv.org/abs/2610.15969v1)**
  - *Paul Teiletche, Kanghyun Ryu, Kyungjoon Park et al.*
  - `2026-10-11`
  - In multi-agent reinforcement learning, exposing a cooperator to partners with diverse strategies during training is key to better collaboration at test time. However, existing methods typically rely on trajectory-level proxies to measure diversity, which may label two distinct tr…

- **[Small but Mighty: Test Suites as Improvement Signals for Self-Evolving Agents](https://arxiv.org/abs/2610.15964v1)**
  - *Yutong Cheng, Wei Cheng, Wenchao Yu et al.*
  - `2026-10-11`
  - A self-evolving agent rewrites its own harness and must decide which rewrites to keep, so its improvement signal is the check a rewrite has to pass. Verifying a rewrite by agent rollout is expensive and subjective, while executable checks such as the repository's own tests are to…

- **[Unfair and Unsafe: Everyday Bias Triggers Emergent Misalignment](https://arxiv.org/abs/2610.15961v1)**
  - *Alex Martí Guiu, Nicolas Zumarraga, Kevin O'Sullivan et al.*
  - `2026-10-11`
  - Emergent misalignment (EM) occurs when fine-tuning a language model to a narrow task makes it misaligned on unrelated ones. Because organizations now routinely fine-tune models on their own data, it matters which kinds of training data cause EM. So far, studies have induced EM wi…

- **[Scalable Weak-to-Strong Verifier Hardening for Agent Environments](https://arxiv.org/abs/2610.15924v1)**
  - *Chong Zeng, Ziqian Zhong, Kexun Zhang et al.*
  - `2026-10-11`
  - Agent environments are essential for large language model (LLM) development. They use programmatic verifiers to turn complex outcomes into rewards. Verifiers can be attacked into awarding full credit to cheating agents without completing the intended task, causing inaccurate eval…

- **[Variance-Optimal State Resampling for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2610.15888v1)**
  - *Yibo Wang, Yuanxin Liu, Zhaoran Wang*
  - `2026-10-11`
  - Reinforcement learning with verifiable rewards spends much of its rollout budget on states that yield no learning signal. We recast this as a question about the sampling distribution itself: under a fixed rollout budget, which distribution over states minimizes the variance of th…

- **[RetryBench: Separating Retry Permission from Recovery Outcomes in GPT Tool Use](https://arxiv.org/abs/2610.15884v1)**
  - *You Liu, Yue Liu, Quanchao Lu*
  - `2026-10-11`
  - False retry permission (FRP) occurs when an agent retries a timed-out tool call without support from the visible contract. RetryBench separates this error from realized recovery. Successful protected recovery does not imply reliable rejection of unsupported retries. In a 720-resp…

- **[LLM Value Functions for Credit Assignment in Agentic RL](https://arxiv.org/abs/2610.15840v1)**
  - *Kaijie Zhu, Weixiang Yan, Omar Attia et al.*
  - `2026-10-11`
  - Reinforcement learning (RL) for large language model (LLM) agents remains challenging in long-horizon tasks with sparse outcome rewards, where assigning credit to individual actions is difficult. Methods such as GRPO assign the same trajectory-level advantage to all actions, whil…

- **[Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams](https://arxiv.org/abs/2610.15788v1)**
  - *Yirui Qi, Xiaoming Zhang, Jaehong Yoon*
  - `2026-10-11`
  - Large language model (LLM) agents are increasingly deployed as teams, yet they fail in characteristically social ways: information holders stay silent, dominant speakers anchor groups on wrong answers, and norm violations go unsanctioned. We present Agent Sociodrama, a framework…

- **[SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation](https://arxiv.org/abs/2610.15766v1)**
  - *Angen Ye, junjie xie, Yujia Song et al.*
  - `2026-10-11`
  - Recent multimodal large language models (MLLMs) and vision--language--action models have provided robots with new capabilities for long-horizon task understanding and planning. In surgical robotics, however, end-to-end prediction of low-level actions remains limited by insufficie…

- **[Google Earth AI Geospatial Reasoning Agent: Capabilities and a Systematic Evaluation](https://arxiv.org/abs/2610.15750v1)**
  - *Noam Slonim, Aviv Slobodkin, Gil Fidel et al.*
  - `2026-10-11`
  - Google Earth AI is a family of geospatial AI models, together with an agent that orchestrates them. We present this agent, Google Earth AI's Geospatial Reasoning agent (GRA), a Gemini-powered research system that combines geospatial data sources, foundation models, and tools to a…

- **[Visible but Not Avoided: State-Dependent Re-Proposal of Rejected Candidates in Catalog-Based LLM Optimization Loops](https://arxiv.org/abs/2610.15738v1)**
  - *Jianlin Chen, Wenhui Chen, Chi Man Vong*
  - `2026-10-11`
  - LLM optimization loops often show the proposer the candidates it has already tried and rejected, but leave it to the proposer to avoid them. We ask whether avoidance measured in a static probe predicts avoidance in the states an optimizer's own trajectory produces. In catalog-bas…

- **[SkillMarker: A KGW-Based Watermarking Method for Agent Skill Ownership Verification](https://arxiv.org/abs/2610.15725v1)**
  - *Alan Tang, Lifeng Wang, Gang Wu et al.*
  - `2026-10-11`
  - Agent skills encode operational procedures and domain expertise as reusable knowledge assets, yet their distribution in plaintext exposes them to unauthorized copying and leakage. However, practical mechanisms for skill ownership verification and leakage tracing remain underdevel…

- **[MedHarnessBench: A Unified Benchmark for Healthcare Agent Evaluation](https://arxiv.org/abs/2610.15714v1)**
  - *Rui Tang, Hongqiu Wang*
  - `2026-10-11`
  - Healthcare agents must transform longitudinal clinical evidence into reliable actions through heterogeneous tools and stateful workflows, conditions under which model-centric systems may lose context, misuse tools, fail to verify consequential transitions, or cross authorization…

- **[SpecForge: Recursive Self-Improvement for Coding Agents via Behavioral Specifications](https://arxiv.org/abs/2610.15708v1)**
  - *Yutong Cheng, Haifeng Chen, Peng Gao et al.*
  - `2026-10-11`
  - Coding agents based on frozen language models can improve their performance by refining the external context they rely on, without updating model weights. We study recursive self-improvement through behavioral specifications: natural-language code documentation that describes the…

- **[FARL: A Fully Automated Pipeline of RL Interface and Solver Design](https://arxiv.org/abs/2610.15691v1)**
  - *Tianyu Jin, Liuyu Xiang, Chaowen Yang et al.*
  - `2026-10-11`
  - Existing reinforcement learning (RL) largely focuses on optimizing learning algorithms within a pre-defined task formulation, while applying RL to new tasks still relies heavily on human expertise to design the learning pipeline: what an agent observes, how it is rewarded, which…

- **[Dynamic Conflict Clustering with Lightweight Learning and Strategic Repair for Distributed Constraint Satisfaction](https://arxiv.org/abs/2610.15658v1)**
  - *Raziyeh Moghaddas, Fabio Caraffini*
  - `2026-10-11`
  - Distributed Constraint Satisfaction Problems (DCSPs) model distributed decision-making in multi-agent systems, where agents assign values to local variables while satisfying shared constraints. However, many DCSP solvers still rely on broad, repeated peer-to-peer communication an…

- **[Recall What Is Missing: Composing Evidence from Long-Term Agent Memory](https://arxiv.org/abs/2610.15642v1)**
  - *Qi Feng, Jicong Fan*
  - `2026-10-11`
  - Under a limited context budget, a long-term agent must recall not merely memories that are individually relevant, but evidence that is collectively sufficient for the current query. Conventional memory access retrieves, scores, and truncates memories, often spending multiple cont…

- **[Inverse Garment Design with Visual Agents](https://arxiv.org/abs/2610.15582v1)**
  - *Nanxiang Jiang, Yunuo Chen, Zeng Tao et al.*
  - `2026-10-11`
  - We study the problem of inverse garment design, reconstructing simulation-ready 3D outfits with arbitrary layers from a single image, with visual agents. Unlike differentiable optimization that is time-consuming, or feed-forward methods limited by training data, we introduce Dres…

- **[Agent-Canary-Mas: End-to-End Evaluation of Protocol Risk in Long-Horizon Multi-Agent Systems](https://arxiv.org/abs/2610.15529v1)**
  - *Xiuming Liu, Le Gai, Zhiyuan Chang et al.*
  - `2026-10-11`
  - Agent-to-agent protocols allow LLM agents to discover peers, exchange results, and coordinate tool use. A locally successful protocol attack, however, may be rejected by a later agent or propagated into a consequential task decision. Measuring local exploitability alone leaves th…

- **[Improving the Bounds on Approximating Weighted Maximin Share for Chores](https://arxiv.org/abs/2610.15520v1)**
  - *Trung Thanh Nguyen, Khaled Elbassioni, Jörg Rothe*
  - `2026-10-11`
  - We investigate the problem of allocating indivisible chores among agents with arbitrary positive weights and additive nonnegative cost functions. An allocation is said to be $α$-weighted-maximin-share (WMMS) fair if the cost incurred by each agent is at most $α$ times her weighte…

- **[When Skills Remain But Access Fails: Factorized Skill Memory for Continual Skill Internalization](https://arxiv.org/abs/2610.15492v1)**
  - *Haomiao Qiu, Yining Tang, Hongyi Wan et al.*
  - `2026-10-11`
  - Skill internalization aims to convert externally specified procedural skills into persistent model capabilities, allowing language-model agents to execute them without retrieving or reinjecting skill descriptions at inference time. Yet when new skills are learned continually, whe…

- **[When Messages Go Wrong: Understanding Communication Faults in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2610.15459v1)**
  - *Jinhao Zhou, Xiaoyu Zhang, Jiongchi Yu et al.*
  - `2026-10-11`
  - LLM-based multi-agent systems (LLM-MAS) use specialized agents that exchange messages to accomplish complex tasks. Their reliance on networked protocols, remote tools, and model endpoints exposes communication to message loss, delay, and context expiration. Because agents often e…

- **[Sensitivity or Criterion? Measuring and Moving When Language Models Act](https://arxiv.org/abs/2610.15415v1)**
  - *Sixun Dong, Yebowen Hu, Ming Yin et al.*
  - `2026-10-11`
  - Before an agent acts, it must decide whether action is warranted. A single accuracy cannot distinguish failure to recognize a warranted action from reluctance to act. Signal-detection theory separates sensitivity from criterion, but criteria estimated from authored binary labels…

- **[CoverSynth: Coverage-Guided Generation of Retrieval Evaluation Sets](https://arxiv.org/abs/2610.15409v1)**
  - *Anahita Sharma, Apaar Shanker, Rishav Chakravarti et al.*
  - `2026-10-11`
  - Enterprise agents need retrieval evaluation sets that expose domain-specific failures and guide developers towards efficient deployment tradeoffs. Neither expert-human-authored sets nor current synthetic generation methods provide a methodology for achieving the necessary coverag…

- **[State Representation Shapes Long-Horizon Agent Learning and Transfer: An Empirical Study](https://arxiv.org/abs/2610.15407v1)**
  - *Dong Nie, Rui Lan, Yixin Nie et al.*
  - `2026-10-11`
  - An end-to-end success rate alone cannot distinguish failure to learn an action from failure to apply it as task state changes. We study this distinction in deterministic tool workflows that provide the current artifact state and candidate action recipes. Using 1.7B, 8B, and 27B Q…

- **[Analyzing the Dynamics of WSBM-based Echo State Networks using InputDSA](https://arxiv.org/abs/2610.15380v1)**
  - *Huy Mai, Robert Clarke*
  - `2026-10-11`
  - Bridging the structural gap between biological brains and artificial neural networks presents a pathway to altered computational dynamics. This paper introduces a Reservoir Computing framework that replaces random networks with biologically realistic modularity by applying the We…

- **[CHEAR: Confusion-Hierarchy Evidence-Aware Reasoning for Cost-Efficient Human Activity Recognition](https://arxiv.org/abs/2610.15298v1)**
  - *Xiangqing Lu, Tao Zhu, Mingxing Nie et al.*
  - `2026-10-11`
  - Large language models (LLMs) offer a new approach to wearable-sensor-based human activity recognition. Retrieval-augmented generation (RAG) further introduces similar motion examples and discriminative sensor knowledge, enabling decisions grounded in observations relevant to the…

- **[OntoAR-HAR: Ontology-Guided Agentic RAG with Personalized Memory for Human Activity Recognition](https://arxiv.org/abs/2610.15292v1)**
  - *Xiangqing Lu, Tao Zhu, Liang Yu et al.*
  - `2026-10-11`
  - LLMs increasingly support sensor-based human activity recognition (HAR) by linking motion signals with activity semantics and physical knowledge. Retrieval-augmented generation (RAG) grounds decisions in sensor examples and domain features, enabling training-free target-user infe…

- **[Sequent-Prover: Training Agents for Formal, Checkable SMT-based Reasoning](https://arxiv.org/abs/2610.15258v1)**
  - *Debargha Ganguly, Weicong Chen, Mohsen Hariri et al.*
  - `2026-10-11`
  - We introduce Sequent-Prover, a family of verifier-using language-model agents, and the post-training framework that produces them. Agents reason in an executable SMT-LIB scratchpad: they write complete SMT-LIB programs, query Z3 across turns, inspect solver feedback, repair forma…

- **[EvolvAttack: Backdooring self Evolving VLM Agents](https://arxiv.org/abs/2610.15244v1)**
  - *Chuan Zou, Yang Xiang, Zexin Li et al.*
  - `2026-10-11`
  - Self-evolving mechanisms let vision-language model (VLM) agents continually adapt through evolving memory, but they also allow malicious behavior to emerge only after deployment. We introduce a new attack surface, the self-evolving backdoor, whose payload stays dormant in the ini…

- **[Mobility Helps Learning: Unsupervised Model Adaptation for Object Recognition via Movement](https://arxiv.org/abs/2610.15846v1)**
  - *Yanan Ma, Yihang Tao, Zhengru Fang et al.*
  - `2026-10-11`
  - Movable agents, such as autonomous vehicles and robots, should be able to autonomously adapt their pre-trained object recognition models to new environments without human annotations. While existing test-time adaptation (TTA) methods address label-free model adaptation, they typi…

- **[Context-Aware Precision Scheduling for Small Language Models](https://arxiv.org/abs/2610.15640v1)**
  - *Mukund Athmaram, Manoj Rao, Liang Ma*
  - `2026-10-11`
  - Small language models (SLMs) used as on-device agents must balance accuracy and latency as their context grows. Mixed precision helps manage this tradeoff by assigning different precisions to weight tensors according to their size and sensitivity. However, these choices depend on…

- **[AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning](https://arxiv.org/abs/2610.15488v1)**
  - *Peiqi Jiang, Fan Zhang, Xin Xu et al.*
  - `2026-10-11`
  - Formulaic alpha mining seeks interpretable expressions that rank assets by future returns. The task is challenging because it demands simultaneous processing of unstructured market descriptions, historical data, and quantitative evaluation of candidate factors, yet most existing…

- **[From Acoustic Sensing to Physical Actions: A Comprehensive Survey of Security Risks in Edge-Deployed Audio LLM-Based Agents](https://arxiv.org/abs/2610.15390v1)**
  - *Binhong Wang, Haidong Kang, Yanfeng Zhang et al.*
  - `2026-10-11`
  - Audio Large Language Models (Audio LLMs) are embedded in agents for smart homes, vehicles, wearables, and embodied systems, where acoustic inputs can propagate from perception into persistent state and consequential execution. This setting extends security analysis beyond model b…

- **[ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs](https://arxiv.org/abs/2610.15368v1)**
  - *Yi Ge, Kangrui Ruan, Jifan Chen et al.*
  - `2026-10-11`
  - Rapid advances in large language models have made software engineering agents capable of tackling complex coding tasks. Within a containerized environment, a coding agent receives tool responses or execution results, and determines its later actions by those earlier results. Howe…

- **[CoLA: Multi-VLA Coordination via Learned Adapters](https://arxiv.org/abs/2610.15337v1)**
  - *Ahaskar Kashyap, Jiawen Zong, Boyu Ma et al.*
  - `2026-10-11`
  - Vision-Language-Action (VLA) models are typically deployed as isolated single-agent policies. When several such agents share a workspace, they can coordinate implicitly, by observing one another, or explicitly, by exchanging messages, but it remains unclear when explicit communic…

- **[ObsSpec: Accelerating Agentic Reinforcement Learning with Observation Speculation](https://arxiv.org/abs/2610.15246v1)**
  - *Kyle Montgomery, Wang Zhang, Chenguang Wang*
  - `2026-10-11`
  - Tool-using agents alternate between model generation and tool execution, waiting for each tool call to complete before starting the next generation. This sequential execution is costly during agentic reinforcement learning (RL), which requires large batches of multi-turn rollouts…

- **[More Reasoning Is Not Always Better: Executing Clinical Guidelines with LLMs and Rules](https://arxiv.org/abs/2610.15912v1)**
  - *Xiaoqian Lu, Guangfu Guo, Long Cheng et al.*
  - `2026-10-11`
  - Large language models (LLMs) have shown considerable promise in clinical decision support. However, existing approaches often rely on multi-step reasoning or multi-agent collaboration to execute clinical guidelines, introducing substantial computational overhead without reliably…

- **[RIVO: Lightweight Adaptive Rerouting for Deep Research Agents](https://arxiv.org/abs/2610.15910v1)**
  - *Mingchen Li, Jiatan Huang, Hong Yu*
  - `2026-10-11`
  - Deep Research agents rely on long-horizon reasoning and iterative tool use to solve complex information-seeking tasks. However, adaptive decision-making over these trajectories remains challenging, as agents may stop prematurely when further evidence is needed, continue unnecessa…

- **[RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution](https://arxiv.org/abs/2610.15772v1)**
  - *Fan Zhang, Hao Wu, Jinyang Wu et al.*
  - `2026-10-11`
  - Recent focus in agentic reinforcement learning (RL) seeks to improve credit assignment in long-horizon tasks. One promising direction combines reinforcement learning with verifiable rewards (RLVR) and on-policy self-distillation (OPSD), integrating trajectory-level advantages wit…

- **[Towards Autopilot Labeling for Short Video Content Governance](https://arxiv.org/abs/2610.15687v1)**
  - *Junwen Chen, Hongwei Wang, Zixuan Wang et al.*
  - `2026-10-11`
  - The explosive growth of short videos has presented significant challenges to content governance. Traditional manual labeling is inefficient, slow to iterate, and costly. Therefore, we explore and develop a multi-stage autopilot labeling framework aimed at progressively increasing…

- **[A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding](https://arxiv.org/abs/2610.15666v1)**
  - *Abdollah Pourasghari, Saeedeh Sadat Sadidpour, Mohammad Roustaei*
  - `2026-10-11`
  - Converting natural-language instructions into executable action plans conditioned on a scene image is a core capability for embodied human-robot interaction, but existing benchmarks target English, simulated or video-grounded environments, and largely assume instructions are clea…

- **[Mind Your Own Role: Reducing Role Overstepping for Effective and Efficient Multi-Agent Collaboration via Dynamic Role Activation Steering](https://arxiv.org/abs/2610.15907v1)**
  - *Xingke Yang, Sicong Li, Lingfeng Yao et al.*
  - `2026-10-11`
  - Multi-Agent Systems (MAS) have shown strong capability in solving complex tasks by assigning different agents specialized roles and corresponding subtasks. However, agents may overstep their assigned responsibilities and perform subtasks belonging to other roles, which can disrup…

- **[Representation Theorems for Actual Powers over Two-Agent General Concurrent Game Frames](https://arxiv.org/abs/2610.15476v1)**
  - *Zixuan Chen, Fengkui Ju, Thomas Ågotnes*
  - `2026-10-11`
  - One of the most well-known connections between logic and games is Pauly's representation theorem: the induced powers of individuals and coalitions in concurrent game frames correspond, in a precise sense, to a certain class of neighborhood frames. The precise sense here is what i…

- **[Do Rollups Self-Organize? Multi-Agent Reinforcement Learning in the EIP-4844 Blob Fee Market](https://arxiv.org/abs/2610.15256v1)**
  - *Alessio Brini*
  - `2026-10-11`
  - EIP-4844 gave Ethereum rollups a separate fee dimension for data, governed by a multiplicative update rule that targets three ``blobs'' per block. Whether this target is reached depends on how many independent, self-interested rollups choose to post data, a question that closed-f…

- **[A Sovereign, Indic-First, Reasoning Model](https://arxiv.org/abs/2610.15371v1)**
  - *Sutanshu Saksena Raj, Prasanjith Pasunuti, Parijat Chatterjee et al.*
  - `2026-10-11`
  - Gnani-Evon-v3.3-30B-A3B is a long-context hybrid Mamba-Transformer mixture-of-experts model for reasoning, instruction following, and tool use in English and eight Indian languages. Starting from NVIDIA's Nemotron-3-Nano-30B-A3B checkpoint, it retains the 52-layer backbone and ch…

- **[JSIR: An Audio-Aligned, Multi-Task Dataset of Jazz Standard Recordings](https://arxiv.org/abs/2610.15356v1)**
  - *Sihun Lee, Dasaem Jeong*
  - `2026-10-11`
  - Beat tracking, chord estimation, and structure analysis are staple tasks of music information retrieval. Their datasets are drawn largely from Western popular music, and jazz remains a repertoire on which state-of-the-art systems underperform. We present JSIR, the Jazz Standards…


## Harness  (144)

### AAAI

- **[GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Through Code Repository Leveraging](https://arxiv.org/abs/2508.18993)**
  - *Zi-Yi Ni, Hua-Can Wang, Shuo Zhang et al.*
  - **AAAI 2025** · `2025-08-26`
  - Beyond scratch coding, exploiting large-scale code repositories (e.g., GitHub) for practical tasks is vital in real-world software development, yet current benchmarks rarely evaluate code agents in such authentic, workflow-driven scenarios. 
To bridge this gap, we introduce GitTa…


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

- **[AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents](https://arxiv.org/abs/2506.00641)**
  - *Han-Jun Luo, Shenyu Dai, Chiming Ni et al.*
  - **NeurIPS 2025** · `2025-05-31`
  - Despite the rapid advancement of LLM-based agents, the reliable evaluation of their safety and security remains a significant challenge. Existing rule-based or LLM-based evaluators often miss dangers in agents'step-by-step actions, overlook subtle meanings, fail to see how small…

- **[ThinkBench: Dynamic Out-of-Distribution Evaluation for Robust LLM Reasoning](https://arxiv.org/abs/2502.16268)**
  - *Shu-Lin Huang, Linyi Yang, Yan Song et al.*
  - **NeurIPS 2025** · `2025-02-22`
  - Evaluating large language models (LLMs) poses significant challenges, particularly due to issues of data contamination and the leakage of correct answers. To address these challenges, we introduce ThinkBench, a novel evaluation framework designed to evaluate LLMs' reasoning capab…


### ICML

- **[Harness Self-Evolution: Theory, Algorithms, Evaluation, Applications, and Impact](https://openreview.net/forum?id=m5jsFGXUM2)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - **ICML 2025** · OpenReview · `2026-10-11`
  - Building agents that learn from experience is a central goal of artificial intelligence. Harness self-evolution offers a path toward this goal by revising an agent’s instructions, memory, workflows, and tools while model weights stay fixed. In this article, we develop a unified f…

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
  - *{'fullname': 'Dongjun Kim', 'username': ''}, {'fullname': 'Gyuho Shim', 'username': ''}, {'fullname': 'Yongchan Chun', 'username': '~Yongchan_Chun1'} et al.*
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

- **[am-ELO: A Stable Framework for Arena-based LLM Evaluation](https://arxiv.org/abs/2505.03475)**
  - *Zi-Rui Liu, Jia-Tong Li, Yan Zhuang et al.*
  - **ICML 2025** · `2025-05-06`
  - Arena-based evaluation is a fundamental yet significant evaluation paradigm for modern AI models, especially large language models (LLMs). Existing framework based on ELO rating system suffers from the inevitable instability problem due to ranking inconsistency and the lack of at…

- **[Accelerating Unbiased LLM Evaluation via Synthetic Feedback](https://arxiv.org/abs/2502.10563)**
  - *Zhaoyi Zhou, Yu-Da Song, Andrea Zanette*
  - **ICML 2025** · `2025-02-14`
  - When developing new large language models (LLMs), a key step is evaluating their final performance, often by computing the win-rate against a reference model based on external feedback. Human feedback is the gold standard, particularly for capturing nuanced qualities like coheren…

- **[Copilot Arena: A Platform for Code LLM Evaluation in the Wild](https://arxiv.org/abs/2502.09328)**
  - *Wayne Chi, Valerie Chen, A. Angelopoulos et al.*
  - **ICML 2025** · `2025-02-13`
  - Evaluating in-the-wild coding capabilities of large language models (LLMs) is a challenging endeavor with no clear solution. We introduce Copilot Arena, a platform to collect user preferences for code generation through native integration into a developer's working environment. C…


### ICLR

- **[RocketEval: Efficient Automated LLM Evaluation via Grading Checklist](https://arxiv.org/abs/2503.05142)**
  - *Tianjun Wei, Wei Wen, Rui-Zhi Qiao et al.*
  - **ICLR 2025** · `2025-03-07`
  - Evaluating large language models (LLMs) in diverse and challenging scenarios is essential to align them with human preferences. To mitigate the prohibitive costs associated with human evaluations, utilizing a powerful LLM as a judge has emerged as a favored approach. Nevertheless…

- **[Know Thy Judge: On the Robustness Meta-Evaluation of LLM Safety Judges](https://arxiv.org/abs/2503.04474)**
  - *Francisco Eiras, Eliott Zemour, Eric Lin et al.*
  - **ICLR 2025** · `2025-03-06`
  - Large Language Model (LLM) based judges form the underpinnings of key safety evaluation processes such as offline benchmarking, automated red-teaming, and online guardrailing. This widespread requirement raises the crucial question: can we trust the evaluations of these evaluator…


### KDD

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, A. Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…


### ACL

- **[When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark](https://arxiv.org/abs/2610.16067v1)**
  - *Junjie Chen*
  - **ACL** · `2026-10-12`
  - Agent evaluation harnesses are software systems that run test suites, generate inputs, and decide outcomes with test oracles. This paper audits such software for reliability defects that score tables cannot reveal.   We introduce an oracle-integrity auditing approach with five st…

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://arxiv.org/abs/2507.21028)**
  - *Jiaju Chen, Yuxuan Lu, Xiaojie Wang et al.*
  - **ACL 2025** · `2025-07-28`
  - Nearly all human work is collaborative; thus, the evaluation of real-world NLP applications often requires multiple dimensions that align with diverse human perspectives. As real human evaluator resources are often scarce and costly, the emerging"LLM-as-a-judge"paradigm sheds lig…

- **[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://arxiv.org/abs/2504.08725)**
  - *Dayu Yang, Antoine Simoulin, Xin Qian et al.*
  - **ACL 2025** · `2025-04-11`
  - High-quality code documentation is crucial for software development especially in the era of AI. However, generating it automatically using Large Language Models (LLMs) remains challenging, as existing approaches often produce incomplete, unhelpful, or factually incorrect outputs…

- **[Right Answer, Wrong Score: Uncovering the Inconsistencies of LLM Evaluation in Multiple-Choice Question Answering](https://arxiv.org/abs/2503.14996)**
  - *F. Molfese, Luca Moroni, Luca Gioffré et al.*
  - **ACL 2025** · `2025-03-19`
  - One of the most widely used tasks for evaluating Large Language Models (LLMs) is Multiple-Choice Question Answering (MCQA). While open-ended question answering tasks are more challenging to evaluate, MCQA tasks are, in principle, easier to assess, as the model's answer is thought…

- **[DOVE: A Large-Scale Multi-Dimensional Predictions Dataset Towards Meaningful LLM Evaluation](https://arxiv.org/abs/2503.01622)**
  - *Eliya Habba, Ofir Arviv, Itay Itzhak et al.*
  - **ACL 2025** · `2025-03-03`
  - Recent work found that LLMs are sensitive to a wide range of arbitrary prompt dimensions, including the type of delimiters, answer enumerators, instruction wording, and more. This throws into question popular single-prompt evaluation practices. We present DOVE (Dataset Of Variati…

- **[A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://arxiv.org/abs/2502.11211)**
  - *Wen-Xuan Wang, Zi-Zhan Ma, Zheng Wang et al.*
  - **ACL 2025** · `2025-02-16`
  - Large Language Models (LLMs) are transforming healthcare through the development of LLM-based agents that can understand, reason about, and assist with medical tasks. This survey provides a comprehensive review of LLM-based agents in medicine, examining their architectures, appli…

- **[SubLIME: Subset Selection via Rank Correlation Prediction for Data-Efficient LLM Evaluation](https://aclanthology.org/2025.acl-long.1477.pdf)**
  - *Gayathri Saranathan, Cong Xu, M. Alam et al.*
  - **ACL 2025**
  - The rapid expansion of Large Language Models (LLMs) and natural language processing datasets has made exhaustive benchmark evaluations computationally prohibitive. Inspired by high-stakes competitions like the International Mathematical Olympiad—where a few well-chosen problems s…

- **[Praetor: A Fine-Grained Generative LLM Evaluator with Instance-Level Customizable Evaluation Criteria](https://aclanthology.org/2025.acl-long.513.pdf)**
  - *Yongqi Leng, Ren-Ren Jin, Yue Chen et al.*
  - **ACL 2025**
  - With the increasing capability of large language models (LLMs), LLM-as-a-judge has emerged as a new evaluation paradigm. Compared with traditional automatic and manual evaluation, LLM evaluators exhibit better interpretability and efficiency. Despite this, existing LLM evaluators…


### EMNLP

- **[Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses](https://arxiv.org/abs/2509.16093)**
  - *Fangyi Yu, Nabeel Seedat, Dasha Herrmannova et al.*
  - **EMNLP 2025** · `2025-09-19`
  - Evaluating long-form answers in high-stakes domains such as law or medicine remains a fundamental challenge. Standard metrics like BLEU and ROUGE fail to capture semantic correctness, and current LLM-based evaluators often reduce nuanced aspects of answer quality into a single un…

- **[ReliableEval: A Recipe for Stochastic LLM Evaluation via Method of Moments](https://arxiv.org/abs/2505.22169)**
  - *G. Lior, Eliya Habba, Shahar Levy et al.*
  - **EMNLP 2025** · `2025-05-28`
  - LLMs are highly sensitive to prompt phrasing, yet standard benchmarks typically report performance using a single prompt, raising concerns about the reliability of such evaluations. In this work, we argue for a stochastic method of moments evaluation over the space of meaning-pre…

- **[Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews](https://arxiv.org/abs/2502.17086)**
  - *Hyungyu Shin, Jingyu Tang, Yoonjoo Lee et al.*
  - **EMNLP 2025** · `2025-02-24`
  - Peer review underpins scientific progress, but it is increasingly strained by reviewer shortages and growing workloads. Large Language Models (LLMs) can automatically draft reviews now, but determining whether LLM-generated reviews are trustworthy requires systematic evaluation.…

- **[ACEBench: A Comprehensive Evaluation of LLM Tool Usage](https://aclanthology.org/2025.findings-emnlp.697.pdf)**
  - *Chen Chen, Xin-Long Hao, Weiwen Liu et al.*
  - **EMNLP 2025**
  - Large Language Models (LLMs) have demonstrated significant potential in decision-making and reasoning, particularly when integrated with various tools to effectively solve complex problems. However, existing benchmarks for evaluating LLMs’ tool usage face several limitations: (1)…


### NAACL

- **[Advancing Persian LLM Evaluation](https://aclanthology.org/2025.findings-naacl.147.pdf)**
  - *Sara Bourbour Hosseinbeigi, Behnam Rohani, Mostafa Masoudi et al.*
  - **NAACL 2025**
  - Evaluation of large language models (LLMs) in low-resource languages like Persian has received less attention than in high-resource languages like English. Existing evaluation approaches for Persian LLMs generally lack comprehensive frameworks, limiting their ability to assess mo…


### Other / arXiv

- **[Agent-Reflex: Teaching Language Agents to Act Reflectively](https://arxiv.org/abs/2610.17953)**
  - *Guanting Dong, Xinyu Yang, Jiajie Jin et al.*
  - 🤗 Featured · `2026-10-13`
  - Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision…

- **[WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution](https://arxiv.org/abs/2610.18067)**
  - *Hang He, Linting Wang, Guanming Liu et al.*
  - 🤗 Featured · `2026-10-13`
  - Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and…

- **[LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity](https://arxiv.org/abs/2610.18092)**
  - *Yibo Wang, Senjie Jin, Yansong Ning et al.*
  - 🤗 Featured · `2026-10-13`
  - Deep research (DR) agents address open-ended information needs through multi-step reasoning, long-horizon web search, and evidence synthesis. However, existing benchmarks primarily focus on academic research or synthetic tasks, leaving DR agents' capabilities in real-world life a…

- **[SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software Coding Agents](https://arxiv.org/abs/2610.18206)**
  - *Do Xuan Trong, Duc Anh Nguyen, Do Xuan Long et al.*
  - 🤗 Featured · `2026-10-13`
  - We present SWE-MISBEHAVIOR, the first taxonomy and evaluation framework for diagnosing boundary-violating misbehaviors in coding agents. It contains 7.4K human-in-the-loop synthesized samples spanning three layers of agent action space: (i) Code Generation, (ii) File Management,…

- **[Harness^2: Recursive Agent Harnessing for an Open World](https://arxiv.org/abs/2610.14224)**
  - *Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu et al.*
  - 🤗 Featured · `2026-10-09`

- **[ClawLoop: Self-Improving Agents via Harness-Native Training Loop](https://arxiv.org/abs/2610.14118)**
  - *Hansi Yang, Linji Hao, Hongyan Hao et al.*
  - 🤗 Featured · `2026-10-09`

- **[Self-Evolving Agent Harness](https://arxiv.org/abs/2610.18813)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - 🤗 · `2026-10-13`
  - Harness self-evolution revises an agent's software scaffolding, including prompts, memory, workflows, and executable components, while keeping model weights fixed. We formalize a feedback-driven process in which accepted revisions persist across runs. The framework separates upda…

- **[Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2610.18352)**
  - *Youpeng Wen, Gang Wang, Tianyu Huang et al.*
  - 🤗 · `2026-10-13`
  - A robot following a multi-step instruction needs to act on the right objects in the right order, even as the scene changes. It must also maintain awareness of task progress and determine when to advance. To address these challenges, we introduce Orchestra, an agent harness that s…

- **[CompanionSafe: From Multi-turn Safety Evaluation to Guardrails for AI Companions](https://arxiv.org/abs/2610.18095)**
  - *Xinyang Liao, Lingyu Li, Kaicheng Shen et al.*
  - 🤗 · `2026-10-13`

- **[SHELDON: Reasoning through Dual Search over Hypothesis and Observation Spaces](https://arxiv.org/abs/2610.18025)**
  - *Harshit Joshi, Priyank Shethia, Monica S. Lam*
  - 🤗 · `2026-10-13`
  - Test-time scaling has enabled LLMs to solve increasingly complex reasoning, discovery, and optimization tasks. However, existing approaches often gather observations while seeking evidence for current hypotheses, then generate new hypotheses conditioned on those hypotheses and th…

- **[GIFT-Eval-CTX: A Benchmark For Contextual Forecasting Model Evaluation](https://arxiv.org/abs/2610.17794)**
  - *Xu Liu, Hanshu Yan, Taha Aksu et al.*
  - 🤗 · `2026-10-13`
  - Contextual forecasting seeks to improve time series forecasting by incorporating forward-looking information, such as planned events, external conditions, and expert expectations. However, reliable evaluation remains difficult: existing benchmarks often have limited domain covera…

- **[Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve](https://arxiv.org/abs/2610.18616v1)**
  - *Yuyang Bai, Yu Wang, Yu Zhang*
  - `2026-10-13`
  - Searching text-rich knowledge graphs requires following relations while examining textual evidence. Predefined graph interfaces constrain what evidence agents can access, even when they write code to combine tool calls or process retrieved subgraphs. We propose direct knowledge g…

- **[Delegating Earth science model calibration to knowledge-guided LLM agents](https://arxiv.org/abs/2610.18378v1)**
  - *Zhanliang Zhu, Ziwei Li, Liujun Zhu et al.*
  - `2026-10-13`
  - Applying process-based Earth science models to new sites and questions often requires expert calibration decisions. Reliable delegation to language-model agents must preserve scientific competence and reproducibility. Here we develop a general calibration harness (GCH) for end-to…

- **[Holding Agents Accountable with Verifiable Agent Insurance](https://arxiv.org/abs/2610.18230v1)**
  - *Cheng Hua, Taro Tsuchiya, Nicolas Christin et al.*
  - `2026-10-13`
  - While AI agents are useful for many tasks, they regularly misbehave in destructive ways, such as deleting important data. While prior work has focused on preventing such misbehavior, we consider how to recover after an agent misbehaves. We propose verifiable agent insurance (VAI)…

- **[APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation](https://arxiv.org/abs/2610.18097v1)**
  - *Sirui Zhang, Fangyun Wei, Dong Chen et al.*
  - `2026-10-13`
  - Post-training is crucial for improving text-to-image models, yet existing pipelines typically rely on manually curated training data and fixed training distributions. We introduce APT (Agentic Post-Training), a fully automated framework that adaptively post-trains a base model ac…

- **[AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses](https://arxiv.org/abs/2610.18090v1)**
  - *Kaiyu Huang, Yiting Li, Angyang Gu et al.*
  - `2026-10-13`
  - Ambiguous or incomplete task specifications complicate both execution and clarification for language-model agents. Yet agents' responses to these information gaps remain poorly characterized across models and execution harnesses. We present AM-Bench, a benchmark built from 48 tas…

- **[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088v1)**
  - *Peng Jiang, Dongyang Li, Quanying Liu et al.*
  - `2026-10-13`
  - Autoresearch systems increasingly undertake entire research projects. In practice, scientific research requires systems to pursue multiple interdependent claims through a continuous, multi-stage workflow and revise experiments as evidence accumulates. Existing evaluations of auto…

- **[AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement](https://arxiv.org/abs/2610.18083v1)**
  - *Wenhao Zhou, Jiajun Song, Haitao Wang et al.*
  - `2026-10-13`
  - Scaling recursive self-improvement requires additional computation to produce useful research progress in reaching persistent objectives. Intuitively, more researcher agents can explore more hypotheses, but early evaluation scores might misrepresent their promise, shared findings…

- **[Interaction-as-a-Judge](https://arxiv.org/abs/2610.17895v1)**
  - *Wayne Chi, I-Hung Hsu, Li Chen et al.*
  - `2026-10-13`
  - Coding agents are tasked with producing sophisticated interactive applications such as websites, desktop applications, and games. While humans assess these applications interactively, current automated LLM evaluations primarily focus on code analysis and unit tests. This mismatch…

- **[Benchmarking and Training Reward Models for Cross-Source Evidence Grounding in Search Agents](https://arxiv.org/abs/2610.17827v1)**
  - *Haochen Zhao, Minsheng Hao, Zheng Li et al.*
  - `2026-10-13`
  - Existing approaches to training and evaluating search agents focus heavily on final-answer quality, largely neglecting how generated answers map back to retrieved evidence. Recent methods track citations to enforce grounding, but citation support alone does not establish source i…

- **[Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution](https://arxiv.org/abs/2610.17816v1)**
  - *Pengcheng Huang, Zhenghao Liu, Shixin Ren et al.*
  - `2026-10-13`
  - Edge-cloud collaboration combines the lower inference overhead and greater data locality of edge-side execution with the stronger capabilities of cloud-hosted models. However, as LLM agents increasingly operate in long-horizon scenarios, cloud participation becomes interleaved th…

- **[Instructions Are Evidence, Not Objectives: Measuring Outcome Alignment of Agents](https://arxiv.org/abs/2610.17757v1)**
  - *Kaiming Liu, Yuxuan Liu, Jinrui Ju et al.*
  - `2026-10-13`
  - Large language model agents can follow complex human instructions to solve real-world tasks. In practice, however, initial instructions are often incomplete. In our analysis of 100 user-agent trajectories from SWE-chat, 56\% of initial instructions omit requirements that later em…

- **[Coupled Harness--Model Evolution for Scientific Equation Discovery](https://arxiv.org/abs/2610.17740v1)**
  - *Pengze Li, Jiaquan Zhang, Encheng Su et al.*
  - `2026-10-13`
  - Large language models (LLMs) are increasingly used to discover scientific equations from experimental data. Such a discovery system has two parts that must work together: a library of executable computational tools and the model's tool-use policy. The tools supply the solving cap…

- **[Verifier-Harness Co-Evolution for Training-Free Self-Improvement on Open-Ended Tasks](https://arxiv.org/abs/2610.17609v1)**
  - *Tianyi Xu, Yaolun Zhang, Yiran Wu et al.*
  - `2026-10-13`
  - Training-free self-improvement lets an agent use feedback to revise the response it is about to return and to update the harness state that shapes how it handles later tasks. On open-ended tasks that feedback rarely comes from reference answers or executable tests, so the agent h…

- **[The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement](https://arxiv.org/abs/2610.18845v1)**
  - *Sijie Zhao, Zeqi Zhou, Heli Qi et al.*
  - `2026-10-13`
  - Earth observation (EO) models are still built by hand. For each new task, experts design a training recipe and tune it against a benchmark. We show that this loop can be handed to an agent. Any verifiable task can be cast as a harness and a verifier, where the harness defines wha…

- **[Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning](https://arxiv.org/abs/2610.18611v1)**
  - *Huaiwen Pang, Jiale Han, Junying Chen et al.*
  - `2026-10-13`
  - Legal question answering requires answers that are not only plausible, but also grounded in legally valid and citable evidence. Standard retrieval-augmented generation often relies on one-shot semantic matching, which is insufficient when legal evidence must be selected according…

- **[The Last Mile of Coding Agents for Long-Document Tasks: An Empirical Study on Clinical Trial Protocol Digitization](https://arxiv.org/abs/2610.18507v1)**
  - *Jiacheng Lin, Geoffrey Low, Nishit Agarwal et al.*
  - `2026-10-13`
  - Clinical trial protocols serve as the source of truth for study design, but are mostly written and used as unstructured PDF documents. Digitizing protocols turns static content into structured, machine-readable data that clinical software can analyze, validate, and execute. Codin…

- **[Jev-Guard: Fast Routing and Auditing Agent Actions over Editable Policy Trees](https://arxiv.org/abs/2610.18326v1)**
  - *Wenbin Hu, Huihao Jing, Haochen Shi et al.*
  - `2026-10-13`
  - Agent harnesses require a low-latency guardrail model together with customizable audit policies. However, deploying an auto-regressive guardrail model remains challenging: such models incur high inference latency and are often poorly aligned with customized policies. To address t…

- **[StateHarness: Maintaining Evolving Project State for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.17616v1)**
  - *Chuan Zou, Yujun Zhou, Xiaonan Luo et al.*
  - `2026-10-13`
  - Long-horizon coding requires agents to maintain an evolving view of the project they are changing: what problem is currently being solved, what has already been learned or modified, which other artifacts may be affected, and what work remains unresolved. When this information is…

- **[Who Improves the Robot? Toward Physical Recursive Self-Improvement](https://arxiv.org/abs/2610.18842v1)**
  - *Hai Zhou, Fan Yang, Zeyi Chen et al.*
  - `2026-10-13`
  - Robots are increasingly autonomous in task execution, yet their improvement remains largely human-driven. This study investigates Physical Recursive Self-Improvement (Physical RSI), in which physical experience guides lasting updates to both a robot's capabilities and its improve…

- **[Same Attack, Different Judge: A First Controlled Adversarial Comparison of Jev, LLM Judges, and Purpose-Built Safety Classifiers](https://arxiv.org/abs/2610.17820v1)**
  - *Xiang Li, Aichun Huang, Mingming Zhang et al.*
  - `2026-10-13`
  - TypeSafe AI's Jev is a new kind of safety judge. It generates no text and no label: it answers questions the developer defines in advance and returns a probability for each answer. The vendor admits that adversarial input can change these answers but gives no numbers. In this pap…

- **[Uncertainty Evaluation: Bridging Machine Learning and Measurement Science](https://arxiv.org/abs/2610.18066v1)**
  - *Dario Petri, Luca Mari*
  - `2026-10-13`
  - Reliable uncertainty evaluation is essential for assessing the trustworthiness of machine learning (ML) predictions, particularly in safety-critical applications. This paper explores conceptual analogies between uncertainty evaluation in ML and measurement science, drawing on the…

- **[A Node Embedding Framework for Model-Centric Conformance Checking in Process Mining](https://arxiv.org/abs/2610.17702v1)**
  - *Mostafa Abbasi, Homayoun Najjaran*
  - `2026-10-13`
  - Evaluating the quality of process models discovered from event logs is a fundamental challenge in process mining. Traditional evaluation relies on conformance metrics such as fitness and precision, which are highly sensitive to noise and deviations in event logs and therefore oft…

- **[Virtual Head Attention](https://arxiv.org/abs/2610.17959v1)**
  - *Xibo Ding, Guoxia Wang, Jinle Zeng et al.*
  - `2026-10-13`
  - The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality. GQA achieves strong quality but incurs high KV cache overhead; alternative approaches such as MLA and MFA…

- **[Do Theorem Provers Need Theorem-Proving Agents? mini-Lean-agent: A Coding-Agent Baseline for Lean](https://arxiv.org/abs/2610.17331v1)**
  - *Tomas Ortega, Simon Park, Ayush Khaitan et al.*
  - `2026-10-12`
  - General-purpose coding agents use standard shell and file interactions, yet formal theorem-proving agents often rely on specialized, ad-hoc tooling. This makes it difficult to determine which components of theorem-proving agents provide benchmark gains: an improved base model, a…

- **[PhysCodeGym: Benchmarking Coding Agents for Physically Verifiable 4D Reconstruction](https://arxiv.org/abs/2610.17288v1)**
  - *Shuai Shao, Jinchen He, Cunxin Fan et al.*
  - `2026-10-12`
  - Building physical simulations from video requires coding agents to translate observations into executable models and refine them through tool use. We introduce PhysCodeGym, a benchmark for physically verifiable 4D reconstruction with $156$ tasks covering rigid-body, liquid, defor…

- **[Glasseek: A Transparent Recipe for Training and Trustworthy Evaluation of DeepSearch Agents](https://arxiv.org/abs/2610.16998v1)**
  - *Cong Pang, Jiaqi Su, Chengrui Wu et al.*
  - `2026-10-12`
  - Deep search enables language agents to solve complex information-seeking tasks through iterative web exploration. However, developing robust open-source agents remains challenging for three reasons. First, opaque trajectory-construction pipelines make training data difficult to a…

- **[Trace-to-Architecture: Capability Bottleneck Diagnosis for Harness Revision](https://arxiv.org/abs/2610.16725v1)**
  - *Wenfeng Wang, Jianrui Shi, Mingang Guo et al.*
  - `2026-10-12`
  - Improving an LLM agent requires knowing what to change when it fails. Similar failures can require different fixes, and resolving one problem can expose another. We introduce Trace-to-Architecture (T2A), a framework that uses execution trajectories to determine what to change in…

- **[LATCH: LLM-Assisted Timing Closure Harness for Post-Route FPGA Optimisation](https://arxiv.org/abs/2610.16625v1)**
  - *Shu Gu, Matthew Youngman, Yuqin Zhao et al.*
  - `2026-10-12`
  - Post-route FPGA timing closure remains expert-dependent and computationally expensive. We present LATCH (LLM-Assisted Timing Closure Harness), a two-layer framework that separates large language model (LLM) orchestration from deterministic FPGA implementation and evaluation. Acro…

- **[Unravel: Recovering an Interactive 3D Scene from a Single Image](https://arxiv.org/abs/2610.16146v1)**
  - *Hui Shan, Keyang Luo, Binjia Zhou et al.*
  - `2026-10-12`
  - We present Unravel, a training-free framework that turns a single image into an interactive 3D scene, where every object is an independent and movable asset. Existing generators either produce one entangled geometry in which no object can be moved, or predict all objects in one f…

- **[Heterogeneous Agentic Coevolution](https://arxiv.org/abs/2610.16078v1)**
  - *Wenqian Ye, Ziwei Guan, Zi Yang et al.*
  - `2026-10-12`
  - Recent advances in self-improving LLM agents have demonstrated the potential of AI systems that drive their own intelligence. However, many domain-specific applications rely on specialized foundation models that possess strong domain expertise but remain dependent on human-design…

- **[Computational Reflective Equilibrium for Agentic AI: A Rawlsian Alignment Scaffold for Governance](https://arxiv.org/abs/2610.16015v1)**
  - *Quanyan Zhu*
  - `2026-10-12`
  - The rapid deployment of agentic AI has introduced complex challenges for the ethics and governance of AI systems. Agents built on large language models act through tools on behalf of people, and each deployment case brings its own instructions, policies, evidence, and stakeholder…

- **[Learning to Design SR Solvers: Harness Optimization for Symbolic Regression](https://arxiv.org/abs/2610.16966v1)**
  - *Qian Li, Yuxiao Hu, Qihao Duan et al.*
  - `2026-10-12`
  - Symbolic regression (SR) seeks explicit equations that explain observed data, and recent methods increasingly employ large language models (LLMs) and agents for equation discovery. However, these systems typically rely on manually designed workflows and prompts. We argue that the…

- **[Scaling Inference-Time Compute with Teams of Coding Agents](https://arxiv.org/abs/2610.17471v1)**
  - *Keenan Samway, Daniel D'souza, Omar Darwiche Domingues et al.*
  - `2026-10-12`
  - Multi-agent systems promise a new axis for scaling inference: rather than having one agent think longer or sample more attempts, a task is split across many agents that work in parallel and coordinate. However, in practice, more agents can easily produce duplicate work, coordinat…

- **[SpecGuardBench: Can Coding Agents Construct Reliable Validation Harnesses from Natural Language Specifications?](https://arxiv.org/abs/2610.16870v1)**
  - *Zhiqing Zhong, Mingyu Chen, Aoyang Fang et al.*
  - `2026-10-12`
  - As coding agents become more capable, tests remain the primary evidence for judging whether their code is correct. Yet passing available tests does not establish that an implementation satisfies its natural language specification. Reliable validation requires checks that faithful…

- **[ANCHOR: Assessing Naturalistic Constraint Hierarchies and Ordering in Repository-Grounded Agentic Coding](https://arxiv.org/abs/2610.16859v1)**
  - *Wenqiang Zhu, Xinping Lei, Zhiyi Lai et al.*
  - `2026-10-12`
  - For repository-grounded coding agents, a functionally correct patch is not necessarily an acceptable one: developers also constrain how the task must be carried out-modification scope, workflow order, validation, tool use, and reporting. This capability, which we call engineering…

- **[CivWorldBench: Evaluating Language World Models in Structured Multi-Agent Sandbox Worlds](https://arxiv.org/abs/2610.16450v1)**
  - *Ang Li, Haofei Yu, Zhengwei Tao et al.*
  - `2026-10-12`
  - The growing use of language models for forecasting motivates a broader evaluation of their world-model capabilities. Such evaluation must go beyond predictive accuracy to assess hidden-state inference and intervention prediction. Real-world forecasting benchmarks offer limited ac…

- **[HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery](https://arxiv.org/abs/2610.17370v1)**
  - *Yingzi Ma, Yulong Cao, Nanxi Li et al.*
  - `2026-10-12`
  - Scientific discovery with language models requires finding the best valid solution within a finite computational budget. We study how feedback from this search can improve the procedure used to conduct it. We introduce HarnessTTT, a test-time learning framework that trains a harn…

- **[ProbabilityBench: Model Evaluation and Calibration with Exact Ground-Truth Uncertainty](https://arxiv.org/abs/2610.17016v1)**
  - *Yuyang Dai, Yuting Tang, Futoshi Futami et al.*
  - `2026-10-12`
  - Evaluating model uncertainty on real-world data is challenging because each instance provides only a single observed label, leaving true conditional class probabilities unknown. To address this, we introduce ProbabilityBench, a benchmark that provides exact, instance-level class…

- **[LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints](https://arxiv.org/abs/2610.16782v1)**
  - *Ming Shin Cindy Sung, Duan Leijiahao, Haoxiang Wang et al.*
  - `2026-10-12`
  - Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions. Such settings impose industrial process constraints, including product variants, moving mate…

- **[VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models](https://arxiv.org/abs/2610.16567v1)**
  - *Jun Xiao, Rui Ye, Dong Cao et al.*
  - `2026-10-12`
  - Vision-Language-Action models (VLAs) have achieved high success rates on familiar manipulation tasks, yet it remains unclear whether such scores reflect genuine zero-shot generalization and perturbation robustness. Existing evaluation frameworks provide limited capability-level d…

- **[A Time-Synchronous Prequential Evaluation Framework for Next-Week Student Disengagement Prediction from Moodle LMS Logs](https://arxiv.org/abs/2610.17490v1)**
  - *David Otoo-Arthur, Terence L. van Zyl*
  - `2026-10-12`
  - Retrospective evaluation of early-warning models may not reflect information available when predictions are issued and outcomes become observable. We developed a time-synchronous prequential framework for online prediction of next-week student disengagement, operationalised as in…

- **[Mean Accuracy Is the Wrong Estimand for a Release Decision](https://arxiv.org/abs/2610.16825v1)**
  - *Jaewon Choi, Jihye Kang, Namhyuk Ahn*
  - `2026-10-12`
  - A release decision about a fine-tuned model is an operational commitment about the \emph{next} rerun of its training recipe. Yet standard benchmark reporting gives only the mean accuracy of past seeds. These target fundamentally different questions: release decisions depend on ca…

- **[EHR-Bench: A Chinese Multi-Task Benchmark for Recruitment AI](https://arxiv.org/abs/2610.16689v1)**
  - *Ruijia Yang, Bing Xu, Zulong Chen et al.*
  - `2026-10-12`
  - Recruitment applications span diverse operations, from drafting job descriptions and interpreting queries to organizing profiles, assessing fit, and recommending candidates and jobs. Systematic LLM evaluation therefore requires task coverage that reflects this range of business n…

- **[SIREN: Situation-aware Index for Response and Emergency ActioNability in Crisis Translation](https://arxiv.org/abs/2610.16646v1)**
  - *Maria Carmen Staiano, Lifeng Han, Johanna Monti et al.*
  - `2026-10-12`
  - Machine translation (MT) is increasingly utilized in multilingual crisis communication, yet conventional evaluation does not directly assess whether translated emergency messages preserve their actionability. We introduce SIREN (Situation-aware Index for Response and Emergency Ac…

- **[Large language model-generated patterns for epidemiological modeling: a multi-benchmark evaluation framework](https://arxiv.org/abs/2610.15994v1)**
  - *Sophia Mao, Keshav Gandhi, Alexander Gutfraind*
  - `2026-10-11`
  - Representing individual-level behavioral heterogeneity is challenging in epidemiological modeling, particularly when empirical behavioral data are sparse. We assess the potential of large language model (LLM)-generated behavioral outputs in addressing this challenge, using hepati…

- **[Small but Mighty: Test Suites as Improvement Signals for Self-Evolving Agents](https://arxiv.org/abs/2610.15964v1)**
  - *Yutong Cheng, Wei Cheng, Wenchao Yu et al.*
  - `2026-10-11`
  - A self-evolving agent rewrites its own harness and must decide which rewrites to keep, so its improvement signal is the check a rewrite has to pass. Verifying a rewrite by agent rollout is expensive and subjective, while executable checks such as the repository's own tests are to…

- **[Visible but Not Avoided: State-Dependent Re-Proposal of Rejected Candidates in Catalog-Based LLM Optimization Loops](https://arxiv.org/abs/2610.15738v1)**
  - *Jianlin Chen, Wenhui Chen, Chi Man Vong*
  - `2026-10-11`
  - LLM optimization loops often show the proposer the candidates it has already tried and rejected, but leave it to the proposer to avoid them. We ask whether avoidance measured in a static probe predicts avoidance in the states an optimizer's own trajectory produces. In catalog-bas…

- **[MedHarnessBench: A Unified Benchmark for Healthcare Agent Evaluation](https://arxiv.org/abs/2610.15714v1)**
  - *Rui Tang, Hongqiu Wang*
  - `2026-10-11`
  - Healthcare agents must transform longitudinal clinical evidence into reliable actions through heterogeneous tools and stateful workflows, conditions under which model-centric systems may lose context, misuse tools, fail to verify consequential transitions, or cross authorization…

- **[CoverSynth: Coverage-Guided Generation of Retrieval Evaluation Sets](https://arxiv.org/abs/2610.15409v1)**
  - *Anahita Sharma, Apaar Shanker, Rishav Chakravarti et al.*
  - `2026-10-11`
  - Enterprise agents need retrieval evaluation sets that expose domain-specific failures and guide developers towards efficient deployment tradeoffs. Neither expert-human-authored sets nor current synthetic generation methods provide a methodology for achieving the necessary coverag…

- **[ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs](https://arxiv.org/abs/2610.15368v1)**
  - *Yi Ge, Kangrui Ruan, Jifan Chen et al.*
  - `2026-10-11`
  - Rapid advances in large language models have made software engineering agents capable of tackling complex coding tasks. Within a containerized environment, a coding agent receives tool responses or execution results, and determines its later actions by those earlier results. Howe…

- **[Harnessing SPAD Noise: Test-Time Gated Attention for Indoor Depth Estimation](https://arxiv.org/abs/2610.15431v1)**
  - *Yiquan Gao*
  - `2026-10-11`
  - Monocular depth estimation (MDE) has emerged as a cost-effective alternative to hardware-dependent 3D sensing modalities, yet predicting precise metric depth remains a persistent challenge due to intrinsic scale ambiguity, edge bleeding, and limited zero-shot generalization in un…

- **[Harnessing VLM in Embodied RL: From Reward Regressor to Success Detector via Exploration-Augmented Key-Observation Gating](https://arxiv.org/abs/2610.15401v1)**
  - *Xin Liu, Yutong Jiang, Jian Su et al.*
  - `2026-10-11`
  - VLMs provide promising solutions to embodied reward design. Most current methods that train VLMs as reward regressors not only require extensive annotations but are also primarily designed for finetuning pretrained policies, and perform less well in the more challenging from-scra…

- **[Apertus 1.5: From Open Text Models to Open Multimodal Reasoners](https://arxiv.org/abs/2610.15542v1)**
  - *Project Apertus, :, Yixuan Xu et al.*
  - `2026-10-11`
  - Language models are becoming infrastructure, and infrastructure built in the open, by public institutions, on documented data, is the alternative to dependence on a few providers; Apertus shows this is viable at scale. Apertus 1.5 extends the fully open Apertus family from text t…


## Finance  (186)

### AAAI

- **[CVE-LLM : Ontology-Assisted Automatic Vulnerability Evaluation Using Large Language Models](https://arxiv.org/abs/2502.15932)**
  - *Rikhiya Ghosh, Hans-Martin von Stockhausen, Martin Schmitt et al.*
  - **AAAI 2025** · `2025-02-21`
  - The National Vulnerability Database (NVD) publishes over a thousand new vulnerabilities monthly, with a projected 25 percent increase in 2024, highlighting the crucial need for rapid vulnerability identification to mitigate cybersecurity attacks and save costs and resources. In t…

- **[CoDe: Communication Delay-Tolerant Multi-Agent Collaboration via Dual Alignment of Intent and Timeliness](https://arxiv.org/abs/2501.05207)**
  - *Shoucheng Song, You-Fang Lin, Sheng Han et al.*
  - **AAAI 2025** · `2025-01-09`
  - Communication has been widely employed to enhance multi-agent collaboration. Previous research has typically assumed delay-free communication, a strong assumption that is challenging to meet in practice. However, real-world agents suffer from channel delays, receiving messages se…


### NeurIPS

- **[The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets](https://openreview.net/forum?id=XZpIu68yW6)**
  - *Shenzhe Zhu, Jiao Sun, Yi Nian et al.*
  - **NeurIPS 2025** · OpenReview · `2025-09-01`
  - AI agents are increasingly used in consumer-facing applications to assist with tasks such as product search, negotiation, and transaction execution. In this paper, we investigate a future setting where both consumers and merchants authorize AI agents to automate the negotiations…

- **[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)**
  - *Yuan-Te Li, Xu Yang, Xiao Yang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - Financial markets pose fundamental challenges for asset return prediction due to their high dimensionality, non-stationarity, and persistent volatility. Despite advances in large language models and multi-agent systems, current quantitative research pipelines suffer from limited…


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

- **[MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://arxiv.org/abs/2503.03686)**
  - *Rui Ye, Shuo Tang, Rui Ge et al.*
  - **ICML 2025** · `2025-03-05`
  - LLM-based multi-agent systems (MAS) have shown significant potential in tackling diverse tasks. However, to design effective MAS, existing approaches heavily rely on manual configurations or multiple calls of advanced LLMs, resulting in inadaptability and high inference costs. In…

- **[MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673)**
  - *Adibvafa Fallahpour, Jun Ma, Alif Munim et al.*
  - **ICML 2025** · `2025-02-04`
  - Chest X-rays (CXRs) play an integral role in driving critical decisions in disease management and patient care. While recent innovations have led to specialized models for various CXR interpretation tasks, these solutions often operate in isolation, limiting their practical utili…


### KDD

- **[XForecast: The KDD 2026 Finance Day Challenge on News-Grounded Financial Forecasting](https://arxiv.org/abs/2610.16131v1)**
  - *Jaehoon Lee, Jun Seo, Seunghan Lee et al.*
  - **KDD** · `2026-10-12`
  - Financial forecasting has traditionally relied on numerical time-series (TS) signals, while textual information such as news remains largely underutilized. We introduce XForecast, a benchmark and competition for news-grounded financial forecasting, where the task is to predict st…

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, A. Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…


### ACL

- **[From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)**
  - *Jing Luo, Yuchen Tian, Chuxue Cao et al.*
  - **ACL 2026** · `2026-05-07`
  - Large Language Model (LLM)-based agents have fundamentally reshaped artificial intelligence by integrating external tools and planning capabilities. While memory mechanisms have emerged as the architectural cornerstone of these systems, current research remains fragmented, oscill…

- **[HalluLens: LLM Hallucination Benchmark](https://arxiv.org/abs/2504.17550)**
  - *Yejin Bang, Ziwei Ji, A. Schelten et al.*
  - **ACL 2025** · `2025-04-24`
  - Large language models (LLMs) often generate responses that deviate from user input or training data, a phenomenon known as"hallucination."These hallucinations undermine user trust and hinder the adoption of generative AI systems. Addressing hallucinations is essential for the adv…

- **[Right Answer, Wrong Score: Uncovering the Inconsistencies of LLM Evaluation in Multiple-Choice Question Answering](https://arxiv.org/abs/2503.14996)**
  - *F. Molfese, Luca Moroni, Luca Gioffré et al.*
  - **ACL 2025** · `2025-03-19`
  - One of the most widely used tasks for evaluating Large Language Models (LLMs) is Multiple-Choice Question Answering (MCQA). While open-ended question answering tasks are more challenging to evaluate, MCQA tasks are, in principle, easier to assess, as the model's answer is thought…

- **[METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](https://arxiv.org/abs/2502.17651)**
  - *Bing-Xuan Li, Yiwei Wang, Jiu-Xiang Gu et al.*
  - **ACL 2025** · `2025-02-24`
  - Chart generation aims to generate code to produce charts satisfying the desired visual properties, e.g., texts, layout, color, and type. It has great potential to empower the automatic professional report generation in financial analysis, research presentation, education, and hea…

- **[FLAG-Trader: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading](https://arxiv.org/abs/2502.11433)**
  - *Guo-Jun Xiong, Zhiyang Deng, Keyi Wang et al.*
  - **ACL 2025** · `2025-02-17`
  - Large language models (LLMs) fine-tuned on multimodal financial data have demonstrated impressive reasoning capabilities in various financial tasks. However, they often struggle with multi-step, goal-oriented scenarios in interactive financial markets, such as trading, where comp…

- **[G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems](https://arxiv.org/abs/2502.11127)**
  - *Shilong Wang, Gui-Min Zhang, Miao Yu et al.*
  - **ACL 2025** · `2025-02-16`
  - Large Language Model (LLM)-based Multi-agent Systems (MAS) have demonstrated remarkable capabilities in various complex tasks, ranging from collaborative problem-solving to autonomous decision-making. However, as these systems become increasingly integrated into critical applicat…


### EMNLP

- **[Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents](https://arxiv.org/abs/2509.17488)**
  - *Shou-Ju Wang, Fenglin Yu, Xirui Liu et al.*
  - **EMNLP 2025** · `2025-09-22`
  - The increasing autonomy of LLM agents in handling sensitive communications, accelerated by Model Context Protocol (MCP) and Agent-to-Agent (A2A) frameworks, creates urgent privacy challenges. While recent work reveals significant gaps between LLMs'privacy Q&A performance and thei…

- **[Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses](https://arxiv.org/abs/2509.16093)**
  - *Fangyi Yu, Nabeel Seedat, Dasha Herrmannova et al.*
  - **EMNLP 2025** · `2025-09-19`
  - Evaluating long-form answers in high-stakes domains such as law or medicine remains a fundamental challenge. Standard metrics like BLEU and ROUGE fail to capture semantic correctness, and current LLM-based evaluators often reduce nuanced aspects of answer quality into a single un…

- **[ReliableEval: A Recipe for Stochastic LLM Evaluation via Method of Moments](https://arxiv.org/abs/2505.22169)**
  - *G. Lior, Eliya Habba, Shahar Levy et al.*
  - **EMNLP 2025** · `2025-05-28`
  - LLMs are highly sensitive to prompt phrasing, yet standard benchmarks typically report performance using a single prompt, raising concerns about the reliability of such evaluations. In this work, we argue for a stochastic method of moments evaluation over the space of meaning-pre…

- **[Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews](https://arxiv.org/abs/2502.17086)**
  - *Hyungyu Shin, Jingyu Tang, Yoonjoo Lee et al.*
  - **EMNLP 2025** · `2025-02-24`
  - Peer review underpins scientific progress, but it is increasingly strained by reviewer shortages and growing workloads. Large Language Models (LLMs) can automatically draft reviews now, but determining whether LLM-generated reviews are trustworthy requires systematic evaluation.…


### Other / arXiv

- **[Hybrid Reasoning Agents](https://arxiv.org/abs/2610.18861)**
  - *Jiaru Zou, Yunzhe Qi, Sirui Chen et al.*
  - 🤗 · `2026-10-13`
  - How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning tran…

- **[Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve](https://arxiv.org/abs/2610.18616v1)**
  - *Yuyang Bai, Yu Wang, Yu Zhang*
  - `2026-10-13`
  - Searching text-rich knowledge graphs requires following relations while examining textual evidence. Predefined graph interfaces constrain what evidence agents can access, even when they write code to combine tool calls or process retrieved subgraphs. We propose direct knowledge g…

- **[AgentStripes: An Evidence-Graded Maturity Model for AI Agents](https://arxiv.org/abs/2610.18603v1)**
  - *Nutan Kumar Naik, Vijay Prasad Poudel, Aditya Kumar Saroj et al.*
  - `2026-10-13`
  - Benchmarks report what an Artificial Intelligence (AI) agent can do on a task suite, but not whether one released version has been engineered with the controls that make it reliable, safe and observable, or how strongly that is shown. This paper proposes AgentStripes, an evidence…

- **[LLM Agents for Automated Post-Training via Structured Recipe Optimization](https://arxiv.org/abs/2610.18572v1)**
  - *Ruohong Liu, Bohan Tang, Lekang Jiang et al.*
  - `2026-10-13`
  - Automated post-training transforms pre-trained large language models (LLMs) into models capable of handling diverse domains by automatically constructing and optimizing a recipe of coupled decisions over data sources, data processing, cross-domain composition, and training config…

- **[On Symmetry for Characterizing Agent Heterogeneity in Multi-Agent Systems](https://arxiv.org/abs/2610.18538v1)**
  - *Jianhong Wang, Jonathan Lawry*
  - `2026-10-13`
  - Understanding agent heterogeneity can inform the design of shared and agent-specific policy representations, however existing criteria provide no unified structural test. We study finite-horizon POSGs and define a type-compatible transformation as a policy-evaluation symmetry whe…

- **[Delegating Earth science model calibration to knowledge-guided LLM agents](https://arxiv.org/abs/2610.18378v1)**
  - *Zhanliang Zhu, Ziwei Li, Liujun Zhu et al.*
  - `2026-10-13`
  - Applying process-based Earth science models to new sites and questions often requires expert calibration decisions. Reliable delegation to language-model agents must preserve scientific competence and reproducibility. Here we develop a general calibration harness (GCH) for end-to…

- **[Choosing LLMs for Strategic Agent Interactions](https://arxiv.org/abs/2610.18354v1)**
  - *Arastun Mammadli, Herbert Woisetschläger, Jawad Fayaz et al.*
  - `2026-10-13`
  - Game-theoretic benchmarks claim that large language model (LLM) strategic decision-making varies across game types, interaction structures, and capability dimensions. However, they only evaluate strategic performance across individual fixed models. In parallel, contemporary LLM r…

- **[AssetForge: Asset-Augmented Task Synthesis for Business Automation Agents](https://arxiv.org/abs/2610.18330v1)**
  - *Xiangrui Liu, Shuo Tang, Siheng Chen*
  - `2026-10-13`
  - Training business automation agents requires executable tasks that connect a natural-language request to an application state and a verifiable end state. Traditional Rubrics requires Authors to recreate application interfaces, initial records, policy evidence, and outcome checks…

- **[AffectWorld: Benchmarking Emotion-Driven Future World Prediction](https://arxiv.org/abs/2610.18305v1)**
  - *Changhao Song, Yacong Chen, Hui Gao et al.*
  - `2026-10-13`
  - The world encompasses both physical environments and human actors. Predicting its evolution requires understanding both physical laws and how emotions shape human actions. However, existing world model benchmarks primarily assess physical plausibility and perceptual quality, leav…

- **[Holding Agents Accountable with Verifiable Agent Insurance](https://arxiv.org/abs/2610.18230v1)**
  - *Cheng Hua, Taro Tsuchiya, Nicolas Christin et al.*
  - `2026-10-13`
  - While AI agents are useful for many tasks, they regularly misbehave in destructive ways, such as deleting important data. While prior work has focused on preventing such misbehavior, we consider how to recover after an agent misbehaves. We propose verifiable agent insurance (VAI)…

- **[AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses](https://arxiv.org/abs/2610.18090v1)**
  - *Kaiyu Huang, Yiting Li, Angyang Gu et al.*
  - `2026-10-13`
  - Ambiguous or incomplete task specifications complicate both execution and clarification for language-model agents. Yet agents' responses to these information gaps remain poorly characterized across models and execution harnesses. We present AM-Bench, a benchmark built from 48 tas…

- **[Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards](https://arxiv.org/abs/2610.17893v1)**
  - *Keru Chen, Sen Lin, Yingbin Liang et al.*
  - `2026-10-13`
  - Effective collaboration among large language model (LLM) agents in multi-agent systems requires sharing relevant evidence, requesting missing information, and incorporating teammates' contributions into decisions. Training these behaviors is challenging because final task outcome…

- **[Learning Adaptive Deliberation Control for Reliable Recognition with Multi-Agent Language Models](https://arxiv.org/abs/2610.17840v1)**
  - *Yuan Liu, Haoyue Peng, Fanliang Hu et al.*
  - `2026-10-13`
  - Multi-agent deliberation can improve recognition by criticizing and revising candidate answers, but fixed controls cannot respond to changes in disagreement or reasoning quality. We present an adaptive multi-agent controller (ADMA) that learns continuous policies for proposal, ch…

- **[Benchmarking and Training Reward Models for Cross-Source Evidence Grounding in Search Agents](https://arxiv.org/abs/2610.17827v1)**
  - *Haochen Zhao, Minsheng Hao, Zheng Li et al.*
  - `2026-10-13`
  - Existing approaches to training and evaluating search agents focus heavily on final-answer quality, largely neglecting how generated answers map back to retrieved evidence. Recent methods track citations to enforce grounding, but citation support alone does not establish source i…

- **[Agentic4PDM: Host-Governed Evidence Admissibility for Industrial Fault Diagnosis](https://arxiv.org/abs/2610.17786v1)**
  - *Nam V. Nguyen, Hoang Van Truong, Hieu D. D. et al.*
  - `2026-10-13`
  - We study industrial fault diagnosis as a classification task that assigns sensor time-series windows to predefined health states or fault types. Scarce labels and changing operating conditions make repeated training of specialized classifiers costly. Yet structures such as period…

- **[Memory Echo in Single-Agent Long-Term Memory: Lifecycle Evaluation and Provenance-Guided Mitigation](https://arxiv.org/abs/2610.17763v1)**
  - *Yufeng Li, Sheng Yao, Peng Zeng et al.*
  - `2026-10-13`
  - Long-term memory supports agents across sessions. Repeated retrieval and write-back can let one historical claim occupy multiple retrieval positions and influence current answers without independent evidence. Existing work examines retrieval, updating, and question answering, lea…

- **[The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement](https://arxiv.org/abs/2610.18845v1)**
  - *Sijie Zhao, Zeqi Zhou, Heli Qi et al.*
  - `2026-10-13`
  - Earth observation (EO) models are still built by hand. For each new task, experts design a training recipe and tune it against a benchmark. We show that this loop can be handed to an agent. Any verifiable task can be cast as a harness and a verifier, where the harness defines wha…

- **[Strategic Multi-Agent Resource Allocation via Statistical Contracts](https://arxiv.org/abs/2610.18336v1)**
  - *Ben Chugg, Michael I. Jordan, Aaditya Ramdas*
  - `2026-10-13`
  - We study a class of strategic hypothesis testing problems in which a principal aims to allocate resources among competing agents who possess data or data-generating mechanisms that may be relevant to the principal's goals. Each agent can pay a participation cost to opt into a sta…

- **[Who Improves the Robot? Toward Physical Recursive Self-Improvement](https://arxiv.org/abs/2610.18842v1)**
  - *Hai Zhou, Fan Yang, Zeyi Chen et al.*
  - `2026-10-13`
  - Robots are increasingly autonomous in task execution, yet their improvement remains largely human-driven. This study investigates Physical Recursive Self-Improvement (Physical RSI), in which physical experience guides lasting updates to both a robot's capabilities and its improve…

- **[Same Attack, Different Judge: A First Controlled Adversarial Comparison of Jev, LLM Judges, and Purpose-Built Safety Classifiers](https://arxiv.org/abs/2610.17820v1)**
  - *Xiang Li, Aichun Huang, Mingming Zhang et al.*
  - `2026-10-13`
  - TypeSafe AI's Jev is a new kind of safety judge. It generates no text and no label: it answers questions the developer defines in advance and returns a probability for each answer. The vendor admits that adversarial input can change these answers but gives no numbers. In this pap…

- **[Chasing Label Shifters: A Change-Aware Framework for Dynamic Graph Node Classification](https://arxiv.org/abs/2610.17582v1)**
  - *Junghoon Kim, Seungyoon Choi, Hyunsung Kim et al.*
  - `2026-10-13`
  - Entities in real-world systems often evolve over time: users shift between information consumption patterns, researchers migrate between fields, and firms transition between financial risk states. When such systems are modeled as dynamic graphs, these transitions correspond to no…

- **[Enhanced Detective: A Dual-Stage Proactive Defense Against Internal Poisoning Attacks in Financial Fraud Detection Using Federated Learning](https://arxiv.org/abs/2610.17523v1)**
  - *Maria-Ioana-Andrea Ivan, Orhan Ermis, Ruxandra F. Olimid*
  - `2026-10-13`
  - With recent developments in Artificial Intelligence (AI), the adoption of distributed learning paradigms such as Federated Learning (FL) has emerged. In simple terms, FL enables multiple entities to collaboratively train AI models without sharing local data. The FL paradigm is pa…

- **[Privacy-Preserving GNN Inference on Financial Transaction Graphs via Homomorphic Encryption](https://arxiv.org/abs/2610.18054v1)**
  - *H. Çağrı Bilgi, Kemal Mutluergil, Ceren Yıldırım et al.*
  - `2026-10-13`
  - Anti-money laundering (AML) in financial networks requires modeling transaction patterns that span multiple institutions. In practice, however, banks cannot share account and transaction features due to strict privacy regulations. We propose a privacy-preserving graph neural netw…

- **[RadarGSOcc: Doppler-Aware 3D Semantic Occupancy Prediction Using 4D Radar Tensor with Geometric-Semantic Feature Extraction](https://arxiv.org/abs/2610.18686v1)**
  - *Christofel Rio Goenawan, Dong-Hee Paek, Seung-Hyun Kong*
  - `2026-10-13`
  - 3D semantic occupancy prediction is crucial for autonomous driving, but camera-based methods degrade in low-light conditions and LiDAR-based methods are sensitive to adverse weather. 4D radar is more robust, yet its sparsity and the high cost of radar tensor processing limit its…

- **[A CaLLM Judge is a Better Judge: Mitigating Bias in LLM-as-a-judge](https://arxiv.org/abs/2610.18108v1)**
  - *Cesare Barbera, Luca Stradiotti, Lorenzo Cascioli et al.*
  - `2026-10-13`
  - Large language models (LLMs) are increasingly used as judges to predict which of two candidate answers a human evaluator would prefer, providing a scalable alternative when human evaluation is too costly. Unfortunately, LLM judgments can exhibit systematic biases. Prior work has…

- **[Risk Measures for the Climate Transition Age: Why Symmetric Risk Budgets are unlikely to mitigate two-dimensionally asymmetric Climate Change risks](https://arxiv.org/abs/2610.18387v1)**
  - *Lars Dijkstra, Andreas G. F. Hoepner, Fabiola I. Schneider et al.*
  - `2026-10-13`
  - The most widely used investment risk measures - variance, standard deviation, and tracking error - treat upside deviations as equally undesirable as downside losses. In stable markets with assumed symmetric return distributions, this simplification is potentially harmless. In the…

- **[Portfolio Decarbonization under Incomplete Carbon and Transition Information](https://arxiv.org/abs/2610.18332v1)**
  - *Olivier Féron, Ruben Haalebos*
  - `2026-10-13`
  - We study dynamic portfolio decarbonization under incomplete information about firms' carbon intensities and the underlying transition state. The investor maximizes expected utility of terminal wealth net of a penalty on perceived cumulative financed emissions. Asset returns and c…

- **[On integrability of local utility maximizing strategies](https://arxiv.org/abs/2610.17915v1)**
  - *Aleš Černý, Johannes Ruf*
  - `2026-10-13`
  - In stochastic control problems involving optimal portfolio choice, one often seeks an optimizer of some local criterion (dynamic programming value function) generated by some global criterion (e.g., expected utility). The local optimizer then typically acts as a stochastic integr…

- **[Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models](https://arxiv.org/abs/2610.17310v1)**
  - *Hanbo Xie, Yue Zhao, Robert C. Wilson*
  - `2026-10-12`
  - Language-model agents are expected to adapt to others whose behavior changes through interaction. Yet adaptation may rely on learned behavioral patterns rather than theory of mind (ToM): the ability to infer others' mental states, including beliefs and intentions. We introduce a…

- **[EvoQuantLab: Training-Free Dual-Loop Evolution for Auditable Quantitative Research](https://arxiv.org/abs/2610.17130v1)**
  - *Haolin Yang, Zhiqiang Qian, Chutian Chen et al.*
  - `2026-10-12`
  - Automated alpha factor discovery is critical for modern quantitative research. While large language models (LLMs) have increasingly been integrated into quantitative workflows, existing agent-based approaches remain highly susceptible to severe backtest overfitting. To address th…

- **[Who is the 'I' in AI? Establishing Decentralized Identity and Accountability for Autonomous Agents](https://arxiv.org/abs/2610.17126v1)**
  - *Ahammod Munim Ramil, Khalid Al Kafi, M. A. Abdullahis Sany et al.*
  - `2026-10-12`
  - The rapid proliferation of autonomous AI agents in decentralized ecosystems challenges existing identity paradigms. While human identity is traditionally anchored in biological and/or self-asserted attributes and government credentials, AI agents lack a standardized definition of…

- **[Glasseek: A Transparent Recipe for Training and Trustworthy Evaluation of DeepSearch Agents](https://arxiv.org/abs/2610.16998v1)**
  - *Cong Pang, Jiaqi Su, Chengrui Wu et al.*
  - `2026-10-12`
  - Deep search enables language agents to solve complex information-seeking tasks through iterative web exploration. However, developing robust open-source agents remains challenging for three reasons. First, opaque trajectory-construction pipelines make training data difficult to a…

- **[MADDIE: Multi-Agent Drug Discovery Engine](https://arxiv.org/abs/2610.16975v1)**
  - *Ye Liu, Reza Averly, Avery Meyer et al.*
  - `2026-10-12`
  - Drug discovery remains a resource-intensive and time-consuming process, involving billions of dollars and a decade of development to advance a drug to market. While many in silico tools have accelerated this process, operating them still demands substantial time, effort, and expe…

- **[REEL: Learning to Retrieve, Evaluate, and Evolve Visual Memory for Any Long-Horizon Multi-Shot Video Generation](https://arxiv.org/abs/2610.16632v1)**
  - *Hang Xu, Guohui Zhang, Xiaoxiao Ma et al.*
  - `2026-10-12`
  - Memory-based long-video generation aims to combine user control with long-range visual consistency. We organize this process into three functional components: a planner, an adapter, and a generator. Representative multi-shot systems couple memory to generator-specific interfaces…

- **[From Caricature to Collective Artifact: How Persona Construction Drives Polarization in Generative Social Simulations](https://arxiv.org/abs/2610.16498v1)**
  - *Dimitris Michailidis, Petter Törnberg, Fernando P. Santos*
  - `2026-10-12`
  - Generative Social Simulation (GSS) leverages Large Language Models (LLMs) to create sophisticated personas that define agents with demographics, emotions, and political opinions. While prior work shows that personas compress outputs into stereotypical caricatures, there is no com…

- **[CryptoFlowBench: Benchmarking Multi-Hop Reasoning on Blockchains for Cryptocurrency Fund Tracing](https://arxiv.org/abs/2610.16449v1)**
  - *Runang He, Tongya Zheng, Jing Cao et al.*
  - `2026-10-12`
  - Pseudonymous accounts and complex smart-contract ecosystems substantially hinder the tracing of illicit cryptocurrency fund flows. Existing Graph Neural Networks (GNNs) have achieved promising performance in blockchain fraud detection, yet their static node- or edge-level predict…

- **[Uncovering Robustness Weaknesses in LLM Agents via Persona Evolution with Task-Integrity Constraints](https://arxiv.org/abs/2610.16155v1)**
  - *Yutao Xie, Jingbo Yang, Guanyu Yao et al.*
  - `2026-10-12`
  - Interactive-agent evaluations commonly rely on standardized LLM-based user simulators that exhibit broadly cooperative behavior, potentially overlooking failures that arise under diverse but realistic user interactions. This can lead to overly optimistic estimates of agent robust…

- **[Position: Beyond Training Time, Test-Time Coordination is Essential for Cooperative MARL](https://arxiv.org/abs/2610.17409v1)**
  - *Dongsu Lee, Sooraj Sathish, Joonkyung Kim et al.*
  - `2026-10-12`
  - We argue that cooperative multi-agent reinforcement learning (MARL) should treat test-time coordination as part of the problem definition rather than a deployment artifact. Our focus is on long-horizon, centrally monitored cooperative systems such as warehouse robotics, automated…

- **[Density-Matrix Reinforcement Learning](https://arxiv.org/abs/2610.17214v1)**
  - *Chiuman Ho*
  - `2026-10-12`
  - What information does a reinforcement learning policy omit? At each state, a standard policy stores one probability per action. It has no place to record how actions relate to each other, such as which pairs go together and which conflict. We ask when this missing structure matte…

- **[OpenDGO: Benchmarking Multi-Agent Organizations Across Diverse Application Domains](https://arxiv.org/abs/2610.17143v1)**
  - *Xunkai Li, Miao Zhang, Zekai Chen et al.*
  - `2026-10-12`
  - Large language model (LLM)-based multi-agent systems are increasingly applied across diverse domains, yet different applications require different forms of agent organization. Existing studies typically adopt predefined organizations, such as Star, Chain, and Tree, or learn commu…

- **[Learning Graded Sparse Mechanisms: A Representation Theorem and Certified Generalization](https://arxiv.org/abs/2610.16537v1)**
  - *Mark Kozdoba, Shie Mannor*
  - `2026-10-12`
  - In a variety of multi-agent and physical environments, an element's update depends strongly on a few other elements and weakly on many, and both the identity and the number of the elements that matter change with the state of the system. Such graded sparse mechanisms are common,…

- **[Transparent Information Flow Modeling for Role-Aware AI Act Assessment](https://arxiv.org/abs/2610.16916v1)**
  - *Mattias Brännström, Themis Dimitra Xanthopoulou, Lili Jiang*
  - `2026-10-12`
  - The European Union's Artificial Intelligence Act introduces a structured framework for governing high-risk AI systems, emphasizing transparency, risk management, and role-specific accountability. However, current assessment practices often rely on monolithic system views or disco…

- **[ProbabilityBench: Model Evaluation and Calibration with Exact Ground-Truth Uncertainty](https://arxiv.org/abs/2610.17016v1)**
  - *Yuyang Dai, Yuting Tang, Futoshi Futami et al.*
  - `2026-10-12`
  - Evaluating model uncertainty on real-world data is challenging because each instance provides only a single observed label, leaving true conditional class probabilities unknown. To address this, we introduce ProbabilityBench, a benchmark that provides exact, instance-level class…

- **[EHR-Bench: A Chinese Multi-Task Benchmark for Recruitment AI](https://arxiv.org/abs/2610.16689v1)**
  - *Ruijia Yang, Bing Xu, Zulong Chen et al.*
  - `2026-10-12`
  - Recruitment applications span diverse operations, from drafting job descriptions and interpreting queries to organizing profiles, assessing fit, and recommending candidates and jobs. Systematic LLM evaluation therefore requires task coverage that reflects this range of business n…

- **[VeriPIE: Checkable Query Plans and Evidence-Guided Selection for Text-to-SQL](https://arxiv.org/abs/2610.17493v1)**
  - *Piyush Jha, Cruise Song, Zhengyu Li et al.*
  - `2026-10-12`
  - Financial Artificial Intelligence (AI) governance and model risk management (MRM) emphasize independent validation, transparency, and effective challenge of AI-generated computations. Text-to-SQL translates natural-language questions into Structured Query Language (SQL), but quer…

- **[Benchmarking Quantum Kernel SVMs for Credit Card Fraud Detection: Performance Realities Under NISQ Constraints](https://arxiv.org/abs/2610.17027v1)**
  - *Hitanshi Arora, Mohit Swarnkar, Aswani Kumar Cherukuri*
  - `2026-10-12`
  - Detecting credit card fraud is notoriously difficult because fraudulent charges make up less than 0.2% of total transactions. Quantum Machine Learning (QML), particularly Quantum Kernel Support Vector Machines (QSVM), promises richer feature representations by embedding classical…

- **[Code-Interactive Visual Reasoning for Financial Candlestick Understanding](https://arxiv.org/abs/2610.16587v1)**
  - *Chenxi Zhang, Youwei Pang, Xiaoqi Zhao et al.*
  - `2026-10-12`
  - Financial candlestick understanding requires locating visual elements, aligning them across trading dates and panels, and combining observations through numerical and financial reasoning. Answer accuracy alone does not reveal whether predictions are supported by chart evidence. W…

- **[Limit Theory for Online Expectile Estimation under Short and Long Range Dependence](https://arxiv.org/abs/2610.16030v1)**
  - *Younghun Lee, Jake Zummo, Wei Biao Wu*
  - `2026-10-12`
  - Expectiles are tail-sensitive distributional summaries with important applications in financial risk measurement and forecasting, yet statistical theory for their online estimation from dependent data remains limited. We study a one-pass, stochastic-gradient algorithm with consta…

- **[Learning to Detect Shifts in Unstructured Data Streams via Monitoring-by-Betting](https://arxiv.org/abs/2610.17399v1)**
  - *Siyu Zhou, Jialin Ouyang, Fan Xia et al.*
  - `2026-10-12`
  - Continuous monitoring of generative AI systems requires detecting distribution shifts in the unstructured data they ingest and generate. Existing monitoring methods typically control false alarms by requiring the discrepancy measure used to detect shifts to be *pre-specified*. Ho…

- **[Reliable Text-to-SQL in Resource-Constrained Settings with Small LLMs via Iterative Retry Workflows](https://arxiv.org/abs/2610.17305v1)**
  - *Bilel Abderrahmane Benziane, Xavier Schepler*
  - `2026-10-12`
  - Large Language Models (LLMs) have recently improved Text-to-SQL generation, but their computational cost can hinder deployment in resource-constrained settings. This paper evaluates the Text-to-SQL capabilities of small and medium open-source LLMs (1B-8B parameters) under a contr…

- **[Learning to Design Convex Relaxations for Nonconvex Optimization](https://arxiv.org/abs/2610.16948v1)**
  - *Jinrun Liu, Bai Yan, Tengfei Liu et al.*
  - `2026-10-12`
  - Convex relaxations make nonconvex optimization tractable by replacing hard nonconvex problems with convex surrogates that give valid bounds. Yet their design is still largely manual: a human expert must decide where to relax, which relaxation to use, and how much formulation grow…

- **[Reinforcement Learning with Hawkes-Structured Networks for Market Making](https://arxiv.org/abs/2610.16524v1)**
  - *Fernando Acero, Philipp Plank, Yufei Zhang*
  - `2026-10-12`
  - Market making under realistic order-flow dynamics is challenging due to the clustered, self-exciting nature of order arrivals, which are naturally modeled by non-Markovian Hawkes processes. We propose a model-free reinforcement learning (RL) framework for market making with gener…

- **[Certified Robustness via Sparse Second-Order Cone Relaxations](https://arxiv.org/abs/2610.16016v1)**
  - *Mohammadreza Maleki, Daniel Sadig, Rushendra Sidibomma et al.*
  - `2026-10-12`
  - Certified robustness is critical for deploying neural networks in safety-sensitive settings, but computing exact certificates typically requires solving nonconvex optimization problems. Practical verifiers use convex relaxations: linear programming (LP) relaxations are scalable b…

- **[The Buffett Effect](https://arxiv.org/abs/2610.17231v1)**
  - *Pawel Robert Smolinski, Siddharth Saridevi*
  - `2026-10-12`
  - We study whether stock disclosures by recognizable investors generate abnormal market reactions beyond the reactions produced by comparable but non-recognizable managers. We define the Buffett effect as the incremental abnormal return to a disclosed new position that is attributa…

- **[Monitoring for Shifts at Unknown Times: Parameter-Free Conditional Conformal Martingales](https://arxiv.org/abs/2610.17343v1)**
  - *Tuo Liu, Drew Prinster, Francesco Orabona*
  - `2026-10-12`
  - Conditional conformal test martingales provide sequential tests for detecting distribution shifts, using a fixed reference dataset to avoid contamination from test-time samples. Prior work used a penalized betting function via online optimization with smoothing, clipping, and oth…

- **[Designing Independent Variation: A Guided Iteration Methodology for Price Experiments in Short, Correlated Panels](https://arxiv.org/abs/2610.17481v1)**
  - *Pedro Cadahia*
  - `2026-10-12`
  - Estimation error in short, correlated pricing panels is dominated by trajectory dispersion rather than sampling noise, creating an identification shortfall that only independently assigned variation can resolve. We propose a guided iteration methodology to decide how much variati…

- **[Asymmetric $q$-Gaussian Distributions from Tsallis Maximum Entropy](https://arxiv.org/abs/2610.16663v1)**
  - *Francesco Cesarone, Massimiliano Corradini, Nicolò Giunta et al.*
  - `2026-10-12`
  - Within the framework of non-extensive statistical mechanics, $q$-Gaussian distributions arise as maximum-entropy solutions of Tsallis entropy under suitable escort moment constraints. Although widely used in physics, biology, geology, finance, and related fields, standard $q$-Gau…

- **[Revocation Is Not Complete at Receipt: An Executable Outcome Contract for Distributed Agent-Tool Gateways](https://arxiv.org/abs/2610.15991v1)**
  - *Lifei Liu, Haoran Yu, Danping Zhang*
  - `2026-10-11`
  - Distributed agent workflows cache delegated authority at tool gateways. Revocation may be reported at issuer commit, transport acknowledgment, or receiver persistence, although none of these observations establishes that all gateways enforced the change or that guarded effects st…

- **[FARL: A Fully Automated Pipeline of RL Interface and Solver Design](https://arxiv.org/abs/2610.15691v1)**
  - *Tianyu Jin, Liuyu Xiang, Chaowen Yang et al.*
  - `2026-10-11`
  - Existing reinforcement learning (RL) largely focuses on optimizing learning algorithms within a pre-defined task formulation, while applying RL to new tasks still relies heavily on human expertise to design the learning pipeline: what an agent observes, how it is rewarded, which…

- **[Agent-Canary-Mas: End-to-End Evaluation of Protocol Risk in Long-Horizon Multi-Agent Systems](https://arxiv.org/abs/2610.15529v1)**
  - *Xiuming Liu, Le Gai, Zhiyuan Chang et al.*
  - `2026-10-11`
  - Agent-to-agent protocols allow LLM agents to discover peers, exchange results, and coordinate tool use. A locally successful protocol attack, however, may be rejected by a later agent or propagated into a consequential task decision. Measuring local exploitability alone leaves th…

- **[AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning](https://arxiv.org/abs/2610.15488v1)**
  - *Peiqi Jiang, Fan Zhang, Xin Xu et al.*
  - `2026-10-11`
  - Formulaic alpha mining seeks interpretable expressions that rank assets by future returns. The task is challenging because it demands simultaneous processing of unstructured market descriptions, historical data, and quantitative evaluation of candidate factors, yet most existing…

- **[More Reasoning Is Not Always Better: Executing Clinical Guidelines with LLMs and Rules](https://arxiv.org/abs/2610.15912v1)**
  - *Xiaoqian Lu, Guangfu Guo, Long Cheng et al.*
  - `2026-10-11`
  - Large language models (LLMs) have shown considerable promise in clinical decision support. However, existing approaches often rely on multi-step reasoning or multi-agent collaboration to execute clinical guidelines, introducing substantial computational overhead without reliably…

- **[Towards Autopilot Labeling for Short Video Content Governance](https://arxiv.org/abs/2610.15687v1)**
  - *Junwen Chen, Hongwei Wang, Zixuan Wang et al.*
  - `2026-10-11`
  - The explosive growth of short videos has presented significant challenges to content governance. Traditional manual labeling is inefficient, slow to iterate, and costly. Therefore, we explore and develop a multi-stage autopilot labeling framework aimed at progressively increasing…

- **[Representation Theorems for Actual Powers over Two-Agent General Concurrent Game Frames](https://arxiv.org/abs/2610.15476v1)**
  - *Zixuan Chen, Fengkui Ju, Thomas Ågotnes*
  - `2026-10-11`
  - One of the most well-known connections between logic and games is Pauly's representation theorem: the induced powers of individuals and coalitions in concurrent game frames correspond, in a precise sense, to a certain class of neighborhood frames. The precise sense here is what i…

- **[Hardware-Assisted Multi-Stage Ransomware Detection with Adaptive Machine Learning](https://arxiv.org/abs/2610.15951v1)**
  - *Salma Aboelmagd, Md. Rakibul Ahasan, Zhixin Pan et al.*
  - `2026-10-11`
  - Ransomware is a fast-escalating privacy threat causing significant financial and data losses worldwide. As attacks grow more sophisticated, traditional static signatures and dynamic behavior analysis struggle to defend. In this paper, we propose an novel framework that couples so…

- **[ProML: Progressive Multi-label Learning](https://arxiv.org/abs/2610.15614v1)**
  - *Yi Kou, Jieting Wang, Yuhua Qian*
  - `2026-10-11`
  - Multi-label learning typically pursues model construction through the joint optimization of label fitting, correlation modeling, and structural regularization. While empirically effective, such a coupled paradigm imposes multiple learning objectives on a single predictive paramet…

- **[Uncovering the Generative Landscape of Diffusion Models: A Spectral-Guided Quality-Diversity Diffusion Framework](https://arxiv.org/abs/2610.15724v1)**
  - *Hannah Janmohamed, Joao Correia, Penousal Machado et al.*
  - `2026-10-11`
  - Denoising Diffusion Probabilistic Models have emerged as powerful generative priors across domains ranging from molecular design to high-resolution image synthesis. However, standard diffusion sampling is inherently biased toward high-likelihood regions, often limiting the divers…


---
*Generated 2026-10-14 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
