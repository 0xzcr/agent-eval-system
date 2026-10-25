import os

from deepeval.models import OllamaModel

# Same local Qwen model the agent uses, so evals never call a cloud API.
eval_model = OllamaModel(
    model=os.getenv("OLLAMA_MODEL", "qwen3-coder:30b"),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    temperature=0,
)
