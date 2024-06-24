import os

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from chronicle_src.api_routes import api_router
from chronicle_src.ui_routes import ui_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(api_router)
app.include_router(ui_router)

app.mount("/public", StaticFiles(directory="public"), name="public")
app.mount("/ui/assets", StaticFiles(directory="public/assets"), name="assets")

@app.get("/")
def root():
    return RedirectResponse("ui/createTask")
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
