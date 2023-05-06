from fastapi import FastAPI, Request
import json
from banco import *

app = FastAPI()


# @app.on_event("startup")
# async def carregarItensDB():
#     global db
#     conectarBanco()


# # métodos get
# @app.get("/")
# async def rootGet():

#     return json.dumps(dadosRecebidos, indent=4)


# métodos post
@app.post("/")
async def rootPost(request: Request):
    dadosRecebidos = await request.json()
    dadosToDict = dict()
    for key, value in dadosRecebidos.items():
        dadosToDict[key] = value
    enviarDadosAoBanco(dadosToDict)
    return dadosRecebidos
