def formatear_numero(valor):
    """ Formatea el número con puntos para miles y coma para decimales. """
    if isinstance(valor, float) and valor.is_integer():
        return f"{int(valor):,}".replace(",", ".")  # Sin decimales si es entero
    else:
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
