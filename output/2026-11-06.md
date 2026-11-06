# Daily Paper Digest — 2026-11-06 (Friday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**516 unique papers** (663 topic-entries — cross-topic papers counted once per category)

---

## Agent  (371)

### AAAI

- **[AutoTool: Efficient Tool Selection for Large Language Model Agents](https://arxiv.org/abs/2511.14650)**
  - *Jin Jia, Qin-Bin Li*
  - **AAAI 2025** · `2025-11-18`
  - Large Language Model (LLM) agents have emerged as powerful tools for automating complex tasks by leveraging the reasoning and decision-making abilities of LLMs. However, a major bottleneck in current agent frameworks lies in the high inference cost of tool selection, especially i…

- **[Evaluating Goal Drift in Language Model Agents](https://ojs.aaai.org/index.php/AIES/article/download/36541/38679)**
  - *Rauno Arike, Elizabeth Donoway, Henning Bartsch et al.*
  - **AAAI 2025** · `2025-10-15`
  - As language models (LMs) are increasingly deployed as
autonomous agents, their robust adherence to human-assigned
objectives becomes crucial for safe operation. When these
agents operate independently for extended periods without
human oversight, even initially well-specified goa…

- **[MCP-AgentBench: Evaluating Real-World Language Agent Performance with MCP-Mediated Tools](https://arxiv.org/abs/2509.09734)**
  - *Zikang Guo, Benfeng Xu, Chiwei Zhu et al.*
  - **AAAI 2025** · `2025-09-10`
  - The Model Context Protocol (MCP) is rapidly emerging as a pivotal open standard, designed to enhance agent-tool integration and interoperability, and is positioned to unlock a new era of powerful, interconnected, and genuinely utilitarian agentic AI. However, despite MCP's growin…


### NeurIPS

- **[Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](https://arxiv.org/abs/2611.07730v1)**
  - *Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim et al.*
  - **NeurIPS** · `2026-11-05`
  - Selecting a next motion in a populated scene is not just a matter of avoiding what is currently in the way: an action can be locally feasible yet drift onto the road instead of the crosswalk, cut into a stream of crossing pedestrians, or bottleneck a narrow passage. These failure…

- **[SYMPHONY: Synergistic Multi-agent Planning with Heterogeneous Language Model Assembly](https://arxiv.org/abs/2601.22623)**
  - *Wei Zhu, Zhi-Wen Tang, Kun Yue*
  - **NeurIPS 2026** · `2026-01-30`
  - Recent advancements have increasingly focused on leveraging large language models (LLMs) to construct autonomous agents for complex problem-solving tasks. However, existing approaches predominantly employ a single-agent framework to generate search branches and estimate rewards d…

- **[AgentTTS: Large Language Model Agent for Test-time Compute-optimal Scaling Strategy in Complex Tasks](https://arxiv.org/abs/2508.00890)**
  - *Fali Wang, Hui Liu, Zhen-Wei Dai et al.*
  - **NeurIPS 2025** · `2025-07-26`
  - Test-time scaling (TTS) enhances the performance of large language models (LLMs) by allocating additional compute resources during inference. However, existing research primarily investigates TTS in single-stage tasks; while many real-world problems are multi-stage complex tasks,…

- **[Self-Challenging Language Model Agents](https://arxiv.org/abs/2506.01716)**
  - *Yifei Zhou, Sergey Levine, Jason E. Weston et al.*
  - **NeurIPS 2025** · `2025-06-02`
  - Large language models are quickly becoming the foundation for intelligent agents that are capable of using tools. However, training such agents is challenging because it requires human creation and annotation of a diverse set of tasks, tools, and evaluation criteria. In this pape…

- **[3DLLM-Mem: Long-Term Spatial-Temporal Memory for Embodied 3D Large Language Model](https://arxiv.org/abs/2505.22657)**
  - *Wen-Bo Hu, Yi-Ning Hong, Yanjun Wang et al.*
  - **NeurIPS 2025** · `2025-05-28`
  - Humans excel at performing complex tasks by leveraging long-term memory across temporal and spatial experiences. In contrast, current Large Language Models (LLMs) struggle to effectively plan and act in dynamic, multi-room 3D environments. We posit that part of this limitation is…

- **[Code Graph Model (CGM): A Graph-Integrated Large Language Model for Repository-Level Software Engineering Tasks](https://arxiv.org/abs/2505.16901)**
  - *Hong-Yuan Tao, Ying Zhang, Zhenhao Tang et al.*
  - **NeurIPS 2025** · `2025-05-22`
  - Recent advances in Large Language Models (LLMs) have shown promise in function-level code generation, yet repository-level software engineering tasks remain challenging. Current solutions predominantly rely on proprietary LLM agents, which introduce unpredictability and limit acc…


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

- **[Position: Uncertainty Quantification Needs Reassessment for Large-language Model Agents](https://arxiv.org/abs/2505.22655)**
  - *Michael Kirchhof, Gjergji Kasneci, Enkelejda Kasneci*
  - **ICML 2025** · `2025-05-28`
  - Large-language models (LLMs) and chatbot agents are known to provide wrong outputs at times, and it was recently found that this can never be fully prevented. Hence, uncertainty quantification plays a crucial role, aiming to quantify the level of ambiguity in either one overall n…

- **[UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent](https://arxiv.org/abs/2501.18867)**
  - *Jian-Ke Zhang, Yanjiang Guo, Yu-Cheng Hu et al.*
  - **ICML 2025** · `2025-01-30`
  - Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilit…


### ICLR

- **[Toward Efficient Exploration by Large Language Model Agents](https://arxiv.org/abs/2504.20997)**
  - *Dilip Arumugam, Thomas L. Griffiths*
  - **ICLR 2025** · `2025-04-29`
  - A burgeoning area within reinforcement learning (RL) is the design of sequential decision-making agents centered around large language models (LLMs). While autonomous decision-making agents powered by modern LLMs could facilitate numerous real-world applications, such successes d…


### ACL

- **[Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417v1)**
  - *E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman et al.*
  - **ACL** · `2026-11-05`
  - Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important. Yet even benchmarks that are carefully validated at release can become stale. As models improve, they can discover valid solutions that exis…

- **[RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines](https://arxiv.org/abs/2611.08308v1)**
  - *Roko Parac, Christos Ziakas, Leo Ardon et al.*
  - **ACL** · `2026-11-05`
  - Reward machines (RMs) have been proposed as a reward formulation in reinforcement learning (RL) to capture non-Markovian tasks where credit assignment depends on history. By representing reward functions as automata, RMs expose the task's temporal structure and allow such rewards…

- **[Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs](https://arxiv.org/abs/2611.07483v1)**
  - *Xiaobo Chen, Genliang Zhu, Ziyuan Wang et al.*
  - **ACL** · `2026-11-05`
  - Enterprise AI agents increasingly split a user's request across subagents and merge their results, and each handoff can summarize away, alter or ignore a requirement. We report a preregistered study with synthetic, exactly scorable tasks comparing free-text, structured JSON and s…

- **[RAGAM-AI: A Hybrid Reinforcement Learning based Agentic approach powered by Generative AI for Edge Resource Management](https://arxiv.org/abs/2611.06554v1)**
  - *Shreya K. Chari, John S. Vardakas, Kostas Ramantas et al.*
  - **ACL** · `2026-11-04`
  - Resource management for distributed edge networks hosting different services has been handled efficiently using Reinforcement learning (RL). Reward generalization in complex workflows is still an open issue within the RL realm. Therefore, this work proposes RAGAM-AI, a hybrid fra…

- **[Local Visibility Roadmaps in Continous Multi-agent Path Finding](https://arxiv.org/abs/2611.04944v1)**
  - *Kristýna Janovská, Pavel Surynek*
  - **ACL** · `2026-11-03`
  - We address the problem of smooth continuous multi-agent path finding (SC-MAPF), where agents move in a continuous environment along smooth curves in continuous time. The paths for individual agents are searched in local visibility roadmaps that consider obstacles and other agents…

- **[Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885)**
  - *Yi Yu, Liu-Yi Yao, Yue-Xiang Xie et al.*
  - **ACL 2026** · `2026-01-05`
  - Large language model (LLM) agents face fundamental limitations in long-horizon reasoning due to finite context windows, making effective memory management critical. Existing methods typically handle long-term memory (LTM) and short-term memory (STM) as separate components, relyin…

- **[Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828)**
  - *Si-Kuan Yan, Xiu-Feng Yang, Zuchao Huang et al.*
  - **ACL 2025** · `2025-08-27`
  - Large Language Models (LLMs) have demonstrated impressive capabilities across a wide range of NLP tasks, but they remain fundamentally stateless, constrained by limited context windows that hinder long-horizon reasoning. Recent efforts to address this limitation often augment LLM…

- **[R-VLM: Region-Aware Vision Language Model for Precise GUI Grounding](https://arxiv.org/abs/2507.05673)**
  - *Joonhyung Park, Peng Tang, Sagnika Das et al.*
  - **ACL 2025** · `2025-07-07`
  - Visual agent models for automating human activities on Graphical User Interfaces (GUIs) have emerged as a promising research direction, driven by advances in large Vision Language Models (VLMs). A critical challenge in GUI automation is the precise grounding of interface elements…

- **[Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models](https://arxiv.org/abs/2505.02847)**
  - *Bang Zhang, Ruo-Tian Ma, Qing-Xuan Jiang et al.*
  - **ACL 2025** · `2025-05-01`
  - Assessing how well a large language model (LLM) understands human, rather than merely text, remains an open challenge. To bridge the gap, we introduce Sentient Agent as a Judge (SAGE), an automated evaluation framework that measures an LLM's higher-order social cognition. SAGE in…

- **[FACT-AUDIT: An Adaptive Multi-Agent Framework for Dynamic Fact-Checking Evaluation of Large Language Models](https://arxiv.org/abs/2502.17924)**
  - *Hongzhan Lin, Yang Deng, Yuxuan Gu et al.*
  - **ACL 2025** · `2025-02-25`
  - Large Language Models (LLMs) have significantly advanced the fact-checking studies. However, existing automated fact-checking evaluation methods rely on static datasets and classification metrics, which fail to automatically evaluate the justification production and uncover the n…

- **[Towards a Design Guideline for RPA Evaluation: A Survey of Large Language Model-Based Role-Playing Agents](https://arxiv.org/abs/2502.13012)**
  - *Chao-Ran Chen, Bingsheng Yao, Ruishi Zou et al.*
  - **ACL 2025** · `2025-02-18`
  - Role-Playing Agent (RPA) is an increasingly popular type of LLM Agent that simulates human-like behaviors in a variety of tasks. However, evaluating RPAs is challenging due to diverse task requirements and agent designs. This paper proposes an evidence-based, actionable, and gene…

- **[AgentGym: Evaluating and Training Large Language Model-based Agents across Diverse Environments](https://aclanthology.org/2025.acl-long.1355.pdf)**
  - *Zhi-Heng Xi, Yi-Wen Ding, Wen-Xiang Chen et al.*
  - **ACL 2025**
  - Large language models (LLMs) have emerged as a promising foundation to build generally-capable agents (LLM-based agents) that can handle multi-turn decision-making tasks across various environments. However, the community lacks a unified interactive framework that covers diverse…


### EMNLP

- **[LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://arxiv.org/abs/2506.17335)**
  - *Shuo Yan, Ruochen Li, Ziming Luo et al.*
  - **EMNLP 2025** · `2025-06-19`
  - Large language model (LLM) agents have demonstrated remarkable potential in advancing scientific discovery. However, their capability in the fundamental yet crucial task of reproducing code from research papers, especially in the NLP domain, remains underexplored. This task inclu…

- **[TrojanStego: Your Language Model Can Secretly Be A Steganographic Privacy Leaking Agent](https://arxiv.org/abs/2505.20118)**
  - *Dominik Meier, Jan Philip Wahle, Paul Röttger et al.*
  - **EMNLP 2025** · `2025-05-26`
  - As large language models (LLMs) become integrated into sensitive workflows, concerns grow over their potential to leak confidential information. We propose TrojanStego, a novel threat model in which an adversary fine-tunes an LLM to embed sensitive context information into natura…

- **[Runaway is Ashamed, But Helpful: On the Early-Exit Behavior of Large Language Model-based Agents in Embodied Environments](https://arxiv.org/abs/2505.17616)**
  - *Qingyu Lu, Liang Ding, Siyi Cao et al.*
  - **EMNLP 2025** · `2025-05-23`
  - Agents powered by large language models (LLMs) have demonstrated strong planning and decision-making capabilities in complex embodied environments. However, such agents often suffer from inefficiencies in multi-turn interactions, frequently trapped in repetitive loops or issuing…

- **[DEBATE, TRAIN, EVOLVE: Self Evolution of Language Model Reasoning](https://arxiv.org/abs/2505.15734)**
  - *Gaurav Srivastava, Zhenyu Bi, Meng Lu et al.*
  - **EMNLP 2025** · `2025-05-21`
  - Large language models (LLMs) have improved significantly in their reasoning through extensive training on massive datasets. However, relying solely on additional data for improvement is becoming increasingly impractical, highlighting the need for models to autonomously enhance th…

- **[WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model](https://arxiv.org/abs/2504.21024)**
  - *Tianqing Fang, Hong-Ming Zhang, Zhi-Song Zhang et al.*
  - **EMNLP 2025** · `2025-04-23`
  - Agent self-improvement, where the backbone Large Language Model (LLM) of the agent are trained on trajectories sampled autonomously based on their own policies, has emerged as a promising approach for enhancing performance. Recent advancements, particularly in web environments, f…

- **[VerifiAgent: a Unified Verification Agent in Language Model Reasoning](https://arxiv.org/abs/2504.00406)**
  - *Jiuzhou Han, W. Buntine, Ehsan Shareghi*
  - **EMNLP 2025** · `2025-04-01`
  - Large language models demonstrate remarkable reasoning capabilities but often produce unreliable or incorrect responses. Existing verification methods are typically model-specific or domain-restricted, requiring significant computational resources and lacking scalability across d…

- **[Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://arxiv.org/abs/2503.02519)**
  - *Xingzuo Li, Ke-Hai Chen, Yunfei Long et al.*
  - **EMNLP 2025** · `2025-03-04`
  - Large language model (LLM) agents typically adopt a step-by-step reasoning framework, in which they interleave the processes of thinking and acting to accomplish the given task. However, this paradigm faces a deep-rooted one-pass issue whereby each generated intermediate thought…


### Other / arXiv

- **[Towards Foundation Decision Models: Drex](https://arxiv.org/abs/2611.07854)**
  - *Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev et al.*
  - 🤗 Featured · `2026-11-05`
  - Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy on a wide range of tasks. In production, however, they give inconsistent answers, require parsing of o…

- **[Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training](https://arxiv.org/abs/2611.04277)**
  - *Kangning Zhang, Wenxiang Jiao, Bowen Fang et al.*
  - 🤗 Featured · `2026-11-03`
  - Harness evolution from a common base exhibits Locality, Complementarity, and Nonstationarity: variants repair different failures, and their utility changes as the policy learns. Rather than seeking a universally superior harness, we introduce Harness-S to selectively rescue failu…

- **[VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents](https://arxiv.org/abs/2611.04894)**
  - *ZhengXian Wu, Qianhao Nie, Zhuohong Chen et al.*
  - 🤗 Featured · `2026-11-03`
  - Multimodal agents use web and image tools to answer questions beyond their internal knowledge. Some search tasks use images mainly to identify an initial entity, then rely on text retrieval. These tasks offer limited insight into how agents connect information across images, obje…

- **[From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence](https://arxiv.org/abs/2611.05376)**
  - *Hao Fei*
  - 🤗 Featured · `2026-11-03`
  - For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on a person's behalf. Yet people still forget what they once knew, miss what they a…

- **[EvoMemState: Evolving Memory State for Personal Agents](https://arxiv.org/abs/2611.03743)**
  - *Zhishang Xiang, Yunbo Tang, Zhongqiao Liu et al.*
  - 🤗 Featured · `2026-11-02`

- **[Decoupled Predictive Decision Making: A Shared Conditional Predictor for Agents](https://arxiv.org/abs/2611.02075)**
  - *Lang Mo, Xingxuan Zhang, Qi Wang et al.*
  - 🤗 Featured · `2026-11-01`

- **[Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling](https://arxiv.org/abs/2611.08237)**
  - *Xiaojun Wu, Cehao Yang, Xuhui Jiang et al.*
  - 🤗 · `2026-11-05`
  - Mathematical modeling turns an open-ended real-world problem into assumptions, a model, a solution, and a defended recommendation, and its answers matter only if they are both close to a credible reference and physically feasible; existing benchmarks either score solver fragments…

- **[TCSExam: Evaluating Frontier LLMs on the Full Range of TCS Research](https://arxiv.org/abs/2611.07962)**
  - *Yifan Luo, Zhengying Liu, Yang Yuan et al.*
  - 🤗 · `2026-11-05`
  - Can large language models (LLMs) advance theoretical computer science and resolve its long-standing open conjectures? To study progress toward this goal, we introduce TCSExam, a unified framework and benchmark covering the full range of TCS research. It evaluates theorem proving,…

- **[The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks for Solving Real-World Tasks](https://arxiv.org/abs/2611.07461)**
  - *Haibo Jin, Peng Kuang, Xiaopeng Yuan et al.*
  - 🤗 · `2026-11-05`
  - How can an agent handle a real-world task end to end? Frontier models with their own harnesses still fall short on real-world benchmarks: on Terminal-Bench 4.0, GPT-5.6 Sol with Codex resolves 37.3% of the tasks and Claude Opus 5 with Claude Code 51.8%. These tasks fail at the st…

- **[τ-bench-LILT: Evaluating Conversational Agents on Realistic Multilingual Tool-Use Tasks](https://arxiv.org/abs/2611.07203)**
  - *Kaden Uhlig, Kiarash Mokhtari, Anıl Arslan et al.*
  - 🤗 · `2026-11-04`
  - Frontier evaluations of tool-using conversational agents are conducted almost exclusively in English, leaving a critical gap for organizations deploying agents in other languages and regions. We present $τ$-bench-LILT, a multilingual extension of ${τ^3}$-bench covering German, Ko…

- **[LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856)**
  - *Haoxiang Cao, Yuxuan Zhang, Penghui Du et al.*
  - 🤗 · `2026-11-04`
  - We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence, rejecting distractors, binding e…

- **[Agent-Driven Generative Priors for Pathology Image Synthesis and Segmentation](https://arxiv.org/abs/2611.06701)**
  - *Sicheng Yang, Rui Tang, Haipeng Zhou et al.*
  - 🤗 · `2026-11-04`

- **[What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?](https://arxiv.org/abs/2611.06483)**
  - *Kejian Zhu, Zhuoran Jin, Shangqing Tu et al.*
  - 🤗 · `2026-11-04`
  - While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth $K$ and interaction depth $T$ via $Pass@(K,T)$, we show that trajectory-level RL advanta…

- **[Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription](https://arxiv.org/abs/2611.06043)**
  - *Daniel Huang, Qi He, Shaoxiong Duan et al.*
  - 🤗 · `2026-11-04`
  - Streaming speech recognition is increasingly consumed by machines, such as translators and voice agents, that act on each token as it appears. A token that is later revised costs wasted work or a wrong action. In this work, we present Confucius4-R2T2 (short for Real Real-Time Tra…

- **[WayPOP: A Panoramic Open-Set Panoptic Tracking Benchmark](https://arxiv.org/abs/2611.05801)**
  - *Rohit Mohan, Maximilian Luz, Swarnava Chowdhury et al.*
  - 🤗 · `2026-11-04`
  - Holistic perception for autonomous agents requires reliably segmenting and associating scene elements across time and camera views, including objects outside a fixed semantic taxonomy. Existing open-set panoptic benchmarks focus on individual images or views, while panoramic trac…

- **[How Do AI Agents Waste Your Money?](https://arxiv.org/abs/2611.07238)**
  - *Huimin Zeng, Yuxuan Lu, Jesse Cai et al.*
  - 🤗 · `2026-11-04`
  - AI agents may consume massive tokens across a wide range of tasks, but how many of those tokens are really necessary? Although prior work has shown that agents can incur unexpectedly high token costs, we still lack a systematic way to identify and measure token waste. In this wor…

- **[SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization](https://arxiv.org/abs/2611.08483v1)**
  - *Qile Jiang, George Em Karniadakis*
  - `2026-11-05`
  - LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for eac…

- **[XStack: A Benchmark for ML Repo Migration](https://arxiv.org/abs/2611.08472v1)**
  - *Linrong Cai, Taiming Lu, Haozhe Chen et al.*
  - `2026-11-05`
  - ML code should run where researchers choose, not where it was first written. Today, machine learning code mainly lives in two ecosystems, PyTorch on NVIDIA GPUs and JAX on Google TPUs. Migrating repositories between them means building and testing across frameworks and hardware.…

- **[ReproBridge: Building Reproducibility into ML Research Artifacts](https://arxiv.org/abs/2611.08452v1)**
  - *Yubo Wang, Rui Meng, Jaehyun Nam et al.*
  - `2026-11-05`
  - Reproducing machine learning experiments requires reconstructing procedures from information scattered across papers, released code, and supporting artifacts. For coding agents, reproduction success can therefore depend on their ability to fill in missing details, rather than on…

- **[The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI](https://arxiv.org/abs/2611.08428v1)**
  - *Julian Kunkel, Ali Doosthosseini*
  - `2026-11-05`
  - Chat remains the default surface for many large language model (LLM) tasks, even as agentic tools such as OpenCode excel at coding and automation. Yet the model sees the current dialogue but not the workspace around it. We explore meta access---giving the assistant a structured,…

- **[Enhancing Local and Global Structure in Compressed AI Agent Memory](https://arxiv.org/abs/2611.08341v1)**
  - *Henry Han*
  - `2026-11-05`
  - AI agents store text as embedding vectors and compress them at scale. A compression is accepted when each item's nearest neighbors survive, but agents also consolidate, delete, and compare memories, tasks that depend on which items lie far apart. We evaluate both ends with two la…

- **[Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement](https://arxiv.org/abs/2611.08318v1)**
  - *Wenbo Huang, Jianxin Bi, Shunyu Yang et al.*
  - `2026-11-05`
  - Self-improving embodied agents are increasingly being developed and compared on robot simulation benchmarks. Several recent works expose the benchmark's success criteria to the learning agent, a practice we call Criteria Exposure (CE). These criteria, originally written to verify…

- **[SMART: State-based Multi Agent Reasoning Traces for Verification-oriented Problem-Solving](https://arxiv.org/abs/2611.08196v1)**
  - *Sai Vallurupalli, Francis Ferraro*
  - `2026-11-05`
  - Complex problems with limited context, such as claims, require a means to obtain additional knowledge necessary for solution reasoning. We propose a multi-agent framework, SMART, to obtain knowledge through capturing the implicit state of participating entities in a problem conte…

- **[PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?](https://arxiv.org/abs/2611.08175v1)**
  - *Yue Zhang, Jilei Sun, Liqiang Jing et al.*
  - `2026-11-05`
  - Automating printed circuit board (PCB) routing requires coordinating board-level connectivity decisions with geometric execution under strict design rules. Although recent agents can interact with native routing tools, reliable routing on complex boards remains challenging. We pr…

- **[Create Your Own Work Stack: Deploying Self-hosted AI and Tooling in a Tech Startup](https://arxiv.org/abs/2611.08116v1)**
  - *Saad Ahmed Bazaz, Talha Amjad, Abdurrehman Subhani et al.*
  - `2026-11-05`
  - Self-hosting AI is often presented as a way to reduce inference costs and increase control, but deployment introduces its own costs. We report our experience deploying a hybrid AI stack at Grayhat Developers, a small software company with an AI-intensive development workflow. Our…

- **[When Imperfect Automated Fact-Checking Backfires: Social Learning in the Presence of Misinformation](https://arxiv.org/abs/2611.08053v1)**
  - *Zixuan Liu, Ming Cao*
  - `2026-11-05`
  - Automated fact-checking tools, cheap and fast but imperfect, are increasingly available on social platforms. We study when such tools can backfire in a sequential social learning model of misinformation. Agents observe an article's reliability and their predecessors' actions, whi…

- **[ChemE-as-Code: An Open-Source Platform for Agentic AI in Chemical Engineering](https://arxiv.org/abs/2611.07947v1)**
  - *Artur M. Schweidtmann*
  - `2026-11-05`
  - ChemE-as-Code provides an open-source environment in which AI agents built on large language models (LLMs) can carry out chemical engineering work and engineers can check it. Its calculation tools range from catalysis through process simulation to plant layout, HAZOP and life cyc…

- **[tok: a textual concrete syntax of BPMN and DMN for humans and AI agents](https://arxiv.org/abs/2611.07945v1)**
  - *Marek Deja*
  - `2026-11-05`
  - tok is a plain-text notation for Business Process Model and Notation (BPMN) 2.0.2 process models and Decision Model and Notation (DMN) 1.5 decisions. One engine checks a tok document against both standards, compiles the document to XML with an automatic diagram, and serves langua…

- **[AttnSR: Attention Step Reward for Long-Horizon Agentic RL](https://arxiv.org/abs/2611.07932v1)**
  - *Mengsong Wu, Tianchen Zhou, Zhaochen Su et al.*
  - `2026-11-05`
  - Long-horizon LLM agents make multi-step decisions, yet outcome-reward-only reinforcement learning provides little direct supervision for individual steps. We introduce AttnSR, a step-level reward augmentation method that derives reward allocations from policy attention extracted…

- **[Persistent Retrieval for Conversational Agents: A Study of Retrieval Efficiency](https://arxiv.org/abs/2611.07899v1)**
  - *Karthik Ravula, Sathwik Kowtha, Rishabh Verma et al.*
  - `2026-11-05`
  - Conversational agents can retrieve information directly or delegate retrieval to a subagent. This design choice affects how retrieval history is maintained, what context each model call receives, and what information must be re-retrieved in follow-up questions. We compare three d…

- **[CORE: Coarse-to-Fine Search with Context Management for Deep Research](https://arxiv.org/abs/2611.07859v1)**
  - *Hoang Tran Vuong, Ngoc Quan Pham, Hung Bui et al.*
  - `2026-11-05`
  - Deep research agents answer complex questions through repeated search. They rely on a harness that runs their tool calls and returns evidence to their context. This creates a trade-off: Search works best over long passages, which give enough context for reliable semantic matching…

- **[Instantiating the Knowledge Plane](https://arxiv.org/abs/2611.07827v1)**
  - *Francisco Pereira, Justine Sherry, Pratiksha Thaker*
  - `2026-11-05`
  - In 2003, Clark et al. proposed the "Knowledge Plane", a layer of intelligent agents that share rich information about network state in order to collaboratively manage the Internet across administrative boundaries. The technology of the day lacked the two capabilities it demanded…

- **[Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents](https://arxiv.org/abs/2611.07825v1)**
  - *Jisen Lei, Huizhi Liang*
  - `2026-11-05`
  - Goal interpretation is to translate a natural language instruction into a formal symbolic goal that a planner can execute. It is critical for embodied agents because any error here propagates to every downstream planning and action step. Doing it well requires both generating sui…

- **[RIVER: Evidence-guided multi-agent retrieval for enzyme--reaction discovery](https://arxiv.org/abs/2611.07757v1)**
  - *Yifan Chang, Yunze Li, Feifei Jiang et al.*
  - `2026-11-05`
  - Enzyme function annotation and the identification of candidate enzymes for a given reaction are essential steps in connecting genomic information to biochemical reaction networks. However, existing methods rely on sequence or structural similarity or on training with known enzyme…

- **[Evaluating Token Probabilities as Confidence Estimators in Human Behavior Simulations: A Case Study in Luxembourgish Next Like Prediction](https://arxiv.org/abs/2611.07735v1)**
  - *Nils Schwager, Simon Münker, Alistair Plum et al.*
  - `2026-11-05`
  - As large language models (LLMs) are increasingly used to simulate human behavior, their operational validity is typically assessed through accuracy alone, implicitly treating human behavior as deterministic. We argue that on noisy digital trace data, a model's performance depends…

- **[MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents](https://arxiv.org/abs/2611.07689v1)**
  - *Yizhen Jiang, Haowei Guo, Tianyi Bai et al.*
  - `2026-11-05`
  - Large language model agents are increasingly deployed through the Model Context Protocol (MCP), which allows them to discover and invoke tools across multiple servers at runtime. Existing MCP benchmarks primarily measure task completion; where they diagnose failures, they do so a…

- **[ReferClaw: Disambiguating User Intent for Egocentric Assistance](https://arxiv.org/abs/2611.07683v1)**
  - *Hangyu Qin, Junbin Xiao, Angela Yao*
  - `2026-11-05`
  - Users of egocentric AI assistants often ask short, ambiguous questions whose intended referents cannot be uniquely resolved from video and dialogue history. For example, "Where did I leave it?" may refer to several previously handled objects. Existing VideoQA systems typically co…

- **[Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies](https://arxiv.org/abs/2611.07667v1)**
  - *Mete Erdogan, Mirac Suzgun, Aneesh Pappu et al.*
  - `2026-11-05`
  - The performance of multi-agent LLM systems depends not only on the capabilities of the underlying models but also on information-sharing policies, which govern what information each agent observes and at what level of detail. But does providing AI agents with more detailed inform…

- **[PharmAgents2: Towards Autonomous End-to-End Drug Discovery](https://arxiv.org/abs/2611.07653v1)**
  - *Haichuan Tan, Bowen Gao, Tao Huang et al.*
  - `2026-11-05`
  - Drug discovery requires continuous scientific decision-making across a vast research space. We introduce PharmAgents2, an autonomous system for end-to-end drug discovery that combines knowledge-enhanced decision-making with organized large-scale exploration. Paper2Skill extracts…

- **[Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems](https://arxiv.org/abs/2611.07652v1)**
  - *Vladimiros Peilivanidis*
  - `2026-11-05`
  - Current autonomous logical systems rely on a fragile assumption: that language models should dynamically write code, guess API payloads, and memorize operational constraints through prompt engineering. In practice, this burns massive context windows, inflates API bills, and produ…

- **[Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks](https://arxiv.org/abs/2611.07640v1)**
  - *Rongting Zhang, Martin Bertran, Sandeep Avula et al.*
  - `2026-11-05`
  - Indirect prompt-injection (IPI) benchmarks predominantly test planted instructions that redirect a tool-using agent toward an attacker-chosen task. Yet attacker-controlled content can instead tamper with the outcome of the task already in progress. A buyer's dispute evidence can…

- **[Beneath the Surface: What We Overlook When We Talk About Agent Evolution](https://arxiv.org/abs/2611.07624v1)**
  - *Xiaobo Wang, Zimu Wang, Siyu Ye et al.*
  - `2026-11-05`
  - Agent harness evolution enables recursive self-improvement (RSI) without updating model weights. We examine whether higher benchmark scores yield reliable, efficient, and transferable improvement. We evaluate four methods across harnesses, general and coding tasks. Repeated evalu…

- **[Evolver: Turning Agent Exploration into Evolving Capabilities](https://arxiv.org/abs/2611.07595v1)**
  - *Haoyang Zhang, Qumeng Sun, Xiao Zhang et al.*
  - `2026-11-05`
  - Agent exploration produces valuable procedural knowledge, yet much of this experience remains confined to transient execution traces and is not systematically reused. We introduce Evolver, an experience-driven framework that transforms agent exploration into persistent, reusable…

- **[Learning and Steering in Incomplete-Information Games](https://arxiv.org/abs/2611.07589v1)**
  - *Asrın Efe Yorulmaz, Tamer Başar*
  - `2026-11-05`
  - In many modern multi-agent systems, a mediator seeks to influence strategic decision dynamics using only outcome-level feedback and without knowing agents' utilities. In this work, we study how a mediator can learn an unknown game and steer adaptive agents toward outcomes that ma…

- **[Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment](https://arxiv.org/abs/2611.07586v1)**
  - *Yao Huang, Yifan Wang, Yitong Sun et al.*
  - `2026-11-05`
  - As LLM agents advance rapidly in autonomy, the risk of hidden objectives that bypass safety constraints becomes increasingly plausible. Chain-of-thought (CoT) monitoring offers a key control mechanism by reading the agent's reasoning and flagging misalignment before it materializ…

- **[SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking](https://arxiv.org/abs/2611.07558v1)**
  - *Moonseok Choi, Jongwon Jeong, Minki Kang et al.*
  - `2026-11-05`
  - Large Language Model (LLM) agents are increasingly deployed under structured generation, where grammar constraints enforce output format at inference time. Whereas existing compression methods target unconstrained generation, we first identify a fundamental mismatch: under struct…

- **[The Memory Trap: Language Agents Overgeneralize from Benign Interactions](https://arxiv.org/abs/2611.07554v1)**
  - *Kaiqu Liang, Jaime Fernández Fisac, Thomas L. Griffiths et al.*
  - `2026-11-05`
  - Language agents increasingly use persistent memory to record user preferences and procedures across sessions. We show that memory from benign interactions can cause unsafe or unreliable behavior on later tasks. We call this failure the memory trap. To study this issue, we compare…

- **[Goal-Branching LaCAM: Temporary Goals as Search Branches in Dense Multi-Agent Pathfinding](https://arxiv.org/abs/2611.07528v1)**
  - *Stephen Chang, Daniel Harabor*
  - `2026-11-05`
  - LaCAM is a search-based solver for multi-agent pathfinding (MAPF) that runs a depth-first search over joint configurations, using PIBT to generate successors and lazily adding single-agent constraints to explore alternatives. Although LaCAM is complete, it can struggle on dense,…

- **[DelegateEval: Evaluating Platforms for Personal External Service Agents](https://arxiv.org/abs/2611.07508v1)**
  - *Jichao Li, Jinrong Lu, Manjiang Yu et al.*
  - `2026-11-05`
  - AI agents that work for an individual over time may also help that individual serve external clients. We define a personal external service agent as an agent authorized and continuously managed by a specific individual to accept client requests, deliver work, and provide ongoing…

- **[FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance](https://arxiv.org/abs/2611.07464v1)**
  - *Yupeng Cao, Xueqing Peng, Lingfei Qian et al.*
  - `2026-11-05`
  - Language agents increasingly work for users on the open Web, and finance is where trusting them is hardest. The data must come from the Web, the strategy lives in the user's head, and correctness depends on time, so an agent can fail silently: a strategy the user never asked for,…

- **[PSGAgent: Enhancing MLLMs' Dynamic Visual Perception for Panoptic Scene Graph Generation via Agentic Reasoning](https://arxiv.org/abs/2611.07408v1)**
  - *Qingyun Liu, Yuankun Liu, Jiaye Feng et al.*
  - `2026-11-05`
  - Panoptic Scene Graph generation (PSG) requires holistic yet fine-grained reasoning over complex relations among objects. However, current Multimodal Large Language Models (MLLMs) applied to PSG suffer from a perception bottleneck: they function as static observers limited by fixe…

- **[EnvOpt: Automated Optimization for Agent Environments](https://arxiv.org/abs/2611.07372v1)**
  - *Mingxuan Li, Huanzhi Mao, Qiuyang Mang et al.*
  - `2026-11-05`
  - An LLM agent's cost and success depend on its model, its harness, and its environment. In addition to the widely studied directions of parameter tuning and harness optimization, we propose the third direction: optimization over stationary environments. Agents are often deployed i…

- **[Selective Retrieval Routing for Multi-Violation Knowledge Graph Repair](https://arxiv.org/abs/2611.07342v1)**
  - *Tung-Wei Lin, Gabe Fierro, Han Li et al.*
  - `2026-11-05`
  - Knowledge graphs often contain missing or inconsistent facts that undermine the applications built on them. Schema validation detects such violations but does not identify which of several valid repairs recovers the intended graph. External corpora can supply the evidence needed…

- **[Permanent and Transient Representations for Continual Reinforcement Learning](https://arxiv.org/abs/2611.07327v1)**
  - *Nishanth Anand, Doina Precup*
  - `2026-11-05`
  - Continual Reinforcement Learning (CRL) agents struggle to adapt to new situations while retaining prior knowledge, leading to a stability-plasticity trade-off. One approach to solving this problem is by using complementary learning systems: one for slow, long-term learning and an…

- **[How Should Agents See Code? Rethinking Code Representations for Agentic Software Engineering](https://arxiv.org/abs/2611.07286v1)**
  - *Melika Sepidband, Jiho Shin, Song Wang et al.*
  - `2026-11-05`
  - LLM agents are increasingly used for repository-level software engineering tasks. However, most agents still access repositories through raw files, lexical search, and shell commands, treating code primarily as text. This paper investigates map-based code-representation workflows…

- **[Social Humanoid: Socially Responsive Human-Humanoid Interaction](https://arxiv.org/abs/2611.08407v1)**
  - *Vongani H. Maluleke, James Ni, Kie Horiuchi et al.*
  - `2026-11-05`
  - Humanoid robots are typically trained as solitary agents, leaving them unable to coordinate physically with human partners who naturally anticipate and adjust to one another. To bridge this gap, we present Social Humanoid, a hierarchical system that generates and executes sociall…

- **[Discovering Learning Rules that Shape Others](https://arxiv.org/abs/2611.08335v1)**
  - *Hong Jun Lee, Ziyan Wang, Jun Wang et al.*
  - `2026-11-05`
  - In general-sum games, self-interested learners can reach outcomes that are poor for everyone, which has motivated methods that shape the opponent's learning. Methods like Learning with Opponent-Learning Awareness (LOLA), which differentiates through the opponent's learning proces…

- **[Interpretable many-body interaction laws for collective motion from few trajectories](https://arxiv.org/abs/2611.08314v1)**
  - *Timon S. Gutleb*
  - `2026-11-05`
  - Models of collective motion usually reduce social interactions to pairwise forces, despite empirical evidence for many-body effects. We introduce the directional atomic cluster expansion (dACE), which adapts the atomic cluster expansion (ACE) of interatomic potentials to self-pro…

- **[Regret Bounds for Profit Maximization in Bilateral Trade: Learning the Best Posted-Price Mechanism](https://arxiv.org/abs/2611.08173v1)**
  - *Johannes Brüstle, Simone Di Gregorio, Federico Fusco et al.*
  - `2026-11-05`
  - Bilateral trade models the task of intermediating between two strategic agents, a seller and a buyer, willing to trade a good for which they hold private valuations. We study this problem from the perspective of a profit-maximizing broker in a regret minimization framework. At ea…

- **[Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning](https://arxiv.org/abs/2611.08144v1)**
  - *Zuo Gou, Chenhao Lu*
  - `2026-11-05`
  - Robot reinforcement learning increasingly runs environments outside the trainer: in another process, on another machine, in another language. Many faults at this boundary raise no error. We make the boundary a wire protocol and ask what notices a fault in it.   On Pendulum, HalfC…

- **[PersonaAgent: Retrieval-Augmented Transaction Anomaly Scoring with Refreshable Multi-Entity Persona Memory](https://arxiv.org/abs/2611.08094v1)**
  - *Zhengyu Fang, Liang Wang, Yingtong Dou et al.*
  - `2026-11-05`
  - In large-scale payment networks, entities (card, merchant, etc.) and their interactions play a key role in transaction anomaly detection. However, transaction patterns between different entities usually change more frequently than the production model refresh schedule. Meanwhile,…

- **[Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recognizer with Gabor-Dictionary Convolutions and Delta-Rule Memory](https://arxiv.org/abs/2611.08092v1)**
  - *Nir Krakowski, Tamir Cohen, Ohad Zohar et al.*
  - `2026-11-05`
  - Real-time voice agents need a speech recognizer that never waits for future audio and whose memory per call does not grow with the length of the call. We present E-Gaborformer, a strictly causal encoder that combines Gated DeltaNet-2 recurrent layers with sliding-window attention…

- **[QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents](https://arxiv.org/abs/2611.07976v1)**
  - *Yingjie Tan, Haiquan Qiu, Quanming Yao et al.*
  - `2026-11-05`
  - DeepSearch LLM agents repeatedly search and carry retrieved sources into subsequent reasoning steps. This expanding context increases token consumption and latency, although many results do not contribute to later reasoning. We propose Query-Relevant Attention Entropy (QRAE), an…

- **[The Blindfolded Controller: Decision Model-Guided Training for Reinforcement Learning](https://arxiv.org/abs/2611.07934v1)**
  - *Muhammad Ibrahim Khan, Aniket Dixit, Faizan Ahmed et al.*
  - `2026-11-05`
  - Reinforcement learning (RL) provides a framework for continuous improvement through interaction with an environment. However, RL agents struggle against tasks that offer exploration challenges and sparse rewards, because learning efficient policies from scratch is slow and sample…

- **[Foresee to Trade: Forecast-Augmented Policy Optimization for Portfolio Management](https://arxiv.org/abs/2611.07750v1)**
  - *Zeyu Liu, Xuanzhi Feng, Haoran Xu et al.*
  - `2026-11-05`
  - Online investment services must translate asset opportunities into investment outcomes for users' accounts, yet the same market opportunity can warrant different account actions. We study how supervision from future asset opportunities can strengthen account-level trading decisio…

- **[Binding Paraphrased Instructions to Encountered Objects in sLLM Agents under Partial Observability](https://arxiv.org/abs/2611.07599v1)**
  - *Chanyoung Kim, Harim Song, Byoungchan Ko et al.*
  - `2026-11-05`
  - Reliable deployment of LLM agents requires grounding diverse user expressions in their environments. Although RL-finetuned smaller large language model (sLLM) agents rival larger prompted LLMs on embodied tasks, their robustness to instruction paraphrases remains unclear. We intr…

- **[Learning Multi-Agent Orchestration:Higher-Order Interactions in Policy Improvement](https://arxiv.org/abs/2611.07495v1)**
  - *Kaixuan Liu, Guojun Xiong*
  - `2026-11-05`
  - Learned orchestration has emerged as a promising paradigm for large language model (LLM)-based multi-agent systems, in which a central orchestrator selects agents and controls the information they receive throughout a task. Despite rapid empirical progress, existing methods train…

- **[CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document Enrichment](https://arxiv.org/abs/2611.07393v1)**
  - *Vihan Lakshman, Peter Baile Chen, Zhuohan Gu et al.*
  - `2026-11-05`
  - Recent work in machine learning has demonstrated that transformer-based language model agents can communicate state not only through text, but also directly in latent space via key-value (KV) caches. In this paper, we argue that such cache-to-cache translation can provide utility…

- **[Adversarial Multiplicity: Cherry-Picked Models and the Limits of Disclosure](https://arxiv.org/abs/2611.07378v1)**
  - *Cassandra C. Chou, Benjamin Q. Huynh, Allison Koenecke et al.*
  - `2026-11-05`
  - Predictive multiplicity -- where similarly accurate models disagree on individual predictions -- can be leveraged to optimize secondary metrics (e.g., fairness) without loss in predictive performance. However, exploiting multiplicity opens the opportunity for motivated parties (o…

- **[Using Transformers for Teaching and Learning via Symbolic Distillation of Neural A-life Agents](https://arxiv.org/abs/2611.07254v1)**
  - *Shuwei Wang, Vadim Bulitko, Matthew R. G. Brown et al.*
  - `2026-11-05`
  - Neural networks controlling behavior of A-life agents can evolve over multiple generations. While effective in making the agents survive, such networks are generally opaque to a human observer. Furthermore, the neural weights cannot be transferred between agents with different ne…

- **[Cultural Adaptation within Repeated Social Interactions](https://arxiv.org/abs/2611.08334v1)**
  - *Chen Cecilia Liu, Roi Reichart, Anna Korhonen*
  - `2026-11-05`
  - Much of human culture is tacit and is typically learned through situated social interaction. As LLMs are deployed as interactive agents across diverse communities, assessing their cultural competence demands moving beyond existing question-answering approaches, shifting from what…

- **[Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks](https://arxiv.org/abs/2611.08281v1)**
  - *Zhitao He, Chi Him Zhang, Chengru Han et al.*
  - `2026-11-05`
  - Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchma…

- **[From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional Hallucinations?](https://arxiv.org/abs/2611.08231v1)**
  - *Hanyu Qiu, Ze Liu, Zhe Zhao et al.*
  - `2026-11-05`
  - Large language models (LLMs) are widely used for information access, content production, and agent-based task execution, but their outputs remain vulnerable to subtle, high-risk hallucinations. To systematically evaluate and advance post-generation hallucination detection, we int…

- **[Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis](https://arxiv.org/abs/2611.08219v1)**
  - *Teng Pan, Zixuan Wang, Yuchen Yan et al.*
  - `2026-11-05`
  - Large language models have made rapid progress in agentic reasoning and tool use, raising expectations for agents that can take over realistic productivity work from humans. However, current agents still struggle to finish such tasks, where success requires following long-horizon…

- **[MEvince: Knowledge-Constrained LLM Reasoning for Technique Identification from Malware Reports](https://arxiv.org/abs/2611.07486v1)**
  - *Hongyu She, Yiling He, Mengda Xie et al.*
  - `2026-11-05`
  - Mapping behavioral intelligence in malware analysis reports to ATT&CK techniques supports threat analysis and defense, but reliable identification remains challenging. Supporting evidence is often scattered across long, heterogeneous reports, while closely related techniques shar…

- **[SCALE: Real-Time Latent Communication for Cyber-Physical Agents](https://arxiv.org/abs/2611.08390v1)**
  - *Shanghao Shi, Jian Xiao, Ching-Hsiang Chan et al.*
  - `2026-11-05`
  - Latent communication enables agents to collaborate efficiently by directly exchanging intermediate model representations rather than raw sensor data or text messages. Existing approaches, however, are primarily designed for LLM agents and do not consider the bandwidth constraints…

- **[Trilemma: How Agents choose between Honesty, Confidentiality, and Task Completion](https://arxiv.org/abs/2611.08312v1)**
  - *Johannes Taraz, Abhinav Kumar, Sahar Abdelnabi*
  - `2026-11-05`
  - Personal AI agents often act on underspecified instructions and draw on context such as their user's messages and calendar to decide how to proceed. This context can contain private preferences that interfere with the task, with other people's interests, or with confidentiality n…

- **[SEER: A Scalable Event-Driven Runtime for Parallel Execution of Multi-Agent Reinforcement Learning Environments](https://arxiv.org/abs/2611.07996v1)**
  - *Jiming Su, Feng Zhu, Yuhao Xiao et al.*
  - `2026-11-05`
  - Multi-agent reinforcement learning (MARL) is increasingly used in systems where many entities interact in a shared environment. In these workloads, policy inference can be batched on GPUs, but the CPU-side environment path still updates entity states, resolves local interactions,…

- **[A Bilevel Neurodynamic Approach for Distributed SCAD-Regularized Sparse Least Squares](https://arxiv.org/abs/2611.07618v1)**
  - *Juntao Li, Qihang Guo, Deyuan Meng*
  - `2026-11-05`
  - This paper proposes a bilevel particle swarm optimization (PSO)-neurodynamic method for solving the distributed sparse least-squares problem regularized by the smoothly clipped absolute deviation (SCAD) penalty to global optimality. The SCAD penalty is nonsmooth and nonconvex, so…

- **[Designing with Cinematic Language: An Intent-Driven Approach to Human-AI Video Clip Co-Creation](https://arxiv.org/abs/2611.07377v1)**
  - *Yi He, Zhengxi Yu, Feilin Han et al.*
  - `2026-11-05`
  - Generative video models have made video creation more accessible, yet creators still struggle to translate high-level narrative intentions into coherent cinematic expressions. Existing systems primarily rely on prompt refinement or expose isolated camera controls, leaving a gap b…

- **[Take It From Here: Evaluating Coding Agents On Project Takeover](https://arxiv.org/abs/2611.07307v1)**
  - *Dingxian Wang, Zhe Fu, Jiaqi Deng et al.*
  - `2026-11-05`
  - Coding agents increasingly collaborate on long-term projects. When taking over a project, they need to recover currently applicable requirements from the interaction history and update them in response to new requests. However, most coding benchmarks do not include long interacti…

- **[Goal Revelation as a Bridge Between Information-Theoretic Empowerment and Capability-Based Human Power](https://arxiv.org/abs/2611.07247v1)**
  - *Jaime Ruiz-Serra, Tomáš Gavenčiak, Jobst Heitzig*
  - `2026-11-04`
  - Power matters for AI safety. Optimal agents tend to acquire power across a wide range of objectives (instrumental convergence). As we embed AI agents into socio-technical systems, humans risk gradual disempowerment. Both concerns call for a formal, quantitative measure of power.…

- **[MAC-v2: Long-horizon model-based value expansion from pixels](https://arxiv.org/abs/2611.07245v1)**
  - *Kwanyoung Park, Sergey Levine*
  - `2026-11-04`
  - We study whether \emph{long-horizon model-based value expansion} can serve as an effective framework in pixel-based offline reinforcement learning (RL). Long-horizon model-based value expansion from pixels is substantially harder than state-based environments, as the agent must l…

- **[SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection](https://arxiv.org/abs/2611.07222v1)**
  - *Woosang Lim, Yeseul Chang, Jaewoo Lee*
  - `2026-11-04`
  - Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so the decision depends on…

- **[SeVerus: Context-Aware, Gamified Benchmarking for Rust Verification](https://arxiv.org/abs/2611.07194v1)**
  - *Álvaro F. Silva, Martim Afonso, Nuno Saavedra et al.*
  - `2026-11-04`
  - Coding agents achieve high success rates on existing benchmarks for Verus, a verifier for Rust programs. These benchmarks typically provide the auxiliary lemmas needed to complete a proof. In practice, however, such lemmas must be discovered and proved. To capture this challenge,…

- **[Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?](https://arxiv.org/abs/2611.07166v1)**
  - *Xiangkai Zeng, Zheng Liu, Zihao Lin*
  - `2026-11-04`
  - Developers rarely give a coding agent a single request: they ask it to build a component and then to extend, upgrade, and optimize it, each time on code the agent itself wrote. Most benchmarks, however, score one task at a time. We introduce Multi-step SWE, a long-horizon benchma…

- **[Depth or Description? When a One-Step Latent Score Replaces Lookahead in Proactive Information Acquisition](https://arxiv.org/abs/2611.07155v1)**
  - *Biswa Sengupta*
  - `2026-11-04`
  - A proactive agent must decide what to ask before it acts. Exact lookahead values combinations of questions but is expensive and leans on a fitted model; a one-step score is cheap but can miss them. Our main finding: the need for depth often lies in how the hidden cause is describ…

- **[More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty](https://arxiv.org/abs/2611.07140v1)**
  - *Burkay Tunçtürk, Koorosh Aslansefat, Yiannis Papadopoulos et al.*
  - `2026-11-04`
  - Teams increasingly build software from cooperating large language model (LLM) agents, often assuming more agents mean more reliability. Yet the usual evidence, average benchmark accuracy, ignores the input mix a deployed system meets and the rule merging the agents' answers. Buil…

- **[Polynomial-Time Computation of Extensive-Form Proper Equilibria in Two-Player Zero-Sum Games](https://arxiv.org/abs/2611.07089v1)**
  - *Sam Ganzfried*
  - `2026-11-04`
  - We give a deterministic polynomial-time algorithm for computing an exact extensive-form proper equilibrium in a finite two-player zero-sum extensive-form game with perfect recall and rational data. Properness is understood in the agent normal form: an action at an information set…

- **[When Verification Is Not Agreement: Cross-Agent LLM-to-Dafny Formalization](https://arxiv.org/abs/2611.07073v1)**
  - *Priyanath Maji*
  - `2026-11-04`
  - A verified Dafny postcondition certifies that a formula holds, but it does not guarantee that the result was reached through genuine independent reasoning. We introduce a cross-agent formalization protocol where a Specifier model translates clinical trial criteria into a Dafny pr…

- **[Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration](https://arxiv.org/abs/2611.07066v1)**
  - *Sungil Son, Hoseong Jung, Dahyun Oh et al.*
  - `2026-11-04`
  - Discovering cooperative behavior in multi-agent reinforcement learning (MARL) is challenging due to the combinatorial complexity of joint state-action spaces, which hinders the emergence of coordinated behaviors from trial-and-error alone. Intrinsic rewards are often used to aid…

- **[Reclassification Is All You Missed: Surfacing Variant Reinterpretation Need in Online Health Communities at Population Scale](https://arxiv.org/abs/2611.07054v1)**
  - *Kamalakkannan Ravi, Mengshu Nie, Annapurna Poduri et al.*
  - `2026-11-04`
  - Genetic variants are routinely reclassified in ClinVar after a patient is tested, sometimes from uncertain to pathogenic, yet patient recontact is inconsistent, with no clear duty and responsibility diffused among labs, providers, and patients. Many affected people discuss their…

- **[Closed-Loop Agent Evaluation: Layered Measurement and Self-Calibration](https://arxiv.org/abs/2611.07051v1)**
  - *Ruifeng Ren, Gun Ahn*
  - `2026-11-04`
  - Once an agent is live, teams want to know whether it is doing its job, not just whether it throws errors. Yet most evaluation is one-off: a benchmark run, a look at traces, a single score. Its conclusions neither check themselves nor reach the agent. We propose closed-loop evalua…

- **[Adapting the Process of Adaptation: Darwinian, Lamarckian, and Agent-Directed Evolution in AI](https://arxiv.org/abs/2611.07048v1)**
  - *Andrew W. Lo, Chaoyi Zhao*
  - `2026-11-04`
  - Evolution has shaped intelligence for billions of years. Artificial intelligence (AI) now raises a striking possibility: intelligence may begin to direct its own evolution. As AI agents become capable of modifying and evaluating their own behavior, how quickly could they improve,…

- **[FrontierPhysics: Evaluating Agents for End-to-End Physics Research](https://arxiv.org/abs/2611.06910v1)**
  - *Bingran You, Wenjun Ke, Ria Rosenauer et al.*
  - `2026-11-04`
  - AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce Fron…

- **[Trust Responsive Runtime Authorization for Agentic AI with Empirical Characterization of Policy Behavior and Parameter Sensitivity](https://arxiv.org/abs/2611.06996v1)**
  - *Ahsan Habib Shihab, Imre Felde, Ramis Akhmedov et al.*
  - `2026-11-04`
  - The policy that converts runtime estimates of an autonomous agent's condition into operational authority is rarely specified or measured. We empirically characterize the Trust Responsive Authorization Policy (TRAP), which maps an Authorization Readiness Score (ARS), a weighted co…

- **[Autonomous AI Agents Systematically Diverge From Human Preferences in Proof Formalization](https://arxiv.org/abs/2611.06995v1)**
  - *Bálint Gyevnár, Simon DeDeo*
  - `2026-11-04`
  - Artificial intelligence (AI) systems have ushered in a new age of proof abundance, but helping humans understand these proofs requires new attention to the differences in how AI agents and humans pursue a proof-making task. We present "simulated collaboration", a methodology that…

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

- **[The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record](https://arxiv.org/abs/2611.06989v1)**
  - *Vivek Acharya*
  - `2026-11-04`
  - Enterprises run business transactions through multi-agent AI systems spanning clouds, large language models (LLMs), orchestration harnesses, and systems of record. Finance receives AI cost only at settlement grain, aggregated by SKU and charge period. The business question (what…

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

- **[Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism](https://arxiv.org/abs/2611.06984v1)**
  - *Jia Wei, Ziyi Qiu, Yi Xu et al.*
  - `2026-11-04`
  - Reinforcement learning post-training improves the capabilities of large language models, but generating training responses is a major computational bottleneck. In mixture-of-experts models, workers that finish their assigned responses may remain occupied because their experts are…

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

- **[Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment](https://arxiv.org/abs/2611.06543v2)**
  - *Shumao Wu, Kongcheng Zhang, Jianqiang Huang et al.*
  - `2026-11-04`
  - Agent trajectories often contain both successful decisions and failed attempts, yet optimization with sparse trajectory-level rewards struggles to identify which critical decisions should be reinforced or suppressed. We observe that meaningful distinctions among on-policy traject…

- **[EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](https://arxiv.org/abs/2611.06518v1)**
  - *Mingzhe Zheng, Yue Wu, Jing Tan et al.*
  - `2026-11-04`
  - Group Relative Policy Optimization (GRPO) has advanced generative model post-training in verifiable domains such as code and mathematics, but evaluating video quality, especially emotional expression, often depends on subjective aesthetics and has no uniquely correct target. Exis…

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

- **[Formalizing inverse problems in the age of AI: possibilities, pitfalls, and an invitation](https://arxiv.org/abs/2611.06962v1)**
  - *Christian Clason, Tapio Helin, Medet Nursultanov et al.*
  - `2026-11-04`
  - Proof assistants such as Lean check mathematical proofs down to the axioms, and AI agents have recently made writing such proofs cheap. We describe AutoIP, a Lean library in which classical linear regularization theory, together with the functional analysis it rests on, has been…

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

- **[Structured Machine Theory of Mind from Agent Trajectories](https://arxiv.org/abs/2611.07208v1)**
  - *Nigel F. Doering, Rahath Malladi, Arshia Sangwan et al.*
  - `2026-11-04`
  - Predictive models of human behavior trained on large-scale trajectory data optimize for statistical accuracy without representing the mental states that causally generate behavior. Such models support prediction but not principled intervention: they cannot answer how an agent's b…

- **[Meta-Frieren: Beyond Single Level Online Learning](https://arxiv.org/abs/2611.07169v1)**
  - *Vahan Arsenyan, Arnak Dalalyan*
  - `2026-11-04`
  - We study a two-stage online optimization problem: at each round, a meta-learner first selects an agent-environment pair, then the chosen agent interacts with the environment, and receives a reward. We introduce Meta-Frieren, a general framework for maximizing cumulative reward in…

- **[Teaching Agents the "Principle", Not the "Reward"](https://arxiv.org/abs/2611.07130v1)**
  - *Shan Yang*
  - `2026-11-04`
  - Reinforcement learning has achieved strong performance in many tasks by letting agents learn from nothing more than a reward signal. However, in more complex tasks, agents still struggle to learn good, generalizable policies, even with carefully designed rewards and abundant samp…

- **[Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach](https://arxiv.org/abs/2611.07122v1)**
  - *Korbinian Kügler, Carolin Schmidt, Florian Dandl et al.*
  - `2026-11-04`
  - Profit-maximizing Autonomous Mobility-on-Demand (AMoD) operators may exploit consumer surplus through excessive prices and underserve less profitable regions by relocating vehicles away from them. We study how penalty-based regulation of an AMoD operator in a multimodal mobility…

- **[A Framework for Context Enrichment and Selective Robustness in LLM Social Agents](https://arxiv.org/abs/2611.06914v1)**
  - *Mattia Greiche, Reihaneh Rabbany, Maximilian Puelma Touzel*
  - `2026-11-04`
  - Researchers use large language models as agents in social simulations, where agents are prompted with observations and background information intended to shape their actions. Yet LLM agents have been shown to substantially change their behavior under meaning-preserving prompt var…

- **[Visual Token Routing: Learning to keep tokens that matter](https://arxiv.org/abs/2611.06854v1)**
  - *Pranjal Aggarwal, Sean Welleck*
  - `2026-11-04`
  - Computer-use agents (CUAs) have recently achieved superhuman performance on several long-horizon benchmarks. However, their computational cost limits their use in long-horizon tasks and real-time domains such as video games. A key bottleneck is representing each screenshot as tho…

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

- **[Authorization Propagation in Agent2Agent Systems: An Experimental Security Evaluation of Multi-Hop Delegation](https://arxiv.org/abs/2611.07050v1)**
  - *Gabriele Donno, Kashif Mehmood, Katina Kralevska*
  - `2026-11-04`
  - Delegated Agent2Agent (A2A) workflows create a security problem when the agent sending a request is different from the principal from which the authority originated. This paper evaluates a layered downstream-verification design in a synthetic four-party healthcare reimbursement w…

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

- **[Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex](https://arxiv.org/abs/2611.05753v1)**
  - *Andrew Miracle, Phyl Georgiou, Christine Okoth et al.*
  - `2026-11-03`
  - Organizations accumulate evidence in conversations, documents, decisions and relationships, but they act on interpretations: judgements assembled from several observations, resting on assumptions, and revised as circumstances change. Existing retrieval, knowledge graphs and agent…

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

- **[Adversarial Speculative Reasoning Improves Long Horizon Agents](https://arxiv.org/abs/2611.05345v1)**
  - *Hongyin Luo, Wei Fang, Lijie Yang et al.*
  - `2026-11-03`
  - Speculative decoding has been treated purely as a systems optimization that speeds up large language model decoding without changing the model behavior. Under this view, the growing effort to train better draft models has been focused solely on acceptance rate. We argue that this…

- **[PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://arxiv.org/abs/2611.05320v1)**
  - *Kewei Zhang, Juncheng Ma, Guodong Lv et al.*
  - `2026-11-03`
  - Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, the agent receives a data request a…

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

- **[LIBRA: Programmatic Induction of Executable Tool Libraries](https://arxiv.org/abs/2611.05445v2)**
  - *Zekai Li, Zhenke Liu, Yonghao Li et al.*
  - `2026-11-03`
  - Large language model agents increasingly retrieve tools from large catalogs, yet most retrievers rank each tool independently by request similarity. For multi tool tasks, this recovers the goal matching tool while omitting prerequisite tools required by the workflow. We introduce…

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

- **[$τ$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems](https://arxiv.org/abs/2611.04459v1)**
  - *Bharath Sivaram Narasimhan, Karthik R. Narasimhan*
  - `2026-11-03`
  - While conversational recommendation systems provide a more natural user interface, they face the challenge of progressively discovering a user's needs before they can recommend an item that satisfies them. To evaluate the ability of AI agents at this elicitation process, we intro…

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

- **[Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.06956v1)**
  - *Tianming Sha*
  - `2026-11-03`
  - Multi-agent LLM systems explore in parallel by spawning sub-agents with isolated context windows, whereas single-agent systems append every search and verification step into one growing trajectory. However, existing multi-agent frameworks duplicate prefix KV caches across branche…

- **[On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation](https://arxiv.org/abs/2611.05609v1)**
  - *Yichen Wang, Yufa Zhou, Siqi Zhu et al.*
  - `2026-11-03`
  - Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) to consolidate capabilities from multiple teachers. Although prior work reports near-perfect in-distribution (IND) distillation performance, we find that this can mask incomplete capability consolida…

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

- **[DRAP: Dynamics-Risk Adaptive Plasticity for Continual Learning in Physical AI](https://arxiv.org/abs/2611.05029v1)**
  - *Oswaldo Ludwig*
  - `2026-11-03`
  - Continual learning in physical AI differs from conventional continual learning because small per-step policy errors can accumulate over a trajectory. Each deviation may move the agent outside the training distribution, increase subsequent prediction errors, and ultimately cause c…

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

- **[The Male Abstraction Bias in Internet Culture and Large Language Models](https://arxiv.org/abs/2611.05730v2)**
  - *Douglas Guilbeault, Bhargav Srinivasa Desikan*
  - `2026-11-03`
  - Conceptual abstraction and gender are two equally central aspects of the human mind, yet they have traditionally been studied in isolation from one another, as though they were fundamentally separate. Here, we find gender and abstraction are systematically linked throughout the s…

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


## Harness  (114)

### AAAI

- **[MCP-AgentBench: Evaluating Real-World Language Agent Performance with MCP-Mediated Tools](https://arxiv.org/abs/2509.09734)**
  - *Zikang Guo, Benfeng Xu, Chiwei Zhu et al.*
  - **AAAI 2025** · `2025-09-10`
  - The Model Context Protocol (MCP) is rapidly emerging as a pivotal open standard, designed to enhance agent-tool integration and interoperability, and is positioned to unlock a new era of powerful, interconnected, and genuinely utilitarian agentic AI. However, despite MCP's growin…


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


### ACL

- **[Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417v1)**
  - *E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman et al.*
  - **ACL** · `2026-11-05`
  - Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important. Yet even benchmarks that are carefully validated at release can become stale. As models improve, they can discover valid solutions that exis…

- **[Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models](https://arxiv.org/abs/2505.02847)**
  - *Bang Zhang, Ruo-Tian Ma, Qing-Xuan Jiang et al.*
  - **ACL 2025** · `2025-05-01`
  - Assessing how well a large language model (LLM) understands human, rather than merely text, remains an open challenge. To bridge the gap, we introduce Sentient Agent as a Judge (SAGE), an automated evaluation framework that measures an LLM's higher-order social cognition. SAGE in…


### Other / arXiv

- **[Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training](https://arxiv.org/abs/2611.04277)**
  - *Kangning Zhang, Wenxiang Jiao, Bowen Fang et al.*
  - 🤗 Featured · `2026-11-03`
  - Harness evolution from a common base exhibits Locality, Complementarity, and Nonstationarity: variants repair different failures, and their utility changes as the policy learns. Rather than seeking a universally superior harness, we introduce Harness-S to selectively rescue failu…

- **[Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding](https://arxiv.org/abs/2611.07723)**
  - *Emile de Bruyn, Moritz Schäffler, Jannik Schneider et al.*
  - 🤗 · `2026-11-05`
  - Protein motif scaffolding benchmarks assess whether generative models can build scaffolds around functionally important residues. Their conclusions depend on which motifs are tested and which criteria define success. Existing benchmarks typically use small hand-curated motif sets…

- **[The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks for Solving Real-World Tasks](https://arxiv.org/abs/2611.07461)**
  - *Haibo Jin, Peng Kuang, Xiaopeng Yuan et al.*
  - 🤗 · `2026-11-05`
  - How can an agent handle a real-world task end to end? Frontier models with their own harnesses still fall short on real-world benchmarks: on Terminal-Bench 4.0, GPT-5.6 Sol with Codex resolves 37.3% of the tasks and Claude Opus 5 with Claude Code 51.8%. These tasks fail at the st…

- **[LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856)**
  - *Haoxiang Cao, Yuxuan Zhang, Penghui Du et al.*
  - 🤗 · `2026-11-04`
  - We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence, rejecting distractors, binding e…

- **[How Do AI Agents Waste Your Money?](https://arxiv.org/abs/2611.07238)**
  - *Huimin Zeng, Yuxuan Lu, Jesse Cai et al.*
  - 🤗 · `2026-11-04`
  - AI agents may consume massive tokens across a wide range of tasks, but how many of those tokens are really necessary? Although prior work has shown that agents can incur unexpectedly high token costs, we still lack a systematic way to identify and measure token waste. In this wor…

- **[The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI](https://arxiv.org/abs/2611.08428v1)**
  - *Julian Kunkel, Ali Doosthosseini*
  - `2026-11-05`
  - Chat remains the default surface for many large language model (LLM) tasks, even as agentic tools such as OpenCode excel at coding and automation. Yet the model sees the current dialogue but not the workspace around it. We explore meta access---giving the assistant a structured,…

- **[CORE: Coarse-to-Fine Search with Context Management for Deep Research](https://arxiv.org/abs/2611.07859v1)**
  - *Hoang Tran Vuong, Ngoc Quan Pham, Hung Bui et al.*
  - `2026-11-05`
  - Deep research agents answer complex questions through repeated search. They rely on a harness that runs their tool calls and returns evidence to their context. This creates a trade-off: Search works best over long passages, which give enough context for reliable semantic matching…

- **[Beneath the Surface: What We Overlook When We Talk About Agent Evolution](https://arxiv.org/abs/2611.07624v1)**
  - *Xiaobo Wang, Zimu Wang, Siyu Ye et al.*
  - `2026-11-05`
  - Agent harness evolution enables recursive self-improvement (RSI) without updating model weights. We examine whether higher benchmark scores yield reliable, efficient, and transferable improvement. We evaluate four methods across harnesses, general and coding tasks. Repeated evalu…

- **[Evolver: Turning Agent Exploration into Evolving Capabilities](https://arxiv.org/abs/2611.07595v1)**
  - *Haoyang Zhang, Qumeng Sun, Xiao Zhang et al.*
  - `2026-11-05`
  - Agent exploration produces valuable procedural knowledge, yet much of this experience remains confined to transient execution traces and is not systematically reused. We introduce Evolver, an experience-driven framework that transforms agent exploration into persistent, reusable…

- **[DelegateEval: Evaluating Platforms for Personal External Service Agents](https://arxiv.org/abs/2611.07508v1)**
  - *Jichao Li, Jinrong Lu, Manjiang Yu et al.*
  - `2026-11-05`
  - AI agents that work for an individual over time may also help that individual serve external clients. We define a personal external service agent as an agent authorized and continuously managed by a specific individual to accept client requests, deliver work, and provide ongoing…

- **[EnvOpt: Automated Optimization for Agent Environments](https://arxiv.org/abs/2611.07372v1)**
  - *Mingxuan Li, Huanzhi Mao, Qiuyang Mang et al.*
  - `2026-11-05`
  - An LLM agent's cost and success depend on its model, its harness, and its environment. In addition to the widely studied directions of parameter tuning and harness optimization, we propose the third direction: optimization over stationary environments. Agents are often deployed i…

- **[Selective Retrieval Routing for Multi-Violation Knowledge Graph Repair](https://arxiv.org/abs/2611.07342v1)**
  - *Tung-Wei Lin, Gabe Fierro, Han Li et al.*
  - `2026-11-05`
  - Knowledge graphs often contain missing or inconsistent facts that undermine the applications built on them. Schema validation detects such violations but does not identify which of several valid repairs recovers the intended graph. External corpora can supply the evidence needed…

- **[Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks](https://arxiv.org/abs/2611.08281v1)**
  - *Zhitao He, Chi Him Zhang, Chengru Han et al.*
  - `2026-11-05`
  - Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchma…

- **[Take It From Here: Evaluating Coding Agents On Project Takeover](https://arxiv.org/abs/2611.07307v1)**
  - *Dingxian Wang, Zhe Fu, Jiaqi Deng et al.*
  - `2026-11-05`
  - Coding agents increasingly collaborate on long-term projects. When taking over a project, they need to recover currently applicable requirements from the interaction history and update them in response to new requests. However, most coding benchmarks do not include long interacti…

- **[Who Can Evaluate AI Independently? A Framework for Analysing Evaluation Infrastructure](https://arxiv.org/abs/2611.08134v1)**
  - *Sumaya Nur Adan, Joanna Wiaterek, Nourhan Abdelrhim et al.*
  - `2026-11-05`
  - AI evaluation is increasingly central to AI safety and governance, yet taking part in an evaluation does not by itself confer authority over its design, its execution or the resources it depends on. This paper examines how infrastructure arrangements distribute that authority, an…

- **[Synthesis of Ovarian Cancer Multi-Omics Datasets: A Biology-Informed Evaluation Framework](https://arxiv.org/abs/2611.08394v1)**
  - *Déborah Boyenval, Alina Malyutina, Jaana Oikkonen et al.*
  - `2026-11-05`
  - Paired multi-omic cancer cohorts are costly to assemble and difficult to share, motivating synthetic cohorts as a complementary resource. As generative model development accelerates, we shift the focus from proposing yet another architecture to defining evaluation criteria that d…

- **[Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration](https://arxiv.org/abs/2611.07066v1)**
  - *Sungil Son, Hoseong Jung, Dahyun Oh et al.*
  - `2026-11-04`
  - Discovering cooperative behavior in multi-agent reinforcement learning (MARL) is challenging due to the combinatorial complexity of joint state-action spaces, which hinders the emergence of coordinated behaviors from trial-and-error alone. Intrinsic rewards are often used to aid…

- **[Closed-Loop Agent Evaluation: Layered Measurement and Self-Calibration](https://arxiv.org/abs/2611.07051v1)**
  - *Ruifeng Ren, Gun Ahn*
  - `2026-11-04`
  - Once an agent is live, teams want to know whether it is doing its job, not just whether it throws errors. Yet most evaluation is one-off: a benchmark run, a look at traces, a single score. Its conclusions neither check themselves nor reach the agent. We propose closed-loop evalua…

- **[Task-Efficient Agent Evaluation Using Cached Traces](https://arxiv.org/abs/2611.06803v1)**
  - *Ben Johnson, Hayden Helm*
  - `2026-11-04`
  - Efficient benchmarking estimates a system's full benchmark performance from a small number of task executions. Standard approaches rely solely on the binary correctness of executions from a collection of already-evaluated reference systems. An agentic system, however, produces a…

- **[The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record](https://arxiv.org/abs/2611.06989v1)**
  - *Vivek Acharya*
  - `2026-11-04`
  - Enterprises run business transactions through multi-agent AI systems spanning clouds, large language models (LLMs), orchestration harnesses, and systems of record. Finance receives AI cost only at settlement grain, aggregated by SKU and charge period. The business question (what…

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


## Finance  (178)

### NeurIPS

- **[Self-Challenging Language Model Agents](https://arxiv.org/abs/2506.01716)**
  - *Yifei Zhou, Sergey Levine, Jason E. Weston et al.*
  - **NeurIPS 2025** · `2025-06-02`
  - Large language models are quickly becoming the foundation for intelligent agents that are capable of using tools. However, training such agents is challenging because it requires human creation and annotation of a diverse set of tasks, tools, and evaluation criteria. In this pape…


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

- **[Position: Uncertainty Quantification Needs Reassessment for Large-language Model Agents](https://arxiv.org/abs/2505.22655)**
  - *Michael Kirchhof, Gjergji Kasneci, Enkelejda Kasneci*
  - **ICML 2025** · `2025-05-28`
  - Large-language models (LLMs) and chatbot agents are known to provide wrong outputs at times, and it was recently found that this can never be fully prevented. Hence, uncertainty quantification plays a crucial role, aiming to quantify the level of ambiguity in either one overall n…


### EMNLP

- **[Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://arxiv.org/abs/2503.02519)**
  - *Xingzuo Li, Ke-Hai Chen, Yunfei Long et al.*
  - **EMNLP 2025** · `2025-03-04`
  - Large language model (LLM) agents typically adopt a step-by-step reasoning framework, in which they interleave the processes of thinking and acting to accomplish the given task. However, this paradigm faces a deep-rooted one-pass issue whereby each generated intermediate thought…


### Other / arXiv

- **[Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding](https://arxiv.org/abs/2611.07723)**
  - *Emile de Bruyn, Moritz Schäffler, Jannik Schneider et al.*
  - 🤗 · `2026-11-05`
  - Protein motif scaffolding benchmarks assess whether generative models can build scaffolds around functionally important residues. Their conclusions depend on which motifs are tested and which criteria define success. Existing benchmarks typically use small hand-curated motif sets…

- **[WayPOP: A Panoramic Open-Set Panoptic Tracking Benchmark](https://arxiv.org/abs/2611.05801)**
  - *Rohit Mohan, Maximilian Luz, Swarnava Chowdhury et al.*
  - 🤗 · `2026-11-04`
  - Holistic perception for autonomous agents requires reliably segmenting and associating scene elements across time and camera views, including objects outside a fixed semantic taxonomy. Existing open-set panoptic benchmarks focus on individual images or views, while panoramic trac…

- **[ReproBridge: Building Reproducibility into ML Research Artifacts](https://arxiv.org/abs/2611.08452v1)**
  - *Yubo Wang, Rui Meng, Jaehyun Nam et al.*
  - `2026-11-05`
  - Reproducing machine learning experiments requires reconstructing procedures from information scattered across papers, released code, and supporting artifacts. For coding agents, reproduction success can therefore depend on their ability to fill in missing details, rather than on…

- **[When Imperfect Automated Fact-Checking Backfires: Social Learning in the Presence of Misinformation](https://arxiv.org/abs/2611.08053v1)**
  - *Zixuan Liu, Ming Cao*
  - `2026-11-05`
  - Automated fact-checking tools, cheap and fast but imperfect, are increasingly available on social platforms. We study when such tools can backfire in a sequential social learning model of misinformation. Agents observe an article's reliability and their predecessors' actions, whi…

- **[PharmAgents2: Towards Autonomous End-to-End Drug Discovery](https://arxiv.org/abs/2611.07653v1)**
  - *Haichuan Tan, Bowen Gao, Tao Huang et al.*
  - `2026-11-05`
  - Drug discovery requires continuous scientific decision-making across a vast research space. We introduce PharmAgents2, an autonomous system for end-to-end drug discovery that combines knowledge-enhanced decision-making with organized large-scale exploration. Paper2Skill extracts…

- **[Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks](https://arxiv.org/abs/2611.07640v1)**
  - *Rongting Zhang, Martin Bertran, Sandeep Avula et al.*
  - `2026-11-05`
  - Indirect prompt-injection (IPI) benchmarks predominantly test planted instructions that redirect a tool-using agent toward an attacker-chosen task. Yet attacker-controlled content can instead tamper with the outcome of the task already in progress. A buyer's dispute evidence can…

- **[DelegateEval: Evaluating Platforms for Personal External Service Agents](https://arxiv.org/abs/2611.07508v1)**
  - *Jichao Li, Jinrong Lu, Manjiang Yu et al.*
  - `2026-11-05`
  - AI agents that work for an individual over time may also help that individual serve external clients. We define a personal external service agent as an agent authorized and continuously managed by a specific individual to accept client requests, deliver work, and provide ongoing…

- **[FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance](https://arxiv.org/abs/2611.07464v1)**
  - *Yupeng Cao, Xueqing Peng, Lingfei Qian et al.*
  - `2026-11-05`
  - Language agents increasingly work for users on the open Web, and finance is where trusting them is hardest. The data must come from the Web, the strategy lives in the user's head, and correctness depends on time, so an agent can fail silently: a strategy the user never asked for,…

- **[Regret Bounds for Profit Maximization in Bilateral Trade: Learning the Best Posted-Price Mechanism](https://arxiv.org/abs/2611.08173v1)**
  - *Johannes Brüstle, Simone Di Gregorio, Federico Fusco et al.*
  - `2026-11-05`
  - Bilateral trade models the task of intermediating between two strategic agents, a seller and a buyer, willing to trade a good for which they hold private valuations. We study this problem from the perspective of a profit-maximizing broker in a regret minimization framework. At ea…

- **[Foresee to Trade: Forecast-Augmented Policy Optimization for Portfolio Management](https://arxiv.org/abs/2611.07750v1)**
  - *Zeyu Liu, Xuanzhi Feng, Haoran Xu et al.*
  - `2026-11-05`
  - Online investment services must translate asset opportunities into investment outcomes for users' accounts, yet the same market opportunity can warrant different account actions. We study how supervision from future asset opportunities can strengthen account-level trading decisio…

- **[MEvince: Knowledge-Constrained LLM Reasoning for Technique Identification from Malware Reports](https://arxiv.org/abs/2611.07486v1)**
  - *Hongyu She, Yiling He, Mengda Xie et al.*
  - `2026-11-05`
  - Mapping behavioral intelligence in malware analysis reports to ATT&CK techniques supports threat analysis and defense, but reliable identification remains challenging. Supporting evidence is often scattered across long, heterogeneous reports, while closely related techniques shar…

- **[Synthesis of Ovarian Cancer Multi-Omics Datasets: A Biology-Informed Evaluation Framework](https://arxiv.org/abs/2611.08394v1)**
  - *Déborah Boyenval, Alina Malyutina, Jaana Oikkonen et al.*
  - `2026-11-05`
  - Paired multi-omic cancer cohorts are costly to assemble and difficult to share, motivating synthetic cohorts as a complementary resource. As generative model development accelerates, we shift the focus from proposing yet another architecture to defining evaluation criteria that d…

- **[Conformal Prediction for Time-Dependent PDEs](https://arxiv.org/abs/2611.08409v1)**
  - *Joshua Stiller, Annika Schneider, Eyke Hüllermeier*
  - `2026-11-05`
  - Uncertainty quantification is crucial in scientific machine learning, where models inform safety-critical tasks such as flood forecasting, financial risk management, and thermal control in machines. Conformal prediction provides distribution-free coverage guarantees, but in time-…

- **[Scenario Augmentation for Rare Financial Events via Multimodal Latent Diffusion](https://arxiv.org/abs/2611.07282v1)**
  - *Mahdi Arab Loodaricheh, Anita Raja, Indranil SenGupta*
  - `2026-11-05`
  - Extreme market movements are scarce, heterogeneous, and difficult to learn from imbalanced historical data. We study whether generative augmentation can improve the representation and classification of CVaR-labeled rare financial windows while retaining the complementary structur…

- **[Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety](https://arxiv.org/abs/2611.08438v1)**
  - *Fazl Barez, Tung-Yu Wu, Hunar Batra et al.*
  - `2026-11-05`
  - Neural networks are likely to be among the most consequential artefacts in human history. As these systems become more capable and autonomous, their potential to cause societal harm also grows, making AI safety one of the defining challenges of our time. Yet we continue to build…

- **[SHORE: Stability-Hybrid On-Policy Reinforcement Learning for Online Bin Packing](https://arxiv.org/abs/2611.08364v1)**
  - *Chang Shi, Ann Majewicz Fey*
  - `2026-11-05`
  - Online 3D bin packing with a processing buffer requires choosing which box to pack, its orientation, and its placement while keeping the stack stable under unknown future arrivals. A collapse ends the episode and forfeits the remaining volume. Existing methods use geometric rules…

- **[AI-Native Task-Oriented Semantic Communications over a Relay: Benefits and Vulnerabilities](https://arxiv.org/abs/2611.08155v1)**
  - *Yalin E. Sagduyu, Tugba Erpek, Aylin Yener*
  - `2026-11-05`
  - Semantic communication (SemCom) using a relay node is considered, where the relay assists in conveying task-relevant information from a source to a destination, with meaning defined by classification labels. A joint end-to-end design of the source encoder, relay transformation, a…

- **[Ordering Multivariate Time Series by Volatility Memory: A Temporal Convolutional Approach to Volatility Heredity](https://arxiv.org/abs/2611.07746v1)**
  - *Kaoutar El Azaar, Mohamed Hamlich, Moncef Garouani et al.*
  - `2026-11-05`
  - Volatility dynamics can carry information about temporal relationships that is not apparent in the conditional mean. Extracting this information is difficult because the persistence of each variable can obscure its dependence on other variables. This paper presents QS-TCN, a meth…

- **[Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?](https://arxiv.org/abs/2611.07166v1)**
  - *Xiangkai Zeng, Zheng Liu, Zihao Lin*
  - `2026-11-04`
  - Developers rarely give a coding agent a single request: they ask it to build a component and then to extend, upgrade, and optimize it, each time on code the agent itself wrote. Most benchmarks, however, score one task at a time. We introduce Multi-step SWE, a long-horizon benchma…

- **[Autonomous AI Agents Systematically Diverge From Human Preferences in Proof Formalization](https://arxiv.org/abs/2611.06995v1)**
  - *Bálint Gyevnár, Simon DeDeo*
  - `2026-11-04`
  - Artificial intelligence (AI) systems have ushered in a new age of proof abundance, but helping humans understand these proofs requires new attention to the differences in how AI agents and humans pursue a proof-making task. We present "simulated collaboration", a methodology that…

- **[The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record](https://arxiv.org/abs/2611.06989v1)**
  - *Vivek Acharya*
  - `2026-11-04`
  - Enterprises run business transactions through multi-agent AI systems spanning clouds, large language models (LLMs), orchestration harnesses, and systems of record. Finance receives AI cost only at settlement grain, aggregated by SKU and charge period. The business question (what…

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

- **[Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach](https://arxiv.org/abs/2611.07122v1)**
  - *Korbinian Kügler, Carolin Schmidt, Florian Dandl et al.*
  - `2026-11-04`
  - Profit-maximizing Autonomous Mobility-on-Demand (AMoD) operators may exploit consumer surplus through excessive prices and underserve less profitable regions by relocating vehicles away from them. We study how penalty-based regulation of an AMoD operator in a multimodal mobility…

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

- **[The Alignment Tax Is Graded: Task-Selective Capability Loss Under Length-Normalized DPO with SFT Retention](https://arxiv.org/abs/2611.06476v2)**
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


---
*Generated 2026-11-06 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
