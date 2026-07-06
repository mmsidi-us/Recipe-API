from app.config import settings
from app.routers import recipes
from fastapi import FastAPI

app = FastAPI(
    title= settings.app_name, description="Recipe API", 
    version="1.0.0")

app.include_router(recipes.router)
@app.get("/")
def root():
    return {"app": settings.app_name, "docs": "/docs"}