import tkinter as tk
from tkinter import ttk, messagebox

class Vendedor:
    def __init__(self, nombre: str, apellidos: str, edad: int):
        if not nombre.strip():
            raise ValueError("El nombre del vendedor no puede estar vacio.")
        if not apellidos.strip():
            raise ValueError("Los apellidos del vendedor no pueden estar vacios.")
        self.nombre = nombre.strip()
        self.apellidos = apellidos.strip()
        self.edad = 0
        self.verificar_edad(edad)

    def verificar_edad(self, edad: int):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 anos.")
        self.edad = edad

    def obtener_resumen(self) -> str:
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad} anos"


class VentanaVendedor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.5 - Registro de Vendedor")
        self.geometry("420x410")
        self.resizable(False, False)
        self.vendedor_actual = None
        self._construir_ui()

    def _construir_ui(self):
        marco = ttk.Frame(self, padding="20")
        marco.pack(fill=tk.BOTH, expand=True)

        lbl_titulo = ttk.Label(marco, text="Registro de Vendedor", font=("Segoe UI", 14, "bold"))
        lbl_titulo.pack(pady=(0, 15))

        marco_form = ttk.LabelFrame(marco, text="Datos del Vendedor", padding="12")
        marco_form.pack(fill=tk.X, pady=5)

        ttk.Label(marco_form, text="Nombre:").grid(row=0, column=0, sticky=tk.W, pady=4)
        self.txt_nombre = ttk.Entry(marco_form, width=25)
        self.txt_nombre.grid(row=0, column=1, sticky=tk.W, padx=5, pady=4)

        ttk.Label(marco_form, text="Apellidos:").grid(row=1, column=0, sticky=tk.W, pady=4)
        self.txt_apellidos = ttk.Entry(marco_form, width=25)
        self.txt_apellidos.grid(row=1, column=1, sticky=tk.W, padx=5, pady=4)

        ttk.Label(marco_form, text="Edad:").grid(row=2, column=0, sticky=tk.W, pady=4)
        self.txt_edad = ttk.Entry(marco_form, width=10)
        self.txt_edad.grid(row=2, column=1, sticky=tk.W, padx=5, pady=4)

        marco_btn = ttk.Frame(marco)
        marco_btn.pack(fill=tk.X, pady=12)

        btn_registrar = ttk.Button(marco_btn, text="Registrar", command=self._accion_registrar)
        btn_registrar.pack(side=tk.LEFT, padx=5)

        btn_limpiar = ttk.Button(marco_btn, text="Limpiar", command=self._accion_limpiar)
        btn_limpiar.pack(side=tk.LEFT, padx=5)

        self.marco_resumen = ttk.LabelFrame(marco, text="Estado del Registro", padding="10")
        self.marco_resumen.pack(fill=tk.BOTH, expand=True, pady=5)

        self.lbl_estado = ttk.Label(self.marco_resumen, text="Ingrese datos y presione Registrar.", font=("Segoe UI", 9))
        self.lbl_estado.pack(anchor=tk.W)

    def _accion_registrar(self):
        nombre = self.txt_nombre.get()
        apellidos = self.txt_apellidos.get()
        edad_str = self.txt_edad.get().strip()

        try:
            if not edad_str:
                raise ValueError("Debe ingresar un valor numerico para la edad.")
            if not edad_str.lstrip("-").isdigit():
                raise ValueError("La edad debe ser un numero entero.")
            edad = int(edad_str)
            self.vendedor_actual = Vendedor(nombre, apellidos, edad)
            info = self.vendedor_actual.obtener_resumen()
            self.lbl_estado.config(text=f"Registro exitoso:\n{info}", foreground="green")
            messagebox.showinfo("Exito", "Vendedor registrado correctamente.")
        except ValueError as err:
            self.lbl_estado.config(text=f"Error: {err}", foreground="red")
            messagebox.showerror("Error de Validacion", str(err))

    def _accion_limpiar(self):
        self.txt_nombre.delete(0, tk.END)
        self.txt_apellidos.delete(0, tk.END)
        self.txt_edad.delete(0, tk.END)
        self.lbl_estado.config(text="Formulario reiniciado.", foreground="black")
        self.vendedor_actual = None


if __name__ == "__main__":
    app = VentanaVendedor()
    app.mainloop()

