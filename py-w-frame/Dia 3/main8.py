import datetime

while True:
    print("\nMenu:")
    print("1 - Exibir mensagem 'Olá!'")
    print("2 - Exibir data/hora atual")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá!")
    elif opcao == "2":
        agora = datetime.datetime.now()
        print("Data e hora atual:", agora)
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")