# Tổng quan dự án

## Tên dự án
TrolysoT5N25

## Mô tả
Dự án phát triển hệ thống AI assistant với khả năng tương tác và xử lý ngôn ngữ tự nhiên, sử dụng framework pydantic-AI cho các agent. Hệ thống có khả năng tương tác qua giao diện console và web, với các tính năng như chat, xử lý ngôn ngữ tự nhiên, và quản lý bộ nhớ.

## Các thành viên chính
- User duy nhất

## Công nghệ sử dụng
- Python 3.8+
- FastAPI
- pydantic-AI (Framework chính cho các agent)
- Groq API (LLM provider chính)
- Streamlit (Ứng dụng Web)
- SQLite (Cơ sở dữ liệu)
- Pydantic (Validation và serialization)
- Rich (CLI formatting)

## Cấu trúc thư mục
- memory_bank: Chứa toàn bộ thông tin về tài liệu của hệ thống
  - notes: Ghi chú nhiệm vụ và tài liệu tham khảo
  - docs: Tài liệu chi tiết từng module, class của dự án
- components/: Chứa các thành phần chính của hệ thống
  - agents/: Các agent AI (dựa trên pydantic-AI)
  - models/: Các mô hình ngôn ngữ
  - mcp/: Các thành phần MCP
- tests/: Chứa các test case
- config/: Các file cấu hình
  - models/: Cấu hình model
  - api/: Cấu hình API
  - logging/: Cấu hình logging
- app/: Chứa ứng dụng
  - console/: Ứng dụng CLI
  - web/: Ứng dụng web (Streamlit)

## Hướng dẫn bắt đầu
1. Cài đặt các dependencies: `pip install -r requirements.txt`
2. Cấu hình biến môi trường: Copy .env.example thành .env và điền các thông tin cần thiết
3. Chạy ứng dụng CLI: `python -m app.console.cli chat`
4. Chạy ứng dụng Web: `streamlit run app/web/app.py`

## Tính năng chính
- Chat tương tác qua CLI và Web
- Hỗ trợ nhiều model LLM thông qua Groq API
- Quản lý bộ nhớ và lịch sử chat
- Xử lý ngôn ngữ tự nhiên
- Logging và monitoring 