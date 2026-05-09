nome = input('digite seu nome>> ')
idade = input('digite sua idade>> ')
peso = float(input('digite seu peso>>' ))
altura = float(input('digite sua altura>> '))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = 'Abaixo do peso'
elif imc < 25:
    classificacao = 'Peso normal'
elif imc < 30:
    classificacao = 'Sobrepeso'
else:
    classificacao = 'Obesidade'

print(f'''
      
    nome : {nome}
    idade : {idade}     IMC : {imc}
    peso : {peso}       status : {classificacao}
    altura : {altura}
      
      ''')