import requests
import base64
import os
from dotenv import load_dotenv


load_dotenv()
# Leitura e codificação em Base64 do arquivo
with open("teste.pdf", "rb") as file:
    arquivo_bytes = file.read()
    base64_bytes = base64.b64encode(arquivo_bytes)
    base64_string = base64_bytes.decode("utf-8")

auth = os.getenv("TOKEN_JWT")

print(auth)

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
        <urn:newDocument>
            <urn:idcategory>Dossiê do Curso</urn:idcategory>
            <urn:iddocument>teste com arquivo</urn:iddocument>
            <urn:title>TÍTULO_DO_DOCUMENTO</urn:title>
            <urn:dsresume>RESUMO_DO_DOCUMENTO</urn:dsresume>
            <urn:iduser></urn:iduser>
            <urn:fgmodel></urn:fgmodel>
            <urn:file>
                <urn:item>
                    <urn:NMFILE>teste.pdf</urn:NMFILE>
                    <urn:BINFILE>{base64_string}</urn:BINFILE>
                    <urn:CONTAINER>?</urn:CONTAINER>
                    <urn:ERROR>?</urn:ERROR>
                </urn:item>
            </urn:file>
        </urn:newDocument>
    </soapenv:Body>
    </soapenv:Envelope>
"""

# Realizando a requisição POST com o XML
response = requests.post(url, headers=headers, data=xml_body)

xml_response = response.text  # Supondo que a resposta da API está aqui

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
