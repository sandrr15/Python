arquivo_origem = input('insira o nome do arquivo de origem: ')
arquivo_destino = input('insira o nome do arquivo de destino: ')

try:
    with open(arquivo_origem,"r",encoding="utf-8") as origem:
        conteudo = origem.readlines()

    with open(arquivo_destino,"w",encoding="utf-8") as destino:
        destino.writelines(conteudo)

    print('Arquivo copiado com sucesso!')

except Exception as e:
    print("Erro:", e)
  