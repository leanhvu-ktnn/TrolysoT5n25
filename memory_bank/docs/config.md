# Module Config

Module config được thiết kế để quản lý tất cả các cấu hình của hệ thống. Module này được tổ chức theo cấu trúc sau:

```
config/
├── __init__.py          # File chính chứa tất cả các biến cấu hình
├── models/              # Module quản lý cấu hình model
│   ├── __init__.py
│   └── model_config.py
├── database/            # Module quản lý cấu hình database
│   ├── __init__.py
│   └── db_config.py
├── logging/             # Module quản lý cấu hình logging
│   ├── __init__.py
│   └── log_config.py
└── app/                 # Module quản lý cấu hình ứng dụng
    ├── __init__.py
    └── app_config.py
```

## Cấu trúc và Chức năng

### 1. File __init__.py

File này chứa tất cả các biến cấu hình chính của hệ thống, bao gồm:

- Cấu hình API Keys
- Cấu hình Google Drive
- Cấu hình TVPL
- Cấu hình ChromaDB
- Cấu hình Models
- Cấu hình Database
- Cấu hình Logging
- Cấu hình MCP Filesystem
- Cấu hình API
- Cấu hình Model
- Cấu hình Streamlit

### 2. Module Models

Quản lý cấu hình cho các model AI:

```python
from config.models import ModelConfig

# Lấy cấu hình Groq
groq_config = ModelConfig.get_groq_config()

# Lấy cấu hình Ollama
ollama_config = ModelConfig.get_ollama_config()
```

### 3. Module Database

Quản lý cấu hình cho các database:

```python
from config.database import DatabaseConfig

# Lấy đường dẫn database TVPL
tvpl_db_path = DatabaseConfig.get_tvpl_db_path()

# Lấy đường dẫn database Memory
mem_db_path = DatabaseConfig.get_mem_db_path()

# Lấy đường dẫn database Chat
chat_db_path = DatabaseConfig.get_chat_db_path()

# Lấy cấu hình database
db_config = DatabaseConfig.get_db_config()
```

### 4. Module Logging

Quản lý cấu hình cho hệ thống logging:

```python
from config.logging import LogConfig

# Lấy cấu hình logging
log_config = LogConfig.get_log_config()
```

### 5. Module App

Quản lý cấu hình cho ứng dụng:

```python
from config.app import AppConfig

# Lấy cấu hình Streamlit
streamlit_config = AppConfig.get_streamlit_config()

# Lấy cấu hình API
api_config = AppConfig.get_api_config()

# Lấy cấu hình Model
model_config = AppConfig.get_model_config()
```

## Cách sử dụng

1. Import các module cấu hình cần thiết
2. Sử dụng các phương thức static để lấy cấu hình
3. Cấu hình được lấy từ biến môi trường hoặc giá trị mặc định

Ví dụ:

```python
from config.models import ModelConfig
from config.database import DatabaseConfig
from config.logging import LogConfig
from config.app import AppConfig

# Lấy các cấu hình cần thiết
groq_config = ModelConfig.get_groq_config()
db_path = DatabaseConfig.get_tvpl_db_path()
log_config = LogConfig.get_log_config()
streamlit_config = AppConfig.get_streamlit_config()
```

## Biến môi trường

Các biến môi trường cần được định nghĩa trong file `.env`:

```env
# API Keys
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key

# Google Drive
GOOGLE_DRIVE_PATH=your_google_drive_path
GOOGLE_TOKEN_FILE=your_token_file
GOOGLE_CLIENT_PASSKEY=your_client_passkey

# TVPL
TVPL_USER=your_tvpl_user
TVPL_PASS=your_tvpl_pass
TVPL_GOOGLE_DRIVE_PATH=your_tvpl_google_drive_path
TVPL_DB_PATH=your_tvpl_db_path
TVPL_DETAILHTML_PATH=your_tvpl_detailhtml_path
TVPL_VANBAN_RASOAT=your_tvpl_vanban_rasoat
TVPL_CONGVAN_RASOAT=your_tvpl_congvan_rasoat
TVPL_TC_RASOAT=your_tvpl_tc_rasoat

# ChromaDB
CHROMADB_PATH=your_chromadb_path
TOP_K_QUERY=5
MIN_SIM=0.7

# Models
GROQ_LLAMA=your_groq_llama
OLLAMA_LLAMA=your_ollama_llama
OLLAMA_QWEN=your_ollama_qwen
OLLAMA_QWEN_CODER=your_ollama_qwen_coder
OLLAMA_QWEN_CODER_3B=your_ollama_qwen_coder_3b
OLLAMA_QWEN_CODER_1_5B=your_ollama_qwen_coder_1_5b

# Database
MEM_DB_PATH=your_mem_db_path
CHAT_DB_PATH=your_chat_db_path
DB_HOST=localhost
DB_PORT=5432
DB_NAME=trolyso
DB_USER=postgres
DB_PASSWORD=your_db_password

# Logging
LOG_DIRECTORY=logs
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s
LOG_LEVEL=INFO

# MCP Filesystem
MCP_FILESYSTEM_DIR=your_mcp_filesystem_dir
``` 