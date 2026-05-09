class Retangulo:
    def __init__(self , largura , altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        
        return self.largura * self.altura

    def calcular_peri(self):
        
        return 2*(self.altura + self.largura)

    def apresentar_ret(self):
        
        print(f'''

        Essa é a area do seu retangulo : {self.calcular_area()}

        Esse é o perimetro do seu retangulo : {self.calcular_peri()}

        ''')

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

ret = Retangulo(largura , altura)

ret.apresentar_ret()