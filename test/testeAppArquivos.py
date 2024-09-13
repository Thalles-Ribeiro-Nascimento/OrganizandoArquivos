# Importando bibliotecas para gerenciamento/manipulação de arquivos e diretórios
import os
import shutil


# Diretório que deseja alterar
entry = input("Digite o diretório que deseja organizar: ")
dir = entry.split()
caminho = os.path.join(*dir)
path = "/" + caminho + "/"
print(path)


# Criando pastas a escolha do usuário
cont = int(input("Insira o número de diretórios que deseja criar: "))
listDirectory = []

for i in range(cont):
    if cont > 0:
        directories = input("Insira um nome de pasta: ")
        listDirectory.append(directories)
    else:
        print("Número de pastas igual a 0")
        break

# print(f"listDirectory")

# print(listDirectory)
# powerPoint = "PowerPoint"
# imagens = "Imagens"
# documentos = "Word"
# pdf1 = "PDF"
# sheets = "Planilhas"
# textos = "TXT"
# # Lista de diretórios
# listDirectory = [powerPoint, imagens, documentos, pdf1, sheets, textos]

# Criando os diretórios
for dir in listDirectory:
    # Comando para criar Diretórios
    os.mkdir(path+dir)

if cont == 1:
    print("Diretório Criado!")

else:
    print("Os diretórios foram criados com sucesso!")

# # Listando os diretórios e arquivos
# arquivos = os.listdir(diretorio)
#     # print(arquivos)

# # Organizando os arquivos em cada diretório respectivo à extensão
# for file in arquivos:
#     if file.lower().endswith((".pptx")):
#         shutil.move(os.path.join(diretorio, file), os.path.join(diretorio, powerPoint, file))
#     elif file.lower().endswith((".png", ".jpg")):
#         shutil.move(os.path.join(diretorio, file), os.path.join(diretorio, imagens, file))
#     elif file.lower().endswith((".docx", ".odt")):
#         shutil.move(os.path.join(diretorio, file), os.path.join(diretorio, documentos, file))
#     elif file.lower().endswith((".pdf")):
#         shutil.move(os.path.join(diretorio, file), os.path.join(diretorio, pdf1, file))
#     elif file.lower().endswith((".xlsx", ".ods", ".csv")):
#         shutil.move(os.path.join(diretorio, file), os.path.join(diretorio, sheets, file))
#     elif file.lower().endswith((".txt")):
#         shutil.move(os.path.join(diretorio, file), os.path.join(diretorio, textos, file))




# Criando uma lista com um Input com espaços
# dir = input("Digite algo: ")
# dir.split()

# print(dir.split())
