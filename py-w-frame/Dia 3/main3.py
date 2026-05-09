soma = 0
quantidade = 0

while True:
    try:
        notas = float(input('digite as notas>>'))
        if notas == -1:
            break
        if notas < 0 or notas > 10:
            print('nota invalida , digite uma nota entre 0 e 10!!!')
            continue
        soma += notas
        quantidade += 1
        media = soma / quantidade
    except ValueError:
        print('Invalido!!! digite um numero')
        
if quantidade > 0:
    print(f'essa e a media das notas: {media}')
else:
    print('nenhuma nota foi informada!!!')