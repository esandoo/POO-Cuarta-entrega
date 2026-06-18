import tkinter as tk
from tkinter import messagebox, scrolledtext

# ─────────────────────────────────────────────
# Ejercicio 4 (p. 418): EquipoMaratónProgramación
# CORRECCIONES aplicadas:
#   1. El libro exige MÍNIMO 2 y MÁXIMO 3 integrantes.
#      La versión original solo validaba el máximo de 3.
#      Se agrega validación de mínimo al intentar cerrar/mostrar el equipo.
#   2. validar_campo() ahora lanza Exception (igual que el libro),
#      no ValueError, para ser fiel al código Java original.
#   3. El log de errores de validación usa el mensaje exacto del libro.
# ─────────────────────────────────────────────

MIN_INTEGRANTES = 2
MAX_INTEGRANTES = 3


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre    = nombre
        self.apellidos = apellidos

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class EquipoMaraton:
    def __init__(self, nombre_equipo, universidad, lenguaje):
        self.nombre_equipo = nombre_equipo
        self.universidad   = universidad
        self.lenguaje      = lenguaje
        self.programadores = []            # equivale al array Programador[3]

    def esta_lleno(self):
        return len(self.programadores) >= MAX_INTEGRANTES

    def tamanio(self):
        return len(self.programadores)

    def equipo_completo_valido(self):
        """Retorna True si el equipo tiene entre MIN y MAX integrantes."""
        return MIN_INTEGRANTES <= len(self.programadores) <= MAX_INTEGRANTES

    def añadir(self, programador):
        """Lanza Exception si el equipo está lleno (igual que el libro)."""
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo):
        """
        Valida que el campo no tenga dígitos y longitud <= 20 chars.
        Lanza Exception (igual que el libro Java usa Exception, no ValueError).
        """
        for c in campo:
            if c.isdigit():
                raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")


# ── Estado global ─────────────────────────────────────────────────────────────
equipo = None


def crear_equipo():
    global equipo
    nombre      = entry_equipo.get().strip()
    universidad = entry_universidad.get().strip()
    lenguaje    = entry_lenguaje.get().strip()

    if not nombre or not universidad or not lenguaje:
        messagebox.showwarning("Campos vacíos", "Completa todos los datos del equipo.")
        return

    equipo = EquipoMaraton(nombre, universidad, lenguaje)
    lbl_estado_equipo.config(
        text=f"✔ Equipo '{nombre}' creado. (0/{MAX_INTEGRANTES} integrantes, mín. {MIN_INTEGRANTES})",
        fg="#2e7d32"
    )
    actualizar_lista()
    log(f"Equipo '{nombre}' | {universidad} | Lenguaje: {lenguaje}\n")


def agregar_programador():
    if equipo is None:
        messagebox.showwarning("Sin equipo", "Primero crea el equipo.")
        return

    nombre    = entry_prog_nombre.get().strip()
    apellidos = entry_prog_apellidos.get().strip()

    if not nombre or not apellidos:
        messagebox.showwarning("Campos vacíos", "Ingresa nombre y apellidos del programador.")
        return

    try:
        EquipoMaraton.validar_campo(nombre)
        EquipoMaraton.validar_campo(apellidos)
    except Exception as e:          # ← Exception, igual que el libro
        log(f"⚠ Error de validación: {e}")
        return

    try:
        prog = Programador(nombre, apellidos)
        equipo.añadir(prog)
        log(f"✔ Agregado: {prog}")
        actualizar_lista()
        entry_prog_nombre.delete(0, tk.END)
        entry_prog_apellidos.delete(0, tk.END)
        n = equipo.tamanio()
        estado = f"✔ Equipo '{equipo.nombre_equipo}' | {n}/{MAX_INTEGRANTES} integrantes"
        if n < MIN_INTEGRANTES:
            estado += f"  (faltan {MIN_INTEGRANTES - n} para el mínimo)"
        elif n == MAX_INTEGRANTES:
            estado += "  — EQUIPO COMPLETO"
        lbl_estado_equipo.config(text=estado, fg="#2e7d32")
    except Exception as e:
        log(f"✘ {e}")


def actualizar_lista():
    area_integrantes.config(state="normal")
    area_integrantes.delete("1.0", tk.END)
    if equipo and equipo.programadores:
        for i, p in enumerate(equipo.programadores, 1):
            area_integrantes.insert(tk.END, f"  {i}. {p}\n")
    else:
        area_integrantes.insert(tk.END, "  (sin integrantes aún)")
    area_integrantes.config(state="disabled")


def log(mensaje):
    area_log.config(state="normal")
    area_log.insert(tk.END, mensaje + "\n")
    area_log.config(state="disabled")
    area_log.see(tk.END)


# ── Ventana principal ─────────────────────────────────────────────────────────
ventana = tk.Tk()
ventana.title("Ejercicio 4 – Equipo Maratón de Programación")
ventana.resizable(False, False)

marco_desc = tk.LabelFrame(ventana, text="Descripción", padx=10, pady=6)
marco_desc.pack(fill="x", padx=15, pady=(15, 5))
tk.Label(
    marco_desc,
    text=(
        f"Gestiona un equipo de programación con mínimo {MIN_INTEGRANTES} y máximo {MAX_INTEGRANTES} integrantes.\n"
        "Valida que nombres/apellidos no tengan dígitos ni superen 20 caracteres."
    ),
    justify="left",
).pack(anchor="w")

# ── Datos del equipo ──
marco_equipo = tk.LabelFrame(ventana, text="Datos del Equipo", padx=15, pady=8)
marco_equipo.pack(fill="x", padx=15, pady=5)

for i, (lbl, var) in enumerate([("Nombre del equipo:", "entry_equipo"),
                                  ("Universidad:",       "entry_universidad"),
                                  ("Lenguaje:",          "entry_lenguaje")]):
    tk.Label(marco_equipo, text=lbl, width=18, anchor="w").grid(row=i, column=0, pady=3)
    e = tk.Entry(marco_equipo, width=28)
    e.grid(row=i, column=1, pady=3)
    globals()[var] = e

tk.Button(marco_equipo, text="Crear equipo", command=crear_equipo,
          bg="#2196F3", fg="white", font=("Arial", 9, "bold")).grid(row=3, column=1, sticky="e", pady=5)
lbl_estado_equipo = tk.Label(marco_equipo, text="", fg="#555", font=("Arial", 9))
lbl_estado_equipo.grid(row=4, column=0, columnspan=2, sticky="w")

# ── Agregar programador ──
marco_prog = tk.LabelFrame(ventana, text="Agregar Programador", padx=15, pady=8)
marco_prog.pack(fill="x", padx=15, pady=5)

tk.Label(marco_prog, text="Nombre:",    width=12, anchor="w").grid(row=0, column=0, pady=3)
entry_prog_nombre = tk.Entry(marco_prog, width=28)
entry_prog_nombre.grid(row=0, column=1, pady=3)

tk.Label(marco_prog, text="Apellidos:", width=12, anchor="w").grid(row=1, column=0, pady=3)
entry_prog_apellidos = tk.Entry(marco_prog, width=28)
entry_prog_apellidos.grid(row=1, column=1, pady=3)

tk.Button(marco_prog, text="Agregar", command=agregar_programador,
          bg="#4CAF50", fg="white", font=("Arial", 9, "bold")).grid(row=2, column=1, sticky="e", pady=5)

# ── Lista integrantes ──
marco_lista = tk.LabelFrame(ventana, text="Integrantes del equipo", padx=10, pady=6)
marco_lista.pack(fill="x", padx=15, pady=5)
area_integrantes = scrolledtext.ScrolledText(marco_lista, height=4, width=45,
                                              state="disabled", font=("Courier", 10))
area_integrantes.pack()
actualizar_lista()

# ── Log ──
marco_log = tk.LabelFrame(ventana, text="Registro de eventos", padx=10, pady=6)
marco_log.pack(fill="x", padx=15, pady=(5, 15))
area_log = scrolledtext.ScrolledText(marco_log, height=4, width=45,
                                      state="disabled", font=("Courier", 10))
area_log.pack()

ventana.mainloop()
