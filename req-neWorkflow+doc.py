import requests
import base64
import os
from dotenv import load_dotenv
import json

# Carrega as variáveis do arquivo .env
load_dotenv()

# Lê e codifica o arquivo em Base64
with open("teste.pdf", "rb") as file:
    arquivo_bytes = file.read()
    base64_string = base64.b64encode(arquivo_bytes).decode("utf-8")

# Configurações da API
url = "https://mackenzie-test.softexpert.com/apigateway/v1/workflow"
auth_token = os.getenv("TOKEN_JWT")

headers = {
    "Content-Type": "application/json",
    "Authorization": auth_token
}

# Corpo da requisição
payload = {
    "processId": "tratamento",
    "workflowTitle": "Your Title Instance",
    "userId": "01",
    "tables": [
        {
            "id": "formindex",
            "fields": [
                {
                    "id": "b64wf",
                    "value": base64_string
                }
            ]
        }
    ],
    "attachments": [
        {
            "filereference": "2c94808680f0ee390180f5c5b4c02054",
            "name": "testejson"
        }
    ]
}

# Envia a requisição POST
response = requests.post(url, headers=headers, json=payload)

# Trata a resposta
if response.ok:
    print(" Requisição bem-sucedida!")
    print("Resposta da API:", response.text)
else:
    print(f" Erro ({response.status_code}): {response.text}")
