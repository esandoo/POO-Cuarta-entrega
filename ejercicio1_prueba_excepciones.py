import tkinter as tk
from tkinter import ttk, scrolledtext

# ─────────────────────────────────────────────
# Ejercicio 1 (p. 400): PruebaExcepciones
# Demuestra try / catch / finally con dos bloques:
#   1) División por cero  → ArithmeticError
#   2) Objeto None        → AttributeError
# ─────────────────────────────────────────────

def ejecutar_prueba():
    """Ejecuta los dos bloques try y muestra la salida en el área de texto."""
    salida.config(state="normal")
    salida.delete("1.0", tk.END)

    # ── Bloque 1: división por cero ──
    try:
        log("Ingresando al primer try...")
        cociente = 10000 / 0          # Genera ZeroDivisionError (equivale a ArithmeticException)
        log(f"Resultado: {cociente}")  # Esta línea NUNCA se ejecuta
    except ZeroDivisionError:
        log("División por cero capturada.")
    finally:
        log("Ingresando al primer finally.\n")

    # ── Bloque 2: objeto None ──
    try:
        log("Ingresando al segundo try...")
        objeto = None
        objeto.upper()                # Genera AttributeError (equivale a NullPointerException)
        log("Imprimiendo objeto")     # Esta línea NUNCA se ejecuta
    except ZeroDivisionError:
        log("División por cero")      # No coincide, no se ejecuta
    except Exception:
        log("Ocurrió una excepción.")
    finally:
        log("Ingresando al segundo finally.")

    salida.config(state="disabled")


def log(mensaje):
    """Agrega una línea al área de texto."""
    salida.insert(tk.END, mensaje + "\n")


# ── Ventana principal ──
ventana = tk.Tk()
ventana.title("Ejercicio 1 – PruebaExcepciones")
ventana.resizable(False, False)

# Marco superior con explicación
marco_info = tk.LabelFrame(ventana, text="Descripción", padx=10, pady=8)
marco_info.pack(fill="x", padx=15, pady=(15, 5))
tk.Label(
    marco_info,
    text=(
        "Demuestra el manejo de excepciones con bloques try/except/finally.\n"
        "Bloque 1: intenta dividir entre cero.\n"
        "Bloque 2: intenta usar un objeto que es None."
    ),
    justify="left",
).pack(anchor="w")

# Botón de ejecución
tk.Button(
    ventana,
    text="▶  Ejecutar prueba",
    command=ejecutar_prueba,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=5,
).pack(pady=10)

# Área de salida
marco_salida = tk.LabelFrame(ventana, text="Salida del programa", padx=10, pady=8)
marco_salida.pack(fill="both", expand=True, padx=15, pady=(0, 15))

salida = scrolledtext.ScrolledText(
    marco_salida, width=55, height=12, font=("Courier", 10), state="disabled"
)
salida.pack()

ventana.mainloop()
