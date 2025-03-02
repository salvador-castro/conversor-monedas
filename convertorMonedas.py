import requests
import tkinter as tk
from tkinter import ttk, messagebox

# API Key de ExchangeRate-API (obtén la tuya en https://www.exchangerate-api.com/)
API_KEY = "0674522f0e200d8ff10ccc3b"  # Reemplázalo con tu clave
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

# Diccionario de símbolos de moneda
SIMBOLOS_MONEDA = {
    "USD": "U$D", "EUR": "€", "ARS": "$", "GBP": "£",
    "JPY": "¥", "BRL": "R$", "MXN": "$", "CAD": "C$",
    "CNY": "¥"
}

def formatear_numero(valor):
    """ Formatea el número con puntos para miles y coma para decimales. """
    if valor.is_integer():
        return f"{int(valor):,}".replace(",", ".")  # Sin decimales si es entero
    else:
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def obtener_tasas(base_currency):
    """ Obtiene las tasas de cambio para la moneda base desde la API. """
    url = BASE_URL + base_currency
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data["conversion_rates"]
        else:
            messagebox.showerror("Error", f"No se pudieron obtener las tasas: {data['error-type']}")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error en la conexión: {e}")
        return None

def convertir():
    """ Realiza la conversión de moneda. """
    try:
        monto = float(entry_monto.get())
        moneda_origen = combo_de.get()
        moneda_destino = combo_a.get()

        tasas = obtener_tasas(moneda_origen)
        if tasas and moneda_destino in tasas:
            resultado = monto * tasas[moneda_destino]

            # Formatear los números
            monto_str = formatear_numero(monto)
            resultado_str = formatear_numero(resultado)

            # Obtener símbolos de moneda
            simbolo_origen = SIMBOLOS_MONEDA.get(moneda_origen, moneda_origen)
            simbolo_destino = SIMBOLOS_MONEDA.get(moneda_destino, moneda_destino)

            label_resultado.config(text=f"{simbolo_origen} {monto_str} = {simbolo_destino} {resultado_str}")
        else:
            messagebox.showerror("Error", "No se encontraron tasas para la conversión.")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un monto válido.")

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

btn_convertir = tk.Button(root, text="Convertir", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=convertir)
btn_convertir.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="black")
label_resultado.pack(pady=10)

# Ejecutar la ventana
root.mainloop()
