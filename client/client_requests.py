import requests
import json

URL = "http://127.0.0.1:8000"


# método get para pedir os dados da tabela nomes
def getNomes():
    respostaServidor = requests.get(f"{URL}/tabela/nomes/")
    return json.loads(respostaServidor.json())


# método get para pedir dados de uma tabela especifica a partir de um id de nome específico
def getTabelaWhereIdNomeEspecificado(tabelaReferencia: str, idNome: int):
    respostaServidor = requests.get(f"{URL}/tabela/{tabelaReferencia}/{idNome}/")
    return json.loads(respostaServidor.json())


# método get para pedir todos os cadastros do banco
def getTodosOsCadastros():
    respostaServidor = requests.get(f"{URL}/todos-cadastros/")
    return json.loads(respostaServidor.json())


# método post para enviar dados à tabela de nomes
def postNomes(nome: str):
    dadosEnviar = {"nome": nome}
    requests.post(f"{URL}/adicionar/nomes/", json=dadosEnviar)


# método post para enviar dados à tabela de telefones
def postTelefones(idNome: int, telefone: str):
    dadosEnviar = {"idNome": idNome, "telefone": telefone}
    requests.post(f"{URL}/adicionar/telefones/", json=dadosEnviar)


# método post para enviar dados à tabela de enderecos
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
