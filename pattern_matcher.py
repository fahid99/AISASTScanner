import re
from config import SENSITIVE_API_IDENTIFIERS
from llm_scan import filename

AWS_KEY_REGEX = re.compile(r"(AKIA|ASIA)[0-9A-Z]{16}")

class PatternMatcher:
    def __init__(self):
            self.issues = []
            self.rules = [{
                   "id": "AWS.AccessKey",
                   "description": "Potential AWS Access Key ID",
                   "regex": re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")
            }]

    def scan_text(self, filename):
            if re.search(re.compile(r"(AKIA|ASIA)[0-9A-Z]{16"}), filename):
                    self.issues.append({
                    "recommendation": f"Do not hardcode your API key: {AWS_KEY_REGEX} into your source code. Store it in an environment variable or keep it in a secure secret manager."
                })