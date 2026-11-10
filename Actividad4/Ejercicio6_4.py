import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class OperacionesExcepciones:
    def __init__(self):
        self.registro = []

    def log(self, mensaje: str):
        self.registro.append(mensaje)

    def ejecutar_division(self, num_str: str, den_str: str) -> tuple[float | None, list[str]]:
        self.registro = []
        resultado = None
        self.log("Ingresando al bloque try de division.")
        try:
            num = float(num_str)
            den = float(den_str)
            resultado = num / den
            self.log(f"Division exitosa: {num} / {den} = {resultado}")
        except ZeroDivisionError as e:
            self.log("Excepcion capturada: ZeroDivisionError (Division por cero).")
            raise ZeroDivisionError("No es posible dividir por cero.") from e
        except ValueError as e:
            self.log("Excepcion capturada: ValueError (Los valores deben ser numericos).")
            raise ValueError("Ingrese valores numericos validos.") from e
        finally:
            self.log("Ingresando al bloque finally de division (se ejecuta siempre).")
        return resultado, self.registro

    def ejecutar_objeto_nulo(self) -> list[str]:
        self.registro = []
        self.log("Ingresando al bloque try de acceso a objeto.")
        try:
            objeto = None
            self.log("Intentando llamar metodo sobre objeto None.")
            objeto.metodo_inexistente()
        except AttributeError as e:
            self.log("Excepcion capturada: AttributeError (Objeto nulo no tiene atributos).")
            raise AttributeError("Intento de acceso a miembro de un objeto None.") from e
        except Exception as e:
            self.log("Excepcion capturada: Exception general.")
            raise Exception("Ocurrio una excepcion general.") from e
        finally:
            self.log("Ingresando al bloque finally de objeto (se ejecuta siempre).")
        return self.registro


class VentanaExcepciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.4 - Manejo de Excepciones")
        self.geometry("520x540")
        self.resizable(False, False)
        self.operaciones = OperacionesExcepciones()
        self._construir_ui()

    def _construir_ui(self):
        marco_principal = ttk.Frame(self, padding="15")
        marco_principal.pack(fill=tk.BOTH, expand=True)

        lbl_titulo = ttk.Label(marco_principal, text="Demostracion de Bloques Try - Catch - Finally", font=("Segoe UI", 13, "bold"))
        lbl_titulo.pack(pady=(0, 15))

        marco_campos = ttk.LabelFrame(marco_principal, text="Division Aritmetica", padding="10")
        marco_campos.pack(fill=tk.X, pady=5)

        ttk.Label(marco_campos, text="Numerador:").grid(row=0, column=0, sticky=tk.W, pady=3)
        self.txt_numerador = ttk.Entry(marco_campos, width=15)
        self.txt_numerador.grid(row=0, column=1, sticky=tk.W, padx=5, pady=3)
        self.txt_numerador.insert(0, "10000")

        ttk.Label(marco_campos, text="Denominador:").grid(row=1, column=0, sticky=tk.W, pady=3)
        self.txt_denominador = ttk.Entry(marco_campos, width=15)
        self.txt_denominador.grid(row=1, column=1, sticky=tk.W, padx=5, pady=3)
        self.txt_denominador.insert(0, "0")

        marco_botones = ttk.Frame(marco_principal)
        marco_botones.pack(fill=tk.X, pady=10)

        btn_dividir = ttk.Button(marco_botones, text="Ejecutar Division", command=self._accion_dividir)
        btn_dividir.pack(side=tk.LEFT, padx=3)

        btn_nulo = ttk.Button(marco_botones, text="Probar Objeto Nulo", command=self._accion_objeto_nulo)
        btn_nulo.pack(side=tk.LEFT, padx=3)

        btn_limpiar = ttk.Button(marco_botones, text="Limpiar Consola", command=self._accion_limpiar)
        btn_limpiar.pack(side=tk.LEFT, padx=3)

        ttk.Label(marco_principal, text="Traza de Ejecucion (Consola):", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W, pady=(5, 2))
        self.txt_consola = scrolledtext.ScrolledText(marco_principal, width=58, height=14, font=("Consolas", 9))
        self.txt_consola.pack(fill=tk.BOTH, expand=True)

    def _imprimir_consola(self, lineas: list[str], es_error: bool = False, msg_error: str = ""):
        for linea in lineas:
            self.txt_consola.insert(tk.END, f"> {linea}\n")
        if es_error:
            self.txt_consola.insert(tk.END, f"[ERROR GESTIONADO]: {msg_error}\n")
        self.txt_consola.insert(tk.END, "-" * 55 + "\n")
        self.txt_consola.see(tk.END)

    def _accion_dividir(self):
        num = self.txt_numerador.get().strip()
        den = self.txt_denominador.get().strip()
        try:
            _, reg = self.operaciones.ejecutar_division(num, den)
            self._imprimir_consola(reg)
        except (ZeroDivisionError, ValueError) as err:
            self._imprimir_consola(self.operaciones.registro, es_error=True, msg_error=str(err))
            messagebox.showerror("Error de Ejecucion", str(err))

    def _accion_objeto_nulo(self):
        try:
            reg = self.operaciones.ejecutar_objeto_nulo()
            self._imprimir_consola(reg)
        except (AttributeError, Exception) as err:
            self._imprimir_consola(self.operaciones.registro, es_error=True, msg_error=str(err))
            messagebox.showwarning("Excepcion de Objeto", str(err))

    def _accion_limpiar(self):
        self.txt_consola.delete("1.0", tk.END)


if __name__ == "__main__":
    app = VentanaExcepciones()
    app.mainloop()

