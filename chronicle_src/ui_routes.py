from fastapi import APIRouter, Request
from starlette.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates


ui_router = APIRouter(prefix="/ui")
templates = Jinja2Templates(directory="templates")


@ui_router.get("/createTask")
def create_task():
    return FileResponse('public/createTask.html')


@ui_router.get("/tasks")
def get_all_tasks():
    return FileResponse('public/tasks.html')


@ui_router.get("/tasks/{task_id}", response_class=HTMLResponse)
def get_task(request: Request, task_id: int):
    return templates.TemplateResponse(name="task.html",
                                      context={"task_id": task_id, "request": request})
