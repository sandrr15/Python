def display1(nome):
    
    print('seja bem vindo', nome)

def display2(produtos,precos,):
    meu_carrinho = []
    valores = []
    print(produtos)
    p = input('deseja fazer seu pedido? y/n >>')
    while p == 'y':

        pedido = int(input('digite seu produto>>')) 
        meu_carrinho.append(pedido)  
        valores.append(precos[pedido])
        soma = sum(valores)
        print(soma)
        p = input('deseja fazer o pedido? y/n >>') 
 
    return meu_carrinho 






    