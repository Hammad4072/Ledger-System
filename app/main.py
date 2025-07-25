from fastapi import FastAPI
from app.routers import auth_router, ledger_router

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(ledger_router.router)
