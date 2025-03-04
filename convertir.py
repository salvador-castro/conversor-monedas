from obtenerTasas import obtener_tasas
from formatearNumeros import formatear_numero
from tkinter import messagebox

# Diccionario de símbolos de moneda
SIMBOLOS_MONEDA = {
    "USD": "U$D", "EUR": "€", "ARS": "$", "GBP": "£",
    "JPY": "¥", "BRL": "R$", "MXN": "$", "CAD": "C$",
    "CNY": "¥"
}

def convertir(entry_monto, combo_de, combo_a, label_resultado):
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