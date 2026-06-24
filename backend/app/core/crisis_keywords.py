"""
crisis_keywords.py

Contains all crisis-related keywords and regex patterns
used by the Safety Service for crisis detection.

Keeping them in a separate file makes maintenance easier
and provides a single source of truth.
"""

# ------------------------------------------------------------------
# Exact keyword / phrase matching
# ------------------------------------------------------------------

CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "end my life",
    "want to die",
    "die",
    "self harm",
    "hurt myself",
    "cut myself",
    "overdose",
    "no reason to live",
    "life is pointless",
    "i want to disappear",
    "i can't take this anymore",
    "there is no point",
    "i wish i were dead",
    "better off dead",
    "everyone would be better off without me",
    "ending everything",
]

# ------------------------------------------------------------------
# Regex-based matching
# Handles extra spaces and small variations in phrasing
# ------------------------------------------------------------------

CRISIS_PATTERNS = [
    r"kill\s+myself",
    r"want\s+to\s+die",
    r"end\s+my\s+life",
    r"hurt\s+myself",
    r"cut\s+myself",
    r"no\s+reason\s+to\s+live",
    r"better\s+off\s+dead",
    r"wish\s+i\s+were\s+dead",
    r"better\s+off\s+without\s+me",
    r"ending\s+everything",
]