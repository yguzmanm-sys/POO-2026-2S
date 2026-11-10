import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = r"C:\Users\USUARIO\Documents\POO\Actividad4\figuras"
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

def draw_window_frame(ax, title, width, height, x=0.05, y=0.05):
    header_h = 0.08
    shadow = patches.FancyBboxPatch((x+0.01, y-0.01), width, height, boxstyle="round,pad=0.01",
                                    facecolor="#d0d0d0", edgecolor="none", zorder=1)
    ax.add_patch(shadow)
    body = patches.FancyBboxPatch((x, y), width, height - header_h, boxstyle="square,pad=0",
                                  facecolor="#f8f9fa", edgecolor="#6c757d", linewidth=1.5, zorder=2)
    ax.add_patch(body)
    header = patches.FancyBboxPatch((x, y + height - header_h), width, header_h,
                                    boxstyle="round,pad=0,rounding_size=0.02",
                                    facecolor="#2b303a", edgecolor="#6c757d", linewidth=1.5, zorder=3)
    ax.add_patch(header)
    ax.text(x + 0.03, y + height - header_h/2, title, color="white", weight="bold",
            fontsize=10, va="center", zorder=4)
    # Window control dots
    for i, c in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        dot = patches.Circle((x + width - 0.08 + i*0.025, y + height - header_h/2), 0.009,
                             facecolor=c, edgecolor="none", zorder=4)
        ax.add_patch(dot)

def draw_button(ax, x, y, w, h, text, color="#0d6efd", text_color="white", fontsize=9):
    btn = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.015",
                                 facecolor=color, edgecolor="#495057", linewidth=0.8, zorder=5)
    ax.add_patch(btn)
    ax.text(x + w/2, y + h/2, text, color=text_color, weight="bold",
            fontsize=fontsize, ha="center", va="center", zorder=6)

def draw_entry(ax, x, y, w, h, text=""):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0",
                                 facecolor="white", edgecolor="#ced4da", linewidth=1.2, zorder=4)
    ax.add_patch(box)
    if text:
        ax.text(x + 0.015, y + h/2, text, color="#212529", fontsize=9, va="center", zorder=5)

def draw_actor(ax, x, y, label="Usuario"):
    # Head
    head = patches.Circle((x, y + 0.06), 0.025, facecolor="#f8f9fa", edgecolor="#212529", linewidth=1.8, zorder=5)
    ax.add_patch(head)
    # Body
    ax.plot([x, x], [y + 0.035, y - 0.02], color="#212529", linewidth=2, zorder=5)
    # Arms
    ax.plot([x - 0.035, x + 0.035], [y + 0.015, y + 0.015], color="#212529", linewidth=2, zorder=5)
    # Legs
    ax.plot([x, x - 0.03], [y - 0.02, y - 0.07], color="#212529", linewidth=2, zorder=5)
    ax.plot([x, x + 0.03], [y - 0.02, y - 0.07], color="#212529", linewidth=2, zorder=5)
    ax.text(x, y - 0.09, label, ha="center", va="top", weight="bold", fontsize=10, zorder=5)

def draw_use_case(ax, x, y, w, h, text):
    oval = patches.Ellipse((x, y), w, h, facecolor="#e8f4fd", edgecolor="#0b5ed7", linewidth=1.5, zorder=4)
    ax.add_patch(oval)
    ax.text(x, y, text, ha="center", va="center", fontsize=8.5, weight="semibold", color="#084298", zorder=5)

def draw_uml_class(ax, x, y, w, h, class_name, attributes, methods, is_interface=False):
    # Overall box
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0",
                                 facecolor="#ffffff", edgecolor="#1a1a1a", linewidth=1.6, zorder=3)
    ax.add_patch(box)
    
    header_h = 0.22 * h
    attr_h = 0.38 * h
    meth_h = h - header_h - attr_h
    
    # Header
    header = patches.Rectangle((x, y + h - header_h), w, header_h,
                               facecolor="#e2e8f0", edgecolor="#1a1a1a", linewidth=1.2, zorder=4)
    ax.add_patch(header)
    
    prefix = "<<interface>>\n" if is_interface else ""
    ax.text(x + w/2, y + h - header_h/2, prefix + class_name, weight="bold",
            ha="center", va="center", fontsize=9.5, zorder=5)
    
    # Attributes line
    ax.plot([x, x + w], [y + h - header_h, y + h - header_h], color="#1a1a1a", linewidth=1.2, zorder=4)
    y_attr = y + h - header_h - 0.03
    for attr in attributes:
        ax.text(x + 0.015, y_attr, attr, fontsize=8, family="monospace", va="top", zorder=5)
        y_attr -= 0.035
        
    # Methods line
    y_meth_line = y + meth_h
    ax.plot([x, x + w], [y_meth_line, y_meth_line], color="#1a1a1a", linewidth=1.2, zorder=4)
    y_meth = y_meth_line - 0.03
    for meth in methods:
        ax.text(x + 0.015, y_meth, meth, fontsize=8, family="monospace", va="top", zorder=5)
        y_meth -= 0.035

# ==================== FIGURAS EJERCICIO 6.4 ====================
def gen_6_4():
    # UI
    fig, ax = plt.subplots(figsize=(6, 6.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    draw_window_frame(ax, "Ejercicio 6.4 - Manejo de Excepciones", 0.9, 0.9, 0.05, 0.05)
    
    ax.text(0.5, 0.86, "Demostracion de Bloques Try - Catch - Finally", ha="center", weight="bold", fontsize=11, color="#1e293b")
    
    # Box division
    frame1 = patches.Rectangle((0.1, 0.63), 0.8, 0.2, facecolor="#ffffff", edgecolor="#adb5bd", linewidth=1, zorder=3)
    ax.add_patch(frame1)
    ax.text(0.13, 0.81, "Division Aritmetica", weight="bold", fontsize=9, color="#495057")
    
    ax.text(0.14, 0.76, "Numerador:", fontsize=9, va="center")
    draw_entry(ax, 0.35, 0.73, 0.22, 0.06, "10000")
    
    ax.text(0.14, 0.67, "Denominador:", fontsize=9, va="center")
    draw_entry(ax, 0.35, 0.64, 0.22, 0.06, "0")
    
    # Buttons
    draw_button(ax, 0.1, 0.54, 0.25, 0.065, "Ejecutar Division", "#0d6efd")
    draw_button(ax, 0.375, 0.54, 0.27, 0.065, "Probar Objeto Nulo", "#ffc107", text_color="#212529")
    draw_button(ax, 0.67, 0.54, 0.23, 0.065, "Limpiar Consola", "#6c757d")
    
    # Terminal
    ax.text(0.1, 0.49, "Traza de Ejecucion (Consola):", weight="bold", fontsize=9)
    term = patches.Rectangle((0.1, 0.1), 0.8, 0.37, facecolor="#1e1e1e", edgecolor="#343a40", zorder=3)
    ax.add_patch(term)
    
    lines = [
        "> Ingresando al bloque try de division.",
        "> Excepcion capturada: ZeroDivisionError (Division por cero).",
        "> Ingresando al bloque finally de division (se ejecuta siempre).",
        "[ERROR GESTIONADO]: No es posible dividir por cero.",
        "-------------------------------------------------------",
        "> Ingresando al bloque try de acceso a objeto.",
        "> Intentando llamar metodo sobre objeto None.",
        "> Excepcion capturada: AttributeError (Objeto nulo).",
        "> Ingresando al bloque finally de objeto (se ejecuta siempre).",
        "[ERROR GESTIONADO]: Intento de acceso a miembro de un objeto None."
    ]
    y_t = 0.44
    for l in lines:
        c = "#f87171" if "ERROR" in l or "capturada" in l else ("#4ade80" if "finally" in l else "#e2e8f0")
        ax.text(0.12, y_t, l, fontsize=7.2, family="monospace", color=c, zorder=5)
        y_t -= 0.033
        
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "ui_ejercicio6_4.png"), dpi=300)
    plt.close()

    # Clases
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_uml_class(ax, 0.05, 0.15, 0.42, 0.7, "OperacionesExcepciones",
                   ["- registro: list[str]"],
                   ["+ log(mensaje: str): void",
                    "+ ejecutar_division(num: str, den: str): tuple",
                    "+ ejecutar_objeto_nulo(): list[str]"])
                    
    draw_uml_class(ax, 0.55, 0.15, 0.4, 0.7, "VentanaExcepciones",
                   ["- operaciones: OperacionesExcepciones",
                    "- txt_numerador: Entry",
                    "- txt_denominador: Entry",
                    "- txt_consola: ScrolledText"],
                   ["+ _construir_ui(): void",
                    "+ _accion_dividir(): void",
                    "+ _accion_objeto_nulo(): void",
                    "+ _accion_limpiar(): void"])
                    
    # Association line
    ax.annotate("", xy=(0.47, 0.5), xytext=(0.55, 0.5),
                arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1e293b"))
    ax.text(0.51, 0.53, "usa", ha="center", fontsize=8.5, weight="bold")
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "clases_ejercicio6_4.png"), dpi=300)
    plt.close()

    # Casos de uso
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_actor(ax, 0.15, 0.52, "Usuario")
    
    system_box = patches.FancyBboxPatch((0.35, 0.08), 0.58, 0.84, boxstyle="square,pad=0",
                                        facecolor="#ffffff", edgecolor="#0b5ed7", linewidth=1.5)
    ax.add_patch(system_box)
    ax.text(0.64, 0.87, "Sistema: Manejo de Excepciones", ha="center", weight="bold", fontsize=9.5)
    
    ucs = [
        (0.64, 0.74, "Ingresar valores de division"),
        (0.64, 0.55, "Ejecutar division (Try-Catch-Finally)"),
        (0.64, 0.36, "Probar llamada a objeto nulo"),
        (0.64, 0.18, "Visualizar traza en consola")
    ]
    for x, y, label in ucs:
        draw_use_case(ax, x, y, 0.42, 0.11, label)
        ax.plot([0.18, x - 0.2], [0.52, y], color="#495057", linewidth=1.2)
        
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "casos_ejercicio6_4.png"), dpi=300)
    plt.close()

# ==================== FIGURAS EJERCICIO 6.5 ====================
def gen_6_5():
    # UI
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    draw_window_frame(ax, "Ejercicio 6.5 - Registro de Vendedor", 0.9, 0.9, 0.05, 0.05)
    
    ax.text(0.5, 0.86, "Registro de Vendedor", ha="center", weight="bold", fontsize=12, color="#1e293b")
    
    # Form frame
    form = patches.Rectangle((0.1, 0.48), 0.8, 0.33, facecolor="#ffffff", edgecolor="#adb5bd", linewidth=1, zorder=3)
    ax.add_patch(form)
    ax.text(0.13, 0.78, "Datos del Vendedor", weight="bold", fontsize=9, color="#495057")
    
    ax.text(0.15, 0.72, "Nombre:", fontsize=9, va="center")
    draw_entry(ax, 0.35, 0.69, 0.48, 0.06, "Carlos")
    
    ax.text(0.15, 0.63, "Apellidos:", fontsize=9, va="center")
    draw_entry(ax, 0.35, 0.60, 0.48, 0.06, "Gomez Montoya")
    
    ax.text(0.15, 0.54, "Edad:", fontsize=9, va="center")
    draw_entry(ax, 0.35, 0.51, 0.2, 0.06, "25")
    
    # Buttons
    draw_button(ax, 0.1, 0.39, 0.35, 0.065, "Registrar Vendedor", "#198754")
    draw_button(ax, 0.55, 0.39, 0.35, 0.065, "Limpiar Campos", "#dc3545")
    
    # Status frame
    stat = patches.Rectangle((0.1, 0.12), 0.8, 0.23, facecolor="#f1f5f9", edgecolor="#cbd5e1", linewidth=1, zorder=3)
    ax.add_patch(stat)
    ax.text(0.13, 0.31, "Estado del Registro", weight="bold", fontsize=9, color="#334155")
    
    info_text = "Registro exitoso:\nNombre: Carlos\nApellidos: Gomez Montoya\nEdad: 25 anos"
    ax.text(0.15, 0.21, info_text, fontsize=8.5, color="#15803d", weight="semibold", zorder=5)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "ui_ejercicio6_5.png"), dpi=300)
    plt.close()

    # Clases
    fig, ax = plt.subplots(figsize=(6.8, 4.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_uml_class(ax, 0.05, 0.15, 0.42, 0.7, "Vendedor",
                   ["- nombre: str",
                    "- apellidos: str",
                    "- edad: int"],
                   ["+ __init__(nom, apel, edad)",
                    "+ verificar_edad(edad: int): void",
                    "+ obtener_resumen(): str"])
                    
    draw_uml_class(ax, 0.55, 0.15, 0.4, 0.7, "VentanaVendedor",
                   ["- vendedor_actual: Vendedor",
                    "- txt_nombre: Entry",
                    "- txt_apellidos: Entry",
                    "- txt_edad: Entry"],
                   ["+ _construir_ui(): void",
                    "+ _accion_registrar(): void",
                    "+ _accion_limpiar(): void"])
                    
    ax.annotate("", xy=(0.47, 0.5), xytext=(0.55, 0.5),
                arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1e293b"))
    ax.text(0.51, 0.53, "gestiona", ha="center", fontsize=8.5, weight="bold")
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "clases_ejercicio6_5.png"), dpi=300)
    plt.close()

    # Casos de uso
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_actor(ax, 0.15, 0.52, "Usuario")
    
    system_box = patches.FancyBboxPatch((0.35, 0.08), 0.58, 0.84, boxstyle="square,pad=0",
                                        facecolor="#ffffff", edgecolor="#0b5ed7", linewidth=1.5)
    ax.add_patch(system_box)
    ax.text(0.64, 0.87, "Sistema: Registro de Vendedor", ha="center", weight="bold", fontsize=9.5)
    
    ucs = [
        (0.64, 0.74, "Ingresar datos del vendedor"),
        (0.64, 0.55, "Validar edad (>=18 y <=120)"),
        (0.64, 0.36, "Capturar excepcion de argumento"),
        (0.64, 0.18, "Visualizar ficha de registro")
    ]
    for x, y, label in ucs:
        draw_use_case(ax, x, y, 0.44, 0.11, label)
        ax.plot([0.18, x - 0.22], [0.52, y], color="#495057", linewidth=1.2)
        
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "casos_ejercicio6_5.png"), dpi=300)
    plt.close()

# ==================== FIGURAS EJERCICIO 6.6 ====================
def gen_6_6():
    # UI
    fig, ax = plt.subplots(figsize=(5.8, 5.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    draw_window_frame(ax, "Ejercicio 6.6 - Calculos Numericos", 0.9, 0.9, 0.05, 0.05)
    
    ax.text(0.5, 0.86, "Calculos Numericos y Multiples Excepciones", ha="center", weight="bold", fontsize=11, color="#1e293b")
    
    frame1 = patches.Rectangle((0.1, 0.58), 0.8, 0.22, facecolor="#ffffff", edgecolor="#adb5bd", linewidth=1, zorder=3)
    ax.add_patch(frame1)
    ax.text(0.13, 0.76, "Entrada de Datos", weight="bold", fontsize=9, color="#495057")
    
    ax.text(0.14, 0.67, "Ingrese un valor numerico:", fontsize=9, va="center")
    draw_entry(ax, 0.52, 0.64, 0.32, 0.065, "100")
    
    draw_button(ax, 0.1, 0.47, 0.29, 0.065, "Logaritmo (ln)", "#0d6efd")
    draw_button(ax, 0.41, 0.47, 0.28, 0.065, "Raiz Cuadrada", "#0d6efd")
    draw_button(ax, 0.71, 0.47, 0.19, 0.065, "Limpiar", "#6c757d")
    
    frame2 = patches.Rectangle((0.1, 0.12), 0.8, 0.31, facecolor="#f8fafc", edgecolor="#cbd5e1", linewidth=1, zorder=3)
    ax.add_patch(frame2)
    ax.text(0.13, 0.39, "Resultado y Diagnostico", weight="bold", fontsize=9, color="#334155")
    
    ax.text(0.14, 0.31, "Resultado = 4.605170", fontsize=10, weight="bold", color="#0f172a")
    ax.text(0.14, 0.22, "Estado: Operacion exitosa sin excepciones.", fontsize=8.5, color="#16a34a", weight="semibold")
    ax.text(0.14, 0.16, "Manejo: Multiples catchs (ValueError, ArithmeticError).", fontsize=8, color="#64748b")
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "ui_ejercicio6_6.png"), dpi=300)
    plt.close()

    # Clases
    fig, ax = plt.subplots(figsize=(6.8, 4.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_uml_class(ax, 0.05, 0.15, 0.42, 0.7, "CalculosNumericos",
                   [],
                   ["+ calcular_logaritmo(val): float",
                    "+ calcular_raiz(val): float"])
                    
    draw_uml_class(ax, 0.55, 0.15, 0.4, 0.7, "VentanaCalculos",
                   ["- txt_valor: Entry",
                    "- lbl_resultado: Label",
                    "- lbl_diagnostico: Label"],
                   ["+ _construir_ui(): void",
                    "+ _obtener_numero(): float",
                    "+ _accion_logaritmo(): void",
                    "+ _accion_raiz(): void",
                    "+ _accion_limpiar(): void"])
                    
    ax.annotate("", xy=(0.47, 0.5), xytext=(0.55, 0.5),
                arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1e293b"))
    ax.text(0.51, 0.53, "invoca", ha="center", fontsize=8.5, weight="bold")
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "clases_ejercicio6_6.png"), dpi=300)
    plt.close()

    # Casos de uso
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_actor(ax, 0.15, 0.52, "Usuario")
    
    system_box = patches.FancyBboxPatch((0.35, 0.08), 0.58, 0.84, boxstyle="square,pad=0",
                                        facecolor="#ffffff", edgecolor="#0b5ed7", linewidth=1.5)
    ax.add_patch(system_box)
    ax.text(0.64, 0.87, "Sistema: Calculos Numericos", ha="center", weight="bold", fontsize=9.5)
    
    ucs = [
        (0.64, 0.74, "Ingresar valor numerico"),
        (0.64, 0.55, "Calcular logaritmo neperiano"),
        (0.64, 0.36, "Calcular raiz cuadrada"),
        (0.64, 0.18, "Capturar excepciones diferenciadas")
    ]
    for x, y, label in ucs:
        draw_use_case(ax, x, y, 0.44, 0.11, label)
        ax.plot([0.18, x - 0.22], [0.52, y], color="#495057", linewidth=1.2)
        
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "casos_ejercicio6_6.png"), dpi=300)
    plt.close()

# ==================== FIGURAS EJERCICIO 6.7 ====================
def gen_6_7():
    # UI
    fig, ax = plt.subplots(figsize=(6, 6.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    draw_window_frame(ax, "Ejercicio 6.7 - Maraton de Programacion", 0.9, 0.9, 0.05, 0.05)
    
    ax.text(0.5, 0.86, "Registro y Validacion de Equipo", ha="center", weight="bold", fontsize=11, color="#1e293b")
    
    # Team frame
    frame1 = patches.Rectangle((0.1, 0.65), 0.8, 0.18, facecolor="#ffffff", edgecolor="#adb5bd", linewidth=1, zorder=3)
    ax.add_patch(frame1)
    ax.text(0.13, 0.80, "Datos del Equipo", weight="bold", fontsize=8.5, color="#495057")
    
    ax.text(0.13, 0.74, "Equipo:", fontsize=8)
    draw_entry(ax, 0.23, 0.71, 0.26, 0.05, "ByteMasters")
    
    ax.text(0.51, 0.74, "Universidad:", fontsize=8)
    draw_entry(ax, 0.64, 0.71, 0.23, 0.05, "UNAL")
    
    ax.text(0.13, 0.67, "Lenguaje:", fontsize=8)
    draw_entry(ax, 0.23, 0.64, 0.26, 0.05, "Python")
    
    draw_button(ax, 0.51, 0.64, 0.36, 0.05, "Crear/Actualizar Equipo", "#0d6efd", fontsize=8)
    
    # Programmer frame
    frame2 = patches.Rectangle((0.1, 0.44), 0.8, 0.19, facecolor="#ffffff", edgecolor="#adb5bd", linewidth=1, zorder=3)
    ax.add_patch(frame2)
    ax.text(0.13, 0.59, "Anadir Programador (Max. 3)", weight="bold", fontsize=8.5, color="#495057")
    
    ax.text(0.13, 0.53, "Nombre:", fontsize=8)
    draw_entry(ax, 0.23, 0.50, 0.26, 0.05, "Yuliana")
    
    ax.text(0.51, 0.53, "Apellidos:", fontsize=8)
    draw_entry(ax, 0.62, 0.50, 0.25, 0.05, "Guzman")
    
    draw_button(ax, 0.13, 0.44, 0.3, 0.045, "Anadir Programador", "#198754", fontsize=7.5)
    draw_button(ax, 0.45, 0.44, 0.22, 0.045, "Limpiar Campos", "#6c757d", fontsize=7.5)
    draw_button(ax, 0.69, 0.44, 0.19, 0.045, "Reiniciar", "#dc3545", fontsize=7.5)
    
    # Table frame
    frame3 = patches.Rectangle((0.1, 0.1), 0.8, 0.31, facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1, zorder=3)
    ax.add_patch(frame3)
    ax.text(0.13, 0.38, "Programadores Inscritos (2 / 3 registrados)", weight="bold", fontsize=8.5, color="#334155")
    
    # Header table
    head_tbl = patches.Rectangle((0.11, 0.31), 0.78, 0.045, facecolor="#e2e8f0", edgecolor="#94a3b8")
    ax.add_patch(head_tbl)
    ax.text(0.14, 0.33, "#", weight="bold", fontsize=8)
    ax.text(0.24, 0.33, "Nombre", weight="bold", fontsize=8)
    ax.text(0.56, 0.33, "Apellidos", weight="bold", fontsize=8)
    
    # Rows
    ax.text(0.14, 0.27, "1", fontsize=8)
    ax.text(0.24, 0.27, "Yuliana", fontsize=8)
    ax.text(0.56, 0.27, "Guzman Montoya", fontsize=8)
    
    ax.text(0.14, 0.22, "2", fontsize=8)
    ax.text(0.24, 0.22, "Carlos", fontsize=8)
    ax.text(0.56, 0.22, "Perez Gomez", fontsize=8)
    
    ax.text(0.13, 0.13, "Validaciones activas: Solo texto, max. 20 car., max. 3 integrantes.", fontsize=7.5, color="#64748b", style="italic")
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "ui_ejercicio6_7.png"), dpi=300)
    plt.close()

    # Clases
    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_uml_class(ax, 0.03, 0.45, 0.36, 0.48, "Programador",
                   ["- nombre: str",
                    "- apellidos: str"],
                   ["+ __init__(nom, apel)",
                    "+ _validar_campo(val, campo)"])
                    
    draw_uml_class(ax, 0.03, 0.04, 0.36, 0.38, "EquipoMaraton",
                   ["- nombre_equipo: str",
                    "- universidad: str",
                    "- lenguaje: str",
                    "- programadores: list"],
                   ["+ esta_lleno(): bool",
                    "+ anadir_programador(p)"])
                    
    draw_uml_class(ax, 0.52, 0.15, 0.44, 0.72, "VentanaEquipoMaraton",
                   ["- equipo: EquipoMaraton",
                    "- txt_nombre_eq: Entry",
                    "- txt_universidad: Entry",
                    "- txt_lenguaje: Entry",
                    "- tabla: Treeview"],
                   ["+ _construir_ui(): void",
                    "+ _accion_crear_equipo(): void",
                    "+ _accion_anadir_prog(): void",
                    "+ _actualizar_tabla(): void",
                    "+ _accion_reiniciar(): void"])
                    
    # Composition Programador -> Equipo
    ax.annotate("", xy=(0.21, 0.45), xytext=(0.21, 0.42),
                arrowprops=dict(arrowstyle="-", lw=1.5, color="#1e293b"))
    diamond = patches.Polygon([[0.21, 0.42], [0.20, 0.40], [0.21, 0.38], [0.22, 0.40]], closed=True,
                              facecolor="#1e293b", edgecolor="#1e293b")
    ax.add_patch(diamond)
    ax.text(0.24, 0.43, "1..3", fontsize=8, weight="bold")
    
    # Association Ventana -> Equipo
    ax.annotate("", xy=(0.39, 0.25), xytext=(0.52, 0.25),
                arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1e293b"))
    ax.text(0.45, 0.28, "gestiona", ha="center", fontsize=8.5, weight="bold")
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "clases_ejercicio6_7.png"), dpi=300)
    plt.close()

    # Casos de uso
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_actor(ax, 0.15, 0.52, "Usuario")
    
    system_box = patches.FancyBboxPatch((0.35, 0.08), 0.58, 0.84, boxstyle="square,pad=0",
                                        facecolor="#ffffff", edgecolor="#0b5ed7", linewidth=1.5)
    ax.add_patch(system_box)
    ax.text(0.64, 0.87, "Sistema: Maraton de Programacion", ha="center", weight="bold", fontsize=9.5)
    
    ucs = [
        (0.64, 0.74, "Definir datos del equipo"),
        (0.64, 0.55, "Anadir programador"),
        (0.64, 0.36, "Validar longitud y solo texto"),
        (0.64, 0.18, "Controlar cupo maximo (3 miembros)")
    ]
    for x, y, label in ucs:
        draw_use_case(ax, x, y, 0.45, 0.11, label)
        ax.plot([0.18, x - 0.22], [0.52, y], color="#495057", linewidth=1.2)
        
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "casos_ejercicio6_7.png"), dpi=300)
    plt.close()

# ==================== FIGURAS EJERCICIO 6.8 ====================
def gen_6_8():
    # UI
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    draw_window_frame(ax, "Ejercicio 6.8 - Lectura de Archivos", 0.9, 0.9, 0.05, 0.05)
    
    ax.text(0.5, 0.86, "Lectura y Visualizacion de Archivos de Texto", ha="center", weight="bold", fontsize=11, color="#1e293b")
    
    # Path frame
    frame1 = patches.Rectangle((0.1, 0.67), 0.8, 0.16, facecolor="#ffffff", edgecolor="#adb5bd", linewidth=1, zorder=3)
    ax.add_patch(frame1)
    ax.text(0.13, 0.80, "Ubicacion del Archivo", weight="bold", fontsize=8.5, color="#495057")
    
    draw_entry(ax, 0.13, 0.70, 0.52, 0.065, "C:/archivos/prueba.txt")
    draw_button(ax, 0.67, 0.70, 0.20, 0.065, "Examinar...", "#495057", fontsize=8.5)
    
    # Action buttons
    draw_button(ax, 0.1, 0.58, 0.25, 0.065, "Leer Archivo", "#0d6efd")
    draw_button(ax, 0.38, 0.58, 0.27, 0.065, "A Mayusculas", "#198754")
    draw_button(ax, 0.68, 0.58, 0.22, 0.065, "Limpiar", "#6c757d")
    
    # Content area
    ax.text(0.1, 0.53, "Contenido del Archivo:", weight="bold", fontsize=9)
    txt_box = patches.Rectangle((0.1, 0.17), 0.8, 0.34, facecolor="#ffffff", edgecolor="#94a3b8", zorder=3)
    ax.add_patch(txt_box)
    
    sample_lines = [
        "UNIVERSIDAD NACIONAL DE COLOMBIA",
        "FACULTAD DE MINAS - SEDE MEDELLIN",
        "PROGRAMACION ORIENTADA A OBJETOS 2026-2S",
        "----------------------------------------",
        "Prueba de lectura secuencial con buffer.",
        "Gestion adecuada de flujo de caracteres.",
        "Tratamiento de excepciones IOException."
    ]
    y_l = 0.47
    for line in sample_lines:
        ax.text(0.13, y_l, line, fontsize=7.5, family="monospace", color="#1e293b", zorder=5)
        y_l -= 0.04
        
    # Status bar
    ax.text(0.1, 0.12, "Estado: Lectura exitosa: 7 lineas, 276 caracteres.", fontsize=8.5, color="#15803d", weight="bold")
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "ui_ejercicio6_8.png"), dpi=300)
    plt.close()

    # Clases
    fig, ax = plt.subplots(figsize=(6.8, 4.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_uml_class(ax, 0.05, 0.15, 0.42, 0.7, "LectorArchivo",
                   [],
                   ["+ leer_archivo(ruta): tuple",
                    "+ convertir_mayusculas(txt): str"])
                    
    draw_uml_class(ax, 0.55, 0.15, 0.4, 0.7, "VentanaLeerArchivo",
                   ["- lector: LectorArchivo",
                    "- txt_ruta: Entry",
                    "- txt_contenido: ScrolledText",
                    "- lbl_estado: Label"],
                   ["+ _construir_ui(): void",
                    "+ _accion_examinar(): void",
                    "+ _accion_leer(): void",
                    "+ _accion_mayusculas(): void",
                    "+ _accion_limpiar(): void"])
                    
    ax.annotate("", xy=(0.47, 0.5), xytext=(0.55, 0.5),
                arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#1e293b"))
    ax.text(0.51, 0.53, "utiliza", ha="center", fontsize=8.5, weight="bold")
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "clases_ejercicio6_8.png"), dpi=300)
    plt.close()

    # Casos de uso
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    draw_actor(ax, 0.15, 0.52, "Usuario")
    
    system_box = patches.FancyBboxPatch((0.35, 0.08), 0.58, 0.84, boxstyle="square,pad=0",
                                        facecolor="#ffffff", edgecolor="#0b5ed7", linewidth=1.5)
    ax.add_patch(system_box)
    ax.text(0.64, 0.87, "Sistema: Lectura de Archivos", ha="center", weight="bold", fontsize=9.5)
    
    ucs = [
        (0.64, 0.74, "Seleccionar archivo del sistema"),
        (0.64, 0.55, "Leer archivo con buffer"),
        (0.64, 0.36, "Gestionar excepciones FileNotFound/IO"),
        (0.64, 0.18, "Transformar texto a mayusculas")
    ]
    for x, y, label in ucs:
        draw_use_case(ax, x, y, 0.45, 0.11, label)
        ax.plot([0.18, x - 0.22], [0.52, y], color="#495057", linewidth=1.2)
        
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "casos_ejercicio6_8.png"), dpi=300)
    plt.close()

if __name__ == "__main__":
    gen_6_4()
    gen_6_5()
    gen_6_6()
    gen_6_7()
    gen_6_8()
    print("Todas las 15 figuras generadas con exito.")

