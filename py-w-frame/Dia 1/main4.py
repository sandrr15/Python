print('ECOMMERCER DO SPANZZZZZZZZZZ')

login = input('digite seu nome>>')

produtos = ['','hd','memoria ram','processador','placa de video']
valores =  [0,500.0,1200.0,1500.0,2000.0]

print(f'''   
    1  {produtos[1]} R$ valor {valores[1]}
    2  {produtos[2]} R$ valor {valores[2]}
    3  {produtos[3]} R$ valor {valores[3]}
    4  {produtos[4]} R$ valor {valores[4]}    
       ''')

carrinho = []
valor = []


for i in range(0,5):
        prod1 = input('escolha um produto')
        if prod1 == 'hd':
            carrinho.append(produtos[1])
            valor.append(valores[1])
        elif prod1 == 'memoria ram':
            carrinho.append(produtos[2])
            valor.append(valores[2])
        elif prod1 == 'processador':
            carrinho.append(produtos[3])
            valor.append(valores[3])
        elif prod1 == 'placa de video':
            carrinho.append(produtos[4])
            valor.append(valores[4])
        
soma_total = sum(valor)
print('esse e seu carrinho' , carrinho , 'esse foi o valor total do seu carrinho>>' , soma_total)





