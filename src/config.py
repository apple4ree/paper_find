"""
Configuration: target conferences, topic keywords, and API settings.
"""

# ---------------------------------------------------------------------------
# Target conferences (canonical name → list of aliases for matching)
# ---------------------------------------------------------------------------
CONFERENCES = {
    "AAAI": [
        "AAAI",
        "AAAI Conference on Artificial Intelligence",
        "Proceedings of the AAAI",
        "Association for the Advancement of Artificial Intelligence",
    ],
    "NeurIPS": [
        "NeurIPS",
        "Neural Information Processing Systems",
        "NIPS",
        "Advances in Neural Information",
    ],
    "ICML": [
        "ICML",
        "International Conference on Machine Learning",
        "Proceedings of Machine Learning Research",
        "PMLR",
    ],
    "ICLR": [
        "ICLR",
        "International Conference on Learning Representations",
        "OpenReview",
    ],
    "CVPR": [
        "CVPR",
        "Computer Vision and Pattern Recognition",
        "IEEE/CVF Conference",
        "IEEE Conference on Computer Vision",
        "CVPR 20",
    ],
    "KDD": [
        "KDD",
        "Knowledge Discovery and Data Mining",
        "ACM SIGKDD",
        "SIGKDD",
        "ACM KDD",
    ],
    "ACL": [
        "ACL",
        "Annual Meeting of the Association for Computational Linguistics",
        "ACL 20",
    ],
    "EMNLP": [
        "EMNLP",
        "Empirical Methods in Natural Language Processing",
    ],
    "NAACL": [
        "NAACL",
        "North American Chapter of the Association for Computational Linguistics",
    ],
    "IJCAI": [
        "IJCAI",
        "International Joint Conference on Artificial Intelligence",
    ],
}

# ---------------------------------------------------------------------------
# Topic keywords  (topic → list of search terms, lowercase)
# ---------------------------------------------------------------------------
TOPICS = {
    "Agent": [
        "agent",
        "multi-agent",
        "multiagent",
        "autonomous agent",
        "llm agent",
        "ai agent",
        "agentic",
        "tool use",
        "tool-use",
        "tool-augmented",
        "tool calling",
        "tool-calling",
        "function calling",
        "agent workflow",
        "agent planning",
        "agent reasoning",
        "react agent",
        "agent framework",
        "web agent",
        "code agent",
        "computer use",
        "gui agent",
        "embodied agent",
        "planning agent",
        "reflection agent",
        "agent benchmark",
        "agent evaluation",
        "agent memory",
        "agent cooperation",
        "language agent",
        "agent task",
        "agent environment",
        "agentic ai",
    ],
    "Harness": [
        "harness",
        "evaluation harness",
        "lm harness",
        "lm-harness",
        "lm eval",
        "lm-eval",
        "evaluation framework",
        "benchmarking framework",
        "eval framework",
        "evaluation suite",
        "benchmark suite",
        "evals",
        "eval harness",
        "model evaluation",
        "language model evaluation",
        "evaluation benchmark",
        "capability evaluation",
        "llm evaluation",
        "llm benchmark",
        "safety evaluation",
        "model assessment",
        "evaluation methodology",
    ],
    "Finance": [
        "finance",
        "financial",
        "trading",
        "stock market",
        "stock price",
        "portfolio",
        "portfolio management",
        "risk management",
        "credit risk",
        "algorithmic trading",
        "market prediction",
        "fintech",
        "quantitative finance",
        "investment",
        "hedge fund",
        "cryptocurrency",
        "bitcoin",
        "blockchain",
        "defi",
        "decentralized finance",
        "forex",
        "foreign exchange",
        "financial market",
        "earnings",
        "fraud detection",
        "anti-money laundering",
        "aml",
        "robo-advisor",
        "asset pricing",
        "market microstructure",
        "order book",
        "high-frequency trading",
        "market making",
        "derivatives",
        "options pricing",
        "fixed income",
        "bond market",
        "volatility prediction",
        "systemic risk",
        "financial nlp",
        "financial llm",
        "finllm",
        "economic forecasting",
        "sentiment analysis stock",
    ],
}

# ---------------------------------------------------------------------------
# ArXiv categories to pull daily submissions from
# ---------------------------------------------------------------------------
ARXIV_CATEGORIES = [
    "cs.AI",    # Artificial Intelligence
    "cs.LG",    # Machine Learning
    "cs.CL",    # Computation and Language (NLP)
    "cs.CV",    # Computer Vision
    "cs.MA",    # Multi-Agent Systems
    "q-fin.TR", # Trading and Market Microstructure
    "q-fin.PM", # Portfolio Management
    "q-fin.RM", # Risk Management
    "q-fin.ST", # Statistical Finance
    "q-fin.CP", # Computational Finance
    "econ.GN",  # General Economics
]

# Semantic Scholar fields to retrieve
SS_FIELDS = (
    "title,abstract,authors,year,venue,externalIds,"
    "openAccessPdf,publicationDate,url"
)

# How far back (days) to look when querying Semantic Scholar / arXiv
LOOKBACK_DAYS = 3
