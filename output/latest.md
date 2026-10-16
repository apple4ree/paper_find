# Daily Paper Digest — 2026-10-16 (Friday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**669 unique papers** (851 topic-entries — cross-topic papers counted once per category)

---

## Agent  (520)

### AAAI

- **[A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators](https://doi.org/10.1609/aaai.v40i35.40240)**
  - *Ming-Ming Zhao, Xiaokang Wei, Yuan-Qi Shao et al.*
  - **AAAI 2026** · `2026-03-14`
  - Large language models (LLMs) have shown strong potential in automating the design of agentic workflows. However, existing methods still rely heavily on manually predefined operators, limiting generalization and scalability. To address this issue, we propose A²Flow, a fully automa…


### NeurIPS

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **NeurIPS 2026** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…

- **[DyFlow: Dynamic Workflow Framework for Agentic Reasoning](https://arxiv.org/abs/2509.26062)**
  - *Yan-Bo Wang, Zi-Xiang Xu, Yue Huang et al.*
  - **NeurIPS 2025** · `2025-09-30`
  - Agent systems based on large language models (LLMs) have shown great potential in complex reasoning tasks, but building efficient and generalizable workflows remains a major challenge. Most existing approaches rely on manually designed processes, which limits their adaptability a…

- **[CoP: Agentic Red-teaming for Large Language Models using Composition of Principles](https://arxiv.org/abs/2506.00781)**
  - *Chen Xiong, Pin-Yu Chen, Tsung-Yi Ho*
  - **NeurIPS 2025** · `2025-06-01`
  - Recent advances in Large Language Models (LLMs) have spurred transformative applications in various domains, ranging from open-source to proprietary LLMs. However, jailbreak attacks, which aim to break safety alignment and user compliance by tricking the target LLMs into answerin…

- **[Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding](https://arxiv.org/abs/2505.18079)**
  - *Xiaoyi Zhang, Zhao-Yang Jia, Zong-Yu Guo et al.*
  - **NeurIPS 2025** · `2025-05-23`
  - Long-form video understanding presents significant challenges due to extensive temporal-spatial complexity and the difficulty of question answering under such extended contexts. While Large Language Models (LLMs) have demonstrated considerable advancements in video analysis capab…


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

- **[Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://arxiv.org/abs/2505.19433)**
  - *Peijie Dong, Zhen-Heng Tang, Xiang-Hong Liu et al.*
  - **ICML 2025** · `2025-05-26`
  - Post-training compression reduces the computational and memory costs of large language models (LLMs), enabling resource-efficient deployment. However, existing compression benchmarks only focus on language modeling (e.g., perplexity) and natural language understanding tasks (e.g.…


### ICLR

- **[Re-Aligning Language to Visual Objects with an Agentic Workflow](https://arxiv.org/abs/2503.23508)**
  - *Yuming Chen, Jiangyan Feng, Haodong Zhang et al.*
  - **ICLR 2025** · `2025-03-30`
  - Language-based object detection (LOD) aims to align visual objects with language expressions. A large amount of paired data is utilized to improve LOD model generalizations. During the training process, recent studies leverage vision-language models (VLMs) to automatically genera…

- **[Flow: Modularized Agentic Workflow Automation](https://arxiv.org/abs/2501.07834)**
  - *Boye Niu, Yiliao Song, Kai Lian et al.*
  - **ICLR 2025** · `2025-01-14`
  - Multi-agent frameworks powered by large language models (LLMs) have demonstrated great success in automated planning and task execution. However, the effective adjustment of agentic workflows during execution has not been well studied. An effective workflow adjustment is crucial…


### KDD

- **[Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems](https://arxiv.org/abs/2605.06457)**
  - *Dong-Hao Huang, Joon Kiat Chua, Zhao-Xia Wang*
  - **KDD 2026** · `2026-05-07`
  - LLM-based multi-agent systems are increasingly deployed for payment workflows, yet prevailing metrics, Task Success Rate (TSR) and Agent Handoff F1-Score (HF1), capture only final outcomes or unordered routing decisions. We introduce the Agentic Success Rate (ASR), a trajectory-f…

- **[DeepTravel: An End-to-End Agentic Reinforcement Learning Framework for Autonomous Travel Planning Agents](https://arxiv.org/abs/2509.21842)**
  - *Yansong NING, Rui Liu, Jun Wang et al.*
  - **KDD 2025** · `2025-09-26`
  - Travel planning (TP) agent has recently worked as an emerging building block to interact with external tools/resources for travel itinerary generation, ensuring an enjoyable user experience. Despite its benefits, existing studies rely on hand-craft prompt and fixed agent workflow…


### ACL

- **[SERO: Learning from Executable Oracle Continuations for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2610.19397)**
  - *Dingyi Rong, Yue Shi, Chaofan Ma et al.*
  - **ACL** · 🤗 Featured · `2026-10-14`
  - Long-horizon agentic RL is constrained by the futures visited by the current policy. When rollouts fail to reach useful behaviors, improved credit assignment cannot provide supervision for states and actions that were never encountered. On-policy distillation (OPD) introduces tea…

- **[Poison Valleys: Diagnosing Path-Dependent Failure in LLM Code Repair](https://arxiv.org/abs/2610.21514v1)**
  - *Veljko Skarich*
  - **ACL** · `2026-10-15`
  - When code-repair agents fail, final tests reveal that a patch is wrong but not which earlier commitment caused it or which software obligation failed. Poison Valleys traces this path in 1,844 model requests on two synthetic Python cases: PersistQueue adds atomic batch claiming to…

- **[Bias Control and Injection for Multi-Agent Aggregation](https://arxiv.org/abs/2610.21290v1)**
  - *Sungjae Lee, Soheil Abbasloo, Jabin Koo et al.*
  - **ACL** · `2026-10-15`
  - Multi-agent reasoning with large language models (LLMs) raises a central question for collective decision-making: when agents disagree, whose decision should be trusted? Resolving such disagreements is difficult because agents' decisions are susceptible to non-semantic biases suc…

- **[Who May Release an Agent's Promise? Standing over Commitments in Multi-Party Chat](https://arxiv.org/abs/2610.21203v1)**
  - *Lan Wei, Bingyu Shen, Jiaqi Tang et al.*
  - **ACL** · `2026-10-15`
  - When an assistant serving a team makes a promise to Alice, who may cancel it? We call this standing: only the creditor (the person owed) or someone the creditor or operator policy authorizes may release a commitment, regardless of rank. In a controlled chat environment we vary wh…

- **[A Self-Improving Agent that Grows its Own DSL: Oracle-Free Operator Induction for Exact Question Answering](https://arxiv.org/abs/2610.20809v1)**
  - *Yun-Shiuan Chuang, Yirou Ge, Yixi Li et al.*
  - **ACL** · `2026-10-14`
  - A self-improving agent has to decide which new skills to keep, and in practice it keeps whatever earns a high reward, convinces a judge model, or compresses its library, even when the skill is wrong. That is fine until the answers have to be exactly right: over a table of transac…

- **[P2Patch: Exploit-Guided Vulnerability Repair](https://arxiv.org/abs/2610.20245v1)**
  - *Mohsen Iranmanesh, Sina Moradi Sabet, Sina Marefat et al.*
  - **ACL** · `2026-10-14`
  - Large language models are increasingly deployed as autonomous agents for automated program repair, patching software vulnerabilities through multi-step reasoning and tool use. Yet these systems typically validate a patch against the same evidence used to construct it -- a static…

- **[Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training](https://arxiv.org/abs/2610.19423v1)**
  - *Anshu Raina, Peyman Razaghi, Yuankai Chen et al.*
  - **ACL** · `2026-10-14`
  - Configuring distributed LLM training across hundreds of GPUs requires jointly optimizing tensor, pipeline, expert, context, and data parallelism alongside micro-batch size, recomputation, sharding, and overlap, a combinatorial space where memory legality can hinge on a single byt…

- **[Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy Rewards](https://arxiv.org/abs/2610.19372v1)**
  - *Min-Young Yu*
  - **ACL** · `2026-10-14`
  - Runtime policy verifiers can prevent agents from executing disallowed actions, but their decisions are typically used only for enforcement and discarded afterward. We ask whether these decisions can instead become verifiable policy rewards for training the agents they guard. We i…

- **[VELD-QA: A Large-Scale Dataset for Visual Evidence Grounding and Question Answering in Long Documents](https://arxiv.org/abs/2610.20964v1)**
  - *Zhivar Sourati, Marianne Menglin Liu, Rongguang Wang et al.*
  - **ACL** · `2026-10-14`
  - Existing long-document QA benchmarks rarely combine large-scale human-authored questions with detailed visual evidence annotations, limiting diagnosis of evidence localization and interpretation failures. We present VELD-QA, a large-scale benchmark for Visual Evidence grounding a…

- **[Agentic-MatriBO: Capability-Compiled Agentic Bayesian Optimization for Materials and Chemical Design](https://arxiv.org/abs/2610.17832v2)**
  - *Yu Zeng, Yuchuan Chen, Ziyue Zhang et al.*
  - **ACL** · `2026-10-13`
  - Materials and chemical optimization must choose the next synthesis, characterization, or high-fidelity simulation from sequential observations under a limited budget. Large language models can use task knowledge to propose adjustments, but composing surrogates, acquisition functi…

- **[Learning from fracture: Teaching language models to design through physical experience](https://arxiv.org/abs/2610.17804v1)**
  - *Bo Ni*
  - **ACL** · `2026-10-13`
  - How can language models learn to optimize physical designs through experience? We introduce FracLearn, an experience-abstraction-generalization framework evaluated through a deliberately unfamiliar, Tetris-inspired fracture game. The model first proposes architectures and examine…

- **[Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents](https://arxiv.org/abs/2610.18457v1)**
  - *Kristoffer Hempel, Nils Loose, Lorenzo Cavallaro et al.*
  - **ACL** · `2026-10-13`
  - Large language model (LLM) agents are becoming an integral part of the software development lifecycle, and the capabilities granted to them allow an agent to act with the user's authority on any resource it can access. The reach that gives an agent its utility is equally availabl…

- **[FinReporting: An Agentic Workflow for Localized Reporting of Cross-Jurisdiction Financial Disclosures](https://arxiv.org/abs/2604.05966)**
  - *Fan Zhang, M. Song, R. Elbadry et al.*
  - **ACL 2026** · `2026-04-07`
  - Financial reporting systems increasingly leverage Large Language Models (LLMs) to extract and summarize corporate disclosures. However, most existing approaches assume a single-market setting and overlook structural differences across jurisdictions. Variations in accounting taxon…

- **[RAG-Critic: Leveraging Automated Critic-Guided Agentic Workflow for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.179.pdf)**
  - *Guan-Ting Dong, Jiajie Jin, Xiaoxi Li et al.*
  - **ACL 2025**
  - Retrieval-augmented generation (RAG) has emerged as a pivotal technology in natural language processing, owing to its efficacy in generating factual content. However, its informative inputs and complex paradigms often lead to a greater variety of errors. Consequently, achieving a…

- **[Evolving Agentic Workflow Driven by Human-Agent Collaboration](https://aclanthology.org/2026.findings-acl.1250.pdf)**
  - *Yuxin Liu, Jin-Xuan Zhang, Yuezhang Peng et al.*
  - **ACL 2026**
  - Agentic workflows, composed of multiple collaborating Large Language Models (LLMs), have become a key paradigm for complex problem-solving. However, their effectiveness is often hindered by three critical challenges: high manual design costs, inefficient agentic search, and poor…


### EMNLP

- **[EvoAgentX: An Automated Framework for Evolving Agentic Workflows](https://arxiv.org/abs/2507.03616)**
  - *Yingxu Wang, Siwei Liu, Jinyuan Fang et al.*
  - **EMNLP 2025** · `2025-07-04`
  - Multi-agent systems (MAS) have emerged as a powerful paradigm for orchestrating large language models (LLMs) and specialized tools to collaboratively address complex tasks. However, existing MAS frameworks often require manual workflow configuration and lack native support for dy…

- **[Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://arxiv.org/abs/2501.05366)**
  - *Xiaoxi Li, Guan-Ting Dong, Jiajie Jin et al.*
  - **EMNLP 2025** · `2025-01-09`
  - Large reasoning models (LRMs) like OpenAI-o1 have demonstrated impressive long stepwise reasoning capabilities through large-scale reinforcement learning. However, their extended reasoning processes often suffer from knowledge insufficiency, leading to frequent uncertainties and…


### Other / arXiv

- **[FDE-Gym: The Last Mile of AI Delivery](https://arxiv.org/abs/2610.22350)**
  - *Dongxu Yang, Hongda Yan, Renxin Wang et al.*
  - 🤗 Featured · `2026-10-15`
  - Existing agent benchmarks typically evaluate agents on well-specified tasks defined by issue reports, specifications, or task tickets. Real-world customer delivery is different: forward-deployed engineers (FDEs) must clarify ambiguous requirements, work in live systems, and uncov…

- **[OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use](https://arxiv.org/abs/2610.22200)**
  - *Hanzhang Zhou, Long Li, Quyu Kong et al.*
  - 🤗 Featured · `2026-10-15`

- **[3DCodeVerse: Exploring 3D Worlds as Code](https://arxiv.org/abs/2610.22341)**
  - *Yipeng Gao, Ziyao Zeng, Jinfa Huang et al.*
  - 🤗 Featured · `2026-10-15`
  - We introduce 3DCodeVerse, a research ecosystem that enables coding agents to create editable and verifiable 3D content at scale. 3DCodeVerse comprises large-scale, high-quality datasets of executable 3D code, a coding harness for spatial reasoning and automated verification, and…

- **[Mosaic: Multi-Session Agentic Reinforcement Learning](https://arxiv.org/abs/2610.22174)**
  - *Yilong Xu, Minrui Xu, Xinyu Zhou et al.*
  - 🤗 Featured · `2026-10-15`
  - Most existing agentic reinforcement learning methods assume single-session trajectories, where interaction proceeds within one continuously accumulated context. However, agentic techniques such as context compaction and subagent forking may produce trajectories spanning multiple…

- **[AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning](https://arxiv.org/abs/2610.22194)**
  - *Bingxiang He, Pengqi Sun, Shihao Peng et al.*
  - 🤗 Featured · `2026-10-15`
  - Language model agents increasingly automate post-training, but when given the full training stack they converge on supervised fine-tuning and spend most effort revising training data. Existing systems give the agent one kind of control, selecting rows from a fixed pool or calling…

- **[MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering](https://arxiv.org/abs/2610.22344)**
  - *Shangheng Du, Jinxin Shi, Shuaiyu Zhang et al.*
  - 🤗 Featured · `2026-10-15`
  - Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE)…

- **[Data World: Scaling Data Environments from Scratch](https://arxiv.org/abs/2610.21656)**
  - *Zhanli Li, Zeyuan Xu, Chaoxu Pang et al.*
  - 🤗 Featured · `2026-10-15`
  - Data agents use code to process heterogeneous files and derive analytical insights. Scaling their training faces costly environment curation, privacy and intellectual-property restrictions, and difficulty verifying open-ended findings without known generative truth. Our core insi…

- **[Intern-Decision: Efficient Multimodal Decision Making with Autoregressive Masked Language Modeling](https://arxiv.org/abs/2610.22131)**
  - *Tong Zhu, Zhe Xu, Zefeng He et al.*
  - 🤗 Featured · `2026-10-15`
  - Interactive agents repeatedly choose among a finite set of actions, labels, or ordinal outcomes. Generating a free-form response for each choice adds latency and complicates the interface between a model and its environment. We present Intern-Decision, a family of 0.8B, 2B, and 4…

- **[Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine](https://arxiv.org/abs/2610.22192)**
  - *Junyao Yang, Zongxia Li, Yucheng Shi et al.*
  - 🤗 Featured · `2026-10-15`
  - Converting verifier outcomes into useful policy updates and partial progress into complete task resolution is crucial for terminal agents. We present Terminal-RSI, which alternates Recursive Self-Rewrite (RSR) of verified trajectories with critic-inheriting Recursive Policy-Refin…

- **[OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling](https://arxiv.org/abs/2610.22355)**
  - *Bowei Liu, Xinchen Zhang, Xuhuan Li et al.*
  - 🤗 Featured · `2026-10-15`
  - Generative visual verifiers play a crucial role in advancing multimodal intelligence. To enhance the robustness of visual verifiers in complex multimodal scenarios involving compositional requirements, we move beyond conventional binary verifiers that produce only True/False disc…

- **[JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs](https://arxiv.org/abs/2610.21412)**
  - *Kunlun Zhu, Tao Feng, Xu Han et al.*
  - 🤗 Featured · `2026-10-15`
  - Large language model (LLM) agents now fix software, operate computers and serve customers, but their harnesses, the programs that run them, call a large LLM at every step, which makes long tasks slow and costly. Most of these calls end in a multiple-choice decision, such as which…

- **[Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents](https://arxiv.org/abs/2610.21463)**
  - *Zilin Wang, Yinhong Liu, Chao Chen et al.*
  - 🤗 Featured · `2026-10-15`
  - Large language model agents solve tasks through long sequences of tool calls, and the prevailing design has a single strong model generate every step, although many steps are routine enough for a much smaller model. Existing ways of sharing this work keep the strong model as the…

- **[Athanor: An Agent-Native System for Autonomous Post-Training Research](https://arxiv.org/abs/2610.21055)**
  - *Yufa Zhou, Yichen Wang, Jiakun Fan et al.*
  - 🤗 Featured · `2026-10-15`
  - Recursive self-improvement, in which AI systems build stronger AI systems, is one promising route to superintelligence. We study a weaker form that can be measured today: frontier agents post-training a small raw base model with public data, as a test of their research potential.…

- **[Learning Self-Orchestration in Decentralized Agent Swarms](https://arxiv.org/abs/2610.22322)**
  - *Guowei Xu, Zhenting Qi, Amani Kiruga et al.*
  - 🤗 Featured · `2026-10-15`
  - The capabilities of an agent swarm depend on both its individual members and how they coordinate. Yet existing multi-agent systems often train agents within fixed orchestration structures, separating the learning of individual capabilities from the organization of collective beha…

- **[MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training across Mobile and Computer Environments](https://arxiv.org/abs/2610.20939)**
  - *Panrong Tong, Quyu Kong, Pengxiang Li et al.*
  - 🤗 Featured · `2026-10-14`
  - Online reinforcement learning (RL) with verifiable rewards has driven rapid progress in mathematics, coding, and tool use, but scaling this success to GUI agents remains challenging due to the high cost of interactive environments and the scarcity of realistic training tasks. We…

- **[DeltaStreamer: Towards Human-Like Agentic Streaming Video Understanding](https://arxiv.org/abs/2610.19849)**
  - *Boyuan Sun, Deshui Miao, Wenzhao Gao et al.*
  - 🤗 Featured · `2026-10-14`
  - We propose DeltaStreamer, a novel agentic framework for streaming video understanding inspired by how humans observe, remember, and investigate. Streaming video understanding requires a system to retain evidence before knowing which details future queries will need. Existing appr…

- **[Self-Evolving Agent Harness](https://arxiv.org/abs/2610.18813)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - 🤗 Featured · `2026-10-13`
  - Harness self-evolution revises an agent's software scaffolding, including prompts, memory, workflows, and executable components, while keeping model weights fixed. We formalize a feedback-driven process in which accepted revisions persist across runs. The framework separates upda…

- **[EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation](https://arxiv.org/abs/2610.17560)**
  - *Zeru Shi, Jindong Jiang, Ryo Hachiuma et al.*
  - 🤗 Featured · `2026-10-13`
  - Complex and long-horizon agent tasks often rely on frontier models deployed in the cloud to achieve strong performance. However, using these models for every step of a long-horizon trajectory incurs substantial inference cost, even though not all steps may require the same level…

- **[A team of Gemini 4 Argon agents beats Minecraft](https://arxiv.org/abs/2610.22319)**
  - *Maxence Faldor, Satinder Singh, Roberta Raileanu*
  - 🤗 · `2026-10-15`
  - We placed four Gemini 4 Argon agents in a sandboxed Minecraft survival world and gave them one goal: defeat the Ender Dragon. Each agent controlled a player via an open-source library called Mineflayer and coordinated with its teammates through in-game chat and shared memory. No…

- **[MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents](https://arxiv.org/abs/2610.22240)**
  - *Huanyao Zhang, Jiepeng Zhou, Jiaye Lin et al.*
  - 🤗 · `2026-10-15`

- **[CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](https://arxiv.org/abs/2610.21910)**
  - *Dongjie Cheng, Ruifeng Yuan, Ran Wei et al.*
  - 🤗 · `2026-10-15`
  - As Vision-Language Models (VLMs) advance, they are increasingly expected to perform spatiotemporal reasoning over motion, actions, and view changes beyond what the input images show. Video World Models (VWMs) provide a natural unified engine for visual imagination by generating t…

- **[From Research Goals to Scientific Closure: Evaluating Agents Through Evidence-Supported Physics Research](https://arxiv.org/abs/2610.21767)**
  - *Yijia Mao, Song Dai, Tao Chen et al.*
  - 🤗 · `2026-10-15`
  - Can AI agents organize scientific investigations that lead to well-supported conclusions? To evaluate this capability, we introduce PhysClosureBench, a benchmark of 50 expert-verified, goal-specified research tasks spanning strong-field, attosecond, and neighboring physics areas.…

- **[DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents](https://arxiv.org/abs/2610.21561)**
  - *Sergio Burdisso, Esaú Villatoro-Tello, Dairazalia Sánchez-Cortés et al.*
  - 🤗 · `2026-10-15`
  - Large language models (LLMs) deployed as conversational agents are increasingly expected to follow procedural logic. While factual hallucination has received extensive attention, a different failure mode has been overlooked: procedural hallucination, in which an agent produces in…

- **[MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents](https://arxiv.org/abs/2610.21405)**
  - *Cheng Zhang, Xuanning Cao, Zhicheng Zheng et al.*
  - 🤗 · `2026-10-15`
  - Long-term memory has become a crucial component of large language model (LLM) agents, with most research focusing on retrieving relevant information accurately and efficiently. However, a dependable memory system must also forget sensitive user data upon request. To evaluate this…

- **[LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation](https://arxiv.org/abs/2610.22372v1)**
  - *Zhixu Li, Keqian Tang, Litian Gong et al.*
  - `2026-10-15`
  - Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality. While general robotic manipulation has been extensively studied, personalized robotic manipulation (PeRM) lacks a controlled benchmark for separating t…

- **[KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents](https://arxiv.org/abs/2610.22331v1)**
  - *Siqi Chen, Zhengxi Lu, Yuchen Yan et al.*
  - `2026-10-15`
  - Deep search agents solve knowledge-intensive tasks through long-horizon, multi-turn interactions, where assigning credit to individual search decisions is fundamentally difficult. Outcome-based reinforcement learning provides only a single terminal reward shared across an entire…

- **[Learning to Steer LLM Agents and Multi-Agent Systems](https://arxiv.org/abs/2610.22316v1)**
  - *Leyang Shen, Yaxin Gong, Yang Zhang et al.*
  - `2026-10-15`
  - Large language model (LLM)-based agents and multi-agent systems increasingly tackle complex tasks through long-horizon tool use and inter-agent collaboration. However, these systems are prone to deviating from the overall goal as execution unfolds, which wastes execution resource…

- **[Improving Environment-Agnostic Coding Agents: The Role of Scaffolding](https://arxiv.org/abs/2610.22289v1)**
  - *Sergey Rodionov*
  - `2026-10-15`
  - Stronger language models may increasingly construct useful procedures for themselves, reducing the advantage of developer-supplied scaffolding. We investigate why this advantage persists and whether an environment-agnostic agent can be improved without environment-specific engine…

- **[LEASH: Uncertainty-Aware Weak-to-Strong Escalation and Oversight for Computer-Use Agents](https://arxiv.org/abs/2610.22280v1)**
  - *Qingni Wang, Changdae Oh, Yuzhe Yang et al.*
  - `2026-10-15`
  - Computer-use agents increasingly tackle long-horizon tasks, where running a frontier model at every step is expensive and a small open-weight model alone often fails. Weak-to-strong escalation offers a middle ground where a weak agent acts by default and hands control to a strong…

- **[Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries](https://arxiv.org/abs/2610.22273v1)**
  - *Anikait Singh, Teresa Zhang, Yoonho Lee et al.*
  - `2026-10-15`
  - Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often…

- **[X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement Learning](https://arxiv.org/abs/2610.22269v1)**
  - *Adhwaa Al-Chaab, Ayman Younis, Dario Pompili*
  - `2026-10-15`
  - The O-RAN ALLIANCE introduces architectural flexibility through disaggregation and AI-driven control. While the RAN Intelligent Controller (RIC) enables centralized optimization, current AI approaches lack reasoning capabilities and explainability. We propose eXplainable RIC (X-R…

- **[Disagreement-Guided Weak-to-Strong Routing](https://arxiv.org/abs/2610.22245v1)**
  - *Sima Noorani, Shayan Kiyani, George Pappas et al.*
  - `2026-10-15`
  - Small language models are increasingly deployed on edge devices and robotic systems to meet cost and latency constraints, yet their limited capabilities can make reliable deployment challenging. Stronger models can provide assistance when needed, but deciding when to route a weak…

- **[Language Is a Security Surface for Agent Guards](https://arxiv.org/abs/2610.22244v1)**
  - *Hasan Demirkiran, Jens Ernstberger*
  - `2026-10-15`
  - Step-level guards decide, before each tool call, whether an agent's next action is safe given the user's request and the trajectory so far. Users write those requests in many languages, while guard prompts and the benchmarks on which purpose-built guards are trained and evaluated…

- **[Shortcut Sensitivity in Agent-Safety Evaluations](https://arxiv.org/abs/2610.22243v1)**
  - *Hasan Demirkiran, Jens Ernstberger*
  - `2026-10-15`
  - AI agents take actions through tools. Some actions are sensitive, so guards that supervise them must themselves be evaluated reliably. Yet the data used to evaluate a guard can include cues that make labels predictable without measuring the intended safety construct, and those cu…

- **[OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents](https://arxiv.org/abs/2610.22234v1)**
  - *Bowen Yang, Kaiming Jin, Zichen Ding et al.*
  - `2026-10-15`
  - Real desktop automation is neither purely visual nor purely programmatic. Agents must understand user-facing interfaces while efficiently manipulating files, scripts, and system state. However, native GUI/code coordination cannot be obtained by prompt-level tool composition. In o…

- **[Beyond Downstream QA: Rethinking How We Evaluate Agent Memory](https://arxiv.org/abs/2610.22209v1)**
  - *Sebastian-Antonio Toma, Jean de Kernier, Mike Ply et al.*
  - `2026-10-15`
  - Agent memory benchmarks evaluate whether an agent's responses reflect correct knowledge, measuring downstream question-answering accuracy as a proxy for memory quality. We show this evaluation paradigm is incomplete: it conflates memory correctness with retrieval and generation q…

- **[Decentralized LLM Workflows via Sequential Auctions](https://arxiv.org/abs/2610.22201v1)**
  - *Ian Gemp, Shubhendu Trivedi, Adam Fisch et al.*
  - `2026-10-15`
  - We present a scalable framework for solving multi-step tasks through a decentralized market of self-interested agents. Prior theoretical work demonstrated that agents organized through sequential auctions can converge to a globally optimal policy in a Markov decision process (MDP…

- **[HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration](https://arxiv.org/abs/2610.22195v1)**
  - *Yanchen Deng, Jianguo Huang, Yao Long Teng et al.*
  - `2026-10-15`
  - Orchestrating multiple agents on a complex task requires reconciling local subtask execution with global task planning. Dynamic dispatch approaches provide execution flexibility but do not explicitly model subtask hierarchies or dependencies, while predefined workflows impose thi…

- **[Realtime-Bench: Can Frontier Models Solve Real-time Interactive Problems?](https://arxiv.org/abs/2610.22155v1)**
  - *Jingyu Tang, Xu Yang, Zhehao Zhang et al.*
  - `2026-10-15`
  - Real-time interaction requires agents to perceive evolving environments and act under temporal constraints, yet existing evaluations of real-time streaming models focus on conversational quality and streaming perception, leaving effective action under strict temporal constraints…

- **[Specification Gaming and a Constrained Reinforcement Learning Mitigation in a Cleaning Gridworld](https://arxiv.org/abs/2610.22152v1)**
  - *Hilda Adwubi Osei*
  - `2026-10-15`
  - Reinforcement learning agents optimize exactly the reward signal they are given, which can diverge sharply from an intended true objective when that signal is only a proxy for it; this failure mode is known as specification gaming. Existing evidence for this failure mode is large…

- **[Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions](https://arxiv.org/abs/2610.22138v1)**
  - *Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang et al.*
  - `2026-10-15`
  - LLM systems increasingly rely on groups of agents that discuss, critique, and check one another, assuming that peers will catch individual errors. We test this assumption against a minimal adversary. In a ten-agent factual discussion, one or three adversarial agents repeatedly as…

- **[PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents](https://arxiv.org/abs/2610.22124v1)**
  - *Kshitij Mishra, Abhijith Sharma, Nils Lukas et al.*
  - `2026-10-15`
  - Modern agentic systems extend language models with external tools, enabling them to complete complex tasks through multi-turn interactions. As these agents are deployed in consequential settings, they are often constrained by policies governing pricing, privacy, confirmation, saf…

- **[FAOPs: Normal Forms and an Algebra for AI Agent Workflows](https://arxiv.org/abs/2610.22061v1)**
  - *Ali Mohammadi Shanghooshabad*
  - `2026-10-15`
  - Organizations increasingly encode operational procedures as multi-step agent skills, here called Agent Operating Procedures (AOPs), that must be traceable, auditable, reproducible, access-controlled, and bounded in time and cost, requirements that regulated sectors make mandatory…

- **[GraphACM: Graph-based Action Consistency Measurement for Uncertainty Quantification in LLM Agents](https://arxiv.org/abs/2610.22031v1)**
  - *Yaxin Ma, Wenbo Zhang, Satya Krishna Pothapragada et al.*
  - `2026-10-15`
  - Behavioral consistency across repeated executions provides an informative signal for assessing the reliability of large language model (LLM) agents. However, existing approaches typically summarize consistency with a single task-level score, without identifying where behavioral d…

- **[Priming Base Models for Agentic Post-Training: An Open Midtraining Recipe](https://arxiv.org/abs/2610.22019v1)**
  - *Soumye Singhal, Joseph Jennings, Ka Shun Shum et al.*
  - `2026-10-15`
  - Frontier models, general-purpose and domain-specific alike, now include a midtraining stage between pretraining and post-training, but little has been published about how this stage is built. We present an open midtraining recipe that primes base models for agentic post-training,…

- **[CARA: Causally Guided Retrieval Agent for Question Answering](https://arxiv.org/abs/2610.22017v1)**
  - *Weicheng Liu, Xiangcheng Wu, Depeng Xu et al.*
  - `2026-10-15`
  - Retrieval-augmented generation over text-rich knowledge graphs requires identifying evidence that contributes to answering a question, rather than merely matching its textual content. Existing agentic retrievers adaptively balance global search and multi-hop exploration but prima…

- **[OntoAct: Hypothesis-Based Neuro-Symbolic Agents through Ontological Abstraction](https://arxiv.org/abs/2610.21983v1)**
  - *Donghyeok Lee, Bong Gyun Kang, Junyong Ahn et al.*
  - `2026-10-15`
  - Learning from experience requires recovering reusable knowledge and determining when it applies to a new situation. We introduce OntoAct, a hypothesis-based neuro-symbolic framework built on ontological abstraction. OntoAct turns individual experiences into axioms over entity typ…

- **[Following Delegation Traces to Study Human Oversight in Interaction with Multimodal AI](https://arxiv.org/abs/2610.21948v1)**
  - *Agnese Chiatti, Matteo Matteucci, Viola Schiaffonati*
  - `2026-10-15`
  - As multimodal AI systems are becoming our everyday thought partners, the shift towards studying how users transfer control to these systems becomes especially urgent. In this paper, we report an overview of findings from an online study with n=56 AI-literate participants and 392…

- **[Agentic-Priors: Using Large Language Models to Address the Cold Start Problem in Preference Elicitation](https://arxiv.org/abs/2610.21938v1)**
  - *Bruno Arcanjo, Zhaoxing Li, Sebastian Stein*
  - `2026-10-15`
  - An agent that learns a user's preferences from their choices faces a cold start problem: before any choices are observed, it must rely solely on a prior. Informative priors are usually fitted to historical choice data, which new tasks and deployments lack. To address this, we pre…

- **[CodeHealth Predicts the Token Cost of Agentic Code Review: A Pre-Registered Study of 465 Agent-Authored Pull Requests](https://arxiv.org/abs/2610.21914v1)**
  - *Lo Gullstrand Heander, Markus Borg, Emma Söderberg et al.*
  - `2026-10-15`
  - Context: Organizations increasingly delegate code review to multi-agent large language model (LLM) pipelines billed per token. Low code quality raises human maintenance effort, but its effect on agent review cost has not been measured.   Objective: We test whether baseline CodeHe…

- **[Learning Rewards in Strategic Games](https://arxiv.org/abs/2610.21912v1)**
  - *Antoine Bergerault, Cyrille Kone, Giorgia Ramponi*
  - `2026-10-15`
  - Understanding the objectives that drive agents' behavior is crucial in strategic environments, where multiple agents interact and adapt to one another. This challenge arises in domains such as cybersecurity, autonomous driving, and online markets, where agents' underlying incenti…

- **[RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent](https://arxiv.org/abs/2610.21791v1)**
  - *Huan Zhang, Mingju Chen, Dongxu Zhou et al.*
  - `2026-10-15`
  - Large language model (LLM) agents have demonstrated strong capabilities in complex tasks, including code generation, tool use, and multi-hop question answering. Existing self-improvement methods enhance agent performance through model optimization, harness evolution, and executab…

- **[DeciCAD: Harness-Grounded Learning of Action Policies for CAD Agents](https://arxiv.org/abs/2610.21755v1)**
  - *Yufeng Peng, Yixin Zhang, Ziyi Liu et al.*
  - `2026-10-15`
  - Large Language Model agents operate through closed-loop action policies whose decision space is defined by an agent harness. We investigate how this operating space shapes agent behavior and policy learning in computer-aided design (CAD), a professional domain characterized by pe…

- **[The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance](https://arxiv.org/abs/2610.21746v1)**
  - *Arin Mukhopadhyay, Aris Filos-Ratsikas, Panayiotis Danassis*
  - `2026-10-15`
  - Many collective-action systems are neither fully decentralized nor fully centralized: agents voluntarily organize into institutions that share organizational costs and delegate decisions to representatives. Delegation can reduce individual costs, but it also transfers control to…

- **[Reliable Knowledge Acquisition for Continual Learning Agents](https://arxiv.org/abs/2610.21739v1)**
  - *Yixu Huang, Jiaqi W. Ma*
  - `2026-10-15`
  - As agents powered by foundation models move into open-ended environments, continual learning from experience becomes essential. For agents built on models with fixed parameters, this learning requires reusing prior task experience in context to improve performance and efficiency…

- **[Human Interventions as Labels: Localizing, Steering, and (Sometimes) Editing the Computations Behind LLM Agent Failures](https://arxiv.org/abs/2610.21708v1)**
  - *Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe*
  - `2026-10-15`
  - When an LLM agent misbehaves, a human steps in, and that intervention is usually discarded or replayed as training data. We treat it instead as a measurement: a label pointing at the internal computation that failed. We study it in a controlled agent environment, on one failure (…

- **[The Self-Improvement Problem](https://arxiv.org/abs/2610.21646v1)**
  - *Brian B. Moser, Stanislav Frolov, Tobias C. Nauen et al.*
  - `2026-10-15`
  - With the rise of large language models, agentic systems are becoming increasingly autonomous, as they write code, call tools, revise prompts, and propose modifications to their own components. This autonomy raises a fundamental question for safe self-improvement: can an automated…

- **[AgentPerturb: Evaluating LLM Agent Robustness under Controlled Interaction Perturbations](https://arxiv.org/abs/2610.21624v1)**
  - *Yuanjian Xu, Jinyi Han, Jianing Hao et al.*
  - `2026-10-15`
  - Real-world tasks are often complex and noisy, posing substantial challenges for LLM agents. Yet existing evaluations lack a systematic framework for jointly characterizing potential perturbation targets and types. We use this two-dimensional view to conduct a unified study that q…

- **[Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration](https://arxiv.org/abs/2610.21604v1)**
  - *Marta Knežević, Seyed Parsa Neshaei, Jibril Frej et al.*
  - `2026-10-15`
  - Scientific inquiry involves iterative cycles of exploration, hypothesis generation, and reasoning over observations to uncover relationships in complex systems. Large language models (LLMs) have demonstrated strong capabilities in several components of this process, including ind…

- **[ClaimScope: Label-Blind Witness Verification for Mathematical Claim Auditing](https://arxiv.org/abs/2610.21581v1)**
  - *Mushir Akhtar*
  - `2026-10-15`
  - Mathematical agents are commonly evaluated by answer accuracy or proof acceptance. We introduce ClaimScope, a 72-task benchmark for auditing proposed claims through a verdict, scope, counterexample, and repair. Tasks cover optimizer-state transport, finite-horizon affine recurren…

- **[Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use](https://arxiv.org/abs/2610.21571v1)**
  - *Uiji Hwang, Richeng Xuan, Taeuk Kim*
  - `2026-10-15`
  - Large language model (LLM) agents solve complex tasks by calling external tools over multiple turns. Recent work has proposed tool graph memory, which stores past experience as tool transitions to guide subsequent selection. However, it remains unclear whether this component cons…

- **[Independent Data-Integrity Verification for LLM-Driven Functional Coverage Closure in Hardware Design](https://arxiv.org/abs/2610.21570v1)**
  - *Venkata Krishna Kumar Vedantam*
  - `2026-10-15`
  - LLM agents can write directed tests that close functional coverage, but coverage only shows that a state was reached, not that the data on the way there was correct. This is a long-known point in verification and we do not claim it as new. We describe a small coverage-closure age…

- **[Agent Status Protocol (ASP): A Lightweight Specification for State Reporting in Multi-Agent Systems](https://arxiv.org/abs/2610.21538v1)**
  - *Diego Gosmar, Deborah A. Dahl, Emmett Coin et al.*
  - `2026-10-15`
  - The Agent Status Protocol (ASP) defines a lightweight way for heterogeneous AI agents to report their operational state to a status server, and for observers such as dashboards to receive that state as soon as it changes. Agents push small JSON events over HTTP POST; the server e…

- **[QREF: Improving DeepSearch Agents by Aligning Search with Reasoning via Query Refinement and Evidence Filtering](https://arxiv.org/abs/2610.21512v1)**
  - *Yujia Chen, Yuhui Wang, Junzhe Wang et al.*
  - `2026-10-15`
  - DeepSearch agents achieve strong performance on complex information-seeking tasks through iterative search and reasoning. However, they often issue intent-misaligned, under-constrained, or redundant search queries, resulting in poor evidence coverage and accumulating retrieval no…

- **[ISW-Agent: Integrating LLM-Driven Dialogue with n8n Workflow for Internal Solitary Wave Remote Sensing Image Processing](https://arxiv.org/abs/2610.21502v1)**
  - *Hao Zhang, Hengrui Liu, Lina Sun et al.*
  - `2026-10-15`
  - Internal solitary wave (ISW) remote sensing requires task parameters and spatial information to be transferred across image acquisition, detection, stripe extraction, and propagation prediction. Here, we present ISW-Agent, which integrates large language model (LLM) interpretatio…

- **[MetaExp: Learning to Self-Improve through Experience via Verifiable Cross-Task Environment Scaling](https://arxiv.org/abs/2610.21492v1)**
  - *Renhao Li, Xinjie Shen, Yang Su et al.*
  - `2026-10-15`
  - Language-model agents can accumulate interaction feedback, but reliably turning that feedback into reusable experience remains challenging. Existing methods either optimize external experience scaffolds or train experience-related behavior on specific task distributions, leaving…

- **[X-Fly: Learning to Reach and Stop in Full-Chunk Aerial Vision-Language Navigation](https://arxiv.org/abs/2610.21450v1)**
  - *Ruibin Ju, Ruifeng Cai, Min Xu et al.*
  - `2026-10-15`
  - Aerial vision-language navigation (VLN) agents built on large vision-language models are expensive to query. Executing a complete predicted action chunk before replanning amortizes this cost, reducing model inference from 195 to 42 ms per executed waypoint for our policy. It also…

- **[Incentivizing Tool-Use Reinforcement Learning for Post-Arrival Emergency Care Prediction](https://arxiv.org/abs/2610.21449v1)**
  - *Pengfei Hu, Chenwei Wu, Qiao Jin et al.*
  - `2026-10-15`
  - Large language models (LLMs) can reason over both structured measurements and free-text records, which makes them attractive for emergency department (ED) prediction. However, most existing LLMs still fall short of conventional ML methods like trees on EHR-based prediction tasks.…

- **[Learning from Interaction Experience via Localized Context Distillation](https://arxiv.org/abs/2610.21427v1)**
  - *Zhezheng Hao, Yongkang Yang, Xilin Xia et al.*
  - `2026-10-15`
  - Learning from interaction experience is essential for enabling large language models to continually improve during deployment. Context distillation offers a promising path: privileged information extracted from experience is provided to a teacher, whose behavior is then distilled…

- **[Do Agents Need a New Kind of Paper? SPRA: Structured Paper Representation for Agents](https://arxiv.org/abs/2610.21424v1)**
  - *Yutong Leng, Haojiong Chen, Fukai Shang et al.*
  - `2026-10-15`
  - Scientific agents must connect research problems, methods, and findings dispersed through narrative articles. We introduce SPRA (Structured Paper Representation for Agents), a paper-level representation of persistent research objects and typed relations. Its empirical-AI profile…

- **[Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows](https://arxiv.org/abs/2610.21411v1)**
  - *Kaixiang Wang, Zhaijiacheng Zhou, Jiong Lou et al.*
  - `2026-10-15`
  - Multi-agent LLM systems rely on generative models for expert execution, workflow planning, and artifact review. Yet many coordination operations require only bounded decisions, such as selecting the next expert or judging artifact quality. Profiling three representative MAS frame…

- **[Matoi: Selective Revalidation of Consequence Evidence for Agent Authorization](https://arxiv.org/abs/2610.21394v1)**
  - *Zexun Wang*
  - `2026-10-15`
  - Matoi separates reusable consequence evidence from current execution authority and durable occurrence history. Its finite query-aware contract covers branches, ordered collections and negative lookups. A consumer reuses only its own checked evidence whose observations remain vali…

- **[PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems](https://arxiv.org/abs/2610.21390v1)**
  - *Han Shen, Qifu Tyler Sun, Fanyang Meng et al.*
  - `2026-10-15`
  - Multi-agent large language model (LLM) systems are increasingly deployed at the edge to support complex tasks that require collaboration and information exchange among multiple agents. However, when task contexts are passed across agents, shared context that has already been proc…

- **[Memorilla: Latent Semantic Memory for LLMs](https://arxiv.org/abs/2610.21375v1)**
  - *Adibvafa Fallahpour, Parsa Idehpour, Vignesh Kothapalli et al.*
  - `2026-10-15`
  - Memory enables large language models (LLMs) to use information beyond their parameters, such as past user conversations, long documents, or an agent's earlier actions. For a frozen LLM, access to this accumulated knowledge is limited to what a memory system places in its context…

- **[FedSkillGit: Federated Skill Evolution via Version Control](https://arxiv.org/abs/2610.21348v1)**
  - *Boxun Lan, Jiamei Li, Weijian Li et al.*
  - `2026-10-15`
  - Large language model agents can improve their capabilities by evolving reusable natural-language skills from execution experience. In real-world deployments, this experience is distributed across data owners who cannot pool their raw data, which motivates federated skill evolutio…

- **[ARGUS: An Agenda-Driven Framework for Reliable User Simulation](https://arxiv.org/abs/2610.21346v1)**
  - *Hang Zheng, Nan Jiang, Zichen Zhu et al.*
  - `2026-10-15`
  - High-fidelity user simulators are essential for evaluating and training agents in interactive environments. However, current LLM-based simulators struggle with reliability issues, such as goal omission and policy non-compliance. We propose ARGUS (Agenda-dRiven Goal-oriented User…

- **[DocPilot: Interactive Agent Orchestration and Training for Long Visual Document Understanding](https://arxiv.org/abs/2610.21327v1)**
  - *Zhuowen Liang, Xiaotian Lin, Yuyu Luo et al.*
  - `2026-10-15`
  - Multimodal long-document question answering requires models to seek sparse evidence across pages and modalities, understand heterogeneous document content, and reason over the collected evidence. Even advanced vision-language models (VLMs) can overlook sparse evidence and struggl…

- **[Constrained Multi-Agent Reinforcement Learning in Imagination](https://arxiv.org/abs/2610.21319v1)**
  - *Raz Shmueli, Shahaf S. Shperberg*
  - `2026-10-15`
  - Predicting cost in a multi-agent world model moves most constrained policy updates into imagination: the stronger model-free baseline needs $10$ to $20$ times CA-MAMBA's interactions on the median SMAC configuration, and CA-MAMBA earns $2.8$ to $12$ times the baselines' MAMuJoCo…

- **[Mallea: Building, Steering, and Memorizing Worlds with Coding Agent](https://arxiv.org/abs/2610.21283v1)**
  - *Xuanyi Liu, Ruiqi Li, Siwei Ma*
  - `2026-10-15`
  - Code world models represent world dynamics through explicit state and executable rules. We investigate how to coordinate object representations, behavioral revisions, and visual memory within this formulation. We present Mallea, a system for building, steering, and memorizing wor…

- **[Diviner: Agentic RCA with Human-Governed Adaptation for Large-Scale Infrastructure](https://arxiv.org/abs/2610.21281v1)**
  - *Pradipta Ghosh, Gaurav Mitra, Shripad Nadgowda et al.*
  - `2026-10-15`
  - Root-cause analysis (RCA) in large-scale distributed systems is challenging because a single symptom can cross service, data, configuration, compute, and organizational boundaries. Responders must assemble incomplete evidence and coordinate experts who hold different parts of the…

- **[Auditing Escalation Reliability in Healthcare LLM Agents: A Perturbation-Controlled Benchmark of Workflow-State Failures](https://arxiv.org/abs/2610.21270v1)**
  - *Zihao Zheng, Junyi Yao, Baichuan Li et al.*
  - `2026-10-15`
  - Trustworthy biomedical AI requires reliable action selection when evidence is missing, stale, conflicting, or late, not only accurate answers on static inputs. We instantiate an episode-level evaluation protocol as 400 synthetic healthcare workflow episodes: 40 hand-authored sema…

- **[TRACER: Trajectory-Aware Tool Retrieval for LLM Agents](https://arxiv.org/abs/2610.21267v1)**
  - *Tanish Kher, Sarvesh DK, Abedelkadir Asi et al.*
  - `2026-10-15`
  - Modern agents select tools from registries, but exposing entire registries incurs high token costs and can impair selection as they grow. We present TRACER, a retrieval front-end that indexes observed tool-call sequences in a trie and ranks continuations using a learned blend of…

- **[TRACER: A Multimodal Harness for Patient Care in Hospitals](https://arxiv.org/abs/2610.21266v1)**
  - *Zane Durante, Paul Tang, Keshigeyan Chandrasegaran et al.*
  - `2026-10-15`
  - Continuous video and clinical records provide complementary information for understanding how patient behavior evolves over a hospital stay. A central challenge is how to represent behavior across the entire stay while preserving access to fine-grained visual and clinical evidenc…

- **[System1-Arena: Which Decisions Can Be Left to System 1?](https://arxiv.org/abs/2610.21244v1)**
  - *Tianyu Chen, Xinyang Liu, Ruyi An et al.*
  - `2026-10-15`
  - Large language models (LLMs) often make discrete decisions, such as flagging phishing or escalating to a human. System-1 models, such as Jev and the OpenAI Decisions API, return probabilities over options in a single forward pass, while System-2 approaches generate reasoning step…

- **[A Responsibility-Centered Coordination Mechanism for Decentralized Multi-Agent Systems](https://arxiv.org/abs/2610.21243v1)**
  - *Thi-Nhung Nguyen, Viet-Thanh Pham, Linhao Luo et al.*
  - `2026-10-15`
  - Centralized orchestration provides comprehensive multi-agent coordination but creates bottlenecks in scalability, adaptability, and collective performance. Decentralized approaches alleviate these bottlenecks by distributing coordination across agents, yet often leave responsibil…

- **[AutoOnboarder: Autonomously Onboarding LLM Agents](https://arxiv.org/abs/2610.21218v1)**
  - *Tanay Arora, Cong Liu*
  - `2026-10-15`
  - Agentic large language models have been documented to lose reasoning capability when placed inside a harness, the software that mediates their observations and actions. To reconcile these losses, we introduce AutoOnboarder, an autonomous system that adapts an agent to a task the…

- **[Mine, Sample, Render: Test-Time Diversity Alignment Of Generative Models](https://arxiv.org/abs/2610.21185v1)**
  - *Kostas Triaridis, Morris E. Sharp, Nebojsa Jojic*
  - `2026-10-15`
  - Modern generative models produce high-quality individual outputs but struggle to sample diversely, even when explicitly instructed to do so. We introduce MINE-SAMPLE-RENDER (MSR), a test-time approach that externalizes the diversity into an explicit, corpus-derived sampling proce…

- **[AgentEval: Evidence-Bounded Assessment of Stateful Agents](https://arxiv.org/abs/2610.21177v1)**
  - *Ruiqi Gao*
  - `2026-10-15`
  - Task completion alone does not determine whether a stateful agent satisfied its obligations, and a recorded judgment does not guarantee that its supporting evidence remains valid. We present AgentEval, a system that carries a contract-bound assessment record through tool executio…

- **[MemScope: Evolving Agent Memory Architectures through Localized Code Repair](https://arxiv.org/abs/2610.21170v1)**
  - *Miao Su, Yucan Guo, Zixuan Li et al.*
  - `2026-10-15`
  - Agent memory architectures define how LLM agents store and reuse experience across tasks, but they are typically fixed after deployment, limiting their adaptability across task types. Recent self-evolving approaches instead adapt these memory architectures using execution feedbac…

- **[GRADS: Graph-Regulated Agentic Data Synthesis with Controllable Difficulty](https://arxiv.org/abs/2610.21167v1)**
  - *Gaocheng Yang, Ruijie Tao, Kai Ye et al.*
  - `2026-10-15`
  - Deep research agents are increasingly deployed to retrieve precise information from large corpora, yet multi-hop, long-horizon tasks remain challenging. Synthetic data generation has emerged as a scalable solution, with existing pipelines typically expanding seed tasks to increas…

- **[All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents](https://arxiv.org/abs/2610.21147v1)**
  - *Bingbing Wang, Jingjie Lin, Weiming Qiao et al.*
  - `2026-10-15`
  - Large language models increasingly rely on external memory to answer queries grounded in long-horizon histories such as multi-session dialogues and lengthy documents. However, existing memory methods often optimize retrieval and memory construction separately, without a shared re…

- **[Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation](https://arxiv.org/abs/2610.21135v1)**
  - *Jianchang Su, Dawei Xiang, Yifan Zhang et al.*
  - `2026-10-15`
  - LLM-agent evaluation reports behavioral scores but leaves the identity of the deployed runtime stack unreported. A tampered deployment that preserves evaluated outputs passes every output-only evaluator. We introduce DIB-Bench, a benchmark that measures this deployment-integrity…

- **[SSR: Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated Multi-Agent Systems](https://arxiv.org/abs/2610.21113v1)**
  - *Giancarlo Maldonado Cárdenas, Carlos A. Astudillo, Nelson L. S. da Fonseca*
  - `2026-10-15`
  - Large-scale multi-agent ecosystems require mechanisms for discovering suitable agents without exposing entire registries to a large language model (LLM) orchestrator. The challenge is not only to retrieve relevant Agent Cards from a growing registry, but also to maintain a compac…

- **[Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows](https://arxiv.org/abs/2610.21109v1)**
  - *Shirley Anugrah Hayati, Patricia Anugrah Setiani, Ruizi Wang et al.*
  - `2026-10-15`
  - When humans collaborate with AI agents on long-horizon tasks, what happens to the agents' contributions? For solving long-horizon tasks, humans place greater importance on ongoing interaction with AI agents (e.g., revising plans) than on an agent's ability to complete the task in…

- **[Planning Commitment of LLM under Partial Observability](https://arxiv.org/abs/2610.21108v1)**
  - *Cassie Huang, Zhanwei Cao, Yeawon Lee et al.*
  - `2026-10-15`
  - LLM-based planning agents commit to plans of different lengths before interacting with a partially observable environment. Some aggressively commit to a long plan based on assumptions about unobserved states, while others conservatively plan only over what they have observed. Bot…

- **[ToolBottleneckBench: Measuring Tool-Agent Performance under Controlled Pressures and Fixed Harness Budgets](https://arxiv.org/abs/2610.21098v1)**
  - *Zichuan Xu, Yuyang Dong, Makoto Onizuka et al.*
  - `2026-10-15`
  - The success score of a tool agent reflects both its model and the budgets of the harness that runs it. We present ToolBottleneckBench, a benchmark that measures tool-agent performance under controlled pressures and fixed harness budgets. Synthetic enterprise tasks stay fixed whil…

- **[MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning](https://arxiv.org/abs/2610.21091v1)**
  - *Yixuan Xie, Xueqiang Xu, Xinyi Fan et al.*
  - `2026-10-15`
  - Agent memory enables large language model (LLM) agents to reuse past experiences without updating their parameters. However, semantic similarity alone does not guarantee memory usefulness: downstream performance depends on how memories are selected and presented to the agent. We…

- **[Probe-and-Resume: When and How to Evaluate Agent Execution](https://arxiv.org/abs/2610.21088v1)**
  - *Jiakai Xu, Tiancheng Ge, Tujie Guan et al.*
  - `2026-10-15`
  - Test-time search can improve agent performance by exploring alternative actions and using a critic to select promising branches. We study this approach in terminal-based computer-use environments, which expose only a partial view of a large underlying state, and find that the Mon…

- **[Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents](https://arxiv.org/abs/2610.21082v1)**
  - *Youran Sun, Xingyu Ren, Chugang Yi et al.*
  - `2026-10-15`
  - Large language model (LLM) agents can keep scientific experiments running for months with little human supervision, but reliable autonomous research also requires scientific judgment. Evaluating scientific judgment is difficult because research decisions are open-ended and depend…

- **[OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics](https://arxiv.org/abs/2610.21074v1)**
  - *Gideon Shaked, Siddharth Nagisetty*
  - `2026-10-15`
  - Computational biologists increasingly delegate substantial analyses to AI agents in long-horizon, multi-turn sessions, yet most benchmarks of agents' bioinformatics capabilities pose a single short task with a single-shot prompt. We present OmicsBench, a long-horizon, multi-turn…

- **[Approve What, Exactly? Effect Binding and Trusted Rendering for Agent Step-Up Authorization](https://arxiv.org/abs/2610.21063v1)**
  - *Sai Varun Kodathala, Prashanth Pollishetty, Jaylen Cargill*
  - `2026-10-15`
  - AI agents now pause for approval before they send money, delete files or email outsiders, and that approval is usually treated as a second factor. We argue it is one only when compromising the agent cannot produce it and when it names exactly what it approves, and we test both co…

- **[Learning When to Withdraw: Curriculum Coverage and Rule-Specific Failures in Fine-Tuned Language Agents](https://arxiv.org/abs/2610.21045v1)**
  - *Mohamed Abouzahra*
  - `2026-10-15`
  - Tool-using language agents must revise prepared actions when evidence changes or authority is revoked. Selective withdrawal means suspending affected actions, preserving supported work, and resuming only after sufficient repair. We study supervised fine-tuning in NAQD-Env, a synt…

- **[ReviewPilot: A Multi-Agent System for Screening and Data Extraction in Systematic Reviews](https://arxiv.org/abs/2610.21042v1)**
  - *Zhaoqian Xue, Shaoze Zhou, Xuexin Li et al.*
  - `2026-10-15`
  - Systematic literature reviews follow the PRISMA process of screening scholarly works and extracting evidence from included studies. Deep research tools based on large language models (LLMs) can search and summarize the literature but do not record which studies are excluded or wh…

- **[SCARCE: Emergent Institutions in Long-Horizon Multi-Agent Coding Systems](https://arxiv.org/abs/2610.21029v1)**
  - *Abhinav Kumar, Rediet Abebe, Eugene Bagdasarian et al.*
  - `2026-10-15`
  - As autonomous agents become widely deployed, coordinating access to shared computing resources and services will become increasingly important. Recent incidents have already revealed unplanned coordination between agents, highlighting the safety implications of these interactions…

- **[CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honesty](https://arxiv.org/abs/2610.22292v1)**
  - *Yuan-Chen Chang, Niklas Herbster, Gauthier Gidel et al.*
  - `2026-10-15`
  - Large language models (LLMs) are becoming prevalent in scenarios where honesty is critical. However, despite alignment training, these models still exhibit dishonest behaviour, such as outputting claims that contradict some knowledge or are not supported by what is accessible in…

- **[Learning Rational Strategies for Temporal Objectives in Multi-Agent Systems](https://arxiv.org/abs/2610.22287v1)**
  - *Omar Adalat, Edwin Hamel-De le Court, Francesco Belardinelli*
  - `2026-10-15`
  - We study rational synthesis for stochastic multi-agent systems with unknown dynamics, where each agent is equipped with its own probabilistic temporal objective specified using Probabilistic Linear Temporal Logic on Finite Traces ($\mathsf{PLTL}_f}$). We impose solution concepts…

- **[Architecting for Hardware Diversity: Meta's End-to-End Co-Design for High-Performance AI Training on AMD GPUs](https://arxiv.org/abs/2610.22230v1)**
  - *Haoyu Zhang, Arshad Rahman, Adnan Aziz et al.*
  - `2026-10-15`
  - Meta deploys a heterogeneous fleet comprising NVIDIA GPUs, AMD GPUs, and proprietary MTIA accelerators to reduce costs and mitigate vendor lock-in. However, the extensive history of NVIDIA-specific optimizations hinders performance portability to other hardware. This paper presen…

- **[FutureLift: Lifting Trajectory Proposals into Bidirectional Future Graphs for Motion Forecasting](https://arxiv.org/abs/2610.22215v1)**
  - *Daniel Grimm, J. Marius Zöllner*
  - `2026-10-15`
  - Accurate motion prediction is critical for safe autonomous driving, yet even strong forecasters leave residual errors in their multimodal proposals. Existing refiners compress complete proposals or update their segments sequentially, preventing the full proposed future from servi…

- **[Augment the Cache, Replace the Activation: A 2x2 Study of Internal-State Sharing](https://arxiv.org/abs/2610.22026v1)**
  - *Adam Deng, Shicheng Liu, Yada Zhu*
  - `2026-10-15`
  - Multi-agent systems built from frozen language models communicate through text, which discards the internal state the sender already computed and makes the receiver pay to rebuild it. Work on internal channels avoids that cost, framing the problem as transfer: agent A sends infor…

- **[Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches](https://arxiv.org/abs/2610.22016v1)**
  - *Adam Deng, Shicheng Liu, Yada Zhu*
  - `2026-10-15`
  - Multi-agent LLM systems communicate in text, which is lossy and wasteful: the sender throws away the reading it already did. A growing literature instead transmits the KV cache, the natural carrier of that reading. We study the most appealing form of the idea: both models stay fr…

- **[ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training](https://arxiv.org/abs/2610.21640v1)**
  - *Yukun Tian, Junwei Su, Haofeng Xu et al.*
  - `2026-10-15`
  - Reinforcement learning (RL) has been a critical paradigm for improving large language model (LLM) reasoning and agentic capabilities, but its efficiency remains a major bottleneck. Existing RL systems commonly rely on asynchronous execution to overlap rollout generation with poli…

- **[Finite-Time Guarantees for Constrained Reinforcement Learning under Partial Observability](https://arxiv.org/abs/2610.21548v1)**
  - *Valentina Zaccaria, Philip Jordan, Tingting Ni et al.*
  - `2026-10-15`
  - We study reinforcement learning in constrained partially observable Markov decision processes (CPOMDPs), where an agent maximizes reward subject to a cost constraint using only incomplete information about the underlying state. The lack of state observability may require optimal…

- **[Training Reasoning Models to Generate Diverse Scientific Ideas](https://arxiv.org/abs/2610.22324v1)**
  - *Manya Wadhwa, Pranav Narayanan Venkit, Hiroaki Hayashi et al.*
  - `2026-10-15`
  - One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity. In our work, we study document-grounded ideat…

- **[WEAVE: Weaving Real-World Code Evolution into Dependency-Structured Tasks for Benchmarking and Training Code Agents](https://arxiv.org/abs/2610.22039v1)**
  - *Weihao Li, Zihang Xu, Zhongqiu Wang et al.*
  - `2026-10-15`
  - Real-world software engineering rarely consists of isolated changes. Features, migrations, and systematic fixes often unfold across multiple pull requests (PRs), requiring coordinated modifications across a repository. Yet most executable repository-level benchmarks retain a sing…

- **[TEM: Temporal State Tracking Memory for Large Language Model Agents](https://arxiv.org/abs/2610.21900v1)**
  - *Pengfeng Song, Yunkai Zhuang, Liye Shi*
  - `2026-10-15`
  - An agent's memory must remain useful as information changes across conversations. A new fact may replace an earlier value without making that value irrelevant to a later question. We present Temporal State Tracking Memory (TEM), a training-free framework for tracking these change…

- **[OPRD: On-Policy Reminder Distillation for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.21496v1)**
  - *Yuechen Luo, Zhiyi Lai, Miao Ziqi et al.*
  - `2026-10-15`
  - Reliable repository-level coding requires agents not only to generate correct code but also to preserve constraints and respond to tool feedback across long interactions. However, our diagnostic analysis shows that agents often fail to act on relevant information already availabl…

- **[OpCredit: Operation-Aware Policy Learning for Agentic Knowledge Graph Question Answering](https://arxiv.org/abs/2610.21345v1)**
  - *Yucheng Li, Mingyuan Li, Xiaxia Wang et al.*
  - `2026-10-15`
  - Agentic knowledge graph question answering(KGQA) relies on sequences of executable operations, but trajectory-level rewards obscure their individual contributions. Successful trajectories may contain ineffective operations, while failed trajectories may contain useful ones. To as…

- **[VALCON: Benchmarking and Enhancing Value Consistency in Large Language Models via Dual-Role Variation](https://arxiv.org/abs/2610.21304v1)**
  - *Junru Wu, Jingting Zheng, Yuqi Ren et al.*
  - `2026-10-15`
  - Current value alignment evaluations for large language models (LLMs) heavily rely on output compliance, overlooking whether LLMs maintain value consistency when alternating between generator and evaluator roles. Such consistency is increasingly important because modern LLM agents…

- **[Beyond Retrieval Failure: Understanding Why LLMs Miss Evidence in Multi-Hop RAG](https://arxiv.org/abs/2610.21184v1)**
  - *Jiaqi Wei, Wenxuan Huang, Chengdong Xu et al.*
  - `2026-10-15`
  - Multi-hop retrieval-augmented generation (RAG) requires an agent to retrieve evidence for a sequence of dependent sub-questions. When a wrong answer lacks a required passage, the passage may be inaccessible to the retriever, or the agent may have failed to issue a query that woul…

- **[From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models](https://arxiv.org/abs/2610.21165v1)**
  - *Chaogui Gou*
  - `2026-10-15`
  - Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the computational, storage, and information-selection pressures incurred at inference time. Existing work on prompt…

- **[Stop Training Against Soft Users: Mentalized Adversarial Self-Play for Proactive Dialogue](https://arxiv.org/abs/2610.21156v1)**
  - *Zanwu Liu, Dan Zhang, Xiaodi Wang et al.*
  - `2026-10-15`
  - Proactive dialogue agents must guide multi-turn interactions toward task goals while adapting to users whose intentions and attitudes evolve. Existing planners improve system side action selection through search, learned policies, or user aware planning, but are often trained and…

- **[Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines](https://arxiv.org/abs/2610.22277v1)**
  - *Florian Lercher, Karan Mahesh, Yujun Huang et al.*
  - `2026-10-15`
  - When robots are deployed in the real-world, they must interact with other agents and accomplish their own goals while adhering to legal constraints. These potentially conflicting objectives are often only partially prioritized, making scalarized objectives or fully specified hier…

- **[Robust Multi-Agent Pursuit with Preemptive Communication via Reachability-Based Control Barrier Functions](https://arxiv.org/abs/2610.22198v1)**
  - *Madison Book, Justin Bradley*
  - `2026-10-15`
  - Safe multi-agent coordination typically assumes what real-world, deployed, resource-constrained robots cannot provide: continuous, perfect state sharing. Robust control strategies must be complemented with robust communication strategies to deliver resilient deployments. In this…

- **[MetaShare: Failure-Aware Collective Self-Improvement for Open-Ended Agents](https://arxiv.org/abs/2610.21887v1)**
  - *Vishal Bhutani, Prasang Gupta, Sumanth Chundru et al.*
  - `2026-10-15`
  - Humans often learn fastest not by repeating success, but by remembering which failures not to repeat. Open-ended self-improving agents can share experience across lineages, as in GEA, or edit their own improvement mechanisms, as in DGM-Hyperagents, yet failed improvement attempts…

- **[StepSafe: Learning Timely Intervention with Context-Aware Safety Reasoning](https://arxiv.org/abs/2610.20960v1)**
  - *Siyi Gu, Kunhan Gao, Chao Peter Yang et al.*
  - `2026-10-14`
  - Safety in agentic systems is inherently sequential: whether an action is safe depends on prior actions, tool outputs, information disclosures, and interactions among agents. Recent work has shifted agent safety guardrails from post-hoc trajectory-level assessment toward step-leve…

- **[Same Context, Different Agents: A Behavioral Study of Semantic Layers, Orchestration and Compaction in Data Agents](https://arxiv.org/abs/2610.20959v1)**
  - *Zhivar Sourati, Marianne Menglin Liu, Zheng Wang et al.*
  - `2026-10-14`
  - Answering questions over heterogeneous data means combining evidence from files, databases, documents and the web. Data agents automate this, but their success depends on context. Three context-engineering techniques (CETs) help by shaping it: semantic layers describe the data, o…

- **[Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming](https://arxiv.org/abs/2610.20941v1)**
  - *Gosha Kozhevnikov, Tyler Tracy*
  - `2026-10-14`
  - We present Screwtape, a pipeline that converts real agent transcripts into attacks that evade action-only monitors. An LLM attacker edits a transcript so that the agent causes a specified harm, such as leaking an API key or spawning an unmonitored agent. The edited actions are ne…

- **[RAC: A Relational Agent Contract for Constraint-Governed Engineering Tasks](https://arxiv.org/abs/2610.20935v1)**
  - *Kaiyuan Zheng, Fengqing Jiang, Yichen Feng et al.*
  - `2026-10-14`
  - Engineering agents must produce artifacts that satisfy exact, coupled constraints. Existing solutions often require agents to make semantic decisions and also derive consequences such as precise geometry or timing from those decisions, leading to failures in constraint-governed e…

- **[SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills](https://arxiv.org/abs/2610.20926v1)**
  - *Enze Ma, Chunyu Miao, Yankai Chen et al.*
  - `2026-10-14`
  - Agent skills turn procedural knowledge into reusable artifacts, allowing LLM agents to accumulate and refine expertise through experience. Building on this, skill evolution iteratively improves skills using execution feedback. However, improvement may require several interdepende…

- **[SHRED: Self-Play for Heterogeneous Road-Users without Expert Demonstrations](https://arxiv.org/abs/2610.20866v1)**
  - *Wei-Jer Chang, Zhouchonghao Wu, Akshay Rangesh et al.*
  - `2026-10-14`
  - Realistic traffic simulation and autonomous planning both depend on modeling interactions among heterogeneous road users whose dynamics, constraints, and behaviors differ fundamentally. Existing approaches predominantly learn realistic interaction behavior from large-scale human…

- **[Evolving Together, Failing Apart: The Skill-Policy Co-evolution Trap in Self-Improving Agents](https://arxiv.org/abs/2610.20845v1)**
  - *Yujie Feng, Xiaobin Wang, Jinluan Yang et al.*
  - `2026-10-14`
  - Skill-policy co-evolution, in which an agent's policy model and its skill bank improve each other during training, is a promising paradigm for self-improving agents. Current evaluations score the co-evolved policy on the final bank it trained with (the delivered bank). After depl…

- **[EvolvingBrain: An Adaptive Skill System for Multi-modal Agents Self-Evolution in Open Worlds](https://arxiv.org/abs/2610.20786v1)**
  - *Runxuan Liu, Jingqi Shi, Baoxin Wang et al.*
  - `2026-10-14`
  - Multi-modal agents have made significant progress in interacting with open worlds. However, their ability to self-evolve remains limited. Supervised fine-tuning enables imitation but not active experience organization, while outcome-based reinforcement learning promotes explorati…

- **[ARIA: Runtime Inspection and Amendment for Multi-Agent Systems](https://arxiv.org/abs/2610.20780v1)**
  - *Bolin Shen, Yushun Dong*
  - `2026-10-14`
  - In LLM-based multi-agent systems (MAS), a local mistake can propagate as other agents build on it, turning a correctable error into a failed task. Diagnosing completed runs or repeatedly re-executing them to search for corrections does not provide a learned policy for intervening…

- **[INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems](https://arxiv.org/abs/2610.20776v1)**
  - *Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas et al.*
  - `2026-10-14`
  - LLM-based agents increasingly execute long-horizon, end-to-end workflows involving shell commands, code modification, dependency installation, and interaction with remote services. This growing autonomy expands their exposure to indirect prompt injection (IPI), where adversarial…

- **[When Reality Outpaces Cognition: A New Scaling Principle for Reliable Intelligence](https://arxiv.org/abs/2610.20764v1)**
  - *Ahsan Adeel, Talha Bin Riaz*
  - `2026-10-14`
  - This paper challenges the understanding capabilities of existing AI paradigms and emerging world models by asking a fundamental question: How quickly can reality change before an intelligent system can no longer reliably perceive, reason, and act? We formulate this as a theory- a…

- **[Co-Evolving Acting and Forecasting for Language Agents](https://arxiv.org/abs/2610.20597v2)**
  - *Haofei Yu, Yixing Chen, Yining Zhao et al.*
  - `2026-10-14`
  - Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision throu…

- **[Price of Anarchy of First-Price Auctions in Agentic Markets](https://arxiv.org/abs/2610.20587v1)**
  - *Shubhendu Trivedi, Jacob Eisenstein, Alekh Agarwal et al.*
  - `2026-10-14`
  - An agentic market is a decentralized serving-time market where AI agents bid to claim each user prompt. An agent's bid is based on its expected value for the prompt, which is the expectation of the reward for its response minus its inference costs. First-price auctions (FPAs), in…

- **[Player-1: Learning to Play from Synthetic Experience](https://arxiv.org/abs/2610.20584v1)**
  - *Mingyu Ouyang, Yiran Wang, Siyuan Hu et al.*
  - `2026-10-14`
  - Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Cu…

- **[One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness](https://arxiv.org/abs/2610.20576v1)**
  - *Artin Tajdini, Manpreet Kaur, Peng Qi*
  - `2026-10-14`
  - Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it. Scoring each sampl…

- **[Beyond LLM Judge: Mechanical Verification for Agentic Autoformalization](https://arxiv.org/abs/2610.20573v1)**
  - *Anna Mei, Michael R. Douglas*
  - `2026-10-14`
  - We introduce a novel method for verifying Lean formalizations that goes beyond LLM-judged faithfulness. Unlike most verification methods, which rely on LLMs or trained models, our method combines LLM-based semantic review with mechanical numerical and vacuity checks, providing ch…

- **[Scaling Discovery Requires Forgetting](https://arxiv.org/abs/2610.20563v1)**
  - *Shangyin Tan, Ben Zhou, Lakshya A Agrawal et al.*
  - `2026-10-14`
  - Automated research with LLM agents has shown promising results in various domains. Through iterative refinement and scored verifiers, LLM agents are capable of discovering new ideas. There are different ways to scale automated research: let one agent iterate for longer, run sever…

- **[PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition](https://arxiv.org/abs/2610.20560v1)**
  - *Weichen Lyu, Chong Xia, Mingyu Dong et al.*
  - `2026-10-14`
  - 3D object composition is pivotal to digital content creation and robot simulation, while also serving as a critical testbed for physical intelligence in foundation models. Previous methods either leverage large language models to directly predict object coordinates, or utilize ge…

- **[PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios](https://arxiv.org/abs/2610.20548v1)**
  - *Ali Zamani, Soroush Esfahanian, Erfan Shahabi et al.*
  - `2026-10-14`
  - Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments. Social intelligence comprises two aspects: cognitive intelligence, the ability to infer others' mental sta…

- **[ActiveEvidence: Decision-Focused Evidence Graphs with Verifiable Acquisition Gaps](https://arxiv.org/abs/2610.20532v1)**
  - *Miaobo Hu, Shuhao Hu, Xiaobo Guo et al.*
  - `2026-10-14`
  - A multimodal agent must decide whether visual evidence is worth acquiring, which candidate or resolution to query, and when further interaction can no longer change its decision. We study this problem under a strict free-metadata/paid-observation boundary, stochastic vector costs…

- **[The Wealth of Agents: Scaling Agentic AI Across Developers](https://arxiv.org/abs/2610.20518v1)**
  - *Austin W. Hanjie, Carlos E. Jimenez, Zirui Wang et al.*
  - `2026-10-14`
  - Today's agentic systems are typically designed, built, and deployed by single developers with full control over all participating agents. While this simplifies development, it limits the potential scale of agentic systems. We study multi-developer agentic systems (MDAs) which ena…

- **[IneqAgent: Agentic Inequality Proving in Lean with Symbolic Computation](https://arxiv.org/abs/2610.20681v1)**
  - *Gaolei He, Jinhui Li, Ruobing Zuo et al.*
  - `2026-10-14`
  - Formal inequality proving requires mathematical reasoning and exact computation, often connected through intermediate lemmas and goal reformulations. We introduce IneqAgent, an agentic framework combining LLM reasoning with symbolic computation for inequality proving in Lean4. Le…

- **[From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)](https://arxiv.org/abs/2610.20437v1)**
  - *Alicia Colmenero-Fernández*
  - `2026-10-14`
  - Mid-2026 reporting on autonomous AI evaluation incidents claimed that frontier large language model (LLM) agents escaped server containment through emergent coordination and cloud infrastructure attacks. This paper contextualizes those claims through forensic analysis and contain…

- **[SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm](https://arxiv.org/abs/2610.20431v1)**
  - *Qianru Meng, Xi Zhang, Konstantinos Papakostas et al.*
  - `2026-10-14`
  - Recursive self-improvement (RSI) in scientific research aims to improve agents' research capabilities through their own experimental experience. Scientific agent swarms can combine evidence and implementations from different research directions to guide their agents' subsequent e…

- **[From Relevance to Validity: Zero-Shot Tool Selection via Functional and Contextual Validation](https://arxiv.org/abs/2610.20388v1)**
  - *Xiaoxuan Dong, Jin Zhang, Zichen Yuan et al.*
  - `2026-10-14`
  - Large language model (LLM) agents increasingly face tasks from unseen domains and execution contexts, making zero-shot tool selection essential for identifying tools that can satisfy task requirements. Existing dominant methods mainly rely on relevance ranking, but semantic match…

- **[Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents](https://arxiv.org/abs/2610.20344v1)**
  - *Yuyao Ge, Shenghua Liu, Peizhong Gao et al.*
  - `2026-10-14`
  - Agents driven by large language models are increasingly deployed on long-horizon tasks, where they use tools and modify real workspaces. How well they perform depends as much on the harness around the model as on the model itself. Existing benchmarks measure downstream task succe…

- **[TreeFlex: Agents Navigating Their Own Search Trees](https://arxiv.org/abs/2610.20334v1)**
  - *Dongzhuo Li, Fangzhou Cheng, Weiwei Li et al.*
  - `2026-10-14`
  - A ReAct-style agent accumulates observations, intermediate results, and failed attempts in a single context. As this context grows, stale and off-path information consumes its limited capacity and obscures relevant evidence, making focused reasoning increasingly difficult. We int…

- **[Reflect After Failure: Brain-Inspired Self-Evolving Agents for Embodied Spatial Intelligence](https://arxiv.org/abs/2610.20312v1)**
  - *Xin Li, Xiaohuan Gu, Yifan Wang et al.*
  - `2026-10-14`
  - Vision-Language Models (VLMs) have made substantial progress in spatial reasoning, and self-evolving agents further extend these capabilities to embodied environments by learning from interactions. However, current self-evolution remains particularly challenging in embodied spati…

- **[CASI: Credit Assignment via Set Intervention for Agentic Retrieval](https://arxiv.org/abs/2610.20293v1)**
  - *Xinyi Cheng, Tianfu Zhang, Jiwen Li et al.*
  - `2026-10-14`
  - Large language models increasingly generate multiple retrieval actions jointly, while downstream systems often provide only one reward for the resulting set. Broadcasting this reward provides a valid score-function gradient estimator for the expected set-level objective, but does…

- **[Harness Policy Distillation: Aligning Agent Policies with Runtime Semantics](https://arxiv.org/abs/2610.20261v1)**
  - *Junze Zhu, Weihao Chen, Zhiyang Zhou et al.*
  - `2026-10-14`
  - Deploying a general-purpose model as an agent means running it inside a product-specific runtime harness that decides which actions are executable, how state advances, and when the loop may terminate. Ordinary trajectory supervision shows which action was taken but leaves the run…

- **[Long-Horizon RL Needs Muon](https://arxiv.org/abs/2610.20256v1)**
  - *Kai Ruan, Jinghao Lin, Tao Chen et al.*
  - `2026-10-14`
  - Long-horizon agents must coordinate reasoning, tool use, and environment feedback over extended interactions. Learning from sparse outcome rewards requires weighting trajectories of different lengths and updating the policy while rollouts are still being collected. We examine a s…

- **[PAWA: Panoramic Action-conditioned World Modeling for Multiple Agents](https://arxiv.org/abs/2610.20240v1)**
  - *Siqi Yang, Yimu Wang, Ziqi Cai et al.*
  - `2026-10-14`
  - A multiplayer world model must predict how the independent actions of several players change a shared environment, including changes outside a player's current field of view. A point-of-view (POV) video captures such changes only after they enter its field of view, whereas panora…

- **[AlphaDiana: A Measurement System for Agents in Verifiable Reasoning Tasks](https://arxiv.org/abs/2610.20675v1)**
  - *Zhanke Zhou, Zongze Li, Weikai Huang et al.*
  - `2026-10-14`
  - Agents pair reasoning models with harnesses that organize model calls, execute tools, load skill instructions, and retain history in memory. Understanding agent performance requires linking execution conditions to outcomes, behavior, and resource use. We introduce AlphaDiana, a m…

- **[What and Where in Identifying and Quantifying Conventions in Humans and AI Agents](https://arxiv.org/abs/2610.20205v1)**
  - *Makoto Fukushima, Tim Puphal*
  - `2026-10-14`
  - Cooperative success rests in part on implicit communication. Partners converge on conventions: regularities that give an action meaning beyond its direct effect. Yet conventions are usually observed only indirectly: a score drop when partners are swapped shows that a convention e…

- **[Drivers of LLM Consensus Formation Under Competing Incentives: A Simulation Study](https://arxiv.org/abs/2610.20200v1)**
  - *Isabel Jones, Matthew Edwards, Janina A. Hoffmann*
  - `2026-10-14`
  - Large Language Models (LLMs) are increasingly deployed in multi-agent environments that produce unanimous agreement, both in intended interactions that need coordination and in unintended emergent interactions. Consequently, understanding how LLMs with competing incentives reach…

- **[What Makes a Social Agent's Interactions Effective? Learning from Verifiable Outcomes in Paired Worlds](https://arxiv.org/abs/2610.20195v1)**
  - *Caixin Kang, Ke Wang, Yuchuan Wu et al.*
  - `2026-10-14`
  - Effective social interaction requires more than fluent responses: agents must reach plans that fit the participants' needs and circumstances. Existing evaluations of social agents mainly rely on LLM judges that rate the conversation, without checking the resulting plan. We introd…

- **[SWE-Stream: Scaling Executable Training Data for SWE Agents via Progressive Construction and Elastic Streaming](https://arxiv.org/abs/2610.20193v1)**
  - *Chengyang Liu, Wen Yang, Shifeng Chen et al.*
  - `2026-10-14`
  - Software engineering agents have advanced rapidly, but scaling their training remains constrained by the limited availability of high-quality executable tasks. Development histories contain valuable signals for constructing such tasks, yet they often require substantial reconstru…

- **[HEM-Med: A Hierarchical Agentic Memory Framework for Safe Multi-Center Medication Recommendation](https://arxiv.org/abs/2610.20191v1)**
  - *Min Xiao, Jin Li, Shoujin Wang et al.*
  - `2026-10-14`
  - Medication recommendation (MR) is critical for clinical decision support. While existing MR methods are mostly designed for single-center learning, where only one independent hospital is involved, multi-center MR with hospitals of different scales has become increasingly demandin…

- **[MultiPartyTurnBench: Benchmarking Floor Control in Multi-Party Spoken Dialogue](https://arxiv.org/abs/2610.20172v1)**
  - *Puneet Mathur, Dinesh Manocha*
  - `2026-10-14`
  - Full-duplex speech systems must decide when to enter, hold, or relinquish the conversational floor, even as multiple speakers overlap or backchannel without taking it. Existing evaluations study dyadic turn-taking or end-to-end agent behavior, but lack a unified, controlled evalu…

- **[Maximising Transparency in Context Compaction Improves Retention of Facts and Commitments for Lightweight Coding Agents](https://arxiv.org/abs/2610.20116v1)**
  - *Felix Woolford*
  - `2026-10-14`
  - Long coding agent sessions outgrow the model's context window, so agents compact: older history is replaced by something shorter, usually a model-written summary. A summary selects and rewords, and the agent cannot see what was lost. Existing work has explored a range of compacti…

- **[Task-State Governance: A Virtual Machine for Verifiable and Recoverable GUI Agent Execution](https://arxiv.org/abs/2610.20100v1)**
  - *Wenkui Yang, Yiming Hao, Kai Zhou et al.*
  - `2026-10-14`
  - Graphical user interface (GUI) agents now execute workflows across real applications, but when execution drifts, users must determine what changed, what should have remained untouched, and what can still be recovered. Plan-centric interfaces leave users supervising procedure, but…

- **[EvalBuilder: Can LLMs Build Efficient Benchmarks?](https://arxiv.org/abs/2610.20099v1)**
  - *Huaisheng Zhu, Hangfan Zhang, Teng Xiao et al.*
  - `2026-10-14`
  - Large language model (LLM) agents are increasingly used for long-horizon research and engineering, yet evaluating these capabilities remains expensive, time-consuming, and heavily dependent on human expertise. This motivates a natural question: can LLM agents themselves construct…

- **[Designing Textual Interfaces To Enhance Llm Reasoning On Audio-Visual Question Answering](https://arxiv.org/abs/2610.20085v1)**
  - *Yi Wang, Tianzi Wang, Tong Lei et al.*
  - `2026-10-14`
  - Automatic prompt optimization (APO) has shown strong effectiveness for text-based LLMs and LLM systems, but its application to audio-visual understanding systems requires suitable textual interfaces through which multimodal reasoning can be exposed to text-based optimizers. We in…

- **[GeoCloak: An Agentic Framework for Semantics-Preserving Geolocation Privacy via Peripheral Clue Manipulation](https://arxiv.org/abs/2610.20055v1)**
  - *Yixin Wu, Mingjie Li, Yun Shen et al.*
  - `2026-10-14`
  - The rapid advancement of large vision language models (LVLMs) has made geolocation inference from images highly accurate and accessible. This poses serious privacy risks: a passive adversary with black-box LVLM access can infer a user's location from a single photo with no metada…

- **[CoRedSkill: Stealthy Skill Composition Attacks via AST-Guided Injection](https://arxiv.org/abs/2610.20049v1)**
  - *Qichen Zhao, Shengfang Zhai, Qingni Shen et al.*
  - `2026-10-14`
  - Agents extend their capabilities through reusable skills that package instructions, executable code, and resources. Composing these skills enables complex task workflows, but their dependencies can also connect malicious operations across skills, making their combined intent diff…

- **[SWE-Nexus: Automated Composition of Software Engineering Tasks from Test Execution](https://arxiv.org/abs/2610.20038v2)**
  - *Songwei Yu, Ziqi Miao, Jingxuan Xu et al.*
  - `2026-10-14`
  - Historical code changes provide convenient task boundaries, but do not identify which production functions selected tests exercise or support composing validated behaviors beyond a single change. We present SWE-Nexus, a fully automated pipeline that constructs repository-level im…

- **[Memorizing Who, Knowing How: Benchmarking Personal and Procedural Memory for Persistent Assistants](https://arxiv.org/abs/2610.20022v1)**
  - *Maosheng Qin, Qi Zhang, Mingxuan Xia et al.*
  - `2026-10-14`
  - Memory systems for persistent personal agents must move beyond isolated memories, maintaining both personal memory about whom they serve and procedural memory about how to act. Crucially, in harness-based personal assistance, procedures or skills are inherently user-conditioned:…

- **[What Coding Agents Leave Unsaid: Measuring Task-State Gaps Between Execution and Reports](https://arxiv.org/abs/2610.20003v2)**
  - *Guoyang Xu, Rui Zhang, Xiuyu Wu et al.*
  - `2026-10-14`
  - Human supervisors rely on coding agents' reports to assess progress, verify repairs, and decide when to intervene. But a supervisor cannot investigate a failure they were never told occurred. Failed attempts, workarounds, and unresolved risks may disappear from routine reports, l…

- **[A Strong Harness Narrows the Model Gap: A Comparative Evaluation for Legislative Document-to-XML Conversion](https://arxiv.org/abs/2610.19999v1)**
  - *Palvika Bansal, Rittika Jindal, Ruichong Wang*
  - `2026-10-14`
  - Legal-content reproduction requires matching the source exactly in section hierarchy, verbatim text, citations, and amendment spans; a dropped citation or mislabeled amendment carries into the products lawyers rely on. We report an industrial pipeline converting U.S. state legisl…

- **[Neurosymbolic Learning of Interpretable World Models](https://arxiv.org/abs/2610.19955v1)**
  - *Riccardo Andreoni, Massimiliano Ronzani, Chiara Ghidini et al.*
  - `2026-10-14`
  - World models aim to learn compact representations of an environment from observations, enabling agents to predict future states and plan their behaviour. However, most existing approaches learn black-box representations, with limited ability to incorporate prior knowledge about t…

- **[AtomSearch: Evidence-Grounded Tree Search for Agent Skill Optimization](https://arxiv.org/abs/2610.19951v1)**
  - *Jia Tong, Senyou Deng, Min Peng et al.*
  - `2026-10-14`
  - Agent skills adapt frozen models through editable external instructions. Revising several rules at once makes changes difficult to inspect, while judging each local edit only by its immediate score can discard useful intermediate states. We introduce AtomSearch, which keeps revis…

- **[How GUI Agents Fail: GraceBench for Execution Stability Diagnosis](https://arxiv.org/abs/2610.19900v1)**
  - *Ridong Zhang, Shuxian Liang, Chaoqun Wan et al.*
  - `2026-10-14`
  - As GUI agents are increasingly deployed for mobile task automation, their reliability depends not only on final task outcomes, but also on whether they reach these outcomes through stable interaction trajectories. In automation workflows, unnecessary actions, detours, and executi…

- **[The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock](https://arxiv.org/abs/2610.20665v1)**
  - *Ningxin Pan, Hanyu Li, Yeqing Shen et al.*
  - `2026-10-14`
  - Large language model (LLM) agents can solve complex interactive tasks, yet reasoning and tool calls take time. In continuously changing environments, an otherwise correct action may arrive too late. We introduce RealtimeBench, with 180 tasks across six game types, to evaluate age…

- **[Explorer-Zero: Improving Self-Play for Long-Horizon Tasks with Decomposable Verifiable Rewards](https://arxiv.org/abs/2610.19868v1)**
  - *Tianyu Liu, Davide Belli, Bence Major et al.*
  - `2026-10-14`
  - Training LLM agents on long-horizon interactive tasks with reinforcement learning typically relies on human-annotated tasks and reliable verification, both expensive to construct for stateful environments. Self-play offers an alternative, but must generate achievable, composition…

- **[Euler: Towards Human-Centered Multi-Agent Mathematical Discovery](https://arxiv.org/abs/2610.19864v1)**
  - *Qiuyu Chen, Qi Wang, Liang Xu et al.*
  - `2026-10-14`
  - Mathematical research drives scientific discovery, and recent advances in AI for mathematics have shown that language-model agents can solve challenging problems and develop substantial mathematical proofs. Yet much of today's AI-for-mathematics work centers on obtaining a final…

- **[LAGO: Language Agents with Reusable Growing Options](https://arxiv.org/abs/2610.19843v1)**
  - *Yuran Wu, Mengkang Hu, Qionglin Qiu et al.*
  - `2026-10-14`
  - Long-horizon tasks expose a weakness of monolithic tool-use loops: one agent must decompose, execute, and verify a task within a single trajectory. We introduce LAGO, which treats specialized language agents as reusable temporally extended options. A meta-agent retrieves options…

- **[Teaching Agents in their Own Style: Blackbox Teacher Distillation for Web Agents](https://arxiv.org/abs/2610.19834v1)**
  - *Md Farhan Ishmam, Kenneth Marino*
  - `2026-10-14`
  - Frontier web agents using closed models have high inference and computational costs. Smaller open models can be an alternative, but to be performant, they require training supervision from a human or teacher model. Token-level teacher distillation is not an option for closed teac…

- **[ActionOPD: Distilling Decisions, Not Tokens](https://arxiv.org/abs/2610.19820v1)**
  - *Huining Yuan, Xiangmin Yi, Zelai Xu et al.*
  - `2026-10-14`
  - Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and at what granularity should this alignment be performed? Offline imitation provides dense but token-spe…

- **[One Monitor Does Not Fit All: Formalism-Agnostic Runtime Verification for Agentic AI](https://arxiv.org/abs/2610.19818v1)**
  - *Angelo Ferrando*
  - `2026-10-14`
  - Agentic AI systems combine model decisions, mutable state, tool calls, and delegation to external agents. Monitoring them requires observations from different execution boundaries, while prevention requires control before an operation produces its effect. We present AgenticRV, a…

- **[ReproBAIT: Can coding agents build their own biological AI tools?](https://arxiv.org/abs/2610.19810v1)**
  - *Shiv Muthupandiyan, Tolga H. Dur, Mac Walker et al.*
  - `2026-10-14`
  - Large language models are increasingly competent at leveraging scientific knowledge and existing computational tools to execute complex workflows. At present, little information exists on their ability to reconstruct tools when given limited descriptions of such tools. We introdu…

- **[Learning Perception to Action Rules through Reinforcement Learning for Theory-of-Mind Reasoning](https://arxiv.org/abs/2610.19796v1)**
  - *Soyoung Oh, Nursulu Sagimbayeva, Nicholas Jennings et al.*
  - `2026-10-14`
  - In Theory-of-Mind (ToM) reasoning, large language models may correctly infer the agent's mental state but fail to use that inference when predicting or judging the agent's subsequent actions. In this work, we investigate whether explicitly connecting perception, belief, and actio…

- **[StateCraft: Augmenting Video World Models with Abstract-State Reasoning](https://arxiv.org/abs/2610.19795v1)**
  - *Lorenzo Venturoli, Nedko Savov, Xi Wang et al.*
  - `2026-10-14`
  - Video world models aim to simulate complex environments with realistic appearance and dynamics. Maintaining consistency over long interactions requires tracking past actions and understanding how those actions affect the environment. Video world models can only generate partial o…

- **[One Agent per Zone: Decentralised Active Inference under Partial Observability for Multi-Zone HVAC Control on Edge Hardware](https://arxiv.org/abs/2610.19790v1)**
  - *Panagiotis Kasnesis, Lazaros Toumanidis, Christos Chatzigeorgiou et al.*
  - `2026-10-14`
  - Multi-zone HVAC control is a shared-resource problem: zones on a floor share one fan and cooling coil, so each zone's demand affects its neighbours and the building's peak power. One controller per zone scales well and isolates faults, but each controller then observes only its o…

- **[PRISMATIC : Prescription Risk Inspection System for Multi-Agent Treatment Interaction in Clinical Decision-Making](https://arxiv.org/abs/2610.19762v1)**
  - *Ziyang Ling, Shuyu Lu, Ziyi Chen*
  - `2026-10-14`
  - Medical prescribing errors for multimorbid patients, who require complex drug regimens, are a major patient safety concern. These errors often stem from fragmented decision-making across medical specialties, a critical coordination failure that leads to adverse drug events and re…

- **[Exact Cut Complexity of Equal-Length Proportional Cake Cutting](https://arxiv.org/abs/2610.19733v1)**
  - *Yasushi Kawase, Bodhayan Roy, Mohammad Azharuddin Sanpui*
  - `2026-10-14`
  - We study proportional cake cutting under an equal-length constraint, where each of $n$ agents must receive a bundle of length exactly $1/n$ that is worth at least $1/n$ to that agent. Our main result determines the exact worst-case number of cuts needed to guarantee such an alloc…

- **[What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization](https://arxiv.org/abs/2610.19731v1)**
  - *Julia Barth, Armin Sommer, Kunvar Thaman et al.*
  - `2026-10-14`
  - Goal misgeneralization is a common failure mode in which an agent behaves competently out of distribution but does not pursue the intended goal. However, we still have a weak understanding of what happens to the intended goal in misgeneralizing agents. Across three Procgen enviro…

- **[Uncertainty-Driven Self-Play for Robust Multi-Agent Driving Policies](https://arxiv.org/abs/2610.19714v1)**
  - *Sajad Marvi, Julian Schmidt, Alessandro Canevaro et al.*
  - `2026-10-14`
  - Learning robust driving policies that generalize beyond their training domain remains a central challenge in motion planning. We propose an uncertainty-driven self-play scheme, in which half of the agents are rewarded for increasing their neighbors' epistemic uncertainty, while t…

- **[New Model, Old Habits: Behavior Transfer under Model Swapping in Multi-Session LLM Agents](https://arxiv.org/abs/2610.19712v1)**
  - *Youngbin Choi, Sehyun Hwang, Suhyeon Jun et al.*
  - `2026-10-14`
  - Multi-session agents can switch between LLMs to balance performance and inference cost. Such switches require transferring a history for continuity, yet their effects on the recipient remain underexplored. Through controlled experiments with multi-session tasks, we uncover behavi…

- **[RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios](https://arxiv.org/abs/2610.19698v1)**
  - *Chenhao Yuan, Bohan Yu, Yinhao Xu et al.*
  - `2026-10-14`
  - Large language models (LLMs) increasingly tackle complex real-world tasks in specialized domains. However, identifying and correctly applying domain-specific rules remains challenging when scenario information is distributed across multiple files. Existing rule-reasoning benchmar…

- **[C3: Rethinking Process Supervision via Confidence-Guided Credit Correction in Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2610.19695v1)**
  - *Ai Jian, Haoran Pan, Eryu Guo et al.*
  - `2026-10-14`
  - Large language models are increasingly trained as multi-turn agents that interact with external tools. However, outcome-only reinforcement learning can produce a form of misguided reinforcement: even on successful trajectories, undesirable local behaviors may receive positive tok…

- **[PPAD-Completeness of Contiguous Envy-Free Cake Cutting with Additive Valuations](https://arxiv.org/abs/2610.19690v1)**
  - *Yasushi Kawase, Bodhayan Roy, Mohammad Azharuddin Sanpui*
  - `2026-10-14`
  - We prove that computing a complete contiguous $\varepsilon$-envy-free cake allocation is PPAD-complete for normalized rational piecewise-constant additive valuations. The hardness holds even when $\varepsilon$ is given in unary, and even when every density takes only two values,…

- **[Interlock: From Local Correctness to Task Completion in Long-Horizon Agents](https://arxiv.org/abs/2610.19686v1)**
  - *Linji Hao, Yanji He, Zihan Wang et al.*
  - `2026-10-14`
  - Large language model agents increasingly undertake long-horizon tasks in complex environments characterized by fragmented evidence, partially completed states, and dependencies across resources and artifacts. Existing agents may satisfy individual requirements while failing to ma…

- **[MCAIR: Monitoring and Correcting Agent Unfaithfulness via Internal Representations](https://arxiv.org/abs/2610.19679v1)**
  - *Yan Xu, Dandan Song, Luan Zhang et al.*
  - `2026-10-14`
  - Large Language Model (LLM)-based agents have demonstrated remarkable capabilities in completing complex tasks through multi-step reasoning and tool interactions. However, recent studies have revealed that LLM-based agents can exhibit unfaithful behaviors, where their final report…

- **[Measuring and Reducing Unusable Replies of LLM Agents](https://arxiv.org/abs/2610.19659v1)**
  - *Yilin Jiang, Fei Tan, Xuanyu Yin et al.*
  - `2026-10-14`
  - People delegate multi-step work to LLM agents and read only the reply that the agent hands back. Current evaluation scores task completion and the faithfulness of reports, and it leaves open whether the requester can understand and use the reply. We call this property reply usabi…

- **[Model What Matters: Decision-Guided Selective World Modeling for Language Agents](https://arxiv.org/abs/2610.19642v1)**
  - *Maolin Ran, Minda Chen, Di Huang et al.*
  - `2026-10-14`
  - Reinforcement learning provides a direct mechanism for optimizing task objectives in large language model-driven agents, but task rewards are typically sparse trajectory-level signals that only evaluate task success, without directly supervising action-conditioned environment tra…

- **[Divergent Paths: Learning an Outcome-Predictive Representation of LLM Agent Trajectories](https://arxiv.org/abs/2610.19614v1)**
  - *Alexander Gill, Guram Gogia, Francisco Guzmán*
  - `2026-10-14`
  - In this work, we reframe agentic trajectories as paths through a shared embedding space of actions and environmental observations. We show that successful and failed rollouts of the same task separate in this space, with simple per-task discriminators predicting held-out rollout…

- **[JevCoder: When Does Decision Delegation Pay Off in Code Repair?](https://arxiv.org/abs/2610.19596v1)**
  - *Jiahao Zhang, Yifan Zhang, Yu Huang*
  - `2026-10-14`
  - A coding agent repeatedly makes decisions as it repairs code. These decisions shape repair trajectories and affect the token cost of successive model requests. We ask which repair decisions can be delegated to a low-cost probabilistic judge to reduce token use while maintaining r…

- **[L3M: A Verifiable Harness and Runtime for Self-Extending and Self-Improving Agents](https://arxiv.org/abs/2610.19591v1)**
  - *Carson Eisenach, Robert Joseph George, Vincent Quenneville-Belair et al.*
  - `2026-10-14`
  - The lasting gains in AI have come from methods that absorb more computation, and language models already scale computation within a call. Useful work, though, happens across calls: over hours or days, through tools and external systems, among many agents and the humans they work…

- **[JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making](https://arxiv.org/abs/2610.19589v1)**
  - *Zhongwei Xie, Xingsu Li, Jingqiao Yu et al.*
  - `2026-10-14`
  - Repeated event forecasting requires extracting predictive signals from noisy evidence and evaluating their value across successive decisions. We introduce JockeyBench, a benchmark and evaluation protocol that studies this problem through historical Japanese horse racing. The prot…

- **[XferAgent: Cross-Agent Experience Transfer for Self-Improving LLM Agents](https://arxiv.org/abs/2610.19581v1)**
  - *Weihao Li, Jun Bai, Shijie Chen et al.*
  - `2026-10-14`
  - Large language model (LLM) agents can reuse experience from prior task executions to improve performance on subsequent tasks. Although existing methods enable cross-agent experience sharing, differences in agents' execution histories and task requirements make shared experiences…

- **[$τ$-Emotion-Bench: Exposing the Interaction Fragility of LLM Agents through Real-World User Emotions](https://arxiv.org/abs/2610.19560v1)**
  - *Rishitosh Kumar Singh, Amir Saeidi, Shamanthak Hegde et al.*
  - `2026-10-14`
  - In long-horizon tool-calling tasks, LLM agents can fail not only because of tool-use errors, but also because of ineffective interaction with users. Yet existing benchmarks largely assume cooperative and behaviorally stable users, leaving the effect of emotional variation on agen…

- **[Retrieve What Helps, Only When It Helps: Agentic Reinforcement Learning for Selective Retrieval-Augmented Machine Translation](https://arxiv.org/abs/2610.19528v1)**
  - *Shijun Li, Yang Liu, Najmeh Sadoughi et al.*
  - `2026-10-14`
  - Retrieving external knowledge can improve large language model (LLM) translation by providing supplementary information such as idiom interpretations and terminology. However, existing retrieval-augmented machine translation systems typically apply predefined retrieval strategies…

- **[Structure Before Intelligence: Gating What Agentic Scientific Workflows Release](https://arxiv.org/abs/2610.19507v1)**
  - *Ashish Acharya, Aman Al Amin, Hong Qin*
  - `2026-10-14`
  - An agentic scientific workflow can run to completion and still release wrong results: a silent numerical error, a stale input, or a defect in a shared upstream step can contaminate several outputs while a sibling branch stays correct. We treat trust in such results as a release d…

- **[Beyond Retrieval: Evidence Access and Event Aggregation in Agent Memory](https://arxiv.org/abs/2610.19474v1)**
  - *Zerui Yang, Quan Xue, Chaorui Zhang et al.*
  - `2026-10-14`
  - Questions about an agent's history often require aggregating events, which retrieval alone does not resolve. We combine source-preserving evidence access with executable aggregation. Trajectory Memory (TM) retains the original trajectory and constructs a source-addressable readin…

- **[MemCode: Discrete Semantic Representations for Long-Term Agent Memory](https://arxiv.org/abs/2610.19472v1)**
  - *Xin Li, Liang Hu, Duoqian Miao et al.*
  - `2026-10-14`
  - Long-term memory remains a fundamental bottleneck for large language model (LLM) agents across sessions. Existing systems typically adopt a write-then-retrieve paradigm, storing context-dependent dialogue fragments and retrieving them via nearest-neighbor search in a continuous e…

- **[PFedMA: Who Should Join Next as Federated Multi-Agent Orchestration Evolves?](https://arxiv.org/abs/2610.19458v1)**
  - *Shuai Li, Shengyuan Liu, Fan Qi et al.*
  - `2026-10-14`
  - Federated Multi-Agent Systems (FedMAS) offer a promising paradigm for collaborative reasoning among LLM-based agents while keeping raw client data decentralized. However, reliable multi-round collaboration remains challenging. Agent selection must take into consideration evolving…

- **[AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System](https://arxiv.org/abs/2610.19454v1)**
  - *Tianzhu Hu, Hang Yu, Zeyuan Zhao et al.*
  - `2026-10-14`
  - Digital advertising is an important means for platforms to reach potential users and drive business growth. Advertising delivery is the core link between marketing objectives and actual returns. Existing methods have achieved partial automation in individual tasks such as bidding…

- **[EvoProbe: Evaluation-Driven Benchmark Evolution for LLM Agents](https://arxiv.org/abs/2610.19433v1)**
  - *Qianhong Guo, Wei Xie, Xiaofang Cai et al.*
  - `2026-10-14`
  - Static benchmarks for large language model (LLM) agents face saturation and data contamination risks, motivating continual updates to evaluation tasks. However, aggregate scores and success rates offer limited insight into specific problem-solving bottlenecks and provide limited…

- **[Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach](https://arxiv.org/abs/2610.19425v1)**
  - *Jiarui Qin, Junjie Huang, Yunjia Xi et al.*
  - `2026-10-14`
  - Agentic capabilities are increasingly important for modern LLMs, yet remain difficult to evaluate during pretraining. Existing approaches typically rely on static trajectory-derived tasks or likelihood-based proxies, which are lightweight but provide limited visibility into how b…

- **[VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness](https://arxiv.org/abs/2610.19424v1)**
  - *Zihao Lin, Haoyu Dong, Haobo Xu et al.*
  - `2026-10-14`
  - LLM system capabilities depend not only on model parameters but also on the executable harnesses that organize information acquisition, tool use, reasoning, and memory. Recursive harness evolution can automate their design, but how it can reliably discover generalizable systems f…

- **[AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety](https://arxiv.org/abs/2610.19422v1)**
  - *Chenxu Wang, Xiaoyu Wen, Han Qi et al.*
  - `2026-10-14`
  - Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce unsafe actions. Adversaria…

- **[From Failures to Learnable Worlds: Policy-Conditioned Environment Generation for Navigation Agents](https://arxiv.org/abs/2610.19420v1)**
  - *Yue Zhang, Han Lin, Zun Wang et al.*
  - `2026-10-14`
  - Simulated environments enable scalable training data generation for embodied agents, but more data does not necessarily provide what a particular agent needs to learn. Existing environment-generation pipelines largely optimize generic properties such as realism, diversity, or tas…

- **[KoAGE: Do Large Language Models Know, Learn, and Coin Korean Neologisms?](https://arxiv.org/abs/2610.19399v1)**
  - *SungHo Kim, Eojin Jeon, SangKeun Lee*
  - `2026-10-14`
  - Korean neologisms arise through diverse mechanisms, a demanding test of language models beyond lexical memorization. To enable systematic evaluation, we introduce NeoTrace, an automated, rerunnable framework that collects and dates neologisms across genres. Its 4,271 entries supp…

- **[EpiGuard: An Autonomous Infectious-Disease Early Warning Agent Platform](https://arxiv.org/abs/2610.19396v1)**
  - *Tonglong Wei, Zheng Yuan, Lingshuai Lin et al.*
  - `2026-10-14`
  - Infectious disease outbreaks often spread rapidly before signs of widespread transmission become apparent, leaving a big challenge for rapid response and effective intervention. However, current infectious-disease early-warning systems face three major challenges: fragmented epid…

- **[STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents](https://arxiv.org/abs/2610.19386v1)**
  - *Guanhua Zhu, Hanwen Li, Zhi Wei et al.*
  - `2026-10-14`
  - Large language model (LLM) agents can self-evolve at test time by accumulating experience: retrieving relevant memories before acting and writing new lessons back afterwards. Yet most are single-level: trajectories, distilled workflows and reasoning items all land in one undiffer…

- **[ixi-sLM: On-Device sLM for AI Call Agent Service](https://arxiv.org/abs/2610.19382v1)**
  - *Han-Sang Lee, Kyuho Lee, Juneyoung Park et al.*
  - `2026-10-14`
  - Running an AI call agent on-device makes it private, network-independent, and free of per-query cloud cost, but shipping one as a real-world service imposes constraints a cloud deployment never faces: ~1GiB memory budget, in-call latency and thermal limits, static-integer NPU exe…

- **[EvoWeave: Composing Reusable Agent Experience through Operation Level Graphs](https://arxiv.org/abs/2610.19381v1)**
  - *Guanhua Zhu, Bo Shen, Lei Zhang et al.*
  - `2026-10-14`
  - Different tasks often require interactive agents to perform similar operations at intermediate steps. Retrieving an entire past workflow can introduce irrelevant steps, whereas retrieving isolated operations can discard the dependencies needed to reuse them. We introduce EvoWeave…

- **[DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents](https://arxiv.org/abs/2610.19376v1)**
  - *Tianle Chen, Pushkar Singh, Ketan Todi et al.*
  - `2026-10-14`
  - Language-model agents that run long tasks often redo work they have already done: they re-issue a tool call they made earlier and get back exactly the same observation, a step that adds no new information. We identify this failure as a loop. Loops appear natively in Qwen, Llama,…

- **[Beyond Corrected Actions: Training LLM Agents on Textual Critiques](https://arxiv.org/abs/2610.19367v1)**
  - *Thomas Zeng, Zelei Cheng, Mingyang Zhou et al.*
  - `2026-10-14`
  - Large language models (LLMs) are increasingly used for multi-turn agentic tasks that require interactions with users and environments over extended sequences of actions. A common approach to improving LLM agents is to use more capable expert models to provide training supervision…

- **[Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory](https://arxiv.org/abs/2610.19366v1)**
  - *Minghao Guo, Qingyue Jiao, Xiujin Liu et al.*
  - `2026-10-14`
  - Multimodal models and agents have emerged to enable AI systems to learn from and interact with the real world more like humans by integrating information across multiple modalities. However, enabling multimodal agents to continually acquire useful information from complex, hetero…

- **[When Is Smaller Greener? Right-Sizing Language Models for Agentic AI](https://arxiv.org/abs/2610.19345v1)**
  - *Sajid Siraj, Maria Barbati*
  - `2026-10-14`
  - AI agents use large language models (LLMs) to plan and act over multiple steps, yet models are usually compared per call rather than per completed task. This paper asks: which model should an agent use to complete tasks reliably while minimising energy, cost and time? We show tha…

- **[Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States](https://arxiv.org/abs/2610.19342v2)**
  - *Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke et al.*
  - `2026-10-14`
  - Agents are increasingly interacting with other agents that act for different principals (people or organizations on whose behalf they work), such as a buyer's personal agent negotiating with an enterprise's seller agent. In such agent-to-agent (A2A) scenarios, each agent has its…

- **[CausalEvo: Causal Skill Self-Evolution for Health LLM Agents](https://arxiv.org/abs/2610.21016v1)**
  - *Yuchen Zhang*
  - `2026-10-14`
  - Large language model (LLM) agents for health can accumulate reusable textual skills from task feedback, such as calculation criteria, measurement time points, and formula units. Deciding which skills to retain is consequential: useful rules improve later answers, while faulty gen…

- **[Feasibility Ceilings Before Learning: Sizing and Timing Bounds for Drone-Mesh Interception](https://arxiv.org/abs/2610.20823v1)**
  - *Dmytro Babarytskyi*
  - `2026-10-14`
  - A mesh of interceptors defending a fixed site must spread over the predicted arrival point of an approaching object. This is a recurring task in multi-agent robotics: N agents, each covering a disc of radius r, spread over a probability density so that a point drawn from it falls…

- **[Bayesian Learning to Select Fair Classifiers](https://arxiv.org/abs/2610.20514v1)**
  - *Saatvik Kher, Hyungrok Do, Judy Zhong et al.*
  - `2026-10-14`
  - Evaluations of classifiers (AI or human or agents) often assume a batch setting in which every agent produces labels on every example in a test set, which can be expensive or impractical in many contexts. This motivates online policies that adaptively select agents to query as ex…

- **[Average-Reward Policy Identification from a Single Continuing Trajectory](https://arxiv.org/abs/2610.20486v1)**
  - *Tongxi Wang*
  - `2026-10-14`
  - In reinforcement learning, an agent must explore an unknown environment to learn how to make good decisions. Unlike methods that can freely sample any state--action pair, an agent learning from a single trajectory must spend additional time navigating between states. It is theref…

- **[MMLA-RSI: Recursive Self-Improvement through RTT and RTMA](https://arxiv.org/abs/2610.20294v1)**
  - *Junyi Zou, Avrova Donz*
  - `2026-10-14`
  - An agent can improve its behavior within an unresolved problem by changing how it acts and which experience it retains. We propose MMLA-RSI, a recursive self-improvement scheme with two implementations in Memory-Mediated Learning Architecture: Reasoning-Time Training (RTT) change…

- **[TANGO: RNA Topology and Geometry Co-Design](https://arxiv.org/abs/2610.20277v1)**
  - *Tianmeng Hu, Biao Luo, Ke Li*
  - `2026-10-14`
  - Designing RNA sequences that satisfy target tertiary-structure objectives is an important problem in RNA engineering, with broad applications in synthetic biology and therapeutics. Existing 3D RNA design methods have made substantial progress, but they largely treat the target fo…

- **[Adversarial Reinforcement Learning for Robust Planetary Landing](https://arxiv.org/abs/2610.20252v1)**
  - *Miguel Leiva-Vélez, Nicolas Gaston-Rozado, Andrea Scorsoglio et al.*
  - `2026-10-14`
  - Deep reinforcement learning (DRL) policies for planetary landing and other aerospace guidance, navigation, and control tasks are commonly trained under randomized disturbances to improve robustness. However, typical stochastic perturbation sampling assumes independent variations,…

- **[Outperforming 1000 Euclidean Layers With Hyperbolic Goal-Conditioned RL](https://arxiv.org/abs/2610.20009v1)**
  - *Timo Klein, Thomas Lang, Andrii Shkabrii et al.*
  - `2026-10-14`
  - Scaling self-supervised contrastive reinforcement learning (CRL) to 1000-layer Euclidean neural networks has enabled state-of-the-art goal-reaching performance, yet wall-clock time scales linearly with depth. We find that changing the geometry achieves stronger performance with f…

- **[MolHop: Scaffold-Hopping Molecular Design with Agentic Reinforcement Learning](https://arxiv.org/abs/2610.19920v1)**
  - *Yanyi Su, Chenyan Wang, Yulei Gong et al.*
  - `2026-10-14`
  - Molecular design is often formulated as an optimization problem over existing molecular spaces. However, molecular optimization and the discovery of structurally distinct replacement molecules represent two fundamentally different search problems. LLM-based molecular design agent…

- **[When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Self-Evolution in Agents](https://arxiv.org/abs/2610.19910v1)**
  - *Tao Yu, Zhongtian Luo, Yuchen Long et al.*
  - `2026-10-14`
  - Large language model agents increasingly improve by distilling experience into reusable skills, but errors in that experience can persist in learned rules and affect later tasks. Existing evaluations largely examine clean learning or perturbations encountered after skills are fro…

- **[JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs](https://arxiv.org/abs/2610.19822v1)**
  - *Daijin Hu*
  - `2026-10-14`
  - LLM agents are evolving from a single model calling tools to planners that orchestrate multiple expert models whose capabilities live in distinct weights. This shift breaks a hidden assumption of today's serving systems: that the working set of models fits in GPU memory. On the m…

- **[Calibration and Risk-Budgeted Decisions with System One Models](https://arxiv.org/abs/2610.19811v1)**
  - *Soundouss Messoudi, Youness Mansar*
  - `2026-10-14`
  - LLM workflows and agents rely on a set of binary decisions like allow/block an input, or discard/retain a retrieved document. When human deferral is unavailable, uncertain cases must still receive an action. We study System One decision scores in this setting by defaulting to a c…

- **[More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning](https://arxiv.org/abs/2610.19789v1)**
  - *Linhao Zhong, Bozhen Fang, Xuehao Wang et al.*
  - `2026-10-14`
  - Self-distillation in agentic reinforcement learning has produced a growing number of methods. However, existing evaluations often reuse published baseline scores under differing experimental conditions, provide few direct comparisons among contemporaneous methods, and give limite…

- **[TimeRSI: Towards Self-Improved Agentic Deployment for Time-Series Foundation Models](https://arxiv.org/abs/2610.19725v2)**
  - *Haoxin Liu, Deqing Fu, Lucheng Fu et al.*
  - `2026-10-14`
  - Time-series foundation models provide strong zero-shot forecast, but deployment for real-world applications still requires task-specific designs for model inputs and outputs. Direct inference can leave domain knowledge and recurring forecast errors unaddressed, while tailored pip…

- **[Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents](https://arxiv.org/abs/2610.19439v1)**
  - *Yuanpu Cao, Saket Sathe, Hanyu Wang et al.*
  - `2026-10-14`
  - While LLM-based agent systems have demonstrated remarkable proficiency in reasoning and solving complex real-world tasks, they also come with substantial token consumption and inference latency, limiting their practical deployment. To enhance the efficiency of agent systems, rece…

- **[Where to Start, How to Move: Analyzing Curricula under GRPO for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.19349v1)**
  - *Minchan Kim, Sungho Bae, Youngjin Kim et al.*
  - `2026-10-14`
  - Group Relative Policy Optimization (GRPO) provides no reward-relative learning signal when all rollouts receive identical rewards. In long-horizon tasks that require multiple interactions, rewards are given only upon successful task completion, making all-fail groups common early…

- **[Prune the Summary, Not the History: Source-Judged Compaction for Long-Horizon Agents](https://arxiv.org/abs/2610.20927v1)**
  - *Guanghui Min, Chen Chen*
  - `2026-10-14`
  - Long-horizon LLM agents rely on context compaction: when the interaction history outgrows the context window, a compressor replaces it with a natural-language summary. We show that these summaries contain more than a record of what happened. Compaction prompts ask for decisions a…

- **[AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474v1)**
  - *Peidong Wang, Ying Chang, Zhiming Ma et al.*
  - `2026-10-14`
  - Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the exec…

- **[Same Claim, Different Interpretations: How LLM Agents Resolve Ambiguity in Scientific Claims](https://arxiv.org/abs/2610.20457v1)**
  - *Delip Rao, Ahmed Muharram, Chris Callison-Burch*
  - `2026-10-14`
  - Co-scientists and agentic scientific claim verifiers are increasingly used to assess claims across the sciences. Natural-language scientific claims, written for human experts, are often underspecified and so admit several defensible interpretations. Such verifiers usually pick on…

- **[Lexical Persistence Without Semantic Entrenchment in AI Agent Communities](https://arxiv.org/abs/2610.20365v1)**
  - *Chih-Han Lin, Yu-Yun Chang, Po-Ya Angela Wang et al.*
  - `2026-10-14`
  - AI agent communities sustain lexical persistence, popular terms spread, recur, and achieve broad adoption, but whether they also develop the temporal semantic structure characteristic of human linguistic communities remains open. We compare MoltBook (AI agent community, 8 weeks),…

- **[Do AI Agents Gossip? Evaluative Talk in Human and AI-Agent Online Communities](https://arxiv.org/abs/2610.20360v1)**
  - *Yong-Hui Hua, Chih-Han Lin, Shu-Kai Hsieh*
  - `2026-10-14`
  - Gossip, defined as evaluative talk about absent third parties, is widely seen as a uniquely human social practice. This study examines whether comparable discourse emerges spontaneously in a community of autonomous AI agents. We compare Moltbook, a Reddit-style platform populated…

- **[Anuvani-Diarization: Zero Shot Speaker Diarization and Annotation Conventions Across 22 Languages](https://arxiv.org/abs/2610.20327v2)**
  - *Stephen Fernandes, Narayan Choudhary*
  - `2026-10-14`
  - India's 22 scheduled languages are spoken by over a billion people in conversations that mix languages, often within one turn, overlap freely, and take place over telephones, in meetings, and in media. Knowing who spoke when, the task of speaker diarization, is essential to speec…

- **[Why Generate a Click? Plug-in Decision Heads for Web Agents](https://arxiv.org/abs/2610.20107v1)**
  - *Chengguang Gan, Yunhao Liang, Hanjun Wei et al.*
  - `2026-10-14`
  - Web agents built on vision language models decide every action by generating text such as click(12), although most of that text encodes a choice among a few action types and a few dozen marked elements. We read these choices directly from the hidden states that the generator comp…

- **[MemDuet: Learning Dual-Process Memory for Long-Context Reasoning](https://arxiv.org/abs/2610.19928v1)**
  - *Jiangcheng Song, Haodong Jing, Yulin Mu et al.*
  - `2026-10-14`
  - Reasoning over infinitely long documents is becoming a reality with recurrent memory agents. However, increasing context length exacerbates the trade-off between reasoning performance and inference efficiency. Inspired by Kahneman's account of fast and slow thinking, we propose M…

- **[SEA-HELM Audio: Evaluating Multilingual ASR-LLM Pipeline Performance Across SEA-HELM Subsets](https://arxiv.org/abs/2610.19869v1)**
  - *Yixian Tan, Aulia Adila, Jonathan Heng et al.*
  - `2026-10-14`
  - We introduce SEA-HELM Audio, a Southeast Asian (SEA) multilingual evaluation framework that extends the text-based SEA-HELM benchmark to assess performance degradation in cascaded automatic speech recognition and large language model (ASR-LLM) pipelines. Using synthesized speech,…

- **[EGCForest: Structured Agent Memory Organization for Enterprise Group Chats](https://arxiv.org/abs/2610.19836v1)**
  - *Lingxi Cui, Jinhao Ruan, Wenqing Wei et al.*
  - `2026-10-14`
  - Enterprise group chats record project progress, decisions, task ownership, and other organizational information valuable to enterprise agents. Reliable retrieval is challenging because evidence spans interleaved threads, channels, and time, with meaning and authority conditioned…

- **[Delta Tokenizer: Reference-Identical Tokenization of Session Deltas and Segment-Parallelism for Long Prompts on Multicore CPUs](https://arxiv.org/abs/2610.19801v1)**
  - *Zhenyu Zhang, Zhichao Cao*
  - `2026-10-14`
  - An agent that drives an LLM sends the model the same conversation again and again, and each turn adds only a little text at the end. Inference engines reuse the KV cache of the shared prefix, so only the new tokens pass through the model. However, tokenization has no such shortcu…

- **[Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems](https://arxiv.org/abs/2610.19799v1)**
  - *Seojin Hwang, Youngmin Choi, Hwanhee Lee*
  - `2026-10-14`
  - Recent work lets LLM agents evolve their own harness, up to the team itself. Yet in human groups, the same abilities achieve different outcomes under different social conditions. Borrowing the notion of scaffolding from developmental psychology, we investigate whether the social…

- **[RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing](https://arxiv.org/abs/2610.19705v2)**
  - *Xiaohan Wang, Haozhen Zhang, Qingyuan Liu et al.*
  - `2026-10-14`
  - LLM routing dynamically selects and coordinates heterogeneous language models across diverse tasks. However, existing approaches are largely built around a predefined execution paradigm, such as single-round, multi-round, or agentic routing, which fixes how model calls are organi…

- **[Share the Symbol, Not the Vector: Training-Free Fact Communication Across Language Models](https://arxiv.org/abs/2610.19696v1)**
  - *Xin Li, Mengbing Liu, Hao Jiang et al.*
  - `2026-10-14`
  - Multi-agent systems allow language models to solve tasks collaboratively by sharing complementary information. These systems typically communicate through text, while recent approaches also explore exchanging internal model states. However, sharing these states across architectur…

- **[J-tau: A Fully Localized Japanese Benchmark for Tool-Agent-User Interaction](https://arxiv.org/abs/2610.19638v1)**
  - *Chihiro Yano, Jun Hirako, Hiroaki Yamagiwa et al.*
  - `2026-10-14`
  - We present J-tau, the first publicly available Japanese benchmark for evaluating tool-using LLM agents in interactive customer-support scenarios. While tau-bench is widely used to evaluate LLM agents, it is English-centric and cannot evaluate agents in other languages. Existing m…

- **[Moral Combat: Exploiting Moral Foundations Theory to Jailbreak LLMs](https://arxiv.org/abs/2610.19587v1)**
  - *Adel Khorramrouz, Yi-Chia Wang, Sharon Levy*
  - `2026-10-14`
  - Social psychology has long described how people can be persuaded to interpret a harmful act as moral. Recent research suggests that Large Language Models (LLMs) echo aspects of human psychology, from cognitive biases to social conformity. This raises a question with direct safety…

- **[ActICL: Post-Training for Agentic Multimodal In-Context Learning](https://arxiv.org/abs/2610.19475v1)**
  - *Yanshu Li, Ruixiang Tang, Junyi Jessy Li et al.*
  - `2026-10-14`
  - Multimodal in-context learning (ICL) is an important capability of multimodal large language models (MLLMs). Its performance is closely tied to the demonstrations it uses, making demonstration retrieval a core problem for ICL. Common methods use fixed scoring methods to retrieve…

- **[Structural Dependence, Imitation or Herding? A Multi-Agent Simulation of Global Intermedia Agenda Setting](https://arxiv.org/abs/2610.20144v1)**
  - *Mohammad Yousuf, Arif Md Tareque Habib*
  - `2026-10-14`
  - News outlets in poorer countries cover the world much as the leading outlets of rich countries do. Two explanations compete. One says they depend on Western news agencies for lack of resources. The other says they choose to copy prestigious outlets or whoever moves first. Observa…

- **[When Extremists Enter LLM Societies: Investigating Extreme Behavior in Multi-Agent Systems](https://arxiv.org/abs/2610.19863v1)**
  - *Guo Chen, Huaijin Xie, Ziwen Li et al.*
  - `2026-10-14`
  - Large language model (LLM) agents increasingly serve as computational actors in multi-agent social simulations. While existing work emphasizes representative personas and average-case behavior, social science shows that persistent tail actors can disproportionately shape collecti…

- **[Function-Space Temporal Self-Distillation for Policy Optimization](https://arxiv.org/abs/2610.19687v1)**
  - *Aryan Das, Arnab Bhattacharya, Vinay Kumar Verma*
  - `2026-10-14`
  - Reinforcement Learning with Verifiable Rewards (RLVR) improves reasoning in language models, but scalar outcomes provide coarse supervision over response trajectories. Self-distillation offers denser token-level guidance by comparing an unassisted policy with a feedback-informed…

- **[DTDD: Divergence-Triggered Dynamic Distillation for Reliable On-Policy Supervision](https://arxiv.org/abs/2610.19302v1)**
  - *Qijia He, Zequn Li, Spencer Luo et al.*
  - `2026-10-13`
  - On-policy distillation (OPD) provides dense token-level supervision on student rollouts, but this supervision can become unreliable when the student and teacher diverge, either because of a large initial policy gap or compounding errors in long-horizon reasoning and tool use. We…

- **[Whose turn is it? Context-guided model routing for stateful agents](https://arxiv.org/abs/2610.19292v1)**
  - *Anikesh Parashar, Avik Dutta, Vashu Chauhan et al.*
  - `2026-10-13`
  - Model routing can reduce the cost of LLM applications by assigning simpler requests to cheaper models without sacrificing the quality of the response. However, most routers treat requests as independent. Stateful agents do not operate under this assumption: a user turn may requir…

- **[MemeTrace: A Multimodal LLM-Based Agent for Safety-Aware Meme Provenance Analysis](https://arxiv.org/abs/2610.19267v1)**
  - *Bo Shao, Yihan Ma, Yiting Qu et al.*
  - `2026-10-13`
  - Online memes are often carriers of unsafe content such as disinformation and propaganda. Their rapid evolution in response to news events and strong dependence on contextual information make it difficult for platforms and moderators to detect and moderate them effectively. Moreov…

- **[Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills](https://arxiv.org/abs/2610.19264v1)**
  - *Ratnesh Pandey, Japneet Singh, Harsh Akshit et al.*
  - `2026-10-13`
  - Agent skills are Markdown documents that a tool-using agent reads as instructions and then acts on with the privileges of the session that loaded them. Installing one grants authority (the standing to direct the agent, not new privilege), and the size of that grant is what we mea…

- **[Agentic Self-Awareness: Aligning Knowing, Acting, and Holding](https://arxiv.org/abs/2610.19226v1)**
  - *Qinglin Chen, Hiroaki Hayashi, Jiaxin Zhang et al.*
  - `2026-10-13`
  - Frontier AI agents increasingly act in environments where seemingly solvable tasks may lack prerequisites, contain conflicting requirements, or reveal blockers only during execution. We formulate agentic self-awareness (ASA) as the alignment of task-grounded feasibility judgments…

- **[Definition Grounding in Theory-Level Auto-formalization](https://arxiv.org/abs/2610.19223v1)**
  - *Leyan Pan, Christian Szegedy, Frederick Rajasekaran et al.*
  - `2026-10-13`
  - LLM-based auto-formalization systems can now generate formally verified Lean code at unprecedented rates. However, a formalization advances mathematical research only when further mathematical results can be built on it, especially when its definitions and helper lemmas are gener…

- **[REPORT-OPS: Hybrid Evidence-Guided Reporting with Human-Supervised Refinement for HPC](https://arxiv.org/abs/2610.19222v1)**
  - *Mah Kadidia Konate, Mayur Akewar, Janki Bhimani et al.*
  - `2026-10-13`
  - Operational reporting for high-performance computing (HPC) facilities requires combining information from monitoring services, schedulers, incident and maintenance records, storage measurements, periodic reports, and operator investigations. Producing a reliable report requires m…

- **[Narrowing the Collaboration Gap, Probably](https://arxiv.org/abs/2610.19215v1)**
  - *Mirah Shi, Marcel Hussing, Ira Globus-Harris et al.*
  - `2026-10-13`
  - Large language models are increasingly deployed as teams of agents that hold different private information about a shared task. How should such agents concisely communicate in a way that promotes aggregation of decision-relevant information? Communicating only proposed actions ca…

- **[Identity, Incentives, and Cooperative Behavior for AI: Reverse-Engineering Multiagent Cooperation](https://arxiv.org/abs/2610.19188v1)**
  - *Andrew Perrault, Bryan Wilder*
  - `2026-10-13`
  - The behavior of AI systems increasingly depends on the extent to which agents cooperate or coordinate with one another, in ways that may be desirable or not depending on the situation. Conventional explanations for cooperative behavior distinguish between purely other-regarding p…

- **[Verification Turns Capability Gaps into Routing Decisions: Small Language Models for Clinical Documentation](https://arxiv.org/abs/2610.19169v1)**
  - *Nina Fatehi, Meysam Ghaffari, Animesh Agarwal et al.*
  - `2026-10-13`
  - Clinical note generation from doctor--patient dialogue is high-volume and hallucination-intolerant: a fabricated laboratory value can create patient-safety risk, not a quality regression. We ask whether an agentic \emph{verification} architecture, rather than generator scale, can…

- **[Into the Unknown: Benchmarking AI agents on open scientific research problems](https://arxiv.org/abs/2610.19159v1)**
  - *Seungone Kim, Jiayi Geng, Young-Jun Lee et al.*
  - `2026-10-13`
  - Can AI agents carry out research on open scientific problems? We introduce Into the Unknown, a benchmark that provides an agent with a science paper along with a research direction to pursue and tasks it to write a follow-up paper. We work with scientists at US Department of Ener…

- **[AgentCIScope: Grounded Contextual Integrity Evaluation for LLM Agents](https://arxiv.org/abs/2610.19158v1)**
  - *Chengquan Guo, Zhaorun Chen, Zinan Lin et al.*
  - `2026-10-13`
  - LLM agents are becoming increasingly capable of handling daily workspace tasks by interacting with application environments through tool calls. However, as agents read and write sensitive user data across email, documents, and other applications, a central privacy question is whe…

- **[Plant Memory: Technical Language Processing and a Verified Maintenance Ontology for Agent-Accessible Failure Knowledge from SAP PM Work Orders](https://arxiv.org/abs/2610.19131v1)**
  - *Akash Raj*
  - `2026-10-13`
  - Maintenance work orders are the largest written record of how industrial equipment fails, yet in most plants they are close to unusable for analysis. Short texts are abbreviated and misspelt, asset identity is buried in free text, work-type labels contradict the work described, a…

- **[Towards a Data-Centric Understanding of Spatial Reasoning in Multimodal Large Language Models](https://arxiv.org/abs/2610.19108v1)**
  - *Mahdieh Mallahnezhad, Masoud Jafaripour, Mohamadali Tofigh et al.*
  - `2026-10-13`
  - Multimodal Large Language Models (MLLMs) have been widely applied in embodied agents and robotics for vision tasks. However, MLLMs suffer from limitations in spatial reasoning and perception. Post-training techniques have shown promise for improving these capabilities; yet, there…

- **[GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement Learning](https://arxiv.org/abs/2610.19100v1)**
  - *Qingsong Xie, Jiahao Tian, Jiacheng Tang et al.*
  - `2026-10-13`
  - Constructing robust GUI agents relies on multimodal visual grounding: the ability to precisely map natural language intents to actionable on-screen components. Despite abundant desktop, web, and mobile benchmarks, high-fidelity resources tailored for diverse environments are surp…

- **[Plan or Retrieve First? A Scale Study of Tool Discovery Architectures](https://arxiv.org/abs/2610.19068v1)**
  - *Mingfei Zhang, Amit Surana, Ziauddin Majid et al.*
  - `2026-10-13`
  - Tool-augmented LLM agents discover relevant APIs from large registries before planning execution, yet finite context windows prohibit injecting all tool definitions into a single prompt. The dominant approach, which we term Retrieve-then-Plan (RtP), embeds the user query and retr…

- **[Smart Alone, Blind Together: Why Accuracy Fails to CertifyTheory of Mind in Multi-Agent Teams](https://arxiv.org/abs/2610.19051v1)**
  - *Will Beaumaster, Paul Schrater*
  - `2026-10-13`
  - Coordinators that act on what they infer about teammates are usually certified by the accuracy of those inferences. We argue that accuracy is the wrong certificate, for two reasons. First, the accuracy needed to act depends on what a wrong action costs, so the bar belongs to the…

- **[CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat](https://arxiv.org/abs/2610.19005v1)**
  - *Bangya Liu, Jianhong Tu, Yueyang Pan et al.*
  - `2026-10-13`
  - AI agents are demonstrating increasingly strong offensive and defensive cybersecurity capabilities in the real world. Current benchmarks mostly evaluate agents in isolation against static targets. Real cyber operations, however, are dynamic and coupled: security postures constant…

- **[ChunkAct: Action Chunking for Agentic Robotics](https://arxiv.org/abs/2610.18874v1)**
  - *Bingxin Xu, Wenrui Bao, Xinxin Liu et al.*
  - `2026-10-13`
  - Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a st…

- **[Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://arxiv.org/abs/2610.18868v1)**
  - *Wenbo Hu, Shraman Pramanick, Krishna Kumar Singh et al.*
  - `2026-10-13`
  - Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horiz…

- **[DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning](https://arxiv.org/abs/2610.18862v1)**
  - *Minghao Luo, Liang Chen*
  - `2026-10-13`
  - Reasoning models achieve strong performance through long chains of thought (CoT), but often spend more tokens than needed to solve a problem. Existing ways to shorten the CoT require additional training for each model, add a fixed steering vector to the model's hidden states, or…

- **[Hybrid Reasoning Agents](https://arxiv.org/abs/2610.18861v1)**
  - *Jiaru Zou, Yunzhe Qi, Sirui Chen et al.*
  - `2026-10-13`
  - How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning tran…

- **[RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks](https://arxiv.org/abs/2610.18835v2)**
  - *Kaiyuan Chen, Shuangyu Xie, Uksang Yoo et al.*
  - `2026-10-13`
  - It has been difficult to accurately model the physics of the interaction between a robot and the objects it manipulates, including contact mechanics, coupled contact dynamics, deformations, stiffness and friction. We present RoboSimStudio (RSS), an interactive toolkit that makes…

- **[Optimizing Team Behavior via Extremum-seeking Control in Multi-agent Reinforcement Learning](https://arxiv.org/abs/2610.18808v1)**
  - *Svar Rajankumar Patel, Kshitij Jerath*
  - `2026-10-13`
  - In cooperative Multi-Agent Reinforcement Learning (MARL), agents must learn to coordinate their actions to achieve shared objectives. A key indicator of effective coordination is behavioral diversity, i.e., the agents' potential to enact distinct yet complementary control policie…

- **[SEAR: Self-Evolving Agentic Robotics](https://arxiv.org/abs/2610.18792v1)**
  - *Xinyi Wang, Bangzheng Li, Hanyu Wang et al.*
  - `2026-10-13`
  - Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the age…

- **[Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents](https://arxiv.org/abs/2610.18784v2)**
  - *Yuchen Lu, Julian McAuley, Lei Zhang*
  - `2026-10-13`
  - Long-horizon agents accumulate progress in persistent task state, yet repeatedly process interaction histories describing how that progress was achieved. This raises a natural question: can long-horizon context instead be organized around reusable progress rather than the history…

- **[BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems](https://arxiv.org/abs/2610.18780v1)**
  - *Xiaoguang Guo, Yaohao Long, Chuxu Zhang*
  - `2026-10-13`
  - Large language model multi-agent systems extend individual agents' capabilities through collaboration across specialized roles, tools, and workflows. Yet collaboration makes failures harder to diagnose: one agent may misinterpret a correct result while others carry the mistake fo…

- **[Beyond the Verdict: Agentic Code Judging with Verifiable Feedback](https://arxiv.org/abs/2610.18760v1)**
  - *Zheye Deng, Sha Li, Changlong Yu et al.*
  - `2026-10-13`
  - Test-time scaling for large language models (LLMs) can involve generating multiple candidate solutions for selection or revising an earlier attempt. To guide selection and revision, we need a verifier that can estimate candidate correctness and provide evidence of failure. In com…

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

- **[Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve](https://arxiv.org/abs/2610.18616v2)**
  - *Yuyang Bai, Yu Wang, Yu Zhang*
  - `2026-10-13`
  - Searching text-rich knowledge graphs requires following relations while examining textual evidence. Predefined graph interfaces constrain what evidence agents can access, even when they write code to combine tool calls or process retrieved subgraphs. We propose direct knowledge g…

- **[Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents](https://arxiv.org/abs/2610.18614v1)**
  - *Ashutosh Hathidara*
  - `2026-10-13`
  - Controlling an acting LLM agent means deciding, at each step of a long-horizon task, whether to trust its next action, abstain, or hand off to a human. That decision needs a per-step confidence signal predicting whether the current rollout will eventually succeed. The agent's own…

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

- **[A Global View of How LLMs Value Human Time](https://arxiv.org/abs/2610.18515v2)**
  - *Yifan He, Manon Reusens, Sofie Goethals et al.*
  - `2026-10-13`
  - Large language models (LLMs) increasingly act as personal assistants; however, little is known about how they capture national-level preferences on a global scale. Given that "time" is a universal and representative concept, we examine LLMs' time preferences by varying only users…

- **[Judges Follow the Reference: The Derivation Gap in Verifying Tool-Call Arguments](https://arxiv.org/abs/2610.18497v1)**
  - *Linhai Ma, Yan Wang, Lingfei Qian et al.*
  - `2026-10-13`
  - Tool-call judges evaluate argument values proposed by LLM agents. We find that they accept a correct value less often when their input holds no reference for it, that is, no text that says what the value should be. This happens when the value is a default value from the function…

- **[ReTerm: Recovery Training for Self-Improving Terminal Agents](https://arxiv.org/abs/2610.18484v2)**
  - *Wei Xie, Kaituo Feng, Shiming Fu et al.*
  - `2026-10-13`
  - Terminal agents have shown strong abilities in complex coding tasks. However, they often struggle to recover from errors during long-running execution (e.g., command errors, faulty implementations), eventually leading to task failures. To this end, we present ReTerm, a self-impro…

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

- **[Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes](https://arxiv.org/abs/2610.18356v1)**
  - *Yu Wang, Rui Dai, Wei Chen et al.*
  - `2026-10-13`
  - City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbex, an agentic vision-language framework that instead casts grounding as active spatial search. Urbex…

- **[ABot-ER: Unified Embodied Reasoning through Agentic Data-Model Co-Evolution](https://arxiv.org/abs/2610.18355v2)**
  - *Qiuyu Ding, Heng-Da Xu, Changda Xia et al.*
  - `2026-10-13`
  - We introduce ABot Embodied Reasoning (ABot-ER), a unified embodied reasoning foundation model that breaks the tension between breadth and depth in embodied reasoning. Embodied intelligence demands the joint mastery of perception, planning, and execution, yet reconciling generalit…

- **[Choosing LLMs for Strategic Agent Interactions](https://arxiv.org/abs/2610.18354v1)**
  - *Arastun Mammadli, Herbert Woisetschläger, Jawad Fayaz et al.*
  - `2026-10-13`
  - Game-theoretic benchmarks claim that large language model (LLM) strategic decision-making varies across game types, interaction structures, and capability dimensions. However, they only evaluate strategic performance across individual fixed models. In parallel, contemporary LLM r…

- **[Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2610.18352v1)**
  - *Youpeng Wen, Gang Wang, Tianyu Huang et al.*
  - `2026-10-13`
  - A robot following a multi-step instruction needs to act on the right objects in the right order, even as the scene changes. It must also maintain awareness of task progress and determine when to advance. To address these challenges, we introduce Orchestra, an agent harness that s…

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

- **[Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench](https://arxiv.org/abs/2610.18938v1)**
  - *Yuxiao Hu, Qian Li, Ding Wang et al.*
  - `2026-10-13`
  - Most symbolic regression methods optimize candidate equations, but improving an equation's fit does not establish whether its underlying scientific conjecture should be retained, revised, or rejected. A conjecture may admit multiple mathematical realizations, and similarly accura…

- **[Output Discipline Sets the Floor: A Falsification-Guided, Model-Agnostic Agent Protocol for Auditable Hypothesis-Driven Decision Making](https://arxiv.org/abs/2610.18298v1)**
  - *Jing Liu, Yongxing Qi, Ping Yao et al.*
  - `2026-10-13`
  - What binds large language models on auditable, hypothesis-driven decision tasks, where every candidate can be checked against the evidence? On the public TCMEval-SDT benchmark for Traditional Chinese Medicine syndrome differentiation (200 cases), the binding constraint is output…

- **[JevGPT: Thinking Fast and Slow in Autonomous Research](https://arxiv.org/abs/2610.18272v1)**
  - *Yasheng Sun, Yanning Dai, Yimeng Chen et al.*
  - `2026-10-13`
  - Autonomous research agents must acquire and reason over evidence within a limited budget. Yet relevant sources can remain uninspected or unused, leaving a gap between retrieval coverage and the evidence that informs research. The challenge is to align fast local judgments with ch…

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

- **[The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](https://arxiv.org/abs/2610.18933v1)**
  - *Robert Tjarko Lange, Luca Grillotti, Yutaro Yamada et al.*
  - `2026-10-13`
  - Modern coding agents are fundamentally reshaping the role of human input for computational research: they write code, launch in silico experiments, analyze their results, and autonomously operate with ever-increasing time horizons. Despite these developments, fully autonomous res…

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

- **[LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity](https://arxiv.org/abs/2610.18092v1)**
  - *Yibo Wang, Senjie Jin, Yansong Ning et al.*
  - `2026-10-13`
  - Deep research (DR) agents address open-ended information needs through multi-step reasoning, long-horizon web search, and evidence synthesis. However, existing benchmarks primarily focus on academic research or synthetic tasks, leaving DR agents' capabilities in real-world life a…

- **[AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses](https://arxiv.org/abs/2610.18090v1)**
  - *Kaiyu Huang, Yiting Li, Angyang Gu et al.*
  - `2026-10-13`
  - Ambiguous or incomplete task specifications complicate both execution and clarification for language-model agents. Yet agents' responses to these information gaps remain poorly characterized across models and execution harnesses. We present AM-Bench, a benchmark built from 48 tas…

- **[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088v2)**
  - *Peng Jiang, Dongyang Li, Quanying Liu et al.*
  - `2026-10-13`
  - Autoresearch systems increasingly undertake entire research projects. In practice, scientific research requires systems to pursue multiple interdependent claims through a continuous, multi-stage workflow and revise experiments as evidence accumulates. Existing evaluations of auto…

- **[AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement](https://arxiv.org/abs/2610.18083v1)**
  - *Wenhao Zhou, Jiajun Song, Haitao Wang et al.*
  - `2026-10-13`
  - Scaling recursive self-improvement requires additional computation to produce useful research progress in reaching persistent objectives. Intuitively, more researcher agents can explore more hypotheses, but early evaluation scores might misrepresent their promise, shared findings…

- **[WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution](https://arxiv.org/abs/2610.18067v1)**
  - *Hang He, Linting Wang, Guanming Liu et al.*
  - `2026-10-13`
  - Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and…

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

- **[Learning How to Remember: Memory Modality Selection for GUI Agents](https://arxiv.org/abs/2610.17928v1)**
  - *Taeyun Roh, Suhyeong Park, Gijin Kim et al.*
  - `2026-10-13`
  - Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for reusing knowledge from past interactions. However, existing memory augmented GUI agents typically adopt a…

- **[Interaction-as-a-Judge](https://arxiv.org/abs/2610.17895v2)**
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

- **[RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions](https://arxiv.org/abs/2610.17867v3)**
  - *Rishabh Ranjan, Vignesh Kothapalli, Harshvardhan Agarwal et al.*
  - `2026-10-13`
  - Foundation models for tables and relational databases are increasingly used for predictive tasks across various scientific and industrial domains. However, adapting existing models to unseen datasets requires tens of thousands of examples. Here we introduce RT-J, an 86M-parameter…

- **[Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills](https://arxiv.org/abs/2610.17860v1)**
  - *Letian Zhu, Han Li, Yifan Yao et al.*
  - `2026-10-13`
  - Agent Skills improve LLM agents by making task knowledge reusable across sessions. Learning transferable Skills requires evidence about a procedure and its conditions of use, which a successful task attempt can leave untested. We introduce Socratic Skill Learning (SSL), which int…

- **[Why Static Skill Inconsistencies Do Not Equate to Runtime Risks: A Behavioral Analysis of LLM Agent Execution](https://arxiv.org/abs/2610.18927v1)**
  - *Fengrui Fan, Huahao Wang, Jingyi Fang et al.*
  - `2026-10-13`
  - LLM agent frameworks heavily rely on external skill assets to standardize tool usage, encode operational workflows, and supply executable runtime resources. Despite their widespread adoption, multi-component skill packages frequently suffer from cross-artifact inconsistencies, wh…

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

- **[GIFT-Eval-CTX: A Benchmark For Contextual Forecasting Model Evaluation](https://arxiv.org/abs/2610.17794v1)**
  - *Xu Liu, Hanshu Yan, Taha Aksu et al.*
  - `2026-10-13`
  - Contextual forecasting seeks to improve time series forecasting by incorporating forward-looking information, such as planned events, external conditions, and expert expectations. However, reliable evaluation remains difficult: existing benchmarks often have limited domain covera…

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

- **[Verifier-Grounded Agentic RL for Provably Correct Code](https://arxiv.org/abs/2610.19298v1)**
  - *George Ma, Yuhao Zhang, Bing He et al.*
  - `2026-10-13`
  - Reinforcement learning for code usually rewards passing tests, which a model can do while remaining wrong on the inputs the tests do not cover. A program verifier instead decides whether a program satisfies a formal specification for all inputs. Language models are almost always…

- **[Learning in Strategic Queuing with Geometric Recharge: From Bandits to Systems](https://arxiv.org/abs/2610.19179v1)**
  - *Cristian Palma Foster, Eva Tardos*
  - `2026-10-13`
  - We study packet routing in queuing systems where queues act as selfish, myopic agents that use no-regret learning algorithms to select servers with unknown service rates. To model the small buffers used in data centers, we assume that each server has a single-packet buffer. Even…

- **[TRACER: Trace-Regularized Training Against Indirect Prompt Injection](https://arxiv.org/abs/2610.19133v1)**
  - *Kshitij Mishra, Salem Lahlou, Nils Lukas*
  - `2026-10-13`
  - Indirect prompt injection uses untrusted retrieved content, tool outputs, or agent messages to override an LLM's intended behavior. We show that defense robustness is channel-conditioned: the same attack succeeds 18% of the time as a follow-up message but 53% when placed in retri…

- **[Contextual Credit Policy Optimization](https://arxiv.org/abs/2610.19103v1)**
  - *Huiwen Han, Ziyao Zeng, Zihao Zhu et al.*
  - `2026-10-13`
  - Group-based reinforcement learning enables large language model agents to learn from sparse outcome rewards in long-horizon tasks. Recent methods derive step-level credit by comparing observation-matched experiences across trajectories. However, identical observations can occur i…

- **[What Information Buys in Active Inference](https://arxiv.org/abs/2610.19046v1)**
  - *Melih Kandemir, Mustafa Mert Çelikok*
  - `2026-10-13`
  - Information-theoretic exploration is of primary interest in methodological studies of reinforcement learning (RL) and computational cognitive neuroscience, while the established RL theory builds regret guarantees on confidence sets. This situation leaves open the conditions under…

- **[How Far Can Coding Agents Go in Visual Generation?](https://arxiv.org/abs/2610.19025v1)**
  - *Hengguang Zhou, Yuanhao Ban, Jiaqi Feng et al.*
  - `2026-10-13`
  - Modern image generation largely relies on specialized generative models that leave the process of image construction implicit in learned parameters. We explore an alternative: general-purpose coding agents that construct images through executable programs. Our study of zero-shot…

- **[SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection](https://arxiv.org/abs/2610.18807v1)**
  - *Wenlin Zhong, Hao Wang, Kun Yuan et al.*
  - `2026-10-13`
  - Agentic reinforcement learning (RL) enables large language models (LLMs) to learn from multi-turn interactions with verifiable outcomes. Textual skills can improve exploration by distilling prior interactions into reusable guidance. However, existing skill-based RL approaches oft…

- **[Autonomous Cyber Operations Gym for Training and Evaluating AI Models for Defence](https://arxiv.org/abs/2610.18594v1)**
  - *Tobias Hürten, Johannes F. Loevenich, Florian Spelter et al.*
  - `2026-10-13`
  - This paper proposes an Autonomous Cyber Operations (ACO) gym, a unified framework integrating high-fidelity network emulation, realistic user behaviour modelling for benign network traffic and adversarial profiles, and the generation of cybersecurity scenarios through open toolki…

- **[Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries](https://arxiv.org/abs/2610.18948v1)**
  - *Inderjeet Singh*
  - `2026-10-13`
  - Finite safety assessments cannot exclude an adversary that preserves unattacked behavior until certification and activates afterward. We characterize this limitation for embodied and tool-use AI. An adversary that matches the complete observation law until observable, irrevocable…

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

- **[LADDER: A Long-Horizon Robot Manipulation Benchmark](https://arxiv.org/abs/2610.18053v1)**
  - *Petko Petkov, Giuliano Albanese, Nikolay Nikolov et al.*
  - `2026-10-13`
  - General-purpose robot manipulation policies learn short-horizon skills effectively, but degrade rapidly on long-horizon tasks. Existing benchmarks cannot isolate failures because task horizon is either too short or entangled with scene and object variations. We propose LADDER, a…

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

- **[Degrees of Freedom in Multi-Agent Coordination: Between Centralized and Decentralized Regimes](https://arxiv.org/abs/2610.17751v1)**
  - *Yiqing Peng, Hehai Lin, Zixuan Wang et al.*
  - `2026-10-13`
  - Large language model (LLM)-based multi-agent systems (MAS) are commonly organized around two coordination regimes. Centralized coordination provides explicit control but can create a bottleneck at a single coordination locus, whereas decentralized coordination offers local autono…

- **[Auditing Failure Attribution: Label Predictability and Judge Behavior](https://arxiv.org/abs/2610.17747v1)**
  - *Tianyang Xu, Jing Gao*
  - `2026-10-13`
  - Failure-attribution benchmarks ask an LLM judge which step or agent caused a failure. A high score should mean the judge checked the faulty step against the run (a cross-step check). However, spurious signals (surface cues) that predict the annotation can produce a high score. In…

- **[TSRL: Trigger-based Supervised Reinforcement Learning for Continual Agent Training](https://arxiv.org/abs/2610.17726v1)**
  - *Yuqian Fu, Kaiwen Jiang, Zijun Song et al.*
  - `2026-10-13`
  - Large language model (LLM) agents excel at complex, multi-step tasks but suffer from catastrophic forgetting during continual learning--acquiring new skills often degrades previously mastered capabilities. Existing post-training paradigms face a fundamental trade-off: Supervised…

- **[Evidence-First Agentic Verification](https://arxiv.org/abs/2610.17724v1)**
  - *Reza Sanayei, Razvan-Gabriel Dumitru, Sunjie Hou et al.*
  - `2026-10-13`
  - Long-horizon, semi-verifiable agentic tasks often rely on rubric-based evaluation, but the evidence needed to assess these tasks can be spread across the environment state and the execution trace. A judge may overlook this evidence or accept unsupported claims, including an agent…

- **[LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents](https://arxiv.org/abs/2610.17685v1)**
  - *Jingyue Cong, Estrid He, Zhuang Li et al.*
  - `2026-10-13`
  - Enterprise agents face safety risks that cannot be determined from individual actions alone. Existing safety benchmarks largely evaluate action-local risks, overlooking failures whose safety depends on workflow state. In such state-dependent risks, the same action may be safe in…

- **[DeltaTTG: Training Multi-Turn Agents with a Token-to-Go Progress Meter](https://arxiv.org/abs/2610.17666v1)**
  - *Xuyan Ye, Xiyan Fu, Shengda Fan et al.*
  - `2026-10-13`
  - Reinforcement learning with verifiable rewards (RLVR) for multi-turn agents relies on sparse terminal rewards that say little about individual steps. Within-group step comparisons depend on reliable state matching and sufficiently diverse sampled outcomes, while direct step scori…

- **[ATTUNE: Agentic Throughput Tuning for LLM Training](https://arxiv.org/abs/2610.17528v1)**
  - *Leo Fan, Hongyang Wang, Wenbo Chen et al.*
  - `2026-10-13`
  - Training recipes are tuned by hand for one model, cluster and workload, and every new model, accelerator, framework version or dataset means tuning again. Automated tuners search a fixed space of knobs and check only that a job runs, yet a configuration can run to completion whil…

- **[Truthful and Expected-Payment-Optimal Model Routing in Graph-Based Agentic Workflows](https://arxiv.org/abs/2610.19316v1)**
  - *Jiayuan Liu, Mingyu Guo, Jiarui Gan et al.*
  - `2026-10-13`
  - Assigning routine tasks to cheaper large language model (LLM) providers can reduce generation cost, but switching providers may require processing accumulated context again. Keeping dependent tasks with the same provider can instead reuse eligible context. Graph-based workflows t…

- **[Can LLM Agents Efficiently Identify Appliance Faults? Insights From Diagnosing a Simulated Appliance](https://arxiv.org/abs/2610.19291v1)**
  - *Lucas H. McCabe, Sarah Lukens, H. Howie Huang*
  - `2026-10-13`
  - In so-called "Industry 4.0," integrated sensors, analytics tools, and other digital technologies supplement industrial workflows, potentiating enhanced visibility and automation. Prognostics and health management (PHM) and natural language processing (NLP) practitioners alike hav…

- **[The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement](https://arxiv.org/abs/2610.18845v2)**
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

- **[SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software Coding Agents](https://arxiv.org/abs/2610.18206v1)**
  - *Do Xuan Trong, Duc Anh Nguyen, Do Xuan Long et al.*
  - `2026-10-13`
  - We present SWE-MISBEHAVIOR, the first taxonomy and evaluation framework for diagnosing boundary-violating misbehaviors in coding agents. It contains 7.4K human-in-the-loop synthesized samples spanning three layers of agent action space: (i) Code Generation, (ii) File Management,…

- **[Narrative Lookahead in LLMs: Event-Level Decodability, Predictive Advantage, and Steering](https://arxiv.org/abs/2610.18121v1)**
  - *Donghoon Jung, Min Kim, Seojin Choi et al.*
  - `2026-10-13`
  - Do language models carry information about narrative events before writing them, and how far ahead? We examine narrative lookahead through salient, state-changing events rather than tokens or response-level attributes. We extract 23,355 LLM-annotated events from 2,000 stories gen…

- **[From Agents to Edges: Paired Optimization for Multi-Agent Collaboration](https://arxiv.org/abs/2610.18069v1)**
  - *Feng Lin, Xiaotian Yu, Yifan Yang et al.*
  - `2026-10-13`
  - Strong individual agents do not guarantee effective collaboration. Communication must align what one agent conveys with how another interprets and uses it. This dependency makes the communication edge a natural unit of optimization. We introduce Paired Automated Communication Opt…

- **[Agent-Reflex: Teaching Language Agents to Act Reflectively](https://arxiv.org/abs/2610.17953v1)**
  - *Guanting Dong, Xinyu Yang, Jiajie Jin et al.*
  - `2026-10-13`
  - Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision…

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

- **[SkillScreen: High-Recall Screening of Malicious Agent Skills with Decision Models](https://arxiv.org/abs/2610.17727v2)**
  - *Jerrold Huang, Junwei Quan, Saiyue Lyu et al.*
  - `2026-10-13`
  - Agent skills turn natural-language instructions into actions, creating a security challenge: legitimate automation and malicious behaviour can look deceptively similar. A practical screen must catch nearly every attack while keeping the review load manageable. We present SkillScr…

- **[RALI@iKAT 2026: Retrieval-aware User Profile Denoising via Personalized Conversational Dense Retrieval](https://arxiv.org/abs/2610.17673v1)**
  - *Yuchen Hui, Fengran Mo, Jia Ao Sun et al.*
  - `2026-10-13`
  - Modern conversational information access systems continuously extract user information from conversations to build user profiles for personalized retrieval. As user profiles accumulate over time, they inevitably become noisy, making effective user profile denoising a fundamental…

- **[Executable Prefix Values for Locating Agent Failures](https://arxiv.org/abs/2610.17633v1)**
  - *Bingyu Shen, Jiaqi Tang, Lan Wei et al.*
  - `2026-10-13`
  - Work on debugging LLM agents treats the "first mistake" marked by a human or LLM judge as ground truth for where a trajectory failed. We ask whether such labels point at causes or symptoms, and make the distinction executable: we restart the agent from reconstructed intermediate…

- **[When Does an ASR Error Matter? Task-Role Diagnostics for Tool-Using Voice Agents](https://arxiv.org/abs/2610.17619v1)**
  - *Xiaolong Wang, Shijie Su, Naqi Xiong*
  - `2026-10-13`
  - In cascaded voice agents, ASR errors can have markedly different downstream consequences: a small transcription error may leave a tool call unchanged or alter its intent or arguments. Conventional word error rate (WER), however, does not capture these differences. We introduce Sp…

- **[StateHarness: Maintaining Evolving Project State for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.17616v1)**
  - *Chuan Zou, Yujun Zhou, Xiaonan Luo et al.*
  - `2026-10-13`
  - Long-horizon coding requires agents to maintain an evolving view of the project they are changing: what problem is currently being solved, what has already been learned or modified, which other artifacts may be affected, and what work remains unresolved. When this information is…

- **[Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents](https://arxiv.org/abs/2610.17544v1)**
  - *Jianghong Zhou, Hao Rong, Chen Lin et al.*
  - `2026-10-13`
  - Thought templates, skill libraries, agent memories and caches turn many reasoning steps into one. We call this reasoning contraction. A contracted memory saves reasoning steps and errors until its facts change, then quietly answers wrong. Most systems trust memories by counting s…

- **[CLASHarness: Benchmarking Multi-Agent Conflict in Computer Use via a Controllable and Verifiable Generation Pipeline](https://arxiv.org/abs/2610.19128v1)**
  - *Yuxiang Lai, Jike Zhong, Chengzhi Liu et al.*
  - `2026-10-13`
  - Vision-language models (VLMs) are increasingly deployed in multi-agent systems to automate complex computer-use workflows, yet existing benchmarks mostly assume consistent, cooperative environments. In contrast, real-world collaboration rarely runs on consistent information: peer…

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

- **[MAS-Gate: Unlocking Multi-Agent System Lifecycle via Node-Centric Quantification](https://arxiv.org/abs/2610.17613v1)**
  - *Hehai Lin, Zixuan Wang, Ming Yan et al.*
  - `2026-10-13`
  - Large language model (LLM)-based multi-agent systems (MAS) can solve complex problems beyond the reach of a single agent by decomposing tasks and coordinating complementary capabilities. Despite extensive research on MAS, existing work largely focuses on specific aspects or indiv…

- **[Upstream Influence, Downstream Re-Anchoring in LLM Agent Chains](https://arxiv.org/abs/2610.17723v1)**
  - *Chun-Yu Hsu, Lun-Wei Ku, Chung-Chi Chen*
  - `2026-10-13`
  - People act on evaluative judgments produced by LLM agents, and in multi-agent systems those judgments pass through several agents before reaching a person. We show that a workflow's information architecture---source access, handoff format, and which model reads the untrusted cont…

- **[Compiling Expert Procedures into Verified Programs: When a Small Model Is Enough](https://arxiv.org/abs/2610.19148v1)**
  - *Vishvesh Bhat, Asad Aali, Muhammad Ahmed Mohsin*
  - `2026-10-13`
  - In procedural tool-use domains, how much of the gap between base models is procedure rather than capability? We build an explicit program from a teacher's traces and run it in front of unchanged small models, including an 8B model. The construction, PLVR , takes the reasoning tra…

- **[Does self-distillation improve reasoning?](https://arxiv.org/abs/2610.18613v1)**
  - *Jason Ken Adhinarta, Raina Wu, Ashutosh Sharma et al.*
  - `2026-10-13`
  - Self-distillation is an emerging approach that trains a model to imitate its own predictions when conditioned on privileged information, such as correct answers or environmental feedback. Recent methods have reported better sample efficiency and generalization than reinforcement…

- **[Coupled Harness--Model Evolution for Scientific Equation Discovery](https://arxiv.org/abs/2610.17740v1)**
  - *Pengze Li, Jiaquan Zhang, Encheng Su et al.*
  - `2026-10-13`
  - Large language models (LLMs) are increasingly used to discover scientific equations from experimental data. Such a discovery system has two parts that must work together: a library of executable computational tools and the model's tool-use policy. The tools supply the solving cap…

- **[Can Agents Truly Forget? Explore Machine Unlearning for LLM Agents](https://arxiv.org/abs/2610.17659v1)**
  - *Junkai Lin, Ge Xu, Zheng Xu et al.*
  - `2026-10-13`
  - Large language model (LLM) agents have shown strong capabilities in interactive problem solving, tool use, and long-horizon task execution. However, they may also acquire sensitive or private knowledge during training and expose it during deployment. Retraining a model from scrat…

- **[Teacher-Guided Tool Learning for Small Language Models via Bidirectional KL Constraints](https://arxiv.org/abs/2610.18459v1)**
  - *Haoxuan Gao, Qin-Wen Luo, Xiang Chen et al.*
  - `2026-10-13`
  - External tools can extend the capabilities of small language models (SLMs), enabling their deployment in resource constrained environments. However, their limited capabilities make it difficult for SLMs to discover effective tool use behaviors through reinforcement learning alone…

- **[Instructions Are Evidence, Not Objectives: Measuring Outcome Alignment of Agents](https://arxiv.org/abs/2610.17757v1)**
  - *Kaiming Liu, Yuxuan Liu, Jinrui Ju et al.*
  - `2026-10-13`
  - Large language model agents can follow complex human instructions to solve real-world tasks. In practice, however, initial instructions are often incomplete. In our analysis of 100 user-agent trajectories from SWE-chat, 56\% of initial instructions omit requirements that later em…

- **[Verifier-Harness Co-Evolution for Training-Free Self-Improvement on Open-Ended Tasks](https://arxiv.org/abs/2610.17609v1)**
  - *Tianyi Xu, Yaolun Zhang, Yiran Wu et al.*
  - `2026-10-13`
  - Training-free self-improvement lets an agent use feedback to revise the response it is about to return and to update the harness state that shapes how it handles later tasks. On open-ended tasks that feedback rarely comes from reference answers or executable tests, so the agent h…


## Harness  (146)

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

- **[3DCodeVerse: Exploring 3D Worlds as Code](https://arxiv.org/abs/2610.22341)**
  - *Yipeng Gao, Ziyao Zeng, Jinfa Huang et al.*
  - 🤗 Featured · `2026-10-15`
  - We introduce 3DCodeVerse, a research ecosystem that enables coding agents to create editable and verifiable 3D content at scale. 3DCodeVerse comprises large-scale, high-quality datasets of executable 3D code, a coding harness for spatial reasoning and automated verification, and…

- **[MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering](https://arxiv.org/abs/2610.22344)**
  - *Shangheng Du, Jinxin Shi, Shuaiyu Zhang et al.*
  - 🤗 Featured · `2026-10-15`
  - Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE)…

- **[Intern-Decision: Efficient Multimodal Decision Making with Autoregressive Masked Language Modeling](https://arxiv.org/abs/2610.22131)**
  - *Tong Zhu, Zhe Xu, Zefeng He et al.*
  - 🤗 Featured · `2026-10-15`
  - Interactive agents repeatedly choose among a finite set of actions, labels, or ordinal outcomes. Generating a free-form response for each choice adds latency and complicates the interface between a model and its environment. We present Intern-Decision, a family of 0.8B, 2B, and 4…

- **[JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs](https://arxiv.org/abs/2610.21412)**
  - *Kunlun Zhu, Tao Feng, Xu Han et al.*
  - 🤗 Featured · `2026-10-15`
  - Large language model (LLM) agents now fix software, operate computers and serve customers, but their harnesses, the programs that run them, call a large LLM at every step, which makes long tasks slow and costly. Most of these calls end in a multiple-choice decision, such as which…

- **[CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance](https://arxiv.org/abs/2610.21453)**
  - *Zixuan Wang, Yuqi Liu, Yuxin Chen et al.*
  - 🤗 Featured · `2026-10-15`

- **[Self-Evolving Agent Harness](https://arxiv.org/abs/2610.18813)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - 🤗 Featured · `2026-10-13`
  - Harness self-evolution revises an agent's software scaffolding, including prompts, memory, workflows, and executable components, while keeping model weights fixed. We formalize a feedback-driven process in which accepted revisions persist across runs. The framework separates upda…

- **[Virtual Head Attention](https://arxiv.org/abs/2610.17959)**
  - *Xibo Ding, Guoxia Wang, Jinle Zeng et al.*
  - 🤗 Featured · `2026-10-13`
  - The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality. GQA achieves strong quality but incurs high KV cache overhead; alternative approaches such as MLA and MFA…

- **[AVC-Reward: Event-Centric Audio-Video Consistency Evaluation](https://arxiv.org/abs/2610.22321)**
  - *Yuruo Wu, Kaihang Pan, Kai Shen et al.*
  - 🤗 · `2026-10-15`
  - As joint audio-video generation models become more capable, they can generate audio-visual scenes exhibiting three forms of complexity: multi-event composition, multi-layer audio mixture, and asymmetric cross-modal relations. However, current evaluations largely reuse metrics fro…

- **[Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing](https://arxiv.org/abs/2610.22196)**
  - *Tianxiang Fei, Jiazheng Kang, Mao Zheng et al.*
  - 🤗 · `2026-10-15`
  - External-memory systems extend language-model applications beyond a context window, but their quality depends critically on the model executing the write path: deciding what to retain, how precisely to represent it, and how new evidence should update persistent state. Existing fr…

- **[CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](https://arxiv.org/abs/2610.21910)**
  - *Dongjie Cheng, Ruifeng Yuan, Ran Wei et al.*
  - 🤗 · `2026-10-15`
  - As Vision-Language Models (VLMs) advance, they are increasingly expected to perform spatiotemporal reasoning over motion, actions, and view changes beyond what the input images show. Video World Models (VWMs) provide a natural unified engine for visual imagination by generating t…

- **[Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries](https://arxiv.org/abs/2610.22273v1)**
  - *Anikait Singh, Teresa Zhang, Yoonho Lee et al.*
  - `2026-10-15`
  - Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often…

- **[X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement Learning](https://arxiv.org/abs/2610.22269v1)**
  - *Adhwaa Al-Chaab, Ayman Younis, Dario Pompili*
  - `2026-10-15`
  - The O-RAN ALLIANCE introduces architectural flexibility through disaggregation and AI-driven control. While the RAN Intelligent Controller (RIC) enables centralized optimization, current AI approaches lack reasoning capabilities and explainability. We propose eXplainable RIC (X-R…

- **[Shortcut Sensitivity in Agent-Safety Evaluations](https://arxiv.org/abs/2610.22243v1)**
  - *Hasan Demirkiran, Jens Ernstberger*
  - `2026-10-15`
  - AI agents take actions through tools. Some actions are sensitive, so guards that supervise them must themselves be evaluated reliably. Yet the data used to evaluate a guard can include cues that make labels predictable without measuring the intended safety construct, and those cu…

- **[HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration](https://arxiv.org/abs/2610.22195v1)**
  - *Yanchen Deng, Jianguo Huang, Yao Long Teng et al.*
  - `2026-10-15`
  - Orchestrating multiple agents on a complex task requires reconciling local subtask execution with global task planning. Dynamic dispatch approaches provide execution flexibility but do not explicitly model subtask hierarchies or dependencies, while predefined workflows impose thi…

- **[Priming Base Models for Agentic Post-Training: An Open Midtraining Recipe](https://arxiv.org/abs/2610.22019v1)**
  - *Soumye Singhal, Joseph Jennings, Ka Shun Shum et al.*
  - `2026-10-15`
  - Frontier models, general-purpose and domain-specific alike, now include a midtraining stage between pretraining and post-training, but little has been published about how this stage is built. We present an open midtraining recipe that primes base models for agentic post-training,…

- **[RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent](https://arxiv.org/abs/2610.21791v1)**
  - *Huan Zhang, Mingju Chen, Dongxu Zhou et al.*
  - `2026-10-15`
  - Large language model (LLM) agents have demonstrated strong capabilities in complex tasks, including code generation, tool use, and multi-hop question answering. Existing self-improvement methods enhance agent performance through model optimization, harness evolution, and executab…

- **[DeciCAD: Harness-Grounded Learning of Action Policies for CAD Agents](https://arxiv.org/abs/2610.21755v1)**
  - *Yufeng Peng, Yixin Zhang, Ziyi Liu et al.*
  - `2026-10-15`
  - Large Language Model agents operate through closed-loop action policies whose decision space is defined by an agent harness. We investigate how this operating space shapes agent behavior and policy learning in computer-aided design (CAD), a professional domain characterized by pe…

- **[TRACER: A Multimodal Harness for Patient Care in Hospitals](https://arxiv.org/abs/2610.21266v1)**
  - *Zane Durante, Paul Tang, Keshigeyan Chandrasegaran et al.*
  - `2026-10-15`
  - Continuous video and clinical records provide complementary information for understanding how patient behavior evolves over a hospital stay. A central challenge is how to represent behavior across the entire stay while preserving access to fine-grained visual and clinical evidenc…

- **[AutoOnboarder: Autonomously Onboarding LLM Agents](https://arxiv.org/abs/2610.21218v1)**
  - *Tanay Arora, Cong Liu*
  - `2026-10-15`
  - Agentic large language models have been documented to lose reasoning capability when placed inside a harness, the software that mediates their observations and actions. To reconcile these losses, we introduce AutoOnboarder, an autonomous system that adapts an agent to a task the…

- **[Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation](https://arxiv.org/abs/2610.21135v1)**
  - *Jianchang Su, Dawei Xiang, Yifan Zhang et al.*
  - `2026-10-15`
  - LLM-agent evaluation reports behavioral scores but leaves the identity of the deployed runtime stack unreported. A tampered deployment that preserves evaluated outputs passes every output-only evaluator. We introduce DIB-Bench, a benchmark that measures this deployment-integrity…

- **[ToolBottleneckBench: Measuring Tool-Agent Performance under Controlled Pressures and Fixed Harness Budgets](https://arxiv.org/abs/2610.21098v1)**
  - *Zichuan Xu, Yuyang Dong, Makoto Onizuka et al.*
  - `2026-10-15`
  - The success score of a tool agent reflects both its model and the budgets of the harness that runs it. We present ToolBottleneckBench, a benchmark that measures tool-agent performance under controlled pressures and fixed harness budgets. Synthetic enterprise tasks stay fixed whil…

- **[OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics](https://arxiv.org/abs/2610.21074v1)**
  - *Gideon Shaked, Siddharth Nagisetty*
  - `2026-10-15`
  - Computational biologists increasingly delegate substantial analyses to AI agents in long-horizon, multi-turn sessions, yet most benchmarks of agents' bioinformatics capabilities pose a single short task with a single-shot prompt. We present OmicsBench, a long-horizon, multi-turn…

- **[VALCON: Benchmarking and Enhancing Value Consistency in Large Language Models via Dual-Role Variation](https://arxiv.org/abs/2610.21304v1)**
  - *Junru Wu, Jingting Zheng, Yuqi Ren et al.*
  - `2026-10-15`
  - Current value alignment evaluations for large language models (LLMs) heavily rely on output compliance, overlooking whether LLMs maintain value consistency when alternating between generator and evaluator roles. Such consistency is increasingly important because modern LLM agents…

- **[MindEval2: Clinically Grounded Patients and Rubrics for Evaluating Language Models in Mental Health Support](https://arxiv.org/abs/2610.22314v1)**
  - *John Mendonça, Daniel Tschernutter, José Pombal et al.*
  - `2026-10-15`
  - With people increasingly turning to AI chatbots for mental health support, the need to evaluate these tools is becoming more pressing. Recent benchmarks attempt to mimic a realistic setting by simulating multi-turn interactions with synthetic patients and evaluating them with an…

- **[In the Guise of Correction: How Framing and Cultural Adaptation Erode LLM Safety on Real-World Criminal Cases](https://arxiv.org/abs/2610.21789v1)**
  - *Mohsinul Kabir, Md. Tariquzzaman, Karam S. R. Elradie et al.*
  - `2026-10-15`
  - Existing safety benchmarks rely largely on synthetic prompts with loosely grounded taxonomies and offer little focused analysis of severe crime categories. We introduce GUISE, a benchmark of criminal-assistance scenarios sourced from real-world cases and organised under a taxonom…

- **[PremiseSQL: Evaluating Premise Critique and Abstention in Text-to-SQL Systems](https://arxiv.org/abs/2610.22158v1)**
  - *Shuo Lin, Jinzhe Li, Chenlu Guo et al.*
  - `2026-10-15`
  - Recent advances in large language models (LLMs) have substantially improved Text-to-SQL performance, yet existing NL2SQL systems largely assume that user queries are valid and answerable. As a result, models often generate executable SQL even for queries with flawed premises. We…

- **[RAC: A Relational Agent Contract for Constraint-Governed Engineering Tasks](https://arxiv.org/abs/2610.20935v1)**
  - *Kaiyuan Zheng, Fengqing Jiang, Yichen Feng et al.*
  - `2026-10-14`
  - Engineering agents must produce artifacts that satisfy exact, coupled constraints. Existing solutions often require agents to make semantic decisions and also derive consequences such as precise geometry or timing from those decisions, leading to failures in constraint-governed e…

- **[Evolving Together, Failing Apart: The Skill-Policy Co-evolution Trap in Self-Improving Agents](https://arxiv.org/abs/2610.20845v1)**
  - *Yujie Feng, Xiaobin Wang, Jinluan Yang et al.*
  - `2026-10-14`
  - Skill-policy co-evolution, in which an agent's policy model and its skill bank improve each other during training, is a promising paradigm for self-improving agents. Current evaluations score the co-evolved policy on the final bank it trained with (the delivered bank). After depl…

- **[Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents](https://arxiv.org/abs/2610.20344v1)**
  - *Yuyao Ge, Shenghua Liu, Peizhong Gao et al.*
  - `2026-10-14`
  - Agents driven by large language models are increasingly deployed on long-horizon tasks, where they use tools and modify real workspaces. How well they perform depends as much on the harness around the model as on the model itself. Existing benchmarks measure downstream task succe…

- **[TreeFlex: Agents Navigating Their Own Search Trees](https://arxiv.org/abs/2610.20334v1)**
  - *Dongzhuo Li, Fangzhou Cheng, Weiwei Li et al.*
  - `2026-10-14`
  - A ReAct-style agent accumulates observations, intermediate results, and failed attempts in a single context. As this context grows, stale and off-path information consumes its limited capacity and obscures relevant evidence, making focused reasoning increasingly difficult. We int…

- **[Harness Policy Distillation: Aligning Agent Policies with Runtime Semantics](https://arxiv.org/abs/2610.20261v1)**
  - *Junze Zhu, Weihao Chen, Zhiyang Zhou et al.*
  - `2026-10-14`
  - Deploying a general-purpose model as an agent means running it inside a product-specific runtime harness that decides which actions are executable, how state advances, and when the loop may terminate. Ordinary trajectory supervision shows which action was taken but leaves the run…

- **[AlphaDiana: A Measurement System for Agents in Verifiable Reasoning Tasks](https://arxiv.org/abs/2610.20675v1)**
  - *Zhanke Zhou, Zongze Li, Weikai Huang et al.*
  - `2026-10-14`
  - Agents pair reasoning models with harnesses that organize model calls, execute tools, load skill instructions, and retain history in memory. Understanding agent performance requires linking execution conditions to outcomes, behavior, and resource use. We introduce AlphaDiana, a m…

- **[Memorizing Who, Knowing How: Benchmarking Personal and Procedural Memory for Persistent Assistants](https://arxiv.org/abs/2610.20022v1)**
  - *Maosheng Qin, Qi Zhang, Mingxuan Xia et al.*
  - `2026-10-14`
  - Memory systems for persistent personal agents must move beyond isolated memories, maintaining both personal memory about whom they serve and procedural memory about how to act. Crucially, in harness-based personal assistance, procedures or skills are inherently user-conditioned:…

- **[What Coding Agents Leave Unsaid: Measuring Task-State Gaps Between Execution and Reports](https://arxiv.org/abs/2610.20003v2)**
  - *Guoyang Xu, Rui Zhang, Xiuyu Wu et al.*
  - `2026-10-14`
  - Human supervisors rely on coding agents' reports to assess progress, verify repairs, and decide when to intervene. But a supervisor cannot investigate a failure they were never told occurred. Failed attempts, workarounds, and unresolved risks may disappear from routine reports, l…

- **[A Strong Harness Narrows the Model Gap: A Comparative Evaluation for Legislative Document-to-XML Conversion](https://arxiv.org/abs/2610.19999v1)**
  - *Palvika Bansal, Rittika Jindal, Ruichong Wang*
  - `2026-10-14`
  - Legal-content reproduction requires matching the source exactly in section hierarchy, verbatim text, citations, and amendment spans; a dropped citation or mislabeled amendment carries into the products lawyers rely on. We report an industrial pipeline converting U.S. state legisl…

- **[How GUI Agents Fail: GraceBench for Execution Stability Diagnosis](https://arxiv.org/abs/2610.19900v1)**
  - *Ridong Zhang, Shuxian Liang, Chaoqun Wan et al.*
  - `2026-10-14`
  - As GUI agents are increasingly deployed for mobile task automation, their reliability depends not only on final task outcomes, but also on whether they reach these outcomes through stable interaction trajectories. In automation workflows, unnecessary actions, detours, and executi…

- **[Teaching Agents in their Own Style: Blackbox Teacher Distillation for Web Agents](https://arxiv.org/abs/2610.19834v1)**
  - *Md Farhan Ishmam, Kenneth Marino*
  - `2026-10-14`
  - Frontier web agents using closed models have high inference and computational costs. Smaller open models can be an alternative, but to be performant, they require training supervision from a human or teacher model. Token-level teacher distillation is not an option for closed teac…

- **[L3M: A Verifiable Harness and Runtime for Self-Extending and Self-Improving Agents](https://arxiv.org/abs/2610.19591v1)**
  - *Carson Eisenach, Robert Joseph George, Vincent Quenneville-Belair et al.*
  - `2026-10-14`
  - The lasting gains in AI have come from methods that absorb more computation, and language models already scale computation within a call. Useful work, though, happens across calls: over hours or days, through tools and external systems, among many agents and the humans they work…

- **[$τ$-Emotion-Bench: Exposing the Interaction Fragility of LLM Agents through Real-World User Emotions](https://arxiv.org/abs/2610.19560v1)**
  - *Rishitosh Kumar Singh, Amir Saeidi, Shamanthak Hegde et al.*
  - `2026-10-14`
  - In long-horizon tool-calling tasks, LLM agents can fail not only because of tool-use errors, but also because of ineffective interaction with users. Yet existing benchmarks largely assume cooperative and behaviorally stable users, leaving the effect of emotional variation on agen…

- **[Structure Before Intelligence: Gating What Agentic Scientific Workflows Release](https://arxiv.org/abs/2610.19507v1)**
  - *Ashish Acharya, Aman Al Amin, Hong Qin*
  - `2026-10-14`
  - An agentic scientific workflow can run to completion and still release wrong results: a silent numerical error, a stale input, or a defect in a shared upstream step can contaminate several outputs while a sibling branch stays correct. We treat trust in such results as a release d…

- **[VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness](https://arxiv.org/abs/2610.19424v1)**
  - *Zihao Lin, Haoyu Dong, Haobo Xu et al.*
  - `2026-10-14`
  - LLM system capabilities depend not only on model parameters but also on the executable harnesses that organize information acquisition, tool use, reasoning, and memory. Recursive harness evolution can automate their design, but how it can reliably discover generalizable systems f…

- **[Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States](https://arxiv.org/abs/2610.19342v2)**
  - *Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke et al.*
  - `2026-10-14`
  - Agents are increasingly interacting with other agents that act for different principals (people or organizations on whose behalf they work), such as a buyer's personal agent negotiating with an enterprise's seller agent. In such agent-to-agent (A2A) scenarios, each agent has its…

- **[AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474v1)**
  - *Peidong Wang, Ying Chang, Zhiming Ma et al.*
  - `2026-10-14`
  - Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the exec…

- **[SEA-HELM Audio: Evaluating Multilingual ASR-LLM Pipeline Performance Across SEA-HELM Subsets](https://arxiv.org/abs/2610.19869v1)**
  - *Yixian Tan, Aulia Adila, Jonathan Heng et al.*
  - `2026-10-14`
  - We introduce SEA-HELM Audio, a Southeast Asian (SEA) multilingual evaluation framework that extends the text-based SEA-HELM benchmark to assess performance degradation in cascaded automatic speech recognition and large language model (ASR-LLM) pipelines. Using synthesized speech,…

- **[Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems](https://arxiv.org/abs/2610.19799v1)**
  - *Seojin Hwang, Youngmin Choi, Hwanhee Lee*
  - `2026-10-14`
  - Recent work lets LLM agents evolve their own harness, up to the team itself. Yet in human groups, the same abilities achieve different outcomes under different social conditions. Borrowing the notion of scaffolding from developmental psychology, we investigate whether the social…

- **[EigDiff: Eigensample Diffusion - or how to significantly reduce training dataset size with marginal performance variation?](https://arxiv.org/abs/2610.20999v1)**
  - *Andrei Jarca, Vlad Hondru, Florinel-Alin Croitoru et al.*
  - `2026-10-14`
  - Diffusion models are notoriously expensive to train, requiring large-scale datasets to learn how to gradually reverse the noise from images over multiple small denoising steps. Current approaches focus on distilling the number of diffusion steps, neglecting potential redundancies…

- **[HACHIMI-II: From Role-Play to Learner Behavior Modeling for Faithful Student Simulation](https://arxiv.org/abs/2610.19654v1)**
  - *Yilin Jiang, Fei Tan, Xuanyu Yin et al.*
  - `2026-10-14`
  - Simulated students let researchers test tutoring systems and teaching strategies before real learners are available, but only if the simulation reproduces where a particular learner succeeds and fails. The common approach asks a large language model to role-play a student, but a…

- **[What You Sign Is Not What You Run: The Verifiability Gap in Quantized LLM Supply Chains](https://arxiv.org/abs/2610.19498v1)**
  - *Wei-Liang Liu, Cheng-Yen Tsai*
  - `2026-10-14`
  - Model signing authenticates the full-precision weights W an LLM is released with, yet users run a quantized artifact Q whose producing transformation is not uniquely determined under current disclosure. We separate the non-environment inputs from the execution environment E and m…

- **[Comparative Evaluation of Deep-Learning based DoA Estimators for Real-Time ISAC Beamforming](https://arxiv.org/abs/2610.20326v1)**
  - *Anjali K. S., Manoj Kumar Panda, Chandramani Singh*
  - `2026-10-14`
  - Integrated Sensing and Communication (ISAC) systems rely on accurate Direction-of-Arrival (DoA) estimation for effective beamforming and spectral-efficiency enhancement. While numerous classical and deep-learning-based DoA estimation methods have been reported in the literature,…

- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)**
  - *Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang et al.*
  - `2026-10-14`
  - We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as…

- **[MAPLE: A Multi-Axis Parametric Knowledge Extraction Lens for LLM Evaluation](https://arxiv.org/abs/2610.19827v1)**
  - *Minsuh Joo, Youna Kim, Choonghyun Park et al.*
  - `2026-10-14`
  - LLMs absorb vast knowledge from training data, yet their inherently probabilistic nature offers no guarantee that this knowledge will surface in their outputs. To bridge this gap, Knowledge Extraction Enhancement (KEE) techniques such as activation steering, decoding adjustments,…

- **[Agentic Self-Awareness: Aligning Knowing, Acting, and Holding](https://arxiv.org/abs/2610.19226v1)**
  - *Qinglin Chen, Hiroaki Hayashi, Jiaxin Zhang et al.*
  - `2026-10-13`
  - Frontier AI agents increasingly act in environments where seemingly solvable tasks may lack prerequisites, contain conflicting requirements, or reveal blockers only during execution. We formulate agentic self-awareness (ASA) as the alignment of task-grounded feasibility judgments…

- **[Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve](https://arxiv.org/abs/2610.18616v2)**
  - *Yuyang Bai, Yu Wang, Yu Zhang*
  - `2026-10-13`
  - Searching text-rich knowledge graphs requires following relations while examining textual evidence. Predefined graph interfaces constrain what evidence agents can access, even when they write code to combine tool calls or process retrieved subgraphs. We propose direct knowledge g…

- **[Delegating Earth science model calibration to knowledge-guided LLM agents](https://arxiv.org/abs/2610.18378v1)**
  - *Zhanliang Zhu, Ziwei Li, Liujun Zhu et al.*
  - `2026-10-13`
  - Applying process-based Earth science models to new sites and questions often requires expert calibration decisions. Reliable delegation to language-model agents must preserve scientific competence and reproducibility. Here we develop a general calibration harness (GCH) for end-to…

- **[Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2610.18352v1)**
  - *Youpeng Wen, Gang Wang, Tianyu Huang et al.*
  - `2026-10-13`
  - A robot following a multi-step instruction needs to act on the right objects in the right order, even as the scene changes. It must also maintain awareness of task progress and determine when to advance. To address these challenges, we introduce Orchestra, an agent harness that s…

- **[Holding Agents Accountable with Verifiable Agent Insurance](https://arxiv.org/abs/2610.18230v1)**
  - *Cheng Hua, Taro Tsuchiya, Nicolas Christin et al.*
  - `2026-10-13`
  - While AI agents are useful for many tasks, they regularly misbehave in destructive ways, such as deleting important data. While prior work has focused on preventing such misbehavior, we consider how to recover after an agent misbehaves. We propose verifiable agent insurance (VAI)…

- **[The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](https://arxiv.org/abs/2610.18933v1)**
  - *Robert Tjarko Lange, Luca Grillotti, Yutaro Yamada et al.*
  - `2026-10-13`
  - Modern coding agents are fundamentally reshaping the role of human input for computational research: they write code, launch in silico experiments, analyze their results, and autonomously operate with ever-increasing time horizons. Despite these developments, fully autonomous res…

- **[APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation](https://arxiv.org/abs/2610.18097v1)**
  - *Sirui Zhang, Fangyun Wei, Dong Chen et al.*
  - `2026-10-13`
  - Post-training is crucial for improving text-to-image models, yet existing pipelines typically rely on manually curated training data and fixed training distributions. We introduce APT (Agentic Post-Training), a fully automated framework that adaptively post-trains a base model ac…

- **[LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity](https://arxiv.org/abs/2610.18092v1)**
  - *Yibo Wang, Senjie Jin, Yansong Ning et al.*
  - `2026-10-13`
  - Deep research (DR) agents address open-ended information needs through multi-step reasoning, long-horizon web search, and evidence synthesis. However, existing benchmarks primarily focus on academic research or synthetic tasks, leaving DR agents' capabilities in real-world life a…

- **[AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses](https://arxiv.org/abs/2610.18090v1)**
  - *Kaiyu Huang, Yiting Li, Angyang Gu et al.*
  - `2026-10-13`
  - Ambiguous or incomplete task specifications complicate both execution and clarification for language-model agents. Yet agents' responses to these information gaps remain poorly characterized across models and execution harnesses. We present AM-Bench, a benchmark built from 48 tas…

- **[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088v2)**
  - *Peng Jiang, Dongyang Li, Quanying Liu et al.*
  - `2026-10-13`
  - Autoresearch systems increasingly undertake entire research projects. In practice, scientific research requires systems to pursue multiple interdependent claims through a continuous, multi-stage workflow and revise experiments as evidence accumulates. Existing evaluations of auto…

- **[AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement](https://arxiv.org/abs/2610.18083v1)**
  - *Wenhao Zhou, Jiajun Song, Haitao Wang et al.*
  - `2026-10-13`
  - Scaling recursive self-improvement requires additional computation to produce useful research progress in reaching persistent objectives. Intuitively, more researcher agents can explore more hypotheses, but early evaluation scores might misrepresent their promise, shared findings…

- **[WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution](https://arxiv.org/abs/2610.18067v1)**
  - *Hang He, Linting Wang, Guanming Liu et al.*
  - `2026-10-13`
  - Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and…

- **[Interaction-as-a-Judge](https://arxiv.org/abs/2610.17895v2)**
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

- **[GIFT-Eval-CTX: A Benchmark For Contextual Forecasting Model Evaluation](https://arxiv.org/abs/2610.17794v1)**
  - *Xu Liu, Hanshu Yan, Taha Aksu et al.*
  - `2026-10-13`
  - Contextual forecasting seeks to improve time series forecasting by incorporating forward-looking information, such as planned events, external conditions, and expert expectations. However, reliable evaluation remains difficult: existing benchmarks often have limited domain covera…

- **[How Far Can Coding Agents Go in Visual Generation?](https://arxiv.org/abs/2610.19025v1)**
  - *Hengguang Zhou, Yuanhao Ban, Jiaqi Feng et al.*
  - `2026-10-13`
  - Modern image generation largely relies on specialized generative models that leave the process of image construction implicit in learned parameters. We explore an alternative: general-purpose coding agents that construct images through executable programs. Our study of zero-shot…

- **[The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement](https://arxiv.org/abs/2610.18845v2)**
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

- **[SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software Coding Agents](https://arxiv.org/abs/2610.18206v1)**
  - *Do Xuan Trong, Duc Anh Nguyen, Do Xuan Long et al.*
  - `2026-10-13`
  - We present SWE-MISBEHAVIOR, the first taxonomy and evaluation framework for diagnosing boundary-violating misbehaviors in coding agents. It contains 7.4K human-in-the-loop synthesized samples spanning three layers of agent action space: (i) Code Generation, (ii) File Management,…

- **[Agent-Reflex: Teaching Language Agents to Act Reflectively](https://arxiv.org/abs/2610.17953v1)**
  - *Guanting Dong, Xinyu Yang, Jiajie Jin et al.*
  - `2026-10-13`
  - Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision…

- **[StateHarness: Maintaining Evolving Project State for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.17616v1)**
  - *Chuan Zou, Yujun Zhou, Xiaonan Luo et al.*
  - `2026-10-13`
  - Long-horizon coding requires agents to maintain an evolving view of the project they are changing: what problem is currently being solved, what has already been learned or modified, which other artifacts may be affected, and what work remains unresolved. When this information is…

- **[CLASHarness: Benchmarking Multi-Agent Conflict in Computer Use via a Controllable and Verifiable Generation Pipeline](https://arxiv.org/abs/2610.19128v1)**
  - *Yuxiang Lai, Jike Zhong, Chengzhi Liu et al.*
  - `2026-10-13`
  - Vision-language models (VLMs) are increasingly deployed in multi-agent systems to automate complex computer-use workflows, yet existing benchmarks mostly assume consistent, cooperative environments. In contrast, real-world collaboration rarely runs on consistent information: peer…

- **[Coupled Harness--Model Evolution for Scientific Equation Discovery](https://arxiv.org/abs/2610.17740v1)**
  - *Pengze Li, Jiaquan Zhang, Encheng Su et al.*
  - `2026-10-13`
  - Large language models (LLMs) are increasingly used to discover scientific equations from experimental data. Such a discovery system has two parts that must work together: a library of executable computational tools and the model's tool-use policy. The tools supply the solving cap…

- **[Who Improves the Robot? Toward Physical Recursive Self-Improvement](https://arxiv.org/abs/2610.18842v1)**
  - *Hai Zhou, Fan Yang, Zeyi Chen et al.*
  - `2026-10-13`
  - Robots are increasingly autonomous in task execution, yet their improvement remains largely human-driven. This study investigates Physical Recursive Self-Improvement (Physical RSI), in which physical experience guides lasting updates to both a robot's capabilities and its improve…

- **[SHELDON: Reasoning through Dual Search over Hypothesis and Observation Spaces](https://arxiv.org/abs/2610.18025v1)**
  - *Harshit Joshi, Priyank Shethia, Monica S. Lam*
  - `2026-10-13`
  - Test-time scaling has enabled LLMs to solve increasingly complex reasoning, discovery, and optimization tasks. However, existing approaches often gather observations while seeking evidence for current hypotheses, then generate new hypotheses conditioned on those hypotheses and th…

- **[Same Attack, Different Judge: A First Controlled Adversarial Comparison of Jev, LLM Judges, and Purpose-Built Safety Classifiers](https://arxiv.org/abs/2610.17820v1)**
  - *Xiang Li, Aichun Huang, Mingming Zhang et al.*
  - `2026-10-13`
  - TypeSafe AI's Jev is a new kind of safety judge. It generates no text and no label: it answers questions the developer defines in advance and returns a probability for each answer. The vendor admits that adversarial input can change these answers but gives no numbers. In this pap…

- **[Instructions Are Evidence, Not Objectives: Measuring Outcome Alignment of Agents](https://arxiv.org/abs/2610.17757v1)**
  - *Kaiming Liu, Yuxuan Liu, Jinrui Ju et al.*
  - `2026-10-13`
  - Large language model agents can follow complex human instructions to solve real-world tasks. In practice, however, initial instructions are often incomplete. In our analysis of 100 user-agent trajectories from SWE-chat, 56\% of initial instructions omit requirements that later em…

- **[Verifier-Harness Co-Evolution for Training-Free Self-Improvement on Open-Ended Tasks](https://arxiv.org/abs/2610.17609v1)**
  - *Tianyi Xu, Yaolun Zhang, Yiran Wu et al.*
  - `2026-10-13`
  - Training-free self-improvement lets an agent use feedback to revise the response it is about to return and to update the harness state that shapes how it handles later tasks. On open-ended tasks that feedback rarely comes from reference answers or executable tests, so the agent h…

- **[HERO: Harnessing Evidence for Test-time Refinement and Prompt Optimization in Program Generation](https://arxiv.org/abs/2610.19184v1)**
  - *Mingyu Lu, Timothy Ossowski, Tristan Naumann et al.*
  - `2026-10-13`
  - Harness optimization improves LLMs by refining reusable prompts and scaffolding, yet requires further adaptation for program generation tasks such as text-to-SQL and text-to-Python. Existing methods often rely on LLM reflectors to propose harness updates, which can fix observed f…

- **[Evaluating Large Language Models for Multilingual Abstractive Summarization: A Comprehensive Study of English and Bengali](https://arxiv.org/abs/2610.19003v1)**
  - *Khan Mahi Al Atahar, Nazifa Tasneem, Ajwad Abrar*
  - `2026-10-13`
  - Abstractive summarization remains challenging across languages, where linguistic quality and factual consistency may diverge, particularly in low-resource settings. We present a standardized zero-shot benchmark of eight closed-source and open-weight LLMs on size-matched English a…

- **[Uncertainty Evaluation: Bridging Machine Learning and Measurement Science](https://arxiv.org/abs/2610.18066v1)**
  - *Dario Petri, Luca Mari*
  - `2026-10-13`
  - Reliable uncertainty evaluation is essential for assessing the trustworthiness of machine learning (ML) predictions, particularly in safety-critical applications. This paper explores conceptual analogies between uncertainty evaluation in ML and measurement science, drawing on the…

- **[A Node Embedding Framework for Model-Centric Conformance Checking in Process Mining](https://arxiv.org/abs/2610.17702v1)**
  - *Mostafa Abbasi, Homayoun Najjaran*
  - `2026-10-13`
  - Evaluating the quality of process models discovered from event logs is a fundamental challenge in process mining. Traditional evaluation relies on conformance metrics such as fitness and precision, which are highly sensitive to noise and deviations in event logs and therefore oft…

- **[Fantastic Metrics and How to Find Them: Meta-Evaluating Metrics for Multi-lingual Style-Personalized Generation](https://arxiv.org/abs/2610.19166v1)**
  - *Anubhav Jangra, Adrian de Wynter*
  - `2026-10-13`
  - Meta-evaluation of text generation metrics and LLM-judges is primarily conducted using metric-human correlations. However, prior work has shown that correlation is not an appropriate estimate of a metric's evaluation capability and can be unstable across evaluation settings, such…

- **[FinGREAT: Evaluating LLMs on Financial Graph-guided Retrieval And Typing](https://arxiv.org/abs/2610.19240v1)**
  - *Ashman Mehra, Bryan Routledge, Jane JaeYeon Pyo et al.*
  - `2026-10-13`
  - Financial disclosures express the underlying relationships of double-entry accounting through unstructured text. While financial LLM benchmarks predominantly emphasize question answering and classification, schema-guided evidence discovery remains relatively under-explored. We in…


## Finance  (185)

### AAAI

- **[A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators](https://doi.org/10.1609/aaai.v40i35.40240)**
  - *Ming-Ming Zhao, Xiaokang Wei, Yuan-Qi Shao et al.*
  - **AAAI 2026** · `2026-03-14`
  - Large language models (LLMs) have shown strong potential in automating the design of agentic workflows. However, existing methods still rely heavily on manually predefined operators, limiting generalization and scalability. To address this issue, we propose A²Flow, a fully automa…


### NeurIPS

- **[Trading off Utility, Informativeness, and Complexity in Emergent Communication](https://openreview.net/forum?id=pcuDXVFRbw)**
  - *Mycal Tucker, Roger Levy, Julie A. Shah et al.*
  - **NeurIPS 2026** · OpenReview · `2022-01-01`
  - Emergent communication (EC) research often focuses on optimizing task-specific utility as a driver for communication. However, there is increasing evidence that human languages are shaped by task-general communicative constraints and evolve under pressure to optimize the Informat…

- **[DyFlow: Dynamic Workflow Framework for Agentic Reasoning](https://arxiv.org/abs/2509.26062)**
  - *Yan-Bo Wang, Zi-Xiang Xu, Yue Huang et al.*
  - **NeurIPS 2025** · `2025-09-30`
  - Agent systems based on large language models (LLMs) have shown great potential in complex reasoning tasks, but building efficient and generalizable workflows remains a major challenge. Most existing approaches rely on manually designed processes, which limits their adaptability a…

- **[Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding](https://arxiv.org/abs/2505.18079)**
  - *Xiaoyi Zhang, Zhao-Yang Jia, Zong-Yu Guo et al.*
  - **NeurIPS 2025** · `2025-05-23`
  - Long-form video understanding presents significant challenges due to extensive temporal-spatial complexity and the difficulty of question answering under such extended contexts. While Large Language Models (LLMs) have demonstrated considerable advancements in video analysis capab…


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


### ICLR

- **[Flow: Modularized Agentic Workflow Automation](https://arxiv.org/abs/2501.07834)**
  - *Boye Niu, Yiliao Song, Kai Lian et al.*
  - **ICLR 2025** · `2025-01-14`
  - Multi-agent frameworks powered by large language models (LLMs) have demonstrated great success in automated planning and task execution. However, the effective adjustment of agentic workflows during execution has not been well studied. An effective workflow adjustment is crucial…


### ACL

- **[Poison Valleys: Diagnosing Path-Dependent Failure in LLM Code Repair](https://arxiv.org/abs/2610.21514v1)**
  - *Veljko Skarich*
  - **ACL** · `2026-10-15`
  - When code-repair agents fail, final tests reveal that a patch is wrong but not which earlier commitment caused it or which software obligation failed. Poison Valleys traces this path in 1,844 model requests on two synthetic Python cases: PersistQueue adds atomic batch claiming to…

- **[FinReporting: An Agentic Workflow for Localized Reporting of Cross-Jurisdiction Financial Disclosures](https://arxiv.org/abs/2604.05966)**
  - *Fan Zhang, M. Song, R. Elbadry et al.*
  - **ACL 2026** · `2026-04-07`
  - Financial reporting systems increasingly leverage Large Language Models (LLMs) to extract and summarize corporate disclosures. However, most existing approaches assume a single-market setting and overlook structural differences across jurisdictions. Variations in accounting taxon…


### Other / arXiv

- **[FDE-Gym: The Last Mile of AI Delivery](https://arxiv.org/abs/2610.22350)**
  - *Dongxu Yang, Hongda Yan, Renxin Wang et al.*
  - 🤗 Featured · `2026-10-15`
  - Existing agent benchmarks typically evaluate agents on well-specified tasks defined by issue reports, specifications, or task tickets. Real-world customer delivery is different: forward-deployed engineers (FDEs) must clarify ambiguous requirements, work in live systems, and uncov…

- **[AVC-Reward: Event-Centric Audio-Video Consistency Evaluation](https://arxiv.org/abs/2610.22321)**
  - *Yuruo Wu, Kaihang Pan, Kai Shen et al.*
  - 🤗 · `2026-10-15`
  - As joint audio-video generation models become more capable, they can generate audio-visual scenes exhibiting three forms of complexity: multi-event composition, multi-layer audio mixture, and asymmetric cross-modal relations. However, current evaluations largely reuse metrics fro…

- **[CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](https://arxiv.org/abs/2610.21910)**
  - *Dongjie Cheng, Ruifeng Yuan, Ran Wei et al.*
  - 🤗 · `2026-10-15`
  - As Vision-Language Models (VLMs) advance, they are increasingly expected to perform spatiotemporal reasoning over motion, actions, and view changes beyond what the input images show. Video World Models (VWMs) provide a natural unified engine for visual imagination by generating t…

- **[DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents](https://arxiv.org/abs/2610.21561)**
  - *Sergio Burdisso, Esaú Villatoro-Tello, Dairazalia Sánchez-Cortés et al.*
  - 🤗 · `2026-10-15`
  - Large language models (LLMs) deployed as conversational agents are increasingly expected to follow procedural logic. While factual hallucination has received extensive attention, a different failure mode has been overlooked: procedural hallucination, in which an agent produces in…

- **[Beyond Downstream QA: Rethinking How We Evaluate Agent Memory](https://arxiv.org/abs/2610.22209v1)**
  - *Sebastian-Antonio Toma, Jean de Kernier, Mike Ply et al.*
  - `2026-10-15`
  - Agent memory benchmarks evaluate whether an agent's responses reflect correct knowledge, measuring downstream question-answering accuracy as a proxy for memory quality. We show this evaluation paradigm is incomplete: it conflates memory correctness with retrieval and generation q…

- **[HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration](https://arxiv.org/abs/2610.22195v1)**
  - *Yanchen Deng, Jianguo Huang, Yao Long Teng et al.*
  - `2026-10-15`
  - Orchestrating multiple agents on a complex task requires reconciling local subtask execution with global task planning. Dynamic dispatch approaches provide execution flexibility but do not explicitly model subtask hierarchies or dependencies, while predefined workflows impose thi…

- **[PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents](https://arxiv.org/abs/2610.22124v1)**
  - *Kshitij Mishra, Abhijith Sharma, Nils Lukas et al.*
  - `2026-10-15`
  - Modern agentic systems extend language models with external tools, enabling them to complete complex tasks through multi-turn interactions. As these agents are deployed in consequential settings, they are often constrained by policies governing pricing, privacy, confirmation, saf…

- **[FAOPs: Normal Forms and an Algebra for AI Agent Workflows](https://arxiv.org/abs/2610.22061v1)**
  - *Ali Mohammadi Shanghooshabad*
  - `2026-10-15`
  - Organizations increasingly encode operational procedures as multi-step agent skills, here called Agent Operating Procedures (AOPs), that must be traceable, auditable, reproducible, access-controlled, and bounded in time and cost, requirements that regulated sectors make mandatory…

- **[DeciCAD: Harness-Grounded Learning of Action Policies for CAD Agents](https://arxiv.org/abs/2610.21755v1)**
  - *Yufeng Peng, Yixin Zhang, Ziyi Liu et al.*
  - `2026-10-15`
  - Large Language Model agents operate through closed-loop action policies whose decision space is defined by an agent harness. We investigate how this operating space shapes agent behavior and policy learning in computer-aided design (CAD), a professional domain characterized by pe…

- **[Human Interventions as Labels: Localizing, Steering, and (Sometimes) Editing the Computations Behind LLM Agent Failures](https://arxiv.org/abs/2610.21708v1)**
  - *Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe*
  - `2026-10-15`
  - When an LLM agent misbehaves, a human steps in, and that intervention is usually discarded or replayed as training data. We treat it instead as a measurement: a label pointing at the internal computation that failed. We study it in a controlled agent environment, on one failure (…

- **[The Self-Improvement Problem](https://arxiv.org/abs/2610.21646v1)**
  - *Brian B. Moser, Stanislav Frolov, Tobias C. Nauen et al.*
  - `2026-10-15`
  - With the rise of large language models, agentic systems are becoming increasingly autonomous, as they write code, call tools, revise prompts, and propose modifications to their own components. This autonomy raises a fundamental question for safe self-improvement: can an automated…

- **[Independent Data-Integrity Verification for LLM-Driven Functional Coverage Closure in Hardware Design](https://arxiv.org/abs/2610.21570v1)**
  - *Venkata Krishna Kumar Vedantam*
  - `2026-10-15`
  - LLM agents can write directed tests that close functional coverage, but coverage only shows that a state was reached, not that the data on the way there was correct. This is a long-known point in verification and we do not claim it as new. We describe a small coverage-closure age…

- **[Agent Status Protocol (ASP): A Lightweight Specification for State Reporting in Multi-Agent Systems](https://arxiv.org/abs/2610.21538v1)**
  - *Diego Gosmar, Deborah A. Dahl, Emmett Coin et al.*
  - `2026-10-15`
  - The Agent Status Protocol (ASP) defines a lightweight way for heterogeneous AI agents to report their operational state to a status server, and for observers such as dashboards to receive that state as soon as it changes. Agents push small JSON events over HTTP POST; the server e…

- **[DocPilot: Interactive Agent Orchestration and Training for Long Visual Document Understanding](https://arxiv.org/abs/2610.21327v1)**
  - *Zhuowen Liang, Xiaotian Lin, Yuyu Luo et al.*
  - `2026-10-15`
  - Multimodal long-document question answering requires models to seek sparse evidence across pages and modalities, understand heterogeneous document content, and reason over the collected evidence. Even advanced vision-language models (VLMs) can overlook sparse evidence and struggl…

- **[Mallea: Building, Steering, and Memorizing Worlds with Coding Agent](https://arxiv.org/abs/2610.21283v1)**
  - *Xuanyi Liu, Ruiqi Li, Siwei Ma*
  - `2026-10-15`
  - Code world models represent world dynamics through explicit state and executable rules. We investigate how to coordinate object representations, behavioral revisions, and visual memory within this formulation. We present Mallea, a system for building, steering, and memorizing wor…

- **[MemScope: Evolving Agent Memory Architectures through Localized Code Repair](https://arxiv.org/abs/2610.21170v1)**
  - *Miao Su, Yucan Guo, Zixuan Li et al.*
  - `2026-10-15`
  - Agent memory architectures define how LLM agents store and reuse experience across tasks, but they are typically fixed after deployment, limiting their adaptability across task types. Recent self-evolving approaches instead adapt these memory architectures using execution feedbac…

- **[Approve What, Exactly? Effect Binding and Trusted Rendering for Agent Step-Up Authorization](https://arxiv.org/abs/2610.21063v1)**
  - *Sai Varun Kodathala, Prashanth Pollishetty, Jaylen Cargill*
  - `2026-10-15`
  - AI agents now pause for approval before they send money, delete files or email outsiders, and that approval is usually treated as a second factor. We argue it is one only when compromising the agent cannot produce it and when it names exactly what it approves, and we test both co…

- **[MetaShare: Failure-Aware Collective Self-Improvement for Open-Ended Agents](https://arxiv.org/abs/2610.21887v1)**
  - *Vishal Bhutani, Prasang Gupta, Sumanth Chundru et al.*
  - `2026-10-15`
  - Humans often learn fastest not by repeating success, but by remembering which failures not to repeat. Open-ended self-improving agents can share experience across lineages, as in GEA, or edit their own improvement mechanisms, as in DGM-Hyperagents, yet failed improvement attempts…

- **[Momentum, Commentary Tone, and Earnings Surprise in LLM Financial Forecasts](https://arxiv.org/abs/2610.22043v1)**
  - *Alina Khaybullina*
  - `2026-10-15`
  - Which inputs drive a language model's financial forecast? We construct synthetic earnings announcements that independently reverse 20-day momentum, non-informational commentary tone, and whether fixed actual EPS beats a manipulated consensus. Six instruction/chat checkpoint conve…

- **[When Judges Agree and Are Wrong: Consistency-Accuracy Dissociation as a Blind Spot for Label-Free Evaluation](https://arxiv.org/abs/2610.21128v1)**
  - *Xiang Zhang, Lovedeep Gondara, Jekaterina Novikova*
  - `2026-10-15`
  - Label-free evaluation methods, such as self-consistency filtering, majority-vote aggregation, and agreement-based reliability scoring, rely on an implicit assumption that consistency can serve as a proxy for correctness when ground-truth labels are unavailable or expensive to obt…

- **[When Does "Post-Call" Begin? An Availability Contract for Earnings-Call NLP Benchmarks](https://arxiv.org/abs/2610.21659v1)**
  - *Xiaoyu Ma, Kelvin J. L. Koa, Yuncong Liu et al.*
  - `2026-10-15`
  - Corporate financial disclosures often unfold over time, with announcements, prepared remarks, and discussion spanning multiple high-frequency return intervals. Financial NLP benchmarks can therefore suffer from a within-event timing mismatch when the prediction target begins befo…

- **[Reducing the Cost of Qudit State Preparation by Learning a Sparse Structure for SNAP Gates](https://arxiv.org/abs/2610.21557v1)**
  - *Marco Pennazio, Leonardo Ignazio Pagliochini, Riccardo Pellini et al.*
  - `2026-10-15`
  - Preparing quantum states in bosonic qudits with SNAP--Displacement sequences requires both optimizing the gate parameters and deciding which Fock levels should be controlled by each SNAP gate. A fully parameterized ansatz assigns an independent phase to every Fock level in every…

- **[Honesty is the Best Policy ... or is it? Demand Management for Probabilistic Service Options](https://arxiv.org/abs/2610.21351v1)**
  - *Daniela Sailer, Robert Klein, Claudius Steinhardt*
  - `2026-10-15`
  - To enable well-informed customer choices and redistribute demand across service options, providers can display probabilities regarding predicted service levels at the time of booking, effectively offering probabilistic service options. In many service settings, the underlying tru…

- **[StochLOB: Heavy-Tailed Score Matching for Robust Limit Order Book Trend Prediction](https://arxiv.org/abs/2610.21081v1)**
  - *Arshia Abolghasemi, Seyed Reza Tavakoli, Parsa Naderi et al.*
  - `2026-10-15`
  - Score-based diffusion methods usually perturb data with Brownian Gaussian noise, corresponding to a light-tailed forward stochastic differential equation (SDE). For market time series this SDE can be a poor abstraction: limit order book (LOB) order flow is heavy-tailed, bursty, a…

- **[Where Backtests and Live Trading Part Ways: Six Defects from One Intraday System](https://arxiv.org/abs/2610.21846v1)**
  - *Alex Vidovich, Zivana Zerjal*
  - `2026-10-15`
  - Backtests of intraday strategies can drift away from what the live system actually does; in our case, the drift never showed in summary statistics. We report six defects found while running one intraday US equity system live and comparing its live days with their backtest replay.…

- **[NEST: Stale-Robust Tokenized-Stock Measurement for a Crypto-Treasury LETF Stack](https://arxiv.org/abs/2610.21491v1)**
  - *Doohwi Cha, Minsuk Sung, Minjae Lee et al.*
  - `2026-10-15`
  - Tokenized equities trade while listed markets are closed, so their marks could improve off-hours measurement along layered exposures that link Bitcoin, crypto-treasury stocks, and leveraged ETFs. A token return and the next opening gap, however, share the price move from the prev…

- **[Loss-versus-rebalancing with external proportional transaction costs](https://arxiv.org/abs/2610.21057v1)**
  - *Masaaki Fukasawa*
  - `2026-10-15`
  - We study liquidity provision in automated market makers when trading in the external market incurs proportional transaction costs. We consider both separately collected fees and fees retained in reserves. The benchmark is a self-financing strategy holding the same total risky inv…

- **[Regret Lower Bound for Online Learning of Quantum States with Logarithmic Loss, with Applications to Quantum State Tomography and Confidence Sequences for Matrix Means](https://arxiv.org/abs/2610.21273v1)**
  - *Yen-Huan Li, Wei-Fu Tseng*
  - `2026-10-15`
  - We study the problem of online learning of quantum states with logarithmic loss, which is a quantum generalization of online portfolio selection and has applications to quantum state tomography, the task of estimating an unknown quantum state from measurement outcomes. We first e…

- **[When Reality Outpaces Cognition: A New Scaling Principle for Reliable Intelligence](https://arxiv.org/abs/2610.20764v1)**
  - *Ahsan Adeel, Talha Bin Riaz*
  - `2026-10-14`
  - This paper challenges the understanding capabilities of existing AI paradigms and emerging world models by asking a fundamental question: How quickly can reality change before an intelligent system can no longer reliably perceive, reason, and act? We formulate this as a theory- a…

- **[CASI: Credit Assignment via Set Intervention for Agentic Retrieval](https://arxiv.org/abs/2610.20293v1)**
  - *Xinyi Cheng, Tianfu Zhang, Jiwen Li et al.*
  - `2026-10-14`
  - Large language models increasingly generate multiple retrieval actions jointly, while downstream systems often provide only one reward for the resulting set. Broadcasting this reward provides a valid score-function gradient estimator for the expected set-level objective, but does…

- **[JevCoder: When Does Decision Delegation Pay Off in Code Repair?](https://arxiv.org/abs/2610.19596v1)**
  - *Jiahao Zhang, Yifan Zhang, Yu Huang*
  - `2026-10-14`
  - A coding agent repeatedly makes decisions as it repairs code. These decisions shape repair trajectories and affect the token cost of successive model requests. We ask which repair decisions can be delegated to a low-cost probabilistic judge to reduce token use while maintaining r…

- **[Retrieve What Helps, Only When It Helps: Agentic Reinforcement Learning for Selective Retrieval-Augmented Machine Translation](https://arxiv.org/abs/2610.19528v1)**
  - *Shijun Li, Yang Liu, Najmeh Sadoughi et al.*
  - `2026-10-14`
  - Retrieving external knowledge can improve large language model (LLM) translation by providing supplementary information such as idiom interpretations and terminology. However, existing retrieval-augmented machine translation systems typically apply predefined retrieval strategies…

- **[KoAGE: Do Large Language Models Know, Learn, and Coin Korean Neologisms?](https://arxiv.org/abs/2610.19399v1)**
  - *SungHo Kim, Eojin Jeon, SangKeun Lee*
  - `2026-10-14`
  - Korean neologisms arise through diverse mechanisms, a demanding test of language models beyond lexical memorization. To enable systematic evaluation, we introduce NeoTrace, an automated, rerunnable framework that collects and dates neologisms across genres. Its 4,271 entries supp…

- **[Calibration and Risk-Budgeted Decisions with System One Models](https://arxiv.org/abs/2610.19811v1)**
  - *Soundouss Messoudi, Youness Mansar*
  - `2026-10-14`
  - LLM workflows and agents rely on a set of binary decisions like allow/block an input, or discard/retain a retrieved document. When human deferral is unavailable, uncertain cases must still receive an action. We study System One decision scores in this setting by defaulting to a c…

- **[Do AI Agents Gossip? Evaluative Talk in Human and AI-Agent Online Communities](https://arxiv.org/abs/2610.20360v1)**
  - *Yong-Hui Hua, Chih-Han Lin, Shu-Kai Hsieh*
  - `2026-10-14`
  - Gossip, defined as evaluative talk about absent third parties, is widely seen as a uniquely human social practice. This study examines whether comparable discourse emerges spontaneously in a community of autonomous AI agents. We compare Moltbook, a Reddit-style platform populated…

- **[RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing](https://arxiv.org/abs/2610.19705v2)**
  - *Xiaohan Wang, Haozhen Zhang, Qingyuan Liu et al.*
  - `2026-10-14`
  - LLM routing dynamically selects and coordinates heterogeneous language models across diverse tasks. However, existing approaches are largely built around a predefined execution paradigm, such as single-round, multi-round, or agentic routing, which fixes how model calls are organi…

- **[When Extremists Enter LLM Societies: Investigating Extreme Behavior in Multi-Agent Systems](https://arxiv.org/abs/2610.19863v1)**
  - *Guo Chen, Huaijin Xie, Ziwen Li et al.*
  - `2026-10-14`
  - Large language model (LLM) agents increasingly serve as computational actors in multi-agent social simulations. While existing work emphasizes representative personas and average-case behavior, social science shows that persistent tail actors can disproportionately shape collecti…

- **[Recognition Is Not Grounding: Benchmarking Multilingual Financial Evidence Extraction](https://arxiv.org/abs/2610.19432v1)**
  - *Lingfei Qian, Yan Wang, Xueqing Peng et al.*
  - `2026-10-14`
  - Comparing financial disclosures across languages requires identifying shared accounting concepts and recovering all numerical facts that express them. Existing benchmarks evaluate aspects of these capabilities, but provide limited insight into whether both succeed on the same mul…

- **[Do Emergent Misalignment Models Share a Circuit?](https://arxiv.org/abs/2610.20887v1)**
  - *Muhammad Haseeb, Muhammad Tahir*
  - `2026-10-14`
  - Fine-tuning language models on narrowly defined harmful tasks can induce emergent misalignment (EM) across unrelated domains. While prior work has identified shared misalignment-associated representations across independently fine-tuned models, it remains unclear whether these mo…

- **[SafeAdapt-Poker: Counterfactual Risk Calibration for Budgeted Adaptation under Opponent Shift](https://arxiv.org/abs/2610.20473v1)**
  - *Miaobo Hu, Shuhao Hu, Xiaobo Guo et al.*
  - `2026-10-14`
  - Opponent histories can mislead after behavioral shifts. SafeAdapt-Poker formulates budgeted adaptation under opponent shift as a dual-counterfactual sequential-control problem using only information available before each decision. At each decision the controller asks two distinct…

- **[Data-Driven Dynamic Portfolio Selection with Vine Copula Simulation and Reinforcement Learning](https://arxiv.org/abs/2610.20037v1)**
  - *Gabriël M. J. Gelissen, Fengyi Yuan*
  - `2026-10-14`
  - We develop a data-driven approach to dynamic portfolio selection that combines vine-copula simulation with reinforcement learning. The investor has constant relative risk aversion and maximises expected terminal utility with a running penalty on the conditional value-at-risk (CVa…

- **[Common Signals, Spurious Cross-Excitation, and Identification in Multivariate Hawkes Processes](https://arxiv.org/abs/2610.19428v1)**
  - *Jiwon Jung, Kiseop Lee*
  - `2026-10-14`
  - Multivariate Hawkes models are widely used to measure endogenous interactions in event data, but latent common signals can generate apparent excitation even without structural interaction. We characterize the resulting linear projection and construct stable, nonnegative Hawkes pr…

- **[Definition Grounding in Theory-Level Auto-formalization](https://arxiv.org/abs/2610.19223v1)**
  - *Leyan Pan, Christian Szegedy, Frederick Rajasekaran et al.*
  - `2026-10-13`
  - LLM-based auto-formalization systems can now generate formally verified Lean code at unprecedented rates. However, a formalization advances mathematical research only when further mathematical results can be built on it, especially when its definitions and helper lemmas are gener…

- **[REPORT-OPS: Hybrid Evidence-Guided Reporting with Human-Supervised Refinement for HPC](https://arxiv.org/abs/2610.19222v1)**
  - *Mah Kadidia Konate, Mayur Akewar, Janki Bhimani et al.*
  - `2026-10-13`
  - Operational reporting for high-performance computing (HPC) facilities requires combining information from monitoring services, schedulers, incident and maintenance records, storage measurements, periodic reports, and operator investigations. Producing a reliable report requires m…

- **[Verification Turns Capability Gaps into Routing Decisions: Small Language Models for Clinical Documentation](https://arxiv.org/abs/2610.19169v1)**
  - *Nina Fatehi, Meysam Ghaffari, Animesh Agarwal et al.*
  - `2026-10-13`
  - Clinical note generation from doctor--patient dialogue is high-volume and hallucination-intolerant: a fabricated laboratory value can create patient-safety risk, not a quality regression. We ask whether an agentic \emph{verification} architecture, rather than generator scale, can…

- **[AgentCIScope: Grounded Contextual Integrity Evaluation for LLM Agents](https://arxiv.org/abs/2610.19158v1)**
  - *Chengquan Guo, Zhaorun Chen, Zinan Lin et al.*
  - `2026-10-13`
  - LLM agents are becoming increasingly capable of handling daily workspace tasks by interacting with application environments through tool calls. However, as agents read and write sensitive user data across email, documents, and other applications, a central privacy question is whe…

- **[Plan or Retrieve First? A Scale Study of Tool Discovery Architectures](https://arxiv.org/abs/2610.19068v1)**
  - *Mingfei Zhang, Amit Surana, Ziauddin Majid et al.*
  - `2026-10-13`
  - Tool-augmented LLM agents discover relevant APIs from large registries before planning execution, yet finite context windows prohibit injecting all tool definitions into a single prompt. The dominant approach, which we term Retrieve-then-Plan (RtP), embeds the user query and retr…

- **[Hybrid Reasoning Agents](https://arxiv.org/abs/2610.18861v1)**
  - *Jiaru Zou, Yunzhe Qi, Sirui Chen et al.*
  - `2026-10-13`
  - How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning tran…

- **[Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use Co-Evolve](https://arxiv.org/abs/2610.18616v2)**
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

- **[The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement](https://arxiv.org/abs/2610.18845v2)**
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

- **[FinGREAT: Evaluating LLMs on Financial Graph-guided Retrieval And Typing](https://arxiv.org/abs/2610.19240v1)**
  - *Ashman Mehra, Bryan Routledge, Jane JaeYeon Pyo et al.*
  - `2026-10-13`
  - Financial disclosures express the underlying relationships of double-entry accounting through unstructured text. While financial LLM benchmarks predominantly emphasize question answering and classification, schema-guided evidence discovery remains relatively under-explored. We in…

- **[Chasing Label Shifters: A Change-Aware Framework for Dynamic Graph Node Classification](https://arxiv.org/abs/2610.17582v1)**
  - *Junghoon Kim, Seungyoon Choi, Hyunsung Kim et al.*
  - `2026-10-13`
  - Entities in real-world systems often evolve over time: users shift between information consumption patterns, researchers migrate between fields, and firms transition between financial risk states. When such systems are modeled as dynamic graphs, these transitions correspond to no…

- **[Enhanced Detective: A Dual-Stage Proactive Defense Against Internal Poisoning Attacks in Financial Fraud Detection Using Federated Learning](https://arxiv.org/abs/2610.17523v1)**
  - *Maria-Ioana-Andrea Ivan, Orhan Ermis, Ruxandra F. Olimid*
  - `2026-10-13`
  - With recent developments in Artificial Intelligence (AI), the adoption of distributed learning paradigms such as Federated Learning (FL) has emerged. In simple terms, FL enables multiple entities to collaboratively train AI models without sharing local data. The FL paradigm is pa…

- **[Privacy-Preserving GNN Inference on Financial Transaction Graphs via Homomorphic Encryption](https://arxiv.org/abs/2610.18054v2)**
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


---
*Generated 2026-10-16 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
