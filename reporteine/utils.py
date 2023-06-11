import unicodedata

def aproximador(datos, precision: int = 2):
    datos_aprox = []
    for dato in datos:
        x = dato[0]
        y = round(dato[1], precision)
        datos_aprox.append((x, y))
    return datos_aprox

def quitar_tildes(s: str) -> str:
    """Quita tildes de una cadena de texto"""
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                if unicodedata.category(c) != 'Mn')

def formato_LaTeX(cadena: str) -> str:
    CARACTERES_ESPECIALES = ('#', '$', '%', '&', '~', '_', '^')
    for caracter in CARACTERES_ESPECIALES:
        cadena = cadena.replace(caracter, "{\\" + caracter + "}")
    return cadena