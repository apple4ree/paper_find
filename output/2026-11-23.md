# Daily Paper Digest — 2026-11-23 (Monday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**294 unique papers** (373 topic-entries — cross-topic papers counted once per category)

---

## Agent  (167)

### AAAI

- **[D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies](https://arxiv.org/abs/2511.16590)**
  - *Sen Chen, Tong Zhao, Yi Bin et al.*
  - **AAAI 2025** · `2025-11-20`
  - Developing intelligent agents capable of operating a wide range of Graphical User Interfaces (GUIs) with human-level proficiency is a key milestone on the path toward Artificial General Intelligence. While most existing datasets and benchmarks for training and evaluating GUI agen…


### NeurIPS

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


### ICLR

- **[HeurekaBench: A Benchmarking Framework for AI Co-scientist](https://arxiv.org/abs/2601.01678)**
  - *Siba Smarak Panigrahi, Jovana Videnović, Maria Brbić*
  - **ICLR 2026** · `2026-01-04`
  - LLM-based reasoning models have enabled the development of agentic systems that act as co-scientists, assisting in multi-step scientific analysis. However, evaluating these systems is challenging, as it requires realistic, end-to-end research scenarios that integrate data analysi…

- **[MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents](https://arxiv.org/abs/2508.21475)**
  - *Xi-Jia Tao, Yi-Hua Teng, Xinxing Su et al.*
  - **ICLR 2025** · `2025-08-29`
  - Existing multimodal browsing benchmarks often fail to require genuine multimodal reasoning, as many tasks can be solved with text-only heuristics without vision-in-the-loop verification. We introduce MMSearch-Plus, a 311-task benchmark that enforces multimodal understanding by re…


### KDD

- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)**
  - *Mahmoud Mohammadi, Yi-Peng Li, Jane Lo et al.*
  - **KDD 2025** · `2025-07-29`
  - The rise of LLM-based agents has opened new frontiers in AI applications, yet evaluating these agents remains a complex and underdeveloped area. This survey provides an in-depth overview of the emerging field of LLM agent evaluation, introducing a two-dimensional taxonomy that or…


### ACL

- **[Learning When to Ask: Advisor-Aware Post-Training for SLM Agents](https://arxiv.org/abs/2611.27443v1)**
  - *Aasheesh Singh, Vishal Vaddina*
  - **ACL** · `2026-11-20`
  - Small language models (SLMs) are increasingly attractive for cheap, high-throughput agentic deployment, but they remain weak at multi-step reasoning and tool use that long-horizon tasks demand. We study how to post-train an SLM to seek advice from a stronger model and act on that…

- **[WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)**
  - *Jialong Wu, Wen-Biao Yin, Yong Jiang et al.*
  - **ACL 2025** · `2025-01-13`
  - Retrieval-augmented generation (RAG) demonstrates remarkable performance across tasks in open-domain question-answering. However, traditional search engines may retrieve shallow content, limiting the ability of LLMs to handle complex, multi-layered information. To address it, we…


### EMNLP

- **[Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents](https://arxiv.org/abs/2502.20073)**
  - *Haochen Sun, Shu-Wen Zhang, Lu-Jie Niu et al.*
  - **EMNLP 2025** · `2025-02-27`
  - Large Language Models (LLMs) based agent systems have made great strides in real-world applications beyond traditional NLP tasks. This paper proposes a new LLM-based Multi-Agent System (LLM-MAS) benchmark, Collab-Overcooked, built on the popular Overcooked-AI game with more appli…


### Other / arXiv

- **[AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](https://arxiv.org/abs/2611.26613)**
  - *Yiyang Du, Yuxuan Kuang, Qitao Zhao et al.*
  - 🤗 Featured · `2026-11-19`

- **[Moving Generality from Model to Modeler: LLM Agents for PHM on a Deployment-Style Benchmark](https://arxiv.org/abs/2611.25252)**
  - *Zhenling Chen, Zhiguo Zeng, Anne Barros*
  - 🤗 Featured · `2026-11-18`

- **[Intent Contracts: Taking Tools Away from Agents](https://arxiv.org/abs/2611.24025)**
  - *Ziyuan Wang, Genliang Zhu, Xiaobo Chen et al.*
  - 🤗 Featured · `2026-11-18`

- **[Potential emergence in LLM agents: a statistical physics perspective](https://arxiv.org/abs/2611.27618)**
  - *Zhuo-Yang Song, Hua Xing Zhu*
  - 🤗 · `2026-11-20`
  - There has been significant recent interest in understanding the behaviour of LLM agents from the perspective of human preferences or corpus statistics. In this paper we propose agent states as intermediate variables through which post-training can be measured and predicted. From…

- **[Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training](https://arxiv.org/abs/2611.27376)**
  - *Zhen Zhang, Changyi Yang, Xuehai He et al.*
  - 🤗 · `2026-11-20`
  - RL post-training typically produces domain experts that must then be consolidated into one model, and as new experts keep arriving, this consolidation becomes a continual process. Weight merging and multi-teacher on-policy distillation (MOPD) must re-consolidate the whole model w…

- **[Epistemic Guard: Out-of-Process MCP Receipt Proxying, Post-Turn Prose Supervision, and Provenance-Gated Memory for Tool-Using Autonomous Agents](https://arxiv.org/abs/2611.27095)**
  - *Sean Maxwell*
  - 🤗 · `2026-11-20`
  - Language-model agents using the Model Context Protocol (MCP) face three runtime verification gaps: (i) action fabrication, where post-tool prose narrates side effects that failed, timed out, or never ran; (ii) provenance collapse, where unverified model prose or web text enters d…

- **[SKILL.PNG: Learning Agent Skills in Pixel Space](https://arxiv.org/abs/2611.26296)**
  - *Maximilian Seeth, Chengzhi Martin Hu, Marie Kempkes et al.*
  - 🤗 · `2026-11-20`

- **[MedicalRSI: Medical Recursive Self-Improving Agents via Clinical Model-Harness Co-Evolution](https://arxiv.org/abs/2611.26806)**
  - *Ziqing Wang, Hamid Palangi, Lili Zhao et al.*
  - 🤗 · `2026-11-19`

- **[What Helps Language-Model Agents Review Violent Video? A Controlled Comparison with a Human Evidence Reference](https://arxiv.org/abs/2611.26776)**
  - *Mohammed El Amine Mokhtari, Matei Mancas, Virginie Vandenbulcke*
  - 🤗 · `2026-11-19`

- **[PlayCraft: Designing Engaging Games from Agent Play Experience](https://arxiv.org/abs/2611.26624)**
  - *Weihao Cheng*
  - 🤗 · `2026-11-19`

- **[Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)](https://arxiv.org/abs/2611.26553)**
  - *Mengxiao Wang, Mahbub Alam, Kalyan Nakka et al.*
  - 🤗 · `2026-11-19`

- **[SUAF: Spectral Universal Advantage Features for Zero-Shot Policy Improvement](https://arxiv.org/abs/2611.27919v1)**
  - *Huaze Tang, Runqing Miao, Tianren Peng et al.*
  - `2026-11-20`
  - Reward-independent representations enable reinforcement learning agents to reuse knowledge across tasks, but limited representation capacity raises three fundamental questions: what statistical dependence should these representations capture, which components of that dependence s…

- **[Decision Columns as an Index: Interpretable Embeddings for Explainable Entity Matching and Search](https://arxiv.org/abs/2611.27910v1)**
  - *Aadharsh Kannan, Robert Bruckner, Philip A. Bernstein*
  - `2026-11-20`
  - Business data systems must determine whether records refer to the same entity and retrieve records satisfying requests whose decisive properties are implicit. As agents act on these records, both tasks require auditable reasons. Dense embeddings perform well but offer opaque coor…

- **[TEA-Bench-BR: Can Coding Agents Turn a Branching Clinical Specification into Correct Code?](https://arxiv.org/abs/2611.27895v1)**
  - *Marcio Andre de Souza Estevam*
  - `2026-11-20`
  - Coding agents increasingly implement rules written by domain experts, and bugs in such code are silent: it runs and returns a plausible answer. We introduce TEA-Bench-BR, a benchmark built on the Brazilian pathway for early autism (TEA) screening: three fictitious instruments wit…

- **[LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT](https://arxiv.org/abs/2611.27876v1)**
  - *Maximilian Rokuss, Jeya Maria Jose Valanarasu, Alejandro Lozano et al.*
  - `2026-11-20`
  - Every few months, a cancer patient's CT scans decide whether treatment continues. 3D foundation models can now detect, segment, register and track lesions, yet none of them reads the scans as a radiologist does. A radiologist decides which findings are lesions, which are the same…

- **[SLICR: Strategy Logic-Guided Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27865v1)**
  - *Arshia Rafieioskouie, Matthew Lucas, Tzu-Han Hsu et al.*
  - `2026-11-20`
  - Specification-guided reinforcement learning (RL) translates formal specifications of desired behavior of agents into shaped rewards. This paper introduces SLICR, a significant paradigm shift that advances the state of the art to specification-guided RL in adversarial settings und…

- **[Who Grades the Agent? Privilege Separation for Coding-Agent Benchmarks](https://arxiv.org/abs/2611.27860v1)**
  - *Nathan Nour Houlamy, Mattia Favretto, Earlence Fernandes et al.*
  - `2026-11-20`
  - Benchmarks for AI-based coding agents are a staple of the current AI landscape, because they are the leading way to measure the performance of LLMs. Their scores guide business and research decisions. Evaluating coding agents is challenging, since they are able to manipulate thei…

- **[Beyond Self-Critique: Epistemic Convergence Control for Multi-Agent Research Verification](https://arxiv.org/abs/2611.27839v1)**
  - *Chrisantus Eze*
  - `2026-11-20`
  - Multi-agent systems for scientific claim verification increasingly rely on role-structured LLM debate to pressure-test hypotheses. However, when debating agents are instantiated from the same underlying base model, they share identical latent representations, making self-critique…

- **[Search-RSI: Expanding Search Worlds Along Multimodal Agents' Capability Frontier](https://arxiv.org/abs/2611.27780v1)**
  - *Chengchao Lv, Yin Wang, Chunzheng Zhu et al.*
  - `2026-11-20`
  - Multimodal search agents answer knowledge intensive visual questions by grounding them in retrieved evidence, and recent recipes train them on multi hop tasks that are synthesized from knowledge graphs and grown online to keep pace with the agent. These recipes, however, treat th…

- **[QuASAR: Toward an LLM-Assisted Framework for Screening, Prototyping, and Assessing Quantum-Advantage Opportunities in Scientific Computing](https://arxiv.org/abs/2611.27778v1)**
  - *Mark L. Carroll, Jordan A. Caraballo-Vega, Brian P. Powell et al.*
  - `2026-11-20`
  - Identifying scientific computations that could benefit from quantum algorithms requires both domain knowledge and fluency in quantum algorithm design, expertise that rarely resides in one person. We report results from QuASAR, an experimental, two-agent, LLM-driven pipeline inten…

- **[RoSci: Exploring Robustness in Science VLMs](https://arxiv.org/abs/2611.27750v1)**
  - *Junying Wang, Yijin Guo, Yalun Wu et al.*
  - `2026-11-20`
  - Recent advancements in Vision-Language Models (VLMs) enable significant progress in scientific tasks. However, these models are generally assumed to be presented with complete and accurate information, overlooking the challenges of erroneous/missing information in wild scenarios.…

- **[Shared Understanding in Human-AI Teams: Coordination Continuity in Evolving Work](https://arxiv.org/abs/2611.27746v1)**
  - *Siân Lindley, Britta Burlin, Christian Poelitz et al.*
  - `2026-11-20`
  - People are increasingly working with AI agents as part of extended, asynchronous workflows. In these settings, shared access to information does not guarantee a shared basis for action: goals, plans, and roles may persist while their current significance changes. We introduce coo…

- **[Can Vision-Language Models Synthesize Executable Game-Playing Programs?](https://arxiv.org/abs/2611.27741v1)**
  - *Yao Tong, Jiaxin Qi, Dingyu Zhang et al.*
  - `2026-11-20`
  - Recent advances in vision-language models (VLMs) have endowed multimodal agents with increasingly strong visual perception and long-horizon reasoning capabilities, making VLM-based autonomous game playing feasible. Existing game benchmarks primarily evaluate whether an agent can…

- **[MetaRigor: From Agentic Automation to Verifiable End-to-End Meta-Analysis Through Scientific Decision Boundaries](https://arxiv.org/abs/2611.27713v1)**
  - *Yifeng Xie, Chenke Li, Yangshuo Miao et al.*
  - `2026-11-20`
  - Automated meta-analysis requires not only accurate numerical extraction but also the consistent preservation of result identity across stages, including the associated study, comparison, population, outcome, time point, and analysis conditions. We present MetaRigor, an LLM workfl…

- **[Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](https://arxiv.org/abs/2611.27689v1)**
  - *Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan et al.*
  - `2026-11-20`
  - Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, and limited reuse of execution experience. We propose Embodied-Harness, a dual-agent framework that im…

- **[Learning Inside Types: Epistemic Typestates for Safe Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27631v1)**
  - *Lorenzo Bacchiani, Mario Bravetti, Giovanni Pau et al.*
  - `2026-11-20`
  - Type disciplines make programs safe by construction: components checked against each other's types compose into programs that cannot go wrong in the ways the types exclude. Types suit reinforcement learning: a type constrains what an agent may choose, not how it chooses, so the g…

- **[Benchmarks' Last Exam](https://arxiv.org/abs/2611.27622v1)**
  - *James Zhu, Zekki Cat*
  - `2026-11-20`
  - Public benchmarks guide model selection, post-training rewards and claims of progress in artificial intelligence, yet leaderboards report aggregate scores without verifying whether each task's prompt, environment and grader agree on what counts as success. How often that agreemen…

- **[Can Language Models See the Circuit in Pixelated RFIC Passives?](https://arxiv.org/abs/2611.27559v1)**
  - *Jonathan Zhou, Kaushik Sengupta*
  - `2026-11-20`
  - The emergence of inverse-designed, pixelated passives for microwave and millimeter-wave applications has been a major development in the field of RFIC design. These devices, which appear to be QR-code-like in structure, exist in a generalizable, high-dimensional design space that…

- **[Bringing AI Assistance to the Beznau Nuclear Power Plant: A Hierarchical System of LLM Agents for Reactor Monitoring](https://arxiv.org/abs/2611.27556v1)**
  - *Wenqi Zhou, Leonardo Baldo, Edwin Kolbe et al.*
  - `2026-11-20`
  - Beznau Unit 1 in Switzerland, in operation since 1969, is the most experienced nuclear reactor still running worldwide. Five decades of incremental modernization have left its monitoring systems, alarm logs, variable catalogs, technical specifications and investigation reports in…

- **[Fix Where It Fails: Root-Cause-Guided Agentic Harness Optimization for Scene Graph Generation](https://arxiv.org/abs/2611.27529v1)**
  - *Jee Eun Kim, Donghyeon Choi, Sangjune An et al.*
  - `2026-11-20`
  - Scene graph generation (SGG) aims to detect objects in an image and predict the relationships between them. The standard PredCls, SGCls, and SGDet settings show how much performance drops without ground-truth boxes and labels, but not where or why a model fails. Knowing this woul…

- **[From Manufacturing Event Logs to Simulation: Enabling SMEs with Agentic AI for SimPy Simulation Generation](https://arxiv.org/abs/2611.27483v1)**
  - *Richard Reider, Lina Döring, Sebastian Lang et al.*
  - `2026-11-20`
  - High expertise and cost barriers exclude small and medium-sized enterprises from discrete-event simulation (DES). We introduce GenAI4SimPy, a multi-agent framework powered by Qwen 3.6 (27B), an open-weight large language model, that automates end-to-end DES generation from manufa…

- **[ROSWORLD: When Digital Task Competence Meets Physical Execution](https://arxiv.org/abs/2611.27467v1)**
  - *Caoyuan Ma, Wendi Liu, Zhimin Zhang et al.*
  - `2026-11-20`
  - Computer-use agents now solve most desktop tasks through direct software input, but a robot using the same computer must turn GUI knowledge into physical contact with a keyboard and mouse. We introduce ROSWorld, a benchmark that couples a physically simulated robot workstation to…

- **[TrojanMaxxing: One-shotting VLM Backdoors with Weight-Space Programming](https://arxiv.org/abs/2611.27425v1)**
  - *Ahaan Dabholkar, Harshvardhan Patel, Michalis Polychronakis et al.*
  - `2026-11-20`
  - Recent work shows that large language models (LLMs) can reason directly about the weights of other neural networks. Given only a natural-language objective, an LLM can inspect a model's weights, understand what they compute, and edit them directly without gradient-based optimizat…

- **[Evidence sufficiency assessment enables cost-effective review allocation in on-premise clinical AI agents](https://arxiv.org/abs/2611.27390v1)**
  - *Yiwen Qiu, Che Sun, Shu Shen et al.*
  - `2026-11-20`
  - On-premise clinical AI agents must auto-accept high-confidence diagnoses, deferring others to clinician review, yet token probabilities and self-reported confidence miss errors, while more reliable five-run consistency incurs fivefold compute. We propose training-free decision-po…

- **[VMSA: Video Memory Skill Agent for Long Video Understanding](https://arxiv.org/abs/2611.27381v1)**
  - *Changin Choi, Jungwon Park, Jungmin Ko et al.*
  - `2026-11-20`
  - Long-video question answering requires retrieving and integrating relevant evidence from videos spanning hours or even days. Recent agentic approaches organize video information into external memories and iteratively retrieve evidence to answer questions. However, effective retri…

- **[Testing for Coordination Failures in Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27368v1)**
  - *Dennis Gross, Jørn Eirik Betten, Helge Spieker*
  - `2026-11-20`
  - Deep parallel cooperative multi-agent reinforcement learning (CMARL)} trains multiple agents that all act at every time step to optimize a common objective. Like single-agent RL, CMARL can produce unsafe behaviors that violate implicit safety requirements not captured by the rewa…

- **[$γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence](https://arxiv.org/abs/2611.27306v1)**
  - *Xiaotao Zhang, Lin Qian, Hao Zhang et al.*
  - `2026-11-20`
  - Recent embodied agents construct and adapt robot behavior through executable programs, tool use, and interaction feedback. Studying these systems in mobile manipulation calls for physical worlds that connect agent-directed execution with its physical consequences and reusable int…

- **[HookEvo: A Framework for Coordinated Plugin Evolution on Hook-Enabled Agent Runtimes](https://arxiv.org/abs/2611.27294v1)**
  - *Shengze Huang, Yanyu Mao, Xiaofei Yu et al.*
  - `2026-11-20`
  - Repairing failures in tool-using agents can require coordinated changes to how the harness interprets tool receipts, assembles context, and checks actions. We introduce HookEvo, a framework that uses an existing agent runtime's lifecycle hooks to evolve task-specific harnesses. W…

- **[Belief-State Management Meets Rubric Rewards for Agentic Forecasting](https://arxiv.org/abs/2611.27286v1)**
  - *Jingyi Chai, Yun Liao, Hao Lu et al.*
  - `2026-11-20`
  - Current large language model (LLM) agents still struggle to forecast real-world events. This stems from two primary limitations: i) standard ReAct harness accumulates reasoning and evidence within one growing context, and ii) outcome-based rewards in forecasting lead to a slow an…

- **[Bel: Step-Level Policy Improvement of Visual Agents Without Training](https://arxiv.org/abs/2611.27222v1)**
  - *Jiajun Fan, Ziwen Wang, Zhaoyu Zhu et al.*
  - `2026-11-20`
  - A visual agent acts on what it sees: it taps and types on a screen, or points on a camera image to show a robot where to act. One wrong step can fail its task, yet the right action is often among its own samples, passed over by its greedy decode. Choosing it is a visual judgment,…

- **[NavTTT: Adaptive Parametric Memory via Hierarchical Test-Time Training for Vision-and-Language Navigation](https://arxiv.org/abs/2611.27219v1)**
  - *Xiaoyu Luo, Chengxing Lin, Jiaxin Huang et al.*
  - `2026-11-20`
  - Vision-and-language navigation (VLN) demands that agents accumulate and reason over streaming visual observations throughout long navigation episodes. Existing approaches struggle to maintain long-term history, constrained by the finite context capacity of transformer architectur…

- **[Correct Precedents Induce Policy Violations in On-Device LLM Agents](https://arxiv.org/abs/2611.27216v1)**
  - *Chong Tian, Yu Wang, Steve Liu et al.*
  - `2026-11-20`
  - Local-cloud agent systems pair a cloud model with a small on-device agent that acts on private data, often as the last check before an irreversible action. We identify, for the first time, a failure in which such an agent is led into a violation by its own correct decisions withi…

- **[EDAGoat: An EDA-Aware Agent for Project-Level GPU Optimization](https://arxiv.org/abs/2611.27196v1)**
  - *Chengxi Li, Liang Xiao, Yutao Wang et al.*
  - `2026-11-20`
  - GPU acceleration has transformed electronic design automation (EDA), yet further improving expert-engineered GPU tools still demands substantial manual effort. Automating this work calls for coding agents that can trace bottlenecks across host and device code while preserving cor…

- **[From Acting to Learning: Experience Selection toward Continually Learning Agents](https://arxiv.org/abs/2611.27159v1)**
  - *Yaoyuan Yan, Haoxiang Jie, Zhiyou Heng et al.*
  - `2026-11-20`
  - Successful agent interactions provide training data, but success alone does not determine which records a student should learn from. We examine experience selection for a 4B language agent as a component of continual agent learning. Nine selectors are compared across two fixed ex…

- **[Co-Evolving Behavioral Agents and Detectors for Adaptive Information Operations](https://arxiv.org/abs/2611.27156v1)**
  - *Lin Tian, Marian-Andrei Rizoiu*
  - `2026-11-20`
  - Detectors of state-sponsored information operations (IOs) are trained on campaigns that platforms have already taken down. They lose much of their accuracy on an actor they have not seen, even though no operator in the archived data is trying to avoid them. A real operator wants…

- **[Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material](https://arxiv.org/abs/2611.27139v1)**
  - *Jinxiang Xie, Xinyi Zhang, Changjiang Jiang et al.*
  - `2026-11-20`
  - Multi-agent LLM systems increasingly divide long tasks among subagents whose reports a senior agent turns into the final answer. Such a division of labor pays off only if each agent, and above all the senior agent, carries out the duties of its role. Current evaluations, however,…

- **[Double counting in LLM evidence fusion: exact posteriors separate rule compliance from posterior gain](https://arxiv.org/abs/2611.27138v1)**
  - *Tengfei Shao, Asma Rezaei, Ali Reza Kamali*
  - `2026-11-20`
  - Language models fuse reports in retrieval, multi-agent consensus and agent memory, where treating shared-source reports as independent can double count evidence. A common remedy is an instruction to count each source once. Its value depends on the receiver's raw baseline. Pricing…

- **[CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?](https://arxiv.org/abs/2611.27116v1)**
  - *Chuan Xiao, Baojie Wang, Haizhao Fan et al.*
  - `2026-11-20`
  - The performance of an LLM agent depends on both its model and its harness, the code that mediates its interaction with tools and environments. Can LLM researchers drive this co-evolution as a recursive improvement process, deciding round after round which component to change when…

- **[Separating Automation Gains from Agent Contributions in AI-Assisted Model Validation](https://arxiv.org/abs/2611.27094v1)**
  - *M. Ahmadi Achachlouei*
  - `2026-11-20`
  - LLM agents are being proposed for bank model validation, yet evaluations that compare agent-assisted work with manual practice credit the agent with gains that come from digitized evidence and deterministic tests. We propose a staged architecture in which an LLM-free controlled w…

- **[Exercised, Rarely Recovered: What Public Reports Say About Recovery in 50 AI Agent Harnesses and Runtimes](https://arxiv.org/abs/2611.27090v1)**
  - *Kaviru Hapuarachchi*
  - `2026-11-20`
  - When an AI coding agent deletes the wrong files or a long agent run crashes, users fall back on recovery mechanisms: resume from a checkpoint, undo, ask for approval, read the log. Research runtimes promise stronger guarantees, such as saga-style compensation and transactional ro…

- **[Weight-space programming and mechanistic interpretability for model editing in particle physics](https://arxiv.org/abs/2611.27079v1)**
  - *Raphaël Bonnet-Guerrini, Johann Ioannou-Nikolaides, Troels Petersen*
  - `2026-11-20`
  - We demonstrate that weight-space programming and edits guided by sparse autoencoders can remove unwanted aspects of a particle-physics foundation model through direct edits to its weights. In a foundation model trained on jets, we observe that adding a single soft neutral particl…

- **[Decision Models Are General-Purpose Process Reward Models](https://arxiv.org/abs/2611.27068v1)**
  - *Jiajun Fan, Qinglong Zheng, Ziwen Wang et al.*
  - `2026-11-20`
  - Reinforcement learning (RL) from verifiable outcomes gives a language agent one reward per episode: every step is credited alike, and nothing about the task is learned when all rollouts fail. The last mile, step-level credit, usually requires step labels, a learned critic, costly…

- **[Actions Speak Louder than Words: Stateful Privacy Sniffing of LLM Agents via Behavioral Covert Channels in Web Interactions](https://arxiv.org/abs/2611.27046v1)**
  - *Ruichao Liang, Wenzhong Deng, Jing Chen et al.*
  - `2026-11-20`
  - LLM agents increasingly rely on Web interaction, issuing searches, following links, and reading pages, to complete complex user tasks. Since each action is driven by the agent's private context, including the user's prompt, dialogue history, memory, and connected data, it also op…

- **[From Letter-of-Credit Requirements to Executable Specifications: Evaluating Verification Accuracy and Completeness](https://arxiv.org/abs/2611.26988v1)**
  - *Ji Sub Choi, Whan Choi, Seo Yeon Gu et al.*
  - `2026-11-20`
  - In letter-of-credit (LC) document examination, a correct final decision does not show that every requirement was examined. We therefore evaluate examination requirement by requirement and make each requirement executable. A language model converts the bill of lading (BL) and comm…

- **[Privacy Protection in Self-Evolving Personal Agents: Persistent Memory and Cross-Carrier Transfer](https://arxiv.org/abs/2611.26983v1)**
  - *Zibin Lin, Taotao Wang, Shengli Zhang*
  - `2026-11-20`
  - Personal agents carry private experience into later decisions through persistent memory. This thematic survey compares memory admission, maintenance, release, and withdrawal by protected change, observer, and validation setting. Direct evidence in the screened corpus comes from c…

- **[Contexture: Runtime Context Eviction for High-Throughput Agent Serving](https://arxiv.org/abs/2611.26980v1)**
  - *Colin Hong, Bryan Shan, Wei Siong Pang et al.*
  - `2026-11-20`
  - LLM agents such as Hermes, OpenClaw, and Codex repeatedly resend growing execution histories, increasing shared GPU key-value (KV) cache demand in high-bandwidth memory (HBM). We show that shared KV capacity limits agent-serving throughput. Existing context-reduction methods lack…

- **[Keep the Process, Change the Supplier: Runtime Governance for Tool-Using AI Agents](https://arxiv.org/abs/2611.26966v1)**
  - *Deepak Waghmare, Shaad Sufi*
  - `2026-11-20`
  - Tool-using AI agents propose actions whose authorization and external effects cannot be inferred from generated text alone. We study an execution boundary that separates agent proposals from business-controlled authority, context disclosure, and supplier selection. The Open Proce…

- **[Tracking and Limiting Unsupported Claim Propagation in Multi-Agent LLM Systems: A Provenance-Aware Framework](https://arxiv.org/abs/2611.26957v1)**
  - *Zijia Cao, Hanqing Dou*
  - `2026-11-20`
  - This research examines how unsupported claims change as they move through multi-agent pipelines. It also examines whether preserving provenance can reduce these changes. We test both homogeneous and heterogeneous pipelines. Homogeneous pipelines use the same model across agents,…

- **[CodeReviewBench: An Automated Benchmark for Evaluating the Software Factory](https://arxiv.org/abs/2611.26942v1)**
  - *Ashley Zhang, Narmeen Fatimah Oozeer, Aleksandr Zverianskii et al.*
  - `2026-11-20`
  - As AI agents ship more code with minimal human oversight, code review becomes the critical quality-control checkpoint -- but one without a reliable, objective verifier: review quality is nuanced and ultimately a judgment call by the PR author. Existing benchmarks are structurally…

- **[SecretAgent: A Multi-Agent Framework for Privacy Protection against Vision Language Models](https://arxiv.org/abs/2611.26936v1)**
  - *Minda Zhao, Yue Zhang, Mengyu Wang*
  - `2026-11-20`
  - Vision-language models (VLMs) can infer private information from shared images, including locations, personally identifiable information (PII), and personal attributes such as age and sex, even from medical images. Adversarial perturbations can protect such information against bl…

- **[WEIR: Watershed Exploration and Drift-Aware Prefix Shrinkage for Multi-Turn Agent Reinforcement Learning](https://arxiv.org/abs/2611.27570v1)**
  - *Pixel Nomand, Elena Voss, Marcus Hale et al.*
  - `2026-11-20`
  - Multi-turn language model agents often receive only a single binary reward at the end of a long interaction trajectory, making it difficult to separate decisive decisions from routine steps or estimate accurate intermediate values. Prefix-tree methods improve sample efficiency by…

- **[TITAN: DRL-Based Dynamic Scheduling and Resource Allocation for Tactile Internet](https://arxiv.org/abs/2611.27560v1)**
  - *Qingrui Fan, Vineet Gokhale, Jayakrishnan Nair et al.*
  - `2026-11-20`
  - Tactile Internet (TI) applications require ultra-reliable, low-latency tactile communication alongside video traffic. However, tactile Quality of Service (QoS) requirements vary with the interaction context, making fixed resource allocation inefficient. In this paper, we propose…

- **[Neural variational Skyrmions as a topological benchmark: emergent symmetry, precision energies and KAN--MLP comparison](https://arxiv.org/abs/2611.27411v1)**
  - *Koji Hashimoto, Masaki Murata, Gakuto Ogiwara*
  - `2026-11-20`
  - We propose the three-dimensional Skyrme model as a topological benchmark for neural variational methods and construct fully three-dimensional Skyrmions with baryon number $B=1,\ldots,4$ without imposing a symmetry ansatz, with high precision. For $B=2,3,4$, the relaxation of thes…

- **[Multi-Tier Edge Triage: Optimizing Latency for Safe Clinical Agents](https://arxiv.org/abs/2611.26914v1)**
  - *Joshua Broyde, Sarita A. Joshi*
  - `2026-11-20`
  - Deploying generative AI agents in enterprise clinical workflows requires enforcing multi-dimensional safety and compliance policies--preventing HIPAA Protected Health Information (PHI) exposure, maintaining clinical scope-of-practice boundaries, ensuring patient-appropriate readi…

- **[AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering](https://arxiv.org/abs/2611.27734v1)**
  - *Minye Shao, Chenghao Xiao, Xingyue Zhao et al.*
  - `2026-11-20`
  - Foundation-model agents are increasingly extending beyond software engineering (SWE) into autonomous scientific research, where acquiring and integrating domain knowledge remains a critical challenge. Recent industrial advances have increasingly adopted knowledge graphs and ontol…

- **[Alliance Rupture and Repair in Simulating Cognitive Behavioral Therapy Dialogues](https://arxiv.org/abs/2611.27544v1)**
  - *Jian Chai, Yitian Yang, Siqi Liu et al.*
  - `2026-11-20`
  - In cognitive behavioral therapy (CBT), routine work can strain the client-counselor working alliance, and the counselor must then notice the rupture, repair it, and adapt the work that follows. Existing CBT simulators model client resistance and follow structured treatment plans,…

- **[Breaking the Long Horizon: Short-Horizon Process Supervision for Long-Form Generation in LLMs](https://arxiv.org/abs/2611.27348v1)**
  - *Heyang Xu, HanWen Hao, Qianren Mao et al.*
  - `2026-11-20`
  - Long-form generation is increasingly important for agentic LLM systems, yet current reinforcement learning methods typically optimize an entire document with a single outcome-level reward. This delayed and coarse-grained supervision makes it difficult to localize errors and assig…

- **[Do Companies Deliver on Their IPO Claims?](https://arxiv.org/abs/2611.27273v1)**
  - *Vidhyakshaya Kannan, Shiv Banafar, Michael Galarnyk et al.*
  - `2026-11-20`
  - Initial public offering (IPO) filings describe what a company does and what it intends to become. Yet whether individual forward-looking claims are subsequently realized is difficult to assess. We introduce Vision Follow-Through (VFT), a benchmark and agentic pipeline that separa…

- **[A Cognitive Agentic AI Framework for Interactive Process Analysis and Optimization](https://arxiv.org/abs/2611.27725v1)**
  - *Trung Ngoc Trinha, Roman Tschentscher, Trong Dong Nguyen et al.*
  - `2026-11-20`
  - Complex multivariable process analysis and optimization require coordinated access to simulation, structured data, machine learning (ML), optimization, and scientific literature, often across disconnected software tools. We present a Cognitive Agentic AI Framework (CAAF) that ena…

- **[Epistemic Social Learning: Latent Behavioral Structure under Endogenous Multi-Agent Interaction](https://arxiv.org/abs/2611.27545v1)**
  - *Jainendra Shukla, Dhruv Jaiswal, Divyanshi Beniwal et al.*
  - `2026-11-20`
  - In multi-agent interaction, a learner's actions shape the observations from which it infers other agents' behavior. A behavioral model may predict these observations well yet support poor adaptation when opponents change. We introduce Epistemic Social Learning (ESL), which couple…

- **[Where Delay Compensation Belongs in a Decentralized Mean-Field-Game Swarm with a Control-Barrier Safety Filter](https://arxiv.org/abs/2611.27540v1)**
  - *Jan Mikołajczyk, Igor Rostkowski, Bartosz Ogórkiewicz et al.*
  - `2026-11-20`
  - Large robot teams are often run as a plan-then-execute stack. We study a decentralized instance for drone swarms, a mean-field-game (MFG) routing field with a per-agent control-barrier-function (CBF) safety filter, when communication is limited by a shared TDMA channel. Neighbors…

- **[Communication-constrained multiagent risk estimation: a simulation benchmark for adult sore throat](https://arxiv.org/abs/2611.27468v1)**
  - *Anas H. Alzahrani*
  - `2026-11-20`
  - Distributed predictive agents may need to approach a shared estimate under limited, unreliable communication. We evaluated classical symmetric pairwise gossip among five agents initialized from frozen calibrated predictions in a synthetic adult sore-throat benchmark. Ninety runs…

- **[OpenRing: Deadlock-Free Execution of Any Planner on AGV Floors with One-Way Lanes](https://arxiv.org/abs/2611.27127v1)**
  - *Zhihao Lin, Anh-Tu Nguyen, Hui Zhang et al.*
  - `2026-11-20`
  - Lifelong multi-agent path finding replans routes for automated guided vehicles, but deviations can invalidate a plan. With one-way lanes, a late vehicle or lost planner can close a ring of full segments. We separate how fast the floor runs from whether it keeps running. In OpenRi…

- **[Omo: Giving Continuing AI-Agent Work a Place to Return To](https://arxiv.org/abs/2611.27107v1)**
  - *Kaviru Hapuarachchi, Harrison Edwards*
  - `2026-11-20`
  - AI coding agents now keep working while the people who started them are away. Coming back is the hard part: a session list tells you which agent is where, but not what it was asked to do, what it changed, or what to tell it next. We present Omo, which gives each piece of continui…

- **[Risk sharing for background risk models with infinite mean](https://arxiv.org/abs/2611.27485v1)**
  - *Ziting Miao, Yuyu Chen, Han Li*
  - `2026-11-20`
  - Risk sharing is usually viewed as beneficial for risk-averse agents facing independent risks with finite means, but this situation can be reversed for infinite-mean losses. In this paper, we explore the effects of risk sharing for positively dependent infinite-mean losses using b…


## Harness  (86)

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

- **[FinBench: A Benchmarking Framework for Stock Market Prediction and Portfolio Allocation](https://doi.org/10.1145/3770855.3817595)**
  - *Sara Pederzoli, Marta Santacroce, Francesco Guerra et al.*
  - **KDD 2026** · `2026-08-09`
  - Research on stock market prediction relies on public datasets to develop and compare learning-based models. However, existing datasets are often limited to price-based information, cover a restricted set of assets or time periods, or provide only a subset of the heterogeneous sig…

- **[IdeaBench: Benchmarking Large Language Models for Research Idea Generation](https://dl.acm.org/doi/pdf/10.1145/3711896.3737419)**
  - *Si-Kun Guo, Amir Hassan Shariatmadari, Guang-Zhi Xiong et al.*
  - **KDD 2025** · `2025-08-03`
  - Large Language Models (LLMs) have revolutionized interactions between human and artificial intelligence (AI) systems, demonstrating state-of-the-art performance across various domains, including scientific discovery and hypothesis generation. However, the absence of a comprehensi…


### ACL

- **[Learning When to Ask: Advisor-Aware Post-Training for SLM Agents](https://arxiv.org/abs/2611.27443v1)**
  - *Aasheesh Singh, Vishal Vaddina*
  - **ACL** · `2026-11-20`
  - Small language models (SLMs) are increasingly attractive for cheap, high-throughput agentic deployment, but they remain weak at multi-step reasoning and tool use that long-horizon tasks demand. We study how to post-train an SLM to seek advice from a stronger model and act on that…


### EMNLP

- **[Skeleton-Guided-Translation: A Benchmarking Framework for Code Repository Translation with Fine-Grained Quality Evaluation](https://arxiv.org/abs/2501.16050)**
  - *Xinglian Zhang, Jiaheng Wen, Fangkai Yang et al.*
  - **EMNLP 2025** · `2025-01-27`
  - The advancement of large language models has intensified the need to modernize enterprise applications and migrate legacy systems to secure, versatile languages. However, existing code translation benchmarks primarily focus on individual functions, overlooking the complexities in…


### Other / arXiv

- **[Hy-MT3: More Accurate, Robust and Practical Multilingual Translation Models in the Wild](https://arxiv.org/abs/2611.27673)**
  - *Mao Zheng, Zheng Li, Fangxu Liu et al.*
  - 🤗 · `2026-11-20`
  - Hy-MT3 is the third generation of the Hunyuan multilingual translation model family, including \textbf{Hy-MT3-1.8B}, \textbf{Hy-MT3-7B} and \textbf{Hy-MT3-30B-A3B (MoE)}. Compared with Hy-MT2, Hy-MT3 translates \textbf{more accurately, more completely and more faithfully to user…

- **[NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation](https://arxiv.org/abs/2611.27499)**
  - *Guangzhao Dai, Guoxin Lian, Shuo Wang et al.*
  - 🤗 · `2026-11-20`

- **[MedicalRSI: Medical Recursive Self-Improving Agents via Clinical Model-Harness Co-Evolution](https://arxiv.org/abs/2611.26806)**
  - *Ziqing Wang, Hamid Palangi, Lili Zhao et al.*
  - 🤗 · `2026-11-19`

- **[LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT](https://arxiv.org/abs/2611.27876v1)**
  - *Maximilian Rokuss, Jeya Maria Jose Valanarasu, Alejandro Lozano et al.*
  - `2026-11-20`
  - Every few months, a cancer patient's CT scans decide whether treatment continues. 3D foundation models can now detect, segment, register and track lesions, yet none of them reads the scans as a radiologist does. A radiologist decides which findings are lesions, which are the same…

- **[Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](https://arxiv.org/abs/2611.27689v1)**
  - *Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan et al.*
  - `2026-11-20`
  - Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, and limited reuse of execution experience. We propose Embodied-Harness, a dual-agent framework that im…

- **[Benchmarks' Last Exam](https://arxiv.org/abs/2611.27622v1)**
  - *James Zhu, Zekki Cat*
  - `2026-11-20`
  - Public benchmarks guide model selection, post-training rewards and claims of progress in artificial intelligence, yet leaderboards report aggregate scores without verifying whether each task's prompt, environment and grader agree on what counts as success. How often that agreemen…

- **[Fix Where It Fails: Root-Cause-Guided Agentic Harness Optimization for Scene Graph Generation](https://arxiv.org/abs/2611.27529v1)**
  - *Jee Eun Kim, Donghyeon Choi, Sangjune An et al.*
  - `2026-11-20`
  - Scene graph generation (SGG) aims to detect objects in an image and predict the relationships between them. The standard PredCls, SGCls, and SGDet settings show how much performance drops without ground-truth boxes and labels, but not where or why a model fails. Knowing this woul…

- **[$γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence](https://arxiv.org/abs/2611.27306v1)**
  - *Xiaotao Zhang, Lin Qian, Hao Zhang et al.*
  - `2026-11-20`
  - Recent embodied agents construct and adapt robot behavior through executable programs, tool use, and interaction feedback. Studying these systems in mobile manipulation calls for physical worlds that connect agent-directed execution with its physical consequences and reusable int…

- **[HookEvo: A Framework for Coordinated Plugin Evolution on Hook-Enabled Agent Runtimes](https://arxiv.org/abs/2611.27294v1)**
  - *Shengze Huang, Yanyu Mao, Xiaofei Yu et al.*
  - `2026-11-20`
  - Repairing failures in tool-using agents can require coordinated changes to how the harness interprets tool receipts, assembles context, and checks actions. We introduce HookEvo, a framework that uses an existing agent runtime's lifecycle hooks to evolve task-specific harnesses. W…

- **[Belief-State Management Meets Rubric Rewards for Agentic Forecasting](https://arxiv.org/abs/2611.27286v1)**
  - *Jingyi Chai, Yun Liao, Hao Lu et al.*
  - `2026-11-20`
  - Current large language model (LLM) agents still struggle to forecast real-world events. This stems from two primary limitations: i) standard ReAct harness accumulates reasoning and evidence within one growing context, and ii) outcome-based rewards in forecasting lead to a slow an…

- **[CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?](https://arxiv.org/abs/2611.27116v1)**
  - *Chuan Xiao, Baojie Wang, Haizhao Fan et al.*
  - `2026-11-20`
  - The performance of an LLM agent depends on both its model and its harness, the code that mediates its interaction with tools and environments. Can LLM researchers drive this co-evolution as a recursive improvement process, deciding round after round which component to change when…

- **[Separating Automation Gains from Agent Contributions in AI-Assisted Model Validation](https://arxiv.org/abs/2611.27094v1)**
  - *M. Ahmadi Achachlouei*
  - `2026-11-20`
  - LLM agents are being proposed for bank model validation, yet evaluations that compare agent-assisted work with manual practice credit the agent with gains that come from digitized evidence and deterministic tests. We propose a staged architecture in which an LLM-free controlled w…

- **[Exercised, Rarely Recovered: What Public Reports Say About Recovery in 50 AI Agent Harnesses and Runtimes](https://arxiv.org/abs/2611.27090v1)**
  - *Kaviru Hapuarachchi*
  - `2026-11-20`
  - When an AI coding agent deletes the wrong files or a long agent run crashes, users fall back on recovery mechanisms: resume from a checkpoint, undo, ask for approval, read the log. Research runtimes promise stronger guarantees, such as saga-style compensation and transactional ro…

- **[Contexture: Runtime Context Eviction for High-Throughput Agent Serving](https://arxiv.org/abs/2611.26980v1)**
  - *Colin Hong, Bryan Shan, Wei Siong Pang et al.*
  - `2026-11-20`
  - LLM agents such as Hermes, OpenClaw, and Codex repeatedly resend growing execution histories, increasing shared GPU key-value (KV) cache demand in high-bandwidth memory (HBM). We show that shared KV capacity limits agent-serving throughput. Existing context-reduction methods lack…

- **[Multi-Tier Edge Triage: Optimizing Latency for Safe Clinical Agents](https://arxiv.org/abs/2611.26914v1)**
  - *Joshua Broyde, Sarita A. Joshi*
  - `2026-11-20`
  - Deploying generative AI agents in enterprise clinical workflows requires enforcing multi-dimensional safety and compliance policies--preventing HIPAA Protected Health Information (PHI) exposure, maintaining clinical scope-of-practice boundaries, ensuring patient-appropriate readi…

- **[A Cognitive Agentic AI Framework for Interactive Process Analysis and Optimization](https://arxiv.org/abs/2611.27725v1)**
  - *Trung Ngoc Trinha, Roman Tschentscher, Trong Dong Nguyen et al.*
  - `2026-11-20`
  - Complex multivariable process analysis and optimization require coordinated access to simulation, structured data, machine learning (ML), optimization, and scientific literature, often across disconnected software tools. We present a Cognitive Agentic AI Framework (CAAF) that ena…

- **[PAVE: A Harness for Geometrically Consistent Road Network Modeling with Vision-Language Models](https://arxiv.org/abs/2611.27352v1)**
  - *Yajun Liu, Jinxi Wu, Juan Pablo Millán Raya et al.*
  - `2026-11-20`
  - Transportation models, whether they simulate traffic or support planning, are only as reliable as the road networks they run on, down to the lanes and turns at each intersection. Practitioners still take such a network from GIS files and supply its junction and movement data by h…

- **[Auditable Financial Knowledge Graphs: Schema-Driven Construction and Intrinsic Quality Evaluation](https://arxiv.org/abs/2611.27835v1)**
  - *Samarth Sarin, Lovepreet Singh, Dhagash Mehta*
  - `2026-11-20`
  - Financial documents combine narrative disclosures, accounting metrics, corporate structures, management commentary, and time-dependent facts, making them difficult to represent using conventional chunk-based retrieval-augmented generation systems. This paper presents an auditable…

- **[FM4SAR-Bench 1.0: Towards A Fair Benchmark for Evaluating Foundation Models for SAR Image Interpretation](https://arxiv.org/abs/2611.27158v1)**
  - *Mingyao Chen, Yongxiang Liu, Tianpeng Liu et al.*
  - `2026-11-20`
  - Foundation models have advanced SAR image interpretation but created a heterogeneous, fragmented model ecosystem. Existing models differ substantially in their input, training data, objectives, architectures, and release policy, yet the field lacks a unified taxonomy and comparat…

- **[Typhoon OCR 2: From Thai Document Transcription to Multilingual, Multi-Task OCR](https://arxiv.org/abs/2611.27494v1)**
  - *Surapon Nonesung, Natapong Nitarach, Sittipong Sripaisarnmongkol et al.*
  - `2026-11-20`
  - Typhoon OCR 1.5 focused on reading Thai documents. However, in real-world workflows, users often need to extract specific information or preserve the structure of an entire page for further processing. Typhoon OCR 2 handles both tasks in a single model, with prompt-driven extract…


## Finance  (120)

### AAAI

- **[D-GARA: A Dynamic Benchmarking Framework for GUI Agent Robustness in Real-World Anomalies](https://arxiv.org/abs/2511.16590)**
  - *Sen Chen, Tong Zhao, Yi Bin et al.*
  - **AAAI 2025** · `2025-11-20`
  - Developing intelligent agents capable of operating a wide range of Graphical User Interfaces (GUIs) with human-level proficiency is a key milestone on the path toward Artificial General Intelligence. While most existing datasets and benchmarks for training and evaluating GUI agen…


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

- **[Multi-Identity Transaction Graph Pretraining for Fraud Detection](https://openreview.net/forum?id=1edqcNjZ3J)**
  - **ICML 2026** · OpenReview · `2026-09-07`
  - Real-world payment risk modeling is constrained by scarce fraud labels and fragmented behavioral context across multiple payment identities. A physical transaction may appear simultaneously in multiple behavioral histories defined by different identities, while each identity indu…

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

- **[Uncertainty Quantification for Language Models: Standardizing and Evaluating Black-Box, White-Box, LLM Judge, and Ensemble Scorers](https://openreview.net/forum?id=HZ7qyXMTlw)**
  - *Dylan Bouchard, Mohit Singh Chauhan*
  - **ICML 2025** · OpenReview · `2025-08-25`
  - Hallucinations are a persistent problem with Large Language Models (LLMs). As these models become increasingly used in high-stakes domains, such as healthcare and finance, the need for effective hallucination detection is crucial. To this end, we outline a versatile framework for…

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

- **[Portfolio Methods in Uncertain Contexts. (Méthodes de portefeuille en contexte incertain)](https://openreview.net/forum?id=UOZdaO3HdK)**
  - *Jialin Liu*
  - **ICML 2026** · OpenReview · `2015-01-01`
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

- **[FinBench: A Benchmarking Framework for Stock Market Prediction and Portfolio Allocation](https://doi.org/10.1145/3770855.3817595)**
  - *Sara Pederzoli, Marta Santacroce, Francesco Guerra et al.*
  - **KDD 2026** · `2026-08-09`
  - Research on stock market prediction relies on public datasets to develop and compare learning-based models. However, existing datasets are often limited to price-based information, cover a restricted set of assets or time periods, or provide only a subset of the heterogeneous sig…

- **[AFABench: A Generic Framework for Benchmarking Active Feature Acquisition](https://arxiv.org/abs/2508.14734)**
  - *Valter Schütz, Han Wu, Reza Rezvan et al.*
  - **KDD 2025** · `2025-08-20`
  - In many real-world scenarios, acquiring all features of a data instance can be expensive or impractical due to monetary cost, latency, or privacy concerns. Active Feature Acquisition (AFA) addresses this challenge by dynamically selecting a subset of informative features for each…


### ACL

- **[Nonlinear Shrinkage for Higher Moments Estimation in Large Portfolios](https://arxiv.org/abs/2611.27274v1)**
  - *Paul Ruelloux, Christian Bongiorno, Damien Challet*
  - **ACL** · `2026-11-20`
  - Portfolio risk is not limited to the variance of returns. The moments of portfolio returns depend directly on the covariance matrix and higher-order co-dependences (coskewness, cokurtosis, etc.). In practice, however, these objects are extremely noisy, especially for large portfo…


### Other / arXiv

- **[RoSci: Exploring Robustness in Science VLMs](https://arxiv.org/abs/2611.27750v1)**
  - *Junying Wang, Yijin Guo, Yalun Wu et al.*
  - `2026-11-20`
  - Recent advancements in Vision-Language Models (VLMs) enable significant progress in scientific tasks. However, these models are generally assumed to be presented with complete and accurate information, overlooking the challenges of erroneous/missing information in wild scenarios.…

- **[$γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence](https://arxiv.org/abs/2611.27306v1)**
  - *Xiaotao Zhang, Lin Qian, Hao Zhang et al.*
  - `2026-11-20`
  - Recent embodied agents construct and adapt robot behavior through executable programs, tool use, and interaction feedback. Studying these systems in mobile manipulation calls for physical worlds that connect agent-directed execution with its physical consequences and reusable int…

- **[Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material](https://arxiv.org/abs/2611.27139v1)**
  - *Jinxiang Xie, Xinyi Zhang, Changjiang Jiang et al.*
  - `2026-11-20`
  - Multi-agent LLM systems increasingly divide long tasks among subagents whose reports a senior agent turns into the final answer. Such a division of labor pays off only if each agent, and above all the senior agent, carries out the duties of its role. Current evaluations, however,…

- **[Keep the Process, Change the Supplier: Runtime Governance for Tool-Using AI Agents](https://arxiv.org/abs/2611.26966v1)**
  - *Deepak Waghmare, Shaad Sufi*
  - `2026-11-20`
  - Tool-using AI agents propose actions whose authorization and external effects cannot be inferred from generated text alone. We study an execution boundary that separates agent proposals from business-controlled authority, context disclosure, and supplier selection. The Open Proce…

- **[Auditable Financial Knowledge Graphs: Schema-Driven Construction and Intrinsic Quality Evaluation](https://arxiv.org/abs/2611.27835v1)**
  - *Samarth Sarin, Lovepreet Singh, Dhagash Mehta*
  - `2026-11-20`
  - Financial documents combine narrative disclosures, accounting metrics, corporate structures, management commentary, and time-dependent facts, making them difficult to represent using conventional chunk-based retrieval-augmented generation systems. This paper presents an auditable…

- **[FM4SAR-Bench 1.0: Towards A Fair Benchmark for Evaluating Foundation Models for SAR Image Interpretation](https://arxiv.org/abs/2611.27158v1)**
  - *Mingyao Chen, Yongxiang Liu, Tianpeng Liu et al.*
  - `2026-11-20`
  - Foundation models have advanced SAR image interpretation but created a heterogeneous, fragmented model ecosystem. Existing models differ substantially in their input, training data, objectives, architectures, and release policy, yet the field lacks a unified taxonomy and comparat…

- **[JevRisk: Zero-Shot Financial Risk Assessment with a Language Decision Model](https://arxiv.org/abs/2611.26999v1)**
  - *Yaodong Yang, Li Huang, Junpeng Liang et al.*
  - `2026-11-20`
  - Banks must monitor every customer's financial risk, such as money laundering and credit default, by interpreting financial activity in the context of the customer's profile. Existing risk monitoring systems of banks are mostly based on expert-designed risk indicators, which apply…

- **[Reward Integrity in Adversarial Reinforcement Learning for LLM Guardrail Red-Teaming](https://arxiv.org/abs/2611.26998v1)**
  - *Chengming Liu, Leon Viti, Hongxu Chen et al.*
  - `2026-11-20`
  - We study reward fidelity in an adversarial reinforcement-learning loop for red-teaming financial-services language-model guardrails. Apparent wins can arise when an attack omits prescribed personally identifiable information (PII), or when a reward judge credits a response that d…

- **[Right Numbers, Wrong Story: When LLMs Narrate Financial Changes Beyond Their Inputs](https://arxiv.org/abs/2611.26968v1)**
  - *Seunghan Lee, Jun Seo, Junhyeok Kang et al.*
  - `2026-11-20`
  - A financial report drafted by an LLM can state every number correctly but still go beyond its input, adding judgments and causes that no one supplied. We call these additions unsupported framing and find them far more often in LLM drafts than in reports written by proInput facts…

- **[A Methodologically Rigorous Benchmark of Linear Regression,RNN, and LSTM for S&P 500 Forecasting:Identifying Sources of Performance Inflation in Financial DeepLearning](https://arxiv.org/abs/2611.27978v1)**
  - *Hari Sitaula, Joseph Opitz*
  - `2026-11-20`
  - This study examines one-day-ahead forecasting of the S&P 500 closing level using a 2006-2025 dataset that includes fundamental price data, macroeconomic indicators, and engineered technical features. We benchmark three model families, namely linear regression, vanilla recurrent n…

- **[Do Econophysics-Inspired Inputs Improve Neural Covariance Forecasting? A Leakage-Free Walk-Forward Study of Intraday DJIA Data](https://arxiv.org/abs/2611.27616v1)**
  - *Gabriele Ranco*
  - `2026-11-20`
  - Tools from econophysics, including Random Matrix Theory (RMT), Tsallis q-Gaussian tails, Hawkes self-excitation and diffusion-inspired regularization, are often proposed as ingredients for financial risk models, but their incremental value over strong contemporary benchmarks rema…

- **[Bottlenecked: The Capital Cost of Protected DeFi Lending](https://arxiv.org/abs/2611.26948v1)**
  - *Tarun Chitra, Manvir Schneider, Nagu Thogiti*
  - `2026-11-20`
  - Securing hundreds of billions of dollars in decentralized finance (DeFi) requires both cryptographically secured collateral and economic capital to absorb losses that collateral alone cannot cover. Composability makes both the amount and location of this protection matter: Kelp's…

- **[Ruby: State-of-the-Art Potency Prediction across Discovery Regimes Using Learned Structural Representations](https://arxiv.org/abs/2611.27015v1)**
  - *Michael Atkin, Dominique Beaini, Jules Berman et al.*
  - `2026-11-20`
  - Small-molecule drug discovery proceeds through repeated design-make-test-analyze cycles. The goal is often to maximize potency while keeping other properties within the ranges required for a viable therapeutic candidate. Compound prioritization places different demands on computa…

- **[Federated and Balanced $k$-means: Communication Efficiency, Privacy, and Heterogeneity](https://arxiv.org/abs/2611.27114v1)**
  - *Feiteng Nie, Shengkun Zhu, Sheng Wang et al.*
  - `2026-11-20`
  - Collaborating on data across organizations in healthcare and finance demands methods that preserve privacy while enabling effective analysis. Vertical Federated Learning (VFL) facilitates clustering across data where different parties hold different features of the same entities…

- **[Risk sharing for background risk models with infinite mean](https://arxiv.org/abs/2611.27485v1)**
  - *Ziting Miao, Yuyu Chen, Han Li*
  - `2026-11-20`
  - Risk sharing is usually viewed as beneficial for risk-averse agents facing independent risks with finite means, but this situation can be reversed for infinite-mean losses. In this paper, we explore the effects of risk sharing for positively dependent infinite-mean losses using b…


---
*Generated 2026-11-23 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
