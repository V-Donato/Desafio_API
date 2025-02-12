import os
import requests
import json
from typing import List, Dict, Any

def gupy_api_extractor(label: str, limit: int = 600) -> List[Dict[str, Any]]:
    dados_completos = []
    offset = 0
    
    while True:
        url = f"https://portal.api.gupy.io/api/job?name={label}&offset={offset}&limit={limit}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            dados = response.json().get('data', [])
            
            if not dados:
                break  # Se não houver mais dados, sai do loop
            
            dados_completos.extend(dados)
            offset += limit  # Atualiza o offset para a próxima requisição
        
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API da Gupy: {e}")
            break
    
    return dados_completos

def gupy_api_writer(dados: List[Dict[str, Any]], dir_path: str, filename: str) -> None:
    # Verifica se o diretório existe, caso contrário, cria
    os.makedirs(dir_path, exist_ok=True)
    
    # Caminho completo do arquivo
    file_path = os.path.join(dir_path, f"{filename}.json")
    
    # Verifica se o arquivo já existe antes de criar
    if os.path.exists(file_path):
        print(f"Arquivo {file_path} já existe. Não será recriado.")
    else:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
            print(f"Arquivo salvo com sucesso em: {file_path}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")

def main():
    dados = gupy_api_extractor(label="dados")
    gupy_api_writer(dados, dir_path="data", filename="vagas")

if __name__ == "__main__":
    main()

    