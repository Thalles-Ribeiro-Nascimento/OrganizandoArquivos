# # Importando bibliotecas para gerenciamento/manipulação de arquivos e diretórios
# import os
# import shutil
# import re


# def espaco():
#     return print()

# # Diretório que deseja alterar
# entry = input("Digite o diretório que deseja organizar (ex: home user Documentos): ")
# dir = entry.split()
# caminho = os.path.join(*dir)
# path = "/" + caminho + "/"
# print(path)
# espaco()

# # Listando os diretórios e arquivos
# with os.scandir(path) as entries:
#     files = [entry.name for entry in entries if entry.is_file()]

# print(f"Lista de arquivos do diretório {path}:\n{files}")
# espaco()

# pergunta = int(input("O que deseja?\n1- Criar uma pasta com nome do arquivo\n2- Criar uma pasta de acordo com a extensão do arquivo?\nInsira um valor: "))

# if pergunta == 1:
#     # Criando pastas a escolha do usuário
#     cont = int(input("Insira o número de diretórios que deseja criar: "))
#     listDirectory = []

#     for i in range(cont):
#         directories = input("Insira um nome de pasta: ")
#         listDirectory.append(directories)
#     listDirectory.sort()

#     espaco()
#     print(listDirectory)
#     espaco()


#     # Criando os diretórios
#     for dir in listDirectory:
#         # Comando para criar Diretórios
#         os.mkdir(path+dir)

#     if cont == 1:
#         print("Diretório Criado!")

#     else:
#         print("Os diretórios foram criados com sucesso!")

# # Inserindo os arquivos nos diretórios criados, comparando os nomes
#     for directory in listDirectory:
#         for file in files:
#             arquivo = file.lower()
#             pasta = directory.lower()
#             comparando = re.search(pasta, arquivo)
#             if comparando:
#                 shutil.move(os.path.join(path, file), os.path.join(path, directory, file))
#                 print(f"Arquivo: {file}\nPasta: {directory}")
#             else:
#                 continue
# elif pergunta == 2:
#     cont2 = int(input("Insira o número de diretórios que deseja criar: "))
#     dicPastas = {}
#     for i in range(cont2):
#         key = input("Insira o nome da pasta: ")
#         k = key
#         value = input("Insira a extensão: ")
#         v = value
#         dicPastas = {k:v}
    
#     print(dicPastas)

















# list1S = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
# list2S = ["Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# for directory in listDirectory:
#     for file in files:
#         pasta = directory
#         arquivo = file
#         comparando_primeiro_semestre = re.search(pasta, "-1S")
#         comparando_segundo_semestre = re.searche(pasta, "-2S")
#         comparando_arquivo = re.search(arquivo, "")
#         if pasta:
#             shutil.move(os.path.join(path, arquivo), os.path.join(path, pasta, arquivo))
#             print(f"Arquivo: {arquivo}\nPasta: {pasta}")
#         else:
#             continue










# Inserindo os arquivos nos diretórios criados, comparando os nomes
# for directory in listDirectory:
#     for file in files:
#         arquivo = file.lower()
#         pasta = directory.lower()
#         comparando = re.search(pasta, arquivo)
#         if comparando:
#             shutil.move(os.path.join(path, file), os.path.join(path, directory, file))
#             print(f"Arquivo: {file}\nPasta: {directory}")
#         else:
#             continue
        




# pergunta = input("Você deseja criar pastas de acordo com o nome ou extensão do arquivo (Y/N)? ")

# Lista de extensões de arquivos
# audio = ler.leituraArquivo("audio")
# comprimido = ler.leituraArquivo("comprimido")
# documentos = ler.leituraArquivo("documentos")
# executavel = ler.leituraArquivo("exe")
# imagens = ler.leituraArquivo("imagens")
# isos = ler.leituraArquivo("isos")
# apresentacoes = ler.leituraArquivo("planilhas_apresentacoes")
