class Triangulo:
    def __init__(self, a, b, c):
        # guardando valores en campos privados
        self.__a = a
        self.__b = b
        self.__c = c

    def calcular_area(self):       
        a = self.__a
        b = self.__b
        c = self.__c
        # Se calcula el area con la formula de Herón
        s = (a + b + c) / 2  # semiperímetro
        area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
        return area


nuevo_triangulo = Triangulo(7, 7, 7)
print(nuevo_triangulo.calcular_area())
