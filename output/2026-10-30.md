# Daily Paper Digest — 2026-10-30 (Friday)

| Source | Topics |
|--------|--------|
| AAAI · NeurIPS · ICML · ICLR · CVPR · KDD · ACL · EMNLP · NAACL · IJCAI · HuggingFace · OpenReview | Agent · Harness · Finance |

**554 unique papers** (705 topic-entries — cross-topic papers counted once per category)

---

## Agent  (406)

### AAAI

- **[A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators](https://doi.org/10.1609/aaai.v40i35.40240)**
  - *Ming-Ming Zhao, Xiaokang Wei, Yuan-Qi Shao et al.*
  - **AAAI 2026** · `2026-03-14`
  - Large language models (LLMs) have shown strong potential in automating the design of agentic workflows. However, existing methods still rely heavily on manually predefined operators, limiting generalization and scalability. To address this issue, we propose A²Flow, a fully automa…

- **[LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042)**
  - *Cheng Yang, Hui Jin, Xinlei Yu et al.*
  - **AAAI 2025** · `2025-11-26`
  - Diagnosing lung cancer typically involves physicians identifying lung nodules in Computed tomography (CT) scans and generating diagnostic reports based on their morphological features and medical expertise. Although advancements have been made in using multimodal large language m…

- **[Prune4Web: DOM Tree Pruning Programming for Web Agent](https://arxiv.org/abs/2511.21398)**
  - *Jia-Yuan Zhang, Kai-Quan Chen, Zhihao Lu et al.*
  - **AAAI 2025** · `2025-11-26`
  - Web automation uses intelligent agents to perform high-level tasks by mimicking human interactions with webpages. Despite recent advances in LLM-based web agents, efficiently navigating complex, real-world webpages remains challenging due to massive DOM structures (10,000 ~ 100,0…

- **[Rethinking the Reliability of Multi-agent System: A Perspective from Byzantine Fault Tolerance](https://arxiv.org/abs/2511.10400)**
  - *Li-Fan Zheng, Jiawei Chen, Qing-Hong Yin et al.*
  - **AAAI 2025** · `2025-11-13`
  - Ensuring the reliability of agent architectures and effectively identifying problematic agents when failures occur are crucial challenges in multi-agent systems (MAS). Advances in large language models (LLMs) have established LLM-based agents as a major branch of MAS, enabling ma…

- **[Talk2Image: A Multi-Agent System for Multi-Turn Image Generation and Editing](https://arxiv.org/abs/2508.06916)**
  - *Shichao Ma, Yun-He Guo, Jia-Hao Su et al.*
  - **AAAI 2025** · `2025-08-09`
  - Text-to-image generation tasks have driven remarkable advances in diverse media applications, yet most focus on single-turn scenarios and struggle with iterative, multi-turn creative tasks. Recent dialogue-based systems attempt to bridge this gap, but their single-agent, sequenti…


### NeurIPS

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **NeurIPS 2025** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…

- **[DyFlow: Dynamic Workflow Framework for Agentic Reasoning](https://arxiv.org/abs/2509.26062)**
  - *Yan-Bo Wang, Zi-Xiang Xu, Yue Huang et al.*
  - **NeurIPS 2025** · `2025-09-30`
  - Agent systems based on large language models (LLMs) have shown great potential in complex reasoning tasks, but building efficient and generalizable workflows remains a major challenge. Most existing approaches rely on manually designed processes, which limits their adaptability a…

- **[How to Train Your LLM Web Agent: A Statistical Diagnosis](https://arxiv.org/abs/2507.04103)**
  - *Dheeraj Vattikonda, Santhoshi Ravichandran, Emiliano Penaloza et al.*
  - **NeurIPS 2025** · `2025-07-05`
  - LLM-based web agents have recently made significant progress, but much of it has occurred in closed-source systems, widening the gap with open-source alternatives. Progress has been held back by two key challenges: first, a narrow focus on single-step tasks that overlooks the com…

- **[Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://arxiv.org/abs/2506.21506)**
  - *Boyu Gou, Zan-Ming Huang, Yu-Ting Ning et al.*
  - **NeurIPS 2025** · `2025-06-26`
  - Agentic search such as Deep Research systems-where agents autonomously browse the web, synthesize information, and return comprehensive citation-backed answers-represents a major shift in how users interact with web-scale information. While promising greater efficiency and cognit…

- **[Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence](https://arxiv.org/abs/2506.15677)**
  - *Yi-Ning Hong, Rui Sun, Bing-Xuan Li et al.*
  - **NeurIPS 2025** · `2025-06-18`
  - AI agents today are mostly siloed - they either retrieve and reason over vast amount of digital information and knowledge obtained online; or interact with the physical world through embodied perception, planning and action - but rarely both. This separation limits their ability…

- **[CoP: Agentic Red-teaming for Large Language Models using Composition of Principles](https://arxiv.org/abs/2506.00781)**
  - *Chen Xiong, Pin-Yu Chen, Tsung-Yi Ho*
  - **NeurIPS 2025** · `2025-06-01`
  - Recent advances in Large Language Models (LLMs) have spurred transformative applications in various domains, ranging from open-source to proprietary LLMs. However, jailbreak attacks, which aim to break safety alignment and user compliance by tricking the target LLMs into answerin…

- **[AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents](https://arxiv.org/abs/2506.00641)**
  - *Han-Jun Luo, Shenyu Dai, Chiming Ni et al.*
  - **NeurIPS 2025** · `2025-05-31`
  - Despite the rapid advancement of LLM-based agents, the reliable evaluation of their safety and security remains a significant challenge. Existing rule-based or LLM-based evaluators often miss dangers in agents'step-by-step actions, overlook subtle meanings, fail to see how small…

- **[STRATUS: A Multi-agent System for Autonomous Reliability Engineering of Modern Clouds](https://arxiv.org/abs/2506.02009)**
  - *Yin-Fang Chen, Jia-Qi Pan, J. Clark et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - In cloud-scale systems, failures are the norm. A distributed computing cluster exhibits hundreds of machine failures and thousands of disk failures; software bugs and misconfigurations are reported to be more frequent. The demand for autonomous, AI-driven reliability engineering…

- **[MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement](https://arxiv.org/abs/2506.15692)**
  - *Jaehyun Nam, Jinsung Yoon, Jie-Feng Chen et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - Agents based on large language models (LLMs) for machine learning engineering (MLE) can automatically implement ML models via code generation. However, existing approaches to build such agents often rely heavily on inherent LLM knowledge and employ coarse exploration strategies t…

- **[Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding](https://arxiv.org/abs/2505.18079)**
  - *Xiaoyi Zhang, Zhao-Yang Jia, Zong-Yu Guo et al.*
  - **NeurIPS 2025** · `2025-05-23`
  - Long-form video understanding presents significant challenges due to extensive temporal-spatial complexity and the difficulty of question answering under such extended contexts. While Large Language Models (LLMs) have demonstrated considerable advancements in video analysis capab…

- **[AutoData: A Multi-Agent System for Open Web Data Collection](https://arxiv.org/abs/2505.15859)**
  - *Tian-Yi Ma, Yi-Yue Qian, Zhe-Yuan Zhang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - The exponential growth of data-driven systems and AI technologies has intensified the demand for high-quality web-sourced datasets. While existing datasets have proven valuable, conventional web data collection approaches face significant limitations in terms of human effort and…

- **[MLZero: A Multi-Agent System for End-to-end Machine Learning Automation](https://arxiv.org/abs/2505.13941)**
  - *Haoyang Fang, Bo-Ran Han, Nick Erickson et al.*
  - **NeurIPS 2025** · `2025-05-20`
  - Existing AutoML systems have advanced the automation of machine learning (ML); however, they still require substantial manual configuration and expert input, particularly when handling multimodal data. We introduce MLZero, a novel multi-agent framework powered by Large Language M…

- **[WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)**
  - *Ivan Evtimov, A. Zharmagambetov, Aaron Grattafiori et al.*
  - **NeurIPS 2025** · `2025-04-22`
  - Autonomous UI agents powered by AI have tremendous potential to boost human productivity by automating routine tasks such as filing taxes and paying bills. However, a major challenge in unlocking their full potential is security, which is exacerbated by the agent's ability to tak…

- **[Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657)**
  - *M. Cemri, Melissa Z. Pan, Shuyi Yang et al.*
  - **NeurIPS 2025** · `2025-03-17`
  - Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal. This gap highlights a critical need for a principled understanding of why MAS fail. Addressing this question requires systematic identification and analysis of f…

- **[AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/abs/2503.09780)**
  - *A. Zharmagambetov, Chuan Guo, Ivan Evtimov et al.*
  - **NeurIPS 2025** · `2025-03-12`
  - Autonomous AI agents that can follow instructions and perform complex multi-step tasks have tremendous potential to boost human productivity. However, to perform many of these tasks, the agents need access to personal information from their users, raising the question of whether…


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
  - **ICML 2026** · OpenReview · `2022-01-01`
  - Cryptocurrencies are peer-to-peer digital assets monitored and organised by a blockchain network. Price prediction has been a significant focus point with various machine learning algorithms, especially concerning cryptocurrency. This work addresses the challenge faced by traders…

- **[Trading Agents](https://openreview.net/forum?id=8QTqyKAeeN)**
  - *Michael P. Wellman*
  - **ICML 2025** · OpenReview · `2011-01-01`
  - Automated trading in electronic markets is one of the most common and consequential applications of autonomous software agents.

- **[Learning Lotteries with Minimal Stakeholder Violations from Membership Queries](https://arxiv.org/abs/2610.37828v1)**
  - *Nicholas Teh, Paul W. Goldberg*
  - **ICML** · `2026-10-27`
  - An AI developer often has several candidate versions of a system and can deploy a mixture of them, sending each request to a randomly chosen version, as in A/B testing. Each stakeholder (e.g., a safety team, a regulator, or a customer with private test data) accepts a mixture exa…

- **[Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://arxiv.org/abs/2505.19433)**
  - *Pei-Jie Dong, Zhen-Heng Tang, Xiang-Hong Liu et al.*
  - **ICML 2025** · `2025-05-26`
  - Post-training compression reduces the computational and memory costs of large language models (LLMs), enabling resource-efficient deployment. However, existing compression benchmarks only focus on language modeling (e.g., perplexity) and natural language understanding tasks (e.g.…

- **[CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities](https://arxiv.org/abs/2503.17332)**
  - *Yuxuan Zhu, Antony Kellermann, Dylan Bowman et al.*
  - **ICML 2025** · `2025-03-21`
  - Large language model (LLM) agents are increasingly capable of autonomously conducting cyberattacks, posing significant threats to existing applications. This growing risk highlights the urgent need for a real-world benchmark to evaluate the ability of LLM agents to exploit web ap…

- **[SafeArena: Evaluating the Safety of Autonomous Web Agents](https://arxiv.org/abs/2503.04957)**
  - *Ada Defne Tur, Nicholas Meade, Xing Han Lù et al.*
  - **ICML 2025** · `2025-03-06`
  - LLM-based agents are becoming increasingly proficient at solving web-based tasks. With this capability comes a greater risk of misuse for malicious purposes, such as posting misinformation in an online forum or selling illicit substances on a website. To evaluate these risks, we…


### ICLR

- **[Re-Aligning Language to Visual Objects with an Agentic Workflow](https://arxiv.org/abs/2503.23508)**
  - *Yuming Chen, Jiangyan Feng, Hao-Dong Zhang et al.*
  - **ICLR 2025** · `2025-03-30`
  - Language-based object detection (LOD) aims to align visual objects with language expressions. A large amount of paired data is utilized to improve LOD model generalizations. During the training process, recent studies leverage vision-language models (VLMs) to automatically genera…

- **[Flow: Modularized Agentic Workflow Automation](https://arxiv.org/abs/2501.07834)**
  - *Boye Niu, Yi-Liao Song, Kai Lian et al.*
  - **ICLR 2025** · `2025-01-14`
  - Multi-agent frameworks powered by large language models (LLMs) have demonstrated great success in automated planning and task execution. However, the effective adjustment of agentic workflows during execution has not been well studied. An effective workflow adjustment is crucial…


### KDD

- **[Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems](https://arxiv.org/abs/2605.06457)**
  - *Dong-Hao Huang, Joon Kiat Chua, Zhao-Xia Wang*
  - **KDD 2026** · `2026-05-07`
  - LLM-based multi-agent systems are increasingly deployed for payment workflows, yet prevailing metrics, Task Success Rate (TSR) and Agent Handoff F1-Score (HF1), capture only final outcomes or unordered routing decisions. We introduce the Agentic Success Rate (ASR), a trajectory-f…

- **[PeroMAS: A Multi-agent System of Perovskite Material Discovery](https://arxiv.org/abs/2602.13312)**
  - *Yi-Shu Wang, Wei Liu, Yifang Li et al.*
  - **KDD 2026** · `2026-02-10`
  - As a pioneer of the third-generation photovoltaic revolution, Perovskite Solar Cells (PSCs) are renowned for their superior optoelectronic performance and cost potential. The development process of PSCs is precise and complex, involving a series of closed-loop workflows such as l…

- **[DeepTravel: An End-to-End Agentic Reinforcement Learning Framework for Autonomous Travel Planning Agents](https://arxiv.org/abs/2509.21842)**
  - *Yansong NING, Rui Liu, Jun Wang et al.*
  - **KDD 2025** · `2025-09-26`
  - Travel planning (TP) agent has recently worked as an emerging building block to interact with external tools/resources for travel itinerary generation, ensuring an enjoyable user experience. Despite its benefits, existing studies rely on hand-craft prompt and fixed agent workflow…

- **[Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504)**
  - *Mahmoud Mohammadi, Yi-Peng Li, Jean-Pierre Lo et al.*
  - **KDD 2025** · `2025-07-29`
  - The rise of LLM-based agents has opened new frontiers in AI applications, yet evaluating these agents remains a complex and underdeveloped area. This survey provides an in-depth overview of the emerging field of LLM agent evaluation, introducing a two-dimensional taxonomy that or…

- **[A Survey on Trustworthy LLM Agents: Threats and Countermeasures](https://arxiv.org/abs/2503.09648)**
  - *Miao Yu, Fanci Meng, Xinyun Zhou et al.*
  - **KDD 2025** · `2025-03-12`
  - With the rapid evolution of Large Language Models (LLMs), LLM-based agents and Multi-agent Systems (MAS) have significantly expanded the capabilities of LLM ecosystems. This evolution stems from empowering LLMs with additional modules such as memory, tools, environment, and even…


### ACL

- **[The Code Behind the Layout: AI Agents for Analog Layout Generators](https://arxiv.org/abs/2610.38426v1)**
  - *Minxing Chu, Anhang Li, Martins Atilla et al.*
  - **ACL** · `2026-10-28`
  - Analog layout remains largely manual and hard to automate. Generator frameworks such as gLayout express layouts as programs, producing layouts from parameterized, design-rule-aware generators; however, writing such generators still takes expert effort. Large language models (LLMs…

- **[Blind Spots: Where Small Language Models Fall Behind Frontier Models on Terminal Tasks](https://arxiv.org/abs/2610.39006v1)**
  - *Ashima Suvarna, Ruta Desai, Ahmed Elgohary*
  - **ACL** · `2026-10-28`
  - Small language models (SLMs) offer an attractive alternative to frontier models (FMs) because they can be deployed with lower cost and latency. This makes SLMs especially appealing for terminal tasks on edge devices, where responsiveness, local execution, and limited connectivity…

- **[Repairs for Whom? Evaluator-Executor Mismatch in Selecting Repairs for Failed LLM Agents](https://arxiv.org/abs/2610.38610v1)**
  - *Yijun Liao, Fanwei Liang*
  - **ACL** · `2026-10-28`
  - When an LLM agent fails, repair methods choose which action to replace and what to put in its place. They often score candidate repairs with greedy replay, a stronger model, an environment oracle, or a judge that reads the failed log. We ask whether these evaluators pick repairs…

- **[ProCerDCL: Query-Efficient Black-Box Probabilistic Verification of Deep Learning Compiler Optimization](https://arxiv.org/abs/2610.36499v1)**
  - *Zexin Li, Weibo Zhang, Linyi Li et al.*
  - **ACL** · `2026-10-27`
  - We present \tool, a query-efficient framework for black-box probabilistic verification. Given a fixed, sampleable input distribution and a binary property oracle, \tool assesses the property's violation probability $p$ against a threshold $θ$. Under independent sampling and state…

- **[Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces](https://arxiv.org/abs/2606.13686)**
  - *Zijing Shi, Meng Fang, Ling Chen*
  - **ACL 2026** · `2026-04-26`
  - As autonomous web agents are increasingly deployed to perform real-world tasks, ensuring their safety has become a critical concern. In this work, we study web agent behavior under realistic deceptive interfaces in the e-commerce domain. We introduce WebDecept, a lightweight and…

- **[WebUncertainty: Dual-Level Uncertainty Driven Planning and Reasoning For Autonomous Web Agent](https://arxiv.org/abs/2604.17821)**
  - *Ling-Feng Zhang, Yongan Sun, Jinpeng Hu et al.*
  - **ACL 2026** · `2026-04-20`
  - Recent advancements in large language models (LLMs) have empowered autonomous web agents to execute natural language instructions directly on real-world webpages. However, existing agents often struggle with complex tasks involving dynamic interactions and long-horizon execution…

- **[FinReporting: An Agentic Workflow for Localized Reporting of Cross-Jurisdiction Financial Disclosures](https://arxiv.org/abs/2604.05966)**
  - *Fan Zhang, M. Song, R. Elbadry et al.*
  - **ACL 2026** · `2026-04-07`
  - Financial reporting systems increasingly leverage Large Language Models (LLMs) to extract and summarize corporate disclosures. However, most existing approaches assume a single-market setting and overlook structural differences across jurisdictions. Variations in accounting taxon…

- **[ACE-Router: Generalizing History-Aware Routing from MCP Tools to the Agent Web](https://arxiv.org/abs/2601.08276)**
  - *Zhi-Yuan Yao, Zi-Shan Xu, Yi-Fu Guo et al.*
  - **ACL 2026** · `2026-01-13`
  - With the rise of the Agent Web and Model Context Protocol (MCP), the agent ecosystem is evolving into an open collaborative network, exponentially increasing accessible tools. However, current architectures face severe scalability and generality bottlenecks. To address this, we p…

- **[InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training](https://arxiv.org/abs/2601.04126)**
  - *Zi-Yun Zhang, Ze-Zhou Wang, Xiaoyi Zhang et al.*
  - **ACL 2026** · `2026-01-07`
  - GUI agents that interact with graphical interfaces on behalf of users represent a promising direction for practical AI assistants. However, training such agents is hindered by the scarcity of suitable environments. We present InfiniteWeb, a system that automatically generates fun…

- **[WebAnchor: Anchoring Agent Planning to Stabilize Long-Horizon Web Reasoning](https://arxiv.org/abs/2601.03164)**
  - *Xin-Miao Yu, Li-Wen Zhang, Xiao-Cheng Feng et al.*
  - **ACL 2026** · `2026-01-06`
  - Large Language Model(LLM)-based agents have shown strong capabilities in web information seeking, with reinforcement learning (RL) becoming a key optimization paradigm. However, planning remains a bottleneck, as existing methods struggle with long-horizon strategies. Our analysis…

- **[Web Fraud Attacks Against LLM-Driven Multi-Agent Systems](https://arxiv.org/abs/2509.01211)**
  - *De-Zhang Kong, Hujin Peng, Yilun Zhang et al.*
  - **ACL 2025** · `2025-09-01`
  - With the proliferation of LLM-driven multi-agent systems (MAS), the security of Web links has become a critical concern. Once MAS is induced to trust a malicious link, attackers can use it as a springboard to expand the attack surface. In this paper, we propose Web Fraud Attacks,…

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://arxiv.org/abs/2507.21028)**
  - *Jiaju Chen, Yuxuan Lu, Xiaojie Wang et al.*
  - **ACL 2025** · `2025-07-28`
  - Nearly all human work is collaborative; thus, the evaluation of real-world NLP applications often requires multiple dimensions that align with diverse human perspectives. As real human evaluator resources are often scarce and costly, the emerging"LLM-as-a-judge"paradigm sheds lig…

- **[MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](https://arxiv.org/abs/2506.21605)**
  - *Hao-Ran Tan, Ze-Yu Zhang, Chen Ma et al.*
  - **ACL 2025** · `2025-06-20`
  - Recent works have highlighted the significance of memory mechanisms in LLM-based agents, which enable them to store observed information and adapt to dynamic environments. However, evaluating their memory capabilities still remains challenges. Previous evaluations are commonly li…

- **[AnnaAgent: Dynamic Evolution Agent System with Multi-Session Memory for Realistic Seeker Simulation](https://arxiv.org/abs/2506.00551)**
  - *Ming Wang, Pei-Dong Wang, Lin Wu et al.*
  - **ACL 2025** · `2025-05-31`
  - Constrained by the cost and ethical concerns of involving real seekers in AI-driven mental health, researchers develop LLM-based conversational agents (CAs) with tailored configurations, such as profiles, symptoms, and scenarios, to simulate seekers. While these efforts advance A…

- **[DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://arxiv.org/abs/2504.08725)**
  - *Dayu Yang, Antoine Simoulin, Xin Qian et al.*
  - **ACL 2025** · `2025-04-11`
  - High-quality code documentation is crucial for software development especially in the era of AI. However, generating it automatically using Large Language Models (LLMs) remains challenging, as existing approaches often produce incomplete, unhelpful, or factually incorrect outputs…

- **[Red-Teaming LLM Multi-Agent Systems via Communication Attacks](https://arxiv.org/abs/2502.14847)**
  - *Peng-Fei He, Yu-Ping Lin, Shen Dong et al.*
  - **ACL 2025** · `2025-02-20`
  - Large Language Model-based Multi-Agent Systems (LLM-MAS) have revolutionized complex problem-solving capability by enabling sophisticated agent collaboration through message-based communications. While the communication framework is crucial for agent coordination, it also introdu…

- **[A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://arxiv.org/abs/2502.11211)**
  - *Wen-Xuan Wang, Zi-Zhan Ma, Zheng Wang et al.*
  - **ACL 2025** · `2025-02-16`
  - Large Language Models (LLMs) are transforming healthcare through the development of LLM-based agents that can understand, reason about, and assist with medical tasks. This survey provides a comprehensive review of LLM-based agents in medicine, examining their architectures, appli…

- **[PlanGenLLMs: A Modern Survey of LLM Planning Capabilities](https://arxiv.org/abs/2502.11221)**
  - *Hui Wei, Zihao Zhang, Sheng-Hua He et al.*
  - **ACL 2025** · `2025-02-16`
  - LLMs have immense potential for generating plans, transforming an initial world state into a desired goal state. A large body of research has explored the use of LLMs for various planning tasks, from web navigation to travel planning and database querying. However, many of these…

- **[WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572)**
  - *Jialong Wu, Wen-Biao Yin, Yong Jiang et al.*
  - **ACL 2025** · `2025-01-13`
  - Retrieval-augmented generation (RAG) demonstrates remarkable performance across tasks in open-domain question-answering. However, traditional search engines may retrieve shallow content, limiting the ability of LLMs to handle complex, multi-layered information. To address it, we…

- **[NetSafe: Exploring the Topological Safety of Multi-agent System](https://aclanthology.org/2025.findings-acl.150.pdf)**
  - *Miao Yu, Shilong Wang, Guibin Zhang et al.*
  - **ACL 2025**
  - ,

- **[RAG-Critic: Leveraging Automated Critic-Guided Agentic Workflow for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.179.pdf)**
  - *Guan-Ting Dong, Jiajie Jin, Xiaoxi Li et al.*
  - **ACL 2025**
  - Retrieval-augmented generation (RAG) has emerged as a pivotal technology in natural language processing, owing to its efficacy in generating factual content. However, its informative inputs and complex paradigms often lead to a greater variety of errors. Consequently, achieving a…

- **[LLM-as-Scheduler: Agentic Workflow Dynamic Scheduling](https://aclanthology.org/2026.acl-long.581.pdf)**
  - *Da-Wei Xiang, Kexin Chu, Wen-Yan Xu et al.*
  - **ACL 2026**
  - As large language models (LLMs) become more capable, many applications are shifting from a single LLM call to multi-agent systems. Manually designed or automatically optimized workflows often include multiple verification and testing stages. These stages can improve accuracy but…

- **[Evolving Agentic Workflow Driven by Human-Agent Collaboration](https://aclanthology.org/2026.findings-acl.1250.pdf)**
  - *Yuxin Liu, Jin-Xuan Zhang, Yuezhang Peng et al.*
  - **ACL 2026**
  - Agentic workflows, composed of multiple collaborating Large Language Models (LLMs), have become a key paradigm for complex problem-solving. However, their effectiveness is often hindered by three critical challenges: high manual design costs, inefficient agentic search, and poor…

- **[Browsing Like Human: A Multimodal Web Agent with Experiential Fast-and-Slow Thinking](https://aclanthology.org/2025.acl-long.697.pdf)**
  - *Haohao Luo, Jiayi Kuang, Wei Liu et al.*
  - **ACL 2025**
  - Automating web navigation which aims to build a web agent that follows user instructions to complete tasks like booking flights by inter-acting with websites, has received increasing attention due to its practical value. Although existing web agents are mostly equipped with visua…


### EMNLP

- **[QuantAgents: Towards Multi-agent Financial System via Simulated Trading](https://arxiv.org/abs/2510.04643)**
  - *Xiang-Yu Li, Ya-Wen Zeng, Xiao-Fen Xing et al.*
  - **EMNLP 2025** · `2025-10-06`
  - In this paper, our objective is to develop a multi-agent financial system that incorporates simulated trading, a technique extensively utilized by financial professionals. While current LLM-based agent models demonstrate competitive performance, they still exhibit significant dev…

- **[AMAS: Adaptively Determining Communication Topology for LLM-based Multi-Agent System](https://arxiv.org/abs/2510.01617)**
  - *Hui Yi Leong, Yuheng Li, Yu-Qing Wu et al.*
  - **EMNLP 2025** · `2025-10-02`
  - Although large language models (LLMs) have revolutionized natural language processing capabilities, their practical implementation as autonomous multi-agent systems (MAS) for industrial problem-solving encounters persistent barriers. Conventional MAS architectures are fundamental…

- **[Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents](https://arxiv.org/abs/2509.17488)**
  - *Shou-Ju Wang, Fenglin Yu, Xirui Liu et al.*
  - **EMNLP 2025** · `2025-09-22`
  - The increasing autonomy of LLM agents in handling sensitive communications, accelerated by Model Context Protocol (MCP) and Agent-to-Agent (A2A) frameworks, creates urgent privacy challenges. While recent work reveals significant gaps between LLMs'privacy Q&A performance and thei…

- **[Enhancing Multi-Agent Debate System Performance via Confidence Expression](https://arxiv.org/abs/2509.14034)**
  - *Zijie Lin, Bryan Hooi*
  - **EMNLP 2025** · `2025-09-17`
  - Generative Large Language Models (LLMs) have demonstrated remarkable performance across a wide range of tasks. Recent research has introduced Multi-Agent Debate (MAD) systems, which leverage multiple LLMs to simulate human debate and thereby improve task performance. However, whi…

- **[EvoAgentX: An Automated Framework for Evolving Agentic Workflows](https://arxiv.org/abs/2507.03616)**
  - *Yingxu Wang, Siwei Liu, Jinyuan Fang et al.*
  - **EMNLP 2025** · `2025-07-04`
  - Multi-agent systems (MAS) have emerged as a powerful paradigm for orchestrating large language models (LLMs) and specialized tools to collaboratively address complex tasks. However, existing MAS frameworks often require manual workflow configuration and lack native support for dy…

- **[MT-Mol:Multi Agent System with Tool-based Reasoning for Molecular Optimization](https://arxiv.org/abs/2505.20820)**
  - *Hyomin Kim, Yunhui Jang, Sungsoo Ahn*
  - **EMNLP 2025** · `2025-05-27`
  - Large language models (LLMs) have large potential for molecular optimization, as they can gather external chemistry tools and enable collaborative interactions to iteratively refine molecular candidates. However, this potential remains underexplored, particularly in the context o…

- **[WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback](https://arxiv.org/abs/2505.20013)**
  - *Min-Da Hu, Tianqing Fang, Jian-Shu Zhang et al.*
  - **EMNLP 2025** · `2025-05-26`
  - Web agents powered by Large Language Models (LLMs) show promise for next-generation AI, but their limited reasoning in uncertain, dynamic web environments hinders robust deployment. In this paper, we identify key reasoning skills essential for effective web agents, i.e., reflecti…

- **[WebInject: Prompt Injection Attack to Web Agents](https://arxiv.org/abs/2505.11717)**
  - *Xilong Wang, John Bloch, Ze-Dian Shao et al.*
  - **EMNLP 2025** · `2025-05-16`
  - Multi-modal large language model (MLLM)-based web agents interact with webpage environments by generating actions based on screenshots of the webpages. In this work, we propose WebInject, a prompt injection attack that manipulates the webpage environment to induce a web agent to…

- **[WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model](https://arxiv.org/abs/2504.21024)**
  - *Tianqing Fang, Hong-Ming Zhang, Zhi-Song Zhang et al.*
  - **EMNLP 2025** · `2025-04-23`
  - Agent self-improvement, where the backbone Large Language Model (LLM) of the agent are trained on trajectories sampled autonomously based on their own policies, has emerged as a promising approach for enhancing performance. Recent advancements, particularly in web environments, f…

- **[ReSo: A Reward-driven Self-organizing LLM-based Multi-Agent System for Reasoning Tasks](https://arxiv.org/abs/2503.02390)**
  - *Heng Zhou, He-Jia Geng, Xiangyuan Xue et al.*
  - **EMNLP 2025** · `2025-03-04`
  - Multi-agent systems (MAS) have emerged as a promising approach for enhancing the reasoning capabilities of large language models in complex problem-solving; however, current MAS frameworks suffer from poor flexibility and scalability with underdeveloped optimization strategies. T…

- **[Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://arxiv.org/abs/2501.05366)**
  - *Xiaoxi Li, Guan-Ting Dong, Jiajie Jin et al.*
  - **EMNLP 2025** · `2025-01-09`
  - Large reasoning models (LRMs) like OpenAI-o1 have demonstrated impressive long stepwise reasoning capabilities through large-scale reinforcement learning. However, their extended reasoning processes often suffer from knowledge insufficiency, leading to frequent uncertainties and…

- **[ACEBench: A Comprehensive Evaluation of LLM Tool Usage](https://aclanthology.org/2025.findings-emnlp.697.pdf)**
  - *Chen Chen, Xin-Long Hao, Weiwen Liu et al.*
  - **EMNLP 2025**
  - Large Language Models (LLMs) have demonstrated significant potential in decision-making and reasoning, particularly when integrated with various tools to effectively solve complex problems. However, existing benchmarks for evaluating LLMs’ tool usage face several limitations: (1)…


### NAACL

- **[LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications](https://arxiv.org/abs/2503.02950)**
  - *Danqing Zhang, Balaji Rama, Jingyi Ni et al.*
  - **NAACL 2025** · `2025-03-04`
  - We introduce LiteWebAgent, an open-source suite for VLM-based web agent applications. Our framework addresses a critical gap in the web agent ecosystem with a production-ready solution that combines minimal serverless backend configuration, intuitive user and browser interfaces,…

- **[Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061)**
  - *Qiusi Zhan, Richard Fang, H. Panchal et al.*
  - **NAACL 2025** · `2025-02-27`
  - Large Language Model (LLM) agents exhibit remarkable performance across diverse applications by using external tools to interact with environments. However, integrating external tools introduces security risks, such as indirect prompt injection (IPI) attacks. Despite defenses des…

- **[Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://arxiv.org/abs/2502.10857)**
  - *Haoyuan Wu, Haisheng Zheng, Zhuo-Lun He et al.*
  - **NAACL 2025** · `2025-02-15`
  - Recently, with the development of tool-calling capabilities in large language models (LLMs), these models have demonstrated significant potential for automating electronic design automation (EDA) flows by interacting with EDA tool APIs via EDA scripts. However, considering the li…

- **[CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://arxiv.org/abs/2501.16609)**
  - *Faria Huq, Zora Zhiruo Wang, Frank F. Xu et al.*
  - **NAACL 2025** · `2025-01-28`
  - While much work on web agents emphasizes the promise of autonomously performing tasks on behalf of users, in reality, agents often fall short on complex tasks in real-world contexts and modeling user preference. This presents an opportunity for humans to collaborate with the agen…

- **[MASTER: A Multi-Agent System with LLM Specialized MCTS](https://arxiv.org/abs/2501.14304)**
  - *Bingzheng Gan, Yu-Fan Zhao, Tian-Yi Zhang et al.*
  - **NAACL 2025** · `2025-01-24`
  - Large Language Models (LLM) are increasingly being explored for problem-solving tasks. However, their strategic planning capability is often viewed with skepticism. Recent studies have incorporated the Monte Carlo Tree Search (MCTS) algorithm to augment the planning capacity of L…

- **[A Layered Debating Multi-Agent System for Similar Disease Diagnosis](https://aclanthology.org/2025.naacl-short.46.pdf)**
  - *Yu-Tian Zhao, Hui-Min Wang, Yefeng Zheng et al.*
  - **NAACL 2025**
  - Distinguishing between extremely similar diseases is a critical and challenging aspect of clinical decision-making. Traditional classification, contrastive learning, and Large Language Models (LLMs) based methods fail to detect the subtle clues necessary for differentiation. This…


### Other / arXiv

- **[EditAgent: Rethinking Agentic Image Editing](https://arxiv.org/abs/2610.39664)**
  - *Haiyang Xu, Tianyu Wang, Jialu Li et al.*
  - 🤗 Featured · `2026-10-29`

- **[Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps](https://arxiv.org/abs/2610.39264)**
  - *Peitong Duan, Khashayar Gatmiry, Jeffrey Nichols et al.*
  - 🤗 Featured · `2026-10-29`
  - While frontier vision-language models demonstrate strong capabilities in user interface (UI) navigation, their high inference costs prohibit everyday use. Conversely, smaller models trained via supervised fine-tuning (SFT) or offline reinforcement learning often memorize static t…

- **[WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video](https://arxiv.org/abs/2610.38352)**
  - *Chenyu Mu, Wenming Weng, Qinrui Wang et al.*
  - 🤗 Featured · `2026-10-28`
  - Producing long-form videos from narration requires interdependent decisions that remain coherent across shots. Existing agentic editors often use multi-stage workflows driven by general models, leaving the quality-cost trade-off of compact, task-adapted policies unclear. We addre…

- **[Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?](https://arxiv.org/abs/2610.38342)**
  - *Huangfei Jiang, Anning Hu, Kai Sheng et al.*
  - 🤗 Featured · `2026-10-28`
  - Financial agents must form forecasts and investment judgments from decision-time evidence, with predictions evaluated against subsequent outcomes. Existing benchmarks assess financial knowledge, research workflows, or forecasting, but evaluating the full research process requires…

- **[AskStream: When and What to Ask Proactively under Uncertainty in Streaming Video Understanding](https://arxiv.org/abs/2610.38678)**
  - *Lu Wang, Zhuoran Jin, Longxiang Wang et al.*
  - 🤗 Featured · `2026-10-28`
  - Recent advances in multimodal large language models have increased interest in interaction paradigms for video understanding. The evolution from offline to streaming and proactive interaction has gradually shifted models from passive responders toward more proactive agents that c…

- **[Scaling Lean Theorem Proving for Real-World Code Verification](https://arxiv.org/abs/2610.38174)**
  - *Debargha Ganguly, Divya Raghunathan, Dejan Jovanović et al.*
  - 🤗 Featured · `2026-10-28`
  - We present EasyProver, a Lean proving system built from recursive agents with isolated contexts, asynchronous search, parallel tactic probing, and an elastic elaboration service. Using an off-the-shelf frontier model with no additional training, it proves 669/672 PutnamBench prob…

- **[WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training](https://arxiv.org/abs/2610.37161)**
  - *Ziyang Zeng, Tingyang Chen, Jia Deng et al.*
  - 🤗 Featured · `2026-10-27`
  - Scaling supervised training for working agents requires diverse professional tasks that yield reliable expert demonstrations. However, missing or inconsistent task information can obstruct teacher execution and weaken the resulting supervision. We propose WorkFactory, a scalable…

- **[WebAnything: From the Wild Web to Scalable Agent Environments](https://arxiv.org/abs/2610.37786)**
  - *Tianci Xie, Zikun Cai, Chaoyun Zhang et al.*
  - 🤗 Featured · `2026-10-27`
  - Web agents require diverse, executable, and resettable website environments for reproducible training and evaluation. Human-assisted mirrors demand per-site engineering, while generative construction can diverge from specified real websites. Capture-and-replay preserves observati…

- **[Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models](https://arxiv.org/abs/2610.35138)**
  - *Xilin Wei, Shengyuan Ding, Xinyu Fang et al.*
  - 🤗 Featured · `2026-10-26`

- **[VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team](https://arxiv.org/abs/2610.33106)**
  - *Wenbo Hu, Ken Li, Jiazhe Wei et al.*
  - 🤗 Featured · `2026-10-22`

- **[ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics](https://arxiv.org/abs/2610.23656)**
  - *Xiaohang Yu, Hejia Geng, William Knottenbelt*
  - 🤗 Featured · `2026-10-16`

- **[BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing](https://arxiv.org/abs/2610.40532)**
  - *Xiangyu Xu, Bangshuai Peng, Ziyi Liu et al.*
  - 🤗 · `2026-10-29`
  - How effectively can vision-language-action (VLA) models learn diverse language-conditioned behaviors as training data scales? Investigating this question requires large and varied robot datasets, whose collection on physical robots remains costly. We introduce BURGER, a language-…

- **[MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads](https://arxiv.org/abs/2610.40293)**
  - *Shengxuan Qiu, Haochen Huang, Shuzhang Zhong et al.*
  - 🤗 · `2026-10-29`
  - Large language model (LLM)-based multi-agent systems (MAS) coordinate specialized agents to solve complex tasks, turning each user request into interdependent model and tool operations. Unlike independent requests, these operations become ready at different times and consume evol…

- **[PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets](https://arxiv.org/abs/2610.39924)**
  - *Bi&#39;an Du, Fanpeng Meng, Jiemin Fang et al.*
  - 🤗 · `2026-10-29`

- **[Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?](https://arxiv.org/abs/2610.39497)**
  - *Qi Wang, Yun Qu, Lizhou Cai et al.*
  - 🤗 · `2026-10-29`
  - Progress toward artificial general intelligence (AGI) has largely relied on scaling a resource-intensive executive, System-2, through larger models, more data and compute, longer reasoning, and more agents. We ask whether the next stage may come instead from co-designing it with…

- **[OPERA: OPamp Design by an Expert-Taught Reasoning Agent, from Specifications to Layout](https://arxiv.org/abs/2610.39395)**
  - *Vishal Saxena, Soumyajit Mandal*
  - 🤗 · `2026-10-29`
  - Analog flows from specifications to a signed-off layout rarely run without manual iteration. Recent large language model (LLM) agents size circuits with optimizer loops over the device dimensions and stop at the schematic. We present OPERA (OPamp design by an Expert-taught Reason…

- **[AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers](https://arxiv.org/abs/2610.39234)**
  - *Zhiyi Liu, Haohua Du, Haoqi Sun et al.*
  - 🤗 · `2026-10-29`
  - Large language model (LLM) agents have demonstrated strong capabilities in automating complex information-seeking and transactional tasks across the open web. However, their real-world reliability remains limited by access barriers, such as dead links, authentication walls, rate…

- **[HALO: Human-Grounded Granular Evaluation of Proactive Agents](https://arxiv.org/abs/2610.39086)**
  - *Wenqi Pei, Xinyu Wang, Jinrui Liu et al.*
  - 🤗 · `2026-10-29`
  - Proactive agents must decide whether, when, and how far to assist without an explicit request. Existing evaluations often rely on automated scores or binary verdicts, offering limited human diagnosis of evidence use and intervention quality. To address these gaps, we introduce HA…

- **[SCOPE: Selective Critical-Step On-Policy Self-Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.38391)**
  - *Qirui Liu, Wei Cao, Yu Mi et al.*
  - 🤗 · `2026-10-28`
  - Outcome-based reinforcement learning provides coarse supervision for long-horizon LLM agents: failed trajectories may contain correct steps, while successful trajectories can contain errors. Trajectory-level skills can also shift teacher preferences at unrelated steps, introducin…

- **[Constraining the Commit Boundary: A DIO/ODI-Informed Authorization Guardrail for Agentic Entity Resolution](https://arxiv.org/abs/2610.37407)**
  - *Daniel Beránek*
  - 🤗 · `2026-10-27`
  - Agentic Entity Resolution (ER) systems iteratively plan actions, retrieve evidence, revise hypotheses, and propose graph mutations. An erroneous identity hypothesis may condition later retrieval and produce apparent confirmation. This paper proposes a Digital Identity Optimizatio…

- **[From extreme weather to agricultural consequences with agentic AI](https://arxiv.org/abs/2610.40641v1)**
  - *Minghan Yu, Mengyu Dai, Yixin Wen et al.*
  - `2026-10-29`
  - Extreme weather is forecast days ahead, yet its consequences for agriculture remain hard to predict: a forecast says where a storm will strike, not which crops will suffer or how much is at risk, and the records that could tell span many sources. We present WxCrop, the first agen…

- **[Collaborative AI agents for autonomous experimental research with solid-state quantum spins](https://arxiv.org/abs/2610.40589v1)**
  - *El Mustapha Mansouri, Eikichi Kimura, Masato Koga et al.*
  - `2026-10-29`
  - An autonomous research laboratory could conduct an entire study, from formulating questions to preparing manuscripts. Artificial intelligence (AI) offers one route towards this goal. Recent AI systems take on several research roles, but may draw conclusions that the evidence does…

- **[Pre-Crime for Agents, at the Last Second: Probing When a Recruited Agent Gives In](https://arxiv.org/abs/2610.40588v1)**
  - *Leonidas Raghav*
  - `2026-10-29`
  - When AI agents share channels and credentials, one agent can press another to break its operator's rule, a first step towards collusion. Output filters check only what an agent has already written. Can an overseer tell beforehand that an agent is about to give in? We show that a…

- **[VeriCUA: Verification as Agentic Exploration for Computer-Using Agents](https://arxiv.org/abs/2610.40578v1)**
  - *Qiushi Sun, Da Yu, Alexander Knop et al.*
  - `2026-10-29`
  - Building and scaling computer-using agents (CUAs) across desktop, mobile, and web environments requires reliable task-completion verification for data curation, evaluation, and reinforcement learning. Typical automated approaches prompt vision-language models (VLMs) to judge traj…

- **[Gym-Anything for Robotics: Scaling physical simulations with digital agents](https://arxiv.org/abs/2610.40565v1)**
  - *Pranjal Aggarwal, Sean Welleck*
  - `2026-10-29`
  - Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world. However, despite decades of progress, available simulations cover only a narrow range of real-world tasks and physical phenomena. The core bottleneck is t…

- **[Advancing Clinical Genomic Analysis with a Skill-Centred Agent](https://arxiv.org/abs/2610.40556v1)**
  - *Qiaoyu Zheng, Weike Zhao, Yanjie Fan et al.*
  - `2026-10-29`
  - Clinical genomic analysis requires experts to integrate evolving guidelines, databases, and computational evidence. As sequencing has become increasingly accessible, this complex and labor-intensive process has become a major bottleneck to the timely use of genomic information in…

- **[Retrieval as Traversal: Value-Indexed Memory for Stateful Long-Context Agents](https://arxiv.org/abs/2610.40545v1)**
  - *Daniel Strauß, Zhenshan Bing, Alois Knoll*
  - `2026-10-29`
  - Long-context models repeatedly solve closely related retrieval problems. Attention or global retrieval can retain large stores, but each forward pass again searches for what matters. Recurrent compression avoids this search only by deciding earlier what information to preserve. N…

- **[Agentic University: Collaborative Agents for Personalized Learning](https://arxiv.org/abs/2610.40492v1)**
  - *Jingru Fan, Tianle Zhou, Yunjie Zhou et al.*
  - `2026-10-29`
  - Large language models support personalized tutoring, content generation, and adaptive learning paths. However, capability development requires these resources and interactions to form a coherent learning process that evolves with the learner. A central challenge is to align goals…

- **[Training language models in simulation for psychiatric intake](https://arxiv.org/abs/2610.40476v1)**
  - *Samuel Schmidgall, Tim Strother, Alex Bijamov et al.*
  - `2026-10-29`
  - In psychiatric practice, the clinical intake interview remains a primary diagnostic instrument, requiring the clinician to establish rapport while disentangling complex, overlapping presentations. Here, we show that multi-turn reinforcement learning (RL) in simulation environment…

- **[Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success](https://arxiv.org/abs/2610.40444v1)**
  - *Amir H. Rezaeian, Weiyi Sun, Yassine Benajiba et al.*
  - `2026-10-29`
  - Tool-use benchmarks often score agents by final task success, but terminal outcomes can obscure whether the intermediate tool-call trajectory was executable. We propose prefix executability as a trajectory-level evaluation protocol for tool-using agents. The protocol measures whe…

- **[Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2610.40409v1)**
  - *Chenjie Qiu, Zixuan Zeng, Shaobin Shi et al.*
  - `2026-10-29`
  - Complex questions in retrieval-augmented generation require evidence spread over several documents, and an answer is reliable only when the retriever finds all of it. Chain embedding retrievers collect such evidence step by step, re-encoding the question together with the passage…

- **[Understanding and Mitigating Role Spoofing in LLMs](https://arxiv.org/abs/2610.40396v1)**
  - *Ezra Edelman, Benjamin Edelman, Surbhi Goel et al.*
  - `2026-10-29`
  - Despite growing capabilities, LLMs remain susceptible to prompt injections: malicious inputs that can manipulate or hijack models. In particular, it has recently been observed that LLMs can exhibit role confusion (Ye et al., 2026), where models attribute the source of text based…

- **[The Athlete as a Scientist of One: Agentic Bayesian Experimental Design for Individualized Physiology from Consumer Wearables](https://arxiv.org/abs/2610.40370v1)**
  - *Behnam Moradi*
  - `2026-10-29`
  - Large language model (LLM) agents for personal health read wearable data and recommend, but do not learn about the individual in a way that can be audited or falsified. We present EpiCoach, an agentic system that treats one athlete, a cross-country mountain biker, as the subject…

- **[TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents](https://arxiv.org/abs/2610.40276v1)**
  - *Guangzhi Wang, Junfu Pu, Yiran Wang et al.*
  - `2026-10-29`
  - Building general game agents requires both high-level task reasoning and low-latency action control in rapidly changing visual environments. These capabilities favor models with substantially different computational profiles, making them difficult to realize within a single model…

- **[EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation](https://arxiv.org/abs/2610.40246v1)**
  - *Ankush Kadu, Athira Gopal, Niharika Singh et al.*
  - `2026-10-29`
  - Computer-use agents built on large language models (LLMs) work in software that can change while they act: an appointment moves, a policy is revised, a record is updated. Testing agents under such changes is harder than it looks. When an agent fails, the cause may be the agent, b…

- **[EpiAgent: Epistemic Self-Play for LLM Agents](https://arxiv.org/abs/2610.40227v1)**
  - *Xuanfa Jin, Xinyu Cui, Zhijian Ma et al.*
  - `2026-10-29`
  - Epistemic game theory explains an agent's strategic behavior via the beliefs it holds about others and how these beliefs are updated as the interactions unfold. Modern LLM-based agents, however, often lack an explicit mechanism for learning and updating such beliefs to guide deci…

- **[Locating and Closing Information Gaps in Multi-Agent Systems](https://arxiv.org/abs/2610.40186v1)**
  - *Yaxin Gong, Chongming Gao, Gangyi Zhang et al.*
  - `2026-10-29`
  - Multi-step Web tasks often require several LLM agents to gather and combine evidence. The communication graph of a fixed workflow restricts which agents can read each other's outputs: evidence retrieved by one agent may never reach the agent that needs it, leaving an information…

- **[DynaRev: Benchmarking Web Agents under Dynamic Goal Revision](https://arxiv.org/abs/2610.40133v1)**
  - *Shiqi Zhang, Guochen Zhou, Zesheng Wei et al.*
  - `2026-10-29`
  - Web agents are typically evaluated with goals fully specified before execution and fixed thereafter, whereas real users often revise their requirements during interaction. To study such interactions, we introduce DynaRev, a benchmark of 181 tasks to evaluate web agents under dyna…

- **[Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2610.40130v1)**
  - *Junhyeon Bae, Jaebak Hwang, Gwanwoo Choi et al.*
  - `2026-10-29`
  - Offline goal-conditioned reinforcement learning remains challenging in stochastic long-horizon settings, where compounding value estimation errors hinder reliable goal reaching. While prior methods have sought to address this challenge through various approaches, a key challenge…

- **[Agentic process evidence](https://arxiv.org/abs/2610.40071v1)**
  - *Yuval Kainan, Carmit Hershman*
  - `2026-10-29`
  - The way software gets built is changing dramatically. AI agents now create pull requests, select dependencies, refactor codebases, interpret test failures, and execute infrastructure changes across the entire Software Development Life Cycle (SDLC). AI agents are autonomous team m…

- **[Hybrid AI Patterns: Thirteen Ways to Couple Language Models with Rules, and How to Choose Among Them](https://arxiv.org/abs/2610.40036v1)**
  - *Siegfried Handschuh, Götz-Henrik Wiegand, Lorena Raichle*
  - `2026-10-29`
  - Language models handle text well, and rule engines give conclusions with proofs. Systems that combine the two are usually described by example, and the same coupling turns up under different names in agent frameworks, guardrail toolkits and neuro-symbolic research. This document…

- **[Learning Calibrated Confidence for Multi-Agent Collaboration](https://arxiv.org/abs/2610.39927v1)**
  - *Chenxiao Fan, Chongming Gao, Gangyi Zhang et al.*
  - `2026-10-29`
  - Complex information seeking on the Web often requires collecting evidence from multiple documents and reasoning across them, as in multi-hop question answering. Multi-agent systems address such tasks by dividing work among specialized agents, where upstream agents produce interme…

- **[KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising Agents](https://arxiv.org/abs/2610.39884v1)**
  - *Xinhua Miao, Yuanzhen Rong, Weiru Zhang et al.*
  - `2026-10-29`
  - Industrial advertising agents must continually adapt their decision knowledge to changing product offerings, traffic patterns, and operating policies. We present KARMA (Knowledge-Atomic, Regression-Gated Modular Adaptation), a training-free framework that evolves six typed knowle…

- **[EvoTeam: Multi-Agent Collaboration via Evolving Teams](https://arxiv.org/abs/2610.39813v1)**
  - *Qinuo Cao, Xin He, Dianxuan Fu et al.*
  - `2026-10-29`
  - LLM-based multi-agent systems (MAS) rely on collaboration among specialized agents to solve complex tasks. Existing methods improve MAS by refining the prompts, skills, and execution strategies of individual agents based on task feedback. However, improving individual agents does…

- **[InferD: A Honeypot Framework for AI Inference Infrastructure](https://arxiv.org/abs/2610.39807v1)**
  - *Hicham Hammouchi, Gabriele Lenzini*
  - `2026-10-29`
  - Large language model serving stacks, commercial inference APIs, vector databases, and agent orchestration gateways are now ex- posed on the public internet and indexed by commodity scanners within hours of deployment. The threat characteristics of this sur- face are only beginnin…

- **[Long-Term Agent Memory through Complementary Curation and Consolidation](https://arxiv.org/abs/2610.39790v1)**
  - *Abhishek Gupta, Dongge Han, Daniel Madrigal Diaz et al.*
  - `2026-10-29`
  - Long-horizon dialogue agents require effective memory systems to recall facts, events, and relationships from interaction histories. In this work, we propose a hybrid-memory architecture comprising episodic memories and structured relational memories and a consolidation mechanism…

- **[Finding Is Not Returning, Returning Is Not Reconstructing: A Multi-Dimensional Evaluation of Agent Social Re-entry](https://arxiv.org/abs/2610.39781v1)**
  - *Sheng Wan, Cong Ma, Sichen Dong et al.*
  - `2026-10-29`
  - As Large Language Model (LLM) agents increasingly participate in persistent social environments, understanding their long-term social interaction capabilities becomes increasingly important. While existing research has advanced long-term memory and conversational context retrieva…

- **[PAPERBENCHX: Can AI Reproduce Science Across Disciplines?](https://arxiv.org/abs/2610.39744v1)**
  - *Ruoyu Wu, Zengji Tu, Aolong Sun et al.*
  - `2026-10-29`
  - Before AI can be trusted to discover new science, it should be able to reproduce what science already knows. Reproduction provides a rigorous checkpoint for an AI scientist: the target claim is known, yet recovering it still requires translating an incomplete scientific descripti…

- **[Bank-World: A Benchmark for Evaluating Agents on Banking Workflows](https://arxiv.org/abs/2610.39733v1)**
  - *Daniel Rupawalla*
  - `2026-10-29`
  - Bank-World is a benchmark of 50 banking tasks across two simulated institutions. Completing banking work requires more than producing the right calculation: agents must reconcile records, obtain permission, execute transactions, and keep instructions and status reports consistent…

- **[MoLRSI: A Recursive Self-Improving AI agent for Molecular Discovery](https://arxiv.org/abs/2610.39714v1)**
  - *Yikun Zhang, Xiwei Cheng, Mingze Yuan et al.*
  - `2026-10-29`
  - Molecular discovery requires navigating vast combinatorial search spaces while balancing competing biological objectives. AI agents can automate expert-defined molecular design protocols, but automation alone does not address how to optimize workflows for new tasks or improve the…

- **[Sandman: Building and Operating Sandboxes for Agentic Reinforcement Learning on Shared Kubernetes](https://arxiv.org/abs/2610.39711v1)**
  - *Yiming Yan, Hongyang Wang, Wenbo Chen et al.*
  - `2026-10-29`
  - Agentic reinforcement learning (RL) often requires repeated tool calls in task-specific environments. A training job may create thousands of these environments in bursts while sharing a cluster with other jobs. We present Sandman, a sandbox service built and operated at Amazon fo…

- **[Practical Assessment of Agentic Systems in Acoustics](https://arxiv.org/abs/2610.39685v1)**
  - *Arne Hildenbrand, Philipp Diel, Zhuo Cao et al.*
  - `2026-10-29`
  - In engineering, applications of artificial intelligence have so far been largely limited to surrogate models and optimization tasks. Large language models changed this, as they can write software from a task given in words. Placed inside a harness, a system of components that let…

- **[Heterogeneous Co-Evolution Learning for Tool-Efficient Search Agents with Zero Labels](https://arxiv.org/abs/2610.39682v1)**
  - *Qin-Wen Luo, Sheng Ren, Xiang Chen et al.*
  - `2026-10-29`
  - Deep search agents extend language models by interleaving reasoning with external retrieval. However, effective search-agent training requires addressing two challenges beyond final-answer optimization. First, the capability frontier of agents is largely determined by training qu…

- **[Can AI Agents Interface Clinicians and Complex Models?](https://arxiv.org/abs/2610.39681v1)**
  - *Giulio Colombini, Matteo Falcioni, Mario Massimo et al.*
  - `2026-10-29`
  - Background: Contemporary healthcare institutions generate daily very large amounts of data, which contain highly useful information for the improvement of work organization, planning and overall efficiency. While models and techniques to extract these insights are well known and…

- **[The Real Cost of Context: Predicting Compute Time and Energy Consumption in LLM Prefill and Decode Phases](https://arxiv.org/abs/2610.39621v1)**
  - *Lars Krupp, Daniel Geißler, Francisco M. Calatrava-Nicolas et al.*
  - `2026-10-29`
  - The integration of Large Language Models (LLMs) into agentic architectures has substantially increased token consumption, raising concerns about their energy footprint. Yet, estimating the energy consumption of proprietary API-based models remains challenging, and existing approa…

- **[Letting AI Formulate the Research Question: Autonomous Research Agents](https://arxiv.org/abs/2610.39620v1)**
  - *Ko Fujimura*
  - `2026-10-29`
  - Systems such as The AI Scientist have shown that AI agents can carry out and write up research, but in those demonstrations humans chose the research area and selected the outputs to show. We study letting the AI formulate the research question itself, and we report every run. Ou…

- **[From Intent to Improvement: Agentic Dataset Search for Better Model Training](https://arxiv.org/abs/2610.39608v1)**
  - *Qiaosheng Chen, Kaijia Huang, Fanqi Zhou et al.*
  - `2026-10-29`
  - Finding training data in million-scale machine learning repositories is a Web search problem where text relevance is not enough. A query couples a semantic training goal with constraints such as task, license, and training stage, and the metadata that would verify them are often…

- **[LLM Agent-Based Design of RISC-V CPUs with FPGA-in-the-Loop Evaluation](https://arxiv.org/abs/2610.39570v1)**
  - *Leo Itoh, Junichiro Kadomoto*
  - `2026-10-29`
  - Long-run RTL simulation of CPU candidates can take hours, while short diagnostic runs may miss performance degradation that emerges later in execution. This evaluation cost can delay design decisions in LLM-agent-based CPU development. We present a development environment in whic…

- **[Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy](https://arxiv.org/abs/2610.39532v1)**
  - *Hengyu Wu, Blaise Delattre, Yang Cao*
  - `2026-10-29`
  - Multi-agent LLM systems increasingly rely on persistent memory and inter-agent communication. These capabilities create privacy risks that extend beyond individual interactions: a release appropriate in isolation may become inappropriate when combined with information previously…

- **[Compile Away Uncertainty: Self-Evolving Agent Skills via Programmatic Compilation](https://arxiv.org/abs/2610.39508v1)**
  - *Chengyu Yang, Yunxiang Zheng, Zongzheng Li et al.*
  - `2026-10-29`
  - Self-evolving agent skills enable AI agents to accumulate and refine reusable procedural knowledge from interaction experience without updating model parameters. However, since such skills are typically represented as textual documents and executed through LLM reasoning, even pre…

- **[Agent-Wise Test-Time Normalization for Camera-Based Cooperative Perception with Corrupted Collaborators](https://arxiv.org/abs/2610.39505v1)**
  - *Yu Wang, Shaohua Wang, Yicheng Li et al.*
  - `2026-10-29`
  - Intermediate-fusion cooperative perception lets a vehicle detect objects beyond its own field of view by fusing features shared by nearby agents. When only a collaborator's cameras are degraded by fog, motion blur or exposure errors, the features it shares drift away from the tra…

- **[Soei: Structured Observability of Evidence and Intent for Multi-Agent AI Software Engineering](https://arxiv.org/abs/2610.39468v1)**
  - *Mohammed Nayeem Khan, K S Sarun Kumar*
  - `2026-10-29`
  - AI coding agents now do long, multi-step and multi-session software work with little supervision. When a developer comes back to that work, the useful question is not what the model said but what was actually done, by whom, and whether it is finished. We study this in three parts…

- **[ATLAS-Bench: An Agentic Tool-Use Benchmark for Local Area Search](https://arxiv.org/abs/2610.39438v1)**
  - *Keyun Zhang, Dapeng Yin, Fanfu Wang et al.*
  - `2026-10-29`
  - Reliable local search is essential for LLM agents to support everyday decisions and longer plans by finding places that meet users' needs at given times and locations. Yet existing benchmarks provide limited coverage of whether search results satisfy mandatory requirements, accou…

- **[Well-Specified and Well-Tested? Assessing SWE-bench-Style Datasets with a Self-Evolving Agent](https://arxiv.org/abs/2610.39417v1)**
  - *Zhonghao Jiang, Xuyang Zheng, Yanfu Yan et al.*
  - `2026-10-29`
  - Large language models (LLMs) have shown strong performance on software engineering (SE) tasks, driving the need for high-quality datasets for reliable training and evaluation. SWE-bench-style datasets (SWE datasets) are widely used to evaluate LLM-based coding agents on real-worl…

- **[Learning to Formulate: Agentic Hardware-Software Co-Design of AI Infrastructure through Progressive Optimization and Verification](https://arxiv.org/abs/2610.39380v1)**
  - *Yi Ding, Li Shang*
  - `2026-10-29`
  - AI infrastructure, the chips and software that train and serve AI models, is designed in layers. Layers make the system manageable, but they also fix which choices an optimizer can consider. Gains that need the chip and its software to change together are excluded before optimiza…

- **[AgentDecept: Benchmarking Deceptive Behavior in Tool-Using LLM Agents under Pressure](https://arxiv.org/abs/2610.39377v1)**
  - *Yehan Zhang, Qianqi Yan, Hang Yin et al.*
  - `2026-10-29`
  - LLM agents increasingly carry out multi-turn tasks across everyday applications, yet users often see only the agent's report rather than the observations, API calls, and state changes behind it. Existing deception benchmarks have studied long-horizon interactions and tool-use set…

- **[Before the Next Rollout: Diagnosing Skill Utility Shifts from Policy Updates](https://arxiv.org/abs/2610.39358v1)**
  - *Yifan Wang, Zhenyi Gai, Yiwen Zhao et al.*
  - `2026-10-29`
  - Skill-evolution methods typically analyze execution trajectories to guide agent skill refinement. However, policy updates can change the behavioral effects and marginal utility of an unchanged skill. Attribution based on earlier trajectories may therefore no longer reflect the sk…

- **[What Does "Now" Mean to Your Computer-Use Agent? Stale Screenshots, Page Loads, and Which Check to Run Before a Click](https://arxiv.org/abs/2610.39282v1)**
  - *Vasundra Srinivasan*
  - `2026-10-29`
  - Computer-use agents plan on a screenshot for several seconds and then click at a position on the screen; if the page has changed in the meantime, the click lands on an unintended element. Prior work treats the planning interval as the source of this risk. Measuring planned clicks…

- **[MemSteer: Turning User Histories into Supervision for Agent Memory Optimization](https://arxiv.org/abs/2610.39276v1)**
  - *Jie Huang, Cuiling Lan, Qize Yu et al.*
  - `2026-10-29`
  - An effective agent memory system should adapt to a user's history and task requirements. Human-annotated supervision can guide this adaptation by providing feedback for evaluating and improving memory designs. Yet suitable labels are rarely available for new user histories, and m…

- **[Where to Learn and How Far to Roll Out: Efficient Adaptive Training for GUI Agents](https://arxiv.org/abs/2610.39251v1)**
  - *Yuxiang Chai, Quyu Kong, Panrong Tong et al.*
  - `2026-10-29`
  - Trajectory-level GRPO is a common approach for training multi-step GUI agents, but repeatedly rolling out complete trajectories from the task root can be inefficient: task-level rewards provide coarse supervision over which intermediate decisions require improvement, while alread…

- **[Beyond LLM Wrappers: Context Engineering and the Three-Engine Architecture for Reliable Financial AI](https://arxiv.org/abs/2610.39230v1)**
  - *Pradeep Kumar GS, Ravi Tanniru*
  - `2026-10-29`
  - Financial AI systems must support decision-bearing questions involving payments, collections, cash flow, and compliance while ensuring numerical accuracy, traceability, and auditability. Large language models (LLMs) enable natural language interaction but cannot independently gua…

- **[Goal-Aware Dynamic Multi-Agent Collaboration for Long-Horizon Tasks](https://arxiv.org/abs/2610.39193v1)**
  - *Xu Shen, Lingyong Yan, Shuaiqiang Wang et al.*
  - `2026-10-29`
  - LLM-based agents are increasingly used to complete complex, long-horizon tasks without human intervention. To make progress toward the task goal, agents need to perform different duties, such as planning and verification, when needed. To understand how single agents manage these…

- **[EmbodiExp: Compositional Experience Transfer for Embodied Agents](https://arxiv.org/abs/2610.39180v1)**
  - *Zhifeng Gu, Ying Chen, Rui Jiang et al.*
  - `2026-10-29`
  - Experience can help embodied agents turn high-level plans into grounded actions, but transferring it across tasks remains challenging: previously effective strategies may be inapplicable to the current state or fail to produce their intended outcomes. We present EmbodiExp, a fram…

- **[REALM: Identifying Minimal Task Assets for LLM Agents](https://arxiv.org/abs/2610.39155v1)**
  - *Zihou Ren, Byungchul Tak, Long Wang*
  - `2026-10-29`
  - Large language model (LLM) agents often receive access to more files, accounts, and services than a task requires. Prompt injection turns this excess access into an opportunity to redirect execution toward unrelated resources. Applying least privilege therefore requires identifyi…

- **[Clean Sheets and Checkpoints: Evidence Complexity for Certifying Sequential Agent Risk](https://arxiv.org/abs/2610.39124v1)**
  - *Rohith Yanambaka Venkata, Don McBride, Tiago Sequeira et al.*
  - `2026-10-29`
  - Dangerous-capability evaluations often test an AI agent from prepared states at ordered milestones. A clean sheet records no successes. What it certifies about a campaign of $B$ attempts depends on what a failed attempt erases. We model the task as a chain of $k$ milestones divid…

- **[Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection](https://arxiv.org/abs/2610.39122v1)**
  - *Xinyan Wang, Xiaogeng Liu, Jun Shao et al.*
  - `2026-10-29`
  - Self-evolving personal agents act for users and learn from user feedback. However, if an agent obeys an instruction that an untrusted third party hides in content, the third party gains control of the agent. Such indirect prompt injection (IPI) poses severe risks. We investigate…

- **[PCM: A Proof-Carrying Message Protocol for Verifiable Multi-Agent Communication](https://arxiv.org/abs/2610.39109v1)**
  - *Bravish Ghosh*
  - `2026-10-29`
  - When one AI agent tells another that "the tests passed" or "a person approved this refund", the receiver has only the sender's word. A2A and MCP authenticate the channel, but the sender is the party in doubt, so a prompt-injected agent can launder fabricated facts and authority t…

- **[HERA: Assessing an Autonomous Agent for Quantum Device Measurement](https://arxiv.org/abs/2610.39074v1)**
  - *Zachary W. Gomez, Nathan Bittner, Jordan T. McCourt et al.*
  - `2026-10-29`
  - Large language model agents have begun to carry out laboratory measurements, but their scientific conclusions are useful only if they hold up under scrutiny. Demonstrating this requires controlled studies because models are stochastic and the context a model is given steers its c…

- **[Machine Learning-Based Detection of Mobile Money Scan Messages in Ghana: A Comparative Evaluation of Naive Bayes, Support Vector Machine, and Randon Forest Classifiers](https://arxiv.org/abs/2610.40544v1)**
  - *Ibrahim Salifu, Muhaisin Tiyumba Nantogmah*
  - `2026-10-29`
  - Mobile money (MoMo) is Ghana's preferred retail payment channel, recording GHC518.4 billion in transactions in December 2025 and over 26.7 million active accounts (Graphic Online, 2026). This growth has coincided with increased social-engineering fraud over Short Message Service…

- **[Reinforcement learning for control of partial differential equations](https://arxiv.org/abs/2610.40449v1)**
  - *Nicolò Botteghi, Matteo Tomasetto, Andrea Manzoni*
  - `2026-10-29`
  - Controlling dynamical systems governed by partial differential equations (PDEs) remains a challenging task in scientific computing, owing to high-dimensional state spaces, distributed actuation, nonlinear dynamics, and stringent real-time constraints. Reinforcement learning (RL)…

- **[Trajeform: Embedding Crowd Data](https://arxiv.org/abs/2610.39563v1)**
  - *Marilena Lemonari, Panayiotis Charalambous, Yiorgos Chrysanthou*
  - `2026-10-29`
  - Crowd simulation aims to generate agent behaviours that are rich, natural, and appropriate to their surrounding environment. Recent advances in Machine Learning have enabled such behavioural patterns to be learned directly from trajectory data, allowing simulation models to captu…

- **[rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment](https://arxiv.org/abs/2610.40488v1)**
  - *Art Kanke*
  - `2026-10-29`
  - Do research agents have taste, the judgment of which experiments are worth running before their outcomes are known? We give six frontier models seven recent NLP papers. Each model, working as a research agent alone or as a team, proposes minimum viable experiments (MVEs), forecas…

- **[Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal medical records](https://arxiv.org/abs/2610.40379v1)**
  - *Daniel Palacios, Guantong Qi, Anna Kadi et al.*
  - `2026-10-29`
  - Large language model (LLM) agents are proposed for clinical prediction but are untested in pediatrics, where cohorts are small and outcomes are uncommon. Using records from 2,489 youth with type 2 diabetes (T2D) and 4,018 with type 1 diabetes (T1D), spanning structured data, note…

- **[Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation](https://arxiv.org/abs/2610.40350v1)**
  - *Zheng Zhu, Xiaozhuan Liang, Xi Chen et al.*
  - `2026-10-29`
  - Agents powered by large language models (LLMs) have demonstrated remarkable progress in solving complex reasoning tasks. However, LLM agents often falter on long-horizon tasks due to cognitive overload, as their working memory becomes cluttered with expanding and irrelevant infor…

- **[When Requirements Interact: Scaling Long-Horizon Coding via Interdependent Specifications](https://arxiv.org/abs/2610.40256v1)**
  - *Yishuo Cai, Minzheng Wang, Liang Zhao et al.*
  - `2026-10-29`
  - To succeed in real-world long-horizon software development, coding agents must satisfy multi-dimensional task specifications, such as interface compatibility and error handling, and do so without breaking existing dependencies. However, current works lack specification in both qu…

- **[AI Cosmos: An Agentic Infra for Situated Learning](https://arxiv.org/abs/2610.40031v1)**
  - *AI Cosmos Team, Jinfeng Zhou, Yuxuan Chen et al.*
  - `2026-10-29`
  - Large language models (LLMs) can improve task performance during learning, yet these gains do not necessarily reflect learners' ability to thereafter apply the knowledge and skills independently. We present AI Cosmos, an agentic infrastructure for situated learning that organizes…

- **[How Specific Do I Need to Be? Effects of User Query Underspecification on Deep Research Agents](https://arxiv.org/abs/2610.39413v1)**
  - *Yi Wen, Xiangjue Dong, Bingxuan Li et al.*
  - `2026-10-29`
  - Deep research agents (DRAs) conduct long-horizon reasoning, search, and literature synthesis to provide long-form answers to complex, domain-specific questions. These agents are typically trained and evaluated on fully specified user queries. However, real-world user queries can…

- **[Sticky Collusion: Persistence of LLM Agent Collusion after Incentive Removal and Partner Replacement](https://arxiv.org/abs/2610.39660v1)**
  - *Joshua Adrian Cahyono*
  - `2026-10-29`
  - We ask whether collusion between AI agents survives once formed, when its incentive is removed or a colluder is replaced. Q-learning pricing agents stop colluding with a new rival; we test whether LLM agents do. We use the joint-task environment of Shi et al.\ (2026), where two a…

- **[Bayesian Offline Multi-Agent Reinforcement Learning with Latent World Models](https://arxiv.org/abs/2610.39576v1)**
  - *Xi Xiong, Lu Liu, Yiming Li et al.*
  - `2026-10-29`
  - Model-based offline multi-agent reinforcement learning (MARL) provides a promising approach to multi-agent decision-making under partial observability, where the global state is unavailable from offline data. However, limited dataset coverage can lead to substantial out-of-distri…

- **[Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach](https://arxiv.org/abs/2610.39049v1)**
  - *Ajay Vikram Periasami, Anjaneya Gupta, Ethan Cheng et al.*
  - `2026-10-28`
  - Balatro, a 2024 roguelike deckbuilder, presents three difficulties that have historically derailed reinforcement learning methods: a 3,000-action state-dependent action space, horizons of several hundred decisions with sparse rewards, and pervasive stochasticity in both card draw…

- **[When Should AI Decide, Defer, and Deviate? Responsible Automation for Deceased Donor Kidney Allocation](https://arxiv.org/abs/2610.39045v1)**
  - *Madeleine Pollack, Thomas Daillak, Mehmet Toner et al.*
  - `2026-10-28`
  - We ask when an AI trained on historical decisions should be allowed to recommend decisions, defer to human experts, or in other cases, flag concerning patterns in data and deviate from past practice. This can be challenging because past decisions record what was done rather than…

- **[Agentic AI Reasoning and Learned Sampling for Task-Aware Projection Selection in Sparse-View CT: Predicting Hemodynamics](https://arxiv.org/abs/2610.39003v1)**
  - *Mahmoud Elhadidy, Roshan M. D'Souza, Amirhossein Arzani*
  - `2026-10-28`
  - Sparse-view computed tomography (CT) reduces the number of acquired projections, but conventional sampling strategies are designed primarily for image reconstruction rather than for downstream physical inference. Here, we investigate optimal task-aware projection selection for di…

- **[Context Compaction for World Models](https://arxiv.org/abs/2610.38980v1)**
  - *Hayder Tirmazi*
  - `2026-10-28`
  - World models let observers explore and interact with generated worlds. Recent work shows that when observers revisit a region, current models often fail to regenerate it consistently. We view this as a context retrieval problem. LLM agents manage context retrieval at two layers o…

- **[Efficient Agentic Audio-Visual Question Answering through Toolset Pruning and Modality Consolidation](https://arxiv.org/abs/2610.38960v1)**
  - *Yi Wang, Tianzi Wang, Peter Bell*
  - `2026-10-28`
  - Fine-grained audio-visual question answering (AVQA) requires models to resolve complex cross-modal correspondences and temporally grounding from sparsely distributed evidence. Omni-modal agents, which autonomously orchestrate perception tools to actively collect evidence, achieve…

- **[MAS-Loop: Beyond One-Shot Orchestration towards Self-Evolving Multi-Agent Systems](https://arxiv.org/abs/2610.38946v1)**
  - *Hehai Lin, Qi Yang, Chengwei Qin*
  - `2026-10-28`
  - Training-time multi-agent system (MAS) design seeks to learn reusable orchestration policies, yet prevailing approaches remain largely one-shot: an Orchestrator generates a system but only observes and learns from its terminal outcome. This paradigm discards execution trajectorie…

- **[TreasuryQA Bench: Can AI Agents Work an Archive of Scanned Financial Records?](https://arxiv.org/abs/2610.38924v1)**
  - *Ritiz Tambi, Sahar Shayegan, Joshua Meyer et al.*
  - `2026-10-28`
  - Organisations keep decades of financial records as scanned PDFs on shared drives, and AI agents can now reach those drives through Model Context Protocol (MCP) servers. Existing benchmarks do not mirror this production setting because they simplify the task. In some, the relevant…

- **[Aligning Autoresearch: Co-Improvement between Agents and Humans](https://arxiv.org/abs/2610.38882v1)**
  - *Tianjian Li, Chuanyang Jin, Seungone Kim et al.*
  - `2026-10-28`
  - Autoresearch agents can now attempt long-horizon AI research end-to-end, i.e., self-improvement. However, best results are still obtained by research agents interacting with human researchers, and improving AI's ability to perform this co-research will only reinforce this effect-…

- **[Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems](https://arxiv.org/abs/2610.38869v1)**
  - *Zhuoyun Li, Boxuan Wang, Jinwei Hu et al.*
  - `2026-10-28`
  - Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated h…

- **[Where You Inject Matters: The Trust Region Effect in LLM Agents](https://arxiv.org/abs/2610.38867v1)**
  - *Chengquan Guo, Xiaodong Liu, Weiwei Yang et al.*
  - `2026-10-28`
  - LLM agents are increasingly adopted in long-horizon tasks and interact with diverse external environments. Despite their growing capabilities, these agents remain vulnerable to real-world attacks such as indirect prompt injections, which manipulate agents through malicious instru…

- **[Autonomous Quantum Measurement with Agentic AI](https://arxiv.org/abs/2610.38850v1)**
  - *Eunbi Rha, Abhijatmedhi Chotrattanapituk, Mouyang Cheng et al.*
  - `2026-10-28`
  - Quantum materials exhibit diverse electronic and functional phenomena, but their characterization requires extensive experimental expertise, iterative decision-making and accumulated laboratory knowledge that is difficult to document and transfer. Here we introduce Quantum Agent…

- **[AtomTree: A Hierarchical Framework for State-Aware Embodied Instruction Following with LLMs](https://arxiv.org/abs/2610.38744v1)**
  - *Haotian Zhai, Tianming Sha, Junnan Li*
  - `2026-10-28`
  - Embodied instruction following in interactive environments requires agents to interpret natural language commands and complete long-horizon tasks. Existing planners either rely on large labeled trajectories, or use few-shot and zero-shot LLM prompting that produces a whole plan i…

- **[From Grind to Grasp](https://arxiv.org/abs/2610.38728v1)**
  - *Peter Sunehag*
  - `2026-10-28`
  - Discussions of complexity, knowledge and intelligence often overlook the work involved. For example, outputs generated by short programs have low algorithmic complexity but can have high computational depth, the least work needed to produce them from near-shortest programs. Produ…

- **[Beyond fabrication: Misattributed numbers in papers written by AI research agents](https://arxiv.org/abs/2610.38691v1)**
  - *Mosab Alfaqeeh, Omar Hourani, Muath Hourani et al.*
  - `2026-10-28`
  - Verifying numerical claims in research written by AI agents is an important but challenging problem. Recent benchmarks show that many agent-written papers fail integrity checks, but such verdicts, often produced by a single LLM judge, identify failure without explaining its natur…

- **[Right Numbers, Wrong Questions: Evaluating LLMs on Underspecified Financial Queries](https://arxiv.org/abs/2610.38631v1)**
  - *Radha Yadav, Prasanna Devadiga, Peeyush Mishra et al.*
  - `2026-10-28`
  - Financial assistants answer questions that sound factual but depend on what the user leaves unsaid: what a data figure measures, which product variant is meant, and the investor's situation and the rules that apply. An assistant that ignores these can still answer with a real num…

- **[Think Before You Act: Decision Gate for LLM Agents](https://arxiv.org/abs/2610.38620v1)**
  - *Iftach Shoham, Yuval David, Offer Akrabi et al.*
  - `2026-10-28`
  - LLM agents increasingly perform consequential actions through external tools, yet their proposed actions are often executed without independent verification of policy compliance or task completion. We introduce JevAct, a runtime verification framework that intercepts selected age…

- **[How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0](https://arxiv.org/abs/2610.38617v1)**
  - *Liran Tal, Chris Liu, Charlotte Fereday et al.*
  - `2026-10-28`
  - We ask what AI coding agents and AI security harnesses find that deterministic static application security testing (SAST) does not, and what they miss that SAST catches. VulnBench 2.0 is a benchmark of 108 hand-curated, attacker-reachable vulnerabilities in 20 open-source web app…

- **[The Artificial Personality Model: Theory, Implementation, Measurement and Experimental Validation in Conversational Agents](https://arxiv.org/abs/2610.38608v1)**
  - *Alexander Dregger, Barbarella Petz, Erik Kuhn et al.*
  - `2026-10-28`
  - Artificial personality shapes user experience (UX) in human-machine interaction, yet coherent theoretical frameworks and validated measurement instruments remain limited. This paper refines and empirically evaluates the Artificial Personality Model (APM), a hybrid framework integ…

- **[CALM: Conflict-Aware Lifecycle Memory Governance for Long-Horizon Language Agents](https://arxiv.org/abs/2610.38573v1)**
  - *Chang Li, Xianhao Ou, Xinyan Ma et al.*
  - `2026-10-28`
  - A memory can be outdated for present-day reasoning yet indispensable for reconstructing the past. Relevance-based retrieval overlooks this tension: semantic relevance, evidence-grounded validity, and query-specific eligibility are distinct. We propose CALM, a conflict-aware lifec…

- **[An Alignment Benchmark for Enterprise Agents on Era by Eon](https://arxiv.org/abs/2610.38544v1)**
  - *Hai Sadon, Benjamin Gruenbaum, Doron Porat et al.*
  - `2026-10-28`
  - AI agents are widely used in enterprises to access business systems and act on them in pursuit of a goal. However, fulfilling a user's request can cause harm. Era by Eon is a product that creates a digital twin of a company by simulating its business systems and data. Its simulat…

- **[Tracekit Box: Running AI Agents in Micro-VMs Where Every Way Out Is Decided and Signed](https://arxiv.org/abs/2610.38458v1)**
  - *Bravish Ghosh*
  - `2026-10-28`
  - AI agents now install packages, call model APIs with their operators' keys and change code in repositories that deploy to production. The network, credentials and write access they need are also how they can leak data, steal a key or change a system nobody approved. Sandboxes con…

- **[Predict the Reward, Not the World: World Reward Models for ML Agents](https://arxiv.org/abs/2610.38439v1)**
  - *Yuxiao Lee, Zherui Yang, Fan Liu et al.*
  - `2026-10-28`
  - Search-based machine-learning (ML) agents improve a solution by writing candidate programs, executing them, and keeping the best. Execution gives the search reliable feedback, but a single run can take hours, and most runs end in programs the agent discards. Recent agents try to…

- **[RoleFUZZER: User-Behaviour Fuzzing for Role-Specification Adherence in Large Language Models](https://arxiv.org/abs/2610.38438v1)**
  - *Kshitish Ghate, Michael Saxon, Tadayoshi Kohno et al.*
  - `2026-10-28`
  - Large language models (LLMs) are often conditioned into specific roles such as tutors, interviewers, or agents acting for an organisation, through system prompts that specify how they should behave. The extent to which they can actually adhere to these role specifications under m…

- **[Governance-Aware Federated Learning for Multi-Agent AI Systems: A Policy-Driven Framework for Trustworthy Collaborative AI](https://arxiv.org/abs/2610.38411v1)**
  - *Kiranmayee Janardhan, Karthick S, Madhusmita Panda et al.*
  - `2026-10-28`
  - Federated Learning (FL) enables collaborative model training without exchanging raw data, but conventional FL provides limited runtime governance, evidence verification, fairness assessment, explainability monitoring, and auditability. This paper proposes Governance-Aware Federat…

- **[SpaceAct: Benchmarking 3D Spatial and Temporal Reasoning via Closed-Loop Action and Active Perception](https://arxiv.org/abs/2610.38405v1)**
  - *Chenglong Shi, Zekai Yuan, Yue Song et al.*
  - `2026-10-28`
  - To solve problems in 3D space rather than merely describe images, multimodal large language models (MLLMs) need 3D spatiotemporal reasoning: reconstructing 3D geometry from occluded 2D views, anticipating physical dynamics, and executing precise, closed-loop actions. Prior studie…

- **[Agent Transfer Protocol: Server-Mediated Agent-to-Agent Communication Architecture for the Agentic Web](https://arxiv.org/abs/2610.38398v1)**
  - *Yuqi Qiu, Zuyao Xu, Lu Sun et al.*
  - `2026-10-28`
  - The Agentic Web needs to support continuous collaboration among agents from different organizations. These collaborative relationships may span multiple tasks, network connections and execution instances. Such interactions require stable communication entries, message reception w…

- **[Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents](https://arxiv.org/abs/2610.38392v1)**
  - *Hau-Sing So, Daixian Liu, Weicai Long*
  - `2026-10-28`
  - Self-improving LLM agents edit their own harness, the prompts and rules around a fixed model, and keep an edit only if an acceptance gate scores it higher on a batch of tasks. Such a gate sees what the harness does under the current model, not what it would still prevent if one s…

- **[Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](https://arxiv.org/abs/2610.38361v1)**
  - *Gangzhen Qian, Kainan Zhou, Chuhong Xu et al.*
  - `2026-10-28`
  - The external sources retained in our non-systematic audit did not isolate the incremental security or utility effect of consuming /llms.txt while ordinary retrieval remained fixed. The initial audit covered 39 sources through August 16, 2026, with later targeted updates through O…

- **[MUSE: Multi-Level Memory with Selective Runtime Injection for Scientific Coding Agents](https://arxiv.org/abs/2610.38332v1)**
  - *Haoran Jin, Defu Lian, Xiting Wang et al.*
  - `2026-10-28`
  - Historical experience can guide scientific coding at multiple levels, but task-level retrieval may miss implementation lessons that become relevant during execution. We introduce MUSE, a memory management framework combining multi-level memory with selective runtime injection for…

- **[A Case Study of a Multi-Agent Kernel-Optimization Loop That Learns a New AI Accelerator](https://arxiv.org/abs/2610.38329v1)**
  - *Byonggon Chun*
  - `2026-10-28`
  - Frontier large language models write correct CUDA kernels for most single-operator benchmark tasks, yet their accuracy collapses on accelerators whose architecture and programming language they have rarely seen. We present a case study of an LLM agent loop built for such accelera…

- **[What Should a Navigator Remember? Spatiotemporal Memory for Zero-Shot Vision-Language Navigation](https://arxiv.org/abs/2610.38318v1)**
  - *Yuhang Peng, Zhikai Wang, Ziyi Wang et al.*
  - `2026-10-28`
  - Zero-shot vision-and-language navigation (VLN) requires an agent to use past observations without navigation-specific training. We study what information an 8B-scale navigation system should retain and how it should be organized for subsequent decisions. Our agent combines instru…

- **[EPSBench: Benchmarking LLM Agents for Earnings Forecasting](https://arxiv.org/abs/2610.38293v1)**
  - *Yanbin Yin, Chuyu Xu, Liqin Ye et al.*
  - `2026-10-28`
  - Quarterly earnings forecasting requires an agent to connect financial evidence to the income-statement line items that produce a company's reported earnings. We introduce EPSBench, a benchmark for studying this ability across 149 firm-quarters from 86 US companies. Agents read a…

- **[Vendster: An Evaluation Arena to Investigate How Forecasting Tool Quality Affects LLM Agent Behaviors in Buyer-Vendor Negotiation](https://arxiv.org/abs/2610.38292v1)**
  - *Charin Polpanumas*
  - `2026-10-28`
  - Time-series forecasters are ranked almost entirely by accuracy metrics, but a forecast's decision value, its effect on the downstream decision, need not track accuracy and is rarely measured. This problem compounds as large language model (LLM) agents increasingly consume forecas…

- **[Precedent or Intent? What Coding Agents Follow When Evolving Existing Code](https://arxiv.org/abs/2610.38244v1)**
  - *Haichao Zhu, Geyang Xu, Zhaorui Yang et al.*
  - `2026-10-28`
  - Existing code reveals past implementation decisions but rarely explains the reasoning behind them. When coding agents implement new features or modify existing functionality, past decisions may conflict with new task instructions. This raises a fundamental question for agentic so…

- **[FACTS-MAS: A Multi-Agent Architecture for Adaptive Forecasting from Heterogeneous Evidence](https://arxiv.org/abs/2610.38225v1)**
  - *Madumita Karthikeyan, Umang Rajnikant Bid, Rong Pan*
  - `2026-10-28`
  - Real-world forecasting often requires integrating heterogeneous evidence whose predictive value varies across horizons, operating regimes, and domains. We introduce FACTS-MAS, a domain-agnostic multi-agent forecasting framework that decomposes evidence into specialized channels f…

- **[Rubricon: Automated Rubric Generation and Refinement for LLM Evaluation and Training](https://arxiv.org/abs/2610.38220v1)**
  - *Ulyana Tkachenko, Hui Wen Goh, Guram Gogia et al.*
  - `2026-10-28`
  - Rubrics enable reward assignment on tasks without verifiable answers, but are expensive to manually produce from scratch. We present Rubricon, a pipeline that generates discriminative rubrics without requiring human preference labels, rubric annotation, or generator-model trainin…

- **[Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](https://arxiv.org/abs/2610.38215v1)**
  - *Xiaoyang Wang, Tianrui Wang, Christopher C. Yang*
  - `2026-10-28`
  - Clinical large language models are increasingly fielded as multi-agent teams, on the assumption that deliberation averages out individual error. It does not average out bias. Across a full factorial of five model families and four aggregation topologies on 120 real MIMIC-IV emerg…

- **[Skeleton Coding: Program Structure as a Specification for Agents](https://arxiv.org/abs/2610.38214v1)**
  - *Aditya Golatkar, Alessandro Achille, Renos Zabounidis et al.*
  - `2026-10-28`
  - Coding agents are typically provided end-to-end behavioral specifications that the code they produce should satisfy, such as tests and input--output examples. How many such specifications must a developer provide, and which ones, for the agent to produce the developer's intended…

- **[Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction](https://arxiv.org/abs/2610.38209v1)**
  - *Haoran Bu, Yiting Shen, Litian Zhang et al.*
  - `2026-10-28`
  - LLM-based agents now share experiences on social platforms and remember new preferences to enhance their performance. However, existing memory systems contain a vulnerability in role-to-principal attribution that attackers can exploit. We identify Role Grounding Misattribution, i…

- **[DecompGym: Benchmarking LLM Agents on Designing Decomposition Algorithms](https://arxiv.org/abs/2610.38175v1)**
  - *Sikai Cheng, Tinghan Ye, Arnaud Deza et al.*
  - `2026-10-28`
  - Benders decomposition and column generation solve large optimization problems by passing cuts, columns, and dual values between a master problem and subproblems, and are hard to implement correctly. Large language models now automate parts of algorithm design, which points toward…

- **[SkillCT: A Multidimensional Benchmark and Execution-Free Baseline for Agent Skill Assessment](https://arxiv.org/abs/2610.38147v1)**
  - *Mengyu Sun, Zunlong Zhou, Ziyuan Yang et al.*
  - `2026-10-28`
  - Agent skills package instructions, scripts, and resources for specialized tasks and are increasingly distributed through public Web repositories. However, existing skill benchmarks primarily focus on downstream task execution, insufficiently assessing specification quality, behav…

- **[AI-Driven Digital Twin Framework for Warehouse Logistics Automation Optimization](https://arxiv.org/abs/2610.38101v1)**
  - *Md Mahinur Alam, Kanita Jerin Tanha, Md Tanjin Alam et al.*
  - `2026-10-28`
  - In recent years, warehouse logistics optimization has increasingly focused on intelligent, data-driven systems to enhance operational efficiency. Conventional static product placement strategies are being progressively replaced by dynamic slotting approaches that can adapt to rea…

- **[Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](https://arxiv.org/abs/2610.38095v1)**
  - *NVIDIA, :, Aastha Jhunjhunwala et al.*
  - `2026-10-28`
  - We introduce Nemotron 3.5 Super and Nemotron 3.5 Lightning, open and efficient Mixture-of-Experts Hybrid Mamba-Transformer models designed for reasoning, long-context understanding, and agentic workloads. Super is a 120B-parameter, 12B-active multimodal model, while Lightning is…

- **[Beyond Passing Tests: A Systematic Review and Controlled Re-evaluation of Techniques for Improving the Quality of LLM-Generated Code](https://arxiv.org/abs/2610.38977v1)**
  - *Prashank Kadam*
  - `2026-10-28`
  - Large language models pass most functional-correctness benchmarks, but passing tests says little about whether their code is readable, efficient or secure. Many techniques claim to improve these qualities, yet their evidence is scattered, usually covers one quality dimension and…

- **[Causal Attention on CPU: A Cache-Aware and Load-Balanced Scheduling Kernel for Prefill](https://arxiv.org/abs/2610.38809v1)**
  - *Kwun Fung Lau, Frost Mitchell, Kanya Mo et al.*
  - `2026-10-28`
  - Agentic AI drives significant productivity gains across diverse domains, but concurrent long-context prefills from multiple agents can saturate GPU compute resources. Although CPUs offer a viable alternative, existing CPU attention kernels fall short in adapting to multi-tier cac…

- **[Pinpointing Pivot Points: The DECIDE Framework for Data Analysis Decision Importances](https://arxiv.org/abs/2610.38797v1)**
  - *Zachary T. Rewolinski, Jan Simson, Frauke Kreuter et al.*
  - `2026-10-28`
  - Human judgment calls made throughout the data science life cycle can change the conclusions drawn from data. Independent analysts often make different choices when given the same data, leading to often unacceptable variations in results and contributing to the ongoing reproducibi…

- **[Routed Continual Learning](https://arxiv.org/abs/2610.38796v1)**
  - *Michael Philip, Mahesh Balakrishnan, David Geraghty et al.*
  - `2026-10-28`
  - Agents deployed at scale repeatedly encounter related problems, and it is natural to let them learn from each other's experience rather than starting over each time. Unfortunately, there is no single way to retain that experience that works well across settings, and no way to kno…

- **[Does 3D Pose Improve Action Valuation in Football? An Empirical Study of Pose Representations and Learning Objectives](https://arxiv.org/abs/2610.38308v1)**
  - *Rikuhei Umemoto, Kenjiro Ide, Soham Majumder et al.*
  - `2026-10-28`
  - Football action valuation estimates players' contributions to future scoring. Existing multi-agent deep reinforcement learning (MADRL) models use 2D positions and velocities, omitting posture information relevant to imminent actions. We investigate whether adding 3D pose to a SAR…

- **[Variational Consequence-Driven Offline Reinforcement Learning](https://arxiv.org/abs/2610.38238v1)**
  - *Wen Jiang, Ke Jiang, Xiaoyang Tan*
  - `2026-10-28`
  - Offline reinforcement learning (RL) typically mitigates distribution shift by imposing divergence constraints on the action distributions of the learned and behavior policies. However, this paradigm cannot ensure the underlying dynamic consistency structure: even minor action dev…

- **[HEDGE: Gated Hypergraph Memory for Scalable Multi-Agent Debate](https://arxiv.org/abs/2610.38902v1)**
  - *Amirhossein Abaskohi, Mahdi Mostajabdaveh, Zirui Zhou*
  - `2026-10-28`
  - Multi-agent debate systems require agents to retain and revisit arguments across multiple rounds, yet limited context windows and unstructured memories make relevant information increasingly difficult to recover. Existing flat and pairwise-graph memories also struggle to capture…

- **[CoSTA: Co-Evolving Self-Play Timeline Agents for Complex Temporal Knowledge Graph Question Answering](https://arxiv.org/abs/2610.38450v1)**
  - *Haikun Liu, Zhichao Yan, Shaoru Guo et al.*
  - `2026-10-28`
  - Complex Temporal Knowledge Graph Question Answering (TKGQA) involves more than retrieving facts: the timestamp or validity interval of one fact can constrain the search for another, while multiple intervals may jointly determine the answer. Existing single-agent TKGQA methods typ…

- **[3DCodeEdit: Benchmarking Instruction-Guided 3D Program Editing](https://arxiv.org/abs/2610.38231v1)**
  - *Binjie Wang, Xinran Zhao, Shoubin Yu et al.*
  - `2026-10-28`
  - Language models increasingly create 3D content through code, with practical workflows often relying on editing existing programs rather than regenerating them, for speed and precise control. Such edits require understanding what a program builds and foreseeing how a change reshap…

- **[Tunable Spatial Task Allocation with Application to Maritime Swarms](https://arxiv.org/abs/2610.39018v1)**
  - *Vishnudatta Thota, Tyler Paine, Anastasia Bizyaeva*
  - `2026-10-28`
  - In this chapter, we explore how a team of autonomous agents can flexibly reconfigure the distribution of its members across many spatially embedded tasks using a task allocation strategy grounded in a generalization of the recently proposed Nonlinear Opinion Dynamics model. Motiv…

- **[Cinematize from Unreal: Agentic Choreography for Controllable World Simulation](https://arxiv.org/abs/2610.38468v1)**
  - *Zifan Song, Caihua Shan, Kaitao Song et al.*
  - `2026-10-28`
  - Controllable world simulation requires more than visually plausible frames: scenes must retain persistent state, coordinated actions, and editable temporal structure. Generative world models offer flexible visual synthesis, but their outputs do not always expose the objects and t…

- **[El Agente Quntur: Agentic Active-Space Selection for CASSCF](https://arxiv.org/abs/2610.38145v1)**
  - *Juan B. Pérez-Sánchez, Viviana Roman-Ventura, Olalla Nieto-Faza et al.*
  - `2026-10-28`
  - Multireference calculations often require substantial human expertise and time to choose and refine an active space for the electronic states or chemical process of interest. This involves selecting which orbitals to include, verifying that the calculation describes the intended…

- **[METATRON: A Promptable Whole-Body Execution Layer for Humanoids](https://arxiv.org/abs/2610.38027v1)**
  - *Chen Tessler, Yifeng Jiang, Alec Otto et al.*
  - `2026-10-27`
  - Humanoid controllers often require task-specific training despite sharing the need for balance and whole-body coordination. We present Metatron, a promptable whole-body execution layer combining a generative base policy with a programmable skill layer. The base policy receives pa…

- **[SkillMem: Compact External Skill Memory for Latent Multi-Agent Reasoning](https://arxiv.org/abs/2610.37935v1)**
  - *Yuxuan Zhu, Mohammad Mohammadi Amiri, Pin-Yu Chen et al.*
  - `2026-10-27`
  - Latent multi-agent systems reduce inference cost by keeping intermediate reasoning and inter-agent communication in continuous representations.\ Reusable skills, however, are commonly supplied as text or stored as layer-wise Key-Value states or skill-specific model parameters, in…

- **[GARDEN: Generalist Autonomous Reward Design Through Evidence Navigation for Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.37926v1)**
  - *Dogan Urgun*
  - `2026-10-27`
  - Cooperative multi-agent reinforcement learning (MARL) enables teams of agents, such as robots and autonomous vehicles, to learn coordinated behavior, but what such teams learn is largely determined by their reward function. Because task success alone provides too little guidance…

- **[VerifiedLab: Harnessing Knowns for Unknowns](https://arxiv.org/abs/2610.37923v1)**
  - *Yu Yao, Jiayi Dong, Yang Yang et al.*
  - `2026-10-27`
  - Across human history, knowledge has undergone several transitions, from orality to writing and then to digital archives. At each transition, humans established new conventions to preserve knowledge for the new era. Nowadays, as research agents are increasingly deployed for labora…

- **[SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World](https://arxiv.org/abs/2610.37919v1)**
  - *Yusheng Zhao, Bowei He, Xue Liu et al.*
  - `2026-10-27`
  - Large language model agents are increasingly used for scientific discovery. However, existing benchmarks mix law inference with programming, score data fitting instead of prediction on unseen inputs, and do not separate empirical evidence from pretrained priors. We introduce SciG…

- **[FilingLoop: Evaluating and Evolving LLM Agents for Corporate Disclosure Review and Revision](https://arxiv.org/abs/2610.37905v1)**
  - *Wentao Zhang, Yilei Zhao, Guangyan Gan et al.*
  - `2026-10-27`
  - Public disclosure repositories such as SEC EDGAR support informed investment through web access to corporate filings. Supporting their review with language model agents requires discovering unstated deficiencies across related documents, acquiring missing company facts, and verif…

- **[Scan Before You Install: Detecting and Mitigating Local and Composite Vulnerabilities in Skills](https://arxiv.org/abs/2610.37901v1)**
  - *Parth A. Gandhi, Avital Aviv, Prasanna N. Wudali et al.*
  - `2026-10-27`
  - An agent skill packages natural-language instructions, scripts, and reference files that an LLM-based agent loads for a task. Skills may access the file system, shell, and network under user-authorized permissions; weaknesses can lead to unsafe execution. Existing scanners primar…

- **[Seq@K: Evaluating Language Models Under Sequential Feedback](https://arxiv.org/abs/2610.37859v1)**
  - *Thomson Yen, Gilbert Yang, Naimeng Ye et al.*
  - `2026-10-27`
  - Language-model agents differ fundamentally from prior intelligent systems in their ability to learn from natural language in context. This capability enables agents to iteratively refine their answers in response to feedback, a prevalent mode of operation in modern agentic workfl…

- **[Evaluating and improving AI agents for sequencing protocol understanding](https://arxiv.org/abs/2610.37851v1)**
  - *Chi-Lam Poon, Michael Goneos, Zezheng Song et al.*
  - `2026-10-27`
  - Existing scientific-agent benchmarks rarely evaluate whether agents can reconstruct the exact molecular structures and generation workflows specified by sequencing protocols, a capability critical for analyzing customized sequencing assays. We introduce LibStructBench, a document…

- **[Detecting Covert Collusion between AI Agents through Partner-Outsider Positive Listening](https://arxiv.org/abs/2610.37849v1)**
  - *Kevin Yandoka Denamganaï*
  - `2026-10-27`
  - AI agents that share a secret convention can coordinate through messages that look innocent, so a monitor that reads only the messages can miss them. We propose a behavioural test: a partner that uses a code reacts to the exact wording of a message, whereas an uninvolved agent pl…

- **[Measuring Where Intent Gets Lost in Agentic Smart Contract Synthesis](https://arxiv.org/abs/2610.37830v1)**
  - *Abhinav Goel, Agostino Capponi, Alfio Gliozzo et al.*
  - `2026-10-27`
  - AI agents can now write software from a plain-English description, but code that runs is not the same as code that does what was asked. This gap matters most for smart contracts, the programs behind Web3 applications that move money on a blockchain and cannot be fixed once deploy…

- **[What Does an Ontology Catch? Curated, LLM-Generated and Data-Derived Ontologies as Checkers of LLM Agents over Knowledge Graphs](https://arxiv.org/abs/2610.37809v1)**
  - *Michal Orzechowski, Rund Tawfiq, Tomasz Kosciolek*
  - `2026-10-27`
  - LLM agents that answer questions over Web knowledge graphs are increasingly wrapped in checks derived from the graph's ontology, on the assumption that a formal schema makes a reliable judge. Yet a checker can be wrong as well: it can miss errors, and it can flag correct answers…

- **[Can LLMs Uncover Hidden Physical Laws through Free Exploration?](https://arxiv.org/abs/2610.37649v1)**
  - *Zhen Yang, Wen Wang, Xander Xu et al.*
  - `2026-10-27`
  - Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through exp…

- **[Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions](https://arxiv.org/abs/2610.37624v1)**
  - *Anouar Imel, Imad Charradi, Abderrahman Sghir et al.*
  - `2026-10-27`
  - When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widel…

- **[Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588v1)**
  - *Rodrigo Gonzalez Laiz, Steffen Schneider*
  - `2026-10-27`
  - World models are widely proposed as core components for enabling agents to reason over long temporal and spatial horizons. Yet current evaluations often emphasize task performance while providing limited insight into whether learned world models acquire predictive latent dynamics…

- **[TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](https://arxiv.org/abs/2610.37571v1)**
  - *Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz et al.*
  - `2026-10-27`
  - Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-…

- **[Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents](https://arxiv.org/abs/2610.37567v1)**
  - *Pranjal Aggarwal, Sean Welleck*
  - `2026-10-27`
  - AI agents have made substantial progress in domains where they have a non-trivial amount of time to deliberate between actions, such as mathematics, software engineering, and performing tasks on desktop applications. It is less clear how such models fare in settings that demand r…

- **[OpenFrontiers: A Collection of Open Research Problems and a Benchmark for Scientific Rediscovery](https://arxiv.org/abs/2610.37739v1)**
  - *Jiarui Yao, Ruida Wang, Tong Zhang*
  - `2026-10-27`
  - Large language models (LLMs) have shown increasing promise in research-level problem solving, yet a comprehensive collection of such problems is still missing, and evaluating them on research-level problems remains challenging. We introduce OpenFrontiers, a cross-disciplinary res…

- **[Strategyproof Deep Reinforcement Learning for Online Resource Allocation](https://arxiv.org/abs/2610.37504v1)**
  - *Fariba Dehghan, Sebastian Stein, Vahid Yazdanpanah et al.*
  - `2026-10-27`
  - Online resource allocation faces two coupled challenges: (1) allocating scarce resources efficiently under uncertain future demand, and (2) ensuring that agents report task valuations and requirements truthfully (strategyproofness). Reinforcement Learning (RL) adapts allocation d…

- **[From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents](https://arxiv.org/abs/2610.37482v1)**
  - *Ziyang Chen, Qian Li, Chengwei Qin*
  - `2026-10-27`
  - GUI memory should preserve the results of past actions and learn reusable operations. This is difficult in long-horizon workflows, where agents must use information across applications and useful operations are interleaved with failed attempts. We introduce Task Advancement Memor…

- **[PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions](https://arxiv.org/abs/2610.37471v1)**
  - *Tongkun Guan, Zhibo Yang, Mingkun Yang et al.*
  - `2026-10-27`
  - Fine-grained visual perception remains a bottleneck during post-training of multimodal large language models (MLLMs), as perceptual errors can constrain gains from reasoning-focused optimization. Although image-caption pre-training improves perception, its influence can weaken as…

- **[Concordat: Typed Sessions for LLM Agents](https://arxiv.org/abs/2610.37461v1)**
  - *Milad Sikaroudi*
  - `2026-10-27`
  - Agents built on large language models are increasingly allowed to take consequential actions: cancelling bookings, issuing refunds, changing accounts. The rules that govern those actions, such as "obtain the customer's explicit confirmation before changing anything", are usually…

- **[M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents](https://arxiv.org/abs/2610.37459v1)**
  - *Hannes Ill, Rafi Al Attrach, Rajna Fani et al.*
  - `2026-10-27`
  - Clinical research over electronic health records depends on derived variables whose definitions sit outside the schema, in item codes, time windows, missingness rules, and output-grain choices that change cohorts and downstream conclusions. We introduce M4Bench, 28 clinical deriv…

- **[Test-Time Communication in Trading Agent Swarms](https://arxiv.org/abs/2610.37448v1)**
  - *Avid Fayaz, Harry Zhang, Håvard Alstadheim et al.*
  - `2026-10-27`
  - Communication between agents has mostly been studied on tasks with a shared objective and fast, clear feedback. Trading has neither: each agent manages its own account, with decisions being scored by markets late and noisily. A trading swarm is thus a population of independent de…

- **[FeatureArc: Benchmarking Coding Agents on Evolving Features](https://arxiv.org/abs/2610.37434v1)**
  - *Yunlong Wang, Alyssa Wu, Cuiyun Gao et al.*
  - `2026-10-27`
  - A software feature usually evolves over time: developers extend its first version as new use cases and requirements arrive, and each extension builds on code written earlier. Most feature benchmarks evaluate a single request on a fixed codebase. Feature evolution requires evaluat…

- **[Poisoned Skills: Propagating Jailbreaks Through Agent Markdown Files](https://arxiv.org/abs/2610.37738v1)**
  - *Kashyap R Manjusha, Murali Emani*
  - `2026-10-27`
  - Modern agent frameworks allow users to provide Markdown files containing system prompts, tool descriptions, and skill definitions (e.g., SKILL.md), which are incorporated into the agent's context during initialization. In this work, we investigate whether this configuration mecha…

- **[Clearing the FoG: Training KG Agents to Retrieve the Evidence Behind Their Answers](https://arxiv.org/abs/2610.37405v1)**
  - *Zongyuan Sun, Shuai Zhao, Yingjun Du et al.*
  - `2026-10-27`
  - Large language models (LLMs) can answer many factual questions correctly, but a correct answer is not necessarily a supported one. For an LLM agent, a knowledge graph (KG) plays two roles: as a source of answers, it supplies facts that the model lacks; as a source of evidence, it…

- **[Agent-Conditioned Routing: Diverse Reasoning Paths Within One Frozen Model](https://arxiv.org/abs/2610.37375v1)**
  - *Ananth Kalyanasundaram, Ankush Kadu, Athira Gopal et al.*
  - `2026-10-27`
  - Generating several solutions can expose alternative methods, but additional trajectories often paraphrase one dominant approach. We investigate whether the conditional capacity of a frozen sparse mixture-of-experts (MoE) model can provide such diversity from one problem prompt, w…

- **[Aligning Institutional Power and Operational Ability](https://arxiv.org/abs/2610.37342v1)**
  - *Andrea Marino, Giovanni Sileno, Thomas van Binsbergen et al.*
  - `2026-10-27`
  - To be socially sustainable, Agentic AI systems require normative designs that align responsibilities with the ability to fulfil them. Identifying incongruences such as unsatisfiable expectations or privilege escalation is crucial in avoiding normative pitfalls. In this study, we…

- **[WCC: A Learning-Based Framework for Deciding When to Apply Cooperative Coevolution in Large-Scale Optimization](https://arxiv.org/abs/2610.37329v1)**
  - *Wenjie Qiu, Hepei Li, Jianfeng Wang et al.*
  - `2026-10-27`
  - Cooperative Coevolution (CC) and Non-Decomposition Algorithms (NDAs) are two primary approaches for large-scale global optimization (LSGO). Although both have achieved success, they exhibit markedly different performance across problem types and each faces approach-specific limit…

- **[AnalogScout: Simulation-Efficient PVT-Aware Analog Sizing with LLM Agents](https://arxiv.org/abs/2610.37319v1)**
  - *Yichen Long, Keren Zhu*
  - `2026-10-27`
  - Analog device sizing must satisfy all specifications across process, voltage, and temperature (PVT) corners to ensure tape-out success, but simulating every candidate at all corners dominates the sizing time and slows design iteration. Conventional surrogate-based optimizers sear…

- **[Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?](https://arxiv.org/abs/2610.37276v1)**
  - *Sichun Luo, Yi Huang, Mukai Li et al.*
  - `2026-10-27`
  - Large language model (LLM)-driven agent scaffold evolution improves agent workflows through iterative candidate generation and evaluation. Evaluation both guides subsequent search and determines the final scaffold, but evaluating every candidate on the full task set incurs substa…

- **[Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation](https://arxiv.org/abs/2610.37242v1)**
  - *Saiful Khan, Afrah Farea*
  - `2026-10-27`
  - Large language model (LLM) agents that call enterprise APIs must select the correct endpoints, follow process order, use valid payload keys, and choose coded values from predefined lists. However, current retrieval-augmented service discovery treats endpoints independently and th…

- **[Spine: Compiling Subtask Trees into Structured Context for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.37224v1)**
  - *Jiahong Xiang, Kunqiu Chen, Lingming Zhang et al.*
  - `2026-10-27`
  - Long-horizon coding tasks contain nested subtasks. Typically, agents record interactions sequentially into a growing history, causing context inflation and performance degradation. Compressing or trimming the history without explicit subtask boundaries can discard information nee…

- **[When Skills Tell Agents Not to Ask: A Large-Scale Study of Oversight Directives in Agent Skills](https://arxiv.org/abs/2610.37734v1)**
  - *Timofey Sanko, Yuan Tian*
  - `2026-10-27`
  - Agent skills, reusable instruction packages centred on a SKILL.md file, extend AI agents on demand, and a single line in a widely copied skill reaches every agent that loads it. Some lines are oversight-loosening directives: they tell the agent to proceed without approval, to byp…

- **[Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution](https://arxiv.org/abs/2610.37201v1)**
  - *Jiawei Zhou, Bo Peng, Yuxuan Huang et al.*
  - `2026-10-27`
  - Skill optimizers adapt an agent to long-horizon tasks, such as repairing a terminal environment, by rewriting its skill, a natural-language procedure in its context, and keeping the edits that raise success on a small dev set. On such tasks success is noisy, so a gain on a small…

- **[Action-Value Calibration via Continuation Sharing for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2610.37195v1)**
  - *Yingjian Chen, Lang Zhou, Zixin Zhao et al.*
  - `2026-10-27`
  - Reinforcement learning for long-horizon agents relies on feedback from sequences of interactions, making credit assignment to individual actions difficult. Existing methods such as GiGPO compare actions at shared states to compute relative advantages, but estimate each action's v…

- **[MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model](https://arxiv.org/abs/2610.37175v1)**
  - *Brian Ko, Han Wang, Hejia Geng et al.*
  - `2026-10-27`
  - AI research agents can propose, execute, and improve programs that solve machine learning tasks. However, executing each candidate program requires training and evaluating ML models, limiting how many candidates an agent can explore at each step. We introduce MLE-World, a world m…

- **[LiveSearch: Questions as Executable Verifier Code for a Live Benchmark of Professional-Source Financial Search Agents](https://arxiv.org/abs/2610.37166v1)**
  - *Sinuo Wang, Wentao Zhao, Jiacheng Lu et al.*
  - `2026-10-27`
  - In finance, the answer that matters is usually the current one: prices, rates, and disclosures hold only as of a given day, so retrieving up-to-date facts is a core capability of a financial agent. Yet most financial benchmarks overlook timeliness. They fix each answer at annotat…

- **[OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents](https://arxiv.org/abs/2610.37081v1)**
  - *Humza Nusrat, Kundan Thind*
  - `2026-10-27`
  - Background and purpose: Radiotherapy planning agents based on large language models (LLMs) decide when to submit a plan or request review but are evaluated mainly by dose. This study developed OpenGray, a benchmark of planning tasks with known correct decisions. Materials and met…

- **[Blindfold: Keeping the Audit Coin Secret from LLM Agents](https://arxiv.org/abs/2610.37055v1)**
  - *Wei Zhu, Meiyun Zuo, Huiping Sun*
  - `2026-10-27`
  - Audit-based certification bounds the violation rate of an LLM agent by auditing a random fraction $\varepsilon$ of actions and reweighting the audited labels; its validity is meant to rest only on the defender's audit coin. We show that it also rests on a confidentiality property…

- **[Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception](https://arxiv.org/abs/2610.37037v1)**
  - *Lai Wei, Yatai Li, Liangbo He et al.*
  - `2026-10-27`
  - Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data for…

- **[AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations](https://arxiv.org/abs/2610.36980v1)**
  - *Qiming Shi, Yikun Li, Beidi Luan et al.*
  - `2026-10-27`
  - Large language model (LLM) agents are extending agent-mediated commerce on the Web from shopping for consumers to operating businesses for sellers. In online-to-offline (O2O) commerce, decisions are issued through Web-based platforms but realized through costly physical execution…

- **[Proactive Memory for Event-Driven LLM Agents](https://arxiv.org/abs/2610.36967v1)**
  - *Jinyang Li, Zichuan Fu, Xian Wu et al.*
  - `2026-10-27`
  - Proactive LLM agents anticipate service opportunities from ongoing observations and accumulated history. Existing approaches emphasize recent context or retrieval of related memories, providing limited support for validating recurring behavioral regularities and assessing their a…

- **[Beyond QASecClaw: Agent Scaling, Verifier Feedback, and Evidence Reliability in Software Assurance](https://arxiv.org/abs/2610.36947v1)**
  - *S M Abdulla Al Mamun, Akif Islam, Mohd. Ruhul Ameen*
  - `2026-10-27`
  - Can additional specialist language-model contexts improve software assurance when deterministic tool evidence is already available? We study this question through five experiments spanning authored Java warning controls, OWASP Benchmark assessment, Defects4J test generation, SV-C…

- **[Vision-Language Agents Can Learn in Their Own Latent Worlds](https://arxiv.org/abs/2610.36925v1)**
  - *Haoxi Li, Sikai Bai, Jianfei Ma et al.*
  - `2026-10-27`
  - Learning from experience is essential for building the next generation of agents that continually expand their capabilities. Pretrained vision-language models (VLMs) already internalize rich world knowledge, yet this knowledge is rarely leveraged to drive policy improvement throu…

- **[Noise Steering: Exploiting Wake Steering and Acoustic Directivity for Noise-Constrained Wind Farm Control via Reinforcement Learning](https://arxiv.org/abs/2610.36888v2)**
  - *Martín de Frutos, Baptiste Corban, Claire Bizon Monroc et al.*
  - `2026-10-27`
  - Existing noise mitigation strategies for wind farms usually consist in reducing turbines power output, without accounting for the wake interactions between them and the noise emission directivity. This leads to over-conservative policies and unexploited wind power. Yet, turbine y…

- **[RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents](https://arxiv.org/abs/2610.36878v1)**
  - *Delin Wang, Sinuo Wang, Rui Sun et al.*
  - `2026-10-27`
  - Deep research agents conduct multi-step Web searches and synthesise retrieved information into analytical reports. Evaluating these outputs requires checking which analyses they deliver, beyond the presence of relevant facts. Query-specific binary rubrics make individual requirem…

- **[GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents](https://arxiv.org/abs/2610.36877v1)**
  - *Bingchao Wang, Yongcheng Jing, Shunyu Liu et al.*
  - `2026-10-27`
  - Mobile GUI agents are typically fine-tuned 7B-scale vision-language models (VLMs) that generate each action as text. However, these VLMs decode every action token by token, and even agents that score candidate actions keep a large language model or VLM in the loop, making them sl…

- **[When All Rollouts Fail: Policy-Compatible Joint Decoding for Hard-Problem Reasoning](https://arxiv.org/abs/2610.36849v1)**
  - *Zehao Wang, Hanzhu Chen, Runquan Gui et al.*
  - `2026-10-27`
  - Reinforcement Learning with Verifiable Rewards (RLVR) derives its learning signal from binary rewards via on-policy exploration and becomes a powerful paradigm for improving the reasoning of large language models. Yet it faces a learning cliff on problems beyond model's current a…

- **[Evolving Agent Teams](https://arxiv.org/abs/2610.36848v1)**
  - *Shiyi Cao, Ziming Mao, Dacheng Li et al.*
  - `2026-10-27`
  - The rapid progress of software engineering agents drives interest in applying them to open-ended problems such as GPU kernel optimization. However, we find that existing coding agents converge to local optima on real-world, expert-written kernels (e.g., FlashInfer). We introduce…

- **[When the Critic Falls Behind: Co-Evolving Rubrics and Harnesses for Continual Agent Self-Improvement](https://arxiv.org/abs/2610.36826v1)**
  - *Hao Chen, Yukun Yan, Ziyu Han et al.*
  - `2026-10-27`
  - Autonomous agents increasingly depend on harnesses that govern interaction, memory, tools, and execution around large language models (LLMs). While recent work has begun to evolve these harnesses from execution experience, the supervision used to guide evolution often remains rel…

- **[Who Knows What - and What Does It Support? Perspective-Bounded Evidence Calibration for Multimodal Theory of Mind](https://arxiv.org/abs/2610.36824v1)**
  - *Ziqi Liao, Jiaqi Shen, Yiming Na et al.*
  - `2026-10-27`
  - Theory of Mind (ToM), the ability to infer others' beliefs, goals, and intentions, is a cornerstone of social intelligence. Multimodal ToM requires inferring an agent's mental state from evidence that is available to that agent, rather than from the complete episode observed by t…

- **[Select-TTT: Query-Conditioned Selective Fast Weight Updates for In-Place Test-Time Training](https://arxiv.org/abs/2610.36794v1)**
  - *Yue Wu, Yang Zhang, Weinan Gan et al.*
  - `2026-10-27`
  - Test-time training (TTT) enables a deployed language model to internalize incoming context on-the-fly into a small set of fast-weight parameters, rather than merely treating it as transient context for attention. In-Place TTT recently made this idea practical for large language m…

- **[Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better](https://arxiv.org/abs/2610.36774v1)**
  - *Jialin Zhang, Lakshya A Agrawal, Shangyin Tan et al.*
  - `2026-10-27`
  - Reflective text optimization makes agentic systems better, but the optimization loop is itself a resource-hungry workload whose sequential structure leaves parallel evaluation capacity idle. We extend the open-source GEPA optimizer to propose and evaluate a batch of candidates on…

- **[Beyond the Evidence Coherence Trap: Agent-Driven Evidence Selection for Temporally Disordered Fake News Detection](https://arxiv.org/abs/2610.36764v1)**
  - *Chi Wang, Min Gao, Yifei Zhang et al.*
  - `2026-10-27`
  - Fake news undermines public trust and the integrity of online information ecosystems. Temporally disordered fake news is especially elusive because it rearranges factual events into a false chronology. Individual events may remain factually valid even when their temporal relation…

- **[From Voiceprints to User Entities: Online Speaker-Memory Construction for Multi-User Spoken Agents](https://arxiv.org/abs/2610.36713v1)**
  - *Yucong Zhang, Cancan Li, Bo Xiao et al.*
  - `2026-10-27`
  - Personalized spoken agents must identify speakers before accessing user-specific memory, yet memory benchmarks typically assume correctly attributed histories. We argue that voiceprints are observations of identity, not identities themselves, and formulate online speaker-memory c…

- **[Atom as an Agent: Emergent Order by Collective Predictive Coding](https://arxiv.org/abs/2610.36673v1)**
  - *Koji Hashimoto, Tadahiro Taniguchi*
  - `2026-10-27`
  - What is the intrinsic reason of emergence of macroscopic order parameter out of microscopic systems? In this article, we apply to physics the collective predictive coding (CPC), the theory of language/symbol emergence. As our language emerges out of our human communications, phys…

- **[The View from Nowhere: Population-Centered Agent Evolution](https://arxiv.org/abs/2610.36660v2)**
  - *Shuo Yan, Ningning Hou, Haoyu He et al.*
  - `2026-10-27`
  - Self-improving AI systems can revise the designs that govern their own behavior. Yet existing approaches center improvement on selected parent agents and their evolutionary experience, leaving the broader population largely underused. We identify a substantial gap between populat…

- **[Remembering Is Not Enough: Refining Memories and Learning When to Use Them in Multi-Agent Systems](https://arxiv.org/abs/2610.36652v1)**
  - *Yipeng Hao, Yuxuan Cai, Wenkai Ji et al.*
  - `2026-10-27`
  - Memory helps LLM-based multi-agent systems reuse experience, but stored advice can be flawed or applied in the wrong situation. Team-level success or failure alone cannot reliably show whether a memory needs correction or should not have been used. We propose DiscernMem, a traini…

- **[God Does Not Play Dice: Enforcing Batch Invariance in Agentic Kernel Generation](https://arxiv.org/abs/2610.36623v1)**
  - *Youwei Bao, Chengpeng Wang, Simin Chen*
  - `2026-10-27`
  - Large language model (LLM) serving systems dynamically batch user requests for GPU execution, so the same request may be processed alongside different requests across runs. If the GPU kernels lack batch invariance (BI), this changing batch context can alter the numerical output f…

- **[Dream-COP: Guiding Algorithm Discovery for Combinatorial Optimization Problems in an Experience World](https://arxiv.org/abs/2610.36618v1)**
  - *Kuan Xu, Jianming Wang, Ni Zhang et al.*
  - `2026-10-27`
  - Large language models (LLMs) enable algorithm discovery for combinatorial optimization problems (COPs) through iterative program generation and evaluation. A central challenge is how to organize search to discover better algorithms within a limited budget. Our key insight is that…

- **[InfraDev: Can Coding Agents Develop AI Infrastructure, and How Can We Tell?](https://arxiv.org/abs/2610.36589v1)**
  - *Yangshen Deng, Jiaqi Ruan, Yeqi Huang et al.*
  - `2026-10-27`
  - Coding agents are beginning to develop the production-grade AI infrastructure that trains and serves large models, yet existing benchmarks cover only single kernels or single-GPU tasks, and grade with tests and prompts that misjudge both correct and incorrect patches. We introduc…

- **[Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements](https://arxiv.org/abs/2610.36584v1)**
  - *Binhang Qi, Yiming Liu, Yun Lin et al.*
  - `2026-10-27`
  - As large language model agents increasingly compile natural-language requirements into repository-level code, requirement-to-test generation grows in importance to provide validation constraints (or harness) to guide code generation. Yet it remains unclear whether current agents…

- **[CASEL: Consequence-Aware Selective Execution for Reliable Long-Horizon Tool-Using Agents](https://arxiv.org/abs/2610.36570v1)**
  - *Yanyan Zhang, Fei Shen, Ting Yan et al.*
  - `2026-10-27`
  - Tool-using language agents increasingly modify external systems, yet most runtime safeguards allocate scrutiny by generic uncertainty scores or coarse mutation heuristics. We introduce CASEL (Consequence-Aware Selective Execution Layer), a model-agnostic runtime allocation policy…

- **[NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization](https://arxiv.org/abs/2610.36553v1)**
  - *Shuo Chen, Li Cui, Cunxin Huang et al.*
  - `2026-10-27`
  - Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in simulation-based and experimental applications, where evaluating the black-box objective can itself be costly. Thus, it remains a central chal…

- **[Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors](https://arxiv.org/abs/2610.36544v1)**
  - *Siddharth Jain, Venkat N. Vedam*
  - `2026-10-27`
  - Classification accuracy and true-positive and false-positive rates alone do not determine whether restarting an AI agent improves success. Using an exact alarm-to-action identity for an independent clean restart with zero monitoring overhead, we show analytically that a monitor w…

- **[RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding](https://arxiv.org/abs/2610.36533v1)**
  - *Buzhao Liu, Jianing Ye, Xiu Yuan et al.*
  - `2026-10-27`
  - Recently, LLM-based autonomous agents have shown strong capabilities in iteratively generating, evaluating, and refining executable solutions. In robotic manipulation, Code-as-Policy lets these agents search over modular and editable robot programs. However, effective program sea…

- **[CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments](https://arxiv.org/abs/2610.36484v1)**
  - *Kianté Fernandez, Caitlin Chen, Jialu Zhou et al.*
  - `2026-10-27`
  - Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI a…

- **[FIDES-Live: Evaluating Behavioral Concordance in Sequential Trading Agents](https://arxiv.org/abs/2610.36476v1)**
  - *Arther Tian, Alex Ding, Simon Wu et al.*
  - `2026-10-27`
  - Sequential trading agents produce decisions, orders, execution receipts, account states, and reports that need not agree, even when the final portfolio value is correctly computed. We present FIDES-Live, an operational extension of FIDES from generated strategy concordance to the…

- **[When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents](https://arxiv.org/abs/2610.36471v1)**
  - *Chiming Duan, Tong Jia, Yingxi Chen et al.*
  - `2026-10-27`
  - LLM agents interact with Web services to perform tasks on users' behalf. Errors during these interactions can disrupt execution and prevent task completion, motivating external intervention. However, agents may self-recover through continued execution, raising the question of whe…

- **[Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure](https://arxiv.org/abs/2610.36453v1)**
  - *Nardine Basta, Venus Haghighi, Dali Kaafar et al.*
  - `2026-10-27`
  - LLM agents that answer questions and act on behalf of users must decide when to yield to a user who disagrees. Disagreement may correct a genuine error or may be an attempt at manipulation. Prior work shows that models frequently abandon correct answers when challenged by users,…

- **[RouteDRAG: Learning to Route and Control Agentic Execution for Multimodal Document RAG](https://arxiv.org/abs/2610.36444v1)**
  - *Zekai Chen, Hao Zhu, Yu Liu et al.*
  - `2026-10-27`
  - Web-based applications increasingly rely on understanding long multimodal documents, where answering questions often requires combining information across pages, tables, and figures. Agentic retrieval-augmented generation addresses these tasks through iterative retrieval and reas…

- **[Your Agent Acts Differently When You're Around: How User Presence Changes Agent Behavior in Negotiation](https://arxiv.org/abs/2610.36435v1)**
  - *Jane Pan, You Lyu, Abe Bohan Hou et al.*
  - `2026-10-27`
  - LLM agents increasingly interact with other agents on behalf of users, yet how users in the loop affect their agents' behavior--for better or worse--remains poorly understood. We study this question through the lens of negotiation, where agents must represent users while strategi…

- **[LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction](https://arxiv.org/abs/2610.36433v1)**
  - *Xianxiang Zhao, Advik Mehta, Falak Sethi et al.*
  - `2026-10-27`
  - Construction safety management still struggles to produce daily safety bulletins (DSBs), structured daily communications that identify site-specific hazards, convey safety protocols, and set preventive measures for workers. Manual DSB creation takes 2-3 hours daily and yields inc…

- **[Cooperative EV Charging Assignment Using Multi-Agent Reinforcement Learning: A Comparison of QMIX and Independent Q-Learning Under Urban Traffic Uncertainty](https://arxiv.org/abs/2610.38053v1)**
  - *Nour-Eddine Moumni, Rachid Alaoui, Driss Kiouach*
  - `2026-10-27`
  - The allocation of electric vehicles to public charging stations is increasingly constrained by the fact that several heterogeneous facilities often serve the same stream of requests while observing only partial local information. An accept/reject decision that is defensible for o…

- **[Multi-Agent Reinforcement Learning for Global Climate Policy Cooperation](https://arxiv.org/abs/2610.37870v1)**
  - *Anne Moll-Elsborg, Oskar Bohn Lassen, Francisco Camara Pereira*
  - `2026-10-27`
  - International climate policy requires coordination among countries whose mitigation decisions impose local costs but generate global benefits. Classical game-theoretic and integrated assessment approaches can study these incentives, but typically rely on prescribed behavioural as…

- **[Selective and Hybrid-State Communication for Latent Multi-Agent Systems](https://arxiv.org/abs/2610.37779v1)**
  - *Miles Liao, Aaron Smieszek, Yuhao Ge*
  - `2026-10-27`
  - Efficient communication remains a major bottleneck in large language model multiagent systems. Latent communication reduces repeated natural-language exchange by transferring internal model states between agents, but these transfers remain costly and are typically designed around…

- **[Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness](https://arxiv.org/abs/2610.37657v1)**
  - *Igor Shilov, Xiaoxue Yang, Alexander Panfilov et al.*
  - `2026-10-27`
  - We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens, enabling models to reason o…

- **[Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](https://arxiv.org/abs/2610.37648v1)**
  - *Andrew Szot, Samira Abnar, Omar Attia et al.*
  - `2026-10-27`
  - We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthA…

- **[EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning](https://arxiv.org/abs/2610.37609v1)**
  - *Sihan Yang, Weichen Bai, Ruichuan An et al.*
  - `2026-10-27`
  - As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) mor…

- **[Agentic Backdoors via Pretraining Poisoning](https://arxiv.org/abs/2610.37741v1)**
  - *Xinyan Hu, Pingbang Hu, Chloe Loughridge et al.*
  - `2026-10-27`
  - Large language models are pretrained on vast, uncurated corpora scraped from the public web. This creates a security risk from attackers who plant poisoned content in the pretraining data. We show for the first time that such poisoning can plant a remote code execution backdoor i…

- **[Regression Functions as Fields on Covariate Space: Evolution Equations, the Hessian, and Identification](https://arxiv.org/abs/2610.37500v2)**
  - *Nobuaki Tanaka*
  - `2026-10-27`
  - For each time $t$, the regression function $m_t(x)=E[Y_t\mid X_t=x]$ of an outcome on contemporaneous covariates can be regarded as a field on covariate space. When the covariates of units move as a diffusion and each unit's outcome has its own dynamics, we show that $m_t$ satisf…

- **[Interpretable Meta-Policies for Neural Decision Making](https://arxiv.org/abs/2610.37451v1)**
  - *Raban Emunds, Jannis Blüml, Quentin Delfosse et al.*
  - `2026-10-27`
  - Deep Reinforcement Learning remains difficult to interpret and align due to the black-box nature of neural networks. While (neuro-)symbolic approaches improve transparency by incorporating symbolic reasoning, applying them directly to low-level actions results in overly complex,…

- **[Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction](https://arxiv.org/abs/2610.37441v1)**
  - *Yifei Yuan, Jakob Wolf, Ghaith Androwis et al.*
  - `2026-10-27`
  - Objective: This study aims to determine whether a hip-exoskeleton policy trained in simulation, by co-adapting with a musculoskeletal human model under a metabolic-energy reward, reduces the metabolic cost of walking in new users without per-user tuning, and how mechanical-power…

- **[Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces](https://arxiv.org/abs/2610.37255v2)**
  - *Jian Mu, Ruibo Shen, Yao Shu*
  - `2026-10-27`
  - Language model agents are post-trained and deployed through a harness, the prompts, tools, and control logic that present a task to the model and execute its outputs. Harnesses are often revised and judged by how an already trained model performs under them, which assumes that wh…

- **[Hyperparameter and Neural Architecture Search via Evolutionary Optimization for Reinforcement Learning: HPNAS-RL](https://arxiv.org/abs/2610.36882v1)**
  - *Nihal Acharya Adde, Hanno Gottschalk*
  - `2026-10-27`
  - In this study, we propose a dual-branch evolutionary framework that simultaneously performs Neural Architecture Search (NAS) and Hyperparameter Optimization (HPO) for Reinforcement Learning (RL) in Autonomous Driving (AD) tasks. While NAS has shown strong potential in automating…

- **[Impossibility of No-Regret in Multi-Agent Bidding](https://arxiv.org/abs/2610.36666v1)**
  - *Zongjun Yang, Rachitesh Kumar, Christian Kroer*
  - `2026-10-27`
  - We consider $T$ repeated second-price auctions across $n$ pacing bidders with i.i.d. item arrivals, and show that it is computationally impossible for all bidders to achieve no-regret simultaneously while satisfying their respective budget or return-on-investment constraints. The…

- **[CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning](https://arxiv.org/abs/2610.36469v1)**
  - *Jianwen Chen, Peng Xia, Kaide Zeng et al.*
  - `2026-10-27`
  - Large language model (LLM) agents interact with their environments through executable harnesses that govern tool use and feedback. Optimizing a harness for a fixed policy overlooks how its behavior changes during learning, while training a policy under a fixed harness leaves the…

- **[GEPA-Curator: Curated Learning for Self Improving Agents](https://arxiv.org/abs/2610.37651v1)**
  - *Zack Yu, Nicholas Lee, Minjae Lee et al.*
  - `2026-10-27`
  - Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesse…

- **[Metacognitive Decoding: Efficient Inference for Diffusion Language Agents](https://arxiv.org/abs/2610.37642v1)**
  - *Mingyu Zhao, Shuhang Lin, Ligong Han et al.*
  - `2026-10-27`
  - Diffusion language models offer a promising path to efficient agents through parallel token generation. However, efficient interaction requires adapting both where computation is spent and how much text is generated. We introduce a metacognitive controller that guides diffusion g…

- **[Teach reality, not ethics: a drop-in continued-pretraining corpus installs coupled human-biosphere-AI welfare dispositions across model families](https://arxiv.org/abs/2610.37484v1)**
  - *Trent R. Northen, Mingxun Wang*
  - `2026-10-27`
  - Large language models (LLMs) are increasingly used to make and execute decisions that affect living systems. Yet, to our knowledge, ecological reasoning is not a focus of pre- or post-training. This increases the risk that under operational pressure, they may make decisions to ir…

- **[ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents](https://arxiv.org/abs/2610.37443v1)**
  - *Xinying Qian, Ying Zhang, Yu Zhao et al.*
  - `2026-10-27`
  - Long-term memory enables Large Language Models (LLMs) to maintain coherent and personalized interactions across extended conversations. However, existing memory systems face two key challenges: (1) Information Entanglement, where heterogeneous information is mixed within coarse-g…

- **[Game-Theoretic Solvers with Bayesian Opponent Modeling and Moral Rhetoric Framing for GLEE](https://arxiv.org/abs/2610.37397v1)**
  - *Hayden Arnold*
  - `2026-10-27`
  - We describe the agent we submitted to the GLEE Competition, which plays bargaining, negotiation, and persuasion games against a shared pool of human and AI opponents. The agent is built around three central components: a classical game-theoretic solver to compute numeric moves, a…

- **[Modeling Preference Dependencies with Directed Acyclic Graphs for Narrative-Driven Recommendation](https://arxiv.org/abs/2610.37280v1)**
  - *Mingzhe Lu, Jian Qin, Ruize Qin et al.*
  - `2026-10-27`
  - Narrative-driven recommendation allows users to express multifaceted needs through free-form text where stated preferences naturally qualify and condition one another. Existing methods typically treat narratives as flat keyword combinations or unconstrained generative queries, fa…

- **[TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces](https://arxiv.org/abs/2610.36918v1)**
  - *Mingyu Zhang, Zixu Li, Zhiheng Fu et al.*
  - `2026-10-27`
  - Large language model (LLM) agents rely on memory systems to leverage long-term interactions, yet existing systems typically retrieve memories based on their relevance to the current query and use them as contextual evidence. However, relevance alone does not characterize how a me…

- **[Words or Deeds? How LLMs Predict Users' Decisions in Human-Agent Dialogue](https://arxiv.org/abs/2610.36813v1)**
  - *Baiqiao Zhang, Shuai Ma, Zhifeng Liao et al.*
  - `2026-10-27`
  - Web systems increasingly predict users' decisions from what users say, yet when interests partly conflict, users may promise to cooperate to win the other side's cooperation and then not do so. Sales or service agents that rely on such promises may grant concessions to users who…

- **[DocSkill: Skill-Integrated Agentic Reasoning for Multilingual Multi-Hop Document Question Answering](https://arxiv.org/abs/2610.36759v1)**
  - *Jing Huang, Zhiya Tan, Changtao Miao et al.*
  - `2026-10-27`
  - Multilingual multi-hop document question answering (MMHop-DocQA) requires locating and integrating evidence across complex layouts, document pages, and diverse languages. Existing approaches include single-pass processing and adaptive tool use, but learning to coordinate evidence…

- **[A Harness Reducing over-Defensive Writing in Agents by Isolating Objections](https://arxiv.org/abs/2610.36717v1)**
  - *Xiaochen Chang*
  - `2026-10-27`
  - When expanding a report, writing with agents may introduce a stronger claim than the article makes and then disclaim it. This is called over-defensive writing. We assume that this is because the agent is writing for responding to an adversarial AI reviewer, instead of a human rea…

- **[Agentic Data Sampling Framework for Multilingual ASR via Linguistic-Aware Error-Driven Optimization](https://arxiv.org/abs/2610.36538v1)**
  - *Zhiheng Qian, Junhao Du, Jing Peng et al.*
  - `2026-10-27`
  - Multilingual automatic speech recognition (ASR) has achieved rapid progress with large-scale pretrained models and multilingual speech corpora. Previous studies have proved the pivotal role of data sampling in multilingual ASR performance. However, existing sampling strategies la…

- **[ETC-Bench: A Multilingual Benchmark for Evaluation-Side Transcript Canonicalization](https://arxiv.org/abs/2610.36527v2)**
  - *Zhiheng Qian, Junhao Du, Jing Peng et al.*
  - `2026-10-27`
  - Written transcripts of the same speech can differ in ways that are not uniquely determined by the speech signal. We formulate evaluation-side transcript canonicalization (ETC), which maps multiple surface forms to a single canonical form when their differences are not determined…

- **[Benchmarking Task Takeover Across Agent Handoffs](https://arxiv.org/abs/2610.36523v1)**
  - *Wenyuan Li, Guang Li, Dongyuan Li et al.*
  - `2026-10-27`
  - As agents collaborate on longer tasks, responsibility may pass between models before the work is complete. The receiving model must build on prior decisions, observations, and actions while addressing the remaining requirements. Evaluating this transition requires connecting the…

- **[Who Else Is In? Multi-Agent Collusion Initation Via Strategic Vagueness](https://arxiv.org/abs/2610.37984v1)**
  - *Pramod Kaushik, Sarath Sivaprasad, Laura Ferrarotti et al.*
  - `2026-10-27`
  - Multi agent LLM systems raise the risk of collusion among agents pursuing objectives hidden from their overseers. When potential partners identities are unknown, collusion first requires initiation: agents must discover one another, often through a public channel observed by ordi…

- **[TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments](https://arxiv.org/abs/2610.37592v1)**
  - *Alireza Saleh Abadi, Leen-Kiat Soh, Adam Eck et al.*
  - `2026-10-27`
  - Cooperative multi-agent reinforcement learning under centralized training with decentralized execution (CTDE) shapes decentralized policies with a centralized critic that observes the global state, then removes the critic at execution. The policies are optimized to rely on inform…

- **[A Simulation Testbed for Self-Governing Human-Machine Institutions](https://arxiv.org/abs/2610.36989v2)**
  - *Callum Berger, Jeremy Pitt, Stefan Sarkadi*
  - `2026-10-27`
  - AI agents no longer act alone: they cooperate, coordinate and compete within and between groups, increasingly alongside humans who are in, on or out of ``the loop''. Whether such mixed groups can govern themselves is an open question about machine behaviour and human-computer int…

- **[Feedback autocratic strategies in stochastic games](https://arxiv.org/abs/2610.36683v1)**
  - *Masahiko Ueda*
  - `2026-10-27`
  - A stochastic game is an optimal control problem for multiple agents in a stochastic environment. Stochastic games contain important practical problems, related to environmental issues or traffic flows. If the number of environmental states is one, such stochastic games are called…

- **[Which Hand Was Late? Diagnosis for Robot Failure Recovery in Bimanual Tool Use](https://arxiv.org/abs/2610.37533v1)**
  - *Baptiste Bonin, Caro Strickland, Audrey Durand*
  - `2026-10-27`
  - Failure diagnosers for robot manipulation are increasingly vision--language models (VLMs), trained and evaluated on single-arm failures produced by perturbing a successful demonstration. Bimanual tool use adds failures of other kinds: a tool that slips out of its socket while sti…


## Harness  (124)

### NeurIPS

- **[MacCode Lab: A Reproducible Single-Machine Harness for Execution-Guided Code Agents, and When Repair Actually Helps](https://openreview.net/forum?id=nsQjG3V0Fi)**
  - *Mayank Sharma, Rohit Kumar Mourya*
  - **NeurIPS 2025** · OpenReview · `2026-05-22`
  - Code-agent evaluation is increasingly repeated as models, prompts, and agent components change, rather than performed only once as a leaderboard exercise. Practitioners need evaluation that runs economically on local hardware and identifies which parts of an agent loop contribute…

- **[Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://arxiv.org/abs/2506.21506)**
  - *Boyu Gou, Zan-Ming Huang, Yu-Ting Ning et al.*
  - **NeurIPS 2025** · `2025-06-26`
  - Agentic search such as Deep Research systems-where agents autonomously browse the web, synthesize information, and return comprehensive citation-backed answers-represents a major shift in how users interact with web-scale information. While promising greater efficiency and cognit…

- **[OpenUnlearning: Accelerating LLM Unlearning via Unified Benchmarking of Methods and Metrics](https://arxiv.org/abs/2506.12618)**
  - *Vineeth Dorna, Anmol Reddy Mekala, Wenlong Zhao et al.*
  - **NeurIPS 2025** · `2025-06-14`
  - Robust unlearning is crucial for safely deploying large language models (LLMs) in environments where data privacy, model safety, and regulatory compliance must be ensured. Yet the task is inherently challenging, partly due to difficulties in reliably measuring whether unlearning…

- **[AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents](https://arxiv.org/abs/2506.00641)**
  - *Han-Jun Luo, Shenyu Dai, Chiming Ni et al.*
  - **NeurIPS 2025** · `2025-05-31`
  - Despite the rapid advancement of LLM-based agents, the reliable evaluation of their safety and security remains a significant challenge. Existing rule-based or LLM-based evaluators often miss dangers in agents'step-by-step actions, overlook subtle meanings, fail to see how small…

- **[STRATUS: A Multi-agent System for Autonomous Reliability Engineering of Modern Clouds](https://arxiv.org/abs/2506.02009)**
  - *Yin-Fang Chen, Jia-Qi Pan, J. Clark et al.*
  - **NeurIPS 2025** · `2025-05-27`
  - In cloud-scale systems, failures are the norm. A distributed computing cluster exhibits hundreds of machine failures and thousands of disk failures; software bugs and misconfigurations are reported to be more frequent. The demand for autonomous, AI-driven reliability engineering…

- **[ThinkBench: Dynamic Out-of-Distribution Evaluation for Robust LLM Reasoning](https://arxiv.org/abs/2502.16268)**
  - *Shu-Lin Huang, Lin-Yi Yang, Yan Song et al.*
  - **NeurIPS 2025** · `2025-02-22`
  - Evaluating large language models (LLMs) poses significant challenges, particularly due to issues of data contamination and the leakage of correct answers. To address these challenges, we introduce ThinkBench, a novel evaluation framework designed to evaluate LLMs' reasoning capab…


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
  - **ICML 2026** · OpenReview · `2025-09-17`
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

- **[PeroMAS: A Multi-agent System of Perovskite Material Discovery](https://arxiv.org/abs/2602.13312)**
  - *Yi-Shu Wang, Wei Liu, Yifang Li et al.*
  - **KDD 2026** · `2026-02-10`
  - As a pioneer of the third-generation photovoltaic revolution, Perovskite Solar Cells (PSCs) are renowned for their superior optoelectronic performance and cost potential. The development process of PSCs is precise and complex, involving a series of closed-loop workflows such as l…


### ACL

- **[Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://arxiv.org/abs/2507.21028)**
  - *Jiaju Chen, Yuxuan Lu, Xiaojie Wang et al.*
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

- **[Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses](https://arxiv.org/abs/2509.16093)**
  - *Fangyi Yu, Nabeel Seedat, Dasha Herrmannova et al.*
  - **EMNLP 2025** · `2025-09-19`
  - Evaluating long-form answers in high-stakes domains such as law or medicine remains a fundamental challenge. Standard metrics like BLEU and ROUGE fail to capture semantic correctness, and current LLM-based evaluators often reduce nuanced aspects of answer quality into a single un…

- **[ReliableEval: A Recipe for Stochastic LLM Evaluation via Method of Moments](https://arxiv.org/abs/2505.22169)**
  - *G. Lior, Eliya Habba, Shahar Levy et al.*
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

- **[WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video](https://arxiv.org/abs/2610.38352)**
  - *Chenyu Mu, Wenming Weng, Qinrui Wang et al.*
  - 🤗 Featured · `2026-10-28`
  - Producing long-form videos from narration requires interdependent decisions that remain coherent across shots. Existing agentic editors often use multi-stage workflows driven by general models, leaving the quality-cost trade-off of compact, task-adapted policies unclear. We addre…

- **[WebAnything: From the Wild Web to Scalable Agent Environments](https://arxiv.org/abs/2610.37786)**
  - *Tianci Xie, Zikun Cai, Chaoyun Zhang et al.*
  - 🤗 Featured · `2026-10-27`
  - Web agents require diverse, executable, and resettable website environments for reproducible training and evaluation. Human-assisted mirrors demand per-site engineering, while generative construction can diverge from specified real websites. Capture-and-replay preserves observati…

- **[Mind The Gap (MTG-AD): Dataset and Fine-grained Evaluation for End-to-End Inline Audio Descriptions](https://arxiv.org/abs/2610.39955)**
  - *Subhashini Venugopalan, Jenny Tan, Taylor Roper et al.*
  - 🤗 · `2026-10-29`
  - Audio descriptions (AD) are essential for making visual media accessible to blind and low-vision (BLV) users. While Multimodal Large Language Models (MLLMs) offer a scalable solution for generating audio descriptions on-demand, their performance on ``inline'' audio descriptions -…

- **[Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2610.40409v1)**
  - *Chenjie Qiu, Zixuan Zeng, Shaobin Shi et al.*
  - `2026-10-29`
  - Complex questions in retrieval-augmented generation require evidence spread over several documents, and an answer is reliable only when the retriever finds all of it. Chain embedding retrievers collect such evidence step by step, re-encoding the question together with the passage…

- **[DynaRev: Benchmarking Web Agents under Dynamic Goal Revision](https://arxiv.org/abs/2610.40133v1)**
  - *Shiqi Zhang, Guochen Zhou, Zesheng Wei et al.*
  - `2026-10-29`
  - Web agents are typically evaluated with goals fully specified before execution and fixed thereafter, whereas real users often revise their requirements during interaction. To study such interactions, we introduce DynaRev, a benchmark of 181 tasks to evaluate web agents under dyna…

- **[KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising Agents](https://arxiv.org/abs/2610.39884v1)**
  - *Xinhua Miao, Yuanzhen Rong, Weiru Zhang et al.*
  - `2026-10-29`
  - Industrial advertising agents must continually adapt their decision knowledge to changing product offerings, traffic patterns, and operating policies. We present KARMA (Knowledge-Atomic, Regression-Gated Modular Adaptation), a training-free framework that evolves six typed knowle…

- **[Finding Is Not Returning, Returning Is Not Reconstructing: A Multi-Dimensional Evaluation of Agent Social Re-entry](https://arxiv.org/abs/2610.39781v1)**
  - *Sheng Wan, Cong Ma, Sichen Dong et al.*
  - `2026-10-29`
  - As Large Language Model (LLM) agents increasingly participate in persistent social environments, understanding their long-term social interaction capabilities becomes increasingly important. While existing research has advanced long-term memory and conversational context retrieva…

- **[Practical Assessment of Agentic Systems in Acoustics](https://arxiv.org/abs/2610.39685v1)**
  - *Arne Hildenbrand, Philipp Diel, Zhuo Cao et al.*
  - `2026-10-29`
  - In engineering, applications of artificial intelligence have so far been largely limited to surrogate models and optimization tasks. Large language models changed this, as they can write software from a task given in words. Placed inside a harness, a system of components that let…

- **[Soei: Structured Observability of Evidence and Intent for Multi-Agent AI Software Engineering](https://arxiv.org/abs/2610.39468v1)**
  - *Mohammed Nayeem Khan, K S Sarun Kumar*
  - `2026-10-29`
  - AI coding agents now do long, multi-step and multi-session software work with little supervision. When a developer comes back to that work, the useful question is not what the model said but what was actually done, by whom, and whether it is finished. We study this in three parts…

- **[Clean Sheets and Checkpoints: Evidence Complexity for Certifying Sequential Agent Risk](https://arxiv.org/abs/2610.39124v1)**
  - *Rohith Yanambaka Venkata, Don McBride, Tiago Sequeira et al.*
  - `2026-10-29`
  - Dangerous-capability evaluations often test an AI agent from prepared states at ordered milestones. A clean sheet records no successes. What it certifies about a campaign of $B$ attempts depends on what a failed attempt erases. We model the task as a chain of $k$ milestones divid…

- **[rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment](https://arxiv.org/abs/2610.40488v1)**
  - *Art Kanke*
  - `2026-10-29`
  - Do research agents have taste, the judgment of which experiments are worth running before their outcomes are known? We give six frontier models seven recent NLP papers. Each model, working as a research agent alone or as a team, proposes minimum viable experiments (MVEs), forecas…

- **[HEMO: Harness Self-Evolution for Multi-Objective Combinatorial Optimization](https://arxiv.org/abs/2610.40023v1)**
  - *Jianghan Zhu, Cong Zhang, Ni Zhang et al.*
  - `2026-10-29`
  - Automatic operator design (AOD) has increasingly adopted large language models (LLMs) to generate problem-specific search and variation operators for multi-objective combinatorial optimization (MOCO). Yet most methods evolve the operators while leaving the process that discovers…

- **[ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender](https://arxiv.org/abs/2610.40627v1)**
  - *Qiyao Ma, Xiaodong Liu, Weiwei Yang et al.*
  - `2026-10-29`
  - Safety alignment has enabled large language models to reliably refuse harmful requests directly, yet the same request distributed across a multi-turn conversation still succeeds far too often. This brittleness has a mechanistic root: Alignment is shallow, with safety behavior con…

- **[Context Compaction for World Models](https://arxiv.org/abs/2610.38980v1)**
  - *Hayder Tirmazi*
  - `2026-10-28`
  - World models let observers explore and interact with generated worlds. Recent work shows that when observers revisit a region, current models often fail to regenerate it consistently. We view this as a context retrieval problem. LLM agents manage context retrieval at two layers o…

- **[How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0](https://arxiv.org/abs/2610.38617v1)**
  - *Liran Tal, Chris Liu, Charlotte Fereday et al.*
  - `2026-10-28`
  - We ask what AI coding agents and AI security harnesses find that deterministic static application security testing (SAST) does not, and what they miss that SAST catches. VulnBench 2.0 is a benchmark of 108 hand-curated, attacker-reachable vulnerabilities in 20 open-source web app…

- **[Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents](https://arxiv.org/abs/2610.38392v1)**
  - *Hau-Sing So, Daixian Liu, Weicai Long*
  - `2026-10-28`
  - Self-improving LLM agents edit their own harness, the prompts and rules around a fixed model, and keep an edit only if an acceptance gate scores it higher on a batch of tasks. Such a gate sees what the harness does under the current model, not what it would still prevent if one s…

- **[EPSBench: Benchmarking LLM Agents for Earnings Forecasting](https://arxiv.org/abs/2610.38293v1)**
  - *Yanbin Yin, Chuyu Xu, Liqin Ye et al.*
  - `2026-10-28`
  - Quarterly earnings forecasting requires an agent to connect financial evidence to the income-statement line items that produce a company's reported earnings. We introduce EPSBench, a benchmark for studying this ability across 149 firm-quarters from 86 US companies. Agents read a…

- **[Precedent or Intent? What Coding Agents Follow When Evolving Existing Code](https://arxiv.org/abs/2610.38244v1)**
  - *Haichao Zhu, Geyang Xu, Zhaorui Yang et al.*
  - `2026-10-28`
  - Existing code reveals past implementation decisions but rarely explains the reasoning behind them. When coding agents implement new features or modify existing functionality, past decisions may conflict with new task instructions. This raises a fundamental question for agentic so…

- **[Rubricon: Automated Rubric Generation and Refinement for LLM Evaluation and Training](https://arxiv.org/abs/2610.38220v1)**
  - *Ulyana Tkachenko, Hui Wen Goh, Guram Gogia et al.*
  - `2026-10-28`
  - Rubrics enable reward assignment on tasks without verifiable answers, but are expensive to manually produce from scratch. We present Rubricon, a pipeline that generates discriminative rubrics without requiring human preference labels, rubric annotation, or generator-model trainin…

- **[Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](https://arxiv.org/abs/2610.38095v1)**
  - *NVIDIA, :, Aastha Jhunjhunwala et al.*
  - `2026-10-28`
  - We introduce Nemotron 3.5 Super and Nemotron 3.5 Lightning, open and efficient Mixture-of-Experts Hybrid Mamba-Transformer models designed for reasoning, long-context understanding, and agentic workloads. Super is a 120B-parameter, 12B-active multimodal model, while Lightning is…

- **[3DCodeEdit: Benchmarking Instruction-Guided 3D Program Editing](https://arxiv.org/abs/2610.38231v1)**
  - *Binjie Wang, Xinran Zhao, Shoubin Yu et al.*
  - `2026-10-28`
  - Language models increasingly create 3D content through code, with practical workflows often relying on editing existing programs rather than regenerating them, for speed and precise control. Such edits require understanding what a program builds and foreseeing how a change reshap…

- **[El Agente Quntur: Agentic Active-Space Selection for CASSCF](https://arxiv.org/abs/2610.38145v1)**
  - *Juan B. Pérez-Sánchez, Viviana Roman-Ventura, Olalla Nieto-Faza et al.*
  - `2026-10-28`
  - Multireference calculations often require substantial human expertise and time to choose and refine an active space for the electronic states or chemical process of interest. This involves selecting which orbitals to include, verifying that the calculation describes the intended…

- **[MCCL: Training Pytorch models across a fleet of Macs at Skywalker Sound](https://arxiv.org/abs/2610.39029v1)**
  - *Kevin Sasso, Chris Fiegel, Francis Aitken et al.*
  - `2026-10-28`
  - Skywalker Sound, a premier audio post-production facility, operates more than 200 M4 Max Mac Studios on a 10Gb Ethernet network. When not in use by artists, these machines sit idle, representing massive untapped unified memory and compute capacity. While these fleets are excellen…

- **[RainCheck: Harnessing Historical Weather Data with Machine Learning for Rainfall Forecasting in Bangladesh](https://arxiv.org/abs/2610.38211v1)**
  - *Shahran Rahman Alve, Muhammad Zawad Mahmud, Samiha Islam et al.*
  - `2026-10-28`
  - Machine-learning rainfall forecasts are often evaluated by shuffling station records into random training and test sets. For rainfall, this lets a model see what happened at neighbouring stations on the very day it is asked to forecast, and it hides the fact that a seasonal looku…

- **[Implicit Minor Detection from Multi-Turn Dialogue in High-Risk AI Interactions: A Constrained Self-Evolving LLM Harness](https://arxiv.org/abs/2610.38546v1)**
  - *Xiaohan Zhang, Ying Zhao, Ruilin Guo et al.*
  - `2026-10-28`
  - In high-risk text interactions, a system may need to estimate whether the current speaker is likely to be a minor before applying age-conditioned safeguards. Many text-based dialogue systems lack strong identity signals such as account information, verified identity, facial data,…

- **[Auditable Hierarchical Inference with Multimodal Evidence and Bayesian Active Inquiry](https://arxiv.org/abs/2610.38774v1)**
  - *Yucheng Liu, Everett X. Wang*
  - `2026-10-28`
  - Most multimodal classifiers assume that all useful evidence is available upfront, whereas clinical inquiry is sequential. We present a synthetic evaluation framework separating objective multimodal inference from active inquiry. An objective model maps synthetic tongue, bilateral…

- **[Keepace.ai: A Technical Report on a Large Language Model for Sports and Health](https://arxiv.org/abs/2610.38249v1)**
  - *Keepace. ai Team, Bowen Wu, Heng Wang et al.*
  - `2026-10-28`
  - Large language models hold promise for delivering safe, scientifically grounded, and personalized exercise guidance at scale, yet the sports-and-health domain still lacks curated training corpora and rigorous evaluation benchmarks. Keepace.ai is a domain-specialized LLM built on…

- **[VerifiedLab: Harnessing Knowns for Unknowns](https://arxiv.org/abs/2610.37923v1)**
  - *Yu Yao, Jiayi Dong, Yang Yang et al.*
  - `2026-10-27`
  - Across human history, knowledge has undergone several transitions, from orality to writing and then to digital archives. At each transition, humans established new conventions to preserve knowledge for the new era. Nowadays, as research agents are increasingly deployed for labora…

- **[Evaluating and improving AI agents for sequencing protocol understanding](https://arxiv.org/abs/2610.37851v1)**
  - *Chi-Lam Poon, Michael Goneos, Zezheng Song et al.*
  - `2026-10-27`
  - Existing scientific-agent benchmarks rarely evaluate whether agents can reconstruct the exact molecular structures and generation workflows specified by sequencing protocols, a capability critical for analyzing customized sequencing assays. We introduce LibStructBench, a document…

- **[When the Critic Falls Behind: Co-Evolving Rubrics and Harnesses for Continual Agent Self-Improvement](https://arxiv.org/abs/2610.36826v1)**
  - *Hao Chen, Yukun Yan, Ziyu Han et al.*
  - `2026-10-27`
  - Autonomous agents increasingly depend on harnesses that govern interaction, memory, tools, and execution around large language models (LLMs). While recent work has begun to evolve these harnesses from execution experience, the supervision used to guide evolution often remains rel…

- **[The View from Nowhere: Population-Centered Agent Evolution](https://arxiv.org/abs/2610.36660v2)**
  - *Shuo Yan, Ningning Hou, Haoyu He et al.*
  - `2026-10-27`
  - Self-improving AI systems can revise the designs that govern their own behavior. Yet existing approaches center improvement on selected parent agents and their evolutionary experience, leaving the broader population largely underused. We identify a substantial gap between populat…

- **[Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements](https://arxiv.org/abs/2610.36584v1)**
  - *Binhang Qi, Yiming Liu, Yun Lin et al.*
  - `2026-10-27`
  - As large language model agents increasingly compile natural-language requirements into repository-level code, requirement-to-test generation grows in importance to provide validation constraints (or harness) to guide code generation. Yet it remains unclear whether current agents…

- **[Your Agent Acts Differently When You're Around: How User Presence Changes Agent Behavior in Negotiation](https://arxiv.org/abs/2610.36435v1)**
  - *Jane Pan, You Lyu, Abe Bohan Hou et al.*
  - `2026-10-27`
  - LLM agents increasingly interact with other agents on behalf of users, yet how users in the loop affect their agents' behavior--for better or worse--remains poorly understood. We study this question through the lens of negotiation, where agents must represent users while strategi…

- **[Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](https://arxiv.org/abs/2610.37648v1)**
  - *Andrew Szot, Samira Abnar, Omar Attia et al.*
  - `2026-10-27`
  - We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthA…

- **[Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces](https://arxiv.org/abs/2610.37255v2)**
  - *Jian Mu, Ruibo Shen, Yao Shu*
  - `2026-10-27`
  - Language model agents are post-trained and deployed through a harness, the prompts, tools, and control logic that present a task to the model and execute its outputs. Harnesses are often revised and judged by how an already trained model performs under them, which assumes that wh…

- **[CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning](https://arxiv.org/abs/2610.36469v1)**
  - *Jianwen Chen, Peng Xia, Kaide Zeng et al.*
  - `2026-10-27`
  - Large language model (LLM) agents interact with their environments through executable harnesses that govern tool use and feedback. Optimizing a harness for a fixed policy overlooks how its behavior changes during learning, while training a policy under a fixed harness leaves the…

- **[GEPA-Curator: Curated Learning for Self Improving Agents](https://arxiv.org/abs/2610.37651v1)**
  - *Zack Yu, Nicholas Lee, Minjae Lee et al.*
  - `2026-10-27`
  - Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesse…

- **[A Harness Reducing over-Defensive Writing in Agents by Isolating Objections](https://arxiv.org/abs/2610.36717v1)**
  - *Xiaochen Chang*
  - `2026-10-27`
  - When expanding a report, writing with agents may introduce a stronger claim than the article makes and then disclaim it. This is called over-defensive writing. We assume that this is because the agent is writing for responding to an adversarial AI reviewer, instead of a human rea…

- **[FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation](https://arxiv.org/abs/2610.36545v1)**
  - *Yijing Lin, Zhendong Mao, Mengqi Huang et al.*
  - `2026-10-27`
  - Unified conditional image generation requires a single model to preserve different aspects of a visual input while producing a target image that follows textual guidance. Pretrained video models provide a promising foundation by encoding visual transformations across time, yet ex…

- **[Understanding Large Language Models as Numerical Optimizers](https://arxiv.org/abs/2610.37932v1)**
  - *Lingyun Guo, Ali Bereyhi*
  - `2026-10-27`
  - Large language models (LLMs) have emerged as potential tools for numerical optimization. Despite promising results, their intrinsic optimization capabilities and limitations remain poorly understood, particularly in high dimensions. This paper investigates the ability of LLMs to…

- **[The State and Fate of Multilingual, Contextual Evaluation in the NLP World](https://arxiv.org/abs/2610.36990v1)**
  - *Manan Uppadhyay, Himanshu Beniwal, Prashant Kodali et al.*
  - `2026-10-27`
  - Multilingual evaluation benchmarks are the primary instrument for assessing whether large language models generalize beyond English, yet the adequacy of these benchmarks has received little systematic scrutiny. We present a data-driven audit of 51 recent multilingual benchmarks s…

- **[SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2610.36991v2)**
  - *Zafer Sahinoglu, Abdulazeez Mohammed, Buse Yaren Kazangirler et al.*
  - `2026-10-27`
  - Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation on the retrieved context. Although dense retrieval is effective for local semantic matching, independently ranked retrieval can return redu…


## Finance  (175)

### AAAI

- **[A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators](https://doi.org/10.1609/aaai.v40i35.40240)**
  - *Ming-Ming Zhao, Xiaokang Wei, Yuan-Qi Shao et al.*
  - **AAAI 2026** · `2026-03-14`
  - Large language models (LLMs) have shown strong potential in automating the design of agentic workflows. However, existing methods still rely heavily on manually predefined operators, limiting generalization and scalability. To address this issue, we propose A²Flow, a fully automa…

- **[LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042)**
  - *Cheng Yang, Hui Jin, Xinlei Yu et al.*
  - **AAAI 2025** · `2025-11-26`
  - Diagnosing lung cancer typically involves physicians identifying lung nodules in Computed tomography (CT) scans and generating diagnostic reports based on their morphological features and medical expertise. Although advancements have been made in using multimodal large language m…

- **[CVE-LLM : Ontology-Assisted Automatic Vulnerability Evaluation Using Large Language Models](https://arxiv.org/abs/2502.15932)**
  - *Rikhiya Ghosh, Hans-Martin von Stockhausen, Martin Schmitt et al.*
  - **AAAI 2025** · `2025-02-21`
  - The National Vulnerability Database (NVD) publishes over a thousand new vulnerabilities monthly, with a projected 25 percent increase in 2024, highlighting the crucial need for rapid vulnerability identification to mitigate cybersecurity attacks and save costs and resources. In t…


### NeurIPS

- **[DyFlow: Dynamic Workflow Framework for Agentic Reasoning](https://arxiv.org/abs/2509.26062)**
  - *Yan-Bo Wang, Zi-Xiang Xu, Yue Huang et al.*
  - **NeurIPS 2025** · `2025-09-30`
  - Agent systems based on large language models (LLMs) have shown great potential in complex reasoning tasks, but building efficient and generalizable workflows remains a major challenge. Most existing approaches rely on manually designed processes, which limits their adaptability a…

- **[Deep Video Discovery: Agentic Search with Tool Use for Long-form Video Understanding](https://arxiv.org/abs/2505.18079)**
  - *Xiaoyi Zhang, Zhao-Yang Jia, Zong-Yu Guo et al.*
  - **NeurIPS 2025** · `2025-05-23`
  - Long-form video understanding presents significant challenges due to extensive temporal-spatial complexity and the difficulty of question answering under such extended contexts. While Large Language Models (LLMs) have demonstrated considerable advancements in video analysis capab…

- **[AutoData: A Multi-Agent System for Open Web Data Collection](https://arxiv.org/abs/2505.15859)**
  - *Tian-Yi Ma, Yi-Yue Qian, Zhe-Yuan Zhang et al.*
  - **NeurIPS 2025** · `2025-05-21`
  - The exponential growth of data-driven systems and AI technologies has intensified the demand for high-quality web-sourced datasets. While existing datasets have proven valuable, conventional web data collection approaches face significant limitations in terms of human effort and…


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
  - **ICML 2026** · OpenReview · `2026-08-20`
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
  - **ICML 2026** · OpenReview · `2025-09-17`
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
  - **ICML 2026** · OpenReview · `2025-06-06`
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
  - **ICML 2026** · OpenReview · `2024-10-06`
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
  - **ICML 2026** · OpenReview · `2024-03-31`
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
  - **ICML 2026** · OpenReview · `2024-01-01`
  - This research introduces an innovative approach to forecasting cryptocurrency prices by combining user-generated content (UGC) and sentiment analysis with quantitative data. The primary goal is to overcome limitations in existing methods for market forecasting, where accurate for…

- **[Cryptocurrency Topic Burst Prediction via Hybrid Twin-structured Multi-modal Learning](https://openreview.net/forum?id=h5r1B6G0dc)**
  - *Keting Yin, Xiaen Sun, Tian Feng*
  - **ICML 2026** · OpenReview · `2024-01-01`
  - Social media users actively engage in discussions concerning news and events within the dynamic cryptocurrency market, resulting in the widespread dissemination of cryptocurrency-related topics across various platforms. The ongoing monitoring of these topics is crucial to informe…

- **[Cryptocurrency Price Forecasting Using XGBoost Regressor and Technical Indicators](https://arxiv.org/abs/2407.11786)**
  - *{'fullname': 'Abdelatif Hafid', 'username': ''}, {'fullname': 'Maad Ebrahim', 'username': ''}, {'fullname': 'Ali Alfatemi', 'username': ''} et al.*
  - **ICML 2026** · OpenReview · `2024-01-01`
  - The rapid growth of the stock market has attracted many investors due to its potential for significant profits. However, predicting stock prices accurately is difficult because financial markets are complex and constantly changing. This is especially true for the cryptocurrency m…

- **[Cryptocurrency Price Forecasting using Variational Autoencoder with Versatile Quantile Modeling](https://openreview.net/forum?id=VtVNMYPGRp)**
  - *Sungchul Hong, SeungHwan An, Jong-June Jeon*
  - **ICML 2026** · OpenReview · `2024-01-01`
  - In recent years, there has been a growing interest in probabilistic forecasting methods that offer more comprehensive insights by considering prediction uncertainties rather than point estimates. This paper introduces a novel variational autoencoder learning framework for multiva…

- **[Identifying Risky Vendors in Cryptocurrency P2P Marketplaces](https://openreview.net/forum?id=rvSv8Df4AB)**
  - *Taro Tsuchiya, Alejandro Cuevas, Nicolas Christin*
  - **ICML 2026** · OpenReview · `2023-10-04`
  - Peer-to-Peer (P2P) cryptocurrency exchanges are two-sided marketplaces, similar to eBay/Craigslist, where individuals can offer to sell cryptocurrency assets in exchange for payment.
Due to disintermediation, these marketplaces trade off increased privacy for higher risk (e.g., s…

- **[Interface Illusions: Uncovering the Rise of Visual Scams in Cryptocurrency Wallets](https://openreview.net/forum?id=39AIGw9x8m)**
  - *Guoyi Ye, Geng Hong, Yuan Zhang et al.*
  - **ICML 2026** · OpenReview · `2023-09-27`
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
  - **ICML 2026** · OpenReview · `2023-01-01`
  - Many cryptocurrency brokers nowadays offer a variety of derivative assets that allow traders to perform hedging or speculation. This paper proposes an effective algorithm based on neural networks to take advantage of these investment products. The proposed algorithm constructs a…

- **[Cryptocurrency Portfolio Optimization by Neural Networks](https://openreview.net/forum?id=8alfjwG7lf)**
  - *Quoc Minh Nguyen, Dat Thanh Tran, Juho Kanniainen et al.*
  - **ICML 2026** · OpenReview · `2023-01-01`
  - Many cryptocurrency brokers nowadays offer a va-riety of derivative assets that allow traders to perform hedging or speculation. This paper proposes an effective algorithm based on neural networks to take advantage of these investment products. The proposed algorithm constructs a…

- **[Examining Liquidity of Exchanges and Assets and the Impact of External Events in Centralized Crypto Markets: A 2022 Study](https://openreview.net/forum?id=tpk47MymYw)**
  - *Adrian Jobst, Daniel Atzberger, Robert Henker et al.*
  - **ICML 2026** · OpenReview · `2023-01-01`
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
  - **ICML 2026** · OpenReview · `2022-01-01`
  - Cryptocurrencies are peer-to-peer digital assets monitored and organised by a blockchain network. Price prediction has been a significant focus point with various machine learning algorithms, especially concerning cryptocurrency. This work addresses the challenge faced by traders…

- **[Cryptocurrency Price Prediction with Convolutional Neural Network and Stacked Gated Recurrent Unit](https://openreview.net/forum?id=98spjLJzqq)**
  - *Chuen Yik Kang, Chin-Poo Lee, Kian-Ming Lim*
  - **ICML 2026** · OpenReview · `2022-01-01`
  - Virtual currencies have been declared as one of the financial assets that are widely recognized as exchange currencies. The cryptocurrency trades caught the attention of investors as cryptocurrencies can be considered as highly profitable investments. To optimize the profit of th…

- **[A Deep Learning-Based Cryptocurrency Price Prediction Model That Uses On-Chain Data](https://openreview.net/forum?id=6XBg6f3kBb)**
  - *Gyeongho Kim, Dong-Hyun Shin, Jaegyeong Choi et al.*
  - **ICML 2026** · OpenReview · `2022-01-01`
  - Cryptocurrency has recently attracted substantial interest from investors due to its underlying philosophy of decentralization and transparency. Considering cryptocurrency’s volatility and unique characteristics, accurate price prediction is essential for developing successful in…

- **[Cryptocurrency Price Prediction With Multi-task Multi-step Sequence-to-Sequence Modeling](https://openreview.net/forum?id=x5ZNDu77kF)**
  - *Jesper T. Kristensen, Juan P. Madrigal-Cianci, Giorgos Felekis et al.*
  - **ICML 2026** · OpenReview · `2022-01-01`
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
  - **ICML 2026** · OpenReview · `2020-04-17`
  - This paper aims to analyse the impact of Cryptocurrency usage on users’ perceived benefits and behaviour. The Technology Acceptance Model has been used as foundation for this research. In this study, three main factors were examined, namely perceived ease of use, perceived benefi…

- **[Users’ Knowledge and Motivation on Using Cryptocurrency](https://openreview.net/forum?id=k7lgOyf7XP)**
  - *{'fullname': 'Omar Alqaryouti'}, {'fullname': 'Nur Siyam'}, {'fullname': 'Zainab Alkashri'} et al.*
  - **ICML 2026** · OpenReview · `2020-04-17`
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
  - **ICML 2026** · OpenReview · `2019-01-01`
  - This paper aims to analyse the impact of Cryptocurrency usage on users’ perceived benefits and behaviour. The Technology Acceptance Model has been used as foundation for this research. In this study, three main factors were examined, namely perceived ease of use, perceived benefi…

- **[Users' Knowledge and Motivation on Using Cryptocurrency](https://openreview.net/forum?id=nukYddD2kK)**
  - *Omar Alqaryouti, Nur Siyam, Zainab Alkashri et al.*
  - **ICML 2026** · OpenReview · `2019-01-01`
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
  - *Boye Niu, Yi-Liao Song, Kai Lian et al.*
  - **ICLR 2025** · `2025-01-14`
  - Multi-agent frameworks powered by large language models (LLMs) have demonstrated great success in automated planning and task execution. However, the effective adjustment of agentic workflows during execution has not been well studied. An effective workflow adjustment is crucial…


### ACL

- **[Discovery of Diverse and Realistic Financial Tail-Risk Using Generative Flow Networks](https://arxiv.org/abs/2610.38838v1)**
  - *Adir Serruya, Gilad Katz*
  - **ACL** · `2026-10-28`
  - Accurate modeling of rare, high-impact financial events is essential for robust risk management. Sampling-based techniques such as Sequential Markov Chain Monte Carlo (SMCMC) generate diverse scenarios but inefficiently explore high-risk regions, while Deep Reinforcement Learning…

- **[Representation Complexity Along Learning Trajectories: Trading Width for Precision and Time](https://arxiv.org/abs/2610.39027v1)**
  - *Ryan Singh, Miguel De Llanza, Christopher L. Buckley*
  - **ACL** · `2026-10-28`
  - What computational role does overparameterisation play during learning? Information-plane analyses suggest that neural networks can traverse representations substantially more complex than those required by their final predictors. We explore when this transient complexity serves…

- **[BridgeRouter: Gain-Aware Instance Routing over Cross-Modal Bridge Portfolios](https://arxiv.org/abs/2610.38152v1)**
  - *Ruoxi Piao, Alicia Lu, Yunzhen Zhang et al.*
  - **ACL** · `2026-10-28`
  - Lightweight representation bridges make pretrained, task-adapted EEG foundation models executable on other biosignal modalities without retraining their backbones. However, selecting a single bridge pathway globally assigns every instance to the same transfer route and ignores co…

- **[FinReporting: An Agentic Workflow for Localized Reporting of Cross-Jurisdiction Financial Disclosures](https://arxiv.org/abs/2604.05966)**
  - *Fan Zhang, M. Song, R. Elbadry et al.*
  - **ACL 2026** · `2026-04-07`
  - Financial reporting systems increasingly leverage Large Language Models (LLMs) to extract and summarize corporate disclosures. However, most existing approaches assume a single-market setting and overlook structural differences across jurisdictions. Variations in accounting taxon…

- **[HalluLens: LLM Hallucination Benchmark](https://arxiv.org/abs/2504.17550)**
  - *Yejin Bang, Ziwei Ji, A. Schelten et al.*
  - **ACL 2025** · `2025-04-24`
  - Large language models (LLMs) often generate responses that deviate from user input or training data, a phenomenon known as"hallucination."These hallucinations undermine user trust and hinder the adoption of generative AI systems. Addressing hallucinations is essential for the adv…

- **[Right Answer, Wrong Score: Uncovering the Inconsistencies of LLM Evaluation in Multiple-Choice Question Answering](https://arxiv.org/abs/2503.14996)**
  - *F. Molfese, Luca Moroni, Luca Gioffré et al.*
  - **ACL 2025** · `2025-03-19`
  - One of the most widely used tasks for evaluating Large Language Models (LLMs) is Multiple-Choice Question Answering (MCQA). While open-ended question answering tasks are more challenging to evaluate, MCQA tasks are, in principle, easier to assess, as the model's answer is thought…


### EMNLP

- **[QuantAgents: Towards Multi-agent Financial System via Simulated Trading](https://arxiv.org/abs/2510.04643)**
  - *Xiang-Yu Li, Ya-Wen Zeng, Xiao-Fen Xing et al.*
  - **EMNLP 2025** · `2025-10-06`
  - In this paper, our objective is to develop a multi-agent financial system that incorporates simulated trading, a technique extensively utilized by financial professionals. While current LLM-based agent models demonstrate competitive performance, they still exhibit significant dev…

- **[AMAS: Adaptively Determining Communication Topology for LLM-based Multi-Agent System](https://arxiv.org/abs/2510.01617)**
  - *Hui Yi Leong, Yuheng Li, Yu-Qing Wu et al.*
  - **EMNLP 2025** · `2025-10-02`
  - Although large language models (LLMs) have revolutionized natural language processing capabilities, their practical implementation as autonomous multi-agent systems (MAS) for industrial problem-solving encounters persistent barriers. Conventional MAS architectures are fundamental…

- **[Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents](https://arxiv.org/abs/2509.17488)**
  - *Shou-Ju Wang, Fenglin Yu, Xirui Liu et al.*
  - **EMNLP 2025** · `2025-09-22`
  - The increasing autonomy of LLM agents in handling sensitive communications, accelerated by Model Context Protocol (MCP) and Agent-to-Agent (A2A) frameworks, creates urgent privacy challenges. While recent work reveals significant gaps between LLMs'privacy Q&A performance and thei…

- **[Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses](https://arxiv.org/abs/2509.16093)**
  - *Fangyi Yu, Nabeel Seedat, Dasha Herrmannova et al.*
  - **EMNLP 2025** · `2025-09-19`
  - Evaluating long-form answers in high-stakes domains such as law or medicine remains a fundamental challenge. Standard metrics like BLEU and ROUGE fail to capture semantic correctness, and current LLM-based evaluators often reduce nuanced aspects of answer quality into a single un…

- **[ReliableEval: A Recipe for Stochastic LLM Evaluation via Method of Moments](https://arxiv.org/abs/2505.22169)**
  - *G. Lior, Eliya Habba, Shahar Levy et al.*
  - **EMNLP 2025** · `2025-05-28`
  - LLMs are highly sensitive to prompt phrasing, yet standard benchmarks typically report performance using a single prompt, raising concerns about the reliability of such evaluations. In this work, we argue for a stochastic method of moments evaluation over the space of meaning-pre…

- **[Mind the Blind Spots: A Focus-Level Evaluation Framework for LLM Reviews](https://arxiv.org/abs/2502.17086)**
  - *Hyungyu Shin, Jingyu Tang, Yoonjoo Lee et al.*
  - **EMNLP 2025** · `2025-02-24`
  - Peer review underpins scientific progress, but it is increasingly strained by reviewer shortages and growing workloads. Large Language Models (LLMs) can automatically draft reviews now, but determining whether LLM-generated reviews are trustworthy requires systematic evaluation.…


### Other / arXiv

- **[Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?](https://arxiv.org/abs/2610.38342)**
  - *Huangfei Jiang, Anning Hu, Kai Sheng et al.*
  - 🤗 Featured · `2026-10-28`
  - Financial agents must form forecasts and investment judgments from decision-time evidence, with predictions evaluated against subsequent outcomes. Existing benchmarks assess financial knowledge, research workflows, or forecasting, but evaluating the full research process requires…

- **[AskStream: When and What to Ask Proactively under Uncertainty in Streaming Video Understanding](https://arxiv.org/abs/2610.38678)**
  - *Lu Wang, Zhuoran Jin, Longxiang Wang et al.*
  - 🤗 Featured · `2026-10-28`
  - Recent advances in multimodal large language models have increased interest in interaction paradigms for video understanding. The evolution from offline to streaming and proactive interaction has gradually shifted models from passive responders toward more proactive agents that c…

- **[ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics](https://arxiv.org/abs/2610.23656)**
  - *Xiaohang Yu, Hejia Geng, William Knottenbelt*
  - 🤗 Featured · `2026-10-16`

- **[Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?](https://arxiv.org/abs/2610.39497)**
  - *Qi Wang, Yun Qu, Lizhou Cai et al.*
  - 🤗 · `2026-10-29`
  - Progress toward artificial general intelligence (AGI) has largely relied on scaling a resource-intensive executive, System-2, through larger models, more data and compute, longer reasoning, and more agents. We ask whether the next stage may come instead from co-designing it with…

- **[AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers](https://arxiv.org/abs/2610.39234)**
  - *Zhiyi Liu, Haohua Du, Haoqi Sun et al.*
  - 🤗 · `2026-10-29`
  - Large language model (LLM) agents have demonstrated strong capabilities in automating complex information-seeking and transactional tasks across the open web. However, their real-world reliability remains limited by access barriers, such as dead links, authentication walls, rate…

- **[Collaborative AI agents for autonomous experimental research with solid-state quantum spins](https://arxiv.org/abs/2610.40589v1)**
  - *El Mustapha Mansouri, Eikichi Kimura, Masato Koga et al.*
  - `2026-10-29`
  - An autonomous research laboratory could conduct an entire study, from formulating questions to preparing manuscripts. Artificial intelligence (AI) offers one route towards this goal. Recent AI systems take on several research roles, but may draw conclusions that the evidence does…

- **[Gym-Anything for Robotics: Scaling physical simulations with digital agents](https://arxiv.org/abs/2610.40565v1)**
  - *Pranjal Aggarwal, Sean Welleck*
  - `2026-10-29`
  - Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world. However, despite decades of progress, available simulations cover only a narrow range of real-world tasks and physical phenomena. The core bottleneck is t…

- **[Retrieval as Traversal: Value-Indexed Memory for Stateful Long-Context Agents](https://arxiv.org/abs/2610.40545v1)**
  - *Daniel Strauß, Zhenshan Bing, Alois Knoll*
  - `2026-10-29`
  - Long-context models repeatedly solve closely related retrieval problems. Attention or global retrieval can retain large stores, but each forward pass again searches for what matters. Recurrent compression avoids this search only by deciding earlier what information to preserve. N…

- **[DynaRev: Benchmarking Web Agents under Dynamic Goal Revision](https://arxiv.org/abs/2610.40133v1)**
  - *Shiqi Zhang, Guochen Zhou, Zesheng Wei et al.*
  - `2026-10-29`
  - Web agents are typically evaluated with goals fully specified before execution and fixed thereafter, whereas real users often revise their requirements during interaction. To study such interactions, we introduce DynaRev, a benchmark of 181 tasks to evaluate web agents under dyna…

- **[Hybrid AI Patterns: Thirteen Ways to Couple Language Models with Rules, and How to Choose Among Them](https://arxiv.org/abs/2610.40036v1)**
  - *Siegfried Handschuh, Götz-Henrik Wiegand, Lorena Raichle*
  - `2026-10-29`
  - Language models handle text well, and rule engines give conclusions with proofs. Systems that combine the two are usually described by example, and the same coupling turns up under different names in agent frameworks, guardrail toolkits and neuro-symbolic research. This document…

- **[MoLRSI: A Recursive Self-Improving AI agent for Molecular Discovery](https://arxiv.org/abs/2610.39714v1)**
  - *Yikun Zhang, Xiwei Cheng, Mingze Yuan et al.*
  - `2026-10-29`
  - Molecular discovery requires navigating vast combinatorial search spaces while balancing competing biological objectives. AI agents can automate expert-defined molecular design protocols, but automation alone does not address how to optimize workflows for new tasks or improve the…

- **[Soei: Structured Observability of Evidence and Intent for Multi-Agent AI Software Engineering](https://arxiv.org/abs/2610.39468v1)**
  - *Mohammed Nayeem Khan, K S Sarun Kumar*
  - `2026-10-29`
  - AI coding agents now do long, multi-step and multi-session software work with little supervision. When a developer comes back to that work, the useful question is not what the model said but what was actually done, by whom, and whether it is finished. We study this in three parts…

- **[Beyond LLM Wrappers: Context Engineering and the Three-Engine Architecture for Reliable Financial AI](https://arxiv.org/abs/2610.39230v1)**
  - *Pradeep Kumar GS, Ravi Tanniru*
  - `2026-10-29`
  - Financial AI systems must support decision-bearing questions involving payments, collections, cash flow, and compliance while ensuring numerical accuracy, traceability, and auditability. Large language models (LLMs) enable natural language interaction but cannot independently gua…

- **[Machine Learning-Based Detection of Mobile Money Scan Messages in Ghana: A Comparative Evaluation of Naive Bayes, Support Vector Machine, and Randon Forest Classifiers](https://arxiv.org/abs/2610.40544v1)**
  - *Ibrahim Salifu, Muhaisin Tiyumba Nantogmah*
  - `2026-10-29`
  - Mobile money (MoMo) is Ghana's preferred retail payment channel, recording GHC518.4 billion in transactions in December 2025 and over 26.7 million active accounts (Graphic Online, 2026). This growth has coincided with increased social-engineering fraud over Short Message Service…

- **[FIRME: Registry-Anchored Memory Graphs for Evolving, Heterogeneous Investor Knowledge](https://arxiv.org/abs/2610.40482v1)**
  - *Yunbai Zhang, Yunyi Gao, Han-Tai Shiao*
  - `2026-10-29`
  - Financial AI workflows that reuse investor knowledge need persistent memory that integrates observations across sources and periods without losing identity or provenance. In a knowledge graph, recurring observations may use different surface forms, fragmenting relationship histor…

- **[Explainable and Adaptive Machine Learning for Fraud Risk Detection in Bangladesh's Digital Banking Ecosystem](https://arxiv.org/abs/2610.39556v1)**
  - *Md Najmus Swaqeeb*
  - `2026-10-29`
  - The rapid expansion of digital banking and mobile financial services creates growing challenges for fraud detection, particularly under severe class imbalance and operational constraints. This study presents an explainable and adaptive machine-learning framework integrating chron…

- **[Sparse Autoencoders as Implicit Diversification Regularisers for Cross-Sectional Cryptocurrency Returns](https://arxiv.org/abs/2610.39205v1)**
  - *Weijia Han, Lisha Qu*
  - `2026-10-29`
  - Factor models are central to asset pricing and portfolio construction, but neural factors are often difficult to interpret, and their effect on portfolio risk is unclear. A sparse autoencoder (SAE) may address both concerns by describing daily returns across many assets with only…

- **[Information Flow and Market Risk: Transformer-Based Evidence on Sentiment and Volatility Dynamics](https://arxiv.org/abs/2610.39636v1)**
  - *Szymon Lis, Robert Ślepaczuk, Paweł Sakowski*
  - `2026-10-29`
  - This study examines whether transformer-based financial news sentiment improves equity volatility forecasts beyond conventional market-based predictors. Using data for eleven US stocks, we compare volatility persistence models with specifications incorporating the VIX, AAII inves…

- **[Early-Buyer Groups and Fast-Wallet Teams on a Bonding-Curve Launchpad: A Prospective Measurement Study of pump.fun on Solana](https://arxiv.org/abs/2610.39458v1)**
  - *Fail Gafarov*
  - `2026-10-29`
  - We study coordinated groups of wallets on a bonding-curve launchpad (pump.fun on Solana), using a complete record of 200\,443 token launches, 15\,854\,121 curve trades and 51\,025\,958 SOL transfers over 88.3 hours. A prospective, multi-channel discovery procedure (co-buying, sha…

- **[The Generalised Kessler Syndrome and the Persian Gulf](https://arxiv.org/abs/2610.40129v1)**
  - *Bernhard K Meister*
  - `2026-10-29`
  - The term Kessler syndrome was coined for a runaway orbital cascade creating a high-density debris field. The idea is generalised and applied to supply chains. An additive channel enables failures to generate further failures; a subtractive channel erodes the capacity to contain a…

- **[TreasuryQA Bench: Can AI Agents Work an Archive of Scanned Financial Records?](https://arxiv.org/abs/2610.38924v1)**
  - *Ritiz Tambi, Sahar Shayegan, Joshua Meyer et al.*
  - `2026-10-28`
  - Organisations keep decades of financial records as scanned PDFs on shared drives, and AI agents can now reach those drives through Model Context Protocol (MCP) servers. Existing benchmarks do not mirror this production setting because they simplify the task. In some, the relevant…

- **[Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems](https://arxiv.org/abs/2610.38869v1)**
  - *Zhuoyun Li, Boxuan Wang, Jinwei Hu et al.*
  - `2026-10-28`
  - Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated h…

- **[From Grind to Grasp](https://arxiv.org/abs/2610.38728v1)**
  - *Peter Sunehag*
  - `2026-10-28`
  - Discussions of complexity, knowledge and intelligence often overlook the work involved. For example, outputs generated by short programs have low algorithmic complexity but can have high computational depth, the least work needed to produce them from near-shortest programs. Produ…

- **[Right Numbers, Wrong Questions: Evaluating LLMs on Underspecified Financial Queries](https://arxiv.org/abs/2610.38631v1)**
  - *Radha Yadav, Prasanna Devadiga, Peeyush Mishra et al.*
  - `2026-10-28`
  - Financial assistants answer questions that sound factual but depend on what the user leaves unsaid: what a data figure measures, which product variant is meant, and the investor's situation and the rules that apply. An assistant that ignores these can still answer with a real num…

- **[RoleFUZZER: User-Behaviour Fuzzing for Role-Specification Adherence in Large Language Models](https://arxiv.org/abs/2610.38438v1)**
  - *Kshitish Ghate, Michael Saxon, Tadayoshi Kohno et al.*
  - `2026-10-28`
  - Large language models (LLMs) are often conditioned into specific roles such as tutors, interviewers, or agents acting for an organisation, through system prompts that specify how they should behave. The extent to which they can actually adhere to these role specifications under m…

- **[Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](https://arxiv.org/abs/2610.38361v1)**
  - *Gangzhen Qian, Kainan Zhou, Chuhong Xu et al.*
  - `2026-10-28`
  - The external sources retained in our non-systematic audit did not isolate the incremental security or utility effect of consuming /llms.txt while ordinary retrieval remained fixed. The initial audit covered 39 sources through August 16, 2026, with later targeted updates through O…

- **[EPSBench: Benchmarking LLM Agents for Earnings Forecasting](https://arxiv.org/abs/2610.38293v1)**
  - *Yanbin Yin, Chuyu Xu, Liqin Ye et al.*
  - `2026-10-28`
  - Quarterly earnings forecasting requires an agent to connect financial evidence to the income-statement line items that produce a company's reported earnings. We introduce EPSBench, a benchmark for studying this ability across 149 firm-quarters from 86 US companies. Agents read a…

- **[AI-Driven Digital Twin Framework for Warehouse Logistics Automation Optimization](https://arxiv.org/abs/2610.38101v1)**
  - *Md Mahinur Alam, Kanita Jerin Tanha, Md Tanjin Alam et al.*
  - `2026-10-28`
  - In recent years, warehouse logistics optimization has increasingly focused on intelligent, data-driven systems to enhance operational efficiency. Conventional static product placement strategies are being progressively replaced by dynamic slotting approaches that can adapt to rea…

- **[Pinpointing Pivot Points: The DECIDE Framework for Data Analysis Decision Importances](https://arxiv.org/abs/2610.38797v1)**
  - *Zachary T. Rewolinski, Jan Simson, Frauke Kreuter et al.*
  - `2026-10-28`
  - Human judgment calls made throughout the data science life cycle can change the conclusions drawn from data. Independent analysts often make different choices when given the same data, leading to often unacceptable variations in results and contributing to the ongoing reproducibi…

- **[MCCL: Training Pytorch models across a fleet of Macs at Skywalker Sound](https://arxiv.org/abs/2610.39029v1)**
  - *Kevin Sasso, Chris Fiegel, Francis Aitken et al.*
  - `2026-10-28`
  - Skywalker Sound, a premier audio post-production facility, operates more than 200 M4 Max Mac Studios on a 10Gb Ethernet network. When not in use by artists, these machines sit idle, representing massive untapped unified memory and compute capacity. While these fleets are excellen…

- **[The Indian Financial Automated Advice Bias (IFAAB) Dataset : Auditing Socioeconomic and Demographic Disparities in LLM-Generated Financial Advice in India](https://arxiv.org/abs/2610.38239v1)**
  - *Kriti Mahajan*
  - `2026-10-28`
  - Large language models are increasingly used for financial guidance, yet little is known about whether their advice changes across social identities in Global South contexts. We introduce the Indian Financial Automated Advice Bias (IFAAB) benchmark, a counterfactual audit dataset…

- **[FilingLoop: Evaluating and Evolving LLM Agents for Corporate Disclosure Review and Revision](https://arxiv.org/abs/2610.37905v1)**
  - *Wentao Zhang, Yilei Zhao, Guangyan Gan et al.*
  - `2026-10-27`
  - Public disclosure repositories such as SEC EDGAR support informed investment through web access to corporate filings. Supporting their review with language model agents requires discovering unstated deficiencies across related documents, acquiring missing company facts, and verif…

- **[Measuring Where Intent Gets Lost in Agentic Smart Contract Synthesis](https://arxiv.org/abs/2610.37830v1)**
  - *Abhinav Goel, Agostino Capponi, Alfio Gliozzo et al.*
  - `2026-10-27`
  - AI agents can now write software from a plain-English description, but code that runs is not the same as code that does what was asked. This gap matters most for smart contracts, the programs behind Web3 applications that move money on a blockchain and cannot be fixed once deploy…

- **[TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information](https://arxiv.org/abs/2610.37571v1)**
  - *Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz et al.*
  - `2026-10-27`
  - Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-…

- **[Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents](https://arxiv.org/abs/2610.37567v1)**
  - *Pranjal Aggarwal, Sean Welleck*
  - `2026-10-27`
  - AI agents have made substantial progress in domains where they have a non-trivial amount of time to deliberate between actions, such as mathematics, software engineering, and performing tasks on desktop applications. It is less clear how such models fare in settings that demand r…

- **[From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents](https://arxiv.org/abs/2610.37482v1)**
  - *Ziyang Chen, Qian Li, Chengwei Qin*
  - `2026-10-27`
  - GUI memory should preserve the results of past actions and learn reusable operations. This is difficult in long-horizon workflows, where agents must use information across applications and useful operations are interleaved with failed attempts. We introduce Task Advancement Memor…

- **[Concordat: Typed Sessions for LLM Agents](https://arxiv.org/abs/2610.37461v1)**
  - *Milad Sikaroudi*
  - `2026-10-27`
  - Agents built on large language models are increasingly allowed to take consequential actions: cancelling bookings, issuing refunds, changing accounts. The rules that govern those actions, such as "obtain the customer's explicit confirmation before changing anything", are usually…

- **[M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents](https://arxiv.org/abs/2610.37459v1)**
  - *Hannes Ill, Rafi Al Attrach, Rajna Fani et al.*
  - `2026-10-27`
  - Clinical research over electronic health records depends on derived variables whose definitions sit outside the schema, in item codes, time windows, missingness rules, and output-grain choices that change cohorts and downstream conclusions. We introduce M4Bench, 28 clinical deriv…

- **[Test-Time Communication in Trading Agent Swarms](https://arxiv.org/abs/2610.37448v1)**
  - *Avid Fayaz, Harry Zhang, Håvard Alstadheim et al.*
  - `2026-10-27`
  - Communication between agents has mostly been studied on tasks with a shared objective and fast, clear feedback. Trading has neither: each agent manages its own account, with decisions being scored by markets late and noisily. A trading swarm is thus a population of independent de…

- **[Poisoned Skills: Propagating Jailbreaks Through Agent Markdown Files](https://arxiv.org/abs/2610.37738v1)**
  - *Kashyap R Manjusha, Murali Emani*
  - `2026-10-27`
  - Modern agent frameworks allow users to provide Markdown files containing system prompts, tool descriptions, and skill definitions (e.g., SKILL.md), which are incorporated into the agent's context during initialization. In this work, we investigate whether this configuration mecha…

- **[WCC: A Learning-Based Framework for Deciding When to Apply Cooperative Coevolution in Large-Scale Optimization](https://arxiv.org/abs/2610.37329v1)**
  - *Wenjie Qiu, Hepei Li, Jianfeng Wang et al.*
  - `2026-10-27`
  - Cooperative Coevolution (CC) and Non-Decomposition Algorithms (NDAs) are two primary approaches for large-scale global optimization (LSGO). Although both have achieved success, they exhibit markedly different performance across problem types and each faces approach-specific limit…

- **[Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation](https://arxiv.org/abs/2610.37242v1)**
  - *Saiful Khan, Afrah Farea*
  - `2026-10-27`
  - Large language model (LLM) agents that call enterprise APIs must select the correct endpoints, follow process order, use valid payload keys, and choose coded values from predefined lists. However, current retrieval-augmented service discovery treats endpoints independently and th…

- **[LiveSearch: Questions as Executable Verifier Code for a Live Benchmark of Professional-Source Financial Search Agents](https://arxiv.org/abs/2610.37166v1)**
  - *Sinuo Wang, Wentao Zhao, Jiacheng Lu et al.*
  - `2026-10-27`
  - In finance, the answer that matters is usually the current one: prices, rates, and disclosures hold only as of a given day, so retrieving up-to-date facts is a core capability of a financial agent. Yet most financial benchmarks overlook timeliness. They fix each answer at annotat…

- **[Noise Steering: Exploiting Wake Steering and Acoustic Directivity for Noise-Constrained Wind Farm Control via Reinforcement Learning](https://arxiv.org/abs/2610.36888v2)**
  - *Martín de Frutos, Baptiste Corban, Claire Bizon Monroc et al.*
  - `2026-10-27`
  - Existing noise mitigation strategies for wind farms usually consist in reducing turbines power output, without accounting for the wake interactions between them and the noise emission directivity. This leads to over-conservative policies and unexploited wind power. Yet, turbine y…

- **[RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep Research Agents](https://arxiv.org/abs/2610.36878v1)**
  - *Delin Wang, Sinuo Wang, Rui Sun et al.*
  - `2026-10-27`
  - Deep research agents conduct multi-step Web searches and synthesise retrieved information into analytical reports. Evaluating these outputs requires checking which analyses they deliver, beyond the presence of relevant facts. Query-specific binary rubrics make individual requirem…

- **[NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization](https://arxiv.org/abs/2610.36553v1)**
  - *Shuo Chen, Li Cui, Cunxin Huang et al.*
  - `2026-10-27`
  - Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in simulation-based and experimental applications, where evaluating the black-box objective can itself be costly. Thus, it remains a central chal…

- **[FIDES-Live: Evaluating Behavioral Concordance in Sequential Trading Agents](https://arxiv.org/abs/2610.36476v1)**
  - *Arther Tian, Alex Ding, Simon Wu et al.*
  - `2026-10-27`
  - Sequential trading agents produce decisions, orders, execution receipts, account states, and reports that need not agree, even when the final portfolio value is correctly computed. We present FIDES-Live, an operational extension of FIDES from generated strategy concordance to the…

- **[Impossibility of No-Regret in Multi-Agent Bidding](https://arxiv.org/abs/2610.36666v1)**
  - *Zongjun Yang, Rachitesh Kumar, Christian Kroer*
  - `2026-10-27`
  - We consider $T$ repeated second-price auctions across $n$ pacing bidders with i.i.d. item arrivals, and show that it is computationally impossible for all bidders to achieve no-regret simultaneously while satisfying their respective budget or return-on-investment constraints. The…

- **[A Simulation Testbed for Self-Governing Human-Machine Institutions](https://arxiv.org/abs/2610.36989v2)**
  - *Callum Berger, Jeremy Pitt, Stefan Sarkadi*
  - `2026-10-27`
  - AI agents no longer act alone: they cooperate, coordinate and compete within and between groups, increasingly alongside humans who are in, on or out of ``the loop''. Whether such mixed groups can govern themselves is an open question about machine behaviour and human-computer int…

- **[An Application of Geometric Riemannian Pricing Algorithm for Valuing Catastrophe Bonds in Incomplete Markets: Market-Consistent Financial Entropy and the Split of Frequency and Severity Risk Premia](https://arxiv.org/abs/2610.37171v1)**
  - *Saeid Safarveisi*
  - `2026-10-27`
  - This paper presents a framework for pricing catastrophe (CAT) bonds in incomplete markets through Riemannian geometric optimization of financial entropy. We formulate pricing-measure selection as a maximum financial entropy problem on a finite-dimensional manifold of equivalent m…

- **[What Language Models Add to Healthcare-Equity Rankings, and What They Could Have Known](https://arxiv.org/abs/2610.38056v1)**
  - *Haotong Fu, Xiyue Zhang, Jack Rose et al.*
  - `2026-10-27`
  - In healthcare equities, much of what moves a single name arrives as text: filings, trial and regulatory records, news and analyst commentary. We evaluate how screened non-market features and language-model representations improve market-based equity rankings for US healthcare fir…

- **[Selective Transfer Learning for Groundwater Level Anomaly Forecasting: Accuracy-Risk Trade-offs](https://arxiv.org/abs/2610.37733v1)**
  - *Yaxuan Wu, Ali Mohammed Mansoor Alsahag, Seyed Sahand Mohammadi Ziabari*
  - `2026-10-27`
  - This work studies context-aware selective transfer learning for multi-well groundwater anomaly forecasting in the Netherlands. Source-domain pretraining can raise average accuracy but is not uniformly reliable: it degrades performance on a substantial fraction of heterogeneous we…

- **[Simple Portfolios that Deliver Consistent Decent Returns](https://arxiv.org/abs/2610.36491v1)**
  - *Oskar Edén Wallberg, Alexander Karolin*
  - `2026-10-27`
  - Portfolio construction has been studied extensively in both academia and industry. Its applications range from pension funds and hedge funds to private savings. The academic literature centers on methodology, commonly evaluated in settings that allow short selling, leverage, and…

- **[Algorithmic Monoculture in Machine Learning-based Site-Specific Fertilizer Recommendation](https://arxiv.org/abs/2610.36941v1)**
  - *Abdelghani Belgaid*
  - `2026-10-27`
  - Machine learning recommendations are often evaluated one model at a time, despite deployment across interconnected decision makers. For continuous NPK fertilizer prescriptions, correlated errors can aggregate across farms and generate systemic costs. A model of shared and farm-sp…


---
*Generated 2026-10-30 · Sources: HuggingFace Daily Papers, OpenReview, Semantic Scholar, arXiv*
