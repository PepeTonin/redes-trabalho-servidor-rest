import requests
import json

URL = "http://127.0.0.1:8000"


def getNomes():
    respostaServidor = requests.get(f"{URL}/tabela/nomes/")
    return json.loads(respostaServidor.json())


def getCadastrosPorNome(idNome: int):
    respostaServidor = requests.get(f"{URL}/dados-cadastrados/{idNome}/")
    return json.loads(respostaServidor.json())


def getTodosOsCadastros():
    respostaServidor = requests.get(f"{URL}/todos-cadastros/")
    return json.loads(respostaServidor.json())


def postNomes(nome: str):
    dadosEnviar = {"nome": nome}
    requests.post(f"{URL}/adicionar/nomes/", json=dadosEnviar)


def postTelefones(idNome: int, telefone: str):
    dadosEnviar = {"idNome": idNome, "telefone": telefone}
    requests.post(f"{URL}/adicionar/telefones/", json=dadosEnviar)


def postEnderecos(
    idNome: int, estado: str, cidade: str, bairro: str, rua: str, numero: int
):
    dadosEnviar = {
        "idNome": idNome,
        "estado": estado,
        "cidade": cidade,
        "bairro": bairro,
        "rua": rua,
        "numero": numero,
    }
    requests.post(f"{URL}/adicionar/enderecos/", json=dadosEnviar)
