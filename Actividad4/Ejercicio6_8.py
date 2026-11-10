import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext

class LectorArchivo:
    @staticmethod
    def leer_archivo(ruta: str) -> tuple[str, int, int]:
        if not ruta.strip():
            raise ValueError("La ruta del archivo no puede estar vacia.")
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"El archivo especificado no existe: {ruta}")
        if not os.path.isfile(ruta):
            raise IOError(f"La ruta indicada no corresponde a un archivo valido: {ruta}")

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                contenido = "".join(lineas)
                total_lineas = len(lineas)
                total_caracteres = sum(len(linea) for linea in lineas)
                return contenido, total_lineas, total_caracteres
        except UnicodeDecodeError:
            with open(ruta, "r", encoding="latin-1") as archivo:
                lineas = archivo.readlines()
                contenido = "".join(lineas)
                return contenido, len(lineas), sum(len(linea) for linea in lineas)
        except PermissionError as e:
            raise PermissionError("Permiso denegado al intentar abrir el archivo.") from e
        except Exception as e:
            raise IOError(f"Ocurrio un error de entrada/salida al leer el archivo: {e}") from e

    @staticmethod
    def convertir_mayusculas(texto: str) -> str:
        return texto.upper()


class VentanaLeerArchivo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.8 - Lectura de Archivos")
        self.geometry("560x520")
        self.resizable(False, False)
        self.lector = LectorArchivo()
        self.contenido_cargado = ""
        self._construir_ui()

    def _construir_ui(self):
        marco = ttk.Frame(self, padding="15")
        marco.pack(fill=tk.BOTH, expand=True)

        lbl_titulo = ttk.Label(marco, text="Lectura y Visualizacion de Archivos de Texto", font=("Segoe UI", 12, "bold"))
        lbl_titulo.pack(pady=(0, 10))

        marco_ruta = ttk.LabelFrame(marco, text="Ubicacion del Archivo", padding="10")
        marco_ruta.pack(fill=tk.X, pady=5)

        self.txt_ruta = ttk.Entry(marco_ruta, width=42)
        self.txt_ruta.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)

        btn_examinar = ttk.Button(marco_ruta, text="Examinar...", command=self._accion_examinar)
        btn_examinar.pack(side=tk.LEFT)

        marco_acciones = ttk.Frame(marco)
        marco_acciones.pack(fill=tk.X, pady=8)

        btn_leer = ttk.Button(marco_acciones, text="Leer Archivo", command=self._accion_leer)
        btn_leer.pack(side=tk.LEFT, padx=3)

        btn_mayus = ttk.Button(marco_acciones, text="A Mayusculas", command=self._accion_mayusculas)
        btn_mayus.pack(side=tk.LEFT, padx=3)

        btn_limpiar = ttk.Button(marco_acciones, text="Limpiar", command=self._accion_limpiar)
        btn_limpiar.pack(side=tk.LEFT, padx=3)

        ttk.Label(marco, text="Contenido del Archivo:", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W, pady=(5, 2))
        self.txt_contenido = scrolledtext.ScrolledText(marco, width=64, height=14, font=("Consolas", 9))
        self.txt_contenido.pack(fill=tk.BOTH, expand=True)

        self.lbl_estado = ttk.Label(marco, text="Estado: Seleccione un archivo para comenzar.", font=("Segoe UI", 9))
        self.lbl_estado.pack(anchor=tk.W, pady=(6, 0))

    def _accion_examinar(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto (*.txt)", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            self.txt_ruta.delete(0, tk.END)
            self.txt_ruta.insert(0, ruta)

    def _accion_leer(self):
        ruta = self.txt_ruta.get().strip()
        try:
            contenido, lineas, caracteres = self.lector.leer_archivo(ruta)
            self.contenido_cargado = contenido
            self.txt_contenido.delete("1.0", tk.END)
            self.txt_contenido.insert(tk.END, contenido)
            self.lbl_estado.config(
                text=f"Lectura exitosa: {lineas} lineas, {caracteres} caracteres.",
                foreground="green"
            )
        except (ValueError, FileNotFoundError, PermissionError, IOError) as e:
            self.txt_contenido.delete("1.0", tk.END)
            self.lbl_estado.config(text=f"Error: {e}", foreground="red")
            messagebox.showerror("Error de Lectura", str(e))

    def _accion_mayusculas(self):
        if not self.contenido_cargado:
            messagebox.showwarning("Atencion", "No hay contenido cargado para transformar.")
            return
        texto_mayus = self.lector.convertir_mayusculas(self.contenido_cargado)
        self.txt_contenido.delete("1.0", tk.END)
        self.txt_contenido.insert(tk.END, texto_mayus)
        self.lbl_estado.config(text="Contenido transformado a mayusculas.", foreground="blue")

    def _accion_limpiar(self):
        self.txt_ruta.delete(0, tk.END)
        self.txt_contenido.delete("1.0", tk.END)
        self.contenido_cargado = ""
        self.lbl_estado.config(text="Estado: Formulario reiniciado.", foreground="black")


if __name__ == "__main__":
    app = VentanaLeerArchivo()
    app.mainloop()

