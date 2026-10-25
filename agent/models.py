import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()
# shortcut: local Ollama only, no cloud key needed; set OLLAMA_MODEL in .env to switch models
model = ChatOllama(model=os.getenv("OLLAMA_MODEL", "qwen3-coder:30b"), temperature=0)

# response = model.invoke("tell me something about the sun in 2 sentences")
# print(response.content)
