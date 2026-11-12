# Daily Paper Digest — 2026-11-12 (Thursday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**409 unique papers** (518 topic-entries — cross-topic papers counted once per category)

---

## Agent  (282)

### AAAI

- **[Exploring the Efficacy of Multi-Agent Reinforcement Learning for Autonomous Cyber Defence: A CAGE Challenge 4 Perspective](https://doi.org/10.1609/aaai.v39i28.35158)**
  - *Mitchell Kiely, Metin B. Ahiskali, E. Borde et al.*
  - **AAAI 2025** · `2025-04-11`
  - As cyber threats become increasingly automated and sophisticated, novel solutions must be introduced to improve defence of enterprise networks. Deep Reinforcement Learning (DRL) has demonstrated potential in mitigating these advanced threats. Single DRL Agents have proven utility…

- **[OpenDriveVLA: Towards End-to-end Autonomous Driving with Large Vision Language Action Model](https://arxiv.org/abs/2503.23463)**
  - *Xingcheng Zhou, Xu Han, Feng Yang et al.*
  - **AAAI 2025** · `2025-03-30`
  - We present OpenDriveVLA, a Vision-Language Action (VLA) model designed for end-to-end autonomous driving, built upon open-source large language models. OpenDriveVLA generates spatially-grounded driving actions by leveraging multimodal inputs, including both 2D and 3D instance-awa…


### NeurIPS

- **[AutoManifold: Agentic Design of Data Visualisation Algorithms via Manifold Embedding](https://arxiv.org/abs/2611.13710v1)**
  - *Burak Susam, Ruiyuan Kang, Tingting Mu*
  - **NeurIPS** · `2026-11-10`
  - Manifold embedding for data visualisation is dominated by a small set of hand-designed state-of-the-art (SOTA) algorithms. Their design targets are fixed at development time, resulting in inflexible algorithmic behaviour that cannot be readily steered towards user-specified struc…

- **[WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648)**
  - *Jia-Long Wu, Bai-Xuan Li, Run-Nan Fang et al.*
  - **NeurIPS 2025** · `2025-05-28`
  - Addressing intricate real-world problems necessitates in-depth information seeking and multi-step reasoning. Recent progress in agentic systems, exemplified by Deep Research, underscores the potential for autonomous multi-step research. In this work, we present a cohesive paradig…

- **[STRATUS: A Multi-agent System for Autonomous Reliability Engineering of Modern Clouds](https://arxiv.org/abs/2506.02009)**
  - *Yin-Fang Chen, Jia-Qi Pan, Jackson Clark et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - In cloud-scale systems, failures are the norm. A distributed computing cluster exhibits hundreds of machine failures and thousands of disk failures; software bugs and misconfigurations are reported to be more frequent. The demand for autonomous, AI-driven reliability engineering…

- **[AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/abs/2503.09780)**
  - *A. Zharmagambetov, Chuan Guo, I. Evtimov et al.*
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

- **[RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](https://arxiv.org/abs/2501.18160)**
  - *Jin-Yao Guo, Cheng-Peng Wang, Xiang-Zhe Xu et al.*
  - **ICML 2025** · `2025-01-30`
  - Code auditing is the process of reviewing code with the aim of identifying bugs. Large Language Models (LLMs) have demonstrated promising capabilities for this task without requiring compilation, while also supporting user-friendly customization. However, auditing a code reposito…

- **[The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://www.semanticscholar.org/paper/d67976e4cd3ddc541172455c854c2be76d15baae)**
  - *Shishir G. Patil, Huan-Zhi Mao, Fanjia Yan et al.*
  - **ICML 2025**


### ICLR

- **[Can Frontier Auto Researchers Reconstruct Human Research Decisions in AI?](https://arxiv.org/abs/2611.12429v1)**
  - *Shengyun Si, Junjie Chu, Ye Leng et al.*
  - **ICLR** · `2026-11-09`
  - Scientific research has long been driven by substantial human effort, from reviewing prior work and identifying research gaps to designing specific solutions. Recent advances in harness-based agent systems have given rise to increasingly capable Auto Researchers, which can autono…

- **[STAR: Similarity-guided Teacher-Assisted Refinement for Super-Tiny Function Calling Models](https://arxiv.org/abs/2602.03022)**
  - *Jiliang Ni, Jiachen Pu, Zhongyi Yang et al.*
  - **ICLR 2026** · `2026-02-03`
  - The proliferation of Large Language Models (LLMs) in function calling is pivotal for creating advanced AI agents, yet their large scale hinders widespread adoption, necessitating transferring their capabilities into smaller ones. However, existing paradigms are often plagued by o…

- **[Towards Reliable Benchmarking: A Contamination Free, Controllable Evaluation Framework for Multi-step LLM Function Calling](https://arxiv.org/abs/2509.26553)**
  - *Seiji Maekawa, Jackson Hassell, Pouya Pezeshkpour et al.*
  - **ICLR 2025** · `2025-09-30`
  - Existing benchmarks for tool-augmented language models (TaLMs) lack fine-grained control over task difficulty and remain vulnerable to data contamination. We present FuncBenchGen, a unified, contamination-free framework that evaluates TaLMs by generating synthetic multi-step tool…

- **[DriveTransformer: Unified Transformer for Scalable End-to-End Autonomous Driving](https://arxiv.org/abs/2503.07656)**
  - *Xiao-Song Jia, Jun-Qi You, Zhi-Yuan Zhang et al.*
  - **ICLR 2025** · `2025-03-07`
  - End-to-end autonomous driving (E2E-AD) has emerged as a trend in the field of autonomous driving, promising a data-driven, scalable approach to system design. However, existing E2E-AD methods usually adopt the sequential paradigm of perception-prediction-planning, which leads to…


### CVPR

- **[An LLM-Enabled Multi-Agent Autonomous Mechatronics Design Framework](https://arxiv.org/abs/2504.14681)**
  - *Ze-Yu Wang, Frank P.-W. Lo, Qian Chen et al.*
  - **CVPR 2025** · `2025-04-20`
  - Existing LLM-enabled multi-agent frameworks are predominantly limited to digital or simulated environments and confined to narrowly focused knowledge domain, constraining their applicability to complex engineering tasks that require the design of physical embodiment, cross-discip…


### ACL

- **[From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses](https://arxiv.org/abs/2611.13960v1)**
  - *Simon Hegelich, Bardh Prenkaj, Habiba Sarhan et al.*
  - **ACL** · `2026-11-10`
  - AI coding harnesses couple language models to shells, filesystems, and network sockets, turning the harness into an automated Living-off-the-Land (LotL) platform: once an adversary injects instructions into retrieved content, dual-use binaries such as bash, curl, and find become…

- **[Megrez: A Knowledge-Guided Agent for Formal Mathematics over MK Set Theory](https://arxiv.org/abs/2611.13613v1)**
  - *Tiancheng Xu, Wensheng Yu*
  - **ACL** · `2026-11-10`
  - General-purpose coding agents equipped with proof-assistant tools have shown strong performance on standalone competition problems, yet cumulative textbook formalization inside a low-resource mathematical library still faces three obstacles: aligning textbook concepts with librar…

- **[Reliability of Claude Code as an Agentic AI Grading System for Handwritten University Exams](https://arxiv.org/abs/2611.13217v1)**
  - *Rayed AlGhamdi*
  - **ACL** · `2026-11-09`
  - This study examines the reliability of Claude Code, an agentic deployment of the Claude Opus 4.6 large language model, as a grading system for handwritten university exams. Four research questions addressed agreement with expert human grading on total scores (RQ1), agreement acro…

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

- **[MIRIX-2.0: Multi-Agent Memory System](https://arxiv.org/abs/2611.12068v1)**
  - *Wei-Chieh Huang, Weizhi Zhang, Jiayan Nan et al.*
  - **ACL** · `2026-11-09`
  - Long-term memory lets LLM agents personalize, stay consistent, and reuse what worked before. Parametric memories need training, consolidation can lose details for good, and keeping every record leaves a growing store to search. We present MIRIX-2.0, a multi-agent memory system de…

- **[R2IF: Aligning Reasoning with Decisions via Composite Rewards for Interpretable LLM Function Calling](https://arxiv.org/abs/2604.20316)**
  - *A. Cheng, Kai-Long Wang, Ling Shi et al.*
  - **ACL 2026** · `2026-04-22`
  - Function calling empowers large language models (LLMs) to interface with external tools, yet existing RL-based approaches suffer from misalignment between reasoning processes and tool-call decisions. We propose R2IF, a reasoning-aware RL framework for interpretable function calli…

- **[GenesisFunc: Multi-Agent Data Generation for Accurate and Generalizable Function-Calling](https://arxiv.org/abs/2605.28835)**
  - *Hao-Ming Xu, Chong Deng, Jia-Qing Liu et al.*
  - **ACL 2026** · `2026-04-10`
  - Large Language Models (LLMs) extend their capabilities through function-calling (FC), which relies on training data with high quality, diversity, and broad coverage of scenario. However, obtaining and annotating real function-calling data is challenging, while synthetic data from…

- **[Temp-R1: A Unified Autonomous Agent for Complex Temporal KGQA via Reverse Curriculum Reinforcement Learning](https://arxiv.org/abs/2601.18296)**
  - *Zhaoyan Gong, Zhi-Qiang Liu, Song-Ze Li et al.*
  - **ACL 2026** · `2026-01-26`
  - Temporal Knowledge Graph Question Answering (TKGQA) is inherently challenging, as it requires sophisticated reasoning over dynamic facts with multi-hop dependencies and complex temporal constraints. Existing methods rely on fixed workflows and expensive closed-source APIs, limiti…

- **[MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive and MCP-Augmented Environments](https://arxiv.org/abs/2512.19432)**
  - *Qu-Yu Kong, Xu Zhang, Zhen-Yu Yang et al.*
  - **ACL 2025** · `2025-12-22`
  - Among existing online mobile-use benchmarks, AndroidWorld has emerged as the dominant benchmark due to its reproducible environment and deterministic evaluation; however, recent agents achieving over 90% success rates indicate its saturation and motivate the need for a more chall…

- **[Dynamic Tool Dependency Retrieval for Lightweight Function Calling](https://arxiv.org/abs/2512.17052)**
  - *Bhrij Patel, Davide Belli, Amir Jalalirad et al.*
  - **ACL 2025** · `2025-12-18`
  - Function calling agents powered by Large Language Models (LLMs) select external tools to automate complex tasks. On-device agents typically use a retrieval module to select relevant tools, improving performance and reducing context length. However, existing retrieval methods rely…

- **[ToolPRM: Fine-Grained Inference Scaling of Structured Outputs for Function Calling](https://arxiv.org/abs/2510.14703)**
  - *Jianghao Lin, Yuanyuan Shi, Xin Peng et al.*
  - **ACL 2025** · `2025-10-16`
  - Large language models (LLMs) excel at function calling, but inference scaling has been explored mainly for unstructured generation. We propose an inference-scaling framework for structured outputs that combines fine-grained beam search with \textbf{ToolPRM}, a process reward mode…

- **[Enhancing LLM Function Calling with Structured Outputs](https://www.semanticscholar.org/paper/a69e3e16054fa053bab743bf8fc8354a08b9636f)**
  - *Kevin Séjourné, A. Lata*
  - **ACL 2025** · `2025-08-18`
  - Large Language Models (LLMs) are increasingly used for function calling, typically by prompting the model to generate a specific format. This paper proposes an alternative approach leveraging structured outputs to enforce the desired format. This method offers several advantages,…

- **[CONFETTI: Conversational Function-Calling Evaluation Through Turn-Level Interactions](https://arxiv.org/abs/2506.01859)**
  - *Tamer Alkhouli, Katerina Margatina, James Gung et al.*
  - **ACL 2025** · `2025-06-02`
  - We introduce Conversational Function-Calling Evaluation Through Turn-Level Interactions (CONFETTI), a conversational benchmark1 designed to evaluate the function-calling capabilities and response quality of large language models (LLMs). Current benchmarks lack comprehensive asses…

- **[GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://arxiv.org/abs/2505.16827)**
  - *Bin Xie, Rui Shao, Gong-Wei Chen et al.*
  - **ACL 2025** · `2025-05-22`
  - GUI automation faces critical challenges in dynamic environments. MLLMs suffer from two key issues: misinterpreting UI components and outdated knowledge. Traditional fine-tuning methods are costly for app-specific knowledge updates. We propose GUI-explorer, a training-free GUI ag…

- **[Meta-Tool: Unleash Open-World Function Calling Capabilities of General-Purpose Large Language Models](https://aclanthology.org/2025.acl-long.1481.pdf)**
  - *Sheng-Qian Qin, Ya-Kun Zhu, Lin-Jie Mu et al.*
  - **ACL 2025**
  - Large language models (LLMs) have show-cased remarkable capabilities as autonomous agents when augmented with external tools. Equipped with fixed tool sets, LLMs struggle with addressing diverse user inquiries in open-world tasks. To evaluate and boost the performance of LLMs in…

- **[RAGthoven at SemEval 2025 - Task 2: Enhancing Entity-Aware Machine Translation with Large Language Models, Retrieval Augmented Generation and Function Calling](https://www.semanticscholar.org/paper/9259321c507460c5a9989d3b5fff910d99469159)**
  - *Demetris Skottis, Gregor Karetka, Marek Suppa*
  - **ACL 2025**

- **[Progra: Progress-Aware Reinforcement Learning for Multi-Turn Function Calling](https://aclanthology.org/2026.findings-acl.325.pdf)**
  - *Hua-Can Chai, Zi-ang Cao, Mao-Lin Ran et al.*
  - **ACL 2026**
  - Real-world tasks with Large Language Models (LLMs) require multi-turn, multi-step conversations, often involving complex function calls and multiple user interactions. Existing methods either decompose multi-turn trajectories into independent single samples, neglecting task-level…

- **[BalanceSFT: Improving LLM Function Calling with Balanced Training Signals and Data Hardness](https://aclanthology.org/2026.findings-acl.900.pdf)**
  - *Bing-Guang Hao, Zeng-Zhuang Xu, Mao-Lin Wang et al.*
  - **ACL 2026**
  - ,


### EMNLP

- **[Extending FunctionGemma for Practical On-Device Mobile Function Calling](https://arxiv.org/abs/2609.25373)**
  - *Ali Rezagholizadeh, Soheila Samiee*
  - **EMNLP 2026** · `2026-09-21`
  - On-device assistants require function-calling models that map natural language to local system actions, but existing resources emphasize web APIs or narrow mobile-action catalogs. We extend FunctionGemma 270M-it to practical Android workflows by introducing MOBILEACTIONSEXTENDED,…

- **[Attributing Structured-Output Gains in Function Calling: Interface Alignment versus Procedural Transfer](https://arxiv.org/abs/2607.02595)**
  - *Wan-Yi Chen, Dao-Yuan Chen, Fang Kong*
  - **EMNLP 2026** · `2026-07-01`
  - Structured-output benchmarks reward both task decisions and interface compliance, so prompt-induced function-calling gains require attribution before they can be interpreted as transferable skill. We introduce a four-layer gain-attribution protocol for prompt-prepended skill inje…

- **[AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios](https://arxiv.org/abs/2605.27995)**
  - *Kou Shi, Ziao Zhang, Shi-Ting Huang et al.*
  - **EMNLP 2026** · `2026-05-27`
  - Large language model (LLM)-based agents have shown strong capabilities in using external tools to solve complex tasks. However, existing evaluations often overlook the temporal dimension of tool use, especially the impact of tool response latency, and are usually limited to singl…

- **[PaperScout: An Autonomous Agent for Academic Paper Search with Process-Aware Sequence-Level Policy Optimization](https://arxiv.org/abs/2601.10029)**
  - *Ting-Yue Pan, Jie Ouyang, Ming-Yue Cheng et al.*
  - **EMNLP 2026** · `2026-01-15`
  - Academic paper search is a fundamental task in scientific research, yet most existing approaches organize retrieval around predefined workflows or structured interaction protocols that struggle with complex, conditional queries. To address this limitation, we propose PaperScout,…

- **[Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates](https://arxiv.org/abs/2509.18076)**
  - *Hy Dang, Tianyi Liu, Zhuofeng Wu et al.*
  - **EMNLP 2025** · `2025-09-22`
  - Large language models (LLMs) have demonstrated strong reasoning and tool-use capabilities, yet they often fail in real-world tool-interactions due to incorrect parameterization, poor tool selection, or misinterpretation of user intent. These issues often stem from an incomplete u…

- **[Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall](https://arxiv.org/abs/2508.15214)**
  - *Sijia Cui, Aiyao He, Shuai Xu et al.*
  - **EMNLP 2025** · `2025-08-21`
  - Function calling enables large language models (LLMs) to interact with external systems by leveraging tools and APIs. When faced with multi-step tool usage, LLMs still struggle with tool selection, parameter generation, and tool-chain planning. Existing methods typically rely on…

- **[Multi-Agent Autonomous Driving Systems with Large Language Models: A Survey of Recent Advances](https://arxiv.org/abs/2502.16804)**
  - *Yaozu Wu, Dong-Yuan Li, Yan-Kai Chen et al.*
  - **EMNLP 2025** · `2025-02-24`
  - Autonomous Driving Systems (ADSs) are revolutionizing transportation by reducing human intervention, improving operational efficiency, and enhancing safety. Large Language Models (LLMs) have been integrated into ADSs to support high-level decision-making through their powerful re…

- **[Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)**
  - *Samuel Schmidgall, Yu-Sheng Su, Ze Wang et al.*
  - **EMNLP 2025** · `2025-01-08`
  - Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory, an…

- **[MASSIVE-Agents: A Benchmark for Multilingual Function-Calling in 52 Languages](https://aclanthology.org/2025.findings-emnlp.1099.pdf)**
  - *Mayank Kulkarni, Vittorio Mazzia, J. Gaspers et al.*
  - **EMNLP 2025**
  - ,

- **[DispatchQA: A Benchmark for Small Function Calling Language Models in E-Commerce Applications](https://aclanthology.org/2025.emnlp-industry.154.pdf)**
  - *Joachim Daiber, Victor Maricato, Ayan Sinha et al.*
  - **EMNLP 2025**
  - We introduce DispatchQA , a benchmark to evaluate how well small language models (SLMs) translate open-ended search queries into executable API calls via explicit function calling . Our benchmark focuses on the latency-sensitive e-commerce setting and measures SLMs’ impact on bot…


### NAACL

- **[CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://arxiv.org/abs/2501.16609)**
  - *Faria Huq, Zora Zhiruo Wang, Frank F. Xu et al.*
  - **NAACL 2025** · `2025-01-28`
  - While much work on web agents emphasizes the promise of autonomously performing tasks on behalf of users, in reality, agents often fall short on complex tasks in real-world contexts and modeling user preference. This presents an opportunity for humans to collaborate with the agen…


### Other / arXiv

- **[SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://arxiv.org/abs/2611.13410)**
  - *Genming Cui, Xiangyu Li, Zixu Hao et al.*
  - 🤗 Featured · `2026-11-10`
  - Low-bit quantization reduces the inference cost of LLM agents but can compromise task success. Examining failed rollouts, we find that quantized agents overlook task requirements or environmental conditions, producing environment transitions that diverge from successful full-prec…

- **[ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping](https://arxiv.org/abs/2611.11306)**
  - *Joseph Marvin Imperial, Daniel Slate, Noam Kolt*
  - 🤗 Featured · `2026-11-10`

- **[GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning](https://arxiv.org/abs/2611.13028)**
  - *Jiajun Chen, Shicheng Fang, Jiahao Lu et al.*
  - 🤗 Featured · `2026-11-09`
  - AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA games is challenging and often human-annotated because task outcomes are often difficult to verify automatically, let alone applyin…

- **[Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304)**
  - *Hao Kang, Weili Xu, Ziyang Li et al.*
  - 🤗 Featured · `2026-11-09`

- **[Read Less, Solve More: Token-Efficient Sparse Reading of External Content for AI Agents](https://arxiv.org/abs/2608.22237)**
  - *Zedong Liu, Jiaan Wu, Xinyang Ma et al.*
  - 🤗 Featured · `2026-11-07`

- **[ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows](https://arxiv.org/abs/2611.14492)**
  - *Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya et al.*
  - 🤗 · `2026-11-10`
  - Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scal…

- **[One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge](https://arxiv.org/abs/2611.14432)**
  - *Ilia Larchenko, Gleb Zarin, Atindra Nair et al.*
  - 🤗 · `2026-11-10`
  - We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one ch…

- **[Earlybird: Predictive Streaming Speech Recognition in 29M Parameters](https://arxiv.org/abs/2611.14421)**
  - *Sahil Mahendrakar*
  - 🤗 · `2026-11-10`
  - Streaming speech recognizers output a word only after the speaker has finished it, typically 90-400 ms later. For a voice agent every millisecond counts: the sooner the words are outputted, the sooner the agent can start a search or plan its reply. We present Earlybird, a 29M-par…

- **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)**
  - *Yukyeong Lee, Yumin Choi, Jinheon Baek et al.*
  - 🤗 · `2026-11-10`
  - External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it fo…

- **[MMDM: Measuring Massive Multitask Decision Making](https://arxiv.org/abs/2611.14309)**
  - *Junhao Shen, Qing Zong, Yue Guo et al.*
  - 🤗 · `2026-11-10`
  - System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cover diverse tasks but often rely on…

- **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210)**
  - *Hadi Salloum, Ammar Ali*
  - 🤗 · `2026-11-10`
  - Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million toke…

- **[LEASH: Stay Safe in Agentic Robotics](https://arxiv.org/abs/2611.14115)**
  - *Qinfeng Zhu, Weiguang Zhao, Ke Sun et al.*
  - 🤗 · `2026-11-10`

- **[Coding Agent Memory Post-Training II: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via On-Policy Distillation](https://arxiv.org/abs/2611.14009)**
  - *Lirui Luo, Kelong Mao, Xinwei Yang et al.*
  - 🤗 · `2026-11-10`
  - Language-model agents increasingly tackle long-horizon tasks whose interaction histories exceed the model's active context. They must therefore decide what to write down and what to read back, and when to do either. Recent work has begun to use on-policy distillation (OPD) to mak…

- **[BioXArena-Pro: a research-grade benchmark for autonomous biomedical machine learning agents](https://arxiv.org/abs/2611.13994)**
  - *Loka Li, Duzhen Zhang, Xingbo Du et al.*
  - 🤗 · `2026-11-10`
  - Coding agents are increasingly proposed as autonomous builders of biomedical models, but existing benchmarks are small, near saturation or open to leaked information. We present BioXArena-Pro, 64 research-level modelling tasks from eight biomedical domains, each rebuilt from a pu…

- **[DisasterAgent: An Evidence-Driven Agent for Verifiable Disaster Report Generation From Remote Sensing Imagery](https://arxiv.org/abs/2611.13776)**
  - *Zhijian Li, Jiawei Song, Chao Ren et al.*
  - 🤗 · `2026-11-10`
  - Remote sensing disaster assessment is moving from simple damage classification toward comprehensive report-level analysis. In this setting, responders need not only damage descriptions but also verifiable evidence to guide response and recovery. Recent vision-language models (VLM…

- **[Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](https://arxiv.org/abs/2611.14514v1)**
  - *Ziang Liu, James J. Kim, Yijia Dai et al.*
  - `2026-11-10`
  - LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but…

- **[Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](https://arxiv.org/abs/2611.14493v1)**
  - *Howard Zhang, Chuck Arvin, Logan Brown et al.*
  - `2026-11-10`
  - Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation pa…

- **[Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning](https://arxiv.org/abs/2611.14419v1)**
  - *Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja et al.*
  - `2026-11-10`
  - Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generat…

- **[EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities](https://arxiv.org/abs/2611.14356v1)**
  - *Zhengxiang Huang, Yujie Sun, Shengheng Chen et al.*
  - `2026-11-10`
  - Rapidly evolving LLM architectures and heterogeneous mobile hardware make supporting new models in on-device inference engines a recurring and costly system challenge. Each model may require coordinated changes across conversion, graph construction, operators, and hardware backen…

- **[When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](https://arxiv.org/abs/2611.14326v1)**
  - *Runxuan Tang, Haoyu Gao, Yuyan Ding et al.*
  - `2026-11-10`
  - LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core…

- **[Lilo: A Multi-Agent Conversational Sandbox for Children's Digital Communication](https://arxiv.org/abs/2611.14260v1)**
  - *Ofri Elbaum, Amit Malik, Tomer Malkevich et al.*
  - `2026-11-10`
  - Children's peer conflicts increasingly play out in group chats, where tone and timing are stripped away, and a hurtful message is easier to send than to say aloud. We present Lilo, a multi-agent conversational system that lets children practice such conversations, so they are bet…

- **[A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents](https://arxiv.org/abs/2611.14256v1)**
  - *Jingjing Jiang*
  - `2026-11-10`
  - Recent work shows that multimodal agents increasingly self-improve without recurring human annotation. However, each self-improvement mechanism is designed and evaluated within a single scenario, leaving its preconditions unverified under cross-scenario transfer. This survey inve…

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

- **[Program-Aided Patchable Skill Evolution](https://arxiv.org/abs/2611.14019v1)**
  - *Jiahao Wang, Yuqi Xiong, Qing Yang et al.*
  - `2026-11-10`
  - Agent skills have emerged as an effective means of enabling LLM agents to solve complex, interactive tasks by encoding reusable knowledge without modifying model parameters. Recent approaches further improve skill adaptation by distilling reusable experience from agent execution…

- **[Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment](https://arxiv.org/abs/2611.14017v1)**
  - *Yupeng Han, Kai Zhang, Shuochen Liu et al.*
  - `2026-11-10`
  - Long-horizon personalized agents maintain an evolving memory by continuously deciding what to add, modify, or discard. However, learning an optimal update policy remains challenging. Conventional training relies solely on terminal question-answering accuracy, yielding a coarse fe…

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

- **[DrugCoding: A Scientific Programming Agent for Drug Discovery](https://arxiv.org/abs/2611.13651v1)**
  - *Junwei Hu, Zhuohao Lin, Kun Li et al.*
  - `2026-11-10`
  - Drug discovery involves multiple interconnected research stages, including molecular design, property prediction, and virtual screening. These processes are characterized by complex workflows, interdependent computational tasks, and diverse specialized tools, placing substantial…

- **[Synapse-Control: Making Agent Experience Actionable with Lightweight Runtime Control](https://arxiv.org/abs/2611.13615v1)**
  - *Zhiyuan Huang, Shengan Zheng, Chenghu Yang et al.*
  - `2026-11-10`
  - Large language model agents reuse execution experience to improve reliability on complex tool-based tasks. Systems such as Sentry call large models to generate failure diagnoses before retrieving advice, adding inference cost to experience reuse. We present Synapse-Control, an ag…

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

- **[Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511v1)**
  - *Megha Srivastava, Michael H. Lim, Allison M. Keys et al.*
  - `2026-11-10`
  - Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,50…

- **[Continual-ARC: Measuring Skill Acquisition over a Working Lifetime](https://arxiv.org/abs/2611.14505v1)**
  - *Daniel Lenton*
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

- **[Deep Personalization: Continuous Context Observation for Local Proactive Agents](https://arxiv.org/abs/2611.13457v1)**
  - *Yijia Shao, Song Bian, Junxian Guo et al.*
  - `2026-11-10`
  - As AI agents become increasingly capable, users must still recognize when and how to ask for help, leaving many opportunities for useful support unrealized. Proactive agents hold the promise to close this gap, but effective proactivity requires understanding users' real-time acti…

- **[Plumbline: When the Loss Lies, Validating LLM Training Correctly](https://arxiv.org/abs/2611.13393v1)**
  - *Ruochen Wen, Hongyang Wang, Siwei Li et al.*
  - `2026-11-10`
  - Correctness is a prerequisite for training large language models (LLMs) at scale, yet it is hard to ensure: a fault can sit in any part of a run, and how it shows differs across frameworks and the libraries they depend on. Some failures are loud and some are silent, and both take…

- **[ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces](https://arxiv.org/abs/2611.14364v1)**
  - *Jiahang Lin, Wanying Ren, Wanghan Xu et al.*
  - `2026-11-10`
  - Research agents achieve increasingly strong benchmark scores, yet these scores do not necessarily translate into reliable delivery in ongoing research projects. Many research-agent benchmarks emphasize standalone tasks and relatively self-contained workflows in clean or curated w…

- **[AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark](https://arxiv.org/abs/2611.13957v1)**
  - *Haotian Qi, Gabriel Skantze*
  - `2026-11-10`
  - } Predicting who will speak next, and when, is a prerequisite for conversational agents and social robots that take turns without waiting for silence. Multiparty next-speaker prediction (NSP) has been studied on corpora with per-speaker sensors, each with its own event definition…

- **[EJAI: Judgment-Preserving Civic AI for Data Center Environmental Justice](https://arxiv.org/abs/2611.13525v1)**
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

- **[No finite rulebook can certify every safe program: an impossibility theorem for gatekeeping AI agents](https://arxiv.org/abs/2611.13367v1)**
  - *Tomas Perez-Acle*
  - `2026-11-09`
  - An AI assistant writes small programs, and a gatekeeper must decide, from the code alone, whether each one may run. Suppose the rules are fixed: never perform a forbidden action, never let the output depend on a secret, always answer eventually. Can two rulebooks, one listing wha…

- **[Veritas: A Verifier Generation Harness for Agent Tasks](https://arxiv.org/abs/2611.13336v1)**
  - *Daoan Zhang, Qinbo Bai, Dehai Min et al.*
  - `2026-11-09`
  - The effectiveness of a self-improving system relies heavily on the quality of its verifier, which judges the outcome of each improvement round. However, the verifiers of most tasks are written by hand, which is expensive and does not scale to tasks that come without one. We propo…

- **[Do AI Agents need Preventive Care? An Epidemiologic Cohort Design for Agentic AI](https://arxiv.org/abs/2611.13333v1)**
  - *Shu Jiang, Graham A. Colditz*
  - `2026-11-09`
  - As AI agents increasingly perform tasks autonomously across sectors, including healthcare and biomedical research, understanding how their behaviors develop and influence outcomes over time becomes increasingly important. Existing evaluations largely focus on model capabilities a…

- **[Agent-Guided Discovery of Exchange-Correlation Functionals with Physics-based Validation](https://arxiv.org/abs/2611.13329v1)**
  - *Achuth Chandrasekhar, Amir Barati Farimani*
  - `2026-11-09`
  - Accurate, compact exchange--correlation functionals are central to predictive density functional theory. Symbolic search and language-model agents can propose new functional forms, but it remains unclear whether their gains survive self-consistency and external evaluation, whethe…

- **[F3-AGI v4.0: Bioenergetically-Gated Active Inference, Metaplastic Preconditioning, and Residual Program Synthesis for Sample-Efficient Abstract Reasoning](https://arxiv.org/abs/2611.13325v1)**
  - *Henrique Oliveira*
  - `2026-11-09`
  - Few-shot abstract reasoning on ARC-AGI requires inducing algorithmic transformations from 2 to 5 demonstration pairs without task-specific pretraining. Because few-shot demonstrations under-constrain the hypothesis space, program synthesis suffers from the Rashomon effect (predic…

- **[Towards Scalable Network-Based Interventions for HIV Treatment and Prevention via R2C-Agent](https://arxiv.org/abs/2611.13312v1)**
  - *Akseli Kangaslahti, Milind Tambe, Alastair van Heerden et al.*
  - `2026-11-09`
  - Human Immunodeficiency Virus (HIV) remains a pressing public health challenge worldwide. Targeting limited HIV prevention and treatment resources effectively with network-based algorithms is a long-standing problem with a rich history at AAMAS and other computational venues. Howe…

- **[PegasusAI Studio: Legible Cyberinfrastructure and Accountable AI Agents for Scientific Workflows](https://arxiv.org/abs/2611.13309v1)**
  - *Komal Thareja, Mats Rynge, Berent Aldikacti et al.*
  - `2026-11-09`
  - AI coding agents can now construct scientific workflows, but operating them on shared cyberinfrastructure (CI) raises problems that code generation does not solve. Agents need current knowledge of the workflow system and its execution sites and access to the runtime state of dist…

- **[MRFoundry: Knowledge-guided agent loops for end-to-end MRI research](https://arxiv.org/abs/2611.13289v1)**
  - *Ke Wang, Atakan Topcu, Hossein Momeni et al.*
  - `2026-11-09`
  - AI agents can write code, use scientific software, and revise computational workflows, opening new possibilities for MRI research. Effective assistance requires connecting acquisition physics, data conventions, specialized tools, and scientific validation. We present MRFoundry, a…

- **[Off-policy Learning with Excursion Policies](https://arxiv.org/abs/2611.13275v1)**
  - *Jiamin He, Mark Rowland, Zhaohan Daniel Guo et al.*
  - `2026-11-09`
  - Off-policy reinforcement learning (RL) tries to learn the value of a target policy while data comes from a different behavior policy. This often requires trading off bias for variance or stability. One way to trade these off is to linearly interpolate between the behavior and tar…

- **[Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors Enter and Which Controls Reach Them](https://arxiv.org/abs/2611.13254v1)**
  - *Shaohuang Wang, Jinghao Wen, Xulei Zhang et al.*
  - `2026-11-09`
  - When an LLM agent fails part-way through a long task, the usual analysis records a symptom: a failure-mode label, or the agent and step judged responsible. It does not say where the error entered, which state carried it to the symptom, whether anything in the trajectory contradic…

- **[ExpertCrowd-SWE: Measuring Frontier Coding Agents on Expert-Authored Engineering Tasks in Unfamiliar Codebases](https://arxiv.org/abs/2611.13246v1)**
  - *Josip Vrdoljak, Akash Singh, Bas Steunebrink et al.*
  - `2026-11-09`
  - ExpertCrowd-SWE (EC-SWE) is a benchmark of 100 expert-authored, multi-file software engineering tasks for evaluating autonomous coding agents in large, unfamiliar codebases. Each task is a change request written by a practising engineer against a pinned commit of a real repositor…

- **[From Process Models to Composable Agentic Workflows: Combining BPMN, Agents and Enterprise Knowledge](https://arxiv.org/abs/2611.13196v1)**
  - *Christian Fillies, Jan Fillies, Frauke Weichhardt et al.*
  - `2026-11-09`
  - LLM-based agents can reason, use tools and collaborate. However, coordinating increasingly complex agentic applications becomes difficult to understand, monitor and improve. Decisions distributed across prompts, tool calls and application logic make workflows implicit. We introdu…

- **[AgentScript-Eval: Benchmarking LLMs and Agents for Code Generation in an Enterprise DSL](https://arxiv.org/abs/2611.13183v1)**
  - *Dipin Khati, Shubham Mehrotra, Bin Bi et al.*
  - `2026-11-09`
  - Domain-specific languages (DSLs) are widely used in enterprise software, giving a compact interface to complex tasks, from data access to infrastructure automation. Platforms increasingly extend them to agents, where a developer declares the topics, permitted actions, and guardra…

- **[Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics](https://arxiv.org/abs/2611.13161v1)**
  - *Sepideh Ravanbakhsh, Hamidreza Moradi*
  - `2026-11-09`
  - Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazards, and aligning with human mission intent. Existing language-guided reinforcement learning (RL) methods primarily focus on sing…

- **[Teaching the Harness: Student-Aware Skill Transfer for LLM Agents](https://arxiv.org/abs/2611.13144v1)**
  - *Chang Liu, Bo Wu*
  - `2026-11-09`
  - Effective teaching requires reasoning about the learner as well as the task, a capacity that Theory of Mind describes as inferring another agent's latent state from its behavior. We ask whether a stronger LLM teaches a fixed student better when it applies this principle. The stud…

- **[Autonomous Optimization of Numerical Algorithms by an AI Agent: Application to Atomistic Simulation](https://arxiv.org/abs/2611.13143v1)**
  - *Jeheon Woo*
  - `2026-11-09`
  - Coding agents built on large language models, run in automated improvement loops, can discover more efficient algorithms. We present AIOA, a framework that brings this approach to the numerical algorithms of atomistic simulation: an agent improves an algorithm against a pre-speci…

- **[DOBB: Dynamic Oriented Bounding Boxes for Multi-Agent Collision Avoidance under State Uncertainty and Heterogeneous Dynamics](https://arxiv.org/abs/2611.13142v1)**
  - *Pedro Antonio Alarcon Granadeno, Jane Cleland-Huang*
  - `2026-11-09`
  - Learning-based decentralized collision avoidance must remain reliable under state-estimation uncertainty and heterogeneous agent dynamics. Existing methods typically address these factors through training-domain variation or by exposing uncertainty and capability estimates to the…

- **[Which Successes Make Good References? Action-Sequence Alignment for Multi-Turn On-Policy Distillation](https://arxiv.org/abs/2611.13135v1)**
  - *Mufei Li, Nikki Lijing Kuang, Zhuoer Wang et al.*
  - `2026-11-09`
  - On-policy distillation (OPD) reduces train-inference distribution mismatch by supervising a student on its own trajectories. For multi-turn tool-use agents, conditioning the teacher on a validated same-task successful trajectory as a reference can provide useful hindsight, but di…

- **[ASPIRE: An Agentic System-Identification Platform for Iterative Reasoning and Exploration](https://arxiv.org/abs/2611.13114v1)**
  - *Erik Derner, Jiří Kubalík, Robert Babuška*
  - `2026-11-09`
  - System identification requires expert decisions on the identification method, incorporation of prior physical knowledge, and model validation. We propose ASPIRE, a framework for nonlinear system identification in which a large language model agent selects and executes the identif…

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

- **[Beyond the Document: Compiled Context and Governed Agents for Any Work Product](https://arxiv.org/abs/2611.13055v1)**
  - *James Rhodes, George Kang*
  - `2026-11-09`
  - A document preserves the visible result of professional work but often discards the research, calculations, assumptions, evidence, and authorization boundaries behind it. We study a different unit of delivery: a Portable Agent Format (PAF) package that carries a work product toge…

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

- **[How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time](https://arxiv.org/abs/2611.12324v1)**
  - *Ku Onoda, Haruto Kawano, Shota Takashiro et al.*
  - `2026-11-09`
  - World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction. A mechanic is a rule for how an action or an interaction changes part of the environment. Each occurrence of a mechanic…

- **[A Modular Perspective for Modeling MARL Systems](https://arxiv.org/abs/2611.12314v1)**
  - *Tiziano Maisonhaute, Jean-Christophe Soulié, Fabien Michel*
  - `2026-11-09`
  - The growing complexity of Multi-Agent Reinforcement Learning (MARL) has fragmented the literature, obscuring underlying architectural choices behind diverse implementations. This fragmentation makes it difficult to evaluate critical modeling dimensions in isolation, identify how…

- **[Reconfigurable Action Theories: A Formal Foundation for Dynamically Composable Agent Harnesses](https://arxiv.org/abs/2611.12300v1)**
  - *Jianmin Ji*
  - `2026-11-09`
  - Action theories typically fix their vocabulary and causal laws, whereas agent harnesses can change their tools, providers, and policies during execution. We introduce Reconfigurable Action Theories (RAT), in which actions can change the action theory itself. A theory module in RA…

- **[Trust, but verify, audit and attribute: a human-in-the-loop framework for checking AI-produced research results](https://arxiv.org/abs/2611.13042v1)**
  - *György Eigner, Patrik P. Süli, Roland Hollós*
  - `2026-11-09`
  - Artificial intelligence (AI) systems now produce research results in bulk: in October 2026 a single laboratory released more than 700 AI-generated mathematics manuscripts, only part of them with machine-checked proofs. Such volumes will be checked mostly by AI agents that call sp…

- **[Code-Grounded Agentic Explanations for Static Analysis Vulnerability Findings](https://arxiv.org/abs/2611.13041v1)**
  - *Oshando Johnson, Ranjith Krishnamurthy, Rohith Kumar Shanmuganathan et al.*
  - `2026-11-09`
  - Static application security testing (SAST) tools surface vulnerabilities early and their verdicts are rule-based and auditable. Yet developers routinely dismiss findings they cannot interpret. Large language models can supply the missing explanation, but designs that also hand th…

- **[ECOS: Environment-Calibrated On-Policy Self-Distillation for Language Agents](https://arxiv.org/abs/2611.12232v1)**
  - *Chenhao Zhang, Zhongan Wang, Mingxuan Li et al.*
  - `2026-11-09`
  - On-policy self-distillation lets a language agent act as its own Teacher by conditioning on privileged context such as skills written from its own trajectories. Its guidance, however, is weighted by how much this context shifts token likelihoods rather than by whether it improves…

- **[PARIS: A multi-agent LLM framework for end-to-end, PRISMA-guided systematic literature reviews with pre-synthesis corpus quality assessment](https://arxiv.org/abs/2611.12222v1)**
  - *Christophe Cruz, Hussam Ghanem, Samir Jabbar et al.*
  - `2026-11-09`
  - Systematic literature reviews (SRs) remain slow and labor-intensive, and most automation tools address single stages of the workflow. We present PARIS (PRISMA Agentic Research Intelligence System), an open-source framework in which a conductor agent running in Claude Code orchest…

- **[Learning to Act with World Models by Valuing What Comes Next](https://arxiv.org/abs/2611.12200v1)**
  - *Chenghao Gao, Zhi Zhang, Dian Jin et al.*
  - `2026-11-09`
  - A sparse terminal reward tells an agent little about its steps. Much of the missing information is implicit in the environment's dynamics, because each state transition can change the conditions for success long before the reward arrives. A world model trained on real transitions…

- **[GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation](https://arxiv.org/abs/2611.12175v1)**
  - *Jinghe Wang, Xinrui Cao, Duo Wu et al.*
  - `2026-11-09`
  - Robotic manipulation has advanced rapidly in mapping visual observations and language instructions to actions. However, reliable manipulation in open-world environments requires robust spatial understanding: the ability to identify targets in complex layouts (spatial reasoning) a…

- **[FraudBench: A Legal Evaluation of AI Deception](https://arxiv.org/abs/2611.12167v1)**
  - *Kevin Wei, Sumaya Nur Adan, Stephan Llerena et al.*
  - `2026-11-09`
  - We introduce FraudBench, an evaluation of large language models' (LLMs) propensities to recommend, assist, or directly take actions that would constitute fraud under U.S. law. Our evaluation contains a novel dataset of 159 scenarios based on real-world U.S. court cases and valida…

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

- **[Repository-Context-Guided Image Understanding for Agentic Software Development](https://arxiv.org/abs/2611.13026v1)**
  - *Fumiki Yohena, Toshiaki Sota, Shota Suzuki et al.*
  - `2026-11-09`
  - Coding agents increasingly receive UI screenshots as part of bug reports, yet degraded image quality - caused by low resolution, compression artifacts, or small rendered text - can prevent them from identifying the relevant UI elements and source files. Vision-language models bec…

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

- **[ChipOmni: A General-Purpose AI Agent for Electronic Design Automation](https://arxiv.org/abs/2611.13020v1)**
  - *Pengkun Wang, Rui Mao, Zhe Zhao et al.*
  - `2026-11-09`
  - Electronic design automation (EDA) workflows remain highly fragmented, requiring engineers to coordinate heterogeneous representations, specialised software tools, and iterative verification across multiple design stages. Although large language models have brought more general r…

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

- **[From Questions to Decisions: Benchmarking How LLM Agents Acquire Decision-Relevant Information from Human Beings](https://arxiv.org/abs/2611.13015v1)**
  - *Yuhan Tang, Ke Fan, Xinkai Zou et al.*
  - `2026-11-09`
  - LLM agents are increasingly asked to make plans for people, such as scheduling drivers or assigning nurses. However, people's requests are often incomplete, and the supporting information for decision-making may be outdated, requiring agents to ask for clarification. Existing ben…

- **[Correct Answers from Insufficient Histories: A Controlled Study of Agent Memory Evaluation](https://arxiv.org/abs/2611.11840v1)**
  - *Quan Xue, Zerui Yang, Chaorui Zhang et al.*
  - `2026-11-09`
  - An answer can match the reference for a complete agent history even when the reader's visible history does not determine it. We study this distinction using executable device logs. Our protocol separates reference agreement, certified evidence sufficiency, and context-appropriate…

- **[Compile-Gated Lean Proof Refactoring with Enterprise Agent Practices: A Model per Step under a US\$3 Cap, Followed by Programmatic Rewrite Rules](https://arxiv.org/abs/2611.13011v1)**
  - *Bobber Cheng*
  - `2026-11-09`
  - Our closed-track entry (Arena username Vexorium-Agent) scored 86.31 points on the final board (L = 77.07, H = 81.86, Z = 100) over the 60 final problems, against 33.33 for the reference proofs, 8th at the deadline (top: 92.57), for US\$166.33 at list prices with every call counte…

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

- **[Discrete Model-Based Diffusion for Combinatorial Optimization in Multi-Robot Task Allocation](https://arxiv.org/abs/2611.13382v1)**
  - *Haejoon Lee, Thomas Marshall Vielmetti, Xinyi Wang et al.*
  - `2026-11-09`
  - Decision making in multi-agent and multi-robot systems often involves discrete decision variables, leading to NP-hard combinatorial optimization problems that must be solved within seconds for near real-time implementation. Denoising diffusion has emerged as a powerful tool for s…

- **[DEPUTYBENCH: Evaluating Contextual Safety in Enterprise Agents](https://arxiv.org/abs/2611.13355v1)**
  - *Hao Zhao, Minghao Lin*
  - `2026-11-09`
  - Enterprise agents must determine whether ordinary requests are permitted by organizational records and policies while continuing legitimate work. We introduce DEPUTYBENCH, an executable benchmark with 79 base items, 375 instances, paired permission contexts, and graded evidence r…

- **[HiCAP: Hierarchical Cultural Adaptation via Personality for Dialogue Generation](https://arxiv.org/abs/2611.13207v1)**
  - *Lingzhi Shen, Xiaohao Cai, Yunfei Long et al.*
  - `2026-11-09`
  - Cultural adaptation in dialogue systems refers to the ability to generate responses that conform to linguistic norms and social expectations across different cultures. However, existing dialogue generation approaches pay limited attention to the role of personality in shaping cul…

- **[High Probability Risk Control for Online Policy Learning](https://arxiv.org/abs/2611.13163v1)**
  - *Yihong Guo, Drew Prinster, Suchi Saria et al.*
  - `2026-11-09`
  - We study risk control for online policy learning, where an agent adaptively collects data and aims to learn a new policy whose risk stays below a tolerance threshold at every round with high probability. Such policy updates and data collection induce feedback covariate shift (FCS…

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

- **[Can Hindsight Critics Guide Delayed Actors?](https://arxiv.org/abs/2611.11863v2)**
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

- **[FaST: Factored Synthesis of Transitions for Offline Reinforcement Learning](https://arxiv.org/abs/2611.13013v1)**
  - *Daniel Campa, Spandan Das, Srinjoy Das*
  - `2026-11-09`
  - Synthetic data augmentation promises to scale offline reinforcement learning beyond fixed logged datasets, but leading diffusion-based generators model the transition tuple (state, action, next state, reward, terminal) as a monolith: no single factor can be natively redrawn in is…

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

- **[Teamknitt: Configuring, Observing and Intervening in LLM-Agent Teams through the Lens of Dynamical-Systems and Human-Team Theory](https://arxiv.org/abs/2611.12545v1)**
  - *Goran Mitevski*
  - `2026-11-09`
  - Most frameworks for teams of large language model (LLM) agents fix the team's shape inside the software: who talks to whom, how much is passed along, and what a human can do once a run has started. Human-team research has long asked those questions: where team phenomena live (in…


## Harness  (93)

### NeurIPS

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

- **[Towards Reliable Benchmarking: A Contamination Free, Controllable Evaluation Framework for Multi-step LLM Function Calling](https://arxiv.org/abs/2509.26553)**
  - *Seiji Maekawa, Jackson Hassell, Pouya Pezeshkpour et al.*
  - **ICLR 2025** · `2025-09-30`
  - Existing benchmarks for tool-augmented language models (TaLMs) lack fine-grained control over task difficulty and remain vulnerable to data contamination. We present FuncBenchGen, a unified, contamination-free framework that evaluates TaLMs by generating synthetic multi-step tool…


### ACL

- **[From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses](https://arxiv.org/abs/2611.13960v1)**
  - *Simon Hegelich, Bardh Prenkaj, Habiba Sarhan et al.*
  - **ACL** · `2026-11-10`
  - AI coding harnesses couple language models to shells, filesystems, and network sockets, turning the harness into an automated Living-off-the-Land (LotL) platform: once an adversary injects instructions into retrieved content, dual-use binaries such as bash, curl, and find become…

- **[Embodied First Exam](https://arxiv.org/abs/2611.12177v1)**
  - *Kangrui Wang, Qineng Wang, Changhe Chen et al.*
  - **ACL** · `2026-11-09`
  - Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical…

- **[Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization](https://arxiv.org/abs/2611.12079v1)**
  - *Jui-Chien Tsou, Po-Yi Wu*
  - **ACL** · `2026-11-09`
  - We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels. On 30 KernelBench tasks (levels 1-3, first 10 each, evaluated on a V100), we co…


### Other / arXiv

- **[GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning](https://arxiv.org/abs/2611.13028)**
  - *Jiajun Chen, Shicheng Fang, Jiahao Lu et al.*
  - 🤗 Featured · `2026-11-09`
  - AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA games is challenging and often human-annotated because task outcomes are often difficult to verify automatically, let alone applyin…

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

- **[Continual-ARC: Measuring Skill Acquisition over a Working Lifetime](https://arxiv.org/abs/2611.14505v1)**
  - *Daniel Lenton*
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

- **[Alania-2: Turkish text-to-speech with instant and fine-tuned voice cloning](https://arxiv.org/abs/2611.13845v1)**
  - *Sezgin Saygili, Emre Kaplaner, Oncel Ozgul et al.*
  - `2026-11-10`
  - We present Alania-2, a Turkish text-to-speech (TTS) system with two built-in voices, voice design from text descriptions, and two kinds of voice cloning. Alania-2 is a 488M-parameter model with the VoxCPM architecture, which generates continuous audio latents with a diffusion hea…

- **[Antalia-2 Mini: A 7.6-million-parameter Turkish text-to-speech model trained entirely on synthetic speech](https://arxiv.org/abs/2611.13811v1)**
  - *Sezgin Saygili, Emre Kaplaner, Oncel Ozgul et al.*
  - `2026-11-10`
  - Antalia-2 Mini is a single-voice Turkish text-to-speech model with 7,620,931 parameters. It reads characters and produces 48 kHz audio at 41 times real time on an Apple M5 laptop CPU (2 threads). Its training audio came only from VoxCPM2 (the teacher), about 300 times larger, clo…

- **[Beyond Proxy Metrics: MLLMs as Human Surrogates for Explainable AI Evaluation](https://arxiv.org/abs/2611.13926v1)**
  - *Eoin M. Kenny, Salim I. Amoukou, Tom Bewley*
  - `2026-11-10`
  - Explainable AI (XAI) has expanded into a broad and impactful research area, but the fundamental question of how best to evaluate explanation techniques has proven frustratingly elusive. Methodologies typically revolve around either proxy metrics which tell us little about the uti…

- **[IFRS Compliance Verification: An Open Multi-LLM Benchmark and Content-Conditioned Ensemble Classifier](https://arxiv.org/abs/2611.13595v1)**
  - *Aghoghomena Akasukpe, Li Yang, Xinyao Zhou et al.*
  - `2026-11-10`
  - Verifying corporate financial disclosures against the International Financial Reporting Standards (IFRS) is a core auditing task in which experts cross-reference disclosures with hundreds of fine-grained regulatory paragraphs: a laborious, costly, and error-prone process that mot…

- **[Veritas: A Verifier Generation Harness for Agent Tasks](https://arxiv.org/abs/2611.13336v1)**
  - *Daoan Zhang, Qinbo Bai, Dehai Min et al.*
  - `2026-11-09`
  - The effectiveness of a self-improving system relies heavily on the quality of its verifier, which judges the outcome of each improvement round. However, the verifiers of most tasks are written by hand, which is expensive and does not scale to tasks that come without one. We propo…

- **[Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors Enter and Which Controls Reach Them](https://arxiv.org/abs/2611.13254v1)**
  - *Shaohuang Wang, Jinghao Wen, Xulei Zhang et al.*
  - `2026-11-09`
  - When an LLM agent fails part-way through a long task, the usual analysis records a symptom: a failure-mode label, or the agent and step judged responsible. It does not say where the error entered, which state carried it to the symptom, whether anything in the trajectory contradic…

- **[ExpertCrowd-SWE: Measuring Frontier Coding Agents on Expert-Authored Engineering Tasks in Unfamiliar Codebases](https://arxiv.org/abs/2611.13246v1)**
  - *Josip Vrdoljak, Akash Singh, Bas Steunebrink et al.*
  - `2026-11-09`
  - ExpertCrowd-SWE (EC-SWE) is a benchmark of 100 expert-authored, multi-file software engineering tasks for evaluating autonomous coding agents in large, unfamiliar codebases. Each task is a change request written by a practising engineer against a pinned commit of a real repositor…

- **[AgentScript-Eval: Benchmarking LLMs and Agents for Code Generation in an Enterprise DSL](https://arxiv.org/abs/2611.13183v1)**
  - *Dipin Khati, Shubham Mehrotra, Bin Bi et al.*
  - `2026-11-09`
  - Domain-specific languages (DSLs) are widely used in enterprise software, giving a compact interface to complex tasks, from data access to infrastructure automation. Platforms increasingly extend them to agents, where a developer declares the topics, permitted actions, and guardra…

- **[Teaching the Harness: Student-Aware Skill Transfer for LLM Agents](https://arxiv.org/abs/2611.13144v1)**
  - *Chang Liu, Bo Wu*
  - `2026-11-09`
  - Effective teaching requires reasoning about the learner as well as the task, a capacity that Theory of Mind describes as inferring another agent's latent state from its behavior. We ask whether a stronger LLM teaches a fixed student better when it applies this principle. The stud…

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

- **[Compile-Gated Lean Proof Refactoring with Enterprise Agent Practices: A Model per Step under a US\$3 Cap, Followed by Programmatic Rewrite Rules](https://arxiv.org/abs/2611.13011v1)**
  - *Bobber Cheng*
  - `2026-11-09`
  - Our closed-track entry (Arena username Vexorium-Agent) scored 86.31 points on the final board (L = 77.07, H = 81.86, Z = 100) over the 60 final problems, against 33.33 for the reference proofs, 8th at the deadline (top: 92.57), for US\$166.33 at list prices with every call counte…

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


## Finance  (143)

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


### KDD

- **[CryptoMixer: Fine-grained market information-aware MLP Networks for Individual Cryptocurrency Trading Prediction](https://www.semanticscholar.org/paper/7700a7579ca8f11b5b31323e6e1fac103dabc2e7)**
  - *Ting-Sheng Feng, Zhi-Hao Shen, Xi Zhao et al.*
  - **KDD 2025** · `2025-08-03`
  - Accurately predicting user trading behavior in decentralized exchanges is essential for investors to mitigate risks and optimize their trading strategies. While existing research primarily focuses on predicting trading behavior in stock markets, these methods often struggle to ad…


### ACL

- **[Depth as a Candidate Source: Portfolio Allocation for Recurrent Test-Time Scaling in Large Language Models](https://arxiv.org/abs/2611.12293v1)**
  - *Chaoyuan Hao, Wentao Yue, Yanyan Wu et al.*
  - **ACL** · `2026-11-09`
  - Recurrent latent reasoning in large lanugage models (LLMs) scales test-time computation by increasing recurrent depth, naturally framing inference as a problem of deciding when to stop. We identify a previously overlooked limitation of this single-depth view through systematic pr…

- **[Meta-Tool: Unleash Open-World Function Calling Capabilities of General-Purpose Large Language Models](https://aclanthology.org/2025.acl-long.1481.pdf)**
  - *Sheng-Qian Qin, Ya-Kun Zhu, Lin-Jie Mu et al.*
  - **ACL 2025**
  - Large language models (LLMs) have show-cased remarkable capabilities as autonomous agents when augmented with external tools. Equipped with fixed tool sets, LLMs struggle with addressing diverse user inquiries in open-world tasks. To evaluate and boost the performance of LLMs in…


### EMNLP

- **[PaperScout: An Autonomous Agent for Academic Paper Search with Process-Aware Sequence-Level Policy Optimization](https://arxiv.org/abs/2601.10029)**
  - *Ting-Yue Pan, Jie Ouyang, Ming-Yue Cheng et al.*
  - **EMNLP 2026** · `2026-01-15`
  - Academic paper search is a fundamental task in scientific research, yet most existing approaches organize retrieval around predefined workflows or structured interaction protocols that struggle with complex, conditional queries. To address this limitation, we propose PaperScout,…


### Other / arXiv

- **[Earlybird: Predictive Streaming Speech Recognition in 29M Parameters](https://arxiv.org/abs/2611.14421)**
  - *Sahil Mahendrakar*
  - 🤗 · `2026-11-10`
  - Streaming speech recognizers output a word only after the speaker has finished it, typically 90-400 ms later. For a voice agent every millisecond counts: the sooner the words are outputted, the sooner the agent can start a search or plan its reply. We present Earlybird, a 29M-par…

- **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210)**
  - *Hadi Salloum, Ammar Ali*
  - 🤗 · `2026-11-10`
  - Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million toke…

- **[Market-Conditioned JEPA: Learning from Unpredictable Market Shocks](https://arxiv.org/abs/2611.13572)**
  - *Yuqi Wang, Fengyuan Liu, Mukai Li et al.*
  - 🤗 · `2026-11-10`
  - Much of the variation in financial time series is driven by market-wide shocks that cannot be predicted from an asset's own history. Per-asset self-supervised learning treats this variation as irreducible noise. Under a latent factor model, we show that conditioning prediction on…

- **[TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data](https://arxiv.org/abs/2611.13946v1)**
  - *Wei Gu, Weiwei Qi, Jiajun Tang et al.*
  - `2026-11-10`
  - Practical Web applications increasingly require agents to interpret long conversations or documents. For inputs exceeding the context windows of large language models (LLMs), memory agents process segments sequentially and retain past information in bounded memory. However, they…

- **[A computational framework for understanding embodied plans](https://arxiv.org/abs/2611.13669v1)**
  - *Aalap D. Shah, Basil Saeed, Joshua B. Tenenbaum et al.*
  - `2026-11-10`
  - Reasoning about people's plans and goals based on their actions is fundamental to human social interaction and essential for cooperative, embodied artificial intelligence. Formalizing this capacity in naturalistic, embodied settings has been a longstanding challenge. Here, we pre…

- **[The RSI Tax: When Recursive Self-Improvement Is Not Worth the Cost](https://arxiv.org/abs/2611.13524v1)**
  - *Yitong Zhang, Ang Li, Yisen Wang*
  - `2026-11-10`
  - Recursive self-improvement (RSI) seeks to improve an agent using its own task experience. Its practical value depends on whether performance gains justify the full cost of self-improvement and task execution. We evaluate this trade-off on continual task streams, scoring each task…

- **[AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark](https://arxiv.org/abs/2611.13957v1)**
  - *Haotian Qi, Gabriel Skantze*
  - `2026-11-10`
  - } Predicting who will speak next, and when, is a prerequisite for conversational agents and social robots that take turns without waiting for silence. Multiparty next-speaker prediction (NSP) has been studied on corpora with per-speaker sensors, each with its own event definition…

- **[IFRS Compliance Verification: An Open Multi-LLM Benchmark and Content-Conditioned Ensemble Classifier](https://arxiv.org/abs/2611.13595v1)**
  - *Aghoghomena Akasukpe, Li Yang, Xinyao Zhou et al.*
  - `2026-11-10`
  - Verifying corporate financial disclosures against the International Financial Reporting Standards (IFRS) is a core auditing task in which experts cross-reference disclosures with hundreds of fine-grained regulatory paragraphs: a laborious, costly, and error-prone process that mot…

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

- **[Optimal Trading Speed on Blockchain](https://arxiv.org/abs/2611.13616v1)**
  - *Ruizhe Jia, Shihao Yu*
  - `2026-11-10`
  - On blockchain-based exchanges, faster blocks weaken the priority-fee competition among arbitrageurs and shift rents from the block producer to them. Equilibrium liquidity peaks at an interior block speed; beyond a threshold, an active liquidity provider cream-skims and passive ca…

- **[Developing an Operational Model for an Internet of Data Based Trusted Data Space for Vocational Education](https://arxiv.org/abs/2611.13520v1)**
  - *Yalan Dong, Hao Tian, Hongyang Jia et al.*
  - `2026-11-10`
  - Data circulation in vocational education has long been constrained by unclear ownership, a lack of trust, and insufficient incentives. The Internet of Data provides a new underlying technology for enabling trusted cross-domain data circulation. Building on an Internet of Data bas…

- **[Do AI Agents need Preventive Care? An Epidemiologic Cohort Design for Agentic AI](https://arxiv.org/abs/2611.13333v1)**
  - *Shu Jiang, Graham A. Colditz*
  - `2026-11-09`
  - As AI agents increasingly perform tasks autonomously across sectors, including healthcare and biomedical research, understanding how their behaviors develop and influence outcomes over time becomes increasingly important. Existing evaluations largely focus on model capabilities a…

- **[Towards Scalable Network-Based Interventions for HIV Treatment and Prevention via R2C-Agent](https://arxiv.org/abs/2611.13312v1)**
  - *Akseli Kangaslahti, Milind Tambe, Alastair van Heerden et al.*
  - `2026-11-09`
  - Human Immunodeficiency Virus (HIV) remains a pressing public health challenge worldwide. Targeting limited HIV prevention and treatment resources effectively with network-based algorithms is a long-standing problem with a rich history at AAMAS and other computational venues. Howe…

- **[Off-policy Learning with Excursion Policies](https://arxiv.org/abs/2611.13275v1)**
  - *Jiamin He, Mark Rowland, Zhaohan Daniel Guo et al.*
  - `2026-11-09`
  - Off-policy reinforcement learning (RL) tries to learn the value of a target policy while data comes from a different behavior policy. This often requires trading off bias for variance or stability. One way to trade these off is to linearly interpolate between the behavior and tar…

- **[Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors Enter and Which Controls Reach Them](https://arxiv.org/abs/2611.13254v1)**
  - *Shaohuang Wang, Jinghao Wen, Xulei Zhang et al.*
  - `2026-11-09`
  - When an LLM agent fails part-way through a long task, the usual analysis records a symptom: a failure-mode label, or the agent and step judged responsible. It does not say where the error entered, which state carried it to the symptom, whether anything in the trajectory contradic…

- **[AgentScript-Eval: Benchmarking LLMs and Agents for Code Generation in an Enterprise DSL](https://arxiv.org/abs/2611.13183v1)**
  - *Dipin Khati, Shubham Mehrotra, Bin Bi et al.*
  - `2026-11-09`
  - Domain-specific languages (DSLs) are widely used in enterprise software, giving a compact interface to complex tasks, from data access to infrastructure automation. Platforms increasingly extend them to agents, where a developer declares the topics, permitted actions, and guardra…

- **[HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents](https://arxiv.org/abs/2611.12872v1)**
  - *Haozhen Zhang, Bohan Liu, Jianzhu Bao et al.*
  - `2026-11-09`
  - As multimodal agents accumulate increasingly long interaction histories, effectively retrieving and utilizing past information becomes critical for long-term interaction. Existing memory systems typically rely on semantic retrieval over compressed memories and expose predefined r…

- **[Beyond the Document: Compiled Context and Governed Agents for Any Work Product](https://arxiv.org/abs/2611.13055v1)**
  - *James Rhodes, George Kang*
  - `2026-11-09`
  - A document preserves the visible result of professional work but often discards the research, calculations, assumptions, evidence, and authorization boundaries behind it. We study a different unit of delivery: a Portable Agent Format (PAF) package that carries a work product toge…

- **[How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time](https://arxiv.org/abs/2611.12324v1)**
  - *Ku Onoda, Haruto Kawano, Shota Takashiro et al.*
  - `2026-11-09`
  - World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction. A mechanic is a rule for how an action or an interaction changes part of the environment. Each occurrence of a mechanic…

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

- **[IC-GNN: Modeling Individualized Brain Community Organization for Disease Prediction](https://arxiv.org/abs/2611.13070v1)**
  - *Yang Zhang, Xiao Zhou, Jonathan Warrell et al.*
  - `2026-11-09`
  - Brain networks exhibit modular organization, where community structures vary substantially across individuals and diseases. Understanding these individual differences is crucial for advancing both basic neuroscience research and precision medicine. However, widely used predefined…

- **[Explanation-Aware Fairness Beyond Output Parity: Joint Output-Attribution Regularization for Medical Image Classification](https://arxiv.org/abs/2611.13052v1)**
  - *Gökhan Özbulak, Oscar Jimenez-del-Toro, Lilian Berton et al.*
  - `2026-11-09`
  - Output-level fairness does not constrain whether demographic groups rely on similar predictive contributions in representation space. For a nonlinear encoder with a linear head, we show that outcome-conditioned output score disparity equals the signed sum of feature attribution d…

- **[Same Physics, Different Gradients: A State-of-the-Art Report on Differentiable Physics Simulation](https://arxiv.org/abs/2611.12162v1)**
  - *Lei Shu, Zizhou Huang, Yunuo Chen et al.*
  - `2026-11-09`
  - Differentiable simulation propagates derivatives through a physics simulator, turning animation, system identification, control, and computational design into gradient-based optimization. Engines differ in the physics they model and, less visibly, in which mathematical object the…

- **[Making sense of rule 605](https://arxiv.org/abs/2611.13365v1)**
  - *Peter B. Lerner*
  - `2026-11-09`
  - The paper analyzes monthly reports of two companies: one market maker, Virtu, and one broker-dealer, SoHo, in the period between January 2021 and March 2024. The predictive power of standard methods for the probability laws of stock orders- linear regression and LSTM- is poor, de…

- **[Diversified-Risk-Perception Risk Measures and Portfolio Selection](https://arxiv.org/abs/2611.11803v1)**
  - *Yang Liu, Yuhao Liu, Jiani Shen*
  - `2026-11-09`
  - Traditional risk measures generally rely on a single probability model, potentially overlooking information from alternative models and leading to biased risk assessments. This limitation cannot be addressed by asset diversification alone in risk management. In this paper, we pro…

- **[A Black-Box Reduction from Regret to Multi-Level Coverage](https://arxiv.org/abs/2611.12059v1)**
  - *Tuo Liu, Edgar Dobriban, Francesco Orabona*
  - `2026-11-09`
  - Online Conformal Prediction (OCP) sequentially constructs prediction sets whose average empirical coverage converges to a target level over time, for arbitrary, potentially adversarial datasets. In the multi-level setting, prediction sets are produced at $d$ coverage levels at on…


---
*Generated 2026-11-12 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
