from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.auth import auth_router
from app.db import mock_router
from app.transports import transport_router
from app.users import user_router
from app.documents import document_router
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Seu Projeto API",
        version="1.0.0",
        description="API com JWT Authentication",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(document_router.router, prefix="/documents", tags=["documents"])
app.include_router(mock_router.router, prefix="/mock", tags=["mock"])
app.include_router(transport_router.router, prefix="/transport", tags=["transport"])
