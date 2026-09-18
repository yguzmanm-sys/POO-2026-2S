"""
Ejercicio Propuesto No 12

Enunciado:
Un empleado trabaja 48 horas en la semana a razón de $5.000 hora. El porcentaje de
retención en la fuente es del 12,5% del salario bruto. Se desea saber cuál es el salario bruto,
la retención en la fuente y el salario neto del trabajador.
"""

class Empleado:
    """Clase para calcular la nómina de un empleado."""
    def __init__(self, horas_semana: float, valor_hora: float, retencion_fuente_porcentaje: float):
        """Inicializa los datos del empleado."""
        self.horas_semana = horas_semana
        self.valor_hora = valor_hora
        self.retencion_fuente_porcentaje = retencion_fuente_porcentaje

    def calcular_salario_bruto(self):
        """Calcula el salario bruto."""
        return self.horas_semana * self.valor_hora

    def calcular_retencion_fuente(self):
        """Calcula la retención en la fuente."""
        return self.calcular_salario_bruto() * (self.retencion_fuente_porcentaje / 100)

    def calcular_salario_neto(self):
        """Calcula el salario neto."""
        return self.calcular_salario_bruto() - self.calcular_retencion_fuente()

    def imprimir_informacion(self):
        """Imprime toda la información del empleado."""
        bruto = self.calcular_salario_bruto()
        retencion = self.calcular_retencion_fuente()
        neto = self.calcular_salario_neto()
        print(f"Salario Bruto: ${bruto:,.2f}")
        print(f"Retención en la fuente: ${retencion:,.2f}")
        print(f"Salario Neto: ${neto:,.2f}")

if __name__ == "__main__":
    empleado = Empleado(48, 5000, 12.5)
    empleado.imprimir_informacion()
