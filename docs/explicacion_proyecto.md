# Explicación del proyecto: Adivina Quién

## Cómo dividimos el código en módulos

- main.py: controla el flujo general del programa.
- cargar_datos.py: lee el archivo y convierte cada línea en un diccionario.
- juego.py: elige el personaje y maneja los turnos.
- preguntas.py: muestra el menú, recibe la opción y responde sí o no.
- personajes.py: busca y filtra personajes de la lista.
- archivos.py: guarda y muestra el historial de partidas.

## Estructuras de datos

Cada personaje es un diccionario con claves como nombre, genero, cabello, gafas, etc.
Todos los personajes se guardan en una lista llamada lista_personajes.

## Uso de listas

Se usa una lista para guardar todos los personajes cargados desde el archivo.

## Uso de diccionarios

Para responder una pregunta se accede directamente al valor:
personaje_secreto["gafas"] devuelve "si" o "no".

## Uso de archivos

Se lee data-personajes.txt al inicio para cargar todos los personajes.
Al terminar cada partida, el programa crea automáticamente el archivo
data/historial.txt, y escribe una línea con el nombre del
jugador, si ganó o perdió, el personaje secreto y cuántas preguntas usó.


## Dificultades encontradas

Manejar los imports entre módulos y validar bien la entrada del usuario
para que el programa no se rompa con valores inesperados.

## Qué aprendimos

A separar un programa en módulos, a leer y escribir archivos de texto,
y a organizar datos con listas de diccionarios.