def mostrar_personajes(personajes):
    print("\nPersonajes disponibles:")
    print("-" * 30)
    for p in personajes:
        print(" -", p["nombre"])
    print("-" * 30)

def buscar_personaje(personajes, nombre):
    nombre = nombre.strip().lower()
    for p in personajes:
        if p["nombre"].lower() == nombre:
            return p
    return None

def nombre_existe(personajes, nombre):
    resultado = buscar_personaje(personajes, nombre)
    if resultado is None:
        return False
    return True

def filtrar_por_caracteristica(personajes, campo, valor):
    resultado = []
    for p in personajes:
        if p[campo] == valor:
            resultado.append(p)
    return resultado