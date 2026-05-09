valor = int(input("Digite o valor do saque: "))


if valor < 10 or valor > 1000 or valor % 5 != 0:
    print("Valor inválido. Deve ser entre 10 e 1000 e múltiplo de 5.")
    exit()


notas50 = valor // 50
resto = valor % 50

notas20 = resto // 20
resto = resto % 20

notas10 = resto // 10
resto = resto % 10

notas5 = resto // 5


print("\nDistribuição de notas:")
print(f"Notas de 50: {notas50}")
print(f"Notas de 20: {notas20}")
print(f"Notas de 10: {notas10}")
print(f"Notas de 5: {notas5}")