import requests
import tkinter as tk
from tkinter import ttk, messagebox
from convertir import convertir  # ✅ Importa la función convertir

# Diccionario de símbolos de moneda
SIMBOLOS_MONEDA = {
    "USD": "U$D", "EUR": "€", "ARS": "$", "GBP": "£",
    "JPY": "¥", "BRL": "R$", "MXN": "$", "CAD": "C$",
    "CNY": "¥"
}

# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de Monedas")
root.geometry("350x300")
root.resizable(False, False)

# Estilos
root.configure(bg="#f4f4f4")

# Widgets
label_monto = tk.Label(root, text="Monto:", bg="#f4f4f4", fg="black", font=("Arial", 12))
label_monto.pack(pady=5)

entry_monto = tk.Entry(root, font=("Arial", 12), justify="center")
entry_monto.pack(pady=5)

label_de = tk.Label(root, text="De:", bg="#f4f4f4", fg="black", font=("Arial", 12))
label_de.pack(pady=5)

monedas = ["USD", "EUR", "ARS", "GBP", "JPY", "BRL", "MXN", "CAD", "CNY"]
combo_de = ttk.Combobox(root, values=monedas, state="readonly", font=("Arial", 12))
combo_de.set("USD")
combo_de.pack(pady=5)

label_a = tk.Label(root, text="A:", bg="#f4f4f4", fg="black", font=("Arial", 12))
label_a.pack(pady=5)

combo_a = ttk.Combobox(root, values=monedas, state="readonly", font=("Arial", 12))
combo_a.set("EUR")
combo_a.pack(pady=5)

<<<<<<< HEAD
btn_convertir = tk.Button(root, text="Convertir", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=convertir)
=======
btn_convertir = tk.Button(
    root, text="Convertir", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
    command=lambda: convertir(entry_monto, combo_de, combo_a, label_resultado)
)
>>>>>>> d46ba9d (V2.0.0)
btn_convertir.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="black")
label_resultado.pack(pady=10)

# Ejecutar la ventana
<<<<<<< HEAD
root.mainloop()
=======
root.mainloop()
>>>>>>> d46ba9d (V2.0.0)
