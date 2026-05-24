def leer_personajes(ruta):
    personajes = []

    archivo = open(ruta, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    
    encabezados = lineas[0].strip().split(",")

    for i in range(1, len(lineas)):
        linea = lineas[i].strip()

        if linea == "":
            continue

        valores = linea.split(",")

        if len(valores) != len(encabezados):
            continue

        personaje = {}
        for j in range(len(encabezados)):
            personaje[encabezados[j]] = valores[j]

        personajes.append(personaje)

    return personajes