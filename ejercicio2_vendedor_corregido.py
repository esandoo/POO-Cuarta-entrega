import tkinter as tk
from tkinter import messagebox

# ─────────────────────────────────────────────
# Ejercicio 2 (p. 406): Clase Vendedor
# Valida que la edad sea mayor de 18 y menor de 120.
# CORRECCIÓN: self.edad = edad no se asignaba cuando la edad era válida.
# El libro usa:
#   if edad < 18 → lanza excepción
#   if (0 <= edad < 120) → asigna self.edad   ← rama positiva
#   else → lanza excepción
# ─────────────────────────────────────────────

class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre    = nombre
        self.apellidos = apellidos
        self.edad      = None

    def verificar_edad(self, edad):
        """Valida la edad y la asigna si es correcta (equivale a IllegalArgumentException)."""
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if 0 <= edad < 120:          # ← rama positiva: asigna
            self.edad = edad
        else:                        # ← edad negativa o >= 120
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

    def imprimir(self):
        return (
            f"Nombre del vendedor    = {self.nombre}\n"
            f"Apellidos del vendedor = {self.apellidos}\n"
            f"Edad del vendedor      = {self.edad}"
        )


# ── GUI ──────────────────────────────────────────────────────────────────────

def registrar_vendedor():
    nombre    = entry_nombre.get().strip()
    apellidos = entry_apellidos.get().strip()
    edad_txt  = entry_edad.get().strip()

    if not nombre or not apellidos or not edad_txt:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return

    try:
        edad = int(edad_txt)
    except ValueError:
        messagebox.showerror("Error de formato", "La edad debe ser un número entero.")
        return

    vendedor = Vendedor(nombre, apellidos)
    try:
        vendedor.verificar_edad(edad)
        lbl_resultado.config(text=vendedor.imprimir(), fg="#2e7d32", bg="#e8f5e9")
    except ValueError as e:
        lbl_resultado.config(text=f"Error: {e}", fg="#c62828", bg="#ffebee")


def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    lbl_resultado.config(text="", bg=ventana.cget("bg"))


ventana = tk.Tk()
ventana.title("Ejercicio 2 – Vendedor")
ventana.resizable(False, False)

marco_desc = tk.LabelFrame(ventana, text="Descripción", padx=10, pady=8)
marco_desc.pack(fill="x", padx=15, pady=(15, 5))
tk.Label(
    marco_desc,
    text=(
        "Registra un vendedor validando que su edad\n"
        "sea mayor de 18 y menor de 120 años.\n"
        "Se lanza un ValueError si la condición no se cumple."
    ),
    justify="left",
).pack(anchor="w")

marco_form = tk.LabelFrame(ventana, text="Datos del Vendedor", padx=15, pady=10)
marco_form.pack(fill="x", padx=15, pady=5)

labels_names = [("Nombre:", "entry_nombre"), ("Apellidos:", "entry_apellidos"), ("Edad:", "entry_edad")]
entries = {}
for i, (lbl, key) in enumerate(labels_names):
    tk.Label(marco_form, text=lbl, width=12, anchor="w").grid(row=i, column=0, pady=4)
    e = tk.Entry(marco_form, width=28)
    e.grid(row=i, column=1, pady=4)
    entries[key] = e

entry_nombre    = entries["entry_nombre"]
entry_apellidos = entries["entry_apellidos"]
entry_edad      = entries["entry_edad"]

marco_btn = tk.Frame(ventana)
marco_btn.pack(pady=10)
tk.Button(marco_btn, text="Registrar", command=registrar_vendedor,
          bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=8).pack(side="left", padx=5)
tk.Button(marco_btn, text="Limpiar", command=limpiar,
          bg="#607D8B", fg="white", font=("Arial", 10), padx=8).pack(side="left", padx=5)

lbl_resultado = tk.Label(ventana, text="", font=("Courier", 10),
                          justify="left", padx=10, pady=8, relief="flat")
lbl_resultado.pack(padx=15, pady=(0, 15), fill="x")

ventana.mainloop()
