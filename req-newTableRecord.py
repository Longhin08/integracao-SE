import requests
import base64
import os
from dotenv import load_dotenv
 
load_dotenv()
 
 
# Leitura e codificação em Base64 do arquivo
with open("teste.pdf", "rb") as file:
    arquivo_bytes = file.read()
    base64_bytes = base64.b64encode(arquivo_bytes)
    file_name = "testeinte"
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
        <urn:newTableRecord>
            <urn:UserID>02</urn:UserID>
            <urn:TableID>bintable</urn:TableID>
            <urn:TableFieldList>
               <urn:TableField>
                  <urn:TableFieldID>b64</urn:TableFieldID>
                  <urn:TableFieldValue>{base64_string}</urn:TableFieldValue>
               </urn:TableField>
               <urn:TableField>
                  <urn:TableFieldID>nmfile</urn:TableFieldID>
<<<<<<< HEAD
                  <urn:TableFieldValue>testeinte123.pdf</urn:TableFieldValue>
               </urn:TableField>
               <urn:TableField>
                  <urn:TableFieldID>guid</urn:TableFieldID>
                  <urn:TableFieldValue>testeinte123</urn:TableFieldValue>
=======
                  <urn:TableFieldValue>teste.pdf</urn:TableFieldValue>
               </urn:TableField>
               <urn:TableField>
                  <urn:TableFieldID>guid</urn:TableFieldID>
                  <urn:TableFieldValue>teste</urn:TableFieldValue>
>>>>>>> 528feb199621fd7ef369f60ca3846b298a723268
               </urn:TableField>
            </urn:TableFieldList>
        </urn:newTableRecord>
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