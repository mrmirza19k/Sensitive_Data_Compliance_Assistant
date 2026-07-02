def calculate_risk(sensitive_data):

    weights = {
        "Emails": 1,
        "Phone Numbers": 2,
        "PAN Numbers": 5,
        "Aadhaar Numbers": 5,
        "Credit Card Numbers": 8,
        "Employee IDs": 2,
        "API Keys": 10,
        "Passwords": 10,
        "Bank Account": 6,
        "IFSC Code": 2,
        "Confidential Business Info": 5,
    }

    score = 0
    reasons = []

    for category, weight in weights.items():

        count = len(sensitive_data.get(category, []))

        if count > 0:
            score += count * weight
            reasons.append(f"{count} {category}")

    if score <= 10:
        level = "Low"

    elif score <= 25:
        level = "Medium"

    else:
        level = "High"

    return {
        "score": score,
        "level": level,
        "reasons": reasons,
    }