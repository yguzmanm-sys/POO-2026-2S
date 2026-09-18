"""
Ejercicio Propuesto No 17

Enunciado:
Dado el radio de un círculo. Haga un algoritmo que obtenga el área del círculo y la longitud de la circunferencia.
"""

import math

class Circulo:
    """Clase que representa un círculo y permite calcular su área y circunferencia."""
    def __init__(self, radio: float):
        """Inicializa el radio del círculo."""
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return math.pi * self.radio ** 2

    def calcular_circunferencia(self):
        """Calcula la longitud de la circunferencia."""
        return 2 * math.pi * self.radio

    def imprimir_resultados(self):
        """Imprime el área y la circunferencia del círculo."""
        print(f"Radio del círculo: {self.radio}")
        print(f"Área del círculo: {self.calcular_area():.4f}")
        print(f"Longitud de la circunferencia: {self.calcular_circunferencia():.4f}")

if __name__ == "__main__":
    circulo = Circulo(10) # Ejemplo con radio 10
    circulo.imprimir_resultados()
