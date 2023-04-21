# aqui va la programación nueva para hacer pruebas
# progamacion paul vega

# programacion

def sort_list(lista, eliminar_duplicados=False):
    """
    Ordena una lista de palabras alfabéticamente y las imprime, opcionalmente eliminando duplicados.

    Args:
        lista (list): Lista de palabras a ordenar.
        eliminar_duplicados (bool, optional): Indica si se deben eliminar duplicados de la lista. Por defecto False.
    """
    lista_ordenada = sorted(lista)  # Ordena la lista alfabéticamente

    if eliminar_duplicados:
        lista_ordenada = list(set(lista_ordenada))  # Elimina duplicados usando un set

    for palabra in lista_ordenada:
        print(palabra)