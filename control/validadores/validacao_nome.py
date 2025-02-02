def validar_nome(nome: str) -> bool:
    return not any(letra not in (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '
        ) for letra in nome.strip().lower()
    ) if nome.strip() != '' else False
