# TrolysoT5N25

TrolysoT5N25 là một hệ thống AI assistant với khả năng tương tác và xử lý ngôn ngữ tự nhiên, sử dụng framework pydantic-AI cho các agent. Hệ thống có khả năng tương tác qua giao diện console và web, với các tính năng như chat, xử lý ngôn ngữ tự nhiên, và quản lý bộ nhớ.

## Tính năng chính

- Chat tương tác qua CLI và Web
- Hỗ trợ nhiều model LLM thông qua Groq API
- Quản lý bộ nhớ và lịch sử chat
- Xử lý ngôn ngữ tự nhiên
- Logging và monitoring

## Cài đặt

1. Clone repository:
```bash
git clone https://github.com/your-username/TrolysoT5N25.git
cd TrolysoT5N25
```

2. Tạo môi trường ảo:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. Cài đặt các package:
```bash
pip install -r requirements.txt
```

4. Tạo file `.env`:
```bash
cp .env.example .env
```

5. Cập nhật các biến môi trường trong file `.env`:
```env
# API Keys
GROQ_API_KEY=your_groq_api_key

# Models
MODEL_NAME=llama2-70b-4096
MODEL_TEMPERATURE=0.7
MODEL_MAX_TOKENS=4096

# API Configuration
API_BASE_URL=https://api.groq.com
API_TIMEOUT=30
API_RETRIES=3

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s
LOG_FILE=logs/app.log
```

## Sử dụng

### 1. Giao diện Console
```bash
# Chạy CLI
python -m app.console.cli chat

# Các lệnh cơ bản
- EXIT: Thoát ứng dụng
- CLEAR: Xóa lịch sử chat
- HELP: Hiển thị trợ giúp
```

### 2. Giao diện Web
```bash
# Chạy Streamlit
streamlit run app/web/app.py
```

## Phát triển

### 1. Cài đặt môi trường phát triển
```bash
pip install -r requirements-dev.txt
```

### 2. Chạy tests
```bash
pytest
```

### 3. Format code
```bash
black .
isort .
```

### 4. Kiểm tra lỗi
```bash
flake8
mypy .
```

## Cấu trúc dự án

```
TrolysoT5N25/
├── app/                    # Ứng dụng chính
│   ├── web/               # Giao diện web
│   └── console/           # Giao diện console
├── components/            # Các thành phần độc lập
│   ├── agents/           # Các agent AI
│   ├── models/           # Các model AI
│   └── mcp/              # Hệ thống quản lý file
├── config/               # Cấu hình
│   ├── models/          # Cấu hình model
│   ├── api/             # Cấu hình API
│   ├── logging/         # Cấu hình logging
│   └── app/             # Cấu hình ứng dụng
├── tests/               # Unit tests
├── memory_bank/         # Thông tin tài liệu
├── logs/               # Log files
├── requirements.txt    # Dependencies
└── .gitignore
```

## Tài liệu

Xem thêm tài liệu chi tiết trong thư mục `memory_bank/`:
- `00-project-overview.md`: Tổng quan dự án
- `01-architecture.md`: Kiến trúc hệ thống
- `02-components.md`: Các thành phần
- `03-development-process.md`: Quy trình phát triển
- `04-api-documentation.md`: Tài liệu API
- `05-progress-log.md`: Nhật ký tiến độ
- `06-environment-setup.md`: Thiết lập môi trường
- `07-documentation-management.md`: Quản lý tài liệu

## Giấy phép

MIT 