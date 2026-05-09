n = int(input("Quantos termos da sequência de Fibonacci você deseja? "))

a, b = 0, 1

if n <= 0:
    print("Digite um número positivo.")
else:
    print("Sequência de Fibonacci:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b