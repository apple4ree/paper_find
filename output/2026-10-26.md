# Daily Paper Digest — 2026-10-26 (Monday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**300 unique papers** (386 topic-entries — cross-topic papers counted once per category)

---

## Agent  (190)

### AAAI

- **[LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042)**
  - *Cheng Yang, Hui Jin, Xinlei Yu et al.*
  - **AAAI 2025** · `2025-11-26`
  - Diagnosing lung cancer typically involves physicians identifying lung nodules in Computed tomography (CT) scans and generating diagnostic reports based on their morphological features and medical expertise. Although advancements have been made in using multimodal large language m…

- **[Rethinking the Reliability of Multi-agent System: A Perspective from Byzantine Fault Tolerance](https://arxiv.org/abs/2511.10400)**
  - *Lifang Zheng, Jiawei Chen, Qing-Hong Yin et al.*
  - **AAAI 2025** · `2025-11-13`
  - Ensuring the reliability of agent architectures and effectively identifying problematic agents when failures occur are crucial challenges in multi-agent systems (MAS). Advances in large language models (LLMs) have established LLM-based agents as a major branch of MAS, enabling ma…

- **[Talk2Image: A Multi-Agent System for Multi-Turn Image Generation and Editing](https://arxiv.org/abs/2508.06916)**
  - *Shichao Ma, Yunhe Guo, Jia-Hao Su et al.*
  - **AAAI 2025** · `2025-08-09`
  - Text-to-image generation tasks have driven remarkable advances in diverse media applications, yet most focus on single-turn scenarios and struggle with iterative, multi-turn creative tasks. Recent dialogue-based systems attempt to bridge this gap, but their single-agent, sequenti…

- **[Exploring the Efficacy of Multi-Agent Reinforcement Learning for Autonomous Cyber Defence: A CAGE Challenge 4 Perspective](https://doi.org/10.1609/aaai.v39i28.35158)**
  - *Mitchell Kiely, Metin B. Ahiskali, E. Borde et al.*
  - **AAAI 2025** · `2025-04-11`
  - As cyber threats become increasingly automated and sophisticated, novel solutions must be introduced to improve defence of enterprise networks. Deep Reinforcement Learning (DRL) has demonstrated potential in mitigating these advanced threats. Single DRL Agents have proven utility…

- **[AutoMV: An Autonomous Agent Framework for Real Estate Marketing Video Generation](https://doi.org/10.1609/aaai.v39i28.35377)**
  - *Kuizong Wu, Shao-Zu Yuan, Chang Shen et al.*
  - **AAAI 2025** · `2025-04-11`
  - In this paper, we introduce AutoMV, an autonomous agent framework designed for generating real estate marketing videos. The framework integrates a diverse set of existing models into a tool library, allowing the agent to intelligently select and execute the appropriate tools. Giv…

- **[OpenDriveVLA: Towards End-to-end Autonomous Driving with Large Vision Language Action Model](https://arxiv.org/abs/2503.23463)**
  - *Xingcheng Zhou, Xu Han, Feng Yang et al.*
  - **AAAI 2025** · `2025-03-30`
  - We present OpenDriveVLA, a Vision-Language Action (VLA) model designed for end-to-end autonomous driving, built upon open-source large language models. OpenDriveVLA generates spatially-grounded driving actions by leveraging multimodal inputs, including both 2D and 3D instance-awa…


### NeurIPS

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **NeurIPS 2025** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **NeurIPS 2025** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…

- **[WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)**
  - *Jia-Long Wu, Baixuan Li, Run-Nan Fang et al.*
  - **NeurIPS 2025** · `2025-05-28`
  - Addressing intricate real-world problems necessitates in-depth information seeking and multi-step reasoning. Recent progress in agentic systems, exemplified by Deep Research, underscores the potential for autonomous multi-step research. In this work, we present a cohesive paradig…

- **[STRATUS: A Multi-agent System for Autonomous Reliability Engineering of Modern Clouds](https://arxiv.org/abs/2506.02009)**
  - *Yinfang Chen, Jia-Qi Pan, J. Clark et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - In cloud-scale systems, failures are the norm. A distributed computing cluster exhibits hundreds of machine failures and thousands of disk failures; software bugs and misconfigurations are reported to be more frequent. The demand for autonomous, AI-driven reliability engineering…

- **[AutoData: A Multi-Agent System for Open Web Data Collection](https://arxiv.org/abs/2505.15859)**
  - *Tian-Yi Ma, Yi-Yue Qian, Zhe-Yuan Zhang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - The exponential growth of data-driven systems and AI technologies has intensified the demand for high-quality web-sourced datasets. While existing datasets have proven valuable, conventional web data collection approaches face significant limitations in terms of human effort and…

- **[MLZero: A Multi-Agent System for End-to-end Machine Learning Automation](https://arxiv.org/abs/2505.13941)**
  - *Haoyang Fang, Bo-Ran Han, Nick Erickson et al.*
  - **NeurIPS 2025** · `2025-05-20`
  - Existing AutoML systems have advanced the automation of machine learning (ML); however, they still require substantial manual configuration and expert input, particularly when handling multimodal data. We introduce MLZero, a novel multi-agent framework powered by Large Language M…

- **[Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657)**
  - *M. Cemri, Melissa Z. Pan, Shuyi Yang et al.*
  - **NeurIPS 2025** · `2025-03-17`
  - Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal. This gap highlights a critical need for a principled understanding of why MAS fail. Addressing this question requires systematic identification and analysis of f…

- **[AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/abs/2503.09780)**
  - *A. Zharmagambetov, Chuan Guo, Ivan Evtimov et al.*
  - **NeurIPS 2025** · `2025-03-12`
  - Autonomous AI agents that can follow instructions and perform complex multi-step tasks have tremendous potential to boost human productivity. However, to perform many of these tasks, the agents need access to personal information from their users, raising the question of whether…

- **[MobileUse: A Hierarchical Reflection-Driven GUI Agent for Autonomous Mobile Operation](https://www.semanticscholar.org/paper/d6515c1b4f75aca67449bc9b2f7045433c03d920)**
  - *Ning Li, Xiang-Mou Qu, Jiamu Zhou et al.*
  - **NeurIPS 2025**
  - Recent advances in Multimodal Large Language Models (MLLMs) have enabled the development of mobile agents that can understand visual inputs and follow user instructions, unlocking new possibilities for automating complex tasks on mobile devices. However, applying these models to…


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

- **[RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](https://arxiv.org/abs/2501.18160)**
  - *Jinyao Guo, Cheng-Peng Wang, Xiang-Zhe Xu et al.*
  - **ICML 2025** · `2025-01-30`
  - Code auditing is the process of reviewing code with the aim of identifying bugs. Large Language Models (LLMs) have demonstrated promising capabilities for this task without requiring compilation, while also supporting user-friendly customization. However, auditing a code reposito…


### ICLR

- **[DriveTransformer: Unified Transformer for Scalable End-to-End Autonomous Driving](https://arxiv.org/abs/2503.07656)**
  - *Xiao-Song Jia, Jun-Qi You, Zhiyuan Zhang et al.*
  - **ICLR 2025** · `2025-03-07`
  - End-to-end autonomous driving (E2E-AD) has emerged as a trend in the field of autonomous driving, promising a data-driven, scalable approach to system design. However, existing E2E-AD methods usually adopt the sequential paradigm of perception-prediction-planning, which leads to…


### CVPR

- **[An LLM-Enabled Multi-Agent Autonomous Mechatronics Design Framework](https://arxiv.org/abs/2504.14681)**
  - *Ze-Yu Wang, Frank P.-W. Lo, Qian Chen et al.*
  - **CVPR 2025** · `2025-04-20`
  - Existing LLM-enabled multi-agent frameworks are predominantly limited to digital or simulated environments and confined to narrowly focused knowledge domain, constraining their applicability to complex engineering tasks that require the design of physical embodiment, cross-discip…


### ACL

- **[Temp-R1: A Unified Autonomous Agent for Complex Temporal KGQA via Reverse Curriculum Reinforcement Learning](https://arxiv.org/abs/2601.18296)**
  - *Zhaoyan Gong, Zhiqiang Liu, Song-Ze Li et al.*
  - **ACL 2026** · `2026-01-26`
  - Temporal Knowledge Graph Question Answering (TKGQA) is inherently challenging, as it requires sophisticated reasoning over dynamic facts with multi-hop dependencies and complex temporal constraints. Existing methods rely on fixed workflows and expensive closed-source APIs, limiti…

- **[MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive and MCP-Augmented Environments](https://arxiv.org/abs/2512.19432)**
  - *Qu-Yu Kong, Xu Zhang, Zhen-Yu Yang et al.*
  - **ACL 2025** · `2025-12-22`
  - Among existing online mobile-use benchmarks, AndroidWorld has emerged as the dominant benchmark due to its reproducible environment and deterministic evaluation; however, recent agents achieving over 90% success rates indicate its saturation and motivate the need for a more chall…

- **[AnnaAgent: Dynamic Evolution Agent System with Multi-Session Memory for Realistic Seeker Simulation](https://arxiv.org/abs/2506.00551)**
  - *Ming Wang, Pei-Dong Wang, Lin Wu et al.*
  - **ACL 2025** · `2025-05-31`
  - Constrained by the cost and ethical concerns of involving real seekers in AI-driven mental health, researchers develop LLM-based conversational agents (CAs) with tailored configurations, such as profiles, symptoms, and scenarios, to simulate seekers. While these efforts advance A…

- **[GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://arxiv.org/abs/2505.16827)**
  - *Bin Xie, Rui Shao, Gongwei Chen et al.*
  - **ACL 2025** · `2025-05-22`
  - GUI automation faces critical challenges in dynamic environments. MLLMs suffer from two key issues: misinterpreting UI components and outdated knowledge. Traditional fine-tuning methods are costly for app-specific knowledge updates. We propose GUI-explorer, a training-free GUI ag…

- **[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://arxiv.org/abs/2504.08725)**
  - *Dayu Yang, Antoine Simoulin, Xin Qian et al.*
  - **ACL 2025** · `2025-04-11`
  - High-quality code documentation is crucial for software development especially in the era of AI. However, generating it automatically using Large Language Models (LLMs) remains challenging, as existing approaches often produce incomplete, unhelpful, or factually incorrect outputs…

- **[NetSafe: Exploring the Topological Safety of Multi-agent System](https://aclanthology.org/2025.findings-acl.150.pdf)**
  - *Miao Yu, Shilong Wang, Guibin Zhang et al.*
  - **ACL 2025**
  - ,


### EMNLP

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

- **[MT-Mol:Multi Agent System with Tool-based Reasoning for Molecular Optimization](https://arxiv.org/abs/2505.20820)**
  - *Hyomin Kim, Yunhui Jang, Sungsoo Ahn*
  - **EMNLP 2025** · `2025-05-27`
  - Large language models (LLMs) have large potential for molecular optimization, as they can gather external chemistry tools and enable collaborative interactions to iteratively refine molecular candidates. However, this potential remains underexplored, particularly in the context o…

- **[ReSo: A Reward-driven Self-organizing LLM-based Multi-Agent System for Reasoning Tasks](https://arxiv.org/abs/2503.02390)**
  - *Heng Zhou, He-Jia Geng, Xiangyuan Xue et al.*
  - **EMNLP 2025** · `2025-03-04`
  - Multi-agent systems (MAS) have emerged as a promising approach for enhancing the reasoning capabilities of large language models in complex problem-solving; however, current MAS frameworks suffer from poor flexibility and scalability with underdeveloped optimization strategies. T…

- **[Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances](https://arxiv.org/abs/2502.16804)**
  - *Yaozu Wu, Dong-Yuan Li, Yan-Kai Chen et al.*
  - **EMNLP 2025** · `2025-02-24`
  - Autonomous Driving Systems (ADSs) are revolutionizing transportation by reducing human intervention, improving operational efficiency, and enhancing safety. Large Language Models (LLMs) have been integrated into ADSs to support high-level decision-making through their powerful re…

- **[Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)**
  - *Samuel Schmidgall, Yu-Sheng Su, Ze Wang et al.*
  - **EMNLP 2025** · `2025-01-08`
  - Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory, an…


### NAACL

- **[Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://arxiv.org/abs/2502.10857)**
  - *Haoyuan Wu, Haisheng Zheng, Zhuo-Lun He et al.*
  - **NAACL 2025** · `2025-02-15`
  - Recently, with the development of tool-calling capabilities in large language models (LLMs), these models have demonstrated significant potential for automating electronic design automation (EDA) flows by interacting with EDA tool APIs via EDA scripts. However, considering the li…

- **[CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://arxiv.org/abs/2501.16609)**
  - *Faria Huq, Zora Zhiruo Wang, Frank F. Xu et al.*
  - **NAACL 2025** · `2025-01-28`
  - While much work on web agents emphasizes the promise of autonomously performing tasks on behalf of users, in reality, agents often fall short on complex tasks in real-world contexts and modeling user preference. This presents an opportunity for humans to collaborate with the agen…

- **[MASTER: A Multi-Agent System with LLM Specialized MCTS](https://arxiv.org/abs/2501.14304)**
  - *Bingzheng Gan, Yu-Fan Zhao, Tian-Yi Zhang et al.*
  - **NAACL 2025** · `2025-01-24`
  - Large Language Models (LLM) are increasingly being explored for problem-solving tasks. However, their strategic planning capability is often viewed with skepticism. Recent studies have incorporated the Monte Carlo Tree Search (MCTS) algorithm to augment the planning capacity of L…

- **[A Layered Debating Multi-Agent System for Similar Disease Diagnosis](https://aclanthology.org/2025.naacl-short.46.pdf)**
  - *Yu-Tian Zhao, Hui-Min Wang, Yefeng Zheng et al.*
  - **NAACL 2025**
  - Distinguishing between extremely similar diseases is a critical and challenging aspect of clinical decision-making. Traditional classification, contrastive learning, and Large Language Models (LLMs) based methods fail to detect the subtle clues necessary for differentiation. This…


### Other / arXiv

- **[RSIHub: A Composable Framework for Agent-Evolution Methods](https://arxiv.org/abs/2610.32253)**
  - *Zimu Wang, Xiaobo Wang, Siyu Ye et al.*
  - 🤗 Featured · `2026-10-23`
  - Agent-evolution methods use execution feedback to improve prompts, skills, tools, and orchestration, but their implementations often rebuild the same experimental machinery. We present RSIHub, an open-source framework for building, comparing, and extending these methods on shared…

- **[UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents](https://arxiv.org/abs/2610.30932)**
  - *Jujia Zhao, Jiakai Tang, Jing Yu et al.*
  - 🤗 Featured · `2026-10-22`

- **[HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games](https://arxiv.org/abs/2610.31162)**
  - *Zecong Tang, Zian Guan, Yuncheng Guo et al.*
  - 🤗 Featured · `2026-10-22`

- **[Dual Exam: Controlled Evaluation of Multimodal Agents and World Models](https://arxiv.org/abs/2610.31066)**
  - *Zhefan Rao, Meng Chu, Xuan Zhang et al.*
  - 🤗 Featured · `2026-10-22`

- **[DraMaze: A Multi-Agent Pipeline with Future-Aware Memory for Diverse Microdrama Script Generation](https://arxiv.org/abs/2610.32002)**
  - *Siyang He, Qiqi Wang, Fan Liu et al.*
  - 🤗 Featured · `2026-10-22`

- **[MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation](https://arxiv.org/abs/2610.23234)**
  - *Yuhan Sun, Jiaxin Zhao, Yongdong Luo et al.*
  - 🤗 Featured · `2026-10-20`

- **[SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning](https://arxiv.org/abs/2610.32978)**
  - *Yuhan Liu, Lianhui Qin, Shenji Wan*
  - 🤗 · `2026-10-23`
  - Training generalizable embodied agents requires realistic, varied, and simulation-ready indoor environments. Language-guided methods support semantic planning and object-level reasoning, but precise spatial grounding remains difficult. Visual generative models offer rich priors o…

- **[Ontology-Guided Knowledge Graph Construction from Structured Metadata and Climate Science Publications](https://arxiv.org/abs/2610.32725)**
  - *Aayush Acharya, Qi Zhang, Eduard Dragut et al.*
  - 🤗 · `2026-10-23`
  - The rapid expansion of scientific literature far outpaces the speed of manual curation, creating a fundamental bottleneck in extracting structured knowledge from scientific texts. To address this, we introduce an agentic, ontology-guided framework for knowledge graph (KG) constru…

- **[Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge](https://arxiv.org/abs/2610.32415)**
  - *Xiaopeng Ke, Zhixin Wang, Xuebo Liu et al.*
  - 🤗 · `2026-10-23`
  - LLM-based annotation has advanced rapidly, yet existing benchmarks remain misaligned with real-world practice. Actual annotation often involves lengthy, task-specific guidelines, and different annotators may produce divergent but reasonable judgments, especially on boundary cases…

- **[Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](https://arxiv.org/abs/2610.32285)**
  - *Zhiyong Cao, Hengjie Zhu, Yongxin Wang et al.*
  - 🤗 · `2026-10-23`
  - LLM agents are increasingly used to solve real-world problems, and their effectiveness depends on both the underlying models and the harnesses that support their operation. However, most existing benchmarks focus on model capabilities and overall agent performance, with limited a…

- **[What Open-Source Projects Tell Their Coding Agents: A Census of AGENTS.md and CLAUDE.md](https://arxiv.org/abs/2610.31715)**
  - *Pawel Zarzycki*
  - 🤗 · `2026-10-22`

- **[BrickWright: Agentic Creation of Physically Feasible Brick Builds](https://arxiv.org/abs/2610.31651)**
  - *Ava Pun, Kevin Dai, Sally Chen et al.*
  - 🤗 · `2026-10-22`

- **[AgentVQA: A Unified Benchmark for Agentic Visual Understanding](https://arxiv.org/abs/2610.31494)**
  - *Advait Gupta, Sachin Konan, Tom Yin et al.*
  - 🤗 · `2026-10-22`

- **[Do "True" and "False" Add Up to One? Complement Consistency in LLM-Agent Opinion Simulations](https://arxiv.org/abs/2610.32874v1)**
  - *Anouar Imel, Jin Qi*
  - `2026-10-23`
  - In LLM-agent opinion simulations, each agent reports the probability that a claim is true after seeing its own previous probability and the probabilities reported by its neighbors, and that number becomes its state in the next round. If the number describes the agent's position r…

- **[Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery](https://arxiv.org/abs/2610.32866v1)**
  - *Marek Masiak, Andrzej Szablewski, Nicola Cancedda et al.*
  - `2026-10-23`
  - Fine-tuning on datasets of unknown origin can create a backdoor in the trained model when the data includes poisoned examples. Difficult to localise and remove, backdoors can persist through safety training. While parameter-efficient fine-tuning methods capture the full parameter…

- **[Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves](https://arxiv.org/abs/2610.32851v1)**
  - *Garima Agrawal, Prasun Das, Akshay Sarvade et al.*
  - `2026-10-23`
  - Enterprises are deploying agentic AI across the software development lifecycle, and they need the behavioral logic of the systems they act on, not stakeholder documentation. A seven-agent reverse-engineering pipeline recovered this logic, processing 241 repositories across 18 ser…

- **[HarnessMM: Recursive Self-Improvement for Harness Token Efficiency](https://arxiv.org/abs/2610.32813v1)**
  - *Yuhua Jiang, Chang Xu, Feifei Gao et al.*
  - `2026-10-23`
  - Agent harnesses repeatedly invoke reasoning after tool feedback, even when an earlier call has already fixed the next action. We introduce HarnessMM (Harness Minus Minus), a method for improving harness token efficiency through guarded decision reuse and recursive self-improvemen…

- **[Every Edge Needs a Quote: Building a Quote-Grounded Knowledge Graph of Healthcare Software Adoption with Language-Model Agents](https://arxiv.org/abs/2610.32781v1)**
  - *Juan Felipe Duran, Arthur Tobler, Martin Vallières*
  - `2026-10-23`
  - Hospitals regularly buy software that clinicians and patients depend on. Because these purchases are costly, hard to reverse and can affect patient care, buyers look for evidence of which peer institutions already use a product and which systems it connects to. This evidence is p…

- **[Semantic Representation for Agentic Self-Play in Automated Laboratories](https://arxiv.org/abs/2610.32755v1)**
  - *Yves Delley, John Coller, Zachary Cutts et al.*
  - `2026-10-23`
  - Navigating complex, high-dimensional biological search spaces necessitates scalable physical and computational intelligence to explore beyond local optima through iterative self-play across ideation, experimentation, and automation. Translating experimental designs into reliable…

- **[ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents](https://arxiv.org/abs/2610.32752v1)**
  - *Navyansh Mahla, Sashank Vandrangi*
  - `2026-10-23`
  - LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages…

- **[Agentic Hazard Mapper: Emulating Expert Map-Making with AI Agents for Risk Communication](https://arxiv.org/abs/2610.32738v1)**
  - *Sidi Wu, Lifeng Lin, Yizi Chen et al.*
  - `2026-10-23`
  - Hazard maps are essential tools for public risk communication, preparedness, and evacuation planning, yet effective cartographic design is not always ensured due to limited access to cartographic expertise across local governments and communities. We present Agentic Hazard Mapper…

- **[Can AI Agents Help Robotic Engineers? Lessons from Two Focus Days in Industry](https://arxiv.org/abs/2610.32636v1)**
  - *Salim Fares, Steffen Herbold*
  - `2026-10-23`
  - Software developers increasingly use AI agents that execute multi-step programming tasks on their own. However, it is unclear if and how this transfers to robotic engineering, where engineers program industrial robots in niche, vendor-specific languages and rely on visual feedbac…

- **[What Transfers Across Protein Pockets? Experience Reuse in Molecular Optimization for Agentic Structure-Based Drug Design](https://arxiv.org/abs/2610.32620v1)**
  - *Zaifei Yang, Weiyu Chen, Yaqing Wang et al.*
  - `2026-10-23`
  - LLM agents optimize a ligand in a protein pocket by editing it step by step and docking each edit. Recent agents first spend extra dockings probing the complex with controlled edits; guidance induced from these probes is reported to help more than the chemical knowledge the model…

- **[Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance](https://arxiv.org/abs/2610.32555v1)**
  - *Antonio Ken Iannillo, Joshua Segun Owotogbe, Roberto Natella et al.*
  - `2026-10-23`
  - LLM agents increasingly rely on external tools exposed via the Model Context Protocol (MCP), yet current benchmarks assume tools respond correctly and on time, leaving agent resilience to realistic tool failures untested. We introduce MCP-Injector, a drop-in, protocol-aware fault…

- **[IGG: A Benchmark for Interactive GUI Grounding under Visibility Constraints](https://arxiv.org/abs/2610.32536v1)**
  - *Kyeongseon Kim, Jiyeon Son, Tae-Hyun Oh*
  - `2026-10-23`
  - GUI grounding benchmarks ask whether an agent can localize a target that is already visible in a static screenshot. Real interfaces often violate this assumption: a target may be off-screen, appear only after a state change or hover, remain occluded, or become actionable after a…

- **[When Agents Fail: Model or Harness--Who's to Blame?](https://arxiv.org/abs/2610.32483v1)**
  - *Shao Zhang, Hangfan Zhang, Yuanyuan Shi et al.*
  - `2026-10-23`
  - LLM agents combine models with execution harnesses, so agentic benchmark performance reflects their joint behavior. We argue that harnesses should therefore be evaluated through their interactions with underlying models. We develop a framework combining five complementary measure…

- **[CASE: Confusion-Aware Skill Evolution for Frozen Multimodal Emotion Models](https://arxiv.org/abs/2610.32481v1)**
  - *Siyu Wu, Zeyu Liang, Linghao Wang et al.*
  - `2026-10-23`
  - Multimodal large language models (MLLMs) have substantially advanced Multimodal Emotion Recognition (MER) by enabling fine-grained emotion understanding through reasoning over multimodal evidence. However, they still exhibit systematic confusion between semantically adjacent emot…

- **[CauProphet: Teaching Agents to Develop Causal Cognition like Humans](https://arxiv.org/abs/2610.32477v1)**
  - *Kaiwen Wu, Chaochao Lu*
  - `2026-10-23`
  - Large language model (LLM) agents increasingly support long-horizon tasks by leveraging external memory and past experience. However, existing agents mainly retrieve records or summaries, lacking the ability to form and refine causal understanding of the world. Inspired by human…

- **[Beyond Copying: Lifelong Smart Contract Security Task Construction via Protocol Mutation](https://arxiv.org/abs/2610.32453v1)**
  - *Zifan Peng, Peng Huang, Jingyi Zheng et al.*
  - `2026-10-23`
  - AI agents can inspect code and run tests to support smart contract security. SlowMist reports about $38.6 billion in losses across the broader blockchain ecosystem. Existing evaluations can reward memorized or copied answers, including attack code recovered from public blockchain…

- **[POSEIDON: Scaling Training Environments for Scientific Agents from Code Repositories](https://arxiv.org/abs/2610.32448v1)**
  - *Qifan Zhang, Yuhan Li, Nuo Chen et al.*
  - `2026-10-23`
  - Training environments remain a major bottleneck for agents in data-driven scientific discovery. Existing collections of executable and verifiable training environments are small, and their construction remains difficult to scale. To address this limitation, we introduce Poseidon,…

- **[Decoupling Patient Personas and Clinical Workflows: A Dual-Agent Approach to Realistic Medical Dialogue Generation](https://arxiv.org/abs/2610.32443v1)**
  - *Qiyuan Li, Xiaomei Guo, Chao Gao et al.*
  - `2026-10-23`
  - Pre-consultation medical dialogues are essential for collecting comprehensive patient information, but are costly to obtain at scale due to privacy and ethical constraints. Existing LLM-based synthesis methods often rely on prompt engineering or rigid rules, limiting their abilit…

- **[Async-RBench: Benchmarking Asynchronous Task Execution in LLM Agents](https://arxiv.org/abs/2610.32429v1)**
  - *Detao Zeng, Guilin Ou, Nuo Chen et al.*
  - `2026-10-23`
  - Large language model (LLM) agents increasingly execute tasks asynchronously: a main agent continues working while its subagents run, and the task state may change before their results arrive. The main agent must decide which work to update or preserve and which checks to repeat,…

- **[LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents](https://arxiv.org/abs/2610.32412v1)**
  - *Shen Liu, Ze Zhou, Zhenguo Xu et al.*
  - `2026-10-23`
  - Recursive large language model (LLM) agents solve long-horizon tasks through decomposition, execution, and environmental feedback. Yet after producing an atomic subtask, they often invoke the same large model again to translate a familiar instruction into an executable action. We…

- **[DealsFlow: An Evidence-Gated Agentic Harness for Venture Capital Deal Triage](https://arxiv.org/abs/2610.32380v1)**
  - *Ming Ze Tang, David Cutting, Boyd Carson et al.*
  - `2026-10-23`
  - Large language models (LLMs) can read startup pitch decks, but letting them emit investment scores directly invites score inflation, run-to-run variance and rationales that are hard to audit. We describe DealsFlow, a human-in-the-loop agentic harness deployed at a UK early-stage…

- **[Adaptive Control of Scientific Instruments with Nonstationary Responses through Multimodal Agents](https://arxiv.org/abs/2610.32370v1)**
  - *Guoyang Shi, Hongwen Li, Yiding Yu et al.*
  - `2026-10-23`
  - Controlling scientific instruments requires parameters to be adjusted progressively in response to feedback from successive operations. When unobserved operating conditions evolve with operational history, responses become nonstationary, and a static mapping from actions to respo…

- **[4DMemory: Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented Agents](https://arxiv.org/abs/2610.32332v1)**
  - *Yanhao Jia, Yi Zhu, Yiran Zhong et al.*
  - `2026-10-23`
  - Humans efficiently process multimodal streams spanning hours to years, building persistent, fine-grained spatiotemporal memories that support reasoning about and predicting long-horizon events. In contrast, existing benchmarks focus on short- and medium-context tasks, and most fo…

- **[TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent](https://arxiv.org/abs/2610.32326v1)**
  - *Junlin He, Junzhang Zhu, Yudong Li et al.*
  - `2026-10-23`
  - Large Language Model (LLM) agents have enabled automated code evolution for algorithm discovery. However, current recursive self-improvement (RSI) research for sequential recommendation faces a dilemma: general-purpose frameworks lack domain-specific feedback, while recommender-s…

- **[Beyond Gain: Measuring Skill Internalization for Agent Skill Retirement](https://arxiv.org/abs/2610.32322v1)**
  - *Yanze Wang, Pengfei Yao, Tianyi Sun et al.*
  - `2026-10-23`
  - LLM agents retrieve skills from public hubs that hold up to about 100,000 entries and serve many models. As models improve, a hub must find the skills a given model has internalized, meaning it can do without them, and retire them for that model, yet internalization has not been…

- **[DMAIC-Bench: From Self-Reflection to Self-Restraint for Agents in Multi-Stage Analytical Tasks](https://arxiv.org/abs/2610.32305v1)**
  - *Shan Peng, Shuaiqi Cheng, Miao Peng et al.*
  - `2026-10-23`
  - Multi-stage analytical tasks require LLM agents to use intermediate evidence to decide whether to continue, redirect or stop. Self-reflection, in which an agent critiques its output, is widely studied, yet a critique does not show whether evidence changed the next action. We call…

- **[Lifelong Context Adaptation through Bidirectional Memory-Skill Learning](https://arxiv.org/abs/2610.32295v1)**
  - *Tianyi Xu, Huazheng Wang*
  - `2026-10-23`
  - Lifelong LLM agents must learn from an expanding history of interactions while making each decision within a bounded context window. Memory makes past experience available, but the agent may still need to infer how to solve each new task from the retrieved records. Skills provide…

- **[MedCaseAgent: From Multimodal Clinical Evidence to Rare Disease Case Reports](https://arxiv.org/abs/2610.32258v1)**
  - *Hongkang Chu, Yifan Shen, Tianjiao Yu et al.*
  - `2026-10-23`
  - Although Large Language Models (LLMs) have demonstrated potential in clinical documentation, generating the rigorous, evidence-based reasoning required for unprecedented, atypical, and rare disease case reports remains a significant challenge. We present MedCaseAgent, an end-to-e…

- **[Minimum Description Length Unsupervisedly Separates Law-Grade from Statistical-Grade Knowledge in a Self-Improving Science Agent - and Reveals 86% of Its Own Discoveries Are Statistical](https://arxiv.org/abs/2610.32245v1)**
  - *Wenbin Mao, Pei Zou*
  - `2026-10-23`
  - AI systems that discover scientific relations now generate candidate "laws" at scale, but the bottleneck has shifted from generation to vetting: which candidates deserve belief? We show that a deployed self-improving science agent - one that has admitted 252 relations through hel…

- **[Financial Context-Rich Strategy for Actor-Critic based Agents: A Deep Reinforcement Learning Approach for Stock Trading](https://arxiv.org/abs/2610.32237v1)**
  - *Hrishikesh Singh, Aarti Sharma, Millie Pant*
  - `2026-10-23`
  - In modern financial markets, more than 3/4th of the large volume trade is executed by algorithmic trading based on advanced trading strategies to attain higher precision and speed than traditional human traders. The conventional strategies focused on price-based indicators are in…

- **[Correct Answers, Closed Gates: SolveBind for GUI Agents at the Verification Barrier](https://arxiv.org/abs/2610.32223v1)**
  - *Xinhao Song, Haoxuan Peng, Su Su et al.*
  - `2026-10-23`
  - Websites and applications deploy CAPTCHAs and anti-automation mechanisms that use behavioral signals such as interaction trajectories and timing, not outcomes alone, to distinguish humans from automated agents. We call these protected GUI environments, where correctly solving a v…

- **[SWE-Shift: Evaluating Coding Agents in Evolving Workspaces](https://arxiv.org/abs/2610.32196v1)**
  - *Victor Shea-Jay Huang, Rongqing Li, Zhangyue Yin et al.*
  - `2026-10-23`
  - Repository-level coding benchmarks largely assume that tasks and environments remain unchanged throughout execution. In software development, code, dependencies, runtime state, and requirements can change while an agent is still working. We introduce SWE-Shift, a benchmark for ev…

- **[The LLENS Platform for On-Premises Large Language Model Agents in a Japanese University Hospital: Development and Evaluation Study](https://arxiv.org/abs/2610.32151v1)**
  - *Ken Enda, Jien Saito, Masami Mukai et al.*
  - `2026-10-23`
  - Large language model agents that use tools could take on part of the electronic health record and desk work that occupies physicians' time, but in many hospitals the medical information systems run inside closed networks, so the model and the agent harness must also sit inside. W…

- **[ImageRSI: Verification-Driven Recursive Self-Improvement for Agentic Image Generation](https://arxiv.org/abs/2610.32120v1)**
  - *Shuo Han, Zhilin Wang, Peng Ling et al.*
  - `2026-10-23`
  - Complex text-to-image requests remain difficult to satisfy reliably. Verifying and repairing an image can fix an individual output, but a successful repair does not necessarily carry over to other requests. We present ImageRSI, a framework that keeps the image generator frozen an…

- **[Who Verifies the Tools? How Warped Formatters Mislead Agents and Their Verifiers](https://arxiv.org/abs/2610.32110v1)**
  - *William Jeffries*
  - `2026-10-23`
  - Agents and verifiers often rely on the text a tool prints, and that text can misrepresent what the tool actually did, even when the tool's computation is correct. We saw this happen in a production RAG research system used by the Pilsudski Institute in New York, where tool output…

- **[PersonaScienceBench: Evaluating Scientific Agents with Diverse Simulated Researchers](https://arxiv.org/abs/2610.32106v1)**
  - *Siyang Wu, Weizhi Zhang, Chen Yang et al.*
  - `2026-10-23`
  - Scientific agents collaborate with researchers whose expertise and preferences differ, but benchmarks usually hold the collaborator fixed. We introduce PersonaScienceBench: 200 tasks from five benchmarks across four scientific domains. Simulated researchers provide context and fe…

- **[AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents](https://arxiv.org/abs/2610.32092v1)**
  - *Gejian Zhao, Hanzhou Wu, Xinpeng Zhang*
  - `2026-10-23`
  - Verifying the provenance of autonomous LLM agents is a critical security challenge. Existing semantic attribution is easily obfuscated by system prompts, while active watermarking conflicts with schema-constrained tool generation. We propose AgentTrace, an active framework that i…

- **[Behaviour analysis for large language model-driven agents](https://arxiv.org/abs/2610.32087v1)**
  - *Tianqiang Yan, Lizhen Qu*
  - `2026-10-23`
  - Understanding language-agent behaviour requires learning how actions are organised across a trajectory and how this organisation relates to context and outcomes. We propose a general framework that connects data-driven behavioural discovery with analysis and experimental investig…

- **[DriveMind: Mind-Evolving Belief Tracking for Closed-Loop Autonomous Driving](https://arxiv.org/abs/2610.32069v1)**
  - *Yan Shi, Kehua Chen, Jiarui Qi et al.*
  - `2026-10-23`
  - Recent multimodal large language models (MLLMs) can perceive a traffic scene, reason about it, and propose a driving action within a single model. However, existing MLLM-based drivers reason from scratch at each frame and commit to a single explanation, discarding earlier hypothe…

- **[Understanding Communication Failures in Multi-Agent LLM Systems](https://arxiv.org/abs/2610.32060v1)**
  - *Priya Pitre, Jun Hou, Yi Fang et al.*
  - `2026-10-23`
  - Multi-agent LLM systems aim to improve reasoning through debate, evidence sharing, and mutual correction, but interaction can also introduce failures that final accuracy alone cannot explain. Agents may converge too early, ignore dissent, suppress correct minority answers, or pre…

- **[Do AI-for-Science Agents Preserve Model Safety?](https://arxiv.org/abs/2610.32045v1)**
  - *Michael Yew Chuan Lee, Manya Sriram, N. Benjamin Erichson*
  - `2026-10-23`
  - AI-for-Science agents are increasingly being used for formulating scientific hypotheses, running autonomous experiments, and interpreting evidence. These agents are constructed by integrating a large language model (LLM) into a domain-specific agent harness, which in turn can imp…

- **[RSI-Opt: Recursive Self-Improvement Optimizer Agents For Model Training](https://arxiv.org/abs/2610.32026v1)**
  - *Binghang Lu, Yige Sun, Guang Lin*
  - `2026-10-23`
  - Conventional neural-network training typically follows a predefined optimization recipe, motivating a LLM agent that monitors training dynamics and adjusts optimizer settings as training progresses, but a fixed agent policy does not accumulate experience across runs. We introduce…

- **[BARC-Bench: Benign Asks, Risky Consequences](https://arxiv.org/abs/2610.32024v1)**
  - *Kangkang Li, Kelvin Luu, Lily Ma et al.*
  - `2026-10-23`
  - Task instructions from users for agents are inherently underspecified, especially regarding safety boundaries--creating behavioral risks. To study these risks, we introduce BARC-Bench, a collection of 110 tasks across nine simulated workspace environments where benign requests le…

- **[CEMIR vs. FISER: a comparative study of reasoning-based and enrichment-based approaches to pragmatic intent recognition](https://arxiv.org/abs/2610.32022v1)**
  - *Ziya Hosseynzadeh, Farjad Fallah, Farnoosh Fallah et al.*
  - `2026-10-23`
  - Intent recognition in human-robot interaction requires agents to resolve ambiguous natural language instructions by inferring the speaker's underlying goals. Research has increasingly focused on two notable paradigms for addressing this task: structured symbolic reasoning and mul…

- **[Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox](https://arxiv.org/abs/2610.32955v1)**
  - *Federico Lucca*
  - `2026-10-23`
  - Personal email agents decide, for every message, what it is, whether it is urgent, whether to draft a reply, create a task, or ignore it. Their error rate is rarely measured: the stored labels were written by the system itself. We present Foyer, a self-hosted personal inbox agent…

- **[J-Comm: Jacobian-Guided Latent Communication between LLM Agents](https://arxiv.org/abs/2610.32871v1)**
  - *Xiangwei Wang, Wei Wang, Sachith Seneviratne et al.*
  - `2026-10-23`
  - Latent communication requires both an effective continuous reasoning process and an interface through which an external model can leverage its intermediate computation. We present J-Comm, a framework comprising two core components. First, a training-free Geometric Agreement for L…

- **[Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents to Go Beyond](https://arxiv.org/abs/2610.32802v1)**
  - *Zheng Jiang, Yiming Chen, Houde Qian et al.*
  - `2026-10-23`
  - On-policy distillation aligns teacher feedback with a student's current behavior, yet acquiring useful supervision for multi-turn agents requires identifying both where guidance is needed and whether the student can sustain the interaction afterward. We introduce Frontier-OPD, wh…

- **[The Butterfly Defects: Tracing Cooperation in LLM Agent Networks](https://arxiv.org/abs/2610.32726v1)**
  - *Maria Sampani, Maria Lymperaiou, Angeliki Dimitriou et al.*
  - `2026-10-23`
  - As large language models (LLMs) increasingly operate as interconnected agents, a fundamental question emerges: does individual cooperation translate into collective cooperation? We investigate this question through the Iterated Prisoner's Dilemma (IPD), moving from dyadic interac…

- **[PHYRD: A Living Benchmark for Reproducing and Extending Theoretical Physics Research](https://arxiv.org/abs/2610.32575v1)**
  - *Qituan Zhang, Guo Chen, Linfeng Zhang et al.*
  - `2026-10-23`
  - Large language models and agents have shown significant power in advanced physical research. In this paper, We introduce PHYRD, a living benchmark for theoretical-physics reasoning with 63 Reproduce and 43 Discover problems. Reproduce tests derivation of published results; Discov…

- **[SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks](https://arxiv.org/abs/2610.32441v1)**
  - *Tianyun Zhong, Wei Wang, Jialin Li et al.*
  - `2026-10-23`
  - Large language model (LLM) agents are increasingly capable of supporting scientific workflows, but their capabilities across diverse research activities remain difficult to assess systematically. Existing benchmarks often focus on selected scientific capabilities or task types, l…

- **[Profile-Driven User Simulation via Reinforcement Learning with Hierarchical Rewards for Task-Oriented Dialogues](https://arxiv.org/abs/2610.32435v1)**
  - *Juan Li, Fangshu Chang, Xinyi Jiang et al.*
  - `2026-10-23`
  - Building Task-Oriented Dialogue (TOD) systems for high-value scenarios such as financial marketing requires large volumes of domain-specific dialogue data, which privacy regulations, annotation costs, and the need for expert labor make hard to obtain. User simulation offers a rem…

- **[Beyond Final Outcomes: Quantifying Claim-Level Information Dynamics in Multi-Agent LLM Interaction](https://arxiv.org/abs/2610.32333v1)**
  - *Haocheng Jiang, Herun Wan, Yongyuan Peng et al.*
  - `2026-10-23`
  - When LLM-powered agents interact, information is repeatedly shared, expanded, and forgotten, yet multi-agent evaluation typically focuses on final task outcomes. We study such interaction as claim-level information dynamics and propose RIVER, which decomposes agent outputs into a…

- **[Beyond What to Say: Proactive Utterance Timing with Inner Thoughts for Werewolf Agents](https://arxiv.org/abs/2610.32107v1)**
  - *Yoshiki Tanaka, Shuya Uchiyama, Daichi Hamaguchi et al.*
  - `2026-10-23`
  - Participating in a conversation involves not only deciding what to say but also whether to speak at all. This judgment carries even greater significance in environments like the Werewolf game, where participants' interests conflict, because both utterances and silence are subject…

- **[CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments](https://arxiv.org/abs/2610.32004v1)**
  - *Monojit Banerjee, Zhujun Lan, Defu Cao*
  - `2026-10-23`
  - Deploying language agents in real applications demands more than the right answer: an agent must execute a multi-step business process correctly, follow domain-specific rules, and interact with a user across a dialogue, where the gap between saying and doing is the gap between a…

- **[Agent-Based Transport Model Calibration via Online Stochastic Batch Optimization](https://arxiv.org/abs/2610.32698v1)**
  - *Abdelkader Dib, Milos Balac*
  - `2026-10-23`
  - Calibrating agent-based models (ABMs) is computationally demanding, as traditional black-box optimization typically requires hundreds or thousands of independent simulation runs. To reduce this burden, we introduce an online calibration framework that estimates parameters within…

- **[HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching](https://arxiv.org/abs/2610.32554v1)**
  - *I-tak Ieong, Hao Tang*
  - `2026-10-23`
  - Zero-shot object navigation requires an embodied agent to choose where to search while retaining evidence from previous observations. HGWM couples an LLM-generated room-anchor prior with persistent spatial-semantic memory. A coarse stage assigns visual-semantic scores to candidat…

- **[PULSES: multi-agent AI for autonomous excited-state model building and dynamics](https://arxiv.org/abs/2610.32392v1)**
  - *Fangning Ren, Lechen Dong, Xu Chen et al.*
  - `2026-10-23`
  - Simulating molecular excited-state processes requires resolving electronic and nuclear dynamics, but the cost of direct quantum-chemical calculations limits accessible system sizes and timescales. Machine-learning models can extend these simulations, yet they often need to be tai…

- **[Markets of Minds: A 51-Billion-State Economy of Intelligence](https://arxiv.org/abs/2610.32190v1)**
  - *Jusheng Zhang, Xuekun Wu, Wenhao Wang et al.*
  - `2026-10-23`
  - When intelligence is shared, reasoning becomes a constrained allocation problem. In a population of agents with limited access to expert models, an intervention can benefit its recipient yet still be a poor use of shared capacity if another feasible intervention has greater expec…

- **[DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection](https://arxiv.org/abs/2610.32969v1)**
  - *Amber Xie, Jiawei Fu, Xiaofeng Guo et al.*
  - `2026-10-23`
  - Collecting high-quality demonstrations remains a central bottleneck for learning dexterous manipulation. Teleoperation records executable robot actions, but it requires a complete robot setup and places the burden of coordinating many finger joints on the operator. Human demonstr…


## Harness  (72)

### NeurIPS

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **NeurIPS 2025** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…

- **[STRATUS: A Multi-agent System for Autonomous Reliability Engineering of Modern Clouds](https://arxiv.org/abs/2506.02009)**
  - *Yinfang Chen, Jia-Qi Pan, J. Clark et al.*
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

- **[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://arxiv.org/abs/2504.08725)**
  - *Dayu Yang, Antoine Simoulin, Xin Qian et al.*
  - **ACL 2025** · `2025-04-11`
  - High-quality code documentation is crucial for software development especially in the era of AI. However, generating it automatically using Large Language Models (LLMs) remains challenging, as existing approaches often produce incomplete, unhelpful, or factually incorrect outputs…


### Other / arXiv

- **[HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games](https://arxiv.org/abs/2610.31162)**
  - *Zecong Tang, Zian Guan, Yuncheng Guo et al.*
  - 🤗 Featured · `2026-10-22`

- **[Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](https://arxiv.org/abs/2610.32285)**
  - *Zhiyong Cao, Hengjie Zhu, Yongxin Wang et al.*
  - 🤗 · `2026-10-23`
  - LLM agents are increasingly used to solve real-world problems, and their effectiveness depends on both the underlying models and the harnesses that support their operation. However, most existing benchmarks focus on model capabilities and overall agent performance, with limited a…

- **[HarnessMM: Recursive Self-Improvement for Harness Token Efficiency](https://arxiv.org/abs/2610.32813v1)**
  - *Yuhua Jiang, Chang Xu, Feifei Gao et al.*
  - `2026-10-23`
  - Agent harnesses repeatedly invoke reasoning after tool feedback, even when an earlier call has already fixed the next action. We introduce HarnessMM (Harness Minus Minus), a method for improving harness token efficiency through guarded decision reuse and recursive self-improvemen…

- **[When Agents Fail: Model or Harness--Who's to Blame?](https://arxiv.org/abs/2610.32483v1)**
  - *Shao Zhang, Hangfan Zhang, Yuanyuan Shi et al.*
  - `2026-10-23`
  - LLM agents combine models with execution harnesses, so agentic benchmark performance reflects their joint behavior. We argue that harnesses should therefore be evaluated through their interactions with underlying models. We develop a framework combining five complementary measure…

- **[DealsFlow: An Evidence-Gated Agentic Harness for Venture Capital Deal Triage](https://arxiv.org/abs/2610.32380v1)**
  - *Ming Ze Tang, David Cutting, Boyd Carson et al.*
  - `2026-10-23`
  - Large language models (LLMs) can read startup pitch decks, but letting them emit investment scores directly invites score inflation, run-to-run variance and rationales that are hard to audit. We describe DealsFlow, a human-in-the-loop agentic harness deployed at a UK early-stage…

- **[4DMemory: Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented Agents](https://arxiv.org/abs/2610.32332v1)**
  - *Yanhao Jia, Yi Zhu, Yiran Zhong et al.*
  - `2026-10-23`
  - Humans efficiently process multimodal streams spanning hours to years, building persistent, fine-grained spatiotemporal memories that support reasoning about and predicting long-horizon events. In contrast, existing benchmarks focus on short- and medium-context tasks, and most fo…

- **[MedCaseAgent: From Multimodal Clinical Evidence to Rare Disease Case Reports](https://arxiv.org/abs/2610.32258v1)**
  - *Hongkang Chu, Yifan Shen, Tianjiao Yu et al.*
  - `2026-10-23`
  - Although Large Language Models (LLMs) have demonstrated potential in clinical documentation, generating the rigorous, evidence-based reasoning required for unprecedented, atypical, and rare disease case reports remains a significant challenge. We present MedCaseAgent, an end-to-e…

- **[The LLENS Platform for On-Premises Large Language Model Agents in a Japanese University Hospital: Development and Evaluation Study](https://arxiv.org/abs/2610.32151v1)**
  - *Ken Enda, Jien Saito, Masami Mukai et al.*
  - `2026-10-23`
  - Large language model agents that use tools could take on part of the electronic health record and desk work that occupies physicians' time, but in many hospitals the medical information systems run inside closed networks, so the model and the agent harness must also sit inside. W…

- **[Do AI-for-Science Agents Preserve Model Safety?](https://arxiv.org/abs/2610.32045v1)**
  - *Michael Yew Chuan Lee, Manya Sriram, N. Benjamin Erichson*
  - `2026-10-23`
  - AI-for-Science agents are increasingly being used for formulating scientific hypotheses, running autonomous experiments, and interpreting evidence. These agents are constructed by integrating a large language model (LLM) into a domain-specific agent harness, which in turn can imp…

- **[ZENO: Nonlinear filtering with Zakai Equation Neural Operators](https://arxiv.org/abs/2610.32926v1)**
  - *Aaditya Prasad, Steven W. Flavell, Brian DePasquale*
  - `2026-10-23`
  - State inference and parameter learning for nonlinear filters is a core computation for scientific machine learning with varied applications in engineering and neuroscience. The unnormalized filtering distribution is governed by the Zakai equation, a stochastic partial differentia…


## Finance  (124)

### AAAI

- **[LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042)**
  - *Cheng Yang, Hui Jin, Xinlei Yu et al.*
  - **AAAI 2025** · `2025-11-26`
  - Diagnosing lung cancer typically involves physicians identifying lung nodules in Computed tomography (CT) scans and generating diagnostic reports based on their morphological features and medical expertise. Although advancements have been made in using multimodal large language m…


### NeurIPS

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **NeurIPS 2025** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…

- **[AutoData: A Multi-Agent System for Open Web Data Collection](https://arxiv.org/abs/2505.15859)**
  - *Tian-Yi Ma, Yi-Yue Qian, Zhe-Yuan Zhang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - The exponential growth of data-driven systems and AI technologies has intensified the demand for high-quality web-sourced datasets. While existing datasets have proven valuable, conventional web data collection approaches face significant limitations in terms of human effort and…


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


### EMNLP

- **[QuantAgents: Towards Multi-agent Financial System via Simulated Trading](https://arxiv.org/abs/2510.04643)**
  - *Xiang-Yu Li, Ya-Wen Zeng, Xiao-Fen Xing et al.*
  - **EMNLP 2025** · `2025-10-06`
  - In this paper, our objective is to develop a multi-agent financial system that incorporates simulated trading, a technique extensively utilized by financial professionals. While current LLM-based agent models demonstrate competitive performance, they still exhibit significant dev…

- **[AMAS: Adaptively Determining Communication Topology for LLM-based Multi-Agent System](https://arxiv.org/abs/2510.01617)**
  - *Hui Yi Leong, Yuheng Li, Yu-Qing Wu et al.*
  - **EMNLP 2025** · `2025-10-02`
  - Although large language models (LLMs) have revolutionized natural language processing capabilities, their practical implementation as autonomous multi-agent systems (MAS) for industrial problem-solving encounters persistent barriers. Conventional MAS architectures are fundamental…


### Other / arXiv

- **[Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves](https://arxiv.org/abs/2610.32851v1)**
  - *Garima Agrawal, Prasun Das, Akshay Sarvade et al.*
  - `2026-10-23`
  - Enterprises are deploying agentic AI across the software development lifecycle, and they need the behavioral logic of the systems they act on, not stakeholder documentation. A seven-agent reverse-engineering pipeline recovered this logic, processing 241 repositories across 18 ser…

- **[CauProphet: Teaching Agents to Develop Causal Cognition like Humans](https://arxiv.org/abs/2610.32477v1)**
  - *Kaiwen Wu, Chaochao Lu*
  - `2026-10-23`
  - Large language model (LLM) agents increasingly support long-horizon tasks by leveraging external memory and past experience. However, existing agents mainly retrieve records or summaries, lacking the ability to form and refine causal understanding of the world. Inspired by human…

- **[Beyond Copying: Lifelong Smart Contract Security Task Construction via Protocol Mutation](https://arxiv.org/abs/2610.32453v1)**
  - *Zifan Peng, Peng Huang, Jingyi Zheng et al.*
  - `2026-10-23`
  - AI agents can inspect code and run tests to support smart contract security. SlowMist reports about $38.6 billion in losses across the broader blockchain ecosystem. Existing evaluations can reward memorized or copied answers, including attack code recovered from public blockchain…

- **[Async-RBench: Benchmarking Asynchronous Task Execution in LLM Agents](https://arxiv.org/abs/2610.32429v1)**
  - *Detao Zeng, Guilin Ou, Nuo Chen et al.*
  - `2026-10-23`
  - Large language model (LLM) agents increasingly execute tasks asynchronously: a main agent continues working while its subagents run, and the task state may change before their results arrive. The main agent must decide which work to update or preserve and which checks to repeat,…

- **[DealsFlow: An Evidence-Gated Agentic Harness for Venture Capital Deal Triage](https://arxiv.org/abs/2610.32380v1)**
  - *Ming Ze Tang, David Cutting, Boyd Carson et al.*
  - `2026-10-23`
  - Large language models (LLMs) can read startup pitch decks, but letting them emit investment scores directly invites score inflation, run-to-run variance and rationales that are hard to audit. We describe DealsFlow, a human-in-the-loop agentic harness deployed at a UK early-stage…

- **[Financial Context-Rich Strategy for Actor-Critic based Agents: A Deep Reinforcement Learning Approach for Stock Trading](https://arxiv.org/abs/2610.32237v1)**
  - *Hrishikesh Singh, Aarti Sharma, Millie Pant*
  - `2026-10-23`
  - In modern financial markets, more than 3/4th of the large volume trade is executed by algorithmic trading based on advanced trading strategies to attain higher precision and speed than traditional human traders. The conventional strategies focused on price-based indicators are in…

- **[Behaviour analysis for large language model-driven agents](https://arxiv.org/abs/2610.32087v1)**
  - *Tianqiang Yan, Lizhen Qu*
  - `2026-10-23`
  - Understanding language-agent behaviour requires learning how actions are organised across a trajectory and how this organisation relates to context and outcomes. We propose a general framework that connects data-driven behavioural discovery with analysis and experimental investig…

- **[Understanding Communication Failures in Multi-Agent LLM Systems](https://arxiv.org/abs/2610.32060v1)**
  - *Priya Pitre, Jun Hou, Yi Fang et al.*
  - `2026-10-23`
  - Multi-agent LLM systems aim to improve reasoning through debate, evidence sharing, and mutual correction, but interaction can also introduce failures that final accuracy alone cannot explain. Agents may converge too early, ignore dissent, suppress correct minority answers, or pre…

- **[RSI-Opt: Recursive Self-Improvement Optimizer Agents For Model Training](https://arxiv.org/abs/2610.32026v1)**
  - *Binghang Lu, Yige Sun, Guang Lin*
  - `2026-10-23`
  - Conventional neural-network training typically follows a predefined optimization recipe, motivating a LLM agent that monitors training dynamics and adjusts optimizer settings as training progresses, but a fixed agent policy does not accumulate experience across runs. We introduce…

- **[SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks](https://arxiv.org/abs/2610.32441v1)**
  - *Tianyun Zhong, Wei Wang, Jialin Li et al.*
  - `2026-10-23`
  - Large language model (LLM) agents are increasingly capable of supporting scientific workflows, but their capabilities across diverse research activities remain difficult to assess systematically. Existing benchmarks often focus on selected scientific capabilities or task types, l…

- **[Profile-Driven User Simulation via Reinforcement Learning with Hierarchical Rewards for Task-Oriented Dialogues](https://arxiv.org/abs/2610.32435v1)**
  - *Juan Li, Fangshu Chang, Xinyi Jiang et al.*
  - `2026-10-23`
  - Building Task-Oriented Dialogue (TOD) systems for high-value scenarios such as financial marketing requires large volumes of domain-specific dialogue data, which privacy regulations, annotation costs, and the need for expert labor make hard to obtain. User simulation offers a rem…

- **[PULSES: multi-agent AI for autonomous excited-state model building and dynamics](https://arxiv.org/abs/2610.32392v1)**
  - *Fangning Ren, Lechen Dong, Xu Chen et al.*
  - `2026-10-23`
  - Simulating molecular excited-state processes requires resolving electronic and nuclear dynamics, but the cost of direct quantum-chemical calculations limits accessible system sizes and timescales. Machine-learning models can extend these simulations, yet they often need to be tai…

- **[Evidence-Grounded SLM Behavioral Prediction Architecture for Future Assistance Use](https://arxiv.org/abs/2610.32193v1)**
  - *Adeyemi Adeseye, Aisvarya Adeseye, Hannu Tenhunen et al.*
  - `2026-10-23`
  - Users often exhibit changes in interaction behavior before explicitly seeking assistance, enabling systems to anticipate future assistance use. This is especially important in high-stakes environments, where delayed assistance can have operational, financial, or safety consequenc…

- **[On the continuity of conditional distributions and stratification for derivative pricing](https://arxiv.org/abs/2610.32970v1)**
  - *Aleksandar Arandjelovic, Patrick Cheridito*
  - `2026-10-23`
  - Stratification can reduce the estimator variance in Monte Carlo simulations by partitioning the sample space according to a low-dimensional factor and sampling separately within the resulting strata, making it well suited to the valuation of path-dependent claims in high-dimensio…

- **[Heterogeneous Space Data Centers: A Key Paradigm for Future Non-Terrestrial and In-Orbit Services](https://arxiv.org/abs/2610.32260v1)**
  - *Peng Hu, Mustafa Alhassan, Amjad Iqbal*
  - `2026-10-23`
  - Lower space-launch cost and advances in AI are driving space-based data centers (SDCs) that provide AI-centric computing and communication services to in-orbit and non-terrestrial assets. However, architectural principles, service models, and energy provisioning for such SDCs, pa…

- **[RootDown: Deploying and Benchmarking Models for Beet-Root Detection on Edge Devices](https://arxiv.org/abs/2610.32275v1)**
  - *Gerardus Croonen, Andreas Trondl, Julia Simon et al.*
  - `2026-10-23`
  - Quality inspection of sugar beets after harvest and storage is critical to preserve sugar content and ensure optimal processing efficiency. The transfer of harvested beets to field clamps or trucks provides an opportunity to visually inspect individual beets automatically on load…

- **[Risk Adequacy and Anti-Discrimination in Insurance Pricing: Classification, Aggregation, and Transfers](https://arxiv.org/abs/2610.32614v1)**
  - *Wiebke Hansen, Stefan Weber, Mario Wüthrich*
  - `2026-10-23`
  - Insurance tariffs must reconcile risk-based pricing, portfolio coverage, and anti-discrimination requirements. We introduce a framework in which tariffs are constructed through classification, aggregation of benchmark risk prices within classes, and balanced transfers, and are ev…


---
*Generated 2026-10-26 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
