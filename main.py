import modulo.cargar_datos as cargar_datos
import modulo.juego as juego
import modulo.archivo as archivos

RUTA_PERSONAJES = "data/personajes.txt"
RUTA_HISTORIAL = "data/historial.txt"

def bienvenida():
    print("=" * 40)
    print("     Bienvenido a Adivina Quien!")
    print("=" * 40)
    print("El programa pensara en un personaje")
    print("y tu tienes que adivinar quien es.")

def pedir_nombre():
    nombre = input("\n¿Cómo te llamas? ").strip()
    while nombre == "":
        print("Por favor escribe tu nombre.")
        nombre = input("¿Cómo te llamas? ").strip()
    return nombre

def preguntar_si_jugar_de_nuevo():
    respuesta = input("\n¿Quieres jugar otra vez? (si/no): ").strip().lower()
    if respuesta == "si":
        return True
    return False

def main():
    bienvenida()

    nombre_jugador = pedir_nombre()
    print("\nHola,", nombre_jugador + "!")

    lista_personajes = cargar_datos.leer_personajes(RUTA_PERSONAJES)

    if len(lista_personajes) == 0:
        print("Error: no se encontraron personajes en el archivo.")
        return

    print("Se cargaron", len(lista_personajes), "personajes.")

    ver_historial = input("\n¿Quieres ver el historial de partidas anteriores? (si/no): ").strip().lower()
    if ver_historial == "si":
        archivos.mostrar_historial(RUTA_HISTORIAL)

    seguir_jugando = True

    while seguir_jugando:
        gano, personaje_secreto, preguntas_usadas = juego.iniciar_partida(nombre_jugador, lista_personajes)

        resultado = juego.mostrar_resultado_final(gano, nombre_jugador, personaje_secreto, preguntas_usadas)

        archivos.guardar_resultado(nombre_jugador, resultado, personaje_secreto["nombre"], preguntas_usadas, RUTA_HISTORIAL)
        print("Resultado guardado en el historial.")

        seguir_jugando = preguntar_si_jugar_de_nuevo()

    print("\n¡Hasta luego,", nombre_jugador + "! Gracias por jugar.")
if __name__ == "__main__":
    main()