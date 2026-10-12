# Daily Paper Digest — 2026-10-12 (Monday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**337 unique papers** (429 topic-entries — cross-topic papers counted once per category)

---

## Agent  (197)

### AAAI

- **[AutoTool: Efficient Tool Selection for Large Language Model Agents](https://arxiv.org/abs/2511.14650)**
  - *Jin Jia, Qin-Bin Li*
  - **AAAI 2025** · `2025-11-18`
  - Large Language Model (LLM) agents have emerged as powerful tools for automating complex tasks by leveraging the reasoning and decision-making abilities of LLMs. However, a major bottleneck in current agent frameworks lies in the high inference cost of tool selection, especially i…

- **[Evaluating Goal Drift in Language Model Agents](https://www.semanticscholar.org/paper/384e32875255f2c17f7b5f3110a11b4be09ffab8)**
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

- **[DMT-RoleBench: A Dynamic Multi-Turn Dialogue Based Benchmark for Role-Playing Evaluation of Large Language Model and Agent](https://ojs.aaai.org/index.php/AAAI/article/download/34768/36923)**
  - *Ding-Bo Yuan, Yi-Peng Chen, Guo-Dong Liu et al.*
  - **AAAI 2025** · `2025-04-11`
  - Recent years have witnessed a profound evolution in the abilities of Large Language Model, which has significantly boosted the proliferation of role-playing agents and platforms.
Nonetheless, there is a conspicuous absence of systematic and comprehensive evaluations of role-playi…


### NeurIPS

- **[DataClawBench: An Agent Benchmark for Exploratory Real-World Financial Data Analysis](https://openreview.net/forum?id=9RSvub7ht8)**
  - **NeurIPS 2025** · OpenReview · `2026-09-17`
  - Realistic analysis often begins without knowing where the relevant evidence lies, raising a fundamental question for autonomous data analysis: can agents discover and use the required evidence with limited human guidance? However, existing benchmarks typically evaluate such agent…

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
  - *Wenbo Hu, Yi-Ning Hong, Yanjun Wang et al.*
  - **NeurIPS 2025** · `2025-05-28`
  - Humans excel at performing complex tasks by leveraging long-term memory across temporal and spatial experiences. In contrast, current Large Language Models (LLMs) struggle to effectively plan and act in dynamic, multi-room 3D environments. We posit that part of this limitation is…

- **[Code Graph Model (CGM): A Graph-Integrated Large Language Model for Repository-Level Software Engineering Tasks](https://arxiv.org/abs/2505.16901)**
  - *Hongyuan Tao, Ying Zhang, Zhenhao Tang et al.*
  - **NeurIPS 2025** · `2025-05-22`
  - Recent advances in Large Language Models (LLMs) have shown promise in function-level code generation, yet repository-level software engineering tasks remain challenging. Current solutions predominantly rely on proprietary LLM agents, which introduce unpredictability and limit acc…


### ICML

- **[Harness Self-Evolution: Theory, Algorithms, Evaluation, Applications, and Impact](https://openreview.net/forum?id=m5jsFGXUM2)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - **ICML 2025** · OpenReview · `2026-10-11`
  - Building agents that learn from experience is a central goal of artificial intelligence. Harness self-evolution offers a path toward this goal by revising an agent’s instructions, memory, workflows, and tools while model weights stay fixed. In this article, we develop a unified f…

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

- **[DS-Lighting: Making Agent Harnesses Explicit for Data-Science Automation](https://openreview.net/forum?id=k7K6gcD74M)**
  - **ICML 2025** · OpenReview · `2026-05-26`
  - Large Language Model (LLM) agents have shown promise for automating data-science workflows, yet their end-to-end performance depends critically on the agent harness that represents tasks, manages execution state, constrains output artifacts, and provides evaluation feedback. Exis…

- **[AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing](https://openreview.net/forum?id=IzKJV1g5jX)**
  - **ICML 2025** · OpenReview · `2026-05-17`
  - Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts.
Recent reinforcement learnin…

- **[Reasoning Is More Than the Model: Harness-Aware Evaluation of Agents on Verifiable Reasoning Tasks](https://openreview.net/forum?id=fnHhEf0cSE)**
  - *Zhanke Zhou, Zongze Li, Weikai Huang et al.*
  - **ICML 2025** · OpenReview · `2026-05-14`
  - Open agents are no longer just models: they are model-harness systems whose behavior depends on tool access, control loops, execution feedback, memory, etc. Yet existing evaluations either test models without a harness or fix a single harness to compare models within a domain, ob…

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
  - *Jianke Zhang, Yan-Jiang Guo, Yucheng Hu et al.*
  - **ICML 2025** · `2025-01-30`
  - Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilit…


### ICLR

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **ICLR 2026** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…


### ACL

- **[SWE-Critix: Post-Training Generalist Verifiers for Assessing Coding-Agent Trajectories](https://arxiv.org/abs/2610.13356)**
  - *Jiajun Hu, Chun Yong Chong*
  - **ACL** · 🤗 · `2026-10-09`
  - Coding agents are increasingly deployed for end-to-end software engineering tasks, where a readily available oracle evaluator that defines the success criteria is often absent. This motivates verifications for coding agents that can reliably judge and explain their behavior. Howe…

- **[Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885)**
  - *Yi Yu, Liuyi Yao, Yue-Xiang Xie et al.*
  - **ACL 2026** · `2026-01-05`
  - Large language model (LLM) agents face fundamental limitations in long-horizon reasoning due to finite context windows, making effective memory management critical. Existing methods typically handle long-term memory (LTM) and short-term memory (STM) as separate components, relyin…

- **[SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073)**
  - *Zong-Hao Ying, Yang-Guang Shao, Jianle Gan et al.*
  - **ACL 2025** · `2025-10-11`
  - Large vision-language model (LVLM)-based web agents are emerging as powerful tools for automating complex online tasks. However, when deployed in real-world environments, they face serious security risks, motivating the design of security evaluation benchmarks. Existing benchmark…

- **[Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828)**
  - *Si-Kuan Yan, Xiu-Feng Yang, Zuchao Huang et al.*
  - **ACL 2025** · `2025-08-27`
  - Large Language Models (LLMs) have demonstrated impressive capabilities across a wide range of NLP tasks, but they remain fundamentally stateless, constrained by limited context windows that hinder long-horizon reasoning. Recent efforts to address this limitation often augment LLM…

- **[R-VLM: Region-Aware Vision Language Model for Precise GUI Grounding](https://arxiv.org/abs/2507.05673)**
  - *Joonhyung Park, Peng Tang, Sagnika Das et al.*
  - **ACL 2025** · `2025-07-07`
  - Visual agent models for automating human activities on Graphical User Interfaces (GUIs) have emerged as a promising research direction, driven by advances in large Vision Language Models (VLMs). A critical challenge in GUI automation is the precise grounding of interface elements…

- **[MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](https://arxiv.org/abs/2506.21605)**
  - *Hao-Ran Tan, Ze-Yu Zhang, Chen Ma et al.*
  - **ACL 2025** · `2025-06-20`
  - Recent works have highlighted the significance of memory mechanisms in LLM-based agents, which enable them to store observed information and adapt to dynamic environments. However, evaluating their memory capabilities still remains challenges. Previous evaluations are commonly li…

- **[Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models](https://arxiv.org/abs/2505.02847)**
  - *Bang Zhang, Ruotian Ma, Qingxuan Jiang et al.*
  - **ACL 2025** · `2025-05-01`
  - Assessing how well a large language model (LLM) understands human, rather than merely text, remains an open challenge. To bridge the gap, we introduce Sentient Agent as a Judge (SAGE), an automated evaluation framework that measures an LLM's higher-order social cognition. SAGE in…

- **[ProjectEval: A Benchmark for Programming Agents Automated Evaluation on Project-Level Code Generation](https://arxiv.org/abs/2503.07010)**
  - *Kaiyuan Liu, You-Cheng Pan, Jing Li et al.*
  - **ACL 2025** · `2025-03-10`
  - Recently, LLM agents have made rapid progress in improving their programming capabilities. However, existing benchmarks lack the ability to automatically evaluate from users' perspective, and also lack the explainability of the results of LLM agents' code generation capabilities.…

- **[FACT-AUDIT: An Adaptive Multi-Agent Framework for Dynamic Fact-Checking Evaluation of Large Language Models](https://arxiv.org/abs/2502.17924)**
  - *Hongzhan Lin, Yang Deng, Yuxuan Gu et al.*
  - **ACL 2025** · `2025-02-25`
  - Large Language Models (LLMs) have significantly advanced the fact-checking studies. However, existing automated fact-checking evaluation methods rely on static datasets and classification metrics, which fail to automatically evaluate the justification production and uncover the n…

- **[SOTOPIA-Ω: Dynamic Strategy Injection Learning and Social Instruction Following Evaluation for Social Agents](https://arxiv.org/abs/2502.15538)**
  - *Wenyuan Zhang, Tian-Yun Liu, Mengxiao Song et al.*
  - **ACL 2025** · `2025-02-21`
  - Despite the abundance of prior social strategies possessed by humans, there remains a paucity of research dedicated to their transfer and integration into social agents. Our proposed SOTOPIA-$\Omega$ framework aims to address and bridge this gap, with a particular focus on enhanc…

- **[Towards a Design Guideline for RPA Evaluation: A Survey of Large Language Model-Based Role-Playing Agents](https://arxiv.org/abs/2502.13012)**
  - *Chao-Ran Chen, Bingsheng Yao, Ruishi Zou et al.*
  - **ACL 2025** · `2025-02-18`
  - Role-Playing Agent (RPA) is an increasingly popular type of LLM Agent that simulates human-like behaviors in a variety of tasks. However, evaluating RPAs is challenging due to diverse task requirements and agent designs. This paper proposes an evidence-based, actionable, and gene…

- **[AgentGym: Evaluating and Training Large Language Model-based Agents across Diverse Environments](https://aclanthology.org/2025.acl-long.1355.pdf)**
  - *Zhi-Heng Xi, Yiwen Ding, Wen-Xiang Chen et al.*
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
  - *Tianqing Fang, Hong-Ming Zhang, Zhisong Zhang et al.*
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

- **[EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents](https://arxiv.org/abs/2610.13021)**
  - *Jie Huang, Yanan Chen, Ruixun Liu et al.*
  - 🤗 Featured · `2026-10-09`
  - Continual learning requires models to accumulate past experience and transfer it to new tasks. Despite substantial research on continual learning, existing work remains largely confined to non-embodied settings, without extending to embodied environments. To address this gap, we…

- **[ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents](https://arxiv.org/abs/2610.13395)**
  - *Chengyi Yang, Renxu Bao, Jue Hou et al.*
  - 🤗 Featured · `2026-10-09`
  - Coding agents are increasingly used to build programs from scratch as software engineers do rather than to resolve issues within a repository or to generate a repository from a given requirements document. However, scalable verifiable training environments that force agents to di…

- **[Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction](https://arxiv.org/abs/2610.12984)**
  - *Yuqi Huang, Hui Li, Yifei Cao et al.*
  - 🤗 Featured · `2026-10-09`
  - Computer-use agents can perform increasingly complex GUI tasks, yet unfamiliar software and workflows requiring human domain knowledge remain challenging. Human demonstrations convey procedural knowledge through the same GUI interaction space, but reuse requires interpreting acti…

- **[Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark](https://arxiv.org/abs/2610.13947)**
  - *Xudong Cai, Ruijie Zhu, Haoliang Shang et al.*
  - 🤗 Featured · `2026-10-09`

- **[The value of information and the emergence of communication in evolved e-puck robots](https://arxiv.org/abs/2610.13118)**
  - *Fernando Montes-Gonzalez*
  - 🤗 Featured · `2026-10-09`
  - We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robo…

- **[SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments](https://arxiv.org/abs/2610.12611)**
  - *Tian Jin, Wenhao Wang, Jing Kang et al.*
  - 🤗 Featured · `2026-10-08`

- **[Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition](https://arxiv.org/abs/2610.12341)**
  - *Kaisen Yang, Qingle Liu, Kejin Wang et al.*
  - 🤗 Featured · `2026-10-08`

- **[SWE-Duel: Towards a Self-Scaling Arena for Coding Agents](https://arxiv.org/abs/2610.12569)**
  - *Wei Minn, Zhensu Sun, Lwin Khin Shar et al.*
  - 🤗 Featured · `2026-10-08`

- **[Recurrent Harness for Agentic Continual Learning](https://arxiv.org/abs/2610.12668)**
  - *Yuxin Xiao, Zhiyun Lu, Jianyu Wang et al.*
  - 🤗 Featured · `2026-10-08`

- **[Coding-Agent Benchmarks Should Match Their Users' Task Flows](https://arxiv.org/abs/2610.09633)**
  - *Igor Slinko, Yaroslav Golubev, Sergey Titov*
  - 🤗 Featured · `2026-10-07`

- **[Stateless Language Agents: Scaling Long-Horizon Automated Research](https://arxiv.org/abs/2610.07625)**
  - *Qizheng Zhang, Changxiu Ji, Isaac Sun et al.*
  - 🤗 Featured · `2026-10-06`

- **[From Given to Gathered Evidence: Agentic Learning for Longitudinal Medical Reasoning](https://arxiv.org/abs/2609.39566)**
  - *Minye Shao, Chaohui Yu, Yixuan Wu et al.*
  - 🤗 Featured · `2026-09-30`

- **[Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution](https://arxiv.org/abs/2609.37950)**
  - *Bingjun Luo, Jialin Guo, Siqi Li*
  - 🤗 Featured · `2026-09-29`

- **[AgentSWE: Can Coding Agents Build the Agent You Actually Want?](https://arxiv.org/abs/2610.13361)**
  - *Jiahao Wang, Hongjin Qian, Yuyang Hu et al.*
  - 🤗 · `2026-10-09`
  - As the production of software passes into the hands of software itself, coding agents are increasingly commissioned to build agents fitted to their users' own workflows. This delegation carries a quiet assumption, that the delivered agent will faithfully serve the requirement it…

- **[Scaling Agentic Data for Long-Horizon Terminal Intelligence](https://arxiv.org/abs/2610.13166)**
  - *Shun Zou, Ziyu Ma, Yi Zou et al.*
  - 🤗 · `2026-10-09`
  - Terminal agents are moving beyond local operations toward completing real-world professional tasks. Short trajectories can demonstrate commands and tool calls, but they do not fully show how agents accumulate evidence through exploration, use it to inform judgments, continually a…

- **[TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications](https://arxiv.org/abs/2610.13065)**
  - *Kazuki Egashira, Niels Mündler-Sasahara, Mark Niklas Müller et al.*
  - 🤗 · `2026-10-09`

- **[GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images](https://arxiv.org/abs/2610.11215)**
  - *Qirui Wu, Stan Birchfield, Hesam Rabeti et al.*
  - 🤗 · `2026-10-08`

- **[VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails](https://arxiv.org/abs/2610.12813)**
  - *Duy Nguyen, Lesly Miculicich, Bhavana Dalvi Mishra et al.*
  - 🤗 · `2026-10-08`

- **[RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](https://arxiv.org/abs/2610.13889v1)**
  - *Weiliang Chen, Song Liao*
  - `2026-10-09`
  - As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via…

- **[X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](https://arxiv.org/abs/2610.13886v1)**
  - *Yeonsung Jung, Zhiyuan Wang, Zifan Wang et al.*
  - `2026-10-09`
  - Personal agents increasingly connect to services across the web and applications by using tools. As the effects of their actions accumulate and interact across services, unintended or harmful outcomes can arise when agents fulfill benign user requests. Proactively identifying the…

- **[MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents](https://arxiv.org/abs/2610.13829v1)**
  - *Jingwei Song, Zhisheng Chen, Bingfan Zeng et al.*
  - `2026-10-09`
  - A central challenge in embodied recursive self-improvement is enabling agents to convert interaction history into capabilities that persist beyond one world and transfer to later tasks. A saved memory or successful final action does not by itself establish that a reusable capabil…

- **[Matched-Context Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2610.13755v1)**
  - *Chenxu Zhang, Yaorui Shi, Wenlong Zhang et al.*
  - `2026-10-09`
  - Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enter…

- **[SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.13737v1)**
  - *Hongrui Zheng, Aditya Singh, Rahul Mangharam*
  - `2026-10-09`
  - Cooperative multi-agent tasks often impose constraints on a shared objective or collective safety. A team level violation cost function can measure this constraint outcome, but does not distinguish which agents' actions most strongly influence that violation. We present SafeDiSTL…

- **[A Baseline Assessment for the Agentic Web Technology Stack](https://arxiv.org/abs/2610.13703v1)**
  - *Vagner Figueredo de Santana, Diogo Cortiz*
  - `2026-10-09`
  - The fast pace in which protocols, frameworks, and technologies are being proposed for LLM-based agents results in a complex scenario for anyone aiming to create state-of-the-art AI solutions. Without an assessment on how different protocols, frameworks, and libraries work togethe…

- **[A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models](https://arxiv.org/abs/2610.13663v1)**
  - *Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev et al.*
  - `2026-10-09`
  - Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models o…

- **[Humanize Olympiad Agents: A Multi-Session Workflow for Olympiad Problem Solving with Solve, Review, Wiki, Verify](https://arxiv.org/abs/2610.13632v1)**
  - *Zhengyang Zhang, Jing Xiong, Hongzhou Lin et al.*
  - `2026-10-09`
  - Large language model (LLM) agents are rapidly improving on long-horizon scientific and olympiad tasks. Recent systems have produced a Lean-formalized resolution of the Navier--Stokes problem and autonomous solutions to four open questions in the Erdős Conjectures database. Yet ne…

- **[MENTOR: Learning from Failure with On-Policy Pedagogical Intervention](https://arxiv.org/abs/2610.13594v1)**
  - *Guanlan Yue, Hang Yu, Xiaoyong Huang et al.*
  - `2026-10-09`
  - Reinforcement Learning from Verifiable Rewards (RLVR) is a key driver for Large Reasoning Models, but it is vulnerable to "zero-reward collapse", a training failure where a sudden increase in task difficulty causes the learning signal to vanish. We argue that the conventional app…

- **[MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures](https://arxiv.org/abs/2610.13534v1)**
  - *Loan Bernat, Matthieu Grard, Ariane Herbulot et al.*
  - `2026-10-09`
  - Long-horizon embodied agents must maintain task-relevant information, coordinate heterogeneous robots, and adapt their decisions as execution unfolds. Existing benchmarks investigate dynamic task execution and embodied multi-agent coordination, but provide limited evaluation of t…

- **[Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits](https://arxiv.org/abs/2610.13494v1)**
  - *Changye Li, Zijian Zhang, Muheng Li et al.*
  - `2026-10-09`
  - Existing LLM-based agent approaches for long-horizon machine learning engineering (MLE) often use context engineering, implemented through custom harnesses that manage tools, skills, and accumulated experience. However, we find that as single-session execution lengthens, the agen…

- **[Branching On-Policy Distillation](https://arxiv.org/abs/2610.13481v1)**
  - *Dongyang Chen, Shudong Liu, Shubo Li et al.*
  - `2026-10-09`
  - On-policy distillation (OPD) provides teacher supervision on student-generated trajectories, but a single trajectory realizes only one continuation at each decision, limiting supervision coverage under a finite sampling budget. We propose BranchOPD (Branching On-Policy Distillati…

- **[A Local Agentic AI Framework to Generate Edge Case Scenarios for Safety Assurance](https://arxiv.org/abs/2610.13479v1)**
  - *Victoria J. Hodge, Colin Paterson, Rob Alexander*
  - `2026-10-09`
  - Generating edge case scenarios is crucial for training, testing and safety assuring autonomous systems. This identifies hazardous failures to increase system reliability and robustness, ensures the system can still function safely on the boundaries of its operational design domai…

- **[SqueezeBench: Saturation-Resilient Evaluation of Mathematical Capability](https://arxiv.org/abs/2610.13461v1)**
  - *Pablo Manrique, Hai Xia, Stefan Szeider*
  - `2026-10-09`
  - AI systems are making rapid progress in mathematics, but this progress is hard to measure. Benchmarks of solved problems saturate, and in benchmarks of open problems each problem can be resolved for the first time only once. We present SqueezeBench, a benchmark that is resilient…

- **[Agentic Large Language Models](https://arxiv.org/abs/2610.13455v1)**
  - *Max van Duijn, Michiel van der Meer, Aske Plaat et al.*
  - `2026-10-09`
  - Large language models (LLMs) have taken the world by storm. Their ability to communicate with us in our own language, and to reason about our world, has made them a favorite tool for writing, answering questions, and much more. Their answers already influence our decisions and ou…

- **[Collective Autonomous Vehicle Routing Needs Social Awareness for Coexistence with Human Drivers](https://arxiv.org/abs/2610.13439v1)**
  - *Anastasia Psarou, Mikolaj Rams, Blazej Torbus et al.*
  - `2026-10-09`
  - Collective Autonomous Vehicle (AV) route choices in real-world traffic networks can create externalities for Human-Driven Vehicles (HDVs), as routes that benefit AVs may increase travel times for other road users. To address this, we introduce a social component, the marginal cos…

- **[Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits](https://arxiv.org/abs/2610.13438v1)**
  - *Chen Xi, Ding Ruixue, Wang Zhigaoyuan et al.*
  - `2026-10-09`
  - Reinforcement learning (RL) has emerged as a key paradigm for improving large language model (LLM) agents, enabling stronger reasoning, planning, and tool-use in interactive environments. However, existing agent RL methods remain fundamentally constrained by an on-policy reasonin…

- **[Web$hell: A Unified Interface for Agentic Web Access](https://arxiv.org/abs/2610.13416v1)**
  - *Sunghwan Kim, Deogyong Kim, Sangam Lee et al.*
  - `2026-10-09`
  - Large language model (LLM) agents are becoming direct users of the open web. As they take on increasingly complex and information-intensive tasks, effective web access is becoming a core capability for agentic problem solving. Existing approaches have advanced agentic web access…

- **[Masked Diffusion Language Agents for Tool-Integrated Chemical Reasoning](https://arxiv.org/abs/2610.13330v1)**
  - *Mengdi Liu, Chenghao Jia, Hong Chang et al.*
  - `2026-10-09`
  - Designing tool-integrated reasoning agent systems for complex chemical tasks remains a fundamental challenge. Although recent chemical agents have demonstrated promising performance through the integration of external tools, they are still built on the autoregressive paradigm, wh…

- **[PRIME: Pre-Retrieval Index Modeling Enhancement for Structured Document Retrieval-Real](https://arxiv.org/abs/2610.13296v1)**
  - *Cheuk Hei Chung, Li Liu*
  - `2026-10-09`
  - High-precision retrieval over external knowledge bases is essential for LLM agents to operate effectively. However, existing Information Retrieval (IR) research primarily optimizes query-side retrievers (e.g., ColBERT, BGE) and generators (e.g., Self-RAG, GraphRAG), while reducin…

- **[Agent4Spec: An LLM-based Agentic System to Optimize API Specifications through Automated Validation and Market Analysis](https://arxiv.org/abs/2610.13273v1)**
  - *Yongjian Tang, Costel Moraru, Doruk Tuncel et al.*
  - `2026-10-09`
  - API specifications serve as critical documentation for modern software development, directly impacting integration efficiency and client code generation. While recent advancements have leveraged Large Language Models (LLMs) to generate initial specifications from source code, exi…

- **[Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents](https://arxiv.org/abs/2610.13267v1)**
  - *Lei Liu, Yunji Liang, Xiaowen Zhang et al.*
  - `2026-10-09`
  - Large language model (LLM) agents are highly vulnerable to memory-poisoning attacks. Existing defenses primarily rely on external modules for either static memory isolation or continuous online auditing, resulting in low memory efficiency and high computational overhead. To addre…

- **[JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models](https://arxiv.org/abs/2610.13194v1)**
  - *Mengdi Liu, Chenghao Jia, Hong Chang et al.*
  - `2026-10-09`
  - Long-horizon autonomous research has shown promise in accelerating scientific progress through sustained cycles of hypothesis generation, implementation, and validation. However, this Generate-Execute-Feedback paradigm relies on reactive trial-and-error, where costly and time-con…

- **[RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions](https://arxiv.org/abs/2610.13172v1)**
  - *Boyuan Xiao, Pu Wang, Ji Feng et al.*
  - `2026-10-09`
  - World models enable large language model (LLM) agents to anticipate action effects and make informed decisions. For generalization, it is desirable for such world models to transfer efficiently to new environments with similar interaction structure and underlying dynamics. Recent…

- **[Quality, Not Just Outcome: A Structural Scoring Framework for Selecting Coding-Agent Trajectories for Supervised Fine-Tuning](https://arxiv.org/abs/2610.13152v1)**
  - *Sida Li, Yuanxin Liu, Shicheng Li et al.*
  - `2026-10-09`
  - Open coding agents are commonly trained through supervised fine-tuning on interaction trajectories whose final patches pass the benchmark test suite. However, this outcome-level filtering criterion ignores process quality: trajectories that eventually succeed may still contain in…

- **[Competence-Aware Orchestration for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2610.13144v1)**
  - *Songmiao Wang, Yuchen Wang, Chenglin Yu et al.*
  - `2026-10-09`
  - LLM-based multi-agent systems (MAS) have emerged as a promising paradigm for enhancing complex reasoning through role specialization and collaboration, yet a key challenge remains: how can collaboration be adapted to a backbone's competence on the current query? This problem matt…

- **[Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index for Open-Domain Multimodal Document QA](https://arxiv.org/abs/2610.13128v1)**
  - *Wenlin Lin, Fanzhe Wei*
  - `2026-10-09`
  - Question answering over large heterogeneous document collections requires first finding the right passages and then reading them, yet current retrieval-augmented agents give one model both kinds of tools and let it schedule itself. We present KnowForge, a pipeline separated by jo…

- **[DRYLAB-Bench: Benchmarking the Biosecurity Risk of Agentic LLM Mutation Design](https://arxiv.org/abs/2610.13116v1)**
  - *Yuzhen Wang, Chunxiao Li, Baichen Le et al.*
  - `2026-10-09`
  - As large language models (LLMs) acquire advanced biological design capabilities, they offer substantial research benefits but simultaneously introduce severe dual-use risks, such as engineering enhanced pathogens or drug-resistant bacteria. While biosecurity frameworks recognize…

- **[VETR: Execution-Grounded Self-Improving Agent for Symbolic Graphics Reasoning](https://arxiv.org/abs/2610.13098v1)**
  - *Yingbo Ma, Kuangshi Ai, Gordon Dai et al.*
  - `2026-10-09`
  - Visual agents for symbolic graphics reasoning depend on executable world representations, yet continued improvement remains bottlenecked by ambiguous supervision from final renders. Recent agentic systems refine scenes through repeated interaction, but they lack mechanisms to rec…

- **[When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows](https://arxiv.org/abs/2610.13092v1)**
  - *Yuchen Ling, Shengcheng Yu, Zhenyu Chen et al.*
  - `2026-10-09`
  - AI agents depend on repeated decisions to accomplish tasks, with large language models (LLMs) commonly serving as their core decision makers. The recent emergence of Jev offers an opportunity to make these decisions faster and at lower cost. However, it remains unclear whether su…

- **[LongHarness: Advancing Agentic Reasoning over 100M-Token Corpora via Stateful Evidence Management](https://arxiv.org/abs/2610.13075v1)**
  - *Songtao Huang, Zhijie Zhong, Xiaohan He et al.*
  - `2026-10-09`
  - Corpus-level long-context reasoning requires agents to acquire and integrate evidence across document collections that exceed their context windows. Existing agent harnesses enable incremental access to these corpora, but acquired evidence and evolving conclusions often remain en…

- **[Travel Back To Move Forward: Retrospective Exploration and Evolving for Long Horizon Agents](https://arxiv.org/abs/2610.13058v1)**
  - *Ziang Ye, Wentao Shi, Lei Chen et al.*
  - `2026-10-09`
  - Large language model agents increasingly operate in long-horizon environments where early mistakes can trigger cascading failures and trap agents in dead-end trajectories. Agents must therefore be able to proactively recover from such states and turn their exploratory experience…

- **[Don't Guess, Just Ask: Evaluating Interactive Requirement Clarification for Repository-Level Software Development](https://arxiv.org/abs/2610.13022v1)**
  - *Mingyu Chen, Zhiqing Zhong, Manyi Wang et al.*
  - `2026-10-09`
  - As LLMs become increasingly capable of implementing software, a critical bottleneck emerges: whether they truly understand what users want. Users often begin with vague intent, leaving important requirements to be clarified through interaction. In repository-level development, mi…

- **[Scaling Empowered Agents](https://arxiv.org/abs/2610.13002v1)**
  - *Catherine Ji, Vivek Myers, Joshua Lin et al.*
  - `2026-10-09`
  - Empowerment measures the capacity of an agent to actively control its environment. In this work, we explain the connection between skill learning and empowerment. While skill learning is not empowerment, we introduce a simple scalable recipe for empowerment maximization: empowerm…

- **[Hindsight Structured Advice Distillation: Steering Executor Agents with Advisors Trained on Their Failures and Task Characteristics](https://arxiv.org/abs/2610.13000v1)**
  - *O. Ozan Koyluoglu*
  - `2026-10-09`
  - Language-model agents are used for specialized work such as financial research, healthcare and law. Such agents are often capable enough for a task but still miss its details. In finance, for example, these details include which filing reports a figure or how a company discloses…

- **[SmartSalesBench: A Resistance-Aware Multi-Turn Benchmark for Evaluating LLM Sales Agents](https://arxiv.org/abs/2610.12975v1)**
  - *P N Bhargav Teja, Velpula Lokesh Reddy, Madhu Basumata et al.*
  - `2026-10-09`
  - We present SmartSalesBench, the first multi-turn conversational benchmark explicitly designed to evaluate large language model (LLM) sales agents against psychologically grounded, resistant buyer personas. Existing task-oriented dialogue benchmarks assume cooperative users and me…

- **[MotionCoach: Constructing Multimodal Guidance for Video Professional Motion Editing](https://arxiv.org/abs/2610.12963v1)**
  - *Siyi Qian, Hanqing Yang, Weihuang Lin et al.*
  - `2026-10-09`
  - Video editing models achieve strong performance in modifying appearance, backgrounds, styles, and motions, empowered by large-scale training data. Beyond general scenarios, professional motions are significant in performance, sports, and martial arts. This paper focuses on profes…

- **[JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents](https://arxiv.org/abs/2610.12957v1)**
  - *Gangyi Li, LuYao Wang, Jingfu Sun et al.*
  - `2026-10-09`
  - Embodied agents must translate multimodal observations and user requests into executable actions while adapting to product constraints, changing goals, and execution feedback. We present JoyInside-VLM-Agent, a ReAct-style multimodal agent developed through product-conditioned tra…

- **[Collaborative Learning and Reasoning over Model Slices](https://arxiv.org/abs/2610.12927v1)**
  - *Yuheng Wang, Runde Yang, Zhuohan Bao et al.*
  - `2026-10-09`
  - Large language models (LLMs) excel across diverse tasks, benefiting from knowledge priors, in-context reasoning, and test-time computation. Despite these strengths, single-model reasoning remains vulnerable to error propagation, as later steps depend on the model's earlier output…

- **[Co-Modifying Application Code and Deployment Infrastructure: A Causal Study of AI Agent Pull Requests](https://arxiv.org/abs/2610.12849v1)**
  - *Mohammad Wathiq Soualhi, Basem Suleiman*
  - `2026-10-09`
  - Current software engineering agents are evaluated predominantly inside isolated sandboxes against synchronous local tests. However, deploying features in collaborative repositories requires modifying continuous integration (CI/CD) pipelines, containers, and provisioning manifests…

- **[Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems](https://arxiv.org/abs/2610.12822v1)**
  - *Yuepeng Hu, Pegah Ghahremani, Reza Aghajani et al.*
  - `2026-10-09`
  - Multi-agent systems are increasingly used to solve coding tasks by coordinating agents that share code and plans. These agents are often optimized with reinforcement learning (RL) using automated evaluators, but bypassing evaluation can earn reward without producing a genuine sol…

- **[Returning to Development States: When Full Sandbox Snapshots Help Coding Agents](https://arxiv.org/abs/2610.13841v1)**
  - *Daniel Thi Graviet, Tanmay Shah*
  - `2026-10-09`
  - Coding agents often make useful progress before they fail, but retry-from-scratch discards the machine state created along the way. This makes failure recovery an interesting search problem: if intermediate environment states preserve meaningful progress, restoring and branching…

- **[Probabilistic Ship Trajectory Forecasting using Transformer Models on AIS Data](https://arxiv.org/abs/2610.13557v1)**
  - *Frederik E. T. Schöller*
  - `2026-10-09`
  - Anticipation of vessel trajectories is an essential task when navigating at sea. This applies to both human navigators and autonomous surface vessels. Trajectory forecasting enables sub-routines such as collision avoidance to assess the situation and react accordingly in time. Th…

- **[AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents](https://arxiv.org/abs/2610.13335v1)**
  - *R E Zera Marveen Lyngkhoi, Abhivansh Gupta, Vidushee Vats et al.*
  - `2026-10-09`
  - Tool-using agents increasingly require a common substrate for building, training, evaluating, distilling, and maintaining agentic systems, yet existing tooling typically addresses these stages in isolation. We present AgentTune, a source-available Python library that provides a u…

- **[Taking Tokenization off the Host for Agentic LLM Serving](https://arxiv.org/abs/2610.13325v1)**
  - *Mohammad Siavashi, Pascal Schwinte, Ali Banaei et al.*
  - `2026-10-09`
  - Agentic workloads resend long contexts that barely change between calls. Prefix caching now skips most of their prefill, yet every request must still be tokenized in full before the cache can even be consulted. Tokenization, a CPU stage long treated as negligible, becomes the lar…

- **[State-OPD: State-Grounded On-Policy Distillation for Multi-Turn Agents](https://arxiv.org/abs/2610.13238v1)**
  - *Zhentao Zhang, Yanzhao Zheng, Yanlin Liu et al.*
  - `2026-10-09`
  - On-Policy Distillation (OPD) has emerged as a powerful paradigm for transferring reasoning capabilities from frontier models to smaller models, while extending its success to multi-turn agentic environments remains challenging. We study agentic OPD through interaction states, dis…

- **[Can Failed Trajectories Reveal Where Agents Go Wrong? Agentic Failure Attribution Without Step-Level Labels](https://arxiv.org/abs/2610.13105v1)**
  - *Do Nguyen-Thanh, Junlin Fang, Bing Li et al.*
  - `2026-10-09`
  - Failure attribution for LLM agents aims to identify decisive steps responsible for task failure, which is critical for debugging and improving agentic systems. Existing methods rely on costly LLM prompting, step-level error annotations, or verified successful trajectories that la…

- **[CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits](https://arxiv.org/abs/2610.13064v1)**
  - *Jiahang Sun, Zhiwei Shang, Zhipiao Liu et al.*
  - `2026-10-09`
  - Large Language Model (LLM) agents have demonstrated remarkable capabilities in tackling complex tasks through agentic workflows. However, manually designing these workflows is labor-intensive and lacks flexibility to adapt to diverse queries. While automated workflow optimization…

- **[Personalized Federated Direct Preference Optimization via LoRA Adapters](https://arxiv.org/abs/2610.12885v1)**
  - *Zhanhong Jiang, Soumik Sarkar*
  - `2026-10-09`
  - Federated Direct Preference Optimization (FedDPO) enables privacy-preserving alignment of language models across distributed agents without centralizing sensitive preference data. However, existing FedDPO analysis assumes all clients converge to a single shared policy, which is f…

- **[TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents](https://arxiv.org/abs/2610.12828v1)**
  - *Debajoy Mukherjee, Jeremy Carleton, Sushil Vemuri et al.*
  - `2026-10-09`
  - Outcome-supervised group-relative policy optimization (GRPO) assigns the same advantage to every token in an LLM agent trajectory, leaving useful and unhelpful decisions undifferentiated. Hindsight credit assignment (HCA) can refine this feedback, but its estimates rely on trajec…

- **[APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces](https://arxiv.org/abs/2610.13623v1)**
  - *Ziyi Yang, Adel Bibi, Guohao Li et al.*
  - `2026-10-09`
  - Professional agents increasingly work through command-line interfaces and multiple tools over shared workspaces containing files, messages, and business applications. These environments create safety risks that are difficult to capture with attacks placed at a single, known read…

- **[Not All Correct Fixes Run Alike: An Empirical Study of Patch Performance in Repository-Level Issue Resolution](https://arxiv.org/abs/2610.13563v1)**
  - *Han Peng, Xing Hu, Feifei Niu et al.*
  - `2026-10-09`
  - Repository-level issue-resolution benchmarks such as SWE-bench evaluate submitted patches primarily based on whether they pass the correctness tests, leaving the runtime performance of different test-passing patches largely unexplored. Evaluating patch performance is essential bu…

- **[Proactive Agentic Orchestration](https://arxiv.org/abs/2610.13485v1)**
  - *Xueyang Feng, Chaozhuo Li, Xiaohe Bo et al.*
  - `2026-10-09`
  - Agentic orchestration delegates tasks to sub-agents with independent contexts, providing a key path to extending the effective execution horizon of large language model agents. However, existing orchestration methods face two limitations: in execution, current methods fix sub-age…

- **[SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents](https://arxiv.org/abs/2610.13157v1)**
  - *Shengze Huang, Zihao Tang, Jinluan Yang et al.*
  - `2026-10-09`
  - Reinforcement learning (RL) for search agents often suffers from evidence fabrication, a failure mode where agents bypass external information ($E_{ext}$) and fabricate an incorrect answer. We argue that this fabrication arises from an over-reliance on unreliable internal knowled…

- **[Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution](https://arxiv.org/abs/2610.13025v1)**
  - *Chejian Xu, Shujian Zhang, Wenxuan Zhou et al.*
  - `2026-10-09`
  - Self-evolving agents are increasingly used to improve language model systems without human intervention through either weight updates or harness improvements. Existing approaches typically pursue these directions separately: some methods update model weights using self-generated…

- **[SEEDS: Preview-Guided Evidence Admission for Search Agents](https://arxiv.org/abs/2610.12932v1)**
  - *Jiajin Liu, Chenxi Xu, Dongzhe Fan et al.*
  - `2026-10-09`
  - Search agents extend large reasoning models with multi-round access to external knowledge, yet most existing systems largely conflate retrieving evidence with consuming it. Retrieved documents are commonly incorporated according to fixed or rank-based policies, despite the fact t…

- **[Temporal Evidence Forests for Long-Horizon Multi-Party Conversational Memory](https://arxiv.org/abs/2610.12874v1)**
  - *Junyou Guo, Chongyang Tao, Yan He et al.*
  - `2026-10-09`
  - Long-term memory has been widely adopted in LLM-based agents to support persistent interaction and personalized assistance. Long-term multi-party interactions, however, accumulate substantially more detailed information, with decisions repeatedly updated and states evolving acros…

- **[When Charts Deceive Web Agents: A Paired Benchmark for Misleading Visualization-Grounded Tasks](https://arxiv.org/abs/2610.12823v1)**
  - *Yisheng Li, Dongming Han, Hongkun Pan et al.*
  - `2026-10-09`
  - Web agents increasingly browse, interpret, and act on web content on behalf of users. In many realistic workflows, however, the visual evidence they consume is not neutral: charts and dashboards can be misleading, shaping judgments without issuing any explicit malicious instructi…

- **[Ask Your Advisor: Learning When to Consult Stronger Models in Agentic Systems](https://arxiv.org/abs/2610.13870v1)**
  - *Pascal Sowietzki, Steffen Holter, Yannick Metz et al.*
  - `2026-10-09`
  - To balance task performance and computational cost, agentic workflows can use a lower-cost model for execution and selectively consult a stronger model. In such executor-advisor systems, the executor decides when to seek advice, making escalation depend on self-assessment, althou…

- **[MARGoS: A Configuration-Driven Platform for Reproducible MARL Experiments in ARGoS](https://arxiv.org/abs/2610.13772v1)**
  - *Tom Philipp Backert, Mohammad D. Soorati, Javad Ghofrani*
  - `2026-10-09`
  - Multi-agent reinforcement learning (MARL) has become a prominent research direction, particularly within collective robotics, where the ARGoS simulator is widely used to study emergent swarm behavior. Yet despite this growth, systematic support for reuse and reproducibility in MA…

- **[OpenSocialJax: Evaluating Social Adaptation in Sequential Social Dilemmas with Open-Ended Environmental Dynamics](https://arxiv.org/abs/2610.13710v1)**
  - *Zihao Guo, Meng Fang, Joel Z. Leibo et al.*
  - `2026-10-09`
  - Sequential social dilemma benchmarks capture diverse social interactions, but rarely test whether agents can infer hidden environmental rules through repeated interaction while adapting to other agents. We introduce \textbf{OpenSocialJax}, which extends Clean Up and Commons Harve…

- **[Limit-sure Winning in Team Games without Shared Randomness](https://arxiv.org/abs/2610.13569v1)**
  - *Léonard Brice, Thomas A. Henzinger, Alipasha Montaseri et al.*
  - `2026-10-09`
  - We study concurrent stochastic games in which a team of agents plays against an adversarial environment. If the agents could access a shared source of randomness, then these games reduce to two-player games. Despite being common in the literature on coalition games, this assumpti…

- **[The Limits of Manipulation within Personalized Incentive Policies](https://arxiv.org/abs/2610.13133v1)**
  - *Andrea Araldo, Alessa Mayer, Ravi Seshadri et al.*
  - `2026-10-09`
  - Demand management policies aim to shift individual behavior toward sustainable choices (e.g., goods, transport modes). Personalized incentive policies tailor subsidies to agents' needs and constraints, but personalization also exposes the regulator to agents' strategic manipulati…

- **[SwingGuard: Risk-Conditioned Multi-Agent Swing Trading with Dual-Timescale Governance](https://arxiv.org/abs/2610.12988v1)**
  - *Junzhou Su, Yichen Luo, Yebo Feng et al.*
  - `2026-10-09`
  - Cryptocurrency swing trading spans mismatched timescales: positions remain active while market and event risk can change within minutes. However, many predictive and large language model (LLM)-based trading systems assess risk after strategy generation or run both functions at th…

- **[OccludeBench: Can VLMs Find What's Missing?](https://arxiv.org/abs/2610.13790v1)**
  - *Jasin Cekinmez, Addison J. Wu, Ryo Mitsuhashi et al.*
  - `2026-10-09`
  - How well can vision-language models (VLMs) reason about what is missing from an image? We study this question with OccludeBench, a manually curated benchmark for recovering fully occluded objects from the visual evidence that remains. OccludeBench distinguishes direct cases, wher…


## Harness  (95)

### AAAI

- **[MCP-AgentBench: Evaluating Real-World Language Agent Performance with MCP-Mediated Tools](https://arxiv.org/abs/2509.09734)**
  - *Zikang Guo, Benfeng Xu, Chiwei Zhu et al.*
  - **AAAI 2025** · `2025-09-10`
  - The Model Context Protocol (MCP) is rapidly emerging as a pivotal open standard, designed to enhance agent-tool integration and interoperability, and is positioned to unlock a new era of powerful, interconnected, and genuinely utilitarian agentic AI. However, despite MCP's growin…

- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243)**
  - *Beiqi Chen, Shuai Shao, Haitang Feng et al.*
  - **AAAI 2025** · `2025-08-26`
  - We introduce Style4D-Bench, the first benchmark suite specifically designed for 4D stylization, with the goal of standardizing evaluation and facilitating progress in this emerging area. Style4D-Bench comprises: 1) a strong baseline that make an initial attempt for 4D stylization…


### NeurIPS

- **[DataClawBench: An Agent Benchmark for Exploratory Real-World Financial Data Analysis](https://openreview.net/forum?id=9RSvub7ht8)**
  - **NeurIPS 2025** · OpenReview · `2026-09-17`
  - Realistic analysis often begins without knowing where the relevant evidence lies, raising a fundamental question for autonomous data analysis: can agents discover and use the required evidence with limited human guidance? However, existing benchmarks typically evaluate such agent…


### ICML

- **[Harness Self-Evolution: Theory, Algorithms, Evaluation, Applications, and Impact](https://openreview.net/forum?id=m5jsFGXUM2)**
  - *Chuyang Wei, Haoxiang Guan, Minghang Zhu et al.*
  - **ICML 2025** · OpenReview · `2026-10-11`
  - Building agents that learn from experience is a central goal of artificial intelligence. Harness self-evolution offers a path toward this goal by revising an agent’s instructions, memory, workflows, and tools while model weights stay fixed. In this article, we develop a unified f…

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

- **[DS-Lighting: Making Agent Harnesses Explicit for Data-Science Automation](https://openreview.net/forum?id=k7K6gcD74M)**
  - **ICML 2025** · OpenReview · `2026-05-26`
  - Large Language Model (LLM) agents have shown promise for automating data-science workflows, yet their end-to-end performance depends critically on the agent harness that represents tasks, manages execution state, constrains output artifacts, and provides evaluation feedback. Exis…

- **[Reasoning Is More Than the Model: Harness-Aware Evaluation of Agents on Verifiable Reasoning Tasks](https://openreview.net/forum?id=fnHhEf0cSE)**
  - *Zhanke Zhou, Zongze Li, Weikai Huang et al.*
  - **ICML 2025** · OpenReview · `2026-05-14`
  - Open agents are no longer just models: they are model-harness systems whose behavior depends on tool access, control loops, execution feedback, memory, etc. Yet existing evaluations either test models without a harness or fix a single harness to compare models within a domain, ob…

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

- **[R-Bench: Graduate-level Multi-disciplinary Benchmarks for LLM & MLLM Complex Reasoning Evaluation](https://arxiv.org/abs/2505.02018)**
  - *Meng-Hao Guo, Jia-Jun Xu, Yi Zhang et al.*
  - **ICML 2025** · `2025-05-04`
  - Reasoning stands as a cornerstone of intelligence, enabling the synthesis of existing knowledge to solve complex problems. Despite remarkable progress, existing reasoning benchmarks often fail to rigorously evaluate the nuanced reasoning capabilities required for complex, real-wo…


### ICLR

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **ICLR 2026** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…


### CVPR

- **[Forensics-Bench: A Comprehensive Forgery Detection Benchmark Suite for Large Vision Language Models](https://arxiv.org/abs/2503.15024)**
  - *Jin Wang, Cheng-Hui Lv, Xian Li et al.*
  - **CVPR 2025** · `2025-03-19`
  - Recently, the rapid development of AIGC has significantly boosted the diversities of fake media spread in the Internet, posing unprecedented threats to social security, politics, law, and etc. To detect the ever-increasingly diverse malicious fake media in the new era of AIGC, re…


### KDD

- **[MultiTab: A Comprehensive Benchmark Suite for Multi-Dimensional Evaluation in Tabular Domains](https://arxiv.org/abs/2505.14312)**
  - *Kyungeun Lee, M. Eo, Hye-Seung Cho et al.*
  - **KDD 2025** · `2025-05-20`
  - Despite the widespread use of tabular data in real-world applications, most benchmarks rely on average-case metrics, which fail to reveal how model behavior varies across diverse data regimes. To address this, we propose MultiTab, a benchmark suite and evaluation framework for mu…


### ACL

- **[AfriSpeech-MultiBench: A Verticalized Multidomain Multicountry Benchmark Suite for African Accented English ASR](https://arxiv.org/abs/2511.14255)**
  - *Gabrial Zencha Ashungafac, M. Sanni, Busayo Awobade et al.*
  - **ACL 2025** · `2025-11-18`
  - Recent advances in speech-enabled AI, including Google's NotebookLM and OpenAI's speech-to-speech API, are driving widespread interest in voice interfaces globally. Despite this momentum, there exists no publicly available application-specific model evaluation that caters to Afri…

- **[SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073)**
  - *Zong-Hao Ying, Yang-Guang Shao, Jianle Gan et al.*
  - **ACL 2025** · `2025-10-11`
  - Large vision-language model (LVLM)-based web agents are emerging as powerful tools for automating complex online tasks. However, when deployed in real-world environments, they face serious security risks, motivating the design of security evaluation benchmarks. Existing benchmark…

- **[CiteEval: Principle-Driven Citation Evaluation for Source Attribution](https://arxiv.org/abs/2506.01829)**
  - *Yumo Xu, Peng Qi, Ji-Fan Chen et al.*
  - **ACL 2025** · `2025-06-02`
  - Citation quality is crucial in information-seeking systems, directly influencing trust and the effectiveness of information access. Current evaluation frameworks, both human and automatic, mainly rely on Natural Language Inference (NLI) to assess binary or ternary supportiveness…

- **[AutoMedEval: Harnessing Language Models for Automatic Medical Capability Evaluation](https://arxiv.org/abs/2505.11887)**
  - *Xiechi Zhang, Zetian Ouyang, Linlin Wang et al.*
  - **ACL 2025** · `2025-05-17`
  - With the proliferation of large language models (LLMs) in the medical domain, there is increasing demand for improved evaluation techniques to assess their capabilities. However, traditional metrics like F1 and ROUGE, which rely on token overlaps to measure quality, significantly…

- **[ChartEdit: How Far Are MLLMs From Automating Chart Analysis? Evaluating MLLMs' Capability via Chart Editing](https://arxiv.org/abs/2505.11935)**
  - *Xuanle Zhao, Xue-Xin Liu, Haoyue Yang et al.*
  - **ACL 2025** · `2025-05-17`
  - Although multimodal large language models (MLLMs) show promise in generating chart rendering code, editing charts via code presents a greater challenge. This task demands MLLMs to integrate chart understanding and reasoning capacities, which are labor-intensive. While many MLLMs…

- **[Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models](https://arxiv.org/abs/2505.02847)**
  - *Bang Zhang, Ruotian Ma, Qingxuan Jiang et al.*
  - **ACL 2025** · `2025-05-01`
  - Assessing how well a large language model (LLM) understands human, rather than merely text, remains an open challenge. To bridge the gap, we introduce Sentient Agent as a Judge (SAGE), an automated evaluation framework that measures an LLM's higher-order social cognition. SAGE in…

- **[NorEval: A Norwegian Language Understanding and Generation Evaluation Benchmark](https://arxiv.org/abs/2504.07749)**
  - *Vladislav Mikhailov, T. Enstad, David Samuel et al.*
  - **ACL 2025** · `2025-04-10`
  - This paper introduces NorEval, a new and comprehensive evaluation suite for large-scale standardized benchmarking of Norwegian generative language models (LMs). NorEval consists of 24 high-quality human-created datasets -- of which five are created from scratch. In contrast to ex…

- **[SEA-HELM: Southeast Asian Holistic Evaluation of Language Models](https://arxiv.org/abs/2502.14301)**
  - *Yosephine Susanto, Adithya Venkatadri Hulagadri, J. Montalan et al.*
  - **ACL 2025** · `2025-02-20`
  - With the rapid emergence of novel capabilities in Large Language Models (LLMs), the need for rigorous multilingual and multicultural benchmarks that are integrated has become more pronounced. Though existing LLM benchmarks are capable of evaluating specific capabilities of LLMs i…

- **[MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs](https://arxiv.org/abs/2501.17399)**
  - *Ved Sirdeshmukh, Kaustubh Deshpande, Johannes Mols et al.*
  - **ACL 2025** · `2025-01-29`
  - We present MultiChallenge, a pioneering benchmark evaluating large language models (LLMs) on conducting multi-turn conversations with human users, a crucial yet underexamined capability for their applications. MultiChallenge identifies four categories of challenges in multi-turn…


### EMNLP

- **[CompassVerifier: A Unified and Robust Verifier for LLMs Evaluation and Outcome Reward](https://arxiv.org/abs/2508.03686)**
  - *Shudong Liu, Hongwei Liu, Jun-Nan Liu et al.*
  - **EMNLP 2025** · `2025-08-05`
  - Answer verification is crucial not only for evaluating large language models (LLMs) by matching their unstructured outputs against standard answers, but also serves as the reward model to guide LLM optimization. Most evaluation frameworks rely on regularized matching or employ ge…

- **[From KMMLU-Redux to Pro: A Professional Korean Benchmark Suite for LLM Evaluation](https://arxiv.org/abs/2507.08924)**
  - *Seokhee Hong, SunKyoung Kim, Guijin Son et al.*
  - **EMNLP 2025** · `2025-07-11`
  - The development of Large Language Models (LLMs) requires robust benchmarks that encompass not only academic domains but also industrial fields to effectively evaluate their applicability in real-world scenarios. In this paper, we introduce two Korean expert-level benchmarks. KMML…

- **[Automated Creativity Evaluation for Large Language Models: A Reference-Based Approach](https://arxiv.org/abs/2504.15784)**
  - *Ruizhe Li, Chiwei Zhu, Benfeng Xu et al.*
  - **EMNLP 2025** · `2025-04-22`
  - Creative writing is a key capability of Large Language Models (LLMs), with potential applications in literature, storytelling, and various creative domains. However, evaluating the creativity of machine-generated texts remains a significant challenge, as existing methods either r…

- **[BenchMAX: A Comprehensive Multilingual Evaluation Suite for Large Language Models](https://arxiv.org/abs/2502.07346)**
  - *Xu Huang, Wenhao Zhu, Hanxu Hu et al.*
  - **EMNLP 2025** · `2025-02-11`
  - Previous multilingual benchmarks focus primarily on simple understanding tasks, but for large language models(LLMs), we emphasize proficiency in instruction following, reasoning, long context understanding, code generation, and so on. However, measuring these advanced capabilitie…

- **[AraEval: An Arabic Multi-Task Evaluation Suite for Large Language Models](https://aclanthology.org/2025.emnlp-main.1679.pdf)**
  - *A. Althnian, Norah A. Alzahrani, Shaykhah Z. Alsubaie et al.*
  - **EMNLP 2025**
  - ,


### NAACL

- **[Automatic Evaluation of Healthcare LLMs Beyond Question-Answering](https://arxiv.org/abs/2502.06666)**
  - *Anna Arias-Duart, P. A. Martin-Torres, Daniel Hinjos et al.*
  - **NAACL 2025** · `2025-02-10`
  - Current Large Language Models (LLMs) benchmarks are often based on open-ended or close-ended QA evaluations, avoiding the requirement of human labor. Close-ended measurements evaluate the factuality of responses but lack expressiveness. Open-ended capture the model's capacity to…


### Other / arXiv

- **[EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents](https://arxiv.org/abs/2610.13021)**
  - *Jie Huang, Yanan Chen, Ruixun Liu et al.*
  - 🤗 Featured · `2026-10-09`
  - Continual learning requires models to accumulate past experience and transfer it to new tasks. Despite substantial research on continual learning, existing work remains largely confined to non-embodied settings, without extending to embodied environments. To address this gap, we…

- **[AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation and Error Diagnosis](https://arxiv.org/abs/2610.13627)**
  - *Natapong Nitarach, Phume Ngampornsukswadi, Pittawat Taveekitworachai et al.*
  - 🤗 Featured · `2026-10-09`

- **[Recurrent Harness for Agentic Continual Learning](https://arxiv.org/abs/2610.12668)**
  - *Yuxin Xiao, Zhiyun Lu, Jianyu Wang et al.*
  - 🤗 Featured · `2026-10-08`

- **[Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution](https://arxiv.org/abs/2609.37950)**
  - *Bingjun Luo, Jialin Guo, Siqi Li*
  - 🤗 Featured · `2026-09-29`

- **[AgentSWE: Can Coding Agents Build the Agent You Actually Want?](https://arxiv.org/abs/2610.13361)**
  - *Jiahao Wang, Hongjin Qian, Yuyang Hu et al.*
  - 🤗 · `2026-10-09`
  - As the production of software passes into the hands of software itself, coding agents are increasingly commissioned to build agents fitted to their users' own workflows. This delegation carries a quiet assumption, that the delivered agent will faithfully serve the requirement it…

- **[RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](https://arxiv.org/abs/2610.13889v1)**
  - *Weiliang Chen, Song Liao*
  - `2026-10-09`
  - As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via…

- **[Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits](https://arxiv.org/abs/2610.13494v1)**
  - *Changye Li, Zijian Zhang, Muheng Li et al.*
  - `2026-10-09`
  - Existing LLM-based agent approaches for long-horizon machine learning engineering (MLE) often use context engineering, implemented through custom harnesses that manage tools, skills, and accumulated experience. However, we find that as single-session execution lengthens, the agen…

- **[LongHarness: Advancing Agentic Reasoning over 100M-Token Corpora via Stateful Evidence Management](https://arxiv.org/abs/2610.13075v1)**
  - *Songtao Huang, Zhijie Zhong, Xiaohan He et al.*
  - `2026-10-09`
  - Corpus-level long-context reasoning requires agents to acquire and integrate evidence across document collections that exceed their context windows. Existing agent harnesses enable incremental access to these corpora, but acquired evidence and evolving conclusions often remain en…

- **[Don't Guess, Just Ask: Evaluating Interactive Requirement Clarification for Repository-Level Software Development](https://arxiv.org/abs/2610.13022v1)**
  - *Mingyu Chen, Zhiqing Zhong, Manyi Wang et al.*
  - `2026-10-09`
  - As LLMs become increasingly capable of implementing software, a critical bottleneck emerges: whether they truly understand what users want. Users often begin with vague intent, leaving important requirements to be clarified through interaction. In repository-level development, mi…

- **[Proactive Agentic Orchestration](https://arxiv.org/abs/2610.13485v1)**
  - *Xueyang Feng, Chaozhuo Li, Xiaohe Bo et al.*
  - `2026-10-09`
  - Agentic orchestration delegates tasks to sub-agents with independent contexts, providing a key path to extending the effective execution horizon of large language model agents. However, existing orchestration methods face two limitations: in execution, current methods fix sub-age…

- **[Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution](https://arxiv.org/abs/2610.13025v1)**
  - *Chejian Xu, Shujian Zhang, Wenxuan Zhou et al.*
  - `2026-10-09`
  - Self-evolving agents are increasingly used to improve language model systems without human intervention through either weight updates or harness improvements. Existing approaches typically pursue these directions separately: some methods update model weights using self-generated…

- **[Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing](https://arxiv.org/abs/2610.13823v1)**
  - *Oktie Hassanzadeh, Dharmashankar Subramanian*
  - `2026-10-09`
  - Semantic query engines ask a large language model (LLM) to judge individual rows, and benchmarks compare these engines on the quality of a few executions at temperature 0. We measure how much another execution changes. We re-execute the text and tabular workloads of SemBench, LRO…

- **[RegulaTutor: A Theory-Informed Framework for Long-Term Personalized Learning](https://arxiv.org/abs/2610.13399v1)**
  - *Yonggang Li, Boqian Han, Rui Sheng et al.*
  - `2026-10-09`
  - Long-term personalized tutoring requires language models to translate a learner's evolving history into appropriate instructional support. Existing LLM-based tutoring systems use memory and retrieval to personalize responses, but the pedagogical rationale linking historical evide…

- **[BLiMPPI: Benchmark of Linguistic Minimal Pairs for Polarity Items](https://arxiv.org/abs/2610.13607v1)**
  - *Arzu Burcu Güven, Anna Rogers, Leonie Weissweiler et al.*
  - `2026-10-09`
  - Negative polarity items (NPIs), such as "anymore" and "ever", are grammatical only in select environments, predominantly in the context of negation. Because their grammaticality depends on both syntax and semantics, they have a rich, multilingual literature in theoretical linguis…


## Finance  (137)

### AAAI

- **[DMT-RoleBench: A Dynamic Multi-Turn Dialogue Based Benchmark for Role-Playing Evaluation of Large Language Model and Agent](https://ojs.aaai.org/index.php/AAAI/article/download/34768/36923)**
  - *Ding-Bo Yuan, Yi-Peng Chen, Guo-Dong Liu et al.*
  - **AAAI 2025** · `2025-04-11`
  - Recent years have witnessed a profound evolution in the abilities of Large Language Model, which has significantly boosted the proliferation of role-playing agents and platforms.
Nonetheless, there is a conspicuous absence of systematic and comprehensive evaluations of role-playi…

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

- **[DataClawBench: An Agent Benchmark for Exploratory Real-World Financial Data Analysis](https://openreview.net/forum?id=9RSvub7ht8)**
  - **NeurIPS 2025** · OpenReview · `2026-09-17`
  - Realistic analysis often begins without knowing where the relevant evidence lies, raising a fundamental question for autonomous data analysis: can agents discover and use the required evidence with limited human guidance? However, existing benchmarks typically evaluate such agent…

- **[Self-Challenging Language Model Agents](https://arxiv.org/abs/2506.01716)**
  - *Yifei Zhou, Sergey Levine, Jason E. Weston et al.*
  - **NeurIPS 2025** · `2025-06-02`
  - Large language models are quickly becoming the foundation for intelligent agents that are capable of using tools. However, training such agents is challenging because it requires human creation and annotation of a diverse set of tasks, tools, and evaluation criteria. In this pape…


### ICML

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

- **[DS-Lighting: Making Agent Harnesses Explicit for Data-Science Automation](https://openreview.net/forum?id=k7K6gcD74M)**
  - **ICML 2025** · OpenReview · `2026-05-26`
  - Large Language Model (LLM) agents have shown promise for automating data-science workflows, yet their end-to-end performance depends critically on the agent harness that represents tasks, manages execution state, constrains output artifacts, and provides evaluation feedback. Exis…

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


### ACL

- **[SWE-Critix: Post-Training Generalist Verifiers for Assessing Coding-Agent Trajectories](https://arxiv.org/abs/2610.13356)**
  - *Jiajun Hu, Chun Yong Chong*
  - **ACL** · 🤗 · `2026-10-09`
  - Coding agents are increasingly deployed for end-to-end software engineering tasks, where a readily available oracle evaluator that defines the success criteria is often absent. This motivates verifications for coding agents that can reliably judge and explain their behavior. Howe…

- **[Partially Informed Stochastic Optimization via Zeroth-Order Residual Tracking](https://arxiv.org/abs/2610.13871v1)**
  - *El Mahdi Chayti, Alireza Mirrokni, Martin Jaggi*
  - **ACL** · `2026-10-09`
  - Many optimization problems provide direct access to only part of the gradient, while the remaining component must be inferred from function evaluations. This structure arises in performative prediction, performative reinforcement learning, and bilevel optimization with a black-bo…

- **[DataCupid: Stable Matching Repair for Training Data Acquisition with Delayed Feedback](https://arxiv.org/abs/2610.12960v1)**
  - *He Sun, Junyuan Mao, Wenhao Jiang et al.*
  - **ACL** · `2026-10-09`
  - Matching repair after utility changes can reuse valid observations, but new evaluations must respect matching capacity and may return out of order. We study announced invalidations with bounded, possibly reward-dependent reporting delays and pending evaluations that do not occupy…

- **[MLP-Initialized Reinforcement Learning for Exit Timing in SPX Short-Straddle Portfolios](https://arxiv.org/abs/2610.13126v1)**
  - *Jianning Wang, Robert Ślepaczuk, Paweł Sakowski*
  - **ACL** · `2026-10-09`
  - This paper studies exit timing for SPX short-straddle portfolios using a two-stage supervised and reinforcement-learning framework. Historical episodes first generate ex-post optimal hold/exit labels for training a multilayer perceptron (MLP) using only contemporaneously availabl…

- **[AfriSpeech-MultiBench: A Verticalized Multidomain Multicountry Benchmark Suite for African Accented English ASR](https://arxiv.org/abs/2511.14255)**
  - *Gabrial Zencha Ashungafac, M. Sanni, Busayo Awobade et al.*
  - **ACL 2025** · `2025-11-18`
  - Recent advances in speech-enabled AI, including Google's NotebookLM and OpenAI's speech-to-speech API, are driving widespread interest in voice interfaces globally. Despite this momentum, there exists no publicly available application-specific model evaluation that caters to Afri…

- **[SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073)**
  - *Zong-Hao Ying, Yang-Guang Shao, Jianle Gan et al.*
  - **ACL 2025** · `2025-10-11`
  - Large vision-language model (LVLM)-based web agents are emerging as powerful tools for automating complex online tasks. However, when deployed in real-world environments, they face serious security risks, motivating the design of security evaluation benchmarks. Existing benchmark…

- **[FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation](https://arxiv.org/abs/2505.24714)**
  - *Junyu Luo, Zhizhuo Kou, Liming Yang et al.*
  - **ACL 2025** · `2025-05-30`
  - Multimodal Large Language Models (MLLMs) have experienced rapid development in recent years. However, in the financial domain, there is a notable lack of effective and specialized multimodal evaluation datasets. To advance the development of MLLMs in the finance domain, we introd…


### EMNLP

- **[Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://arxiv.org/abs/2503.02519)**
  - *Xingzuo Li, Ke-Hai Chen, Yunfei Long et al.*
  - **EMNLP 2025** · `2025-03-04`
  - Large language model (LLM) agents typically adopt a step-by-step reasoning framework, in which they interleave the processes of thinking and acting to accomplish the given task. However, this paradigm faces a deep-rooted one-pass issue whereby each generated intermediate thought…


### Other / arXiv

- **[AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation and Error Diagnosis](https://arxiv.org/abs/2610.13627)**
  - *Natapong Nitarach, Phume Ngampornsukswadi, Pittawat Taveekitworachai et al.*
  - 🤗 Featured · `2026-10-09`

- **[SelectArena: A Modern Benchmark for Feature Selection on Real-world Tabular Data](https://arxiv.org/abs/2610.13644)**
  - *Bastian Schäfer, Dominika Matus, Lennart Purucker et al.*
  - 🤗 · `2026-10-09`
  - Selecting a subset of features (columns) from a tabular dataset is a ubiquitous challenge in real-world applications. Industry experts seek to minimize model training costs, climate scientists require an interpretable subset of factors to understand extreme weather events, and cl…

- **[MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents](https://arxiv.org/abs/2610.13829v1)**
  - *Jingwei Song, Zhisheng Chen, Bingfan Zeng et al.*
  - `2026-10-09`
  - A central challenge in embodied recursive self-improvement is enabling agents to convert interaction history into capabilities that persist beyond one world and transfer to later tasks. A saved memory or successful final action does not by itself establish that a reusable capabil…

- **[Matched-Context Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2610.13755v1)**
  - *Chenxu Zhang, Yaorui Shi, Wenlong Zhang et al.*
  - `2026-10-09`
  - Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enter…

- **[MENTOR: Learning from Failure with On-Policy Pedagogical Intervention](https://arxiv.org/abs/2610.13594v1)**
  - *Guanlan Yue, Hang Yu, Xiaoyong Huang et al.*
  - `2026-10-09`
  - Reinforcement Learning from Verifiable Rewards (RLVR) is a key driver for Large Reasoning Models, but it is vulnerable to "zero-reward collapse", a training failure where a sudden increase in task difficulty causes the learning signal to vanish. We argue that the conventional app…

- **[Web$hell: A Unified Interface for Agentic Web Access](https://arxiv.org/abs/2610.13416v1)**
  - *Sunghwan Kim, Deogyong Kim, Sangam Lee et al.*
  - `2026-10-09`
  - Large language model (LLM) agents are becoming direct users of the open web. As they take on increasingly complex and information-intensive tasks, effective web access is becoming a core capability for agentic problem solving. Existing approaches have advanced agentic web access…

- **[RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions](https://arxiv.org/abs/2610.13172v1)**
  - *Boyuan Xiao, Pu Wang, Ji Feng et al.*
  - `2026-10-09`
  - World models enable large language model (LLM) agents to anticipate action effects and make informed decisions. For generalization, it is desirable for such world models to transfer efficiently to new environments with similar interaction structure and underlying dynamics. Recent…

- **[Hindsight Structured Advice Distillation: Steering Executor Agents with Advisors Trained on Their Failures and Task Characteristics](https://arxiv.org/abs/2610.13000v1)**
  - *O. Ozan Koyluoglu*
  - `2026-10-09`
  - Language-model agents are used for specialized work such as financial research, healthcare and law. Such agents are often capable enough for a task but still miss its details. In finance, for example, these details include which filing reports a figure or how a company discloses…

- **[APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces](https://arxiv.org/abs/2610.13623v1)**
  - *Ziyi Yang, Adel Bibi, Guohao Li et al.*
  - `2026-10-09`
  - Professional agents increasingly work through command-line interfaces and multiple tools over shared workspaces containing files, messages, and business applications. These environments create safety risks that are difficult to capture with attacks placed at a single, known read…

- **[Proactive Agentic Orchestration](https://arxiv.org/abs/2610.13485v1)**
  - *Xueyang Feng, Chaozhuo Li, Xiaohe Bo et al.*
  - `2026-10-09`
  - Agentic orchestration delegates tasks to sub-agents with independent contexts, providing a key path to extending the effective execution horizon of large language model agents. However, existing orchestration methods face two limitations: in execution, current methods fix sub-age…

- **[Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution](https://arxiv.org/abs/2610.13025v1)**
  - *Chejian Xu, Shujian Zhang, Wenxuan Zhou et al.*
  - `2026-10-09`
  - Self-evolving agents are increasingly used to improve language model systems without human intervention through either weight updates or harness improvements. Existing approaches typically pursue these directions separately: some methods update model weights using self-generated…

- **[MARGoS: A Configuration-Driven Platform for Reproducible MARL Experiments in ARGoS](https://arxiv.org/abs/2610.13772v1)**
  - *Tom Philipp Backert, Mohammad D. Soorati, Javad Ghofrani*
  - `2026-10-09`
  - Multi-agent reinforcement learning (MARL) has become a prominent research direction, particularly within collective robotics, where the ARGoS simulator is widely used to study emergent swarm behavior. Yet despite this growth, systematic support for reuse and reproducibility in MA…

- **[SwingGuard: Risk-Conditioned Multi-Agent Swing Trading with Dual-Timescale Governance](https://arxiv.org/abs/2610.12988v1)**
  - *Junzhou Su, Yichen Luo, Yebo Feng et al.*
  - `2026-10-09`
  - Cryptocurrency swing trading spans mismatched timescales: positions remain active while market and event risk can change within minutes. However, many predictive and large language model (LLM)-based trading systems assess risk after strategy generation or run both functions at th…

- **[DeFiRank: Federated Pairwise Ranking for Governance in Decentralized Financial Networks](https://arxiv.org/abs/2610.12916v1)**
  - *Zahra Batool, Michael Duchesne, Kaiwen Zhang et al.*
  - `2026-10-09`
  - Existing governance approaches in decentralized financial networks rely on manual review processes conducted by human committees, which introduces subjective bias, creates a scalability bottleneck under high network volume, and fails to capture complex behavioural patterns and ev…

- **[Machine Unlearning for Federated Socially Fair k-Means Clustering](https://arxiv.org/abs/2610.13717v1)**
  - *Aravind Reddy, Deeraj S K, Mohd Wasif Raza et al.*
  - `2026-10-09`
  - Federated clustering can support applications such as patient stratification across hospitals and customer segmentation across distributed financial datasets. Responsible AI calls for fair representation of demographic groups and support for data deletion, motivated in part by ri…

- **[CorrFlow: Exact and Permutation-Equivariant Flow Matching on the Correlation Elliptope](https://arxiv.org/abs/2610.13606v1)**
  - *Gautier Marti*
  - `2026-10-09`
  - Correlation matrices combine nonlinear positive-definiteness constraints with a simultaneous row-column permutation symmetry. Their generation therefore involves two distinct problems. First, every output must remain on the correlation elliptope, irrespective of how its variables…

- **[$L_0$ Feature Selection via Monte Carlo Tree Search in High-Dimensional Financial Regression](https://arxiv.org/abs/2610.13574v1)**
  - *Cameron Mouangue, Tristan Cazenave*
  - `2026-10-09`
  - Feature selection is a central problem in high-dimensional financial regression, where large numbers of engineered variables and strong correlations among predictors reduce model stability and interpretability. $L_1$ regularization (Lasso) is widely used for sparse regression, bu…

- **[Does Financial Speech Need Continual Learning Regularization? A Study of EWC and mini-KFAC on Earnings Call ASR](https://arxiv.org/abs/2610.13432v1)**
  - *Thai Quoc On, Homayoon Beigi*
  - `2026-10-09`
  - Earnings call transcription presents a realistic continual learning scenario where Automatic Speech Recognition (ASR) systems are updated with new recordings but risk catastrophic forgetting of previously learned financial speech patterns. Adapting Whisper-small from a general-do…

- **[Enhancing credit risk scorecards with transactional-based behavioural features](https://arxiv.org/abs/2610.13199v1)**
  - *Dian Prinsloo, Tanja Verster, Neill Smit*
  - `2026-10-09`
  - Background: Credit risk modelling is fundamental in financial institutions, typically using credit history, repayment behaviour, income, and outstanding debt to estimate a borrower's probability of default. Although transactional data are sometimes incorporated through aggregated…

- **[Scalable Learning of Determinantal Point Processes with Kernel-Structured Interactions](https://arxiv.org/abs/2610.12829v1)**
  - *Takahiro Kawashima, Hideitsu Hino*
  - `2026-10-09`
  - Determinantal point processes (DPPs) on a finite set are probability models that exhibit repulsion where inter-item similarities are encoded by a positive definite kernel matrix. Scaling DPP learning to large datasets typically requires imposing structural constraints on the kern…

- **[FOMO: FLEX Options and Market Outcomes](https://arxiv.org/abs/2610.13044v1)**
  - *Shivesh Prakash, Frank Ferstler, Nicholas Pezolano*
  - `2026-10-09`
  - FLEX options are customized exchange-traded contracts allowing participants to choose nonstandard strikes, expirations, exercise styles, and settlement terms while retaining central clearing. We investigate whether single-name FLEX activity leaves measurable footprints in regular…

- **[Entropy Regularization under No-Shorting: Structure Preservation and Convexity in Dynamic Mean-Variance Portfolio Selection](https://arxiv.org/abs/2610.13162v1)**
  - *Xinagyu Cui, Xun Li, Ziyan Li et al.*
  - `2026-10-09`
  - This paper studies entropy regularization for the discrete-time dynamic mean--variance portfolio problem with no-shorting constraints. In the unconstrained setting, entropy regularization can be introduced without changing the basic quadratic structure of the dynamic program. Und…


---
*Generated 2026-10-12 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
