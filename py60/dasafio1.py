print('seja bem-vindo ao nosso hotel!!')
nome = []
idade = []

nome1 = input('digite o nome do primeiro hospede: ')
idade1 = int(input('digite a idade do primeiro hospede: '))
quarto1 = input('escolha seu quarto: ')
nome.append(nome1)
idade.append(idade1)

nome2 = input('digite o nome do segundo hospede: ')
idade2 = int(input('digite a idade do segundo hospede: '))
quarto2 = input('escolha seu quarto: ')
nome.append(nome2)
idade.append(idade2)


nome3= input('digite o nome do terceiro hospede: ')
idade3= int(input('digite a idade do terceiro: '))
quarto3 = input('escolha seu quarto: ')
nome.append(nome3)
idade.append(idade3)

dicionario1 = [
'nome', nome1 ,
'idade' , idade2 , 
'quarto' , quarto1
]
print(dicionario1)
dicionario2 = [
'nome',nome2,
'idade',idade2,
'quarto',quarto2
]
print(dicionario2)
dicionario3 = [
'nome',nome3,
'idade',idade3,
'quarto',quarto3
]
print(dicionario3)

preço_dos_quartos = [150,200,300]
estadia= int(input('digite o tempo de sua estadia: '))


soma= preço_dos_quartos[0] * estadia

print(soma)
 




