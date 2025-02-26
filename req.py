import requests

# URL da sua API (substitua pela URL correta)
url = "https://mackenzie-test.softexpert.com/apigateway/se/ws/dc_ws.php"

# Headers da requisição (ajuste conforme necessário)
headers = {
    "Content-Type": "text/xml;charset=UTF-8",
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NDA1Nzc3OTIsImV4cCI6MTg5ODM0NDE5MiwiaWRsb2dpbiI6Im9wdGltaXplIn0.C2kZ5hFLVJSxungMKnVWVcL7oOSreClc7ZGM9GHMTHs"  # se necessário
}

# Corpo da requisição em XML
xml_body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:document">
    <soapenv:Header/>
    <soapenv:Body>
        <urn:newDocument>
            <urn:idcategory>Dossiê do Curso</urn:idcategory>
            <urn:iddocument>1234teste py</urn:iddocument>
            <urn:title>TÍTULO_DO_DOCUMENTO</urn:title>
            <urn:dsresume>RESUMO_DO_DOCUMENTO</urn:dsresume>
            <urn:iduser></urn:iduser>
            <urn:fgmodel></urn:fgmodel>
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

try:
    data = response.json()
    print("Resposta JSON:", data)
except requests.exceptions.JSONDecodeError:
    print("resposta:", conteudo)

