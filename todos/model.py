from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form

class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(
            cls,
            item: str = Form(...)
    ):
        return cls(item=item)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Моя персональная задача от Камиля Рашитова"
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Обновлённая задача Камиля Рашитова"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Первая задача Камиля"},
                    {"item": "Вторая задача Камиля"}
                ]
            }
        }