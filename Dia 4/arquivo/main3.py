palavra = input('digite uma palavra>>').lower()
nome_arquivo = input('digite o nome do arquivo>>')

total = 0

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        palavras = linha.lower().split()
        total += palavras.count(palavra)
 
print(f"A palavra {palavra} aparece {total} vezes no arquivo")