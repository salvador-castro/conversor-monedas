import requests
from tkinter import messagebox

# API Key de ExchangeRate-API (obtén la tuya en https://www.exchangerate-api.com/)
API_KEY = "0674522f0e200d8ff10ccc3b"  # Reemplázalo con tu clave
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def obtener_tasas(base_currency):
    """ Obtiene las tasas de cambio para la moneda base desde la API. """
    url = BASE_URL + base_currency
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data["conversion_rates"]
        else:
            messagebox.showerror("Error", f"No se pudieron obtener las tasas: {data.get('error-type', 'Desconocido')}")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error en la conexión: {e}")
        return None
