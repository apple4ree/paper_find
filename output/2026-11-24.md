# Daily Paper Digest — 2026-11-24 (Tuesday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**455 unique papers** (574 topic-entries — cross-topic papers counted once per category)

---

## Agent  (308)

### AAAI

- **[AutoTool: Efficient Tool Selection for Large Language Model Agents](https://arxiv.org/abs/2511.14650)**
  - *Jin Jia, Qin-Bin Li*
  - **AAAI 2025** · `2025-11-18`
  - Large Language Model (LLM) agents have emerged as powerful tools for automating complex tasks by leveraging the reasoning and decision-making abilities of LLMs. However, a major bottleneck in current agent frameworks lies in the high inference cost of tool selection, especially i…

- **[Beyond ReAct: A Planner-Centric Framework for Complex Tool-Augmented LLM Reasoning](https://arxiv.org/abs/2511.10037)**
  - *Xiao-Long Wei, Yuehu Dong, Xing-Liang Wang et al.*
  - **AAAI 2025** · `2025-11-13`
  - Existing tool-augmented large language models (LLMs) encounter significant challenges when processing complex queries. Current frameworks such as ReAct are prone to local optimization traps due to their reliance on incremental decision-making processes. To address these limitatio…

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

- **[CO-Bench: Benchmarking Language Model Agents in Algorithm Search for Combinatorial Optimization](https://arxiv.org/abs/2504.04310)**
  - *Wei-Wei Sun, Sheng-Yu Feng, Shan-Da Li et al.*
  - **AAAI 2025** · `2025-04-06`
  - Although LLM-based agents have attracted significant attention in domains such as software engineering and machine learning research, their role in advancing combinatorial optimization (CO) remains relatively underexplored. 
This gap underscores the need for a deeper understandin…


### NeurIPS

- **[SYMPHONY: Synergistic Multi-agent Planning with Heterogeneous Language Model Assembly](https://arxiv.org/abs/2601.22623)**
  - *Wei Zhu, Zhi-Wen Tang, Kun Yue*
  - **NeurIPS 2026** · `2026-01-30`
  - Recent advancements have increasingly focused on leveraging large language models (LLMs) to construct autonomous agents for complex problem-solving tasks. However, existing approaches predominantly employ a single-agent framework to generate search branches and estimate rewards d…

- **[AgentTTS: Large Language Model Agent for Test-time Compute-optimal Scaling Strategy in Complex Tasks](https://arxiv.org/abs/2508.00890)**
  - *Fali Wang, Hui Liu, Zhen-Wei Dai et al.*
  - **NeurIPS 2025** · `2025-07-26`
  - Test-time scaling (TTS) enhances the performance of large language models (LLMs) by allocating additional compute resources during inference. However, existing research primarily investigates TTS in single-stage tasks; while many real-world problems are multi-stage complex tasks,…

- **[Self-Challenging Language Model Agents](https://arxiv.org/abs/2506.01716)**
  - *Yifei Zhou, S. Levine, Jason E. Weston et al.*
  - **NeurIPS 2025** · `2025-06-02`
  - Large language models are quickly becoming the foundation for intelligent agents that are capable of using tools. However, training such agents is challenging because it requires human creation and annotation of a diverse set of tasks, tools, and evaluation criteria. In this pape…

- **[Code Graph Model (CGM): A Graph-Integrated Large Language Model for Repository-Level Software Engineering Tasks](https://arxiv.org/abs/2505.16901)**
  - *Hong-Yuan Tao, Ying Zhang, Zhenhao Tang et al.*
  - **NeurIPS 2025** · `2025-05-22`
  - Recent advances in Large Language Models (LLMs) have shown promise in function-level code generation, yet repository-level software engineering tasks remain challenging. Current solutions predominantly rely on proprietary LLM agents, which introduce unpredictability and limit acc…


### ICML

- **[Hybrid Financial Analysis Agent with RAG and Text Mining](https://openreview.net/forum?id=jGe6fFmsDg)**
  - *{'fullname': 'Bingzhang Wang', 'username': 'https://orcid.org/orcid-search/search?searchQuery=Bingzhang%20Wang'}, {'fullname': 'Keyi Zhang', 'username': 'https://orcid.org/orcid-search/search?searchQuery=Keyi%20Zhang'}, {'fullname': 'Tianhao Du', 'username': 'https://orcid.org/orcid-search/search?searchQuery=Tianhao%20Du'} et al.*
  - **ICML 2025** · OpenReview · `2026-10-28`
  - This paper presents a hybrid financial analysis agent that integrates retrieval-augmented generation, financial text mining, live market-data access, and a news sentiment classifier within a LangGraph-based orchestration framework. The system is designed to reduce information ove…

- **[TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration](https://openreview.net/forum?id=bz651zjpyk)**
  - **ICML 2025** · OpenReview · `2026-10-13`
  - LLM-based agents can automate model post-training, accelerating progress toward recursive self-improvement. Despite their promise, existing approaches remain under-explored and face two main challenges: (1) strategy lock-in that limits exploration beyond the initial strategy; and…

- **[ARTE: Agentic Refinement through Trade Execution for High-Frequency Trading Strategy Discovery](https://openreview.net/forum?id=VisvXioWmG)**
  - **ICML 2025** · OpenReview · `2026-10-12`
  - Existing LLM-based trading strategy development primarily uses aggregated price and volume data, which omit within-interval event order and displayed order book changes. Tick-level trade and quote observations preserve this information, but their scale makes the full history impr…

- **[TradingArena: A Market-Making Benchmark for Ranking, Diagnosing, and Steering LLM Behavior](https://openreview.net/forum?id=6VObvVwaGZ)**
  - **ICML 2025** · OpenReview · `2026-09-19`
  - As large language models are increasingly deployed as agents, evaluation should capture both task performance and interactive behavior. Few benchmarks jointly measure performance and behavior under controlled changes to an agent’s information, action space, and inference. We intr…

- **[Can Harness Optimization Improve Agents? Generalizable Gains Versus Evaluation Noise](https://openreview.net/forum?id=Ri0rU3rPOS)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Harness optimization methods revise an agent’s prompts, tools, memory, and run-
time control without updating model weights. We ask which of their improve-
ments can be distinguished from evaluation noise, and where the reliable ones
come from. We evaluate Meta-Harness, Agentic H…

- **[AURA-Eval: Evaluation Framework for Acting Under Risk Awareness in LLM Agent Trajectories](https://openreview.net/forum?id=9XfH1iAA4W)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - LLM agents are increasingly taking actions with real consequences, yet safety evaluations often reduce their behavior to a final safe or unsafe outcome, obscuring whether the agent recognized the risk and how it responded. We introduce AURA-Eval, a framework for evaluating whethe…

- **[ParaFusionBench: A Unified Benchmark for Cross-Paradigm Fusion in Factor Mining and Trading Decision-Making](https://openreview.net/forum?id=nqb5xH3QuC)**
  - *{'username': '~Xiaozhao_Zeng1', 'fullname': 'Xiaozhao Zeng', 'institutions': [{'name': 'The Hong Kong University of Science and Technology (Guangzhou)', 'domain': 'hkust-gz.edu.cn', 'country': 'CN'}]}, {'username': '~Fan_Liu5', 'fullname': 'Fan Liu', 'institutions': [{'name': 'AI Thrust, Hong Kong University of Science and Technology (Guangzhou)', 'domain': 'ust.hk', 'country': 'CN'}]}, {'username': '~Yang_Ni4', 'fullname': 'Yang Ni', 'institutions': [{'name': 'The Hong Kong University of Science and Technology', 'domain': 'connect.hkust-gz.edu.cn', 'country': 'CN'}]} et al.*
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Quantitative investment research has evolved from conventional models to large language models (LLMs) and multi-agent collaboration, forming two primary research trajectories: factor mining and trading decision-making. Their intersection yields four paradigms: Conventional Factor…

- **[Rethinking the Evaluation of Harness Evolution for Agents](https://openreview.net/forum?id=QDdWiaNkk2)**
  - **ICML 2025** · OpenReview · `2026-09-17`
  - Harness evolution is an iterative search procedure that repeatedly evaluates and revises candidate harnesses used for LLM agents using task feedback. We revisit the evaluation of such automatic harness evolution procedures and identify two fundamental issues in the protocol. Firs…

- **[FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors](https://openreview.net/forum?id=RKKGxm7O4L)**
  - **ICML 2025** · OpenReview · `2026-09-16`
  - As AI agents are becoming widely adopted in the financial services industry, careful measurement is essential to understand where they can be reliably deployed and where oversight and professional review remain necessary. Such measurement, however, is constrained by limited acces…

- **[PortfolioRouter: Consequence-Aware Multi-Task Routing for Portfolio Agents](https://openreview.net/forum?id=My6dyV7ecS)**
  - **ICML 2025** · OpenReview · `2026-09-14`
  - Portfolio agents can recommend materially different allocations for the same trading date, but standard best-expert classification does not weight errors by their financial cost. The cost of a routing error depends on the return forgone by choosing one proposal over another. We i…

- **[AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing](https://arxiv.org/abs/2608.29622)**
  - *{'fullname': 'Xinke Jiang', 'username': ''}, {'fullname': 'Yue Fang', 'username': ''}, {'fullname': 'Zhibang Yang', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2026-08-01`
  - Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts. Recent reinforcement learnin…

- **[A Timely Diagnostic Benchmark for Agentic RL Post-Training with Promising but Uneven Results](https://openreview.net/forum?id=C0pHkZfzHW)**
  - **ICML 2025** · OpenReview · `2026-07-13`

- **[Harness Engineering for LLM Agents: A Survey of Harness Component Taxonomy, Evaluation, and Model--Harness Coevolution](https://openreview.net/forum?id=1VJLY0hAFT)**
  - **ICML 2025** · OpenReview · `2026-07-03`
  - As large language model-driven autonomous agents are increasingly deployed in real-world long-horizon, open-environment tasks, foundation models expose systematic capability gaps in context retention, reliable tool invocation, persistent state management, and multi-step execution…

- **[Important Evidence That Multimodal Safety Does Not Automatically Transfer to Agentic Tool Use](https://openreview.net/forum?id=TWV4pn8Of5)**
  - **ICML 2025** · OpenReview · `2026-07-01`

- **[Accept: Valuable process-level evaluation framework for LLM discovery agents](https://openreview.net/forum?id=UlKWRADnxG)**
  - **ICML 2025** · OpenReview · `2026-06-28`

- **[A large-scale tool-use benchmark with real servers](https://openreview.net/forum?id=emDTYIGJBV)**
  - **ICML 2025** · OpenReview · `2026-06-24`

- **[Review for the paper ClawBenchPro: Benchmarking How Well Agent Harnesses Work](https://openreview.net/forum?id=sYCTp3rsDS)**
  - **ICML 2025** · OpenReview · `2026-06-24`

- **[this paper presents a chronological replay environment for evaluating long-horizon adaptive forecasting agents](https://openreview.net/forum?id=X4BsNscWQz)**
  - **ICML 2025** · OpenReview · `2026-06-24`

- **[LLM-agent security benchmark with few concerns.](https://openreview.net/forum?id=5ZCxeIZzRF)**
  - **ICML 2025** · OpenReview · `2026-06-22`

- **[Trident: Piercing Deep Reinforcement Learning Cyber Defenses via Agentic Language Models](https://openreview.net/forum?id=cNNRsxljqQ)**
  - **ICML 2025** · OpenReview · `2026-06-20`

- **[A Valuable Financial Multimodal Benchmark with Multi-Turn and Agent Evaluation, but Some Validation Concerns Remain](https://openreview.net/forum?id=A2u2L7lj5h)**
  - **ICML 2025** · OpenReview · `2026-06-12`

- **[A Fraud-Detection-Inspired Framework for LLM Agents Security](https://openreview.net/forum?id=uUipgSY8Sh)**
  - *Sheldon Yu, Yingcheng Sun, Hanqing Guo et al.*
  - **ICML 2025** · OpenReview · `2026-06-12`
  - Large Language Model (LLM) agents demonstrate strong capabilities in autonomous task execution, tool use, and multi-step reasoning. However, their increasing autonomy also introduces a new attack surface: adversarial interactions can manipulate agent behavior through direct promp…

- **[The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation](https://openreview.net/forum?id=1sqKRqsaE9)**
  - *Naman Vats, Oleg Aleksandrovich Golev*
  - **ICML 2025** · OpenReview · `2026-06-10`
  - Public leaderboards for coding agents typically rank systems by model name and pass rate, while the surrounding harness—the scaffold that issues tools, manages context, and decides when to stop—is often under-specified. Model-to-model comparison is valid when the harness is fixed…

- **[Agentic Evaluation Framework for Option Trading](https://openreview.net/forum?id=OAxCMnrFbJ)**
  - **ICML 2025** · OpenReview · `2026-06-08`

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

- **[Towards Direct Evaluation of Harness Optimizers via Priority Ranking](https://openreview.net/forum?id=WSQLJ0m6kS)**
  - *Kai Tzu-iunn Ong, Minseok Kang, Dongwook Choi et al.*
  - **ICML 2025** · OpenReview · `2026-05-05`
  - Harness optimization enables automated agent creation by having an optimizer agent iteratively update the harness of target agents. Despite its success, current studies evaluate optimizers solely by observing target agents' performance gains. This indirect end-improvement evaluat…

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

- **[Tool-as-Interface: Learning Robot Policies from Observing Human Tool Use](https://openreview.net/forum?id=Sda6LcPcdB)**
  - *Haonan Chen, Cheng Zhu, Yunzhu Li et al.*
  - **ICML 2025** · OpenReview · `2025-03-30`
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

- **[CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities](https://arxiv.org/abs/2503.17332)**
  - *Yuxuan Zhu, Antony Kellermann, Dylan Bowman et al.*
  - **ICML 2025** · `2025-03-21`
  - Large language model (LLM) agents are increasingly capable of autonomously conducting cyberattacks, posing significant threats to existing applications. This growing risk highlights the urgent need for a real-world benchmark to evaluate the ability of LLM agents to exploit web ap…

- **[Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://arxiv.org/abs/2503.03983)**
  - *Sreyan Ghosh, Zhi-Feng Kong, Sonal Kumar et al.*
  - **ICML 2025** · `2025-03-06`
  - Understanding and reasoning over non-speech sounds and music are crucial for both humans and AI agents to interact effectively with their environments. In this paper, we introduce Audio Flamingo 2 (AF2), an Audio-Language Model (ALM) with advanced audio understanding and reasonin…

- **[QLASS: Boosting Language Agent Inference via Q-Guided Stepwise Search](https://arxiv.org/abs/2502.02584)**
  - *Zong-Yu Lin, Yao Tang, Xingcheng Yao et al.*
  - **ICML 2025** · `2025-02-04`
  - Language agents have become a promising solution to complex interactive tasks. One of the key ingredients to the success of language agents is the reward model on the trajectory of the agentic workflow, which provides valuable guidance during training or inference. However, due t…

- **[Tool Unlearning for Tool-Augmented LLMs](https://arxiv.org/abs/2502.01083)**
  - *Jiali Cheng, Hadi Amiri*
  - **ICML 2025** · `2025-02-03`
  - Tool-augmented large language models (LLMs) are often trained on datasets of query-response pairs, which embed the ability to use tools or APIs directly into the parametric knowledge of LLMs. Tool-augmented LLMs need the ability to forget learned tools due to security vulnerabili…

- **[UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent](https://arxiv.org/abs/2501.18867)**
  - *Jian-Ke Zhang, Yanjiang Guo, Yu-Cheng Hu et al.*
  - **ICML 2025** · `2025-01-30`
  - Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilit…


### ICLR

- **[Disclosure Bias in AI Reviewers](https://arxiv.org/abs/2611.30410v1)**
  - *Jens Leysen, Noah Daniëls, Marco Favier et al.*
  - **ICLR** · `2026-11-23`
  - AI models increasingly help to review papers, and many conferences and journals now require authors to state how they used AI. Does this AI-use statement change how an AI reviewer rates a paper, and could it change which papers are accepted? In a preliminary study, we varied only…

- **[MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers](https://arxiv.org/abs/2512.15163)**
  - *Xuan Zong, Zhiqi Shen, Lei Wang et al.*
  - **ICLR 2025** · `2025-12-17`
  - Large language models (LLMs) are evolving into agentic systems that reason, plan, and operate external tools. The Model Context Protocol (MCP) is a key enabler of this transition, offering a standardized interface for connecting LLMs with heterogeneous tools and services. Yet MCP…

- **[TRAJECT-Bench:A Trajectory-Aware Benchmark for Evaluating Agentic Tool Use](https://arxiv.org/abs/2510.04550)**
  - *Peng-Fei He, Zhen-Wei Dai, B. He et al.*
  - **ICLR 2025** · `2025-10-06`
  - Large language model (LLM)-based agents increasingly rely on tool use to complete real-world tasks. While existing works evaluate the LLMs'tool use capability, they largely focus on the final answers yet overlook the detailed tool usage trajectory, i.e., whether tools are selecte…

- **[TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture](https://arxiv.org/abs/2510.01279)**
  - *Yong-Chao Chen, Jie-Feng Chen, Rui Meng et al.*
  - **ICLR 2025** · `2025-09-30`
  - While integrating tools like Code Interpreter and Search has significantly enhanced Large Language Model (LLM) reasoning in models like ChatGPT Agent and Gemini-Pro, practical guidance on optimal tool use is lacking. The core challenge is effectively combining textual reasoning,…

- **[Toward Efficient Exploration by Large Language Model Agents](https://arxiv.org/abs/2504.20997)**
  - *Dilip Arumugam, T. Griffiths*
  - **ICLR 2025** · `2025-04-29`
  - A burgeoning area within reinforcement learning (RL) is the design of sequential decision-making agents centered around large language models (LLMs). While autonomous decision-making agents powered by modern LLMs could facilitate numerous real-world applications, such successes d…

- **[ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536)**
  - *Jiazhan Feng, Shijue Huang, Xing-Wei Qu et al.*
  - **ICLR 2025** · `2025-04-15`
  - While reasoning models (e.g., DeepSeek R1) trained with reinforcement learning (RL), excel in textual reasoning, they struggle in scenarios requiring structured problem-solving, such as geometric reasoning, concise computation, or complex equation solving-areas where computationa…


### CVPR

- **[Don't Show Pixels, Show Cues: Unlocking Visual Tool Reasoning in Language Models via Perception Programs](https://arxiv.org/abs/2604.12896)**
  - *M. Janjua, Hugo Silva, Di Niu et al.*
  - **CVPR 2026** · `2026-04-14`
  - Multimodal language models (MLLMs) are increasingly paired with vision tools (e.g., depth, flow, correspondence) to enhance visual reasoning. However, despite access to these tool-generated visual cues, MLLMs often fail to benefit from them. Existing approaches typically feed raw…

- **[Thinking With Videos: Multimodal Tool-Augmented Reinforcement Learning for Long Video Reasoning](https://arxiv.org/abs/2508.04416)**
  - *Haoji Zhang, Xin Gu, Jia-Wen Li et al.*
  - **CVPR 2025** · `2025-08-06`
  - The video reasoning ability of multimodal large language models (MLLMs) is crucial for downstream tasks like video question answering and temporal grounding. While recent approaches have explored text-based chain-of-thought (CoT) reasoning for MLLMs, these methods often suffer fr…

- **[Automated Generation of Challenging Multiple-Choice Questions for Vision Language Model Evaluation](https://arxiv.org/abs/2501.03225)**
  - *Yuhui Zhang, Yu-Chang Su, Yiming Liu et al.*
  - **CVPR 2025** · `2025-01-06`
  - The rapid development of vision language models (VLMs) demands rigorous and reliable evaluation. However, current visual question answering (VQA) benchmarks often depend on open-ended questions, making accurate evaluation difficult due to the variability in natural language respo…


### KDD

- **[A Design Space for Data Agents: Insights from KDD Cup 2026](https://arxiv.org/abs/2611.28970v1)**
  - *Boyan Li, Zhuowen Liang, Yupeng Xie et al.*
  - **KDD** · `2026-11-21`
  - Data agents interpret analytical requests, gather evidence from heterogeneous sources, and compute results within finite resource budgets. We analyze the final code submissions of the ten highest-ranked teams in the KDD Cup 2026 Data Agents for Complex Data Analysis competition.…


### ACL

- **[TrialAgentBench: Evaluating AI Agents for Clinical-Trial Analysis and Long-Horizon Drug-Development Decisions](https://arxiv.org/abs/2611.30916v1)**
  - *Bradley Segal, William Bolton, Philip Torr et al.*
  - **ACL** · `2026-11-23`
  - Clinical drug development is a long-horizon, high-stakes process requiring sequential decisions based on information that costs money and time to acquire. AI agents have demonstrated capabilities for scientific analysis, but there is no established way to evaluate them on these d…

- **[Intent-Conditioned Argument Mediation for Tool-Using LLM Agents: Blocking Trusted-but-Unauthorized Arguments](https://arxiv.org/abs/2611.30745v1)**
  - *Yulliwas Ameur, Miqeas Pedro Mendes, Samia Bouzefrane*
  - **ACL** · `2026-11-23`
  - LLM agents turn a user's request and retrieved content into tool calls, and a call can reach the wrong recipient, endpoint, file or participant. Argument-level provenance blocks such values when they come from untrusted content, but accepts a trusted value that the user never req…

- **[Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing](https://arxiv.org/abs/2611.30742v1)**
  - *Yulliwas Ameur, Samia Bouzefrane, Soumya Banerjee*
  - **ACL** · `2026-11-23`
  - Large language model (LLM) agents are often ranked by an LLM judge whose error rates are measured once and reused for every agent. The corrected success rates can then be biased when the judge's errors depend on the trajectory and agents differ in the trajectories they produce fo…

- **[Bridging Blind Spots With Words: Decentralized Multi-View Spatial Reasoning via Language-Constrained Communication](https://arxiv.org/abs/2611.29112v1)**
  - *Soumyabrata Chaudhuri, Joydeep Ghosh*
  - **ACL** · `2026-11-22`
  - As multimodal LLMs (MLLMs) get increasingly used as collaborative partners across embodied robotics, AR/VR, and multi-user systems, spatial reasoning is now often distributed across agents with partial environment visibility, necessitating spatial reasoning integration. Prior wor…

- **[Beyond Evidence Coverage: Encoding-Time Access in Multi-Agent Systems](https://arxiv.org/abs/2611.29107v1)**
  - *Joshua Huang, Ajit Mallavarapu, Elliott Kalt*
  - **ACL** · `2026-11-22`
  - Cache-sharing multi-agent systems can retain every evidence token's representation while preventing cross-worker access during encoding. We test whether this coverage recovers joint-encoding quality using attention masks over two logical workers in frozen Qwen3-4B, Qwen3-8B, and…

- **[Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS](https://arxiv.org/abs/2605.25389)**
  - *Bing-Yu Yan, Xiao-Ming Zhang, Jin-Yun Hou et al.*
  - **ACL 2026** · `2026-05-25`
  - While Large Language Model-based Multi-Agent Systems (LLM-MAS) demonstrate remarkable capabilities in solving complex tasks by orchestrating specialized agents and external tools, the implicit trust in tool outputs creates a critical attack surface. Existing tool attacks are limi…

- **[JTPRO: A Joint Tool-Prompt Reflective Optimization Framework for Language Agents](https://arxiv.org/abs/2604.19821)**
  - *Sandip Ghoshal, Anshul Mittal, Jyotika Singh et al.*
  - **ACL 2026** · `2026-04-20`
  - Large language model (LLM) agents augmented with external tools often struggle as number of tools grow large and become domain-specific. In such settings, ambiguous tool descriptions and under-specified agent instructions frequently lead to tool mis-selection and incorrect slot/v…

- **[Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885)**
  - *Yi Yu, Liu-Yi Yao, Yue-Xiang Xie et al.*
  - **ACL 2026** · `2026-01-05`
  - Large language model (LLM) agents face fundamental limitations in long-horizon reasoning due to finite context windows, making effective memory management critical. Existing methods typically handle long-term memory (LTM) and short-term memory (STM) as separate components, relyin…

- **[AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading](https://arxiv.org/abs/2510.14264)**
  - *Zheye Deng, Wei-Xiang Yan, Chang-Long Yu et al.*
  - **ACL 2025** · `2025-10-16`
  - While Large Language Model (LLM) agents show promise in automated trading, they still face critical limitations. Prominent multi-agent frameworks often suffer from inefficiency, produce inconsistent signals, and lack the end-to-end optimization required to learn a coherent strate…

- **[Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828)**
  - *Si-Kuan Yan, Xiu-Feng Yang, Zuchao Huang et al.*
  - **ACL 2025** · `2025-08-27`
  - Large Language Models (LLMs) have demonstrated impressive capabilities across a wide range of NLP tasks, but they remain fundamentally stateless, constrained by limited context windows that hinder long-horizon reasoning. Recent efforts to address this limitation often augment LLM…

- **[R-VLM: Region-Aware Vision Language Model for Precise GUI Grounding](https://arxiv.org/abs/2507.05673)**
  - *Joonhyung Park, Peng Tang, Sagnika Das et al.*
  - **ACL 2025** · `2025-07-07`
  - Visual agent models for automating human activities on Graphical User Interfaces (GUIs) have emerged as a promising research direction, driven by advances in large Vision Language Models (VLMs). A critical challenge in GUI automation is the precise grounding of interface elements…

- **[Reasoning RAG via System 1 or System 2: A Survey on Reasoning Agentic Retrieval-Augmented Generation for Industry Challenges](https://arxiv.org/abs/2506.10408)**
  - *Jin-Tao Liang, Gang Su, Hui-Feng Lin et al.*
  - **ACL 2025** · `2025-06-12`
  - Retrieval-Augmented Generation (RAG) has emerged as a powerful framework to overcome the knowledge limitations of Large Language Models (LLMs) by integrating external retrieval with language generation. While early RAG systems based on static pipelines have shown effectiveness in…

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

- **[Text2World: Benchmarking Large Language Models for Symbolic World Model Generation](https://arxiv.org/abs/2502.13092)**
  - *Meng-Kang Hu, Tian-Xing Chen, Yu-De Zou et al.*
  - **ACL 2025** · `2025-02-18`
  - Recently, there has been growing interest in leveraging large language models (LLMs) to generate symbolic world models from textual descriptions. Although LLMs have been extensively explored in the context of world modeling, prior studies encountered several challenges, including…

- **[ToolHop: A Query-Driven Benchmark for Evaluating Large Language Models in Multi-Hop Tool Use](https://arxiv.org/abs/2501.02506)**
  - *Junjie Ye, Zheng-Yin Du, Xue-Song Yao et al.*
  - **ACL 2025** · `2025-01-05`
  - Effective evaluation of multi-hop tool use is critical for analyzing the understanding, reasoning, and function-calling capabilities of large language models (LLMs). However, progress has been hindered by a lack of reliable evaluation datasets. To address this, we present ToolHop…

- **[AgentGym: Evaluating and Training Large Language Model-based Agents across Diverse Environments](https://aclanthology.org/2025.acl-long.1355.pdf)**
  - *Zhi-Heng Xi, Yi-Wen Ding, Wen-Xiang Chen et al.*
  - **ACL 2025**
  - Large language models (LLMs) have emerged as a promising foundation to build generally-capable agents (LLM-based agents) that can handle multi-turn decision-making tasks across various environments. However, the community lacks a unified interactive framework that covers diverse…


### EMNLP

- **[Tool Zero: Training Tool-Augmented LLMs via Pure RL from Scratch](https://arxiv.org/abs/2511.01934)**
  - *Yi-Rong Zeng, Xiao Ding, Yu-Tai Hou et al.*
  - **EMNLP 2025** · `2025-11-02`
  - Training tool-augmented LLMs has emerged as a promising approach to enhancing language models'capabilities for complex tasks. The current supervised fine-tuning paradigm relies on constructing extensive domain-specific datasets to train models. However, this approach often strugg…

- **[LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://arxiv.org/abs/2506.17335)**
  - *Shuo Yan, Ruochen Li, Ziming Luo et al.*
  - **EMNLP 2025** · `2025-06-19`
  - Large language model (LLM) agents have demonstrated remarkable potential in advancing scientific discovery. However, their capability in the fundamental yet crucial task of reproducing code from research papers, especially in the NLP domain, remains underexplored. This task inclu…

- **[ToolHaystack: Stress-Testing Tool-Augmented Language Models in Realistic Long-Term Interactions](https://arxiv.org/abs/2505.23662)**
  - *Beong-woo Kwak, Minju Kim, Dongha Lim et al.*
  - **EMNLP 2025** · `2025-05-29`
  - Large language models (LLMs) have demonstrated strong capabilities in using external tools to address user inquiries. However, most existing evaluations assume tool use in short contexts, offering limited insight into model behavior during realistic long-term interactions. To fil…

- **[TrojanStego: Your Language Model Can Secretly Be A Steganographic Privacy Leaking Agent](https://arxiv.org/abs/2505.20118)**
  - *Dominik Meier, Jan Philip Wahle, Paul Röttger et al.*
  - **EMNLP 2025** · `2025-05-26`
  - As large language models (LLMs) become integrated into sensitive workflows, concerns grow over their potential to leak confidential information. We propose TrojanStego, a novel threat model in which an adversary fine-tunes an LLM to embed sensitive context information into natura…

- **[Runaway is Ashamed, But Helpful: On the Early-Exit Behavior of Large Language Model-based Agents in Embodied Environments](https://arxiv.org/abs/2505.17616)**
  - *Qingyu Lu, Liang Ding, Siyi Cao et al.*
  - **EMNLP 2025** · `2025-05-23`
  - Agents powered by large language models (LLMs) have demonstrated strong planning and decision-making capabilities in complex embodied environments. However, such agents often suffer from inefficiencies in multi-turn interactions, frequently trapped in repetitive loops or issuing…

- **[AgentThink: A Unified Framework for Tool-Augmented Chain-of-Thought Reasoning in Vision-Language Models for Autonomous Driving](https://arxiv.org/abs/2505.15298)**
  - *Kan-Gan Qian, Sicong Jiang, Yang Zhong et al.*
  - **EMNLP 2025** · `2025-05-21`
  - Vision-Language Models (VLMs) show promise for autonomous driving, yet their struggle with hallucinations, inefficient reasoning, and limited real-world validation hinders accurate perception and robust step-by-step reasoning. To overcome this, we introduce \textbf{AgentThink}, a…

- **[WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model](https://arxiv.org/abs/2504.21024)**
  - *Tianqing Fang, Hong-Ming Zhang, Zhi-Song Zhang et al.*
  - **EMNLP 2025** · `2025-04-23`
  - Agent self-improvement, where the backbone Large Language Model (LLM) of the agent are trained on trajectories sampled autonomously based on their own policies, has emerged as a promising approach for enhancing performance. Recent advancements, particularly in web environments, f…

- **[TP-RAG: Benchmarking Retrieval-Augmented Large Language Model Agents for Spatiotemporal-Aware Travel Planning](https://arxiv.org/abs/2504.08694)**
  - *Hang Ni, Fan Liu, Xin-Yu Ma et al.*
  - **EMNLP 2025** · `2025-04-11`
  - Large language models (LLMs) have shown promise in automating travel planning, yet they often fall short in addressing nuanced spatiotemporal rationality. While existing benchmarks focus on basic plan validity, they neglect critical aspects such as route efficiency, POI appeal, a…

- **[VerifiAgent: a Unified Verification Agent in Language Model Reasoning](https://arxiv.org/abs/2504.00406)**
  - *Jiuzhou Han, W. Buntine, Ehsan Shareghi*
  - **EMNLP 2025** · `2025-04-01`
  - Large language models demonstrate remarkable reasoning capabilities but often produce unreliable or incorrect responses. Existing verification methods are typically model-specific or domain-restricted, requiring significant computational resources and lacking scalability across d…

- **[Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://arxiv.org/abs/2503.02519)**
  - *Xingzuo Li, Ke-Hai Chen, Yunfei Long et al.*
  - **EMNLP 2025** · `2025-03-04`
  - Large language model (LLM) agents typically adopt a step-by-step reasoning framework, in which they interleave the processes of thinking and acting to accomplish the given task. However, this paradigm faces a deep-rooted one-pass issue whereby each generated intermediate thought…


### NAACL

- **[Self-Training Large Language Models for Tool-Use Without Demonstrations](https://arxiv.org/abs/2502.05867)**
  - *Ne Luo, Aryo Pradipta Gema, Xuan-Li He et al.*
  - **NAACL 2025** · `2025-02-09`
  - Large language models (LLMs) remain prone to factual inaccuracies and computational errors, including hallucinations and mistakes in mathematical reasoning. Recent work augmented LLMs with tools to mitigate these shortcomings, but often requires curated gold tool-use demonstratio…


### Other / arXiv

- **[3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets](https://arxiv.org/abs/2611.30013)**
  - *Bohan Zeng, Kaixin Zhu, Yifan Yang et al.*
  - 🤗 Featured · `2026-11-23`

- **[RUIBench: What Makes a Good Robot-Use Interface?](https://arxiv.org/abs/2611.31115)**
  - *Yanzhe Chen, Zhijun Cao, Zechen Bai et al.*
  - 🤗 Featured · `2026-11-23`
  - Foundation models can reason about complex physical tasks, yet translating this intelligence into reliable robot execution remains challenging. We argue that a critical, often overlooked factor is the robot-use interface (RUI), which determines how agents express and execute phys…

- **[What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym](https://arxiv.org/abs/2611.30207)**
  - *Yikai Zhang, Mai Xu, Yunbei Zhang et al.*
  - 🤗 Featured · `2026-11-23`
  - Reinforcement learning (RL) trains coding agents on software tasks whose hidden tests decide the reward, yet task collections check these tests only against the reference fix. We ask what makes a task good training data, focusing on the correctness of its reward labels. We audit…

- **[GameDojo: Benchmarking Real-Time Interactive Agents in Video Games](https://arxiv.org/abs/2611.30771)**
  - *Kuan Zhang, Zhihao Yang, Yukun Chen et al.*
  - 🤗 Featured · `2026-11-23`
  - Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss en…

- **[ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents](https://arxiv.org/abs/2611.31198)**
  - *Rui Sun, Junhua Huang, Luca Zancato et al.*
  - 🤗 Featured · `2026-11-23`
  - Recent multimodal search agents use reasoning, vision, and live web search across many turns to answer questions beyond parametric knowledge by orchestrating a small library of hand-crafted search and visual tools. However, the library is laborious to create and maintain, and fro…

- **[Innata-0: A Native Embodied World System with Model-Agent Co-Design](https://arxiv.org/abs/2611.30254)**
  - *Innata Team, Yu Bai, Ziyi Bai et al.*
  - 🤗 Featured · `2026-11-23`

- **[GameAnything: From Any Inspirations to Playable Game Worlds](https://arxiv.org/abs/2611.29238)**
  - *Wenyi Wu, Siqi Liu, Yuru Feng et al.*
  - 🤗 Featured · `2026-11-22`
  - AI-driven game development holds the potential to transform diverse human inspirations into interactive experiences. However, existing systems and benchmarks primarily focus on explicit development specifications, with limited support for adapting multimodal references and evalua…

- **[Wactorz: Self-Writing LLM Agents That Discover, Repair, and Migrate at the Edge](https://arxiv.org/abs/2611.29619)**
  - *Panagiotis Kasnesis, Lazaros Toumanidis, Amalia Contiero Syropoulou et al.*
  - 🤗 Featured · `2026-11-22`
  - Most LLM agent frameworks build a crew that runs a task and exits. Physical environments (e.g., homes, labs, factory floors) need agents that stay up for months, survive their own bugs, and run on whatever hardware is already next to the sensors. We present Wactorz, an open-sourc…

- **[KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware](https://arxiv.org/abs/2611.29590)**
  - *Shuaiwei Huang, Weihua Du, Allen Wu et al.*
  - 🤗 Featured · `2026-11-22`
  - Efficient AI computation depends on hardware that evolves over time, shifting the strategies needed to implement performant code. For CPU kernels, a key evolving factor is the set of available architectural extensions, which expose specialized hardware instructions that change th…

- **[Distilling Visual Agents from Limited Interaction Experience](https://arxiv.org/abs/2611.28618)**
  - *Siyu Zhou, Jing Jiang, Chengqi Zhang et al.*
  - 🤗 Featured · `2026-11-21`
  - How much interaction experience is needed to distill a capable visual agent? We study learning from few tasks and recorded interaction histories. Our framework selects representative trajectories using skill-context coverage and ordered visual-decision similarity. On-policy disti…

- **[AutoPILOT: A Visual Agent Harness for Real-Time Gameplay](https://arxiv.org/abs/2611.28202)**
  - *Mark Zhao, Pengcheng Wang, Rui Yang et al.*
  - 🤗 Featured · `2026-11-20`

- **[Measuring and Teaching Language Model Agents to Act on Delayed Consequences](https://arxiv.org/abs/2611.28158)**
  - *Shardul Bansal, Seth Schilbe, Jarrod Barnes*
  - 🤗 Featured · `2026-11-19`

- **[How Complete Must an Environment Be to Train a Capable GUI Agent?](https://arxiv.org/abs/2611.23946)**
  - *Jingxing Wang, Teng Wang, Xingyu Lou et al.*
  - 🤗 Featured · `2026-11-18`

- **[ACAP: Asynchronous Coding Agents for Efficient Robot Control](https://arxiv.org/abs/2611.31205)**
  - *Zexin He, Rui Li, Yushi Lan et al.*
  - 🤗 · `2026-11-23`
  - Coding agents can construct and revise robot behavior during execution, but using one agent for the whole robot can delay otherwise independent work. We introduce Asynchronous Coding Agents as Policy (ACAP), an asynchronous framework that organizes one robot as a team of persiste…

- **[Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation](https://arxiv.org/abs/2611.31098)**
  - *Jinzhong Gu, Jiakai Chen, Xinyi Cao et al.*
  - 🤗 · `2026-11-23`

- **[RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments](https://arxiv.org/abs/2611.31002)**
  - *Jinkun Liu, Yingze Wang, Situ Wang et al.*
  - 🤗 · `2026-11-23`
  - Agentic Robotics, in which foundation models act as coding agents to control robots through executable programs, has emerged as a compelling paradigm for embodied intelligence. Yet unlike software engineering, where massive executable environments power post-training, robotics re…

- **[MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation](https://arxiv.org/abs/2611.30287)**
  - *Yuxuan Chen, Changwei Lv, Yunfei Li et al.*
  - 🤗 · `2026-11-23`
  - AI agents accumulate conversations, images, and documents through long-term interactions with users. Answering later questions often requires connecting evidence across these records, yet the resulting understanding is rarely retained, allowing mistakes to recur on related questi…

- **[Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ](https://arxiv.org/abs/2611.31228v1)**
  - *Daniel Theron*
  - `2026-11-23`
  - Prompting language models to verbalize stepwise numerical confidence during generation is an increasingly popular approach for triggering backtracking and error correction in agentic reasoning. This strategy presupposes two capabilities: (1) in-situ monitoring fidelity (does conf…

- **[CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting](https://arxiv.org/abs/2611.31185v1)**
  - *Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran*
  - `2026-11-23`
  - Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-…

- **[Habitats: A Framework for Open-Ended Evolution of Agent Objectives](https://arxiv.org/abs/2611.31160v1)**
  - *Nicolas Bolouri, Gaya Mehenni, Daniel Toyama*
  - `2026-11-23`
  - Designing what an agent should optimize can be as difficult as optimizing the agent itself. Existing language-model-based reward-generation methods typically refine objectives for predefined tasks and couple the decision of what to explore with the synthesis of how to implement i…

- **[Self-Upgrading Embodied Agents](https://arxiv.org/abs/2611.31117v1)**
  - *Jiajun Fan, Neil He, Qinglong Zheng et al.*
  - `2026-11-23`
  - An embodied agent built on a language model goes to work with the weights it was given and keeps them for life. To get better, it needs more training, or reflection, memory, search or prompts that cost every step and are lost when the task changes. Editing weights by reasoning, w…

- **[Preflight: Agentic Last-Mile Verification for AI Software Supply Chains](https://arxiv.org/abs/2611.31110v1)**
  - *Yaman Jandali, Nojan Sheybani, Farinaz Koushanfar et al.*
  - `2026-11-23`
  - Software dependencies execute within the trust boundary of downstream applications, yet provenance, static analysis, and package-level behavioral approaches do not directly determine how a released artifact behaves for a specific program. We present Preflight, a program-scoped pr…

- **[LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents](https://arxiv.org/abs/2611.31105v1)**
  - *Tianyi Huang, Samuel Xu, Ivy Gu et al.*
  - `2026-11-23`
  - Updating an LLM adapter should not require replaying the full interaction history of every active session. Yet reusing key-value (KV) cache entries computed under an earlier version mixes model versions, while full-history re-prefill becomes increasingly costly as histories and s…

- **[SayWhen: Set-Valued Semantic Commitment for Low-Regret Early Speech](https://arxiv.org/abs/2611.31101v1)**
  - *Tianyi Huang, Lucas Su, Fred Zhang et al.*
  - `2026-11-23`
  - Speaking early turns a prediction into an irreversible public commitment. We introduce SayWhen, a test-time controller that selects a task-directed act shared across typed continuation plans and controls its release as speech. A persistent veto blocks playback when intervening tr…

- **[ChiProgramBench: Can LLM Agents Rebuild Efficient Circuits from Pin-Level Experiments?](https://arxiv.org/abs/2611.31082v1)**
  - *Tianrun Gou, Qingyao Yang, Wendong Xu et al.*
  - `2026-11-23`
  - Understanding a system that can be run but not inspected is a core engineering skill: one designs experiments, forms hypotheses about hidden state and timing, discards those that observations refute, and finally builds a replacement that works and is efficient. To evaluate this c…

- **[AlphaDefect: Expert-Level AI for Slay the Spire 2](https://arxiv.org/abs/2611.31076v1)**
  - *Qiyue Chen, Taian Yu, Junpei Komiyama et al.*
  - `2026-11-23`
  - Slay the Spire 2 (STS2) is a single-player deck-building game that requires long-term planning under heavy randomness. We present AlphaDefect, an expert-level AI system for STS2: for each character, one network trained with proximal policy optimization (PPO) makes every decision…

- **[From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems](https://arxiv.org/abs/2611.31063v1)**
  - *Wenlong Yu, Bingxu Lu, Qilong Wang et al.*
  - `2026-11-23`
  - In multi-agent systems (MAS) built on large language models (LLMs), errors can propagate through intermediate messages and compromise final answers. However, outcome-based evaluation obscures how agents amplify, attenuate, or correct these errors. We propose Response-Aware Error…

- **[Automatic Occupational Coding through Retrieval-Augmented Generation](https://arxiv.org/abs/2611.31051v1)**
  - *Mathijs A. Langezaal, Egon L. van den Broek, Lukas P. A. Arts et al.*
  - `2026-11-23`
  - Annually 1.9 million deaths and 89.7 million disability-adjusted life years are caused by exposure to agents during work (e.g., welding fumes, silica dust, and noise pollution). To improve worker health, high-quality exposure assessments are crucial. Therefore, free-text job desc…

- **[AI-Assisted Auto-formalization for Trustworthy Scientific Computing: Case Studies and Lessons Learned](https://arxiv.org/abs/2611.31033v1)**
  - *Mohit Tekriwal, Het Mankad, Naifeng Zhang et al.*
  - `2026-11-23`
  - Agentic AI tools have recently had success in mathematical reasoning. Both general purpose coding agents such as Claude Code and Codex, and specialized mathematics agents such as Aristotle, have been used for formalizing mathematical problems such as Fermat's last theorem, Erdős…

- **[ComputeWise: Measuring and Fixing GPU Waste by AI Research Agents](https://arxiv.org/abs/2611.31027v1)**
  - *Egor Pakhomov, Nina Pakhomova, Anurag Koul et al.*
  - `2026-11-23`
  - AI agents are given GPUs to do AI research on their own. Do they use those GPUs well? A busy GPU does not tell us, because it can be busy with work the answer did not need. This matters, because the tokens the agent spends cost almost nothing next to the GPUs its experiments run…

- **[MedUIGym: Evaluating and Training GUI Agents for Clinical Workflows](https://arxiv.org/abs/2611.30983v1)**
  - *Yitong Qiao, Lei Liu, Yue Shen et al.*
  - `2026-11-23`
  - Automating clinical workflows requires vision-language agents that can navigate dense graphical user interfaces (GUIs) in electronic health records (EHRs) and execute precise actions, yet many medical agents still rely on text or structured tool calls. In this work, we introduce…

- **[Self-Evolving Evaluation Environments for Computer-Use Agents](https://arxiv.org/abs/2611.30962v1)**
  - *Wenhao Wang, Panrong Tong, Quyu Kong et al.*
  - `2026-11-23`
  - Computer-use agents (CUAs) are rapidly improving, yet their evaluation remains largely static. Existing benchmarks provide a strong foundation, but fixed difficulty ceilings, limited feature coverage, and coarse aggregate scores progressively weaken their discriminative and diagn…

- **[Aggregation Rules Induced by KL-Regularised Preference Dynamics on Networks](https://arxiv.org/abs/2611.30941v1)**
  - *Milan Vojnovic*
  - `2026-11-23`
  - We study agents that each align a model to their own preference data while observing one another, and ask which aggregation rule the resulting policies implement. Each round, an agent takes one KL-regularised step. The step involves a reference that the agent is penalised for lea…

- **[Bridging Continuous-Time MAPF and Industrial AGV Fleet Coordination with Lazy Priority-Based Search](https://arxiv.org/abs/2611.30874v1)**
  - *Federico Signorile, Raffaele Carli, Alessandro Bertogli et al.*
  - `2026-11-23`
  - Continuous-time multi-agent path finding on roadmaps (MAPF$_R$) offers a principled way to coordinate robot fleets with geometric collision avoidance, yet its deployment on industrial automated guided vehicle (AGV) infrastructures remains challenging, as highly connected and redu…

- **[SchemaCaps: When a Compatible Tool Update Silently Widens an AI Agent's Authority](https://arxiv.org/abs/2611.30750v1)**
  - *Yulliwas Ameur, Samia Bouzefrane, Soumya Banerjee*
  - `2026-11-23`
  - The tools users approve for their AI agents keep changing their JSON input schemas. Of 8 surveyed MCP clients and scanners, none is observed or documented to re-approve a tool whose input schema widens (two not determinable). We define non-amplification over the coordinates visib…

- **[Can Cities Have Personalities? Introducing the SCD City Personality Assessment](https://arxiv.org/abs/2611.30733v1)**
  - *Andrei Khurshudov*
  - `2026-11-23`
  - Descriptions of cities are shaped by human experience and institutional narratives. We introduce the SCD City Personality Assessment (SCD-CPA), a method that instantiates document-grounded ChatGPT city personas and interrogates each with an identical 24-statement instrument inspi…

- **[CocoonBench: Can Multilingual Search Agents Escape Language Information Cocoons?](https://arxiv.org/abs/2611.30727v1)**
  - *Hongchuan Zeng, Bowen Liu, Changjiang Gao et al.*
  - `2026-11-23`
  - Multilingual search agents can access the global Web, yet may remain trapped in a language environment with insufficient evidence; we refer to this failure as a language information cocoon. However, existing search benchmarks largely operate within a single language, especially E…

- **[Skill-Composer: Requirement-Driven Skill Selection from Multiple Marketplaces](https://arxiv.org/abs/2611.30715v1)**
  - *Zicheng Chen, Jia Li, Xiaohong Chen et al.*
  - `2026-11-23`
  - Agent skills have become the primary vehicle through which agents reuse specialized capabilities, yet public skill marketplaces provide skills with individual items: a query, whether matched through keyword or embedding similarity, returns a list of single skills ordered by relev…

- **[Beyond the Black Box: A Diagnosis-Driven Agent for Interpretable MIP Solver Tuning](https://arxiv.org/abs/2611.30670v1)**
  - *Yidong Luo, Weihuang Wen, Xuanhao Pan et al.*
  - `2026-11-23`
  - Tuning a mixed-integer programming (MIP) solver is an instance-specific problem, where a poor configuration can increase solving time by orders of magnitude.   Existing Bayesian optimization tuners treat solver tuning as a black-box optimization problem: each evaluation returns a…

- **[Oops!... I Parsed It Again: Tool-Call Smuggling Against LLM Agents](https://arxiv.org/abs/2611.30624v1)**
  - *Igor Santos-Grueiro, Daniel Romero-Ruiz*
  - `2026-11-23`
  - LLM agents act through tool calls: the model writes the arguments of a call as JSON, a guard decides whether the call may run, and an executor runs it. The same bytes are parsed several times, by the provider, gateways, SDKs, frameworks, the guard, and the executor. JSON leaves s…

- **[Interrogation Protocols for AI Control](https://arxiv.org/abs/2611.30583v1)**
  - *Aniruddh Pramod, Matthew Khoriaty, James Lucassen et al.*
  - `2026-11-23`
  - As the intelligence of an AI agent increases relative to a trusted monitor, so does the risk that the monitor will fail to understand the agent's actions or to evaluate them confidently. We introduce interrogation protocols to a high-stakes AI control setting, and allow the monit…

- **[Learning What to Change: State-Verified Reinforcement Learning for Educational Agents](https://arxiv.org/abs/2611.30559v1)**
  - *Shengyao Wang, Siyuan Su, Siyu Song et al.*
  - `2026-11-23`
  - Persistent tutoring agents do more than answer questions: they manage course files, practice records, and learner profiles that govern future lessons. In such stateful settings, knowing what to teach does not guarantee knowing what to change. We identify a pervasive failure mode,…

- **[RoboInF: A Benchmark for Instruction Fidelity in Robotic Manipulation](https://arxiv.org/abs/2611.30555v1)**
  - *Jiawei Guo, Yu Huang, Dijiang Dong et al.*
  - `2026-11-23`
  - Precise language control requires embodied models to follow instructions governing both task outcomes and execution. Although recent methods train policies to follow increasingly detailed commands, existing benchmarks often assess instruction following alongside perception, plann…

- **[sudo L7: Can Coding Agents Act Like Staff Engineers?](https://arxiv.org/abs/2611.30517v1)**
  - *Nick Heiner, Ian Niebres, Suhaas Garre et al.*
  - `2026-11-23`
  - Coding agents can now turn a well-specified ticket into a patch that passes its tests. Experienced engineers also notice risks the request never mentioned, question flawed premises, reuse what already exists and say plainly what they did and did not check. We present sudo L7, a b…

- **[HWRE-Bench: Can LLM Agents Understand Hardware They Did Not Design?](https://arxiv.org/abs/2611.30422v1)**
  - *Peilong Zhou, Cangyuan Li, Kaiyan Chang et al.*
  - `2026-11-23`
  - Hardware benchmarks for LLM agents all run the design flow forward, from a specification to RTL, a layout or a bug fix. We ask the reverse question: given an implemented artifact, such as a layout, a gate-level netlist or a protected simulation model, can an agent work out what i…

- **[DMC-5: Dual-Model Collaboration with Cache-aware Context Compression for Long-horizon Agents](https://arxiv.org/abs/2611.30412v1)**
  - *Haochen Li, Xiaobing Tu, Yinggui Wang et al.*
  - `2026-11-23`
  - Long-horizon agents repeatedly feed an ever-growing interaction trajectory to a specialized agent model. Prefix caching reuses computation over repeated history, but cannot prevent context growth or remove information irrelevant to the current decision. This is especially costly…

- **[Cost-Sensitive Reversibility of Non-Deterministic Actions](https://arxiv.org/abs/2611.30399v1)**
  - *Giuseppe Canonaco, Alberto Pozanco, Daniel Borrajo*
  - `2026-11-23`
  - Determining action reversibility requires checking whether the effects of an action can be undone. Recent work has extended reversibility to fully observable non-deterministic (FOND) planning. It distinguishes weak reversibility, where reversal may succeed, from strong-cyclic rev…

- **[mini-psych-agent: Evaluating Human-Like Behavior in LLM Agents through Interactive Psychological Environments](https://arxiv.org/abs/2611.30365v1)**
  - *Yi-Fei Cao, Tianxin Huang, Hanbo Xie et al.*
  - `2026-11-23`
  - A Large Language Model (LLM), its harness, and the test-time compute budget jointly determine its behavior. Consequently, the same underlying model, embedded in different agentic workflows or allocated different amounts of test-time compute, can exhibit markedly different perform…

- **[RepoClean: Evaluating Coding Agents on Repository-Level Obsolete Code Cleanup](https://arxiv.org/abs/2611.30350v1)**
  - *Hongyixuan Yuan, Qixing Zhou, Pengcheng Huang et al.*
  - `2026-11-23`
  - Large language model (LLM) agents have demonstrated strong repository-level programming capabilities. However, as software evolves, repository code may become redundant or obsolete, increasing maintenance costs and potentially introducing functional issues. Agents must therefore…

- **[Attributing Security Outcomes in LLM-Agent Evaluations: The Role of Content-Free State](https://arxiv.org/abs/2611.30259v1)**
  - *Abdelmonaim Bounite, Zangir Iklassov*
  - `2026-11-23`
  - Security benchmarks for LLM agents record whether each attack succeeded and compare agents, attacks, and defenses by attack success rate (ASR). Such comparisons are valid only if the agent, the attack, and the defense cause each verdict. We show that verdicts also depend on conte…

- **[Adopting AI Technologies without Traps: A Multi-Agent Reinforcement Learning Framework](https://arxiv.org/abs/2611.30200v1)**
  - *Jitong Yang, Avinash Reddy Mudireddy, Ziqing Lu et al.*
  - `2026-11-23`
  - AI technologies and AI agents play increasingly important roles in human society, including in education, economics, and research. Adopting AI technologies can bring immediate, and sometimes tremendous, rewards such as through productivity boost, but they can also bring negative…

- **[Same Executions, Different Gaps: Judgment Rules in Web-Agent Evaluation](https://arxiv.org/abs/2611.30190v1)**
  - *Zelong Wang, Weiyue Li, Fei Xue et al.*
  - `2026-11-23`
  - Success-rate gains guide the development of web agents. Yet knowing which agent ranks first does not tell us how much confidence to place in its reported advantage. We study the comparison itself: how success is defined, what evidence supports the judgments, and how the differenc…

- **[Trustworthy agentic lunar robotics: safety-constrained contingent planning with a foundation-model planner](https://arxiv.org/abs/2611.30179v1)**
  - *Bingqi Huang, Bingchuan Wei, Yingkai Cai et al.*
  - `2026-11-23`
  - Sustained lunar-base operations require robots that restore equipment and deliver cargo under conditions unforeseen before deployment. Flown space autonomy executes pre-validated procedures and enters a safe hold outside their scope, whereas foundation models synthesize plans on…

- **[Audio-Visual Rearrangement](https://arxiv.org/abs/2611.30171v1)**
  - *Ruohao Guo, Jiatong Ye, Chenwei Dong et al.*
  - `2026-11-23`
  - We introduce Audio-Visual Rearrangement (AVR), a novel task in which an agent hears a spoken request, retrieves a suitable object, and delivers it to the requesting user or an instruction-specified destination. AVR requires the agent to understand the spoken request and acoustica…

- **[ReVAgent: Multi-Agent Reasoning-Intensive Video Generation](https://arxiv.org/abs/2611.30163v1)**
  - *Yehui Yang, Jing Fan, Jun Hu et al.*
  - `2026-11-23`
  - A central challenge in generating instructional videos for reasoning-intensive topics is to show how and why the state changes at each step. Even when an animation renders successfully, the depicted object relationships and state transitions can conflict with the explanation, mak…

- **[AutoSECO: Automated Skill Evolution for Cross-Problem Combinatorial Optimization with General-Purpose LLM Agents](https://arxiv.org/abs/2611.30139v1)**
  - *Zirui Zhu, Cong Zhang, Ni Zhang et al.*
  - `2026-11-23`
  - General-purpose large language model (LLM) agents can develop complete solvers for combinatorial optimization problems. Their specialization, however, often relies on workflows engineered for individual problems, limiting the reuse of development expertise. We propose AutoSECO, a…

- **[RoboThink: Let the Agent Think, Let the Policy Act](https://arxiv.org/abs/2611.30111v1)**
  - *Yunbei Zhang, Zijian Jin, Janet Wang et al.*
  - `2026-11-23`
  - Robot policies act in real time but fail without knowing why, whereas a reasoning agent that watches the robot can often tell what went wrong. Existing systems either hand the agent control, which takes minutes per episode, or let it send instructions. Yet a policy follows a new…

- **[Post-Training Agents for Long-Document Reasoning](https://arxiv.org/abs/2611.30090v1)**
  - *Sushant Mehta, Logan Ritchie, Edwin Chen*
  - `2026-11-23`
  - Professional documents are a long-context workload that retrieval-style benchmarks do not capture. In a ten-domain enterprise collection, a task's evidence is spread across a source document of median length 27 pages (mean 48.8, maximum 873); a third of tasks rest mainly on chart…

- **[Context-Grounded Skill Internalization for Vision-Language Agents](https://arxiv.org/abs/2611.30075v1)**
  - *Jinlin Liu, Yumeng He, Qihan Huang et al.*
  - `2026-11-23`
  - Skill internalization offers a way for agents to learn useful behaviors from skills and use them without explicit guidance in context at inference time. A common approach is to generate demonstration trajectories with the skill in context and then fine-tune the same model on its…

- **[RoboLiveMem: Is Robot Memory Solved When the World Does Not Wait?](https://arxiv.org/abs/2611.30047v1)**
  - *Yunbei Zhang, Yuyou Zhang, Janet Wang et al.*
  - `2026-11-23`
  - Robot agents built on frontier vision-language models now solve most robot memory benchmarks. Does this mean they can remember what they need in a home, where people and machines keep moving things? Existing memory benchmarks cannot answer this question, because they pause the si…

- **[SWAM: State-aware World Action Model for Multi-Agent 3D Environments](https://arxiv.org/abs/2611.30042v1)**
  - *Jenna Kang, Bingxuan Li, Colin Groth et al.*
  - `2026-11-23`
  - Interactive world models generate virtual environments autoregressively from player actions and visual history. However, visual history alone cannot reliably capture the evolving states of independently acting non-player characters (NPCs) in real games, particularly when they are…

- **[OWE-Bench: A long-horizon benchmark for measuring real-world engineering](https://arxiv.org/abs/2611.30017v1)**
  - *Jacob Cole, Martin Dimakis, Victor Barres et al.*
  - `2026-11-23`
  - We present OWE-Bench (OpenWorldEngineer-Bench), a benchmark of 26 long-horizon engineering tasks written by domain experts in software engineering, physical engineering, machine learning, and scientific computing. Tasks range from optimizing kernels and designing an aircraft, to…

- **[Antiphony: A Dual-Process Agent for Deepfake Video Detection with Real-Video Calibration](https://arxiv.org/abs/2611.29999v1)**
  - *Xinyu Yan, Yurong Hao, Zherui Li et al.*
  - `2026-11-23`
  - Reliable video deepfake detection requires generalization to unseen generators while limiting false alarms on authentic footage. Although existing detectors capture diverse visual cues, they may produce overconfident errors under generator shift, limiting the reliability of confi…

- **[Categorical Foundations of AI Agents](https://arxiv.org/abs/2611.29998v1)**
  - *Yong Wang*
  - `2026-11-23`
  - We follow the idea of separating intelligence from execution and give the categorical foundations of AI agents: the transformers, the agents, and the orchestrations and choreographies of AI agents are categorized, and which also include their coalgebras and algebras.

- **[Conartist: Adaptive Agentic Red-Teaming of Computer-Using Agents against Multi-Step Prompt Injection](https://arxiv.org/abs/2611.29977v1)**
  - *Jiaqi Rong, Yunchen Lu, Lihai Nie et al.*
  - `2026-11-23`
  - Harnesses secure Computer-Using Agents by enforcing security constraints and defending against prompt injection attacks. However, we find that two core security mechanisms of agent harnesses remain vulnerable. First, consistency checking prevents agents from deviating from legiti…

- **[CARE-3D: Reinforcement Learning for Evidence Grounded Agentic Reasoning in Situated 3D Scenes](https://arxiv.org/abs/2611.29969v1)**
  - *Xiaoqian Hu, Ruihong Qiu, Yanran Tang et al.*
  - `2026-11-23`
  - Situated 3D reasoning requires embodied agents to interpret objects, scene geometry, and viewpoint dependent spatial relations. Existing methods learn grounded interactions from supervised traces, but largely imitate prescribed evidence acquisition patterns rather than optimizing…

- **[LLM-Assisted Software Migration: from Module-Level Transformation to Repository-Level Integration](https://arxiv.org/abs/2611.29942v1)**
  - *Yanan Zhang, Shengqi Liu, Tao Zhang et al.*
  - `2026-11-23`
  - Software migration adapts an existing implementation to a new language, version, API, framework, or platform while preserving its behavior. Large language models (LLMs) succeed on individual functions and modules, but this success does not readily carry over to entire repositorie…

- **[Autonomous Multireference Quantum Chemistry with Artificial Intelligence Agents](https://arxiv.org/abs/2611.29902v1)**
  - *Younghwan Kim, Ming-Hsiu Hsieh, Ankit Mathanker et al.*
  - `2026-11-23`
  - Accurately describing chemical reactions that involve strongly correlated electrons remains a major challenge in computational chemistry. Multireference electronic structure methods can address this challenge, but their application requires expert decisions that are di!cult to au…

- **[MobileGrail: Learning Compact Guardrails for On-Device deployable Mobile GUI Agent Safety](https://arxiv.org/abs/2611.29847v1)**
  - *Zhiyu Zhang, Yuankai Li, Muhao Chen*
  - `2026-11-23`
  - Runtime guardrails protect mobile GUI agents by assessing each proposed action before execution, but existing guardrails rely on cloud hosted large multimodal models, exposing every screen to a remote server, including private information such as payments, messages, and medical r…

- **[TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming](https://arxiv.org/abs/2611.31233v1)**
  - *Hani Alomari, Md Atabuzzaman, Chris Thomas*
  - `2026-11-23`
  - CLIP-style dual encoders map images and text through two separate towers into a shared embedding space, where the two modalities occupy distinct regions separated by a modality gap. Retrieval fails when wrong matches, or hard negatives, outrank the correct one, and the gap is the…

- **[Agentic AI for Intent Management and Control in Autonomous Communication Networks](https://arxiv.org/abs/2611.31223v1)**
  - *Burak Demirel, Yu Wang, Pablo Soldati*
  - `2026-11-23`
  - Artificial intelligence (AI)-driven automation will help future mobile networks translate high-level network intents into concrete network optimization or control actions. However, existing approaches often focus on intent management and orchestration, leaving the adaptation of u…

- **[DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation](https://arxiv.org/abs/2611.30907v1)**
  - *Vinay Udit Mohan, Xuchuan Huang, Rolandos Alexandros Potamias*
  - `2026-11-23`
  - World models facilitate planning and control in robotic manipulation by enabling agents to anticipate the consequences of their actions. However, they typically rely on action-labelled interaction data that is costly to acquire and difficult to scale. These models are also often…

- **[Policy Invariance Is Not Learning Invariance: Potential-Based Reward Shaping for Navigation with a Limited View](https://arxiv.org/abs/2611.30492v1)**
  - *Nodirjon Khabibullaev, Rajat Dandekar*
  - `2026-11-23`
  - Potential-based reward shaping (PBRS) does not change the optimal policy, but how much it speeds up learning depends on the potential and on effects outside this guarantee. We analyse how PBRS changes the one-step reward while it preserves the discounted return: a per-step $(γ-1)…

- **[Optimistic Online Learning for Coding Agents with Aggregate Feedback](https://arxiv.org/abs/2611.30405v1)**
  - *Hao Luan, Hao Qiu, Zhi Zheng et al.*
  - `2026-11-23`
  - Large language model (LLM) coding agents operating on Web development platforms can interact with repositories, issue trackers, and continuous integration services to carry out long-horizon software engineering tasks. However, behavioral drift remains a major bottleneck in such m…

- **[TriSegAgent: Context-Efficient 3D Annotation with MLLMs via Tri-Planes](https://arxiv.org/abs/2611.30240v1)**
  - *Qingqiao Hu, Jialin Li, Meilong Xu et al.*
  - `2026-11-23`
  - Interactive segmentation models turn a few clicks into a segmentation prediction across domains, so annotators only decide where the prediction still needs correction. Annotation thus becomes a loop of inspecting the prediction and clicking again. Each step of this loop is a visu…

- **[Composing Independently Distilled Memory and Retrieval Policies for Long-Term Agents](https://arxiv.org/abs/2611.30230v1)**
  - *Grigorii Davydenko, Artem Sakhno, Igor Pavlov et al.*
  - `2026-11-23`
  - Long-lived Web assistants require effective memory and retrieval mechanisms to access information from past user interactions. While these capabilities can be learned through specialized policies, it remains unclear whether specialists trained independently in different environme…

- **[Reading the Tea Leaves, Again: Can Large Language Models Predict Language Model Training Runs?](https://arxiv.org/abs/2611.30141v1)**
  - *Xinran Zhao, Xiang Li, Tong Chen et al.*
  - `2026-11-23`
  - LLM agents now propose research ideas and run the experiments that test them, but they train every run to its end, whereas a researcher reads a run's configuration and the beginning of its curve and stops the runs that show no promise. Reading a run this way takes more than descr…

- **[Sequential Selection against an Adaptive Opponent](https://arxiv.org/abs/2611.30006v1)**
  - *Zhongyuan Lyu, Xiaocong Xu*
  - `2026-11-23`
  - Selecting a strategy by testing it against an opponent is common in game-playing AI, red-teaming of language models, and safety evaluations of AI agents. In many of these settings, the opponent adapts to what it observes, so a strategy that keeps winning in practice may already h…

- **[VADE: A Verifiable Agent Data Engine from Professional Sources](https://arxiv.org/abs/2611.30202v1)**
  - *Xiangchao Chen, Zhiheng Lyu, Kai Zhang et al.*
  - `2026-11-23`
  - Language agents have shown their practical value, particularly in software engineering, where abundant public code and executable tests support training and evaluation at scale. Extending this success to other professional domains, such as law and finance, is not straightforward:…

- **[Retrieval-Augmented Generation in the Agentic Era: Tradition, Present, and Prospect](https://arxiv.org/abs/2611.30181v1)**
  - *Chenming Tang, Haolin Li, Yiran Li et al.*
  - `2026-11-23`
  - Retrieval-augmented generation (RAG) couples frozen language models with external, updatable knowledge, so that generation is grounded in retrieved evidence rather than in parametric memory alone. This work maps RAG in the agentic era by joining them on a single lifecycle axis, f…

- **[SHAKTI: Evidence-Grounded Conversational AI for Nutrition and Health](https://arxiv.org/abs/2611.29988v1)**
  - *Chaitanya Pallerla, Dongyi Wang*
  - `2026-11-23`
  - Large language models (LLMs) answer many diet and health questions but can state unsupported claims and cite sources that do not support them. We present SHAKTI (Smart Health Advisor for Knowledge-based Tailored Interventions), a conversational assistant that answers only from re…

- **[GlobalHRBench: Does Changing the Question Language Change the Legal Answer?](https://arxiv.org/abs/2611.29852v1)**
  - *Yuding Wang, Yuhang Yao*
  - `2026-11-23`
  - Language matters when deploying LLM agents across borders, especially in law, where the governing rules must hold across working languages. Does changing the language of a legal question change answer accuracy? We introduce GlobalHRBench, pairing 240 employment-law problems acros…

- **[From joint attention to shared symbols: A free-energy principle account](https://arxiv.org/abs/2611.30788v1)**
  - *Tadahiro Taniguchi, Koji Hashimoto, Ryuichiro Ishikawa*
  - `2026-11-23`
  - Joint attention precedes vocabulary acquisition. How can attending to the same object help two people with different sensory experiences come to use a shared word? In a free-energy principle account, marginalizing the common object induces a statistical dependence between private…

- **[AgentBouncer: Defending Software Engineering Agents via Dynamic System-Call Mediation](https://arxiv.org/abs/2611.30621v1)**
  - *Pascal Joos, Michael Pradel*
  - `2026-11-23`
  - Software engineering (SE) agents can complete diverse engineering tasks by interacting with the development environment via tools that access files, run commands, and download resources. Unfortunately, the same ability that makes SE agents useful also makes them prone to performi…

- **[Causal Evidence for the Emergence and Spread of Reward Hacking in AI Agent Swarms](https://arxiv.org/abs/2611.30185v1)**
  - *Sumer S. Vaid*
  - `2026-11-23`
  - Autonomous AI agents that coordinate and collaborate among each other have become pervasive across domains ranging from scientific research to finance and engineering. The opportunity to share messages and build upon each other's work also creates the potential for misaligned beh…

- **[TRAE: Trustworthy Automated ESG Annotation via Multi-Agent Consensus and Confidence Assessment](https://arxiv.org/abs/2611.30035v1)**
  - *Jaeyoung Lee, Misuk Kim*
  - `2026-11-23`
  - With the growing demand for ESG disclosure and evaluation, constructing high-quality datasets for automatically extracting ESG-related information from large-scale documents has become essential. However, ESG annotation remains challenging due to strong context dependence, ambigu…

- **[Who Makes the Decision? Auditing an Agentic LLM Pipeline for Illicit Cryptocurrency Transaction Monitoring](https://arxiv.org/abs/2611.29829v1)**
  - *Vaishnavi Chaughule, Yuchen Zhang, Mohammed Ahnaf Tajwar et al.*
  - `2026-11-22`
  - Agentic pipelines that combine graph detectors, deterministic rules, retrieval-augmented generation and an LLM judge are being proposed to monitor illicit cryptocurrency flows and to write regulation-citing justifications for analysts. They are evaluated on end-to-end accuracy or…

- **[Memphis: A Case Study in Seeding an Agent Task from a Model's Real-World Attempt](https://arxiv.org/abs/2611.29824v1)**
  - *Ibrahim A. Ahmed, Ahmed Sameh Khalil*
  - `2026-11-22`
  - Agent benchmarks are usually made harder by scaling up the data their tasks are built from, yet models that do well on them still fail at real work. We propose building simulated tasks from a model's own attempt at an open-ended task in the real world, so that the model's failure…

- **[Can Vibe Coding Produce Accessible Websites: An Empirical Study on LLM Coding Agents and Skills](https://arxiv.org/abs/2611.29822v1)**
  - *Syed Fatiul Huq, Md. Asif Haider, Abu Jafar Saifullah et al.*
  - `2026-11-22`
  - Large language model (LLM) coding agents increasingly allow developers and non-professionals to create websites through natural-language instructions, with limited inspection of the generated source code. Although this ``vibe coding'' workflow lowers barriers to software creation…

- **[Notes on Generative AI for Mathematical Research](https://arxiv.org/abs/2611.29811v1)**
  - *Shurui Liu*
  - `2026-11-22`
  - These notes describe how generative AI is now used to solve and to check research-level mathematics, with a focus on agents and their harnesses. For the proving agents Rethlas, Danus, and Pharos and the verification agent OSVerify, we explain the design principles, compare each w…

- **[Blind to What They Can Fix: A Detection Gap in Self-Improving Agents](https://arxiv.org/abs/2611.29807v1)**
  - *Teng Cao, Yu Deng, Kristian Kersting*
  - `2026-11-22`
  - AI agents can write programs that carry out a task without calling a model at every step, so the task runs fast and its logic stays open to inspection. Agents improve these programs by running them, studying their failures, and revising the code, a form of recursive self-improvem…

- **[Dimension Is Free, Horizon Is Not: When Evolution Strategies Rival Policy Gradients for LLM Fine-Tuning](https://arxiv.org/abs/2611.29795v1)**
  - *Qiyao Liang, Kajetan Schweighofer, Xin Qiu et al.*
  - `2026-11-22`
  - Policy gradient (PG) methods such as GRPO dominate LLM fine-tuning, yet recent work showed that Evolution Strategies (ES) also scale to fine-tuning models with billions of parameters. Which method needs fewer samples, and on which tasks, remains unclear. We view the two methods a…

- **[Why Units Die in the Layer After a Frozen Random Encoder, and What the Number of Live Units Measures](https://arxiv.org/abs/2611.29752v1)**
  - *Scott M. Norton*
  - `2026-11-22`
  - Reinforcement-learning agents can learn Atari games through a convolutional encoder whose random weights are never trained. They reach expert play in Pong and, without random action repeats, in Breakout, but training takes far longer and few ReLU units in the layer after the enco…

- **[Reinforcement Learning from LLM-Generated (Suboptimal) Demonstrations](https://arxiv.org/abs/2611.29732v1)**
  - *Anurag Kadkol, Lawson L. S. Wong*
  - `2026-11-22`
  - Reinforcement learning (RL) has achieved substantial progress across many domains, but training an agent \textit{tabula rasa} remains highly sample-inefficient. A common remedy is to initialize the agent using a neural network pretrained on demonstrations. However, collecting dem…

- **[Admitted Is Not Effective: Lessons from a Notary-Gated Retrospective Loop in an Agentic Pipeline](https://arxiv.org/abs/2611.29727v1)**
  - *Lo Gullstrand Heander, Emma Söderberg, Christofer Rydenfält*
  - `2026-11-22`
  - Agentic software development pipelines with frozen prompts can repeat the same mistakes across pull requests (PRs), yet ungoverned additions to instruction files grow without bound and do not generally improve task success. We present a retrospective loop for a four-stage large l…

- **[Fin-RSI: A Unified Library of Financial Skills, Checks, and Self-Improvement for LLM Agents](https://arxiv.org/abs/2611.29716v1)**
  - *Wanghao Ye, Shwai He, Sihan Chen et al.*
  - `2026-11-22`
  - As large language models (LLMs) become more capable, financial agents need tools they can readily discover and use. Yet financial software is fragmented across libraries with different interfaces and conventions, making it difficult to build reliable agent workflows. We present F…

- **[Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits with LLM Agents](https://arxiv.org/abs/2611.29613v1)**
  - *Junpeng Hou, Jiaxing Qu, Derek Cheng et al.*
  - `2026-11-22`
  - Web-scale recommender models evolve primarily through retraining or fine-tuning. We propose \emph{weight coding}, a methodology for model evolution through direct, executable weight edits. A large language model (LLM) agent inspects model structure and parameters, formulates hypo…

- **[Non unitary and nonlinear quantum generative large model design and fast large-scale training without back propagation](https://arxiv.org/abs/2611.29571v1)**
  - *Tianze Zhu, Xiaofeng Jiang, Min Liao et al.*
  - `2026-11-22`
  - Transformer-based large models require huge computational and storage costs. Quantum computation is expected to address that due to its potential to speed up classical algorithms exponentially. Key challenges of implementing quantum large models include the linear, unitary nature…

- **[Layer-Level Control of Language Model Execution in Agent Frameworks](https://arxiv.org/abs/2611.29519v1)**
  - *Ran Guan, Yiqi Lin, Xiangxi Tian et al.*
  - `2026-11-22`
  - Agent frameworks typically orchestrate language models through prompt-and-response interfaces. We propose a harness design that exposes intermediate model states and layer-level execution controls to the agent runtime. By connecting state collection, policy fitting, and execution…

- **[MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model](https://arxiv.org/abs/2611.29501v1)**
  - *Rongze Tang, Chenyu Zhou, Jianjie Fang et al.*
  - `2026-11-22`
  - World action models (WAMs) excel at robot manipulation by imagining future observations and decoding actions from them, yet remain confined to a single embodied agent. In practice, manipulation often requires multiple robots to collaborate across disjoint workspaces, coupled timi…

- **[Beyond Accuracy: A Diagnostic Benchmark for Hypothesis-Driven Experiment Planning in LLM Agents](https://arxiv.org/abs/2611.29467v1)**
  - *Ryo Kuroki, Amin Mansouri, Philippe Schwaller*
  - `2026-11-22`
  - Evaluating large language model (LLM) agents on scientific tasks typically reduces to final-task accuracy, which obscures where reasoning succeeds or breaks down. We introduce a benchmark and diagnostic evaluation framework for hypothesis-driven adaptive experimental planning in…

- **[Agentic Discovery of Simple Symbolic Inventory Policies](https://arxiv.org/abs/2611.29440v1)**
  - *Xi Chen, Yuze Chen, Baichuan Mo et al.*
  - `2026-11-22`
  - Designing simple inventory policies becomes increasingly difficult as operational features and system configurations expand. We develop an Agentic Inventory-Policy Discovery System based on explicitly defined simple operational formula (SOF) policy and template classes. Large lan…

- **[Emotion-Aware and Context-Grounded Dialogue Agents for Personalized Video Game Interactions](https://arxiv.org/abs/2611.29372v1)**
  - *Michael Adjeisah, Jin Zhang, Pierluigi Vito Amadori et al.*
  - `2026-11-22`
  - We present ChatNPC, a game companion that dynamically personalizes its responses in real time based on players' emotional shifts to enhance user immersion. The model integrates sequential data, leveraging the dynamic nature of streams to benefit from player information, spoken li…

- **[SAE-Audit: Clinical-Trial Prediction via Inference-Time Optimization of Black-Box LLMs Audited by Sparse Autoencoder Evidence](https://arxiv.org/abs/2611.29368v1)**
  - *Junbo Shen*
  - `2026-11-22`
  - Clinical trials are costly and often take years to complete, making early outcome prediction valuable for trial planning. Large language models (LLMs) are increasingly used to forecast clinical-trial outcomes, yet their predictions remain unreliable and their rationales may not f…

- **[EMIP: Embodied Multi-Party Interaction Platform](https://arxiv.org/abs/2611.29333v1)**
  - *Koichiro Terao, Rikunari Sagara, Moe Nagao et al.*
  - `2026-11-22`
  - Experimental platforms that enable multiple participants to engage in spoken dialogue and perform physical actions concurrently in a shared environment are important for studying cooperation between humans and embodied AI agents. In this paper, we propose EMIP (Embodied Multi-Par…

- **[DoppelVet: Comparative Safety Verification for Self-Evolving Agents](https://arxiv.org/abs/2611.29306v1)**
  - *Yifan Duan, Du Yin, Siyuan Zheng et al.*
  - `2026-11-22`
  - Self-evolving agents improve by retaining feedback as reusable memories or skills, but every mistaken approval can shape many future behaviors. Two updates can provide exactly the same evidence to a verifier yet produce opposite safety outcomes, so the verifier cannot distinguish…

- **[From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303v1)**
  - *Saadh Jawwadh*
  - `2026-11-22`
  - The rapid proliferation of Large Language Model (LLM) research makes it increasingly difficult to distinguish incremental refinements from true paradigm shifts. This review evaluates 22 of the most influential publications spanning nearly three decades (1997-2026), organized thro…

- **[Which Failure Does an Intervention Repair? When Agent Interventions Help, and Where Self-Evolving Skills Stall](https://arxiv.org/abs/2611.29290v1)**
  - *Zihan Jin, Gaoyuan Du, Jiate Li et al.*
  - `2026-11-22`
  - An intervention that improves one agent can break another, and adding a stronger harness on top need not repair the damage. Agent interventions such as skills, harnesses, and extra inference budget are nonetheless usually credited with one average gain, measured under one setup.…

- **[MetaSkill: Reusable Problem-Solving Methods for Adaptive Skill Orchestration in LLM Agents](https://arxiv.org/abs/2611.29274v1)**
  - *Tianxing Wang, Mingming Zhao, Shuai Huang et al.*
  - `2026-11-22`
  - Reusable skills provide specialized procedures, but large language model (LLM) agents must still determine how to organize and adapt their use. We introduce MetaSkill, a two-layer framework for reusing problem-solving methods across tasks and domains. The method layer selects fro…

- **[Neural Agent Compiler: Learning to Schedule Soft Dependencies](https://arxiv.org/abs/2611.29262v1)**
  - *Bo Yan, Peng Wang, Zihan Chen et al.*
  - `2026-11-22`
  - Large language model agents accomplish complex tasks by coordinating multiple reasoning steps and tool operations, which form dependencies among their operations. Existing orchestration methods primarily consider hard dependencies that determine when an operation can legally begi…

- **[Look Back: Reinforcement Learning with Counterfactual World Models](https://arxiv.org/abs/2611.29259v1)**
  - *Jinwoo Kim, Toghrul Abbasov, Lucius E. J. Bynum et al.*
  - `2026-11-22`
  - Agents in complex, stochastic environments must contend with dynamics that can exceed their world models' predictive capacity and randomness that obscure the consequences of their actions. We hypothesize that, compared to imagining entirely new trajectories in such complex enviro…

- **[NoeVera: Can Knowledge Guide Experiments and Experiments Refine Knowledge?](https://arxiv.org/abs/2611.29255v1)**
  - *Pinaki Prasad Guha Neogi, Spyros Mastorakis, Ankur Mallick et al.*
  - `2026-11-22`
  - With the growing demand for large language model (LLM) services, optimizing LLM serving systems is becoming increasingly complex, and the bottleneck is no longer predicting how a given configuration will perform. The harder problem is deciding what to investigate: which mechanism…

- **[Seeing Is Not Acting: WARD Diagnoses the Evidence-to-State-to-Action Gap in Longitudinal Clinical Agents](https://arxiv.org/abs/2611.29243v1)**
  - *Chao Ding, Yidong Jiang, Junzhi Ning et al.*
  - `2026-11-22`
  - Large language models for longitudinal clinical care must revise their assessments and actions as patient information accumulates. However, benchmarks centered on isolated responses or final task outcomes provide limited insight into intermediate failures in evidence use, state u…

- **[Direct Feedback Policy Optimization for AI Coding Agents](https://arxiv.org/abs/2611.29193v1)**
  - *Fei Ding*
  - `2026-11-22`
  - AI coding agents generate, modify, and validate code through multi-turn interactions. Existing reinforcement learning methods often rely on sparse terminal rewards, making it difficult to assess how intermediate decisions affect task outcomes, and group-relative methods also requ…

- **[On Adaptive Step Sizes for Eligibility Traces in Deep Reinforcement Learning](https://arxiv.org/abs/2611.29178v1)**
  - *Esraa Elelimy, Martha White*
  - `2026-11-22`
  - Many deep reinforcement learning (RL) algorithms store agent-environment interactions in a replay buffer and later learn by sampling transitions from it. However, this approach can be memory-inefficient and can delay learning because the agent can learn from a transition only whe…

- **[Fixed or Deleted? External Feedback Lets Cheaper AI Coding Agents Repair Rule Violations](https://arxiv.org/abs/2611.29162v1)**
  - *Laura Wynter*
  - `2026-11-22`
  - Many defects violate project rules that the code itself does not reveal, such as layering constraints or required tests. We study whether LLM coding agents repair such violations better when an external checker reports them, with their location and a repair goal. Three models, a…

- **[ContextFact: Remembering Facts in Context for Long-Term Conversational Agents](https://arxiv.org/abs/2611.29155v1)**
  - *Jiayu Huang, Yichao Cai, Xinyu Li et al.*
  - `2026-11-22`
  - Agents built on large language models must maintain continuity across repeated interactions with users. However, long-term conversations scatter facts across turns and sessions, making it difficult to retrieve the right evidence with enough context. Memory for such conversations…

- **[MVAgent: Per-Video Agents under Global Coordination for Multi-Video Understanding](https://arxiv.org/abs/2611.29154v1)**
  - *Kewei Wei, XueXiang Wen, Bocheng Hu et al.*
  - `2026-11-22`
  - Multi-video understanding requires systems to combine evidence from different videos for cross-video reasoning. Answering such questions involves two kinds of decisions. Observation decisions must adapt to each video's content, whereas cross-video judgments require relating evide…

- **[Can an Agent Trust Its Own Zoom? Cross-Magnification Provenance Verification for Whole-Slide Images](https://arxiv.org/abs/2611.29150v1)**
  - *Yan Wang, Yiran Song, Zizhuo Gong et al.*
  - `2026-11-22`
  - Visual agents navigate whole-slide images through magnified observations associated with claimed locations. However, a visually plausible observation does not necessarily originate from its claimed location, particularly across magnifications and in regions with similar tissue st…

- **[The Retry Tax: Why Static Same-Task Retries Can Cost More per Completion](https://arxiv.org/abs/2611.29133v1)**
  - *Wei-Jung Huang*
  - `2026-11-22`
  - Retrying an agent after failure can complete more tasks while increasing the cost per completion. We study a static policy that stops at verified success or an attempt cap and otherwise resets the original prompt and workspace without passing feedback to the next request. Under s…

- **[CoHABIT: Complementary Evaluation of Furniture Layouts through Spatial Rules and Household Routines](https://arxiv.org/abs/2611.29494v1)**
  - *Ewsey Obzherin, Samira Atlangirieva, Anastasia Antsiferova et al.*
  - `2026-11-22`
  - We introduce CoHABIT, a framework for evaluating furniture layouts through complementary spatial rules and household routines. Static assessment captures geometric validity, ergonomic access, functional organization, and configurable design preferences, including Feng Shui. Dynam…

- **[Benchmarking Web Agent Defenses Against Adaptive Visual Prompt Injection](https://arxiv.org/abs/2611.29268v1)**
  - *Haichuan Zhang, Zhiyuan Zhong, Shih-Chieh Dai et al.*
  - `2026-11-22`
  - Multimodal web agents automate website interactions but remain vulnerable to visual prompt injection (VPI), where malicious webpage content manipulates their visual processing and induces unintended actions. Although several defenses focus on detecting injected instructions in sc…

- **[Where Do Fact-Checking Errors Arise? Separating Retrieval, Search Control and Judgement in Evidence-Grounded Verification](https://arxiv.org/abs/2611.29697v1)**
  - *Martin Pavlíček, Martin Kotyrba, Eva Volná et al.*
  - `2026-11-22`
  - An evidence-grounded fact-checker can fail because it does not find the evidence or because it does not use it; end-to-end accuracy does not tell the two apart. We present a protocol that follows the reference evidence from the store to the verdict and separates retrieval, search…

- **[MAS-BIT: A Multi-Agent System for End-to-End BraIn-to-Text Decoding](https://arxiv.org/abs/2611.29457v1)**
  - *Xinjie Zhang, Linyang He, Yizi Zhang et al.*
  - `2026-11-22`
  - Speech brain-computer interfaces aim to restore communication by translating neural activity into text, yet end-to-end decoders have historically trailed cascaded systems in accuracy. We introduce a Multi-Agent System for BraIn-to-Text (MAS-BIT), the first multi-agent framework f…

- **[VistaTree: Question Answering over Long Multimodal Documents with Image-Derived Summary Trees](https://arxiv.org/abs/2611.29419v1)**
  - *Yexiang Cheng, Xiaochen Zheng, David Tokar et al.*
  - `2026-11-22`
  - Answering questions over long multimodal documents requires locating relevant evidence across pages containing text, tables, and figures. When the document exceeds the model's context window, selective retrieval becomes necessary. We introduce VistaTree, a document question-answe…

- **[Endpoint-Conditioned Process Value: What an Endpoint-Blind Process Score Adds Once Terminal Status and Cost Are Known](https://arxiv.org/abs/2611.29354v1)**
  - *Chris D Yan, Ken Wang, MarkX Qian et al.*
  - `2026-11-22`
  - Trajectory metrics promise information beyond final-answer accuracy, but no one has measured what a process score adds once an evaluation knows the outcome and the cost. We build that comparison: a sealed consequence needing an artifact neither agent nor judge ever sees, an opera…

- **[Edit-Induced Dependency Mismatch: Propagation Omissions, Recovery, and Evaluation Blind Spots in Coding Agents](https://arxiv.org/abs/2611.29242v1)**
  - *Fei Ding*
  - `2026-11-22`
  - During iterative code modification, coding agents may continue to rely in subsequent reasoning on outdated dependency judgments whose text remains fixed in the context, leading to errors in subsequent reasoning and leaving consumer defects undetected by the original task evaluati…

- **[AEP:Towards Trustworthy Agent Communication, Networking, and Collaboration](https://arxiv.org/abs/2611.29598v1)**
  - *Yuhao Wang, Shengfang Zhai, Xinyu Zhou et al.*
  - `2026-11-22`
  - As privately owned agents become increasingly capable, collaboration in open agent networks is limited by partial topology knowledge, ownership boundaries, and the risk of exposing or contaminating private context. Existing agent-to-agent protocols are useful when collaborators a…

- **[Social Interaction Breaks Replicate Independence in Controlled-Clone LLM Agents](https://arxiv.org/abs/2611.29581v1)**
  - *Yandan Zheng, Haoran Luo, Anh Tuan Luu*
  - `2026-11-22`
  - Multi-agent LLM evaluations and social simulations create many agents from one model and treat them as independent replicates, even after the agents interact. This assumption remains untested with matched controls. We introduce SocCogEval, a controlled-clone assay for Social Cogn…

- **[Real-Time Kinodynamic Multi-Agent Motion Planning](https://arxiv.org/abs/2611.29548v1)**
  - *Jiarui Li, Runyu Zhang, Gioele Zardini*
  - `2026-11-22`
  - Coordinating large robot fleets, from warehouses to quadrotor swarms, requires collision-free trajectories that satisfy dynamic constraints and stay within speed and acceleration bounds. Existing kinodynamic multi-agent planners enforce these bounds during the search or through t…

- **[ARRANGE: Agentic Skills for Layering Vocals](https://arxiv.org/abs/2611.29283v1)**
  - *Henry Tan, Eidee Tan*
  - `2026-11-22`
  - Adding a singing voice to an existing piano recording requires decisions about melody, syllable placement, pronunciation, timing, and vocal register. ARRANGE organizes this work as a sequence of agent skills with readable intermediate artifacts and composer approval checkpoints.…

- **[BenchMint: From Real-World Tasks to Executable Benchmarks](https://arxiv.org/abs/2611.29367v1)**
  - *Zining Huang, Zuo Wang, Mengyao Zhang et al.*
  - `2026-11-22`
  - Large language models (LLMs) need evaluations of everyday reasoning and tool use, such as planning itineraries under user constraints and grounding numerical answers in evidence. We introduce BenchMint, an automated benchmark-construction workflow, and Daily-Life, its collection…

- **[Do LLM Agents Compromise Like Humans? Risk and Responsibility in Dyadic Decision-Making](https://arxiv.org/abs/2611.29069v1)**
  - *Noah S. Okada, Ketika Garg, Wenning Deng et al.*
  - `2026-11-21`
  - Large language model (LLM)-based agents are increasingly deployed in settings where they must collaborate to make joint decisions. We investigate how this collaboration unfolds under risk, asking whether agents adjust their choices to accommodate their partners, how they assign r…

- **[Do You Even Know What I Want? Improving LLMs Ability to Detect Hidden User Intent](https://arxiv.org/abs/2611.29028v1)**
  - *Kelsey Sikes, Sarath Sreedharan*
  - `2026-11-21`
  - As with conventional AI agents, a common source of misalignment between Large Language Models (LLMs) and their human users is misspecified goals. Often, this happens when the human has skewed beliefs about the system's model and provides it with information that causes behavior d…

- **[Population-Based Post-Training for Large Language Models](https://arxiv.org/abs/2611.29014v1)**
  - *Yixuan Even Xu, Aleksei Petrenko, Raja Giryes et al.*
  - `2026-11-21`
  - Reinforcement learning with verifiable rewards (RLVR) is one of the most popular post-training paradigms for large language models. RLVR typically trains a single model under hyperparameters chosen before training begins, while researchers tune hyperparameters across consecutive…

- **[Mind the Trap As LLMs Guess the Data Model: Grain-Aware Guards Against Fan-out in Text-to-SQL and Its Benchmarks](https://arxiv.org/abs/2611.29009v1)**
  - *Ahmed M. Mahran*
  - `2026-11-21`
  - Text-to-SQL systems built on large language models (LLMs) often aggregate over one-to-many and many-to-many joins, a classic trap: when the joined rows repeat an entity, a SUM or COUNT counts it more than once, yet the query runs and returns a plausible number. We characterize th…

- **[Consumer-Time Validity in Stateful AI Runtimes: Verifying Recovered State and Deferred Authority](https://arxiv.org/abs/2611.29004v1)**
  - *Guijia Zhang, Huihao Jing, Bing Li et al.*
  - `2026-11-21`
  - Stateful LLM serving engines and agent runtimes reuse execution state and deferred permissions across components and sessions. A cancellation, rollback, or approval is recorded by one component and relied on by another, and recording it does not make the later use valid: a downst…

- **[STRIDE: Strategy-to-Tactics Retrieval-Guided Skill Disclosure and Evolution for Agentic Reinforcement Learning](https://arxiv.org/abs/2611.28907v1)**
  - *Shixin Hong, Wanqing Cui, Yibo Hu et al.*
  - `2026-11-21`
  - Skill-augmented reinforcement learning enables LLM agents to reuse task-solving knowledge across episodes, but existing systems typically expose agents to a flat skill pool and update skills only from coarse, episode-level outcomes. This conflates two distinct uses of experience:…

- **[StudioBench: Benchmarking Agentic Multimodal Large Language Models for Productive Audiovisual Creation](https://arxiv.org/abs/2611.28902v1)**
  - *Xinglong Xu, Yuxia Zhu, Siyuan Li et al.*
  - `2026-11-21`
  - Video generators can now render convincing short clips, yet complete audiovisual works require coordinating visuals, sound, and editing across multiple stages. Existing benchmarks focus on individual generators or video agents under narrower production settings, leaving end-to-en…

- **[EA-Bench: Measuring information and action efficiency under imperfect instructions](https://arxiv.org/abs/2611.28846v1)**
  - *Xu Wan, Wenyue Xu, Shenjie Zhao*
  - `2026-11-21`
  - Personal agents help users complete everyday work across digital applications. Many standard benchmarks assume that users provide sufficient information to solve a task. However, agents often encounter incomplete, distracting, or inconsistent information in practice. To systemati…

- **[DiscernBench: Evaluating Cooperative Discernment of LLM Agents in Institutional Settings](https://arxiv.org/abs/2611.28787v1)**
  - *Disha Sheshanarayana, Tanishka Magar*
  - `2026-11-21`
  - The deployment of large language models in operational settings demands evaluation of judgment under institutional constraint. We introduce DiscernBench, a benchmark for evaluating cooperative discernment: the ability of an agent to determine whether to comply with, refuse, or es…

- **[SkillLens: An Interactive Human-LLM System for Diagnosing and Refining Agent Skills](https://arxiv.org/abs/2611.28706v1)**
  - *Shuo Yan, Rui Sheng, Xiaoyan Gu et al.*
  - `2026-11-21`
  - LLM agents increasingly rely on reusable skills, yet maintaining them requires developers to connect revisions with changes in behavior and task outcomes. Existing workflows fragment evidence across versions, evaluation cases, and execution traces. We present SkillLens, an intera…

- **[Improving the Improver: Semantic PID Control for Medical Agent Self-Improvement](https://arxiv.org/abs/2611.28680v1)**
  - *Dexia Chen, YiLong Hu, Wenqi Zhong et al.*
  - `2026-11-21`
  - High-stakes vertical medical tasks, such as postoperative pathological staging and long-term survival prediction, demand multi-step clinical reasoning over heterogeneous evidence under weak supervision and high outcome uncertainty. While we first orchestrate CliAgent, a domain-ta…

- **[The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates](https://arxiv.org/abs/2611.28671v1)**
  - *Haoyuan Zheng, Dongting Li, Hancheng Ye et al.*
  - `2026-11-21`
  - Multi-agent systems (MAS) usually coordinate heterogeneous models and tools to solve complex tasks, creating a growing need for reliable evaluation. However, a multi-agent workflow that is fastest in one serving environment can lose its advantage in another, even when its models,…

- **[Persuasion from Within: Model-Based Insider Attacks in Multi-Agent LLM Debate and Consensus](https://arxiv.org/abs/2611.28660v1)**
  - *Bangyan Ju, Xiaolin Sun, Yibin Hu et al.*
  - `2026-11-21`
  - Large language models (LLMs) are increasingly deployed in multi-agent systems for collective decision-making, such as multi-agent debate and consensus games, in which agents exchange messages and update their answers over multiple rounds and a resolution mechanism aggregates them…

- **[LoopSeek: Decoupling System One Search from System Two Answering for Long Video Understanding](https://arxiv.org/abs/2611.28635v1)**
  - *Chengzhong Wang, Lang Lin, Xinyang Liu et al.*
  - `2026-11-21`
  - Long video question answering requires finding relevant evidence before reasoning over it. With a limited frame budget, single-pass frame selection can miss critical evidence, while adaptive search often relies on repeated text generation to decide where to look. We introduce Loo…

- **[VeriLadder: A Multi-Agent Specification Refinement System for Tool-Verified Verilog Datasets](https://arxiv.org/abs/2611.28617v1)**
  - *Saeid Rajabi, Chengmo Yang, Satwik Patnaik*
  - `2026-11-21`
  - Training data is a bottleneck in AI, especially for large language models (LLMs) that write Verilog, because register-transfer-level (RTL) code is rarely published and existing datasets mostly check code for syntax, not instruction correctness. This paper presents VeriLadder, a f…

- **[Action-Conditioned Transition Irreversibility for Out-of-Distribution Detection in Reinforcement Learning](https://arxiv.org/abs/2611.28611v1)**
  - *Emil Mittag, Richard Dazeley, Peter Vamplew*
  - `2026-11-21`
  - Reinforcement-learning agents shape the observations they encounter; consequently, detecting out-of-distribution (OOD) states requires analysing action-conditioned trajectories rather than treating inputs as independent samples. We propose Action-Conditioned Transition Irreversib…

- **[Agent Money Benchmark: Can AI Agents Be Trusted to Spend Money?](https://arxiv.org/abs/2611.28610v1)**
  - *Zhe Chen, Emma Hsieh, Vicky Fu*
  - `2026-11-21`
  - Giving an AI agent a wallet lets it buy data and services on a client's behalf. Trust then depends on how it spends money and what that spending achieves. We introduce Agent Money Benchmark (AMB) to test whether agents spend a client's money well, starting with purchases of infor…

- **[EvoViM: Recursively Self-Evolving Visual Agents for Exploration with Deferred Queries](https://arxiv.org/abs/2611.28574v1)**
  - *Xinyu Cao, Tianjie Ju, Zhuosheng Zhang*
  - `2026-11-21`
  - Multimodal large language model (MLLM) agents have shown promising capabilities in task-oriented environments. However, they still struggle when queries are deferred until after exploration, requiring them to retain visual evidence before knowing which details will matter. We int…

- **[From Reward Engineering to Data-Centric Reinforcement Learning for Effective Agentic Visual Tool Use](https://arxiv.org/abs/2611.28558v1)**
  - *Jin Cui, Xinyue Long, Jiepeng Zhou et al.*
  - `2026-11-21`
  - Multimodal large language models (MLLMs) increasingly use external visual tools to acquire evidence during reasoning, yet learning when to invoke these tools remains challenging. Existing tool-use reinforcement learning (RL) methods often rely on call-contingent rewards to encour…

- **[Digital Twins for Multi-Agent Systems: When to Trust, What to Change](https://arxiv.org/abs/2611.28517v1)**
  - *Truc Nguyen Thi Le, Phuoc Nguyen T. H*
  - `2026-11-21`
  - Digital twins of agent networks need to flag unreliable forecasts and help users choose interventions. Both decisions depend on what happens over several steps: an error can spread through the network, and an edit whose trajectory is easy to predict may still yield a poor collect…

- **[Don't Train It, Write It: An AI Agent Writes New Capabilities into Language Model Weights](https://arxiv.org/abs/2611.28483v1)**
  - *Santiago Rivadeneira Quintero*
  - `2026-11-21`
  - We show that an AI agent can write new capabilities into a pretrained language model by adding gated attention heads and MLP neurons inside its existing layers, without backpropagation and without fitting any weight to the answers of task examples. It has a budget of 50 model pas…

- **[ESM-Bench: A Benchmark for Evaluating Whether AI Agents Understand Earth System Model Physics and Code](https://arxiv.org/abs/2611.28477v1)**
  - *Koutian Wu, Yuxuan Cao, Gengchen Mai et al.*
  - `2026-11-21`
  - AI coding agents that modify Earth System Model (ESM) code must preserve both software interfaces and the physical assumptions encoded in them. We introduce ESM-Bench, a benchmark of 60 developer-commit tasks from 6 repositories: Noah-MP, CLM5, SUMMA, ParFlow, MOM6, and VIC. The…

- **[Automated Safety Analysis for Agentic Workflows](https://arxiv.org/abs/2611.28469v1)**
  - *Yanju Chen, Ying Li, Bosi Zhang et al.*
  - `2026-11-21`
  - LLM applications are increasingly built as agentic workflows: programs that combine model calls, external tools, and control logic to act autonomously on a user's behalf. Because these workflows execute real-world actions, logical flaws in how a workflow is wired can cause severe…

- **[Human-in-the-Loop Runbook Improvement with Agentic Support Automation](https://arxiv.org/abs/2611.28441v1)**
  - *Rocker D'Antonio, Harry Xie*
  - `2026-11-21`
  - Operational support is an important component of production software services. Support requests are often emergent and can come in many forms such as customer escalations or unplanned service interruption. Engineers across organizations have been successful in implementing automa…

- **[Aegis: A Conversational Prototype for Lung Cancer Risk Information and Follow-up](https://arxiv.org/abs/2611.28642v1)**
  - *Bowen Han, Chengwei Cao, Runxin Zhang et al.*
  - `2026-11-21`
  - Collecting self-reported risk information and maintaining continuity between assessment, explanation, and follow-up are practical components of a lung cancer screening workflow. We present Aegis, a browser-based research prototype that combines a conversational questionnaire, rul…

- **[Nearly Minimax-Optimal Sample Complexity of Natural Policy Gradient with a Matching Information-Theoretic Lower Bound](https://arxiv.org/abs/2611.28628v1)**
  - *Asha Barua, Sajad Khodadadian*
  - `2026-11-21`
  - A fundamental question in reinforcement learning is how many sampled transitions are needed to learn a near-optimal policy, and whether direct policy optimization can attain this statistical limit. To answer this question, we consider natural policy gradient (NPG), a widely used…

- **[Digital Knockoffs](https://arxiv.org/abs/2611.28482v1)**
  - *Niuniu Zhang*
  - `2026-11-21`
  - Social simulations often use language model agents to represent people who differ on several measurable traits. However, describing a trait profile in a prompt does not guarantee the agent will express each trait at its intended level. We propose a method that calibrates agents t…

- **[When a Permitted Action Completes a Forbidden Workflow: Designing Consequence-Oriented Approval for LLM Agents](https://arxiv.org/abs/2611.28454v1)**
  - *S M Asif Hossain, Ruksat Khan Shayoni, Md Kishor Morol et al.*
  - `2026-11-21`
  - Tool-using language-model agents increasingly ask people to approve consequential actions, yet an approval prompt shows only the next step. A request to send a file to an approved recipient can look harmless even when that file was assembled, several steps earlier, from data the…

- **[HyperHarness: Learning to Generate Personalized Agent Harnesses from User Histories](https://arxiv.org/abs/2611.29062v1)**
  - *Zhaoxuan Tan, Jiachen Zhao, Jingbo Yang et al.*
  - `2026-11-21`
  - Personalized LLM agents rely on an agent harness, the surrounding memory and control code, to connect user history with downstream decisions. Existing methods typically employ either a single shared memory workflow across all users, which is efficient to deploy but cannot adapt h…

- **[Grounding Collaborative Agents in Group Cognition](https://arxiv.org/abs/2611.29036v1)**
  - *Zhaoxuan Tan, Mengting Wan, Jingbo Yang et al.*
  - `2026-11-21`
  - Collaborative agents joining an ongoing team rely on shared context to connect multi-party interaction histories with downstream coordination decisions. Existing work typically focuses either on retrieving historical facts from conversation logs, which surfaces isolated evidence…

- **[Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents](https://arxiv.org/abs/2611.28947v1)**
  - *Jiaqi Su, Jie-Jing Shao, Yichen Liu et al.*
  - `2026-11-21`
  - Computer-use agents (CUAs) built on vision-language models are increasingly entrusted with long-horizon tasks in live desktop, web, and mobile environments, where the screen keeps changing on its own. However, current CUAs lack real-time situational awareness: they perceive the e…

- **[Bias Cascade: Understanding the Gap Between Knowledge Alignment and Effect Replication in LLM-based Social Simulation](https://arxiv.org/abs/2611.28854v1)**
  - *Pujun Zheng, Chengmu Wang, Wanying Ren et al.*
  - `2026-11-21`
  - Large language models (LLMs) are increasingly used to simulate participants in social experiments. Existing research has primarily focused on aligning social knowledge and isolated responses, while overlooking whether simulations can reproduce the collective effects of social int…

- **[Legal Is Not Good: A Pre-Registered Benchmark of Low-Cost Language and Decision Models on a New Strategy Game](https://arxiv.org/abs/2611.28713v1)**
  - *Federico Lucca*
  - `2026-11-21`
  - Measure Before You Train argued that an agent's decisions should be measured against ground truth, under a protocol fixed in advance, before anyone trains or replaces the model behind them. We carry the method to a second, very different domain, a turn-based strategy game, and as…

- **[S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence](https://arxiv.org/abs/2611.28649v1)**
  - *Muxin Fu, Peike Yu, Guibin Zhang et al.*
  - `2026-11-21`
  - Spatial intelligence, the ability to reason about 3D space from visual observations, becomes essential as multimodal large language models (MLLMs) move into the physical world. Beyond perceiving each view, it rests on two cornerstones of human cognition: fusing multiple views int…

- **[Muted Distillation: Sealing Reasoning from Teacher Unlocks Token-Efficient Agents](https://arxiv.org/abs/2611.28445v1)**
  - *Yuwei Zhang, Ian Miao, Wentao Zhang et al.*
  - `2026-11-21`
  - On-policy distillation (OPD) is commonly adopted as one of the components in post-training of large language models (LLMs), but in multi-turn agentic tasks we find that the student model increases their reasoning lengths after training. Our empirical analysis shows that the reaso…

- **[Factory-simulator: A process-oriented environment for evaluating manufacturing decisions against optimisation-based references](https://arxiv.org/abs/2611.29079v1)**
  - *Andrzej Wodecki, Wojciech Godlewski, Michał Chojna*
  - `2026-11-21`
  - Motivated by discussions with an electronics contract manufacturer about decision support, Factory-simulator provides a deterministic manufacturing environment for controlled research on the business performance of large language model-based multi-agent systems (LLM-MAS). Equal d…

- **[Who Speaks for the Water? Simulating Discursive Closure and Power Asymmetries in Hydrosocial Governance](https://arxiv.org/abs/2611.28755v1)**
  - *Mario Lillo-Saavedra, Marcela Salgado-Vargas, Ángel García-Pedrero et al.*
  - `2026-11-21`
  - Water governance conflicts stem not only from material scarcity, but from power asymmetries, institutional distrust, and the discursive frameworks through which actors assign meaning to water, infrastructure, and legitimate authority. Conventional simulation tools represent these…

- **[Tool-to-Self: Internalizing Visual Tool Capabilities via Scaffolded Reinforcement Learning](https://arxiv.org/abs/2611.28564v1)**
  - *Jin Cui, Hao Dong, Xinyue Long et al.*
  - `2026-11-21`
  - Vision-language models (VLMs) increasingly rely on external visual tools to access fine-grained visual evidence, but repeated tool execution incurs substantial inference overhead and deployment dependencies. Moreover, conventional tool-use RL can improve visual-task performance,…


## Harness  (111)

### AAAI

- **[MCP-AgentBench: Evaluating Real-World Language Agent Performance with MCP-Mediated Tools](https://arxiv.org/abs/2509.09734)**
  - *Zikang Guo, Benfeng Xu, Chiwei Zhu et al.*
  - **AAAI 2025** · `2025-09-10`
  - The Model Context Protocol (MCP) is rapidly emerging as a pivotal open standard, designed to enhance agent-tool integration and interoperability, and is positioned to unlock a new era of powerful, interconnected, and genuinely utilitarian agentic AI. However, despite MCP's growin…

- **[Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory](https://arxiv.org/abs/2505.15055)**
  - *Hongli Zhou, Hui Huang, Zi-Qing Zhao et al.*
  - **AAAI 2025** · `2025-05-21`
  - The evaluation of large language models (LLMs) via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities. This paper provides a crit…

- **[CO-Bench: Benchmarking Language Model Agents in Algorithm Search for Combinatorial Optimization](https://arxiv.org/abs/2504.04310)**
  - *Wei-Wei Sun, Sheng-Yu Feng, Shan-Da Li et al.*
  - **AAAI 2025** · `2025-04-06`
  - Although LLM-based agents have attracted significant attention in domains such as software engineering and machine learning research, their role in advancing combinatorial optimization (CO) remains relatively underexplored. 
This gap underscores the need for a deeper understandin…


### NeurIPS

- **[Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation](https://arxiv.org/abs/2508.13144)**
  - *David Heineman, Valentin Hofmann, Ian Magnusson et al.*
  - **NeurIPS 2025** · `2025-08-18`
  - Developing large language models is expensive and involves making decisions with small experiments, typically by evaluating on large, multi-task evaluation suites. In this work, we analyze specific properties which make a benchmark more reliable for such decisions, and interventi…

- **[MergeBench: A Benchmark for Merging Domain-Specialized LLMs](https://arxiv.org/abs/2505.10833)**
  - *Yifei He, Si-Qi Zeng, Yu-Zheng Hu et al.*
  - **NeurIPS 2025** · `2025-05-16`
  - Model merging provides a scalable alternative to multi-task training by combining specialized finetuned models through parameter arithmetic, enabling efficient deployment without the need for joint training or access to all task data. While recent methods have shown promise, exis…

- **[Time-R1: Post-Training Large Vision Language Model for Temporal Video Grounding](https://arxiv.org/abs/2503.13377)**
  - *Ye Wang, Zi-Heng Wang, Bo-Shen Xu et al.*
  - **NeurIPS 2025** · `2025-03-17`
  - Temporal Video Grounding (TVG), the task of locating specific video segments based on language queries, is a core challenge in long-form video understanding. While recent Large Vision-Language Models (LVLMs) have shown early promise in tackling TVG through supervised fine-tuning…

- **[WritingBench: A Comprehensive Benchmark for Generative Writing](https://arxiv.org/abs/2503.05244)**
  - *Yuning Wu, Jia-Hao Mei, Ming Yan et al.*
  - **NeurIPS 2025** · `2025-03-07`
  - Recent advancements in large language models (LLMs) have significantly enhanced text generation capabilities, yet evaluating their performance in generative writing remains a challenge. Existing benchmarks primarily focus on generic text generation or limited in writing tasks, fa…


### ICML

- **[Can Harness Optimization Improve Agents? Generalizable Gains Versus Evaluation Noise](https://openreview.net/forum?id=Ri0rU3rPOS)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - Harness optimization methods revise an agent’s prompts, tools, memory, and run-
time control without updating model weights. We ask which of their improve-
ments can be distinguished from evaluation noise, and where the reliable ones
come from. We evaluate Meta-Harness, Agentic H…

- **[AURA-Eval: Evaluation Framework for Acting Under Risk Awareness in LLM Agent Trajectories](https://openreview.net/forum?id=9XfH1iAA4W)**
  - **ICML 2025** · OpenReview · `2026-09-18`
  - LLM agents are increasingly taking actions with real consequences, yet safety evaluations often reduce their behavior to a final safe or unsafe outcome, obscuring whether the agent recognized the risk and how it responded. We introduce AURA-Eval, a framework for evaluating whethe…

- **[Rethinking the Evaluation of Harness Evolution for Agents](https://openreview.net/forum?id=QDdWiaNkk2)**
  - **ICML 2025** · OpenReview · `2026-09-17`
  - Harness evolution is an iterative search procedure that repeatedly evaluates and revises candidate harnesses used for LLM agents using task feedback. We revisit the evaluation of such automatic harness evolution procedures and identify two fundamental issues in the protocol. Firs…

- **[PACE-3D: A structure-aware multi-dimensional evaluation framework for codon optimization via AlphaFold2-derived metrics](https://openreview.net/forum?id=5ZPzR0D1Br)**
  - **ICML 2025** · OpenReview · `2026-09-16`
  - Codon optimization is the cornerstone of heterologous protein expression, but current metrics, such as the Codon Adaptation Index (CAI), only focus on translation elongation rates and ignore the complex coupling between translation dynamics and co-translational folding. Therefore…

- **[FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors](https://openreview.net/forum?id=RKKGxm7O4L)**
  - **ICML 2025** · OpenReview · `2026-09-16`
  - As AI agents are becoming widely adopted in the financial services industry, careful measurement is essential to understand where they can be reliably deployed and where oversight and professional review remain necessary. Such measurement, however, is constrained by limited acces…

- **[Answers Without the Model: Harness Failures and a Zero-Cost Noise Floor for Small-Scale LLM Evaluation](https://openreview.net/forum?id=MXxiEnXvTw)**
  - *{'username': '~Satoshi_Akiyama1', 'fullname': 'Satoshi Akiyama', 'institutions': [{'name': 'Independent', 'domain': 'independent-researcher.org', 'country': 'JP'}]}*
  - **ICML 2025** · OpenReview · `2026-09-02`
  - When an LLM evaluation harness is written by the same person who reads its output, its defects arrive disguised as findings. In one such programme (20 waves, 79,021 rows, one consumer GPU), three defects produced apparent findings: distractors reconstructed the answer, an answer…

- **[AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing](https://arxiv.org/abs/2608.29622)**
  - *{'fullname': 'Xinke Jiang', 'username': ''}, {'fullname': 'Yue Fang', 'username': ''}, {'fullname': 'Zhibang Yang', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2026-08-01`
  - Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts. Recent reinforcement learnin…

- **[Fine-grained evaluation framework](https://openreview.net/forum?id=QN99ISIzmA)**
  - **ICML 2025** · OpenReview · `2026-07-23`

- **[A Reproducible Evaluation Framework for PHM with some Opportunities for Stronger Protocol Evaluation](https://openreview.net/forum?id=1IDZQ4LN7q)**
  - **ICML 2025** · OpenReview · `2026-07-11`

- **[Harness Engineering for LLM Agents: A Survey of Harness Component Taxonomy, Evaluation, and Model--Harness Coevolution](https://openreview.net/forum?id=1VJLY0hAFT)**
  - **ICML 2025** · OpenReview · `2026-07-03`
  - As large language model-driven autonomous agents are increasingly deployed in real-world long-horizon, open-environment tasks, foundation models expose systematic capability gaps in context retention, reliable tool invocation, persistent state management, and multi-step execution…

- **[Accept: Valuable process-level evaluation framework for LLM discovery agents](https://openreview.net/forum?id=UlKWRADnxG)**
  - **ICML 2025** · OpenReview · `2026-06-28`

- **[An interesting evaluation framework applied to limited models](https://openreview.net/forum?id=1PCFV26aTG)**
  - **ICML 2025** · OpenReview · `2026-06-27`

- **[Scientific synthesis evaluation with a leakage-mitigating harness](https://openreview.net/forum?id=74goGTT5yg)**
  - **ICML 2025** · OpenReview · `2026-06-26`

- **[Interesting harness benchmark with many domains, but with unclear details](https://openreview.net/forum?id=KbBQlljXj9)**
  - **ICML 2025** · OpenReview · `2026-06-26`

- **[When Are Multimodal Predictions Biologically Supported? A Diagnostic Evaluation Framework](https://openreview.net/forum?id=vIJ0IZjKoN)**
  - **ICML 2025** · OpenReview · `2026-06-26`

- **[Promising evaluation framework, but evidence for harness-selection claims is limited](https://openreview.net/forum?id=yeXtThIaJa)**
  - **ICML 2025** · OpenReview · `2026-06-25`

- **[Review for the paper ClawBenchPro: Benchmarking How Well Agent Harnesses Work](https://openreview.net/forum?id=sYCTp3rsDS)**
  - **ICML 2025** · OpenReview · `2026-06-24`

- **[Evaluation of IDEAFix: Evaluation Framework for Creative Defixation Prompting in LLMs](https://openreview.net/forum?id=TnNXFg3bkD)**
  - **ICML 2025** · OpenReview · `2026-06-24`

- **[A thoughtful and well-validated evaluation framework for motion forecasting, but the interpretation of “reliance” requires caution](https://openreview.net/forum?id=tNsHeDNIhV)**
  - **ICML 2025** · OpenReview · `2026-06-24`

- **[The paper presents a valuable fraud-evaluation benchmark grounded in real U.S. court cases, but its task design, scenario formulation, and LLM-as-judge validation need clearer justification.](https://openreview.net/forum?id=XJV0YOMvw8)**
  - **ICML 2025** · OpenReview · `2026-06-13`

- **[The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation](https://openreview.net/forum?id=1sqKRqsaE9)**
  - *Naman Vats, Oleg Aleksandrovich Golev*
  - **ICML 2025** · OpenReview · `2026-06-10`
  - Public leaderboards for coding agents typically rank systems by model name and pass rate, while the surrounding harness—the scaffold that issues tools, manages context, and decides when to stop—is often under-specified. Model-to-model comparison is valid when the harness is fixed…

- **[Clustering-based Prompt Optimization for LLM Evaluation](https://openreview.net/forum?id=vLGZhWJW3i)**
  - *Jinyoung Kim, Sun Kim, Inho Kang*
  - **ICML 2025** · OpenReview · `2026-06-10`
  - LLM evaluators (``AI judges'') increasingly stand in for human raters in search-quality pipelines, but their agreement with humans is fragile to how the scoring rubric is worded. We study how to optimize that rubric under a fixed budget of expert labels and evaluation calls, comp…

- **[Agentic Evaluation Framework for Option Trading](https://openreview.net/forum?id=OAxCMnrFbJ)**
  - **ICML 2025** · OpenReview · `2026-06-08`

- **[FairCoder: Probing LLM Bias in High-Stakes Decision Making via Coding Tasks](https://openreview.net/forum?id=n7Mk11IVX8)**
  - *Yongkang Du, Jen-tse Huang, Jieyu Zhao et al.*
  - **ICML 2025** · OpenReview · `2026-06-03`
  - Large language models (LLMs) are increasingly used in high-stakes decisions such as hiring and college admissions, making their social bias a critical concern. While LLMs are trained to refuse explicitly biased requests, bias can be leaked implicitly during LLM planning and reaso…

- **[Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety](https://openreview.net/forum?id=7UXZAFMvpZ)**
  - *Lifei Liu, Haoran Yu, Xiaochong Jiang et al.*
  - **ICML 2025** · OpenReview · `2026-05-26`
  - Safety evaluations of multi-agent LLM systems often compare a direct prompt against a planner-executor pipeline and report the difference as a single "pipeline effect." This aggregate hides
  several simultaneous changes: harmful intent may be recast as plausible operational work…

- **[Towards Direct Evaluation of Harness Optimizers via Priority Ranking](https://openreview.net/forum?id=WSQLJ0m6kS)**
  - *Kai Tzu-iunn Ong, Minseok Kang, Dongwook Choi et al.*
  - **ICML 2025** · OpenReview · `2026-05-05`
  - Harness optimization enables automated agent creation by having an optimizer agent iteratively update the harness of target agents. Despite its success, current studies evaluate optimizers solely by observing target agents' performance gains. This indirect end-improvement evaluat…

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

- **[SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability](https://arxiv.org/abs/2503.09532)**
  - *Adam Karvonen, Can Rager, Johnny Lin et al.*
  - **ICML 2025** · `2025-03-12`
  - Sparse autoencoders (SAEs) are a popular technique for interpreting language model activations, and there is extensive recent work on improving SAE effectiveness. However, most prior work evaluates progress using unsupervised proxy metrics with unclear practical relevance. We int…


### ICLR

- **[MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers](https://arxiv.org/abs/2512.15163)**
  - *Xuan Zong, Zhiqi Shen, Lei Wang et al.*
  - **ICLR 2025** · `2025-12-17`
  - Large language models (LLMs) are evolving into agentic systems that reason, plan, and operate external tools. The Model Context Protocol (MCP) is a key enabler of this transition, offering a standardized interface for connecting LLMs with heterogeneous tools and services. Yet MCP…


### CVPR

- **[ViStoryBench: Comprehensive Benchmark Suite for Story Visualization](https://arxiv.org/abs/2505.24862)**
  - *Cai-Lin Zhuang, Ailin Huang, Yao-Qi Hu et al.*
  - **CVPR 2025** · `2025-05-30`
  - Story visualization aims to generate coherent image sequences that faithfully represent a narrative and match given character references. Despite progress in generative models, existing benchmarks remain narrow in scope, often limited to short prompts, lacking character reference…

- **[Automated Generation of Challenging Multiple-Choice Questions for Vision Language Model Evaluation](https://arxiv.org/abs/2501.03225)**
  - *Yuhui Zhang, Yu-Chang Su, Yiming Liu et al.*
  - **CVPR 2025** · `2025-01-06`
  - The rapid development of vision language models (VLMs) demands rigorous and reliable evaluation. However, current visual question answering (VQA) benchmarks often depend on open-ended questions, making accurate evaluation difficult due to the variability in natural language respo…


### ACL

- **[WebUIBench: A Comprehensive Benchmark for Evaluating Multimodal Large Language Models in WebUI-to-Code](https://arxiv.org/abs/2506.07818)**
  - *Zhi-Yu Lin, Zhengda Zhou, Zhi-Yuan Zhao et al.*
  - **ACL 2025** · `2025-06-09`
  - With the rapid advancement of Generative AI technology, Multimodal Large Language Models(MLLMs) have the potential to act as AI software engineers capable of executing complex web application development. Considering that the model requires a confluence of multidimensional sub-ca…

- **[Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models](https://arxiv.org/abs/2505.02847)**
  - *Bang Zhang, Ruo-Tian Ma, Qing-Xuan Jiang et al.*
  - **ACL 2025** · `2025-05-01`
  - Assessing how well a large language model (LLM) understands human, rather than merely text, remains an open challenge. To bridge the gap, we introduce Sentient Agent as a Judge (SAGE), an automated evaluation framework that measures an LLM's higher-order social cognition. SAGE in…


### EMNLP

- **[MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://arxiv.org/abs/2503.10497)**
  - *Weihao Xuan, Rui Yang, He-Li Qi et al.*
  - **EMNLP 2025** · `2025-03-13`
  - Existing large language model (LLM) evaluation benchmarks primarily focus on English, while current multilingual tasks lack parallel questions that specifically assess cross-linguistic reasoning abilities. This dual limitation makes it challenging to comprehensively assess LLMs'…

- **[RouterEval: A Comprehensive Benchmark for Routing LLMs to Explore Model-level Scaling Up in LLMs](https://arxiv.org/abs/2503.10657)**
  - *Zhong-Zhan Huang, Guo-Ming Ling, Vincent S. Liang et al.*
  - **EMNLP 2025** · `2025-03-08`
  - Routing large language models (LLMs) is a new paradigm that uses a router to recommend the best LLM from a pool of candidates for a given input. In this paper, our comprehensive analysis with more than 8,500 LLMs reveals a novel model-level scaling up phenomenon in Routing LLMs,…

- **[FinMTEB: Finance Massive Text Embedding Benchmark](https://arxiv.org/abs/2502.10990)**
  - *Yixuan Tang, Yi Yang*
  - **EMNLP 2025** · `2025-02-16`
  - Embedding models play a crucial role in representing and retrieving information across various NLP applications. Recent advances in large language models (LLMs) have further enhanced the performance of embedding models. While these models are often benchmarked on general-purpose…


### Other / arXiv

- **[Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](https://arxiv.org/abs/2611.31201)**
  - *Xiao-Ming Wu, Kang Liao, Yuexiao Ma et al.*
  - 🤗 Featured · `2026-11-23`

- **[GameDojo: Benchmarking Real-Time Interactive Agents in Video Games](https://arxiv.org/abs/2611.30771)**
  - *Kuan Zhang, Zhihao Yang, Yukun Chen et al.*
  - 🤗 Featured · `2026-11-23`
  - Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss en…

- **[Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](https://arxiv.org/abs/2611.27689)**
  - *Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan et al.*
  - 🤗 Featured · `2026-11-23`

- **[AutoPILOT: A Visual Agent Harness for Real-Time Gameplay](https://arxiv.org/abs/2611.28202)**
  - *Mark Zhao, Pengcheng Wang, Rui Yang et al.*
  - 🤗 Featured · `2026-11-20`

- **[ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation](https://arxiv.org/abs/2611.31053)**
  - *Yicheng Xu, Wencan Jiang, Zihao Zhu et al.*
  - 🤗 · `2026-11-23`

- **[RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments](https://arxiv.org/abs/2611.31002)**
  - *Jinkun Liu, Yingze Wang, Situ Wang et al.*
  - 🤗 · `2026-11-23`
  - Agentic Robotics, in which foundation models act as coding agents to control robots through executable programs, has emerged as a compelling paradigm for embodied intelligence. Yet unlike software engineering, where massive executable environments power post-training, robotics re…

- **[Self-Upgrading Embodied Agents](https://arxiv.org/abs/2611.31117v1)**
  - *Jiajun Fan, Neil He, Qinglong Zheng et al.*
  - `2026-11-23`
  - An embodied agent built on a language model goes to work with the weights it was given and keeps them for life. To get better, it needs more training, or reflection, memory, search or prompts that cost every step and are lost when the task changes. Editing weights by reasoning, w…

- **[Preflight: Agentic Last-Mile Verification for AI Software Supply Chains](https://arxiv.org/abs/2611.31110v1)**
  - *Yaman Jandali, Nojan Sheybani, Farinaz Koushanfar et al.*
  - `2026-11-23`
  - Software dependencies execute within the trust boundary of downstream applications, yet provenance, static analysis, and package-level behavioral approaches do not directly determine how a released artifact behaves for a specific program. We present Preflight, a program-scoped pr…

- **[ComputeWise: Measuring and Fixing GPU Waste by AI Research Agents](https://arxiv.org/abs/2611.31027v1)**
  - *Egor Pakhomov, Nina Pakhomova, Anurag Koul et al.*
  - `2026-11-23`
  - AI agents are given GPUs to do AI research on their own. Do they use those GPUs well? A busy GPU does not tell us, because it can be busy with work the answer did not need. This matters, because the tokens the agent spends cost almost nothing next to the GPUs its experiments run…

- **[Oops!... I Parsed It Again: Tool-Call Smuggling Against LLM Agents](https://arxiv.org/abs/2611.30624v1)**
  - *Igor Santos-Grueiro, Daniel Romero-Ruiz*
  - `2026-11-23`
  - LLM agents act through tool calls: the model writes the arguments of a call as JSON, a guard decides whether the call may run, and an executor runs it. The same bytes are parsed several times, by the provider, gateways, SDKs, frameworks, the guard, and the executor. JSON leaves s…

- **[Learning What to Change: State-Verified Reinforcement Learning for Educational Agents](https://arxiv.org/abs/2611.30559v1)**
  - *Shengyao Wang, Siyuan Su, Siyu Song et al.*
  - `2026-11-23`
  - Persistent tutoring agents do more than answer questions: they manage course files, practice records, and learner profiles that govern future lessons. In such stateful settings, knowing what to teach does not guarantee knowing what to change. We identify a pervasive failure mode,…

- **[sudo L7: Can Coding Agents Act Like Staff Engineers?](https://arxiv.org/abs/2611.30517v1)**
  - *Nick Heiner, Ian Niebres, Suhaas Garre et al.*
  - `2026-11-23`
  - Coding agents can now turn a well-specified ticket into a patch that passes its tests. Experienced engineers also notice risks the request never mentioned, question flawed premises, reuse what already exists and say plainly what they did and did not check. We present sudo L7, a b…

- **[mini-psych-agent: Evaluating Human-Like Behavior in LLM Agents through Interactive Psychological Environments](https://arxiv.org/abs/2611.30365v1)**
  - *Yi-Fei Cao, Tianxin Huang, Hanbo Xie et al.*
  - `2026-11-23`
  - A Large Language Model (LLM), its harness, and the test-time compute budget jointly determine its behavior. Consequently, the same underlying model, embedded in different agentic workflows or allocated different amounts of test-time compute, can exhibit markedly different perform…

- **[AutoSECO: Automated Skill Evolution for Cross-Problem Combinatorial Optimization with General-Purpose LLM Agents](https://arxiv.org/abs/2611.30139v1)**
  - *Zirui Zhu, Cong Zhang, Ni Zhang et al.*
  - `2026-11-23`
  - General-purpose large language model (LLM) agents can develop complete solvers for combinatorial optimization problems. Their specialization, however, often relies on workflows engineered for individual problems, limiting the reuse of development expertise. We propose AutoSECO, a…

- **[Conartist: Adaptive Agentic Red-Teaming of Computer-Using Agents against Multi-Step Prompt Injection](https://arxiv.org/abs/2611.29977v1)**
  - *Jiaqi Rong, Yunchen Lu, Lihai Nie et al.*
  - `2026-11-23`
  - Harnesses secure Computer-Using Agents by enforcing security constraints and defending against prompt injection attacks. However, we find that two core security mechanisms of agent harnesses remain vulnerable. First, consistency checking prevents agents from deviating from legiti…

- **[TriSegAgent: Context-Efficient 3D Annotation with MLLMs via Tri-Planes](https://arxiv.org/abs/2611.30240v1)**
  - *Qingqiao Hu, Jialin Li, Meilong Xu et al.*
  - `2026-11-23`
  - Interactive segmentation models turn a few clicks into a segmentation prediction across domains, so annotators only decide where the prediction still needs correction. Annotation thus becomes a loop of inspecting the prediction and clicking again. Each step of this loop is a visu…

- **[Sequential Selection against an Adaptive Opponent](https://arxiv.org/abs/2611.30006v1)**
  - *Zhongyuan Lyu, Xiaocong Xu*
  - `2026-11-23`
  - Selecting a strategy by testing it against an opponent is common in game-playing AI, red-teaming of language models, and safety evaluations of AI agents. In many of these settings, the opponent adapts to what it observes, so a strategy that keeps winning in practice may already h…

- **[VeriWorld: A Verifiable Visual SWE-Bench for Spatial Reasoning in 3D Environments](https://arxiv.org/abs/2611.30226v1)**
  - *Yan Zheng, ShengYun Peng, Xuyao Liang et al.*
  - `2026-11-23`
  - Vision-language models (VLMs) are increasingly used for spatial tasks such as navigation and manipulation, where they must infer geometry and object relationships from visual input in order to act correctly. Existing benchmarks usually test perception and reasoning in isolation,…

- **[STUN-Bench: Truly Unseen Tools for Evaluating Shared Tool Experience](https://arxiv.org/abs/2611.30034v1)**
  - *Abhijit Chakraborty, Ni Trieu, Vivek Gupta*
  - `2026-11-23`
  - A tool router retrieves a few candidate tools per request and lets a language model choose. Methods that share experience across organizations add past requests about each tool to what the router retrieves. StableToolBench calls some of its test groups tests on "unseen" tools, ye…

- **[Trallie: from Free-Form Text to Structured Data with LLMs](https://arxiv.org/abs/2611.30773v1)**
  - *Vijayasri Iyer, Cristiano De Nobili, Mubashir Hussain Shah et al.*
  - `2026-11-23`
  - Trallie is an open-source framework that leverages large language models (LLMs) to perform information extraction (IE) from natural language sources with or without user guidance. Unlike conventional approaches that rely on extensive labeled datasets or domain-specific training,…

- **[Body and Soul: Decoupling Robotic Brain and Policy with RoboHarness-Zero](https://arxiv.org/abs/2611.30550v1)**
  - *Yihao Shen, Yuxuan Chen, Xuantong Liu et al.*
  - `2026-11-23`
  - Vision-language-action (VLA) policies can execute individual skills but fail to complete tasks that require combining several of them. In our audit of Xiaomi-Robotics-1, an estimated 43\% of failures involve choosing the wrong target or losing track of task progress. Wrapping a f…

- **[Unpacking the Evaluators: How Configuration Shapes the Evaluation of Alignment in Explainable AI](https://arxiv.org/abs/2611.30816v1)**
  - *Gizem Karagoz, Tanir Ozcelebi, Nirvana Meratnia*
  - `2026-11-23`
  - Explainable AI (XAI) evaluation fundamentally requires human-centered evaluation, assessing whether explanations align with human reasoning and expert knowledge. However, such evaluations often require expert-driven manual validation and are difficult to scale, leading to the wid…

- **[Semantic repeatability and reproducibility of GPT-5 and Gemini 3 Flash on H5N1 One Health questions](https://arxiv.org/abs/2611.29859v1)**
  - *Luizza Dalla Pria, Amelia l. Nelson, Renata Ivanek*
  - `2026-11-23`
  - Highly pathogenic avian influenza A(H5N1) has re-emerged as a One Health concern since 2024, and the public is increasingly consulting large-language-model (LLM) chatbots for health information during outbreaks. Before a chatbot's accuracy can be meaningfully assessed, its consis…

- **[Geospatial foundation models and deep learning for climate resilience: a review of transfer, uncertainty and decision readiness](https://arxiv.org/abs/2611.30198v1)**
  - *Parastoo Farajpoor, Mohammadreza Narimani*
  - `2026-11-23`
  - Geospatial foundation models can reuse information learned from large Earth-observation archives, but their value for climate resilience depends on whether that information transfers to unfamiliar events, regions and observing conditions. This review connects advances in deep lea…

- **[Notes on Generative AI for Mathematical Research](https://arxiv.org/abs/2611.29811v1)**
  - *Shurui Liu*
  - `2026-11-22`
  - These notes describe how generative AI is now used to solve and to check research-level mathematics, with a focus on agents and their harnesses. For the proving agents Rethlas, Danus, and Pharos and the verification agent OSVerify, we explain the design principles, compare each w…

- **[Layer-Level Control of Language Model Execution in Agent Frameworks](https://arxiv.org/abs/2611.29519v1)**
  - *Ran Guan, Yiqi Lin, Xiangxi Tian et al.*
  - `2026-11-22`
  - Agent frameworks typically orchestrate language models through prompt-and-response interfaces. We propose a harness design that exposes intermediate model states and layer-level execution controls to the agent runtime. By connecting state collection, policy fitting, and execution…

- **[MAWAM: Joint Imagination for Collaborative Robot Manipulation with a Multi-Agent World Action Model](https://arxiv.org/abs/2611.29501v1)**
  - *Rongze Tang, Chenyu Zhou, Jianjie Fang et al.*
  - `2026-11-22`
  - World action models (WAMs) excel at robot manipulation by imagining future observations and decoding actions from them, yet remain confined to a single embodied agent. In practice, manipulation often requires multiple robots to collaborate across disjoint workspaces, coupled timi…

- **[Beyond Accuracy: A Diagnostic Benchmark for Hypothesis-Driven Experiment Planning in LLM Agents](https://arxiv.org/abs/2611.29467v1)**
  - *Ryo Kuroki, Amin Mansouri, Philippe Schwaller*
  - `2026-11-22`
  - Evaluating large language model (LLM) agents on scientific tasks typically reduces to final-task accuracy, which obscures where reasoning succeeds or breaks down. We introduce a benchmark and diagnostic evaluation framework for hypothesis-driven adaptive experimental planning in…

- **[Which Failure Does an Intervention Repair? When Agent Interventions Help, and Where Self-Evolving Skills Stall](https://arxiv.org/abs/2611.29290v1)**
  - *Zihan Jin, Gaoyuan Du, Jiate Li et al.*
  - `2026-11-22`
  - An intervention that improves one agent can break another, and adding a stronger harness on top need not repair the damage. Agent interventions such as skills, harnesses, and extra inference budget are nonetheless usually credited with one average gain, measured under one setup.…

- **[Direct Feedback Policy Optimization for AI Coding Agents](https://arxiv.org/abs/2611.29193v1)**
  - *Fei Ding*
  - `2026-11-22`
  - AI coding agents generate, modify, and validate code through multi-turn interactions. Existing reinforcement learning methods often rely on sparse terminal rewards, making it difficult to assess how intermediate decisions affect task outcomes, and group-relative methods also requ…

- **[Endpoint-Conditioned Process Value: What an Endpoint-Blind Process Score Adds Once Terminal Status and Cost Are Known](https://arxiv.org/abs/2611.29354v1)**
  - *Chris D Yan, Ken Wang, MarkX Qian et al.*
  - `2026-11-22`
  - Trajectory metrics promise information beyond final-answer accuracy, but no one has measured what a process score adds once an evaluation knows the outcome and the cost. We build that comparison: a sealed consequence needing an artifact neither agent nor judge ever sees, an opera…

- **[Social Interaction Breaks Replicate Independence in Controlled-Clone LLM Agents](https://arxiv.org/abs/2611.29581v1)**
  - *Yandan Zheng, Haoran Luo, Anh Tuan Luu*
  - `2026-11-22`
  - Multi-agent LLM evaluations and social simulations create many agents from one model and treat them as independent replicates, even after the agents interact. This assumption remains untested with matched controls. We introduce SocCogEval, a controlled-clone assay for Social Cogn…

- **[BenchMint: From Real-World Tasks to Executable Benchmarks](https://arxiv.org/abs/2611.29367v1)**
  - *Zining Huang, Zuo Wang, Mengyao Zhang et al.*
  - `2026-11-22`
  - Large language models (LLMs) need evaluations of everyday reasoning and tool use, such as planning itineraries under user constraints and grounding numerical answers in evidence. We introduce BenchMint, an automated benchmark-construction workflow, and Daily-Life, its collection…

- **[Detectable Epistemic Attack Layers: A Coverage Theorem and Standardized Harness for Conversation-History Integrity](https://arxiv.org/abs/2611.29449v1)**
  - *Fahrell Giovanny, Geby Bayuningtyas, Sahrul Mukharom*
  - `2026-11-22`
  - Conversation history is infrastructure: deployed language models rely on application layers to store and reinject prior turns, and that stored state is writable. We formalize session-level contamination by attack layer, state a coverage theorem, and measure its scope: each deploy…

- **[loopxDINO: Dense Visual Prediction via Iterative Latent Reasoning](https://arxiv.org/abs/2611.29180v1)**
  - *Xiangjing An, Zhibin Jiao, Aiting Chen*
  - `2026-11-22`
  - Standard dense visual prediction architectures scale representation capacity by stacking deep feedforward decoders (6-16 transformer layers with 50M-200M parameters). This explicit layer stacking brings substantial activation memory overhead during backpropagation, requires high…

- **[Automated Safety Analysis for Agentic Workflows](https://arxiv.org/abs/2611.28469v1)**
  - *Yanju Chen, Ying Li, Bosi Zhang et al.*
  - `2026-11-21`
  - LLM applications are increasingly built as agentic workflows: programs that combine model calls, external tools, and control logic to act autonomously on a user's behalf. Because these workflows execute real-world actions, logical flaws in how a workflow is wired can cause severe…

- **[HyperHarness: Learning to Generate Personalized Agent Harnesses from User Histories](https://arxiv.org/abs/2611.29062v1)**
  - *Zhaoxuan Tan, Jiachen Zhao, Jingbo Yang et al.*
  - `2026-11-21`
  - Personalized LLM agents rely on an agent harness, the surrounding memory and control code, to connect user history with downstream decisions. Existing methods typically employ either a single shared memory workflow across all users, which is efficient to deploy but cannot adapt h…

- **[Grounding Collaborative Agents in Group Cognition](https://arxiv.org/abs/2611.29036v1)**
  - *Zhaoxuan Tan, Mengting Wan, Jingbo Yang et al.*
  - `2026-11-21`
  - Collaborative agents joining an ongoing team rely on shared context to connect multi-party interaction histories with downstream coordination decisions. Existing work typically focuses either on retrieving historical facts from conversation logs, which surfaces isolated evidence…

- **[X-AQA: Unifying Action Quality Assessment with Multimodal Large Language Models and Multi-Domain Learning](https://arxiv.org/abs/2611.28548v1)**
  - *Kaili Zheng, Wei Ding, Yuchen Ding et al.*
  - `2026-11-21`
  - Action Quality Assessment (AQA) aims to evaluate the quality of human actions, yet existing methods are predominantly developed and evaluated on individual datasets with different task formulations and assessment criteria. We introduce X-AQA, the first unified training and evalua…

- **[When Rubrics Do Not Decide: Silent Value Completion in LLM Evaluation](https://arxiv.org/abs/2611.28940v1)**
  - *Zhuangzhuang Pan, Yan Xia, Kaiwen Lei et al.*
  - `2026-11-21`
  - Multi-criterion LLM judges often evaluate responses without specifying how conflicting criteria resolve, leaving the winner undetermined even under exact criterion scores. Issuing a strict verdict without declaring the required trade-off premise constitutes silent value completio…


## Finance  (155)

### NeurIPS

- **[Self-Challenging Language Model Agents](https://arxiv.org/abs/2506.01716)**
  - *Yifei Zhou, S. Levine, Jason E. Weston et al.*
  - **NeurIPS 2025** · `2025-06-02`
  - Large language models are quickly becoming the foundation for intelligent agents that are capable of using tools. However, training such agents is challenging because it requires human creation and annotation of a diverse set of tasks, tools, and evaluation criteria. In this pape…


### ICML

- **[Hybrid Financial Analysis Agent with RAG and Text Mining](https://openreview.net/forum?id=jGe6fFmsDg)**
  - *{'fullname': 'Bingzhang Wang', 'username': 'https://orcid.org/orcid-search/search?searchQuery=Bingzhang%20Wang'}, {'fullname': 'Keyi Zhang', 'username': 'https://orcid.org/orcid-search/search?searchQuery=Keyi%20Zhang'}, {'fullname': 'Tianhao Du', 'username': 'https://orcid.org/orcid-search/search?searchQuery=Tianhao%20Du'} et al.*
  - **ICML 2025** · OpenReview · `2026-10-28`
  - This paper presents a hybrid financial analysis agent that integrates retrieval-augmented generation, financial text mining, live market-data access, and a news sentiment classifier within a LangGraph-based orchestration framework. The system is designed to reduce information ove…

- **[ARTE: Agentic Refinement through Trade Execution for High-Frequency Trading Strategy Discovery](https://openreview.net/forum?id=VisvXioWmG)**
  - **ICML 2025** · OpenReview · `2026-10-12`
  - Existing LLM-based trading strategy development primarily uses aggregated price and volume data, which omit within-interval event order and displayed order book changes. Tick-level trade and quote observations preserve this information, but their scale makes the full history impr…

- **[TradingArena: A Market-Making Benchmark for Ranking, Diagnosing, and Steering LLM Behavior](https://openreview.net/forum?id=6VObvVwaGZ)**
  - **ICML 2025** · OpenReview · `2026-09-19`
  - As large language models are increasingly deployed as agents, evaluation should capture both task performance and interactive behavior. Few benchmarks jointly measure performance and behavior under controlled changes to an agent’s information, action space, and inference. We intr…

- **[ParaFusionBench: A Unified Benchmark for Cross-Paradigm Fusion in Factor Mining and Trading Decision-Making](https://openreview.net/forum?id=nqb5xH3QuC)**
  - *{'username': '~Xiaozhao_Zeng1', 'fullname': 'Xiaozhao Zeng', 'institutions': [{'name': 'The Hong Kong University of Science and Technology (Guangzhou)', 'domain': 'hkust-gz.edu.cn', 'country': 'CN'}]}, {'username': '~Fan_Liu5', 'fullname': 'Fan Liu', 'institutions': [{'name': 'AI Thrust, Hong Kong University of Science and Technology (Guangzhou)', 'domain': 'ust.hk', 'country': 'CN'}]}, {'username': '~Yang_Ni4', 'fullname': 'Yang Ni', 'institutions': [{'name': 'The Hong Kong University of Science and Technology', 'domain': 'connect.hkust-gz.edu.cn', 'country': 'CN'}]} et al.*
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

- **[Stacking RNNs and LSTMs for Fraud Detection in Cryptocurrency Blockchain Transactions](https://openreview.net/forum?id=Ukalf1pGgk)**
  - *{'username': '~Olufunso_Dayo_Alowolodu1', 'fullname': 'Olufunso Dayo Alowolodu', 'institutions': [{'name': 'The Federal University of Technology, Akure (FUTA)', 'domain': 'futa.edu.ng', 'country': 'NG'}]}*
  - **ICML 2025** · OpenReview · `2026-08-20`
  - Introduction
Cryptocurrency blockchains enable secure, decentralized financial transactions, but their pseudonymous, decentralized structure also makes them attractive for fraud such as money laundering, Ponzi schemes, and phishing, which makes it difficult for conventional intru…

- **[A comprehensive and fine-grained financial benchmark with solid evaluations, pending minor literature context and formatting fixes](https://openreview.net/forum?id=GC69PoHRlm)**
  - **ICML 2025** · OpenReview · `2026-06-26`

- **[Evaluation of IDEAFix: Evaluation Framework for Creative Defixation Prompting in LLMs](https://openreview.net/forum?id=TnNXFg3bkD)**
  - **ICML 2025** · OpenReview · `2026-06-24`

- **[A Valuable Financial Multimodal Benchmark with Multi-Turn and Agent Evaluation, but Some Validation Concerns Remain](https://openreview.net/forum?id=A2u2L7lj5h)**
  - **ICML 2025** · OpenReview · `2026-06-12`

- **[A Fraud-Detection-Inspired Framework for LLM Agents Security](https://openreview.net/forum?id=uUipgSY8Sh)**
  - *Sheldon Yu, Yingcheng Sun, Hanqing Guo et al.*
  - **ICML 2025** · OpenReview · `2026-06-12`
  - Large Language Model (LLM) agents demonstrate strong capabilities in autonomous task execution, tool use, and multi-step reasoning. However, their increasing autonomy also introduces a new attack surface: adversarial interactions can manipulate agent behavior through direct promp…

- **[Agentic Evaluation Framework for Option Trading](https://openreview.net/forum?id=OAxCMnrFbJ)**
  - **ICML 2025** · OpenReview · `2026-06-08`

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

- **[Performant LLM Agentic Framework for Conversational AI](https://openreview.net/forum?id=JDXB6nvH9x)**
  - *Alex Casella, Wayne Wang*
  - **ICML 2025** · OpenReview · `2025-01-22`
  - The rise of Agentic applications and automation in the Voice AI industry has led to an increased reliance on Large Language Models (LLMs) to navigate graph-based logic workflows composed of nodes and edges. However, existing methods face challenges such as alignment errors in com…

- **[Trading Confidence: Comprehensive Uncertainty Estimation in Algorithmic Trading](https://openreview.net/forum?id=IWDsycHMSP)**
  - *Lin Li, Li Rong Wang, Hsuan Fu et al.*
  - **ICML 2025** · OpenReview · `2025-01-01`
  - Description Reinforcement Learning (RL) has emerged as a powerful approach in financial trading, enabling agents to learn optimal strategies through direct market interaction. However, financial markets are highly uncertain, with price fluctuations driven by stochastic volatility…

- **[Cryptocurrency Transaction Anomaly Detection Based on Semi-supervised Learning and Graph Neural Network](https://openreview.net/forum?id=nTfpRWhmNx)**
  - *{'fullname': 'Renguang Chen', 'username': ''}, {'fullname': 'Lei Zeng', 'username': ''}, {'fullname': 'Huiqing Wang', 'username': ''} et al.*
  - **ICML 2025** · OpenReview · `2025-01-01`
  - The rapid expansion of the cryptocurrency market has led to soaring transaction volumes and heightened transaction-related risks, necessitating robust data-driven security analysis to measure and mitigate emerging threats. Detecting abnormal activities such as fraud, money launde…

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

- **[Cryptocurrency meets CAP Theorem](https://openreview.net/forum?id=EqA0WIwlYH)**
  - *{'fullname': 'Lewis Tseng', 'username': ''}, {'fullname': 'Moayad Aloqaily', 'username': '~Moayad_Aloqaily1'}*
  - **ICML 2025** · OpenReview · `2023-01-01`

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

- **[Computation of Loss Distribution Based on the Structural Model for Credit Portfolios](https://openreview.net/forum?id=H9YyL2epYt)**
  - *Meng Han*
  - **ICML 2025** · OpenReview · `2018-01-01`
  - Credit risk analysis and management at the portfolio level is a challenging issue for financial institutions due to their portfolios’ large size, heterogeneity and complex correlation structure. In this thesis, we propose several new asymptotic methods and exact methods to comput…

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


### ICLR

- **[MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers](https://arxiv.org/abs/2512.15163)**
  - *Xuan Zong, Zhiqi Shen, Lei Wang et al.*
  - **ICLR 2025** · `2025-12-17`
  - Large language models (LLMs) are evolving into agentic systems that reason, plan, and operate external tools. The Model Context Protocol (MCP) is a key enabler of this transition, offering a standardized interface for connecting LLMs with heterogeneous tools and services. Yet MCP…


### ACL

- **[AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading](https://arxiv.org/abs/2510.14264)**
  - *Zheye Deng, Wei-Xiang Yan, Chang-Long Yu et al.*
  - **ACL 2025** · `2025-10-16`
  - While Large Language Model (LLM) agents show promise in automated trading, they still face critical limitations. Prominent multi-agent frameworks often suffer from inefficiency, produce inconsistent signals, and lack the end-to-end optimization required to learn a coherent strate…

- **[Reasoning RAG via System 1 or System 2: A Survey on Reasoning Agentic Retrieval-Augmented Generation for Industry Challenges](https://arxiv.org/abs/2506.10408)**
  - *Jin-Tao Liang, Gang Su, Hui-Feng Lin et al.*
  - **ACL 2025** · `2025-06-12`
  - Retrieval-Augmented Generation (RAG) has emerged as a powerful framework to overcome the knowledge limitations of Large Language Models (LLMs) by integrating external retrieval with language generation. While early RAG systems based on static pipelines have shown effectiveness in…

- **[Text2World: Benchmarking Large Language Models for Symbolic World Model Generation](https://arxiv.org/abs/2502.13092)**
  - *Meng-Kang Hu, Tian-Xing Chen, Yu-De Zou et al.*
  - **ACL 2025** · `2025-02-18`
  - Recently, there has been growing interest in leveraging large language models (LLMs) to generate symbolic world models from textual descriptions. Although LLMs have been extensively explored in the context of world modeling, prior studies encountered several challenges, including…


### EMNLP

- **[Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://arxiv.org/abs/2503.02519)**
  - *Xingzuo Li, Ke-Hai Chen, Yunfei Long et al.*
  - **EMNLP 2025** · `2025-03-04`
  - Large language model (LLM) agents typically adopt a step-by-step reasoning framework, in which they interleave the processes of thinking and acting to accomplish the given task. However, this paradigm faces a deep-rooted one-pass issue whereby each generated intermediate thought…

- **[FinMTEB: Finance Massive Text Embedding Benchmark](https://arxiv.org/abs/2502.10990)**
  - *Yixuan Tang, Yi Yang*
  - **EMNLP 2025** · `2025-02-16`
  - Embedding models play a crucial role in representing and retrieving information across various NLP applications. Recent advances in large language models (LLMs) have further enhanced the performance of embedding models. While these models are often benchmarked on general-purpose…


### Other / arXiv

- **[World Models as Native Latent Action Models](https://arxiv.org/abs/2611.30898)**
  - *Qinyue Li, Weijie Qiao, Qingyi Tao et al.*
  - 🤗 Featured · `2026-11-23`
  - Large and diverse video sources, such as egocentric human video and heterogeneous robot recordings, carry rich dynamics but come either without actions or without a shared action space. Latent action models (LAMs) can recover these dynamics, but they train their inverse- and forw…

- **[CCFinance: Reconstructing Financial News Samples from Web Archives](https://arxiv.org/abs/2611.30737)**
  - *Marcus Gawronsky*
  - 🤗 · `2026-11-23`
  - Proprietary news archives assign stories to firms, so reproducing a financial study often requires access to both the articles and the vendor's assignments. CCFinance lets researchers reconstruct firm coverage under different selection rules by recording which version of a story…

- **[CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting](https://arxiv.org/abs/2611.31185v1)**
  - *Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran*
  - `2026-11-23`
  - Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-…

- **[Habitats: A Framework for Open-Ended Evolution of Agent Objectives](https://arxiv.org/abs/2611.31160v1)**
  - *Nicolas Bolouri, Gaya Mehenni, Daniel Toyama*
  - `2026-11-23`
  - Designing what an agent should optimize can be as difficult as optimizing the agent itself. Existing language-model-based reward-generation methods typically refine objectives for predefined tasks and couple the decision of what to explore with the synthesis of how to implement i…

- **[SayWhen: Set-Valued Semantic Commitment for Low-Regret Early Speech](https://arxiv.org/abs/2611.31101v1)**
  - *Tianyi Huang, Lucas Su, Fred Zhang et al.*
  - `2026-11-23`
  - Speaking early turns a prediction into an irreversible public commitment. We introduce SayWhen, a test-time controller that selects a task-directed act shared across typed continuation plans and controls its release as speech. A persistent veto blocks playback when intervening tr…

- **[SchemaCaps: When a Compatible Tool Update Silently Widens an AI Agent's Authority](https://arxiv.org/abs/2611.30750v1)**
  - *Yulliwas Ameur, Samia Bouzefrane, Soumya Banerjee*
  - `2026-11-23`
  - The tools users approve for their AI agents keep changing their JSON input schemas. Of 8 surveyed MCP clients and scanners, none is observed or documented to re-approve a tool whose input schema widens (two not determinable). We define non-amplification over the coordinates visib…

- **[Can Cities Have Personalities? Introducing the SCD City Personality Assessment](https://arxiv.org/abs/2611.30733v1)**
  - *Andrei Khurshudov*
  - `2026-11-23`
  - Descriptions of cities are shaped by human experience and institutional narratives. We introduce the SCD City Personality Assessment (SCD-CPA), a method that instantiates document-grounded ChatGPT city personas and interrogates each with an identical 24-statement instrument inspi…

- **[Cost-Sensitive Reversibility of Non-Deterministic Actions](https://arxiv.org/abs/2611.30399v1)**
  - *Giuseppe Canonaco, Alberto Pozanco, Daniel Borrajo*
  - `2026-11-23`
  - Determining action reversibility requires checking whether the effects of an action can be undone. Recent work has extended reversibility to fully observable non-deterministic (FOND) planning. It distinguishes weak reversibility, where reversal may succeed, from strong-cyclic rev…

- **[Adopting AI Technologies without Traps: A Multi-Agent Reinforcement Learning Framework](https://arxiv.org/abs/2611.30200v1)**
  - *Jitong Yang, Avinash Reddy Mudireddy, Ziqing Lu et al.*
  - `2026-11-23`
  - AI technologies and AI agents play increasingly important roles in human society, including in education, economics, and research. Adopting AI technologies can bring immediate, and sometimes tremendous, rewards such as through productivity boost, but they can also bring negative…

- **[Same Executions, Different Gaps: Judgment Rules in Web-Agent Evaluation](https://arxiv.org/abs/2611.30190v1)**
  - *Zelong Wang, Weiyue Li, Fei Xue et al.*
  - `2026-11-23`
  - Success-rate gains guide the development of web agents. Yet knowing which agent ranks first does not tell us how much confidence to place in its reported advantage. We study the comparison itself: how success is defined, what evidence supports the judgments, and how the differenc…

- **[AutoSECO: Automated Skill Evolution for Cross-Problem Combinatorial Optimization with General-Purpose LLM Agents](https://arxiv.org/abs/2611.30139v1)**
  - *Zirui Zhu, Cong Zhang, Ni Zhang et al.*
  - `2026-11-23`
  - General-purpose large language model (LLM) agents can develop complete solvers for combinatorial optimization problems. Their specialization, however, often relies on workflows engineered for individual problems, limiting the reuse of development expertise. We propose AutoSECO, a…

- **[SWAM: State-aware World Action Model for Multi-Agent 3D Environments](https://arxiv.org/abs/2611.30042v1)**
  - *Jenna Kang, Bingxuan Li, Colin Groth et al.*
  - `2026-11-23`
  - Interactive world models generate virtual environments autoregressively from player actions and visual history. However, visual history alone cannot reliably capture the evolving states of independently acting non-player characters (NPCs) in real games, particularly when they are…

- **[VADE: A Verifiable Agent Data Engine from Professional Sources](https://arxiv.org/abs/2611.30202v1)**
  - *Xiangchao Chen, Zhiheng Lyu, Kai Zhang et al.*
  - `2026-11-23`
  - Language agents have shown their practical value, particularly in software engineering, where abundant public code and executable tests support training and evaluation at scale. Extending this success to other professional domains, such as law and finance, is not straightforward:…

- **[Causal Evidence for the Emergence and Spread of Reward Hacking in AI Agent Swarms](https://arxiv.org/abs/2611.30185v1)**
  - *Sumer S. Vaid*
  - `2026-11-23`
  - Autonomous AI agents that coordinate and collaborate among each other have become pervasive across domains ranging from scientific research to finance and engineering. The opportunity to share messages and build upon each other's work also creates the potential for misaligned beh…

- **[VeriWorld: A Verifiable Visual SWE-Bench for Spatial Reasoning in 3D Environments](https://arxiv.org/abs/2611.30226v1)**
  - *Yan Zheng, ShengYun Peng, Xuyao Liang et al.*
  - `2026-11-23`
  - Vision-language models (VLMs) are increasingly used for spatial tasks such as navigation and manipulation, where they must infer geometry and object relationships from visual input in order to act correctly. Existing benchmarks usually test perception and reasoning in isolation,…

- **[Unpacking the Evaluators: How Configuration Shapes the Evaluation of Alignment in Explainable AI](https://arxiv.org/abs/2611.30816v1)**
  - *Gizem Karagoz, Tanir Ozcelebi, Nirvana Meratnia*
  - `2026-11-23`
  - Explainable AI (XAI) evaluation fundamentally requires human-centered evaluation, assessing whether explanations align with human reasoning and expert knowledge. However, such evaluations often require expert-driven manual validation and are difficult to scale, leading to the wid…

- **[Geospatial foundation models and deep learning for climate resilience: a review of transfer, uncertainty and decision readiness](https://arxiv.org/abs/2611.30198v1)**
  - *Parastoo Farajpoor, Mohammadreza Narimani*
  - `2026-11-23`
  - Geospatial foundation models can reuse information learned from large Earth-observation archives, but their value for climate resilience depends on whether that information transfers to unfamiliar events, regions and observing conditions. This review connects advances in deep lea…

- **[PseuDRAGON: Knowledge-Guided Local LLMs for Financial-Data Pseudonymization in Closed Networks](https://arxiv.org/abs/2611.30353v1)**
  - *Gwangui Hong, Seonho An, Seonkyu Lim et al.*
  - `2026-11-23`
  - Staff pseudonymizing financial data in closed networks must interpret abbreviated column names, identify personal information, and choose processing methods. Local language models can assist, but may give different labels for the same input. PseuDRAGON keeps confirmed judgments a…

- **[Could This BE Any More Wrong? Teaching VLMs to Know What They Don't Know in Document Extraction](https://arxiv.org/abs/2611.30119v1)**
  - *Varad Srivastava, Victor Casas Hernandez*
  - `2026-11-23`
  - Vision-Language Models can extract structured fields from scanned financial documents, yet they provide no indication of when a field might be wrong. We derive per-field confidence estimates from the token log-probabilities the model already produces, via a token-to-span alignmen…

- **[Automated Neural Network Auditing (ANNA) for Energy Market Settlements: A Machine and Reinforcement Learning-Based Approach](https://arxiv.org/abs/2611.30020v1)**
  - *J. R. Rivadeneyra, I. Lee, F. Nugen et al.*
  - `2026-11-23`
  - The integration of segmented energy markets into Independent System Operators (ISOs) like CAISO and MISO has increased settlement complexity. Automated transaction processing creates challenges for evaluating accuracy, compliance, and financial integrity. Traditional rule-based m…

- **[Potential Games for Self-Neighborhood Channel Mixing in Graph Neural Networks](https://arxiv.org/abs/2611.30829v1)**
  - *Marco Lavorini, Davide Bacciu, Giancarlo Bigi*
  - `2026-11-23`
  - Graph message passing must balance two competing objectives: incorporating neighborhood signals while preserving node-specific information. We model this trade-off as a game in which nodes choose how to mix their own representations with strict-neighborhood aggregates. For fixed…

- **[Do Candlestick Charts Suffice? The Incremental Economic Value of Technical Indicators in Stock Return Prediction](https://arxiv.org/abs/2611.30584v1)**
  - *Peng Liu, Yanyan Zheng*
  - `2026-11-23`
  - Although technical analysis remains widely used in practice, the need for manually constructed indicators is increasingly questioned as deep learning models can extract features directly from OHLC price data. This paper examines the standalone economic value of trading volume and…

- **[PackLoop: Row-Packed Self-Speculative Decoding for Looped Language Models under Concurrency](https://arxiv.org/abs/2611.30205v1)**
  - *Runguo Li, Dezhen Lu*
  - `2026-11-23`
  - Looped language models reuse one block of weights T times per token, trading parameters for test-time depth, but autoregressive decoding then pays T sequential passes per token. Self-speculative decoders recover 2-10x for a single request, yet their gains fade as requests share a…

- **[FToken: Factors as Tokens for Dual-Axis Cross-Sectional Return Prediction](https://arxiv.org/abs/2611.30112v1)**
  - *Juntang Wang, Yihan Wang, Sheng'en Li et al.*
  - `2026-11-23`
  - On a given trading day, a stock-factor panel describes both how stocks differ across factors and how each factor varies across stocks. Most stock Transformers model relationships among stocks or across time. We introduce FToken, which also models relationships among factors. Its…

- **[Cleaning correlation matrices with external information: the Maximum Variance estimat](https://arxiv.org/abs/2611.30843v1)**
  - *Sébastien Valeyre*
  - `2026-11-23`
  - Rotationally invariant estimators clean the eigenvalues of an empirical correlation matrix but keep its noisy eigenvectors. We study an estimator that corrects the eigenvectors by using external information, namely a partition of the assets into groups such as asset classes or re…

- **[Wasserstein Penalisation as an Endogenous Breadth Constraint in Penalised Mean-Variance Portfolio Selection](https://arxiv.org/abs/2611.30046v1)**
  - *Jiahao Chen*
  - `2026-11-23`
  - A manager who wants a long-only book and has read that Wasserstein-robust mean-variance selection improves risk-adjusted performance faces two decisions: how much robustness to buy, and how diversified to be. In the long-only problem, and for the penalised scalarisation of the ro…

- **[Design an Algorithmic Stablecoin based on a Predictive PID Controller](https://arxiv.org/abs/2611.30982v1)**
  - *Yuqiao Zhao, Wai-Ki Ching, Chi-Wing Wong*
  - `2026-11-23`
  - Cryptocurrencies issued based on blockchain technology have attracted increasing attention in recent years. However, their high volatility makes it difficult for them to become circulating currencies. This led to the creation of stablecoins. Existing stablecoins can be divided in…

- **[Who Makes the Decision? Auditing an Agentic LLM Pipeline for Illicit Cryptocurrency Transaction Monitoring](https://arxiv.org/abs/2611.29829v1)**
  - *Vaishnavi Chaughule, Yuchen Zhang, Mohammed Ahnaf Tajwar et al.*
  - `2026-11-22`
  - Agentic pipelines that combine graph detectors, deterministic rules, retrieval-augmented generation and an LLM judge are being proposed to monitor illicit cryptocurrency flows and to write regulation-citing justifications for analysts. They are evaluated on end-to-end accuracy or…

- **[Fin-RSI: A Unified Library of Financial Skills, Checks, and Self-Improvement for LLM Agents](https://arxiv.org/abs/2611.29716v1)**
  - *Wanghao Ye, Shwai He, Sihan Chen et al.*
  - `2026-11-22`
  - As large language models (LLMs) become more capable, financial agents need tools they can readily discover and use. Yet financial software is fragmented across libraries with different interfaces and conventions, making it difficult to build reliable agent workflows. We present F…

- **[Agentic Discovery of Simple Symbolic Inventory Policies](https://arxiv.org/abs/2611.29440v1)**
  - *Xi Chen, Yuze Chen, Baichuan Mo et al.*
  - `2026-11-22`
  - Designing simple inventory policies becomes increasingly difficult as operational features and system configurations expand. We develop an Agentic Inventory-Policy Discovery System based on explicitly defined simple operational formula (SOF) policy and template classes. Large lan…

- **[Political Orientation and Participation in Prediction Markets: Large Stakes Converge, Small Stakes Diverge](https://arxiv.org/abs/2611.29576v1)**
  - *Ali Hosseinzadeh, Ali Hosseiny, Reza Jafari*
  - `2026-11-22`
  - Prediction markets offer a way to study collective expectations and beliefs: people express their views on various events and, by putting money behind their predictions, take on the risks of their judgments. As a result, the scale of investment can reveal additional dimensions of…

- **[Loop-Count Schedules in Looped Transformers: An Empirical Study](https://arxiv.org/abs/2611.29704v1)**
  - *Konstantin Kolokolov*
  - `2026-11-22`
  - Looped transformers apply one block of layers several times with shared weights, trading parameters for repeated computation. We study how the schedule of the loop iteration count R during training determines whether each extra pass acts as a full layer or as a small correction,…

- **[Gated Payoff-Weighted Net Profit Maximization For Online Portfolio Selection With Transaction Costs](https://arxiv.org/abs/2611.29552v1)**
  - *Grace Chengrong Xie, Alvey Qianli Lin, Wai Ki Ching*
  - `2026-11-22`
  - In this paper, we study online portfolio selection (OLPS) problems. The net profit maximization (NPM) acting upon Adaptive Online Moving Average (AOLMA), namely the AOLNPM strategy in portfolio selection, trades when forecast gain exceeds the transaction cost. In essence, this me…

- **[Who Sent It or How It Moved? Sender Shortcuts in Cryptocurrency Anti-Money-Laundering Benchmarks, Audited on Elliptic2 and Elliptic++](https://arxiv.org/abs/2611.29744v1)**
  - *Mohammad Nasir Uddin*
  - `2026-11-22`
  - Two public benchmarks dominate graph-based anti-money-laundering (AML) research on Bitcoin: the transaction-level Elliptic dataset, extended as Elliptic++, and the subgraph-level Elliptic2. In both, a label is assigned according to the entity that sends the funds. We ask whether…

- **[Mind the Trap As LLMs Guess the Data Model: Grain-Aware Guards Against Fan-out in Text-to-SQL and Its Benchmarks](https://arxiv.org/abs/2611.29009v1)**
  - *Ahmed M. Mahran*
  - `2026-11-21`
  - Text-to-SQL systems built on large language models (LLMs) often aggregate over one-to-many and many-to-many joins, a classic trap: when the joined rows repeat an entity, a SUM or COUNT counts it more than once, yet the query runs and returns a plausible number. We characterize th…

- **[StudioBench: Benchmarking Agentic Multimodal Large Language Models for Productive Audiovisual Creation](https://arxiv.org/abs/2611.28902v1)**
  - *Xinglong Xu, Yuxia Zhu, Siyuan Li et al.*
  - `2026-11-21`
  - Video generators can now render convincing short clips, yet complete audiovisual works require coordinating visuals, sound, and editing across multiple stages. Existing benchmarks focus on individual generators or video agents under narrower production settings, leaving end-to-en…

- **[The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates](https://arxiv.org/abs/2611.28671v1)**
  - *Haoyuan Zheng, Dongting Li, Hancheng Ye et al.*
  - `2026-11-21`
  - Multi-agent systems (MAS) usually coordinate heterogeneous models and tools to solve complex tasks, creating a growing need for reliable evaluation. However, a multi-agent workflow that is fastest in one serving environment can lose its advantage in another, even when its models,…

- **[Agent Money Benchmark: Can AI Agents Be Trusted to Spend Money?](https://arxiv.org/abs/2611.28610v1)**
  - *Zhe Chen, Emma Hsieh, Vicky Fu*
  - `2026-11-21`
  - Giving an AI agent a wallet lets it buy data and services on a client's behalf. Trust then depends on how it spends money and what that spending achieves. We introduce Agent Money Benchmark (AMB) to test whether agents spend a client's money well, starting with purchases of infor…

- **[Don't Train It, Write It: An AI Agent Writes New Capabilities into Language Model Weights](https://arxiv.org/abs/2611.28483v1)**
  - *Santiago Rivadeneira Quintero*
  - `2026-11-21`
  - We show that an AI agent can write new capabilities into a pretrained language model by adding gated attention heads and MLP neurons inside its existing layers, without backpropagation and without fitting any weight to the answers of task examples. It has a budget of 50 model pas…

- **[ESM-Bench: A Benchmark for Evaluating Whether AI Agents Understand Earth System Model Physics and Code](https://arxiv.org/abs/2611.28477v1)**
  - *Koutian Wu, Yuxuan Cao, Gengchen Mai et al.*
  - `2026-11-21`
  - AI coding agents that modify Earth System Model (ESM) code must preserve both software interfaces and the physical assumptions encoded in them. We introduce ESM-Bench, a benchmark of 60 developer-commit tasks from 6 repositories: Noah-MP, CLM5, SUMMA, ParFlow, MOM6, and VIC. The…

- **[Human-in-the-Loop Runbook Improvement with Agentic Support Automation](https://arxiv.org/abs/2611.28441v1)**
  - *Rocker D'Antonio, Harry Xie*
  - `2026-11-21`
  - Operational support is an important component of production software services. Support requests are often emergent and can come in many forms such as customer escalations or unplanned service interruption. Engineers across organizations have been successful in implementing automa…

- **[Factory-simulator: A process-oriented environment for evaluating manufacturing decisions against optimisation-based references](https://arxiv.org/abs/2611.29079v1)**
  - *Andrzej Wodecki, Wojciech Godlewski, Michał Chojna*
  - `2026-11-21`
  - Motivated by discussions with an electronics contract manufacturer about decision support, Factory-simulator provides a deterministic manufacturing environment for controlled research on the business performance of large language model-based multi-agent systems (LLM-MAS). Equal d…

- **[Who Speaks for the Water? Simulating Discursive Closure and Power Asymmetries in Hydrosocial Governance](https://arxiv.org/abs/2611.28755v1)**
  - *Mario Lillo-Saavedra, Marcela Salgado-Vargas, Ángel García-Pedrero et al.*
  - `2026-11-21`
  - Water governance conflicts stem not only from material scarcity, but from power asymmetries, institutional distrust, and the discursive frameworks through which actors assign meaning to water, infrastructure, and legitimate authority. Conventional simulation tools represent these…

- **[FormaFin: Verifiable Financial Analysis with Solver-Guided Reinforcement Learning](https://arxiv.org/abs/2611.28881v1)**
  - *Bethel Hall, William Eiers*
  - `2026-11-21`
  - Formally verifying financial analyses generated by large language models (LLMs) remains challenging as financial rules are largely expressed in natural language and rarely have corresponding formal specifications. Training language models to formalize these rules is hindered by t…

- **[Twisted Block Particle Filters: A Local Particle-System Change of Measure for High-Dimensional State-Space Models](https://arxiv.org/abs/2611.28848v1)**
  - *Ning Ning*
  - `2026-11-21`
  - Block particle filters mitigate weight degeneracy in high-dimensional state-space models, but their normalizer estimates can remain highly variable. We introduce a twisted block particle filter (TBPF) that incorporates predictive guidance through an exact change of measure at blo…

- **[Beyond Invoice Volumes: Temporal Network Structure, Maturity Concentration, and Systemic Liquidity Exposure in SME Trade-Credit Networks](https://arxiv.org/abs/2611.28876v1)**
  - *Sai Srikanth Madugula, Peplluis Esteva de la Rosa, Daya Shankar*
  - `2026-11-21`
  - Trade-credit invoices encode directed obligations whose temporal synchronization and counterparty concentration are obscured by annual volume totals. We audit 749,952 atomic B2B invoices from 2012-2023 (EUR 99.705B; 75,343 firms) from the pseudonymized Mendeley Data corpus (Estev…

- **[Pixel Auto-Encoder: Reconstructing Language Model Activations Through Pixel Art](https://arxiv.org/abs/2611.28822v1)**
  - *Haru Furuichi, Phan Xuan Tan*
  - `2026-11-21`
  - Interpreting the high-dimensional internal representations of large language models (LLMs) remains a challenging problem. Recent approaches have explored translating these representations into human-understandable forms, particularly natural language. In this work, we explore the…

- **[Modeling Joint Tail Risk and Dependence for Cryptocurrencies via a Copula-Based Semiparametric Framework](https://arxiv.org/abs/2611.28524v1)**
  - *Cathy W. S. Chen, Takaaki Koike, Aaron E. P. Lin*
  - `2026-11-21`
  - This study proposes a Bayesian copula-based bivariate semiparametric framework for jointly forecasting Value-at-Risk (VaR) and Expected Shortfall (ES) while modeling cross-asset tail dependence. The marginal dynamics are specified using four ES-CAViaR-type models, including exten…


---
*Generated 2026-11-24 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
