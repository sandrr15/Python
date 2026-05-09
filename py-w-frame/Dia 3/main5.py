num = int(input('digite um numero>>'))

if num <= 0:
    print('nao é primo')
else:
    for i in range(2, int(num ** 0.5)+ 1):
        if num % i == 0:
            print('nao e primo')
    else:
        print('é primo')