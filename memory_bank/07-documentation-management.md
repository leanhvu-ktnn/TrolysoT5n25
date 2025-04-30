# Quản lý Tài liệu Dự án

## Cấu trúc tài liệu
```
memory_bank/
├── 00-project-overview.md    # Tổng quan dự án
├── 01-architecture.md        # Kiến trúc hệ thống
├── 02-components.md          # Các thành phần
├── 03-development-process.md # Quy trình phát triển
├── 04-api-documentation.md   # Tài liệu API
├── 05-progress-log.md        # Nhật ký tiến độ
├── 06-environment-setup.md   # Thiết lập môi trường
└── 07-documentation-management.md # Quản lý tài liệu
```

## Quy trình làm việc với tài liệu

### 1. Tạo tài liệu mới
```bash
# Tạo file markdown mới
touch memory_bank/new-file.md

# Thêm nội dung cơ bản
echo "# Tiêu đề\n\n## Tổng quan" > memory_bank/new-file.md
```

### 2. Cập nhật tài liệu
```bash
# Đọc nội dung file
cat memory_bank/file.md

# Thêm nội dung mới
echo "\n\n## Nội dung mới" >> memory_bank/file.md

# Xóa nội dung cũ
> memory_bank/file.md
```

### 3. Di chuyển tài liệu
```bash
# Di chuyển file
mv memory_bank/old-location/file.md memory_bank/new-location/

# Copy file
cp memory_bank/source/file.md memory_bank/destination/
```

### 4. Quản lý version
```bash
# Kiểm tra trạng thái
git status

# Thêm file mới
git add memory_bank/new-file.md

# Commit thay đổi
git commit -m "docs: add new documentation"

# Push lên remote
git push origin main
```

## Quy tắc viết tài liệu

### 1. Cấu trúc file
```markdown
# Tiêu đề

## Tổng quan
Mô tả ngắn gọn về nội dung

## Chi tiết
Nội dung chi tiết

## Ví dụ
```python
# Code ví dụ
```

## API Reference
- Method 1: Mô tả
- Method 2: Mô tả
```

### 2. Quy ước đặt tên
- Sử dụng snake_case cho tên file
- Tên file phải rõ ràng, mô tả đúng nội dung
- Không sử dụng dấu cách trong tên file
- Đánh số thứ tự file theo thứ tự ưu tiên (00-, 01-, ...)

### 3. Formatting
- Sử dụng Markdown
- Code block phải có ngôn ngữ được chỉ định
- Sử dụng tiếng Việt cho nội dung
- Sử dụng tiếng Anh cho code và technical terms
- Sử dụng rich formatting cho CLI output

## Các lệnh hữu ích

### Tìm kiếm trong tài liệu
```bash
# Tìm từ khóa trong tất cả file .md
grep -r "từ khóa" memory_bank/*.md

# Tìm file chứa từ khóa
grep -l "từ khóa" memory_bank/*.md
```

### Kiểm tra cấu trúc
```bash
# Liệt kê tất cả file .md
ls -R memory_bank/*.md

# Kiểm tra file trùng lặp
find memory_bank -name "*.md" | sort | uniq -d
```

### Tự động hóa
```bash
# Tạo file tài liệu cho tất cả class trong components
for file in components/**/*.py; do
    doc_path="memory_bank/components/$(dirname "$file")/$(basename "$file" .py).md"
    mkdir -p "$(dirname "$doc_path")"
    echo "# $(basename "$file" .py)\n\n## Tổng quan" > "$doc_path"
done
```

## Cập nhật tài liệu

### 1. Khi thêm tính năng mới
- Cập nhật project-overview.md
- Cập nhật architecture.md
- Cập nhật components.md
- Cập nhật api-documentation.md
- Cập nhật progress-log.md

### 2. Khi sửa lỗi
- Cập nhật progress-log.md
- Cập nhật components.md nếu cần

### 3. Khi thay đổi cấu hình
- Cập nhật environment-setup.md
- Cập nhật components.md

### 4. Khi thay đổi quy trình
- Cập nhật development-process.md
- Cập nhật documentation-management.md 