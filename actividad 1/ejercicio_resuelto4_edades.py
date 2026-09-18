"""
Ejercicio Resuelto No 4

Enunciado:
A la mamá de Juan le preguntan su edad, y contesta: tengo 3 hijos, pregúntele a Juan su
edad. Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la edad de Juan y mi edad es
la suma de las tres. Hacer un algoritmo que muestre la edad de los cuatro.
"""

class FamiliaJuan:
    """Clase para representar a la familia de Juan y calcular sus edades."""
    def __init__(self, edad_juan: float):
        """Inicializa la clase con la edad de Juan."""
        self.edad_juan = edad_juan

    def calcular_edades(self):
        """Calcula las edades de Alberto, Ana y la mamá basados en la edad de Juan."""
        alberto = (2 / 3) * self.edad_juan
        ana = (4 / 3) * self.edad_juan
        mama = self.edad_juan + alberto + ana
        return self.edad_juan, alberto, ana, mama

    def imprimir_edades(self):
        """Imprime las edades de todos los miembros de la familia."""
        juan, alberto, ana, mama = self.calcular_edades()
        print(f"Edad de Juan: {juan:.0f}")
        print(f"Edad de Alberto: {alberto:.0f}")
        print(f"Edad de Ana: {ana:.0f}")
        print(f"Edad de la mamá: {mama:.0f}")

if __name__ == "__main__":
    # Ejemplo asumiendo que Juan tiene 9 años (para que las edades den enteras)
    familia = FamiliaJuan(9)
    familia.imprimir_edades()
