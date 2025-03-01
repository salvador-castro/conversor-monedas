# Conversor de Monedas con API de Tasas de Cambio

Este es un **conversor de monedas en tiempo real** desarrollado en **Python** utilizando la API de ExchangeRate-API y una interfaz gráfica con **Tkinter**. Permite convertir entre diversas monedas globales con formato numérico adecuado y símbolos de moneda correctos.

## 🚀 Características

✅ **Conversión de monedas en tiempo real** usando una API de tasas de cambio.  
✅ **Interfaz gráfica intuitiva** con `Tkinter`.  
✅ **Soporte para múltiples monedas** como USD, EUR, ARS, GBP, JPY, entre otras.  
✅ **Formato de números personalizado** (`xxx.xxx,xx`), con puntos para miles y comas para decimales.  
✅ **Muestra los símbolos de moneda** en el resultado (`U$D`, `$`, `€`, `¥`, etc.).  
✅ **Manejo de errores** para valores incorrectos o problemas de conexión.  

---

## 🛠️ **Requisitos Previos**

Antes de ejecutar el proyecto, asegúrate de tener instalados:

- **Python 3.x** (descárgalo desde [python.org](https://www.python.org/downloads/))
- **Módulo `requests`** (para conectarse a la API)
- **Módulo `tkinter`** (incluido en Python por defecto)

Si `requests` no está instalado, puedes instalarlo con:

```bash
pip install requests
