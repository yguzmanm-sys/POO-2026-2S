import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, longitud: float):
        self.longitud = longitud

    def calcular_area(self) -> float:
        return self.longitud ** 2

    def calcular_perimetro(self) -> float:
        return 4 * self.longitud

class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> str:
        hipotenusa = self.calcular_hipotenusa()
        if math.isclose(self.base, self.altura) and math.isclose(self.base, hipotenusa):
            return "Es un triángulo Equilátero"
        elif not math.isclose(self.base, self.altura) and not math.isclose(self.base, hipotenusa) and not math.isclose(self.altura, hipotenusa):
            return "Es un triángulo Escaleno"
        else:
            return "Es un triángulo Isósceles"

    # Alias por compatibilidad
    determinar_tipo_triagunlo = determinar_tipo_triangulo

class Figuras_geometricas:
    @staticmethod
    def main():
        figura1 = Circulo(2.0)
        figura2 = Rectangulo(1, 2)
        figura3 = Cuadrado(3)
        figura4 = TrianguloRectangulo(3, 5)

        print(f"El área del círculo es = {figura1.calcular_area()}")
        print(f"El perímetro del círculo es = {figura1.calcular_perimetro()}")
        print(f"El área del rectángulo es = {figura2.calcular_area()}")
        print(f"El perímetro del rectángulo es = {figura2.calcular_perimetro()}")
        print(f"El área del cuadrado es = {figura3.calcular_area()}")
        print(f"El perímetro del cuadrado es = {figura3.calcular_perimetro()}")
        print(f"El área del triángulo rectángulo es = {figura4.calcular_area()}")
        print(f"El perímetro del triángulo rectángulo es = {figura4.calcular_perimetro()}")
        print(figura4.determinar_tipo_triangulo())

if __name__ == "__main__":
    Figuras_geometricas.main()
