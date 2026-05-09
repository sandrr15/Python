print('SISTEMA DE NOTAS')

lista_nomes = []
aluno_1 = input('digite o nome do aluno>> ')
aluno_2 = input('digite o nome do aluno>> ')
lista_nomes.append(aluno_1)
lista_nomes.append(aluno_2)

notas_al1 = []
notas_al2 = []

for i in range(0,6):
    nota_al1 = float(input('digite as notas do aluno 1>>'))
    notas_al1.append(nota_al1)
for i in range(0,6):
    nota_al2 = float(input('digite as notas do aluno 2>>'))
    notas_al2.append(nota_al2)

print(f'''
      
    notas aluno 1:{notas_al1}
      
    notas aluno 2:{notas_al2}

      ''')


soma_al1 = sum(notas_al1)
soma_al2 = sum(notas_al2)

resul_final_al1 = soma_al1 / 6
resul_final_al2 = soma_al2 / 6

match resul_final_al1:
    case i if resul_final_al1 < 5:
        print(f'''
              
              aluno {aluno_1}:reprovado!
              
              ''')
    case i if resul_final_al1 >= 5:
        print(f'''
              
              aluno {aluno_1}:aprovado!
              
              ''')
match resul_final_al2:
    case i if resul_final_al2 < 5:
        print(f'''
              
              aluno {aluno_2}:reprovado!
              
              ''')
    case i if resul_final_al2 >= 5:
        print(f'''
              
              aluno {aluno_2}:aprovado!
              
              ''')