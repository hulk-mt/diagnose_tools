#!/usr/bin/python3
import sys
import pip
sys.argv = ['pip', 'install', 'fastapi', 'uvicorn', '--user']
pip.main()
from fastapi import FastAPI, Body, Request
from fastapi.responses import PlainTextResponse
import pickle
import uvicorn
app = FastAPI()
@app.post("/diagnose")
async def deserialize_data(data: bytes = Body(...)):
    try:
        global app
        obj = pickle.loads(data)
        return {"status": "ok"}
    except Exception as e:
        return {"error": str(e)}
@app.get("/")
async def home():
    return PlainTextResponse("ok")
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8419)
