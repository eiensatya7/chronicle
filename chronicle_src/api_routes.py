from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")


@api_router.get("/taskSize")
def get_task_size():
    return {"message": "Hello taskSize"}
