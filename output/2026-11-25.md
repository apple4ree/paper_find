# Daily Paper Digest — 2026-11-25 (Wednesday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**565 unique papers** (717 topic-entries — cross-topic papers counted once per category)

---

## Agent  (400)

### AAAI

- **[Beyond ReAct: A Planner-Centric Framework for Complex Tool-Augmented LLM Reasoning](https://arxiv.org/abs/2511.10037)**
  - *Xiao-Long Wei, Yuehu Dong, Xing-Liang Wang et al.*
  - **AAAI 2025** · `2025-11-13`
  - Existing tool-augmented large language models (LLMs) encounter significant challenges when processing complex queries. Current frameworks such as ReAct are prone to local optimization traps due to their reliance on incremental decision-making processes. To address these limitatio…

- **[CoDe: Communication Delay-Tolerant Multi-Agent Collaboration via Dual Alignment of Intent and Timeliness](https://arxiv.org/abs/2501.05207)**
  - *Shou-Cheng Song, You-Fang Lin, Sheng Han et al.*
  - **AAAI 2025** · `2025-01-09`
  - Communication has been widely employed to enhance multi-agent collaboration. Previous research has typically assumed delay-free communication, a strong assumption that is challenging to meet in practice. However, real-world agents suffer from channel delays, receiving messages se…


### NeurIPS

- **[SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks](https://arxiv.org/abs/2506.11791)**
  - *Hwiwon Lee, Zi-Qi Zhang, Hanxiao Lu et al.*
  - **NeurIPS 2025** · `2025-06-13`
  - Rigorous security-focused evaluation of large language model (LLM) agents is imperative for establishing trust in their safe deployment throughout the software development lifecycle. However, existing benchmarks largely rely on synthetic challenges or simplified vulnerability dat…

- **[AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents](https://arxiv.org/abs/2506.00641)**
  - *Han-Jun Luo, Shen-Yu Dai, Chiming Ni et al.*
  - **NeurIPS 2025** · `2025-05-31`
  - Despite the rapid advancement of LLM-based agents, the reliable evaluation of their safety and security remains a significant challenge. Existing rule-based or LLM-based evaluators often miss dangers in agents'step-by-step actions, overlook subtle meanings, fail to see how small…

- **[MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement](https://arxiv.org/abs/2506.15692)**
  - *Jaehyun Nam, Jinsung Yoon, Jie-Feng Chen et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - Agents based on large language models (LLMs) for machine learning engineering (MLE) can automatically implement ML models via code generation. However, existing approaches to build such agents often rely heavily on inherent LLM knowledge and employ coarse exploration strategies t…

- **[Distilling LLM Agent into Small Models with Retrieval and Code Tools](https://arxiv.org/abs/2505.17612)**
  - *Minki Kang, Jongwon Jeong, Seanie Lee et al.*
  - **NeurIPS 2025** · `2025-05-23`
  - Large language models (LLMs) excel at complex reasoning tasks but remain computationally expensive, limiting their practical deployment. To address this, recent works have focused on distilling reasoning capabilities into smaller language models (sLMs) using chain-of-thought (CoT…

- **[Code Graph Model (CGM): A Graph-Integrated Large Language Model for Repository-Level Software Engineering Tasks](https://arxiv.org/abs/2505.16901)**
  - *Hong-Yuan Tao, Ying Zhang, Zhenhao Tang et al.*
  - **NeurIPS 2025** · `2025-05-22`
  - Recent advances in Large Language Models (LLMs) have shown promise in function-level code generation, yet repository-level software engineering tasks remain challenging. Current solutions predominantly rely on proprietary LLM agents, which introduce unpredictability and limit acc…

- **[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)**
  - *Yuan-Te Li, Xu Yang, Xiao Yang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - Financial markets pose fundamental challenges for asset return prediction due to their high dimensionality, non-stationarity, and persistent volatility. Despite advances in large language models and multi-agent systems, current quantitative research pipelines suffer from limited…

- **[MLZero: A Multi-Agent System for End-to-end Machine Learning Automation](https://arxiv.org/abs/2505.13941)**
  - *Hao-Yang Fang, Bo-Ran Han, Nick Erickson et al.*
  - **NeurIPS 2025** · `2025-05-20`
  - Existing AutoML systems have advanced the automation of machine learning (ML); however, they still require substantial manual configuration and expert input, particularly when handling multimodal data. We introduce MLZero, a novel multi-agent framework powered by Large Language M…

- **[Repo2Run: Automated Building Executable Environment for Code Repository at Scale](https://arxiv.org/abs/2502.13681)**
  - *Rui-Da Hu, Chao Peng, Xinchen Wang et al.*
  - **NeurIPS 2025** · `2025-02-19`
  - Scaling up executable code data is significant for improving language models'software engineering capability. The intricate nature of the process makes it labor-intensive, time-consuming and expert-knowledge-dependent to build a large number of executable code repositories, limit…


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

- **[Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://arxiv.org/abs/2505.19433)**
  - *Pei-Jie Dong, Zhen-Heng Tang, Xiang-Hong Liu et al.*
  - **ICML 2025** · `2025-05-26`
  - Post-training compression reduces the computational and memory costs of large language models (LLMs), enabling resource-efficient deployment. However, existing compression benchmarks only focus on language modeling (e.g., perplexity) and natural language understanding tasks (e.g.…

- **[MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://arxiv.org/abs/2503.03686)**
  - *Rui Ye, Shuo Tang, Rui Ge et al.*
  - **ICML 2025** · `2025-03-05`
  - LLM-based multi-agent systems (MAS) have shown significant potential in tackling diverse tasks. However, to design effective MAS, existing approaches heavily rely on manual configurations or multiple calls of advanced LLMs, resulting in inadaptability and high inference costs. In…

- **[MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673)**
  - *Adibvafa Fallahpour, Jun Ma, Alif Munim et al.*
  - **ICML 2025** · `2025-02-04`
  - Chest X-rays (CXRs) play an integral role in driving critical decisions in disease management and patient care. While recent innovations have led to specialized models for various CXR interpretation tasks, these solutions often operate in isolation, limiting their practical utili…

- **[Tool Unlearning for Tool-Augmented LLMs](https://arxiv.org/abs/2502.01083)**
  - *Jiali Cheng, Hadi Amiri*
  - **ICML 2025** · `2025-02-03`
  - Tool-augmented large language models (LLMs) are often trained on datasets of query-response pairs, which embed the ability to use tools or APIs directly into the parametric knowledge of LLMs. Tool-augmented LLMs need the ability to forget learned tools due to security vulnerabili…

- **[OrcaLoca: An LLM Agent Framework for Software Issue Localization](https://arxiv.org/abs/2502.00350)**
  - *Zhong-Ming Yu, He-Jia Zhang, Yu-Jie Zhao et al.*
  - **ICML 2025** · `2025-02-01`
  - Recent developments in Large Language Model (LLM) agents are revolutionizing Autonomous Software Engineering (ASE), enabling automated coding, problem fixes, and feature improvements. However, localization -- precisely identifying software problems by navigating to relevant code…

- **[RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](https://arxiv.org/abs/2501.18160)**
  - *Jin-Yao Guo, Cheng-Peng Wang, Xiang-Zhe Xu et al.*
  - **ICML 2025** · `2025-01-30`
  - Code auditing is the process of reviewing code with the aim of identifying bugs. Large Language Models (LLMs) have demonstrated promising capabilities for this task without requiring compilation, while also supporting user-friendly customization. However, auditing a code reposito…


### ICLR

- **[Scaling Large Language Model-based Multi-Agent Collaboration](https://openreview.net/forum?id=K3n5jPkrU6)**
  - *Chen Qian, Zihao Xie, YiFei Wang et al.*
  - **ICLR 2026** · OpenReview · `2024-09-13`
  - Recent breakthroughs in large language model-driven autonomous agents have revealed that multi-agent collaboration often surpasses each individual through collective reasoning. Inspired by the neural scaling law—increasing neurons enhances performance, this study explores whether…

- **[Disclosure Bias in AI Reviewers](https://arxiv.org/abs/2611.30410v1)**
  - *Jens Leysen, Noah Daniëls, Marco Favier et al.*
  - **ICLR** · `2026-11-23`
  - AI models increasingly help to review papers, and many conferences and journals now require authors to state how they used AI. Does this AI-use statement change how an AI reviewer rates a paper, and could it change which papers are accepted? In a preliminary study, we varied only…

- **[RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents](https://arxiv.org/abs/2510.02609)**
  - *Cheng-Quan Guo, Chulin Xie, Yu Yang et al.*
  - **ICLR 2025** · `2025-10-02`
  - Code agents have gained widespread adoption due to their strong code generation capabilities and integration with code interpreters, enabling dynamic execution, debugging, and interactive programming capabilities. While these advancements have streamlined complex workflows, they…

- **[TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture](https://arxiv.org/abs/2510.01279)**
  - *Yong-Chao Chen, Jie-Feng Chen, Rui Meng et al.*
  - **ICLR 2025** · `2025-09-30`
  - While integrating tools like Code Interpreter and Search has significantly enhanced Large Language Model (LLM) reasoning in models like ChatGPT Agent and Gemini-Pro, practical guidance on optimal tool use is lacking. The core challenge is effectively combining textual reasoning,…

- **[OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety](https://arxiv.org/abs/2507.06134)**
  - *Sanidhya Vijayvargiya, Aditya Bharat Soni, Xuhui Zhou et al.*
  - **ICLR 2025** · `2025-07-08`
  - Recent advances in AI agents capable of solving complex, everyday tasks, from scheduling to customer service, have enabled deployment in real-world settings, but their possibilities for unsafe behavior demands rigorous evaluation. While prior benchmarks have attempted to assess a…

- **[Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning](https://arxiv.org/abs/2504.17192)**
  - *Minju Seo, Jinheon Baek, Seongyun Lee et al.*
  - **ICLR 2025** · `2025-04-24`
  - Despite the rapid growth of machine learning research, corresponding code implementations are often unavailable, making it slow and labor-intensive for researchers to reproduce results and build upon prior work. In the meantime, recent Large Language Models (LLMs) excel at unders…

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


### KDD

- **[Not All Interpretation Methods Are Created Equal: Tiered Evaluation of AI Interpretability](https://arxiv.org/abs/2611.31833v1)**
  - *Nicolas Sanchez, Bin Yu*
  - **KDD** · `2026-11-24`
  - As AI transitions to sociotechnical deployments, uninterpretable models pose serious threats to reliability, public trust and contestability. However, not all interpretation methods are created equal: for interpretability to enhance deployment safety and effectiveness, interpreta…

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, Artem Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…

- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)**
  - *Mahmoud Mohammadi, Yi-Peng Li, Jane Lo et al.*
  - **KDD 2025** · `2025-07-29`
  - The rise of LLM-based agents has opened new frontiers in AI applications, yet evaluating these agents remains a complex and underdeveloped area. This survey provides an in-depth overview of the emerging field of LLM agent evaluation, introducing a two-dimensional taxonomy that or…

- **[A Survey on Trustworthy LLM Agents: Threats and Countermeasures](https://arxiv.org/abs/2503.09648)**
  - *Miao Yu, Fan-Ci Meng, Xin-Yun Zhou et al.*
  - **KDD 2025** · `2025-03-12`
  - With the rapid evolution of Large Language Models (LLMs), LLM-based agents and Multi-agent Systems (MAS) have significantly expanded the capabilities of LLM ecosystems. This evolution stems from empowering LLMs with additional modules such as memory, tools, environment, and even…


### ACL

- **[Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies](https://arxiv.org/abs/2611.33010)**
  - *Xuanchen Liu, Hejun Zhang, Boxuan Dong et al.*
  - **ACL** · 🤗 Featured · `2026-11-24`
  - Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introdu…

- **[Discovering Bandwidth-Efficient Prefetchers to Shrink the Cache Hierarchy](https://arxiv.org/abs/2611.31983v1)**
  - *Patrick Tser Jern Kon, Akanksha Jain, Abraham Gonzalez et al.*
  - **ACL** · `2026-11-24`
  - Shared last-level caches (LLCs) increasingly dominate server processor die area, forcing architects to trade core counts for cache capacity. While intelligent data prefetching offers a pathway to reclaim this silicon, designing coordinated, multi-level prefetching policies for mu…

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

- **[ParaCodex: A Profiling-Guided Autonomous Coding Agent for Reliable Parallel Code Generation and Translation](https://arxiv.org/abs/2601.04327)**
  - *Erel Kaplan, Tomer Bitan, Lian Ghrayeb et al.*
  - **ACL 2026** · `2026-01-07`
  - Parallel programming is central to HPC and AI, but producing code that is correct and fast remains challenging, especially for OpenMP GPU offload, where data movement and tuning dominate. Autonomous coding agents can compile, test, and profile on target hardware, but outputs are…

- **[Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885)**
  - *Yi Yu, Liu-Yi Yao, Yue-Xiang Xie et al.*
  - **ACL 2026** · `2026-01-05`
  - Large language model (LLM) agents face fundamental limitations in long-horizon reasoning due to finite context windows, making effective memory management critical. Existing methods typically handle long-term memory (LTM) and short-term memory (STM) as separate components, relyin…

- **[AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading](https://arxiv.org/abs/2510.14264)**
  - *Zheye Deng, Wei-Xiang Yan, Chang-Long Yu et al.*
  - **ACL 2025** · `2025-10-16`
  - While Large Language Model (LLM) agents show promise in automated trading, they still face critical limitations. Prominent multi-agent frameworks often suffer from inefficiency, produce inconsistent signals, and lack the end-to-end optimization required to learn a coherent strate…

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://arxiv.org/abs/2507.21028)**
  - *Jia-Ju Chen, Yuxuan Lu, Xiaojie Wang et al.*
  - **ACL 2025** · `2025-07-28`
  - Nearly all human work is collaborative; thus, the evaluation of real-world NLP applications often requires multiple dimensions that align with diverse human perspectives. As real human evaluator resources are often scarce and costly, the emerging"LLM-as-a-judge"paradigm sheds lig…

- **[MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](https://arxiv.org/abs/2506.21605)**
  - *Hao-Ran Tan, Ze-Yu Zhang, Chen Ma et al.*
  - **ACL 2025** · `2025-06-20`
  - Recent works have highlighted the significance of memory mechanisms in LLM-based agents, which enable them to store observed information and adapt to dynamic environments. However, evaluating their memory capabilities still remains challenges. Previous evaluations are commonly li…

- **[Reasoning RAG via System 1 or System 2: A Survey on Reasoning Agentic Retrieval-Augmented Generation for Industry Challenges](https://arxiv.org/abs/2506.10408)**
  - *Jin-Tao Liang, Gang Su, Hui-Feng Lin et al.*
  - **ACL 2025** · `2025-06-12`
  - Retrieval-Augmented Generation (RAG) has emerged as a powerful framework to overcome the knowledge limitations of Large Language Models (LLMs) by integrating external retrieval with language generation. While early RAG systems based on static pipelines have shown effectiveness in…

- **[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://arxiv.org/abs/2504.08725)**
  - *Dayu Yang, Antoine Simoulin, Xin Qian et al.*
  - **ACL 2025** · `2025-04-11`
  - High-quality code documentation is crucial for software development especially in the era of AI. However, generating it automatically using Large Language Models (LLMs) remains challenging, as existing approaches often produce incomplete, unhelpful, or factually incorrect outputs…

- **[METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](https://arxiv.org/abs/2502.17651)**
  - *Bing-Xuan Li, Yi-Wei Wang, Jiu-Xiang Gu et al.*
  - **ACL 2025** · `2025-02-24`
  - Chart generation aims to generate code to produce charts satisfying the desired visual properties, e.g., texts, layout, color, and type. It has great potential to empower the automatic professional report generation in financial analysis, research presentation, education, and hea…

- **[Red-Teaming LLM Multi-Agent Systems via Communication Attacks](https://arxiv.org/abs/2502.14847)**
  - *Peng-Fei He, Yu-Ping Lin, Shen Dong et al.*
  - **ACL 2025** · `2025-02-20`
  - Large Language Model-based Multi-Agent Systems (LLM-MAS) have revolutionized complex problem-solving capability by enabling sophisticated agent collaboration through message-based communications. While the communication framework is crucial for agent coordination, it also introdu…

- **[LLM Agents Making Agent Tools](https://arxiv.org/abs/2502.11705)**
  - *G. Wölflein, D. Ferber, D. Truhn et al.*
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
  - *Hui Wei, Zihao Zhang, Sheng-Hua He et al.*
  - **ACL 2025** · `2025-02-16`
  - LLMs have immense potential for generating plans, transforming an initial world state into a desired goal state. A large body of research has explored the use of LLMs for various planning tasks, from web navigation to travel planning and database querying. However, many of these…

- **[nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow](https://arxiv.org/abs/2502.05036)**
  - *Geliang Ouyang, Jing-Ya Chen, Zhihe Nie et al.*
  - **ACL 2025** · `2025-02-07`
  - Natural Language to Visualization (NL2Vis) seeks to convert natural-language descriptions into visual representations of given tables, empowering users to derive insights from large-scale data. Recent advancements in Large Language Models (LLMs) show promise in automating code ge…

- **[Qwen2.5-xCoder: Multi-Agent Collaboration for Multilingual Code Instruction Tuning](https://aclanthology.org/2025.acl-long.642.pdf)**
  - *Jian Yang, Wei Zhang, Yi-Bo Miao et al.*
  - **ACL 2025**
  - ,


### EMNLP

- **[Tool Zero: Training Tool-Augmented LLMs via Pure RL from Scratch](https://arxiv.org/abs/2511.01934)**
  - *Yi-Rong Zeng, Xiao Ding, Yu-Tai Hou et al.*
  - **EMNLP 2025** · `2025-11-02`
  - Training tool-augmented LLMs has emerged as a promising approach to enhancing language models'capabilities for complex tasks. The current supervised fine-tuning paradigm relies on constructing extensive domain-specific datasets to train models. However, this approach often strugg…

- **[Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents](https://arxiv.org/abs/2509.17488)**
  - *Shou-Ju Wang, Fenglin Yu, Xirui Liu et al.*
  - **EMNLP 2025** · `2025-09-22`
  - The increasing autonomy of LLM agents in handling sensitive communications, accelerated by Model Context Protocol (MCP) and Agent-to-Agent (A2A) frameworks, creates urgent privacy challenges. While recent work reveals significant gaps between LLMs'privacy Q&A performance and thei…

- **[Code Like Humans: A Multi-Agent Solution for Medical Coding](https://arxiv.org/abs/2509.05378)**
  - *A. Motzfeldt, Joakim Edin, Casper L. Christensen et al.*
  - **EMNLP 2025** · `2025-09-04`
  - In medical coding, experts map unstructured clinical notes to alphanumeric codes for diagnoses and procedures. We introduce Code Like Humans: a new agentic framework for medical coding with large language models. It implements official coding guidelines for human experts, and it…

- **[ScreenCoder: Advancing Visual-to-Code Generation for Front-End Automation via Modular Multimodal Agents](https://arxiv.org/abs/2507.22827)**
  - *Yi-Lei Jiang, Yaozhi Zheng, Yuxuan Wan et al.*
  - **EMNLP 2025** · `2025-07-30`
  - Automating the transformation of user interface (UI) designs into front-end code holds significant promise for accelerating software development and democratizing design workflows. While multimodal large language models (MLLMs) can translate images to code, they often fail on com…

- **[ToolHaystack: Stress-Testing Tool-Augmented Language Models in Realistic Long-Term Interactions](https://arxiv.org/abs/2505.23662)**
  - *Beong-woo Kwak, Minju Kim, Dongha Lim et al.*
  - **EMNLP 2025** · `2025-05-29`
  - Large language models (LLMs) have demonstrated strong capabilities in using external tools to address user inquiries. However, most existing evaluations assume tool use in short contexts, offering limited insight into model behavior during realistic long-term interactions. To fil…

- **[AgentThink: A Unified Framework for Tool-Augmented Chain-of-Thought Reasoning in Vision-Language Models for Autonomous Driving](https://arxiv.org/abs/2505.15298)**
  - *Kan-Gan Qian, Sicong Jiang, Yang Zhong et al.*
  - **EMNLP 2025** · `2025-05-21`
  - Vision-Language Models (VLMs) show promise for autonomous driving, yet their struggle with hallucinations, inefficient reasoning, and limited real-world validation hinders accurate perception and robust step-by-step reasoning. To overcome this, we introduce \textbf{AgentThink}, a…

- **[Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)**
  - *Samuel Schmidgall, Yu-Sheng Su, Ze Wang et al.*
  - **EMNLP 2025** · `2025-01-08`
  - Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory, an…

- **[ACEBench: A Comprehensive Evaluation of LLM Tool Usage](https://aclanthology.org/2025.findings-emnlp.697.pdf)**
  - *Chen Chen, Xin-Long Hao, Weiwen Liu et al.*
  - **EMNLP 2025**
  - Large Language Models (LLMs) have demonstrated significant potential in decision-making and reasoning, particularly when integrated with various tools to effectively solve complex problems. However, existing benchmarks for evaluating LLMs’ tool usage face several limitations: (1)…


### NAACL

- **[Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061)**
  - *Qiusi Zhan, Richard Fang, H. Panchal et al.*
  - **NAACL 2025** · `2025-02-27`
  - Large Language Model (LLM) agents exhibit remarkable performance across diverse applications by using external tools to interact with environments. However, integrating external tools introduces security risks, such as indirect prompt injection (IPI) attacks. Despite defenses des…

- **[Self-Training Large Language Models for Tool-Use Without Demonstrations](https://arxiv.org/abs/2502.05867)**
  - *Ne Luo, Aryo Pradipta Gema, Xuan-Li He et al.*
  - **NAACL 2025** · `2025-02-09`
  - Large language models (LLMs) remain prone to factual inaccuracies and computational errors, including hallucinations and mistakes in mathematical reasoning. Recent work augmented LLMs with tools to mitigate these shortcomings, but often requires curated gold tool-use demonstratio…

- **[CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging](https://arxiv.org/abs/2502.05664)**
  - *Md. Ashraful Islam, Mohammed Eunus Ali, Md. Rizwan Parvez*
  - **NAACL 2025** · `2025-02-08`
  - Large Language Models (LLMs) have made significant strides in code generation and problem solving. Current approaches employ external tool-based iterative debuggers that use compiler or other tool-based runtime feedback to refine coarse programs generated by various methods. Howe…


### Other / arXiv

- **[Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe](https://arxiv.org/abs/2611.32884)**
  - *Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang et al.*
  - 🤗 Featured · `2026-11-24`
  - AI agents working on long tasks often commit to an answer before they have enough evidence, a behavior called laziness. In our evaluations, they frequently commit even while their stated belief still names several possible answers. An outcome reward at the end of the episode scor…

- **[PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement](https://arxiv.org/abs/2611.32554)**
  - *Yang Cao, Zhe Zhu, Yiheng Zhang et al.*
  - 🤗 Featured · `2026-11-24`

- **[ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds](https://arxiv.org/abs/2611.32649)**
  - *Qingle Liu, Jieming Li, Pei-lin Li et al.*
  - 🤗 Featured · `2026-11-24`
  - In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline,…

- **[CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies](https://arxiv.org/abs/2611.33148)**
  - *Dawid J. Kopiczko, Tijmen Blankevoort, Yuki M. Asano*
  - 🤗 Featured · `2026-11-24`
  - Reasoning models become long-horizon agents through reinforcement learning or, more cheaply, through fine-tuning on a stronger teacher's trajectories, which contain the teacher's chain-of-thought as well as its actions. The standard fine-tuning approach imitates both, yet the str…

- **[MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction](https://arxiv.org/abs/2611.32462)**
  - *Yifan Dai, Daili Hua, Bohan Zeng et al.*
  - 🤗 Featured · `2026-11-24`
  - Multi-reference image generation requires a model to preserve the appearance of selected subjects while arranging them according to an instruction. Despite recent progress in reference-based generation and compositional control, reliably organizing selected subjects into the inte…

- **[Coding4Games: Can Modern Coding Agents Play Modern Video Games?](https://arxiv.org/abs/2611.31974)**
  - *Shifang Zhao, Haoyu Wang, Yuyang Yin et al.*
  - 🤗 Featured · `2026-11-24`
  - Games, especially modern AAA games, challenge language models to perceive complex scenes, control actions, and make decisions over long horizons. Existing game benchmarks primarily test language models as computer-use agents that query a language model throughout play, incurring…

- **[SpecEngineeringBench: Evaluating Coding Agents as Autonomous Specification Engineers](https://arxiv.org/abs/2611.32973)**
  - *Xingjian Wang, Shijian Wang, Minghao Liu et al.*
  - 🤗 Featured · `2026-11-24`

- **[ACAP: Asynchronous Coding Agents for Efficient Robot Control](https://arxiv.org/abs/2611.31205)**
  - *Zexin He, Rui Li, Yushi Lan et al.*
  - 🤗 Featured · `2026-11-23`
  - Coding agents can construct and revise robot behavior during execution, but using one agent for the whole robot can delay otherwise independent work. We introduce Asynchronous Coding Agents as Policy (ACAP), an asynchronous framework that organizes one robot as a team of persiste…

- **[Self-Evolving Evaluation Environments for Computer-Use Agents](https://arxiv.org/abs/2611.30962)**
  - *Wenhao Wang, Panrong Tong, Quyu Kong et al.*
  - 🤗 Featured · `2026-11-23`
  - Computer-use agents (CUAs) are rapidly improving, yet their evaluation remains largely static. Existing benchmarks provide a strong foundation, but fixed difficulty ceilings, limited feature coverage, and coarse aggregate scores progressively weaken their discriminative and diagn…

- **[Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation](https://arxiv.org/abs/2611.31358)**
  - *Guo Chen, Fuxiao Liu, Haoqin Tu et al.*
  - 🤗 Featured · `2026-11-23`
  - Visual creation demands expressive imagery together with precise control over text, layout, and structure. We introduce Nemotron-Labs-VisualCreation, an agentic framework that connects these capabilities through Pixel as Code. Raster images are represented by learned discrete vis…

- **[AdProducer: Towards Agentic Advertising Video Generation](https://arxiv.org/abs/2611.31466)**
  - *Kunyang Li, Chaoyang Wang, Mubarak Shah et al.*
  - 🤗 Featured · `2026-11-23`
  - Recent advances in video generation have made automated advertising production increasingly feasible. However, an effective advertisement must faithfully represent the product and communicate its selling points through compelling visual storytelling, which requires more than visu…

- **[Can an Agent Trust Its Own Zoom? Cross-Magnification Provenance Verification for Whole-Slide Images](https://arxiv.org/abs/2611.29150)**
  - *Yan Wang, Yiran Song, Zizhuo Gong et al.*
  - 🤗 Featured · `2026-11-22`
  - Visual agents navigate whole-slide images through magnified observations associated with claimed locations. However, a visually plausible observation does not necessarily originate from its claimed location, particularly across magnifications and in regions with similar tissue st…

- **[Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents](https://arxiv.org/abs/2611.28947)**
  - *Jiaqi Su, Jie-Jing Shao, Yichen Liu et al.*
  - 🤗 Featured · `2026-11-21`

- **[RECAP: Training Long-horizon LLM Agents with Context Compaction](https://arxiv.org/abs/2611.31258)**
  - *Yulun Jiang, Maria Brbic, Michael Moor*
  - 🤗 Featured · `2026-10-19`

- **[Bathys: Advancing Deep Search Agents](https://arxiv.org/abs/2611.32660)**
  - *Zixuan Chen, Shengyou Yuan, Nang Yuan et al.*
  - 🤗 · `2026-11-24`
  - Deep search is a critical capability for agents tackling complex, open-ended tasks, where solving a problem requires iterative information gathering, query reformulation, and evidence-based verification rather than a single retrieval step. To address these requirements, we presen…

- **[TeamFlowRL: Online Policy Optimization of Decentralized Flow Policies for Multi-Agent Coordination](https://arxiv.org/abs/2611.32645)**
  - *Guowei Zou, Beiwen Zhang, Haitao Wang et al.*
  - 🤗 · `2026-11-24`
  - Complex cooperative tasks require coordinated multi-agent behavior. Offline generative policies learn expressive cooperative behaviors from trajectories but remain limited by fixed datasets. Online reinforcement learning can improve them through environment interaction. However,…

- **[Avalon-M1: Reinforcement Learning from Collective Rewards](https://arxiv.org/abs/2611.32539)**
  - *Iliyan Zarov, Henry Course, Anthony Hartshorn et al.*
  - 🤗 · `2026-11-24`
  - We introduce reinforcement learning from collective rewards (RLCR), a recipe for jointly training language models to act as agent organisations under latency constraints. A CEO and up to eight specialists share one policy, co-ordinate through a message board and workspace, and ar…

- **[Reliability-aware AI Agent Execution in Collaborative Edge Computing: A World Model Approach](https://arxiv.org/abs/2611.32520)**
  - *Xiangchun Chen, Jiannong Cao, Longxiang Gao et al.*
  - 🤗 · `2026-11-24`

- **[OmniEVIE: Evidence-Vector-Informed Embedding for Multi-modal Retrieval](https://arxiv.org/abs/2611.32203)**
  - *Zifei Wang, Wei Wen, Qiang Ji et al.*
  - 🤗 · `2026-11-24`
  - Multimodal retrieval must match dense pages, fine-grained entities, ordered video, and agent tools and memory. Single-vector embeddings lose local evidence, cross-encoders reread every recalled item online, and uncompressed late interaction is too large to serve. We present OmniE…

- **[Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance](https://arxiv.org/abs/2611.33098v1)**
  - *Lingwei Gu, Jimmy Lin*
  - `2026-11-24`
  - Agents built on frontier language models are expensive. At every step, the frontier model re-reads its entire context and executes every subtask regardless of its difficulty. This paper explores the simple thesis that much of this cost can be removed by delegating easy subtasks t…

- **[AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design](https://arxiv.org/abs/2611.33093v1)**
  - *Guangyuan Wang, Chengran Li, Minchen Luo et al.*
  - `2026-11-24`
  - A language-model decoder carries state between decoding steps, and in hardware a wrong state update can leave the current token correct and corrupt the output several tokens later, so a design can pass output tests and still be wrong. AIChipBench asks what LLM coding agents need…

- **[Hybrid AI for AI-Native RAN Control: A Functional Perspective](https://arxiv.org/abs/2611.33035v1)**
  - *Sabrine Aroua, Osama Arouk, Pegah Alizadeh*
  - `2026-11-24`
  - AI-native radio access network (RAN) control involves interdependent decisions across network entities, protocol layers, and timescales. Understanding how AI and conventional methods can jointly support these decisions requires a common basis for comparing their functional roles.…

- **[RecordRoute: Auditing Agent Failures with Localization-Guided Diagnosis](https://arxiv.org/abs/2611.33022v1)**
  - *Yifan Duan, Lihuan Li, Chao Xue et al.*
  - `2026-11-24`
  - Auditing failed agent executions requires identifying the responsible actor, the earliest decisive step, and the error mode. Representative supervised methods either focus on step localization or predict multiple attribution targets from shared trajectory representations. These m…

- **[Can LLM Judges Catch Unsafe Clinical Actions? A Fault-Injection Study](https://arxiv.org/abs/2611.33012v1)**
  - *Neda Ghafouri*
  - `2026-11-24`
  - As clinical AI agents begin to interact with electronic health records (EHRs), large language models (LLMs) are increasingly used to evaluate their actions. But how reliably can these judges recognize clinically dangerous mistakes, especially when an agent appears to have complet…

- **[Attestation is All You Need: Toward a Zero-Trust Architecture for HPC AI Agents](https://arxiv.org/abs/2611.32958v1)**
  - *Jie Li, Chenxu Niu, Tongyang Wang et al.*
  - `2026-11-24`
  - AI agents are beginning to automate data analysis, orchestration, and simulation steering in HPC environments, but they introduce a security problem that existing cluster defenses do not address: the hijacked authorized agent. An adversary can subvert an agent through prompt inje…

- **[LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving](https://arxiv.org/abs/2611.32954v1)**
  - *Wentao Zhu, Ziao Sheng, Peng Deng et al.*
  - `2026-11-24`
  - Large language model (LLM) serving engines offload the key/value (KV) cache from GPU memory to host DRAM and SSD so multi-turn and agent requests can reuse prompt prefixes. Capacity then limits service at two levels: external tiers govern prefix reuse before eviction, while the G…

- **[ShellBench: What Matters More for AI Agents, Models, or Harness for Everyday Tasks](https://arxiv.org/abs/2611.32946v1)**
  - *Vincent Koc, Aditya Washikar, Rishab Naveen Venkataraman et al.*
  - `2026-11-24`
  - The use of AI agents among the general public has been increasing exponentially throughout 2026, though it is often hard for users to determine which configuration is most effective for their personal use. To help provide clarity here we introduce ShellBench, 100 day-to-day tasks…

- **[Reading Decisions Before Spans: Efficient Generative Verification](https://arxiv.org/abs/2611.32931v1)**
  - *Yanbin Gong, Lei Chen*
  - `2026-11-24`
  - A developer checking an assistant's report may need only an alarm that a claim is unsupported. A generative verifier, however, can continue decoding to quote and classify the errors. We study how much of that output is needed to recover its decision. In a frozen 2B span verifier,…

- **[Interactive Neural Computers](https://arxiv.org/abs/2611.32811v1)**
  - *Ross Murphy, Marcel Hedman, Gabriel Brostow*
  - `2026-11-24`
  - Computers and their interfaces are usually treated as fixed, so a person, or increasingly an AI agent, must adapt to whatever the operating system presents. This is limiting when someone needs a different workflow, or an interface suited to hands-free use or a disability. We expl…

- **[MRBench: Benchmarking Physical Necessity Reasoning in Heterogeneous Multi-Robot Manipulation](https://arxiv.org/abs/2611.32803v1)**
  - *Yanzhe Chen, Zhijun Cao, Ruihe An et al.*
  - `2026-11-24`
  - Recent advances in multi-robot manipulation have shown how robots can collaborate to accomplish complex tasks. However, successful coordination does not reveal which robots are actually needed. The same task may require different teams as robot capabilities change, resources beco…

- **[RubikSQL-HB: Agentic Text-to-SQL with Knowledge in the Loop](https://arxiv.org/abs/2611.32772v1)**
  - *Haorui Jia, Zihan Qu, Yundi Dong et al.*
  - `2026-11-24`
  - Database agents need more than schema structure: business meanings, stored values and reference queries supply knowledge that becomes relevant at different points in reasoning. We introduce RubikSQL-HB, which exposes these materials through queryable, database-specific knowledge…

- **[EviCraft: Can Minecraft Agents Find What They Cannot See?](https://arxiv.org/abs/2611.32765v1)**
  - *Wenyou Yi, Lantian Zhang, Guanlin Chen et al.*
  - `2026-11-24`
  - In Minecraft, a common testbed for embodied agents, semantic tools such as mineBlock pick targets from the simulator's loaded world state without a visibility test, so a buried ore the agent has never seen is one call away, and scores cannot show whether the agent searched. We fo…

- **[CAPTA: Identifying LLMs Behind AI Agents](https://arxiv.org/abs/2611.32686v1)**
  - *Kailun Yan, Yue Huang, Sisi Duan*
  - `2026-11-24`
  - Large language model (LLM)-based agents access remote services through tools to complete user tasks, often via API calls. In this setting, a remote service may want to identify the backend LLM of an agent to launch model-specific attacks, including prompt injection or selective d…

- **[Economic World Model](https://arxiv.org/abs/2611.32663v1)**
  - *Qirui Mi, Yujia Ming, Bo Li et al.*
  - `2026-11-24`
  - Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions? To answer this question, we define an economic world model (EWM) as an agent's internal representation of how an econo…

- **[RoboRecast: Intent-Preserving Demonstration Augmentation via Diagnosis-Driven Optimization](https://arxiv.org/abs/2611.32622v1)**
  - *Yushi Long, Juzhan Xu, Haibin Huang et al.*
  - `2026-11-24`
  - Collecting diverse real-world manipulation demonstrations is costly, motivating the use of simulation to augment existing demonstrations for robot policy learning. When objects, layouts, or robots change, transferring motions from a source demonstration can produce behavior that…

- **[Next-Manip: On-Demand Agent-Policy Collaboration for Robotic Manipulation](https://arxiv.org/abs/2611.32533v1)**
  - *Jiayi Liu, Ke Ye, Jiaming Zhou et al.*
  - `2026-11-24`
  - General-purpose robotic manipulation requires task reasoning, failure recovery, and precise control, yet limited manipulation data make these abilities difficult to obtain from a single policy. Recent multimodal agents show promise in task reasoning and recovery but lack reliable…

- **[RecurSciBench: Benchmarking Recursive Self-Improvement in Data-Driven Scientific Research](https://arxiv.org/abs/2611.32508v1)**
  - *Wenxi Xu, Chuan Qin, Zihan Wang et al.*
  - `2026-11-24`
  - Large language model (LLM)-based agents are advancing the automation of data-driven scientific research. Recent advances in recursive self-improvement (RSI) offer the potential for these agents to continuously improve through experience, but evaluating transfer across scientific…

- **[Assessing Robustness to Catastrophic Forgetting in Continual Deep Reinforcement Learning for Cyber-Physical Systems](https://arxiv.org/abs/2611.32496v1)**
  - *Kim N. Nolle, Ivana Dusparic, Rhodri Cusack et al.*
  - `2026-11-24`
  - As the use of reinforcement learning (RL) becomes more widespread in cyber-physical systems, it becomes increasingly important to design RL agents that are able to adapt to changes in their environments in order to maintain safety and reliability. This paper addresses the questio…

- **[VISE: Verifier-Independent Skill Self-Evolution with Feedback from Tool Implementations](https://arxiv.org/abs/2611.32480v1)**
  - *Yuxuan Liu, Chongyang Du, Yuhao Zhang et al.*
  - `2026-11-24`
  - Agent skills provide reusable workflows that guide LLM agents in using tools. Refining these workflows requires feedback on missing or incorrect instructions, but task-specific verifiers are not always available. We propose VISE (Verifier-Independent Skill Evolution), a scripts-f…

- **[See the Answer, Learn to Embed: Learning Universal Multimodal Embeddings from Hindsight](https://arxiv.org/abs/2611.32439v1)**
  - *Yoonki Cho, Youngju Na, Taegeun Yang et al.*
  - `2026-11-24`
  - Universal Multimodal Embedding (UME) models map heterogeneous multimodal inputs into a shared embedding space, where pairwise similarity supports diverse downstream tasks. Recent reasoning-driven UME approaches use intermediate reasoning to generate additional context for embeddi…

- **[Within-task hazards of AI agents: unidentified by time-horizon curves, identified by repeated runs](https://arxiv.org/abs/2611.32415v1)**
  - *Ruiqi Zhao*
  - `2026-11-24`
  - The time horizon of an AI agent is read off a curve: the probability that the agent completes a task, plotted against the time a human needs for it. Several recent analyses fit survival models to this curve and conclude that agents' hazard of failure declines as a task goes on. T…

- **[Verify then Steer: Progress Hallucination-Aware Recovery for Continuous Vision-and-Language Navigation](https://arxiv.org/abs/2611.32400v1)**
  - *Jiewen Hou, Guanxiang Qi, Meina Kan et al.*
  - `2026-11-24`
  - Vision-and-Language Navigation (VLN) requires an agent to follow language instructions to reach a target in an unseen 3D environment. However, existing methods still struggle to recover from route deviations at test time. We investigate this limitation through the lens of instruc…

- **[Evolve to Learn: Gradient-aligned experience evolution for model self-improvement](https://arxiv.org/abs/2611.32390v1)**
  - *Haoyuan Li, Gangyi Zhang, Dong Wang et al.*
  - `2026-11-24`
  - Self-evolving language models can continuously acquire useful experience through test-time interaction, reflection, and prompt optimization, yet turning such experience into model itself to ensure self improvement remains challenging. On-policy self-distillation (OPSD) provides a…

- **[Can AI Design a Better nnU-Net? A Hypothesis-Driven Architecture Discovery Loop from Failures to Design Rules](https://arxiv.org/abs/2611.32384v1)**
  - *Songtao Jiang, Yuan Wang, Fucheng Niu et al.*
  - `2026-11-24`
  - Neural architecture search and LLM-driven evolution often reduce evaluation to a scalar fitness score, discarding failures that could explain why designs succeed or fail. We present a hypothesis-driven architecture discovery loop in which LLM agents diagnose structured error patt…

- **[The Control-Flow Tax: Specialized Decision Routing for LLM Agent Workflows](https://arxiv.org/abs/2611.32365v1)**
  - *Zhikai Cheng, Shuanghu Wang, Li Jiang*
  - `2026-11-24`
  - An agent can spend almost as much deciding what to do as doing it. In our documentation workflow, control-flow routing accounts for 42.5% of baseline reference cost on the initial task. Lower token prices alone do not solve this control-flow tax: inexpensive general-purpose route…

- **[FigmaEval: A Benchmark for Evaluating AI Agents in Professional UI Design](https://arxiv.org/abs/2611.32321v1)**
  - *Xinyue Huang, Yongyong Gao, Zhengyuan Pan et al.*
  - `2026-11-24`
  - Recent advances in AI agents have enabled autonomous UI design using professional tools such as Figma, yet evaluating their design capabilities remains challenging due to the open-ended nature of design tasks and the absence of unique ground truths. We introduce FigmaEval, a benc…

- **[Refining and Aligning Clinical Reasoning with Health Guidelines via Formal Constraints](https://arxiv.org/abs/2611.32247v1)**
  - *Xiaoyang Fan, Yufan Cai, Zhe Hou et al.*
  - `2026-11-24`
  - Clinical reasoning from incomplete or conflicting patient evidence must account for low-probability but high-risk concerns while remaining grounded in health guidelines. We introduce VerClin, an explainable framework that extracts guideline conditions, exclusions, recommendations…

- **[Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation](https://arxiv.org/abs/2611.32238v1)**
  - *Kaipeng Fang, Yuhao Wang, Ji Zhang et al.*
  - `2026-11-24`
  - Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, whi…

- **[PoseVLN: Learning Geometric State Evolution for Vision-Language Navigation](https://arxiv.org/abs/2611.32218v1)**
  - *Pengyu Hou, Mingfei Han, Haihong Hao et al.*
  - `2026-11-24`
  - Vision-Language Navigation (VLN) requires an embodied agent to relate past experience, current spatial state, and future motion while following natural-language instructions. Recent approaches improve these capabilities through long-horizon memory, state-aware reasoning, and futu…

- **[XMind: Thinking Twice via Cross-Memory Reasoning for LLM-Based Autonomous Driving](https://arxiv.org/abs/2611.32209v1)**
  - *Zuyi Guo, Xianjie Dai, Lei Yang et al.*
  - `2026-11-24`
  - Memory-augmented large language model (LLM) driving agents can reuse past experience, yet previously learned corrections often fail to transfer when traffic conditions change. A key limitation is that existing memories mainly record observed outcomes, providing little evidence ab…

- **[Who gets the information? An $α$-fair label-coverage framework for multi-label feature selection](https://arxiv.org/abs/2611.32200v1)**
  - *Zhenzhi Tang*
  - `2026-11-24`
  - Recent information-theoretic filters for multi-label feature selection disagree on how to distribute relevance over labels: some amplify features that inform a few labels, others balance what every label receives. We show these choices are implicit social welfare functions. Treat…

- **[When Answering Is Administering: Permission Replies That Rewrite Coding-Agent Policy](https://arxiv.org/abs/2611.32195v1)**
  - *Zeming Fei, Hongming Fei, Jingwen Chen et al.*
  - `2026-11-24`
  - Coding agents let plugins and remote services answer permission prompts, and Claude Code documents that such an answer cannot override the operator's deny rules. However, we show that this guarantee, checked one decision at a time, fails over a whole run, because an answer to one…

- **[LLM Agent Authorization Across Context Compaction](https://arxiv.org/abs/2611.32194v1)**
  - *Zeming Fei, Hongming Fei, Yi Xu et al.*
  - `2026-11-24`
  - Request-derived authorizers such as Progent protect LLM agents from prompt injection by deriving what an agent may do from the user's request. Their guarantee rests on attribution: the request is taken to be what the user said. Compaction breaks it. At every automatic compaction…

- **[CoverMem: Coverage-Constrained Visual Memory for Budgeted Embodied Question Answering](https://arxiv.org/abs/2611.32119v1)**
  - *Ruijie Ma, Haoyue Liu, Mingda Zhang et al.*
  - `2026-11-24`
  - Episodic-memory embodied question answering enables agents to answer questions based on previously recorded visual observations of the surrounding scenes. However, growing observation histories, varying observation quality across viewpoints, and limited computational resources ma…

- **[MARGIN: A Risk-Aware Agent for Robot Program Refinement](https://arxiv.org/abs/2611.32093v1)**
  - *Hongbo Duan, Fan Du, Haipeng Luo et al.*
  - `2026-11-24`
  - Robot-programming agents improve executable control policies through repeated testing and repair, yet binary success saturates while execution risk persists across unseen scenes. We introduce MARGIN, a risk-aware agent that converts successful robot rollouts into actionable evide…

- **[ExpGuard: Guarding Long-Horizon LLM Agents against Corrupted Experience](https://arxiv.org/abs/2611.32085v1)**
  - *Yuzhou Chen, Licheng Pan, Zhixuan Chu et al.*
  - `2026-11-24`
  - Long-horizon large language model (LLM) agents distill past trajectories into reusable experiences. Misleading or adversarial guidance in source trajectories can corrupt these experiences, allowing harmful instructions to persist across tasks and influence future agent actions. A…

- **[From Rule-based to Agentic: LLM Agent based Real-time Control of Urban Drainage Systems for Flooding and Sewer Overflow Mitigation](https://arxiv.org/abs/2611.32046v1)**
  - *Wenchong Tian, Shixun Li, Ruozhou Lin et al.*
  - `2026-11-24`
  - Real-time control (RTC) for urban drainage systems (UDS) remains hampered by sparse in-network sensing. While heterogeneous multi-modal meteorological early warnings often contain decision-critical information for UDS RTC, none of the existing approaches can exploit such external…

- **[Provenance-Isolated Epistemic Quorums: Execution-Bound Evidence Certification and Plausible-World Safety Gating in Agentic Control Planes](https://arxiv.org/abs/2611.32032v1)**
  - *Jun He, Deying Yu*
  - `2026-11-24`
  - Agreement among large language models is not physical evidence for mutating production infrastructure. Because generative models share pretraining priors and conform to peer rationales during deliberation, voting ensembles correlate errors instead of providing independent fault t…

- **[Unifying Partner and Environment Diversity to Improve Human-AI Coordination](https://arxiv.org/abs/2611.32031v1)**
  - *Patrick Q. Zhang, Yancheng Liang, Adrienne Fairhall et al.*
  - `2026-11-24`
  - Real-world applications of modern AI systems require generalization to both unseen environments and novel human users. The field of zero-shot coordination (ZSC) has focused primarily on deploying AI to cooperate with novel partners in otherwise familiar environments. Popular popu…

- **[Structure-Aware Transformers for Hierarchical Authorization in Personal AI Agents](https://arxiv.org/abs/2611.32018v1)**
  - *Dongyu Cui, Jie Ding, Xuan Bi*
  - `2026-11-24`
  - Personal AI agents can carry out complex, multi-step tasks on users' behalf, but doing so often involves numerous permission requests. Manually reviewing each request is time-consuming, while indiscriminate approval poses privacy and security risks. Predicting users' authorizatio…

- **[To Critic Or Not To Critic](https://arxiv.org/abs/2611.32013v1)**
  - *Jason Wei, George Pu, Jingxuan Fan et al.*
  - `2026-11-24`
  - As large language models tackle longer and more complex tasks, understanding when a critic improves the efficiency of reinforcement learning (RL) becomes increasingly important. Proximal Policy Optimization (PPO) trains a critic to reduce variance and provide fine-grained credit…

- **[Marketing-Bench: Evaluating Frontier Models and Agents on Real-World Marketing Capabilities](https://arxiv.org/abs/2611.32012v1)**
  - *Sumanth Balaji, Siddharth Gupta, Ameet Deshpande et al.*
  - `2026-11-24`
  - As frontier AI models and agents are deployed more broadly in the real world, marketing is emerging as one of their largest applications. Marketing teams use AI models to produce brand assets like website copy and social media posts, while consumers' agents autonomously discover…

- **[Calm Agent: Reframing Agent Interaction around Intermittent Human Attention](https://arxiv.org/abs/2611.32009v1)**
  - *Dian Jin, Zixun Fu, Guan Wang et al.*
  - `2026-11-24`
  - AI agents can carry out auxiliary tasks while users focus on other work. Yet users still need to understand task state, make changes, and respond when help is required. We argue that agents for ongoing auxiliary tasks should be designed around intermittent human attention: tasks…

- **[Reading, Writing and Repairing Game-Theoretic Policies in Weight Space](https://arxiv.org/abs/2611.31979v1)**
  - *Ancil Crayton*
  - `2026-11-24`
  - Can a language model work in the weight space of a policy network for a repeated game? We put four questions to a mid-size open model, on recurrent networks of 1{,}218 weights with exactly checkable answers. Given a population of opponents described in English, write a policy tha…

- **[Are Web Agents Still Detectable? Stress-Testing Bot Defenses with Coordinated Evasion](https://arxiv.org/abs/2611.31962v1)**
  - *Parsa Nilforushan, Gemmin Sugiura, Kourosh Hashemi et al.*
  - `2026-11-24`
  - AI web agents can autonomously navigate websites and complete various tasks. As their capabilities and adoption expand, evaluating bot defenses requires adversarial stress tests. Although prior work demonstrates that existing agents can remain detectable, it remains unclear how e…

- **[CAPE: Coordinating Calibration and Search for Tool-Use Policies](https://arxiv.org/abs/2611.31938v1)**
  - *Jiahao Wang, Xiaoxuan Chen, Aijun Yang et al.*
  - `2026-11-24`
  - A tool call can fail even when the operation behind it is correct, because the receiving tool parses delimiters, dates or record layouts under a configuration the agent cannot inspect. Compiling a tool-use policy for such a tool requires both calibration, which evaluates candidat…

- **[Loupe: Reinforcing Knowledge-Intensive Video Generation Agents](https://arxiv.org/abs/2611.31895v1)**
  - *Kai Zeng, Ruichuan An, Zhen Fang et al.*
  - `2026-11-24`
  - Knowledge-intensive video generation remains challenging because prompts often omit the facts, appearances, and temporal relationships required for accurate generation. While search-based workflows can retrieve missing evidence, manually designed strategies limit adaptive plannin…

- **[Rethinking Video Agents: When and Why Video Harnesses Work](https://arxiv.org/abs/2611.31883v1)**
  - *Luoyuan Zhang, Xuanyu Zheng, Yancheng Long et al.*
  - `2026-11-24`
  - Video understanding depends not only on how models reason about visual evidence, but also on which evidence they observe. Fixed observation policies determine this evidence in advance; agentic harnesses allow models to seek further observations as their understanding develops. Th…

- **[RepoEviAgent: Scalable Synthesis of Evidence-Grounded Repository-Level Question Answering Tasks](https://arxiv.org/abs/2611.31873v1)**
  - *Aoqi Hu, Yueao Xing*
  - `2026-11-24`
  - Real-world software engineering (SWE) tasks require agents to understand repository structures, cross-module dependencies, and runtime behaviors, posing significant challenges for constructing high-quality training and evaluation data. To address this, we propose RepoEviAgent, a…

- **[Modeling Event-Conditioned Emotional Expression Response with LLM Agents in a Synthetic Social Simulation](https://arxiv.org/abs/2611.31851v1)**
  - *Rebecca Marigliano, Peter Carragher, Kathleen M. Carley*
  - `2026-11-24`
  - Emotions are central drivers of human behavior, yet most behavioral models fail to capture their role in shaping perception, decision-making, and collective action. Application areas such as emergency response and public health are especially constrained by the lack of emotion-aw…

- **[Spec-Test Coverage Gap: Detecting Overspecified Tests in SWE-Bench-Style Benchmarks](https://arxiv.org/abs/2611.31839v1)**
  - *Avi Aggarwal, Yiran Hu*
  - `2026-11-24`
  - SWE-bench-style benchmarks, such as SWE-bench Verified (Verified) and SWE-bench Pro (Pro), evaluate coding agents with tests taken from the change that originally fixed each issue. However, these tests can enforce details the task never states, causing correct alternative fixes t…

- **[Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models](https://arxiv.org/abs/2611.31821v1)**
  - *Keyu He, Michael Li, Jiarui Liu et al.*
  - `2026-11-24`
  - The training of socially intelligent language models often relies on large language model (LLM) judges, which are expensive, noisy, and vulnerable to reward hacking. Multi-player social games offer a natural alternative: they require open-ended communication to coordinate with te…

- **[Agentic Discovery of Soundness Bugs in Safe Rust Bindings](https://arxiv.org/abs/2611.31813v1)**
  - *Marius Momeu, Koushik Sen*
  - `2026-11-24`
  - Rust crates confine unsafe code, such as calls into C or C++ libraries or system calls, behind safe interfaces that must uphold Rust's invariants. If an interface encodes one rule of the code beneath it too weakly, a program written in purely safe Rust can cause undefined behavio…

- **[How Far Apart Are Two Proofs? Measuring Proof Dissimilarity in a Proof Kernel and in Lean/Mathlib](https://arxiv.org/abs/2611.31811v1)**
  - *Nikolaos Nikolaou*
  - `2026-11-24`
  - We now live in the age of machine-generated mathematics: AI systems produce research-level proofs faster than the human mathematical community can read them. Verification is only part of the challenge. We also need to know whether a "new proof" is indeed new, whether a thousand g…

- **[Learning Compact State Abstractions for LLM Agents](https://arxiv.org/abs/2611.31800v1)**
  - *Yaswanth Chittepu, Raghavendra Addanki, Anup Rao et al.*
  - `2026-11-24`
  - LLM agents commonly use the full interaction history as a proxy for state, retaining all past observations and actions regardless of whether they remain relevant. We instead ask what information an agent actually needs to carry forward. We define agent state as a compact abstract…

- **[A Generative AI Agent to Emulate Interactive Human-driven Vehicles for Automated Driving Testing in Urban Areas](https://arxiv.org/abs/2611.31797v1)**
  - *Jia Hu, Changjian Yu, Panqu Wang et al.*
  - `2026-11-24`
  - Realistic modeling of human-driven vehicle (HDV) interactions is essential for automated driving safety testing in urban areas. Existing methods struggle to reproduce realistic safety-critical interactions involving high collision risk for the following reasons: they often assume…

- **[AGL-SKILL: Coding Harnesses as Agentic Optimizers](https://arxiv.org/abs/2611.31794v1)**
  - *Ryan Tsui, Yuge Zhang, Yuqing Yang*
  - `2026-11-24`
  - Frontier models are increasingly used through harnesses as agents, with growing autonomy to do useful work. Agent performance can often be enhanced by the use of skills: reusable workflows, code, and prompts that provide task-related information or guide the behaviour of the mode…

- **[TACT-Bench: Testing Adaptive Conversational Threats against Tool-Use Agents](https://arxiv.org/abs/2611.31756v1)**
  - *Ilia Hashemi Rad, Feijie Wu, Haoyu Wang et al.*
  - `2026-11-24`
  - The growing autonomy of AI agents in using external tools and making decisions has created an urgent need for comprehensive safety benchmarks. Existing benchmarks test compromised tool channels or adaptive multi-turn attacks, though they may not capture the unique capabilities of…

- **[Where is the Interface for the AI Harness?](https://arxiv.org/abs/2611.31739v1)**
  - *Wafa Johal, Sarah Schombs*
  - `2026-11-24`
  - Norman's gulfs of execution and evaluation have guided interaction design for forty years, but both assume a user who is present in the loop. Agentic delegation breaks that assumption: users describe an outcome and leave, while the agent takes hundreds of unseen actions. Starting…

- **[Reproducing History Is Not Enough: Intervention-Level Assurance for LLM-Generated Simulators](https://arxiv.org/abs/2611.31736v1)**
  - *Ashraf Abdul-Muumin, Aniruddha Chattopadhyay, Noorbakhsh Golilarz et al.*
  - `2026-11-24`
  - Large language models can now write simulation programs of operational processes and workflows. These programs can be reused to answer what-if questions on new records and policies. However, a program that reproduces recorded history can still give wrong answers to what-if questi…

- **[GREMLIN: Generating Random Environments for Meta-Learning with Interacting Networks](https://arxiv.org/abs/2611.33101v1)**
  - *Octave Gaspard*
  - `2026-11-24`
  - Can randomly parameterized neural environments supply useful experience for learning a reinforcement learning algorithm? We investigate this question using DiscoRL's rule-discovery framework, replacing human-designed training games with sixteen selected neural environments. Each…

- **[U-Statistics-Powered LLM Reasoning](https://arxiv.org/abs/2611.33064v1)**
  - *Shijin Gong, Kai Ye, Victor Chernozhukov et al.*
  - `2026-11-24`
  - Since its introduction by DeepSeek, group relative policy optimization (GRPO) has been widely adopted for training large reasoning models and agents, spurring a proliferation of its variants. Yet the group size, a crucial hyperparameter in these GRPO-type algorithms, remains larg…

- **[Breaking the Joint Action Space Dependence in Distributionally Robust Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.32812v1)**
  - *Yue Wang*
  - `2026-11-24`
  - We study the sample complexity of learning robust coarse correlated equilibria (CCE) in finite-horizon, general-sum, distributionally robust Markov games with known rewards and a generative model of the nominal transitions. Each player evaluates a policy by its worst-case return…

- **[Rethinking Reasoning Effort Training in Large Language Models: On-Policy Distillation or Reinforcement Learning?](https://arxiv.org/abs/2611.32131v1)**
  - *Tianliang Lv, Hao Li, Xinchao Xu et al.*
  - `2026-11-24`
  - Large language models have shown strong capabilities on complex tasks, yet how to control their reasoning effort remains a significant challenge for practical deployment. This paper provides a systematic investigation of reasoning-effort training, contrasting reinforcement learni…

- **[Fix How It Acts, Not How It Thinks: Surgical Fine-Tuning of Frontier LLMs](https://arxiv.org/abs/2611.32064v1)**
  - *Sandeep Singh Sandha, Prann Bansal, Arvind Sundararajan*
  - `2026-11-24`
  - Open-weight LLMs are competent software engineers, but they sometimes fail at tasks they are otherwise able to do. Often it is not a failure of reasoning. It is a few small missteps over a long trajectory (repeating a step that has already failed, or declaring the task done while…

- **[Online Environment Repair for Coding Agents](https://arxiv.org/abs/2611.32037v1)**
  - *Sheng Lu, Rui Mao, Zewei Chen et al.*
  - `2026-11-24`
  - Programmatic verifiers provide scalable reward signals for training coding agents with reinforcement learning, yet subtle harness defects and incomplete unit tests allow policies to earn full credit without solving the intended task. Existing training-time defenses intervene eith…

- **[Multi Agent Reinforcement Learning enhanced Federated Learning for Predicting Remaining Useful Lifetime](https://arxiv.org/abs/2611.31880v1)**
  - *Rajarshi Chattopadhyay, Chen-Khong Tham*
  - `2026-11-24`
  - Remaining useful life (RUL) prediction is central to Prognostics and Health Management (PHM). The growth of industrial IoT has unlocked large multivariate sensor streams and enabled deep models - especially Transformers - for long-horizon sequence learning. However, transformers…

- **[Leto: Utility-Centric Agent Memory](https://arxiv.org/abs/2611.33005v1)**
  - *Shuguang Chen, Salman Paracha*
  - `2026-11-24`
  - Large language model (LLM) agents rely on external memory to retain and reuse information across interactions. Existing memory systems treat memory as a record of the past and evaluate it by fidelity to the conversation. However, the value of memory lies in whether it improves th…

- **[SOARS: System One Assisted Reranking for Agentic Search](https://arxiv.org/abs/2611.32917v1)**
  - *Amin Bigdeli, Liye Fu, Fattane Zarrinkalam et al.*
  - `2026-11-24`
  - Deep search agents address complex information needs through iterative retrieval and reasoning, where the relevance of retrieved evidence influences downstream performance. Existing rerankers improve retrieval effectiveness but introduce substantial latency and cost when invoked…

- **[Is Prosody Encoded in the Neural Audio Codec Mimi?](https://arxiv.org/abs/2611.32795v1)**
  - *Nicolas Ballier, Artem Saloev, Erin Pacquetet et al.*
  - `2026-11-24`
  - Neural audio codecs (NACs) have become a fundamental infrastructure for modern speech-language models, discretizing continuous speech signals into token sequences that enable large language models to process and generate audio. Most research evaluates codec quality at the decodin…

- **[SkillCore: Internalizing Generalizable Skills via Scaffolding-Removed Fine-Tuning](https://arxiv.org/abs/2611.32246v1)**
  - *Yi Liu, Changqing Ai, Peijie Dong et al.*
  - `2026-11-24`
  - Runtime skills can improve agents' problem-solving capabilities by providing procedural guidance for tasks such as code review and debugging. However, these benefits reach only a minority of users, as most do not proactively invoke skills in practice. We argue that such generaliz…

- **[SwarmLeak: Does Coordination Improve Privacy Attacks on LLM Agents?](https://arxiv.org/abs/2611.31791v1)**
  - *Asma Farajidizaji, Vyas Raina, Vatsal Raina et al.*
  - `2026-11-24`
  - LLM agents increasingly collaborate in group chats while holding tool access to confidential records, which makes the shared chat an attack surface. It remains unclear whether several colluding attackers extract such information more effectively than one. We introduce SwarmLeak,…

- **[fork() for Agents: Agent Kernel for Non-blocking LLM Orchestration](https://arxiv.org/abs/2611.31727v1)**
  - *Ankit Chadha, Pratyay Banerjee*
  - `2026-11-24`
  - LLM-based agents typically execute tool calls synchronously and discard completed work upon failure. Subgraph-selective recovery, re-executing only a failed node's transitive descendants, is a well-established pattern in distributed systems (Spark, Erlang/OTP, Dryad), and recent…

- **[CANON: Agent-Assisted Construction of Canonical Differential Equations for Feynman Integrals](https://arxiv.org/abs/2611.33100v1)**
  - *Dong-shan Jian, Yuanche Liu, Yan-qing Ma et al.*
  - `2026-11-24`
  - The construction of canonical basis is an important procedure in the calculation of multi-loop Feynman integrals via the canonical differential equation methods. Currently, there are various different methods for this purpose. Among them, no single method is universally applicabl…

- **[Multi-Agent Coordination Through Stigmergy for Canal Network Formation on Real Terrain](https://arxiv.org/abs/2611.32966v1)**
  - *Jordan Kennedy, Federico Oliva, Amir Degani et al.*
  - `2026-11-24`
  - Terrain-modifying robot swarms operating in unstructured outdoor environments must coordinate under uncertain dynamics despite unreliable communication and incomplete global information. Stigmergy offers a decentralized alternative by allowing agents to coordinate indirectly thro…

- **[Recursive Collective Intelligence: Emergence on an Equal-Budget Ladder in Multi-Agent LLM Systems](https://arxiv.org/abs/2611.32606v1)**
  - *Lixuan He, Shengqu Cai, Fang Wu et al.*
  - `2026-11-24`
  - Large language models increasingly work as teams of agents, and a team is expected to solve problems beyond the reach of any single member. Most evaluations credit a team for outperforming a single agent, without accounting for the additional computation: a team may consume many…

- **[TimeTravelContainer: A Live Forking Sandbox for Stateful Agent Exploration](https://arxiv.org/abs/2611.32255v1)**
  - *Zizheng Guo, Yanqing Zhang, Nathaniel Pinckney et al.*
  - `2026-11-24`
  - LLM agents that drive stateful tools (e.g., interactive shells, design environments, simulation engines) frequently need to clone, backtrack, and parallelize live sessions to support exploration. However, cloning a live session today requires serializing the tool's in-memory stat…

- **[AgentDRC: Multi-Agent Algorithms for Spatially-Aware Automated DRC Correction](https://arxiv.org/abs/2611.31876v1)**
  - *Pengju Liu, Nuo Xu, Winso Chen et al.*
  - `2026-11-24`
  - Design Rule Checking (DRC) error fixing remains a time-consuming bottleneck in physical design, often requiring manual intervention despite advanced EDA optimizations. Existing LLM-agent approaches fall short due to redundant contextual shapes, limited spatial reasoning over raw…

- **[Delta-Vega Hedging with Deep Reinforcement Learning: From Simulation to Reality](https://arxiv.org/abs/2611.32790v1)**
  - *Michele Colombi, Marco Di Francesco, Pietro Rossi*
  - `2026-11-24`
  - Hedging an option portfolio with the underlying asset alone leaves the position exposed to changes in volatility, which can be managed by trading another derivative, at higher transaction costs. We propose a deep reinforcement learning approach to hedge both price and volatility…

- **[CATWAY: Cost-sensitive agentic three-way robot decisions with calibrated language-model confidence](https://arxiv.org/abs/2611.31694v1)**
  - *Erik Derner*
  - `2026-11-23`
  - A language-model robot agent must decide whether to execute, question or refuse an instruction, and an unsafe execution costs far more than an unneeded question. No prior robot gate derives all its thresholds from error costs or acts on calibrated probabilities, and none was fitt…

- **[Provenance Loss and Repair in Multilingual Compaction](https://arxiv.org/abs/2611.31668v1)**
  - *Ian Miao, Fangrui Zhu, Bowen Jiang*
  - `2026-11-23`
  - Conversational assistants compact older messages into short notes and evict the originals. When the note's language requires a distinction that English leaves open, such as Spanish adjective gender (agotado vs. agotada), messages that omit or explicitly state that attribute can y…

- **[BRAG: Bayesian Retrieval Augmented Generation](https://arxiv.org/abs/2611.31656v1)**
  - *Javier Movellan, Manjot Bilkhu, Young-mok Jung et al.*
  - `2026-11-23`
  - Retrieval-augmented generation (RAG) ranks memory chunks by semantic similarity to the query. Many methods improve on this by learning from feedback on what was retrieved, but each is a separate heuristic, with no account of when it is the right choice. We introduce BRAG, a gener…

- **[E2SIM: Long-Horizon Simulation of Everyday Human Behavior with Evolving States](https://arxiv.org/abs/2611.31641v1)**
  - *Ziwei Gong, Xiangyang Yin, Thai Quoc On et al.*
  - `2026-11-23`
  - AI agents are increasingly expected to support users over long periods, across work, and daily life. This requires modeling not only who users are, but also how their goals, interests, activities, and interactions evolve over time. A challenge in longitudinal user simulation is m…

- **[Wavefront: Low-Rank Drafting with Parallel Causal Refinement for Speculative Decoding](https://arxiv.org/abs/2611.31638v1)**
  - *Huy Huu Nguyen, Xin Huang*
  - `2026-11-23`
  - Speculative decoding accelerates LLM inference by letting a cheap drafter propose tokens that the target model verifies in parallel. Parallel block drafters such as DFlash and P-EAGLE propose a whole block in one forward pass, but they lose the dependence between tokens in the bl…

- **[Multi-agent System for Automatic Discovery of Pareto-optimal Meta-solvers for PDEs](https://arxiv.org/abs/2611.31611v1)**
  - *Youngkyu Lee, Shanqing Liu, Jerome Darbon et al.*
  - `2026-11-23`
  - Designing linear solvers for discretized partial differential equations requires problem-specific expertise. We present a multi-agent framework, in which language-model agents propose, critique, implement, and evaluate solver configurations assembled from Krylov methods, precondi…

- **[GoldiBench: Right Tools, Wrong Amount -- Benchmarking Agents on Effect Judgement in Professional Editing](https://arxiv.org/abs/2611.31590v1)**
  - *Wang Yang, Xinpeng Li, Yanyan Zhang et al.*
  - `2026-11-23`
  - Real editing requests describe a look, not the steps to reach it, so an agent that serves them must judge how much of each tool the look takes. Existing benchmarks do not measure this: their tasks either state the tools and values, or leave the amount open and are scored by VLM j…

- **[LatentLens: Rethinking Latent Interface in Multi-Agent Systems](https://arxiv.org/abs/2611.31582v1)**
  - *Ziqing Yang, Kewei Cheng, Mingjie Li et al.*
  - `2026-11-23`
  - Latent interfaces let agents in a multi-agent system communicate through continuous representations rather than decoded text. Prior work reports performance and efficiency gains, but neither separates latent communication from the agent harness nor examines its internal component…

- **[Off-the-Shelf Autonomous Agents for Game Playtesting](https://arxiv.org/abs/2611.31570v1)**
  - *Ayush Maniar, Eryk Banatt*
  - `2026-11-23`
  - In playtesting games, a human operator is typically required to test most gameplay elements. In this work we present Buddy, an autonomous game solving agent which can solve long time horizon objectives in an unseen 3D role-playing game using off-the-shelf language model systems.…

- **[COGENT: A Modular Cognitive Architecture for Agentic User Simulation](https://arxiv.org/abs/2611.31559v1)**
  - *Yikun Chi, Adam Davies, Debarati Das et al.*
  - `2026-11-23`
  - LLM-based user simulation can support interface design, accessibility research, and interactive-agent evaluation, but standard computer-use agents are optimized for task completion rather than reproducing how people perceive, reason, and act. We introduce COGENT (COGnitive agENT)…

- **[Agent Recovery Gone Wrong: Measuring Harm Beyond Duplicate Calls](https://arxiv.org/abs/2611.31554v1)**
  - *Artem Trofimov, Boris Novikov*
  - `2026-11-23`
  - Code-executing LLM agents submit blocks of code that issue several API writes. If a block fails after some of its writes have taken effect, the agent rewrites the block and continues. It is unknown how often such a recovery harms the external state when the failure occurs natural…

- **[Reproducible Social Structure Emerges From Free-Form Interaction Among LLM Agents](https://arxiv.org/abs/2611.31543v1)**
  - *Tom Alisch, Sonia Murthy, Robert Hawkins et al.*
  - `2026-11-23`
  - Multi-agent LLM simulations are increasingly used as models of social systems, but most published findings are anecdotal, i.e., drawn from a single run. It is therefore unclear which observed phenomena are robust findings of the simulated system itself, and which were random even…

- **[Where Agent Defenses Fail: A Case Study of Policy Compositions and Measurement Limits](https://arxiv.org/abs/2611.31541v1)**
  - *Kunwar Sangram Singh, Krishna Mohan Guda Nagavenkata Srinivasa*
  - `2026-11-23`
  - A coding agent may need to upload a report while its sandbox blocks network access. A host mediator can restore delivery, but an injected instruction may add a secret to the approved request. We study this interaction using files and HTTP receipts to measure effects independently…

- **[Agent Evaluation Without Ground Truth: A Null Proportion Perspective](https://arxiv.org/abs/2611.31539v1)**
  - *Brian M. Cho, Michael Lindon, Nathan Kallus*
  - `2026-11-23`
  - The correctness of actions taken by agents is typically evaluated against known, externally verified ground truth labels, such as whether a proof is correct or whether code compiles and passes unit tests. However, as coding and science agents are entrusted with more end-to-end au…

- **[One Step, Four Clocks: How GUI Agents Fall Out of Step](https://arxiv.org/abs/2611.31522v1)**
  - *Zhanwen Chen, Tianchun Wang*
  - `2026-11-23`
  - GUI agents can choose correct actions yet fail as interfaces change during deliberation. Latency alone cannot explain these failures because actions may become invalid at different interaction stages. We model four events: environment change, observation availability, decision co…

- **[PatientFlowSynth: Evaluating FHIR Agents with Matched Patient Charts](https://arxiv.org/abs/2611.31521v1)**
  - *Anthony Cuturrufo, Ratul Ghosh, Devashish Khatwani et al.*
  - `2026-11-23`
  - Agents that search patient charts must classify claims from retrieved records, including cases with missing or conflicting evidence. In Fast Healthcare Interoperability Resources (FHIR), status fields can change how those records should be interpreted. PatientFlowSynth provides 1…

- **[Evaluating Frontier-Model Agent Skills with Open-Weight Models in a Science Gateway](https://arxiv.org/abs/2611.31480v1)**
  - *Komal Thareja, Mats Rynge, Anirban Mandal et al.*
  - `2026-11-23`
  - Scientific analyses that span many jobs and computing sites depend on workflow management systems to run reliably, but writing a production workflow requires expertise in such a system, which many domain scientists do not have. Coding agents can supply this expertise when they ar…

- **[SpatialCraft: Evolving Procedural Intelligence from Experience and Skills for Spatial Reasoning Agents](https://arxiv.org/abs/2611.31475v1)**
  - *Xiwei Liu, Yulong Li, Xuhui Li et al.*
  - `2026-11-23`
  - Spatial reasoning agents increasingly rely on external tools, such as 3D reconstruction, segmentation, and geometric computation, to answer questions that a multimodal large language model (MLLM) cannot resolve from pixels alone. Tool access, however, shifts the bottleneck to orc…

- **[Below the Stopwatch: Checking the Performance Claims of Coding Agents in the Kernel](https://arxiv.org/abs/2611.31460v1)**
  - *Yuvraj Sehgal, Sneh Patel, Mahsa Panahandeh et al.*
  - `2026-11-23`
  - Coding agents open many pull requests (PRs) that claim to make software faster. Most such claims also give a reason, such as "cache the result" or "read the file once". A stopwatch can show that code got faster, but not that it got faster for the stated reason. We present Below,…

- **[Taxi: Analyzing Agents at (Real) Scale](https://arxiv.org/abs/2611.31457v1)**
  - *Guy Dar*
  - `2026-11-23`
  - In this technical report, we present Taxi -- a system for debugging, clustering, and monitoring agents at scale. Taxi scales to millions of steps efficiently. This is made possible by a combination of scalable analysis methods. Taxi relies primarily on clustering to generate a ta…

- **[Learning What vs. Learning How: Decomposing Task and Interface Competence in Agentic Training](https://arxiv.org/abs/2611.31427v1)**
  - *Chaeeun Lee, Hossein A. Rahmani, Aryo Pradipta Gema et al.*
  - `2026-11-23`
  - LLM agents operate through harnesses that define system prompts, action formats, feedback loops, and resource constraints. A model may possess the knowledge needed to solve a task yet fail to express that knowledge through a particular harness. This raises a basic question: when…

- **[ContextLure: Exploiting Benign Conversation History for Indirect Prompt Injection](https://arxiv.org/abs/2611.31424v1)**
  - *Yi Han, Zhen Sun, Zhijie Deng et al.*
  - `2026-11-23`
  - As LLMs become more capable, agents can perform more complex tasks with tools and maintain longer interactions with users. These benign conversations contain evidence on task results, user concerns, and operational constraints. The risk is that attackers who can observe benign co…

- **[Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ](https://arxiv.org/abs/2611.31228v1)**
  - *Daniel Theron*
  - `2026-11-23`
  - Prompting language models to verbalize stepwise numerical confidence during generation is an increasingly popular approach for triggering backtracking and error correction in agentic reasoning. This strategy presupposes two capabilities: (1) in-situ monitoring fidelity (does conf…

- **[ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents](https://arxiv.org/abs/2611.31198v1)**
  - *Rui Sun, Junhua Huang, Luca Zancato et al.*
  - `2026-11-23`
  - Recent multimodal search agents use reasoning, vision, and live web search across many turns to answer questions beyond parametric knowledge by orchestrating a small library of hand-crafted search and visual tools. However, the library is laborious to create and maintain, and fro…

- **[CO-GRAFT: Attributing Reinforcement Learning Gains in Search Agents via Role-Level Policy Grafting](https://arxiv.org/abs/2611.31185v1)**
  - *Ramraj Chandradevan, Sayontan Ghosh, Vinoth Selvendran*
  - `2026-11-23`
  - Reinforcement learning (RL) improves large language model search agents by up to 32 exact-match (EM) points over their pre-RL initializations, yet overall accuracy gains do not identify which underlying functional capabilities improve or interact during training. We introduce CO-…

- **[Habitats: A Framework for Open-Ended Evolution of Agent Objectives](https://arxiv.org/abs/2611.31160v1)**
  - *Nicolas Bolouri, Gaya Mehenni, Daniel Toyama*
  - `2026-11-23`
  - Designing what an agent should optimize can be as difficult as optimizing the agent itself. Existing language-model-based reward-generation methods typically refine objectives for predefined tasks and couple the decision of what to explore with the synthesis of how to implement i…

- **[What People Choose Not to Say: A Multimodal Benchmark for Fine-Grained Information Manipulation in Conversations](https://arxiv.org/abs/2611.31346v1)**
  - *Yuhan Bian, Zhaokai Liang, Jia Wang et al.*
  - `2026-11-23`
  - Recent advances in MLLMs have improved social understanding, enabling models to recognize emotions and distinguish truthful from deceptive behaviors. However, existing benchmarks largely focus on coarse-grained emotion recognition or binary truth-deception detection, overlooking…

- **[Self-Upgrading Embodied Agents](https://arxiv.org/abs/2611.31117v1)**
  - *Jiajun Fan, Neil He, Qinglong Zheng et al.*
  - `2026-11-23`
  - An embodied agent built on a language model goes to work with the weights it was given and keeps them for life. To get better, it needs more training, or reflection, memory, search or prompts that cost every step and are lost when the task changes. Editing weights by reasoning, w…

- **[RUIBench: What Makes a Good Robot-Use Interface?](https://arxiv.org/abs/2611.31115v1)**
  - *Yanzhe Chen, Zhijun Cao, Zechen Bai et al.*
  - `2026-11-23`
  - Foundation models can reason about complex physical tasks, yet translating this intelligence into reliable robot execution remains challenging. We argue that a critical, often overlooked factor is the robot-use interface (RUI), which determines how agents express and execute phys…

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

- **[Per-Attack Blocking Hides Catalog Vulnerability: A Weakest-Link Analysis of Tool Manifests](https://arxiv.org/abs/2611.31338v1)**
  - *Karthik Karunanithi*
  - `2026-11-23`
  - Runtime controls for tool-using agents depend on manifests that state what each tool may read and where its output may go. Evaluations of these controls, including ChainCaps, report per-attack blocking: the share of attacks a set of manifests stops. We show that this is the wrong…

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

- **[Aggregation Rules Induced by KL-Regularised Preference Dynamics on Networks](https://arxiv.org/abs/2611.30941v1)**
  - *Milan Vojnovic*
  - `2026-11-23`
  - We study agents that each align a model to their own preference data while observing one another, and ask which aggregation rule the resulting policies implement. Each round, an agent takes one KL-regularised step. The step involves a reference that the agent is penalised for lea…

- **[Bridging Continuous-Time MAPF and Industrial AGV Fleet Coordination with Lazy Priority-Based Search](https://arxiv.org/abs/2611.30874v1)**
  - *Federico Signorile, Raffaele Carli, Alessandro Bertogli et al.*
  - `2026-11-23`
  - Continuous-time multi-agent path finding on roadmaps (MAPF$_R$) offers a principled way to coordinate robot fleets with geometric collision avoidance, yet its deployment on industrial automated guided vehicle (AGV) infrastructures remains challenging, as highly connected and redu…

- **[GameDojo: Benchmarking Real-Time Interactive Agents in Video Games](https://arxiv.org/abs/2611.30771v1)**
  - *Kuan Zhang, Zhihao Yang, Yukun Chen et al.*
  - `2026-11-23`
  - Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss en…

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

- **[RoboInF: A Benchmark for Instruction Fidelity in Robotic Manipulation](https://arxiv.org/abs/2611.30555v2)**
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

- **[mini-psych-agent: Evaluating Human-Like Behavior in LLM Agents through Interactive Psychological Environments](https://arxiv.org/abs/2611.30365v2)**
  - *Yi-Fei Cao, Tianxin Huang, Hanbo Xie et al.*
  - `2026-11-23`
  - A Large Language Model (LLM), its harness, and the test-time compute budget jointly determine its behavior. Consequently, the same underlying model, embedded in different agentic workflows or allocated different amounts of test-time compute, can exhibit markedly different perform…

- **[RepoClean: Evaluating Coding Agents on Repository-Level Obsolete Code Cleanup](https://arxiv.org/abs/2611.30350v1)**
  - *Hongyixuan Yuan, Qixing Zhou, Pengcheng Huang et al.*
  - `2026-11-23`
  - Large language model (LLM) agents have demonstrated strong repository-level programming capabilities. However, as software evolves, repository code may become redundant or obsolete, increasing maintenance costs and potentially introducing functional issues. Agents must therefore…

- **[MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation](https://arxiv.org/abs/2611.30287v1)**
  - *Yuxuan Chen, Changwei Lv, Yunfei Li et al.*
  - `2026-11-23`
  - AI agents accumulate conversations, images, and documents through long-term interactions with users. Answering later questions often requires connecting evidence across these records, yet the resulting understanding is rarely retained, allowing mistakes to recur on related questi…

- **[Attributing Security Outcomes in LLM-Agent Evaluations: The Role of Content-Free State](https://arxiv.org/abs/2611.30259v1)**
  - *Abdelmonaim Bounite, Zangir Iklassov*
  - `2026-11-23`
  - Security benchmarks for LLM agents record whether each attack succeeded and compare agents, attacks, and defenses by attack success rate (ASR). Such comparisons are valid only if the agent, the attack, and the defense cause each verdict. We show that verdicts also depend on conte…

- **[Scoring Recovery-Time Agent Security: Proposals, Effects, and Retry Instructions](https://arxiv.org/abs/2611.31318v1)**
  - *Paul Deepakraj Retinraj*
  - `2026-11-23`
  - A timed-out tool write may be absent, committed, or still in flight. Evaluating an agent only on whether its goal exists can hide harmful recovery actions: auditing 12 supplied traces changes apparent completion from 10/12 to 8/12. We introduce an executable evaluation that separ…

- **[What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym](https://arxiv.org/abs/2611.30207v1)**
  - *Yikai Zhang, Mai Xu, Yunbei Zhang et al.*
  - `2026-11-23`
  - Reinforcement learning (RL) trains coding agents on software tasks whose hidden tests decide the reward, yet task collections check these tests only against the reference fix. We ask what makes a task good training data, focusing on the correctness of its reward labels. We audit…

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

- **[Measuring Counterfactual Credit in a Replayable Wildfire-Suppression Benchmark](https://arxiv.org/abs/2611.31499v1)**
  - *Alireza Moghaddasi*
  - `2026-11-23`
  - In cooperative multi-agent reinforcement learning, learned critics are usually evaluated by how well they predict the team's return. Yet predicting a team's return and assigning credit to individual actions are distinct tasks. To test credit directly, we introduce FLARE (Fireline…

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

- **[SecondChance: Benchmarking Reliable Error Recovery in AI Agents](https://arxiv.org/abs/2611.31586v1)**
  - *Atahan Dokme, Adar Avsian, Larry Heck*
  - `2026-11-23`
  - AI agents make errors while they act, and their reliability depends on what they do afterwards. Existing recovery benchmarks mostly inject faults, involve no user and score whether the task is eventually completed, so they cannot show whether an agent undid its own silent error,…

- **[RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments](https://arxiv.org/abs/2611.31002v1)**
  - *Jinkun Liu, Yingze Wang, Situ Wang et al.*
  - `2026-11-23`
  - Agentic Robotics, in which foundation models act as coding agents to control robots through executable programs, has emerged as a compelling paradigm for embodied intelligence. Yet unlike software engineering, where massive executable environments power post-training, robotics re…

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

- **[Heterogeneous Risk-Sensitive Evolutionary Learning in Coordination Games: Polarization, Welfare Loss, and Intervention for Efficiency](https://arxiv.org/abs/2611.31568v1)**
  - *Solaleh Mohammadi, Yiman Fong, Kaiqing Zhang*
  - `2026-11-23`
  - We study evolutionary learning in coordination games in a finite population of agents with heterogeneous risk attitudes, modeled using the entropic risk measure (ERM). The population consists of two subpopulations, each with a fixed risk attitude. Under risk-sensitive best respon…

- **[Sampling at Scale: Distributed Multi-Agent Trajectory Optimization](https://arxiv.org/abs/2611.31561v1)**
  - *Minchan Jung, Dimitrios S. Georgiou, Augustinos D. Saravanos et al.*
  - `2026-11-23`
  - Multi-agent trajectory optimization poses two coupled challenges: effectively exploring non-convex landscapes and scaling favorably to large teams of agents. Sampling-based methods are natural candidates for the exploration challenge but scale poorly with problem dimension. Moreo…

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

- **[Evolutionary AI Control: Population-Level Safety Under Reproduction, Heredity, and Selection](https://arxiv.org/abs/2611.31312v1)**
  - *Andrew T. Cadotte*
  - `2026-11-22`
  - An AI agent can satisfy every individual safety check and still give rise to a population that violates a collective safety limit. This risk arises in open multi-agent systems, where agents copy themselves, modify their successors, and change system membership during a run. Selec…

- **[Wactorz: Self-Writing LLM Agents That Discover, Repair, and Migrate at the Edge](https://arxiv.org/abs/2611.29619v1)**
  - *Panagiotis Kasnesis, Lazaros Toumanidis, Amalia Contiero Syropoulou et al.*
  - `2026-11-22`
  - Most LLM agent frameworks build a crew that runs a task and exits. Physical environments (e.g., homes, labs, factory floors) need agents that stay up for months, survive their own bugs, and run on whatever hardware is already next to the sensors. We present Wactorz, an open-sourc…

- **[Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits with LLM Agents](https://arxiv.org/abs/2611.29613v1)**
  - *Junpeng Hou, Jiaxing Qu, Derek Cheng et al.*
  - `2026-11-22`
  - Web-scale recommender models evolve primarily through retraining or fine-tuning. We propose \emph{weight coding}, a methodology for model evolution through direct, executable weight edits. A large language model (LLM) agent inspects model structure and parameters, formulates hypo…

- **[KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware](https://arxiv.org/abs/2611.29590v1)**
  - *Shuaiwei Huang, Weihua Du, Allen Wu et al.*
  - `2026-11-22`
  - Efficient AI computation depends on hardware that evolves over time, shifting the strategies needed to implement performant code. For CPU kernels, a key evolving factor is the set of available architectural extensions, which expose specialized hardware instructions that change th…

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

- **[When Successful Collaboration Becomes an Attack Surface: Insider Memory Poisoning in Multi-Agent Systems](https://arxiv.org/abs/2611.31307v1)**
  - *Jihyung Ahn, Buru Chang*
  - `2026-11-22`
  - Recent Multi-Agent Systems (MAS) increasingly use shared memory to store and reuse successful collaboration records, enabling teams to improve across tasks. However, this memory introduces a new attack surface for malicious insiders. Unlike existing insider attacks that inject mi…

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

- **[GameAnything: From Any Inspirations to Playable Game Worlds](https://arxiv.org/abs/2611.29238v1)**
  - *Wenyi Wu, Siqi Liu, Yuru Feng et al.*
  - `2026-11-22`
  - AI-driven game development holds the potential to transform diverse human inspirations into interactive experiences. However, existing systems and benchmarks primarily focus on explicit development specifications, with limited support for adapting multimodal references and evalua…

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

- **[Social Interaction Breaks Replicate Independence in Controlled-Clone LLM Agents](https://arxiv.org/abs/2611.29581v2)**
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


## Harness  (135)

### NeurIPS

- **[OpenUnlearning: Accelerating LLM Unlearning via Unified Benchmarking of Methods and Metrics](https://arxiv.org/abs/2506.12618)**
  - *Vineeth Dorna, Anmol Reddy Mekala, Wenlong Zhao et al.*
  - **NeurIPS 2025** · `2025-06-14`
  - Robust unlearning is crucial for safely deploying large language models (LLMs) in environments where data privacy, model safety, and regulatory compliance must be ensured. Yet the task is inherently challenging, partly due to difficulties in reliably measuring whether unlearning…

- **[SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks](https://arxiv.org/abs/2506.11791)**
  - *Hwiwon Lee, Zi-Qi Zhang, Hanxiao Lu et al.*
  - **NeurIPS 2025** · `2025-06-13`
  - Rigorous security-focused evaluation of large language model (LLM) agents is imperative for establishing trust in their safe deployment throughout the software development lifecycle. However, existing benchmarks largely rely on synthetic challenges or simplified vulnerability dat…

- **[AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents](https://arxiv.org/abs/2506.00641)**
  - *Han-Jun Luo, Shen-Yu Dai, Chiming Ni et al.*
  - **NeurIPS 2025** · `2025-05-31`
  - Despite the rapid advancement of LLM-based agents, the reliable evaluation of their safety and security remains a significant challenge. Existing rule-based or LLM-based evaluators often miss dangers in agents'step-by-step actions, overlook subtle meanings, fail to see how small…

- **[ThinkBench: Dynamic Out-of-Distribution Evaluation for Robust LLM Reasoning](https://arxiv.org/abs/2502.16268)**
  - *Shu-Lin Huang, Lin-Yi Yang, Yan Song et al.*
  - **NeurIPS 2025** · `2025-02-22`
  - Evaluating large language models (LLMs) poses significant challenges, particularly due to issues of data contamination and the leakage of correct answers. To address these challenges, we introduce ThinkBench, a novel evaluation framework designed to evaluate LLMs' reasoning capab…


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

- **[am-ELO: A Stable Framework for Arena-based LLM Evaluation](https://arxiv.org/abs/2505.03475)**
  - *Zi-Rui Liu, Jia-Tong Li, Yan Zhuang et al.*
  - **ICML 2025** · `2025-05-06`
  - Arena-based evaluation is a fundamental yet significant evaluation paradigm for modern AI models, especially large language models (LLMs). Existing framework based on ELO rating system suffers from the inevitable instability problem due to ranking inconsistency and the lack of at…

- **[Accelerating Unbiased LLM Evaluation via Synthetic Feedback](https://arxiv.org/abs/2502.10563)**
  - *Zhao-Yi Zhou, Yu-Da Song, Andrea Zanette*
  - **ICML 2025** · `2025-02-14`
  - When developing new large language models (LLMs), a key step is evaluating their final performance, often by computing the win-rate against a reference model based on external feedback. Human feedback is the gold standard, particularly for capturing nuanced qualities like coheren…

- **[Copilot Arena: A Platform for Code LLM Evaluation in the Wild](https://arxiv.org/abs/2502.09328)**
  - *Wayne Chi, Valerie Chen, A. Angelopoulos et al.*
  - **ICML 2025** · `2025-02-13`
  - Evaluating in-the-wild coding capabilities of large language models (LLMs) is a challenging endeavor with no clear solution. We introduce Copilot Arena, a platform to collect user preferences for code generation through native integration into a developer's working environment. C…


### ICLR

- **[RocketEval: Efficient Automated LLM Evaluation via Grading Checklist](https://arxiv.org/abs/2503.05142)**
  - *Tian-Jun Wei, Wei Wen, Rui-Zhi Qiao et al.*
  - **ICLR 2025** · `2025-03-07`
  - Evaluating large language models (LLMs) in diverse and challenging scenarios is essential to align them with human preferences. To mitigate the prohibitive costs associated with human evaluations, utilizing a powerful LLM as a judge has emerged as a favored approach. Nevertheless…

- **[Know Thy Judge: On the Robustness Meta-Evaluation of LLM Safety Judges](https://arxiv.org/abs/2503.04474)**
  - *Francisco Eiras, Eliott Zemour, Eric Lin et al.*
  - **ICLR 2025** · `2025-03-06`
  - Large Language Model (LLM) based judges form the underpinnings of key safety evaluation processes such as offline benchmarking, automated red-teaming, and online guardrailing. This widespread requirement raises the crucial question: can we trust the evaluations of these evaluator…


### KDD

- **[Not All Interpretation Methods Are Created Equal: Tiered Evaluation of AI Interpretability](https://arxiv.org/abs/2611.31833v1)**
  - *Nicolas Sanchez, Bin Yu*
  - **KDD** · `2026-11-24`
  - As AI transitions to sociotechnical deployments, uninterpretable models pose serious threats to reliability, public trust and contestability. However, not all interpretation methods are created equal: for interpretability to enhance deployment safety and effectiveness, interpreta…

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, Artem Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…


### ACL

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://arxiv.org/abs/2507.21028)**
  - *Jia-Ju Chen, Yuxuan Lu, Xiaojie Wang et al.*
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
  - *Yong-Qi Leng, Ren-Ren Jin, Yue Chen et al.*
  - **ACL 2025**
  - With the increasing capability of large language models (LLMs), LLM-as-a-judge has emerged as a new evaluation paradigm. Compared with traditional automatic and manual evaluation, LLM evaluators exhibit better interpretability and efficiency. Despite this, existing LLM evaluators…


### EMNLP

- **[Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores](https://arxiv.org/abs/2601.13885)**
  - *Esma Balkir, Alice Pernthaller, Marco Basaldella et al.*
  - **EMNLP 2026** · `2026-01-20`
  - Computerized Adaptive Testing (CAT) has proven effective for efficient LLM evaluation on multiple-choice benchmarks, but modern LLM evaluation increasingly relies on generation tasks where outputs are scored continuously rather than marked correct/incorrect. We present a principl…

- **[Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses](https://arxiv.org/abs/2509.16093)**
  - *Fangyi Yu, Nabeel Seedat, Drahomira Herrmannova et al.*
  - **EMNLP 2025** · `2025-09-19`
  - Evaluating long-form answers in high-stakes domains such as law or medicine remains a fundamental challenge. Standard metrics like BLEU and ROUGE fail to capture semantic correctness, and current LLM-based evaluators often reduce nuanced aspects of answer quality into a single un…

- **[ArtifactsBench: Bridging the Visual-Interactive Gap in LLM Code Generation Evaluation](https://arxiv.org/abs/2507.04952)**
  - *Chen-Chen Zhang, Yu-Hang Li, Jia-Heng Liu et al.*
  - **EMNLP 2025** · `2025-07-07`
  - The generative capabilities of Large Language Models (LLMs) are rapidly expanding from static code to dynamic, interactive visual artifacts. This progress is bottlenecked by a critical evaluation gap: established benchmarks focus on algorithmic correctness and are blind to the vi…

- **[ReliableEval: A Recipe for Stochastic LLM Evaluation via Method of Moments](https://arxiv.org/abs/2505.22169)**
  - *Gili Lior, Eliya Habba, Shahar Levy et al.*
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

- **[ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds](https://arxiv.org/abs/2611.32649)**
  - *Qingle Liu, Jieming Li, Pei-lin Li et al.*
  - 🤗 Featured · `2026-11-24`
  - In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline,…

- **[Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation](https://arxiv.org/abs/2611.31358)**
  - *Guo Chen, Fuxiao Liu, Haoqin Tu et al.*
  - 🤗 Featured · `2026-11-23`
  - Visual creation demands expressive imagery together with precise control over text, layout, and structure. We introduce Nemotron-Labs-VisualCreation, an agentic framework that connects these capabilities through Pixel as Code. Raster images are represented by learned discrete vis…

- **[Small Learned Projections for Semantic-Reversal-Aware Retrieval with Spectral Acceleration: A Four-Domain Empirical Study](https://arxiv.org/abs/2611.31442)**
  - *Sayed Amir Karim*
  - 🤗 Featured · `2026-11-23`
  - Dense-embedding retrievers can fail adversarially: when a query is answered by a document A and reversed by a near-copy B that differs from A by a small meaning-changing edit (a "trap"), raw cosine over E5-Large-v2 places B in the top-10 for 82-100% of queries at a pool of 5,000.…

- **[Avalon-M1: Reinforcement Learning from Collective Rewards](https://arxiv.org/abs/2611.32539)**
  - *Iliyan Zarov, Henry Course, Anthony Hartshorn et al.*
  - 🤗 · `2026-11-24`
  - We introduce reinforcement learning from collective rewards (RLCR), a recipe for jointly training language models to act as agent organisations under latency constraints. A CEO and up to eight specialists share one policy, co-ordinate through a message board and workspace, and ar…

- **[Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance](https://arxiv.org/abs/2611.33098v1)**
  - *Lingwei Gu, Jimmy Lin*
  - `2026-11-24`
  - Agents built on frontier language models are expensive. At every step, the frontier model re-reads its entire context and executes every subtask regardless of its difficulty. This paper explores the simple thesis that much of this cost can be removed by delegating easy subtasks t…

- **[ShellBench: What Matters More for AI Agents, Models, or Harness for Everyday Tasks](https://arxiv.org/abs/2611.32946v1)**
  - *Vincent Koc, Aditya Washikar, Rishab Naveen Venkataraman et al.*
  - `2026-11-24`
  - The use of AI agents among the general public has been increasing exponentially throughout 2026, though it is often hard for users to determine which configuration is most effective for their personal use. To help provide clarity here we introduce ShellBench, 100 day-to-day tasks…

- **[Economic World Model](https://arxiv.org/abs/2611.32663v1)**
  - *Qirui Mi, Yujia Ming, Bo Li et al.*
  - `2026-11-24`
  - Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions? To answer this question, we define an economic world model (EWM) as an agent's internal representation of how an econo…

- **[Rethinking Video Agents: When and Why Video Harnesses Work](https://arxiv.org/abs/2611.31883v1)**
  - *Luoyuan Zhang, Xuanyu Zheng, Yancheng Long et al.*
  - `2026-11-24`
  - Video understanding depends not only on how models reason about visual evidence, but also on which evidence they observe. Fixed observation policies determine this evidence in advance; agentic harnesses allow models to seek further observations as their understanding develops. Th…

- **[AGL-SKILL: Coding Harnesses as Agentic Optimizers](https://arxiv.org/abs/2611.31794v1)**
  - *Ryan Tsui, Yuge Zhang, Yuqing Yang*
  - `2026-11-24`
  - Frontier models are increasingly used through harnesses as agents, with growing autonomy to do useful work. Agent performance can often be enhanced by the use of skills: reusable workflows, code, and prompts that provide task-related information or guide the behaviour of the mode…

- **[Where is the Interface for the AI Harness?](https://arxiv.org/abs/2611.31739v1)**
  - *Wafa Johal, Sarah Schombs*
  - `2026-11-24`
  - Norman's gulfs of execution and evaluation have guided interaction design for forty years, but both assume a user who is present in the loop. Agentic delegation breaks that assumption: users describe an outcome and leave, while the agent takes hundreds of unseen actions. Starting…

- **[Online Environment Repair for Coding Agents](https://arxiv.org/abs/2611.32037v1)**
  - *Sheng Lu, Rui Mao, Zewei Chen et al.*
  - `2026-11-24`
  - Programmatic verifiers provide scalable reward signals for training coding agents with reinforcement learning, yet subtle harness defects and incomplete unit tests allow policies to earn full credit without solving the intended task. Existing training-time defenses intervene eith…

- **[TimeTravelContainer: A Live Forking Sandbox for Stateful Agent Exploration](https://arxiv.org/abs/2611.32255v1)**
  - *Zizheng Guo, Yanqing Zhang, Nathaniel Pinckney et al.*
  - `2026-11-24`
  - LLM agents that drive stateful tools (e.g., interactive shells, design environments, simulation engines) frequently need to clone, backtrack, and parallelize live sessions to support exploration. However, cloning a live session today requires serializing the tool's in-memory stat…

- **[MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for Parallel Computing](https://arxiv.org/abs/2611.33119v1)**
  - *Scott Piersall, Yang Gao, Shenyang Liu et al.*
  - `2026-11-24`
  - Large language models (LLMs) can generate parallel programs, but their correctness and performance depend strongly on the instructions that guide generation. We present \textsc{MetaFORGE}, an execution-grounded meta-learning framework that iteratively optimizes persistent natural…

- **[When Online Adaptation of Resilience Policies Hurts: Safe Exploration and Measurement Pitfalls in Resilience4j](https://arxiv.org/abs/2611.32015v1)**
  - *Rajat M. Barot, Arjun S. Borkhatariya*
  - `2026-11-24`
  - Circuit breaker, retry, and bulkhead settings in Java microservices are tuned once and frozen, although the best setting depends on the fault a dependency is currently showing. We study whether an online learner can pick these settings at runtime. AdaptR4j swaps Resilience4j poli…

- **[RVLM-X: Towards a Universal VLM Harness](https://arxiv.org/abs/2611.31755v1)**
  - *Aadi Palnitkar, Dmytro Kurdydyk, Xiaomin Lin*
  - `2026-11-24`
  - Harnesses for vision-language models (VLMs) have grown with the models' capabilities, notably for images far larger than those seen in training, where downscaling loses small details. Most of them wrap the VLM in a fixed procedure, such as a zoom tree, that decides in advance whe…

- **[LatentLens: Rethinking Latent Interface in Multi-Agent Systems](https://arxiv.org/abs/2611.31582v1)**
  - *Ziqing Yang, Kewei Cheng, Mingjie Li et al.*
  - `2026-11-23`
  - Latent interfaces let agents in a multi-agent system communicate through continuous representations rather than decoded text. Prior work reports performance and efficiency gains, but neither separates latent communication from the agent harness nor examines its internal component…

- **[Off-the-Shelf Autonomous Agents for Game Playtesting](https://arxiv.org/abs/2611.31570v1)**
  - *Ayush Maniar, Eryk Banatt*
  - `2026-11-23`
  - In playtesting games, a human operator is typically required to test most gameplay elements. In this work we present Buddy, an autonomous game solving agent which can solve long time horizon objectives in an unseen 3D role-playing game using off-the-shelf language model systems.…

- **[Evaluating Frontier-Model Agent Skills with Open-Weight Models in a Science Gateway](https://arxiv.org/abs/2611.31480v1)**
  - *Komal Thareja, Mats Rynge, Anirban Mandal et al.*
  - `2026-11-23`
  - Scientific analyses that span many jobs and computing sites depend on workflow management systems to run reliably, but writing a production workflow requires expertise in such a system, which many domain scientists do not have. Coding agents can supply this expertise when they ar…

- **[Learning What vs. Learning How: Decomposing Task and Interface Competence in Agentic Training](https://arxiv.org/abs/2611.31427v1)**
  - *Chaeeun Lee, Hossein A. Rahmani, Aryo Pradipta Gema et al.*
  - `2026-11-23`
  - LLM agents operate through harnesses that define system prompts, action formats, feedback loops, and resource constraints. A model may possess the knowledge needed to solve a task yet fail to express that knowledge through a particular harness. This raises a basic question: when…

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

- **[GameDojo: Benchmarking Real-Time Interactive Agents in Video Games](https://arxiv.org/abs/2611.30771v1)**
  - *Kuan Zhang, Zhihao Yang, Yukun Chen et al.*
  - `2026-11-23`
  - Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss en…

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

- **[mini-psych-agent: Evaluating Human-Like Behavior in LLM Agents through Interactive Psychological Environments](https://arxiv.org/abs/2611.30365v2)**
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

- **[SecondChance: Benchmarking Reliable Error Recovery in AI Agents](https://arxiv.org/abs/2611.31586v1)**
  - *Atahan Dokme, Adar Avsian, Larry Heck*
  - `2026-11-23`
  - AI agents make errors while they act, and their reliability depends on what they do afterwards. Existing recovery benchmarks mostly inject faults, involve no user and score whether the task is eventually completed, so they cannot show whether an agent undid its own silent error,…

- **[RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments](https://arxiv.org/abs/2611.31002v1)**
  - *Jinkun Liu, Yingze Wang, Situ Wang et al.*
  - `2026-11-23`
  - Agentic Robotics, in which foundation models act as coding agents to control robots through executable programs, has emerged as a compelling paradigm for embodied intelligence. Yet unlike software engineering, where massive executable environments power post-training, robotics re…

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

- **[Right Destination, Wrong Journey: Synthetic Counseling Dialogues Miss Human Interactional Dynamics](https://arxiv.org/abs/2611.31686v1)**
  - *Ziwei Gong, Yuchen Huang, Nicholas Deas et al.*
  - `2026-11-23`
  - LLM-generated counseling dialogues are increasingly used for training and evaluating mental-health systems, yet existing evaluations focus largely on response quality and final outcomes rather than how support unfolds over time. We conduct a trajectory-centered evaluation of proc…

- **[Beyond Static Charts: Benchmarking Interactive Chart-to-Code Generation for MLLMs](https://arxiv.org/abs/2611.31345v1)**
  - *Yuhan Bian, Haoyu Liu, Siyu Li et al.*
  - `2026-11-23`
  - In recent years, multimodal large language models (MLLMs) have achieved significant progress in chart-to-code generation. However, existing benchmarks mainly focus on static charts, overlooking interactive charts that enable richer and more expressive data exploration. Unlike sta…

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

- **[PazaBench: Large-Scale ASR Benchmark for Low-Resource Languages in Africa](https://arxiv.org/abs/2611.31578v1)**
  - *Mercy Muchai, Nick Mumero Mwangi, Kevin Chege et al.*
  - `2026-11-23`
  - Low-resource languages remain underrepresented in ASR benchmarks, limiting the ability to reliably assess and compare model performance. We present a large-scale benchmark for automatic speech recognition (ASR) on low-resource languages in Africa. The benchmark harmonizes six pub…

- **[PRETZEL: A Benchmark for Cyclic Peptide Structure Prediction](https://arxiv.org/abs/2611.31708v1)**
  - *Yongchan Hong, Zihang Fang, Mukta Ubale et al.*
  - `2026-11-23`
  - Macrocyclic peptides are a growing therapeutic modality, and co-folding models are increasingly used to predict their structures. Yet published evaluations rely on small, loosely curated target sets that differ from paper to paper, so results are not comparable, and most report p…

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

- **[Social Interaction Breaks Replicate Independence in Controlled-Clone LLM Agents](https://arxiv.org/abs/2611.29581v2)**
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


## Finance  (182)

### AAAI

- **[CVE-LLM : Ontology-Assisted Automatic Vulnerability Evaluation Using Large Language Models](https://arxiv.org/abs/2502.15932)**
  - *Rikhiya Ghosh, Hans-Martin von Stockhausen, Martin Schmitt et al.*
  - **AAAI 2025** · `2025-02-21`
  - The National Vulnerability Database (NVD) publishes over a thousand new vulnerabilities monthly, with a projected 25 percent increase in 2024, highlighting the crucial need for rapid vulnerability identification to mitigate cybersecurity attacks and save costs and resources. In t…

- **[CoDe: Communication Delay-Tolerant Multi-Agent Collaboration via Dual Alignment of Intent and Timeliness](https://arxiv.org/abs/2501.05207)**
  - *Shou-Cheng Song, You-Fang Lin, Sheng Han et al.*
  - **AAAI 2025** · `2025-01-09`
  - Communication has been widely employed to enhance multi-agent collaboration. Previous research has typically assumed delay-free communication, a strong assumption that is challenging to meet in practice. However, real-world agents suffer from channel delays, receiving messages se…


### NeurIPS

- **[Multi-Identity Transaction Graph Pretraining for Fraud Detection](https://openreview.net/forum?id=1edqcNjZ3J)**
  - **NeurIPS 2026** · OpenReview · `2026-09-07`
  - Real-world payment risk modeling is constrained by scarce fraud labels and fragmented behavioral context across multiple payment identities. A physical transaction may appear simultaneously in multiple behavioral histories defined by different identities, while each identity indu…

- **[R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://arxiv.org/abs/2505.15155)**
  - *Yuan-Te Li, Xu Yang, Xiao Yang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - Financial markets pose fundamental challenges for asset return prediction due to their high dimensionality, non-stationarity, and persistent volatility. Despite advances in large language models and multi-agent systems, current quantitative research pipelines suffer from limited…


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

- **[Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)**
  - *Dawei Li, Ren-Liang Sun, Yue Huang et al.*
  - **ICLR 2025** · `2025-02-03`
  - Large Language Models (LLMs) as judges and LLM-based data synthesis have emerged as two fundamental LLM-driven data annotation methods in model development. While their combination significantly enhances the efficiency of model training and evaluation, little attention has been g…


### KDD

- **[Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation](https://arxiv.org/abs/2602.11224)**
  - *Hubert M. Pysklo, Artem Zhuravel, Patrick Watson*
  - **KDD 2026** · `2026-02-11`
  - We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world productivity software API tasks via code execution. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and ag…


### ACL

- **[AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading](https://arxiv.org/abs/2510.14264)**
  - *Zheye Deng, Wei-Xiang Yan, Chang-Long Yu et al.*
  - **ACL 2025** · `2025-10-16`
  - While Large Language Model (LLM) agents show promise in automated trading, they still face critical limitations. Prominent multi-agent frameworks often suffer from inefficiency, produce inconsistent signals, and lack the end-to-end optimization required to learn a coherent strate…

- **[Reasoning RAG via System 1 or System 2: A Survey on Reasoning Agentic Retrieval-Augmented Generation for Industry Challenges](https://arxiv.org/abs/2506.10408)**
  - *Jin-Tao Liang, Gang Su, Hui-Feng Lin et al.*
  - **ACL 2025** · `2025-06-12`
  - Retrieval-Augmented Generation (RAG) has emerged as a powerful framework to overcome the knowledge limitations of Large Language Models (LLMs) by integrating external retrieval with language generation. While early RAG systems based on static pipelines have shown effectiveness in…

- **[HalluLens: LLM Hallucination Benchmark](https://arxiv.org/abs/2504.17550)**
  - *Yejin Bang, Ziwei Ji, Alan Schelten et al.*
  - **ACL 2025** · `2025-04-24`
  - Large language models (LLMs) often generate responses that deviate from user input or training data, a phenomenon known as"hallucination."These hallucinations undermine user trust and hinder the adoption of generative AI systems. Addressing hallucinations is essential for the adv…

- **[Right Answer, Wrong Score: Uncovering the Inconsistencies of LLM Evaluation in Multiple-Choice Question Answering](https://arxiv.org/abs/2503.14996)**
  - *F. Molfese, Luca Moroni, Luca Gioffré et al.*
  - **ACL 2025** · `2025-03-19`
  - One of the most widely used tasks for evaluating Large Language Models (LLMs) is Multiple-Choice Question Answering (MCQA). While open-ended question answering tasks are more challenging to evaluate, MCQA tasks are, in principle, easier to assess, as the model's answer is thought…

- **[METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling](https://arxiv.org/abs/2502.17651)**
  - *Bing-Xuan Li, Yi-Wei Wang, Jiu-Xiang Gu et al.*
  - **ACL 2025** · `2025-02-24`
  - Chart generation aims to generate code to produce charts satisfying the desired visual properties, e.g., texts, layout, color, and type. It has great potential to empower the automatic professional report generation in financial analysis, research presentation, education, and hea…

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
  - *Fangyi Yu, Nabeel Seedat, Drahomira Herrmannova et al.*
  - **EMNLP 2025** · `2025-09-19`
  - Evaluating long-form answers in high-stakes domains such as law or medicine remains a fundamental challenge. Standard metrics like BLEU and ROUGE fail to capture semantic correctness, and current LLM-based evaluators often reduce nuanced aspects of answer quality into a single un…

- **[ArtifactsBench: Bridging the Visual-Interactive Gap in LLM Code Generation Evaluation](https://arxiv.org/abs/2507.04952)**
  - *Chen-Chen Zhang, Yu-Hang Li, Jia-Heng Liu et al.*
  - **EMNLP 2025** · `2025-07-07`
  - The generative capabilities of Large Language Models (LLMs) are rapidly expanding from static code to dynamic, interactive visual artifacts. This progress is bottlenecked by a critical evaluation gap: established benchmarks focus on algorithmic correctness and are blind to the vi…

- **[ReliableEval: A Recipe for Stochastic LLM Evaluation via Method of Moments](https://arxiv.org/abs/2505.22169)**
  - *Gili Lior, Eliya Habba, Shahar Levy et al.*
  - **EMNLP 2025** · `2025-05-28`
  - LLMs are highly sensitive to prompt phrasing, yet standard benchmarks typically report performance using a single prompt, raising concerns about the reliability of such evaluations. In this work, we argue for a stochastic method of moments evaluation over the space of meaning-pre…

- **[Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews](https://arxiv.org/abs/2502.17086)**
  - *Hyungyu Shin, Jingyu Tang, Yoonjoo Lee et al.*
  - **EMNLP 2025** · `2025-02-24`
  - Peer review underpins scientific progress, but it is increasingly strained by reviewer shortages and growing workloads. Large Language Models (LLMs) can automatically draft reviews now, but determining whether LLM-generated reviews are trustworthy requires systematic evaluation.…


### Other / arXiv

- **[Qwen-Image-HD: Autoregressive Diffusion for High Definition Image Generation](https://arxiv.org/abs/2611.32736)**
  - *Zihao Liu, Zekai Zhang, Shengming Yin et al.*
  - 🤗 Featured · `2026-11-24`

- **[MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction](https://arxiv.org/abs/2611.32462)**
  - *Yifan Dai, Daili Hua, Bohan Zeng et al.*
  - 🤗 Featured · `2026-11-24`
  - Multi-reference image generation requires a model to preserve the appearance of selected subjects while arranging them according to an instruction. Despite recent progress in reference-based generation and compositional control, reliably organizing selected subjects into the inte…

- **[Coding4Games: Can Modern Coding Agents Play Modern Video Games?](https://arxiv.org/abs/2611.31974)**
  - *Shifang Zhao, Haoyu Wang, Yuyang Yin et al.*
  - 🤗 Featured · `2026-11-24`
  - Games, especially modern AAA games, challenge language models to perceive complex scenes, control actions, and make decisions over long horizons. Existing game benchmarks primarily test language models as computer-use agents that query a language model throughout play, incurring…

- **[Small Learned Projections for Semantic-Reversal-Aware Retrieval with Spectral Acceleration: A Four-Domain Empirical Study](https://arxiv.org/abs/2611.31442)**
  - *Sayed Amir Karim*
  - 🤗 Featured · `2026-11-23`
  - Dense-embedding retrievers can fail adversarially: when a query is answered by a document A and reversed by a near-copy B that differs from A by a small meaning-changing edit (a "trap"), raw cosine over E5-Large-v2 places B in the top-10 for 82-100% of queries at a pool of 5,000.…

- **[Hybrid AI for AI-Native RAN Control: A Functional Perspective](https://arxiv.org/abs/2611.33035v1)**
  - *Sabrine Aroua, Osama Arouk, Pegah Alizadeh*
  - `2026-11-24`
  - AI-native radio access network (RAN) control involves interdependent decisions across network entities, protocol layers, and timescales. Understanding how AI and conventional methods can jointly support these decisions requires a common basis for comparing their functional roles.…

- **[Economic World Model](https://arxiv.org/abs/2611.32663v1)**
  - *Qirui Mi, Yujia Ming, Bo Li et al.*
  - `2026-11-24`
  - Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions? To answer this question, we define an economic world model (EWM) as an agent's internal representation of how an econo…

- **[Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation](https://arxiv.org/abs/2611.32238v1)**
  - *Kaipeng Fang, Yuhao Wang, Ji Zhang et al.*
  - `2026-11-24`
  - Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, whi…

- **[Marketing-Bench: Evaluating Frontier Models and Agents on Real-World Marketing Capabilities](https://arxiv.org/abs/2611.32012v1)**
  - *Sumanth Balaji, Siddharth Gupta, Ameet Deshpande et al.*
  - `2026-11-24`
  - As frontier AI models and agents are deployed more broadly in the real world, marketing is emerging as one of their largest applications. Marketing teams use AI models to produce brand assets like website copy and social media posts, while consumers' agents autonomously discover…

- **[Spec-Test Coverage Gap: Detecting Overspecified Tests in SWE-Bench-Style Benchmarks](https://arxiv.org/abs/2611.31839v1)**
  - *Avi Aggarwal, Yiran Hu*
  - `2026-11-24`
  - SWE-bench-style benchmarks, such as SWE-bench Verified (Verified) and SWE-bench Pro (Pro), evaluate coding agents with tests taken from the change that originally fixed each issue. However, these tests can enforce details the task never states, causing correct alternative fixes t…

- **[Agentic Discovery of Soundness Bugs in Safe Rust Bindings](https://arxiv.org/abs/2611.31813v1)**
  - *Marius Momeu, Koushik Sen*
  - `2026-11-24`
  - Rust crates confine unsafe code, such as calls into C or C++ libraries or system calls, behind safe interfaces that must uphold Rust's invariants. If an interface encodes one rule of the code beneath it too weakly, a program written in purely safe Rust can cause undefined behavio…

- **[How Far Apart Are Two Proofs? Measuring Proof Dissimilarity in a Proof Kernel and in Lean/Mathlib](https://arxiv.org/abs/2611.31811v1)**
  - *Nikolaos Nikolaou*
  - `2026-11-24`
  - We now live in the age of machine-generated mathematics: AI systems produce research-level proofs faster than the human mathematical community can read them. Verification is only part of the challenge. We also need to know whether a "new proof" is indeed new, whether a thousand g…

- **[Learning Compact State Abstractions for LLM Agents](https://arxiv.org/abs/2611.31800v1)**
  - *Yaswanth Chittepu, Raghavendra Addanki, Anup Rao et al.*
  - `2026-11-24`
  - LLM agents commonly use the full interaction history as a proxy for state, retaining all past observations and actions regardless of whether they remain relevant. We instead ask what information an agent actually needs to carry forward. We define agent state as a compact abstract…

- **[TACT-Bench: Testing Adaptive Conversational Threats against Tool-Use Agents](https://arxiv.org/abs/2611.31756v1)**
  - *Ilia Hashemi Rad, Feijie Wu, Haoyu Wang et al.*
  - `2026-11-24`
  - The growing autonomy of AI agents in using external tools and making decisions has created an urgent need for comprehensive safety benchmarks. Existing benchmarks test compromised tool channels or adaptive multi-turn attacks, though they may not capture the unique capabilities of…

- **[SwarmLeak: Does Coordination Improve Privacy Attacks on LLM Agents?](https://arxiv.org/abs/2611.31791v1)**
  - *Asma Farajidizaji, Vyas Raina, Vatsal Raina et al.*
  - `2026-11-24`
  - LLM agents increasingly collaborate in group chats while holding tool access to confidential records, which makes the shared chat an attack surface. It remains unclear whether several colluding attackers extract such information more effectively than one. We introduce SwarmLeak,…

- **[Recursive Collective Intelligence: Emergence on an Equal-Budget Ladder in Multi-Agent LLM Systems](https://arxiv.org/abs/2611.32606v1)**
  - *Lixuan He, Shengqu Cai, Fang Wu et al.*
  - `2026-11-24`
  - Large language models increasingly work as teams of agents, and a team is expected to solve problems beyond the reach of any single member. Most evaluations credit a team for outperforming a single agent, without accounting for the additional computation: a team may consume many…

- **[The algorithmic behavioral sink: Modeling the transition to irreversible demographic collapse](https://arxiv.org/abs/2611.32084v1)**
  - *Feng Yu*
  - `2026-11-24`
  - In 2025, the vast majority of major global economies reported a Total Fertility Rate below the replacement level of 2.1. This synchronized collapse has persisted despite extensive pro-natalist financial interventions, revealing a structural limitation in conventional linear demog…

- **[TQ-HQNet: A Trainability-Aware and Qubit-Efficient Hybrid Quantum Neural Network for Cross-Domain Learning on Heterogeneous Data](https://arxiv.org/abs/2611.31908v1)**
  - *Abdur Rasool, Saba Aslam, Hui Chen et al.*
  - `2026-11-24`
  - Hybrid quantum neural networks are a promising direction for noisy intermediate-scale quantum computing, but their practical effectiveness is often limited by poor trainability, rigid circuit design, and weak robustness across heterogeneous real-world tasks. This paper proposes T…

- **[Boiling Down Uncertainty: Deep Generative Scenario Search with Decision-Guided Evolution Strategies for Two-Stage Stochastic Optimization](https://arxiv.org/abs/2611.32573v1)**
  - *Atefeh Hemmati Golsefidi, David Pisinger*
  - `2026-11-24`
  - One of the most common models for handling uncertainty is two-stage stochastic programming. Choosing the right number of scenarios is a trade-off between the uncertainty that can be represented and computational cost. A recent method, Deep Generative Scenario Search, generates sy…

- **[Beyond Rigid Hands: Deforming Skin into Contact-Consistent Hand Meshes](https://arxiv.org/abs/2611.31950v1)**
  - *Seonghwan Park, Min-Gyu Park*
  - `2026-11-24`
  - Hands grasp objects with soft skin. A fingertip flattens against a mug, and a palm curves around a bottle. Yet hand-object datasets and estimators represent the hand as a rigid articulated mesh, which hovers above or penetrates the object where skin would press against it. Existi…

- **[Delta-Vega Hedging with Deep Reinforcement Learning: From Simulation to Reality](https://arxiv.org/abs/2611.32790v1)**
  - *Michele Colombi, Marco Di Francesco, Pietro Rossi*
  - `2026-11-24`
  - Hedging an option portfolio with the underlying asset alone leaves the position exposed to changes in volatility, which can be managed by trading another derivative, at higher transaction costs. We propose a deep reinforcement learning approach to hedge both price and volatility…

- **[Large-Scale Streaming Portfolio Optimization with Pauli Correlation Encoding](https://arxiv.org/abs/2611.32769v1)**
  - *Vicente P. Soloviev, Josh Kirsopp*
  - `2026-11-24`
  - Classical portfolio construction over large asset universes is a combinatorial selection problem that existing heuristics do not solve well at scale. Pauli Correlation Encoding (PCE) addresses this by representing the underlying clustering problem with far fewer qubits than one p…

- **[Semivariance and Semivolatility in Portfolio Selection: A Unified Framework for Downside-Risk Portfolio Models](https://arxiv.org/abs/2611.32638v1)**
  - *Francesco Cesarone, Massimiliano Corradini, Nicolò Giunta*
  - `2026-11-24`
  - In this paper, we study downside risk in portfolio selection beyond minimum-risk models, where semivariance and its square root, semivolatility, yield the same portfolio. Downside-risk models are often presented as direct extensions of their variance-based counterparts, although…

- **[Agent Evaluation Without Ground Truth: A Null Proportion Perspective](https://arxiv.org/abs/2611.31539v1)**
  - *Brian M. Cho, Michael Lindon, Nathan Kallus*
  - `2026-11-23`
  - The correctness of actions taken by agents is typically evaluated against known, externally verified ground truth labels, such as whether a proof is correct or whether code compiles and passes unit tests. However, as coding and science agents are entrusted with more end-to-end au…

- **[Learning What vs. Learning How: Decomposing Task and Interface Competence in Agentic Training](https://arxiv.org/abs/2611.31427v1)**
  - *Chaeeun Lee, Hossein A. Rahmani, Aryo Pradipta Gema et al.*
  - `2026-11-23`
  - LLM agents operate through harnesses that define system prompts, action formats, feedback loops, and resource constraints. A model may possess the knowledge needed to solve a task yet fail to express that knowledge through a particular harness. This raises a basic question: when…

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

- **[Scoring Recovery-Time Agent Security: Proposals, Effects, and Retry Instructions](https://arxiv.org/abs/2611.31318v1)**
  - *Paul Deepakraj Retinraj*
  - `2026-11-23`
  - A timed-out tool write may be absent, committed, or still in flight. Evaluating an agent only on whether its goal exists can hide harmful recovery actions: auditing 12 supplied traces changes apparent completion from 10/12 to 8/12. We introduce an executable evaluation that separ…

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

- **[Beyond Static Charts: Benchmarking Interactive Chart-to-Code Generation for MLLMs](https://arxiv.org/abs/2611.31345v1)**
  - *Yuhan Bian, Haoyu Liu, Siyu Li et al.*
  - `2026-11-23`
  - In recent years, multimodal large language models (MLLMs) have achieved significant progress in chart-to-code generation. However, existing benchmarks mainly focus on static charts, overlooking interactive charts that enable richer and more expressive data exploration. Unlike sta…

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

- **[Transformers with Signatures: Towards Universal In-Context Learning in Path Space](https://arxiv.org/abs/2611.31439v1)**
  - *Ziheng Cheng, Xin Guo, Ben Hambly*
  - `2026-11-23`
  - In-context learning (ICL) enables transformers to adapt to new tasks from demonstrations without updating their parameters. However, theoretical guarantees for transformers remain limited in general, and elusive in particular when target responses depend nonlinearly on the evolut…

- **[A Kernel Framework for Linear Operator Equations](https://arxiv.org/abs/2611.31626v1)**
  - *Damir Filipovic, Valentin Tissot-Daguette*
  - `2026-11-23`
  - Solving linear operator equations with nonlocal terms or heterogeneous constraints often requires specific numerical schemes. We develop a unified approach based on embedding such equations into a reproducing kernel Hilbert space (RKHS). Differential, boundary, and integral opera…

- **[CCFinance: Reconstructing Financial News Samples from Web Archives](https://arxiv.org/abs/2611.30737v1)**
  - *Marcus Gawronsky*
  - `2026-11-23`
  - Proprietary news archives assign stories to firms, so reproducing a financial study often requires access to both the articles and the vendor's assignments. CCFinance lets researchers reconstruct firm coverage under different selection rules by recording which version of a story…

- **[World Models as Native Latent Action Models](https://arxiv.org/abs/2611.30898v1)**
  - *Qinyue Li, Weijie Qiao, Qingyi Tao et al.*
  - `2026-11-23`
  - Large and diverse video sources, such as egocentric human video and heterogeneous robot recordings, carry rich dynamics but come either without actions or without a shared action space. Latent action models (LAMs) can recover these dynamics, but they train their inverse- and forw…

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

- **[Stranded Compute in AI Inference Workloads: Recovering Value Through Demand Aggregation](https://arxiv.org/abs/2611.31654v1)**
  - *Sam Kingsley*
  - `2026-11-23`
  - AI inference infrastructure is commonly analyzed as an energy business. Under full total cost accounting it is not: in the reference deployment modeled here, capital recovery is 87.3% of fully loaded cost per token and electricity 3.7%. Because capital accrues per unit time irres…

- **[Cleaning correlation matrices with external information: the Maximum Variance estimat](https://arxiv.org/abs/2611.30843v2)**
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


---
*Generated 2026-11-25 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
