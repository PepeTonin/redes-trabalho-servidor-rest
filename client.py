import requests

URL = "http://127.0.0.1:8000"

print("\n -- MÉTODO POST -- ")
dadosEnviar = {"nome": "pedro henrique de avila tonin"}
respostaServidor = requests.post(f"{URL}/adicionar/nomes/", json=dadosEnviar)
print(respostaServidor.status_code)
print(respostaServidor.json())


print("\n -- MÉTODO GET -- ")
respostaServidor = requests.get(f"{URL}/tabela/nomes/")
print(f"STATUS CODE = {respostaServidor.status_code}")
conteudo = respostaServidor.json()
print("CONTEÚDO:")
print(conteudo)
