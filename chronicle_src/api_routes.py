from fastapi import FastAPI, File, UploadFile, APIRouter
import pandas as pd
from numpy import ndarray
from pandas import DataFrame
from pandas.core.arrays import ExtensionArray

api_router = APIRouter(prefix="/api/v1")


@api_router.get("/taskSize")
def get_task_size():
    return {"message": "Hello taskSize"}


@api_router.post("/fetchColumns")
def create_upload_file(file: UploadFile):
    df: DataFrame = pd.read_csv(file.file)
    filtered = [x for x in df.columns.values if 'Unnamed' not in x]
    print(filtered)
    return filtered
