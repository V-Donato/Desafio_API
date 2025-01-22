from gupy import gupy_api_extractor, gupy_api_writer

def main():

    dados = gupy_api_extractor(label="dados")
    

    gupy_api_writer(dados, dir_path="data", filename="vagas")

if __name__ == "__main__":
    main()
