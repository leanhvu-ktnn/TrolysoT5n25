"""
Package config chứa các cấu hình cho ứng dụng
"""

import os
from dotenv import load_dotenv

# Tải các biến môi trường từ file .env
load_dotenv()

# Cấu hình API Keys
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Cấu hình Google Drive
GOOGLE_DRIVE_PATH = os.getenv("GOOGLE_DRIVE_PATH")
GOOGLE_TOKEN_FILE = os.getenv("GOOGLE_TOKEN_FILE")
GOOGLE_CLIENT_PASSKEY = os.getenv("GOOGLE_CLIENT_PASSKEY")

# Cấu hình TVPL
TVPL_USER = os.getenv("TVPL_USER")
TVPL_PASS = os.getenv("TVPL_PASS")
TVPL_GOOGLE_DRIVE_PATH = os.getenv("TVPL_GOOGLE_DRIVE_PATH")
TVPL_DB_PATH = os.path.join(TVPL_GOOGLE_DRIVE_PATH, os.getenv("TVPL_DB_PATH"))
TVPL_DETAILHTML_PATH = os.path.join(TVPL_GOOGLE_DRIVE_PATH, os.getenv("TVPL_DETAILHTML_PATH"))
TVPL_VANBAN_RASOAT = os.path.join(TVPL_GOOGLE_DRIVE_PATH, os.getenv("TVPL_VANBAN_RASOAT"))
TVPL_CONGVAN_RASOAT = os.path.join(TVPL_GOOGLE_DRIVE_PATH, os.getenv("TVPL_CONGVAN_RASOAT"))
TVPL_TC_RASOAT = os.path.join(TVPL_GOOGLE_DRIVE_PATH, os.getenv("TVPL_TC_RASOAT"))

# Cấu hình ChromaDB
CHROMADB_PATH = os.path.join(TVPL_GOOGLE_DRIVE_PATH, os.getenv("CHROMADB_PATH"))
TOP_K_QUERY = int(os.getenv('TOP_K_QUERY', 5))
MIN_SIM = float(os.getenv('MIN_SIM', 0.7))

# Cấu hình Models
GROQ_LLAMA = os.getenv("GROQ_LLAMA")
OLLAMA_LLAMA = os.getenv("OLLAMA_LLAMA")
OLLAMA_QWEN = os.getenv("OLLAMA_QWEN")
OLLAMA_QWEN_CODER = os.getenv("OLLAMA_QWEN_CODER")
OLLAMA_QWEN_CODER_3B = os.getenv("OLLAMA_QWEN_CODER_3B")
OLLAMA_QWEN_CODER_1_5B = os.getenv("OLLAMA_QWEN_CODER_1_5B")
CODE_MODEL = GROQ_LLAMA

# Cấu hình Database
MEM_DB_PATH = os.path.join(TVPL_GOOGLE_DRIVE_PATH, os.getenv("MEM_DB_PATH"))
CHAT_DB_PATH = os.path.join(TVPL_GOOGLE_DRIVE_PATH, os.getenv("CHAT_DB_PATH"))

# Cấu hình Logging
LOG_DIRECTORY = os.getenv("LOG_DIRECTORY", "logs")
LOG_FORMAT = os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOG_CONFIG = {
    "level": os.getenv("LOG_LEVEL", "INFO"),
    "format": LOG_FORMAT,
    "filename": os.path.join(LOG_DIRECTORY, "app.log")
}

# Cấu hình MCP Filesystem
MCP_FILESYSTEM_DIR = os.getenv("MCP_FILESYSTEM_DIR")

# Cấu hình API
API_CONFIG = {
    "api_key": GROQ_API_KEY,
    "base_url": "https://api.groq.com/openai/v1"
}

# Cấu hình Model
MODEL_CONFIG = {
    "model": "llama-3.3-70b-versatile",
    "temperature": 0.7,
    "max_tokens": 4096
}

# Cấu hình Streamlit
STREAMLIT_CONFIG = {
    "page_title": "TrolysoT4N25",
    "page_icon": "🤖",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Cấu hình Database
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "database": os.getenv("DB_NAME", "trolyso"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "")
}

__all__ = [
    "TAVILY_API_KEY", "GROQ_API_KEY",
    "GOOGLE_DRIVE_PATH", "GOOGLE_TOKEN_FILE", "GOOGLE_CLIENT_PASSKEY",
    "TVPL_USER", "TVPL_PASS", "TVPL_GOOGLE_DRIVE_PATH", "TVPL_DB_PATH",
    "TVPL_DETAILHTML_PATH", "TVPL_VANBAN_RASOAT", "TVPL_CONGVAN_RASOAT",
    "TVPL_TC_RASOAT", "CHROMADB_PATH", "TOP_K_QUERY", "MIN_SIM",
    "GROQ_LLAMA", "OLLAMA_LLAMA", "OLLAMA_QWEN", "OLLAMA_QWEN_CODER",
    "OLLAMA_QWEN_CODER_3B", "OLLAMA_QWEN_CODER_1_5B", "CODE_MODEL",
    "MEM_DB_PATH", "CHAT_DB_PATH", "LOG_DIRECTORY", "LOG_FORMAT", "LOG_CONFIG"
]