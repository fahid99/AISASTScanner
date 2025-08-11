# AISASTScanner

AISASTScanner combines Python static analysis and large language model (LLM) scanning to find potential security issues in source code.

## Features
- Parses target files with an AST visitor to flag calls to insecure functions or modules defined in `config.py`.
- Sends the source code and AST findings to an OpenAI model for an additional vulnerability report in JSON format.

## Requirements
- Python 3.11+
- Dependencies listed in `requirements.txt`
- An OpenAI API key available in a `.env` file as `OPENAI_API_KEY`

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file and define `OPENAI_API_KEY` with your key.
3. Adjust `config.py` to set the file you want to analyze and customize insecure constructs.

## Usage
Run the scanner:
```bash
python main.py
```
The script analyzes the file specified in `config.py` and saves the LLM results to `llm_results.json`.

## Project Structure
- `ast_logic.py` – AST-based detection of insecure calls.
- `llm_scan.py` – OpenAI prompt construction and result handling.
- `config.py` – Configuration for insecure constructs and API settings.
- `sample.py` – Example Python file containing intentionally insecure patterns.


