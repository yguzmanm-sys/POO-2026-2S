"""
Ejercicio resuelto Nº 5

Enunciado:
Hacer un seguimiento (prueba de escritorio) del siguiente grupo de instrucciones.
INICIO
SUMA = 0
X = 20
SUMA = SUMA + X
Y = 40
X = X + Y ** 2
SUMA = SUMA + X / Y
ESCRIBA: "EL VALOR DE LA SUMA ES:", SUMA
FIN_INICIO
"""

class SeguimientoInstrucciones:
    """Clase para ejecutar las instrucciones del seguimiento."""
    def __init__(self):
        """Inicializa las variables que se usarán en el bloque."""
        self.suma = 0
        self.x = 0
        self.y = 0

    def ejecutar_instrucciones(self):
        """Ejecuta paso a paso las instrucciones del algoritmo y devuelve el resultado."""
        self.suma = 0
        self.x = 20
        self.suma = self.suma + self.x
        self.y = 40
        self.x = self.x + self.y ** 2
        self.suma = self.suma + self.x / self.y
        return self.suma

    def imprimir_resultado(self):
        """Imprime el valor final de la suma después del proceso."""
        resultado = self.ejecutar_instrucciones()
        print(f"EL VALOR DE LA SUMA ES: {resultado}")

if __name__ == "__main__":
    seguimiento = SeguimientoInstrucciones()
    seguimiento.imprimir_resultado()
