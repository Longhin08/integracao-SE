import requests
import pandas as pd
from datetime import datetime, timedelta
 
# Gera datas D-1 automaticamente
ontem_ultimo = datetime.now()
ontem = datetime.now() - timedelta(days=3)
inicio = ontem.replace(hour=0, minute=0, second=0, microsecond=0)
fim = ontem_ultimo.replace(hour=23, minute=59, second=59, microsecond=0)
 
# Defina seu token aqui
token = "eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NTM5ODU1ODEsImV4cCI6MTkxMTc1MTk4MSwiaWRsb2dpbiI6Im9wdGltaXplIn0.7vBm--g1Un3WHhuAjN-5RPlSIkiyT4OieqrHS37UB28"
 
# Cabeçalhos da requisição
headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}
 
# Corpo base da requisição
params_base = {  
    "your_id_dataset": "relatoriogeral"
}
 
# URL da API
url = "https://mackenzie.softexpert.com/apigateway/v1/dataset-integration/relatoriogeral"
 
# Inicialização
instancias = []
form_fields = []
page_number = 1
 
# Loop de paginação
while True:
    params = params_base.copy()
    params["pageNumber"] = page_number
    print(f"Processando página {page_number}...")
 
    response = requests.post(url, headers=headers, json=params)
    if response.status_code != 200:
        print(f"Erro {response.status_code}: {response.text}")
        break
 
    data = response.json()
    if not data:
        print("Fim das páginas.")
        break
 
    for instancia in data:
        instancia_id = instancia.get("id")
        instancias.append(instancia)
 
        # FORM FIELDS
        for field in instancia.get("formFields") or []:
            field["instance_id"] = instancia_id
            form_fields.append(field)
 
    page_number += 1
 
# Converter para DataFrame
df_form_fields = pd.json_normalize(form_fields)
 
# Caminho para salvar
caminho = r'D:\DW\DataWarehouse\Arquivos\QA'
 
# Exportar para Excel
df_form_fields.to_excel(f"{caminho}\\form_fields.xlsx", index=False)
 
print("Tudo pronto e salvo com sucesso!")