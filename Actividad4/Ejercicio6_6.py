import math
import tkinter as tk
from tkinter import ttk, messagebox

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo(valor: float) -> float:
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un numero positivo mayor a cero para calcular el logaritmo neperiano.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz(valor: float) -> float:
        if valor < 0:
            raise ArithmeticError("El valor debe ser un numero no negativo para calcular la raiz cuadrada.")
        return math.sqrt(valor)


class VentanaCalculos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.6 - Calculos Numericos y Catchs Multiples")
        self.geometry("460x380")
        self.resizable(False, False)
        self._construir_ui()

    def _construir_ui(self):
        marco = ttk.Frame(self, padding="20")
        marco.pack(fill=tk.BOTH, expand=True)

        lbl_titulo = ttk.Label(marco, text="Calculos Numericos y Excepciones Multiples", font=("Segoe UI", 12, "bold"))
        lbl_titulo.pack(pady=(0, 15))

        marco_entrada = ttk.LabelFrame(marco, text="Entrada de Datos", padding="12")
        marco_entrada.pack(fill=tk.X, pady=5)

        ttk.Label(marco_entrada, text="Ingrese un valor numerico:").grid(row=0, column=0, sticky=tk.W, pady=4)
        self.txt_valor = ttk.Entry(marco_entrada, width=18)
        self.txt_valor.grid(row=0, column=1, sticky=tk.W, padx=8, pady=4)

        marco_botones = ttk.Frame(marco)
        marco_botones.pack(fill=tk.X, pady=12)

        btn_log = ttk.Button(marco_botones, text="Logaritmo Neperiano", command=self._accion_logaritmo)
        btn_log.pack(side=tk.LEFT, padx=4)

        btn_raiz = ttk.Button(marco_botones, text="Raiz Cuadrada", command=self._accion_raiz)
        btn_raiz.pack(side=tk.LEFT, padx=4)

        btn_limpiar = ttk.Button(marco_botones, text="Limpiar", command=self._accion_limpiar)
        btn_limpiar.pack(side=tk.LEFT, padx=4)

        self.marco_salida = ttk.LabelFrame(marco, text="Resultado y Captura de Excepciones", padding="12")
        self.marco_salida.pack(fill=tk.BOTH, expand=True, pady=5)

        self.lbl_resultado = ttk.Label(self.marco_salida, text="Resultado = ", font=("Segoe UI", 10))
        self.lbl_resultado.pack(anchor=tk.W, pady=2)

        self.lbl_diagnostico = ttk.Label(self.marco_salida, text="Estado: En espera de operacion.", font=("Segoe UI", 9), foreground="gray")
        self.lbl_diagnostico.pack(anchor=tk.W, pady=2)

    def _obtener_numero(self) -> float:
        texto = self.txt_valor.get().strip()
        if not texto:
            raise ValueError("El campo de valor se encuentra vacio.")
        try:
            return float(texto)
        except ValueError as e:
            raise ValueError("El dato ingresado no es numerico.") from e

    def _accion_logaritmo(self):
        try:
            val = self._obtener_numero()
            res = CalculosNumericos.calcular_logaritmo(val)
            self.lbl_resultado.config(text=f"Resultado = {res:.6f}")
            self.lbl_diagnostico.config(text="Operacion exitosa sin excepciones.", foreground="green")
        except ValueError as e:
            self.lbl_resultado.config(text="Resultado = Error")
            self.lbl_diagnostico.config(text=f"Catch ValueError: {e}", foreground="red")
            messagebox.showerror("Error de Formato", str(e))
        except ArithmeticError as e:
            self.lbl_resultado.config(text="Resultado = Error")
            self.lbl_diagnostico.config(text=f"Catch ArithmeticError: {e}", foreground="red")
            messagebox.showerror("Error Matematico", str(e))
        except Exception as e:
            self.lbl_resultado.config(text="Resultado = Error")
            self.lbl_diagnostico.config(text=f"Catch Exception: {e}", foreground="red")
            messagebox.showerror("Error Desconocido", str(e))

    def _accion_raiz(self):
        try:
            val = self._obtener_numero()
            res = CalculosNumericos.calcular_raiz(val)
            self.lbl_resultado.config(text=f"Resultado = {res:.6f}")
            self.lbl_diagnostico.config(text="Operacion exitosa sin excepciones.", foreground="green")
        except ValueError as e:
            self.lbl_resultado.config(text="Resultado = Error")
            self.lbl_diagnostico.config(text=f"Catch ValueError: {e}", foreground="red")
            messagebox.showerror("Error de Formato", str(e))
        except ArithmeticError as e:
            self.lbl_resultado.config(text="Resultado = Error")
            self.lbl_diagnostico.config(text=f"Catch ArithmeticError: {e}", foreground="red")
            messagebox.showerror("Error Matematico", str(e))
        except Exception as e:
            self.lbl_resultado.config(text="Resultado = Error")
            self.lbl_diagnostico.config(text=f"Catch Exception: {e}", foreground="red")
            messagebox.showerror("Error Desconocido", str(e))

    def _accion_limpiar(self):
        self.txt_valor.delete(0, tk.END)
        self.lbl_resultado.config(text="Resultado = ")
        self.lbl_diagnostico.config(text="Estado: En espera de operacion.", foreground="gray")


if __name__ == "__main__":
    app = VentanaCalculos()
    app.mainloop()

