import os
from dotenv import load_dotenv
from openai import OpenAI

INSECURE_FUNCTIONS = {
    # Add insecure functions you want the scanner to look over
    "eval", "exec", "compile", "input",
    "os.system", "subprocess.call", "subprocess.Popen",
    "pickle.load", "yaml.load", "open"
}

INSECURE_MODULES = {
    # Add insecure modules you want the scanner to look over
    "random", "pickle"
}

SENSITIVE_API_IDENTIFIERS = {
    # Add API keys you want the scanner to look over
    "AWS_KEY_PREFIXES" : ["AKIA", "ASIA"]
}

# Loads OpenAI API key from .env
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Add your Python files you want the scanner to analyze
filename = 'sample.py'