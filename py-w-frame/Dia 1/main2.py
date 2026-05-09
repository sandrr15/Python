valor = float(input('qual seria o valor do produto>>'))

desconto = valor * 0.10
valor_final =  valor - desconto

match valor_final:
    case i if valor_final >= 100:
        print(valor_final , 'esse produto e caro')
    case i if valor_final<= 50:
        print(valor_final , 'esse produto e barato')