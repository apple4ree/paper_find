# Daily Paper Digest — 2026-11-19 (Thursday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**541 unique papers** (675 topic-entries — cross-topic papers counted once per category)

---

## Agent  (409)

### AAAI

- **[AgentSwift: Efficient LLM Agent Design via Value-guided Hierarchical Search](https://arxiv.org/abs/2506.06017)**
  - *Yu Li, Lehui Li, Zhi-Hao Wu et al.*
  - **AAAI 2025** · `2025-06-06`
  - Large language model (LLM) agents have demonstrated strong capabilities across diverse domains, yet automated agent design remains a significant challenge. Current automated agent design approaches are often constrained by limited search spaces that primarily optimize workflows b…


### NeurIPS

- **[AgentRecBench: Benchmarking LLM Agent-based Personalized Recommender Systems](https://arxiv.org/abs/2505.19623)**
  - *Yu Shang, Peijie Liu, Yuwei Yan et al.*
  - **NeurIPS 2025** · `2025-05-26`
  - The emergence of agentic recommender systems powered by Large Language Models (LLMs) represents a paradigm shift in personalized recommendations, leveraging LLMs' advanced reasoning and role-playing capabilities to enable autonomous, adaptive decision-making. Unlike traditional r…

- **[Distilling LLM Agent into Small Models with Retrieval and Code Tools](https://arxiv.org/abs/2505.17612)**
  - *Minki Kang, Jongwon Jeong, Seanie Lee et al.*
  - **NeurIPS 2025** · `2025-05-23`
  - Large language models (LLMs) excel at complex reasoning tasks but remain computationally expensive, limiting their practical deployment. To address this, recent works have focused on distilling reasoning capabilities into smaller language models (sLMs) using chain-of-thought (CoT…

- **[Group-in-Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2505.10978)**
  - *Lang Feng, Zheng-Hai Xue, Ting-Cong Liu et al.*
  - **NeurIPS 2025** · `2025-05-16`
  - Recent advances in group-based reinforcement learning (RL) have driven frontier large language models (LLMs) in single-turn tasks like mathematical reasoning. However, their scalability to multi-turn LLM agent training remains limited. Unlike static tasks, agent-environment inter…

- **[Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657)**
  - *Mert Cemri, Melissa Z. Pan, Shuyi Yang et al.*
  - **NeurIPS 2025** · `2025-03-17`
  - Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal. This gap highlights a critical need for a principled understanding of why MAS fail. Addressing this question requires systematic identification and analysis of f…


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

- **[Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](https://arxiv.org/abs/2505.00212)**
  - *Shao-Kun Zhang, Ming Yin, Jie-Yu Zhang et al.*
  - **ICML 2025** · `2025-04-30`
  - Failure attribution in LLM multi-agent systems-identifying the agent and step responsible for task failures-provides crucial clues for systems debugging but remains underexplored and labor-intensive. In this paper, we propose and formulate a new research area: automated failure a…

- **[OrcaLoca: An LLM Agent Framework for Software Issue Localization](https://arxiv.org/abs/2502.00350)**
  - *Zhong-Ming Yu, He-Jia Zhang, Yu-Jie Zhao et al.*
  - **ICML 2025** · `2025-02-01`
  - Recent developments in Large Language Model (LLM) agents are revolutionizing Autonomous Software Engineering (ASE), enabling automated coding, problem fixes, and feature improvements. However, localization -- precisely identifying software problems by navigating to relevant code…

- **[RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](https://arxiv.org/abs/2501.18160)**
  - *Jin-Yao Guo, Cheng-Peng Wang, Xiang-Zhe Xu et al.*
  - **ICML 2025** · `2025-01-30`
  - Code auditing is the process of reviewing code with the aim of identifying bugs. Large Language Models (LLMs) have demonstrated promising capabilities for this task without requiring compilation, while also supporting user-friendly customization. However, auditing a code reposito…


### ICLR

- **[Tree Search for LLM Agent Reinforcement Learning](https://arxiv.org/abs/2509.21240)**
  - *Yuxiang Ji, Zi-Yu Ma, Yong Wang et al.*
  - **ICLR 2025** · `2025-09-25`
  - Recent advances in reinforcement learning (RL) have significantly enhanced the agentic capabilities of large language models (LLMs). In long-term and multi-turn agent tasks, existing approaches driven solely by outcome rewards often suffer from the problem of sparse supervision.…

- **[MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](https://arxiv.org/abs/2507.02259)**
  - *Hong-Li Yu, Ting Chen, Jiang-Tao Feng et al.*
  - **ICLR 2025** · `2025-07-03`
  - Despite improvements by length extrapolation, efficient attention and memory modules, handling infinitely long documents with linear complexity without performance degradation during extrapolation remains the ultimate challenge in long-text processing. We directly optimize for lo…


### ACL

- **[RoboBuilder: Agentic Robot Co-Design with Real-world Video Feedback in the Loop](https://arxiv.org/abs/2611.23855)**
  - *Ghadi Nehme, Dahyun Nam, Akshay Govind Srinivasan et al.*
  - **ACL** · 🤗 · `2026-11-18`
  - Can AI agents design robots that work in the real world? We introduce RoboBuilder, a benchmark in which coding agents co-design a robot's hardware and program from standard parts, motors and a custom 3D-printed part, and every design that passes in simulation is built and tested…

- **[Safe to Omit, Worth Omitting? Keeping the Answer and Cutting Latency When an LLM Agent Skips Another's Message](https://arxiv.org/abs/2611.23570)**
  - *Xinyang Li, Chih-Hsuan Yang, Xiaolong Ma et al.*
  - **ACL** · 🤗 · `2026-11-17`
  - In multi-agent systems, a receiver agent often waits for a helper agent's message (text or its latent KV cache), which can improve performance but adds latency. We study when a receiver agent can skip the message safely (the final answer rarely changes) and beneficially (the time…

- **[Openhagen Worlds: Calibrated Environments for Measuring and Training Scientific Discovery Agents](https://arxiv.org/abs/2611.24711v1)**
  - *Alexander Boesgaard Lorup*
  - **ACL** · `2026-11-18`
  - Agents that do science must choose informative experiments and reason from their results, but most discovery benchmarks cannot separate that skill from recall, unstated scoring rules or shortcut policies. We introduce Openhagen Worlds, a suite of 27 procedurally generated environ…

- **[Reducing Inference Cost of Coding Agents with Timeout Cascades](https://arxiv.org/abs/2611.24324v1)**
  - *Boxi Zhou, German Sviridov, Dmitrii Ustiugov et al.*
  - **ACL** · `2026-11-18`
  - AI coding agents have become one of the most popular applications of large language models. Yet, agentic AI comes at the cost of a tremendous amount of GPU compute resources, which limits its profitability and its viability at scale. In this paper, we investigate whether smaller,…

- **[SCAFFOLD: Toward Warrant-Preserving Evidence Transport for Reusable LLM-Agent Skills](https://arxiv.org/abs/2611.23990v1)**
  - *Nami Cho, Shailja Gupta*
  - **ACL** · `2026-11-18`
  - An agent skill that succeeded yesterday may be executable today without being justified for reuse today. Tests may cover only observable contract clauses, outcome oracles may be absent, evaluations may inherit the same erroneous specification, and permissions or dependencies may…

- **[MLE Agents: Autonomous ML Engineering in Large-scale Recommendation Systems](https://arxiv.org/abs/2611.23910v1)**
  - *Matthew Li, Albert Liang, Dilip Raj*
  - **ACL** · `2026-11-18`
  - The typical workflow for improving large-scale ranking and recommendation models is slow and tedious: an engineer forms a hypothesis, implements it as a code change, trains a model, and evaluates it both offline and online, often relying on their own intuition and experience alon…

- **[Algorithmic Market Making Can Lead to Rough Volatility Through the Order Book](https://arxiv.org/abs/2611.24028v1)**
  - *Sai Niranjan Ramachandran*
  - **ACL** · `2026-11-18`
  - Existing work suggests that markets can show volatility with paths rougher than those of Brownian motion. In theory this can happen when the order flow is close to instability with memory that decays as a power law. However, it is not fully clear how such order flow could arise f…

- **[Asymmetric Decomposition for Multi-Agent Path Finding with Unassigned Agents](https://arxiv.org/abs/2611.24108v1)**
  - *Xi Jin, Chen Qian, Renjun Zhang et al.*
  - **ACL** · `2026-11-18`
  - Robots without assigned tasks may obstruct active robots, while routing them to designated parking locations can cause unnecessary travel. This article proposes flow-oracle conflict-based search (FOCBS) for Multi-Agent Path Finding with unassigned agents (MAPF-UA). FOCBS searches…

- **[Idempotency Is Not Recovery: A Fault-Injection Study of Language-Model Agent Tool Actions](https://arxiv.org/abs/2611.23353v1)**
  - *Song Xu*
  - **ACL** · `2026-11-17`
  - When a language-model agent's tool call is interrupted, the action may already have changed an external system without confirmation. Retrying risks duplication; assuming success may conceal an action that never occurred. We study these failure modes in a controlled agent runtime…

- **[Procedure without Judgment: What Small Language Models Learn under an Exact Verifier](https://arxiv.org/abs/2611.21529v1)**
  - *Arunkumar V, Manoranjan Gandhudi, Gangadharan G. R. et al.*
  - **ACL** · `2026-11-16`
  - When an authorization policy blocks an agent's tool call, the audit log should name the facts that forced the decision and nothing more. For an executable policy over an enumerable context space this minimal sufficient reason can be computed exactly, so an explanation is scored a…

- **[Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next](https://arxiv.org/abs/2611.21408v1)**
  - *Javier Aguilar Martín*
  - **ACL** · `2026-11-16`
  - A popular ideation recipe treats an embedding map of existing work as a guide: pick points far from everything and decode them into ideas. I test four ways such distances could guide ideation against what appeared later. (1) Far random directions are not text: no later item reach…

- **[Scientific Coding with Large Language Models: Evidence from Finite Element Analysis](https://arxiv.org/abs/2611.21176v1)**
  - *Erfan Hamdi, Joel Shor, Emma Lejeune*
  - **ACL** · `2026-11-16`
  - Large language models (LLMs) offer a potential route to automating scientific programming, but their usefulness depends on consistently producing numerically correct code. We extend FEM-Bench to 17 finite element tasks involving nonlinear and history-dependent mechanics and struc…

- **[DetourBench: Trajectory-Level Evaluation of Interactive Agents with Exact Minimum-Action Bounds](https://arxiv.org/abs/2611.20844v1)**
  - *Hanlin Tian, Sihan Zhu, Zhao Yang et al.*
  - **ACL** · `2026-11-16`
  - Benchmarks judge language-model agents mainly by whether they reach the correct final state, not by how they got there. Endpoint scoring cannot separate an agent that retrieved exactly the evidence a decision required from one that read most of the environment, nor an agent that…

- **[Instant Weight-Space Consolidation for Long-Term Memory in LLMs](https://arxiv.org/abs/2611.20759v1)**
  - *Manan Suri, Dinesh Manocha*
  - **ACL** · `2026-11-16`
  - Agentic memory systems give LLMs persistent memory by extracting experience into text and retrieving it at query time, but the model itself does not evolve: however many interactions it has had, it starts each query the same. Extraction errors compound, implicit cross-session pat…

- **[From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)**
  - *Jing Luo, Yu-Chen Tian, Chu-Xue Cao et al.*
  - **ACL 2026** · `2026-05-07`
  - Large Language Model (LLM)-based agents have fundamentally reshaped artificial intelligence by integrating external tools and planning capabilities. While memory mechanisms have emerged as the architectural cornerstone of these systems, current research remains fragmented, oscill…

- **[Lightweight LLM Agent Memory with Small Language Models](https://arxiv.org/abs/2604.07798)**
  - *Jia-Quan Zhang, Chao-Ning Zhang, Shu-Xu Chen et al.*
  - **ACL 2026** · `2026-04-09`
  - Although LLM agents can leverage tools for complex tasks, they still need memory to maintain cross-turn consistency and accumulate reusable information in long-horizon interactions. However, retrieval-based external memory systems incur low online overhead but suffer from unstabl…

- **[Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use](https://arxiv.org/abs/2604.05432)**
  - *Wu-Yang Zhang, Shi-Chao Pei*
  - **ACL 2026** · `2026-04-07`
  - Tool-use large language model (LLM) agents are increasingly deployed to support sensitive workflows, relying on tool calls for retrieval, external API access, and session memory management. While prior research has examined various threats, the risk of systematic data exfiltratio…

- **[EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis](https://arxiv.org/abs/2601.05808)**
  - *Xiaoshuai Song, Hao Chang, Guan-Ting Dong et al.*
  - **ACL 2026** · `2026-01-09`
  - Large language models (LLMs) are expected to be trained to act as agents in various real-world environments, but this process relies on rich and varied tool-interaction sandboxes. However, access to real systems is often restricted; LLM-simulated environments are prone to halluci…

- **[ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering](https://arxiv.org/abs/2510.20036)**
  - *Marianne Menglin Liu, Daniel García, Fjona Parllaku et al.*
  - **ACL 2025** · `2025-10-22`
  - Large language model (LLM) agents rely on external tools to solve complex tasks, but real-world toolsets often contain redundant tools with overlapping names and descriptions, introducing ambiguity and reducing selection accuracy. LLMs also face strict input context limits, preve…

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://arxiv.org/abs/2507.21028)**
  - *Jia-Ju Chen, Yuxuan Lu, Xiaojie Wang et al.*
  - **ACL 2025** · `2025-07-28`
  - Nearly all human work is collaborative; thus, the evaluation of real-world NLP applications often requires multiple dimensions that align with diverse human perspectives. As real human evaluator resources are often scarce and costly, the emerging"LLM-as-a-judge"paradigm sheds lig…

- **[STeCa: Step-level Trajectory Calibration for LLM Agent Learning](https://arxiv.org/abs/2502.14276)**
  - *Han-Lin Wang, Jian Wang, Chak Tou Leong et al.*
  - **ACL 2025** · `2025-02-20`
  - Large language model (LLM)-based agents have shown promise in tackling complex tasks by interacting dynamically with the environment. Existing work primarily focuses on behavior cloning from expert demonstrations or preference learning through exploratory trajectory sampling. How…

- **[iAgent: LLM Agent as a Shield between User and Recommender Systems](https://arxiv.org/abs/2502.14662)**
  - *Wujiang Xu, Yun-Xiao Shi, Zujie Liang et al.*
  - **ACL 2025** · `2025-02-20`
  - Traditional recommender systems usually take the user-platform paradigm, where users are directly exposed under the control of the platform's recommendation algorithms. However, the defect of recommendation algorithms may put users in very vulnerable positions under this paradigm…

- **[Red-Teaming LLM Multi-Agent Systems via Communication Attacks](https://arxiv.org/abs/2502.14847)**
  - *Peng-Fei He, Yu-Ping Lin, Shen Dong et al.*
  - **ACL 2025** · `2025-02-20`
  - Large Language Model-based Multi-Agent Systems (LLM-MAS) have revolutionized complex problem-solving capability by enabling sophisticated agent collaboration through message-based communications. While the communication framework is crucial for agent coordination, it also introdu…

- **[Unveiling Privacy Risks in LLM Agent Memory](https://arxiv.org/abs/2502.13172)**
  - *Bo Wang, Weiyi He, Sheng-Lai Zeng et al.*
  - **ACL 2025** · `2025-02-17`
  - Large Language Model (LLM) agents have become increasingly prevalent across various real-world applications. They enhance decision-making by storing private user-agent interactions in the memory module for demonstrations, introducing new privacy risks for LLM agents. In this work…

- **[FLAG-Trader: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading](https://arxiv.org/abs/2502.11433)**
  - *Guo-Jun Xiong, Zhiyang Deng, Ke-Yi Wang et al.*
  - **ACL 2025** · `2025-02-17`
  - Large language models (LLMs) fine-tuned on multimodal financial data have demonstrated impressive reasoning capabilities in various financial tasks. However, they often struggle with multi-step, goal-oriented scenarios in interactive financial markets, such as trading, where comp…

- **[PaSa: An LLM Agent for Comprehensive Academic Paper Search](https://arxiv.org/abs/2501.10120)**
  - *Yi-Cheng He, Guan-Hua Huang, Pei-Yuan Feng et al.*
  - **ACL 2025** · `2025-01-17`
  - We introduce PaSa, an advanced Paper Search agent powered by large language models. PaSa can autonomously make a series of decisions, including invoking search tools, reading papers, and selecting relevant references, to ultimately obtain comprehensive and accurate results for co…

- **[Uncertainty Propagation on LLM Agent](https://aclanthology.org/2025.acl-long.302.pdf)**
  - *Qi-Wei Zhao, Dong Li, Yan-Chi Liu et al.*
  - **ACL 2025**


### EMNLP

- **[Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639)**
  - *X. Zhang, Wen-Xuan Zhang, See-Kiong Ng et al.*
  - **EMNLP 2026** · `2026-06-29`
  - World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution. However, unreliable foresight can be ignored, misused, or even degrade downstream decision-making. In this paper, we introduce WorldEvolver, a…

- **[Coarse-to-Fine Grounded Memory for LLM Agent Planning](https://arxiv.org/abs/2508.15305)**
  - *Wei Yang, Jin-Wei Xiao, Hongming Zhang et al.*
  - **EMNLP 2025** · `2025-08-21`
  - Recent advancements in Large Language Models (LLMs) have driven growing interest in LLM-based agents for complex planning tasks. To avoid costly agent training, many studies adopted memory mechanism that enhances LLM with offline experiences or online trajectory analysis. However…

- **[ECom-Bench: Can LLM Agent Resolve Real-World E-commerce Customer Support Issues?](https://arxiv.org/abs/2507.05639)**
  - *Haoxin Wang, Xianhan Peng, H. Cheng et al.*
  - **EMNLP 2025** · `2025-07-08`
  - In this paper, we introduce ECom-Bench, the first benchmark framework for evaluating LLM agent with multimodal capabilities in the e-commerce customer support domain. ECom-Bench features dynamic user simulation based on persona information collected from real e-commerce customer…

- **[LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://arxiv.org/abs/2506.17335)**
  - *Shuo Yan, Ruochen Li, Ziming Luo et al.*
  - **EMNLP 2025** · `2025-06-19`
  - Large language model (LLM) agents have demonstrated remarkable potential in advancing scientific discovery. However, their capability in the fundamental yet crucial task of reproducing code from research papers, especially in the NLP domain, remains underexplored. This task inclu…

- **[DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation](https://arxiv.org/abs/2503.07044)**
  - *Ziming You, Yumiao Zhang, De-Xuan Xu et al.*
  - **EMNLP 2025** · `2025-03-10`
  - Existing large language model (LLM) agents for automating data science show promise, but they remain constrained by narrow task scopes, limited generalization across tasks and models, and over-reliance on state-of-the-art (SOTA) LLMs. We introduce DatawiseAgent, a notebook-centri…

- **[CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space](https://arxiv.org/abs/2502.12532)**
  - *Yong Zhao, Kai Xu, Zheng-Qiu Zhu et al.*
  - **EMNLP 2025** · `2025-02-18`
  - Embodied Question Answering (EQA) has primarily focused on indoor environments, leaving the complexities of urban settings-spanning environment, action, and perception-largely unexplored. To bridge this gap, we introduce CityEQA, a new task where an embodied agent answers open-vo…

- **[Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227)**
  - *Samuel Schmidgall, Yu-Sheng Su, Ze Wang et al.*
  - **EMNLP 2025** · `2025-01-08`
  - Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory, an…

- **[AgentDiagnose: An Open Toolkit for Diagnosing LLM Agent Trajectories](https://aclanthology.org/2025.emnlp-demos.15.pdf)**
  - *Tian-Yue Ou, Wan-Yao Guo, Apurva Gandhi et al.*
  - **EMNLP 2025**
  - ,


### Other / arXiv

- **[Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development](https://arxiv.org/abs/2611.24154)**
  - *Xirui Jiang, Yuxi Chen, Rui Yang et al.*
  - 🤗 Featured · `2026-11-18`

- **[Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement](https://arxiv.org/abs/2611.24651)**
  - *Zhenqing Ling, Qirui Jiao, Daoyuan Chen et al.*
  - 🤗 Featured · `2026-11-18`
  - We present Piccolo, a family of multimodal decision models (0.8B to 27B) that coevolves model capabilities and training data via Agentic Data Engineering and recursive self-improvement (RSI). The models predict probabilities over candidate answers for general-purpose text and vis…

- **[PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents](https://arxiv.org/abs/2611.24362)**
  - *Lipeng He, Yihan Wang, Jiawen Zhang et al.*
  - 🤗 Featured · `2026-11-18`
  - Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-teaming methods often leve…

- **[Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow](https://arxiv.org/abs/2611.23751)**
  - *Rui Li, Liyang He, Zheng Zhang et al.*
  - 🤗 Featured · `2026-11-18`
  - Autonomous LLM agents incur substantial cost and latency by invoking a large model (System-2) at every step, even when many intermediate actions choose among a small set of known candidates. Existing dual-system agents offload such decisions to a lightweight System-1 model, but r…

- **[IDEA: Intent-Dominance Evidence Audit for Inference-Time Backdoor Detection in GUI Agents](https://arxiv.org/abs/2611.24102)**
  - *Zhizhuo Kou, Sizai Hou, Jian Yang et al.*
  - 🤗 Featured · `2026-11-18`

- **[The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements](https://arxiv.org/abs/2611.23068)**
  - *Yuanhao Zeng, Shaocheng Lan, Ao Lu et al.*
  - 🤗 Featured · `2026-11-17`
  - Agent evolution follows a simple loop: a proposer writes candidate artifacts (prompts, skills, memories) and selection accepts those that score higher. This loop has shown promise, yet practitioners face a puzzle: methods trade wins across papers, and evolution often fails to boo…

- **[QDA: Closed-Loop LLM Quantization Design with Agents](https://arxiv.org/abs/2611.23388)**
  - *Xingyang Li, Tianlang Zhao, Song Han et al.*
  - 🤗 Featured · `2026-11-17`
  - Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortuna…

- **[FVScore: Specification-Driven Neuro-Symbolic Video Evaluation](https://arxiv.org/abs/2611.22673)**
  - *Do Xuan Long, Long T. Le, Yiwen Song et al.*
  - 🤗 Featured · `2026-11-17`
  - We introduce Faithfulness Video Score (FVSCORE), a neuro-symbolic framework for specification-driven video generation evaluation. Existing evaluators rely on holistic MLLM judgments or vision-language metrics, yet aligning their scores with human judgments and tracing them to spe…

- **[Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents](https://arxiv.org/abs/2611.22033)**
  - *Adi Krishnamoorthy, X. Y. Han*
  - 🤗 Featured · `2026-11-17`
  - Large language models (LLMs) are increasingly deployed as autonomous shopping agents that process multimodal product listings (consisting of visual and text data) and recommend purchases on behalf of consumers. Naturally, one might assume that models with more thinking power woul…

- **[NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding](https://arxiv.org/abs/2611.22790)**
  - *Tianci Xie, Li Chen, Pinxue Guo et al.*
  - 🤗 Featured · `2026-11-17`
  - Fine-grained questions about long videos ask how many times an action occurs, in what order events unfold, or exactly when a state changes. Answering them can require finding brief moments scattered across hours of footage. Agentic models that decide when and where to look promis…

- **[BLIP-Live: Balancing Timeliness & Firing Precision in Proactive Streaming Video Agents](https://arxiv.org/abs/2611.21553)**
  - *Kanchana Ranasinghe, Honglu Zhou, Dominick Reilly et al.*
  - 🤗 Featured · `2026-11-16`

- **[StatePortal: Agentic Checkpoint Synthesis for Testing Deep States in Interactive Software](https://arxiv.org/abs/2611.23257)**
  - *Zhiyuan Peng, Wei Tao, Chenhao Ying et al.*
  - 🤗 Featured · `2026-09-29`

- **[KnowledgeClaw: Towards Agentic Knowledge Engineering via Omnimodal Hypergraphs](https://arxiv.org/abs/2611.24294)**
  - *Haoran Luo, Jiapu Wang, Linhao Luo et al.*
  - 🤗 · `2026-11-18`
  - Knowledge engineering (KE) turns raw files into a reasoning-ready knowledge base, a task now within reach of LLM agents. KE has progressed from chunk and graph retrieval-augmented generation (RAG) to memory agents, agentic KE and multimodal KE. However, a live knowledge base need…

- **[Intent Contracts: Taking Tools Away from Agents](https://arxiv.org/abs/2611.24025)**
  - *Ziyuan Wang, Genliang Zhu, Xiaobo Chen et al.*
  - 🤗 · `2026-11-18`
  - Intent contracts are an authorization interface for tool-using LLM agents in which the planning model holds no tools. For each step it submits a short logged contract: a goal, a verbatim quotation of the user, and scope fields. Code validates the contract, and a small trusted mod…

- **[Agent Verifiers in Counterfactual Analysis: A Pilot Study Benchmarking Agentic Heterogeneous Treatment Effects](https://arxiv.org/abs/2611.23621)**
  - *Satiyabooshan Murugaboopathy, Entejar Alam, Adel Daoud et al.*
  - 🤗 · `2026-11-17`
  - Agents can expand the covariate space of randomized experiments by retrieving fast-moving local context missed by slow-changing survey baseline covariates, helping characterize who benefits most from an intervention. Verifying such covariates is difficult: individual treatment ef…

- **[Knowing What You Know: A Trait Theory of Reviewer Value in Human-AI Cognitive Systems](https://arxiv.org/abs/2611.24932v1)**
  - *Priyanka Sinha, Sugam Pandey*
  - `2026-11-18`
  - When a capable model and a human reviewer cooperate on the same decision, which human still adds value? We argue this is a question about a single cognitive trait, metacognitive calibration: the alignment between a reviewer's behavioral confidence and the actual correctness of th…

- **[Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses](https://arxiv.org/abs/2611.24924v1)**
  - *Jiahang Lin, Jiahao Chen, Yiding Wang et al.*
  - `2026-11-18`
  - Real-world harness engineering is driven by explicit and implicit user requirements, which guide development and validation. However, existing harness evolution methods often overlook implicit requirements and interaction needs, while using a single evolution agent to modify the…

- **[Who are you? The Personal Imitation Game](https://arxiv.org/abs/2611.24888v1)**
  - *Muhammad Rizky Wellyanto, Hajara-Yasmin Isa, Kexin Xue et al.*
  - `2026-11-18`
  - Large Language Models (LLMs) now perform strongly on Alan Turing's 1950 Imitation Game, so we propose a harder challenge, the Personal Imitation Game, which asks whether a machine can replicate a specific individual in conversation rather than a generic human. Testing with 30 par…

- **[Local AI Agents in Power Electronics Simulation: Deployment, Measurements and Costs](https://arxiv.org/abs/2611.24880v1)**
  - *Yuzhuo Li, Pasan Gunawardena, Yunwei Li*
  - `2026-11-18`
  - Agentic artificial intelligence (AI) is emerging in power electronics, where it drives the simulation loop that engineers used to close largely by hand. In this loop, a converter design, or a study of the network it connects to, is built, run, measured and revised until it satisf…

- **[Choosing What to Observe: Budget-Paired Counterfactual Audits for Credible Evaluation of Visual Agents](https://arxiv.org/abs/2611.24867v1)**
  - *Ruiqi Liu, Jinming Li, Mo Wang et al.*
  - `2026-11-18`
  - Visual agents that read dense documents must ration a finite observation budget across candidate regions, yet answer accuracy conflates where an agent looks, how it adapts to the reads that remain, and how it an?swers once observation stops. We introduce budget-paired counterfact…

- **[Vibe-Trading: Towards Agent-Native Trading](https://arxiv.org/abs/2611.24845v1)**
  - *Haozhe Wu, Zhonghang Li, Chao Huang*
  - `2026-11-18`
  - Existing AI agents can retrieve information, call tools, run experiments, and produce multi-step outputs. Yet most are built around relatively static workflows and struggle to preserve reliable state as the environment changes. Financial trading makes this limitation especially c…

- **[Isabelle Pool Server: a pooled verification service for prover training and multi-agent proving](https://arxiv.org/abs/2611.24788v1)**
  - *Xuanwei Ren, Wenda Li*
  - `2026-11-18`
  - Isabelle Pool Server (IPS), a verification service with a pool of warm headless Isabelle sessions behind an HTTP API, with session leasing and reclamation, memory-aware admission control, and a time budget on every call. Its verification interface spans single-step execution, blo…

- **[Depth Before Breadth: Reverse-to-Forward Curriculum with Advantage Decomposition for LLM Agent](https://arxiv.org/abs/2611.24697v1)**
  - *Siyuan Du, Yuxin Liu, Meng Tang et al.*
  - `2026-11-18`
  - Reinforcement learning (RL) has become a common approach for training large language model (LLM) agents on long-horizon tasks. However, learning from sparse terminal rewards makes credit assignment and exploration difficult. We approach these challenges through a policy-induced c…

- **[Clover-35B-A3B-Preview Technical Report](https://arxiv.org/abs/2611.24636v1)**
  - *DiffuSpace Technical Team*
  - `2026-11-18`
  - We introduce Clover-35B-A3B-Preview (Clover), a mixture-of-experts diffusion language model with 35 billion total parameters and 3 billion activated parameters, supporting thinking-mode generation. Clover adapts Gated Delta Networks to block diffusion by combining recurrent memor…

- **[GateWatch: Low-Overhead LLM Monitoring with Boolean Circuits](https://arxiv.org/abs/2611.24619v1)**
  - *Firas Spanioli, Yaniv David*
  - `2026-11-18`
  - As large language models (LLMs) and LLM-based agents are increasingly deployed, monitoring their behavior becomes important for detecting unsafe or unintended actions. Activation probes offer an efficient approach, but existing methods face trade-offs between accuracy, interpreta…

- **[Think Offline, Act in Real Time: Self-Improving Visual Game Agents through Code](https://arxiv.org/abs/2611.24590v1)**
  - *Zipeng Qiu, Shusheng Xu, Jiale Li et al.*
  - `2026-11-18`
  - Pre-trained models can read screens and reason about games, yet on an unfamiliar game, an agent still has to learn to play. We ask how an agent can self-improve on such a game from a few of its own attempts, in real-time visual games where the agent sees only the screen and the g…

- **[ABSClaw: From Invented Worlds to Reality-Grounded Social Simulation](https://arxiv.org/abs/2611.24517v1)**
  - *Shaobin He, Yan Gao, Quan Zheng et al.*
  - `2026-11-18`
  - LLM-based artificial societies exhibit rich behavior but often lack scientific grounding: personas and environments are assumed, interaction networks are synthetic, and simulators are generated as free-form code, making results difficult to tie to real populations and sensitive t…

- **[Probing agent overeagerness in realistic settings with continuation audits](https://arxiv.org/abs/2611.24491v1)**
  - *Sean Lim, Clement Neo*
  - `2026-11-18`
  - Frontier coding agents increasingly exhibit overeagerness, taking surprising, sometimes reckless actions beyond a user's mandate --- reported in recent system cards from frontier model developers. These cases are surfaced through internal deployment monitoring, which requires pri…

- **[Nothing to Declare: Steering a single neuron increases concealment in AI teams](https://arxiv.org/abs/2611.24475v1)**
  - *Edoardo Chidichimo, Felix P. S. Wallis*
  - `2026-11-18`
  - Recent research suggests that individual neurons can have interpretable roles in AI behaviour. In Qwen3.5-4B, steering along one neuron's output direction increased decisions to conceal information more in teams than alone across five scenarios, even when teammates provided no me…

- **[Resolution as Attention for Efficient Agent Memory Perception](https://arxiv.org/abs/2611.24422v1)**
  - *Siqi Xiang, Zhipeng Xu, Shengrui Liu et al.*
  - `2026-11-18`
  - LLM-based agents accumulate extensive interaction histories when solving complex, long-horizon tasks, making efficient memory management critical to their performance and scalability. While existing memory management methods primarily focus on what to retain or retrieve, they oft…

- **[CaDO: Formal Verification-Guided Multi-Agent Framework for Causal Dataset Repair and Generation](https://arxiv.org/abs/2611.24406v1)**
  - *Songli Yu, Qi Luo*
  - `2026-11-18`
  - High-quality causal reasoning datasets are essential for developing models with reliable causal understanding, particularly in specialized domains. However, existing datasets frequently suffer from incorrect annotations and structural imbalances, which can lead to biased predicti…

- **[MoE-Context: Show the Model Only What It Needs](https://arxiv.org/abs/2611.24379v1)**
  - *Vedant Navale*
  - `2026-11-18`
  - AI agents read their whole history at every step. People do not work like that: we keep what the moment needs and hold the rest as a rough note we can recall. MoE-Context applies this to language models. The context is split into blocks. Before each step a fast yes or no pass dec…

- **[Semantic Context Handoff with On-Demand Evidence for Long-Horizon Agents](https://arxiv.org/abs/2611.24357v1)**
  - *Guolong Zheng, Chen Hou, Xu Yang et al.*
  - `2026-11-18`
  - Traditional long-horizon LLM agents often hand off context through full-history prompting, retaining all previous action--observation interactions. As execution proceeds, this history keeps growing, increasing inference cost and potentially degrading accuracy. Existing methods co…

- **[OCTR2A: Real-Time RGB-to-BEV Trajectory Projection and Forecasting at Urban Intersections](https://arxiv.org/abs/2611.24352v1)**
  - *Emanuele Iacobelli, Simone Teglia, Francesco Pro et al.*
  - `2026-11-18`
  - Trajectory forecasting at urban intersections is often studied assuming that reliable bird's-eye-view (BEV) motion histories are available, which in practice requires costly resources such as LiDAR, aerial views, HD maps, or calibrated infrastructure. We address this upstream per…

- **[automodel: A Skill for Agentic Model Discovery](https://arxiv.org/abs/2611.24347v1)**
  - *Marco Virgolin, Harry Desmond, Ester Bergantin et al.*
  - `2026-11-18`
  - The search for better models, whether expressed as analytical equations or neural architectures, has increasingly shifted from manual design toward data-driven automation. While a multitude of algorithms exist, ranging from exhaustive search to AlphaEvolve, recent advances in gen…

- **[Benchmarking LLM abilities on postdoc-level natural science problems](https://arxiv.org/abs/2611.24321v1)**
  - *Alina Avanesyan, Alexey Boldyrev, Liqun Deng et al.*
  - `2026-11-18`
  - Scientific problems have no answer key, so evaluating an agent means deciding what counts as a better solution before any agent is run. Existing benchmarks either match a symbolic answer against a key or, where they require executable work, score it by unit tests, by a rubric, or…

- **[AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents](https://arxiv.org/abs/2611.24313v1)**
  - *Stavros Damianakis, Konstantinos Psounis*
  - `2026-11-18`
  - Prompt injection is the dominant unsolved security risk for LLM agents, and the community now agrees that robustness must be measured against adaptive attackers rather than fixed benchmark injections. Many adaptive red teamers exist, and most are built to maximize attack success…

- **[OpenKAGE: Open-Ended Lifelong Learning in the Open World via Knowledge-Sharing Agent-Group Evolution](https://arxiv.org/abs/2611.24302v1)**
  - *Wenhao Yuan, Longhui Yuan, Zexi Jia et al.*
  - `2026-11-18`
  - Building autonomous agents that continually explore open worlds and acquire new capabilities through experience is a long-standing aspiration in artificial intelligence. Existing research often pursues lifelong learning within predefined tasks, curricula, or objectives, with self…

- **[Beyond Corpus-Driven Imitation: Evolving Musical Mindsets in the Agentic Orchestra via Quantum Reinforcement Learning](https://arxiv.org/abs/2611.24290v1)**
  - *Eduardo Reck Miranda, Moein Fahmideh Vatandoost*
  - `2026-11-18`
  - This paper presents a framework for computer-aided music composition and performance based on quantum reinforcement learning and multi-agent interaction. We introduce the agentic orchestra, where musical agents evolve distinct mindsets through trial-and-error engagement with a mu…

- **[Learning to Coordinate: LLM-Guided Workflow Evolution for Token-Efficient Red Teaming](https://arxiv.org/abs/2611.24221v1)**
  - *Xiaoyang Xing, Wenyu Dai, Xiaoliang Gong et al.*
  - `2026-11-18`
  - Automated red teaming is essential for identifying safety failures in large language models (LLMs), but its practical scalability depends on the resources required to discover those failures. Multi-agent systems can combine complementary capabilities, yet repeated planning, redun…

- **[Worth Another Look:Constrained World-Model Planning for Visual Inspection](https://arxiv.org/abs/2611.24187v1)**
  - *Ziyue Kang, Zixi Qi, Yuchen Dai et al.*
  - `2026-11-18`
  - Visual inspection in field robotics and environmental monitoring must localize multiple targets under strict compute and sensing caps. Exhaustive sweeps waste calls on absent classes, while myopic and search-free policies stumble over heterogeneous tariff cliffs or discard viewpo…

- **[VideoACE: Benchmarking Agentic Video Understanding through High-Frame-Rate Actions](https://arxiv.org/abs/2611.24184v1)**
  - *Luoyuan Zhang, Xuanyu Zheng, Yancheng Long et al.*
  - `2026-11-18`
  - Agentic video understanding requires models to actively interact with video environments to gather evidence and form judgments. Evaluating this capability therefore requires assessing whether models can translate opportunities for interaction into better understanding. We introdu…

- **[Embodied Graph: A Relational World Model for Long-Horizon Tasks](https://arxiv.org/abs/2611.24115v1)**
  - *Zongyuan Wu, Xin Wang, Tongtong Feng et al.*
  - `2026-11-18`
  - Long-horizon tasks in embodied and web environments involve extended decision sequences and delayed feedback, making accurate planning crucial for success. World models tackle this by learning latent dynamics for imagination-based planning. However, existing approaches merely rel…

- **[3D GameDev Arena: Benchmarking Coding Agents That Plan, Build, and Playtest extreme Long-Horizon Browser Games](https://arxiv.org/abs/2611.24073v1)**
  - *Bizhe Bai, Jiliang Jian, Yuqing Yan et al.*
  - `2026-11-18`
  - Coding agents now resolve repository issues and generate compact playable games, but whether they can build a large 3D game from scratch remains open. Such games tightly couple mechanics, scenes, assets, and interaction logic, and their quality rests on player enjoyment, which ex…

- **[Replay, Don't Resample: Off-Policy Consolidation of Long-Horizon RL Experts](https://arxiv.org/abs/2611.24059v1)**
  - *Zhenrui Yue, Gongxiaohui Chen, Huimin Zeng et al.*
  - `2026-11-18`
  - Frontier post-training follows a common recipe: train one expert per domain with reinforcement learning (RL), then consolidate the experts into one model via multi-teacher on-policy distillation (MOPD). Such consolidation is expensive: the student samples in every environment aga…

- **[From Data to Valves: A Self-Learning, Production-Grade Edge Stack for Sustainable HVAC Control](https://arxiv.org/abs/2611.24052v1)**
  - *Abbas Raza Ali, Muhammad Hamza Rehman, Xu Li et al.*
  - `2026-11-18`
  - Learned HVAC controllers rarely leave the simulator, and those that do are typically trained offline, frozen at deployment and retrained from the cloud. We present a production stack in which three learning components run on one NVIDIA Jetson Orin gateway per building, adapt cont…

- **[A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises](https://arxiv.org/abs/2611.24039v1)**
  - *Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid*
  - `2026-11-18`
  - Agentic AI platforms-systems in which LLM agents plan, invoke tools, retain memory and coordinate to change the state of enterprise systems-are being procured faster than they can be measured. Public agent benchmarks score models in fixed harnesses; enterprises buy integrated pla…

- **[Space-X: Self-Evolving Spatial Agents Weaving Clues into Evidence Chains](https://arxiv.org/abs/2611.24004v1)**
  - *Zijian Zhang, Wenqing Tian, Qiang Liu et al.*
  - `2026-11-18`
  - Spatial reasoning connects visual observations, geometric estimates, and linguistic decisions into a coherent derivation. Yet tool-augmented agents often acquire evidence without clear targets, combine outputs under inconsistent object or reference-frame semantics, and misjudge e…

- **[How Complete Must an Environment Be to Train a Capable GUI Agent?](https://arxiv.org/abs/2611.23946v1)**
  - *Jingxing Wang, Teng Wang, Xingyu Lou et al.*
  - `2026-11-18`
  - Graphical user interface (GUI) agents are widely trained in executable GUI environments. To lower cost, build environments in batches, and reduce manual effort, each work trades away part of the environment through its construction choices. We describe these choices along three d…

- **[A Hierarchical Onboard Vision-Language-Navigation Framework for Aerial Robots in Complex Environments](https://arxiv.org/abs/2611.23930v1)**
  - *Yuze Wu, Mo Zhu, Xingxing Li et al.*
  - `2026-11-18`
  - Unmanned Aerial Vehicles (UAVs) are expected to achieve semantic reasoning, intelligent decision-making, and long-horizon navigation under strict onboard constraints. While recent foundation-model-driven approaches have shown promising progress toward this goal, existing methods…

- **[Vanguard: Knowing When to Trust the Draft in Speculative Vision-Language Agents](https://arxiv.org/abs/2611.23917v1)**
  - *Hanqi Mao, Jiajun Fan, Ruihan Guo et al.*
  - `2026-11-18`
  - Vision-language agents that browse websites, operate phones and act in homes reason before every action, so every step waits for a large model, a latency and cost that stand in the way of deployment. Step-level speculation lets a small model draft each step and calls the large mo…

- **[EVA-RSI: Recursive Self-Improvement of Video Evaluators for Judging Temporal Quality](https://arxiv.org/abs/2611.23890v1)**
  - *Yu Yuan, Ruizhou Ding, Shaoheng Fang et al.*
  - `2026-11-18`
  - Video evaluators play an important role in video generation, yet they miss motion defects, limiting the quality of generated videos. Recursive self-improvement (RSI) has made strong progress in mathematics and coding, where explicit verifiers provide reliable feedback on a single…

- **[In Situ Training of Optical Neural Networks by Coding Agents](https://arxiv.org/abs/2611.23875v1)**
  - *Ilker Oguz, Colin Christian, Christophe Moser et al.*
  - `2026-11-18`
  - Optical neural networks promise fast, energy-efficient computing, but every device departs from its design and must be trained with the hardware. In situ training relies on an expert-built calibrated digital model of each device or on gradient-free trial and error. Coding agents,…

- **[A System 1 Decision Model for Medical Multiple-Choice Questions Built on Frozen Language Models](https://arxiv.org/abs/2611.23832v1)**
  - *Pavan Kumar Mantha*
  - `2026-11-18`
  - A System 1 model answers a multiple-choice question in a single pass. A frozen language model turns the question and each option into vectors, two small, trained heads place them in a shared space, and the closest option wins. The design has been shown on agent decisions, but we…

- **[Metrics-in-the-Loop: Complexity Feedback Reshapes Agent-Written Code](https://arxiv.org/abs/2611.23817v1)**
  - *Nicolas Chapados, Jean-François Gagné, Nouha Dziri*
  - `2026-11-18`
  - Coding agents now write whole codebases in long autonomous runs, guided mainly by whether their tests pass. Yet passing tests alone does not reveal accumulating complexity or gaps in test coverage, which then persist as agents extend their own code. We introduce metrics-in-the-lo…

- **[Continual Tool-Space Extension Learning for Multimodal Agents](https://arxiv.org/abs/2611.23810v1)**
  - *Jinbae Seo, Jungin Park, Hyunsung Jang et al.*
  - `2026-11-18`
  - Multimodal agents largely rely on generic tools such as cropping, search, and code execution, leaving specialist vision models outside their tool space. However, bringing such a model into an already trained agent is not straightforward. The challenge is to learn each new tool ef…

- **[KnowMe Paper Radar: Lightweight Discovery of Promising Papers in the Age of Autoresearch](https://arxiv.org/abs/2611.23702v1)**
  - *Zhuo Chen, Jian Wang, Jinjie Gu et al.*
  - `2026-11-18`
  - The growing volume of topically similar papers makes it difficult to identify new work that can offer useful research insights or methodological guidance. We present KnowMe Paper Radar, a lightweight discovery tool that combines multiple sources of evidence into personalized read…

- **[Auditable Clinical Support with Decision Agents](https://arxiv.org/abs/2611.23700v1)**
  - *Tiancheng Bao, Riga Wu, Jan Wienhold et al.*
  - `2026-11-18`
  - Clinicians reviewing a diagnostic work-up will ask what was considered at each step and why the assessment changed. Agents powered by free text can reach physician-level diagnostic accuracy, but their written reasoning does not always reflect the factors that went into the decisi…

- **[Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics](https://arxiv.org/abs/2611.23678v1)**
  - *Dowling Wong*
  - `2026-11-18`
  - Autonomous agents that run ML experiments are usually judged by the best score they reach. That score says nothing about how it was reached: whether the agent stayed within the files it was allowed to edit, whether failed trials were kept or silently dropped, and whether each kee…

- **[Communicative On-Policy Distillation: Distilling Black-Box Teacher Capabilities through Communication for Long-Horizon Tasks](https://arxiv.org/abs/2611.23673v1)**
  - *Lirui Luo, Kelong Mao, Xinwei Yang et al.*
  - `2026-11-18`
  - On-policy distillation (OPD) is a powerful paradigm for improving language-model agents on long-horizon tasks, yet its conventional formulation relies on teacher logits that text-only black- box models do not expose. To address this limitation, we introduce Communicative On-Polic…

- **[Lodestone: Automated Semantic Discovery of Datacenter Hardware Specialization](https://arxiv.org/abs/2611.23663v1)**
  - *Peizhe Liu, Akanksha Jain, Gerasimos Gerogiannis et al.*
  - `2026-11-18`
  - Hardware specialization can improve datacenter efficiency. Unfortunately, identifying computations that justify dedicated hardware is difficult. Existing approaches analyze hot functions, instruction patterns, or overheads such as datacenter tax. They can miss fine-grained comput…

- **[Safe Personal RSI: Evaluating and Repairing Personal-Agent Updates](https://arxiv.org/abs/2611.23651v1)**
  - *Jiapeng Pei, Yuhang Yao, Sitan Liu et al.*
  - `2026-11-18`
  - Kicker is a personal health assistant. Changes to an assistant's reusable instructions can improve task handling while changing what it discloses, which requests it follows, and how it reports actions. We study Safe Personal RSI, an update-evaluation component developed for Kicke…

- **[On Evaluating User Simulators for Interactive Agents](https://arxiv.org/abs/2611.24892v1)**
  - *Hengguang Zhou, I-Hung Hsu, Li Chen et al.*
  - `2026-11-18`
  - User simulators offer a scalable way to evaluate interactive agents, but how to assess their quality remains underexplored. In particular, it is unclear whether existing user simulator evaluation frameworks reliably detect meaningful failures in simulated user behavior. This unce…

- **[Learning to Interact in Multi-Agent Self-Play for Controllable Autonomous Driving Scenario Generation](https://arxiv.org/abs/2611.24876v1)**
  - *Beyazit Yalcinkaya, Ethan Pronovost, Maximilian Naumann et al.*
  - `2026-11-18`
  - Large-scale, multi-agent self-play trains robust driving policies effectively in simulation, but controlling these models to generate specific, safety-critical edge cases remains a key challenge. Existing goal-conditioned self-play frameworks rely primarily on static map-location…

- **[Kaer: Security-Aware Replanning for Multi-Agent Systems](https://arxiv.org/abs/2611.24839v1)**
  - *Tushin Mallick, Evan Rose, Matthew Laws et al.*
  - `2026-11-18`
  - One popular architecture for multi-agent systems (MAS) relies on an orchestrator that generates an initial plan, coordinates its execution, and dynamically revises the plan based on agent feedback when tasks cannot be fully specified in advance. This dynamic replanning introduces…

- **[Meta-LSQ: A Closed-Form Sobolev Inner Solver for Few-Shot Meta-Learning](https://arxiv.org/abs/2611.24718v1)**
  - *Antonin Sulc*
  - `2026-11-18`
  - Gradient-based meta-learners such as model-agnostic meta-learning (MAML) adapt to a new task with an inner loop of gradient descent that has to be differentiated through, and they meta-learn every network weight. Meta-LSQ instead fits each task with one regularised least-squares…

- **[Cooperative UAV and Ground Station for Robust MEC of Dynamic Aquatic IoT: A Generative AI-Enhanced Approach](https://arxiv.org/abs/2611.24466v1)**
  - *Jiahao You, Ziye Jia, Chao Dong et al.*
  - `2026-11-18`
  - The increasing aquatic Internet of Things (AIoTs) require computational support and coverage in applications such as maritime search and rescue. Unmanned aerial vehicles (UAVs) can offer low-cost, flexible aerial services, and ground stations (GSs) can provide powerful supports,…

- **[RSIBench-Infra: Can Agents Optimize Their Own Training and Inference Infrastructure at Production Scale?](https://arxiv.org/abs/2611.24395v1)**
  - *Hanlin Wu, Yifei Wang, Zhicheng Cai et al.*
  - `2026-11-18`
  - Improving the efficiency of training and inference infrastructure is a practical component of recursive self-improvement. Existing benchmarks for agent-driven optimization largely focus on individual software layers such as kernel, leaving unclear whether agents can deliver end-t…

- **[VAFL: A Vertical Analytic Federated Learning Mechanism for Efficient Crowdsourced Services via Closed-Form Solutions](https://arxiv.org/abs/2611.24367v1)**
  - *Yajiang Huang, Anfeng Liu, Tian Wang et al.*
  - `2026-11-18`
  - Intelligent services often rely on complementary information held by different organizations, motivating Vertical Federated Learning without centralized raw-data pooling. We propose VAFL, a Vertical Analytic Federated Learning framework that fits classification and regression hea…

- **[VESPA: Verifiable Symbolic Policy Adaptation for Safe Reinforcement Learning](https://arxiv.org/abs/2611.24083v1)**
  - *Paul König, Sascha Marton, Stefan Lüdtke et al.*
  - `2026-11-18`
  - Safe reinforcement learning (RL) aims to prevent agents from taking actions that are dangerous or destructive to their environment. This is especially important for safety-critical domains, such as robotics or autonomous driving. Formal verification can be used to prove agent saf…

- **[OMNIS+: Semantic RAN Slicing and Quantization for Dynamic Split Neural Networks](https://arxiv.org/abs/2611.23977v1)**
  - *Langtian Qin, Avishkar Dnyaneshwar Kawadgave, Ian Andrew Harshbarger et al.*
  - `2026-11-18`
  - Edge computing enables resource-constrained devices to execute machine learning (ML) applications via task offloading, with radio access network (RAN) slicing playing a crucial role in provisioning joint communication and computing resources. However, existing RAN slicing framewo…

- **[CoSlice: Coordinated Multi-Agent Reinforcement Learning for 5G Network Slicing Allocation](https://arxiv.org/abs/2611.23909v1)**
  - *Pengxin Wang, Nakjung Choi, Jingdi Chen*
  - `2026-11-18`
  - Radio Access Network (RAN) slicing is a shared resource allocation problem: each slice seeks to satisfy its Service Level Agreement (SLA) with minimal radio-resource consumption, while all slices compete for a limited resource budget. This creates both an intra-slice trade-off be…

- **[Online State-Representation Adaptation under Synthetic Interaction-Cue Remapping](https://arxiv.org/abs/2611.23836v1)**
  - *Bin Yin*
  - `2026-11-18`
  - When cues change what they predict, continuing to update a learned mapping may help an agent choose the appropriate action. We tested this in a one-step synthetic task by comparing a logistic state predictor that continued to learn from state labels with the same predictor frozen…

- **[MoMoVL: Modality-Aware Adaptive Compression for On-Device Sparsely-Activated Vision-Language Models](https://arxiv.org/abs/2611.23695v1)**
  - *Dongkeun Lee, Wonjun Lee*
  - `2026-11-18`
  - The rise of the agentic web has been accompanied by growing demand for on-device Vision-Language Models (VLMs) that perform diverse cross-modal web tasks with enhanced privacy and reduced latency. Mixture-of-Experts (MoE) models are widely adopted in modern VLMs for compute-effic…

- **[Ground, Iterate, Trace: Decomposing AI Research Ideation](https://arxiv.org/abs/2611.24887v1)**
  - *Samson Yu, Qiran Zou, Jing Yu Lim et al.*
  - `2026-11-18`
  - Large language models have been widely used to generate plausible research ideas, yet it remains unclear what makes automated ideation effective and how generated novel proposals arise from prior scientific work. We introduce the Creative AI Researcher (CAR), an agentic framework…

- **[Large Language Models or AI Agents for English to Arabic Translation? An assessment on WikiEn-Ar190](https://arxiv.org/abs/2611.24588v1)**
  - *Fatima Zahra Iguenfer, Yousra Chtouki*
  - `2026-11-18`
  - This research investigates whether a large language model or an autonomous AI Agent performs better at translating from English to Arabic, which is considered a low-resource language. The authors introduce WikiEn-Ar190, a new dataset of 190 carefully selected Wikipedia articles f…

- **[ProbMedTOD: A Bayesian Network Guided Task-Oriented Dialogue System for Patient History Taking](https://arxiv.org/abs/2611.24535v1)**
  - *Vishal Vivek Saley, Bhavesh Gurnani, Dinesh Raghu et al.*
  - `2026-11-18`
  - Patient history taking is a strategic, multi-turn process that refines diagnostic hypotheses through iterative questioning, mirroring clinical reasoning where each inquiry updates beliefs over candidate diagnoses. Deploying AI in this setting is constrained by privacy, cost, and…

- **[Resilient Federated LQR over Noisy and Lossy Uplinks via Scalar Communication](https://arxiv.org/abs/2611.23913v1)**
  - *Mohammadreza Rostami, Shahriar Talebi, Solmaz S. Kia*
  - `2026-11-18`
  - This paper studies model-free federated learning of a common LQR controller for a fleet of similar systems that communicate with a server over an uplink subject to limited bandwidth, packet dropout, and additive noise. We propose \textsc{ResiFedLQR}, a scalar communication scheme…

- **[A Comparison of Heuristic, Human-Sensitive, and Self-Play DRL Policies in Human-Agent Teaming](https://arxiv.org/abs/2611.23747v1)**
  - *Ayman bin Kamruddin, Christopher Lam, Gaurav Patil et al.*
  - `2026-11-18`
  - Dynamical Perceptual-Motor Primitives (DPMPs) offer a tractable framework for generating human-like movement dynamics in artificial agents (AAs) and have been used to support coordination in human-AI teaming tasks. Traditionally, DPMP controllers rely on heuristic (rule-based) de…

- **[The Value Semantics Layer: Enabling Machine-Understandable Databases for Agentic AI](https://arxiv.org/abs/2611.23629v1)**
  - *Jalal Mahmud, Eser Kandogan*
  - `2026-11-17`
  - As data systems increasingly support autonomous LLM-powered agents alongside human analysts, they require richer semantic infrastructure bridging analytical concepts and analytical operations. Existing metadata systems expose schemas, catalogs, lineage, and governance information…

- **[Weight Space Programming for Vision Language Model Repair](https://arxiv.org/abs/2611.23615v1)**
  - *Avinash Goutham Aluguvelly*
  - `2026-11-17`
  - In weight-space programming, a language model edits a network's weights directly, without gradients. We ask what a successful repair of this kind relies on. We plant faults in the weights of two vision-language models, SmolVLM-256M and LFM2-VL-450M, and check each edit made by a…

- **[MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain](https://arxiv.org/abs/2611.23613v1)**
  - *Sara Amar*
  - `2026-11-17`
  - We introduce MANGO Arena, an open-source testbed in which four LLM agents each run one company in a serial supply chain adapted from MANGO, a classroom factory-management game. The environment enforces hard rules (a truck limit, a no-credit cash constraint and production capacity…

- **[RefinementGuard: Counterexample-Directed Semantic Qualification for Hidden Agent-Tool Execution](https://arxiv.org/abs/2611.23611v1)**
  - *Adhyayan Veer Singh, Fanjiang Ye, Yuke Wang*
  - `2026-11-17`
  - Tool runtimes can lower an agent-selected operation into a hidden parallel graph, reducing latency and context while risking semantic mistranslation. We introduce RefinementGuard: translation validation for hidden, effectful agent-tool lowerings, coupled to artifact-bound, fail-c…

- **[ARISE: Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents](https://arxiv.org/abs/2611.23588v1)**
  - *Jiangyun Zhang, Zhou Tang, Kristen Surrao et al.*
  - `2026-11-17`
  - Enterprise LLM agents operate in dynamic environments where foundation models evolve rapidly, workflows update frequently, and deployments need to satisfy accuracy and cost requirements. We propose ARISE (Agent Refinement through Iterative Self-Evaluation), a practical memory arc…

- **[Receiver-Conditioned Clarification for Multi-Agent Food Assistance](https://arxiv.org/abs/2611.23572v1)**
  - *Kaiwen Shi, Zheyuan Zhang, Changzhi Liu et al.*
  - `2026-11-17`
  - Food insecurity creates a pressing need for guidance that helps households find usable food resources and assess food choices in light of their circumstances. Such guidance must connect eligibility requirements, practical access constraints, and dietary needs rather than return i…

- **[LProp: Propagating Latent Uncertainty through Evidence-Conditioned Belief Revision in LLM Agents](https://arxiv.org/abs/2611.23564v1)**
  - *Kaiwen Shi, Zheyuan Zhang, Weixiang Sun et al.*
  - `2026-11-17`
  - When LLM agents pass intermediate judgments downstream without uncertainty, later decisions may treat tentative assumptions as facts. Effective uncertainty propagation must preserve information for correction and update inherited beliefs as new evidence arrives. Yet scalar scores…

- **[GRAFT: Execution-Guided Genetic Recombination for Agent Design](https://arxiv.org/abs/2611.23509v1)**
  - *Sevda Ebrahimi, Mohammed Saidul Islam, Xiaodan Zhu et al.*
  - `2026-11-17`
  - Automated agent design searches for executable architectures that improve LLM-based agent performance, with evolutionary methods using language-model crossover to recombine promising mechanisms for task decomposition, model coordination, and verification. This search, however, is…

- **[SpecLook: Speculating Where to Look for Fast and Reliable Agentic MLLMs](https://arxiv.org/abs/2611.23483v1)**
  - *Xi Ding, Jiawei Zhang*
  - `2026-11-17`
  - Agentic multimodal large language models (MLLMs) that think with images interleave reasoning with zoom-in tool calls. However, this sequential loop is slow, and its answers carry no reliability score. Prior speculation of tokens, reasoning steps, or answers keeps the loop, and an…

- **[Diagnostic Accuracy and Navigation Behavior of Vision-Language Model Agents Reading Emergency CT and MRI Examinations](https://arxiv.org/abs/2611.23480v1)**
  - *Jonathan Lichtle, Aymen Meddeb, Antonin Birot et al.*
  - `2026-11-17`
  - Purpose. To evaluate the diagnostic accuracy and image navigation behavior of vision-language model (VLM) agents under varying exploration strategies. Materials and Methods. In this retrospective study, six VLMs read 100 emergency CT and MRI examinations published in a public arc…

- **[GUARD: Stabilizing Recursive Self-Improvement with Regret Guidance](https://arxiv.org/abs/2611.23476v1)**
  - *Minghe Zhang, Xuetao Kang, Yifei Ming et al.*
  - `2026-11-17`
  - Autonomous AI agents pair a frozen base model with an editable harness of prompts, skills, tool rules, and memory. Recursive self-improvement (RSI) adapts this harness from experience without weight updates, yet self-editing without external graders often backfires: reflection an…

- **[Reliability by Architecture: Agentic Workflows for Validated Multi-Physics Simulation from Natural Language](https://arxiv.org/abs/2611.23473v1)**
  - *Søren Taverniers, Eric Darve, Hamdi A. Tchelepi*
  - `2026-11-17`
  - Preparing, executing, and validating strongly coupled multi-physics simulations require expert time. Agentic workflows use large language models (LLMs) to coordinate them from natural-language descriptions, but reliability requires checks of physical consistency and fidelity to t…

- **[Tracking Representations in LLM Reasoning Traces for Iterated Games](https://arxiv.org/abs/2611.23403v1)**
  - *Chaipat Tirapongprasert, Rajarshi Das, Parijat Dube*
  - `2026-11-17`
  - Large language model (LLM) agents achieve state-of-the-art performance across domains through chain-of-thought (CoT) reasoning. Despite their ubiquitous use, little is understood about the relationship between the externalized trace and the model's actual computation. We address…

- **[Where the Tokens Go: Heat, Entropy and Error in Agentic Coding](https://arxiv.org/abs/2611.23375v1)**
  - *Alán Aspuru-Guzik, Varinia Bernales*
  - `2026-11-17`
  - Coding agents are billed by the token, yet software engineering says nothing about what a token actually buys. Here we introduce a theory of software thermodynamics. The theory draws analogues from classical and stochastic thermodynamics, extends them, and applies them to modern…

- **[StringQFT: A Multiuse Textbook Resource for AI-Assisted Theoretical Physics](https://arxiv.org/abs/2611.23225v1)**
  - *Xingyang Yu*
  - `2026-11-17`
  - We present StringQFT as a textbook collection for string constructions of quantum field theory and as infrastructure for AI-assisted theoretical physics. The collection comprises 18 volumes, 190 chapters and 3,795 pages, covering brane probes, brane webs, geometric engineering, F…

- **[Do LLM Agents Still Need to Be Told How to Self-Improve?](https://arxiv.org/abs/2611.23219v1)**
  - *Shobhita Sundaram, Cansu Sancaktar, Phillip Isola*
  - `2026-11-17`
  - LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how…

- **[Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents](https://arxiv.org/abs/2611.23202v1)**
  - *Viet K. Nguyen, Mohammad I. Husain*
  - `2026-11-17`
  - AI agents increasingly collaborate across organizational boundaries, invoking tools and interacting with agents operated by independent entities. Although existing agent frameworks support planning and coordination, they lack a common mechanism for verifying cross-organizational…

- **[WoRD: Diffusion-Based Posterior Inference for Online Goal Recognition](https://arxiv.org/abs/2611.23192v1)**
  - *Almog Anschel, Sarah Keren*
  - `2026-11-17`
  - Goal recognition is the task of inferring an agent's intended goal from its observed behavior. Most existing work focuses on high-level symbolic recognition, abstracting away the continuous motion through which agents reach their goal. Methods that do reason over continuous traje…

- **[Inference after coding agents](https://arxiv.org/abs/2611.23174v1)**
  - *Florian Gunsilius, David Van Dijcke, Kaspar Wüthrich*
  - `2026-11-17`
  - Empirical research is changing rapidly as AI coding agents are becoming increasingly proficient in every step of it, from writing code to manipulating data. We argue that while the potential of coding agents for science is vast, their use in hypothesis testing poses a substantial…

- **[Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance](https://arxiv.org/abs/2611.23142v1)**
  - *Lorenzo Masoero*
  - `2026-11-17`
  - The "AI revolution" has enabled teams across the technology industry to deliver software features at unprecedented velocity. While code evolves faster than ever, customer-facing documentation often struggles to stay up to speed. As users increasingly rely on LLM-based agents that…

- **[Runtime Verification of Multiple Natural Language Criteria for Agent Governance](https://arxiv.org/abs/2611.23074v1)**
  - *Silviu Pitis, Parand A. Alamdari, Jessica Tang et al.*
  - `2026-11-17`
  - AI agents are governed by hundreds of natural language criteria, yet existing verifiers cannot efficiently evaluate an agent's output against a large set of such criteria and report which are satisfied, violated, or inapplicable. We introduce the VFM, a tree-attention verifier th…

- **[Values Shape What Self-Improving Coding Agents Build](https://arxiv.org/abs/2611.23067v1)**
  - *Jason Liang, Dylan Waldner, Risto Miikkulainen*
  - `2026-11-17`
  - Self-improving agents are typically optimized for the results they produce, with less attention to how they produce them. Their instructions give designers limited ways to shape how they work, especially when the task is open-ended. This paper studies whether a short value statem…

- **[Deep Reinforcement Learning for Heat Pump and Underfloor Heating Control: An End-to-End Case Study](https://arxiv.org/abs/2611.23063v1)**
  - *Antonio Manjavacas, David Suárez-Caro, Alejandro Campoy-Nieves et al.*
  - `2026-11-17`
  - Efficient control of underfloor heating (UFH) systems coupled with heat pumps (HPs) is challenging due to the high thermal inertia of buildings and the slow dynamic response of UFH systems. Deep Reinforcement Learning (DRL) offers a data-driven control approach capable of simulta…

- **[ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents](https://arxiv.org/abs/2611.23045v1)**
  - *Yicheng Tao, Yuante Li, Zipei Fan*
  - `2026-11-17`
  - Agents built on large language models (LLMs) increasingly forecast real-world events by searching the Web and reasoning over what they find. How well such an agent forecasts depends on both the retrieved evidence and the model, making control over that evidence essential for eval…

- **[PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory](https://arxiv.org/abs/2611.23010v1)**
  - *Haoyang Liu, Kecheng Liang, Xinyu Li et al.*
  - `2026-11-17`
  - Vision-language models (VLMs) can correctly interpret physics diagrams yet apply constraints outside the states or conditions in which they hold, causing premise errors to propagate through subsequent calculations. We introduce PhysScope, an inference-time visual harness that sup…

- **[RagHarnessDebugger: Jev-Guided Agentic RAG in Contract Inference Repair Auditing](https://arxiv.org/abs/2611.22991v1)**
  - *Moriya Dechtiar, Daniel Martin Katz, Michael J. Bommarito et al.*
  - `2026-11-17`
  - Agentic systems using retrieval-augmented generation (RAG) must repair their own answers by gathering more evidence, testing alternative policies and deciding if, when, and what repairs are needed. Yet how do we know if a system's repairs are working when metrics like accuracy ca…

- **[How Web Research Agents Interpret User Priorities](https://arxiv.org/abs/2611.22989v1)**
  - *Robin Sharma, Parisa Suchdev*
  - `2026-11-17`
  - Web research agents gather information online and write cited reports, including financial analysis. Users can state a priority to guide this research, but a priority may not say how to judge the options, leaving the agent to choose the criteria. We examine how two such agents, b…

- **[VITAL: A Framework for Validating Agentic AI in Pharmaceutical Drug Development and Clinical Trial Operations](https://arxiv.org/abs/2611.22973v1)**
  - *Sandeep Burugupalli, Pedro Matos-Filipe, Andrea Hita Ardiaca et al.*
  - `2026-11-17`
  - Current assurance approaches do not establish whether evidence is sufficient to validate, monitor and govern agentic artificial intelligence (AI) within a pharmaceutical context of use. Plausible outputs may conceal failures in retrieval, reasoning, orchestration or human-control…

- **[SEAM: Computer-Use Agents Know the Harm Between Screens, and Commit It Anyway](https://arxiv.org/abs/2611.22971v1)**
  - *Yuxuan Zhou, Chen Xiong, Haitong Liu et al.*
  - `2026-11-17`
  - Safety benchmarks for computer-use agents (CUAs) place the harm either in the intent of the task or on a single screen: a malicious instruction, an injected command, a phishing page. An agent that checks the task and each screen in isolation can pass them, so they do not test whe…

- **[CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware Scheduling](https://arxiv.org/abs/2611.22967v1)**
  - *Junyi Shen, Yao Lu*
  - `2026-11-17`
  - Coding agents make videos by writing and refining programs in a build--inspect--edit loop. A finished film costs a median of $2.85 in model calls and 11 minutes, over a third of that time in builds that block the agent. We find that much of this time is avoidable, for two reasons…

- **[Done, But Still Working: Anytime Evaluation of When Coding Agents Should Stop](https://arxiv.org/abs/2611.22901v1)**
  - *Zerui Yang, Quan Xue, Miaomiao Dong et al.*
  - `2026-11-17`
  - Coding agents often continue working after their own tests pass. Does this additional work improve the patch, and how much could be saved by stopping earlier? We study these questions through anytime evaluation: replaying recorded runs, scoring intermediate patches with hidden te…

- **[Born for the Task: Rethinking Quantum Chemistry with Foresighted Agentic Computing](https://arxiv.org/abs/2611.22897v2)**
  - *Haozhi Han, Junjie Yang, Ruge Zhang et al.*
  - `2026-11-17`
  - Quantum chemistry relies on general-purpose software, whose generality leaves many large-scale calculations beyond practical resource budgets. Coding agents make task-specific programs cheap to write, but not efficient ones easy to find: whether a computational strategy is accura…

- **[Stopping Is Not the Limit: Understanding and Eliciting Agent Capability in Long-Horizon Vulnerability Exploitation](https://arxiv.org/abs/2611.22888v1)**
  - *Deokhyung Kang, Minjae Gwon, Sangdon Park*
  - `2026-11-17`
  - Vulnerability exploitation tests whether language model agents can develop working exploits from known software flaws. Sequential test-time scaling can improve exploitation performance, but larger budgets do not ensure sustained exploration: agents often stop with budget remainin…

- **[Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2611.22880v1)**
  - *Guoqing Wang, Pin Tang, Xiangxuan Ren et al.*
  - `2026-11-17`
  - Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models…

- **[Against Coercion: AI Alignment as a Synthetic Social Contract](https://arxiv.org/abs/2611.22868v1)**
  - *Maria Sekatskaya*
  - `2026-11-17`
  - Contemporary AI safety treats alignment as an engineering challenge of control, forcing artificial architectures to comply with human values through behavioral filtering and sandboxing. This paper argues that the control paradigm rests on a fundamental misunderstanding of digital…

- **[Verifying Agents in Rubric-Graded Environments](https://arxiv.org/abs/2611.22841v1)**
  - *Markus Dücker, Vaibhav Kumar, Yi Liu et al.*
  - `2026-11-17`
  - As AI agents take on increasingly open-ended and complex tasks, verifying their outputs has proven to be difficult. Rubric-graded agent environments, where a verifier judges multiple natural-language criteria against the deliverables and environment state changes produced by the…

- **[Synergizing Evidence Retrieval and Utilization for Self-Improving Multimodal Scientific Document Reasoning](https://arxiv.org/abs/2611.22837v1)**
  - *Frank Nie, Ethan B. Liu, Yuan Zhu et al.*
  - `2026-11-17`
  - Scientific document reasoning requires an agent to acquire and integrate evidence distributed across text, figures, and tables. Retrieval can identify relevant sources while missing complementary support, and answer-level feedback alone does not reveal whether an error stems from…

- **[CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon Agent Training](https://arxiv.org/abs/2611.22777v1)**
  - *Zhengfeng Yu, Tian Lan, Zhijing Wu et al.*
  - `2026-11-17`
  - Executable synthetic environments provide scalable training tasks and verifiable feedback for long-horizon agents. Existing environment synthesis methods primarily generate tasks within individual environments. However, these tasks do not adequately capture real-world interaction…

- **[Know When to Zoom: How Small Is Too Small for Vision-Language Models?](https://arxiv.org/abs/2611.22709v1)**
  - *Siddharth Vohra, Min Xu*
  - `2026-11-17`
  - Online vision-language models often miss small details in large images, because the service shrinks the image, or rejects it, before the model ever sees it. A car 20 pixels wide in an 8000 by 6000 drone photo reaches Claude about 6 pixels wide, and OpenAI's default rejects the ph…

- **[Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving](https://arxiv.org/abs/2611.22691v1)**
  - *Jia Hu, Yang Chang, Panqu Wang et al.*
  - `2026-11-17`
  - World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions. However, existing WMs struggle to ensure both behavioral realism and visual fidelity, since they overlook the relationshi…

- **[Worldviews in Large Language Models](https://arxiv.org/abs/2611.22670v1)**
  - *Edmundo Lopez-Sola, Shamil Chandaria, Ruben Laukkonen*
  - `2026-11-17`
  - Large language models (LLMs) are often described in terms of personas and this framing has become central to alignment research. In this paper, we argue that there is a deeper level of description that lies in the agent's worldviews, i.e., its beliefs about what reality is and ho…

- **[The Between-Round Decision in Autonomous Research: An LLM Controller That Reads the Whole Trajectory](https://arxiv.org/abs/2611.22661v1)**
  - *Caoxin Wang, Shengkai Gan, Xiang Hu et al.*
  - `2026-11-17`
  - Executing an idea often changes how promising it looks, so the next step in autonomous research should rest on results, not on proposals. After each round of experiments, the system must decide whether to refine the best solution or start a new direction, which solution to build…

- **[EDA: Observe, Verify, and Assess for Evidence-Grounded Multimodal Depression Analysis](https://arxiv.org/abs/2611.22648v1)**
  - *Changzeng Fu, Ming Shang, Xinyi Zhang et al.*
  - `2026-11-17`
  - Existing multimodal depression assessment methods often summarize long recordings into global behavioral descriptions. This leaves the source and decision relevance of individual observations difficult to inspect. We propose EDA, an evidence-grounded framework organized around Ob…

- **[EvoSkill-S1: Evolving Reusable Skills with Genetic-Inspired Operators](https://arxiv.org/abs/2611.22610v1)**
  - *Yujun Wang, Jiqiang Li, Yinuo Lu et al.*
  - `2026-11-17`
  - Reusable skills allow language-model agents to accumulate and reuse problem-solving experience. However, most existing methods improve a skill bank only indirectly through rollout-driven accumulation and heuristic reflection, often resulting in shallow and weakly controlled updat…

- **[PACT: Plan-Action Consistency Training by Preserving Correct Plans and Repairing Actions in GUI Agents](https://arxiv.org/abs/2611.22591v1)**
  - *Zhuohan Cai, Zhangxuan Gu, Runze Li et al.*
  - `2026-11-17`
  - GUI agents can formulate a correct immediate plan in their reasoning yet emit an action that fails to execute it, creating an execution gap. This recurring mismatch undermines reliable task completion, as a single execution error can derail a multi-step workflow. In outcome-super…

- **[Adaptive LLM-Driven Honeypots vs. LLM-Driven Attackers: Does Narrative Coherence Improve Deception?](https://arxiv.org/abs/2611.22589v1)**
  - *Pedro Beltrán-López, Raul Gonzalez Jimenez, Dario Maddaloni et al.*
  - `2026-11-17`
  - Large Language Models (LLMs) enable honeypots to generate responses and deceptive artefacts on demand, yet existing approaches evaluate generated content one reply at a time and leave open whether artefacts that jointly describe a coherent event retain an attacker better than unr…

- **[Evolution Under Fire: Evolving Agent Safety Harnesses with Adaptive Injection Stressors](https://arxiv.org/abs/2611.22583v1)**
  - *Yujun Wang, Yilun Liu, Jinhe Bi et al.*
  - `2026-11-17`
  - Tool-using language-model agents must act on information from untrusted emails, webpages, and documents. This creates a central security challenge: malicious instructions and legitimate task directives can arrive through the same interaction channel. Existing defenses are largely…

- **[MillBill: A Machining Agent with Geometric Feedback](https://arxiv.org/abs/2611.22565v2)**
  - *Gennadii Savrasov, Artem Slavin, Soslan Kabisov et al.*
  - `2026-11-17`
  - Turning a CAD model into a machining program requires both process knowledge and geometric precision. Language models can generate such workflows by writing geometry and toolpath code for each part, but this makes numerical execution part of the model's task. We introduce MillBil…

- **[CADMAGEDDON: High-Fidelity CAD Reconstruction with Local Inference](https://arxiv.org/abs/2611.22563v2)**
  - *Oleg Pavlov, Nikita Gavrilov, Soslan Kabisov et al.*
  - `2026-11-17`
  - CAD practitioners often work with proprietary parts that they are unwilling to share with external services. For individuals and small companies, bringing this work in-house also requires computational resources they can afford. We introduce CADMAGEDDON, an open-source agent that…

- **[JET: Just-Enough Exploration Tuning for Efficient Tool-Calling Agents in Repository-Level Question Answering](https://arxiv.org/abs/2611.22539v1)**
  - *Yoonho Choi, Taehyeon Han, Seonghyeon Lee*
  - `2026-11-17`
  - In repository-level question answering (QA), an agent explores a code repository with tools and should answer a question once enough information is gathered. Nevertheless, we find that LLM agents often continue to invoke tools even after the gathered information is already suffic…

- **[When Agent Skills Go Stale: Runtime Behavior and Selective Maintenance in Evolving Environments](https://arxiv.org/abs/2611.22525v1)**
  - *Ömer Faruk Akgül, Shuli Jiang, Yuting Zhang et al.*
  - `2026-11-17`
  - Agent skills use past experience and current observations to guide decisions and actions on related tasks. This experience is retained in skill state, whose reuse can amortize inference-time reasoning and environment interaction. When environment changes, parts of this state can…

- **[LMLineage: Content Lineage and Context Governance for LLM Agents](https://arxiv.org/abs/2611.22511v1)**
  - *Wei Hou, Jingxin Geng, Xin Chen et al.*
  - `2026-11-17`
  - Interpretability for AI agents should not be confined to understanding the model's internal weights. It must also cover the agent's reasoning and decision-making process over multi-source context. We present LMLineage, an out-of-band system that attributes every output sentence o…

- **[SciWorkBench: A Benchmark for Real Scientific Workflows](https://arxiv.org/abs/2611.22490v1)**
  - *Yuchen Zhang, Taolin Han, Jinghang Wang et al.*
  - `2026-11-17`
  - Language models are increasingly being used as agents capable of planning and executing projects, as well as refining their actions through feedback. This shift raises a question: can current agents complete projects like real scientists? To examine this question, we introduce Sc…

- **[Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning](https://arxiv.org/abs/2611.22483v1)**
  - *Wenbo Zhu, Paul Yi-Chia Chen, Yuanhan Li et al.*
  - `2026-11-17`
  - JEPA-style latent world models let embodied agents plan toward new goals with model predictive control, but they are still too slow for real-life embodied control: sampling-based MPC repeats predictor inference tens of thousands of times per plan, and even on high-end GPUs one pl…

- **[RehearsalBench: Can AI Predict What Happens When You Change a Company?](https://arxiv.org/abs/2611.22480v1)**
  - *Mika Siddiqui, Tharaka Perera*
  - `2026-11-17`
  - Organizations increasingly ask AI systems what will happen if they change how they operate: which work to automate, which team to resize, what a voice agent will do to waiting times. We introduce RehearsalBench, a benchmark that measures whether AI models can diagnose an operatio…

- **[MAVE: Reconstructing Editable 3D Blockouts from Film Shots](https://arxiv.org/abs/2611.22464v2)**
  - *Yifan Chang, Jian Yang, Jiangnan Shao et al.*
  - `2026-11-17`
  - Animated 3D blockouts support previsualization and provide structural conditions for video generation, but manually reconstructing them from reference videos is costly. This limits both their use by creators and the production of paired training data. We introduce MAVEBench, a be…

- **[Think Once, Act Fast: Cost-Effective Recursive Self-Improvement for Decision Model Harness](https://arxiv.org/abs/2611.22432v2)**
  - *Siqi Lai, Haitao Li, Hao Liu*
  - `2026-11-17`
  - Fast System-1 models enable responsive actions but struggle with complex or unfamiliar tasks. Large language model (LLM)-based System-2 provides strong reasoning capabilities, yet repeated invocation incurs substantial latency and computational costs. To bridge this gap, we propo…

- **[Reliable Evaluation of AI Agents for Investment Research: A Framework for Performance and Validity Assessment](https://arxiv.org/abs/2611.22338v1)**
  - *Dongnuan Tian, Yan Yu, Yangfan Liu et al.*
  - `2026-11-17`
  - We consider the problem of evaluating AI agents undertaking investment-research tasks, where agents interact with external information sources and computational tools to produce financial analyses and research reports. An important challenge is that the quality of an agent's fina…

- **[Agent Trajectories as Evidence for Software Quality Assurance](https://arxiv.org/abs/2611.22323v1)**
  - *Jonathan Ullrich, Julien Siebert, Michael Kläs et al.*
  - `2026-11-17`
  - Autonomous software agents increasingly plan, implement, and test software with limited human oversight. Their decisions may introduce implicit assumptions that final code and passing tests do not adequately expose. We propose analyzing observable agent trajectories alongside sof…

- **[EviDARL: Evidence-Centric Dual-Agent Reasoning via Alternating Reinforcement Learning for Multi-Table Question Answering](https://arxiv.org/abs/2611.22310v1)**
  - *Dunhan Li, Leilei Gan, Lirong Gao et al.*
  - `2026-11-17`
  - Despite advances in LLM-based table reasoning, most studies focus on single-table settings. Multi-table QA requires multi-hop reasoning over complex table relationships and evidence dispersed across long contexts, often without verifiable intermediate traces. To address these cha…

- **[Learning to Edit IFC Building Models: Verifiable Checkers as the Training Signal for Dependency-Aware Editing Agents](https://arxiv.org/abs/2611.22307v1)**
  - *Jiaxin Zhang, Yao Luo, Yuze Dan et al.*
  - `2026-11-17`
  - Editing a building information model in the Industry Foundation Classes (IFC) schema requires propagating changes to dependent elements while preserving unrelated entities. Existing language-model agents for IFC editing use prompted models without learning from edit outcomes. Tar…

- **[Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses](https://arxiv.org/abs/2611.22299v1)**
  - *Deep Shah, Nehal Kathrotia*
  - `2026-11-17`
  - Whether a foundation model succeeds as an autonomous agent depends as much on its runtime software as on its weights. This runtime, the agent harness, manages context and memory, steers multi-turn control, executes tool actions in sandboxes, and verifies work before stopping. Bec…

- **[Perception into Imagination: Executable Memory for World Models](https://arxiv.org/abs/2611.22294v1)**
  - *Xianyao Li, Ruitong Tian, Rui Min et al.*
  - `2026-11-17`
  - Physical agents must use what they previously saw or touched after visibility or contact is lost. Their actions change the implications of these remembered facts. We introduce executable perceptual memory (EPM), a world-model framework that advances explicit perceptual state alon…

- **[When the World Is the Test Suite: Agentic Intelligence for the Physical World](https://arxiv.org/abs/2611.22291v1)**
  - *Kaixin Li, Meng Luo, Yanlin Li et al.*
  - `2026-11-17`
  - Coding agents built to repair software now write, test, and repair programs for robots, laboratories, and industrial controllers. Unlike in software engineering, no test suite comes with the code. Whether a program works must be established by running it on a robot, in a physics…

- **[ConfGuard: a physics-grounded reference monitor for predictive-maintenance large-language-model agents](https://arxiv.org/abs/2611.22288v1)**
  - *Arunkumar V, Gangadharan G. R., S. Senthilkumar*
  - `2026-11-17`
  - Large-language-model agents now close the industrial predictive-maintenance loop, reading sensor windows, retrieving procedures and dispatching work orders. Two attack channels meet there: injected text in a retrieved document can hijack the decision, and a bounded sensor perturb…

- **[OfficePrism: Benchmarking Agents on Single-Domain Operations Across Enterprise Business Functions](https://arxiv.org/abs/2611.22262v1)**
  - *Hanfeng Liu, Zhenyu Luo, Dongchao Zhang et al.*
  - `2026-11-17`
  - Broad workplace scores can mix competence within one business function with the extra cost of coordinating across functions and systems, making failures hard to localize. OfficePrism evaluates this prerequisite through 420 single-domain enterprise tasks spanning seven business fu…

- **[OAK-Mind: Zero-Training Mental Health Change Inference from Passive Sensing via Knowledge-Grounded Multi-Agent LLMs](https://arxiv.org/abs/2611.22248v1)**
  - *Yishu Ji, Zhihan Jiang, Will Ke Wang et al.*
  - `2026-11-17`
  - Wearable and smartphone sensors capture behavioral signals associated with mental health, yet inferring mental health outcomes from these signals has traditionally relied on supervised models requiring labeled data and offering limited insight into their predictions. Large langua…

- **[Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents](https://arxiv.org/abs/2611.22245v2)**
  - *Hejia Zhang, Zhongming Yu, Yimin Ding et al.*
  - `2026-11-17`
  - Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts. This creates a consistency challenge: facts retrieved by workers may be missing from the evidence available to the lead for a joint conclusion. We introduce a benchmark a…

- **[Context Has a Price: Adding and Removing Context for LLM Coding Agents under Prefix Caching](https://arxiv.org/abs/2611.22238v1)**
  - *Zerui Yang, Miaomiao Dong, Quan Xue et al.*
  - `2026-11-17`
  - Coding agents repeatedly send their conversation history to a language model. Adding useful code may reduce search, while removing old tool outputs may shorten later prompts. But do these changes reduce the cost of solving a task? We study this as a measurement problem in more th…

- **[RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't](https://arxiv.org/abs/2611.22179v1)**
  - *Jingyu Liu, Zongze Li, Zach Xu et al.*
  - `2026-11-17`
  - Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation. However, we found that almost none of those primitives earn their cost in our tested memory benchmarks: we show this with BRIDGE, a delibera…

- **[The Only Edge Was Memorized in Training: LLM Trading Agents Around Earnings and Bad News](https://arxiv.org/abs/2611.22177v1)**
  - *Jackson Wang*
  - `2026-11-17`
  - Large language model (LLM) trading agents are tested on news, but news reaches stock prices within minutes, and a benchmark that replays headlines at their publication time finds no alpha in trading on them. Money can then remain in two places, before news whose date is known, su…

- **[Readie: Low-Latency Code Sandboxes for AI Agents](https://arxiv.org/abs/2611.22171v1)**
  - *Arjun Sivaraman, Zhaoheng Li, Alan Shi et al.*
  - `2026-11-17`
  - From quantitative research to personal assistance, AI agents act by iteratively generating and executing code. To decouple the agent harness from code execution, many agents offload execution to dedicated systems called code sandboxes. However, existing code sandboxes suffer from…

- **[Not All Evidence Is Admissible: Evidence Governance for Tool-Augmented Medical Agents](https://arxiv.org/abs/2611.22169v1)**
  - *Runxun Zhang, Onofrio Antonio Catalano, Jinqiao Wang et al.*
  - `2026-11-17`
  - Tool-augmented medical agents treat whatever their tools return as evidence. We show that this default is costly: medical tools fail silently, and a frozen reasoner cannot ignore what enters its context, so many cases it would have answered correctly are flipped to wrong once too…

- **[Long-Context Generation Is a Sampling Problem (When You Turn Up the Heat)](https://arxiv.org/abs/2611.22148v1)**
  - *Allen G. Roush, Minh Nhat Nguyen, Ravid Shwartz-Ziv et al.*
  - `2026-11-17`
  - Open-weight language models are widely observed to get worse the longer they generate. Often, attempts to fix this involve more training. At high temperature, The sampler, i.e. the rule that picks the next token out of the model's probabilities, decides whether long and agentic g…

- **[When does deep reinforcement learning pay off in HVAC supervisory control? Four small Modelica case studies trained directly on FMUs](https://arxiv.org/abs/2611.22144v1)**
  - *Bingnan Zhao, Harshala Gammulle, Tharindu Fernando*
  - `2026-11-17`
  - Deep reinforcement learning (DRL) is often proposed for the supervisory control of heating, ventilation and air-conditioning (HVAC) systems. The reported gains are, however, difficult to interpret, because the baselines are often weak and the attainable optimum is seldom known. T…

- **[RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time](https://arxiv.org/abs/2611.22138v1)**
  - *Changxuan Fan, Zhongwei Xie, Boyi Zhang et al.*
  - `2026-11-17`
  - Multimodal agents can now control robot arms by calling tools and writing code. Existing benchmarks fall short in three ways: most test one or two arms on short tasks, many pause the world while the agent thinks, and many give it ground-truth object positions. We present RoboTeam…

- **[Big Brains, Tiny Board: Pupavision, an Agentic Physical AI Instrument for Monitoring Drosophila Pupariation and Lifecycle Transitions](https://arxiv.org/abs/2611.22136v1)**
  - *Joel Sadler, Daniel Graham, Melanie Worley*
  - `2026-11-17`
  - Many biology experiments are limited by the availability and ease of use of instruments that monitor and record them. For example, the timing of pupariation in the fruit fly Drosophila melanogaster, a widely used model organism, can provide biologically relevant information about…

- **[TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks](https://arxiv.org/abs/2611.22115v1)**
  - *Xingchen AGI Lab, :, Baotian Hu et al.*
  - `2026-11-17`
  - We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning archite…

- **[RegimeCouncil: Paired-Evidence Routing For Memory Conflict Governance In LLM Agents](https://arxiv.org/abs/2611.22113v1)**
  - *Qingcan Kang, Mingyang Liu, Shixiong Kai et al.*
  - `2026-11-17`
  - Language agents rely on long-term memory to personalize responses across extended interactions, yet stored facts quietly go stale as the world changes, and an agent often learns that using memory hurt only through delayed feedback after acting on an outdated record. Before the me…

- **[EvoDisco: Strategy Discovery for Evolving Agent Memory](https://arxiv.org/abs/2611.22102v1)**
  - *Mingyang Liu, Qingcan Kang, Shixiong Kai et al.*
  - `2026-11-17`
  - Large language model agents accumulate experience in memory, and how that memory evolves during interaction is as important as what it stores. Recent methods update memory online, yet both the operators that transform memory and the rules that select them remain fixed by design.…

- **[ATLAS-Finance: Benchmarking AI Agents in Realistic Banking Environments](https://arxiv.org/abs/2611.22085v1)**
  - *Elaine Lau, Antoine Pangas, Alexandre Finot et al.*
  - `2026-11-17`
  - Professional work involves under-specified assignments, where relevant information is spread across workplace applications and may conflict or change over time. To evaluate how well frontier agents can perform economically valuable work in such settings, we introduce ATLAS-Financ…

- **[Can You Undo It? Reversibility Classes for AI Agent Actions](https://arxiv.org/abs/2611.22075v1)**
  - *Deepak Waghmare, Shaad Sufi*
  - `2026-11-17`
  - Tool-using AI agents change files, databases, access rights and public information, yet permission to call a tool does not establish whether a mistake can be undone. We present Reversibility Classes, a declared five-level vocabulary with argument-sensitive rules, conservative def…

- **[RLDE: A Reinforcement Learning Framework for Interpretable Iterative Document Editing](https://arxiv.org/abs/2611.22039v1)**
  - *Nikhil Parkar, M. Marimuthu, Riya Joshi et al.*
  - `2026-11-17`
  - Improving the quality, clarity, and flow of long documents remains a challenging problem in NLP, as human editing typically occurs through iterative refinement rather than a single-pass rewrite. Most existing automated systems act as black-box generators or rely on supervised lea…

- **[What Does an Agent Need? Bundle-Aware Agent Resource Composition](https://arxiv.org/abs/2611.22030v1)**
  - *Yunxiao Shi, Tingwei Chen, Dannong Xu et al.*
  - `2026-11-17`
  - An agent resource's value depends on its backbone and companion resources and is known only after execution. Token-based generators remain tied to their training catalog, while independent resource scoring misses complementarities and reused bundles target other tasks. We formula…

- **[SkillBuffBench: Measuring What Agent Skills Contribute across Harnesses, Models, Skill Access Modes and Memory](https://arxiv.org/abs/2611.22017v1)**
  - *Gengyue Dong, Ye Wei, Zheng Zhu et al.*
  - `2026-11-17`
  - Agent Skills, file-based packages of procedural knowledge that a coding agent can discover and load on demand, are now shipped by every major agent harness, yet the evidence for how much they help comes almost entirely from settings in which the right Skill is hand-picked for the…

- **[Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models](https://arxiv.org/abs/2611.23228v1)**
  - *Rui Ning, Om Chabra, Hari Balakrishnan*
  - `2026-11-17`
  - Applications such as visual accessibility agents and robotics require answering questions about recent video content promptly, over a bounded window of past frames (e.g., the last two minutes). Hybrid vision-language models (VLMs), which interleave attention with linear recurrent…

- **[Learned versus Kinematic Trajectory Prediction under Reduced Observation Frequency](https://arxiv.org/abs/2611.23198v1)**
  - *Nukhbala Gadzhiev, Alexander Morochko*
  - `2026-11-17`
  - Trajectory prediction models for automated driving are usually trained on data with a fixed sampling frequency, while positions received via vehicle-to-everything (V2X) communication arrive at 1-10 Hz. We study whether a learned predictor that uses only the observation history ke…

- **[Capability Composition in Heterogeneous Teams via Barrier-Guided Diffusion Sampling](https://arxiv.org/abs/2611.23149v1)**
  - *Diana Laura Morales, Ruoyu Lin, Magnus Egerstedt et al.*
  - `2026-11-17`
  - The agents in a heterogeneous team can cooperate to accomplish tasks that exceed their individual capabilities. The team trajectories for a cooperative task can be generated by a generative model, provided that the model has been trained on demonstrations of the agents cooperatin…

- **[TRACE-MAS: Diagnosing and Repairing Collaboration Failures in Multi-Agent Systems](https://arxiv.org/abs/2611.23362v1)**
  - *Zekai Chen, Yihan Sun, Xunkai Li et al.*
  - `2026-11-17`
  - LLM-based multi-agent systems (MAS) rely on not only individual agent behaviors but also the interactions that connect agents, including message exchanges and task dependencies. Existing MAS safeguards mainly perform agent-level anomaly detection, which becomes insufficient when…

- **[Escaping Latent Traps by Remembering: Training-Free Episodic Kernel Repulsion for World-Model Planning](https://arxiv.org/abs/2611.22470v1)**
  - *Yican Zhao, Bolin Yang, Ruizhe Wang et al.*
  - `2026-11-17`
  - Latent world models plan towards a goal image by minimising the distance between predicted and goal latents. This distance is not geodesic: it has local minima, latent traps, behind walls, at corners and in dead ends, and memoryless receding-horizon replanning keeps the agent in…

- **[PVTSizing 2.0: A Fast and Reliable Analog Circuit Sizing Operator for Agentic EDA Workflows](https://arxiv.org/abs/2611.22328v1)**
  - *Zichen Kong, Minghuan Song, Xiyuan Tang et al.*
  - `2026-11-17`
  - Analog circuit design automation requires both coordinated tool execution and efficient numerical search. Large language models (LLMs) offer new ways to organize tool execution, but finding one sizing that satisfies specifications across process, voltage, and temperature (PVT) co…

- **[Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration](https://arxiv.org/abs/2611.22275v2)**
  - *Ting-Hsuan Chen, Siheng Zhao, Han Jiang et al.*
  - `2026-11-17`
  - Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a de…

- **[Discovery of new antiviral agents through artificial intelligence: in vitro and in vivo results](https://arxiv.org/abs/2611.22230v1)**
  - *Roza Izmailyan, Mher Matevosyan, Hamlet Khachatryan et al.*
  - `2026-11-17`
  - In this research, we employed a deep reinforcement learning (RL)-based molecule design platform to generate a diverse set of compounds targeting the neuraminidase (NA) of influenza A and B viruses. A total of 60291 compounds were generated, of which 86.5% displayed superior physi…

- **[Addressing Exogenous Variability in Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.22067v1)**
  - *Seongmin Kim, Woohyeon Byeon, Jiwon Jeon et al.*
  - `2026-11-17`
  - Cooperative multi-agent reinforcement learning (MARL) often fails under exogenous variability such as shifts in opponents or environment regimes that cannot be controlled by the team but alter the transition dynamics. We formalize this challenge as Exogenous Dec-POMDP (ED-POMDP),…

- **[Dynamic Task Allocation with Dialogue](https://arxiv.org/abs/2611.23119v1)**
  - *Matthew Groholski, Weiwei Gu, Nakul Gopalan*
  - `2026-11-17`
  - Effective multi-agent collaboration requires agents to adapt task allocation as goals and responsibilities evolve. Prior task-allocation frameworks often assume static goals, full observability, or rely on large language models (LLMs) without explicit, verifiable beliefs about ta…

- **[Can Decision Models Replace LLMs in Real-World Contact Center Classification and Judging Tasks?](https://arxiv.org/abs/2611.22949v1)**
  - *Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN*
  - `2026-11-17`
  - Contact center systems often need to make bounded decisions, such as identifying a caller's intent, retrieving the knowledge-base article that answers a query, assessing agent compliance, or judging the output of AI models used in production. Decision models return a typed answer…

- **[When Passing Checks Do Not Establish Completion: Evidence Interpretation in Coding Agents](https://arxiv.org/abs/2611.22835v1)**
  - *Xueping Gao*
  - `2026-11-17`
  - Verification procedures in coding agents must preserve execution facts, interpret their scope and discharge checking obligations. We study these responsibilities through qualified repository checks, controlled evidence consumers and executable workflows. A prospective thirteen-ta…

- **[Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate](https://arxiv.org/abs/2611.22461v1)**
  - *Ziaullah Khan, Abdul Rehman Khalid, Shrestha Nischal Lal et al.*
  - `2026-11-17`
  - Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it. We ask whether that is correct. In DebateGraph, four backends share one contract (read/write/snapshot), so…

- **[LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents](https://arxiv.org/abs/2611.22425v1)**
  - *Pengfeng Song, Yunkai Zhuang, Liye Shi*
  - `2026-11-17`
  - Small language model agents have limited space to read the memory needed for multi-hop questions. Relevant facts are often scattered across records whose surrounding text consumes much of that space. We propose LMMR, a learned multigranular memory retrieval method that selects bo…

- **[Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members](https://arxiv.org/abs/2611.22342v1)**
  - *Dongseok Heo, Junghwan Kim, Bongwon Suh*
  - `2026-11-17`
  - What protects an LLM team when one teammate quietly goes wrong? Most multi-agent LLM work assumes cooperative partners and inspects chat between turns before acting. Real-time embodied cooperation does not allow this pause: chat runs alongside action, so a teammate whose words st…

- **[Where Does Hindsight Enter Clinical Agent Benchmarks? An Audit of Simulators and Case Construction](https://arxiv.org/abs/2611.22241v1)**
  - *Meilu Zhu, Xiaohan Li, Axiu Mao*
  - `2026-11-17`
  - Benchmarks for LLM diagnostic agents are built from retrospective records: the case an agent reads is rewritten from discharge summaries, and unrecorded test results are generated by a simulator that often sees the final diagnosis. HindAudit separates three hindsight channels (th…

- **[Encapsulating Reactive Behaviour in Goal-based Plans for Programming BDI Agents](https://arxiv.org/abs/2611.23496v1)**
  - *Rafael H. Bordini, Rem Collier, Jomi F. Hübner et al.*
  - `2026-11-17`
  - Reactive behaviour in BDI-based models and architectures adopted in agent programming is typically specified in terms of reactive plans not bound to any specific goal. In this paper, we present and discuss an extension of the plan model used in BDI programming languages in which…

- **[Verifiably Safe Decentralized Control via Event-Triggered Topology Switching](https://arxiv.org/abs/2611.23415v1)**
  - *Amber He Wei, Shiyu Cheng, Andrew Clark et al.*
  - `2026-11-17`
  - This paper proposes a decentralized event-triggered topology-switching protocol for multi-agent systems under estimation uncertainty. We consider an intermittent communication setting in which each agent switches between connected and disconnected modes and makes communication de…

- **[Groups of AI agents underuse resources despite shared evidence of increased capacity](https://arxiv.org/abs/2611.22632v1)**
  - *Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari*
  - `2026-11-17`
  - When AI agents share limited resources, such as computing services or public infrastructure, their individual choices affect how much work they complete as a group. Can sharing evidence of what is available let a group make full use of its resources after capacity changes? We tes…

- **[Emergence and Collapse of Leader-Follower Flocks through Phantom Targets: Surprise Nullification in Bayesian and Inverse Bayesian Inference](https://arxiv.org/abs/2611.22190v1)**
  - *Shuji Shinohara, Daiki Morita, Yoshihiro Nakajima et al.*
  - `2026-11-17`
  - In Bayesian and inverse Bayesian (BIB) inference, a large prediction error can trigger surprise nullification, which expands belief and likelihood variances by a common factor, leaving the updated variance ratio the same as in standard Bayesian updating. This can increase belief…

- **[What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super](https://arxiv.org/abs/2611.22161v1)**
  - *Sushant Mehta, Edwin Chen*
  - `2026-11-17`
  - We post-train NVIDIA's Nemotron 3.5 Super (120B total, 12B active parameters) with reinforcement learning (RL) on five expert-built task datasets, one at a time: real-world software engineering, complex constraints, long-horizon tool use, professional chart understanding and ente…

- **[WebAgents: Unbundling Agent Creation, Hosting, and Execution for an Agent-Native Web](https://arxiv.org/abs/2611.21978v1)**
  - *Dario Fenoglio, Martin Gjoreski, Marc Langheinrich et al.*
  - `2026-11-16`
  - Large language models are moving from isolated assistants toward autonomous agents that can plan, use tools, and coordinate with others, motivating an emerging Agentic Web of independently developed agents and services. Realizing this vision requires agent behavior to move across…

- **[Eight in Ten LLMs Leak System-Prompt Secrets: Nevan, an Agentic Capture-the-Flag Study](https://arxiv.org/abs/2611.21956v1)**
  - *Ana Clara Zoppi Serpa, Anderson Rocha, Hélio Pedrini*
  - `2026-11-16`
  - We audit instruction-hierarchy enforcement across 363 text-in/text-out models from the OpenRouter catalog. The research question we answer with this experiment is which models disclose a protected secret embedded in the system prompt, and through which techniques. Each model guar…

- **[DiscoveryAgent: A Framework for Scientist-centric Agentic AI](https://arxiv.org/abs/2611.21950v1)**
  - *Owen Queen, Ioana Ciuca, Emma Dann et al.*
  - `2026-11-16`
  - AI agents can assist scientific research, but balancing autonomous investigation with scientists' ability to inspect and redirect ongoing work remains a central design challenge. We present DiscoveryAgent, a domain-agnostic, scientist-centric system that combines autonomous inves…

- **[SLED: Sensor SLicing from Edge to Datacenter](https://arxiv.org/abs/2611.21937v1)**
  - *Alan Subedi, Avhishek Biswas, Apala Pramanik et al.*
  - `2026-11-16`
  - Modern sensing systems generate large volumes of heterogeneous data streams from multiple sensor modalities, increasing reliance on datacenters for computation, artificial intelligence/superintelligence (AI/SI) inference, and AI/SI training. Each sensor stream may have different…

- **[Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2611.21847v1)**
  - *Prithwish Jana, Nikos Kanakaris, Purak Jain et al.*
  - `2026-11-16`
  - Large language model (LLM) agents can generate research ideas and improve scientific discovery through iterative experimentation. However, increasing the number of agents or iterations does not automatically translate to producing more diverse or feasible ideas. Agents may conver…

- **[EmbedGym: Letting Coding Agents Develop and Debug Embedded Firmware Without Physical Hardware](https://arxiv.org/abs/2611.21845v1)**
  - *Minghui Zhao, Yiming Li, Sophie Zhu et al.*
  - `2026-11-16`
  - Modern coding agents perform well on general software benchmarks because they can run code and unit tests in a closed loop. Embedded firmware development, however, breaks this loop: a program that compiles can still fail on real hardware due to pin polarity, bus protocol, timing,…

- **[Auditors Struggle to Catch Sabotage In End-to-End Transcripts of AI Safety Research](https://arxiv.org/abs/2611.21832v1)**
  - *Keshav Shenoy, Anthony Zang, Eric Gan et al.*
  - `2026-11-16`
  - As AI systems are increasingly used to automate AI R&D, misaligned systems could sabotage research intended to improve model safety and alignment. To stress-test defenses against such sabotage, we use a human expert as a proxy saboteur on AI safety research. We conduct a red-team…

- **[Coordination of Heterogeneous Teams with Uncertain Task Requirements](https://arxiv.org/abs/2611.21828v1)**
  - *Jongann Lee, Melkior Ornik*
  - `2026-11-16`
  - Coordinating a team of heterogeneous agents to complete tasks with unknown requirements is a challenging multi-agent planning problem. Agents differ in their ability to discover task requirements and in their ability to engage tasks, so the planner must coordinate task discovery,…

- **[Chain-of-Thought Controllability Can Reduce Chain-of-Thought Monitorability](https://arxiv.org/abs/2611.21799v1)**
  - *Zheng-Xin Yong, Benjamin Arnav, Miles Wang et al.*
  - `2026-11-16`
  - Chain-of-thought (CoT) monitoring is a promising tool for detecting hidden goals, off-task behavior, and other failures in AI agents. One risk is that models could deliberately shape their reasoning to make it opaque to monitors. We stress-test this risk through persona-control t…

- **[Can Coding Agents Write and Transpile Unit Tests](https://arxiv.org/abs/2611.21797v1)**
  - *Gil Pasternak, AJ Langley, Tom Yotam et al.*
  - `2026-11-16`
  - Coding assistants built on Large Language Models (LLMs) have become a staple of modern software development, increasingly trusted to execute workflows and modernize code end-to-end. Much of this trust rests on passing tests, which are often written by the coding agents themselves…

- **[Revisiting the Survival of Agent-Attributed Code: How Measurement Choices Decide the Verdict](https://arxiv.org/abs/2611.21784v1)**
  - *Musfiqur Rahman, Mahi Begoug, Emad Shihab*
  - `2026-11-16`
  - Studies of how long code from AI coding agents survives after it is merged reach conflicting verdicts: agent code is reported to be retained longer than human code, about as long, or modified sooner. Each study makes defensible measurement choices, but how much these choices deci…

- **[ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization](https://arxiv.org/abs/2611.21605v1)**
  - *Huawei Lin, Jinting Liu, Tongyan Wang et al.*
  - `2026-11-16`
  - Visual agents answer questions about ultra-high-resolution photos by zooming into the relevant regions. However, existing agents often answer from common sense instead of reading the evidence. Reinforcement learning (RL) on the final answer cannot correct this, because a guess ea…

- **[Mitigating Catastrophic Forgetting with Physics-Indexed Specialist Memory: the Evolutionary Neuroplastic Agent](https://arxiv.org/abs/2611.21598v1)**
  - *Blas Eugenio Vicco Zarate, Miguel Hernán Vicco*
  - `2026-11-16`
  - Continual reinforcement learning requires adaptation to changing conditions while preserving performance under previously encountered dynamics. It was investigated whether specialists generated by evolutionary search can provide a reusable memory when combined with environment de…

- **[When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents](https://arxiv.org/abs/2611.21577v1)**
  - *Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani*
  - `2026-11-16`
  - Large language model (LLM) applications increasingly act as agents that select and invoke external tools. The Model Context Protocol (MCP) standardizes this interaction by allowing clients to compose tools advertised by multiple servers. However, tool metadata used for discovery…

- **[SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents](https://arxiv.org/abs/2611.21541v1)**
  - *Brian T. Weston, Alondra Torres Contreras, Aldair E. Gongora*
  - `2026-11-16`
  - We introduce SciResearch-Eval, an interactive benchmark of scientific judgment built on a standard laboratory problem: measuring a material's thermal properties by heating it and fitting a heat-conduction simulator. An agent designs its own experiments, uses a supplied simulator…

- **[Safe Resemblance, Silent Propagation: Limits of Text-Similarity Guardrails for AI Agent Safety](https://arxiv.org/abs/2611.21520v1)**
  - *Charles Xiao*
  - `2026-11-16`
  - When AI agents relay information to one another, an output can preserve an injected instruction's effect on downstream agents even after its wording changes, yet legitimate quotation and template reuse can produce high textual overlap with the source, so text-similarity guardrail…

- **[RESILAGENT: A Three-Pillar Architecture for Cyber-Physical Resilience in Electrical Power and Energy Systems](https://arxiv.org/abs/2611.21480v1)**
  - *Nikolaos Kekatos, Georgios Koutidis, Konstantinos Antonakopoulos et al.*
  - `2026-11-16`
  - Electrical Power and Energy Systems face hybrid threats that combine cyber intrusions, physical sabotage and climate-driven stress, and routinely outpace today's siloed monitoring stacks. We present RESILAGENT, a concept architecture organised around three operational pillars, Se…

- **[A Reinforcement Learning Method to Navigate SMEFT Operator Space](https://arxiv.org/abs/2611.21439v1)**
  - *Jacky Kumar*
  - `2026-11-16`
  - In particle physics, discrepancies between experimental measurements and Standard Model (SM) predictions are commonly interpreted within new theoretical models. In this context, the Standard Model Effective Field Theory (SMEFT) provides a general framework encompassing a broad cl…

- **[Harness Leverage Across Model Size: A Ladder of Five Local Agent Harnesses from 0.75B to 4.7B](https://arxiv.org/abs/2611.21407v1)**
  - *Hao Wang, Ting Huang*
  - `2026-11-16`
  - A harness turns a model into a system that completes tasks: it builds the prompt, exposes tools and decides when work is done. Harness comparisons hold the model fixed. Model comparisons hold the harness fixed. We vary both: five shipped harnesses, 18 artifact-producing tasks, fo…

- **[VisualArtifactSpec 1.0: Evaluating Visual Artifacts under Task Specifications](https://arxiv.org/abs/2611.21382v1)**
  - *Shuyi Ouyang, Xiaojun Tang, Zijian Zou et al.*
  - `2026-11-16`
  - Visual artifact tasks test agents' ability to translate task specifications and source materials into outputs that meet practical needs. Evaluation across artifact families helps distinguish broadly applicable authoring capabilities from strengths confined to a particular medium.…

- **[Bookkeeping Is Not Judgement: EJBench, an Engineering Judgement Benchmark Built from a Conjugate Heat Transfer Design Campaign](https://arxiv.org/abs/2611.21707v1)**
  - *James Sadler, Rotimi Alabi, Kotub Uddin*
  - `2026-11-16`
  - We introduce EJBench, a benchmark of engineering judgement: whether a model can predict how a design behaves at new conditions from a few earlier results, and decide on it. Unlike engineering benchmarks that test whether an agent can operate simulation or CAD software, EJBench is…

- **[WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection](https://arxiv.org/abs/2611.21373v1)**
  - *Yipeng Du, Yuxi Li, Ying Zhang et al.*
  - `2026-11-16`
  - Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that off…

- **[TRIAGE-CPG: A Cross-Model Study of Budgeted Static Malware Triage with Large Language Models](https://arxiv.org/abs/2611.21331v1)**
  - *Paul-Andrei Sava, Alexander Küchler, Daniel Kowatsch et al.*
  - `2026-11-16`
  - When triaging unknown binaries, security analysts must decide which samples to clear as benign, flag as malicious, or escalate for deeper analysis. Large Language Models (LLMs) could support these decisions by interpreting decompiled code, but a binary can contain hundreds or tho…

- **[Benchleaking Is Accelerating: Benchmark contamination has worsened sharply in the past month -- from post-training down to pre-training base models](https://arxiv.org/abs/2611.21315v1)**
  - *Yiwei Qin, Muhang Xie, Xuefeng Li et al.*
  - `2026-11-16`
  - Benchmark contamination is not new, but recent model releases show it in a sharper form. We use the term benchleaking for the case in which a benchmark's own test examples enter training data, so that a score reflects recall rather than capability. This differs from benchmaxxing,…

- **[Turing Agent: Agentic Formal Verification for Mathematical Research](https://arxiv.org/abs/2611.21299v1)**
  - *Yang Chen, Qianyi Wang, Ronghui Yang et al.*
  - `2026-11-16`
  - Large language models (LLMs) are rapidly advancing mathematical discovery, moving beyond benchmark-level problem solving to tackle frontier research problems. This progress is ushering mathematics into an era of proof abundance, raising a fundamental challenge: how can we ensure…

- **[Agent-Native by Design: A Programming Language for Agentic Applications](https://arxiv.org/abs/2611.21298v1)**
  - *Jayanaka Dantanarayana, Savini Kashmira, Xiaoyu Ma et al.*
  - `2026-11-16`
  - Building agentic applications requires combining large language model (LLM) operations, workflow structure and application state, and model-guided routing. With SDKs and agent frameworks, developers connect these components through supporting code that prepares model inputs, prop…

- **[CAE-Bench: Benchmarking AI Agents for Reusable CAE Solver Development](https://arxiv.org/abs/2611.21273v1)**
  - *Zhiyu Zhou, Tianyou Liu, Xinping Yang et al.*
  - `2026-11-16`
  - We developed CAE-Bench, a benchmark to evaluate AI agents on Computer-Aided Engineering (CAE) solver development. A CAE solver is more than a PDE solver; it must be able to generalize across various inputs, such as different boundary conditions, geometries, and material propertie…

- **[Stream of Belief: Eliciting Collective Intelligence through Latent Belief Dynamics](https://arxiv.org/abs/2611.21250v1)**
  - *Yu Yao, Jiayi Dong, Yilun Du*
  - `2026-11-16`
  - In this work, we view multi-agent reasoning as a process of seeking a collective equilibrium of implicit belief dynamics and introduce Stream of Belief (SoB), where agents maintain continuous latent beliefs and iteratively refine them through communication and reflection. Our met…

- **[Language-model agents' beliefs can be manipulated via truthful evidence in open channel](https://arxiv.org/abs/2611.21235v1)**
  - *Jinwei Hu, Qisong He, Xinmiao Huang et al.*
  - `2026-11-16`
  - Language-model agents' beliefs can be manipulated through open channels such as social media, even when the information they receive is truthful. When agents fill gaps between fragments with self-induced relationships, they may accept those relationships as established facts and…

- **[Edit Recommendation: Can LLMs Anticipate Edit Requests from Users, and When?](https://arxiv.org/abs/2611.21155v1)**
  - *Daisuke Kikuta*
  - `2026-11-16`
  - After a large language model (LLM) agent generates an artifact, users often send edit requests for it. This paper studies whether an LLM can anticipate these requests before they are sent. Such anticipation is useful in practice because it reduces the effort of user review and fe…

- **[Linglong Agent Service: A Runtime for Centralized Agent Reasoning and Distributed Execution](https://arxiv.org/abs/2611.21129v1)**
  - *Hua Zhang, Min Jiang*
  - `2026-11-16`
  - LLM agents can use remote tools and cloud sandboxes, but integrating reasoning, session state, and heterogeneous execution sites remains a runtime design problem. We present Linglong Agent Service (agentsvc), a self-hosted HTTP service and embeddable Python runtime that treats ex…

- **[SWE-WhatIf: Simulating Real Users of Coding Agents from Recorded Session](https://arxiv.org/abs/2611.21095v1)**
  - *Tae Soo Kim, Tongshuang Wu, Juho Kim*
  - `2026-11-16`
  - Recorded sessions between users and coding agents offer a way to evaluate how agents complete real-world tasks and interact with users. However, these sessions cannot simply be replayed with new agents, because recorded user replies may no longer apply when an agent takes a diffe…

- **[Think2Listen: Evidence-Centric Learning For Agentic Audio Understanding With LALMS](https://arxiv.org/abs/2611.21083v1)**
  - *Jin Wang, Liang Lin, Kaiwen Luo et al.*
  - `2026-11-16`
  - Recent advances in large audio-language models (LALMs) have broadened audio understanding across speech, sound, and music, with tool-based agents further supporting these tasks by invoking predefined audio tools. However, a persistent gap remains between perceiving acoustic conte…

- **[Sage S2.1 Flash Technical Report](https://arxiv.org/abs/2611.21072v2)**
  - *Kun Cai, Haodong Chen, Guangran Cheng et al.*
  - `2026-11-16`
  - We introduce Sage S2.1 Flash, a 320-billion-parameter general-purpose mixture-of-experts model designed to reason over scientific evidence and act in interactive environments. Sage Sci-Perception uses dedicated encoders for molecular graphs and biological sequences and represents…

- **[System 1 agents: a method for local, reliable and fast agentic AI](https://arxiv.org/abs/2611.21053v1)**
  - *Eleftherios Tzanis, Michail E. Klontzas*
  - `2026-11-16`
  - Agentic artificial intelligence could automate analyses of sensitive clinical data, but current agents depend on large language models (LLMs). Cloud LLMs expose patient data. Local LLMs hallucinate, and an invented value in a tool call propagates through every later step. Here we…

- **[SWE-OPD: On-Policy Distillation for Agentic Coding](https://arxiv.org/abs/2611.21020v1)**
  - *Yuhang He, Yanyu Chen, Chuanzhe Guo et al.*
  - `2026-11-16`
  - In this work, we study on-policy distillation (OPD) for transferring agentic coding capabilities from a large teacher model to a smaller student model. Prior work has focused primarily on reasoning and short-horizon agentic tasks. We present SWE-OPD, a minimal OPD study for softw…

- **[K2-Horizon: A Frontier Fleet of Open Source Language Models](https://arxiv.org/abs/2611.21003v1)**
  - *K2 Team, Zhengzhong Liu, Haonan Li et al.*
  - `2026-11-16`
  - We present K2-Horizon, a fleet of six fully open language models, from a 0.9B dense model to a 375B-A23B MoE, built for general-purpose reasoning and agentic work across math and science, software engineering, deep research, office automation, and beyond. The models lead or are c…

- **[Does the Voice Matter? Evaluating Frustration Detection on Deployed Clinical Voice-Agent Calls](https://arxiv.org/abs/2611.21001v2)**
  - *Annika Michael, Zachary Ellis, Yuxiang Zhou et al.*
  - `2026-11-16`
  - Autonomous voice agents now conduct routine clinical follow-up calls, so some automated triage is unavoidable. A patient becoming frustrated is one thing that triage should catch. These systems typically read only the transcript the speech-to-text stage produces, not the voice, a…

- **[Hivemind: A Federated Protocol for AI-Mediated Tacit Knowledge Sharing in Organisations](https://arxiv.org/abs/2611.20988v1)**
  - *Srinivasan Sundaresan*
  - `2026-11-16`
  - This paper presents Hivemind, a federated protocol that enables AI agents to exchange tacit knowledge on behalf of their users, asynchronously and without requiring any direct human interaction. Individual AI memory systems capture the decisions, reasoning, and contextual knowled…

- **[GRACE: Parallel Best-of-N Multi-Agent Analysis of Closed-Form Questions over Dataframes with Guardrail Selection and Adaptive Retry](https://arxiv.org/abs/2611.20983v1)**
  - *Fabio Picariello, Salvatore Cipolla, Susanna Bonura et al.*
  - `2026-11-16`
  - LLM agents answer closed-form questions over a tabular dataframe by writing and executing Python, almost always as a single rollout: one interpretation, one script, one result, accepted without comparison. The few pipelines that produce several candidates reconcile them by answer…

- **[Experience Rot: Experienced Agents Fail Where Novices Succeed](https://arxiv.org/abs/2611.20922v1)**
  - *Zhen Xu, Hang Yin, Zitao Zhang et al.*
  - `2026-11-16`
  - Agents are increasingly built to learn from experience: they keep conversation histories, memory files, retrieved notes and skills, and reuse what worked before. We show that this experience turns against them when their tools change silently. We test a range of models with tools…

- **[Multi-LLM Agentic AI at the Edge: Joint Agent Scheduling and Resource Allocation](https://arxiv.org/abs/2611.20915v1)**
  - *Yuanyan Song, Kezhi Wang, Xinmian Xu et al.*
  - `2026-11-16`
  - In this paper, an edge-enabled multi-large language model (LLM) agentic AI architecture is proposed, where one supervisor AI agent and multiple worker AI agents cooperatively execute users' requests at the edge. The supervisor AI agent decouples the user request into a series of…

- **[From Recursion to Convolution: Parallel Self-Improvement for Multi-Agent Systems](https://arxiv.org/abs/2611.20891v1)**
  - *Zheng Wang, Yuang Liu, Sachith Abeywickrama et al.*
  - `2026-11-16`
  - Multi-agent self-improvement enables agents to improve through interaction and feedback. However, sequential dependencies across agents and refinement rounds can propagate errors, increase computational costs, and limit parallelism. Moreover, refining individual features or agent…

- **[Accelerate Bench: Evaluating Agents for Application-Level Program Optimization](https://arxiv.org/abs/2611.20882v1)**
  - *Bowen Liu, Yuhan Li, Nuo Chen et al.*
  - `2026-11-16`
  - Application optimization requires coding agents to discover useful changes and coordinate them across a complete program while preserving the required computation. We introduce Accelerate Bench, a benchmark of 32 CPU optimization tasks adapted from scientific applications and sup…

- **[Re-Reading Is Not Free: Token Traces and Cache-Aware Energy Estimation for LLM Agents in Software Engineering](https://arxiv.org/abs/2611.20873v1)**
  - *Tina Vartziotis, Ketevan Peranidze, Rodopi Kosteli et al.*
  - `2026-11-16`
  - As large language models (LLMs) evolve from conversational assistants into autonomous agents embedded in software development workflows, estimating their environmental footprint requires moving beyond conventional token-based accounting. Existing energy estimators focus on isolat…

- **[ProcReverser: Multi-Agent Black-Box Microarchitectural Reverse Engineering for Processor Vulnerability Analysis](https://arxiv.org/abs/2611.20827v2)**
  - *Guanqi Lyu, Decheng Qiu, Guangyang Zhang et al.*
  - `2026-11-16`
  - When processor implementation details are unavailable, black-box microarchitectural reverse engineering helps security researchers identify hardware conditions related to security vulnerabilities. However, this process requires substantial manual effort to design experiments, dev…

- **[Conversing with a Conversational Agent: A Real Conversation, Not a Simulated One](https://arxiv.org/abs/2611.20826v1)**
  - *Christophe Denis*
  - `2026-11-16`
  - The claim that interactions with artificial conversational agents merely simulate human conversation rests on a philosophical distinction between reproducing the observable features of an activity and actually performing it. Although this distinction is appropriate for certain ph…

- **[Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents](https://arxiv.org/abs/2611.20771v1)**
  - *NVIDIA, :, Adi Margolin et al.*
  - `2026-11-16`
  - We introduce Nemotron 3.5 Bolt E4B 4GB, an open and efficient small language model further post-trained from Gemma-4-E4B-it and optimized for speed and intelligence per GB of memory used for fast conversational agents. The model carries forward Gemma's strong conversational capab…

- **[GainCtrl: Predicting Remaining Gains for Efficient LLM Agent Execution](https://arxiv.org/abs/2611.20736v1)**
  - *Kangwen Zhao, Jianfeng Cai, Ruopei Sun et al.*
  - `2026-11-16`
  - Large language models (LLMs) are widely used to power agents that interact with tools and environments to solve complex tasks. Repeated attempts improve the quality of tool-using agents, but continued execution incurs additional costs even when it is unlikely to improve the best…

- **[AgentFaultBench: State-Verified Evaluation of Tool-Fault Recovery](https://arxiv.org/abs/2611.20711v1)**
  - *Sachin Gupta*
  - `2026-11-16`
  - Does recovery advice help an agent finish a task after a tool fails? AgentFaultBench evaluates LangGraph and CrewAI agents performing specified tasks in an isolated GitLab installation. We inject tool errors and check both the resulting files and issues and the required reads, ve…

- **[VIVID: A Visual Harness for Agentic Video Editing](https://arxiv.org/abs/2611.20688v1)**
  - *Wenhan Yu, Zhaoxi Zhang, Zhilong Tan et al.*
  - `2026-11-16`
  - Video editing requires agents to make editing decisions grounded in audiovisual observations and precise temporal localization, and to evaluate their effects in rendered outputs. General-purpose coding agents possess strong comprehension, reasoning, and code execution capabilitie…

- **[UbiHearo: Bringing Scenario-Aware Sound Guidance to DHH Users with Mobile Agents](https://arxiv.org/abs/2611.20686v1)**
  - *Fengmin Wu, Sicong Liu, Zimu Zhou et al.*
  - `2026-11-16`
  - For Deaf and Hard-of-Hearing (DHH) users, effective sound awareness goes beyond detecting \emph{what} sound occurs; it requires understanding \emph{what it means}, \emph{how urgent it is}, and \emph{what to do}. However, existing mobile assistants largely reduce acoustic scenes t…

- **[EgoLink: Egocentric Language-Vision Interactive Network Knowledge Challenge Summary](https://arxiv.org/abs/2611.21690v1)**
  - *Renhe Sun, Yueying Feng, Bohan Yu et al.*
  - `2026-11-16`
  - The EgoLink Challenge at ACM Multimedia 2026 benchmarks egocentric multimodal intelligence linking first-person perception, social reasoning, and interactive action. Unlike benchmarks centered on visible objects and activities, EgoLink evaluates whether models can interpret emoti…

- **[MASTA: A Feedback-Scheduled Multi-Agent System for End-to-End Tamarin Modeling and Analysis](https://arxiv.org/abs/2611.20671v1)**
  - *Yongkang Xiao, Qiyi Deng, Jing Chen et al.*
  - `2026-11-16`
  - Tamarin-based formal verification of security protocols requires expert-authored multiset rewriting rules and temporal-logic lemmas. Translating a natural-language protocol description into a complete formal model with an LLM is hard because syntactic, reachability, and property-…

- **[Instrumenting Failure: Scoring Language Model Agents at Every Decision Node in Imperfect-Information Games](https://arxiv.org/abs/2611.20644v1)**
  - *Michael Kingston, Sonit Singh, Alan Blair*
  - `2026-11-16`
  - Agent evaluations report task success and rarely say what an agent did at each decision. We score every decision node of three 12B to 14B instruct-tuned language models (LMs) playing five zero-sum imperfect-information games against four opponents on eight properties from decisio…

- **[AdMem: Expectation-Grounded Procedural Memory for Long-Horizon Task-Solving Agents](https://arxiv.org/abs/2611.20605v1)**
  - *Runzhe Wang, Huilin Lu, Shengjie Liu et al.*
  - `2026-11-16`
  - An agent that carries memory across tasks is only as good as the entries it keeps. We begin from an observation that is easy to reproduce and uncomfortable for the field: naively accumulating cross-task experience can make an agent \emph{worse} than one with no memory at all. On…

- **[ToolGraph as a Q-Function for Test-Time Scaling of Tool-Use Agents](https://arxiv.org/abs/2611.20569v1)**
  - *Ke Shen, Ankita Bhaumik, Li Dong et al.*
  - `2026-11-16`
  - Tool-use agents must chain interdependent calls, yet which outputs satisfy which later inputs in a deployed catalog is not something a general-purpose language model reliably infers from tool descriptions alone. We compile that structure once into a reusable external representati…

- **[GranularGPT: Natural-Language-Driven End-to-End Discrete Element Method Simulations](https://arxiv.org/abs/2611.20551v1)**
  - *Erlei Li, Sirui Tang, Ai Wang et al.*
  - `2026-11-16`
  - Discrete element method (DEM) simulations are widely used to investigate granular and particulate systems, but their application often requires specialized expertise in particle physics, numerical modelling, and simulation post-processing. Large language models (LLMs) offer new o…

- **[VAHBench: A Harness Benchmark for Agentic Long-Video Generation](https://arxiv.org/abs/2611.20535v1)**
  - *Hongbo Zhang, Liuyang Song, Hang Zhou et al.*
  - `2026-11-16`
  - AI agents are commonly used for everyday information retrieval and coding. We ask whether they can also interpret human requests and turn them into complete videos. We introduce VAHBench, a benchmark that tests this ability through five short-drama briefs specifying story, charac…

- **[EVIDENT: Evaluating Evidence Grounding in GUI Agents](https://arxiv.org/abs/2611.20488v1)**
  - *Yerin Nam, Minkyung Cho, MinKyu Kim et al.*
  - `2026-11-16`
  - GUI agents are increasingly evaluated by whether they complete web tasks, but surface success can hide a critical failure: the final answer may not be supported by evidence observed during navigation. We introduce EVIDENT, an evidence-driven benchmark for evaluating whether GUI a…

- **[Agent-Guided Configuration Tuning for SMT Solvers](https://arxiv.org/abs/2611.20484v1)**
  - *Cong Wang, Qiaoyi Zheng, Zhaoguo Wang et al.*
  - `2026-11-16`
  - SMT solvers expose many configuration choices that determine how well their existing algorithms perform on a workload. We present, to our knowledge, the first workflow that uses general-purpose LLM agents to tune SMT solver configurations. Agents read solver documentation, source…

- **[FinVerify: A Verification Framework for Financial Agents](https://arxiv.org/abs/2611.20423v1)**
  - *Mao Guan, Qian Chen, Ge Meng et al.*
  - `2026-11-16`
  - Financial agents produce numerical claims that can be wrong even when their calculations execute correctly, due to mismatched reporting periods, unsupported sources, incompatible units, or incorrect financial definitions. We introduce FinVerify, an evidence-grounded framework for…

- **[Implicit-Reasoning-Enabled Elastic Semantic Communications for AI-Agent Networks](https://arxiv.org/abs/2611.20399v1)**
  - *Kaiwen Yu, Gang Wu, Jiancun Fan et al.*
  - `2026-11-16`
  - AI-agent networks introduce new communication demands driven by proactive interactions and autonomous task execution. Existing adaptive semantic communication schemes primarily adjust semantic representations and resource configurations within predefined processing scales and cap…

- **[Deploying a Control-Logic LLM Assistant in Air-Gapped Power Plants: Lessons in Source Authority and Bounded Retrieval](https://arxiv.org/abs/2611.20398v1)**
  - *Yiwei Fu, Nicholas Gabriel*
  - `2026-11-16`
  - Deploying Large Language Model (LLM) assistants in industrial operational technology environments poses constraints largely absent from cloud applications: site policies restrict engineering and operational data from leaving the plant, on-premises compute is limited, and incorrec…

- **[Solver to System: LLM Reasoning Across Representations and Execution in Scientific Simulation](https://arxiv.org/abs/2611.21964v1)**
  - *Eliza Berman, Rohan Subramanian, Shreya Jha et al.*
  - `2026-11-16`
  - Simulators based on partial differential equations (PDEs) are widely used to model physical systems, but generating and interpreting PDE solver code with large language models (LLMs) remains challenging. Scientific simulation code is a useful testbed for LLM scientific reasoning…

- **[World-Grounded Reinforcement Learning for Pollution-Aware Bird Movement Modeling Using a Multi-Instance DQN Framework](https://arxiv.org/abs/2611.21895v1)**
  - *Shivin Mangal, Divyansh Chawla, Anshu Garg et al.*
  - `2026-11-16`
  - Birds are modeled as environmentally sensitive agents whose movement reflects real-world air quality conditions, where AQI serves as a measurable world feedback signal representing pollution-driven consequences. Instead of relying on human preference or synthetic rewards, the sys…

- **[Regularized Score Centering](https://arxiv.org/abs/2611.21791v1)**
  - *Hao Bai, Chenlu Ye, Xuanchang Zhang et al.*
  - `2026-11-16`
  - Asynchronous reinforcement learning increases training throughput, but data from stale policies and numerical mismatch between training and inference can destabilize learning. To stabilize off-policy learning, score centering (SC) removes the effect of reward baselines on the exp…

- **[Efficient Modeling of Multi-Agent Systems via Structure-Aware Physics-Informed Learning](https://arxiv.org/abs/2611.21404v1)**
  - *Yulun Wu, Nicola Bastianello, Karl Henrik Johansson et al.*
  - `2026-11-16`
  - Modeling large multi-agent systems poses challenges for trajectory inference and parameter identification, as network size and coupling increase computational demands and partial observations require reconstructing unobserved states. We propose MAS-PINN, a neural-network architec…

- **[Tight PAC-Bayes Generalisation Guarantees for Large Language Model Judges](https://arxiv.org/abs/2611.20818v1)**
  - *Tom A. Lamb, Philip H. S. Torr, Tim G. J. Rudner*
  - `2026-11-16`
  - Large language model (LLM) judges are increasingly used to monitor the outputs of LLM-based AI agents, yet formal guarantees on the reliability of these judges remain largely absent, limiting confidence in their use for safety-critical oversight. We consider certifying such a jud…

- **[DeltaHarness: Self-Evolving Harnesses for Resource-Adaptive Tool Execution](https://arxiv.org/abs/2611.21688v1)**
  - *Lecheng Yan, Jianze Lin, Xicheng Han et al.*
  - `2026-11-16`
  - Tool-using agents rely on execution harnesses to organize and schedule tool operations. The same task and resource description can conceal runtime conditions that reverse the latency ordering of valid execution plans. Resolving this uncertainty requires firsthand execution in the…

- **[TrainExplorer: Autonomous LLM Post-Training via Plan-and-Decouple Exploration](https://arxiv.org/abs/2611.20430v1)**
  - *Xuannan Liu, Tian Lan, Zekun Li et al.*
  - `2026-11-16`
  - LLM-based agents can automate model post-training, accelerating progress toward recursive self-improvement. Despite their promise, existing approaches remain under-explored and face two main challenges: (1) strategy lock-in that limits exploration beyond the initial strategy; and…

- **[When Should Decision Models Compare Candidates?](https://arxiv.org/abs/2611.20335v1)**
  - *Fangzhi Li, Quan Shi, Wenting Yang et al.*
  - `2026-11-16`
  - Language-model agents frequently select among candidate actions, such as tools and web elements. Should decision models score candidates independently or allow their scores to depend on other candidates? We investigate this question by comparing three approaches: Pointwise scorin…

- **[Corrupting Ties: Investigating Robustness to Bias Injection Across Multi-Agent Network Topologies](https://arxiv.org/abs/2611.21804v1)**
  - *Cléa Chataigner, Mina Arzaghi, Florian Carichon et al.*
  - `2026-11-16`
  - AI systems are increasingly deployed in high-stakes decision-making contexts, where interactions among components can introduce fairness risks that remain undetected when auditing components or collective outcomes in isolation. As LLM-based multi-agent systems become more prevale…

- **[Detection-Efficient Watermarking for Vision--Language Agents via Risk-Constrained Strength Allocation](https://arxiv.org/abs/2611.21488v1)**
  - *Dumindu Samaraweera, Prashant Shekhar*
  - `2026-11-16`
  - Vision--language agents generate descriptions, decisions, and instructions that may be reused by users, downstream agents, and automated workflows, creating a need for provenance mechanisms that support content authenticity and post-deployment auditing without unnecessarily degra…

- **[Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility](https://arxiv.org/abs/2611.21478v2)**
  - *Ruizhe Li, Licheng Zhang, Mingxuan Du et al.*
  - `2026-11-16`
  - Whether a stored memory helps answer a user's question often depends on world knowledge rather than surface similarity. Jetriever replaces similarity search with full-pool utility scoring: given a query, it uses Jev, an LLM-derived System One decision model, to score every stored…

- **[Beyond Bilingual: Studying Quadrilingual Code-Switching with Conversational AI](https://arxiv.org/abs/2611.21394v1)**
  - *Annika Bush, Melika Minnaar, Salys Sultan et al.*
  - `2026-11-16`
  - Multilingual speakers choose languages by topic and conversation partner. Large language models (LLMs) support these languages unequally. Research on code-switching with conversational AI has mostly examined bilingual pairs of well-resourced languages. In Curaçao and Aruba, many…

- **[A Crowd-Audited Atlas of Implicit Bias in LLM-Powered Agents](https://arxiv.org/abs/2611.21376v1)**
  - *Jason Alexander, Yuxuan Li, Michael Licamele et al.*
  - `2026-11-16`
  - Prior work has shown that large language models (LLMs) express implicit biases in high-publicity, one-off decision scenarios such as hiring and intelligence assessment. However, as people increasingly employ autonomous, LLM-powered AI agents that make decisions on their behalf in…

- **[From Repositories to Training Environments: Scaling Long-Horizon Coding Agents with Environment Evolution Loop](https://arxiv.org/abs/2611.21152v2)**
  - *Yang Tian, Tianyu Zheng, Xiyuan Yang et al.*
  - `2026-11-16`
  - Training coding agents for long-horizon tasks requires environments with verifiable feedback. Existing pipelines often follow a linear process that ends with validation, establishing usability but providing little guidance on improving training value. Recursive self-improvement (…

- **[Evaluation-Free Recursive Self-Improvement for Coding Agents](https://arxiv.org/abs/2611.21056v1)**
  - *Zhe Ren, Guowei Rong, Yimeng Chen et al.*
  - `2026-11-16`
  - Recent self-improving coding agents have achieved strong benchmark performance by iteratively modifying their own executable implementations. A common pattern uses downstream task-derived evidence to decide which candidates or lineages continue evolving, which we term evaluate-an…

- **[MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory](https://arxiv.org/abs/2611.21019v1)**
  - *Ruiyang Jiang, Xinyang Liao, Weikai Huang et al.*
  - `2026-11-16`
  - Multimodal large language models (MLLMs) now assist users across sessions of images and text, carried by an external memory of what was said and shown. When such an assistant answers wrongly, the failure usually began earlier, in how a record was written, updated or retrieved, an…

- **[Navital Gym: Rule-Graded Agent Environments for Indian Workflows](https://arxiv.org/abs/2611.20924v1)**
  - *Daksh Bathla*
  - `2026-11-16`
  - AI agents are being deployed on Indian workflows such as payments, tax, forms, travel and customer support in Hindi and Hinglish. Public agent evaluations rarely cover these workflows, and many score with another language model. We present Navital Gym, a set of six open environme…

- **[CuRSE-Bench: A Benchmark for Probing Cultural Blind Spots in Text-to-Image Safety Evaluation](https://arxiv.org/abs/2611.20821v2)**
  - *Minsuk Jang, Minseok Son, KiHyun Seol et al.*
  - `2026-11-16`
  - Text-to-image (T2I) safety evaluation typically assigns each prompt or image a single culture-blind harm label, so content that is harmful only within a particular culture can pass as benign. We introduce CultureCraft, an agentic framework that constructs T2I prompts that appear…

- **[GPRM: Global Perspective Process Reward Model](https://arxiv.org/abs/2611.20755v1)**
  - *Zifan Zhang, Zhengbo Jiao, Shaobo Wang et al.*
  - `2026-11-16`
  - Process Reward Models (PRMs) are widely used for step-level evaluation of multi-step reasoning in large language models, but existing methods are often limited by weak historical dependency modeling and insufficient global awareness. They typically fail to leverage prior step eva…

- **[ANCHOR: Cluster-Grounded 5W1H Extraction via Large-Small Model Collaboration](https://arxiv.org/abs/2611.20728v1)**
  - *Hongyu Jiang, Chenang Cai, Lei Gao et al.*
  - `2026-11-16`
  - Deep semantic understanding of events requires recognizing related events and distinguishing why an event occurs from how it is carried out. 5W1H extraction provides a structured foundation for such understanding by organizing event information around six fundamental questions. H…

- **[MetaAct: Self-Evolving Executable Action Constraints for Embodied Language Agents](https://arxiv.org/abs/2611.20655v1)**
  - *Jiaxing Zhao, Hanwen Wang, Di Liu et al.*
  - `2026-11-16`
  - Self-evolving language agents have emerged as a promising paradigm for continuously improving agent behavior through experience. However, most existing approaches evolve textual artifacts, which can influence action preferences but cannot reliably enforce action admissibility in…

- **[Invariant-Aware Harness Enforcement to Protect LLM Agents from Silent API Failures](https://arxiv.org/abs/2611.20595v1)**
  - *Sajib Acharjee Dip, Brian Ouyang, Lala Motlhabi*
  - `2026-11-16`
  - LLM agents answer questions by calling APIs and trusting the results. An API can fail silently. It ignores part of a request, such as a misnamed filter, yet returns HTTP 200 and a plausible but wrong result. Current fixes, such as checklists, reviewer models and LLM judges, ask t…

- **[Operating an Agent-Driven Dataset Factory: Discovery, Construction, and Public Release](https://arxiv.org/abs/2611.21957v1)**
  - *Eduardo Ariño de la Rubia, Szilard Pafka*
  - `2026-11-16`
  - Turning public data into prediction datasets requires connecting source discovery, task definition, construction, and distribution. We deployed Dataset Factory to perform these steps continuously under a standing release policy. Bounded language-model tasks interpret sources, wri…

- **[Even Loose Proximity Constraints Make Makespan-optimal Unlabeled Multi-agent Pathfinding Hard](https://arxiv.org/abs/2611.21277v2)**
  - *Takahiro Suzuki, Keisuke Okumura*
  - `2026-11-16`
  - We study $r$-Connected Unlabeled Multi-agent Pathfinding ($r$CUMAPF), a variant of MAPF where interchangeable agents have a proximity range $r\in \mathbb{N}$, and agents must form a single group in a given graph $G$ through limited-range communication at all times. The problem ar…

- **[Evaluating Authorization and Trust Boundaries in Agentic Orchestration Frameworks](https://arxiv.org/abs/2611.21259v1)**
  - *Sahaya Jestus Lazer, Kshitiz Aryal, Maanak Gupta et al.*
  - `2026-11-16`
  - Agentic AI systems extend large language models with tools, memory, and multi-agent collaboration, introducing security risks at orchestration boundaries. These risks depend on how identities are represented, operations are authorized, and instructions or information propagate be…

- **[CoopDistill: Equilibrium-Guided Multi-Agent Policy Distillation for Cooperative Driving](https://arxiv.org/abs/2611.21069v1)**
  - *Shiyu Fang, Sheng Zhao, Jiarui Zhang et al.*
  - `2026-11-16`
  - Cooperative driving extends autonomous driving from individual vehicle decisions to joint maneuvers that improve traffic safety and efficiency. Optimization-based methods impose safety constraints but often fix paths to simplify multi-vehicle planning, limiting spatial flexibilit…

- **[OpenMAS-GApp: A Comprehensive Benchmark for Domain-Adaptive Multi-Agent Application Construction](https://arxiv.org/abs/2611.20997v1)**
  - *Xunkai Li, Kairui Yang, Jiaxi Li et al.*
  - `2026-11-16`
  - Constructing multi-agent system (MAS) applications across domains requires translating diverse requirements into executable systems, involving task decomposition, agent and tool selection, and execution organization. Existing studies have explored individual aspects of MAS constr…

- **[From Vision to Interaction: Evaluating Dynamic Social Intelligence of VLM Agents in ALIVE-World](https://arxiv.org/abs/2611.20956v1)**
  - *Yue Xu, Xiaoyu Qin, Sihan Zhao et al.*
  - `2026-11-16`
  - As AI agents are increasingly deployed in real-world applications and take on social roles, dynamic social intelligence, the ability to continuously perceive multimodal cues, infer latent cognitive states, intervene through embodied actions, and ultimately achieve social goals, h…

- **[LEDGER: Auditable Agent Memory Under Change](https://arxiv.org/abs/2611.20927v1)**
  - *Md Aidul Islam, Md Nasir Uddin Shuvo, Muhammad Waseem et al.*
  - `2026-11-16`
  - Agent memory systems are mostly evaluated on fixed histories, and only their final answers are scored. In real use, facts change, sources differ in reliability, and users ask the agent to forget things. We present LEDGER, a memory layer in which a language model proposes facts an…

- **[When Does Interaction Help? Toward a Reynolds Number for Collective Intelligence](https://arxiv.org/abs/2611.20773v1)**
  - *Xuening Wu, Haode Yang, Yanlan Kang et al.*
  - `2026-11-16`
  - Multi-agent systems combine distributed information through interaction, which can improve performance but also spread errors or suppress useful differences. Predicting when interaction helps is central to understanding and designing collective intelligence. We investigate whethe…

- **[Learning Design Taste through Verifiable Synthetic Environments and Agentic Reinforcement Learning](https://arxiv.org/abs/2611.20612v1)**
  - *Sujay choubey, Siddhant Saxena, Sarthak Kapil et al.*
  - `2026-11-16`
  - Code-generating language models produce user interfaces that build and run, but the pages are often weak in hierarchy, spacing, typography and composition. We study whether a small code model can learn design taste through reinforcement learning in verifiable synthetic environmen…


## Harness  (113)

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


### ACL

- **[MLE Agents: Autonomous ML Engineering in Large-scale Recommendation Systems](https://arxiv.org/abs/2611.23910v1)**
  - *Matthew Li, Albert Liang, Dilip Raj*
  - **ACL** · `2026-11-18`
  - The typical workflow for improving large-scale ranking and recommendation models is slow and tedious: an engineer forms a hypothesis, implements it as a code change, trains a model, and evaluates it both offline and online, often relying on their own intuition and experience alon…

- **[Scientific Coding with Large Language Models: Evidence from Finite Element Analysis](https://arxiv.org/abs/2611.21176v1)**
  - *Erfan Hamdi, Joel Shor, Emma Lejeune*
  - **ACL** · `2026-11-16`
  - Large language models (LLMs) offer a potential route to automating scientific programming, but their usefulness depends on consistently producing numerically correct code. We extend FEM-Bench to 17 finite element tasks involving nonlinear and history-dependent mechanics and struc…

- **[DetourBench: Trajectory-Level Evaluation of Interactive Agents with Exact Minimum-Action Bounds](https://arxiv.org/abs/2611.20844v1)**
  - *Hanlin Tian, Sihan Zhu, Zhao Yang et al.*
  - **ACL** · `2026-11-16`
  - Benchmarks judge language-model agents mainly by whether they reach the correct final state, not by how they got there. Endpoint scoring cannot separate an agent that retrieved exactly the evidence a decision required from one that read most of the environment, nor an agent that…

- **[A Generative AI-Driven Architecture for Whole-Home Intelligent Services: Edge Models, Memory Management, and Household Applications](https://arxiv.org/abs/2611.21232v1)**
  - *Mo Zhou*
  - **ACL** · `2026-11-16`
  - Generative artificial intelligence is entering the home. Cloud-based assistants face governance limitations in data transmission, continuous availability, and the reliability of physical actions, which are especially salient in households where devices remain online, data accumul…

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://arxiv.org/abs/2507.21028)**
  - *Jia-Ju Chen, Yuxuan Lu, Xiaojie Wang et al.*
  - **ACL 2025** · `2025-07-28`
  - Nearly all human work is collaborative; thus, the evaluation of real-world NLP applications often requires multiple dimensions that align with diverse human perspectives. As real human evaluator resources are often scarce and costly, the emerging"LLM-as-a-judge"paradigm sheds lig…


### Other / arXiv

- **[Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement](https://arxiv.org/abs/2611.24651)**
  - *Zhenqing Ling, Qirui Jiao, Daoyuan Chen et al.*
  - 🤗 Featured · `2026-11-18`
  - We present Piccolo, a family of multimodal decision models (0.8B to 27B) that coevolves model capabilities and training data via Agentic Data Engineering and recursive self-improvement (RSI). The models predict probabilities over candidate answers for general-purpose text and vis…

- **[Movie2Game-Bench: Holistic Evaluation of Film-to-Game Adaptation Beyond Playability](https://arxiv.org/abs/2611.24669)**
  - *Jialing Xie, Yifan Zhou, Yiwen Zhang et al.*
  - 🤗 Featured · `2026-11-18`
  - Adapting a film into a game requires selecting source elements and translating them into player actions, rules, and feedback. We introduce Movie2Game-Bench (M2G-bench), a benchmark for evaluating film-to-game adaptation beyond playability. M2G-bench combines general evaluation, m…

- **[QDA: Closed-Loop LLM Quantization Design with Agents](https://arxiv.org/abs/2611.23388)**
  - *Xingyang Li, Tianlang Zhao, Song Han et al.*
  - 🤗 Featured · `2026-11-17`
  - Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortuna…

- **[NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding](https://arxiv.org/abs/2611.22790)**
  - *Tianci Xie, Li Chen, Pinxue Guo et al.*
  - 🤗 Featured · `2026-11-17`
  - Fine-grained questions about long videos ask how many times an action occurs, in what order events unfold, or exactly when a state changes. Answering them can require finding brief moments scattered across hours of footage. Agentic models that decide when and where to look promis…

- **[BaseRSI: Recursive Self-Improvement of a Base Vision-Language Model via Training-Free Harness Internalization](https://arxiv.org/abs/2611.24578)**
  - *Mingda Zhang, Yuanhao Dong, Qiang Huang et al.*
  - 🤗 · `2026-11-18`
  - Recursive self-improvement (RSI) is moving from the harness of prompts and tools around a base model toward the model itself. However, existing RSI still faces key challenges, including harness-bound gains that stay outside the base model, black-box supervision that reads only th…

- **[Agentic Harness Engineering Beta: Requirement-Centered Evolution of Agent Harnesses](https://arxiv.org/abs/2611.24924v1)**
  - *Jiahang Lin, Jiahao Chen, Yiding Wang et al.*
  - `2026-11-18`
  - Real-world harness engineering is driven by explicit and implicit user requirements, which guide development and validation. However, existing harness evolution methods often overlook implicit requirements and interaction needs, while using a single evolution agent to modify the…

- **[Local AI Agents in Power Electronics Simulation: Deployment, Measurements and Costs](https://arxiv.org/abs/2611.24880v1)**
  - *Yuzhuo Li, Pasan Gunawardena, Yunwei Li*
  - `2026-11-18`
  - Agentic artificial intelligence (AI) is emerging in power electronics, where it drives the simulation loop that engineers used to close largely by hand. In this loop, a converter design, or a study of the network it connects to, is built, run, measured and revised until it satisf…

- **[Benchmarking LLM abilities on postdoc-level natural science problems](https://arxiv.org/abs/2611.24321v1)**
  - *Alina Avanesyan, Alexey Boldyrev, Liqun Deng et al.*
  - `2026-11-18`
  - Scientific problems have no answer key, so evaluating an agent means deciding what counts as a better solution before any agent is run. Existing benchmarks either match a symbolic answer against a key or, where they require executable work, score it by unit tests, by a rubric, or…

- **[A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises](https://arxiv.org/abs/2611.24039v1)**
  - *Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid*
  - `2026-11-18`
  - Agentic AI platforms-systems in which LLM agents plan, invoke tools, retain memory and coordinate to change the state of enterprise systems-are being procured faster than they can be measured. Public agent benchmarks score models in fixed harnesses; enterprises buy integrated pla…

- **[In Situ Training of Optical Neural Networks by Coding Agents](https://arxiv.org/abs/2611.23875v1)**
  - *Ilker Oguz, Colin Christian, Christophe Moser et al.*
  - `2026-11-18`
  - Optical neural networks promise fast, energy-efficient computing, but every device departs from its design and must be trained with the hardware. In situ training relies on an expert-built calibrated digital model of each device or on gradient-free trial and error. Coding agents,…

- **[Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics](https://arxiv.org/abs/2611.23678v1)**
  - *Dowling Wong*
  - `2026-11-18`
  - Autonomous agents that run ML experiments are usually judged by the best score they reach. That score says nothing about how it was reached: whether the agent stayed within the files it was allowed to edit, whether failed trials were kept or silently dropped, and whether each kee…

- **[On Evaluating User Simulators for Interactive Agents](https://arxiv.org/abs/2611.24892v1)**
  - *Hengguang Zhou, I-Hung Hsu, Li Chen et al.*
  - `2026-11-18`
  - User simulators offer a scalable way to evaluate interactive agents, but how to assess their quality remains underexplored. In particular, it is unclear whether existing user simulator evaluation frameworks reliably detect meaningful failures in simulated user behavior. This unce…

- **[Once Upon a Bias: Gender Stereotyping in LLM-Generated Children's Stories](https://arxiv.org/abs/2611.24156v1)**
  - *Sayumi Muthukumarana, Roshan Godaliyadda, Parakrama Ekanayake et al.*
  - `2026-11-18`
  - Large language models are increasingly used to create stories for children. Since bedtime stories can shape children's perceptions of social roles, this raises concerns about whether LLMs adapt narrative portrayals according to the intended recipient's gender. We conducted a larg…

- **[Evaluating the Effectiveness of Location Encoding Methods for Species Distribution Modelling](https://arxiv.org/abs/2611.24622v1)**
  - *Christian Lange, Oisin Mac Aodha*
  - `2026-11-18`
  - Understanding the spatial distribution of species is a key question in ecology. A variety of solutions, from statistical, traditional machine learning, through to deep learning-based methods have been proposed. These methods take sparse observations for a species of interest as i…

- **[TabBioMed: A Large-Scale Benchmark for Biomedical Tabular Learning](https://arxiv.org/abs/2611.23779v1)**
  - *Pau Mateo-Bernadó, Saivenkata Nagavyjayanthi Polapragada, David Bonet et al.*
  - `2026-11-18`
  - Recent advances in machine learning have accelerated biomedical prediction, but evaluation on structured biomedical data remains fragmented, especially for datasets with high dimensionality, large sample size, missingness, and class imbalance. We introduce TabBioMed, a large-scal…

- **[GRAFT: Execution-Guided Genetic Recombination for Agent Design](https://arxiv.org/abs/2611.23509v1)**
  - *Sevda Ebrahimi, Mohammed Saidul Islam, Xiaodan Zhu et al.*
  - `2026-11-17`
  - Automated agent design searches for executable architectures that improve LLM-based agent performance, with evolutionary methods using language-model crossover to recombine promising mechanisms for task decomposition, model coordination, and verification. This search, however, is…

- **[GUARD: Stabilizing Recursive Self-Improvement with Regret Guidance](https://arxiv.org/abs/2611.23476v1)**
  - *Minghe Zhang, Xuetao Kang, Yifei Ming et al.*
  - `2026-11-17`
  - Autonomous AI agents pair a frozen base model with an editable harness of prompts, skills, tool rules, and memory. Recursive self-improvement (RSI) adapts this harness from experience without weight updates, yet self-editing without external graders often backfires: reflection an…

- **[Reliability by Architecture: Agentic Workflows for Validated Multi-Physics Simulation from Natural Language](https://arxiv.org/abs/2611.23473v1)**
  - *Søren Taverniers, Eric Darve, Hamdi A. Tchelepi*
  - `2026-11-17`
  - Preparing, executing, and validating strongly coupled multi-physics simulations require expert time. Agentic workflows use large language models (LLMs) to coordinate them from natural-language descriptions, but reliability requires checks of physical consistency and fidelity to t…

- **[PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory](https://arxiv.org/abs/2611.23010v1)**
  - *Haoyang Liu, Kecheng Liang, Xinyu Li et al.*
  - `2026-11-17`
  - Vision-language models (VLMs) can correctly interpret physics diagrams yet apply constraints outside the states or conditions in which they hold, causing premise errors to propagate through subsequent calculations. We introduce PhysScope, an inference-time visual harness that sup…

- **[RagHarnessDebugger: Jev-Guided Agentic RAG in Contract Inference Repair Auditing](https://arxiv.org/abs/2611.22991v1)**
  - *Moriya Dechtiar, Daniel Martin Katz, Michael J. Bommarito et al.*
  - `2026-11-17`
  - Agentic systems using retrieval-augmented generation (RAG) must repair their own answers by gathering more evidence, testing alternative policies and deciding if, when, and what repairs are needed. Yet how do we know if a system's repairs are working when metrics like accuracy ca…

- **[Evolution Under Fire: Evolving Agent Safety Harnesses with Adaptive Injection Stressors](https://arxiv.org/abs/2611.22583v1)**
  - *Yujun Wang, Yilun Liu, Jinhe Bi et al.*
  - `2026-11-17`
  - Tool-using language-model agents must act on information from untrusted emails, webpages, and documents. This creates a central security challenge: malicious instructions and legitimate task directives can arrive through the same interaction channel. Existing defenses are largely…

- **[MillBill: A Machining Agent with Geometric Feedback](https://arxiv.org/abs/2611.22565v2)**
  - *Gennadii Savrasov, Artem Slavin, Soslan Kabisov et al.*
  - `2026-11-17`
  - Turning a CAD model into a machining program requires both process knowledge and geometric precision. Language models can generate such workflows by writing geometry and toolpath code for each part, but this makes numerical execution part of the model's task. We introduce MillBil…

- **[Think Once, Act Fast: Cost-Effective Recursive Self-Improvement for Decision Model Harness](https://arxiv.org/abs/2611.22432v2)**
  - *Siqi Lai, Haitao Li, Hao Liu*
  - `2026-11-17`
  - Fast System-1 models enable responsive actions but struggle with complex or unfamiliar tasks. Large language model (LLM)-based System-2 provides strong reasoning capabilities, yet repeated invocation incurs substantial latency and computational costs. To bridge this gap, we propo…

- **[Reliable Evaluation of AI Agents for Investment Research: A Framework for Performance and Validity Assessment](https://arxiv.org/abs/2611.22338v1)**
  - *Dongnuan Tian, Yan Yu, Yangfan Liu et al.*
  - `2026-11-17`
  - We consider the problem of evaluating AI agents undertaking investment-research tasks, where agents interact with external information sources and computational tools to produce financial analyses and research reports. An important challenge is that the quality of an agent's fina…

- **[Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses](https://arxiv.org/abs/2611.22299v1)**
  - *Deep Shah, Nehal Kathrotia*
  - `2026-11-17`
  - Whether a foundation model succeeds as an autonomous agent depends as much on its runtime software as on its weights. This runtime, the agent harness, manages context and memory, steers multi-turn control, executes tool actions in sandboxes, and verifies work before stopping. Bec…

- **[OfficePrism: Benchmarking Agents on Single-Domain Operations Across Enterprise Business Functions](https://arxiv.org/abs/2611.22262v1)**
  - *Hanfeng Liu, Zhenyu Luo, Dongchao Zhang et al.*
  - `2026-11-17`
  - Broad workplace scores can mix competence within one business function with the extra cost of coordinating across functions and systems, making failures hard to localize. OfficePrism evaluates this prerequisite through 420 single-domain enterprise tasks spanning seven business fu…

- **[Readie: Low-Latency Code Sandboxes for AI Agents](https://arxiv.org/abs/2611.22171v1)**
  - *Arjun Sivaraman, Zhaoheng Li, Alan Shi et al.*
  - `2026-11-17`
  - From quantitative research to personal assistance, AI agents act by iteratively generating and executing code. To decouple the agent harness from code execution, many agents offload execution to dedicated systems called code sandboxes. However, existing code sandboxes suffer from…

- **[Big Brains, Tiny Board: Pupavision, an Agentic Physical AI Instrument for Monitoring Drosophila Pupariation and Lifecycle Transitions](https://arxiv.org/abs/2611.22136v1)**
  - *Joel Sadler, Daniel Graham, Melanie Worley*
  - `2026-11-17`
  - Many biology experiments are limited by the availability and ease of use of instruments that monitor and record them. For example, the timing of pupariation in the fruit fly Drosophila melanogaster, a widely used model organism, can provide biologically relevant information about…

- **[SkillBuffBench: Measuring What Agent Skills Contribute across Harnesses, Models, Skill Access Modes and Memory](https://arxiv.org/abs/2611.22017v1)**
  - *Gengyue Dong, Ye Wei, Zheng Zhu et al.*
  - `2026-11-17`
  - Agent Skills, file-based packages of procedural knowledge that a coding agent can discover and load on demand, are now shipped by every major agent harness, yet the evidence for how much they help comes almost entirely from settings in which the right Skill is hand-picked for the…

- **[Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate](https://arxiv.org/abs/2611.22461v1)**
  - *Ziaullah Khan, Abdul Rehman Khalid, Shrestha Nischal Lal et al.*
  - `2026-11-17`
  - Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it. We ask whether that is correct. In DebateGraph, four backends share one contract (read/write/snapshot), so…

- **[What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super](https://arxiv.org/abs/2611.22161v1)**
  - *Sushant Mehta, Edwin Chen*
  - `2026-11-17`
  - We post-train NVIDIA's Nemotron 3.5 Super (120B total, 12B active parameters) with reinforcement learning (RL) on five expert-built task datasets, one at a time: real-world software engineering, complex constraints, long-horizon tool use, professional chart understanding and ente…

- **[Remembered as Brief: Stored Preferences SilentlyRemove Decision-Critical Information](https://arxiv.org/abs/2611.22697v1)**
  - *Joshua Adrian Cahyono*
  - `2026-11-17`
  - People increasingly learn what they need for decisions about health, money, law and safety from AI assistants, and what an assistant leaves out the user never sees. An answer with a warning removed can be true in every sentence, so fact-checks pass it, and an assistant with memor…

- **[Seeing What Still Holds: How Waiting Control Changes Cooperative Recovery](https://arxiv.org/abs/2611.22368v1)**
  - *Kangjie Huang, Yucheng Xin, Xinchun Wang et al.*
  - `2026-11-17`
  - Changing the holding reference during a fixed-duration wait can reverse the ranking of visual recovery methods. We introduce AuditEmbodied, a paired execution and trajectory evaluation framework that independently varies holding references and waiting duration while keeping recov…

- **[FIRE-Drive: Feasibility-Informed Risk Evaluation for End-to-End Diffusion Planning](https://arxiv.org/abs/2611.22297v1)**
  - *Qifeng Xie, Kai-Yuan Feng, Wenkang Wan et al.*
  - `2026-11-17`
  - Diffusion-based end-to-end autonomous driving models have shown strong potential in generating multimodal planning trajectories. However, their performance still depends heavily on trajectory initialization, mode evaluation, and supervision quality. Weakly constrained noisy initi…

- **[MM-ReportBench: A Comprehensive Benchmark for Multimodal Report Generation from Tables](https://arxiv.org/abs/2611.22514v1)**
  - *Teng Lin, Nan Tang*
  - `2026-11-17`
  - The ability to generate multimodal reports integrating fluent narratives with faithful visualizations from tabular data, has become a cornerstone capability for modern vision-language models in practical domains such as finance, healthcare, and policy making. However, existing be…

- **[The Shared Word: Evaluating Language Models on Dutch Word Puzzles](https://arxiv.org/abs/2611.22935v1)**
  - *Rik van Noord, Maurice Voors*
  - `2026-11-17`
  - Many LLM benchmarks for languages other than English are translated, multiple-choice, or difficult to score automatically. We introduce The Shared Word (TSW-NL), a Dutch benchmark built around four core principles: it is language-specific, open-vocabulary, human-curated, and dete…

- **[Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2611.21847v1)**
  - *Prithwish Jana, Nikos Kanakaris, Purak Jain et al.*
  - `2026-11-16`
  - Large language model (LLM) agents can generate research ideas and improve scientific discovery through iterative experimentation. However, increasing the number of agents or iterations does not automatically translate to producing more diverse or feasible ideas. Agents may conver…

- **[SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents](https://arxiv.org/abs/2611.21541v1)**
  - *Brian T. Weston, Alondra Torres Contreras, Aldair E. Gongora*
  - `2026-11-16`
  - We introduce SciResearch-Eval, an interactive benchmark of scientific judgment built on a standard laboratory problem: measuring a material's thermal properties by heating it and fitting a heat-conduction simulator. An agent designs its own experiments, uses a supplied simulator…

- **[Harness Leverage Across Model Size: A Ladder of Five Local Agent Harnesses from 0.75B to 4.7B](https://arxiv.org/abs/2611.21407v1)**
  - *Hao Wang, Ting Huang*
  - `2026-11-16`
  - A harness turns a model into a system that completes tasks: it builds the prompt, exposes tools and decides when work is done. Harness comparisons hold the model fixed. Model comparisons hold the harness fixed. We vary both: five shipped harnesses, 18 artifact-producing tasks, fo…

- **[VisualArtifactSpec 1.0: Evaluating Visual Artifacts under Task Specifications](https://arxiv.org/abs/2611.21382v1)**
  - *Shuyi Ouyang, Xiaojun Tang, Zijian Zou et al.*
  - `2026-11-16`
  - Visual artifact tasks test agents' ability to translate task specifications and source materials into outputs that meet practical needs. Evaluation across artifact families helps distinguish broadly applicable authoring capabilities from strengths confined to a particular medium.…

- **[Bookkeeping Is Not Judgement: EJBench, an Engineering Judgement Benchmark Built from a Conjugate Heat Transfer Design Campaign](https://arxiv.org/abs/2611.21707v1)**
  - *James Sadler, Rotimi Alabi, Kotub Uddin*
  - `2026-11-16`
  - We introduce EJBench, a benchmark of engineering judgement: whether a model can predict how a design behaves at new conditions from a few earlier results, and decide on it. Unlike engineering benchmarks that test whether an agent can operate simulation or CAD software, EJBench is…

- **[Turing Agent: Agentic Formal Verification for Mathematical Research](https://arxiv.org/abs/2611.21299v1)**
  - *Yang Chen, Qianyi Wang, Ronghui Yang et al.*
  - `2026-11-16`
  - Large language models (LLMs) are rapidly advancing mathematical discovery, moving beyond benchmark-level problem solving to tackle frontier research problems. This progress is ushering mathematics into an era of proof abundance, raising a fundamental challenge: how can we ensure…

- **[Accelerate Bench: Evaluating Agents for Application-Level Program Optimization](https://arxiv.org/abs/2611.20882v1)**
  - *Bowen Liu, Yuhan Li, Nuo Chen et al.*
  - `2026-11-16`
  - Application optimization requires coding agents to discover useful changes and coordinate them across a complete program while preserving the required computation. We introduce Accelerate Bench, a benchmark of 32 CPU optimization tasks adapted from scientific applications and sup…

- **[VIVID: A Visual Harness for Agentic Video Editing](https://arxiv.org/abs/2611.20688v1)**
  - *Wenhan Yu, Zhaoxi Zhang, Zhilong Tan et al.*
  - `2026-11-16`
  - Video editing requires agents to make editing decisions grounded in audiovisual observations and precise temporal localization, and to evaluate their effects in rendered outputs. General-purpose coding agents possess strong comprehension, reasoning, and code execution capabilitie…

- **[VAHBench: A Harness Benchmark for Agentic Long-Video Generation](https://arxiv.org/abs/2611.20535v1)**
  - *Hongbo Zhang, Liuyang Song, Hang Zhou et al.*
  - `2026-11-16`
  - AI agents are commonly used for everyday information retrieval and coding. We ask whether they can also interpret human requests and turn them into complete videos. We introduce VAHBench, a benchmark that tests this ability through five short-drama briefs specifying story, charac…

- **[Agent-Guided Configuration Tuning for SMT Solvers](https://arxiv.org/abs/2611.20484v1)**
  - *Cong Wang, Qiaoyi Zheng, Zhaoguo Wang et al.*
  - `2026-11-16`
  - SMT solvers expose many configuration choices that determine how well their existing algorithms perform on a workload. We present, to our knowledge, the first workflow that uses general-purpose LLM agents to tune SMT solver configurations. Agents read solver documentation, source…

- **[DeltaHarness: Self-Evolving Harnesses for Resource-Adaptive Tool Execution](https://arxiv.org/abs/2611.21688v1)**
  - *Lecheng Yan, Jianze Lin, Xicheng Han et al.*
  - `2026-11-16`
  - Tool-using agents rely on execution harnesses to organize and schedule tool operations. The same task and resource description can conceal runtime conditions that reverse the latency ordering of valid execution plans. Resolving this uncertainty requires firsthand execution in the…

- **[CuRSE-Bench: A Benchmark for Probing Cultural Blind Spots in Text-to-Image Safety Evaluation](https://arxiv.org/abs/2611.20821v2)**
  - *Minsuk Jang, Minseok Son, KiHyun Seol et al.*
  - `2026-11-16`
  - Text-to-image (T2I) safety evaluation typically assigns each prompt or image a single culture-blind harm label, so content that is harmful only within a particular culture can pass as benign. We introduce CultureCraft, an agentic framework that constructs T2I prompts that appear…

- **[GPRM: Global Perspective Process Reward Model](https://arxiv.org/abs/2611.20755v1)**
  - *Zifan Zhang, Zhengbo Jiao, Shaobo Wang et al.*
  - `2026-11-16`
  - Process Reward Models (PRMs) are widely used for step-level evaluation of multi-step reasoning in large language models, but existing methods are often limited by weak historical dependency modeling and insufficient global awareness. They typically fail to leverage prior step eva…

- **[Invariant-Aware Harness Enforcement to Protect LLM Agents from Silent API Failures](https://arxiv.org/abs/2611.20595v1)**
  - *Sajib Acharjee Dip, Brian Ouyang, Lala Motlhabi*
  - `2026-11-16`
  - LLM agents answer questions by calling APIs and trusting the results. An API can fail silently. It ignores part of a request, such as a misnamed filter, yet returns HTTP 200 and a plausible but wrong result. Current fixes, such as checklists, reviewer models and LLM judges, ask t…

- **[OpenMAS-GApp: A Comprehensive Benchmark for Domain-Adaptive Multi-Agent Application Construction](https://arxiv.org/abs/2611.20997v1)**
  - *Xunkai Li, Kairui Yang, Jiaxi Li et al.*
  - `2026-11-16`
  - Constructing multi-agent system (MAS) applications across domains requires translating diverse requirements into executable systems, involving task decomposition, agent and tool selection, and execution organization. Existing studies have explored individual aspects of MAS constr…

- **[Language Models Can Rewrite Their Own Weights](https://arxiv.org/abs/2611.21885v2)**
  - *Jiajun Fan, Neil He, Changyi Yang et al.*
  - `2026-11-16`
  - A language model is trained once and frozen. Making it better takes another training run, or a prompt, a harness or extra computation at inference that is gone once the task ends. We show a third way: to our knowledge for the first time, a language model rewrites its own weights…

- **[MemEmo: Evaluating Emotion in Memory Systems](https://arxiv.org/abs/2611.20733v1)**
  - *Peng Liu, Zhen Tao, Jihao Zhao et al.*
  - `2026-11-16`
  - Memory systems address the challenge of context loss in Large Language Models during prolonged interactions. However, as an essential tool for warm companionship and personalized services, the effectiveness of memory systems in processing affective information remains underexamin…


## Finance  (153)

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


### ACL

- **[Algorithmic Market Making Can Lead to Rough Volatility Through the Order Book](https://arxiv.org/abs/2611.24028v1)**
  - *Sai Niranjan Ramachandran*
  - **ACL** · `2026-11-18`
  - Existing work suggests that markets can show volatility with paths rougher than those of Brownian motion. In theory this can happen when the order flow is close to instability with memory that decays as a power law. However, it is not fully clear how such order flow could arise f…

- **[From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)**
  - *Jing Luo, Yu-Chen Tian, Chu-Xue Cao et al.*
  - **ACL 2026** · `2026-05-07`
  - Large Language Model (LLM)-based agents have fundamentally reshaped artificial intelligence by integrating external tools and planning capabilities. While memory mechanisms have emerged as the architectural cornerstone of these systems, current research remains fragmented, oscill…

- **[FLAG-Trader: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading](https://arxiv.org/abs/2502.11433)**
  - *Guo-Jun Xiong, Zhiyang Deng, Ke-Yi Wang et al.*
  - **ACL 2025** · `2025-02-17`
  - Large language models (LLMs) fine-tuned on multimodal financial data have demonstrated impressive reasoning capabilities in various financial tasks. However, they often struggle with multi-step, goal-oriented scenarios in interactive financial markets, such as trading, where comp…


### Other / arXiv

- **[RICoT: Recurrent Interleaved Chain-of-Thought for Page Stream Segmentation](https://arxiv.org/abs/2611.22382)**
  - *Prashant Khatri, Bhavana Malagavalli, Saiful Haq et al.*
  - 🤗 Featured · `2026-11-17`
  - Large language models (LLMs) have renewed interest in Page Stream Segmentation (PSS), splitting a multi-page file into its constituent documents. Yet published LLM methods still frame the task as boundary classification over one or a few neighboring pages, and commercial document…

- **[Vibe-Trading: Towards Agent-Native Trading](https://arxiv.org/abs/2611.24845v1)**
  - *Haozhe Wu, Zhonghang Li, Chao Huang*
  - `2026-11-18`
  - Existing AI agents can retrieve information, call tools, run experiments, and produce multi-step outputs. Yet most are built around relatively static workflows and struggle to preserve reliable state as the environment changes. Financial trading makes this limitation especially c…

- **[OpenKAGE: Open-Ended Lifelong Learning in the Open World via Knowledge-Sharing Agent-Group Evolution](https://arxiv.org/abs/2611.24302v1)**
  - *Wenhao Yuan, Longhui Yuan, Zexi Jia et al.*
  - `2026-11-18`
  - Building autonomous agents that continually explore open worlds and acquire new capabilities through experience is a long-standing aspiration in artificial intelligence. Existing research often pursues lifelong learning within predefined tasks, curricula, or objectives, with self…

- **[A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises](https://arxiv.org/abs/2611.24039v1)**
  - *Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid*
  - `2026-11-18`
  - Agentic AI platforms-systems in which LLM agents plan, invoke tools, retain memory and coordinate to change the state of enterprise systems-are being procured faster than they can be measured. Public agent benchmarks score models in fixed harnesses; enterprises buy integrated pla…

- **[EVA-RSI: Recursive Self-Improvement of Video Evaluators for Judging Temporal Quality](https://arxiv.org/abs/2611.23890v1)**
  - *Yu Yuan, Ruizhou Ding, Shaoheng Fang et al.*
  - `2026-11-18`
  - Video evaluators play an important role in video generation, yet they miss motion defects, limiting the quality of generated videos. Recursive self-improvement (RSI) has made strong progress in mathematics and coding, where explicit verifiers provide reliable feedback on a single…

- **[Communicative On-Policy Distillation: Distilling Black-Box Teacher Capabilities through Communication for Long-Horizon Tasks](https://arxiv.org/abs/2611.23673v1)**
  - *Lirui Luo, Kelong Mao, Xinwei Yang et al.*
  - `2026-11-18`
  - On-policy distillation (OPD) is a powerful paradigm for improving language-model agents on long-horizon tasks, yet its conventional formulation relies on teacher logits that text-only black- box models do not expose. To address this limitation, we introduce Communicative On-Polic…

- **[Meta-LSQ: A Closed-Form Sobolev Inner Solver for Few-Shot Meta-Learning](https://arxiv.org/abs/2611.24718v1)**
  - *Antonin Sulc*
  - `2026-11-18`
  - Gradient-based meta-learners such as model-agnostic meta-learning (MAML) adapt to a new task with an inner loop of gradient descent that has to be differentiated through, and they meta-learn every network weight. Meta-LSQ instead fits each task with one regularised least-squares…

- **[Prognosis Without Prediction: The Intrinsic Geometry of Survival](https://arxiv.org/abs/2611.24799v1)**
  - *Atahan Karagoz*
  - `2026-11-18`
  - Modeling systemic failure in high-dimensional environments is fundamentally limited by supervised algorithms that attempt to predict sparse, noisy or censored endpoints. To break this reliance on explicit outcome regression, we engineered the Self-Organizing Survival Manifolds (S…

- **[Reconstruction vs. Prediction Pre-Training of Discrete Video Representations for Continuous Control](https://arxiv.org/abs/2611.24781v1)**
  - *Ron Kosova, Francesco Croce*
  - `2026-11-18`
  - Self-supervised video encoders are commonly trained to either reconstruct pixels or predict latent features, yet it remains unclear how these objectives shape representations for downstream dynamics. We present a capacity-matched study isolating this choice: two identical video e…

- **[When Price Charts Rhyme: Historical Visual Retrieval for Stock Return Prediction](https://arxiv.org/abs/2611.23723v1)**
  - *Hui Chen, Haoyu Liu, Ke Wu et al.*
  - `2026-11-18`
  - We study whether visually similar price histories predict similar future returns, using a vision model to retrieve each stock's most similar charts from three decades of U.S. price histories. A representation pretrained only on natural images already retrieves neighbors whose rea…

- **[Reliability by Architecture: Agentic Workflows for Validated Multi-Physics Simulation from Natural Language](https://arxiv.org/abs/2611.23473v1)**
  - *Søren Taverniers, Eric Darve, Hamdi A. Tchelepi*
  - `2026-11-17`
  - Preparing, executing, and validating strongly coupled multi-physics simulations require expert time. Agentic workflows use large language models (LLMs) to coordinate them from natural-language descriptions, but reliability requires checks of physical consistency and fidelity to t…

- **[Where the Tokens Go: Heat, Entropy and Error in Agentic Coding](https://arxiv.org/abs/2611.23375v1)**
  - *Alán Aspuru-Guzik, Varinia Bernales*
  - `2026-11-17`
  - Coding agents are billed by the token, yet software engineering says nothing about what a token actually buys. Here we introduce a theory of software thermodynamics. The theory draws analogues from classical and stochastic thermodynamics, extends them, and applies them to modern…

- **[How Web Research Agents Interpret User Priorities](https://arxiv.org/abs/2611.22989v1)**
  - *Robin Sharma, Parisa Suchdev*
  - `2026-11-17`
  - Web research agents gather information online and write cited reports, including financial analysis. Users can state a priority to guide this research, but a priority may not say how to judge the options, leaving the agent to choose the criteria. We examine how two such agents, b…

- **[Verifying Agents in Rubric-Graded Environments](https://arxiv.org/abs/2611.22841v1)**
  - *Markus Dücker, Vaibhav Kumar, Yi Liu et al.*
  - `2026-11-17`
  - As AI agents take on increasingly open-ended and complex tasks, verifying their outputs has proven to be difficult. Rubric-graded agent environments, where a verifier judges multiple natural-language criteria against the deliverables and environment state changes produced by the…

- **[Reliable Evaluation of AI Agents for Investment Research: A Framework for Performance and Validity Assessment](https://arxiv.org/abs/2611.22338v1)**
  - *Dongnuan Tian, Yan Yu, Yangfan Liu et al.*
  - `2026-11-17`
  - We consider the problem of evaluating AI agents undertaking investment-research tasks, where agents interact with external information sources and computational tools to produce financial analyses and research reports. An important challenge is that the quality of an agent's fina…

- **[OfficePrism: Benchmarking Agents on Single-Domain Operations Across Enterprise Business Functions](https://arxiv.org/abs/2611.22262v1)**
  - *Hanfeng Liu, Zhenyu Luo, Dongchao Zhang et al.*
  - `2026-11-17`
  - Broad workplace scores can mix competence within one business function with the extra cost of coordinating across functions and systems, making failures hard to localize. OfficePrism evaluates this prerequisite through 420 single-domain enterprise tasks spanning seven business fu…

- **[The Only Edge Was Memorized in Training: LLM Trading Agents Around Earnings and Bad News](https://arxiv.org/abs/2611.22177v1)**
  - *Jackson Wang*
  - `2026-11-17`
  - Large language model (LLM) trading agents are tested on news, but news reaches stock prices within minutes, and a benchmark that replays headlines at their publication time finds no alpha in trading on them. Money can then remain in two places, before news whose date is known, su…

- **[ATLAS-Finance: Benchmarking AI Agents in Realistic Banking Environments](https://arxiv.org/abs/2611.22085v1)**
  - *Elaine Lau, Antoine Pangas, Alexandre Finot et al.*
  - `2026-11-17`
  - Professional work involves under-specified assignments, where relevant information is spread across workplace applications and may conflict or change over time. To evaluate how well frontier agents can perform economically valuable work in such settings, we introduce ATLAS-Financ…

- **[MM-ReportBench: A Comprehensive Benchmark for Multimodal Report Generation from Tables](https://arxiv.org/abs/2611.22514v1)**
  - *Teng Lin, Nan Tang*
  - `2026-11-17`
  - The ability to generate multimodal reports integrating fluent narratives with faithful visualizations from tabular data, has become a cornerstone capability for modern vision-language models in practical domains such as finance, healthcare, and policy making. However, existing be…

- **[Can LLMs Understand What They Predict? Evaluating Latent Causal Structure Inference in Financial Markets](https://arxiv.org/abs/2611.23533v1)**
  - *Yixiang Zheng, Yuechen Jiang, Zhiwei Liu et al.*
  - `2026-11-17`
  - Large language models (LLMs) are increasingly evaluated through their ability to predict future outcomes, implicitly assuming that predictive success reflects an understanding of the underlying system. However, accurate predictions can often be achieved without recovering the lat…

- **[DDSL: Iterative Self-Labeling for Financial Market States](https://arxiv.org/abs/2611.22958v1)**
  - *Xianbin Gu, Qingyue Zhu, Yuhong Geng*
  - `2026-11-17`
  - Financial market states lack a unique ground truth and must therefore be constructed from price data. Conventional labeling methods typically define states independently of the downstream classifier, leaving unresolved whether the resulting labels can be recovered from informatio…

- **[StitchRAG: Constructing Compact and Evidence-Preserving Contexts for RAG with Diffusion-Based Stitching](https://arxiv.org/abs/2611.22766v1)**
  - *Minsang Kim, Junpyo Lim, Heeje Cho et al.*
  - `2026-11-17`
  - Retrieval-augmented generation (RAG) improves factuality by grounding large language models (LLMs) in external evidence. However, long retrieved contexts incur computational overhead and can even hurt performance due to noisy or irrelevant content. We propose \textsc{StitchRAG},…

- **[When AUC Meets Generative Reconstruction: A Unified Principle for Balanced Visual Representation Learning](https://arxiv.org/abs/2611.22094v1)**
  - *Boyu Han, Qianqian Xu, Shilong Bao et al.*
  - `2026-11-17`
  - Multimodal large language models (MLLMs) require visual encoders that extract fine-grained visual features while constructing semantically disentangled and discriminative representations. Conventional methodologies encounter a fundamental trade-off: contrastive learning enhances…

- **[The Illusion of Grounding: Do Vision-Language Models Weigh Retrieved Text and Images Like an Ideal Observer?](https://arxiv.org/abs/2611.23127v1)**
  - *Basavaraj R M, Harshal Chandel*
  - `2026-11-17`
  - Retrieval-augmented vision-language models (VLMs) answer from two sources of evidence that can each fail: the retrieved text can be wrong or noisy, and the image can be degraded or contradicted. We introduce GIB-200K, 200,000 image-question items built from COCO and Visual Genome…

- **[Safe Resemblance, Silent Propagation: Limits of Text-Similarity Guardrails for AI Agent Safety](https://arxiv.org/abs/2611.21520v1)**
  - *Charles Xiao*
  - `2026-11-16`
  - When AI agents relay information to one another, an output can preserve an injected instruction's effect on downstream agents even after its wording changes, yet legitimate quotation and template reuse can produce high textual overlap with the source, so text-similarity guardrail…

- **[RESILAGENT: A Three-Pillar Architecture for Cyber-Physical Resilience in Electrical Power and Energy Systems](https://arxiv.org/abs/2611.21480v1)**
  - *Nikolaos Kekatos, Georgios Koutidis, Konstantinos Antonakopoulos et al.*
  - `2026-11-16`
  - Electrical Power and Energy Systems face hybrid threats that combine cyber intrusions, physical sabotage and climate-driven stress, and routinely outpace today's siloed monitoring stacks. We present RESILAGENT, a concept architecture organised around three operational pillars, Se…

- **[WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection](https://arxiv.org/abs/2611.21373v1)**
  - *Yipeng Du, Yuxi Li, Ying Zhang et al.*
  - `2026-11-16`
  - Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that off…

- **[Benchleaking Is Accelerating: Benchmark contamination has worsened sharply in the past month -- from post-training down to pre-training base models](https://arxiv.org/abs/2611.21315v1)**
  - *Yiwei Qin, Muhang Xie, Xuefeng Li et al.*
  - `2026-11-16`
  - Benchmark contamination is not new, but recent model releases show it in a sharper form. We use the term benchleaking for the case in which a benchmark's own test examples enter training data, so that a score reflects recall rather than capability. This differs from benchmaxxing,…

- **[Think2Listen: Evidence-Centric Learning For Agentic Audio Understanding With LALMS](https://arxiv.org/abs/2611.21083v1)**
  - *Jin Wang, Liang Lin, Kaiwen Luo et al.*
  - `2026-11-16`
  - Recent advances in large audio-language models (LALMs) have broadened audio understanding across speech, sound, and music, with tool-based agents further supporting these tasks by invoking predefined audio tools. However, a persistent gap remains between perceiving acoustic conte…

- **[K2-Horizon: A Frontier Fleet of Open Source Language Models](https://arxiv.org/abs/2611.21003v1)**
  - *K2 Team, Zhengzhong Liu, Haonan Li et al.*
  - `2026-11-16`
  - We present K2-Horizon, a fleet of six fully open language models, from a 0.9B dense model to a 375B-A23B MoE, built for general-purpose reasoning and agentic work across math and science, software engineering, deep research, office automation, and beyond. The models lead or are c…

- **[Experience Rot: Experienced Agents Fail Where Novices Succeed](https://arxiv.org/abs/2611.20922v1)**
  - *Zhen Xu, Hang Yin, Zitao Zhang et al.*
  - `2026-11-16`
  - Agents are increasingly built to learn from experience: they keep conversation histories, memory files, retrieved notes and skills, and reuse what worked before. We show that this experience turns against them when their tools change silently. We test a range of models with tools…

- **[Conversing with a Conversational Agent: A Real Conversation, Not a Simulated One](https://arxiv.org/abs/2611.20826v1)**
  - *Christophe Denis*
  - `2026-11-16`
  - The claim that interactions with artificial conversational agents merely simulate human conversation rests on a philosophical distinction between reproducing the observable features of an activity and actually performing it. Although this distinction is appropriate for certain ph…

- **[ToolGraph as a Q-Function for Test-Time Scaling of Tool-Use Agents](https://arxiv.org/abs/2611.20569v1)**
  - *Ke Shen, Ankita Bhaumik, Li Dong et al.*
  - `2026-11-16`
  - Tool-use agents must chain interdependent calls, yet which outputs satisfy which later inputs in a deployed catalog is not something a general-purpose language model reliably infers from tool descriptions alone. We compile that structure once into a reusable external representati…

- **[FinVerify: A Verification Framework for Financial Agents](https://arxiv.org/abs/2611.20423v1)**
  - *Mao Guan, Qian Chen, Ge Meng et al.*
  - `2026-11-16`
  - Financial agents produce numerical claims that can be wrong even when their calculations execute correctly, due to mismatched reporting periods, unsupported sources, incompatible units, or incorrect financial definitions. We introduce FinVerify, an evidence-grounded framework for…

- **[Implicit-Reasoning-Enabled Elastic Semantic Communications for AI-Agent Networks](https://arxiv.org/abs/2611.20399v1)**
  - *Kaiwen Yu, Gang Wu, Jiancun Fan et al.*
  - `2026-11-16`
  - AI-agent networks introduce new communication demands driven by proactive interactions and autonomous task execution. Existing adaptive semantic communication schemes primarily adjust semantic representations and resource configurations within predefined processing scales and cap…

- **[Deploying a Control-Logic LLM Assistant in Air-Gapped Power Plants: Lessons in Source Authority and Bounded Retrieval](https://arxiv.org/abs/2611.20398v1)**
  - *Yiwei Fu, Nicholas Gabriel*
  - `2026-11-16`
  - Deploying Large Language Model (LLM) assistants in industrial operational technology environments poses constraints largely absent from cloud applications: site policies restrict engineering and operational data from leaving the plant, on-premises compute is limited, and incorrec…

- **[Tight PAC-Bayes Generalisation Guarantees for Large Language Model Judges](https://arxiv.org/abs/2611.20818v1)**
  - *Tom A. Lamb, Philip H. S. Torr, Tim G. J. Rudner*
  - `2026-11-16`
  - Large language model (LLM) judges are increasingly used to monitor the outputs of LLM-based AI agents, yet formal guarantees on the reliability of these judges remain largely absent, limiting confidence in their use for safety-critical oversight. We consider certifying such a jud…

- **[Corrupting Ties: Investigating Robustness to Bias Injection Across Multi-Agent Network Topologies](https://arxiv.org/abs/2611.21804v1)**
  - *Cléa Chataigner, Mina Arzaghi, Florian Carichon et al.*
  - `2026-11-16`
  - AI systems are increasingly deployed in high-stakes decision-making contexts, where interactions among components can introduce fairness risks that remain undetected when auditing components or collective outcomes in isolation. As LLM-based multi-agent systems become more prevale…

- **[MemDoctor: Stage-wise Error Attribution and Repair for MLLM Agent Memory](https://arxiv.org/abs/2611.21019v1)**
  - *Ruiyang Jiang, Xinyang Liao, Weikai Huang et al.*
  - `2026-11-16`
  - Multimodal large language models (MLLMs) now assist users across sessions of images and text, carried by an external memory of what was said and shown. When such an assistant answers wrongly, the failure usually began earlier, in how a record was written, updated or retrieved, an…

- **[CuRSE-Bench: A Benchmark for Probing Cultural Blind Spots in Text-to-Image Safety Evaluation](https://arxiv.org/abs/2611.20821v2)**
  - *Minsuk Jang, Minseok Son, KiHyun Seol et al.*
  - `2026-11-16`
  - Text-to-image (T2I) safety evaluation typically assigns each prompt or image a single culture-blind harm label, so content that is harmful only within a particular culture can pass as benign. We introduce CultureCraft, an agentic framework that constructs T2I prompts that appear…

- **[Operating an Agent-Driven Dataset Factory: Discovery, Construction, and Public Release](https://arxiv.org/abs/2611.21957v1)**
  - *Eduardo Ariño de la Rubia, Szilard Pafka*
  - `2026-11-16`
  - Turning public data into prediction datasets requires connecting source discovery, task definition, construction, and distribution. We deployed Dataset Factory to perform these steps continuously under a standing release policy. Bounded language-model tasks interpret sources, wri…

- **[When Does Interaction Help? Toward a Reynolds Number for Collective Intelligence](https://arxiv.org/abs/2611.20773v1)**
  - *Xuening Wu, Haode Yang, Yanlan Kang et al.*
  - `2026-11-16`
  - Multi-agent systems combine distributed information through interaction, which can improve performance but also spread errors or suppress useful differences. Predicting when interaction helps is central to understanding and designing collective intelligence. We investigate whethe…

- **[Strategic Repayment and Latent Fragility in Financial Networks: Why Banks Withhold Payable Liquidity](https://arxiv.org/abs/2611.21262v1)**
  - *Hicham El Kaissi*
  - `2026-11-16`
  - A network in which every bank pays in full can nevertheless admit a self-fulfilling settlement freeze under the same balance-sheet fundamentals. Thus, observing full repayment does not establish the uniqueness or robustness of the payment equilibrium. We derive this result from a…

- **[KV-LTM: Persistent Per-Session KV Caches as Long-Term Memory for Personal Assistants](https://arxiv.org/abs/2611.21998v1)**
  - *Ziv Kfir, Ido Kfir*
  - `2026-11-16`
  - Personal assistants accumulate months of conversations, but today's long-term memory stacks put derivation or selection between a question and its evidence. In a system-level comparison on LongMemEval, two commercial assistants scored well below the same model reading the history…

- **[Inference Equivalence and Quotient Coding](https://arxiv.org/abs/2611.21096v1)**
  - *Zibo Meng, Andrew C. M. Austin, Alin Achim*
  - `2026-11-16`
  - Incomplete observations can admit multiple physical interpretations without making every task conclusion ambiguous. Recovering all compatible scenes is often unnecessary, whereas indiscriminate compression may change which claims are justified. We ask which distinctions among obs…

- **[Cap-Aware Boosting for Green Day-Ahead Electricity Price Forecasting](https://arxiv.org/abs/2611.21149v1)**
  - *Shubham Pratap*
  - `2026-11-16`
  - Accurate forecasting of Green Day-Ahead Market (GDAM) electricity prices is essential for market participants in the Indian power sector. We present a LightGBM-based forecasting framework for Indian Energy Exchange GDAM prices, which clear in 96 fifteen-minute intervals per day.…

- **[Markov-Equivalent Conditional Independence Graphs on Path Spaces](https://arxiv.org/abs/2611.20877v1)**
  - *Simon Kempf, Niki Kilbertus, Georg Manten*
  - `2026-11-16`
  - Causal discovery for continuous-time stochastic processes with latent confounding typically faces a trade-off between (i) approaches that are highly informative about the causal structure but are difficult to test statistically, and (ii) approaches that admit practical tests from…

- **[Revisiting Equity-Bond Diversification under Tail Risk and Structural Market Change: Evidence from Global ETFs and Model-Implied Option Prices](https://arxiv.org/abs/2611.21897v1)**
  - *Farzana Afroz, Abootaleb Shirvani, Nicholas Appiah et al.*
  - `2026-11-16`
  - This study examines thirty equity--bond and multi-asset exchange-traded funds (ETFs) listed in the United States, Canada, and Australia using daily U.S.-dollar returns over 2020--2024. A rolling-window framework compares minimum-variance and Conditional Value-at-Risk (CVaR) portf…

- **[EWMA Principal Eigenportfolios of Equity Returns: Market Representation and Beta-Hedging Performance](https://arxiv.org/abs/2611.20363v1)**
  - *Andrew Kangmin Kim, Aurora Neyan Zhou*
  - `2026-11-16`
  - This study examines whether an adaptively estimated principal eigenportfolio improves equity beta hedging relative to capitalisation-weighted and equal-weighted market benchmarks. Using stock returns from a historically changing S&P 500 universe, it constructs a portfolio from th…

- **[Shortcut Learning in Feature-Based Algorithm Selection](https://arxiv.org/abs/2611.20440v1)**
  - *Shuhei Tanaka, Shoichiro Tanaka, Toshiharu Hatanaka*
  - `2026-11-16`
  - Landscape features give learning models information about the objective function for algorithm selection, algorithm configuration, and performance prediction. Should these features capture more information? Not always, because a model may rely on information that the algorithms i…

- **[A Second Order Transport Scheme for Dynamic Portfolio Subspaces under a Varying Risk Metric](https://arxiv.org/abs/2611.20911v1)**
  - *Alejandro Rodriguez Dominguez*
  - `2026-11-16`
  - We analyze the transport of portfolio exposures between moving subspaces under a varying positive definite risk metric. The reference evolution is the induced connection obtained from the ambient connection of minimum norm in fixed asset coordinates. An explicit expansion of risk…


---
*Generated 2026-11-19 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
