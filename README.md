# Local Command-Line Chatbot (Hugging Face)

A simple local chatbot that runs in your terminal using a small Hugging Face text-generation model (default: `distilgpt2`).

## Features
- Local Hugging Face Transformers text-generation
- Sliding memory window of recent turns (default: 4)
- Simple CLI: type messages; /exit to quit
- Modular code structure

## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Run
```bash
python interface.py --model distilgpt2 --window 4 --max-new-tokens 128 --temperature 0.7
```

## Example
```
User: What is the capital of France?
Bot: The capital of France is Paris.
User: And what about Italy?
Bot: The capital of Italy is Rome.
User: /exit
```
