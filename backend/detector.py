import re

def detect_sensitive_data(lines):
    findings = []

    email_pattern = r"[\w\.-]+@[\w\.-]+"
    password_pattern = r"password\s*=\s*\S+"
    api_pattern = r"sk-[a-zA-Z0-9]+"

    for i, line in enumerate(lines):
        if re.search(email_pattern, line):
            findings.append({"type": "email", "risk": "low", "line": i+1})

        if re.search(password_pattern, line):
            findings.append({"type": "password", "risk": "critical", "line": i+1})

        if re.search(api_pattern, line):
            findings.append({"type": "api_key", "risk": "high", "line": i+1})

    return findings