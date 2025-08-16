from openai import OpenAI
from config import client, filename
from ast_logic import ast_scan
import json

def llm_scan():
    with open(filename, "r") as file:
        code = file.read()

    issues = ast_scan(code)
    issues_str = json.dumps(issues, indent=2)

    prompt = f"""You are a static application security testing (SAST) tool.
				Analyze the code and return the vulnerabilities found in JSON format.
				For each issue, include:
				- Type of vulnerability
				- Line number
				- Description
				- Recommendation or remediation code

				Here is the code:

				{code}

				Here are AST-detected function calls that may be insecure. Double check to reduce false positives:

				{issues_str}
				"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    output = response.output_text  # <- or use output.choices[0].message.content if needed

    with open("llm_results.json", "w") as f:
        f.write(output)

    print("LLM scan results saved to llm_results.json")
    print(output)

if __name__ == "__main__":
    llm_scan()
