from .. import (
    GROQ_API_KEY, GROQ_LLAMA,
    OLLAMA_LLAMA, OLLAMA_QWEN,
    OLLAMA_QWEN_CODER, OLLAMA_QWEN_CODER_3B,
    OLLAMA_QWEN_CODER_1_5B
)

class ModelConfig:
    @staticmethod
    def get_groq_config() -> dict:
        return {
            "api_key": GROQ_API_KEY,
            "model": GROQ_LLAMA,
            "temperature": 0.7,
            "max_tokens": 4096
        }
    
    @staticmethod
    def get_openai_config() -> dict:
        return {
            "api_key": config.get("api.openai.api_key"),
            "model": config.get("api.openai.model"),
            "temperature": 0.7,
            "max_tokens": 4096
        }
    
    @staticmethod
    def get_ollama_config() -> dict:
        return {
            "llama": OLLAMA_LLAMA,
            "qwen": OLLAMA_QWEN,
            "qwen_coder": OLLAMA_QWEN_CODER,
            "qwen_coder_3b": OLLAMA_QWEN_CODER_3B,
            "qwen_coder_1_5b": OLLAMA_QWEN_CODER_1_5B
        } 