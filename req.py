import requests
import logging
import base64
import os
import time
from dotenv import load_dotenv

load_dotenv()

#Arquivo de log
logger = logging.getLogger(__name__)
logging.basicConfig(filename='monitor.log', encoding='utf-8', format='%(message)s %(asctime)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.WARNING)

# Diretório a ser monitorado
diretorio_monitorado = r"C:\testes\monitor"

# Função para monitorar a pasta e subpastas
def monitorar_pasta(diretorio):
    arquivos_processados = set()

    logging.warning("Monitoramento Iniciado...")
    while True:
        for pasta_raiz, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(pasta_raiz, arquivo)
                if caminho_arquivo not in arquivos_processados:
                    arquivos_processados.add(caminho_arquivo)
                    logging.info(f"Novo arquivo encontrado: {arquivo}")
                    processar_arquivo(caminho_arquivo)
        time.sleep(2) 

# Função para processar o arquivo
def processar_arquivo(caminho_arquivo):
    file_name = os.path.basename(caminho_arquivo)  # Obtém o nome do arquivo

    with open(caminho_arquivo, "rb") as file:
        arquivo_bytes = file.read()
        base64_bytes = base64.b64encode(arquivo_bytes)
        base64_string = base64_bytes.decode("utf-8")

    auth = os.getenv("TOKEN_JWT")

    url = os.getenv("DOMAIN")

    headers = {
        "Content-Type": "text/xml;charset=UTF-8",
        "Authorization": auth
    }

    xml_body = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:document">
        <soapenv:Header/>
        <soapenv:Body>
            <urn:newDocument>
                <urn:idcategory>Dossiê do Curso</urn:idcategory>
                <urn:iddocument>{file_name}</urn:iddocument>
                <urn:title>{file_name}</urn:title>
                <urn:dsresume>Documento enviado automaticamente</urn:dsresume>
                <urn:iduser></urn:iduser>
                <urn:fgmodel></urn:fgmodel>
                <urn:file>
                    <urn:item>
                        <urn:NMFILE>{file_name}</urn:NMFILE>
                        <urn:BINFILE>{base64_string}</urn:BINFILE>
                        <urn:CONTAINER>?</urn:CONTAINER>
                        <urn:ERROR>?</urn:ERROR>
                    </urn:item>
                </urn:file>
            </urn:newDocument>
        </soapenv:Body>
        </soapenv:Envelope>
    """

    response = requests.post(url, headers=headers, data=xml_body)

    if response.status_code == 200:
        logging.info(f"Arquivo {file_name} enviado com sucesso!")
        os.remove(caminho_arquivo)
    else:
        logging.ERROR(f"Erro ao enviar {file_name}. Código de status: {response.status_code} Resposta: {response.text}")

# Iniciar a monitoração
monitorar_pasta(diretorio_monitorado)

