import re

PATTERNS = {
    "Emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",

    "Phone Numbers": r"\b(?:\+91[- ]?)?[6-9]\d{9}\b",

    "PAN Numbers": r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b",

    "Aadhaar Numbers": r"\b\d{4}\s?\d{4}\s?\d{4}\b",

    "Credit Card Numbers": r"\b(?:\d[ -]*?){13,16}\b",

    "Employee IDs": r"\bEMP[- ]?\d+\b",

    "API Keys": r"sk-[A-Za-z0-9]{10,}",

    "Passwords": r"(?i)(?:password|passwd|pwd)\s*[:=]\s*\S+",

    "Bank Account": r"\b\d{9,18}\b",

    "IFSC Code": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
}

BUSINESS_KEYWORDS = [
    "confidential",
    "internal use only",
    "trade secret",
    "salary",
    "financial forecast",
    "roadmap",
    "merger",
    "acquisition",
    "do not share",
]

def detect_sensitive_data(text):

    results = {}

    for label, pattern in PATTERNS.items():

        matches = re.findall(pattern, text)

        results[label] = list(set(matches))

    text_lower = text.lower()

    business_matches = []

    for keyword in BUSINESS_KEYWORDS:

        if keyword in text_lower:
            business_matches.append(keyword)

    results["Confidential Business Info"] = business_matches

    return results