from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.api.routes.session import (
    router as session_router
)

from app.api.routes.message import (
    router as message_router
)

from app.api.routes.summary import (
    router as summary_router
)
from app.api.routes.export import (
    router as export_router
)

app = FastAPI(
    title="Empathetic Counselor API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    session_router,
    prefix="/api"
)

app.include_router(
    message_router,
    prefix="/api"
)

app.include_router(
    summary_router,
    prefix="/api"
)

app.include_router(
    export_router,
    prefix="/api"
)


@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }