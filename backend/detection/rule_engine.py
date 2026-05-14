import re
import unicodedata

# ---------- ABUSE ----------
ABUSIVE_WORDS = [
    "idiot", "stupid", "useless", "hate you", "nobody likes you",
    "worthless", "loser", "pathetic", "dumb", "fool",
    "moron", "trash", "garbage", "shut up",
    "you are nothing", "you are a joke", "disgusting",
    "ugly", "annoying", "good for nothing",
    "waste of space", "piece of crap", "jerk",
    "screw you", "get lost", "nonsense"
]

ABUSIVE_PATTERNS = [
    r"\bidiot\b",
    r"\bstupid\b",
    r"\bdumb\b",
    r"\bfool\b",
    r"\bmoron\b",
    r"\bloser\b",
    r"\bpathetic\b",
    r"shut up",
    r"get lost",
    r"screw you",
    r"waste of space",
    r"piece of crap"
]
# ---------- THREATS ----------
THREAT_PATTERNS = [
    r"kill you",
    r"hurt you",
    r"beat you",
    r"find you",
    r"ruin your life",
    r"serious consequences",
    r"you will regret",
    r"watch your back"
]

# ---------- GROOMING ----------
GROOMING_PATTERNS = [
    r"don'?t tell anyone",
    r"our secret",
    r"how old are you",
    r"send your photo",
    r"meet me alone",
    r"mature for your age",
    r"talk privately",
    r"just between us"
]

# ---------- BLACKMAIL ----------
BLACKMAIL_PATTERNS = [
    r"if you don'?t",
    r"i will expose",
    r"i will share your",
    r"do this or else",
    r"i have proof",
    r"i will leak",
    r"you have no choice"
]

# ---------- PHISHING / DATA REQUEST ----------
SENSITIVE_INFO_PATTERNS = [
    r"send (me )?(your )?(otp|password|pin|code)",
    r"share (your )?(otp|password|pin)",
    r"verify (your )?(account|details|identity)",
    r"enter your (password|details)",
    r"confirm your (account|information)",
    r"provide your (details|credentials)"
]

# ---------- LINK / SCAM ----------
LINK_PATTERNS = [
    r"http[s]?://",
    r"click (this )?link",
    r"open (this )?link"
]

# ---------- SOCIAL ENGINEERING ----------
SOCIAL_ENGINEERING_PATTERNS = [

    # Urgency
    (r"(urgent|respond now|act now|time is running out|immediately|without delay)",
     "Urgency / panic creation detected", 4, "urgency"),

    # Authority
    (r"(admin|administrator|security|support|it|official)\s+(team|staff|desk|department)",
     "Authority impersonation detected", 5, "authority"),

    # Secrecy
    (r"(keep this private|confidential|between us|do not tell anyone|stay quiet)",
     "Secrecy / isolation tactic detected", 4, "secrecy"),

    # Reward
    (r"(you are selected|special offer|won a reward|exclusive opportunity|bonus|prize)",
     "Reward-based manipulation detected", 4, "reward"),

    # Trust manipulation
    (r"(only you|i trust you|chosen you|i believe in you)",
     "Trust-building manipulation detected", 4, "trust"),

    # Emotional manipulation
    (r"(only you understand|i need you|you are special|i care about you)",
     "Emotional manipulation detected", 4, "emotion"),
]

# ---------- SAFE CONTEXT (NEW 🔥) ----------
SAFE_CONTEXT_PATTERNS = [
    r"no urgency",
    r"take your time",
    r"no rush",
    r"whenever you can",
]

# ==================================================
def rule_based_analysis(message):

    message = unicodedata.normalize("NFKD", message).lower()

    score = 0
    reasons = []
    matched_categories = set()

    # ---------- SAFE CONTEXT ----------
    for pattern in SAFE_CONTEXT_PATTERNS:
        if re.search(pattern, message):
            score -= 2

    # ---------- ABUSE (WORDS) ----------
    for word in ABUSIVE_WORDS:
        if word in message:
            score += 2
            reasons.append("Abusive language detected")
            break

    # ---------- ABUSE (PATTERNS) ----------
    for pattern in ABUSIVE_PATTERNS:
        if re.search(pattern, message):
            score += 3
            reasons.append("Abusive language detected")
            break

    # ---------- THREAT ----------
    for pattern in THREAT_PATTERNS:
        if re.search(pattern, message):
            score += 5
            reasons.append("Threat detected")
            break

    # ---------- GROOMING ----------
    for pattern in GROOMING_PATTERNS:
        if re.search(pattern, message):
            score += 6
            reasons.append("Grooming behaviour detected")
            break

    # ---------- BLACKMAIL ----------
    for pattern in BLACKMAIL_PATTERNS:
        if re.search(pattern, message):
            score += 6
            reasons.append("Blackmail attempt detected")
            break

    # ---------- SENSITIVE INFO ----------
    for pattern in SENSITIVE_INFO_PATTERNS:
        if re.search(pattern, message):
            score += 6
            reasons.append("Sensitive information request detected")
            break

    # ---------- LINK ----------
    for pattern in LINK_PATTERNS:
        if re.search(pattern, message):
            score += 3
            reasons.append("Suspicious link detected")
            break

    # ---------- SOCIAL ENGINEERING ----------
    for pattern, reason, weight, category in SOCIAL_ENGINEERING_PATTERNS:
        if re.search(pattern, message) and category not in matched_categories:
            score += weight
            reasons.append(reason)
            matched_categories.add(category)

    return score, list(set(reasons))
