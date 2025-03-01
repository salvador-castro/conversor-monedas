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
```

---

## 📥 **Instalación y Uso**

1. **Clona o descarga** este repositorio:

   ```bash
   git clone https://github.com/tuusuario/conversor-monedas.git
   cd conversor-monedas
   ```

2. **Reemplaza tu clave de API** en el archivo Python:

   - Regístrate en [ExchangeRate-API](https://www.exchangerate-api.com/)
   - Obtén una **API Key gratuita** y reemplázala en `API_KEY` dentro del código:

   ```python
   API_KEY = "TU_API_KEY"
   ```

3. **Ejecuta el programa**:

   ```bash
   python conversor_monedas.py
   ```

---

## 🖥️ **Funcionamiento**

1. Ingresa un **monto** en el campo de texto.
2. Selecciona la **moneda de origen** y la **moneda destino**.
3. Haz clic en el botón **Convertir**.
4. El resultado se mostrará en el formato correcto, por ejemplo:

   - `U$D 1.500 = $1.596.000`
   - `€ 1.234.567,89 = ¥190.568.928,45`

---

## 🔄 **Formato de Salida**
El resultado se muestra con:

- **Símbolos de moneda correctos** (`$`, `U$D`, `€`, `¥`, etc.).
- **Miles separados por puntos** (`1.000`, `10.000`, `1.000.000`).
- **Decimales separados por comas** (`100,50`, `1.250.000,75`).

Ejemplo de conversión de **USD a ARS**:

```txt
U$D 1 = $1.064
U$D 1.500 = $1.596.000
U$D 10.000 = $10.640.000
```

---

## 📌 **Monedas Disponibles**

Este conversor incluye las siguientes monedas:

- **Dólar estadounidense (USD)**
- **Euro (EUR)**
- **Peso argentino (ARS)**
- **Libra esterlina (GBP)**
- **Yen japonés (JPY)**
- **Real brasileño (BRL)**
- **Peso mexicano (MXN)**
- **Dólar canadiense (CAD)**
- **Yuan chino (CNY)**

Puedes agregar más monedas fácilmente editando la lista en el código:

```python
monedas = ["USD", "EUR", "ARS", "GBP", "JPY", "BRL", "MXN", "CAD", "CNY"]
```

---

## ⚠️ **Manejo de Errores**

El programa está preparado para manejar errores como:

❌ **Valor no numérico** → Muestra un mensaje de error.  
❌ **Falla en la API** → Notifica si la API no responde o la clave es inválida.  
❌ **Conversión no soportada** → Si una moneda no está disponible, muestra un aviso.  

---

## 🏗️ **Posibles Mejoras Futuras**

🔹 Agregar soporte para **más monedas**.  
🔹 Permitir conversión **offline** con tasas almacenadas en caché.  
🔹 Guardar el **historial de conversiones** en un archivo o base de datos.  
🔹 Crear una **versión web** con Flask o Django.  

---

## 📝 **Licencia**
Este proyecto es de código abierto bajo la licencia **MIT**.

---

## 🤝 **Contribuciones**
Si deseas mejorar el proyecto:

1. Haz un **fork**.
2. Crea una nueva **rama**:  
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Realiza los cambios y **sube tu código**.  
4. Envía un **pull request**.

🚀 **¡Gracias por usar este conversor de monedas!** 🌍💰  
