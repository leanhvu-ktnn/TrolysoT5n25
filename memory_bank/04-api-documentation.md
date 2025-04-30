# Tài Liệu API

## 1. API Endpoints

### 1.1. Chat API
```python
POST /api/v1/chat
```
- **Mô tả**: Gửi tin nhắn chat và nhận phản hồi
- **Request Body**:
  ```json
  {
    "message": "string",
    "model": "string",  // "groq:llama2-70b-4096" hoặc model khác
    "stream": boolean
  }
  ```
- **Response**:
  ```json
  {
    "response": "string",
    "model": "string",
    "timestamp": "string"
  }
  ```

### 1.2. Console API
```python
POST /api/v1/console
```
- **Mô tả**: Thực thi lệnh console
- **Request Body**:
  ```json
  {
    "command": "string",
    "args": ["string"]
  }
  ```
- **Response**:
  ```json
  {
    "output": "string",
    "status": "string",
    "timestamp": "string"
  }
  ```

### 1.3. CLI Interface
```bash
# Chạy CLI
python -m app.console.cli chat
```
- **Mô tả**: Giao diện dòng lệnh với Rich formatting
- **Output**: Hiển thị kết quả dạng rich text
- **Cách sử dụng**: Chạy trực tiếp từ terminal

## 2. Model APIs

### 2.1. Groq API
```python
class GroqModel:
    async def generate(self, prompt: str, **kwargs) -> str:
        """
        Tạo phản hồi từ Groq
        
        Args:
            prompt (str): Prompt cần xử lý
            **kwargs: Các tham số bổ sung
                - model (str): Tên model
                - temperature (float): Nhiệt độ sampling
                - max_tokens (int): Số token tối đa
                
        Returns:
            str: Phản hồi từ model
        """
        pass

    async def stream(self, prompt: str, **kwargs) -> AsyncGenerator:
        """
        Stream phản hồi từ Groq
        
        Args:
            prompt (str): Prompt cần xử lý
            **kwargs: Các tham số bổ sung
                - model (str): Tên model
                - temperature (float): Nhiệt độ sampling
                - max_tokens (int): Số token tối đa
                
        Returns:
            AsyncGenerator: Stream phản hồi
        """
        pass
```

## 3. Agent APIs

### 3.1. Base Agent
```python
class BaseAgent(Agent):
    """
    Lớp cơ sở cho tất cả các agent
    Kế thừa từ PydanticAI Agent với các tính năng mở rộng
    """
    
    def __init__(
        self,
        model_name: Optional[str] = None,
        logger: Optional[logging.Logger] = None
    ):
        """
        Khởi tạo BaseAgent
        
        Args:
            model_name (Optional[str]): Tên model (mặc định lấy từ config)
            logger (Optional[logging.Logger]): Logger instance
        """
        pass
        
    def process_input(self, user_input: str) -> str:
        """
        Xử lý input từ người dùng
        
        Args:
            user_input (str): Input từ người dùng
            
        Returns:
            str: Phản hồi từ agent
        """
        pass
        
    async def _make_request(self, messages: List[Dict[str, str]]) -> str:
        """
        Gửi request đến Groq API
        
        Args:
            messages (List[Dict[str, str]]): Danh sách các message
            
        Returns:
            str: Response từ model
        """
        pass
        
    def get_history(self) -> List[Dict]:
        """
        Lấy lịch sử tương tác
        
        Returns:
            List[Dict]: Danh sách các tương tác
        """
        pass
        
    def clear_history(self) -> None:
        """
        Xóa lịch sử tương tác
        """
        pass
        
    def get_status(self) -> Dict:
        """
        Lấy trạng thái của agent
        
        Returns:
            Dict: Thông tin trạng thái
        """
        pass
```

## 4. Error Handling

### 4.1. Error Codes
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

### 4.2. Error Response
```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": "string"
  }
}
```

## 5. Authentication

### 5.1. API Key
- Sử dụng API key trong header
- Format: `Authorization: Bearer <api_key>`
- Lấy từ biến môi trường `GROQ_API_KEY`

### 5.2. Rate Limiting
- 100 requests/minute
- 1000 requests/hour
- 10000 requests/day

## 6. Configuration

### 6.1. Model Configuration
```python
MODEL_CONFIG = {
    "model": "llama2-70b-4096",
    "temperature": 0.7,
    "max_tokens": 4096
}
```

### 6.2. API Configuration
```python
API_CONFIG = {
    "base_url": "https://api.groq.com",
    "timeout": 30,
    "retries": 3
}
```

### 6.3. Logging Configuration
```python
LOG_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/app.log"
}
```
