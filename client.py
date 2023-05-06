import requests

URL = "http://127.0.0.1:8000"

print("\n -- MÉTODO POST -- ")
dadosEnviar = {"nome": "emanuelly cristhyna batista", "telefone": "(45)99977-0902"}
respostaServidor = requests.post(f"{URL}/adicionar-contato/", json=dadosEnviar)
print(respostaServidor.status_code)
print(respostaServidor.json())


print("\n -- MÉTODO GET -- ")
respostaServidor = requests.get(f"{URL}/agenda/")
print(f"STATUS CODE = {respostaServidor.status_code}")
conteudo = respostaServidor.json()
print("CONTEÚDO:")
print(conteudo)
