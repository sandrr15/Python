def contar_linhas(cadastro):
    linha = 1
    with open(cadastro, "r", encoding="utf-8") as arquivo:
        return sum(1 for linha in arquivo)
    
quantidade = contar_linhas('cadastro.txt')
print(f"O arquivo possui {quantidade} linhas.")
