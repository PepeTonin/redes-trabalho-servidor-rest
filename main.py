from fastapi import FastAPI, Request
from banco import *

app = FastAPI()


@app.get("/agenda/")
async def rootGet():
    agendaContatos = receberDadosDoBanco()
    return agendaContatos


@app.post("/adicionar-contato/")
async def rootPost(request: Request):
    dadosRecebidos = await request.json()
    dadosToDict = dict()
    for key, value in dadosRecebidos.items():
        dadosToDict[key] = value
    enviarDadosAoBanco(dadosToDict)
    return dadosRecebidos
