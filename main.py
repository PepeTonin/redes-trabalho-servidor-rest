from fastapi import FastAPI, Request
from banco.postMethods import *
from banco.getMethods import *

app = FastAPI()


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
