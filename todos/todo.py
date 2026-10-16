from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from model import Todo, TodoItem, TodoItems
from fastapi.templating import Jinja2Templates



todo_router = APIRouter()
todo_list = []

templates = Jinja2Templates(directory="templates/")

# CREATE
@todo_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse(
        request=request,
        name="todo.html",
        context={"todos": todo_list}
    )

# READ all (с моделью ответа)
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="todo.html",
        context={"todos": todo_list}
    )


# READ one
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                request=request,
                name="todo.html",
                context={"todo": todo}
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

# UPDATE
@todo_router.put("/todo/{todo_id}")
@todo_router.post("/todo/{todo_id}")
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="ID задачи для обновления")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Камиль Рашитов: задача успешно обновлена!"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Камиль Рашитов: задача с таким ID не найдена"
    )

# DELETE one
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Камиль Рашитов: задача успешно удалена!"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Камиль Рашитов: задача с таким ID не найдена"
    )

# DELETE all
@todo_router.delete("/todo")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {
        "message": "Камиль Рашитов: все задачи успешно удалены!"
    }