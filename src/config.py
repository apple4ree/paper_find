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
    ],
    "ICLR": [
        "ICLR",
        "International Conference on Learning Representations",
    ],
    "CVPR": [
        "CVPR",
        "Computer Vision and Pattern Recognition",
        "IEEE/CVF Conference",
        "IEEE Conference on Computer Vision",
    ],
    "KDD": [
        "KDD",
        "Knowledge Discovery and Data Mining",
        "ACM SIGKDD",
        "SIGKDD",
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
        "agent workflow",
        "agent planning",
        "agent reasoning",
        "tool-calling",
        "function calling",
        "react agent",
        "agent framework",
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
    "q-fin.TR", # Trading and Market Microstructure
    "q-fin.PM", # Portfolio Management
    "q-fin.RM", # Risk Management
    "q-fin.ST", # Statistical Finance
]

# Semantic Scholar fields to retrieve
SS_FIELDS = (
    "title,abstract,authors,year,venue,externalIds,"
    "openAccessPdf,publicationDate,url"
)

# How far back (days) to look when querying Semantic Scholar / arXiv
LOOKBACK_DAYS = 7
