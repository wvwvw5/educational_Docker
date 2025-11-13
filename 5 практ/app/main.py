import asyncio
import os
import random
import time
from typing import Dict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Gauge, Histogram, generate_latest

app = FastAPI(title="Demo monitored service", version="1.0.0")

REQUEST_COUNT = Counter(
    "app_http_requests_total",
    "Количество HTTP-запросов",
    labelnames=("method", "endpoint", "http_status"),
)
REQUEST_LATENCY = Histogram(
    "app_http_request_duration_seconds",
    "Продолжительность обработки HTTP-запросов",
    labelnames=("endpoint",),
    buckets=(0.05, 0.1, 0.3, 0.5, 1, 2, 3, 5),
)
IN_PROCESS_TASKS = Gauge(
    "app_inflight_requests",
    "Количество запросов, находящихся в обработке",
)

ACTIVE_USERS = Gauge(
    "app_active_users",
    "Текущее количество активных пользователей",
)
DB_SIZE_MB = Gauge(
    "app_database_size_megabytes",
    "Размер базы данных в мегабайтах",
)
CACHE_HIT_RATIO = Gauge(
    "app_cache_hit_ratio",
    "Доля попаданий в кеш",
)
ORDERS_PROCESSED = Counter(
    "app_orders_processed_total",
    "Всего обработано заказов",
)
BUSINESS_ERRORS = Counter(
    "app_business_errors_total",
    "Количество бизнес-ошибок",
    labelnames=("error_type",),
)

RANDOM_USERS = ["alice", "bob", "carol", "dave", "erin", "frank", "grace"]


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.perf_counter()
    IN_PROCESS_TASKS.inc()
    try:
        response = await call_next(request)
        return response
    finally:
        elapsed = time.perf_counter() - start
        endpoint = request.url.path
        REQUEST_LATENCY.labels(endpoint=endpoint).observe(elapsed)
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=endpoint,
            http_status=getattr(request.state, "status_code", getattr(response, "status_code", 500)),
        ).inc()
        IN_PROCESS_TASKS.dec()


@app.middleware("http")
async def capture_status_code(request: Request, call_next):
    response = await call_next(request)
    request.state.status_code = response.status_code
    return response


@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_running_loop()
    loop.create_task(simulate_metrics())


async def simulate_metrics():
    db_size = 512.0
    cache_ratio = 0.8

    while True:
        current_users = ACTIVE_USERS._value.get()
        active_users = max(0, int(current_users * 0.9 + random.randint(-5, 10)))
        db_size = max(100.0, DB_SIZE_MB._value.get() + random.uniform(-5.0, 8.0))
        cache_ratio = min(0.99, max(0.4, CACHE_HIT_RATIO._value.get() + random.uniform(-0.05, 0.05)))

        ACTIVE_USERS.set(active_users)
        DB_SIZE_MB.set(round(db_size, 2))
        CACHE_HIT_RATIO.set(round(cache_ratio, 4))

        if random.random() < 0.4:
            ORDERS_PROCESSED.inc(random.randint(1, 4))

        if random.random() < 0.1:
            err_type = random.choice(["payment", "validation", "internal"])
            BUSINESS_ERRORS.labels(error_type=err_type).inc()

        await asyncio.sleep(5)


@app.get("/")
async def read_root() -> Dict[str, str]:
    return {
        "service": "demo-monitoring-app",
        "status": "ok",
        "active_users": str(int(ACTIVE_USERS._value.get())),
    }


@app.post("/orders")
async def create_order(payload: Dict[str, str]):
    customer = payload.get("customer") or random.choice(RANDOM_USERS)
    value = float(payload.get("amount", random.uniform(10, 200)))

    ORDERS_PROCESSED.inc()
    ACTIVE_USERS.set(max(ACTIVE_USERS._value.get(), 1))

    if value > 150 and random.random() < 0.2:
        BUSINESS_ERRORS.labels(error_type="fraud_suspected").inc()
        return JSONResponse(
            status_code=409,
            content={"status": "rejected", "reason": "fraud_suspected", "customer": customer},
        )

    return {"status": "accepted", "customer": customer, "amount": value}


@app.get("/healthz")
async def healthcheck():
    return {"status": "healthy"}


@app.get("/metrics")
async def metrics() -> PlainTextResponse:
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/simulate/load")
async def simulate_load(multiplier: float = 1.0):
    added_users = max(1, int(5 * multiplier))
    ACTIVE_USERS.inc(added_users)
    DB_SIZE_MB.inc(2.5 * multiplier)
    CACHE_HIT_RATIO.set(max(0.1, CACHE_HIT_RATIO._value.get() - 0.05 * multiplier))
    REQUEST_LATENCY.labels(endpoint="/simulate/load").observe(0.2 * multiplier)
    return {"status": "load_increased", "by": added_users}


@app.post("/simulate/error")
async def simulate_error(error_type: str = "manual_test"):
    BUSINESS_ERRORS.labels(error_type=error_type).inc()
    return {"status": "error_recorded", "type": error_type}


@app.post("/simulate/reset")
async def simulate_reset():
    ACTIVE_USERS.set(5)
    CACHE_HIT_RATIO.set(0.85)
    return {"status": "reset"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", "8000")),
        reload=bool(os.getenv("APP_RELOAD", "0") == "1"),
    )
