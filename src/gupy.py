import os
import requests
import json
from typing import List, Dict, Any

def gupy_api_extractor(label: str, limit: int = 400, offset: int = 0) -> List[Dict[str, Any]]:
    
    url = f"https://portal.api.gupy.io/api/job?name={label}&offset={offset}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API da Gupy: {e}")
        return []

def gupy_api_writer(dados: List[Dict[str, Any]], dir_path: str, filename: str) -> None:
   
    os.makedirs(dir_path, exist_ok=True) 
    file_path = os.path.join(dir_path, f"{filename}.json")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)  
        print(f"Arquivo salvo com sucesso em: {file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")



    