# Các Thành Phần Hệ Thống

## 1. User Interface Components

### 1.1. Web Interface
- **Streamlit App** (`app/web/app.py`)
  - Giao diện web chính
  - Hỗ trợ tương tác qua trình duyệt
  - Hiển thị kết quả dạng rich text và markdown
  - Tích hợp các widget tương tác
  - Quản lý session và state
  - Cách chạy: `streamlit run app/web/app.py`

### 1.2. Console Interface
- **CLI** (`app/console/cli.py`)
  - Giao diện dòng lệnh với Rich formatting
  - Hỗ trợ các lệnh cơ bản
  - Tích hợp với shell commands
  - Hiển thị kết quả dạng rich text
  - Quản lý lịch sử chat
  - Cách chạy: `python -m app.console.cli chat`

## 2. Agent Components

### 2.1. Base Agent
- **BaseAgent** (`components/agents/base_agent.py`)
  - Lớp cơ sở cho tất cả các agent
  - Kế thừa từ pydantic_ai.Agent
  - Tích hợp với Groq API
  - Quản lý lịch sử tương tác
  - Xử lý tin nhắn và trả về phản hồi
  - Các phương thức chính:
    - `process_input(input: str) -> str`: Xử lý input từ người dùng
    - `_make_request(messages: List[Dict]) -> str`: Gửi request đến Groq API
    - `get_history() -> List[Dict]`: Lấy lịch sử tương tác
    - `clear_history() -> None`: Xóa lịch sử tương tác
    - `get_status() -> Dict`: Lấy trạng thái của agent
  - Tính năng:
    - Xử lý lỗi tự động
    - Logging tích hợp
    - Quản lý message history
    - Tích hợp với Groq API
    - Quản lý token và context window

## 3. Model Components

### 3.1. Groq Integration
- **GroqModel** (`components/models/groq_model.py`)
  - Wrapper cho Groq API
  - Quản lý kết nối và tương tác
  - Hỗ trợ nhiều model khác nhau
  - Xử lý lỗi và retry
  - Quản lý rate limiting
  - Xử lý token và context window

## 4. MCP Components

### 4.1. File System Management
- **MCP** (`components/mcp/mcp.py`)
  - Quản lý hệ thống file
  - Xử lý các thao tác file
  - Quản lý quyền truy cập
  - Xử lý đồng bộ hóa

### 4.2. File System Operations
- **FileSystem** (`components/mcp/filesystem/`)
  - Các thao tác file cơ bản
  - Quản lý metadata
  - Xử lý versioning
  - Backup và restore

## 5. Configuration Components

### 5.1. Model Configuration
- **ModelConfig** (`config/models/model_config.py`)
  - Quản lý cấu hình model
  - Cung cấp cấu hình cho Groq API
  - Quản lý các tham số model
  - Xử lý validation

### 5.2. API Configuration
- **APIConfig** (`config/api/api_config.py`)
  - Quản lý cấu hình API
  - Cung cấp base URL và endpoints
  - Quản lý headers và authentication
  - Xử lý rate limiting

### 5.3. Logging Configuration
- **LogConfig** (`config/logging/log_config.py`)
  - Quản lý cấu hình logging
  - Cung cấp logger cho toàn hệ thống
  - Quản lý log levels và formats
  - Xử lý log rotation

### 5.4. App Configuration
- **AppConfig** (`config/app/app_config.py`)
  - Quản lý cấu hình ứng dụng
  - Cung cấp cấu hình cho web và console
  - Quản lý session và state
  - Xử lý environment variables
