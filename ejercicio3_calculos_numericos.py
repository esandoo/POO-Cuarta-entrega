import tkinter as tk
from tkinter import ttk
import math

# ─────────────────────────────────────────────
# Ejercicio 3 (p. 412): CálculosNuméricos
# Calcula logaritmo neperiano y raíz cuadrada.
# Usa múltiples except para manejar:
#   - Valor negativo  → ValueError
#   - Entrada no numérica → ValueError de float()
# ─────────────────────────────────────────────

class CalculosNumericos:

    @staticmethod
    def calcular_logaritmo(valor):
        """Calcula ln(valor). Lanza ValueError si el valor no es positivo."""
        if valor <= 0:
            raise ValueError("El valor debe ser un número positivo para calcular el logaritmo.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        """Calcula √valor. Lanza ValueError si el valor es negativo."""
        if valor < 0:
            raise ValueError("El valor debe ser un número positivo para calcular la raíz cuadrada.")
        return math.sqrt(valor)


def calcular():
    """Lee el valor ingresado, ejecuta los cálculos y muestra resultados."""
    texto = entry_valor.get().strip()
    resultado_log.config(text="")
    resultado_raiz.config(text="")

    # Intentar convertir a float (InputMismatchException equivalente)
    try:
        valor = float(texto)
    except ValueError:
        resultado_log.config(text="⚠  El valor debe ser numérico.", fg="#c62828")
        resultado_raiz.config(text="⚠  El valor debe ser numérico.", fg="#c62828")
        return

    # Logaritmo neperiano
    try:
        log_result = CalculosNumericos.calcular_logaritmo(valor)
        resultado_log.config(text=f"✔  ln({valor}) = {log_result:.6f}", fg="#2e7d32")
    except ValueError as e:
        resultado_log.config(text=f"✘  {e}", fg="#c62828")

    # Raíz cuadrada
    try:
        raiz_result = CalculosNumericos.calcular_raiz_cuadrada(valor)
        resultado_raiz.config(text=f"✔  √{valor} = {raiz_result:.6f}", fg="#2e7d32")
    except ValueError as e:
        resultado_raiz.config(text=f"✘  {e}", fg="#c62828")


def limpiar():
    entry_valor.delete(0, tk.END)
    resultado_log.config(text="")
    resultado_raiz.config(text="")


# ── Ventana principal ──
ventana = tk.Tk()
ventana.title("Ejercicio 3 – CálculosNuméricos")
ventana.resizable(False, False)

# Descripción
marco_desc = tk.LabelFrame(ventana, text="Descripción", padx=10, pady=8)
marco_desc.pack(fill="x", padx=15, pady=(15, 5))
tk.Label(
    marco_desc,
    text=(
        "Calcula el logaritmo neperiano y la raíz cuadrada de un número.\n"
        "Se manejan múltiples excepciones: valor no numérico y valor negativo."
    ),
    justify="left",
).pack(anchor="w")

# Entrada
marco_entrada = tk.LabelFrame(ventana, text="Valor numérico", padx=15, pady=10)
marco_entrada.pack(fill="x", padx=15, pady=5)

tk.Label(marco_entrada, text="Ingresa un número:", anchor="w").grid(row=0, column=0, sticky="w")
entry_valor = tk.Entry(marco_entrada, width=20, font=("Arial", 11))
entry_valor.grid(row=0, column=1, padx=10)

# Botones
marco_btn = tk.Frame(ventana)
marco_btn.pack(pady=10)

tk.Button(
    marco_btn, text="Calcular", command=calcular,
    bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=8
).pack(side="left", padx=5)

tk.Button(
    marco_btn, text="Limpiar", command=limpiar,
    bg="#607D8B", fg="white", font=("Arial", 10), padx=8
).pack(side="left", padx=5)

# Resultados
marco_res = tk.LabelFrame(ventana, text="Resultados", padx=15, pady=10)
marco_res.pack(fill="x", padx=15, pady=(0, 15))

tk.Label(marco_res, text="Logaritmo neperiano:", anchor="w", width=22).grid(row=0, column=0, sticky="w", pady=4)
resultado_log = tk.Label(marco_res, text="", anchor="w", width=45, font=("Courier", 10))
resultado_log.grid(row=0, column=1, sticky="w")

tk.Label(marco_res, text="Raíz cuadrada:", anchor="w", width=22).grid(row=1, column=0, sticky="w", pady=4)
resultado_raiz = tk.Label(marco_res, text="", anchor="w", width=45, font=("Courier", 10))
resultado_raiz.grid(row=1, column=1, sticky="w")

ventana.mainloop()
