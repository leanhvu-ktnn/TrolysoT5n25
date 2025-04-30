# Quy Trình Phát Triển

## 1. Thiết Lập Môi Trường

### 1.1. Yêu Cầu Hệ Thống
- Python 3.8+
- Virtual Environment
- Git
- Các dependencies trong requirements.txt
- Groq API key

### 1.2. Cài Đặt
```bash
# Clone repository
git clone https://github.com/your-username/TrolysoT5N25.git
cd TrolysoT5N25

# Tạo và kích hoạt virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Cài đặt dependencies
pip install -r requirements.txt

# Cài đặt pre-commit hooks
pre-commit install

# Cấu hình biến môi trường
cp .env.example .env
# Điền GROQ_API_KEY vào file .env
```

## 2. Quy Trình Phát Triển

### 2.1. Tạo Branch Mới
- Tạo branch từ develop
- Đặt tên branch theo quy tắc: `feature/`, `bugfix/`, `hotfix/`
- Ví dụ: `feature/add-console-interface`

### 2.2. Phát Triển
1. Cập nhật memory_bank nếu cần
2. Phát triển code theo kiến trúc đã định
3. Viết unit tests
4. Chạy tests và kiểm tra lỗi
5. Format code
6. Commit code với message rõ ràng

### 2.3. Code Review
1. Tạo Pull Request
2. Đảm bảo CI/CD pass
3. Chờ review từ team
4. Sửa lỗi nếu có
5. Merge vào develop

## 3. Quy Tắc Code

### 3.1. Style Guide
- Tuân thủ PEP 8
- Sử dụng black để format code
- Sử dụng isort để sắp xếp imports
- Sử dụng flake8 để kiểm tra lỗi

### 3.2. Documentation
- Viết docstring cho tất cả các hàm
- Cập nhật tài liệu trong memory_bank
- Ghi chú rõ ràng các thay đổi

### 3.3. Testing
- Viết unit tests cho mọi chức năng mới
- Đảm bảo test coverage > 80%
- Chạy tests trước khi commit

## 4. Quy Trình Release

### 4.1. Chuẩn Bị Release
1. Tạo release branch từ develop
2. Tăng version number
3. Cập nhật CHANGELOG.md
4. Chạy tests và kiểm tra lỗi

### 4.2. Release
1. Merge vào main
2. Tạo tag
3. Deploy lên production
4. Merge main vào develop

## 5. Quy Trình Hỗ Trợ

### 5.1. Bug Fix
1. Tạo issue
2. Tạo branch fix
3. Sửa lỗi
4. Tạo PR
5. Review và merge

### 5.2. Feature Request
1. Tạo issue
2. Thảo luận yêu cầu
3. Lập kế hoạch triển khai
4. Phát triển và test
5. Review và merge

## Quy trình làm việc

### Quản lý code
- Sử dụng Git cho version control
- Branching strategy:
  - main: Branch chính
  - develop: Branch phát triển
  - feature/*: Các tính năng mới
  - bugfix/*: Sửa lỗi
  - hotfix/*: Sửa lỗi khẩn cấp

### Quy trình review code
1. Tạo pull request
2. Review code
3. Chạy CI/CD
4. Merge code

## Testing

### Unit Tests
- Sử dụng pytest
- Test coverage tối thiểu 80%
- Chạy test tự động trong CI/CD
- Test CLI: `python -m app.console.cli chat`
- Test Web: `streamlit run app/web/app.py`

### Integration Tests
- Test các thành phần tích hợp
- Test API endpoints
- Test database operations

## CI/CD Pipeline

### Build
- Kiểm tra cấu trúc code
- Chạy linter
- Build package

### Test
- Chạy unit tests
- Chạy integration tests
- Kiểm tra coverage

### Deploy
- Deploy lên staging
- Deploy lên production
- Rollback nếu cần

## Documentation

### Code Documentation
- Sử dụng docstrings
- Type hints
- Comments cho code phức tạp

### API Documentation
- OpenAPI/Swagger
- API endpoints
- Request/response examples

### Project Documentation
- README.md
- Architecture docs
- Development guides

## Quy tắc quản lý dự án

### Cấu trúc thư mục
- Tuân thủ nghiêm ngặt cấu trúc thư mục đã định nghĩa
- Không tạo file ở vị trí không đúng
- Mỗi file chỉ tồn tại ở một vị trí duy nhất

### Quản lý file
- Kiểm tra kỹ trước khi tạo file mới
- Không tạo file trùng lặp
- Xóa file cũ trước khi tạo file mới (nếu cần)
- Backup file trước khi thay đổi lớn

### Quy trình làm việc với file
1. Kiểm tra file đã tồn tại chưa
2. Xác định vị trí chính xác cho file
3. Backup file cũ (nếu cần)
4. Tạo/xóa file
5. Cập nhật import path
6. Kiểm tra tính nhất quán của code

### Kiểm soát thay đổi
- Mỗi thay đổi phải được review
- Không thực hiện nhiều thay đổi cùng lúc
- Test kỹ sau mỗi thay đổi
- Ghi log các thay đổi quan trọng

### Quy tắc đặt tên
- Tên file phải rõ ràng, mô tả đúng chức năng
- Tuân thủ quy ước đặt tên của Python
- Sử dụng snake_case cho tên file
- Tránh tên file quá dài hoặc không rõ nghĩa 