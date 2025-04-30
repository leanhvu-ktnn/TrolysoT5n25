# BaseAgent

## Tổng quan
`BaseAgent` là lớp cơ sở cho tất cả các agent trong hệ thống, cung cấp các chức năng cơ bản cho việc tương tác với Groq API và quản lý lịch sử chat.

## Cấu trúc

### Import
```python
from typing import List, Dict, Optional, Any
import httpx
from config import GROQ_API_KEY, MODEL_CONFIG, API_CONFIG
from config.logging import LogConfig
import logging
import asyncio
import os
import json
```

### Constructor
```python
def __init__(
    self,
    model_name: Optional[str] = None,
    logger: Optional[logging.Logger] = None
)
```

#### Parameters
- `model_name` (Optional[str]): Tên model (mặc định lấy từ config)
- `logger` (Optional[logging.Logger]): Logger instance

#### Attributes
- `api_key` (str): API key cho Groq
- `logger` (logging.Logger): Logger instance
- `model` (str): Tên model đang sử dụng
- `message_history` (List[Dict]): Lịch sử các tin nhắn

## Các phương thức chính

### 1. _make_request
```python
async def _make_request(self, messages: List[Dict[str, str]]) -> str
```

Gửi request đến Groq API để lấy phản hồi từ model.

#### Parameters
- `messages` (List[Dict[str, str]]): Danh sách các tin nhắn

#### Returns
- `str`: Nội dung phản hồi từ model

#### Throws
- `Exception`: Khi có lỗi trong quá trình gọi API

### 2. process_input
```python
def process_input(self, user_input: str) -> str
```

Xử lý input từ người dùng và trả về phản hồi.

#### Parameters
- `user_input` (str): Input từ người dùng

#### Returns
- `str`: Phản hồi từ agent

#### Throws
- `Exception`: Khi có lỗi trong quá trình xử lý

### 3. get_history
```python
def get_history(self) -> List[Dict]
```

Lấy lịch sử chat.

#### Returns
- `List[Dict]`: Danh sách các tin nhắn trong lịch sử

### 4. clear_history
```python
def clear_history(self) -> None
```

Xóa toàn bộ lịch sử chat.

### 5. get_status
```python
def get_status(self) -> Dict
```

Lấy thông tin trạng thái của agent.

#### Returns
- `Dict`: Thông tin trạng thái bao gồm:
  - `model`: Tên model đang sử dụng
  - `history_length`: Số lượng tin nhắn trong lịch sử

## Cấu hình

### 1. API Configuration
- Base URL: `API_CONFIG['base_url']`
- Headers:
  - Authorization: Bearer {api_key}
  - Content-Type: application/json

### 2. Model Configuration
- Model name: `MODEL_CONFIG["model"]`
- Temperature: `MODEL_CONFIG["temperature"]`
- Max tokens: `MODEL_CONFIG["max_tokens"]`

## Xử lý lỗi

### 1. API Errors
- Kiểm tra status code của response
- Log lỗi và trả về thông báo lỗi cho người dùng

### 2. Processing Errors
- Bắt và xử lý các exception
- Log lỗi và trả về thông báo lỗi cho người dùng

## Ví dụ sử dụng

### 1. Khởi tạo agent
```python
from components.agents import BaseAgent

# Khởi tạo với model mặc định
agent = BaseAgent()

# Hoặc chỉ định model cụ thể
agent = BaseAgent(model_name="llama2-70b-4096")
```

### 2. Xử lý input
```python
# Gửi tin nhắn và nhận phản hồi
response = agent.process_input("Xin chào!")
print(response)
```

### 3. Quản lý lịch sử
```python
# Lấy lịch sử chat
history = agent.get_history()

# Xóa lịch sử
agent.clear_history()
```

### 4. Kiểm tra trạng thái
```python
# Lấy thông tin trạng thái
status = agent.get_status()
print(f"Model: {status['model']}")
print(f"Số tin nhắn: {status['history_length']}")
```

## Lưu ý khi sử dụng

1. Đảm bảo đã cấu hình đúng API key trong config
2. Kiểm tra kết nối internet trước khi sử dụng
3. Xử lý rate limiting của Groq API
4. Quản lý bộ nhớ khi lịch sử chat quá dài
5. Sử dụng logging để debug và theo dõi lỗi 