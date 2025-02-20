from gupy import gupy_api_extractor, gupy_api_writer

def main():
    dados = gupy_api_extractor(label="dados")  # Extrai os dados para a categoria "dados"
    
    if dados:
        gupy_api_writer(dados, dir_path="data", filename="vagas")  # Salva os dados extraídos na pasta "data"
    else:
        print("Nenhuma vaga encontrada.")

if __name__ == "__main__":
    main()

