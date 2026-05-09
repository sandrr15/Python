import random

lista = ['😂','🤣','😭']

while True:

    aleatorio = random.choice(lista)

    adivinhe = input('adivinhe o emoji 😂 | 🤣 | 😭 |')

    if adivinhe == aleatorio:
        print(aleatorio , '|' , adivinhe , ' ' , 'voce acertou!!')
        break
    else:
        print(aleatorio , '|' , adivinhe , ' ' , 'voce errou!!')





