import random

print('''
Pedra - 1
Tesoura - 2
Papel - 3
''')

jogador = int(input('Pedra, papel ou tesoura? '))
maquina = random.randint(1, 3)

print(f'Jogador: {jogador}')
print(f'Máquina: {maquina}')

if jogador == maquina:
    print('Empate!')
elif (jogador == 1 and maquina == 2) or \
     (jogador == 2 and maquina == 3) or \
     (jogador == 3 and maquina == 1):
    print('Jogador venceu!')
else:
    print('Máquina venceu!')