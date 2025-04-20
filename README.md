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
