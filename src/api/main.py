from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from predict import predict
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/result/")
async def result(request: Request):
    request_body = await request.body()
    request_body = request_body.decode('utf8').replace("'", '"')
    request_body = json.loads(request_body)
    data = request_body['data']
    prediction = predict(data)
    response = {
        "data": data,
        "category": prediction
    }
    return response


@app.get("/")
def index():
    return {"data": "OK"}
