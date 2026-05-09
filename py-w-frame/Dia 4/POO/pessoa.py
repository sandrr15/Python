class Pessoa:
    def __init__(self , nome , idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Ola,meu nome é {self.nome} e eu tenho {self.idade} anos de idade")

pessoa1 = Pessoa("Enzo" , 17)
pessoa2 = Pessoa("Anthony" , 17)

pessoa1.apresentar()
pessoa2.apresentar()