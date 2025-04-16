import requests
import base64
import os
from dotenv import load_dotenv
 
load_dotenv()
 
 
# Leitura e codificação em Base64 do arquivo
with open("teste.pdf", "rb") as file:
    arquivo_bytes = file.read()
    base64_bytes = base64.b64encode(arquivo_bytes)
    file_name = "123"
    base64_string = base64_bytes.decode("utf-8")
 
# URL da sua API (substitua pela URL correta)
url = os.getenv("DOMAIN")
auth = os.getenv("TOKEN_JWT")
 
 
# Headers da requisição (ajuste conforme necessário)
headers = {
    "Content-Type": "text/xml;charset=UTF-8",
    "Authorization": auth
}
 
# Corpo da requisição em XML
xml_body = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:document">
    <soapenv:Header/>
    <soapenv:Body>
        <urn:newDocument>
            <urn:idcategory>naoIndex</urn:idcategory>
            <urn:iddocument>testeCaix3j333a2222</urn:iddocument>
            <urn:title>{file_name}123</urn:title>
            <urn:dsresume>Documento enviado automaticamente</urn:dsresume>
            <urn:iduser></urn:iduser>
            <urn:attributes>caixa=123123</urn:attributes>
            <urn:fgmodel></urn:fgmodel>
            <urn:file>
                <urn:item>
                    <urn:NMFILE>teste1234.pdf</urn:NMFILE>
                    <urn:BINFILE>{base64_string}41231231231231231233</urn:BINFILE>
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
 
# Verificando a resposta da API
if response.status_code == 200:
    xml_response = response.text  # Supondo que a resposta da API está aqui
    print("Resposta da API:", xml_response)
else:
    print(f"Erro ao enviar a requisição. Código de status: {response.text}")