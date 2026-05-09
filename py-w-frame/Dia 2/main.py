idade = int(input('digite sua idade>> '))
carta = input('possui carta? Sim / Nao >> ')

if idade >= 18:
    if carta == 'sim':
        print('pode dirigir')
else:
    print('nao pode dirigir')