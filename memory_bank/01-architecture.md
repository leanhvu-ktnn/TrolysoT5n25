# Kiến trúc hệ thống

## Tổng quan kiến trúc
Hệ thống được xây dựng theo mô hình microservices với các thành phần chính:

1. User Interface:
   - Web Interface (Streamlit): Giao diện người dùng web
   - Console Interface: Giao diện dòng lệnh với Rich formatting
2. Agent System: Hệ thống các agent AI dựa trên pydantic-AI
3. LLM Integration: Kết nối với Groq API (LLM provider chính)
4. Configuration System: Quản lý cấu hình tập trung
5. Memory System: Quản lý bộ nhớ và lịch sử tương tác

## Các thành phần chính

### User Interface
- Web Interface (`app/web/`):
  - Streamlit App: Giao diện web trực quan
  - Hỗ trợ tương tác qua trình duyệt
  - Hiển thị kết quả dạng rich text và markdown
  - Tích hợp các widget tương tác
  - Quản lý session và state

- Console Interface (`app/console/`):
  - Giao diện dòng lệnh với Rich formatting
  - Hỗ trợ tương tác qua terminal
  - Hiển thị kết quả dạng rich text
  - Tích hợp với shell commands
  - Quản lý lịch sử chat

### Agent System
- Base Agent (`components/agents/base_agent.py`):
  - Kế thừa từ pydantic_ai.Agent
  - Cung cấp các chức năng cơ bản cho tất cả các agent
  - Quản lý lịch sử tương tác
  - Xử lý tin nhắn và trả về phản hồi
  - Tích hợp với Groq API
  - Quản lý logging và error handling

### LLM Integration
- Groq Model Integration (`components/models/groq_model.py`):
  - Wrapper cho Groq API
  - Xử lý kết nối và tương tác với Groq
  - Quản lý cấu hình model
  - Hỗ trợ các model khác nhau
  - Xử lý rate limiting và retry
  - Quản lý token và context window

### Configuration System
Module config được thiết kế để quản lý tất cả các cấu hình của hệ thống:

```
config/
├── __init__.py          # File chính chứa tất cả các biến cấu hình
├── models/              # Module quản lý cấu hình model
│   ├── __init__.py
│   └── model_config.py
├── api/                 # Module quản lý cấu hình API
│   ├── __init__.py
│   └── api_config.py
├── logging/             # Module quản lý cấu hình logging
│   ├── __init__.py
│   └── log_config.py
└── app/                 # Module quản lý cấu hình ứng dụng
    ├── __init__.py
    └── app_config.py
```

Các thành phần chính của Configuration System:

1. Environment Variables (`.env`):
   - Các biến môi trường cho API keys
   - Cấu hình đường dẫn và thư mục
   - Cấu hình logging và monitoring

2. Module Config:
   - Quản lý cấu hình tập trung
   - Tổ chức theo chức năng (models, api, logging, app)
   - Cung cấp interface thống nhất để truy cập cấu hình
   - Hỗ trợ giá trị mặc định cho các cấu hình

3. Cách sử dụng:
```python
from config.models import MODEL_CONFIG
from config.api import API_CONFIG
from config.logging import LogConfig
from config.app import APP_CONFIG

# Lấy các cấu hình cần thiết
model_config = MODEL_CONFIG
api_config = API_CONFIG
log_config = LogConfig.get_log_config()
app_config = APP_CONFIG
```

## Luồng dữ liệu
1. Người dùng tương tác qua:
   - Web Interface (Streamlit) hoặc
   - Console Interface
2. Interface gửi request đến Base Agent
3. Base Agent xử lý request và tương tác với Groq API
4. Kết quả được trả về cho người dùng qua interface tương ứng
5. Lịch sử tương tác được lưu trữ và quản lý

## Bảo mật
- Quản lý API key thông qua biến môi trường
- Mã hóa dữ liệu nhạy cảm
- Giới hạn truy cập API
- Xử lý lỗi và exception
- Logging và monitoring

## Kiến trúc thư mục
```
TrolysoT5N25/
├── app/                    # Ứng dụng chính
│   ├── web/               # Giao diện web
│   │   └── app.py
│   └── console/           # Giao diện console
│       ├── cli.py         # Command Line Interface
│       └── commands/      # Các lệnh console
│
├── components/            # Các thành phần độc lập
│   ├── agents/           # Các agent AI
│   │   └── base_agent.py
│   │
│   ├── models/           # Các model AI
│   │   └── groq_model.py
│   │
│   └── mcp/              # Hệ thống quản lý file
│       ├── mcp.py
│       └── filesystem/
│
├── config/               # Cấu hình
│   ├── __init__.py      # File cấu hình chính
│   ├── models/          # Cấu hình model
│   ├── api/             # Cấu hình API
│   ├── logging/         # Cấu hình logging
│   └── app/             # Cấu hình ứng dụng
│
├── tests/               # Unit tests
│   ├── test_agents/
│   ├── test_models/
│   └── test_mcp/
│
├── memory_bank/         # Thông tin tài liệu hệ thống
│   ├── notes/          # Ghi chú nhiệm vụ
│   └── docs/           # Tài liệu chi tiết
│
├── logs/               # Log files
│
├── requirements.txt    # Dependencies
└── .gitignore
```

## Quy tắc cấu trúc thư mục
1. Mỗi thành phần chính được tổ chức trong thư mục riêng
2. Tài liệu và ghi chú được lưu trữ trong memory_bank
3. Cấu hình được quản lý tập trung trong thư mục config
4. Tests được tổ chức theo cấu trúc tương tự với code chính
5. Giao diện người dùng được tách biệt thành web và console
6. Logging và monitoring được quản lý tập trung