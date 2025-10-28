import tkinter as tk
import os
import sys

peso_10 = 3.50
peso_50 = 7.0
peso_100_antigua = 9.0
peso_100_nueva = 7.58
peso_500 = 6.5

def leer_valor(entry):
    texto = entry.get().strip().lower()
    texto = texto.replace("g", "").strip()
    if texto == "":
        return 0
    try:
        return float(texto)
    except ValueError:
        return None

def agregar_sufijo(event):
    texto = event.widget.get().strip().lower()
    if not texto.endswith("g"):
        if texto == "":
            return
        event.widget.delete(0, tk.END)
        event.widget.insert(0, texto + " g")
        event.widget.icursor(len(texto))

def calcular():
    monedas_de_10 = leer_valor(entry_10)
    monedas_de_50 = leer_valor(entry_50)
    monedas_de_100n = leer_valor(entry_100n)
    monedas_de_100a = leer_valor(entry_100a)
    monedas_de_500 = leer_valor(entry_500)

    if None in [monedas_de_10, monedas_de_50, monedas_de_100n, monedas_de_100a, monedas_de_500]:
        resultado_label.config(text="⚠ Error: Solo se permiten números.")
        return

    if all(v == 0 for v in [monedas_de_10, monedas_de_50, monedas_de_100n, monedas_de_100a, monedas_de_500]):
        resultado_label.config(text="⚠ Error: Ingrese algún número en los campos para continuar.")
        return

    cant_10 = round(monedas_de_10 / peso_10)
    cant_50 = round(monedas_de_50 / peso_50)
    cant_100n = round(monedas_de_100n / peso_100_nueva)
    cant_100a = round(monedas_de_100a / peso_100_antigua)
    cant_500 = round(monedas_de_500 / peso_500)

    total_10 = cant_10 * 10
    total_50 = cant_50 * 50
    total_100n = cant_100n * 100
    total_100a = cant_100a * 100
    total_500 = cant_500 * 500

    total_general = total_10 + total_50 + total_100n + total_100a + total_500

    resultado = (
        f"Monedas de 10: ${total_10:,.0f}\n"
        f"Monedas de 50: ${total_50:,.0f}\n"
        f"Monedas de 100 (nuevas): ${total_100n:,.0f}\n"
        f"Monedas de 100 (antiguas): ${total_100a:,.0f}\n"
        f"Monedas de 500: ${total_500:,.0f}\n\n"
        f"Total: Tienes ${total_general:,.0f} de pesos."
    ).replace(",", ".")

    resultado_label.config(text=resultado)


def limpiar():
    for entry in [entry_10, entry_50, entry_100n, entry_100a, entry_500]:
        entry.delete(0, tk.END)
    resultado_label.config(text="")

ventana = tk.Tk()
ventana.title("Contador de Monedas")
ventana.geometry("500x600")
if getattr(sys, 'frozen', False):
    ruta_icono = os.path.join(sys._MEIPASS, "icono.ico")
else:
    ruta_icono = os.path.join(os.path.dirname(__file__), "icono.ico")

ventana.iconbitmap(ruta_icono)


contenedor = tk.Frame(ventana, bg="white", bd=2, relief="flat", padx=10, pady=10)
contenedor.place(relx=0.5, rely=0.2, anchor="n", relwidth=0.8)

tk.Label(contenedor, text="Ingresa el peso total (en gramos) de tus monedas:",
         font=("Arial", 12), bg="white").pack(pady=10)

entry_10 = tk.Entry(contenedor)
entry_50 = tk.Entry(contenedor)
entry_100n = tk.Entry(contenedor)
entry_100a = tk.Entry(contenedor)
entry_500 = tk.Entry(contenedor)

entradas = [
    ("Peso de monedas de 10", entry_10),
    ("Peso de monedas de 50", entry_50),
    ("Peso de monedas de 100 (nuevas)", entry_100n),
    ("Peso de monedas de 100 (antiguas)", entry_100a),
    ("Peso de monedas de 500", entry_500)
]

for texto, entrada in entradas:
    tk.Label(contenedor, text=texto, bg="white").pack()
    entrada.pack()
    entrada.bind("<KeyRelease>", agregar_sufijo)

tk.Button(contenedor, text="Calcular", command=calcular).pack(pady=10)
ventana.bind("<Return>", lambda event: calcular())
tk.Button(contenedor, text="Limpiar", command=limpiar).pack()

resultado_label = tk.Label(contenedor, text="", justify="left", fg="darkgreen", bg="white")
resultado_label.pack(pady=10)

ventana.mainloop()

# Que wea estai leyendo chuchetumare? 
