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
      <urn:newAttachment>
         <!--You may enter the following 8 items in any order-->
         <urn:WorkflowID>tratamento</urn:WorkflowID>
         <urn:ActivityID>000853</urn:ActivityID>
         <urn:FileName>teste</urn:FileName>
         <urn:FileContent>cid:279685291020</urn:FileContent>
         <!--Optional:-->
         <urn:UserID></urn:UserID>  
         <urn:AttachmentID></urn:AttachmentID>
         <urn:AttachmentName></urn:AttachmentName>
         <urn:Summary></urn:Summary>
      </urn:newAttachment>
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