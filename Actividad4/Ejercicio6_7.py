import tkinter as tk
from tkinter import ttk, messagebox

class Programador:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = self._validar_campo(nombre, "Nombre")
        self.apellidos = self._validar_campo(apellidos, "Apellidos")

    @staticmethod
    def _validar_campo(valor: str, nombre_campo: str) -> str:
        limpio = valor.strip()
        if not limpio:
            raise ValueError(f"El campo '{nombre_campo}' no puede estar vacio.")
        if len(limpio) > 20:
            raise ValueError(f"La longitud de '{nombre_campo}' no debe ser superior a 20 caracteres.")
        if any(char.isdigit() for char in limpio):
            raise ValueError(f"El campo '{nombre_campo}' no puede contener caracteres numericos.")
        return limpio


class EquipoMaratonProgramacion:
    CAPACIDAD_MAXIMA = 3

    def __init__(self, nombre_equipo: str, universidad: str, lenguaje: str):
        if not nombre_equipo.strip():
            raise ValueError("El nombre del equipo no puede estar vacio.")
        if not universidad.strip():
            raise ValueError("El nombre de la universidad no puede estar vacio.")
        if not lenguaje.strip():
            raise ValueError("El lenguaje de programacion no puede estar vacio.")
        if len(nombre_equipo.strip()) > 20:
            raise ValueError("El nombre del equipo no debe superar 20 caracteres.")
        if len(universidad.strip()) > 20:
            raise ValueError("La universidad no debe superar 20 caracteres.")
        if len(lenguaje.strip()) > 20:
            raise ValueError("El lenguaje no debe superar 20 caracteres.")

        self.nombre_equipo = nombre_equipo.strip()
        self.universidad = universidad.strip()
        self.lenguaje = lenguaje.strip()
        self.programadores: list[Programador] = []

    def esta_lleno(self) -> bool:
        return len(self.programadores) >= self.CAPACIDAD_MAXIMA

    def anadir_programador(self, programador: Programador):
        if self.esta_lleno():
            raise OverflowError("El equipo de programacion esta completo (maximo 3 integrantes).")
        self.programadores.append(programador)


class VentanaEquipoMaraton(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.7 - Equipo de Maraton de Programacion")
        self.geometry("540x550")
        self.resizable(False, False)
        self.equipo = None
        self._construir_ui()

    def _construir_ui(self):
        marco = ttk.Frame(self, padding="15")
        marco.pack(fill=tk.BOTH, expand=True)

        lbl_titulo = ttk.Label(marco, text="Registro y Validacion de Equipo", font=("Segoe UI", 13, "bold"))
        lbl_titulo.pack(pady=(0, 10))

        marco_equipo = ttk.LabelFrame(marco, text="Datos del Equipo", padding="10")
        marco_equipo.pack(fill=tk.X, pady=5)

        ttk.Label(marco_equipo, text="Nombre Equipo:").grid(row=0, column=0, sticky=tk.W, pady=3)
        self.txt_nombre_eq = ttk.Entry(marco_equipo, width=22)
        self.txt_nombre_eq.grid(row=0, column=1, padx=5, pady=3)

        ttk.Label(marco_equipo, text="Universidad:").grid(row=0, column=2, sticky=tk.W, padx=(10, 0), pady=3)
        self.txt_universidad = ttk.Entry(marco_equipo, width=22)
        self.txt_universidad.grid(row=0, column=3, padx=5, pady=3)

        ttk.Label(marco_equipo, text="Lenguaje:").grid(row=1, column=0, sticky=tk.W, pady=3)
        self.txt_lenguaje = ttk.Entry(marco_equipo, width=22)
        self.txt_lenguaje.grid(row=1, column=1, padx=5, pady=3)

        btn_crear_eq = ttk.Button(marco_equipo, text="Crear/Actualizar Equipo", command=self._accion_crear_equipo)
        btn_crear_eq.grid(row=1, column=2, columnspan=2, sticky=tk.EW, padx=5, pady=3)

        marco_prog = ttk.LabelFrame(marco, text="Anadir Programador (Max. 3)", padding="10")
        marco_prog.pack(fill=tk.X, pady=8)

        ttk.Label(marco_prog, text="Nombre:").grid(row=0, column=0, sticky=tk.W, pady=3)
        self.txt_prog_nombre = ttk.Entry(marco_prog, width=22)
        self.txt_prog_nombre.grid(row=0, column=1, padx=5, pady=3)

        ttk.Label(marco_prog, text="Apellidos:").grid(row=0, column=2, sticky=tk.W, padx=(10, 0), pady=3)
        self.txt_prog_apellidos = ttk.Entry(marco_prog, width=22)
        self.txt_prog_apellidos.grid(row=0, column=3, padx=5, pady=3)

        marco_btn_prog = ttk.Frame(marco_prog)
        marco_btn_prog.grid(row=1, column=0, columnspan=4, pady=(8, 2))

        btn_anadir = ttk.Button(marco_btn_prog, text="Anadir Programador", command=self._accion_anadir_prog)
        btn_anadir.pack(side=tk.LEFT, padx=5)

        btn_limpiar_p = ttk.Button(marco_btn_prog, text="Limpiar Campos", command=self._accion_limpiar_campos)
        btn_limpiar_p.pack(side=tk.LEFT, padx=5)

        btn_reiniciar = ttk.Button(marco_btn_prog, text="Reiniciar Todo", command=self._accion_reiniciar)
        btn_reiniciar.pack(side=tk.LEFT, padx=5)

        marco_lista = ttk.LabelFrame(marco, text="Programadores Inscritos", padding="10")
        marco_lista.pack(fill=tk.BOTH, expand=True, pady=5)

        self.lbl_conteo = ttk.Label(marco_lista, text="Integrantes registrados: 0 / 3", font=("Segoe UI", 9, "bold"))
        self.lbl_conteo.pack(anchor=tk.W, pady=(0, 5))

        columnas = ("num", "nombre", "apellidos")
        self.tabla = ttk.Treeview(marco_lista, columns=columnas, show="headings", height=4)
        self.tabla.heading("num", text="#")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("apellidos", text="Apellidos")
        self.tabla.column("num", width=40, anchor=tk.CENTER)
        self.tabla.column("nombre", width=200)
        self.tabla.column("apellidos", width=200)
        self.tabla.pack(fill=tk.BOTH, expand=True)

    def _accion_crear_equipo(self):
        try:
            nom = self.txt_nombre_eq.get()
            uni = self.txt_universidad.get()
            leng = self.txt_lenguaje.get()
            self.equipo = EquipoMaratonProgramacion(nom, uni, leng)
            self._actualizar_tabla()
            messagebox.showinfo("Equipo Creado", f"Equipo '{nom}' inicializado correctamente.")
        except ValueError as e:
            messagebox.showerror("Error de Validacion", str(e))

    def _accion_anadir_prog(self):
        if not self.equipo:
            messagebox.showerror("Error", "Primero debe crear e inicializar los datos del equipo.")
            return

        try:
            nombre = self.txt_prog_nombre.get()
            apellidos = self.txt_prog_apellidos.get()
            nuevo_p = Programador(nombre, apellidos)
            self.equipo.anadir_programador(nuevo_p)
            self._actualizar_tabla()
            self.txt_prog_nombre.delete(0, tk.END)
            self.txt_prog_apellidos.delete(0, tk.END)
            messagebox.showinfo("Programador Anadido", "Integrante registrado con exito.")
        except (ValueError, OverflowError) as e:
            messagebox.showerror("Excepcion Capturada", str(e))

    def _actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        if self.equipo:
            for idx, p in enumerate(self.equipo.programadores, start=1):
                self.tabla.insert("", tk.END, values=(idx, p.nombre, p.apellidos))
            total = len(self.equipo.programadores)
            self.lbl_conteo.config(text=f"Integrantes registrados: {total} / {self.equipo.CAPACIDAD_MAXIMA}")
        else:
            self.lbl_conteo.config(text="Integrantes registrados: 0 / 3")

    def _accion_limpiar_campos(self):
        self.txt_prog_nombre.delete(0, tk.END)
        self.txt_prog_apellidos.delete(0, tk.END)

    def _accion_reiniciar(self):
        self.txt_nombre_eq.delete(0, tk.END)
        self.txt_universidad.delete(0, tk.END)
        self.txt_lenguaje.delete(0, tk.END)
        self.txt_prog_nombre.delete(0, tk.END)
        self.txt_prog_apellidos.delete(0, tk.END)
        self.equipo = None
        self._actualizar_tabla()


if __name__ == "__main__":
    app = VentanaEquipoMaraton()
    app.mainloop()

