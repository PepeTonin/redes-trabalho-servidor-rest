import requests

URL = "http://127.0.0.1:8000"

# POST
dadosEnviados = {"nome": "pedro henrique de avila tonin", "telefone": "(45)99800-9100"}
response = requests.post(f"{URL}/", json=dadosEnviados)
print(response.status_code)
print(response.json())

# GET
# response = requests.get(f"{URL}/")
# print(response.status_code)
# content = response.json()
# print(content)
