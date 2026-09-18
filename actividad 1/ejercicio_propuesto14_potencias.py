"""
Ejercicio Propuesto No 14

Enunciado:
Elabore un algoritmo que lea un número y obtenga su cuadrado y su cubo.
"""

class Numero:
    """Clase que representa un número y sus potencias."""
    def __init__(self, valor: float):
        """Inicializa el valor del número."""
        self.valor = valor

    def obtener_cuadrado(self):
        """Devuelve el cuadrado del número."""
        return self.valor ** 2

    def obtener_cubo(self):
        """Devuelve el cubo del número."""
        return self.valor ** 3

    def imprimir_resultados(self):
        """Imprime el cuadrado y el cubo del número."""
        print(f"Número: {self.valor}")
        print(f"Cuadrado: {self.obtener_cuadrado()}")
        print(f"Cubo: {self.obtener_cubo()}")

if __name__ == "__main__":
    numero = Numero(5) # Ejemplo con el número 5
    numero.imprimir_resultados()
