import requests
import base64
import os
from dotenv import load_dotenv


load_dotenv()


auth = os.getenv("TOKEN_JWT")

# URL da sua API (substitua pela URL correta)
url = "https://mackenzie-test.softexpert.com/apigateway/se/ws/dc_ws.php"

# Headers da requisição (ajuste conforme necessário)
headers = {
    "Content-Type": "text/xml;charset=UTF-8",
    "Authorization": auth  # se necessário
}

# Corpo da requisição em XML
xml_body = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:document">
        <soapenv:Header/>
        <soapenv:Body>
            <urn:viewDocumentData>
                <urn:iddocument>123</urn:iddocument>
                <urn:idrevision></urn:idrevision>
                <urn:iduser></urn:iduser>
                <urn:idcategory>naoIndex</urn:idcategory>
            </urn:viewDocumentData>
        </soapenv:Body>
    </soapenv:Envelope>
"""

# Realizando a requisição POST com o XML
response = requests.post(url, headers=headers, data=xml_body)

xml_response = response.text  # Supondo que a resposta da API está aqu

# Extrai o conteúdo dentro da tag <return>
inicio = xml_response.find("<return>") + len("<return>")
fim = xml_response.find("</return>")

if inicio != -1 and fim != -1:
    conteudo = xml_response[inicio:fim].strip()

# Verificando a resposta da API
if response.status_code == 200:
    print("Resposta da API:", conteudo)
else:
    print(f"Erro ao enviar a requisição. Código de status: {response.status_code}")
