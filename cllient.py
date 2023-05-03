import requests

URL = "http://127.0.0.1:8000"

# GET
# response = requests.get(f"{URL}/")
# print(response.status_code)
# content = response.json()
# print(content)

# POST
dadosEnviados = {"nome": "pedro"}
response = requests.post(f"{URL}/", json=dadosEnviados)
print(response.status_code)
print(response.json)
