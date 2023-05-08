from fastapi import FastAPI, Request
from banco import *
from bancoHandler import *

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


@app.post("/adicionar/{tabelaReferencia}/")
async def adicionarElemento(request: Request, tabelaReferencia: str):
    try:
        dadosRecebidos = await request.json()
        dados_dict = dict()
        for key, value in dadosRecebidos.items():
            dados_dict[key] = value
        adicionarElementoNaTabela(dados_dict, tabelaReferencia)
        return dadosRecebidos
    except:
        return "ERRO"


@app.get("/tabela/{tabelaReferencia}/")
async def mostraElementos(tabelaReferencia: str):
    resposta = retornaTabela(tabelaReferencia)
    return resposta
