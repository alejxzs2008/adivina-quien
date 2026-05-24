import random
import modulo.preguntas as preguntas
import modulo.personajes as personajes_mod

LIMITE_PREGUNTAS = 10

def seleccionar_secreto(lista_personajes):
    indice = random.randint(0, len(lista_personajes) - 1)
    return lista_personajes[indice]

def iniciar_partida(nombre_jugador, lista_personajes):
    personaje_secreto = seleccionar_secreto(lista_personajes)
    preguntas_usadas = 0
    gano = False

    print("\n¡El personaje secreto ha sido elegido!")
    print("Tienes hasta", LIMITE_PREGUNTAS, "preguntas para adivinarlo.")

    personajes_mod.mostrar_personajes(lista_personajes)

    while preguntas_usadas < LIMITE_PREGUNTAS:
        preguntas_restantes = LIMITE_PREGUNTAS - preguntas_usadas
        print("\nPreguntas restantes:", preguntas_restantes)

        preguntas.mostrar_menu_preguntas()
        opcion = preguntas.recibir_opcion()

        if not preguntas.validar_opcion(opcion):
            print("Esa opcion no es valida, intenta de nuevo.")
            continue

        if opcion == "11":
            intento = input("¿Quién crees que es el personaje secreto? ").strip()

            if not personajes_mod.nombre_existe(lista_personajes, intento):
                print("Ese nombre no esta en la lista de personajes.")
                continue

            if intento.lower() == personaje_secreto["nombre"].lower():
                gano = True
                break
            else:
                print("Incorrecto. Sigue intentando.")
                preguntas_usadas += 1
        else:
            preguntas.responder_pregunta(opcion, personaje_secreto)
            preguntas_usadas += 1

    return gano, personaje_secreto, preguntas_usadas

def mostrar_resultado_final(gano, nombre_jugador, personaje_secreto, preguntas_usadas):
    print("\n" + "=" * 40)
    if gano:
        print("¡Felicidades", nombre_jugador + "! Adivinaste correctamente.")
        print("El personaje era:", personaje_secreto["nombre"])
    else:
        print("Se acabaron las preguntas,", nombre_jugador + ".")
        print("El personaje secreto era:", personaje_secreto["nombre"])
    print("Preguntas usadas:", preguntas_usadas)
    print("=" * 40)

    if gano:
        return "gano"
    return "perdio"