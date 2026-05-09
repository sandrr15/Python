num = int(input('digite um numero inteiro positivo'))
soma = 0
lista = []

while soma < num:
    soma += 1
    lista.append(soma)
    lista_sum = sum(lista)
    
print(lista_sum)
