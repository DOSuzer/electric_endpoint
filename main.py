import random

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/{item_id}")
def root(item_id):
    A = random.randint(0, 50)
    kW = 22
    return JSONResponse(content=jsonable_encoder(
        {"id": item_id, "A": str(A), "kW": str(kW)}
    ))
