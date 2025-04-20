# Hệ thống Định giá BĐS Đà Nẵng

## Yêu cầu hệ thống
- Docker 20.10+
- Docker Compose 2.20+

## Cài đặt
1. Clone repository
```bash
git clone https://github.com/your-repo/danang-realestate.git
cd danang-realestate

# Scale backend service
docker compose up -d --scale backend=4

# Xem logs thời gian thực
docker compose logs -f --tail=100

# Giám sát hiệu năng
docker stats

# Cập nhật không downtime
docker compose pull
docker compose up -d --force-recreate

## Cài đặt
1. Clone repository
```bash
git clone https://github.com/your-repo/danang-realestate.git
cd danang-realestate
```

2. Cấu hình môi trường
```bash
cp .env.example .env
# Cập nhật các giá trị trong .env
```

3. Khởi động hệ thống
```bash
docker compose up -d --build
```

4. Khởi tạo dữ liệu
```bash
docker compose exec backend python -m app.core.gis.init_danang
```

## API Endpoints
- `POST /api/v1/predict` - Dự đoán giá BĐS
- `GET /api/v1/properties` - Danh sách BĐS
```

Tất cả các file này cần được đặt đúng cấu trúc thư mục và chạy lệnh sau để triển khai:

```bash
docker compose build --no-cache && docker compose up -d
```

Hệ thống sẽ tự động:
1. Khởi tạo cơ sở dữ liệu
2. Nạp dữ liệu GIS Đà Nẵng
3. Khởi động các service với cấu hình production
4. Tạo SSL certificate tự động với Let's Encrypt

Truy cập https://your-domain.com để bắt đầu sử dụng ứng dụng.

