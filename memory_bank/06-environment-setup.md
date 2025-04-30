# Thiết Lập Môi Trường

## 1. Yêu Cầu Hệ Thống

### 1.1. Phần Cứng
- CPU: Intel Core i5 trở lên
- RAM: 8GB trở lên
- Ổ cứng: 20GB trống

### 1.2. Phần Mềm
- Python 3.8+
- Git
- Virtual Environment
- IDE (VS Code, PyCharm)

## 2. Cài Đặt Môi Trường

### 2.1. Cài Đặt Python
```bash
# Windows
winget install Python.Python.3.8

# Linux
sudo apt update
sudo apt install python3.8 python3.8-venv

# Mac
brew install python@3.8
```

### 2.2. Cài Đặt Git
```bash
# Windows
winget install Git.Git

# Linux
sudo apt install git

# Mac
brew install git
```

### 2.3. Tạo Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2.4. Quản Lý Virtual Environment

#### 2.4.1. Kích Hoạt Môi Trường
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

#### 2.4.2. Thoát Môi Trường
```bash
deactivate
```

#### 2.4.3. Cài Đặt Dependencies
```bash
# Cài đặt từ requirements.txt
pip install -r requirements.txt

# Cài đặt package mới
pip install <package_name>

# Cập nhật requirements.txt
pip freeze > requirements.txt
```

#### 2.4.4. Kiểm Tra Môi Trường
```bash
# Kiểm tra đường dẫn môi trường
python -c "import sys; print(sys.prefix)"

# Kiểm tra các package đã cài đặt
pip list
```

#### 2.4.5. Lưu Ý
- Thư mục `venv/` đã được thêm vào `.gitignore`
- Không commit thư mục `venv/` vào repository
- Mỗi developer cần tạo môi trường ảo riêng
- Cập nhật `requirements.txt` khi thêm/xóa package

### 2.5. Cài Đặt IDE
- VS Code: https://code.visualstudio.com/
- PyCharm: https://www.jetbrains.com/pycharm/

## 3. Thiết Lập Dự Án

### 3.1. Clone Repository
```bash
git clone https://github.com/your-username/TrolysoT5N25.git
cd TrolysoT5N25
```

### 3.2. Cài Đặt Dependencies
```bash
pip install -r requirements.txt
```

### 3.3. Cài Đặt Pre-commit Hooks
```bash
pre-commit install
```

## 4. Cấu Hình Biến Môi Trường

### 4.1. Tạo File .env
```bash
cp .env.example .env
```

### 4.2. Cấu Hình Các Biến
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

### 4.3. Cấu Trúc Module Config
Module config được tổ chức theo cấu trúc sau:

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

### 4.4. Cách Sử Dụng Module Config
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

## 5. Kiểm Tra Cài Đặt

### 5.1. Chạy Tests
```bash
pytest
```

### 5.2. Chạy Ứng Dụng
```bash
# Web Interface
streamlit run app/web/app.py

# Console Interface
python -m app.console.cli chat
```

## 6. Xử Lý Sự Cố

### 6.1. Lỗi Thường Gặp
1. Lỗi thiếu dependencies
   - Giải pháp: `pip install -r requirements.txt`

2. Lỗi biến môi trường
   - Giải pháp: Kiểm tra file .env

3. Lỗi không chạy được CLI
   - Giải pháp: Kiểm tra đường dẫn và quyền thực thi

4. Lỗi Groq API
   - Giải pháp: Kiểm tra API key và rate limiting

### 6.2. Hỗ Trợ
- Tạo issue trên GitHub
- Liên hệ qua email
- Tham khảo tài liệu trong memory_bank 