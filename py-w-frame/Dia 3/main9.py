import random

contagem = {i: 0 for i in range(1, 7)}

for _ in range(100):
    resultado = random.randint(1, 6)
    contagem[resultado] += 1

for face in range(1, 7):
    print(f"Face {face}: {contagem[face]} vezes")