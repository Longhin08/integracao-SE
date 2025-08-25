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
            <urn:downloadEletronicFile>
                <!--You may enter the following 8 items in any order-->
                <urn:iddocument>000019fee8474b5385e6a9e8675eba5f-001</urn:iddocument>
                <urn:idrevision></urn:idrevision>
                <urn:iduser></urn:iduser>
                <urn:fgconverttopdf></urn:fgconverttopdf>
                <urn:idcategory></urn:idcategory>
                <urn:fgwatermark></urn:fgwatermark>
                <urn:nmfile></urn:nmfile>
                <urn:fgfilelink></urn:fgfilelink>
            </urn:downloadEletronicFile>
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