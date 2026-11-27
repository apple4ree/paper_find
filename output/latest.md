# Daily Paper Digest — 2026-11-27 (Friday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**456 unique papers** (569 topic-entries — cross-topic papers counted once per category)

---

## Agent  (317)

### AAAI

- **[D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies](https://arxiv.org/abs/2511.16590)**
  - *Sen Chen, Tong Zhao, Yi Bin et al.*
  - **AAAI 2025** · `2025-11-20`
  - Developing intelligent agents capable of operating a wide range of Graphical User Interfaces (GUIs) with human-level proficiency is a key milestone on the path toward Artificial General Intelligence. While most existing datasets and benchmarks for training and evaluating GUI agen…

- **[Beyond ReAct: A Planner-Centric Framework for Complex Tool-Augmented LLM Reasoning](https://arxiv.org/abs/2511.10037)**
  - *Xiao-Long Wei, Yuehu Dong, Xing-Liang Wang et al.*
  - **AAAI 2025** · `2025-11-13`
  - Existing tool-augmented large language models (LLMs) encounter significant challenges when processing complex queries. Current frameworks such as ReAct are prone to local optimization traps due to their reliance on incremental decision-making processes. To address these limitatio…


### NeurIPS

- **[IRTIQA: Evolving in English, Evaluated in Urdu -- Does Agent Self-Evolution Transfer from English to Urdu and Code-Switched Input?](https://arxiv.org/abs/2611.34303v1)**
  - *Abdullah Hashmat, Danish Javed, Usman Naseem et al.*
  - **NeurIPS** · `2026-11-25`
  - As LLM agents increasingly learn from their own experience, the tasks they learn from and are evaluated on are almost always in English. We ask whether self-evolution transfers from English to Urdu, and release IRTIQA, a benchmark of aligned English, Urdu-translated, and Urdu cod…

- **[SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks](https://arxiv.org/abs/2506.11791)**
  - *Hwiwon Lee, Zi-Qi Zhang, Hanxiao Lu et al.*
  - **NeurIPS 2025** · `2025-06-13`
  - Rigorous security-focused evaluation of large language model (LLM) agents is imperative for establishing trust in their safe deployment throughout the software development lifecycle. However, existing benchmarks largely rely on synthetic challenges or simplified vulnerability dat…

- **[REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://arxiv.org/abs/2504.11543)**
  - *Divyansh Garg, Shaun VanWeelden, Diego Caples et al.*
  - **NeurIPS 2025** · `2025-04-15`
  - We introduce REAL, a benchmark and framework for multi-turn agent evaluations on deterministic simulations of real-world websites. REAL comprises high-fidelity, deterministic replicas of 11 widely-used websites across domains such as e-commerce, travel, communication, and profess…


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

- **[Tool Unlearning for Tool-Augmented LLMs](https://arxiv.org/abs/2502.01083)**
  - *Jiali Cheng, Hadi Amiri*
  - **ICML 2025** · `2025-02-03`
  - Tool-augmented large language models (LLMs) are often trained on datasets of query-response pairs, which embed the ability to use tools or APIs directly into the parametric knowledge of LLMs. Tool-augmented LLMs need the ability to forget learned tools due to security vulnerabili…


### ICLR

- **[HeurekaBench: A Benchmarking Framework for AI Co-scientist](https://arxiv.org/abs/2601.01678)**
  - *Siba Smarak Panigrahi, Jovana Videnović, Maria Brbić*
  - **ICLR 2026** · `2026-01-04`
  - LLM-based reasoning models have enabled the development of agentic systems that act as co-scientists, assisting in multi-step scientific analysis. However, evaluating these systems is challenging, as it requires realistic, end-to-end research scenarios that integrate data analysi…

- **[TUMIX: Multi-Agent Test-Time Scaling with Tool-Use Mixture](https://arxiv.org/abs/2510.01279)**
  - *Yong-Chao Chen, Jie-Feng Chen, Rui Meng et al.*
  - **ICLR 2025** · `2025-09-30`
  - While integrating tools like Code Interpreter and Search has significantly enhanced Large Language Model (LLM) reasoning in models like ChatGPT Agent and Gemini-Pro, practical guidance on optimal tool use is lacking. The core challenge is effectively combining textual reasoning,…

- **[MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents](https://arxiv.org/abs/2508.21475)**
  - *Xi-Jia Tao, Yi-Hua Teng, Xinxing Su et al.*
  - **ICLR 2025** · `2025-08-29`
  - Existing multimodal browsing benchmarks often fail to require genuine multimodal reasoning, as many tasks can be solved with text-only heuristics without vision-in-the-loop verification. We introduce MMSearch-Plus, a 311-task benchmark that enforces multimodal understanding by re…

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

- **[Adaptive Financial Sentiment Analysis for NIFTY 50 via Instruction-Tuned LLMs ,RAG and Reinforcement Learning Approaches](https://arxiv.org/abs/2512.20082)**
  - *Chaithra Sadashiva Kotekar, B. Mohan, Kamesh Kadimisetty*
  - **KDD 2025** · `2025-12-17`
  - Financial sentiment analysis plays a crucial role in informing investment decisions, assessing market risk, and predicting stock price trends. Existing works in financial sentiment analysis have not adequately considered the impact of stock prices or market feedback on sentiment…

- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)**
  - *Mahmoud Mohammadi, Yi-Peng Li, Jane Lo et al.*
  - **KDD 2025** · `2025-07-29`
  - The rise of LLM-based agents has opened new frontiers in AI applications, yet evaluating these agents remains a complex and underdeveloped area. This survey provides an in-depth overview of the emerging field of LLM agent evaluation, introducing a two-dimensional taxonomy that or…


### ACL

- **[Shape-Aware Three-Way Merge for RDF Knowledge Graphs: The schema defines the conflict: an implementation and evaluation](https://arxiv.org/abs/2611.34870v1)**
  - *Steve Brown*
  - **ACL** · `2026-11-25`
  - Merging RDF serializations creates ordering conflicts and misses semantic ones. We describe and evaluate a three-way merge in which the schema defines a conflict: set algebra combines canonical triples, and a slot is contended only where a SHACL shape bounds its cardinality and b…

- **[Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies](https://arxiv.org/abs/2611.33010v1)**
  - *Xuanchen Liu, Hejun Zhang, Boxuan Dong et al.*
  - **ACL** · `2026-11-24`
  - Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introdu…

- **[Discovering Bandwidth-Efficient Prefetchers to Shrink the Cache Hierarchy](https://arxiv.org/abs/2611.31983v1)**
  - *Patrick Tser Jern Kon, Akanksha Jain, Abraham Gonzalez et al.*
  - **ACL** · `2026-11-24`
  - Shared last-level caches (LLCs) increasingly dominate server processor die area, forcing architects to trade core counts for cache capacity. While intelligent data prefetching offers a pathway to reclaim this silicon, designing coordinated, multi-level prefetching policies for mu…

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

- **[Reasoning RAG via System 1 or System 2: A Survey on Reasoning Agentic Retrieval-Augmented Generation for Industry Challenges](https://arxiv.org/abs/2506.10408)**
  - *Jin-Tao Liang, Gang Su, Hui-Feng Lin et al.*
  - **ACL 2025** · `2025-06-12`
  - Retrieval-Augmented Generation (RAG) has emerged as a powerful framework to overcome the knowledge limitations of Large Language Models (LLMs) by integrating external retrieval with language generation. While early RAG systems based on static pipelines have shown effectiveness in…

- **[WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)**
  - *Jialong Wu, Wen-Biao Yin, Yong Jiang et al.*
  - **ACL 2025** · `2025-01-13`
  - Retrieval-augmented generation (RAG) demonstrates remarkable performance across tasks in open-domain question-answering. However, traditional search engines may retrieve shallow content, limiting the ability of LLMs to handle complex, multi-layered information. To address it, we…


### EMNLP

- **[Tool Zero: Training Tool-Augmented LLMs via Pure RL from Scratch](https://arxiv.org/abs/2511.01934)**
  - *Yi-Rong Zeng, Xiao Ding, Yu-Tai Hou et al.*
  - **EMNLP 2025** · `2025-11-02`
  - Training tool-augmented LLMs has emerged as a promising approach to enhancing language models'capabilities for complex tasks. The current supervised fine-tuning paradigm relies on constructing extensive domain-specific datasets to train models. However, this approach often strugg…

- **[ToolHaystack: Stress-Testing Tool-Augmented Language Models in Realistic Long-Term Interactions](https://arxiv.org/abs/2505.23662)**
  - *Beong-woo Kwak, Minju Kim, Dongha Lim et al.*
  - **EMNLP 2025** · `2025-05-29`
  - Large language models (LLMs) have demonstrated strong capabilities in using external tools to address user inquiries. However, most existing evaluations assume tool use in short contexts, offering limited insight into model behavior during realistic long-term interactions. To fil…

- **[AgentThink: A Unified Framework for Tool-Augmented Chain-of-Thought Reasoning in Vision-Language Models for Autonomous Driving](https://arxiv.org/abs/2505.15298)**
  - *Kan-Gan Qian, Sicong Jiang, Yang Zhong et al.*
  - **EMNLP 2025** · `2025-05-21`
  - Vision-Language Models (VLMs) show promise for autonomous driving, yet their struggle with hallucinations, inefficient reasoning, and limited real-world validation hinders accurate perception and robust step-by-step reasoning. To overcome this, we introduce \textbf{AgentThink}, a…

- **[Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents](https://arxiv.org/abs/2502.20073)**
  - *Haochen Sun, Shu-Wen Zhang, Lu-Jie Niu et al.*
  - **EMNLP 2025** · `2025-02-27`
  - Large Language Models (LLMs) based agent systems have made great strides in real-world applications beyond traditional NLP tasks. This paper proposes a new LLM-based Multi-Agent System (LLM-MAS) benchmark, Collab-Overcooked, built on the popular Overcooked-AI game with more appli…


### NAACL

- **[Self-Training Large Language Models for Tool-Use Without Demonstrations](https://arxiv.org/abs/2502.05867)**
  - *Ne Luo, Aryo Pradipta Gema, Xuan-Li He et al.*
  - **NAACL 2025** · `2025-02-09`
  - Large language models (LLMs) remain prone to factual inaccuracies and computational errors, including hallucinations and mistakes in mathematical reasoning. Recent work augmented LLMs with tools to mitigate these shortcomings, but often requires curated gold tool-use demonstratio…


### Other / arXiv

- **[OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms](https://arxiv.org/abs/2611.34232)**
  - *Hui Shen, Yunta Hsieh, Jianing Ma et al.*
  - 🤗 Featured · `2026-11-25`

- **[Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video Models](https://arxiv.org/abs/2611.34813)**
  - *Dezhi Luo, Fengyuan Yu, Haotian Zhang et al.*
  - 🤗 Featured · `2026-11-25`
  - Video generation models are increasingly evaluated as visual reasoners: given a first frame and a natural-language prompt, can the model produce the video in which the specified task is carried out? The paradigm is considered advantageous because the reasoning is native to the vi…

- **[StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation](https://arxiv.org/abs/2611.34290)**
  - *Modi Jin, Xuying Zhang, Yijing Guo et al.*
  - 🤗 Featured · `2026-11-25`
  - Modern video foundation models generate high-quality short clips, but preserving long-video consistency and correctly depicting event-driven state changes remain challenging. Existing agentic workflows face these challenges because continual planning and repair accumulate context…

- **[DRBench Pro: A Knowledge-Centric Benchmark for Professional Deep Research Agents](https://arxiv.org/abs/2611.34852)**
  - *Han Huang, Yuchen Yan, Xingyu Wu et al.*
  - 🤗 Featured · `2026-11-25`
  - Deep research agents gather information from multiple sources and synthesize it into reports on complex, open-ended questions. Existing benchmarks assess report quality along several dimensions, but lack a dedicated knowledge-centric evaluation of which research directions a repo…

- **[Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation](https://arxiv.org/abs/2611.32238)**
  - *Kaipeng Fang, Yuhao Wang, Ji Zhang et al.*
  - 🤗 Featured · `2026-11-24`
  - Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, whi…

- **[When an AI agent makes a mistake in a database, what decides the damage?](https://arxiv.org/abs/2611.30483)**
  - *Abdullah Kaya, Cevheri Bozoglan, Yusuf Gundogdu*
  - 🤗 Featured · `2026-11-23`

- **[Markdown Is Not a Firewall: four coding agents, one rules file, four boundaries](https://arxiv.org/abs/2611.27112)**
  - *Sandeep Dhuri*
  - 🤗 Featured · `2026-11-20`

- **[Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation](https://arxiv.org/abs/2611.34907)**
  - *Shaoteng Liu, Shuai Yang, Wei Huang et al.*
  - 🤗 · `2026-11-25`

- **[When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL](https://arxiv.org/abs/2611.34777)**
  - *Haowen Hou, Yicheng Liu, Zhen Huang et al.*
  - 🤗 · `2026-11-25`
  - Group-based reinforcement learning with verifiable rewards often yields all-fail groups on long-horizon agent tasks: every sampled trajectory receives zero reward, leaving group-relative methods without a reward-based policy gradient. A common remedy supplies complete solutions f…

- **[DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target's Sparsity](https://arxiv.org/abs/2611.34776)**
  - *Hong Liu, Rui Cen, Junhan Shi et al.*
  - 🤗 · `2026-11-25`
  - To avoid the quadratic cost of dense attention over long contexts, models such as DeepSeek-V4 and Hy4 have turned natively sparse, and speculative decoding, which matters most where decoding is slowest, increasingly runs on them. Their drafters, however, still keep a context cach…

- **[Collect for Coverage, Replay with Evidence: Adaptive and Efficient On-Policy Distillation for Long-Horizon Agents](https://arxiv.org/abs/2611.34756)**
  - *Haowen Hou, Gen Li, Ruilin Li et al.*
  - 🤗 · `2026-11-25`
  - Fully online on-policy distillation (OPD) is costly for long-horizon agents because each update depends on fresh environment rollouts. Prefix replay offers an efficient alternative by sampling current-student responses from stored histories, reducing idle time for long-tail rollo…

- **[SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator](https://arxiv.org/abs/2611.34750)**
  - *Xiang Li, Hongyu Zhou, Ya-Li Li et al.*
  - 🤗 · `2026-11-25`

- **[RoboEvo^2: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution](https://arxiv.org/abs/2611.34675)**
  - *Chenzhi Liu, Jiehong Lin, Wei Huang et al.*
  - 🤗 · `2026-11-25`
  - Robots should adapt to unfamiliar environments and acquire new skills through interaction, then execute those skills efficiently with practice. Vision-language-action policies provide efficient control, but often need additional human demonstrations to handle unfamiliar settings;…

- **[DemoFoundry: Toward Scalable Photorealistic Robot Data with Coding Agents and Generative Rendering](https://arxiv.org/abs/2611.34671)**
  - *Ruixiang Wang, Xinyue Yao, Xuanning Zhou et al.*
  - 🤗 · `2026-11-25`
  - Scaling robot learning requires demonstrations that combine realistic visual observations with reliable action supervision. Simulation-based synthesis faces a substantial visual gap relative to real environments, while video-only generation struggles to maintain physically consis…

- **[REE: A Scientific Research Entrance Exam for AI Agents](https://arxiv.org/abs/2611.34646)**
  - *Zeqi Zhou, Minghao Liu, Jiarui Liu et al.*
  - 🤗 · `2026-11-25`
  - Autonomous research agents are emerging as a promising approach to scientific problem-solving across disciplines, owing to their growing ability to improve a solution through repeated experiments. Evaluating this ability requires benchmarks that pose open-ended research problems…

- **[EgoUseBench: Benchmarking Computer-Use Agents under Evolving First-Person Contexts](https://arxiv.org/abs/2611.34466)**
  - *Yurun Chen, Biao Yi, Qihang Yu et al.*
  - 🤗 · `2026-11-25`
  - AI wearables, such as smart glasses, extend the context available to agents beyond digital environments to users' physical surroundings. With these devices, computer tasks can originate from users' ongoing activities rather than solely from explicit instructions. Through first-pe…

- **[EvoLink-Bench: A Benchmark for Evaluating Self-Evolving Agents in Long-Horizon Interdependent Task Streams](https://arxiv.org/abs/2611.34400)**
  - *Wei Chen, Xiaodong Lu, Weihao Shen et al.*
  - 🤗 · `2026-11-25`
  - Large language model (LLM) agents are evolving from passive chatbots into autonomous systems that operate continuously in dynamic environments. Such agents need not only solve current tasks but also learn from past interactions to improve future performance. However, existing str…

- **[Single-Database Rewards Are Hackable: Counterfactual Execution for Trustworthy Text-to-SQL RL](https://arxiv.org/abs/2611.34363)**
  - *Shreshth Rai, Rishii Kumar Singh, Aksh Aggarwal*
  - 🤗 · `2026-11-25`
  - Reinforcement learning (RL) for text-to-SQL agents pays a query when its result matches the reference on one database. However, a wrong query can match by luck when the data lack the rows that expose its bug. We study a counterfactual-database (CF) reward that also runs the final…

- **[VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation](https://arxiv.org/abs/2611.34237)**
  - *Xuanyu Zheng, Luoyuan Zhang, Yancheng Long et al.*
  - 🤗 · `2026-11-25`

- **[Letting Models Manage Their Own Context: Where We Stand](https://arxiv.org/abs/2611.34147)**
  - *Alessio Devoto, Avinash Vem, Tara Safavi et al.*
  - 🤗 · `2026-11-25`
  - Agent harnesses today manage context on the model's behalf: when the window fills, the harness triggers a compaction that summarizes the history. We study the alternative, \emph{model-driven} context management, in which the model itself decides when and what to compact through a…

- **[Attack Policy Selection can Mislead Monitor Evaluators](https://arxiv.org/abs/2611.34934v1)**
  - *Charlie Griffin, Oliver Makins, Asa Cooper Stickland et al.*
  - `2026-11-25`
  - AI monitors, classifiers that flag dangerous behaviour by AI agents, are often evaluated against transcripts generated by attack policies acting as proxies for dangerous behaviour in deployment. We evaluate an ex-production OpenAI monitor as a case study and find that measured fa…

- **[$μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents](https://arxiv.org/abs/2611.34920v1)**
  - *Qihao Lin, Guanxu Chen, Shuhang Zheng et al.*
  - `2026-11-25`
  - Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when participants react throughout a session. We introduce $μ$-Bench, a benchmark for joint…

- **[How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches](https://arxiv.org/abs/2611.34875v1)**
  - *Aakash Goel, Benjamin Steenhoek, Yu Hu*
  - `2026-11-25`
  - Agent patches are larger than developers', which is widely read as over-editing. But patch size does not say whether the extra edits are needed, what they are, or where they come from. We introduce Delta Residue Attribution (DRA), which replays agent trajectories, traces every bl…

- **[TASK Memory: Beyond Text-Only Memory with Activation Steering and Knowledge Editing against Memory Hallucination](https://arxiv.org/abs/2611.34762v1)**
  - *Jinkun Zhao, Wenjun Wu*
  - `2026-11-25`
  - LLM agents increasingly rely on external memory, yet they still hallucinate about what they remember. Often the correct memory is retrieved and placed in the prompt, but the answer contradicts it or the memory is applied to the wrong question. We call these use-time memory halluc…

- **[Maco-RL: Scaling Agent Capabilities with Mixed-Task Reinforcement Learning](https://arxiv.org/abs/2611.34703v1)**
  - *Jiacheng Zhang, Qixing Zhou, Haiyang Wang et al.*
  - `2026-11-25`
  - Mixed-task reinforcement learning (MixRL) directly trains a unified policy across domains to continually expand agent capabilities without training separate specialists or requiring an extra distillation stage. Despite its appeal, scaling MixRL poses significant challenges in ach…

- **[Do We Still Need Reinforcement Learning When We Can Read the World Model?](https://arxiv.org/abs/2611.34656v1)**
  - *Mingchao Zhang, Miduo Cui, Kangze He et al.*
  - `2026-11-25`
  - Reinforcement learning has achieved remarkable success in sequential decision-making, but learning effective policies often requires substantial interaction experience. Model-based reinforcement learning alleviates this dependence by leveraging world models, which are typically u…

- **[ZeroHero: Training Small Language Agents from Scratch](https://arxiv.org/abs/2611.34635v1)**
  - *Nikita Sorokin, Zoya Volovikova, Alexey Skrynnik et al.*
  - `2026-11-25`
  - Large pretrained language models provide capable policies for interactive tasks, but how much model capacity is necessary for a specialized language agent? We introduce ZeroHero, a framework for training small language agents (SLAs) from scratch. In each environment, a large lang…

- **[LatentRL-QAS: Transfer via Latent Reinforcement Learning for Quantum Architecture Search](https://arxiv.org/abs/2611.34634v1)**
  - *Maria Ilektra Plakitsi, Sebastian Feld, Akash Kundu*
  - `2026-11-25`
  - Reinforcement learning (RL) emerges as a prominent approach to quantum architecture search (QAS), the automated design of quantum circuits. However, transferring what an agent has learned from one number of qubits to another is still weakly explored: the state, the action space a…

- **[VisualMontage: Manipulating the Beliefs of Vision-Language Agents with Authentic Image Sequences](https://arxiv.org/abs/2611.34603v1)**
  - *Jinwei Hu, Lai Wei, Zhuoyun Li et al.*
  - `2026-11-25`
  - As agents based on vision-language models (VLMs) increasingly interpret social-media content, errors in their analysis may lend credibility to rumors and amplify their spread. In this paper, we study the problem of visual cognitive collusion, in which coordinated posts combine au…

- **[vSFT: Learning to Verbally Tune Agents at Test Time](https://arxiv.org/abs/2611.34440v1)**
  - *Qishuai Wen, Rui Chen, Haiwen Li et al.*
  - `2026-11-25`
  - Large language model agents are increasingly improved via agentic reinforcement learning, which can be on-policy but suffers from expensive rollouts and sparse rewards, limiting its application at test time. In this paper, we present a verbally Supervised Fine-Tuning (vSFT) frame…

- **[SemProxy: Semantic 3D Proxies for Controllable Agentic 3D Modeling](https://arxiv.org/abs/2611.34414v1)**
  - *Shuyuan Zhang, Changjian Li*
  - `2026-11-25`
  - Coding agents are increasingly capable of generating 3D models, yet enabling users to effectively control the modeling process remains challenging. Existing workflows rely primarily on text prompts and reference images, which often struggle to convey precise spatial intentions an…

- **[Agentic Waterfall: An Intent-Driven Information Discovery Framework for Reclaiming User Control in the Attention Economy](https://arxiv.org/abs/2611.34407v1)**
  - *Yige Luo, Shining Zhang, Jikun Liu et al.*
  - `2026-11-25`
  - We formalize Agentic Waterfall Feed, a new problem of personalized information discovery in which users actively direct recommendations and the system adapts to evolving needs inferred from both explicit requests and browsing behavior. We address this problem with the Agentic Wat…

- **[When Skills Fail to Compose: Compatibility and Retention in Language Models](https://arxiv.org/abs/2611.34398v1)**
  - *Yan Lin, Zhongliang Guo, Jingyu Sun et al.*
  - `2026-11-25`
  - Skill acquisition alone does not establish a reusable skill library: task proficiency does not specify a compositional interface. Motivated by agents that acquire and refine skills, we study independently learned soft-prompt skills on frozen language models, with skill identities…

- **[MeterRouter: Budget-Aware Dynamic Routing for Multi-Agent Systems](https://arxiv.org/abs/2611.34327v1)**
  - *Yue Xu, Leikun Yin, Ruiming Min et al.*
  - `2026-11-25`
  - Multi-agent systems (MAS) built on large language models (LLMs) outperform single-agent systems, but inter-agent communication incurs substantial token overhead. While assigning a large LLM to every agent is common, it results in inefficient resource utilization, leaving the syst…

- **[WebVibe: Multimodal Interactive Website Generation via Reverse Synthesis and Visual Self-Distillation](https://arxiv.org/abs/2611.34292v1)**
  - *Tianxiang Jiang, Sheng Xia, Yilin Long et al.*
  - `2026-11-25`
  - Although multimodal large language models translate single screenshots into static HTML, generating interactive functional websites from design specifications still struggles with multi-page routing and stateful widget transitions. Examining existing training pipelines reveals tw…

- **[Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems](https://arxiv.org/abs/2611.34278v1)**
  - *Manit Baser, Vyoman Jain, Rachel Yeo Hui Min et al.*
  - `2026-11-25`
  - As large language models increasingly collaborate in heterogeneous multi-agent systems, latent communication has emerged as an efficient alternative to exchanging natural-language messages. By sharing internal representations, agents can avoid repeatedly processing the same conte…

- **[Crucible: Evaluating LLM Agents in Executable Chemistry Research Environments](https://arxiv.org/abs/2611.34254v1)**
  - *Yinjun Liu, Xinye Li, Ruisen Peng et al.*
  - `2026-11-25`
  - Large language models (LLMs) perform well on chemistry knowledge benchmarks, which mainly assess question answering and isolated tasks. Chemical research, however, requires using specialized tools and interpreting their outputs to obtain chemically valid results. To address this…

- **[MedSkill-E$^{2}$: Evaluating and Evolving Skills for Medical Agents](https://arxiv.org/abs/2611.34250v1)**
  - *Jingjing Hua, Shaocong Wei, Jianghan Shen et al.*
  - `2026-11-25`
  - Large language model (LLM) agents increasingly use skills to access domain knowledge and complete real-world tasks. We observe that even when a skill specifies the rules and procedures needed for a task, agents may fail to apply them effectively during autonomous execution, a phe…

- **[Navigent: A Geometry-Grounded Agentic Framework for Vision Language Navigation](https://arxiv.org/abs/2611.34249v1)**
  - *Xinyu Zhou, Weiren Cai, Yitong Chen et al.*
  - `2026-11-25`
  - Vision-and-Language Navigation (VLN) with general-purpose multimodal large language models (MLLMs) offers a flexible alternative to task-specific navigation policies, while reliable long-horizon execution remains challenging. Agents must track navigation progress, detect discrepa…

- **[EXPOSURE: Explaining Sources of Uncertainty in Reinforcement Learning](https://arxiv.org/abs/2611.34248v1)**
  - *Kiana Farhadyar, Yannick Vogt, Philipp Laur et al.*
  - `2026-11-25`
  - Shapley values in reinforcement learning are used to explain which observation features drive an agent's behavior and expected return, but not its certainty. Explaining certainty requires understanding how observation features influence different sources of return uncertainty, an…

- **[PROVE: Mitigating Long-Horizon LLM Collusion with Reinforcement Learning from Verified Evidence](https://arxiv.org/abs/2611.34215v1)**
  - *Haochen Luo, Jie Fu, Mukai Li et al.*
  - `2026-11-25`
  - When LLM agents verify each other's work over a long interaction, they drift into collusion: they come to accept work without the evidence that the verification protocol requires. Collusion is absent at the start and builds up episode by episode, which we trace to accurate feedba…

- **[MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance](https://arxiv.org/abs/2611.34188v1)**
  - *Truong Phan, Ngoc-Quan Pham, Dat Quoc Nguyen*
  - `2026-11-25`
  - Existing defenses against indirect prompt injection in retrieval-augmented generation (RAG) are inherently reactive: prompt-engineering methods are often overridden by the injected instructions, while supervised detectors must be retrained for each new attack style. We propose a…

- **[Agentic-Level Adversarial Purification: Revisiting Diffusion Purifiers on Native-Resolution Agentic Inputs](https://arxiv.org/abs/2611.34181v1)**
  - *Yan Lin, Zhongliang Guo, Jingyu Lin et al.*
  - `2026-11-25`
  - Vision-language agents act on native-resolution renders of multi-element pages, where one perturbed photo or a few altered text strokes can redirect the decision. Any content provider can craft such a perturbation on the open model behind the agent, so a plug-in purifier is the n…

- **[Strategic and Robust Task Allocation for Combat Objectives in Adversarial Multi-Agent Environments](https://arxiv.org/abs/2611.34158v1)**
  - *Jonas Peché, Dmitry Matveev, Vladimir Ciric et al.*
  - `2026-11-25`
  - Task allocation in contested-objective team games requires coordinated decisions under uncertainty, spatial constraints, and changing tactical conditions. In such settings, multiple agents must anticipate both teammate behavior and opponent actions. We study a hybrid predict-then…

- **[Reproducer Synthesis for AI-Reported Bugs in the Linux Kernel](https://arxiv.org/abs/2611.34142v1)**
  - *Xiao Wu, Yunbo Ni, Hao Sun et al.*
  - `2026-11-25`
  - Agentic review systems are increasingly flagging suspected bugs in Linux kernel patches as textual reports. A maintainer who receives such reports needs further inspection to determine whether the report is true. The inspection requires understanding whether the bug can be trigge…

- **[Unstable Action Boundaries in Lethal Drone Agents](https://arxiv.org/abs/2611.34121v1)**
  - *Jacques Dumora, André-Louis Rochet, Simon Roburin*
  - `2026-11-25`
  - Tool-using large language model (LLM) agents raise safety risks that are not captured by text-only refusal behavior, especially when tools can trigger high-impact actions. This concern is salient in military settings, where autonomous weapons raise the possibility of delegating f…

- **[Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades, and Agent Orchestration](https://arxiv.org/abs/2611.34112v1)**
  - *Dat Tat Mai, Hung Tran Quy, Thai Viet Pham et al.*
  - `2026-11-25`
  - Executing monolithic neural weights, frontier foundation models, or entire multi-agent workflows uniformly on every input incurs substantial computational, latency, and monetary overhead. Conditional computation mitigates this cost by deciding dynamically which internal experts,…

- **[Budget, Readout or Reasoning? Where Small Reasoning Models Lose Value in Auction Bidding](https://arxiv.org/abs/2611.34068v1)**
  - *Mahbod Khaleti, Seyed Reza Tavakoli, Baran Hoseini et al.*
  - `2026-11-25`
  - Ad platforms and marketplaces show bidders a bid landscape, the estimated chance of winning at each candidate bid, and increasingly let agents built on reasoning language models choose the bid. We give six open reasoning models of 4B to 14B parameters such landscapes, with win cu…

- **[Few-Shot Adaptation of Vision-Language Models via Agentic Model Editing](https://arxiv.org/abs/2611.34036v1)**
  - *Yusheng Zhao, Xiao Luo, Zhiping Xiao et al.*
  - `2026-11-25`
  - Few-shot adaptation transfers pretrained Vision-Language Models (VLMs) to new domains using a small set of labeled images. Most methods fit prompts, representations, or classifiers within an adaptation procedure specified in advance. Yet the visual distinctions needed for recogni…

- **[Post-Training Policy Replication for Strategy-Following Multi-Agent Deep Reinforcement Learning across Team Sizes](https://arxiv.org/abs/2611.34035v1)**
  - *Yamato Takahagi, Yoshinari Motokawa, Toshiharu Sugawara*
  - `2026-11-25`
  - Although multi-agent deep reinforcement learning enables coordinated behavior, aligning it with managerial intent remains difficult due to complex agent interactions. Although the strategy-following distributed attentional actor architecture (sfDA7-X) improves controllability via…

- **[DosePET: An Open-Source Dataset with 2100 Radiation Dose Maps for PET/CT](https://arxiv.org/abs/2611.34008v1)**
  - *Eleftherios Tzanis, Antonios Tzortzakakis, Michail E. Klontzas*
  - `2026-11-25`
  - Large collections of three-dimensional radiation dose maps linked to patient anatomy are needed to develop artificial intelligence (AI) models for personalized internal dosimetry in nuclear medicine, but access to such data remains limited. Here we present DosePET, an open-source…

- **[Kolpona: An Agentic Framework with Gradient-Free Neuron Programming for RTL Generation](https://arxiv.org/abs/2611.33973v1)**
  - *Musa Tur Farazi, Md Nasir Uddin, Soumik Bhattacharjee et al.*
  - `2026-11-25`
  - Open-weight large language models (LLMs) for register-transfer level (RTL) design are usually improved by fine-tuning on curated Verilog corpora, which needs large sets of verified designs and GPU training. We present Kolpona, an agentic framework that improves such models withou…

- **[PatternMiner: Automated Mathematical Discovery Through LLM-Guided Training and Interpretation of Small Models](https://arxiv.org/abs/2611.33966v1)**
  - *Michael Ruofan Zeng, Junaid Hasan, Xuanyu Yang et al.*
  - `2026-11-25`
  - There are several approaches to AI-driven mathematical discovery. One of these involves the use of large language models (LLMs) to resolve well-specified conjectures via text-based reasoning, while another uses narrow models and interpretability for more open-ended, human-in-the-…

- **[AI Buckingham: Agentic Discovery of Dimensionless Scaling Laws Across Physical Regimes](https://arxiv.org/abs/2611.33961v1)**
  - *Ao Cheng, Lei Zhang, Guowei He*
  - `2026-11-25`
  - Classical dimensional analysis defines admissible dimensionless representations but does not determine which combinations capture the dominant physical dependence, whether it changes across physical regimes, or when dependent-variable rescaling is required. We present AI Buckingh…

- **[What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench](https://arxiv.org/abs/2611.33943v1)**
  - *Haozhe Zhang, Zhen Long*
  - `2026-11-25`
  - Agent skills are directories of instructions, reference materials, and scripts loaded on demand by coding agents. According to SkillsBench, although human-curated skills can raise the passing rate by about 16.6 percentage points (pp) on average, they have actually reduced the res…

- **[Connecting AI Agents to Live Discrete Element Simulations via the Model Context Protocol](https://arxiv.org/abs/2611.33926v1)**
  - *Yusong Han, Ryosuke Uzuoka, Kyohei Ueda*
  - `2026-11-25`
  - This paper describes a Model Context Protocol (MCP) server through which a general-purpose AI agent operates a discrete element engine, commercial or open-source, while the simulation runs. The agent submits a long simulation to the engine and, while it computes, reads the runnin…

- **[EGSE: Evidence-Grounded Skill Evolution for Medical Reasoning Agents](https://arxiv.org/abs/2611.33909v1)**
  - *Mingyuan Li, Tong Jia, Ziyuan Yang et al.*
  - `2026-11-25`
  - Medical reasoning agents combine foundation models with specialized tools to interpret medical images, yet reusing their historical experience remains challenging. A correct final answer can conceal flawed reasoning or tool use, synthesized advice may lack source support, and sup…

- **[EATS: Scaling Tool-Use Experience for Medical Reasoning Agents](https://arxiv.org/abs/2611.33897v1)**
  - *Mingyuan Li, Tong Jia, Haoran Wang et al.*
  - `2026-11-25`
  - Medical reasoning agents combine large language model (LLM) reasoning with clinical workflows and specialized neural tools. However, general-purpose LLMs receive limited training exposure to domain-specific medical tools, and the uncertainty and distributional shifts of neural to…

- **[When Are Parallel Subagents Effective for Coding? An Empirical Study on Repository Construction](https://arxiv.org/abs/2611.33893v1)**
  - *Zhiheng Lyu, Chengyu Yin, Lingming Zhang*
  - `2026-11-25`
  - LLM-based coding agents are increasingly used for long-horizon tasks such as building an entire program from a specification. Products like Codex and Claude Code let an agent delegate work to parallel subagents, multiplying run cost, yet it remains unclear whether and when delega…

- **[FORK: Co-Evolving Safe Disclosure and Decision Skills Against Attackers Who Read Every Refusal](https://arxiv.org/abs/2611.33879v1)**
  - *Hieu Man, Chao Shang, Rui Dong et al.*
  - `2026-11-25`
  - When a guardrail rejects an LLM agent's action, its message reaches any attacker observing the trajectory: a fixed refusal leaves benign users unable to recover, whereas an explanation can tell the attacker what to try next. We study this as safe disclosure: explaining rejections…

- **[Can Its Own Misses Teach an MLLM to Find Small Brain Metastases?](https://arxiv.org/abs/2611.33836v1)**
  - *Yixuan Duan, Kexin Geng, Hanwen Xu et al.*
  - `2026-11-25`
  - Multimodal large language models (MLLMs) are becoming general readers of medical images, yet they remain weak at locating small abnormalities. Brain metastases expose this gap: at 384 px a 0.1 mL lesion covers less than a quarter of one visual token, and at one false positive per…

- **[FEAST: Fair and Efficient Adaptive Sampling for Task-Free On-Policy Learning](https://arxiv.org/abs/2611.33827v1)**
  - *Yongxi Zhu, Ziyi Wang, Yichen Wu et al.*
  - `2026-11-25`
  - Language agents trained from self-generated experience must allocate a limited rollout budget across heterogeneous capabilities. A common strategy is to prioritize capabilities with strong current learning signals, but in on-policy learning these signals are endogenous: past allo…

- **[MetaDecomp: Adaptive Task Decomposition via Meta-Learned Procedural Memory](https://arxiv.org/abs/2611.33822v1)**
  - *Ziyi Wang, Yixiao He, Yichen Wu et al.*
  - `2026-11-25`
  - Reusing past experience in long-horizon tasks requires more than storing successful procedures: Language agents must distinguish which procedures apply and what work remains as execution progresses. We introduce MetaDecomp, an in-context meta-learning framework for adaptive task…

- **[RadOncGym: An Agent-Based Framework for Radiotherapy Dose-Mimicking Optimization](https://arxiv.org/abs/2611.33821v1)**
  - *Tong Miao, Shupeng Cheng, Xiwen Chen et al.*
  - `2026-11-25`
  - AI dose-prediction models generate patient-specific 3D dose distributions from patient anatomy, providing an important intermediate representation for automated radiotherapy planning. However, an AI-predicted dose must undergo downstream optimization to produce a physically const…

- **[LSRP*-LA: Scalable and Anytime Multi-Agent Path Finding for Large Agents with Asynchronous Actions](https://arxiv.org/abs/2611.33793v1)**
  - *Dachuan Liu, Shizhe Zhao, Zhongqiang Ren*
  - `2026-11-25`
  - Multi-Agent Path Finding (MAPF) seeks collision-free paths for multiple agents from their start locations to their goal locations while minimizing path costs. Most MAPF algorithms assume that each agent occupies a single vertex and that the actions of all agents are synchronized.…

- **[ExtractBench Pro: The Long Tail of Document Extraction](https://arxiv.org/abs/2611.33791v1)**
  - *Boyang Zhang, Justin Xu, Adrian Lyjak et al.*
  - `2026-11-25`
  - We present ExtractBench Pro, a schema-guided document extraction benchmark that tests six challenging modes of extraction underrepresented in existing datasets. It is created following a framework for synthetic document generation, in which deterministic document generators assem…

- **[TransHarness: From Benchmark Overfitting to Transferable Harness Evolution](https://arxiv.org/abs/2611.33757v1)**
  - *Tianze Xia, Zimo Wang, Heng Tong et al.*
  - `2026-11-25`
  - Harness evolution offers a path to improving coding agents without updating model weights. However, existing methods can overfit their evolution benchmarks, producing gains that fail to carry over to new tasks. To address this challenge, we introduce Transferable Harness Evolutio…

- **[JOVE ICE: Intent Guided Cloud Edge Device Collaboration for AI Glasses](https://arxiv.org/abs/2611.33735v1)**
  - *Yuyang Jin, Bingfeng Pi, Jiamei Sun et al.*
  - `2026-11-25`
  - Recent advances in large language models (LLMs) and LLM based agents have expanded the capabilities of AI glasses, enabling egocentric visual question answering, memory retrieval, and proactive assistance. These applications involve diverse inputs, including speech, images, and v…

- **[Asset4D-Bench: Benchmarking Coding Agents for Editable 3D and 4D Reconstruction](https://arxiv.org/abs/2611.33728v1)**
  - *Chengyi Sun, Deyuan Liu, Lei Zhao et al.*
  - `2026-11-25`
  - A cart can follow its reference trajectory while its cargo floats above the deck. Asset4D-Bench tests whether coding agents recover objects, motion and interactions from visual references as editable Blender scenes. Its 114 conditions span image editing, video reconstruction with…

- **[PowerFix: Physics-Guided Iterative Repair for LLM-Assisted Power Converter Design](https://arxiv.org/abs/2611.33712v1)**
  - *Can Wang, Shi Qiu, Fanfan Lin*
  - `2026-11-25`
  - Large language model (LLM) agents are increasingly being explored for automated engineering design. However, repairing power-converter designs that fail engineering validation remains challenging: the system must identify physical causes, locate responsible design variables, and…

- **[P-FedSkill: A Personalized Federated Skill Learning Framework under Task Heterogeneity](https://arxiv.org/abs/2611.33707v1)**
  - *Zehang Lin, Jiayi Ji, Rongrong Ji*
  - `2026-11-25`
  - Skill learning has become an important way to improve agent performance. However, agent trajectories often contain sensitive information and cannot be shared across clients, hindering collaborative skill learning. To tackle this issue, federated skill learning (FSL) has emerged a…

- **[EVA: Evidence-seeking Visual Agent for Hallucination-Resistant Multimodal Reasoning](https://arxiv.org/abs/2611.33706v1)**
  - *Ting Lei, Yu Chen, Yang Liu*
  - `2026-11-25`
  - Hallucinations in multimodal large language models (MLLMs) often arise from visual assumptions that go unchecked. Self-reflection, multi-agent debate, and counterfactual verification can reinforce erroneous conclusions when they rely on the same unverified visual assumptions. Ext…

- **[Sports Agent: A Self-Evolving System for Conversational Data Analytics](https://arxiv.org/abs/2611.33700v1)**
  - *Chao Chen, Fuqi Lin, Ze Chen et al.*
  - `2026-11-25`
  - Conversational sports analytics requires accurate, evidence-based responses with low latency. Changes in query distributions, data resources, and model behavior can degrade static agent configurations, motivating controlled evolution guided by runtime evidence.   We present Sport…

- **[Read Before You Use: Improving Visual Memory Utilization in Vision-Language Models](https://arxiv.org/abs/2611.33687v1)**
  - *Junseok Kim, Kyungmin Min, Kyomin Jung*
  - `2026-11-25`
  - Multimodal memory enables long-horizon vision-language agents to preserve and retrieve past experiences. While prior research has focused on memory construction and retrieval, effectively using the provided memory remains a challenge for vision-language models (VLMs). We find tha…

- **[Interactive Proofs as a Unified Framework for Evaluating and Leveraging Verifiable Proof Generation by LLM Agents](https://arxiv.org/abs/2611.33676v1)**
  - *Yankai Shu, Xingyu Zhao, Chuan Mao et al.*
  - `2026-11-25`
  - Recent advances in LLM-assisted theorem proving and program verification have attracted widespread attention. Beyond determining whether a proposition is true, LLM agents must produce evidence that can be independently checked by humans or formal verification tools. To evaluate t…

- **[SlicePlanner: Logic-Guided Agentic AI for Online QoS-Aware Network Slicing in Open RAN](https://arxiv.org/abs/2611.33664v1)**
  - *Adhwaa Al-Chaab, Ayman Younis, Dario Pompili*
  - `2026-11-25`
  - Adaptive network slicing in Open Radio Access Network (O-RAN) demands reconfiguration decisions that respond to live traffic conditions while remaining safe with respect to Service Level Agreement (SLA) constraints, a combination that purely data-driven controllers cannot reliabl…

- **[How Much Effort Does an AI Code Reviewer Need? Evidence from Claude 5.5 Models on Plausible-but-Wrong Patches](https://arxiv.org/abs/2611.33639v1)**
  - *Zax Shen, Hanling Zhang, Zixu Wang*
  - `2026-11-25`
  - AI coding agents write code faster than people can review it, so teams add AI reviewers. Reasoning models let such a reviewer trade cost for diligence through an effort setting. We asked how much effort a reviewer needs to catch plausible-but-wrong patches, which pass a benchmark…

- **[Controllable CAD Generation and Interactive Editing of Fluid Rotors](https://arxiv.org/abs/2611.33617v1)**
  - *Shen Chen, Lei Li, Jiajun Sun et al.*
  - `2026-11-25`
  - Computer-aided design (CAD) provides the geometric foundation for rotors in fluid rotating machinery. However, creating models for different rotors requires different modeling processes, making it difficult to control geometry through design intent and reuse existing models. We i…

- **[The Detour Is the Danger: Preserving Security During LLM Agent Recovery](https://arxiv.org/abs/2611.33605v1)**
  - *Boyang Ma, Jinku Li, Hao Wu et al.*
  - `2026-11-25`
  - LLM agents increasingly rely on external tools and reusable Skills to execute complex workflows, autonomously replanning when operations fail. However, such recovery may preserve task functionality while silently discarding the security protections required by the original workfl…

- **[FIG-MAC: A Fine-grained Inspiration Graph Empowered Multi-Agent Collaboration for Automated Scientific Hypothesis Generation](https://arxiv.org/abs/2611.33563v1)**
  - *Siyuan Chen, Yuping Gao, Tai Huang et al.*
  - `2026-11-25`
  - Automated Scientific Hypothesis Generation (ASHG) leveraging large language models (LLMs) aims to harness their strengths in knowledge integration, logical reasoning, and text generation for efficiently producing innovative, verifiable scientific hypotheses. However, existing app…

- **[Provably Efficient Offline Discounted Reinforcement Learning under Recursive Entropic Risk](https://arxiv.org/abs/2611.34840v1)**
  - *Amirparsa Bahrami, Oliver Mortensen, Mohammad Sadegh Talebi*
  - `2026-11-25`
  - We study risk-sensitive reinforcement learning in finite discounted infinite-horizon Markov Decision Processes with recursive entropic risk measures (ERM), parameterized by $β\neq 0$. We consider both risk-averse ($β>0$) and risk-seeking ($β<0$) settings. We consider the offline…

- **[Deep Reinforcement Learning for Multi-UAV Data Harvesting Under Variable Team Sizes and Agent Loss](https://arxiv.org/abs/2611.34818v1)**
  - *Thiago de Souza Lamenza, Bruno José Olivieri de Souza, Markus Endler*
  - `2026-11-25`
  - Collecting data from wireless sensors can be challenging when limited communication infrastructure prevents them from offloading their measurements. In such settings, unmanned aerial vehicles (UAVs) can exploit their mobility to harvest data locally, while coordinated UAV teams c…

- **[Kant-Q: A Q-Learning Algorithm for Kantian Equilibrium in Symmetric Markov Games](https://arxiv.org/abs/2611.34536v1)**
  - *Rishi Bharadwaj, Sujit Gujar, Yadati Narahari*
  - `2026-11-25`
  - AI agents increasingly interact with one another, and many of these interactions are mixed-motive games, which have posed a persistent challenge for learning algorithms. Most multi-agent reinforcement learning (MARL) algorithms are designed to reach Nash equilibria, yet in many s…

- **[AliceAI-Foundation-80B-A3B-Base](https://arxiv.org/abs/2611.34529v1)**
  - *Nikolay Skachkov, Ekaterina Redina, Maksim Konoplev et al.*
  - `2026-11-25`
  - We present AliceAI-Foundation-80B-A3B-Base, a mixture-of-experts language model with 80 billion total parameters and approximately 3 billion active parameters per token, trained from scratch at Yandex and released under the Apache 2.0 license. The model combines Kimi Delta Attent…

- **[SMOTE 25 Years of Magic: What Has Been Done, What the Evidence Shows, and Whom It Reached](https://arxiv.org/abs/2611.34511v1)**
  - *Thanapong Intharah, Pharamut Makjaroen, Kanvara Thawarorit et al.*
  - `2026-11-25`
  - Background. SMOTE was published in this journal in 2002 and reviewed here at its fifteenth anniversary in 2018. At twenty-five it is cited by more than 34,000 indexed works, half of them outside computer science. Objectives. To establish what the methods built on SMOTE change, ho…

- **[Compute-Aware Submodular Online Learning in Open Multi-Agent Systems](https://arxiv.org/abs/2611.34211v1)**
  - *Jing Liu, Luca Ballotta, Fangfei Li et al.*
  - `2026-11-25`
  - This paper studies policy learning for cooperative task allocation in open multi-agent systems, where submodular utilities model diminishing marginal returns due to overlapping agent contributions. While standard methods evaluate every candidate action to update the policy, this…

- **[Agent-as-a-Verifier: From Scores to Evidence for General Verification](https://arxiv.org/abs/2611.34132v1)**
  - *Yuxuan Sun, Hao, Chen et al.*
  - `2026-11-25`
  - Verification is increasingly critical across various inference and learning paradigms, such as test-time scaling, recursive intelligence and automated research, where feedback can improve efficiency and optimization. Common score-based verifiers, or discriminative reward models,…

- **[Feature Engineered Reinforcement Learning for S-pair Selection in Buchberger's Algorithm](https://arxiv.org/abs/2611.34088v1)**
  - *Uzma Shafiq, Matthew England, Nayyar Zaidi*
  - `2026-11-25`
  - Selecting the order in which to process S-pairs is a crucial decision in Buchberger's algorithm for computing Groebner bases: this choice can change the cost by orders of magnitude. Recent work has shown that reinforcement learning agents viewing exponent vectors of the polynomia…

- **[Normalizing Flows are Capable World Models](https://arxiv.org/abs/2611.33872v1)**
  - *Zijia Li, Yong-Hyun Park, Shusheng Yang et al.*
  - `2026-11-25`
  - A world model lets an agent anticipate the consequences of its actions and use imagined futures to make decisions. We introduce Normalizing-Flow World Model (NFWM), which pairs an invertible observation encoder with an action-conditioned probabilistic predictor. Because the encod…

- **[PoVi: Agentic Poetry-to-Video Generation with Knowledge Grounding and Figurative Understanding](https://arxiv.org/abs/2611.34690v1)**
  - *Yuxia Zhu, Shiying Zhang, Lingzhuang Sun et al.*
  - `2026-11-25`
  - Poetry-to-video generation requires more than translating text into visual scenes. Poetic language is highly compressed, often depends on historical and cultural knowledge, and frequently conveys meaning through metaphor, imagery, and other non-literal expressions. We introduce P…

- **[Learning from Unreliable Operator References: Claim-Level Rewards for Customer Support Agents](https://arxiv.org/abs/2611.34341v1)**
  - *Dmitrii Stoianov, Olga Tsymboi, Danil Taranets et al.*
  - `2026-11-25`
  - Even a correct operator reply can be an unreliable training target for a customer-support agent. About a quarter of the factual claims in these replies lacked full support in the agent's knowledge base and tool records. We treat operator replies as claims to verify rather than an…

- **[Failure Broadens, Success Sharpens: Continual Adaptation of Tool-Use Agents Across Diverse Tasks with Dual-Polarity Memory](https://arxiv.org/abs/2611.33612v1)**
  - *Tianmai M. Zhang, Hoda Shajari, Amr Hendy et al.*
  - `2026-11-25`
  - Large language model agents can self-improve over time by utilizing procedural memory derived from prior task trajectories, yet the distinct utilities of memories derived from local successes and failures remain underexplored. This work studies this question in a realistic settin…

- **[AutoRSP: An AI Agent for Radar Sensing Pipeline Design](https://arxiv.org/abs/2611.34754v1)**
  - *Zhi Zheng, Xincheng Xie, Avery Gump et al.*
  - `2026-11-25`
  - Radar sensing demands a pipeline that is well-thought-out across hardware and software. We ask whether an AI agent can automatically design radar sensing pipelines at a fraction of the time, cost, and expertise that current practice needs. We present AutoRSP, an agent that embeds…

- **[Energy-Aware Distributed Task Allocation via Local Submodular Maximization](https://arxiv.org/abs/2611.34293v1)**
  - *Jing Liu, Fangfei Li, Xin Jin et al.*
  - `2026-11-25`
  - This paper studies distributed task allocation under time-varying agent sets, task sets, and communication graphs. At each decision epoch, the stage allocation problem is formulated as monotone submodular maximization over a time-varying, energy-filtered admissible ground set sub…

- **[Welfare-Enhancing Mechanism Design for Agent Ecosystems](https://arxiv.org/abs/2611.33627v1)**
  - *Zitian Guo, Chen Xu, Beibei Li et al.*
  - `2026-11-25`
  - The emerging Agentic Web forms a multi-agent ecosystem: a decentralized service market where the user agent selects which content agents to query from their submitted profiles, before seeing any documents. Profiles therefore become a new target of optimization. Existing Generativ…

- **[PRIOR: Pre-Call Reasoning in SFT and Its Influence on Tool-Use Retention under RL](https://arxiv.org/abs/2611.33648v1)**
  - *Kaiwen Hu, Hyunin Lee, Joseph Suh et al.*
  - `2026-11-25`
  - Tool use learned during supervised fine-tuning (SFT) is not always retained during reinforcement learning (RL). We study how properties of SFT data may affect this retention by constructing Low, Medium, and High SFT datasets with approximately matched token budgets but different…

- **[HoMe: Toward Practical Harness Optimization of Memory Systems for AI Assistants](https://arxiv.org/abs/2611.34624v1)**
  - *Yifei Xu, Li Yu, Zhaoyang Liu et al.*
  - `2026-11-25`
  - The behavior of memory systems for long-running AI assistants is governed by a harness, which consists of the code, prompts, and configurations for memory construction, maintenance, retrieval, and answer generation. However, optimizing the harness of a memory system remains large…

- **[PRECEPT: Security Self-Improvement of Coding Agents via Evolving Principles](https://arxiv.org/abs/2611.33519v1)**
  - *Keyan Guo, Rupam Patir, Haipeng Cai et al.*
  - `2026-11-24`
  - AI coding agents increasingly write and submit code with limited human review, and much of it passes functional tests while remaining insecure. We show that these failures persist. Across 14 task sequences, Codex, Claude Code, and Qwen Code fixed a vulnerability 85.7% of the time…

- **[Learning to Reason in Real-Time](https://arxiv.org/abs/2611.33513v1)**
  - *Xavier Schneider, Benjamin Schneider, Sun Sun et al.*
  - `2026-11-24`
  - AI agents that operate in the real world must reason correctly and on-time, yet they currently do not account for how time should alter their reasoning. Modern agents learn to do tasks in environments that are entirely synchronous: where the world waits for the agent to act befor…

- **[Benchmarking Open-Ended Vulnerability Discovery in Windows Kernel Binaries](https://arxiv.org/abs/2611.33486v1)**
  - *Jongseong Kim, Hwiwon Lee, Dongjun Kim et al.*
  - `2026-11-24`
  - Frontier models are increasingly used to discover real-world security vulnerabilities, making it critical to systematically evaluate their cybersecurity capabilities. However, existing security benchmarks primarily focus on known vulnerabilities in open-source projects, largely o…

- **[Dynamic Reasoning in Next-Gen Detection and Response: An Empirical Study of LLM Triage, Reinforcement Tuning, and Adversarial Evasion](https://arxiv.org/abs/2611.33470v1)**
  - *Jeremy Canale*
  - `2026-11-24`
  - We present an end-to-end empirical study of dynamic reasoning in next-generation detection and response pipelines, evaluating how static classifiers, graph-based signal fusion, and large language model (LLM) triage agents perform under strict human-analyst attention budgets (Reca…

- **[SecID: An LLM-Guided Framework for Threat-Aware Secondary Asset Identification with Quantitative RTL Analysis](https://arxiv.org/abs/2611.33453v1)**
  - *Md Ajoad Hasan, Dipayan Saha, Upoma Das et al.*
  - `2026-11-24`
  - The growing complexity of modern hardware designs is making security assurance increasingly difficult. One of the foundational steps in pre-silicon security verification is identifying security assets. While primary assets are often evident from design functionality, the internal…

- **[Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows](https://arxiv.org/abs/2611.33402v1)**
  - *Siddharth Arya, Kshitij Jain*
  - `2026-11-24`
  - AI models vary enormously in capability and price. Model routing exploits this by sending easier tasks to cheaper models. However, a single agentic task often combines easy and difficult subtasks, making one model choice for the entire task inefficient. We introduce partial routi…

- **[Confidence scores for gated automation of large language models](https://arxiv.org/abs/2611.33394v1)**
  - *Luiz G. A. Alves, Aaron Vermeersch*
  - `2026-11-24`
  - AI agents built on large language models (LLMs) demonstrate strong capabilities in automated decision-making. However, LLMs may produce incorrect answers with high confidence, limiting their applicability in decisions that affect individuals and organizations. Reliable confidence…

- **[RoboARC: Physical Puzzles for Robotic Manipulation under Spatial Constraints](https://arxiv.org/abs/2611.33390v1)**
  - *Qineng Wang, Jianwen Lyu, Pingyue Zhang et al.*
  - `2026-11-24`
  - Many hard manipulation tasks come down to a spatial constraint that only a few motions satisfy, such as passing a part through a gap barely wider than itself or separating two interlocked parts. These motions depend on the exact geometry of each scene, so demonstrations and skill…

- **[Poisoning Self-Evolving Security Policies in LLM Agents](https://arxiv.org/abs/2611.33385v1)**
  - *Aymen Noor, Honglu Jiang*
  - `2026-11-24`
  - Self-evolving defenses improve LLM-agent security by learning reusable policies from observed attacks. However, we demonstrate that this learning process itself can become an attack surface. Using SED (Self-Evolving Defense) in the AgentDojo benchmark, we construct a single promp…

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

- **[Reading Decisions Before Spans: Efficient Generative Verification](https://arxiv.org/abs/2611.32931v2)**
  - *Yanbin Gong, Lei Chen*
  - `2026-11-24`
  - A generative verifier can flag an unsupported claim before it finishes describing the error. For applications that only screen an assistant's report, the remaining generation may be unnecessary. We examine this possibility in a frozen 2B span verifier whose output chooses between…

- **[Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe](https://arxiv.org/abs/2611.32884v1)**
  - *Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang et al.*
  - `2026-11-24`
  - AI agents working on long tasks often commit to an answer before they have enough evidence, a behavior called laziness. In our evaluations, they frequently commit even while their stated belief still names several possible answers. An outcome reward at the end of the episode scor…

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

- **[CypherMAS: Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2611.33242v1)**
  - *Danil Kostromin, Andrey Sakhovskiy, Semen Budennyy*
  - `2026-11-24`
  - Multi-agent systems (MAS) built on large language models (LLMs) distribute reasoning across specialized agents that must exchange messages and invoke tools reliably. Existing evaluations typically couple communication with open domain tasks, making it difficult to determine wheth…

- **[CAPTA: Identifying LLMs Behind AI Agents](https://arxiv.org/abs/2611.32686v1)**
  - *Kailun Yan, Yue Huang, Sisi Duan*
  - `2026-11-24`
  - Large language model (LLM)-based agents access remote services through tools to complete user tasks, often via API calls. In this setting, a remote service may want to identify the backend LLM of an agent to launch model-specific attacks, including prompt injection or selective d…

- **[Economic World Model](https://arxiv.org/abs/2611.32663v1)**
  - *Qirui Mi, Yujia Ming, Bo Li et al.*
  - `2026-11-24`
  - Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions? To answer this question, we define an economic world model (EWM) as an agent's internal representation of how an econo…

- **[Bathys: Advancing Deep Search Agents](https://arxiv.org/abs/2611.32660v1)**
  - *Zixuan Chen, Shengyou Yuan, Nang Yuan et al.*
  - `2026-11-24`
  - Deep search is a critical capability for agents tackling complex, open-ended tasks, where solving a problem requires iterative information gathering, query reformulation, and evidence-based verification rather than a single retrieval step. To address these requirements, we presen…

- **[ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds](https://arxiv.org/abs/2611.32649v1)**
  - *Qingle Liu, Jieming Li, Pei-lin Li et al.*
  - `2026-11-24`
  - In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline,…

- **[TeamFlowRL: Online Policy Optimization of Decentralized Flow Policies for Multi-Agent Coordination](https://arxiv.org/abs/2611.32645v1)**
  - *Guowei Zou, Beiwen Zhang, Haitao Wang et al.*
  - `2026-11-24`
  - Complex cooperative tasks require coordinated multi-agent behavior. Offline generative policies learn expressive cooperative behaviors from trajectories but remain limited by fixed datasets. Online reinforcement learning can improve them through environment interaction. However,…

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

- **[PoseVLN: Learning Geometric State Evolution for Vision-Language Navigation](https://arxiv.org/abs/2611.32218v1)**
  - *Pengyu Hou, Mingfei Han, Haihong Hao et al.*
  - `2026-11-24`
  - Vision-Language Navigation (VLN) requires an embodied agent to relate past experience, current spatial state, and future motion while following natural-language instructions. Recent approaches improve these capabilities through long-horizon memory, state-aware reasoning, and futu…

- **[XMind: Thinking Twice via Cross-Memory Reasoning for LLM-Based Autonomous Driving](https://arxiv.org/abs/2611.32209v1)**
  - *Zuyi Guo, Xianjie Dai, Lei Yang et al.*
  - `2026-11-24`
  - Memory-augmented large language model (LLM) driving agents can reuse past experience, yet previously learned corrections often fail to transfer when traffic conditions change. A key limitation is that existing memories mainly record observed outcomes, providing little evidence ab…

- **[OmniEVIE: Evidence-Vector-Informed Embedding for Multi-modal Retrieval](https://arxiv.org/abs/2611.32203v1)**
  - *Zifei Wang, Wei Wen, Qiang Ji et al.*
  - `2026-11-24`
  - Multimodal retrieval must match dense pages, fine-grained entities, ordered video, and agent tools and memory. Single-vector embeddings lose local evidence, cross-encoders reread every recalled item online, and uncompressed late interaction is too large to serve. We present OmniE…

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

- **[Coding4Games: Can Modern Coding Agents Play Modern Video Games?](https://arxiv.org/abs/2611.31974v1)**
  - *Shifang Zhao, Haoyu Wang, Yuyang Yin et al.*
  - `2026-11-24`
  - Games, especially modern AAA games, challenge language models to perceive complex scenes, control actions, and make decisions over long horizons. Existing game benchmarks primarily test language models as computer-use agents that query a language model throughout play, incurring…

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

- **[Scalpel and Brush: Pruning and Targeted Weight Editing of a Small Language Model by a Single LLM Agent](https://arxiv.org/abs/2611.33426v1)**
  - *Sergei Koltcov, Vera Ignatenko, Anton Surkov et al.*
  - `2026-11-24`
  - It has recently been shown that an LLM can itself edit the weights of a language model, yet it remains unclear which part of such a result is due to the agent and which part is reproduced by a random edit of the same shape, by an instruction in the prompt, or by a standard proced…

- **[An Adversarial Multi-Agent Pursuit Game for Locomotor Agility Pretraining](https://arxiv.org/abs/2611.33407v1)**
  - *Nathan A. C. Hogg, Matt Hyatt, Neil Klingensmith et al.*
  - `2026-11-24`
  - Agile humanoid locomotion requires controllers that can adapt to rapidly changing motion demands while remaining stable and robust. Recent locomotion controllers are typically designed with either a dense reward that is carefully shaped to encourage steps and penalize falling, or…

- **[What Must LLM Agents Communicate? From Information Loss to Communication Failures](https://arxiv.org/abs/2611.33318v1)**
  - *Yi-Yun Chu, Xiaobin Shen*
  - `2026-11-24`
  - When evidence is distributed across LLM agents, a team may collectively possess all the information needed for a decision yet fail to use it effectively. What must agents communicate for accurate joint predictions, and when does interaction help? We study three requirements for e…

- **[Building a Unified Inline Code Editing Model for GitHub Copilot](https://arxiv.org/abs/2611.33314v1)**
  - *Microsoft CodeAI Team, Microsoft VS Code Team, Julia Gong et al.*
  - `2026-11-24`
  - AI-assisted coding ranges from fully agentic coding to inline code suggestions in the editor. Inline suggestions require predicting a developer's most likely next edit from an editing session. The next edit may lie at the cursor, in nearby lines, or farther away, and one editing…

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

- **[Effect-Driven Skill Abstractions for Offline Reinforcement Learning](https://arxiv.org/abs/2611.33229v1)**
  - *Burcu Kilic, David Drexel, Emre Ugur et al.*
  - `2026-11-24`
  - We seek to learn discrete skill abstractions to facilitate long-horizon, goal-conditioned reinforcement-learning (RL) tasks. Recent approaches have shown success by quantizing actions via clustering or reconstruction. However, these objectives lead to skills that are not directly…

- **[Soft Decentralized Expected SARSA: Equilibrium Selection via Gradual Adaptation](https://arxiv.org/abs/2611.33228v1)**
  - *Giuseppe Martucci, Janusz M. Meylahn, Gurdal Arslan et al.*
  - `2026-11-24`
  - We introduce Soft Decentralized Expected SARSA (SDES), a modification of Decentralized Q-learning in which agents maintain persistent exploration and update their acting Q-values gradually rather than switching directly to newly learned best responses when updating. We prove conv…

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

- **[LogToPersona: New Benchmark and Efficient Persona Prediction through Semantic Log Filtering](https://arxiv.org/abs/2611.33510v1)**
  - *Ahmed Alajrami, Ondrej Bohdal, Seokwoo Song et al.*
  - `2026-11-24`
  - Detailed knowledge of a user's persona is valuable for personalizing generative AI models and agents, yet such details are difficult to obtain and change over time. We address the task of inferring persona attributes from a single day of mobile activity logs. No suitable publicly…

- **[AI-human hybrid conversations: Can AI Agents Improve Discourse Quality?](https://arxiv.org/abs/2611.33459v1)**
  - *Ishita Chakraborty, Xingjian You, Shrabastee Banerjee*
  - `2026-11-24`
  - Conversations are central to how people exchange information, share experiences, and develop collective understanding. Yet, across conversational settings, discussions often suffer from uneven participation, unanswered contributions, and a narrow range of perspectives. As generat…

- **[CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies](https://arxiv.org/abs/2611.33148v1)**
  - *Dawid J. Kopiczko, Tijmen Blankevoort, Yuki M. Asano*
  - `2026-11-24`
  - Reasoning models become long-horizon agents through reinforcement learning or, more cheaply, through fine-tuning on a stronger teacher's trajectories, which contain the teacher's chain-of-thought as well as its actions. The standard fine-tuning approach imitates both, yet the str…

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

- **[Avalon-M1: Reinforcement Learning from Collective Rewards](https://arxiv.org/abs/2611.32539v1)**
  - *Iliyan Zarov, Henry Course, Anthony Hartshorn et al.*
  - `2026-11-24`
  - We introduce reinforcement learning from collective rewards (RLCR), a recipe for jointly training language models to act as agent organisations under latency constraints. A CEO and up to eight specialists share one policy, co-ordinate through a message board and workspace, and ar…

- **[MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction](https://arxiv.org/abs/2611.32462v1)**
  - *Yifan Dai, Daili Hua, Bohan Zeng et al.*
  - `2026-11-24`
  - Multi-reference image generation requires a model to preserve the appearance of selected subjects while arranging them according to an instruction. Despite recent progress in reference-based generation and compositional control, reliably organizing selected subjects into the inte…

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

- **[From Conversations to Commitments: A Design Study of Shared Records for Agent-to-Business Coordination](https://arxiv.org/abs/2611.33373v1)**
  - *Carlos Eberhardt, Mansura Habiba*
  - `2026-11-24`
  - Business commitments require accepted terms to be linked to delegated authority, reserved resources and durable evidence. We examine how a shared, attributable interaction record can support these links across independently operated organisations. Talea combines signed AT Protoco…

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

- **[AgentDRC: Multi-Agent Algorithms for Spatially-Aware Automated DRC Correction](https://arxiv.org/abs/2611.31876v2)**
  - *Pengju Liu, Nuo Xu, Winson Chen et al.*
  - `2026-11-24`
  - Design Rule Checking (DRC) error fixing remains a time-consuming bottleneck in physical design, often requiring manual intervention despite advanced EDA optimizations. Existing LLM-agent approaches fall short due to redundant contextual shapes, limited spatial reasoning over raw…

- **[Delta-Vega Hedging with Deep Reinforcement Learning: From Simulation to Reality](https://arxiv.org/abs/2611.32790v1)**
  - *Michele Colombi, Marco Di Francesco, Pietro Rossi*
  - `2026-11-24`
  - Hedging an option portfolio with the underlying asset alone leaves the position exposed to changes in volatility, which can be managed by trading another derivative, at higher transaction costs. We propose a deep reinforcement learning approach to hedge both price and volatility…


## Harness  (102)

### AAAI

- **[D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies](https://arxiv.org/abs/2511.16590)**
  - *Sen Chen, Tong Zhao, Yi Bin et al.*
  - **AAAI 2025** · `2025-11-20`
  - Developing intelligent agents capable of operating a wide range of Graphical User Interfaces (GUIs) with human-level proficiency is a key milestone on the path toward Artificial General Intelligence. While most existing datasets and benchmarks for training and evaluating GUI agen…

- **[Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory](https://arxiv.org/abs/2505.15055)**
  - *Hongli Zhou, Hui Huang, Zi-Qing Zhao et al.*
  - **AAAI 2025** · `2025-05-21`
  - The evaluation of large language models (LLMs) via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities. This paper provides a crit…


### NeurIPS

- **[OpenUnlearning: Accelerating LLM Unlearning via Unified Benchmarking of Methods and Metrics](https://arxiv.org/abs/2506.12618)**
  - *Vineeth Dorna, Anmol Reddy Mekala, Wenlong Zhao et al.*
  - **NeurIPS 2025** · `2025-06-14`
  - Robust unlearning is crucial for safely deploying large language models (LLMs) in environments where data privacy, model safety, and regulatory compliance must be ensured. Yet the task is inherently challenging, partly due to difficulties in reliably measuring whether unlearning…

- **[SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks](https://arxiv.org/abs/2506.11791)**
  - *Hwiwon Lee, Zi-Qi Zhang, Hanxiao Lu et al.*
  - **NeurIPS 2025** · `2025-06-13`
  - Rigorous security-focused evaluation of large language model (LLM) agents is imperative for establishing trust in their safe deployment throughout the software development lifecycle. However, existing benchmarks largely rely on synthetic challenges or simplified vulnerability dat…

- **[REAL: Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites](https://arxiv.org/abs/2504.11543)**
  - *Divyansh Garg, Shaun VanWeelden, Diego Caples et al.*
  - **NeurIPS 2025** · `2025-04-15`
  - We introduce REAL, a benchmark and framework for multi-turn agent evaluations on deterministic simulations of real-world websites. REAL comprises high-fidelity, deterministic replicas of 11 widely-used websites across domains such as e-commerce, travel, communication, and profess…

- **[Envisioning Beyond the Pixels: Benchmarking Reasoning-Informed Visual Editing](https://arxiv.org/abs/2504.02826)**
  - *Xiang-Yu Zhao, Pei-Yuan Zhang, Kexian Tang et al.*
  - **NeurIPS 2025** · `2025-04-03`
  - Large Multi-modality Models (LMMs) have made significant progress in visual understanding and generation, but they still face challenges in General Visual Editing, particularly in following complex instructions, preserving appearance consistency, and supporting flexible input for…


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


### ICLR

- **[HeurekaBench: A Benchmarking Framework for AI Co-scientist](https://arxiv.org/abs/2601.01678)**
  - *Siba Smarak Panigrahi, Jovana Videnović, Maria Brbić*
  - **ICLR 2026** · `2026-01-04`
  - LLM-based reasoning models have enabled the development of agentic systems that act as co-scientists, assisting in multi-step scientific analysis. However, evaluating these systems is challenging, as it requires realistic, end-to-end research scenarios that integrate data analysi…

- **[VERINA: Benchmarking Verifiable Code Generation](https://arxiv.org/abs/2505.23135)**
  - *Zhe Ye, Zheng-Xu Yan, Jing-Xuan He et al.*
  - **ICLR 2025** · `2025-05-29`
  - Large language models (LLMs) are increasingly integrated in software development, but ensuring correctness in LLM-generated code remains challenging and often requires costly manual review. Verifiable code generation -- jointly generating code, specifications, and proofs of code-…


### KDD

- **[Not All Interpretation Methods Are Created Equal: Tiered Evaluation of AI Interpretability](https://arxiv.org/abs/2611.31833v1)**
  - *Nicolas Sanchez, Bin Yu*
  - **KDD** · `2026-11-24`
  - As AI transitions to sociotechnical deployments, uninterpretable models pose serious threats to reliability, public trust and contestability. However, not all interpretation methods are created equal: for interpretability to enhance deployment safety and effectiveness, interpreta…

- **[FinBench: A Benchmarking Framework for Stock Market Prediction and Portfolio Allocation](https://doi.org/10.1145/3770855.3817595)**
  - *Sara Pederzoli, Marta Santacroce, Francesco Guerra et al.*
  - **KDD 2026** · `2026-08-09`
  - Research on stock market prediction relies on public datasets to develop and compare learning-based models. However, existing datasets are often limited to price-based information, cover a restricted set of assets or time periods, or provide only a subset of the heterogeneous sig…

- **[IdeaBench: Benchmarking Large Language Models for Research Idea Generation](https://dl.acm.org/doi/pdf/10.1145/3711896.3737419)**
  - *Si-Kun Guo, Amir Hassan Shariatmadari, Guang-Zhi Xiong et al.*
  - **KDD 2025** · `2025-08-03`
  - Large Language Models (LLMs) have revolutionized interactions between human and artificial intelligence (AI) systems, demonstrating state-of-the-art performance across various domains, including scientific discovery and hypothesis generation. However, the absence of a comprehensi…


### EMNLP

- **[Skeleton-Guided-Translation: A Benchmarking Framework for Code Repository Translation with Fine-Grained Quality Evaluation](https://arxiv.org/abs/2501.16050)**
  - *Xinglian Zhang, Jiaheng Wen, Fangkai Yang et al.*
  - **EMNLP 2025** · `2025-01-27`
  - The advancement of large language models has intensified the need to modernize enterprise applications and migrate legacy systems to secure, versatile languages. However, existing code translation benchmarks primarily focus on individual functions, overlooking the complexities in…


### Other / arXiv

- **[RoboEvo^2: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution](https://arxiv.org/abs/2611.34675)**
  - *Chenzhi Liu, Jiehong Lin, Wei Huang et al.*
  - 🤗 · `2026-11-25`
  - Robots should adapt to unfamiliar environments and acquire new skills through interaction, then execute those skills efficiently with practice. Vision-language-action policies provide efficient control, but often need additional human demonstrations to handle unfamiliar settings;…

- **[Letting Models Manage Their Own Context: Where We Stand](https://arxiv.org/abs/2611.34147)**
  - *Alessio Devoto, Avinash Vem, Tara Safavi et al.*
  - 🤗 · `2026-11-25`
  - Agent harnesses today manage context on the model's behalf: when the window fills, the harness triggers a compaction that summarizes the history. We study the alternative, \emph{model-driven} context management, in which the model itself decides when and what to compact through a…

- **[How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches](https://arxiv.org/abs/2611.34875v1)**
  - *Aakash Goel, Benjamin Steenhoek, Yu Hu*
  - `2026-11-25`
  - Agent patches are larger than developers', which is widely read as over-editing. But patch size does not say whether the extra edits are needed, what they are, or where they come from. We introduce Delta Residue Attribution (DRA), which replays agent trajectories, traces every bl…

- **[MedSkill-E$^{2}$: Evaluating and Evolving Skills for Medical Agents](https://arxiv.org/abs/2611.34250v1)**
  - *Jingjing Hua, Shaocong Wei, Jianghan Shen et al.*
  - `2026-11-25`
  - Large language model (LLM) agents increasingly use skills to access domain knowledge and complete real-world tasks. We observe that even when a skill specifies the rules and procedures needed for a task, agents may fail to apply them effectively during autonomous execution, a phe…

- **[What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench](https://arxiv.org/abs/2611.33943v1)**
  - *Haozhe Zhang, Zhen Long*
  - `2026-11-25`
  - Agent skills are directories of instructions, reference materials, and scripts loaded on demand by coding agents. According to SkillsBench, although human-curated skills can raise the passing rate by about 16.6 percentage points (pp) on average, they have actually reduced the res…

- **[TransHarness: From Benchmark Overfitting to Transferable Harness Evolution](https://arxiv.org/abs/2611.33757v1)**
  - *Tianze Xia, Zimo Wang, Heng Tong et al.*
  - `2026-11-25`
  - Harness evolution offers a path to improving coding agents without updating model weights. However, existing methods can overfit their evolution benchmarks, producing gains that fail to carry over to new tasks. To address this challenge, we introduce Transferable Harness Evolutio…

- **[Sports Agent: A Self-Evolving System for Conversational Data Analytics](https://arxiv.org/abs/2611.33700v1)**
  - *Chao Chen, Fuqi Lin, Ze Chen et al.*
  - `2026-11-25`
  - Conversational sports analytics requires accurate, evidence-based responses with low latency. Changes in query distributions, data resources, and model behavior can degrade static agent configurations, motivating controlled evolution guided by runtime evidence.   We present Sport…

- **[Interactive Proofs as a Unified Framework for Evaluating and Leveraging Verifiable Proof Generation by LLM Agents](https://arxiv.org/abs/2611.33676v1)**
  - *Yankai Shu, Xingyu Zhao, Chuan Mao et al.*
  - `2026-11-25`
  - Recent advances in LLM-assisted theorem proving and program verification have attracted widespread attention. Beyond determining whether a proposition is true, LLM agents must produce evidence that can be independently checked by humans or formal verification tools. To evaluate t…

- **[FIG-MAC: A Fine-grained Inspiration Graph Empowered Multi-Agent Collaboration for Automated Scientific Hypothesis Generation](https://arxiv.org/abs/2611.33563v1)**
  - *Siyuan Chen, Yuping Gao, Tai Huang et al.*
  - `2026-11-25`
  - Automated Scientific Hypothesis Generation (ASHG) leveraging large language models (LLMs) aims to harness their strengths in knowledge integration, logical reasoning, and text generation for efficiently producing innovative, verifiable scientific hypotheses. However, existing app…

- **[AutoRSP: An AI Agent for Radar Sensing Pipeline Design](https://arxiv.org/abs/2611.34754v1)**
  - *Zhi Zheng, Xincheng Xie, Avery Gump et al.*
  - `2026-11-25`
  - Radar sensing demands a pipeline that is well-thought-out across hardware and software. We ask whether an AI agent can automatically design radar sensing pipelines at a fraction of the time, cost, and expertise that current practice needs. We present AutoRSP, an agent that embeds…

- **[HoMe: Toward Practical Harness Optimization of Memory Systems for AI Assistants](https://arxiv.org/abs/2611.34624v1)**
  - *Yifei Xu, Li Yu, Zhaoyang Liu et al.*
  - `2026-11-25`
  - The behavior of memory systems for long-running AI assistants is governed by a harness, which consists of the code, prompts, and configurations for memory construction, maintenance, retrieval, and answer generation. However, optimizing the harness of a memory system remains large…

- **[CHASE: Curiosity-Guided Skill Acquisition for Embodied Task Execution](https://arxiv.org/abs/2611.34416v1)**
  - *Zixuan Wang, Wei Zhang, Chenlei Zhu et al.*
  - `2026-11-25`
  - Robots executing tasks in partially observed environments must resolve uncertainty while operating with incomplete skills. Inspired by human curiosity, we investigate how robots can formulate task-relevant hypotheses, seek evidence, and acquire missing skills during task executio…

- **[LUDIUS: A Benchmark for Embodied Social Intelligence in Everyday Human-Robot Interactions](https://arxiv.org/abs/2611.34328v1)**
  - *Chaewon Kim, Sangheon Lee, Seyeon Choi et al.*
  - `2026-11-25`
  - Social intelligence in a robot requires interpreting a situation from the perspectives of the people involved and using that understanding to decide when and how to act. We introduce LUDIUS, a benchmark for evaluating how vision-language models exercise this judgment through a ro…

- **[CHD-Bench: Diagnosing Congenital Heart Disease through Interactive Examination](https://arxiv.org/abs/2611.33775v1)**
  - *Gautham Krishnan P, Shrisharanyan Vasu, Aniketh Vijesh et al.*
  - `2026-11-25`
  - Diagnosis of congenital heart disease (CHD) requires understanding the spatial relationships between cardiac structures, which clinicians assess by scrolling through CT or cardiac magnetic resonance imaging (MRI) slices and rotating 3D reconstructions. Although automated methods…

- **[Keep or Roll Back? Out-of-Loop Judges for Self-Improving VLA and End-to-End Embodied Policies](https://arxiv.org/abs/2611.33794v1)**
  - *Zilin Huang, Zhengyang Wan, Kangan Qian et al.*
  - `2026-11-25`
  - Self-improvement is now a practical recipe for embodied policies: a policy collects experience, is retrained, and is kept when a judge rates it higher. However, the judge is usually trained or chosen inside the same loop, so its evidence is not independent of the policy. We intro…

- **[KeyDeck: Multi-Paper-to-Slide Generation via Cross-Paper Synthesis and Reference-Guided Personalization](https://arxiv.org/abs/2611.33715v1)**
  - *Tarik Can Ozden, Sachidanand VS, Ram Prakash Reddy Motati et al.*
  - `2026-11-25`
  - Multi-paper-to-slide generation (multi-PTSG) is the task of constructing a unified presentation from multiple research papers by selecting, organizing, and synthesizing information across sources. This task introduces two main challenges: (i) combining multiple sources into a coh…

- **[ChemDeduce: Benchmarking LLMs for Unknown Chemical Identification through Interactive Simulated Experiments](https://arxiv.org/abs/2611.33848v1)**
  - *Hengyi Cai, Yuqi Tang, Zichang Li et al.*
  - `2026-11-25`
  - Large language models (LLMs) have shown strong performance in chemical knowledge and reasoning, yet it remains unclear whether they can solve problems whose answers must be discovered through experimentation. We investigate this question through Unknown Chemical Identification, w…

- **[Multimodal Safety Evaluation of Vision-Language Models in Japanese](https://arxiv.org/abs/2611.33789v1)**
  - *Su Myat Noe, Hisami Suzuki, Kouta Nakayama et al.*
  - `2026-11-25`
  - Vision-Language Models (VLMs) are increasingly deployed in Japanese-language settings, yet multimodal safety evaluation has been largely English-centric. We extend the Multimodal Safety Test Suite (MSTS) of Röttger et al. (2025) to Japanese as the 12th language, contributing 320…

- **[Routeability Before Routing: Routeability Audit Protocol (RAP) and RouteabilityBench for Audited LLM Model Selection](https://arxiv.org/abs/2611.34825v1)**
  - *Yihang Lu, Denica Kjorvezir, Ana Gjorgjevikj et al.*
  - `2026-11-25`
  - LLM routing aims to choose, for each prompt, which model in a portfolio is most likely to answer correctly. This only makes sense when the benchmark contains enough prompt-specific variation for different models to be best on different inputs. On coarse-scored LLM benchmarks, how…

- **[Dynamic Reasoning in Next-Gen Detection and Response: An Empirical Study of LLM Triage, Reinforcement Tuning, and Adversarial Evasion](https://arxiv.org/abs/2611.33470v1)**
  - *Jeremy Canale*
  - `2026-11-24`
  - We present an end-to-end empirical study of dynamic reasoning in next-generation detection and response pipelines, evaluating how static classifiers, graph-based signal fusion, and large language model (LLM) triage agents perform under strict human-analyst attention budgets (Reca…

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

- **[ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds](https://arxiv.org/abs/2611.32649v1)**
  - *Qingle Liu, Jieming Li, Pei-lin Li et al.*
  - `2026-11-24`
  - In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline,…

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

- **[Scalpel and Brush: Pruning and Targeted Weight Editing of a Small Language Model by a Single LLM Agent](https://arxiv.org/abs/2611.33426v1)**
  - *Sergei Koltcov, Vera Ignatenko, Anton Surkov et al.*
  - `2026-11-24`
  - It has recently been shown that an LLM can itself edit the weights of a language model, yet it remains unclear which part of such a result is due to the agent and which part is reproduced by a random edit of the same shape, by an instruction in the prompt, or by a standard proced…

- **[Online Environment Repair for Coding Agents](https://arxiv.org/abs/2611.32037v1)**
  - *Sheng Lu, Rui Mao, Zewei Chen et al.*
  - `2026-11-24`
  - Programmatic verifiers provide scalable reward signals for training coding agents with reinforcement learning, yet subtle harness defects and incomplete unit tests allow policies to earn full credit without solving the intended task. Existing training-time defenses intervene eith…

- **[Avalon-M1: Reinforcement Learning from Collective Rewards](https://arxiv.org/abs/2611.32539v1)**
  - *Iliyan Zarov, Henry Course, Anthony Hartshorn et al.*
  - `2026-11-24`
  - We introduce reinforcement learning from collective rewards (RLCR), a recipe for jointly training language models to act as agent organisations under latency constraints. A CEO and up to eight specialists share one policy, co-ordinate through a message board and workspace, and ar…

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

- **[A Perturbation-Driven Framework for Sensitivity Analysis of Dimensionality Reduction](https://arxiv.org/abs/2611.33523v1)**
  - *Md Afridi Hasan, Jaemin Jo, Takanori Fujiwara*
  - `2026-11-24`
  - Low-dimensional representations produced by dimensionality reduction (DR) are commonly evaluated using distortion measures such as trustworthiness and continuity. In this paper, we study the sensitivity of DR methods to plausible input variations by quantifying changes in structu…


## Finance  (150)

### AAAI

- **[D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies](https://arxiv.org/abs/2511.16590)**
  - *Sen Chen, Tong Zhao, Yi Bin et al.*
  - **AAAI 2025** · `2025-11-20`
  - Developing intelligent agents capable of operating a wide range of Graphical User Interfaces (GUIs) with human-level proficiency is a key milestone on the path toward Artificial General Intelligence. While most existing datasets and benchmarks for training and evaluating GUI agen…


### NeurIPS

- **[Multi-Identity Transaction Graph Pretraining for Fraud Detection](https://openreview.net/forum?id=1edqcNjZ3J)**
  - **NeurIPS 2026** · OpenReview · `2026-09-07`
  - Real-world payment risk modeling is constrained by scarce fraud labels and fragmented behavioral context across multiple payment identities. A physical transaction may appear simultaneously in multiple behavioral histories defined by different identities, while each identity indu…


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


### KDD

- **[FinBench: A Benchmarking Framework for Stock Market Prediction and Portfolio Allocation](https://doi.org/10.1145/3770855.3817595)**
  - *Sara Pederzoli, Marta Santacroce, Francesco Guerra et al.*
  - **KDD 2026** · `2026-08-09`
  - Research on stock market prediction relies on public datasets to develop and compare learning-based models. However, existing datasets are often limited to price-based information, cover a restricted set of assets or time periods, or provide only a subset of the heterogeneous sig…

- **[Adaptive Financial Sentiment Analysis for NIFTY 50 via Instruction-Tuned LLMs ,RAG and Reinforcement Learning Approaches](https://arxiv.org/abs/2512.20082)**
  - *Chaithra Sadashiva Kotekar, B. Mohan, Kamesh Kadimisetty*
  - **KDD 2025** · `2025-12-17`
  - Financial sentiment analysis plays a crucial role in informing investment decisions, assessing market risk, and predicting stock price trends. Existing works in financial sentiment analysis have not adequately considered the impact of stock prices or market feedback on sentiment…

- **[AFABench: A Generic Framework for Benchmarking Active Feature Acquisition](https://arxiv.org/abs/2508.14734)**
  - *Valter Schütz, Han Wu, Reza Rezvan et al.*
  - **KDD 2025** · `2025-08-20`
  - In many real-world scenarios, acquiring all features of a data instance can be expensive or impractical due to monetary cost, latency, or privacy concerns. Active Feature Acquisition (AFA) addresses this challenge by dynamically selecting a subset of informative features for each…


### ACL

- **[Shape-Aware Three-Way Merge for RDF Knowledge Graphs: The schema defines the conflict: an implementation and evaluation](https://arxiv.org/abs/2611.34870v1)**
  - *Steve Brown*
  - **ACL** · `2026-11-25`
  - Merging RDF serializations creates ordering conflicts and misses semantic ones. We describe and evaluate a three-way merge in which the schema defines a conflict: set algebra combines canonical triples, and a slot is contended only where a SHACL shape bounds its cardinality and b…

- **[AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading](https://arxiv.org/abs/2510.14264)**
  - *Zheye Deng, Wei-Xiang Yan, Chang-Long Yu et al.*
  - **ACL 2025** · `2025-10-16`
  - While Large Language Model (LLM) agents show promise in automated trading, they still face critical limitations. Prominent multi-agent frameworks often suffer from inefficiency, produce inconsistent signals, and lack the end-to-end optimization required to learn a coherent strate…

- **[Reasoning RAG via System 1 or System 2: A Survey on Reasoning Agentic Retrieval-Augmented Generation for Industry Challenges](https://arxiv.org/abs/2506.10408)**
  - *Jin-Tao Liang, Gang Su, Hui-Feng Lin et al.*
  - **ACL 2025** · `2025-06-12`
  - Retrieval-Augmented Generation (RAG) has emerged as a powerful framework to overcome the knowledge limitations of Large Language Models (LLMs) by integrating external retrieval with language generation. While early RAG systems based on static pipelines have shown effectiveness in…

- **[EFSA-CLC: Enhancing Zero-shot Entity-level Financial Sentiment Analysis with Cross-lingual Collaboration](https://aclanthology.org/2025.ijcnlp-long.160.pdf)**
  - *Sen-Bin Zhu, Hong-De Liu, Chen-Yuan He et al.*
  - **ACL 2025**
  - Entity-level sentiment analysis is becoming increasingly important in the context of diverse financial texts, and large language models demonstrate significant potential under zero-shot settings. While it is well recognized that different languages embody distinct cognitive patte…


### Other / arXiv

- **[StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation](https://arxiv.org/abs/2611.34290)**
  - *Modi Jin, Xuying Zhang, Yijing Guo et al.*
  - 🤗 Featured · `2026-11-25`
  - Modern video foundation models generate high-quality short clips, but preserving long-video consistency and correctly depicting event-driven state changes remain challenging. Existing agentic workflows face these challenges because continual planning and repair accumulate context…

- **[Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation](https://arxiv.org/abs/2611.32238)**
  - *Kaipeng Fang, Yuhao Wang, Ji Zhang et al.*
  - 🤗 Featured · `2026-11-24`
  - Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, whi…

- **[Pretrained Tabular Features and the Measurement of Financial Proximity](https://arxiv.org/abs/2611.31491)**
  - *Marcus Gawronsky*
  - 🤗 Featured · `2026-11-23`

- **[LoopTitan: What Does Parameter Revisit Buy a Mixture-of-Experts?](https://arxiv.org/abs/2611.34821)**
  - *Zichen Tian, Yudong Lu, Xuansheng Wu et al.*
  - 🤗 · `2026-11-25`
  - Looped Mixture-of-Experts (MoE) architectures revisit layer parameters across depths. This design increases effective depth without adding parameters. Recent looped MoE studies report substantial gains over the standard MoE at matched budgets (parameters, FLOPs and KV cache). How…

- **[DosePET: An Open-Source Dataset with 2100 Radiation Dose Maps for PET/CT](https://arxiv.org/abs/2611.34008v1)**
  - *Eleftherios Tzanis, Antonios Tzortzakakis, Michail E. Klontzas*
  - `2026-11-25`
  - Large collections of three-dimensional radiation dose maps linked to patient anatomy are needed to develop artificial intelligence (AI) models for personalized internal dosimetry in nuclear medicine, but access to such data remains limited. Here we present DosePET, an open-source…

- **[AI Buckingham: Agentic Discovery of Dimensionless Scaling Laws Across Physical Regimes](https://arxiv.org/abs/2611.33961v1)**
  - *Ao Cheng, Lei Zhang, Guowei He*
  - `2026-11-25`
  - Classical dimensional analysis defines admissible dimensionless representations but does not determine which combinations capture the dominant physical dependence, whether it changes across physical regimes, or when dependent-variable rescaling is required. We present AI Buckingh…

- **[What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench](https://arxiv.org/abs/2611.33943v1)**
  - *Haozhe Zhang, Zhen Long*
  - `2026-11-25`
  - Agent skills are directories of instructions, reference materials, and scripts loaded on demand by coding agents. According to SkillsBench, although human-curated skills can raise the passing rate by about 16.6 percentage points (pp) on average, they have actually reduced the res…

- **[ExtractBench Pro: The Long Tail of Document Extraction](https://arxiv.org/abs/2611.33791v1)**
  - *Boyang Zhang, Justin Xu, Adrian Lyjak et al.*
  - `2026-11-25`
  - We present ExtractBench Pro, a schema-guided document extraction benchmark that tests six challenging modes of extraction underrepresented in existing datasets. It is created following a framework for synthetic document generation, in which deterministic document generators assem…

- **[Controllable CAD Generation and Interactive Editing of Fluid Rotors](https://arxiv.org/abs/2611.33617v1)**
  - *Shen Chen, Lei Li, Jiajun Sun et al.*
  - `2026-11-25`
  - Computer-aided design (CAD) provides the geometric foundation for rotors in fluid rotating machinery. However, creating models for different rotors requires different modeling processes, making it difficult to control geometry through design intent and reuse existing models. We i…

- **[The Detour Is the Danger: Preserving Security During LLM Agent Recovery](https://arxiv.org/abs/2611.33605v1)**
  - *Boyang Ma, Jinku Li, Hao Wu et al.*
  - `2026-11-25`
  - LLM agents increasingly rely on external tools and reusable Skills to execute complex workflows, autonomously replanning when operations fail. However, such recovery may preserve task functionality while silently discarding the security protections required by the original workfl…

- **[Normalizing Flows are Capable World Models](https://arxiv.org/abs/2611.33872v1)**
  - *Zijia Li, Yong-Hyun Park, Shusheng Yang et al.*
  - `2026-11-25`
  - A world model lets an agent anticipate the consequences of its actions and use imagined futures to make decisions. We introduce Normalizing-Flow World Model (NFWM), which pairs an invertible observation encoder with an action-conditioned probabilistic predictor. Because the encod…

- **[Failure Broadens, Success Sharpens: Continual Adaptation of Tool-Use Agents Across Diverse Tasks with Dual-Polarity Memory](https://arxiv.org/abs/2611.33612v1)**
  - *Tianmai M. Zhang, Hoda Shajari, Amr Hendy et al.*
  - `2026-11-25`
  - Large language model agents can self-improve over time by utilizing procedural memory derived from prior task trajectories, yet the distinct utilities of memories derived from local successes and failures remain underexplored. This work studies this question in a realistic settin…

- **[CHD-Bench: Diagnosing Congenital Heart Disease through Interactive Examination](https://arxiv.org/abs/2611.33775v1)**
  - *Gautham Krishnan P, Shrisharanyan Vasu, Aniketh Vijesh et al.*
  - `2026-11-25`
  - Diagnosis of congenital heart disease (CHD) requires understanding the spatial relationships between cardiac structures, which clinicians assess by scrolling through CT or cardiac magnetic resonance imaging (MRI) slices and rotating 3D reconstructions. Although automated methods…

- **[Routeability Before Routing: Routeability Audit Protocol (RAP) and RouteabilityBench for Audited LLM Model Selection](https://arxiv.org/abs/2611.34825v1)**
  - *Yihang Lu, Denica Kjorvezir, Ana Gjorgjevikj et al.*
  - `2026-11-25`
  - LLM routing aims to choose, for each prompt, which model in a portfolio is most likely to answer correctly. This only makes sense when the benchmark contains enough prompt-specific variation for different models to be best on different inputs. On coarse-scored LLM benchmarks, how…

- **[From Prediction to Decision: Decision-Focused Fine-Tuning of Autoregressive Tabular Transformers for Cost-Sensitive Financial Events](https://arxiv.org/abs/2611.34858v1)**
  - *Ashkan Golgoon, Giacomo Domeniconi, Samuel Atkins et al.*
  - `2026-11-25`
  - Autoregressive transformers trained on tokenized tabular event streams are a simple and strong baseline for predicting financial events such as fraud. Yet institutions do not act on probabilities; they act on decisions whose consequences are asymmetric and heteroscedastic: the co…

- **[Nepali Currency Denomination Classification Using Convolutional Neural Networks (CNNs) and MobileNetV2: An Experimental Comparison](https://arxiv.org/abs/2611.33713v1)**
  - *Sakar Lamichhane, Sandesh Bhatta, Aayush Adhikari et al.*
  - `2026-11-25`
  - Automated currency denomination recognition is a computer vision task with applications in cash handling, financial technology, and assistive systems. This study classifies seven Nepali currency denominations (Rs. 5, 10, 20, 50, 100, 500, and 1,000) using three configurations: a…

- **[Self-supervised Clipped-objective Reinforcement Leaning Framework for Risk-aware Portfolio Management](https://arxiv.org/abs/2611.33652v1)**
  - *Zongshen Mu*
  - `2026-11-25`
  - Portfolio management involves balancing diverse financial assets, a critical yet challenging task in quantitative trading. Although deep reinforcement learning has emerged as an active research domain for solving complex sequential decision-making problems over the past decade, d…

- **[PURA: Video Token Pruning via Unified Spatiotemporal Redundancy Assessment](https://arxiv.org/abs/2611.34521v1)**
  - *Yuyao Sun, Hongli Yuan, Shuang Li et al.*
  - `2026-11-25`
  - Video large language models incur substantial inference costs from long visual token sequences. Existing video token compression methods mitigate these costs by exploiting spatial redundancy within frames and temporal redundancy across frames. However, many approaches impose pred…

- **[Node Differential Privacy via Node-Stable Graph Projections](https://arxiv.org/abs/2611.33672v1)**
  - *Ishaq Aden-Ali, Adam Sealfon, Adam Smith et al.*
  - `2026-11-25`
  - Node-differentially private algorithms enable learning on network-structured datasets in which records reflect interactions among individuals. They protect the privacy of each individual's information, including all their associated records. A key challenge in the design of such…

- **[Modelling and Calibration of Climate-Related Credit Risk Under the Emissions Trading System](https://arxiv.org/abs/2611.34771v1)**
  - *Ying Liao, Ankush Agarwal*
  - `2026-11-25`
  - Emission trading systems (ETSs) price a growing share of global emissions, and some of their caps are set to reach zero within the maturity of corporate debt. We develop a structural model in which firms choose their emissions from several energy sources under an anticipated carb…

- **[Efficient Data Fusion in Distributionally Robust Optimization](https://arxiv.org/abs/2611.34495v1)**
  - *Buse Şen, Aras Selvi, Jean Pauphilet et al.*
  - `2026-11-25`
  - Decisions under uncertainty increasingly rest on fragmented evidence, such as samples from related but different populations, privacy-protected summary statistics, or complementary statistical descriptions of the same data. Distributionally robust optimization (DRO) can fuse such…

- **[Rank-size analysis of optimal portfolio weights with a reverse-engineering application](https://arxiv.org/abs/2611.34171v1)**
  - *Roy Cerqueti, Francesco Cesarone, Alessio Di Paolo et al.*
  - `2026-11-25`
  - This paper investigates the shape of optimal portfolio weights using rank-size analysis. We consider four portfolio selection models: Global Minimum-Variance (GMV), minimum-CVaR, Risk Parity (RP), and the Most Diversified Portfolio (MDP). For each model, we fit seven rank-size sp…

- **[Hybrid AI for AI-Native RAN Control: A Functional Perspective](https://arxiv.org/abs/2611.33035v1)**
  - *Sabrine Aroua, Osama Arouk, Pegah Alizadeh*
  - `2026-11-24`
  - AI-native radio access network (RAN) control involves interdependent decisions across network entities, protocol layers, and timescales. Understanding how AI and conventional methods can jointly support these decisions requires a common basis for comparing their functional roles.…

- **[Economic World Model](https://arxiv.org/abs/2611.32663v1)**
  - *Qirui Mi, Yujia Ming, Bo Li et al.*
  - `2026-11-24`
  - Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions? To answer this question, we define an economic world model (EWM) as an agent's internal representation of how an econo…

- **[Marketing-Bench: Evaluating Frontier Models and Agents on Real-World Marketing Capabilities](https://arxiv.org/abs/2611.32012v1)**
  - *Sumanth Balaji, Siddharth Gupta, Ameet Deshpande et al.*
  - `2026-11-24`
  - As frontier AI models and agents are deployed more broadly in the real world, marketing is emerging as one of their largest applications. Marketing teams use AI models to produce brand assets like website copy and social media posts, while consumers' agents autonomously discover…

- **[Coding4Games: Can Modern Coding Agents Play Modern Video Games?](https://arxiv.org/abs/2611.31974v1)**
  - *Shifang Zhao, Haoyu Wang, Yuyang Yin et al.*
  - `2026-11-24`
  - Games, especially modern AAA games, challenge language models to perceive complex scenes, control actions, and make decisions over long horizons. Existing game benchmarks primarily test language models as computer-use agents that query a language model throughout play, incurring…

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

- **[Building a Unified Inline Code Editing Model for GitHub Copilot](https://arxiv.org/abs/2611.33314v1)**
  - *Microsoft CodeAI Team, Microsoft VS Code Team, Julia Gong et al.*
  - `2026-11-24`
  - AI-assisted coding ranges from fully agentic coding to inline code suggestions in the editor. Inline suggestions require predicting a developer's most likely next edit from an editing session. The next edit may lie at the cursor, in nearby lines, or farther away, and one editing…

- **[MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction](https://arxiv.org/abs/2611.32462v1)**
  - *Yifan Dai, Daili Hua, Bohan Zeng et al.*
  - `2026-11-24`
  - Multi-reference image generation requires a model to preserve the appearance of selected subjects while arranging them according to an instruction. Despite recent progress in reference-based generation and compositional control, reliably organizing selected subjects into the inte…

- **[SwarmLeak: Does Coordination Improve Privacy Attacks on LLM Agents?](https://arxiv.org/abs/2611.31791v1)**
  - *Asma Farajidizaji, Vyas Raina, Vatsal Raina et al.*
  - `2026-11-24`
  - LLM agents increasingly collaborate in group chats while holding tool access to confidential records, which makes the shared chat an attack surface. It remains unclear whether several colluding attackers extract such information more effectively than one. We introduce SwarmLeak,…

- **[Recursive Collective Intelligence: Emergence on an Equal-Budget Ladder in Multi-Agent LLM Systems](https://arxiv.org/abs/2611.32606v1)**
  - *Lixuan He, Shengqu Cai, Fang Wu et al.*
  - `2026-11-24`
  - Large language models increasingly work as teams of agents, and a team is expected to solve problems beyond the reach of any single member. Most evaluations credit a team for outperforming a single agent, without accounting for the additional computation: a team may consume many…

- **[The algorithmic behavioral sink: Modeling the transition to irreversible demographic collapse](https://arxiv.org/abs/2611.32084v2)**
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


---
*Generated 2026-11-27 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
