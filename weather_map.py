import requests                                                 # Documentation: https://www.meteomatics.com/en/api/getting-started/
from requests.auth import HTTPBasicAuth                         # API Request: https://www.meteomatics.com/en/api/request/
from credentials import METEOMATICS_LOGIN, METEOMATICS_SENHA    # Aqui estou usando um arquivo separado com as credenciais

def get_meteomatics(cidade, start_date, end_date, time_step="PT1H", parameters="t_2m:C", output_format="html"):
    coordenadas_anapolis = '-16.3285,-48.9534'
    url = f'https://api.meteomatics.com/{start_date}--{end_date}:{time_step}/{parameters}/{coordenadas_anapolis}/{output_format}'
    auth = HTTPBasicAuth(METEOMATICS_LOGIN, METEOMATICS_SENHA)

    resposta = requests.get(url, auth=auth)

    if resposta.status_code == 200:
        print(resposta.text)
    else:
        print(f'Erro ao obter a previsão do tempo. Código de status: {resposta.status_code}')
        print(f'Mensagem de erro: {resposta.text}')

if __name__ == "__main__":
    data_inicial = '2024-01-09T00:00:00Z'
    data_final = '2024-01-12T00:00:00Z'
    get_meteomatics('Anápolis', data_inicial, data_final)
