import meu_modulo1

def mercado():

      nome = input('digite seu nome>>')
      meu_modulo1.display1(nome)
      produtos = ['arroz R$50' , 'feijao R$30', 'macarrao R$30' , 'carne R$40' , 'frango R$20' , 'vegetais R$10']
      lista_de_valores = [50 , 30 , 30 ,40 ,20 ,10]      
      q = meu_modulo1.display2(produtos,lista_de_valores)
      print(q)

mercado() 