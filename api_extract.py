import resquests
import json
import os

def gupy_extractor(label):
    label =  "dados"
    url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"
    response = requests.get(url)
    dados = response.json()

    with open("gupy.json" , "w") as f:
        json.dump(dados, f, indent=4)

label=["dados"]
gupy_extractor(label)
