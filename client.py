import requests

URL = "http://127.0.0.1:8000"

print("\n -- MÉTODO POST -- ")
dadosEnviados = {"nome": "emanuelly cristhyna batista", "telefone": "(45)99977-0902"}
response = requests.post(f"{URL}/adicionar-contato/", json=dadosEnviados)
print(response.status_code)
print(response.json())


print("\n -- MÉTODO GET -- ")
response = requests.get(f"{URL}/agenda/")
print(f"STATUS CODE = {response.status_code}")
content = response.json()
print("CONTEÚDO:")
print(content)
