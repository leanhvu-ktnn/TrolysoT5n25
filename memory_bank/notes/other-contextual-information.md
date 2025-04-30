# Thông tin bối cảnh dự án

## 1. Môi trường phát triển
- Python 3.8+
- Virtual Environment
- Git
- IDE: VS Code, PyCharm
- OS: Windows, Linux, Mac

## 2. Các công nghệ sử dụng
- FastAPI
- pydantic-AI
- Groq API
- Streamlit
- SQLite
- Pydantic
- Rich

## 3. Cấu trúc dự án
```
TrolysoT5N25/
├── app/                    # Ứng dụng chính
├── components/            # Các thành phần độc lập
├── config/               # Cấu hình
├── tests/               # Unit tests
├── memory_bank/         # Thông tin tài liệu
├── logs/               # Log files
├── requirements.txt    # Dependencies
└── .gitignore
```

## 4. Quy trình phát triển
1. Tạo branch mới
2. Phát triển tính năng
3. Viết unit tests
4. Code review
5. Merge vào develop
6. Release

## 5. Các thành viên
- User duy nhất

## 6. Tài liệu tham khảo
- Groq API Documentation
- pydantic-AI Documentation
- FastAPI Documentation
- Streamlit Documentation
- Python Documentation

## 7. Các vấn đề đang gặp phải
1. Cần tối ưu hóa hiệu suất của Groq API
2. Cần cải thiện xử lý lỗi
3. Cần thêm unit tests
4. Cần cải thiện quản lý bộ nhớ

## 8. Kế hoạch phát triển
1. Hoàn thiện giao diện console
2. Tích hợp đầy đủ Groq API
3. Viết unit tests
4. Tối ưu hóa hiệu suất
5. Cải thiện xử lý lỗi
6. Cải thiện quản lý bộ nhớ

## 9. Các lưu ý quan trọng
1. Luôn cập nhật tài liệu khi thay đổi code
2. Kiểm tra kỹ trước khi merge code
3. Đảm bảo test coverage > 80%
4. Tuân thủ quy tắc code style
5. Sử dụng logging để debug

## 10. Các công cụ hỗ trợ
1. Git cho version control
2. pytest cho testing
3. black cho code formatting
4. isort cho import sorting
5. flake8 cho linting 