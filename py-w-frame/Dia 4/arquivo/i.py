arquivo = open("dados.txt", "r")
linhas = arquivo.readlines()
for l in linhas:
    print(linhas.strip())
arquivo.close()
