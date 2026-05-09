# par_impar = int(input('digite um numero>>'))%2 == 0

# match par_impar:
#     case True:
#         print('par') 
    
#     case False:
#         print('impar')


# num_1 = int(input('digite um numero'))

# match num_1:

#     case i if i <0:
#         print('negativo')

#     case i if i >0:
#         print('positivo')

# num_1 = (input('digite um texto')) == ''

# match num_1:

#      case True :
#          print('vazio')

#      case False :
#          print('aqui tem um texto')
                



num_1 = int(input('digite um numero:>> ' )) 

match num_1:
    case i if num_1 ==10:
        print('igual a 10')
    case i if num_1 < 10:
        print('menor que dez')
    case i if num_1 > 10:
        print('maior que dez')
