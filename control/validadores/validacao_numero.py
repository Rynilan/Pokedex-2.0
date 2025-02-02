def validar_numero(numero: str) -> bool:
    numero = numero.strip()
    try:
        numero = int(numero)
        return numero > 0
    except ValueError:
        return False
