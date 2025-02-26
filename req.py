import base64
import zeep

# Configuração
WSDL_URL = "https://mackenzie-test.softexpert.com/se/ws/dc_ws.php?wsdl"
client = zeep.Client(wsdl=WSDL_URL)

# Leitura do arquivo e conversão para Base64
with open("relatorio.pdf", "rb") as file:  # Aqui o nome do arquivo precisa estar entre aspas
    encoded_file = base64.b64encode(file.read()).decode("utf-8")

# Montando a requisição
document_data = {
    "idcategory": 123,
    "title": "Relatório Financeiro",
    "dsresume": "Resumo do relatório",
    "dtdocument": "2025-02-26",
    "attributes": "campo1=valor1;campo2=valor2;",
    "iduser": 456,
    "file": [{
        "name": "relatorio.pdf",  # Tente "name" ao invés de "NMFILE"
        "data": encoded_file,      # Tente "data" ao invés de "BINFILE"
    }]
}

# Chamando o serviço
response = client.service.newDocument(**document_data)

# Exibindo a resposta
print(response)
