num1 = float(input('digite um numero>>'))
num2 = float(input('digite um numero>>'))
operacao = str(input('escolha a operacao + | - | / | * >>'))

match operacao:
    case i if operacao == ('+'):
        soma = num1 + num2
        print(soma)
    case i if operacao == '-':
        subtracao = num1 - num2
        print(subtracao)
    case i if operacao == '/':
        dividir = num1 / num2
        print(dividir)
    case i if operacao == '*':
        multiplicar = num1 * num2
        print (multiplicar)






