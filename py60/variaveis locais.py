# def multiplicaçao():

#     n1 = float(input('insira um numero: '))
#     n2 = float(input('insira um numero: '))
#     n3 = float(input('insira um numero: '))

#     multi = n1 * n2 * n3

#     print(multi)

#multiplicaçao ()


# def elevaçao():
    
#     e1 = float(input('digite o numero qual voce quer elevar: '))

#     elevar = e1**2
#     print(elevar)
#elevaçao()

# def mensagem():
#     idade1 = int(input('digite sua idade: '))

#     if idade1 <= 18:

#        print('nao vai ser possivel sua entrada em nosso site,pois voce e menor de idade')


#     elif idade1 > 18:
#          print('seja bem vindo ao nosso site')

# mensagem()

# def idade():

#     ano = int(input('digite o ano que voce nasceu: '))
    
#     idade = 2025 - ano

#     print(idade)

#idade()


# def copa():
    
#     print('copa america 1999/copa do mundo 1999')
#     copa1 = input('qual dessas informaçoes vc deseja receber? ')
#     if copa1 == 'copa america 1999':
#        print('o brasil foi campeao em 1999!!!')               

#     elif copa1 == 'copa do mundo 1999':
#          print('nao houve copa do mundo esse ano')
#copa()


def restaurante():
    
    nome = input('digite seu nome>>')
   
    print('''
          seja-bem vindo : {}

          escolha o seu pedido

          1-salada 2-macarronada 3-sanduiche 4-sorvete

          '''.format(nome))
    
    opçao = input('>>')

    if opçao == '1':
        print('voce escolheu salada')
    elif opçao == '2':
        print('voce escolheu macarronada')
    elif opçao == '3':
        print('voce escolheu sanduiche')
    elif opçao == '4':
        print('voce escolheu sorvete')

        print(opçao)
    
restaurante()


          



    


