import os

def leituraArquivo():
    caminho = "/home/thalles/Documentos/Python/Organizador_Arquivos/arquivos/ExtensoesArquivos"
    if os.path.exists(caminho):
        with open(caminho) as file:
            lista_lida = file.readlines()
        
    return lista_lida