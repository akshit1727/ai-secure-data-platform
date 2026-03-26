def generate_insights(findings):
    insights = []

    types = [f["type"] for f in findings]

    if "password" in types:
        insights.append("Sensitive credentials exposed in logs")

    if "api_key" in types:
        insights.append("API key detected - potential security risk")

    if "email" in types:
        insights.append("User email found in logs (PII exposure)")

    if len(findings) > 3:
        insights.append("Multiple sensitive entries detected")

    return insights