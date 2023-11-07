import math

class FormaGeometrica:
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcularArea(self):
        return self.comprimento * self.largura

    def calcularPerimetro(self):
        return 2 * (self.comprimento + self.largura)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return math.pi * self.raio * self.raio

    def calcularPerimetro(self):
        return 2 * math.pi * self.raio

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcularArea(self):
        # Usando a fórmula de Heron para calcular a área de um triângulo
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def calcularPerimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Exemplos de uso:
retangulo = Retangulo(4, 5)
print("Área do retângulo:", retangulo.calcularArea())
print("Perímetro do retângulo:", retangulo.calcularPerimetro())

circulo = Circulo(3)
print("Área do círculo:", circulo.calcularArea())
print("Perímetro do círculo:", circulo.calcularPerimetro())

triangulo = Triangulo(3, 4, 5)
print("Área do triângulo:", triangulo.calcularArea())
print("Perímetro do triângulo:", triangulo.calcularPerimetro())
