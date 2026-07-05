from fastapi import FastAPI
from backend.app.api.health import router as health_router

app = FastAPI(
    title="Enterprise Knowledge Assistant API",
    version="1.0.0",
    description="Backend API for the Enterprise Knowledge Assistant"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Enterprise Knowledge Assistant API is running!"
    }