senha = '1234'
tentativa = 3

while tentativa > 0:
    login = input('digite sua senha>>')
    if login == senha:
        print('acesso liberado!!')
        break
    else:
        tentativa -= 1
        print(f'Senha incorreta!!! tentativas restantes: {tentativa}')

if tentativa == 0:
    print('conta bloqueada')