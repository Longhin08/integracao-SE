import requests
import base64
import os
from dotenv import load_dotenv
 
load_dotenv()
 
 
# URL da sua API (substitua pela URL correta)
url = os.getenv("DOMAIN-WF")
auth = os.getenv("TOKEN_JWT")
 
 
# Headers da requisição (ajuste conforme necessário)
headers = {
    "Content-Type": "text/xml;charset=UTF-8",
    "Authorization": auth
}
 
# Corpo da requisição em XML
xml_body = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:getWorkflow>
         <urn:WorkflowID>000822</urn:WorkflowID>
      </urn:getWorkflow>
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
