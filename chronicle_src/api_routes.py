from typing import Optional, Annotated

from fastapi import FastAPI, File, UploadFile, APIRouter, Request, Form, Depends
import pandas as pd
from numpy import ndarray
from pandas import DataFrame
from pandas.core.arrays import ExtensionArray
from pydantic import BaseModel
from devtools import debug

api_router = APIRouter(prefix="/api/v1")





@api_router.get("/taskSize")
def get_task_size():
    return {"message": "Hello taskSize"}


@api_router.post("/fetchColumns")
def fetch_columns(file: UploadFile):
    df: DataFrame = pd.read_csv(file.file)
    filtered = [x for x in df.columns.values if 'Unnamed' not in x]
    print(filtered)
    return filtered


@api_router.post("/task")
def create_task(
        connection_str: Optional[str] = Form(None),
        table_str: Optional[str] = Form(None),
        date_time_column: str = Form(...),
        data_column: str = Form(...),
        data_description: str = Form(...),
        date_time_column_desc: str = Form(...),
        data_column_desc: str = Form(...),
        window_size: Optional[str] = Form(None),
        continuous_data_flag: Optional[bool] = Form(False),
        file: UploadFile = File(...)):
    # df: DataFrame = pd.read_csv(file.file)
    # print(df.columns.values)
    print(connection_str, table_str, date_time_column, data_column, data_description, date_time_column_desc,
          data_column_desc, window_size, continuous_data_flag, file.filename)
    return "filtered"


@api_router.post("/task1")
async def create_task(request: Request):
    # df: DataFrame = pd.read_csv(file.file)
    # print(df.columns.values)
    form = await request.form()
    debug(form)
    return "filtered"


@api_router.post("/task2")
async def create_file(
        file: Annotated[bytes, File()],
        fileb: Annotated[UploadFile, File()],
        token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
