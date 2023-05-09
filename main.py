from fastapi import FastAPI, Request
from banco.postMethods import *
from banco.getMethods import *

app = FastAPI()


# método post para adicionar um elemento a uma tabela
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


# método get para retornar valores de uma tabela
@app.get("/tabela/{tabelaReferencia}/")
async def mostrarElementos(tabelaReferencia: str):
    try:
        resposta = retornaTabela(tabelaReferencia)
        return resposta
    except:
        return "ERRO"


# método get para retornar valores de uma tabela especifica a partir de um id de nome especifico
@app.get("/tabela/{tabelaReferencia}/{idNome}/")
async def mostrarElementosIdEspecifico(tabelaReferencia: str, idNome: int):
    try:
        resposta = retornaTabelaIdNomeEspecifico(tabelaReferencia, idNome)
        return resposta
    except:
        return "ERRO"


# método get para retornar todos os dados cadastrados
@app.get("/todos-cadastros/")
async def mostrarTodosOsCadastros():
    try:
        resposta = retornaTodosCadastros()
        return resposta
    except:
        return "ERRO"
