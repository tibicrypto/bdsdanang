# backend/app/core/security/limiter.py
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from redis.asyncio import Redis

async def init_limiter():
    redis = Redis.from_url("redis://redis:6379")
    await FastAPILimiter.init(redis)

limiter = RateLimiter(times=100, seconds=60)  # 100 requests/phút
