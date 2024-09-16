# Importando bibliotecas para gerenciamento/manipulação de arquivos e diretórios
import os
import shutil
import re


def espaco():
    return print()

# Diretório que deseja alterar
entry = input("Digite o diretório que deseja organizar (ex: home user Documentos): ")
dir = entry.split()
caminho = os.path.join(*dir)
path = "/" + caminho + "/"
print(path)
espaco()

# Listando os diretórios e arquivos
with os.scandir(path) as entries:
    files = [entry.name for entry in entries if entry.is_file()]

print(f"Lista de arquivos do diretório {path}:\n{files}")
espaco()

# Criando pastas a escolha do usuário
cont = int(input("Insira o número de diretórios que deseja criar: "))
listDirectory = []
    
for i in range(cont):
    directories = input("Insira um nome de pasta: ")
    listDirectory.append(directories)
listDirectory.sort()

espaco()
print(listDirectory)
espaco()


# Criando os diretórios
for dir in listDirectory:
    # Comando para criar Diretórios
    os.mkdir(path+dir)

if cont == 1:
    print("Diretório Criado!")

else:
    print("Os diretórios foram criados com sucesso!")

# Inserindo os arquivos nos diretórios criados de acordo com a extensão
for directory in listDirectory:
    for file in files:
        arquivo = file.lower()
        pasta = directory.lower()
        comparando = re.search(pasta, arquivo)
        if comparando:
            shutil.move(os.path.join(path, file), os.path.join(path, directory, file))
            print(f"Arquivo: {file}\nPasta: {directory}")
        else:
            continue
        
