def guardar_resultado(nombre_jugador, resultado, personaje, preguntas_usadas, ruta):
    archivo = open(ruta, "a", encoding="utf-8")

    linea = "Jugador: " + nombre_jugador
    linea = linea + " | Resultado: " + resultado
    linea = linea + " | Personaje: " + personaje
    linea = linea + " | Preguntas usadas: " + str(preguntas_usadas)
    linea = linea + "\n"

    archivo.write(linea)
    archivo.close()

def mostrar_historial(ruta):
    try:
        archivo = open(ruta, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        if len(lineas) == 0:
            print("No hay partidas guardadas todavia.")
        else:
            print("\n--- Historial de partidas ---")
            for linea in lineas:
                print(linea.strip())
            print("-----------------------------")
    except:
        print("No hay historial todavia.")