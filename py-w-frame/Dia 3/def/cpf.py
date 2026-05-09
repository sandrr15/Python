def verificar_cpf(cpf):
    if len(cpf) != 11:
        print('digite algo válido...')
    else:
        soma = 0
        for x in range(9):
            soma  = soma +  int(cpf[x]) * ( 10 - x)


        if soma == 10:
           soma = 1      
        
        print((soma *10 ) % 11)
        soma1 = 0
        for x in range(10):
            soma1  = soma1 +  int(cpf[x]) * ( 11 - x) 
        if soma1 == 10:
           soma1 = 1     
        print((soma1 *10 ) % 11)
        


verificar_cpf('57974208058')            



        





