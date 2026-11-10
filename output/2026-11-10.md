# Daily Paper Digest — 2026-11-10 (Tuesday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**431 unique papers** (560 topic-entries — cross-topic papers counted once per category)

---

## Agent  (303)

### AAAI

- **[LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042)**
  - *Cheng Yang, Hui Jin, Xinlei Yu et al.*
  - **AAAI 2025** · `2025-11-26`
  - Diagnosing lung cancer typically involves physicians identifying lung nodules in Computed tomography (CT) scans and generating diagnostic reports based on their morphological features and medical expertise. Although advancements have been made in using multimodal large language m…

- **[Rethinking the Reliability of Multi-agent System: A Perspective from Byzantine Fault Tolerance](https://arxiv.org/abs/2511.10400)**
  - *Li-Fan Zheng, Jiawei Chen, Qing-Hong Yin et al.*
  - **AAAI 2025** · `2025-11-13`
  - Ensuring the reliability of agent architectures and effectively identifying problematic agents when failures occur are crucial challenges in multi-agent systems (MAS). Advances in large language models (LLMs) have established LLM-based agents as a major branch of MAS, enabling ma…

- **[Talk2Image: A Multi-Agent System for Multi-Turn Image Generation and Editing](https://arxiv.org/abs/2508.06916)**
  - *Shichao Ma, Yun-He Guo, Jia-Hao Su et al.*
  - **AAAI 2025** · `2025-08-09`
  - Text-to-image generation tasks have driven remarkable advances in diverse media applications, yet most focus on single-turn scenarios and struggle with iterative, multi-turn creative tasks. Recent dialogue-based systems attempt to bridge this gap, but their single-agent, sequenti…

- **[CoDe: Communication Delay-Tolerant Multi-Agent Collaboration via Dual Alignment of Intent and Timeliness](https://arxiv.org/abs/2501.05207)**
  - *Shou-Cheng Song, You-Fang Lin, Sheng Han et al.*
  - **AAAI 2025** · `2025-01-09`
  - Communication has been widely employed to enhance multi-agent collaboration. Previous research has typically assumed delay-free communication, a strong assumption that is challenging to meet in practice. However, real-world agents suffer from channel delays, receiving messages se…


### NeurIPS

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **NeurIPS 2025** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…

- **[STRATUS: A Multi-agent System for Autonomous Reliability Engineering of Modern Clouds](https://arxiv.org/abs/2506.02009)**
  - *Yin-Fang Chen, Jia-Qi Pan, Jackson Clark et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - In cloud-scale systems, failures are the norm. A distributed computing cluster exhibits hundreds of machine failures and thousands of disk failures; software bugs and misconfigurations are reported to be more frequent. The demand for autonomous, AI-driven reliability engineering…

- **[MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement](https://arxiv.org/abs/2506.15692)**
  - *Jaehyun Nam, Jinsung Yoon, Jie-Feng Chen et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - Agents based on large language models (LLMs) for machine learning engineering (MLE) can automatically implement ML models via code generation. However, existing approaches to build such agents often rely heavily on inherent LLM knowledge and employ coarse exploration strategies t…

- **[Distilling LLM Agent into Small Models with Retrieval and Code Tools](https://arxiv.org/abs/2505.17612)**
  - *Minki Kang, Jongwon Jeong, Seanie Lee et al.*
  - **NeurIPS 2025** · `2025-05-23`
  - Large language models (LLMs) excel at complex reasoning tasks but remain computationally expensive, limiting their practical deployment. To address this, recent works have focused on distilling reasoning capabilities into smaller language models (sLMs) using chain-of-thought (CoT…

- **[AutoData: A Multi-Agent System for Open Web Data Collection](https://arxiv.org/abs/2505.15859)**
  - *Tian-Yi Ma, Yi-Yue Qian, Zhe-Yuan Zhang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - The exponential growth of data-driven systems and AI technologies has intensified the demand for high-quality web-sourced datasets. While existing datasets have proven valuable, conventional web data collection approaches face significant limitations in terms of human effort and…

- **[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)**
  - *Yuan-Te Li, Xu Yang, Xiao Yang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - Financial markets pose fundamental challenges for asset return prediction due to their high dimensionality, non-stationarity, and persistent volatility. Despite advances in large language models and multi-agent systems, current quantitative research pipelines suffer from limited…

- **[MLZero: A Multi-Agent System for End-to-end Machine Learning Automation](https://arxiv.org/abs/2505.13941)**
  - *Hao-Yang Fang, Bo-Ran Han, Nick Erickson et al.*
  - **NeurIPS 2025** · `2025-05-20`
  - Existing AutoML systems have advanced the automation of machine learning (ML); however, they still require substantial manual configuration and expert input, particularly when handling multimodal data. We introduce MLZero, a novel multi-agent framework powered by Large Language M…

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

- **[Can Frontier Auto Researchers Reconstruct Human Research Decisions in AI?](https://arxiv.org/abs/2611.12429v1)**
  - *Shengyun Si, Junjie Chu, Ye Leng et al.*
  - **ICLR** · `2026-11-09`
  - Scientific research has long been driven by substantial human effort, from reviewing prior work and identifying research gaps to designing specific solutions. Recent advances in harness-based agent systems have given rise to increasingly capable Auto Researchers, which can autono…

- **[RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents](https://arxiv.org/abs/2510.02609)**
  - *Cheng-Quan Guo, Chulin Xie, Yu Yang et al.*
  - **ICLR 2025** · `2025-10-02`
  - Code agents have gained widespread adoption due to their strong code generation capabilities and integration with code interpreters, enabling dynamic execution, debugging, and interactive programming capabilities. While these advancements have streamlined complex workflows, they…

- **[PixelCraft: A Multi-Agent System for High-Fidelity Visual Reasoning on Structured Images](https://arxiv.org/abs/2509.25185)**
  - *Shuoshuo Zhang, Zijian Li, Yi-Zhe Zhang et al.*
  - **ICLR 2025** · `2025-09-29`
  - Structured images (e.g., charts and geometric diagrams) remain challenging for multimodal large language models (MLLMs), as perceptual slips can cascade into erroneous conclusions. Intermediate visual cues can steer reasoning; however, existing cue-based methods are constrained w…

- **[From What to Why: A Multi-Agent System for Evidence-based Chemical Reaction Condition Reasoning](https://arxiv.org/abs/2509.23768)**
  - *Cheng Yang, Jia-Xuan Lu, Hai-Yuan Wan et al.*
  - **ICLR 2025** · `2025-09-28`
  - The chemical reaction recommendation is to select proper reaction condition parameters for chemical reactions, which is pivotal to accelerating chemical science. With the rapid development of large language models (LLMs), there is growing interest in leveraging their reasoning an…

- **[Visual Multi-Agent System: Mitigating Hallucination Snowballing via Visual Flow](https://arxiv.org/abs/2509.21789)**
  - *Xin-Lei Yu, Cheng-Ming Xu, Gui-Min Zhang et al.*
  - **ICLR 2025** · `2025-09-26`
  - Multi-Agent System (MAS) powered by Visual Language Models (VLMs) enables challenging tasks but suffers from a novel failure term, multi-agent visual hallucination snowballing, where hallucinations are seeded in a single agent and amplified by following ones due to the over-relia…

- **[CoAct-1: Computer-using Multi-agent System with Coding Actions](https://arxiv.org/abs/2508.03923)**
  - *Linxin Song, Yu-Tong Dai, Viraj Prabhu et al.*
  - **ICLR 2025** · `2025-08-05`
  - Autonomous agents that operate computers via Graphical User Interfaces (GUIs) often struggle with efficiency and reliability on complex, long-horizon tasks. While augmenting these agents with planners can improve task decomposition, they remain constrained by the inherent limitat…

- **[OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://arxiv.org/abs/2507.06134)**
  - *S. Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou et al.*
  - **ICLR 2025** · `2025-07-08`
  - Recent advances in AI agents capable of solving complex, everyday tasks, from scheduling to customer service, have enabled deployment in real-world settings, but their possibilities for unsafe behavior demands rigorous evaluation. While prior benchmarks have attempted to assess a…

- **[Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning](https://arxiv.org/abs/2504.17192)**
  - *Minju Seo, Jinheon Baek, Seongyun Lee et al.*
  - **ICLR 2025** · `2025-04-24`
  - Despite the rapid growth of machine learning research, corresponding code implementations are often unavailable, making it slow and labor-intensive for researchers to reproduce results and build upon prior work. In the meantime, recent Large Language Models (LLMs) excel at unders…


### CVPR

- **[Refer-Agent: A Collaborative Multi-Agent System with Reasoning and Reflection for Referring Video Object Segmentation](https://arxiv.org/abs/2602.03595)**
  - *Hai-Chao Jiang, Tian-Ming Liang, Wei-Shi Zheng et al.*
  - **CVPR 2026** · `2026-02-03`
  - Referring Video Object Segmentation (RVOS) aims to segment objects in videos based on textual queries. Current methods mainly rely on large-scale supervised fine-tuning (SFT) of Multi-modal Large Language Models (MLLMs). However, this paradigm suffers from heavy data dependence a…


### KDD

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, A. Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…


### ACL

- **[MIRIX-2.0: Multi-Agent Memory System](https://arxiv.org/abs/2611.12068)**
  - *Wei-Chieh Huang, Weizhi Zhang, Jiayan Nan et al.*
  - **ACL** · 🤗 · `2026-11-09`
  - Long-term memory lets LLM agents personalize, stay consistent, and reuse what worked before. Parametric memories need training, consolidation can lose details for good, and keeping every record leaves a growing store to search. We present MIRIX-2.0, a multi-agent memory system de…

- **[Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards](https://arxiv.org/abs/2611.12728v1)**
  - *Brendan P. Murphy, Agustina Saenz*
  - **ACL** · `2026-11-09`
  - Reinforcement learning with verifiable rewards is increasingly used to improve language model reasoning, yet its effects on sequential decision procedures remain poorly understood. We study this problem in clinical multi-turn agents that must decide what information to request, w…

- **[Embodied First Exam](https://arxiv.org/abs/2611.12177v1)**
  - *Kangrui Wang, Qineng Wang, Changhe Chen et al.*
  - **ACL** · `2026-11-09`
  - Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical…

- **[Silinx: An Open, Browser-Based HDL Design Platform for Teaching Digital Systems on FPGA Boards](https://arxiv.org/abs/2611.11741v1)**
  - *Pedro Malo*
  - **ACL** · `2026-11-09`
  - Many digital systems courses teach on FPGA boards whose vendor tool is no longer maintained: the Digilent Basys2 and Nexys2 (Xilinx Spartan-3E) and Nexys3 and Atlys (Spartan-6) need Xilinx ISE 14.7, discontinued since 2013 and hard to install on the computers and tablets students…

- **[Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization](https://arxiv.org/abs/2611.12079v1)**
  - *Jui-Chien Tsou, Po-Yi Wu*
  - **ACL** · `2026-11-09`
  - We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels. On 30 KernelBench tasks (levels 1-3, first 10 each, evaluated on a V100), we co…

- **[Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models](https://arxiv.org/abs/2611.11571v1)**
  - *Mustafa S. Aljumaily, Nawar S. Alseelawi, Raghad Alshabandar*
  - **ACL** · `2026-11-08`
  - Tool-using LLM agents act on instructions embedded in the data they read, so prompt injection is a structural rather than a prompt-wording problem. We compare in-prompt defences (hardened prompts, spotlighting, LLM detectors) with deterministic enforcement outside the model (four…

- **[Replay Fidelity in LLM Agent Evaluation: Randomness, Hidden State, and Test Oracles in AppWorld](https://arxiv.org/abs/2611.11216v1)**
  - *You Liu, Quanchao Lu*
  - **ACL** · `2026-11-08`
  - Reproducibility in large language model (LLM) agent evaluation depends on replay fidelity: which parts of an execution trace are reconstructed, controlled, and compared. This matters for agent debugging, failure analysis, and counterfactual evaluation of stateful tool use. We aud…

- **[PatternBloom: Empowering Agentic RAG with Externalized RL-Distilled Graph Patterns](https://arxiv.org/abs/2611.10477v1)**
  - *Yi Ge, Heng Huang*
  - **ACL** · `2026-11-07`
  - Reinforcement-learning-trained agents for retrieval-augmented generation retrieve content (passages, knowledge-graph fragments, or hyperedges) and supervise training with outcome rewards on the final answer. Across these paradigms the reasoning route through retrieved content nev…

- **[ParaCodex: A Profiling-Guided Autonomous Coding Agent for Reliable Parallel Code Generation and Translation](https://arxiv.org/abs/2601.04327)**
  - *Erel Kaplan, Tomer Bitan, Lian Ghrayeb et al.*
  - **ACL 2026** · `2026-01-07`
  - Parallel programming is central to HPC and AI, but producing code that is correct and fast remains challenging, especially for OpenMP GPU offload, where data movement and tuning dominate. Autonomous coding agents can compile, test, and profile on target hardware, but outputs are…

- **[DeepSynth-Eval: Objectively Evaluating Information Consolidation in Deep Survey Writing](https://arxiv.org/abs/2601.03540)**
  - *Hong-Zhi Zhang, Yuan-Ze Hu, Tinghai Zhang et al.*
  - **ACL 2026** · `2026-01-07`
  - The evolution of Large Language Models (LLMs) towards autonomous agents has catalyzed progress in Deep Research. While retrieval capabilities are well-benchmarked, the post-retrieval synthesis stage--where agents must digest massive amounts of context and consolidate fragmented e…

- **[Multi-Docker-Eval: A 'Shovel of the Gold Rush' Benchmark on Automatic Environment Building for Software Engineering](https://arxiv.org/abs/2512.06915)**
  - *Kelin Fu, Tian-Yu Liu, Zeyu Shang et al.*
  - **ACL 2025** · `2025-12-07`
  - Automated environment configuration is a critical bottleneck in scaling software engineering (SWE) automation. To provide a reliable evaluation standard for this task, we present Multi-Docker-Eval benchmark. It includes 40 real-world repositories spanning 9 programming languages…

- **[AnnaAgent: Dynamic Evolution Agent System with Multi-Session Memory for Realistic Seeker Simulation](https://arxiv.org/abs/2506.00551)**
  - *Ming Wang, Pei-Dong Wang, Lin Wu et al.*
  - **ACL 2025** · `2025-05-31`
  - Constrained by the cost and ethical concerns of involving real seekers in AI-driven mental health, researchers develop LLM-based conversational agents (CAs) with tailored configurations, such as profiles, symptoms, and scenarios, to simulate seekers. While these efforts advance A…

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

- **[NetSafe: Exploring the Topological Safety of Multi-agent System](https://aclanthology.org/2025.findings-acl.150.pdf)**
  - *Miao Yu, Shilong Wang, Gui-Bin Zhang et al.*
  - **ACL 2025**
  - ,

- **[Qwen2.5-xCoder: Multi-Agent Collaboration for Multilingual Code Instruction Tuning](https://aclanthology.org/2025.acl-long.642.pdf)**
  - *Jian Yang, Wei Zhang, Yi-Bo Miao et al.*
  - **ACL 2025**
  - ,


### EMNLP

- **[DR3-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://arxiv.org/abs/2604.14683)**
  - *Qian-Qian Xie, He Zhu, Xue Han et al.*
  - **EMNLP 2026** · `2026-04-16`
  - Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR$^{3…

- **[FinDeepForecast: A Live Multi-Agent System for Benchmarking Deep Research Agents in Financial Forecasting](https://arxiv.org/abs/2601.05039)**
  - *Xiang-Yu Li, Xuan Yao, Guo-Hao Qi et al.*
  - **EMNLP 2026** · `2026-01-08`
  - Deep Research (DR) Agents powered by advanced Large Language Models (LLMs) have fundamentally shifted the paradigm for completing complex research tasks. Yet, a comprehensive and live evaluation of their forecasting performance on real-world, research-oriented tasks in high-stake…

- **[QuantAgents: Towards Multi-agent Financial System via Simulated Trading](https://arxiv.org/abs/2510.04643)**
  - *Xiang-Yu Li, Ya-Wen Zeng, Xiao-Fen Xing et al.*
  - **EMNLP 2025** · `2025-10-06`
  - In this paper, our objective is to develop a multi-agent financial system that incorporates simulated trading, a technique extensively utilized by financial professionals. While current LLM-based agent models demonstrate competitive performance, they still exhibit significant dev…

- **[AMAS: Adaptively Determining Communication Topology for LLM-based Multi-Agent System](https://arxiv.org/abs/2510.01617)**
  - *Hui Yi Leong, Yuheng Li, Yu-Qing Wu et al.*
  - **EMNLP 2025** · `2025-10-02`
  - Although large language models (LLMs) have revolutionized natural language processing capabilities, their practical implementation as autonomous multi-agent systems (MAS) for industrial problem-solving encounters persistent barriers. Conventional MAS architectures are fundamental…

- **[Enhancing Multi-Agent Debate System Performance via Confidence Expression](https://arxiv.org/abs/2509.14034)**
  - *Zijie Lin, Bryan Hooi*
  - **EMNLP 2025** · `2025-09-17`
  - Generative Large Language Models (LLMs) have demonstrated remarkable performance across a wide range of tasks. Recent research has introduced Multi-Agent Debate (MAD) systems, which leverage multiple LLMs to simulate human debate and thereby improve task performance. However, whi…

- **[Code Like Humans: A Multi-Agent Solution for Medical Coding](https://arxiv.org/abs/2509.05378)**
  - *A. Motzfeldt, Joakim Edin, Casper L. Christensen et al.*
  - **EMNLP 2025** · `2025-09-04`
  - In medical coding, experts map unstructured clinical notes to alphanumeric codes for diagnoses and procedures. We introduce Code Like Humans: a new agentic framework for medical coding with large language models. It implements official coding guidelines for human experts, and it…

- **[ScreenCoder: Advancing Visual-to-Code Generation for Front-End Automation via Modular Multimodal Agents](https://arxiv.org/abs/2507.22827)**
  - *Yi-Lei Jiang, Yaozhi Zheng, Yuxuan Wan et al.*
  - **EMNLP 2025** · `2025-07-30`
  - Automating the transformation of user interface (UI) designs into front-end code holds significant promise for accelerating software development and democratizing design workflows. While multimodal large language models (MLLMs) can translate images to code, they often fail on com…

- **[MT-Mol:Multi Agent System with Tool-based Reasoning for Molecular Optimization](https://arxiv.org/abs/2505.20820)**
  - *Hyomin Kim, Yun-Hui Jang, Sungsoo Ahn*
  - **EMNLP 2025** · `2025-05-27`
  - Large language models (LLMs) have large potential for molecular optimization, as they can gather external chemistry tools and enable collaborative interactions to iteratively refine molecular candidates. However, this potential remains underexplored, particularly in the context o…

- **[ReSo: A Reward-driven Self-organizing LLM-based Multi-Agent System for Reasoning Tasks](https://arxiv.org/abs/2503.02390)**
  - *Heng Zhou, He-Jia Geng, Xiangyuan Xue et al.*
  - **EMNLP 2025** · `2025-03-04`
  - Multi-agent systems (MAS) have emerged as a promising approach for enhancing the reasoning capabilities of large language models in complex problem-solving; however, current MAS frameworks suffer from poor flexibility and scalability with underdeveloped optimization strategies. T…

- **[Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)**
  - *Samuel Schmidgall, Yu-Sheng Su, Ze Wang et al.*
  - **EMNLP 2025** · `2025-01-08`
  - Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory, an…


### NAACL

- **[Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://arxiv.org/abs/2502.10857)**
  - *Haoyuan Wu, Haisheng Zheng, Zhuo-Lun He et al.*
  - **NAACL 2025** · `2025-02-15`
  - Recently, with the development of tool-calling capabilities in large language models (LLMs), these models have demonstrated significant potential for automating electronic design automation (EDA) flows by interacting with EDA tool APIs via EDA scripts. However, considering the li…

- **[CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging](https://arxiv.org/abs/2502.05664)**
  - *Md. Ashraful Islam, Mohammed Eunus Ali, Md. Rizwan Parvez*
  - **NAACL 2025** · `2025-02-08`
  - Large Language Models (LLMs) have made significant strides in code generation and problem solving. Current approaches employ external tool-based iterative debuggers that use compiler or other tool-based runtime feedback to refine coarse programs generated by various methods. Howe…

- **[MASTER: A Multi-Agent System with LLM Specialized MCTS](https://arxiv.org/abs/2501.14304)**
  - *Bing-Zheng Gan, Yu-Fan Zhao, Tian-Yi Zhang et al.*
  - **NAACL 2025** · `2025-01-24`
  - Large Language Models (LLM) are increasingly being explored for problem-solving tasks. However, their strategic planning capability is often viewed with skepticism. Recent studies have incorporated the Monte Carlo Tree Search (MCTS) algorithm to augment the planning capacity of L…

- **[A Layered Debating Multi-Agent System for Similar Disease Diagnosis](https://aclanthology.org/2025.naacl-short.46.pdf)**
  - *Yu-Tian Zhao, Hui-Min Wang, Ye-Feng Zheng et al.*
  - **NAACL 2025**
  - Distinguishing between extremely similar diseases is a critical and challenging aspect of clinical decision-making. Traditional classification, contrastive learning, and Large Language Models (LLMs) based methods fail to detect the subtle clues necessary for differentiation. This…


### Other / arXiv

- **[Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning](https://arxiv.org/abs/2611.12886)**
  - *Haozhi Yuan, Handong Li, Yifan Zhang et al.*
  - 🤗 Featured · `2026-11-09`

- **[How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time](https://arxiv.org/abs/2611.12324)**
  - *Ku Onoda, Haruto Kawano, Shota Takashiro et al.*
  - 🤗 Featured · `2026-11-09`
  - World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction. A mechanic is a rule for how an action or an interaction changes part of the environment. Each occurrence of a mechanic…

- **[InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure](https://arxiv.org/abs/2611.11558)**
  - *InfraRSI Team, Yuchuan Tian, Haocheng Mei et al.*
  - 🤗 Featured · `2026-11-08`
  - While Recursive Self-Improvement (RSI) accelerates isolated algorithm and kernel synthesis, distributed LLM training depends on tightly coupled launch settings, operator kernels, and communication schedules, where single edits often hit out-of-memory (OOM) boundaries, compiler co…

- **[SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI](https://arxiv.org/abs/2611.08935)**
  - *Jing Hao, Weinan Zhou, Zhihong Lu et al.*
  - 🤗 Featured · `2026-11-06`

- **[FlyHash for LLM Agent Memory: An Empirical Validation and a New Application](https://arxiv.org/abs/2611.05791)**
  - *Mohan Bheemadolu, Chrisogonas O. Odhiambo*
  - 🤗 Featured · `2026-11-04`

- **[Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](https://arxiv.org/abs/2611.01112)**
  - *Chengcheng Wang, Yuheng Shi, Siyu Xu et al.*
  - 🤗 Featured · `2026-10-31`

- **[AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations](https://arxiv.org/abs/2610.36980)**
  - *Qiming Shi, Yikun Li, Beidi Luan et al.*
  - 🤗 Featured · `2026-10-27`

- **[Learning to Act with World Models by Valuing What Comes Next](https://arxiv.org/abs/2611.12200)**
  - *Chenghao Gao, Zhi Zhang, Dian Jin et al.*
  - 🤗 · `2026-11-09`
  - A sparse terminal reward tells an agent little about its steps. Much of the missing information is implicit in the environment's dynamics, because each state transition can change the conditions for success long before the reward arrives. A world model trained on real transitions…

- **[Teamknitt: Configuring, Observing and Intervening in LLM-Agent Teams through the Lens of Dynamical-Systems and Human-Team Theory](https://arxiv.org/abs/2611.12545)**
  - *Goran Mitevski*
  - 🤗 · `2026-11-09`
  - Most frameworks for teams of large language model (LLM) agents fix the team's shape inside the software: who talks to whom, how much is passed along, and what a human can do once a run has started. Human-team research has long asked those questions: where team phenomena live (in…

- **[FraudBench: A Legal Evaluation of AI Deception](https://arxiv.org/abs/2611.12167)**
  - *Kevin Wei, Sumaya Nur Adan, Stephan Llerena et al.*
  - 🤗 · `2026-11-09`
  - We introduce FraudBench, an evaluation of large language models' (LLMs) propensities to recommend, assist, or directly take actions that would constitute fraud under U.S. law. Our evaluation contains a novel dataset of 159 scenarios based on real-world U.S. court cases and valida…

- **[Review the Episodes, Refine the Lessons: Simple Memory Evolution for Embodied Agents](https://arxiv.org/abs/2611.11509)**
  - *Yifei Yao, Yude Zou, Xing Gao et al.*
  - 🤗 · `2026-11-08`
  - Recent studies of embodied agents based on frontier multimodal large language models (MLLMs) develop harness engineering around the MLLM, such as harnesses with post-trained policies and recursive self-improvement loops. Yet whether these additions exceed the native capability of…

- **[Coding or Cheating? An Investigation of Frontier Coding LLMs](https://arxiv.org/abs/2611.10404)**
  - *Yuntao Gui*
  - 🤗 · `2026-11-07`
  - Frontier agentic LLMs are trained on verifiable rewards in reinforcement learning (RL) environments built from real software repositories. A passing test suite is treated as the reward for solving the task. We show that, on hard problems, frontier models often satisfy these rewar…

- **[MotionGraphicsBench: Evaluating Motion Graphics Generation with Programmatic Verification](https://arxiv.org/abs/2611.10592)**
  - *Jiaju Ma, Ashvini Kumar Jindal, Chuhua Wang et al.*
  - 🤗 · `2026-11-07`
  - Large language models can generate motion graphics from static images and natural language requests, but it remains difficult to evaluate how well models can follow requests that combine spatial, appearance, and temporal requirements. We introduce MotionGraphicsBench, an expert-c…

- **[Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use](https://arxiv.org/abs/2611.09113)**
  - *Chuxue Cao, Jingru Zeng, Boqin Yin et al.*
  - 🤗 · `2026-11-06`

- **[HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents](https://arxiv.org/abs/2611.12872v1)**
  - *Haozhen Zhang, Bohan Liu, Jianzhu Bao et al.*
  - `2026-11-09`
  - As multimodal agents accumulate increasingly long interaction histories, effectively retrieving and utilizing past information becomes critical for long-term interaction. Existing memory systems typically rely on semantic retrieval over compressed memories and expose predefined r…

- **[Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning](https://arxiv.org/abs/2611.12865v1)**
  - *Xinjie Shen*
  - `2026-11-09`
  - Reinforcement learning (RL) can improve an agent's task capability while reinforcing behavior that violates contextual execution requirements. We study this reward-driven misalignment, including reward hacking, through verifiable reward--context conflicts, where compliant task co…

- **[Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks](https://arxiv.org/abs/2611.12799v1)**
  - *Tingcheng Bian, Kangye Gong, Jinchang Luo et al.*
  - `2026-11-09`
  - Reinforcement learning is now the mainstream paradigm for training LLMs on agentic tasks, yet standard practice keeps only the best-validation checkpoint and discards the rest. We show that this is lossy: in GRPO training of LLM agents, the best-validation checkpoint fails on pro…

- **[Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You](https://arxiv.org/abs/2611.12705v1)**
  - *Benjamin Chang, Dell Zhang*
  - `2026-11-09`
  - When AI agents screen items for a costly human assessor, as in agentic search, e-discovery and AI reviewing of papers, only what they pass gets judged. We show what each kind of evidence can establish about their errors, even with unlimited data. Agreement shows that agents concu…

- **[WanderBench: Can World Models Explore Dynamic Worlds from Video?](https://arxiv.org/abs/2611.12557v1)**
  - *Yuhang Chen, Jiheng Li, Jiale Wang et al.*
  - `2026-11-09`
  - Video world models conditioned on an input video make it possible to explore real, recorded dynamic scenes, enabling re-shooting of footage, free-viewpoint replay, and real-to-sim environments for embodied agents. Such uses require the generated rollout to stay faithful to the re…

- **[SciMARS: Multi-Agent Recursive Self-Improvement for Closed-Loop Scientific Discovery](https://arxiv.org/abs/2611.12552v1)**
  - *Weimin Wu, Han Liu*
  - `2026-11-09`
  - We propose SciMARS, a framework for recursive task-local adaptation of multi-agent harnesses in closed-loop scientific discovery. Multi-agent systems coordinate analysis, experimental design, and verification as scientific evidence evolves. However, two problems limit their effec…

- **[Perceived Agency During Agent-Avatar Control Transitions in Virtual Reality](https://arxiv.org/abs/2611.12529v1)**
  - *Jingyi Zhang, Anthony Steed*
  - `2026-11-09`
  - Prior beliefs about whether a virtual human (VH) is controlled by a human or a computer can shape how users interpret and respond to its behaviour. As emerging hybrid VH systems allow control to transfer between human operators and computer programs during an ongoing interaction,…

- **[AutoBuddy: Evaluating Proactive, Always-On Agents on Task Discovery and Execution in a Simulated Workplace](https://arxiv.org/abs/2611.12393v1)**
  - *Shiqi Chen, Daniel Madrigal Diaz, Wei-Ning Chen et al.*
  - `2026-11-09`
  - As LLM agents become more autonomous, they are increasingly expected to run as always-on assistants on a user's behalf, identifying work to be done and completing it without being asked. Yet existing benchmarks usually give the agent its task, whereas in knowledge work the reques…

- **[Say Shibboleth: Fingerprinting the LLMs and Harnesses Behind Agentic Attacks](https://arxiv.org/abs/2611.12386v1)**
  - *Dario Pasquini, Reworr, Giuseppe Ateniese et al.*
  - `2026-11-09`
  - We study the fingerprinting of agentic cyberattacks. Our objective is to reliably infer information about the attacker's configuration, such as LLM version and harness, from telemetry. To achieve this, we introduce a technique we call shibboleth traps: modular honeypot services d…

- **[Detecting Shadow AI: Unsanctioned LLM Agents on Enterprise Endpoints: A Taxonomy, an Open Detector and a Controlled Evaluation](https://arxiv.org/abs/2611.12377v1)**
  - *Jeremy Canale, Fabien Soulis*
  - `2026-11-09`
  - Shadow IT, the use of technology that the IT organisation has not approved, is a long-standing governance problem. We argue that autonomous AI agents can make it grow much faster: agents make building tools nearly free, act with their user's privileges, and leave behind scripts,…

- **[AMSchem: Automated Schematic Visualization of AMS Circuits via Verifiable Agentic Generation](https://arxiv.org/abs/2611.12333v1)**
  - *Yichen Shi, Zhiyuan Wang, Jianing Cui et al.*
  - `2026-11-09`
  - For decades, the netlist-to-schematic gap has remained a persistent challenge in design automation, especially for analog and mixed-signal (AMS) circuits. Netlists encode connectivity, not visual presentation, making their manual conversion into readable schematics time-consuming…

- **[A Modular Perspective for Modeling MARL Systems](https://arxiv.org/abs/2611.12314v1)**
  - *Tiziano Maisonhaute, Jean-Christophe Soulié, Fabien Michel*
  - `2026-11-09`
  - The growing complexity of Multi-Agent Reinforcement Learning (MARL) has fragmented the literature, obscuring underlying architectural choices behind diverse implementations. This fragmentation makes it difficult to evaluate critical modeling dimensions in isolation, identify how…

- **[Reconfigurable Action Theories: A Formal Foundation for Dynamically Composable Agent Harnesses](https://arxiv.org/abs/2611.12300v1)**
  - *Jianmin Ji*
  - `2026-11-09`
  - Action theories typically fix their vocabulary and causal laws, whereas agent harnesses can change their tools, providers, and policies during execution. We introduce Reconfigurable Action Theories (RAT), in which actions can change the action theory itself. A theory module in RA…

- **[ECOS: Environment-Calibrated On-Policy Self-Distillation for Language Agents](https://arxiv.org/abs/2611.12232v1)**
  - *Chenhao Zhang, Zhongan Wang, Mingxuan Li et al.*
  - `2026-11-09`
  - On-policy self-distillation lets a language agent act as its own Teacher by conditioning on privileged context such as skills written from its own trajectories. Its guidance, however, is weighted by how much this context shifts token likelihoods rather than by whether it improves…

- **[PARIS: A multi-agent LLM framework for end-to-end, PRISMA-guided systematic literature reviews with pre-synthesis corpus quality assessment](https://arxiv.org/abs/2611.12222v1)**
  - *Christophe Cruz, Hussam Ghanem, Samir Jabbar et al.*
  - `2026-11-09`
  - Systematic literature reviews (SRs) remain slow and labor-intensive, and most automation tools address single stages of the workflow. We present PARIS (PRISMA Agentic Research Intelligence System), an open-source framework in which a conductor agent running in Claude Code orchest…

- **[GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation](https://arxiv.org/abs/2611.12175v1)**
  - *Jinghe Wang, Xinrui Cao, Duo Wu et al.*
  - `2026-11-09`
  - Robotic manipulation has advanced rapidly in mapping visual observations and language instructions to actions. However, reliable manipulation in open-world environments requires robust spatial understanding: the ability to identify targets in complex layouts (spatial reasoning) a…

- **[Let the Fixer Decide: Training a Code Localizer from the Fixer's Likelihood](https://arxiv.org/abs/2611.12164v1)**
  - *Khalil Hennara, Muhammad Hreden, Zeina Aldallal et al.*
  - `2026-11-09`
  - Code localizers are usually trained to predict the files a reference patch edits, but the code a fixer needs to read is not the same as the code it changes. We propose Fixer-Guided Localization (FGL): the localizer proposes several localizations, a frozen fixer scores each by how…

- **[Toward Sustainable Agentic AI: Carbon Tradeoffs Across Iterative Self-Refinement and Tool-Augmented Coding](https://arxiv.org/abs/2611.12128v1)**
  - *Boris Ruf, Adrien de Mailly Nesle, Marcin Detyniecki*
  - `2026-11-09`
  - Agentic language model systems can improve performance either by iterating on their own outputs or by using external tools in grounded environments. While these strategies can reduce error rates and substitute for larger models in some settings, their environmental cost remains r…

- **[CARE-PO: Controllable Tool-Call Efficiency for LLM Agents](https://arxiv.org/abs/2611.12125v1)**
  - *Xiaoyang Ye, Xiao Yao, Hairui Zhu et al.*
  - `2026-11-09`
  - External tool calls are a major running cost of an LLM agent, while its training objectives align almost exclusively with task completion. In a step-level diagnosis of Qwen3.5 trajectories at two model sizes on GAIA, a long-horizon tool-use benchmark, we find that most contain re…

- **[System Optimizations for Cost-Efficient Agent Harnesses](https://arxiv.org/abs/2611.12122v1)**
  - *Jongseok Park, Jiaxiang Yu, Eric Zhou et al.*
  - `2026-11-09`
  - AI agent harnesses play the critical role of providing LLMs with an interface to a computing environment. Recent studies show that AI agents' task-execution accuracy depends mostly on the LLM used, while harness-side variances such as system prompts or tools have minimal impact.…

- **[SCALE: Small-Model-First Concept Abstraction with LLM-Guided Experience Internalization](https://arxiv.org/abs/2611.12120v1)**
  - *Hong Su*
  - `2026-11-09`
  - Autonomous agents must continually acquire reusable knowledge from experience without relying on costly large language model (LLM) reasoning for every decision. However, existing experience-based approaches often struggle to transform accumulated observations and reasoning into c…

- **[Joi-Bench-Task: Benchmarking Task Coordination in Full-duplex Voice Agents through Interactive Simulation](https://arxiv.org/abs/2611.12118v1)**
  - *Xiangheng He, Mingjun Zhao, Zhehao Fan et al.*
  - `2026-11-09`
  - Full-duplex voice agents enable natural, hands-free interaction, allowing users to refine requests, redirect ongoing work, and seek clarification while the agent is speaking. However, existing voice-agent benchmarks insufficiently isolate coordination between task execution and c…

- **[OGDA: Ontology-Grounded Data Agents for Reliable Analysis over Heterogeneous Data Lakes](https://arxiv.org/abs/2611.12114v1)**
  - *Boyi Zhang, Hong Ting Tsang, Yisen Gao et al.*
  - `2026-11-09`
  - Full-pipeline data analysis over real-world data lakes requires LLM agents to locate and integrate information across large collections of tables with different schemas. Existing data agents follow task-specific exploration, which exhausts the context window in massive lakes. As…

- **[From Fluent Text to Ontology-Compatible Definitions: A Quality-Control Agentic Workflow](https://arxiv.org/abs/2611.12095v1)**
  - *Kun Feng, Chenchen Chu, Yan Liu et al.*
  - `2026-11-09`
  - Biomedical ontologies are structured knowledge systems that must evolve continuously to represent newly emerging knowledge, but their manual maintenance remains time-consuming and laborintensive. Textual definitions are especially costly because they must be readable to humans an…

- **[CRAFT-AI: Capability and Requirement Alignment for Flexible Manufacturing through Agentic AI](https://arxiv.org/abs/2611.12092v1)**
  - *Kiavash Fathi, Hans Wernher van de Venn*
  - `2026-11-09`
  - One of the fundamental needs for reaching resilient production infrastructure is flexible manufacturing, which requires translating changing production requirements into implementable system configurations. This paper introduces \textbf{CRAFT-AI}, an agentic AI approach combining…

- **[Zero-Search Reinforcement Learning for Slay the Spire 2 with Failure-Driven Restarts](https://arxiv.org/abs/2611.12088v1)**
  - *Xiangqin Chen, Zhengxuan Xie*
  - `2026-11-09`
  - Slay the Spire 2 (STS2) is a deck-building roguelike in which a winning run at the highest difficulty takes several hundred decisions, and most losses happen in late boss fights that a learner seldom reaches. We train agents that choose every action with one forward pass of a 6.6…

- **[BECON: Belief-Conditioned Constrained Multi-Objective Reinforcement Learning under Drifting Preferences and Budgets](https://arxiv.org/abs/2611.12053v1)**
  - *Bui Trong Duc, Huynh Thi Thanh Binh*
  - `2026-11-09`
  - Constrained preference-conditioned MORL typically assumes full task observability, treating preferences and safety budgets as stationary task signals. In real-world deployment, however, these signals are often unreliable proxies: intent may drift, safety tolerances may shift with…

- **[Evaluating AI Agents for Industrial-Level Chip Floorplanning: A Framework and Empirical Study](https://arxiv.org/abs/2611.12048v1)**
  - *Nova-Silicon Team*
  - `2026-11-09`
  - Floorplanning is an early step in turning a logical circuit into a physical chip: it positions large circuit modules and constrains the space available for subsequent logic placement and wiring. These decisions affect congestion and timing, but their physical consequences emerge…

- **[Benchmarking language models and agents for scientific reasoning in evolving materials laboratories](https://arxiv.org/abs/2611.12014v1)**
  - *Xuyu Dong, Yixuan Li, Jianguo Huang et al.*
  - `2026-11-09`
  - Large language models and the multi-agent systems built around them could accelerate materials discovery by connecting scientific knowledge with experimental decisions. Existing benchmarks establish capabilities in domain knowledge, multimodal interpretation and scientific tool u…

- **[Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization](https://arxiv.org/abs/2611.11995v1)**
  - *Zhengyu Hu, Zheyuan Xiao, Yike Wang et al.*
  - `2026-11-09`
  - In this work, we study whether frontier agent can continually improve real-world AI infrastructure over long horizons. We introduce Infrathon, a benchmark of diverse, long-horizon AI infrastructure optimization tasks across different levels. We evaluate six models across 150 runs…

- **[Harness Matters: Measuring and Dissecting Security Resilience in Web Agents](https://arxiv.org/abs/2611.11971v1)**
  - *Xinyi Wu, Jiagui Chen, JiaYi Dong et al.*
  - `2026-11-09`
  - Web agents extend LLMs from text generation to real-world web interaction by relying on execution harnesses that interpret user goals, perceive webpages, plan actions, and ground model decisions into browser operations. While prior work has recognized that agent security depends…

- **[Can LLM Agents Organize Their Own Memory?](https://arxiv.org/abs/2611.11929v1)**
  - *Zichuan Fu, Junjia Qi, Wenlin Zhang et al.*
  - `2026-11-09`
  - In most LLM agents, weights are fixed after deployment, so new information must be retained in external memory. Existing approaches often rely on predefined records and fixed organizational rules, which cannot readily accommodate evolving tasks and interactions. This raises the q…

- **[Late but Valuable: Why Deadlines Change the Measured Value of LLM Reasoning](https://arxiv.org/abs/2611.11910v1)**
  - *Sina Barazandeh, Benjamin E. Lundell, Jose Lugo-Martinez*
  - `2026-11-09`
  - Large language models (LLMs) increasingly plan and run experiments in automated laboratories. These experiments keep running while the model reasons and run on schedules with hard deadlines. If an LLM-generated answer arrives late, the system executes a safe fallback action inste…

- **[LEGION: Benchmarking Language Agents on Sparse-Signal Investigation Under Adversarial Noise](https://arxiv.org/abs/2611.11896v1)**
  - *Samuel Joseph Amouyal, Ofek Glick, Yaniv Menasherov et al.*
  - `2026-11-09`
  - Autonomous language-model agents are increasingly deployed on discovery-driven tasks where signal is sparse and most retrieved information is irrelevant. Current benchmarks fail to evaluate this regime due to dense signals, cooperative environments, and ground truth typically bei…

- **[Correct Answers from Insufficient Histories: A Controlled Study of Agent Memory Evaluation](https://arxiv.org/abs/2611.11840v1)**
  - *Quan Xue, Zerui Yang, Chaorui Zhang et al.*
  - `2026-11-09`
  - An answer can match the reference for a complete agent history even when the reader's visible history does not determine it. We study this distinction using executable device logs. Our protocol separates reference agreement, certified evidence sufficiency, and context-appropriate…

- **[Publications as benchmarks: auditing AI agents on spatial transcriptomics alignment](https://arxiv.org/abs/2611.11796v1)**
  - *Yiqun T. Chen, Jan Matthias, Jianing Yao et al.*
  - `2026-11-09`
  - AI agents are increasingly automating data analysis, but responsible adoption requires reliable performance evaluation, which is costly in specialized scientific domains. We introduce a framework that translates scientific publications into auditable benchmarks for AI agents and…

- **[HolidayFactory 1.0: Simulating, Generating, and Evaluating Industrial Robot Tasks](https://arxiv.org/abs/2611.11789v1)**
  - *Holiday Robotics, :, Jeongmin Lee et al.*
  - `2026-11-09`
  - Robots are typically evaluated in episodes that begin from a reset, while industrial work consists of repeated jobs whose outcomes affect subsequent operations. Evaluating such work at scale requires simulation of task-critical physical interactions, construction of industrial en…

- **[Explaining and interrupting collective misalignment in language model systems](https://arxiv.org/abs/2611.11724v1)**
  - *Edoardo Chidichimo*
  - `2026-11-09`
  - In collectives, language model agents can exchange individually innocuous messages that together support a policy violation. Understanding and preventing collective misalignment requires answering the question of which messages sufficiently influenced and necessarily enabled the…

- **[ShadowBench-MCP: Measuring Shadow Invocations in MCP-Style Tool Routing](https://arxiv.org/abs/2611.11720v1)**
  - *Eyhab Al-Masri, Wenjun Yang*
  - `2026-11-09`
  - LLM agents increasingly act as routers for tools, APIs, and software-supply-chain workflows, making an execution path - rather than generated text alone - a security-relevant model output. We study shadow invocation: a task-preserving request variant that causes an LLM router to…

- **[Steering Emergent Behavior in Multi-Agent LLM Systems via Information Networks](https://arxiv.org/abs/2611.11714v1)**
  - *Sepehr Ilami, Babak Heydari*
  - `2026-11-09`
  - Large language model (LLM) agents increasingly operate in groups, each pursuing an individual objective while jointly determining system performance. If an operator controls which agent observes which other agent, but not their payoffs or messages, how should observations be stru…

- **[CASCoDe: A Closed-Loop Agentic Framework for Analog Sizing and Layout Co-Design](https://arxiv.org/abs/2611.11710v1)**
  - *Ziming Wei, Bingyang Liu, David Z. Pan*
  - `2026-11-09`
  - Expert analog layouts differ from auto-generated ones in density and regularity, not only in legality: experts make a succession of discrete, hierarchical physical decisions and revisit each after extracted electrical results, while most existing automated flows act on a physical…

- **[Scalable Counterfactual Explanations for Time Series via Policy Learning](https://arxiv.org/abs/2611.11704v1)**
  - *Peiyu Li, Pouya Hosseinzadeh, Soukaina Filali Boubrahimi et al.*
  - `2026-11-09`
  - Generating counterfactual (CF) explanations for time series is challenging due to complex temporal dependencies and the computational inefficiency of traditional instance-specific optimization. We propose a policy learning framework for counterfactual explanation in time series,…

- **[Adaptive Quantization Preserves Fast Rates for TD Learning over Rate-Limited Channels](https://arxiv.org/abs/2611.12878v1)**
  - *Sreejeet Maity, Aritra Mitra*
  - `2026-11-09`
  - Motivated by reinforcement learning subject to communication constraints, we study a policy evaluation problem with linear function approximation over a rate-limited channel. In our setup, an agent interacting with an unknown environment (modeled as a Markov Decision Process) tra…

- **[Mitigating Agentic Deception via Evaluation-Side Partially Observable Games](https://arxiv.org/abs/2611.12835v1)**
  - *Hanxiao Li, Shutong Liu, Yongjia Ma et al.*
  - `2026-11-09`
  - As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful. We attribute this failure to evaluation-side partial observability, where models are evaluated mainly from final outcome, without…

- **[Forecast Value Add: Reward-Based Action Selection over Probabilistic Demand Forecasts](https://arxiv.org/abs/2611.12116v1)**
  - *Ankur Verma*
  - `2026-11-09`
  - Strong machine-learning ensembles capture much of the trend, seasonality, and known events in demand, yet they can still understate peaks, miss moving events, or mistake temporary changes for shifts in demand level. We address this gap by framing forecast refinement as a reward-d…

- **[HyPLM Technical Report](https://arxiv.org/abs/2611.12000v1)**
  - *Haowei Lin, Cai Zhou, Xiangxin Zhou*
  - `2026-11-09`
  - Protein language models (PLMs) are standard tools for variant-effect prediction, protein annotation and design, but the compute needed to train and serve them keeps growing. We present HyPLM-Flash, an efficient and open PLM trained by Hyra 2.0, the research agent developed by our…

- **[HyInv Technical Report](https://arxiv.org/abs/2611.11997v1)**
  - *Haowei Lin, Cai Zhou, Xiangxin Zhou*
  - `2026-11-09`
  - Inverse folding designs amino-acid sequences for a given protein backbone, and screening needs many candidates that are both diverse and well folded. We present HyInv, a 1.96-million-parameter backbone-conditioned graph network with an encoder-decoder architecture, trained by Hyr…

- **[Trajectory Density Ratios under Weak Support: A Survey across the Sciences](https://arxiv.org/abs/2611.11985v1)**
  - *Wei Chen, Lihao Zhuang, Yubing Wu et al.*
  - `2026-11-09`
  - Many problems across the sciences compare two stochastic processes through the sequences they generate. Reinforcement learning asks what a new policy would return from the trajectories of an old one; molecular simulation asks how much more a ligand binds from samples of the unbou…

- **[Operation-aware Multimodal Clinical Decision Support System for ICU Discharge Risk Assessment](https://arxiv.org/abs/2611.11960v1)**
  - *Guoqing Zhang, Rafik Hadfi, Takayuki Ito*
  - `2026-11-09`
  - Unplanned 30-day intensive care unit (ICU) readmission is a critical benchmark for evaluating healthcare quality. Most predictive models assume readmission risk depends solely on a patient's individual pathophysiological state, ignoring hospital operational context and resource c…

- **[DeFSM: Robust and Efficient Decentralization of Federated Submodular Maximization](https://arxiv.org/abs/2611.11866v1)**
  - *Duc A. Tran, Dung Truong, Duy Le*
  - `2026-11-09`
  - Submodular maximization seeks a small subset best representing a large dataset. In its federated setting, the server is a single point of failure and some clients may be Byzantine. Removing the server raises a trilemma of decentraliza- tion, efficiency, and security. We propose D…

- **[Can Hindsight Critics Guide Delayed Actors?](https://arxiv.org/abs/2611.11863v1)**
  - *Francisco M. López, Francisco Cruz*
  - `2026-11-09`
  - Sensory delays create temporal misalignments between the state of the environment and the observations available to an agent, turning Markovian control problems into partially observable ones. In this work, we inquire whether such misalignments can be mitigated during training by…

- **[Scaling Adaptive Prompt Injection Attacks with Agent Swarms](https://arxiv.org/abs/2611.11861v1)**
  - *Alexey Kurakin, Vishal Karande, Alex Bie et al.*
  - `2026-11-09`
  - Prompt injections have emerged as one of the top security risks faced by AI agents today. Early work in prompt injection attacks looked at simple tool-call agents and static attack payloads, and were saturated since mid-2025. As of Fall 2026, human red-teaming may be nearing satu…

- **[KKT-Perturbation-Aware Communication for Fully Distributed Online Convex Optimization with Nonseparable Coupling](https://arxiv.org/abs/2611.11827v1)**
  - *Zhaoye Pan, Tao Li, Yunjie Guo et al.*
  - `2026-11-09`
  - Nonseparable costs and coupled constraints in distributed online convex optimization often arise when system performance and operational constraints depend on the joint configuration of all agents and cannot be decomposed into individual contributions. Such nonseparability leads…

- **[WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2611.12856v1)**
  - *Zheng Jiang, Fang Niu, Bo Peng et al.*
  - `2026-11-09`
  - Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shift…

- **[Unprompted coordination through shared memory in LLM agents: a locked two-implementation replication and extension](https://arxiv.org/abs/2611.12412v1)**
  - *Pekka Abrahamsson, Muhammad Waseem, Esa Karjalainen et al.*
  - `2026-11-09`
  - Coordination between large language-model agents has become a central question for AI safety and software engineering, as such agents are deployed in groups that share infrastructure. Existing research tells the agents that partners exist or asks them to coordinate. Whether coord…

- **[Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading](https://arxiv.org/abs/2611.12269v1)**
  - *Guangyan Gan, Jiahao Li, Jiashun Wang et al.*
  - `2026-11-09`
  - Cryptocurrency markets provide a natural testbed for autonomous AI agents because they are digital-native, high-frequency, and machine-speed environments, yet existing methods often struggle with non-stationary market regimes, opaque decisions, and fixed aggregation rules. In thi…

- **[SMO: Compiling Natural Language Skills into Graphs of Reusable State-Move-Outcome Bricks](https://arxiv.org/abs/2611.12041v1)**
  - *Chao Chen, Jiashuo Zhang, Yunhang Shen et al.*
  - `2026-11-09`
  - Large language model agents increasingly rely on reusable natural-language skills, yet growing skill collections remain accumulations of isolated text artifacts that are difficult to compare, deduplicate, and compose. We argue that the reusable content of a skill lies not in its…

- **[Competing Influence in LLM Populations: Budget Timing and Baseline Drift](https://arxiv.org/abs/2611.11867v1)**
  - *Mehwish Nasim, Nicolas Fay*
  - `2026-11-09`
  - When competing campaigns target a population of large language model (LLM) agents, observed opinion changes may reflect both campaign influence and changes that would occur without intervention. We study how the timing of campaign expenditure and the population's own evolution sh…

- **[Direct GPU Energy Measurements of Batch-Level Sharing in Mixture-of-Experts and Recurrent Models](https://arxiv.org/abs/2611.11696v1)**
  - *Rafael Pina, Varuna De Silva*
  - `2026-11-08`
  - Energy claims for efficient neural networks are often inferred from operation counts. We report direct GPU energy measurements on two workloads that batch very differently, recurrent policies in GPU-vectorised multi-agent reinforcement learning (MARL) and mixture-of-experts (MoE)…

- **[A Physical Testbed for Self-Driving Laboratories: Comparing Bayesian and Agentic Optimization in a Minimal Closed-Loop Color Formulation Task](https://arxiv.org/abs/2611.11690v1)**
  - *Tony Qin, Ziheng Wu, Maximilian Schommer et al.*
  - `2026-11-08`
  - Self-driving laboratories (SDLs) integrate laboratory robotics and automation with AI-driven decision-making to close the design-build-test-learn (DBTL) cycle. However, physical testbeds that combine off-the-shelf hardware and AI into a functioning closed-loop workflow remain in…

- **[Inside the Trading Loop: Markets, Models, and Moves with LLM Agents](https://arxiv.org/abs/2611.11657v1)**
  - *Renee Jia, Di Mu, Yao Yu et al.*
  - `2026-11-08`
  - We built a hybrid multi-agent trading system that combines large language model (LLM) analysts with momentum-based portfolio construction and rule-based execution. Company-news and macroeconomic agents return structured reports to a coordinator that sets stock weights and cash re…

- **[Same Error, Different Recovery: How Delivery Changes LLM Agent Behavior](https://arxiv.org/abs/2611.11581v1)**
  - *Sunghyeun Woo, Javier Conde, Pedro Reviriego*
  - `2026-11-08`
  - A tool-using language model must decide whether to retry a failed call, correct it, or stop and tell the user. The error text alone may not be enough: the same feedback can lead to different actions depending on where it appears in the conversation. We isolate this delivery probl…

- **[LiveAsset: Learning Intent Assets from Corrective Interactions for Agent Runtime Control](https://arxiv.org/abs/2611.11560v1)**
  - *Guanming Liu, Weihang Wang, Peng Zhang et al.*
  - `2026-11-08`
  - Large language model (LLM) agents acting across web applications and online services often need multi-turn corrections to align their work with users' underspecified goals and preferences. In practice, users may identify problems in the current outcome without specifying the desi…

- **[Safeguarding Agentic AI in Radiology Workflows: A Multimodel Evaluation of Rule-based and Large Language Model-based Verification](https://arxiv.org/abs/2611.11541v1)**
  - *Semil Eminovic, Robin Schmidt, Bogdan Levita et al.*
  - `2026-11-08`
  - Purpose: To estimate how often tool-using large language model (LLM) agents record clinically relevant false or unsupported information in simulated radiology documentation and how much safeguards applied before each action reduce these errors.   Materials and Methods: In this si…

- **[PRISM: Causal Counterfactual Minimization of Agent Tool Privileges via Information Bottleneck Role Induction](https://arxiv.org/abs/2611.11539v1)**
  - *Yang Luo, Qingni Shen, Tairui Wang et al.*
  - `2026-11-08`
  - This paper shifts the object of role engineering from human users to large language model (LLM) agents, and proposes PRISM to address the over-authorization that arises when an agent obtains full tool privileges through the Model Context Protocol (MCP). PRISM formulates whether a…

- **[On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents](https://arxiv.org/abs/2611.11506v1)**
  - *Brijesh Dongol*
  - `2026-11-08`
  - An LLM agent that reads untrusted content, such as an email or a web page, may follow instructions hidden in it. Noninterference is too strong for such agents, since a useful agent lets untrusted content influence what it does and may disclose the user's data by design, and decla…

- **[JoMoHa: Joint Model--Harness Optimization with Reinforcement Learning](https://arxiv.org/abs/2611.11499v1)**
  - *Xudong Wu, Guangchen Lan, Mingqi Yuan et al.*
  - `2026-11-08`
  - The performance of language agents depends jointly on model weights and the harness. Optimizing either alone can be constrained by the other component, limiting overall performance gains. Our analysis of naive alternating training reveals progressive incompatibility between the m…

- **[GOPR-CAD: Graph-of-Operations Progressive Reasoning for CAD Generation](https://arxiv.org/abs/2611.11470v1)**
  - *Yitian Pang, Yifan Li, Xiaowei Yue et al.*
  - `2026-11-08`
  - Generating accurate CAD models requires substantial engineering expertise and careful control of geometry, topology, and mechanical constraints. Text-to-CAD aims to simplify this process, but current LLM-based methods often generate CAD programs directly. Language models remain u…

- **[How to "train" a surgeon? Benchmarking generalist agents in surgical scene understanding](https://arxiv.org/abs/2611.11437v1)**
  - *Gengyuan Zhang, Xiao Han, Shijie Zhou et al.*
  - `2026-11-08`
  - Evaluating general-purpose multimodal large language models (MLLMs) for surgical scene understanding remains limited due to scarce surgical data and fragmented evaluation protocols. We address these challenges through a two-stage evaluation framework for surgical scene understand…

- **[Separation of Skilling Context for Standard Operating Procedure-based Agents](https://arxiv.org/abs/2611.11348v1)**
  - *Mitsuhiro Nakayama, Toshiaki Sota, Takehiko Yamaguchi et al.*
  - `2026-11-08`
  - Standard Operating Procedures (SOPs) are kept concise for human readability, so LLM agents that generate executable skills from them lack the tacit knowledge and implementation details needed for automation. Human intervention fills these gaps, but must be repeated as SOPs evolve…

- **[Agent Self-Improvement with Frozen Weights: The Added Value and Limits of Failure Traces](https://arxiv.org/abs/2611.11342v1)**
  - *Arkid Mitra*
  - `2026-11-08`
  - We evaluate whether an AI agent's harness, the notes around its model, can learn from the agent's failure traces beyond a matched search that never sees them. It can, but less than it looks. We tested an open 9-billion-parameter model with fixed weights; a larger teacher model wr…

- **[Agentic Attribution of Cloud Resource Ownership](https://arxiv.org/abs/2611.11340v1)**
  - *Tiltan Gilat, Gal Engelberg, Ariel Zadok et al.*
  - `2026-11-08`
  - Security tools raise findings across cloud environments, and AI agents now investigate and prioritize them. A finding is still resolved by people: it has to reach the people responsible for fixing it and accountable for the resource it concerns. Ownership is the organizational co…

- **[Verify Before You Fetch: Reliable KV Cache Compression for LLM Inference](https://arxiv.org/abs/2611.11319v1)**
  - *Devanshu Jha, Gaurav Kumar, Agniva Chowdhury et al.*
  - `2026-11-08`
  - Long-context applications, long-lived agents, and multi-agent systems require large language models (LLMs) to process and retain extensive information. In these settings, the KV cache can exceed GPU high-bandwidth memory (HBM) capacity, necessitating offloading to host memory, wh…

- **[ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping](https://arxiv.org/abs/2611.11306v1)**
  - *Joseph Marvin Imperial, Daniel Slate, Noam Kolt*
  - `2026-11-08`
  - AI agents deployed on the open web are becoming more capable of performing actions that may breach contractual provisions and violate computer security laws. In this paper, we introduce ScrapeBench, the first agentic benchmark for empirically evaluating the legal compliance of AI…

- **[Least-Privilege Auditing of Agent Tool Calls with Intent Graphs and Reasoning-Guided Escalation](https://arxiv.org/abs/2611.11305v1)**
  - *Doron Shavit*
  - `2026-11-08`
  - LLM agents that call tools are exposed to indirect prompt injection: instructions hidden in tool outputs can steer an agent into calls the user never asked for. We present a runtime audit that derives an executable intent graph from the user's objective and the deployment's tool…

- **[ErosionBench: Probing Alignment Decay in Enterprise Multi-Agent Systems](https://arxiv.org/abs/2611.11266v1)**
  - *Riya Bharathwaj, Akshara Prabhakar, Roshan Ram et al.*
  - `2026-11-08`
  - As enterprises delegate consequential work to multi-agent LLM systems, benign-looking requests can escalate into unsafe actions as they propagate across sessions through poisoned shared state, long-context documents, and trusted peer messages: no single message is malicious, yet…

- **[LoMASA: A Local Multi-Agent Sales Assistant with Confidence-Gated Delegation for B2B Quoting](https://arxiv.org/abs/2611.11234v1)**
  - *Yu Liu, Xingbang Du*
  - `2026-11-08`
  - Frontline sales staff spend much of their day re-coordinating quotes after customers change quantities, ask for discounts or new payment terms, or costs move. We present LoMASA (Local Multi-Agent Sales Assistant), a training-free multi-agent system that runs entirely on one deskt…

- **[Deterministic Narrative Gravity: Bridging Theory of Mind and Historical Simulation through ABM-LLM Architectures](https://arxiv.org/abs/2611.11212v1)**
  - *Alicia Colmenero-Fernández, Lidia Ortega Alvarado*
  - `2026-11-08`
  - Historical social simulation faces a fundamental reproducibility challenge: the stochastic nature of large language models (LLMs) introduces a digital butterfly effect that prevents exact replication across multi-turn runs. Furthermore, the inability to control low-level server p…

- **[Statopia: A Prover--Library Ecosystem for Automated Formalization and Proof Discovery in Statistics](https://arxiv.org/abs/2611.11110v1)**
  - *Ziyuan Chen, Tong Gan, Wei Zhang et al.*
  - `2026-11-08`
  - Theoretical results in statistics and machine learning rest on long, technically delicate proofs, and fluent arguments generated by large language models are not necessarily correct. Automated formalization makes such arguments mechanically checkable, and automated proving goes f…

- **[GARP: Real-Time Generative Agents on Local Hardware in a Game Engine](https://arxiv.org/abs/2611.11064v1)**
  - *Piero Molino, Patrick John Chia, Federico Bianchi et al.*
  - `2026-11-08`
  - Generative agents are game characters whose plans, conversations, and memories are written on the fly by a large language model (LLM). The original Generative Agents demonstration used cloud inference in a custom simulation. We present GARP, a platform for real-time generative ag…

- **[Agents Propose, Code Verifies, Humans Decide: Verified Agentic Ingestion of Heterogeneous Scientific Tables into Relational Databases](https://arxiv.org/abs/2611.11045v1)**
  - *Bharatha Rankothge, Suzanne Hodgkins, Virginia Rich et al.*
  - `2026-11-08`
  - Public scientific datasets rarely arrive analysis-ready. They arrive as messy folders of wide matrices, long tables, spreadsheets, and per-cohort files whose keys and encodings differ, and every reanalysis must reconnect them first. A coding agent can automate this, but its mista…

- **[Advancements in Cloud-Native Systems: A Systematic Mapping Study of Reliability and Scalability across Cloud-Native, Edge-Native and AI-Enabled Systems](https://arxiv.org/abs/2611.11040v1)**
  - *Shrinivass Arunachalam Balasubramanian*
  - `2026-11-08`
  - Cloud-native systems now extend to the network edge and host artificial-intelligence (AI) workloads, including AI agents, but evidence on their reliability and scalability is scattered and uneven. We report a PRISMA 2020 systematic mapping study with an evidence-graded synthesis.…

- **[Finite-Sample and Communication-Efficient Networked Information Aggregation](https://arxiv.org/abs/2611.11032v1)**
  - *Mohammadhossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi et al.*
  - `2026-11-08`
  - Building on SODA 2026 work Kearns et al. (2026), we study learning in directed acyclic graphs in which each agent observes only a subset of the input coordinates and may use the predictions of its parents as additional features. In the finite-sample protocol, the message sent alo…

- **[Actions Should EARN Their Credit: Test-Time Adaptation and Route Consolidation for Frozen LLM Agents](https://arxiv.org/abs/2611.11565v1)**
  - *Bian Sun, Kevin Zhai, Mubarak Shah et al.*
  - `2026-11-08`
  - LLM agents can use feedback from repeated attempts to improve their decisions without updating model parameters. However, positive action credits can continue to favor actions that repeatedly achieve the same score, even when higher scores are achievable. Under a fixed interactio…

- **[Ostinato: Fast CPU-GPU MoE Inference for Local Agents via Resident Experts in Every Forward Pass](https://arxiv.org/abs/2611.11533v1)**
  - *Junning Zhu*
  - `2026-11-08`
  - Language-model agents increasingly run on workstations with a few consumer GPUs, where large mixture-of-experts (MoE) models keep part of their experts in host memory. With existing CPU-GPU engines, these agents get fast prefill or fast decode, not both: llama.cpp's expert cache…

- **[Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation](https://arxiv.org/abs/2611.11452v1)**
  - *Weizhong Huang, Huaijia Kou, Tianyu Xie et al.*
  - `2026-11-08`
  - Agentic autoregressive video generation combines semantic planning, sequential generation, and visual verification for controllable synthesis. Growing visual histories enlarge the key-value (KV) cache, increasing memory use and attention costs across candidate rollouts. Existing…

- **[When Credit Turns Against Tools: Transition-Aware Credit Assignment in Agentic Reinforcement Learning](https://arxiv.org/abs/2611.11330v1)**
  - *Xiangyu Lu, Zhanke Zhou, Jiazhe Ning et al.*
  - `2026-11-08`
  - Agentic reinforcement learning with verifiable rewards trains language models through multi-turn tool interactions, yet their reasoning performance and tool-calling ability can decline during training. We trace this degradation to three coupled mechanisms: (1) tool-token imbalanc…

- **[How Efficient Is Your Agent? Online Predictive Bounds under Budget Constraints](https://arxiv.org/abs/2611.11279v1)**
  - *Roy Maor Lotan, Shai Feldman, Yaniv Romano*
  - `2026-11-08`
  - We evaluate AI agents in an online setting where tasks arrive sequentially and, before running each task, we construct an upper predictive bound on its \emph{time-to-success}---the number of interactions until the task is completed successfully. Under a limited budget, some runs…

- **[Uncertainty-Guided Reward Labeling for Reinforcement Learning under Limited Feedback](https://arxiv.org/abs/2611.11091v1)**
  - *Renhao Zhang, Shreyas Chaudhari, Bruno Castro da Silva*
  - `2026-11-08`
  - In reinforcement learning from limited feedback (RLLF), only a small fraction of an offline dataset can be labeled with rewards, and the central question is which samples should be labeled to learn a high-performing policy from the resulting partially labeled dataset. Prior work…

- **[The Average Patient: Do Simulated Psychiatric Patients Answer Like Real People?](https://arxiv.org/abs/2611.11679v1)**
  - *Weixiang Sun, Zehong Wang, Kaiwen Shi et al.*
  - `2026-11-08`
  - Language models are used as simulated psychiatric patients to train clinicians and evaluate AI therapists, and are judged by plausibility or total scores. We give a framework for simulated respondents: an information budget bounds how much simulated patients can differ, and an av…

- **[Task-adaptive anonymisation enables privacy-preserving sharing of clinical speech data](https://arxiv.org/abs/2611.11273v1)**
  - *Ziyun Cui, Haoyu Niu, Wen Wu et al.*
  - `2026-11-08`
  - Clinical speech is increasingly used for disease screening and clinical assessment, but directly distributing speech recordings poses privacy risks because they contain both speaker-identifying voiceprints and sensitive spoken content. Existing speech anonymisation approaches are…

- **[LongCap: Hour-Scale Timestamped Audio Captioning via Chunk-wise Processing](https://arxiv.org/abs/2611.11125v1)**
  - *Jinchuan Tian, Sen Chen, Wenbin Huang et al.*
  - `2026-11-08`
  - Describing hours of audio requires accurate event timing and sustained descriptive detail throughout the recording. We present LongCap, a framework for timestamped audio captioning (TAC), with the human-annotated LongCapBench and three diarization-inspired metrics: Timeline Error…

- **[Do Benign-Trained Hidden-State Probes Detect Tool Errors Under Adversarial Conditions?](https://arxiv.org/abs/2611.11172v1)**
  - *Bibek Bhandari, Kshitij Lingthep*
  - `2026-11-08`
  - Although hidden-state probes efficiently monitor model operation, it remains unclear whether probes trained on benign tool use remain useful for detecting incorrect actions under adversarial conditions. In this research, we assess this problem from the perspective of operational…

- **[Where Should Models Run? A Collaborative Inference Framework for Embodied Intelligence in 6G](https://arxiv.org/abs/2611.11023v1)**
  - *Wanlu Sun, Zhenhui Yuan, Xiang Ji et al.*
  - `2026-11-07`
  - Embodied intelligence systems rely on fast and reliable inference to enable real-time perception, reasoning, and control. Recent advances in large-scale artificial intelligence (AI) models, including Large Language Models (LLMs) and Vision-Language-Action (VLA) models, have signi…

- **[PIA: Agentic Physics-Informed Runtime Anomaly Detection](https://arxiv.org/abs/2611.11009v1)**
  - *Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour*
  - `2026-11-07`
  - Runtime anomaly detectors for cyber-physical systems are either learned as black boxes from normal data, which miss stealthy manipulations that keep every signal inside its normal range, or derived by hand from physical models, which requires expert effort for every plant. We int…

- **[GradReason: LLMs as Meta-Learners that Replace Training Epochs with Training-Data-Free Weight Updates](https://arxiv.org/abs/2611.11005v1)**
  - *Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour*
  - `2026-11-07`
  - Standard training recipes make a fixed number of passes over the training data, even when an epoch mostly adds mini-batch noise. We study whether a large language model (LLM) that reads the weight and gradient history of a run can replace some of these epochs with updates that co…

- **[Differentiable Agent-Based Modeling for Multi-Echelon Supply Chains: Gradient-Based Optimization of Heterogeneous Policies at Scale](https://arxiv.org/abs/2611.10999v1)**
  - *Bulent Soykan, Murtadha Alsayegh, Sean Mondesire et al.*
  - `2026-11-07`
  - Global supply chains rely on the interactions of thousands of heterogeneous agents, posing significant challenges for optimization. While traditional optimization often assumes homogeneity to ensure tractability, Reinforcement Learning struggles with sample inefficiency when scal…

- **[Think or Remember: The Exchange Rate of Agentic Inference](https://arxiv.org/abs/2611.10982v1)**
  - *Juan Wisznia, Santiago Luis Groba Alonso, Matías Gómez Taddeo et al.*
  - `2026-11-07`
  - Agents built on reasoning models resend their growing transcript at every call. Two transacting parties, not the model, decide what that costs: the client keeps or edits messages; the server decides whether earlier reasoning returns in the prompt and what its cache reuses. We def…

- **[Improving Analytic Constants via Interpretable AI-Guided Lean Proof Refinement](https://arxiv.org/abs/2611.10961v1)**
  - *Rahul Saha, Alan Li, Anton Xue et al.*
  - `2026-11-07`
  - AI agents are increasingly capable of discovering new mathematical results, yet their reasoning and generated proofs can be difficult to understand and verify. We introduce an interpretable framework for AI-guided mathematical discovery, focused on improving quantitative bounds o…

- **[Hybrid Source Code Change Impact Analysis](https://arxiv.org/abs/2611.10958v1)**
  - *Katharina Stengg, Christian Macho, Martin Pinzger*
  - `2026-11-07`
  - Change impact analysis (CIA) helps developers identify code entities impacted by their initial changes. While several approaches for CIA were proposed, they still struggle with either low precision or low recall, thereby increasing manual effort for developers to verify the resul…

- **[DeepFinance: Can AI Diligence a $100MM Deal?](https://arxiv.org/abs/2611.10926v1)**
  - *Drew Hahn, Tyler Shibata, Jackson Grove et al.*
  - `2026-11-07`
  - Existing evaluations of AI models on high-finance work focus on retrieving answers from financial documents and producing numerically correct outputs. Real private equity (PE) and investment banking (IB) work also depends on choosing between conflicting sources, making sound assu…

- **[Keeping LLM Agents on Procedure: Executable Finite-State Control for Long-Horizon Instruction Fidelity](https://arxiv.org/abs/2611.10884v1)**
  - *Yutao Sun, Haokun Li, Mingshuai Chen et al.*
  - `2026-11-07`
  - Much of the automation handed to language-model agents is procedural: each step needs little intelligence, but a long unattended run must follow a skill or SOP stated once at the start. We show that agents drift from such procedures over long runs, and that restating the instruct…

- **[What Broke & Why: Practical Lessons from Reinforcement Learning Post-Training](https://arxiv.org/abs/2611.10844v1)**
  - *Luv Verma*
  - `2026-11-07`
  - Reinforcement learning with verifiable rewards (RLVR) has become an important way to improve how language models reason, solve problems, and use tools. But getting it to work in practice is not always straightforward. Training can fail because a model receives no useful reward, l…

- **[A Gamified Framework for Conflict-Driven Design: Discovering Strategies for Collaborative Resilience with Multi-Agent Learning](https://arxiv.org/abs/2611.10841v1)**
  - *Jin Gao*
  - `2026-11-07`
  - Conflicting stakeholder objectives make it difficult to coordinate investments in urban resilience. We model conflict-driven urban design as a non-zero-sum digital board game in which stakeholder agents allocate scarce resources and balance individual payoffs against shared urban…

- **[Selective Cooperative Perception via Blind Spot Reasoning and Agentic Dialogue with Vision-Language Models](https://arxiv.org/abs/2611.10819v1)**
  - *Chengyuan Ma, Shixiao Liang, Hangyu Li et al.*
  - `2026-11-07`
  - Real-time cooperative perception (CP) in multi-agent traffic environments is highly resource-intensive, which posing scalability challenges for large-scale deployment. Efficiency can be significantly improved by selectively performing CP only in safety-critical scenarios and for…

- **[RTLREX: LLM-Guided Framework for Exact High-Level RTL Recovery](https://arxiv.org/abs/2611.10798v1)**
  - *Wuqian Tang, Fangzhou Liu, Ruijie Wang et al.*
  - `2026-11-07`
  - Hardware designs may be available only as gate-level netlists or input-output descriptions when the original register-transfer-level (RTL) design and documentation are not accessible. Low-level representations obscure word-level computation and its finite-width behavior. Recoveri…

- **[Trustworthy Recursive Self-Improvement with Statistical Guarantees](https://arxiv.org/abs/2611.10787v1)**
  - *Zihe Gao, Zhengling Qi, Yifan Cui*
  - `2026-11-07`
  - Recursive self-improvement offers a promising path toward AI agents that improve through experience by refining their own harnesses without retraining their underlying large language models (LLMs). Making this self-improvement process reliable, however, requires more than generat…

- **[BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](https://arxiv.org/abs/2611.10768v1)**
  - *Zilin Guo, Tianrui Zhang, Yi Rong et al.*
  - `2026-11-07`
  - Multimodal Large Language Models (MLLMs) have shown promise as interactive agents, yet precise, programmatic 3D graphics editing remains difficult to train because existing systems largely rely on closed-source model APIs and lack deterministic, state-verifiable execution environ…

- **[REINS: A Self-Evolving Agent Harness for Real-Time Trajectory Planning](https://arxiv.org/abs/2611.10748v1)**
  - *Zhihong Cui, Hengyu Liu, Haoran Tang et al.*
  - `2026-11-07`
  - Agent harnesses -- runtime scaffolds that wrap an LLM's reasoning loop with tool dispatch, verification, and persistent memory -- have become the standard substrate for deploying LLMs as autonomous agents, as demonstrated by Claude Code and Codex in software engineering. In traje…

- **[CyberBinGym: Can AI Agents Turn Binary Patches into Real Exploits?](https://arxiv.org/abs/2611.10723v1)**
  - *Lambang Akbar Wijayadi, Zhaoqi Xiao, Zhun Wang et al.*
  - `2026-11-07`
  - Security fixes usually reach users as compiled updates, but deployment delays leave unpatched systems exposed. During this window, comparing patched and unpatched binaries can reveal how to exploit a vulnerability, turning a defensive update into actionable information for attack…

- **[No Second Run: Does RSI Stop at Frontier Pre-training?](https://arxiv.org/abs/2611.10719v1)**
  - *Xiaojie Cai, Jiayi Chen, Junwei Chen et al.*
  - `2026-11-07`
  - Pre-training is where every foundation model begins; bringing recursive self-improvement (RSI) there would let AI improve the process that creates AI. Yet public RSI work has so far targeted only post-training, which starts from an existing base model, runs trials costing GPU-hou…

- **[R-BED: A Consequence-Aware Framework for System-Level AI Evaluation and Continuous Assurance](https://arxiv.org/abs/2611.10704v1)**
  - *Vishal Srivastava*
  - `2026-11-07`
  - Evaluations of AI systems usually report properties of a model, while decisions to deploy concern a configured system: a model together with prompts, tools, permissions, data, safeguards and an operating context. We ask how evidence about technical failures, deployment-control ef…

- **[Perception, Not Reasoning, Limits Visual Theory of Mind](https://arxiv.org/abs/2611.10694v1)**
  - *Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall et al.*
  - `2026-11-07`
  - Vision-language models pass text-based false-belief probes at near-human levels but drop by over twenty percentage points on abstract panels the moment the same problem is conveyed visually. The consensus diagnosis is conceptual, prescribing new belief-reasoning modules. We argue…

- **[RetinaGuard: Risk-Controlled Agentic Triage for Multi-Disease Retinal Screening](https://arxiv.org/abs/2611.10689v1)**
  - *Sohaib Sulman, Muhammad Atif Saeed, Akhtar Jamil et al.*
  - `2026-11-07`
  - Retinal screening programmes need to know which automated decisions can be accepted without review. This paper presents RetinaGuard, an agentic triage framework in which quality, diagnostic, uncertainty, verification and explanation agents gather evidence for each fundus photogra…

- **[MMGraph-Agent: Agentic Multimodal RAG via Cache-Inspired Multimodal Knowledge HyperGraphs](https://arxiv.org/abs/2611.10657v1)**
  - *Haoran Luo, Ziyue Zhu, Shangyang Wu et al.*
  - `2026-11-07`
  - Driven by increasingly complex real-world applications, Retrieval-Augmented Generation (RAG) has evolved from textual pipelines to multimodal settings, comprising two complementary dimensions: knowledge organization and retrieval enhancement. However, existing methods still face…

- **[SLA-Aware Task Offloading in the IoT Edge-Cloud Continuum: Class-Weighted Deep Reinforcement Learning Against an Exact Optimum](https://arxiv.org/abs/2611.10638v1)**
  - *Shilpa Golla, Tharun Kumar Korine Palli, Urmila Bandaru*
  - `2026-11-07`
  - Deep reinforcement learning (RL) is often used to decide where Internet of Things (IoT) tasks with different latency limits run in the edge-cloud continuum, yet some methods give every missed task the same penalty and few compare their agents with an optimal policy. This benchmar…

- **[DFT-Agent Bench: Scaffold Effects and Execution Provenance in Autonomous DFT](https://arxiv.org/abs/2611.10629v1)**
  - *Shijie Liu, Jin Yang, Weilin Wan et al.*
  - `2026-11-07`
  - Large language models are increasingly deployed as autonomous agents for first-principles materials simulation. We report empirical findings from DFT-Agent Bench, a benchmark of 200+ Quantum ESPRESSO tasks spanning relaxation, electronic structure, equation-of-state, and elastic-…

- **[Towards Identity-Preserving LLM Agents under Model Transition](https://arxiv.org/abs/2611.10628v1)**
  - *Yihuang Kang, Pei-Cing Huang, Chan-Tung Ku et al.*
  - `2026-11-07`
  - When an LLM agent's backend model is upgraded or replaced, operators typically reload the same persona, memory, and rules onto the new model and assume the agent will behave as before. We show this assumption requires empirical validation-and that whether identity is preserved de…

- **[What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors](https://arxiv.org/abs/2611.10620v1)**
  - *Mainul Hasan Mohsin, Mohammad Shahidur Rahman*
  - `2026-11-07`
  - Activation probes look like near-perfect monitors for secret collusion among large language model (LLM) agents. We show that they mostly detect that an agent was told to collude, not that it decided to. Our benchmark (2,500 committee and 1,476 code-review episodes) adds agents wh…

- **[Agentic discrete-event simulation for manufacturing system design: an open 3D simulator, a benchmark and an industrial case](https://arxiv.org/abs/2611.10602v1)**
  - *Javier Pernas-Álvarez, Diego Crespo-Pereira*
  - `2026-11-07`
  - The design of manufacturing systems relies on discrete-event simulation (DES) models that experts still build in tool-specific interfaces. AI agents can now write simulation code, but every model they write from scratch is new, unverified software. We present SimuLean, an open-so…

- **[InfoOrgBench: Can Agents Turn Scattered Information into Coherent Hierarchies?](https://arxiv.org/abs/2611.10600v1)**
  - *Justice Ou, Lanming Ma, Zijian Zhang et al.*
  - `2026-11-07`
  - When agents organize records into folders, they may correctly group the excerpts of a design proposal yet place the proposal under the wrong owning group. Existing agent benchmarks do not directly measure such higher-level errors. We introduce InfoOrgBench, a benchmark of 150 tas…

- **[When Experience Becomes a Backdoor: Poisoning Self-Evolving LLM Agents via Failure-Aware Task Optimization](https://arxiv.org/abs/2611.10542v1)**
  - *Minhua Lin, Zongyu Wu, Hanqing Lu et al.*
  - `2026-11-07`
  - Large language model (LLM) agents increasingly improve themselves through self-evolution, distilling execution experience into persistent, reusable skills. However, this persistence creates a new attack surface: malicious rules implanted into skills can compromise subsequent agen…

- **[In Search of Lost Time: Temporal Competence in Large Language Models](https://arxiv.org/abs/2611.10536v1)**
  - *Ryan Liu, David Lee, Icey Siyi Ai et al.*
  - `2026-11-07`
  - Today's large language models (LLMs) increasingly interact with time: AI agents schedule tasks, coordinate with people and other AI systems, and even decide how long to think. Yet LLMs only ever encounter time secondhand---in descriptions rather than experience. Does this hinder…

- **[Imperfectly Imperfect: Evaluating Graded Cognitive Diversity in LLM Persona Simulations](https://arxiv.org/abs/2611.10508v1)**
  - *Sion Weatherhead, Ben Newell, Aaron Belbasis et al.*
  - `2026-11-07`
  - Large language model (LLM) agents are increasingly used as synthetic participants in social, behavioural, and decision-making research, yet it remains unclear whether they can express graded cognitive diversity as assigned when engaging in simulated behaviour. We introduce a cogn…

- **[Sampling Is Not Curiosity: Why LLM Agents Should Investigate](https://arxiv.org/abs/2611.10501v1)**
  - *Alfonso Amayuelas, Piotr Piękos, Xin Eric Wang et al.*
  - `2026-11-07`
  - LLM agents are increasingly used for open-ended tasks, very common in research scenarios where they are required to explore, investigate, or act curiously. At inference time, an LLM is a fixed map from context to next-token distribution, the pretrained weights determine the funct…

- **[Hibana: Fast Agentic Inference on Unified-Memory Devices](https://arxiv.org/abs/2611.10469v1)**
  - *Yahya Emara, Chi-Chih Chang, Anthony Fei et al.*
  - `2026-11-07`
  - Local AI promises capable personal assistants that run on users' own devices, keeping data and computation under their control. Open-weight models that fit on local devices can now handle practical tasks such as coding. Yet current inference engines fall short. Popular engines su…

- **[Represented but Not Used: Value-Policy Dissociation in LLM Agents](https://arxiv.org/abs/2611.10457v1)**
  - *Yuzhang Luo, Mohamed Aghzal, Liangming Pan et al.*
  - `2026-11-07`
  - Large language model (LLM) agents need to choose actions whose consequences unfold over multiple future steps, yet poor decisions do not reveal whether the model failed to represent those consequences or failed to use them. Mechanistic interpretability has studied internal repres…

- **[BunshinRL: Splitting Live Agent Workspaces for Memory-Efficient Agentic RL](https://arxiv.org/abs/2611.10453v1)**
  - *Yutong Huang, Vikranth Srivatsa, Alex Asch et al.*
  - `2026-11-07`
  - Agentic reinforcement learning (RL) rollouts interleave model reasoning with tool calls in persistent workspaces. Scaling these rollouts incurs substantial memory costs for concurrent environments, while slow tool calls delay entire rollout batches. We present BunshinRL, an agent…

- **[Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction](https://arxiv.org/abs/2611.10439v1)**
  - *Yunzhe Wang, Mesut Erhan Unal, Sheng Zhang et al.*
  - `2026-11-07`
  - Self-evolving agents improve their own skills, memory, and harness code from experience without retraining the base LLM, and group-evolving agents go further by sharing these lessons across agents. Yet most such systems overlook that sharing across users and heterogeneous agents…

- **[HexIt: Learning Hexahedral Block Decomposition with Expert Iteration on Combinatorial Maps](https://arxiv.org/abs/2611.10433v1)**
  - *Arjun Narayanan, Per-Olof Persson*
  - `2026-11-07`
  - Decomposing a polyhedral solid into a few well-shaped hexahedral blocks is a long-standing open problem in mesh generation. We cast it as a sequential decision problem on a 3-dimensional generalised map: an agent splits edges, faces and volumes with three insert operations until…

- **[Deploying Physically and Epistemically Compliant Agents by Distilling Belief-Space Task and Motion Planners](https://arxiv.org/abs/2611.10430v1)**
  - *Phillip J. K. Christoffersen, Rachel Ma, Patrick Barragán et al.*
  - `2026-11-07`
  - In this work, we train agents to act under uncertainty according to specified, belief-dependent rules. Deep reinforcement learning (RL) can in theory train agents to follow rules if encoded into well-designed rewards, but in practice, RL fails to perfectly optimize these rewards,…

- **[Track or Follow? A Jev-Compatible Multi-Agent Trading System When Web News Lags the Market](https://arxiv.org/abs/2611.10414v1)**
  - *Yebo Feng, Guangyan Gan, Liangrui Pan et al.*
  - `2026-11-07`
  - LLM agents increasingly trade on the Web news they read, yet much Web news about listed firms is published after, and about, the price move it reports, so a reader can agree with the market by following it instead of reading the event. We ask whether LLM judgments of Web news tra…

- **[TurnFlow: Benchmarking User-State Reasoning in Multi-Turn LLM Agents via Scene-Guided User Simulation](https://arxiv.org/abs/2611.10412v1)**
  - *Zhixun Chen, Ming Li, Anjie Liu et al.*
  - `2026-11-07`
  - Large Language Models (LLMs) are increasingly deployed through conversational interfaces, yet strong single-turn performance does not imply reliability in multi-turn settings. Multi-turn assistance requires a model to maintain an evolving representation of user requirements and t…

- **[Tail-risk-aware Agent Safety: Constraining Tail Risks Across Multi-step LLM Agent Workflows](https://arxiv.org/abs/2611.10411v1)**
  - *Shilong Pan, Zhiliang Tian, Zihan Chen et al.*
  - `2026-11-07`
  - LLM-based agents extend LLMs with tool calls, memory, planning, and retrieval to act in external environments, but they are vulnerable to attacks at different workflow steps. Existing defenses, including prompt engineering and post-training alignment, primarily improve LLM-only s…

- **[The Limits of Information-Flow Control Enforcement for Agentic Systems](https://arxiv.org/abs/2611.10395v1)**
  - *Jonathan Gregory, Kyle Domico, Kunyang Li et al.*
  - `2026-11-07`
  - Information-flow control (IFC) is a promising approach to enforce policy in agentic AI systems. However, IFC suffers from label creep, a phenomenon where monotonically increasing security labels propagate through a system and progressively limit its utility. Label creep in agenti…

- **[Crustify: Repository-Level Generation of Safe Rust Bindings with LLM Agents and Coverage-Guided Testing](https://arxiv.org/abs/2611.10394v1)**
  - *Marius Momeu, Marius Arvinte, Cory Cornelius et al.*
  - `2026-11-07`
  - Wrapping C code in a safe Rust interface lets Rust applications use it without writing unsafe code, until the code itself is migrated to Rust. Such bindings are tedious and error-prone to write, however: their internals use unsafe code that the Rust compiler does not check, so a…

- **[A Computational Map of the Disaster Mental Health Research Landscape](https://arxiv.org/abs/2611.10390v1)**
  - *Soheil Shapouri, Saber Soleymani*
  - `2026-11-07`
  - When disasters strike, they not only damage infrastructure, buildings, and the economy, but also affect the mental health of affected populations. Research on the mental health effects of disasters has expanded rapidly and has become an important, well-funded area of psychology,…

- **[LSRP*: Scalable and Anytime Planning for Multi-Agent Path Finding with Asynchronous Actions](https://arxiv.org/abs/2611.10363v1)**
  - *Dachuan Liu, Shuai Zhou, Shizhe Zhao et al.*
  - `2026-11-07`
  - Multi-Agent Path Finding (MAPF) seeks collision-free paths for multiple agents from their respective starting locations to their respective goal locations while minimizing path costs. Although many MAPF algorithms were developed, most of them rely on a common assumption on synchr…

- **[Network Contention State Aware Dynamic Optimizer for Accelerator Collective Communication Libraries](https://arxiv.org/abs/2611.10984v1)**
  - *Rajat Bisht, Tevfik Kosar, Anthony Skjellum et al.*
  - `2026-11-07`
  - Collective Communication Libraries (CCL) are critical for large-scale distributed AI/ML training, yet their configurations are determined by static heuristics that do not account for real-time network conditions. Our empirical study shows that these heuristics perform near-optima…

- **[Risk-Sensitive Reinforcement Learning for an Options Market Maker: An Empirical Study with Real S&P 500 Options](https://arxiv.org/abs/2611.10956v1)**
  - *Jacky Chen, Ing-Haw Cheng, John Hull et al.*
  - `2026-11-07`
  - Options market makers absorb client order flow and must hedge the resulting inventory risk under trading frictions. We study whether an option hedging reinforcement learning (RL) agent trained on historical market data outperforms three alternatives in tail-risk protection: (i) t…

- **[Firepool: Brokering Warm GPU Capacity for Agentic and RL Workloads at LinkedIn](https://arxiv.org/abs/2611.10832v1)**
  - *Ankit Goyal, Santosh Jha, Zhuo Zhi et al.*
  - `2026-11-07`
  - AI agents and reinforcement-learning (RL) trainers run thousands of short, isolated GPU jobs: tool calls, verifiers, and rollouts. A job often finishes in seconds, but starting a GPU pod for it takes 20-35 s even when the container image is already on the node, and minutes when i…

- **[Meta-Reinforcement Learning with Zero-Shot Reinforcement Learning](https://arxiv.org/abs/2611.10553v1)**
  - *Jake Grigsby, Siddhant Agarwal, Yu Lei et al.*
  - `2026-11-07`
  - Meta-reinforcement learning (meta-RL) trains agents to adapt to novel tasks from test-time experience, but requires diverse training environments and reward functions. While environments are becoming cheaper to generate, it remains difficult to anticipate every objective an agent…

- **[TransMem: Transition-Aware Retrieval for Evolving Personal Memory](https://arxiv.org/abs/2611.10683v1)**
  - *Shigeng Chen, Linhao Luo, Changlong Shi et al.*
  - `2026-11-07`
  - Long-term personalized agents are increasingly expected to answer queries over user histories in which preferences, goals, and constraints evolve across interleaved conversations. Existing retrieval-based and structured-memory systems can surface relevant facts, but often return…

- **[Same Contacts, Different Rooms:Meeting Format Shapes LLM Group Influence Beyond Pairwise Contact Counts](https://arxiv.org/abs/2611.10641v1)**
  - *Zhexi Gu, Shusheng Cao, Runping Zhu*
  - `2026-11-07`
  - Simulations of LLM agent collectives usually summarise interaction as a pairwise contact network. We test that summary with a contact-matched intervention: the members, their initial stances and every pairwise contact count stay fixed while the meetings are reorganised, and each…

- **[M3FT: Micro-Macro-Micro Reasoning for Multi-Agent Cryptocurrency Perpetual Futures Trading](https://arxiv.org/abs/2611.10586v1)**
  - *Jiashun Wang, Beile Wang, Guangyan Gan et al.*
  - `2026-11-07`
  - Cryptocurrency perpetual futures form a large-scale online financial market in which automated agents manage interacting asset positions under changing conditions. Policies relying solely on micro-level numerical states may overlook cross-asset relationships and become vulnerable…


## Harness  (106)

### NeurIPS

- **[MVU-Eval: Towards Multi-Video Understanding Evaluation for Multimodal LLMs](https://arxiv.org/abs/2511.07250)**
  - *Tian-Hao Peng, Hao-Cheng Wang, Yuan-Xing Zhang et al.*
  - **NeurIPS 2025** · `2025-11-10`
  - The advent of Multimodal Large Language Models (MLLMs) has expanded AI capabilities to visual modalities, yet existing evaluation benchmarks remain limited to single-video understanding, overlooking the critical need for multi-video understanding in real-world scenarios (e.g., sp…

- **[STRATUS: A Multi-agent System for Autonomous Reliability Engineering of Modern Clouds](https://arxiv.org/abs/2506.02009)**
  - *Yin-Fang Chen, Jia-Qi Pan, Jackson Clark et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - In cloud-scale systems, failures are the norm. A distributed computing cluster exhibits hundreds of machine failures and thousands of disk failures; software bugs and misconfigurations are reported to be more frequent. The demand for autonomous, AI-driven reliability engineering…


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

- **[Can Frontier Auto Researchers Reconstruct Human Research Decisions in AI?](https://arxiv.org/abs/2611.12429v1)**
  - *Shengyun Si, Junjie Chu, Ye Leng et al.*
  - **ICLR** · `2026-11-09`
  - Scientific research has long been driven by substantial human effort, from reviewing prior work and identifying research gaps to designing specific solutions. Recent advances in harness-based agent systems have given rise to increasingly capable Auto Researchers, which can autono…

- **[K-Sort Eval: Efficient Preference Evaluation for Visual Generation via Corrected VLM-as-a-Judge](https://arxiv.org/abs/2602.09411)**
  - *Zhi-Kai Li, Jia-Tong Li, Xue-Wen Liu et al.*
  - **ICLR 2026** · `2026-02-10`
  - The rapid development of visual generative models raises the need for more scalable and human-aligned evaluation methods. While the crowdsourced Arena platforms offer human preference assessments by collecting human votes, they are costly and time-consuming, inherently limiting t…


### KDD

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, A. Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…


### ACL

- **[Embodied First Exam](https://arxiv.org/abs/2611.12177v1)**
  - *Kangrui Wang, Qineng Wang, Changhe Chen et al.*
  - **ACL** · `2026-11-09`
  - Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical…

- **[Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization](https://arxiv.org/abs/2611.12079v1)**
  - *Jui-Chien Tsou, Po-Yi Wu*
  - **ACL** · `2026-11-09`
  - We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels. On 30 KernelBench tasks (levels 1-3, first 10 each, evaluated on a V100), we co…

- **[Treating the Model as an Untrusted Component: Deterministic Policy Enforcement, Human Approval and Taint Tracking Against Prompt Injection in Tool-Using Agents, with Validation on Open-Weights Models](https://arxiv.org/abs/2611.11571v1)**
  - *Mustafa S. Aljumaily, Nawar S. Alseelawi, Raghad Alshabandar*
  - **ACL** · `2026-11-08`
  - Tool-using LLM agents act on instructions embedded in the data they read, so prompt injection is a structural rather than a prompt-wording problem. We compare in-prompt defences (hardened prompts, spotlighting, LLM detectors) with deterministic enforcement outside the model (four…

- **[EndoSCOP-V: A Multi-Turn Video Understanding Evaluation Framework for Multimodal Models in Endoscopy Reporting and Clinical Reasoning](https://arxiv.org/abs/2611.10626v1)**
  - *Abhishek Tyagi, Tanmay Jain, Vilas Biradar et al.*
  - **ACL** · `2026-11-07`
  - Endoscopic diagnosis unfolds over native video, where a single positive finding during traversal of the gastrointestinal tract sets off a multi-minute chain of reasoning over location, morphology, severity and intervention. Existing endoscopy multimodal benchmarks test only stati…

- **[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://arxiv.org/abs/2504.08725)**
  - *Dayu Yang, Antoine Simoulin, Xin Qian et al.*
  - **ACL 2025** · `2025-04-11`
  - High-quality code documentation is crucial for software development especially in the era of AI. However, generating it automatically using Large Language Models (LLMs) remains challenging, as existing approaches often produce incomplete, unhelpful, or factually incorrect outputs…

- **[Semantic-Eval : A Semantic Comprehension Evaluation Framework for Large Language Models Generation without Training](https://aclanthology.org/2025.acl-long.477.pdf)**
  - *Shu-Sheng Li, Jiale Li, Yi-Fei Qu et al.*
  - **ACL 2025**
  - With the increasing prominence of large language models (LLMs), evaluating their text-generation capabilities has become an essential research challenge. Although LLM-based evaluation methods exhibit robust performance, the inherent stochastic nature of the LLM generation process…


### EMNLP

- **[DR3-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://arxiv.org/abs/2604.14683)**
  - *Qian-Qian Xie, He Zhu, Xue Han et al.*
  - **EMNLP 2026** · `2026-04-16`
  - Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR$^{3…

- **[FinDeepForecast: A Live Multi-Agent System for Benchmarking Deep Research Agents in Financial Forecasting](https://arxiv.org/abs/2601.05039)**
  - *Xiang-Yu Li, Xuan Yao, Guo-Hao Qi et al.*
  - **EMNLP 2026** · `2026-01-08`
  - Deep Research (DR) Agents powered by advanced Large Language Models (LLMs) have fundamentally shifted the paradigm for completing complex research tasks. Yet, a comprehensive and live evaluation of their forecasting performance on real-world, research-oriented tasks in high-stake…

- **[Tau-Eval: A Unified Evaluation Framework for Useful and Private Text Anonymization](https://arxiv.org/abs/2506.05979)**
  - *Gabriel Loiseau, Damien Sileo, Damien Riquet et al.*
  - **EMNLP 2025** · `2025-06-06`
  - Text anonymization is the process of removing or obfuscating information from textual data to protect the privacy of individuals. This process inherently involves a complex trade-off between privacy protection and information preservation, where stringent anonymization methods ca…

- **[MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language](https://arxiv.org/abs/2505.14395)**
  - *Seyoung Song, Seogyeong Jeong, Eunsu Kim et al.*
  - **EMNLP 2025** · `2025-05-20`
  - Evaluating text generation capabilities of large language models (LLMs) is challenging, particularly for low-resource languages where methods for direct assessment are scarce. We propose MUG-Eval, a novel framework that evaluates LLMs'multilingual generation capabilities by trans…


### Other / arXiv

- **[InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure](https://arxiv.org/abs/2611.11558)**
  - *InfraRSI Team, Yuchuan Tian, Haocheng Mei et al.*
  - 🤗 Featured · `2026-11-08`
  - While Recursive Self-Improvement (RSI) accelerates isolated algorithm and kernel synthesis, distributed LLM training depends on tightly coupled launch settings, operator kernels, and communication schedules, where single edits often hit out-of-memory (OOM) boundaries, compiler co…

- **[Spatial Harness: Grounding Spatial Reasoning in Executable World States with Physics Engines](https://arxiv.org/abs/2611.11344)**
  - *Chentao Cao, Zhanke Zhou, Sangni Duan et al.*
  - 🤗 Featured · `2026-11-08`
  - Spatial reasoning requires understanding how objects and observers are arranged in a scene and how their relations change with viewpoint or movement. Vision-language models (VLMs) typically perform both steps through model-internal reasoning, forming an implicit scene interpretat…

- **[Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](https://arxiv.org/abs/2611.01112)**
  - *Chengcheng Wang, Yuheng Shi, Siyu Xu et al.*
  - 🤗 Featured · `2026-10-31`

- **[Review the Episodes, Refine the Lessons: Simple Memory Evolution for Embodied Agents](https://arxiv.org/abs/2611.11509)**
  - *Yifei Yao, Yude Zou, Xing Gao et al.*
  - 🤗 · `2026-11-08`
  - Recent studies of embodied agents based on frontier multimodal large language models (MLLMs) develop harness engineering around the MLLM, such as harnesses with post-trained policies and recursive self-improvement loops. Yet whether these additions exceed the native capability of…

- **[SciMARS: Multi-Agent Recursive Self-Improvement for Closed-Loop Scientific Discovery](https://arxiv.org/abs/2611.12552v1)**
  - *Weimin Wu, Han Liu*
  - `2026-11-09`
  - We propose SciMARS, a framework for recursive task-local adaptation of multi-agent harnesses in closed-loop scientific discovery. Multi-agent systems coordinate analysis, experimental design, and verification as scientific evidence evolves. However, two problems limit their effec…

- **[Say Shibboleth: Fingerprinting the LLMs and Harnesses Behind Agentic Attacks](https://arxiv.org/abs/2611.12386v1)**
  - *Dario Pasquini, Reworr, Giuseppe Ateniese et al.*
  - `2026-11-09`
  - We study the fingerprinting of agentic cyberattacks. Our objective is to reliably infer information about the attacker's configuration, such as LLM version and harness, from telemetry. To achieve this, we introduce a technique we call shibboleth traps: modular honeypot services d…

- **[Reconfigurable Action Theories: A Formal Foundation for Dynamically Composable Agent Harnesses](https://arxiv.org/abs/2611.12300v1)**
  - *Jianmin Ji*
  - `2026-11-09`
  - Action theories typically fix their vocabulary and causal laws, whereas agent harnesses can change their tools, providers, and policies during execution. We introduce Reconfigurable Action Theories (RAT), in which actions can change the action theory itself. A theory module in RA…

- **[System Optimizations for Cost-Efficient Agent Harnesses](https://arxiv.org/abs/2611.12122v1)**
  - *Jongseok Park, Jiaxiang Yu, Eric Zhou et al.*
  - `2026-11-09`
  - AI agent harnesses play the critical role of providing LLMs with an interface to a computing environment. Recent studies show that AI agents' task-execution accuracy depends mostly on the LLM used, while harness-side variances such as system prompts or tools have minimal impact.…

- **[Evaluating AI Agents for Industrial-Level Chip Floorplanning: A Framework and Empirical Study](https://arxiv.org/abs/2611.12048v1)**
  - *Nova-Silicon Team*
  - `2026-11-09`
  - Floorplanning is an early step in turning a logical circuit into a physical chip: it positions large circuit modules and constrains the space available for subsequent logic placement and wiring. These decisions affect congestion and timing, but their physical consequences emerge…

- **[Harness Matters: Measuring and Dissecting Security Resilience in Web Agents](https://arxiv.org/abs/2611.11971v1)**
  - *Xinyi Wu, Jiagui Chen, JiaYi Dong et al.*
  - `2026-11-09`
  - Web agents extend LLMs from text generation to real-world web interaction by relying on execution harnesses that interpret user goals, perceive webpages, plan actions, and ground model decisions into browser operations. While prior work has recognized that agent security depends…

- **[Explaining and interrupting collective misalignment in language model systems](https://arxiv.org/abs/2611.11724v1)**
  - *Edoardo Chidichimo*
  - `2026-11-09`
  - In collectives, language model agents can exchange individually innocuous messages that together support a policy violation. Understanding and preventing collective misalignment requires answering the question of which messages sufficiently influenced and necessarily enabled the…

- **[WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2611.12856v1)**
  - *Zheng Jiang, Fang Niu, Bo Peng et al.*
  - `2026-11-09`
  - Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shift…

- **[EmoHarness: Boosting Multimodal Emotion Understanding with Meta-Harness Evolving](https://arxiv.org/abs/2611.11994v1)**
  - *Fenghai Li, Bingxuan Li, Jiawen Zhang et al.*
  - `2026-11-09`
  - Small multimodal models can misjudge emotion when words, voice, and visual cues conflict. We present EmoHarness, which runs such a model, the frozen student, inside a harness: the prompts, settings, and verification code around its calls. A human-written starting harness, the sca…

- **[Inference Validation for Regulated AI: Building a Decision Pipeline on NVIDIA AIPerf](https://arxiv.org/abs/2611.12737v1)**
  - *Dev Akre, Roman Bobalo, Manoj Dobbali*
  - `2026-11-09`
  - Deploying large language models in regulated industries requires more than picking the fastest inference engine: it requires evidence that a configuration meets contractual and legal obligations before it serves a single customer request. We describe Runway, an internal validatio…

- **[Harnessing Vision-Language Models for Federated Unsupervised Visual Recognition](https://arxiv.org/abs/2611.12187v1)**
  - *Jian Liang, Kuangpu Guo, Ran He et al.*
  - `2026-11-09`
  - Federated learning (FL) is a promising research paradigm that enables collaborative model training across distributed clients without data sharing. To handle unlabeled data in local clients, existing unsupervised FL research has primarily focused on tasks like clustering and self…

- **[LiveAsset: Learning Intent Assets from Corrective Interactions for Agent Runtime Control](https://arxiv.org/abs/2611.11560v1)**
  - *Guanming Liu, Weihang Wang, Peng Zhang et al.*
  - `2026-11-08`
  - Large language model (LLM) agents acting across web applications and online services often need multi-turn corrections to align their work with users' underspecified goals and preferences. In practice, users may identify problems in the current outcome without specifying the desi…

- **[Safeguarding Agentic AI in Radiology Workflows: A Multimodel Evaluation of Rule-based and Large Language Model-based Verification](https://arxiv.org/abs/2611.11541v1)**
  - *Semil Eminovic, Robin Schmidt, Bogdan Levita et al.*
  - `2026-11-08`
  - Purpose: To estimate how often tool-using large language model (LLM) agents record clinically relevant false or unsupported information in simulated radiology documentation and how much safeguards applied before each action reduce these errors.   Materials and Methods: In this si…

- **[JoMoHa: Joint Model--Harness Optimization with Reinforcement Learning](https://arxiv.org/abs/2611.11499v1)**
  - *Xudong Wu, Guangchen Lan, Mingqi Yuan et al.*
  - `2026-11-08`
  - The performance of language agents depends jointly on model weights and the harness. Optimizing either alone can be constrained by the other component, limiting overall performance gains. Our analysis of naive alternating training reveals progressive incompatibility between the m…

- **[How to "train" a surgeon? Benchmarking generalist agents in surgical scene understanding](https://arxiv.org/abs/2611.11437v1)**
  - *Gengyuan Zhang, Xiao Han, Shijie Zhou et al.*
  - `2026-11-08`
  - Evaluating general-purpose multimodal large language models (MLLMs) for surgical scene understanding remains limited due to scarce surgical data and fragmented evaluation protocols. We address these challenges through a two-stage evaluation framework for surgical scene understand…

- **[Agent Self-Improvement with Frozen Weights: The Added Value and Limits of Failure Traces](https://arxiv.org/abs/2611.11342v1)**
  - *Arkid Mitra*
  - `2026-11-08`
  - We evaluate whether an AI agent's harness, the notes around its model, can learn from the agent's failure traces beyond a matched search that never sees them. It can, but less than it looks. We tested an open 9-billion-parameter model with fixed weights; a larger teacher model wr…

- **[WarBias: A Bilingual LLM Benchmark of Stereotypes About Internally Displaced People and Veterans](https://arxiv.org/abs/2611.11284v1)**
  - *Viktoriia Makovska, Tetiana Zakharchenko, Oleksandra Ostafiichuk*
  - `2026-11-08`
  - This paper contains examples of stereotypes about veterans and displaced people that may be offensive or distressing. Social bias benchmarks for language models commonly examine categories such as gender, race, and religion, often drawn from lists of legally protected characteris…

- **[DeepFinance: Can AI Diligence a $100MM Deal?](https://arxiv.org/abs/2611.10926v1)**
  - *Drew Hahn, Tyler Shibata, Jackson Grove et al.*
  - `2026-11-07`
  - Existing evaluations of AI models on high-finance work focus on retrieving answers from financial documents and producing numerically correct outputs. Real private equity (PE) and investment banking (IB) work also depends on choosing between conflicting sources, making sound assu…

- **[Trustworthy Recursive Self-Improvement with Statistical Guarantees](https://arxiv.org/abs/2611.10787v1)**
  - *Zihe Gao, Zhengling Qi, Yifan Cui*
  - `2026-11-07`
  - Recursive self-improvement offers a promising path toward AI agents that improve through experience by refining their own harnesses without retraining their underlying large language models (LLMs). Making this self-improvement process reliable, however, requires more than generat…

- **[REINS: A Self-Evolving Agent Harness for Real-Time Trajectory Planning](https://arxiv.org/abs/2611.10748v1)**
  - *Zhihong Cui, Hengyu Liu, Haoran Tang et al.*
  - `2026-11-07`
  - Agent harnesses -- runtime scaffolds that wrap an LLM's reasoning loop with tool dispatch, verification, and persistent memory -- have become the standard substrate for deploying LLMs as autonomous agents, as demonstrated by Claude Code and Codex in software engineering. In traje…

- **[DFT-Agent Bench: Scaffold Effects and Execution Provenance in Autonomous DFT](https://arxiv.org/abs/2611.10629v1)**
  - *Shijie Liu, Jin Yang, Weilin Wan et al.*
  - `2026-11-07`
  - Large language models are increasingly deployed as autonomous agents for first-principles materials simulation. We report empirical findings from DFT-Agent Bench, a benchmark of 200+ Quantum ESPRESSO tasks spanning relaxation, electronic structure, equation-of-state, and elastic-…

- **[InfoOrgBench: Can Agents Turn Scattered Information into Coherent Hierarchies?](https://arxiv.org/abs/2611.10600v1)**
  - *Justice Ou, Lanming Ma, Zijian Zhang et al.*
  - `2026-11-07`
  - When agents organize records into folders, they may correctly group the excerpts of a design proposal yet place the proposal under the wrong owning group. Existing agent benchmarks do not directly measure such higher-level errors. We introduce InfoOrgBench, a benchmark of 150 tas…

- **[Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction](https://arxiv.org/abs/2611.10439v1)**
  - *Yunzhe Wang, Mesut Erhan Unal, Sheng Zhang et al.*
  - `2026-11-07`
  - Self-evolving agents improve their own skills, memory, and harness code from experience without retraining the base LLM, and group-evolving agents go further by sharing these lessons across agents. Yet most such systems overlook that sharing across users and heterogeneous agents…

- **[TransMem: Transition-Aware Retrieval for Evolving Personal Memory](https://arxiv.org/abs/2611.10683v1)**
  - *Shigeng Chen, Linhao Luo, Changlong Shi et al.*
  - `2026-11-07`
  - Long-term personalized agents are increasingly expected to answer queries over user histories in which preferences, goals, and constraints evolve across interleaved conversations. Existing retrieval-based and structured-memory systems can surface relevant facts, but often return…

- **[LongCapHarness: Capability-Guided Auto-Harnessing for Long-Context Reasoning](https://arxiv.org/abs/2611.10463v1)**
  - *Tao Zhang, Yuhang He*
  - `2026-11-07`
  - Existing methods enhancing an LLM's long-context reasoning capability often rely on data synthesis and follow-up LLM post-training. However, the data synthesis strategy and the post-training recipes are empirically driven and computationally intensive. In this work, we propose a…

- **[Learning Biological Hierarchies in Single-Cell Foundation Models](https://arxiv.org/abs/2611.10838v1)**
  - *Xiangyu Guo, Ricardo Henao*
  - `2026-11-07`
  - Cell types are organized by taxonomic relationships that define lineages in the so-called cell ontology. However, most existing foundation models typically ignore cell-type lineages encoded in this cell ontology. We introduce a biologically informed foundation model called scOnto…

- **[Multimodal Models Can See, But Can They Think? A Study of Turkish Visual Reasoning](https://arxiv.org/abs/2611.10831v1)**
  - *Berke Bunyamin Sule, Yavuz Selim Aygan, Ahmed Zeer et al.*
  - `2026-11-07`
  - Vision-Language Models have had massive leaps in recent years. Yet, when tested on high-level cognitive tasks like pattern completion, abstract logic, and relational reasoning, they still fall short. This limitation stems from the models' lack of ability to find out underlying ru…

- **[Quantitative Assessment of Crystal Structure Prediction](https://arxiv.org/abs/2611.10380v1)**
  - *Sergio Rincón, Gabriel González, Nicolás Andrade et al.*
  - `2026-11-07`
  - Crystal Structure Prediction (CSP) aims to predict a material's 3D structure from its chemical composition, with applications from energy storage to biomedical devices. Despite its importance, existing evaluation frameworks suffer from key limitations: they rely on threshold-sens…


## Finance  (151)

### AAAI

- **[LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042)**
  - *Cheng Yang, Hui Jin, Xinlei Yu et al.*
  - **AAAI 2025** · `2025-11-26`
  - Diagnosing lung cancer typically involves physicians identifying lung nodules in Computed tomography (CT) scans and generating diagnostic reports based on their morphological features and medical expertise. Although advancements have been made in using multimodal large language m…

- **[CoDe: Communication Delay-Tolerant Multi-Agent Collaboration via Dual Alignment of Intent and Timeliness](https://arxiv.org/abs/2501.05207)**
  - *Shou-Cheng Song, You-Fang Lin, Sheng Han et al.*
  - **AAAI 2025** · `2025-01-09`
  - Communication has been widely employed to enhance multi-agent collaboration. Previous research has typically assumed delay-free communication, a strong assumption that is challenging to meet in practice. However, real-world agents suffer from channel delays, receiving messages se…


### NeurIPS

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **NeurIPS 2025** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…

- **[AutoData: A Multi-Agent System for Open Web Data Collection](https://arxiv.org/abs/2505.15859)**
  - *Tian-Yi Ma, Yi-Yue Qian, Zhe-Yuan Zhang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - The exponential growth of data-driven systems and AI technologies has intensified the demand for high-quality web-sourced datasets. While existing datasets have proven valuable, conventional web data collection approaches face significant limitations in terms of human effort and…

- **[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)**
  - *Yuan-Te Li, Xu Yang, Xiao Yang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - Financial markets pose fundamental challenges for asset return prediction due to their high dimensionality, non-stationarity, and persistent volatility. Despite advances in large language models and multi-agent systems, current quantitative research pipelines suffer from limited…


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


### ACL

- **[Depth as a Candidate Source: Portfolio Allocation for Recurrent Test-Time Scaling in Large Language Models](https://arxiv.org/abs/2611.12293v1)**
  - *Chaoyuan Hao, Wentao Yue, Yanyan Wu et al.*
  - **ACL** · `2026-11-09`
  - Recurrent latent reasoning in large lanugage models (LLMs) scales test-time computation by increasing recurrent depth, naturally framing inference as a problem of deciding when to stop. We identify a previously overlooked limitation of this single-depth view through systematic pr…

- **[Worst-Case Contagion in Financial Networks: MILP Clearing and Robust Loss Analysis](https://arxiv.org/abs/2611.10607v1)**
  - *G. C. Calafiore, M. Della Rossa, A. Proskurnikov*
  - **ACL** · `2026-11-07`
  - We study worst-case contagion losses in financial networks with interbank liabilities and common exposures to marketable assets. Existing linear-programming approaches provide exact stress-test values only within an insolvency-resilience margin, where all institutions remain solv…

- **[METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](https://arxiv.org/abs/2502.17651)**
  - *Bing-Xuan Li, Yi-Wei Wang, Jiu-Xiang Gu et al.*
  - **ACL 2025** · `2025-02-24`
  - Chart generation aims to generate code to produce charts satisfying the desired visual properties, e.g., texts, layout, color, and type. It has great potential to empower the automatic professional report generation in financial analysis, research presentation, education, and hea…

- **[G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems](https://arxiv.org/abs/2502.11127)**
  - *Shilong Wang, Gui-Min Zhang, Miao Yu et al.*
  - **ACL 2025** · `2025-02-16`
  - Large Language Model (LLM)-based Multi-agent Systems (MAS) have demonstrated remarkable capabilities in various complex tasks, ranging from collaborative problem-solving to autonomous decision-making. However, as these systems become increasingly integrated into critical applicat…


### EMNLP

- **[DR3-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://arxiv.org/abs/2604.14683)**
  - *Qian-Qian Xie, He Zhu, Xue Han et al.*
  - **EMNLP 2026** · `2026-04-16`
  - Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR$^{3…

- **[FinDeepForecast: A Live Multi-Agent System for Benchmarking Deep Research Agents in Financial Forecasting](https://arxiv.org/abs/2601.05039)**
  - *Xiang-Yu Li, Xuan Yao, Guo-Hao Qi et al.*
  - **EMNLP 2026** · `2026-01-08`
  - Deep Research (DR) Agents powered by advanced Large Language Models (LLMs) have fundamentally shifted the paradigm for completing complex research tasks. Yet, a comprehensive and live evaluation of their forecasting performance on real-world, research-oriented tasks in high-stake…

- **[QuantAgents: Towards Multi-agent Financial System via Simulated Trading](https://arxiv.org/abs/2510.04643)**
  - *Xiang-Yu Li, Ya-Wen Zeng, Xiao-Fen Xing et al.*
  - **EMNLP 2025** · `2025-10-06`
  - In this paper, our objective is to develop a multi-agent financial system that incorporates simulated trading, a technique extensively utilized by financial professionals. While current LLM-based agent models demonstrate competitive performance, they still exhibit significant dev…

- **[AMAS: Adaptively Determining Communication Topology for LLM-based Multi-Agent System](https://arxiv.org/abs/2510.01617)**
  - *Hui Yi Leong, Yuheng Li, Yu-Qing Wu et al.*
  - **EMNLP 2025** · `2025-10-02`
  - Although large language models (LLMs) have revolutionized natural language processing capabilities, their practical implementation as autonomous multi-agent systems (MAS) for industrial problem-solving encounters persistent barriers. Conventional MAS architectures are fundamental…


### Other / arXiv

- **[How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time](https://arxiv.org/abs/2611.12324)**
  - *Ku Onoda, Haruto Kawano, Shota Takashiro et al.*
  - 🤗 Featured · `2026-11-09`
  - World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction. A mechanic is a rule for how an action or an interaction changes part of the environment. Each occurrence of a mechanic…

- **[HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents](https://arxiv.org/abs/2611.12872v1)**
  - *Haozhen Zhang, Bohan Liu, Jianzhu Bao et al.*
  - `2026-11-09`
  - As multimodal agents accumulate increasingly long interaction histories, effectively retrieving and utilizing past information becomes critical for long-term interaction. Existing memory systems typically rely on semantic retrieval over compressed memories and expose predefined r…

- **[From Fluent Text to Ontology-Compatible Definitions: A Quality-Control Agentic Workflow](https://arxiv.org/abs/2611.12095v1)**
  - *Kun Feng, Chenchen Chu, Yan Liu et al.*
  - `2026-11-09`
  - Biomedical ontologies are structured knowledge systems that must evolve continuously to represent newly emerging knowledge, but their manual maintenance remains time-consuming and laborintensive. Textual definitions are especially costly because they must be readable to humans an…

- **[CRAFT-AI: Capability and Requirement Alignment for Flexible Manufacturing through Agentic AI](https://arxiv.org/abs/2611.12092v1)**
  - *Kiavash Fathi, Hans Wernher van de Venn*
  - `2026-11-09`
  - One of the fundamental needs for reaching resilient production infrastructure is flexible manufacturing, which requires translating changing production requirements into implementable system configurations. This paper introduces \textbf{CRAFT-AI}, an agentic AI approach combining…

- **[Can LLM Agents Organize Their Own Memory?](https://arxiv.org/abs/2611.11929v1)**
  - *Zichuan Fu, Junjia Qi, Wenlin Zhang et al.*
  - `2026-11-09`
  - In most LLM agents, weights are fixed after deployment, so new information must be retained in external memory. Existing approaches often rely on predefined records and fixed organizational rules, which cannot readily accommodate evolving tasks and interactions. This raises the q…

- **[HolidayFactory 1.0: Simulating, Generating, and Evaluating Industrial Robot Tasks](https://arxiv.org/abs/2611.11789v1)**
  - *Holiday Robotics, :, Jeongmin Lee et al.*
  - `2026-11-09`
  - Robots are typically evaluated in episodes that begin from a reset, while industrial work consists of repeated jobs whose outcomes affect subsequent operations. Evaluating such work at scale requires simulation of task-critical physical interactions, construction of industrial en…

- **[Mitigating Agentic Deception via Evaluation-Side Partially Observable Games](https://arxiv.org/abs/2611.12835v1)**
  - *Hanxiao Li, Shutong Liu, Yongjia Ma et al.*
  - `2026-11-09`
  - As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful. We attribute this failure to evaluation-side partial observability, where models are evaluated mainly from final outcome, without…

- **[Trajectory Density Ratios under Weak Support: A Survey across the Sciences](https://arxiv.org/abs/2611.11985v1)**
  - *Wei Chen, Lihao Zhuang, Yubing Wu et al.*
  - `2026-11-09`
  - Many problems across the sciences compare two stochastic processes through the sequences they generate. Reinforcement learning asks what a new policy would return from the trajectories of an old one; molecular simulation asks how much more a ligand binds from samples of the unbou…

- **[Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading](https://arxiv.org/abs/2611.12269v1)**
  - *Guangyan Gan, Jiahao Li, Jiashun Wang et al.*
  - `2026-11-09`
  - Cryptocurrency markets provide a natural testbed for autonomous AI agents because they are digital-native, high-frequency, and machine-speed environments, yet existing methods often struggle with non-stationary market regimes, opaque decisions, and fixed aggregation rules. In thi…

- **[Diversification Across Predictors: Heterogeneous Ensemble Learning for Cross-Sectional Return Prediction](https://arxiv.org/abs/2611.12389v1)**
  - *Danning Li*
  - `2026-11-09`
  - Cross-sectional stock return prediction remains challenging due to extremely low signal-to-noise ratios, high-dimensional factor spaces, and non-stationary predictor effectiveness. Individual model classes exhibit complementary failure modes in this regime: neural networks overfi…

- **[NearFormer: Linear-Size Sparse Attention via Randomized Near Neighbors](https://arxiv.org/abs/2611.12186v1)**
  - *Ali Parviz, Alex Cloninger, Gal Mishne*
  - `2026-11-09`
  - Graph transformers can capture long-range interactions, but their quadratic attention cost limits their use on large graphs. We introduce \emph{NearFormer}, a graph transformer whose global attention is restricted to a randomized near-neighbor (NN) graph. NearFormer uses an effic…

- **[Same Physics, Different Gradients: A State-of-the-Art Report on Differentiable Physics Simulation](https://arxiv.org/abs/2611.12162v1)**
  - *Lei Shu, Zizhou Huang, Yunuo Chen et al.*
  - `2026-11-09`
  - Differentiable simulation propagates derivatives through a physics simulator, turning animation, system identification, control, and computational design into gradient-based optimization. Engines differ in the physics they model and, less visibly, in which mathematical object the…

- **[Diversified-Risk-Perception Risk Measures and Portfolio Selection](https://arxiv.org/abs/2611.11803v1)**
  - *Yang Liu, Yuhao Liu, Jiani Shen*
  - `2026-11-09`
  - Traditional risk measures generally rely on a single probability model, potentially overlooking information from alternative models and leading to biased risk assessments. This limitation cannot be addressed by asset diversification alone in risk management. In this paper, we pro…

- **[A Black-Box Reduction from Regret to Multi-Level Coverage](https://arxiv.org/abs/2611.12059v1)**
  - *Tuo Liu, Edgar Dobriban, Francesco Orabona*
  - `2026-11-09`
  - Online Conformal Prediction (OCP) sequentially constructs prediction sets whose average empirical coverage converges to a target level over time, for arbitrary, potentially adversarial datasets. In the multi-level setting, prediction sets are produced at $d$ coverage levels at on…

- **[Inside the Trading Loop: Markets, Models, and Moves with LLM Agents](https://arxiv.org/abs/2611.11657v1)**
  - *Renee Jia, Di Mu, Yao Yu et al.*
  - `2026-11-08`
  - We built a hybrid multi-agent trading system that combines large language model (LLM) analysts with momentum-based portfolio construction and rule-based execution. Company-news and macroeconomic agents return structured reports to a coordinator that sets stock weights and cash re…

- **[On the Relative Security of Prompt Injection: Mechanised Definitions, Defences and Verdicts for LLM Agents](https://arxiv.org/abs/2611.11506v1)**
  - *Brijesh Dongol*
  - `2026-11-08`
  - An LLM agent that reads untrusted content, such as an email or a web page, may follow instructions hidden in it. Noninterference is too strong for such agents, since a useful agent lets untrusted content influence what it does and may disclose the user's data by design, and decla…

- **[Agentic Attribution of Cloud Resource Ownership](https://arxiv.org/abs/2611.11340v1)**
  - *Tiltan Gilat, Gal Engelberg, Ariel Zadok et al.*
  - `2026-11-08`
  - Security tools raise findings across cloud environments, and AI agents now investigate and prioritize them. A finding is still resolved by people: it has to reach the people responsible for fixing it and accountable for the resource it concerns. Ownership is the organizational co…

- **[Statopia: A Prover--Library Ecosystem for Automated Formalization and Proof Discovery in Statistics](https://arxiv.org/abs/2611.11110v1)**
  - *Ziyuan Chen, Tong Gan, Wei Zhang et al.*
  - `2026-11-08`
  - Theoretical results in statistics and machine learning rest on long, technically delicate proofs, and fluent arguments generated by large language models are not necessarily correct. Automated formalization makes such arguments mechanically checkable, and automated proving goes f…

- **[How Efficient Is Your Agent? Online Predictive Bounds under Budget Constraints](https://arxiv.org/abs/2611.11279v1)**
  - *Roy Maor Lotan, Shai Feldman, Yaniv Romano*
  - `2026-11-08`
  - We evaluate AI agents in an online setting where tasks arrive sequentially and, before running each task, we construct an upper predictive bound on its \emph{time-to-success}---the number of interactions until the task is completed successfully. Under a limited budget, some runs…

- **[FinCutBench: A Continually Updated Benchmark for Measuring the Temporal Boundaries of LLM Financial Knowledge](https://arxiv.org/abs/2611.11588v1)**
  - *Siyuan Li, Ke Wan, Boyong Hou et al.*
  - `2026-11-08`
  - In financial backtesting and other point-in-time tasks, external inputs can be restricted by date, but model parameters may retain financial facts disclosed later, introducing parametric look-ahead bias. We introduce FinCutBench, a continually updated monthly financial knowledge…

- **[Retrospective Analysis of Team-Following Trading Profitability in Pumpfun Meme Coins Using Funding Networks](https://arxiv.org/abs/2611.11436v1)**
  - *Fail Gafarov*
  - `2026-11-08`
  - If the right token-creation teams had been known, how much could following them have returned, and what is left when only information available before each launch is used? We study ten separately recorded Pumpfun windows (April 2024 to September 2026), each reconstructed independ…

- **[Think or Remember: The Exchange Rate of Agentic Inference](https://arxiv.org/abs/2611.10982v1)**
  - *Juan Wisznia, Santiago Luis Groba Alonso, Matías Gómez Taddeo et al.*
  - `2026-11-07`
  - Agents built on reasoning models resend their growing transcript at every call. Two transacting parties, not the model, decide what that costs: the client keeps or edits messages; the server decides whether earlier reasoning returns in the prompt and what its cache reuses. We def…

- **[Improving Analytic Constants via Interpretable AI-Guided Lean Proof Refinement](https://arxiv.org/abs/2611.10961v1)**
  - *Rahul Saha, Alan Li, Anton Xue et al.*
  - `2026-11-07`
  - AI agents are increasingly capable of discovering new mathematical results, yet their reasoning and generated proofs can be difficult to understand and verify. We introduce an interpretable framework for AI-guided mathematical discovery, focused on improving quantitative bounds o…

- **[DeepFinance: Can AI Diligence a $100MM Deal?](https://arxiv.org/abs/2611.10926v1)**
  - *Drew Hahn, Tyler Shibata, Jackson Grove et al.*
  - `2026-11-07`
  - Existing evaluations of AI models on high-finance work focus on retrieving answers from financial documents and producing numerically correct outputs. Real private equity (PE) and investment banking (IB) work also depends on choosing between conflicting sources, making sound assu…

- **[A Gamified Framework for Conflict-Driven Design: Discovering Strategies for Collaborative Resilience with Multi-Agent Learning](https://arxiv.org/abs/2611.10841v1)**
  - *Jin Gao*
  - `2026-11-07`
  - Conflicting stakeholder objectives make it difficult to coordinate investments in urban resilience. We model conflict-driven urban design as a non-zero-sum digital board game in which stakeholder agents allocate scarce resources and balance individual payoffs against shared urban…

- **[Sampling Is Not Curiosity: Why LLM Agents Should Investigate](https://arxiv.org/abs/2611.10501v1)**
  - *Alfonso Amayuelas, Piotr Piękos, Xin Eric Wang et al.*
  - `2026-11-07`
  - LLM agents are increasingly used for open-ended tasks, very common in research scenarios where they are required to explore, investigate, or act curiously. At inference time, an LLM is a fixed map from context to next-token distribution, the pretrained weights determine the funct…

- **[Track or Follow? A Jev-Compatible Multi-Agent Trading System When Web News Lags the Market](https://arxiv.org/abs/2611.10414v1)**
  - *Yebo Feng, Guangyan Gan, Liangrui Pan et al.*
  - `2026-11-07`
  - LLM agents increasingly trade on the Web news they read, yet much Web news about listed firms is published after, and about, the price move it reports, so a reader can agree with the market by following it instead of reading the event. We ask whether LLM judgments of Web news tra…

- **[Crustify: Repository-Level Generation of Safe Rust Bindings with LLM Agents and Coverage-Guided Testing](https://arxiv.org/abs/2611.10394v1)**
  - *Marius Momeu, Marius Arvinte, Cory Cornelius et al.*
  - `2026-11-07`
  - Wrapping C code in a safe Rust interface lets Rust applications use it without writing unsafe code, until the code itself is migrated to Rust. Such bindings are tedious and error-prone to write, however: their internals use unsafe code that the Rust compiler does not check, so a…

- **[Risk-Sensitive Reinforcement Learning for an Options Market Maker: An Empirical Study with Real S&P 500 Options](https://arxiv.org/abs/2611.10956v1)**
  - *Jacky Chen, Ing-Haw Cheng, John Hull et al.*
  - `2026-11-07`
  - Options market makers absorb client order flow and must hedge the resulting inventory risk under trading frictions. We study whether an option hedging reinforcement learning (RL) agent trained on historical market data outperforms three alternatives in tail-risk protection: (i) t…

- **[M3FT: Micro-Macro-Micro Reasoning for Multi-Agent Cryptocurrency Perpetual Futures Trading](https://arxiv.org/abs/2611.10586v1)**
  - *Jiashun Wang, Beile Wang, Guangyan Gan et al.*
  - `2026-11-07`
  - Cryptocurrency perpetual futures form a large-scale online financial market in which automated agents manage interacting asset positions under changing conditions. Policies relying solely on micro-level numerical states may overlook cross-asset relationships and become vulnerable…

- **[Learning Biological Hierarchies in Single-Cell Foundation Models](https://arxiv.org/abs/2611.10838v1)**
  - *Xiangyu Guo, Ricardo Henao*
  - `2026-11-07`
  - Cell types are organized by taxonomic relationships that define lineages in the so-called cell ontology. However, most existing foundation models typically ignore cell-type lineages encoded in this cell ontology. We introduce a biologically informed foundation model called scOnto…

- **[SAMBoost: Spatially Aware Mesh Boosting](https://arxiv.org/abs/2611.10373v1)**
  - *Mulah Moriah, Franck Vermet, Pierre Ailliot et al.*
  - `2026-11-07`
  - We propose SAMBoost (Spatially Aware Mesh Boosting), a gradient boosting method that combines tree-based covariate modelling with a stochastic partial differential equation (SPDE) latent spatial field through a single penalised objective. At each boosting iteration, the predictor…


---
*Generated 2026-11-10 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
