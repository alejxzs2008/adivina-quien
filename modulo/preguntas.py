def mostrar_menu_preguntas():
    print("\n¿Qué quieres preguntar?")
    print("  1. ¿Tiene gafas?")
    print("  2. ¿Tiene sombrero?")
    print("  3. ¿Tiene barba?")
    print("  4. ¿Tiene cabello negro?")
    print("  5. ¿Tiene cabello rubio?")
    print("  6. ¿Tiene cabello castano?")
    print("  7. ¿Tiene cabello rojo?")
    print("  8. ¿Tiene ojos azules?")
    print("  9. ¿Tiene ojos verdes?")
    print("  10. ¿Es mujer?")
    print("  11. Intentar adivinar el personaje")

def recibir_opcion():
    opcion = input("\nEscribe el numero de tu pregunta: ").strip()
    return opcion

def validar_opcion(opcion):
    opciones_validas = ["1","2","3","4","5","6","7","8","9","10","11"]
    if opcion in opciones_validas:
        return True
    return False

def responder_pregunta(opcion, personaje_secreto):
    respuesta = ""

    if opcion == "1":
        print("\nPregunta: ¿Tiene gafas?")
        if personaje_secreto["gafas"] == "si":
            respuesta = "si"
        else:
            respuesta = "no"

    elif opcion == "2":
        print("\nPregunta: ¿Tiene sombrero?")
        if personaje_secreto["sombrero"] == "si":
            respuesta = "si"
        else:
            respuesta = "no"

    elif opcion == "3":
        print("\nPregunta: ¿Tiene barba?")
        if personaje_secreto["barba"] == "si":
            respuesta = "si"
        else:
            respuesta = "no"

    elif opcion == "4":
        print("\nPregunta: ¿Tiene cabello negro?")
        if personaje_secreto["cabello"] == "negro":
            respuesta = "si"
        else:
            respuesta = "no"

    elif opcion == "5":
        print("\nPregunta: ¿Tiene cabello rubio?")
        if personaje_secreto["cabello"] == "rubio":
            respuesta = "si"
        else:
            respuesta = "no"

    elif opcion == "6":
        print("\nPregunta: ¿Tiene cabello castano?")
        if personaje_secreto["cabello"] == "castano":
            respuesta = "si"
        else:
            respuesta = "no"

    elif opcion == "7":
        print("\nPregunta: ¿Tiene cabello rojo?")
        if personaje_secreto["cabello"] == "rojo":
            respuesta = "si"
        else:
            respuesta = "no"

    elif opcion == "8":
        print("\nPregunta: ¿Tiene ojos azules?")
        if personaje_secreto["ojos"] == "azules":
            respuesta = "si"
        else:
            respuesta = "no"

    elif opcion == "9":
        print("\nPregunta: ¿Tiene ojos verdes?")
        if personaje_secreto["ojos"] == "verdes":
            respuesta = "si"
        else:
            respuesta = "no"

    elif opcion == "10":
        print("\nPregunta: ¿Es mujer?")
        if personaje_secreto["genero"] == "femenino":
            respuesta = "si"
        else:
            respuesta = "no"

    print("Respuesta:", respuesta.upper())
    return respuesta