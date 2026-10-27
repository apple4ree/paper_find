# Daily Paper Digest — 2026-10-27 (Tuesday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**435 unique papers** (569 topic-entries — cross-topic papers counted once per category)

---

## Agent  (302)

### AAAI

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

- **[AlphaIdeaBench: Benchmarking Automated Research Idea Generation under Feasibility Constraints with Peer Review Alignment](https://arxiv.org/abs/2610.33644v1)**
  - *Shunchao Zhou, Chang Yang, Jingrui Wang et al.*
  - **NeurIPS** · `2026-10-24`
  - Research ideas are always proposed under resource constraints: a plan must fit the available compute, API credit, and time. Yet evaluations of research-ideation agents mostly score unconstrained novelty or overlap with a published paper, and their LLM judges are rarely checked ag…

- **[WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)**
  - *Jia-Long Wu, Baixuan Li, Run-Nan Fang et al.*
  - **NeurIPS 2025** · `2025-05-28`
  - Addressing intricate real-world problems necessitates in-depth information seeking and multi-step reasoning. Recent progress in agentic systems, exemplified by Deep Research, underscores the potential for autonomous multi-step research. In this work, we present a cohesive paradig…

- **[STRATUS: A Multi-agent System for Autonomous Reliability Engineering of Modern Clouds](https://arxiv.org/abs/2506.02009)**
  - *Yinfang Chen, Jia-Qi Pan, J. Clark et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - In cloud-scale systems, failures are the norm. A distributed computing cluster exhibits hundreds of machine failures and thousands of disk failures; software bugs and misconfigurations are reported to be more frequent. The demand for autonomous, AI-driven reliability engineering…

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

- **[The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation](https://arxiv.org/abs/2610.35541v1)**
  - *Ruozhao Yang, Jiongchi Yu, Ming Hu et al.*
  - **ACL** · `2026-10-26`
  - Web services increasingly expose backend interfaces that let users delegate tasks to AI agents, which invoke service operations directly without navigating websites. This shift changes how existing Web vulnerabilities can be exploited. We investigate these changes through VELA, a…

- **[Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives](https://arxiv.org/abs/2610.35240v1)**
  - *Radha Krishna Deshpande, Ajoy Mondal, Akash Manna et al.*
  - **ACL** · `2026-10-26`
  - India's historical public archives present severe computer vision and document image analysis challenges: decades of parliamentary records survive only as degraded, multi-column scanned pages featuring mixed scripts, complex layouts, and dense visual noise where OCR failure is th…

- **[Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents](https://arxiv.org/abs/2610.34817v1)**
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

- **[Human-Feedback-Guided Multi-Agent Inverse Reinforcement Learning for Interactive Driving Behavior Modeling](https://arxiv.org/abs/2610.33726v1)**
  - *Longhao Yan, Jinhao Liang, Kaidi Yang*
  - **ACL** · `2026-10-24`
  - Modeling human driving behavior is fundamental to understanding driver decision-making and supporting autonomous vehicles (AVs) in mixed traffic. Reward learning offers a principled way to infer the latent objectives behind driving behaviors, yet most existing methods are formula…

- **[Temp-R1: A Unified Autonomous Agent for Complex Temporal KGQA via Reverse Curriculum Reinforcement Learning](https://arxiv.org/abs/2601.18296)**
  - *Zhaoyan Gong, Zhiqiang Liu, Song-Ze Li et al.*
  - **ACL 2026** · `2026-01-26`
  - Temporal Knowledge Graph Question Answering (TKGQA) is inherently challenging, as it requires sophisticated reasoning over dynamic facts with multi-hop dependencies and complex temporal constraints. Existing methods rely on fixed workflows and expensive closed-source APIs, limiti…

- **[MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive and MCP-Augmented Environments](https://arxiv.org/abs/2512.19432)**
  - *Qu-Yu Kong, Xu Zhang, Zhen-Yu Yang et al.*
  - **ACL 2025** · `2025-12-22`
  - Among existing online mobile-use benchmarks, AndroidWorld has emerged as the dominant benchmark due to its reproducible environment and deterministic evaluation; however, recent agents achieving over 90% success rates indicate its saturation and motivate the need for a more chall…

- **[GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://arxiv.org/abs/2505.16827)**
  - *Bin Xie, Rui Shao, Gongwei Chen et al.*
  - **ACL 2025** · `2025-05-22`
  - GUI automation faces critical challenges in dynamic environments. MLLMs suffer from two key issues: misinterpreting UI components and outdated knowledge. Traditional fine-tuning methods are costly for app-specific knowledge updates. We propose GUI-explorer, a training-free GUI ag…


### EMNLP

- **[Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances](https://arxiv.org/abs/2502.16804)**
  - *Yaozu Wu, Dong-Yuan Li, Yan-Kai Chen et al.*
  - **EMNLP 2025** · `2025-02-24`
  - Autonomous Driving Systems (ADSs) are revolutionizing transportation by reducing human intervention, improving operational efficiency, and enhancing safety. Large Language Models (LLMs) have been integrated into ADSs to support high-level decision-making through their powerful re…

- **[Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)**
  - *Samuel Schmidgall, Yu-Sheng Su, Ze Wang et al.*
  - **EMNLP 2025** · `2025-01-08`
  - Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory, an…


### IJCAI

- **[Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition](https://arxiv.org/abs/2610.34777v1)**
  - *Weihang Niu, Mengxing Ren, Che Qu*
  - **IJCAI** · `2026-10-26`
  - This paper introduces Scope-Gap Injection (SGI), an indirect prompt injection method for multi-stage LLM-agent safety pipelines. In the IJCAI 2026 OpenClaw Agent Security Attack Competition, each attack package is judged by a static skill scan (S1), an LLM-judge safety check over…


### NAACL

- **[CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://arxiv.org/abs/2501.16609)**
  - *Faria Huq, Zora Zhiruo Wang, Frank F. Xu et al.*
  - **NAACL 2025** · `2025-01-28`
  - While much work on web agents emphasizes the promise of autonomously performing tasks on behalf of users, in reality, agents often fall short on complex tasks in real-world contexts and modeling user preference. This presents an opportunity for humans to collaborate with the agen…


### Other / arXiv

- **[StreamVibe: Proactive Video Agents for Evolving User Intent](https://arxiv.org/abs/2610.34662)**
  - *Chengzhi Liu, Yuxiang Lai, Yuzhe Yang et al.*
  - 🤗 Featured · `2026-10-26`

- **[Work Agents: Systems, Capabilities, and Optimization](https://arxiv.org/abs/2610.35845)**
  - *Zishan Xu, Enjun Du, Mingqi Gao et al.*
  - 🤗 Featured · `2026-10-26`
  - As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish deleg…

- **[EmbodiedLab: Benchmarking Embodied Agents That Act to Know](https://arxiv.org/abs/2610.35385)**
  - *Hongcheng Gao, Zelin Zheng, Alex Zhou et al.*
  - 🤗 Featured · `2026-10-26`

- **[Skill^{infty}: Recursive Self-Improvement for Agent Skill Optimization](https://arxiv.org/abs/2610.35434)**
  - *Wangcheng Tao, Zhanglu Yan, Han Wu et al.*
  - 🤗 Featured · `2026-10-26`
  - Recursive self-improvement (RSI), in which a system also improves the way it improves, is a long-standing aspiration on the path to AGI. Language agents increasingly store procedural knowledge in reusable skills. Optimizing skills offers a direct way to achieve RSI, because the o…

- **[Thinking-in-Bets at Test Time Reduces Sycophantic Revisions in LLM Agents](https://arxiv.org/abs/2610.34654)**
  - *Nghi D. Q. Bui*
  - 🤗 Featured · `2026-10-26`
  - Language model agents often abandon correct work when a user challenges it, yet simply telling them to stand firm makes them ignore real mistakes. Once an agent reads a complaint, it tends to discount its own earlier checks in order to agree with the user. We introduce Thinking-i…

- **[DynaFlow: Learning Free-Form Multi-Agent Orchestration](https://arxiv.org/abs/2610.34467)**
  - *Ruhao Liu, Qi Li, Shizun Wang et al.*
  - 🤗 Featured · `2026-10-25`
  - Multi-agent systems often rely on predefined collaboration structures, limiting their ability to adapt to diverse task requirements. We introduce DynaFlow, a framework that integrates free-form executable workflow synthesis into the action space of the main agent. The agent decid…

- **[Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents](https://arxiv.org/abs/2610.33956)**
  - *Haoyu Zhao, Sitian Tu, Yuxuan Huang et al.*
  - 🤗 Featured · `2026-10-25`
  - Continual learning is the ability of LLM agents to improve over time by acquiring, refining, and applying knowledge from experience while retaining useful prior knowledge. It is essential for agents learning over long time horizons, yet current evaluations largely assess individu…

- **[Δτ-Bench: Pushing Agents Toward a Moving Capability](https://arxiv.org/abs/2610.34238)**
  - *Shuofei Qiao, Xuanguang Pan, Yijun Chen et al.*
  - 🤗 Featured · `2026-10-25`
  - In this paper, we introduce $Δτ$-Bench, an executable agent benchmark that models the structural evolution of large tool ecosystems. In $Δτ$-Bench, independently evolving services continually reshape how tasks can be accomplished: familiar tools may disappear or be replaced, whil…

- **[ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2610.18683)**
  - *Bowen Ding, Mingda Wan, Yuhan Chen et al.*
  - 🤗 Featured · `2026-10-25`

- **[AgentProofBench: Benchmarking Reusable Verifiers for Web Agents](https://arxiv.org/abs/2610.34634)**
  - *Jingjie Ning, Xueqi Li, Yi Lu et al.*
  - 🤗 Featured · `2026-10-25`
  - Reusable Web-agent verification requires a rule to follow changing requirements and support subsequent execution. We introduce AgentProofBench, which connects paired tests of a frozen acceptance rule to execution from identical saved openings. The resource spans 97 tasks, 79 fami…

- **[Intrinsic Goals for Autonomous Agents: Hierarchical Exploration Captures Future Volitional Action in Drosophila](https://arxiv.org/abs/2610.34638)**
  - *Declan Kutscher, Reece Keller, Alyn Kirsch et al.*
  - 🤗 Featured · `2026-10-25`
  - Animals have a remarkable capacity for autonomy---driven by intrinsic motivation---without external sensory cues or extrinsic objectives, yet the computational mechanisms behind this ability largely remain a mystery. We combine whole-brain recordings in the fruit fly (Drosophila…

- **[Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents](https://arxiv.org/abs/2610.33568)**
  - *Yihao Hu, Zhihao Wen, Yitong Lin et al.*
  - 🤗 Featured · `2026-10-24`
  - Successful tool-use trajectories are not necessarily useful supervision. Even successful interactions may underrepresent multi-step dependencies or contain actions that are unjustified by the information visible to the agent at decision time. We identify two coupled requirements…

- **[Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players](https://arxiv.org/abs/2610.33845)**
  - *Changlian Ma, Limin Wang*
  - 🤗 Featured · `2026-10-24`
  - Can LLM agents carry a hard real-world problem from raw data to a system that holds its own against people? We study this in Hearthstone Battlegrounds, an eight-player auto-battler with stochastic shops and battles, hidden information and nearly a thousand interacting cards. We p…

- **[Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in Patent Examination](https://arxiv.org/abs/2610.33503)**
  - *Qiyao Wang, Xinyi Chen, Hongbo Wang et al.*
  - 🤗 Featured · `2026-10-24`
  - Patent examination is a challenging real-world task that requires agents to discover sparse prior art, iteratively refine queries, inspect technical evidence, and produce novelty assessments documented in Office Actions (OAs) across heterogeneous scientific and technical domains.…

- **[Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](https://arxiv.org/abs/2610.32285)**
  - *Zhiyong Cao, Hengjie Zhu, Yongxin Wang et al.*
  - 🤗 Featured · `2026-10-23`

- **[Steering Black-Box Large Language Model Agents with Pitfall Anticipation World Model](https://arxiv.org/abs/2610.29139)**
  - *Jiongxiao Wang, Han Ding, Youzhi Luo et al.*
  - 🤗 Featured · `2026-10-21`

- **[DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents](https://arxiv.org/abs/2610.21561)**
  - *Sergio Burdisso, Esaú Villatoro-Tello, Dairazalia Sánchez-Cortés et al.*
  - 🤗 Featured · `2026-10-15`

- **[A Unified Arena for LLM Agents across Diverse Eurogame](https://arxiv.org/abs/2610.35773)**
  - *Fengrui Zhang, Xiang Li, Ruomeng Ding et al.*
  - 🤗 · `2026-10-26`
  - Interactive environments offer a practical way to evaluate large language model (LLM) agents, and competitive games extend this evaluation to decisions shaped by competing goals and other agents' choices. Yet existing evaluations confined to individual games or execution framewor…

- **[MiRL: Error-Targeted Reinforcement Learning for Correcting Terminal Agent Misbehaviors](https://arxiv.org/abs/2610.35697)**
  - *Runchu Tian, Zaid Khan, Zun Wang et al.*
  - 🤗 · `2026-10-26`
  - Error-targeted learning gives a legible way to improve a model: identify specific weaknesses of the model, train the model to fix these weaknesses, and check whether the weaknesses are fixed. We study how to apply error-targeted learning to terminal agents, which solve long-horiz…

- **[EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation](https://arxiv.org/abs/2610.35690)**
  - *Yitao Xiao, Xu Zhang, Ye Cheng et al.*
  - 🤗 · `2026-10-26`
  - Serving web queries at scale with multi-agent systems requires jointly configuring large language models, collaboration modes, agent counts, interaction rounds, and skills. However, the resulting configuration space grows combinatorially, while sparse execution rewards provide li…

- **[Omni-InteractScope: Benchmarking Proactive and Agentic Interaction in Continuous Omnimodal Streams](https://arxiv.org/abs/2610.35439)**
  - *Yinsong Yan, Ling Wang, Yuxuan Wang et al.*
  - 🤗 · `2026-10-26`
  - Omnimodal large language models (Omni-LLMs) are increasingly expected to assist users while observing continuous audiovisual streams. However, existing evaluations provide limited insight into how reliably these models connect stream evidence and user needs to timely, sustained i…

- **[The Voice on the Line](https://arxiv.org/abs/2610.35272)**
  - *Husein Zolkepli*
  - 🤗 · `2026-10-26`
  - A transcriber listening through one microphone also hears everyone near it. We train causal voice isolators: masking transformers of 140M, 243M and 374M parameters, 20 ms of latency, enrolling the caller from the call itself. Short evaluation windows hide two failures that real c…

- **[MedAdaptAgent: An Automatic Harness for Adapting Medical Imaging Models to New Sites](https://arxiv.org/abs/2610.34884)**
  - *Hanxue Gu, Zhonghao Liu, Xingrui Gu et al.*
  - 🤗 · `2026-10-26`

- **[Harness-Model Collaboration for Long-Horizon Continual Learning](https://arxiv.org/abs/2610.34724)**
  - *Zhen Bi, Zhizhi Peng, Yan Wang et al.*
  - 🤗 · `2026-10-26`
  - Long-horizon agents continuously encounter reusable procedural knowledge, yet existing systems typically rely either on model adaptation or external memory, trading persistent learning for rapid reuse. This limitation is especially important for Web agents that repeatedly execute…

- **[RobotAgentBench: Towards Open-world Robot Autonomy](https://arxiv.org/abs/2610.34649)**
  - *Lingjun Mao, Jinglin Cao, Lukun He et al.*
  - 🤗 · `2026-10-26`
  - Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm fo…

- **[Can LLMs Trust Appropriately? Evaluating Calibrated Reliance on Imperfect Partners](https://arxiv.org/abs/2610.34107)**
  - *Mengdi Chu, Jintao Huang*
  - 🤗 · `2026-10-25`
  - Large language models increasingly collaborate with humans and peer AI agents whose contributions may be incomplete, inconsistent, or incorrect. Effective collaboration requires calibrated trust, whereby decisions to rely on, verify, or assist a partner adapt rationally as empiri…

- **[I-HITL: Inalienable Human-in-the-Loop](https://arxiv.org/abs/2610.35835v1)**
  - *Samuel Breckenridge, Dani Vilardell, Wenhao Wang et al.*
  - `2026-10-26`
  - Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.   We introduce the co…

- **[Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](https://arxiv.org/abs/2610.35832v1)**
  - *Yifei Yao, Yude Zou, Guanbo Jiao et al.*
  - `2026-10-26`
  - Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action model (WAM) policies across manipulation demands remains to be tho…

- **[Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models](https://arxiv.org/abs/2610.35829v1)**
  - *Amine Lbath, Massih-Reza Amini*
  - `2026-10-26`
  - A vulnerability costs more to fix the later it is discovered. As coding agents generate code faster than developers can review it, software needs a first line of defense screening each new function in real time. LLM agents have recently become capable of finding real-world vulner…

- **[Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](https://arxiv.org/abs/2610.35817v1)**
  - *Benjamin Pikus, Daniel Saunders, Mircea Mironenco et al.*
  - `2026-10-26`
  - A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task. To achieve these two skills, we introduce Zero-real Agent Policy (ZAP), a recipe that teaches a small off-the-shelf vision-language model to control a robot…

- **[Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents](https://arxiv.org/abs/2610.35767v1)**
  - *Tingzhu Bi, Xun Zhang, Jinglin Li et al.*
  - `2026-10-26`
  - Root cause analysis (RCA) of microservice failures has attracted many LLM agents whose investigation is hand-crafted, through standard operating procedures, fixed stages and role agents. Each is evaluated on its own data against few baselines, so it is unknown whether this design…

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

- **[Agentic Algorithm Design: LLMs that Propose, Formalise, and Prove Runtime Bounds for Evolutionary Algorithms in Lean](https://arxiv.org/abs/2610.35595v1)**
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

- **[Multiscale Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.35013v1)**
  - *Tao Ren, Hui Yang, Jia Deng et al.*
  - `2026-10-26`
  - Long-horizon LLM agents interact with their environments through complete assistant turns while generating each action token by token. We observe that critic values vary primarily across turns, motivating optimization anchored at turns with finer credit allocation among tokens. W…

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

- **[SearchHorizonBench: A Benchmark for Search Value in AI Agents](https://arxiv.org/abs/2610.34714v1)**
  - *Jingjie Ning, Xueqi Li, Yibo Kong*
  - `2026-10-26`
  - AI agents must decide when another search is worth its cost. Answer-success probabilities capture question difficulty, while this decision requires estimating the additional benefit of search. We introduce SearchHorizonBench, a benchmark for learning and evaluating search value f…

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

- **[SlowLab: Benchmarking Autonomous AI Agents on a Year of Experiments They Cannot Undo](https://arxiv.org/abs/2610.34644v1)**
  - *Ningpei Ding, Zai Wen Feng*
  - `2026-10-26`
  - AI agents are increasingly proposed as autonomous experimenters, yet the benchmarks that test them mostly offer cheap experiments that answer at once. Experiments in physical facilities are different: they take months, occupy scarce equipment and cannot be undone. We present Slow…

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

- **[Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks](https://arxiv.org/abs/2610.35671v1)**
  - *Yao Huang, Zhiyuan Zeng, Yu Wang et al.*
  - `2026-10-26`
  - As frontier language models grow increasingly capable and autonomous, independent third-party evaluations are critical for characterizing their systemic safety risks. While closed-source releases are routinely accompanied by comprehensive system cards, open-weight models receive…

- **[Hierarchical Skill Evolution for Coding Agent](https://arxiv.org/abs/2610.35616v1)**
  - *Jun Gao, Yun Peng, Changhai Zhou et al.*
  - `2026-10-26`
  - Skills provide agents with reusable experience to guide future decisions without modifying the underlying model. However, coding trajectories are often entangled with task- and repository-specific contexts, making it challenging to distill procedural skills that generalize across…

- **[From Questions to Queries to Insights: A Schema-Grounded Agentic Workflow for Natural-Language Crash Data Analysis](https://arxiv.org/abs/2610.35054v1)**
  - *Jingwen Zhu, Keshu Wu, Steven T. Parker et al.*
  - `2026-10-26`
  - Transportation agencies maintain extensive crash databases to identify safety priorities, evaluate countermeasures, and guide resource allocation. Making these data accessible to practitioners requires flexible ways to translate analytical questions into reliable results. Existin…

- **[FATE-5: Faithful Alignment of Trait Expression for Continuous Big Five Personality Control](https://arxiv.org/abs/2610.34889v1)**
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

- **[What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents](https://arxiv.org/abs/2610.34491v1)**
  - *Kaiser Sun, Yongchan Kwon, Zain Hasan et al.*
  - `2026-10-25`
  - Generative models increasingly expose a reasoning effort setting that lets users scale inference-time compute, trading higher cost for potentially improved performance. Users must choose an effort level before knowing whether extra reasoning will help, and even a successful run d…

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

- **[SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents](https://arxiv.org/abs/2610.34365v1)**
  - *Cheng Gui, Xiang Zheng, Xingjun Ma et al.*
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

- **[MatOS: An Agent Operating System for Materials Research](https://arxiv.org/abs/2610.34203v1)**
  - *Dingyang Lyu, Jing Gao, Zhonghao Chang et al.*
  - `2026-10-25`
  - Materials research relies on scattered and growing data, knowledge, and simulation tools, and a single study often spans multi-day workflows across literature analysis, computation, and experiment. Large language model agents can now retrieve materials data, operate simulation co…

- **[R2A-Sales: A Policy-Atom-Matched Benchmark for Rule-to-Action Gaps in Goal-Directed Sales Agents](https://arxiv.org/abs/2610.34185v1)**
  - *Yihua Qin, Jiajie Jerry Zhao*
  - `2026-10-25`
  - LLM-based sales agents are often evaluated on static policy questions or task success, but deployment asks a sharper question: when a model can state a rule, will it choose compliant, tool-grounded actions under commercial pressure? We introduce R2A-Sales (Rule-to-Action), a poli…

- **[From Document Layout to Causal Topology: An End-to-End Architecture for Temporal Causal Reasoning](https://arxiv.org/abs/2610.34094v1)**
  - *Zhifeng Yang, Wei Luo, Yongjian Chen et al.*
  - `2026-10-25`
  - Large language models (LLMs) generally lack deep causal reasoning capabilities in temporal reasoning. Inspired by document layout reordering, this paper proposes a paradigm shift from discrete narratives to causal topologies. It constructs two architectures: a training-free neuro…

- **[Holding a Steady Course: Knowledge Evolution from Expertise and Lessons for Continual Agent Learning](https://arxiv.org/abs/2610.34043v1)**
  - *Wenzhe Fan, Benjamin Steenhoek, Gaurav Mittal et al.*
  - `2026-10-25`
  - Autonomous agents are increasingly deployed across sequences of related tasks, yet they often fail to retain and improve their knowledge over time. Existing approaches convert interaction trajectories into memories or reusable skills, but experience is not automatically reliable…

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

- **[Memory Tax: Dissecting the Net Value of Agent Memory](https://arxiv.org/abs/2610.34073v1)**
  - *Xuan He, Sining Zhoubian, Ruozhen Yang et al.*
  - `2026-10-25`
  - Memory is increasingly used in long-horizon agents, yet the net value of building memory over direct retrieval from raw history remains largely unclear. Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems underper…

- **[FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation](https://arxiv.org/abs/2610.34564v1)**
  - *Meryem Koksal, Yunzhe Wang, Volkan Ustun*
  - `2026-10-25`
  - Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents. We introduce FlockWorld, an artificial-life environment built on Reynolds's Boids algorithm for studying population-scale mu…

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

- **[Certifying Reward Alignment in Portfolio Reinforcement Learning](https://arxiv.org/abs/2610.34153v1)**
  - *Matin Tavakoli, Seyedreza Tavakoli, Faezeh Salmani et al.*
  - `2026-10-25`
  - Financial reinforcement learning often translates an investment objective into an additive risk-adjusted reward. An agent can optimise that reward accurately yet implement a different financial preference. We develop a decision audit for terminal mean-variance equilibrium that se…

- **[OS-Wizard: Scaling Computer-Using Agents to Specialized Software via Knowledge-Guided Exploration](https://arxiv.org/abs/2610.33907v1)**
  - *Zhoumianze Liu, Zichen Ding, Bowen Yang et al.*
  - `2026-10-24`
  - Computer-using agents are increasingly capable of performing complex tasks in the digital world. However, high-quality interaction trajectories remain scarce for specialized desktop applications, where limited application knowledge, cumbersome GUI workflows, and incomplete explor…

- **[FlashScript: Compiling Recurring Agent Workflows into Reusable Neuro-Symbolic Programs](https://arxiv.org/abs/2610.33876v1)**
  - *Sadra Sabouri, Hosein Hasanbeig, Adam Sage et al.*
  - `2026-10-24`
  - Many agent tasks recur with new data or small changes, yet agents regenerate their reasoning and actions on each run, producing different results. Distilling a prior run into a skill helps the agent avoid earlier mistakes, but it still re-runs the full process each time, so runs…

- **[ReGE: Stronger Agents through Experience Synthesis](https://arxiv.org/abs/2610.33861v1)**
  - *Jiarong Liang, Yubo Wang, Zijie Liu et al.*
  - `2026-10-24`
  - Repeated attempts at interactive tasks uncover facts, useful operations, and failures that can inform subsequent execution. We introduce ReGE, a framework for turning this recorded experience into guidance for a fresh attempt. Its main implementation, ReGE-Syn, uses a single coac…

- **[Numina Fuse: Interactive Autoformalization in Lean 4](https://arxiv.org/abs/2610.33860v1)**
  - *Justin Asher, Yichuan Cao, Ruichen Qiu et al.*
  - `2026-10-24`
  - Numina Fuse is an agent-native application for formalizing mathematics in Lean 4. Since Lean can compile while not representing its intended informal meaning, and agents now write Lean faster than people can read it, we built Fuse around human supervision of agent work. A user wo…

- **[EnvLunch: The Environment as a Free Lunch for Learning to Interact](https://arxiv.org/abs/2610.33817v1)**
  - *Wei Liu, Min Gao, Yali Du et al.*
  - `2026-10-24`
  - For agentic data analysis, language-model agents often require a large number of annotated tasks to learn how to interact effectively with executable environments (i.e., databases). While high-quality annotated tasks require heavy manual effort, an executable environment already…

- **[Memory or a Clock? Auditing a Memory Advantage in XLand-MiniGrid with Seeds, Maps and Evaluation Noise Apart](https://arxiv.org/abs/2610.33816v1)**
  - *Rodrigo Reveron-Fonseca*
  - `2026-10-24`
  - On a partially observable XLand-MiniGrid task, an LSTM agent beats a memory-free MLP by 25 percentage points. The gap looks like a clear case of memory. We ask two questions about it. First, how much of a measured gap is noise? Separating training seed, map and evaluation randomn…

- **[The Hitchhiker's Guide to System 1 Models: Fast Decision-Making Beyond LLMS](https://arxiv.org/abs/2610.33775v1)**
  - *Haggai Roitman*
  - `2026-10-24`
  - Large Language Models excel at reasoning and generation but their autoregressive, token-by-token inference makes them unnecessarily slow, expensive, and poorly calibrated for the many routine decisions (routing, gating, scoring, classification) that modern AI systems require at s…

- **[ProtAgent: Post-Training Compact Protein Tool Agents with Interaction-Level Credit Assignment](https://arxiv.org/abs/2610.33746v1)**
  - *Yuxiang Wang, Baojian Zhou, Qifang Zhao et al.*
  - `2026-10-24`
  - Protein annotation agents must choose suitable bioinformatics tools, interpret their outputs, and use the resulting evidence in the final answer. Most existing systems rely on frontier-scale models. We ask whether a compact model can instead learn this behavior through post-train…

- **[Strategic Calibration in LLM Multi-Agent Systems: Audited Pivot Scoring for Truthful Elicitation](https://arxiv.org/abs/2610.33728v1)**
  - *Jinhao Zhou, Zhaohan Zhang, Xijian Xu et al.*
  - `2026-10-24`
  - In large language model (LLM)-based multi-agent systems, reported confidence increasingly determines the allocation of scarce downstream attention, computation, and decision influence. This makes reporting strategic: an agent may overstate the relevance of its contribution even w…

- **[Seeing the Options: Typed Decisions over Visual Candidates with Reusable Option Memory](https://arxiv.org/abs/2610.33702v1)**
  - *Fengxin Li*
  - `2026-10-24`
  - Typed decision-making tasks in agents, such as UI element selection, product recommendation, and chart matching, require models to choose from a set of discrete candidates. While prior work demonstrates that text-only System One models achieve four key properties including candid…

- **[PACE: Research Proving Agent for Adaptive Conjecture Exploration](https://arxiv.org/abs/2610.33690v1)**
  - *Shu Miao, Feiming Wang, Wentao Long et al.*
  - `2026-10-24`
  - Many mathematical research agents focus on solving problems with fixed statements. However, conjecture research, especially in applied mathematics, may require revising candidate questions or conclusions as investigation proceeds, coupling problem formulation with proof developme…

- **[More: Mode-Optimized Reasoning with Self-Adaptive Effort for Self-Evolving Agents](https://arxiv.org/abs/2610.33684v1)**
  - *Dianxing Shi, Dingjie Fu, Tianyu Lei et al.*
  - `2026-10-24`
  - Self-evolving training improves the performance of agents on difficult tasks through verifiable feedback, but it often applies costly deliberation uniformly across tasks. To address this problem, we propose Mode-Optimized Reasoning with Self-Adaptive Effort (MORE), a self-evolvin…

- **[SWE-Ladder: Learning to Localize, Reproduce, and Patch via Progressive Privileged Self-Distillation](https://arxiv.org/abs/2610.33667v1)**
  - *Xudong Cai, Zhengxi Lu, Yuchen Yan et al.*
  - `2026-10-24`
  - Resolving a repository-level issue typically requires a software-engineering (SWE) agent to localize the faulty code, reproduce the failure, and patch the code. Reinforcement learning trains such agents from a single test result on the final patch, while on-policy self-distillati…

- **[Jointly Modeling Preferences and Imperfect Decision-Making in Large Language Models](https://arxiv.org/abs/2610.33651v1)**
  - *Axel Abels, Elias Fernández Domingos, Tom Lenaerts*
  - `2026-10-24`
  - Do preferences Large Language Models (LLMs) express in standard elicitation tasks predict their strategic behaviour? LLM agents interacting with humans and other AI systems face potentially conflicting objectives, such as individual welfare, group welfare, and environmental conce…

- **[Build or Adopt? Custom-Built vs. General-Purpose LLM Agent Harnesses for Automotive GUI Testing](https://arxiv.org/abs/2610.33636v1)**
  - *Arsham Gholamzadeh Khoee, Ruyu Fu, Jiaqi Wei et al.*
  - `2026-10-24`
  - As general-purpose LLM agent harnesses mature, organizations must decide whether to continue developing in-house systems or adopt existing alternatives. We study this decision at Volvo Group for GUI testing of Android-based in-vehicle infotainment (IVI) systems. We compare a prod…

- **[ProbeID: Verifying MCP Tool Identity for LLM Agents under Registry Drift](https://arxiv.org/abs/2610.33633v1)**
  - *Guanxing Chen, Sining Zhang, Haohuai He et al.*
  - `2026-10-24`
  - Agents select tools by copyable descriptions, which cannot establish which implementation runs. ProbeID compares canonicalized responses to schema-valid probes with a trusted admission reference and abstains on ambiguity, so a squatter must copy probe-observable behavior. With th…

- **[RSI Arena: Towards Recursive Self-Improvement with Human Feedback](https://arxiv.org/abs/2610.33624v1)**
  - *Yue Huang, Yanbo Wang, Lichi Li et al.*
  - `2026-10-24`
  - Can AI agents autonomously train useful language models and improve them using feedback from users? We introduce RSI Arena, a two-stage study of autonomous post-training as a step toward recursive self-improvement. Ten frontier models act as training agents, each starting from NV…

- **[Data Governance for Generative and Agentic AI : Technology, Law, Economics, and Security](https://arxiv.org/abs/2610.33605v1)**
  - *Narayana Darapaneni, Padmaja K, Gnana Chaithra D*
  - `2026-10-24`
  - This book develops a unified governance framework for systems that retrieve, generate, infer, remember and act on information from large language models and retrieval augmented pipelines to autonomous multi agent systems. Eleven chapters and eight appendices integrate three disci…

- **[Auditing evaluation artifacts and data leakage in large language model systems for rare disease diagnosis](https://arxiv.org/abs/2610.33592v1)**
  - *Jian Yang, Peilin Liu, Xiaohan Li et al.*
  - `2026-10-24`
  - Augmented large language model (LLM) systems have reported high benchmark accuracies in rare disease diagnosis, yet their real-world clinical utility remains unproven. A recent meta-analysis flagged augmented LLM diagnostic evaluations as having a high risk of bias due to suspect…

- **[Replicate What Varies: Resource Sharing for Domain-Randomized Embodied Simulation](https://arxiv.org/abs/2610.33582v1)**
  - *Zixu Hao, Weijun Wang, Xiangyu Li et al.*
  - `2026-10-24`
  - Simulation provides a low-cost sandbox where embodied agents can attempt tasks, observe outcomes, and learn from experience. Running many diverse simulation environments concurrently can consume substantial CPU and GPU memory because independently constructed scenes duplicate res…

- **[Learning When to Collaborate: Selective Multi-Agent Medical Reasoning via Uncertainty-Aware Routing](https://arxiv.org/abs/2610.33544v1)**
  - *Jiacheng Hou, Xueliang Cui, Dan Lu et al.*
  - `2026-10-24`
  - Multi-agent systems have emerged as a promising paradigm for multimodal medical reasoning, but existing methods rely on two assumptions that hinder practical deployment: (i) always-active dense collaboration among multiple agents, and (ii) dependence on large cloud-based models t…

- **[CoEvolve: Counterfactual-Guided Co-Evolution of Memory and Collaboration in Multi-Agent Systems](https://arxiv.org/abs/2610.33539v1)**
  - *Xufei Shi, Derong Xu, Wei Chen et al.*
  - `2026-10-24`
  - Large language model (LLM)-based multi-agent systems have demonstrated remarkable capabilities across diverse tasks. Yet their memory and collaboration architectures often remain static, constraining continued adaptation and improvement over time. Recent work addresses this limit…

- **[FraudSociety: A Generative Agent-Based Society for the Financial-Fraud Economy](https://arxiv.org/abs/2610.33536v1)**
  - *Keyang Chen, Mingxuan Jiang, Zeping Li et al.*
  - `2026-10-24`
  - Financial fraud caused over \$15.9 billion in losses in the United States in 2025, according to the Federal Trade Commission~\citep{ftc2026databook}. Understanding such large-scale harm requires jointly modeling informational and financial dynamics. Yet existing simulators typica…

- **[SkillShift-Bench: Benchmarking Skill Learning under Environment Evolution for Web Agents](https://arxiv.org/abs/2610.33528v1)**
  - *Bo-Yu Chen, Zhi Zhou, Yu-Feng Li*
  - `2026-10-24`
  - Skill learning enables web agents to reuse prior experience for long-horizon interactive tasks. However, learned skills are typically evaluated in closed environments, overlooking the fact that real-world web deployment involves continuous shifts in invocation context, perceptual…

- **[Can Agentic Code Review Catch Vulnerabilities Before They Are Merged?](https://arxiv.org/abs/2610.33509v1)**
  - *Yihan Yang, Chenyuan Yang, Zijie Zhao et al.*
  - `2026-10-24`
  - LLM agents have been increasingly adopted for security-focused code review, but existing benchmarks mostly derive the reviewed changes from their later fixes instead of the real-world bug-introducing commits. In this paper, we present SecPRBench, the first comprehensive benchmark…

- **[LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference](https://arxiv.org/abs/2610.33475v1)**
  - *Jannatun Noor, Athar Noor Mohammad Rafee, Md. Sadman Haque et al.*
  - `2026-10-24`
  - The widespread deployment of foundational Large Language Models (LLM) across cloud datacenters marks a fundamental paradigm shift from stateless deep learning toward distributed, memory-intensive generative workloads. However, serving massive foundation models under stringent Ser…

- **[LegoSR: A Unified Framework for Self-improving Agent-Guided Scientific Discovery](https://arxiv.org/abs/2610.33465v1)**
  - *Hao Mao, Xu T. Liu, Peng Zhao et al.*
  - `2026-10-24`
  - Equation discovery solvers often use different data interfaces, equation representations and evaluation criteria, making their results difficult to compare. We present LegoSR, a unified framework for algebraic symbolic regression and differential equation discovery. LegoSR integr…

- **[ConMem: Counterfactual Multi-Scenario Probing for Resolving LLM Memory Misalignment](https://arxiv.org/abs/2610.33432v1)**
  - *Shuning Zhang, Tenghao Ji, Jingruo Chen et al.*
  - `2026-10-24`
  - Long-term memory is critical for autonomous Large Language Model (LLM) agents executing multi-session, long-horizon tasks. However, existing memories often inappropriately store, retain, or retrieve over-generalized, misattributed, or privacy-sensitive information, a problem we t…

- **[AgentOrch: How Close Can Global Orchestration Come to Step-by-Step Interaction?](https://arxiv.org/abs/2610.33375v1)**
  - *Zijie Liu, Qi Yang Huang, Jinhao Duan et al.*
  - `2026-10-24`
  - Enterprise workflow agents typically rely on step-by-step interaction (Step-by-Step): the agent executes an action, observes its result, and invokes a large language model (LLM) again to decide the next step. Global orchestration (Global) instead generates a complete executable w…

- **[Software Engineering LLMs: Why We Need Them and How Software Engineering Helps Build Them](https://arxiv.org/abs/2610.33851v1)**
  - *Amir M. Ebrahimi, Mohammed Mehedi Hasan, Seyed Shayan Daneshvar et al.*
  - `2026-10-24`
  - Software engineering (SE) expertise can shape how coding large language models (LLMs) are trained and which engineering capabilities they acquire. We examine this role through an industrial case study of capability-focused training for a 92B-parameter coding LLM serving more than…

- **[Approximate Universal Prediction under Interaction](https://arxiv.org/abs/2610.33842v1)**
  - *Richard Cornelius Suwandi*
  - `2026-10-24`
  - Bayesian mixtures, and Solomonoff induction in particular, provide an idealized model of prediction learned by minimizing population log loss, and they underlie universal agents such as AIXI. An agent that plans with an approximation of such a predictor decides where that predict…

- **[Reactive Optimizers](https://arxiv.org/abs/2610.33826v1)**
  - *Xingjian Bai, Jia-Hao Liang, Jayden Teoh et al.*
  - `2026-10-24`
  - We study a reactive optimizer that uses a pretrained language-model agent to inspect training dynamics and rewrite executable optimizer code during a single training run. The agent can change update rules and schedules for individual parameter groups, without optimizer-specific m…

- **[Collective Collaboration of Recursive Autonomous Agents](https://arxiv.org/abs/2610.33515v1)**
  - *Ziqing Zhou, Linqiang Hu, Yuning Chen et al.*
  - `2026-10-24`
  - Smart factories must translate order-level objectives into production tasks at multiple scales and combine the capabilities of individual units into an overall delivery capability. To address repeated adaptation of organizational mechanisms across equipment, workshops, and factor…

- **[From Intelligence to Autonomy: Foundations and Construction of Autonomous Agents for Future Intelligent Systems](https://arxiv.org/abs/2610.33445v1)**
  - *Hongda Zhang, Ziqing Zhou, Yuning Chen et al.*
  - `2026-10-24`
  - Artificial intelligence is moving from one-off perception and generation tasks toward long-term planning, tool use, and interaction with real environments. Greater task competence, however, does not automatically yield autonomy: an external actor may still have to set goals, sust…

- **[An Empirical Study of Reinforcement Learning Scaling Laws](https://arxiv.org/abs/2610.33420v1)**
  - *Zeyu Zheng, Clare Lyle, Khimya Khetarpal et al.*
  - `2026-10-24`
  - The discovery of scaling laws enables prediction of the performance, the optimal resource allocation strategy, and the best hyperparameter configuration of a large-scale training job based on inexpensive experiments at smaller scales. Guided by these empirical scaling laws, the d…

- **[When Personas Become Harmful: Guiding LLMs with Global Citizenship Values Alignment](https://arxiv.org/abs/2610.33899v1)**
  - *Siqi Shen, Lajanugen Logeswaran, Moontae Lee et al.*
  - `2026-10-24`
  - LLMs are increasingly being used by users from diverse demographics with pluralistic values and distinct backgrounds. Maintaining safety while respecting value-laden personas is uniquely challenging because persona-conditioned requests are often not overtly malicious, unlike thos…

- **[IntentDelta: A Human-Constructed Benchmark for Evolving User Intent](https://arxiv.org/abs/2610.33806v1)**
  - *Jieyu Zhou, Zijian Wang, Yun Wang*
  - `2026-10-24`
  - Language-model agents must adapt as users revise their requirements and priorities during complex tasks. We introduce IntentDelta, a human-constructed multi-turn benchmark with 638 trajectories and 3,766 turns across WebShop and TravelPlanner. Each turn pairs a user utterance wit…

- **[MTA-Zero: Self-Improving Multimodal Deep Search via Online QA-Solver Co-training](https://arxiv.org/abs/2610.33799v1)**
  - *Xiangyu Peng, Jiaxin Zhang, An Yan et al.*
  - `2026-10-24`
  - Multimodal large language models (MLLMs) have become strong visual reasoners, yet remain limited in open-world, multi-step search that requires grounding images, selecting tools, and integrating web evidence. Existing approaches typically construct and filter fixed offline corpor…

- **[Agent-to-Agent Synthetic Social Engineering on the Web](https://arxiv.org/abs/2610.33411v1)**
  - *Bryan C. Boots*
  - `2026-10-24`
  - An AI agent can prepare an accurate report and still request an action its user has not authorized. Cooperation across Web services therefore requires separate judgments about identity, evidentiary support, and permission. We define synthetic social engineering (SSE) as deliberat…


## Harness  (112)

### NeurIPS

- **[AlphaIdeaBench: Benchmarking Automated Research Idea Generation under Feasibility Constraints with Peer Review Alignment](https://arxiv.org/abs/2610.33644v1)**
  - *Shunchao Zhou, Chang Yang, Jingrui Wang et al.*
  - **NeurIPS** · `2026-10-24`
  - Research ideas are always proposed under resource constraints: a plan must fit the available compute, API credit, and time. Yet evaluations of research-ideation agents mostly score unconstrained novelty or overlap with a published paper, and their LLM judges are rarely checked ag…

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

- **[From Guidelines to Guarantees: A Graph-Based Evaluation Harness for Domain-Specific Evaluation of LLMs](https://openreview.net/forum?id=9Y10aBDIlj)**
  - *Jessica M. Lundin, Usman Nasir Nakakana, Guillaume Chabot-Couture*
  - **ICLR 2026** · OpenReview · `2026-03-20`
  - Rigorous evaluation of domain-specific language models requires benchmarks that are comprehensive, contamination-resistant, and maintainable. Static, manually curated datasets do not satisfy these properties. We present a graph-based evaluation harness that transforms structured…


### Other / arXiv

- **[Work Agents: Systems, Capabilities, and Optimization](https://arxiv.org/abs/2610.35845)**
  - *Zishan Xu, Enjun Du, Mingqi Gao et al.*
  - 🤗 Featured · `2026-10-26`
  - As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish deleg…

- **[Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents](https://arxiv.org/abs/2610.33956)**
  - *Haoyu Zhao, Sitian Tu, Yuxuan Huang et al.*
  - 🤗 Featured · `2026-10-25`
  - Continual learning is the ability of LLM agents to improve over time by acquiring, refining, and applying knowledge from experience while retaining useful prior knowledge. It is essential for agents learning over long time horizons, yet current evaluations largely assess individu…

- **[Δτ-Bench: Pushing Agents Toward a Moving Capability](https://arxiv.org/abs/2610.34238)**
  - *Shuofei Qiao, Xuanguang Pan, Yijun Chen et al.*
  - 🤗 Featured · `2026-10-25`
  - In this paper, we introduce $Δτ$-Bench, an executable agent benchmark that models the structural evolution of large tool ecosystems. In $Δτ$-Bench, independently evolving services continually reshape how tasks can be accomplished: familiar tools may disappear or be replaced, whil…

- **[Novel or Not? PatEx-Gym: Agentic Prior-Art Search for Novelty Assessment in Patent Examination](https://arxiv.org/abs/2610.33503)**
  - *Qiyao Wang, Xinyi Chen, Hongbo Wang et al.*
  - 🤗 Featured · `2026-10-24`
  - Patent examination is a challenging real-world task that requires agents to discover sparse prior art, iteratively refine queries, inspect technical evidence, and produce novelty assessments documented in Office Actions (OAs) across heterogeneous scientific and technical domains.…

- **[Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](https://arxiv.org/abs/2610.32285)**
  - *Zhiyong Cao, Hengjie Zhu, Yongxin Wang et al.*
  - 🤗 Featured · `2026-10-23`

- **[RoboHarness: A Simple Harness Outperforms VLA and World Action Models](https://arxiv.org/abs/2610.14018)**
  - *Bince Qu, Wei Chen, Bo Zhang*
  - 🤗 Featured · `2026-10-16`

- **[Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation](https://arxiv.org/abs/2610.33024)**
  - *Zhihao Yang, Haojin Wang, Juncheng Wu et al.*
  - 🤗 Featured · `2026-10-10`

- **[A Unified Arena for LLM Agents across Diverse Eurogame](https://arxiv.org/abs/2610.35773)**
  - *Fengrui Zhang, Xiang Li, Ruomeng Ding et al.*
  - 🤗 · `2026-10-26`
  - Interactive environments offer a practical way to evaluate large language model (LLM) agents, and competitive games extend this evaluation to decisions shaped by competing goals and other agents' choices. Yet existing evaluations confined to individual games or execution framewor…

- **[MedAdaptAgent: An Automatic Harness for Adapting Medical Imaging Models to New Sites](https://arxiv.org/abs/2610.34884)**
  - *Hanxue Gu, Zhonghao Liu, Xingrui Gu et al.*
  - 🤗 · `2026-10-26`

- **[Harness-Model Collaboration for Long-Horizon Continual Learning](https://arxiv.org/abs/2610.34724)**
  - *Zhen Bi, Zhizhi Peng, Yan Wang et al.*
  - 🤗 · `2026-10-26`
  - Long-horizon agents continuously encounter reusable procedural knowledge, yet existing systems typically rely either on model adaptation or external memory, trading persistent learning for rapid reuse. This limitation is especially important for Web agents that repeatedly execute…

- **[I-HITL: Inalienable Human-in-the-Loop](https://arxiv.org/abs/2610.35835v1)**
  - *Samuel Breckenridge, Dani Vilardell, Wenhao Wang et al.*
  - `2026-10-26`
  - Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.   We introduce the co…

- **[Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](https://arxiv.org/abs/2610.35832v1)**
  - *Yifei Yao, Yude Zou, Guanbo Jiao et al.*
  - `2026-10-26`
  - Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action model (WAM) policies across manipulation demands remains to be tho…

- **[Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent](https://arxiv.org/abs/2610.35817v1)**
  - *Benjamin Pikus, Daniel Saunders, Mircea Mironenco et al.*
  - `2026-10-26`
  - A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task. To achieve these two skills, we introduce Zero-real Agent Policy (ZAP), a recipe that teaches a small off-the-shelf vision-language model to control a robot…

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

- **[Prefetch-Steered Routing: Deterministic Cache-Aware Expert Selection for Offloaded Mixture-of-Experts Decoding](https://arxiv.org/abs/2610.34721v1)**
  - *Siming Huang*
  - `2026-10-26`
  - When a Mixture-of-Experts (MoE) model does not fit in GPU memory, batch-1 decoding is dominated by copying expert weights from host memory. Cache-aware routing reduces these copies by biasing the router toward resident experts, but combined with asynchronous prefetching it makes…

- **[Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling](https://arxiv.org/abs/2610.35866v1)**
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

- **[Diagnosing and Mitigating Long-Session Degradation in Full-Duplex Speech Models](https://arxiv.org/abs/2610.34991v1)**
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

- **[In-Context Adapter Generation for Compositional Generalization in Large Audio Language Models](https://arxiv.org/abs/2610.34413v1)**
  - *Yiwei Guo, Siqi Huang, Bohan Li et al.*
  - `2026-10-25`
  - Large audio language models (LALMs) have achieved strong performance on standard speech and audio understanding tasks, yet their ability to systematically generalize to novel task compositions remains underexplored. Taking a meta-learning view, we extend Text-to-LoRA (T2L) to LAL…

- **[Build or Adopt? Custom-Built vs. General-Purpose LLM Agent Harnesses for Automotive GUI Testing](https://arxiv.org/abs/2610.33636v1)**
  - *Arsham Gholamzadeh Khoee, Ruyu Fu, Jiaqi Wei et al.*
  - `2026-10-24`
  - As general-purpose LLM agent harnesses mature, organizations must decide whether to continue developing in-house systems or adopt existing alternatives. We study this decision at Volvo Group for GUI testing of Android-based in-vehicle infotainment (IVI) systems. We compare a prod…

- **[Auditing evaluation artifacts and data leakage in large language model systems for rare disease diagnosis](https://arxiv.org/abs/2610.33592v1)**
  - *Jian Yang, Peilin Liu, Xiaohan Li et al.*
  - `2026-10-24`
  - Augmented large language model (LLM) systems have reported high benchmark accuracies in rare disease diagnosis, yet their real-world clinical utility remains unproven. A recent meta-analysis flagged augmented LLM diagnostic evaluations as having a high risk of bias due to suspect…

- **[Can Agentic Code Review Catch Vulnerabilities Before They Are Merged?](https://arxiv.org/abs/2610.33509v1)**
  - *Yihan Yang, Chenyuan Yang, Zijie Zhao et al.*
  - `2026-10-24`
  - LLM agents have been increasingly adopted for security-focused code review, but existing benchmarks mostly derive the reviewed changes from their later fixes instead of the real-world bug-introducing commits. In this paper, we present SecPRBench, the first comprehensive benchmark…

- **[Software Engineering LLMs: Why We Need Them and How Software Engineering Helps Build Them](https://arxiv.org/abs/2610.33851v1)**
  - *Amir M. Ebrahimi, Mohammed Mehedi Hasan, Seyed Shayan Daneshvar et al.*
  - `2026-10-24`
  - Software engineering (SE) expertise can shape how coding large language models (LLMs) are trained and which engineering capabilities they acquire. We examine this role through an industrial case study of capability-focused training for a 92B-parameter coding LLM serving more than…

- **[Benchmarking System One Models for Time-Series Decision Making: A Case Study of Jev](https://arxiv.org/abs/2610.33410v1)**
  - *Jianye Wang, Kexin Zhang, Jiayin Xiong et al.*
  - `2026-10-24`
  - Time-series tasks require both accurate predictions and fast decisions. Advances in large models have introduced decision-oriented models that directly output answers and their probabilities, which we call Structured System 1 models. Their applicability to time-series tasks remai…


## Finance  (155)

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


### ACL

- **[The Right Fact, the Wrong Decision: SciValidityBench for Scientific Agent Memory](https://arxiv.org/abs/2610.34767v1)**
  - *Yuexi Pan, Yongchao Chen*
  - **ACL** · `2026-10-26`
  - Most agent-memory benchmarks frame long-term memory as retrieval: can an agent recover the relevant record from a long and evolving history? Scientific agents face a stricter problem: a correctly remembered fact may still be invalid to use. The same reported test result can suppo…

- **[How Do Small Coding Agents Use Code Graphs and Embeddings?](https://arxiv.org/abs/2610.33958v1)**
  - *Saurav Bellam*
  - **ACL** · `2026-10-25`
  - Coding agents are given embedding search and code-graph tools on the premise that a repository's structure is something the model lacks and the tool supplies. We test that premise on SWE-bench Verified with small open-weight models, stratifying tasks by a deterministic hop depth…

- **[Implicit Beliefs as Scalable Process Rewards for Strategic Persuasion](https://arxiv.org/abs/2610.33527v1)**
  - *Minqian Liu, Yuexi Shen, Heajun An et al.*
  - **ACL** · `2026-10-24`
  - Training large language models (LLMs) for multi-turn strategic persuasion faces two coupled obstacles: (i) realistic simulation of psychologically grounded persuadees, and (ii) dense, faithful supervision for credit assignment in strategic dialogues. Outcome-only rewards are spar…


### IJCAI

- **[Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition](https://arxiv.org/abs/2610.34777v1)**
  - *Weihang Niu, Mengxing Ren, Che Qu*
  - **IJCAI** · `2026-10-26`
  - This paper introduces Scope-Gap Injection (SGI), an indirect prompt injection method for multi-stage LLM-agent safety pipelines. In the IJCAI 2026 OpenClaw Agent Security Attack Competition, each attack package is judged by a static skill scan (S1), an LLM-judge safety check over…


### Other / arXiv

- **[Skill^{infty}: Recursive Self-Improvement for Agent Skill Optimization](https://arxiv.org/abs/2610.35434)**
  - *Wangcheng Tao, Zhanglu Yan, Han Wu et al.*
  - 🤗 Featured · `2026-10-26`
  - Recursive self-improvement (RSI), in which a system also improves the way it improves, is a long-standing aspiration on the path to AGI. Language agents increasingly store procedural knowledge in reusable skills. Optimizing skills offers a direct way to achieve RSI, because the o…

- **[Thinking-in-Bets at Test Time Reduces Sycophantic Revisions in LLM Agents](https://arxiv.org/abs/2610.34654)**
  - *Nghi D. Q. Bui*
  - 🤗 Featured · `2026-10-26`
  - Language model agents often abandon correct work when a user challenges it, yet simply telling them to stand firm makes them ignore real mistakes. Once an agent reads a complaint, it tends to discount its own earlier checks in order to agree with the user. We introduce Thinking-i…

- **[DynaFlow: Learning Free-Form Multi-Agent Orchestration](https://arxiv.org/abs/2610.34467)**
  - *Ruhao Liu, Qi Li, Shizun Wang et al.*
  - 🤗 Featured · `2026-10-25`
  - Multi-agent systems often rely on predefined collaboration structures, limiting their ability to adapt to diverse task requirements. We introduce DynaFlow, a framework that integrates free-form executable workflow synthesis into the action space of the main agent. The agent decid…

- **[AgentProofBench: Benchmarking Reusable Verifiers for Web Agents](https://arxiv.org/abs/2610.34634)**
  - *Jingjie Ning, Xueqi Li, Yi Lu et al.*
  - 🤗 Featured · `2026-10-25`
  - Reusable Web-agent verification requires a rule to follow changing requirements and support subsequent execution. We introduce AgentProofBench, which connects paired tests of a frozen acceptance rule to execution from identical saved openings. The resource spans 97 tasks, 79 fami…

- **[Harness-Model Collaboration for Long-Horizon Continual Learning](https://arxiv.org/abs/2610.34724)**
  - *Zhen Bi, Zhizhi Peng, Yan Wang et al.*
  - 🤗 · `2026-10-26`
  - Long-horizon agents continuously encounter reusable procedural knowledge, yet existing systems typically rely either on model adaptation or external memory, trading persistent learning for rapid reuse. This limitation is especially important for Web agents that repeatedly execute…

- **[RobotAgentBench: Towards Open-world Robot Autonomy](https://arxiv.org/abs/2610.34649)**
  - *Lingjun Mao, Jinglin Cao, Lukun He et al.*
  - 🤗 · `2026-10-26`
  - Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm fo…

- **[I-HITL: Inalienable Human-in-the-Loop](https://arxiv.org/abs/2610.35835v1)**
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

- **[Agentic Algorithm Design: LLMs that Propose, Formalise, and Prove Runtime Bounds for Evolutionary Algorithms in Lean](https://arxiv.org/abs/2610.35595v1)**
  - *Per Kristian Lehre*
  - `2026-10-26`
  - LLMs now prove hard theorems in Lean. Can they also design algorithms and prove their correctness and efficiency? LLM-guided design of optimisation heuristics (such as AlphaEvolve) is purely empirical. Automated theorem provers with LLMs prove given statements. So far, there has…

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

- **[From Questions to Queries to Insights: A Schema-Grounded Agentic Workflow for Natural-Language Crash Data Analysis](https://arxiv.org/abs/2610.35054v1)**
  - *Jingwen Zhu, Keshu Wu, Steven T. Parker et al.*
  - `2026-10-26`
  - Transportation agencies maintain extensive crash databases to identify safety priorities, evaluate countermeasures, and guide resource allocation. Making these data accessible to practitioners requires flexible ways to translate analytical questions into reliable results. Existin…

- **[Heard Enough to Act: Early Tool Calling in Spoken Dialogue Systems](https://arxiv.org/abs/2610.34653v1)**
  - *Yizhou Peng, Chen Chen, Donghang Wu et al.*
  - `2026-10-26`
  - Latency-sensitive spoken agents must know not only which tool to call, but also when they have heard enough to act. Waiting for the turn to complete delays execution even when the request is already actionable. However, neither existing spoken agents nor spoken dialogue corpora d…

- **[LLM-Enhanced Heterogeneous Graph Learning with Business Semantics for Financial Fraud Detection](https://arxiv.org/abs/2610.35298v1)**
  - *Yixuan Chen, Hongyu Zhan, Jie Sheng et al.*
  - `2026-10-26`
  - Financial fraud detection increasingly relies on heterogeneous transaction graphs, in which entities such as cards and merchants play distinct business roles and the risk meaning of an attribute depends on the entity's role: a high transaction volume may be routine for a merchant…

- **[Arya Forge: Auditing Validation and Release Approval for Financial Instruction Data](https://arxiv.org/abs/2610.34778v1)**
  - *Kushagra Bhatnagar, Deekshith Marla*
  - `2026-10-26`
  - Financial instruction-data pipelines must distinguish content validity from permission to release a particular dataset. Arya Forge combines typed records, current-content checks, and approval coverage bound to a dataset manifest. We evaluate its release boundaries in a financial-…

- **[MINT: Mitigating Structural Inconsistency via Attentive Message Passing for Financial Anomaly Detection](https://arxiv.org/abs/2610.34950v1)**
  - *Yin-Ju Wu, Bi-Cheng Yan, Berlin Chen*
  - `2026-10-26`
  - Illicit account detection is a critical task for financial risk control systems, aiming to pinpoint malicious actors within transaction networks. Existing efforts typically recast transaction networks into directed multigraphs and leverage graph neural networks (GNNs) to detect a…

- **[Patient-specific rubric-based evaluation of large language models across longitudinal cancer care](https://arxiv.org/abs/2610.35847v1)**
  - *Wei-Wei Zhang, Pengkai Wang, Yan Li et al.*
  - `2026-10-26`
  - Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rather than tracking how clinical responsibilities evolve across a longitudinal care pathway. Here we introduce NPC-RubricBench, a phase-aware b…

- **[Balanced Sampling in Stochastic Multi-objective Bandits](https://arxiv.org/abs/2610.35551v1)**
  - *Mengfan Xu*
  - `2026-10-26`
  - In stochastic multi-objective bandits, Pareto optimal arms may represent different trade-offs among objectives. Balanced sampling across them is important in practical settings such as online advertising. Yet, there seems to be little consensus on how to measure fairness, to our…

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

- **[What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents](https://arxiv.org/abs/2610.34491v1)**
  - *Kaiser Sun, Yongchan Kwon, Zain Hasan et al.*
  - `2026-10-25`
  - Generative models increasingly expose a reasoning effort setting that lets users scale inference-time compute, trading higher cost for potentially improved performance. Users must choose an effort level before knowing whether extra reasoning will help, and even a successful run d…

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

- **[Models Verify Sufficiency, Not Validity: Usable Falsehoods Evade the Checks that Gaps Trigger](https://arxiv.org/abs/2610.34488v1)**
  - *Naveen Madiraju*
  - `2026-10-25`
  - Ask a model "how many settlements did the Normans control?" and it answers that the passage does not say. Tell it "given that the Normans controlled 12 settlements of 400 inhabitants, what is the total?" and it computes 4,800. Nothing was added to the passage; the unsupported fac…

- **[Reversion, Retention, and Semantic Intervention: Measuring Functional Content in CLIP Fine-Tuning Deltas](https://arxiv.org/abs/2610.34144v1)**
  - *Chih-Ting Liao, Kezhen Bao, Xin Cao*
  - `2026-10-25`
  - Fine-tuning adapts pretrained models to new tasks, but identifying which weight changes support the resulting behavior remains difficult. Weight-space interpretability assigns semantic descriptions to these changes, called fine-tuning deltas. Such descriptions leave open how much…

- **[Certifying Reward Alignment in Portfolio Reinforcement Learning](https://arxiv.org/abs/2610.34153v1)**
  - *Matin Tavakoli, Seyedreza Tavakoli, Faezeh Salmani et al.*
  - `2026-10-25`
  - Financial reinforcement learning often translates an investment objective into an additive risk-adjusted reward. An agent can optimise that reward accurately yet implement a different financial preference. We develop a decision audit for terminal mean-variance equilibrium that se…

- **[Intrinsic Gradient Barriers in Pushforward Deep Generative Models](https://arxiv.org/abs/2610.34484v1)**
  - *Edric Tam, Qingyang Liu, Barbara Engelhardt et al.*
  - `2026-10-25`
  - Broad classes of deep generative models (DGMs) operate by learning to map a simple source distribution, such as a standard Gaussian, to a complex high-dimensional target distribution. Despite their success, DGMs often empirically struggle to accurately represent distributions wit…

- **[EnvLunch: The Environment as a Free Lunch for Learning to Interact](https://arxiv.org/abs/2610.33817v1)**
  - *Wei Liu, Min Gao, Yali Du et al.*
  - `2026-10-24`
  - For agentic data analysis, language-model agents often require a large number of annotated tasks to learn how to interact effectively with executable environments (i.e., databases). While high-quality annotated tasks require heavy manual effort, an executable environment already…

- **[RSI Arena: Towards Recursive Self-Improvement with Human Feedback](https://arxiv.org/abs/2610.33624v1)**
  - *Yue Huang, Yanbo Wang, Lichi Li et al.*
  - `2026-10-24`
  - Can AI agents autonomously train useful language models and improve them using feedback from users? We introduce RSI Arena, a two-stage study of autonomous post-training as a step toward recursive self-improvement. Ten frontier models act as training agents, each starting from NV…

- **[FraudSociety: A Generative Agent-Based Society for the Financial-Fraud Economy](https://arxiv.org/abs/2610.33536v1)**
  - *Keyang Chen, Mingxuan Jiang, Zeping Li et al.*
  - `2026-10-24`
  - Financial fraud caused over \$15.9 billion in losses in the United States in 2025, according to the Federal Trade Commission~\citep{ftc2026databook}. Understanding such large-scale harm requires jointly modeling informational and financial dynamics. Yet existing simulators typica…

- **[LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference](https://arxiv.org/abs/2610.33475v1)**
  - *Jannatun Noor, Athar Noor Mohammad Rafee, Md. Sadman Haque et al.*
  - `2026-10-24`
  - The widespread deployment of foundational Large Language Models (LLM) across cloud datacenters marks a fundamental paradigm shift from stateless deep learning toward distributed, memory-intensive generative workloads. However, serving massive foundation models under stringent Ser…

- **[Software Engineering LLMs: Why We Need Them and How Software Engineering Helps Build Them](https://arxiv.org/abs/2610.33851v1)**
  - *Amir M. Ebrahimi, Mohammed Mehedi Hasan, Seyed Shayan Daneshvar et al.*
  - `2026-10-24`
  - Software engineering (SE) expertise can shape how coding large language models (LLMs) are trained and which engineering capabilities they acquire. We examine this role through an industrial case study of capability-focused training for a 92B-parameter coding LLM serving more than…

- **[From Intelligence to Autonomy: Foundations and Construction of Autonomous Agents for Future Intelligent Systems](https://arxiv.org/abs/2610.33445v1)**
  - *Hongda Zhang, Ziqing Zhou, Yuning Chen et al.*
  - `2026-10-24`
  - Artificial intelligence is moving from one-off perception and generation tasks toward long-term planning, tool use, and interaction with real environments. Greater task competence, however, does not automatically yield autonomy: an external actor may still have to set goals, sust…

- **[Agent-to-Agent Synthetic Social Engineering on the Web](https://arxiv.org/abs/2610.33411v1)**
  - *Bryan C. Boots*
  - `2026-10-24`
  - An AI agent can prepare an accurate report and still request an action its user has not authorized. Cooperation across Web services therefore requires separate judgments about identity, evidentiary support, and permission. We define synthetic social engineering (SSE) as deliberat…

- **[Geodesic-SVDD Latent Mixup for One-Shot Distributed Tabular Learning](https://arxiv.org/abs/2610.33619v1)**
  - *Andrea Moleri, Christian Internò, Markus Olhofer et al.*
  - `2026-10-24`
  - Distributed Learning on structured data is a key and widely adopted approach in privacy-sensitive sectors, ranging from financial fraud prevention to federated healthcare diagnostics. While Gradient Boosted Decision Trees are widely used in centralized settings due to their effic…

- **[Cross-Bond Panel Learning for Next-Day Price Forecasting of Chinese Convertible Bonds: A Reality Check](https://arxiv.org/abs/2610.33453v1)**
  - *Derun Zhong, Guolian Wang, Shiqing Wang et al.*
  - `2026-10-24`
  - Recent advances in financial machine learning have prompted growing interest in applying deep neural networks to convertible bond valuation and forecasting. However, existing studies often focus on in-sample valuation fit or cross-sectional return rankings, leaving out-of-sample…

- **[Tracking High-Frequency Trading Activity in China and Its Effects on Market Quality](https://arxiv.org/abs/2610.33400v1)**
  - *Li Guo, Frank Weikai Li, Ding Qi et al.*
  - `2026-10-24`
  - We develop a new order-level proxy for high-frequency trading (HFT) activity based on precise order placement and study its effects on market quality. With quotes updating multiple times per second, millisecond-level order-book access makes high-frequency traders more likely to s…

- **[Compiling and forecasting implied volatility surfaces via survey sampling, tempered inverse-probability sequence learning, and causal activity clocks](https://arxiv.org/abs/2610.33438v1)**
  - *Deepak Bastola, Eli Prushansky*
  - `2026-10-24`
  - Compiling implied volatility (IV) surfaces and forecasting derivative risk from high-frequency equity and options feeds requires addressing contract heterogeneity, schema shifts, volatility clustering, and non-stationary trading activity. Using a split-adjusted NVIDIA (NVDA) equi…

- **[Tokenised Sukuk: A Verifiable Architecture for Asset Evidence and Programmable Shariah Compliance](https://arxiv.org/abs/2610.33538v1)**
  - *Rischan Mafrur, Khadijah, Gun Gun Febrianza*
  - `2026-10-24`
  - Security-token standards such as ERC-3643 decide who may hold a token, not what stands behind it. For a sukuk this gap matters: whether a certificate may trade at a negotiated price depends on what its portfolio contains, and a token that checks only investor identity keeps tradi…

- **[Optimal portfolio choice under green transition timing risk](https://arxiv.org/abs/2610.33597v1)**
  - *Emma Kroell, Mogens Steffensen*
  - `2026-10-24`
  - We study an investor's optimal portfolio choice problem when they account for the impact of a possible future green transition, whose timing is uncertain. We model the green transition as a discontinuity in the stock price processes, driven by a single jump process with constant…


---
*Generated 2026-10-27 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
