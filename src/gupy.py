import os
import requests
import json
from typing import List, Dict, Any

# Função para extrair os dados da API da Gupy
def gupy_api_extractor(label: str) -> List[Dict[str, Any]]:
    dados_completos = []
    offset = 0
    limit = 400  # Mantendo um limite adequado por requisição
    
    print(f'Iniciando extração para: {label}...')
    while True:
        url = f"https://portal.api.gupy.io/api/job?name={label}&offset={offset}&limit={limit}"
        print(f'Buscando página com offset {offset}...')
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            dados = response.json().get('data', [])
            
            if not dados:
                break  # Se não houver mais dados, sai do loop
            
            dados_completos.extend(dados)
            offset += 10  # Pula para a próxima página
        
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API da Gupy: {e}")
            break
    
    print(f'Extração concluída para: {label}. Total de vagas coletadas: {len(dados_completos)}')
    return dados_completos

# Função para salvar os dados extraídos na pasta 'data' dentro de 'Desafio_API'
def gupy_api_writer(dados: List[Dict[str, Any]], dir_path: str, filename: str) -> None:
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Diretório Desafio_API
    data_dir = os.path.join(base_dir, dir_path)  # Caminho da pasta 'data' dentro de Desafio_API

    os.makedirs(data_dir, exist_ok=True)  # Garantindo que a pasta existe
    file_path = os.path.join(data_dir, f"{filename}.json")  # Caminho final do arquivo
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"Arquivo salvo com sucesso em: {file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
