import tkinter as tk
from tkinter import filedialog, scrolledtext

# ─────────────────────────────────────────────
# Ejercicio 5 (p. 427): LeerArchivo
# Abre un archivo .txt seleccionado por el usuario
# y muestra su contenido línea a línea.
# Maneja IOError si el archivo no se puede leer.
# ─────────────────────────────────────────────

def seleccionar_archivo():
    """Abre un diálogo para elegir un archivo .txt."""
    ruta = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if ruta:
        entry_ruta.config(state="normal")
        entry_ruta.delete(0, tk.END)
        entry_ruta.insert(0, ruta)
        entry_ruta.config(state="readonly")
        leer_archivo(ruta)


def leer_archivo(ruta):
    """
    Lee el archivo línea a línea y muestra el contenido.
    Captura IOError si no se puede abrir o leer el archivo.
    """
    area_contenido.config(state="normal")
    area_contenido.delete("1.0", tk.END)
    lbl_info.config(text="")

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            area_contenido.insert(tk.END, "(El archivo está vacío)")
            lbl_info.config(text="Archivo vacío.", fg="#f57c00")
        else:
            for numero, linea in enumerate(lineas, start=1):
                area_contenido.insert(tk.END, f"{numero:>3}: {linea}")
            lbl_info.config(
                text=f"✔ Archivo leído correctamente. {len(lineas)} línea(s).",
                fg="#2e7d32"
            )

    except IOError as e:
        area_contenido.insert(tk.END, f"No se pudo leer el archivo.\nDetalle: {e}")
        lbl_info.config(text="✘ Error de lectura.", fg="#c62828")
    finally:
        area_contenido.config(state="disabled")


def limpiar():
    area_contenido.config(state="normal")
    area_contenido.delete("1.0", tk.END)
    area_contenido.config(state="disabled")
    entry_ruta.config(state="normal")
    entry_ruta.delete(0, tk.END)
    entry_ruta.config(state="readonly")
    lbl_info.config(text="")


# ── Ventana principal ──
ventana = tk.Tk()
ventana.title("Ejercicio 5 – LeerArchivo")
ventana.resizable(False, False)

# Descripción
marco_desc = tk.LabelFrame(ventana, text="Descripción", padx=10, pady=8)
marco_desc.pack(fill="x", padx=15, pady=(15, 5))
tk.Label(
    marco_desc,
    text=(
        "Lee un archivo de texto (.txt) y muestra su contenido línea a línea.\n"
        "Se captura IOError si el archivo no puede abrirse o leerse."
    ),
    justify="left",
).pack(anchor="w")

# Selector de archivo
marco_archivo = tk.LabelFrame(ventana, text="Archivo", padx=15, pady=10)
marco_archivo.pack(fill="x", padx=15, pady=5)

tk.Label(marco_archivo, text="Ruta:", anchor="w").grid(row=0, column=0, sticky="w")

entry_ruta = tk.Entry(marco_archivo, width=38, state="readonly", font=("Arial", 9))
entry_ruta.grid(row=0, column=1, padx=8)

tk.Button(
    marco_archivo, text="Examinar...", command=seleccionar_archivo,
    bg="#2196F3", fg="white", font=("Arial", 9, "bold")
).grid(row=0, column=2)

# Botón limpiar
tk.Button(
    ventana, text="Limpiar", command=limpiar,
    bg="#607D8B", fg="white", font=("Arial", 9), padx=8
).pack(pady=6)

# Área de contenido
marco_cont = tk.LabelFrame(ventana, text="Contenido del archivo", padx=10, pady=8)
marco_cont.pack(fill="both", expand=True, padx=15, pady=(0, 5))

area_contenido = scrolledtext.ScrolledText(
    marco_cont, width=58, height=16, state="disabled",
    font=("Courier", 10), wrap="none"
)
area_contenido.pack()

# Estado
lbl_info = tk.Label(ventana, text="", font=("Arial", 9))
lbl_info.pack(pady=(0, 12))

ventana.mainloop()
