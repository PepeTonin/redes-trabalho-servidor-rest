from fastapi import FastAPI, Request
import json

app = FastAPI()

global resultado
resultado = dict()


# métodos get
@app.get("/")
async def rootGet():
    return json.dumps(resultado, indent=4)


# métodos post
@app.post("/")
async def rootPost(request: Request):
    dados = await request.json()
    global resultado
    for key, value in dados.items():
        resultado[key] = value
    return resultado
