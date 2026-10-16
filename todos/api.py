from fastapi import FastAPI
from todo import todo_router

app = FastAPI(
    title="Todo API Камиль Рашитов",
    description="CRUD-приложение с моделями ответов и обработкой ошибок"
)

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Привет! Это Todo-приложение Камиль Рашитов"
    }

app.include_router(todo_router)