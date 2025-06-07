# Programa: Juego de preguntas y respuestas
# Tema: Algoritmos de búsqueda y ordenamiento
# Materia: Programación I - UTN
# Integrantes: Federico Duarte y Natalia Córdoba
# ---------------------------------------------------------------------------------------------------

# PREGUNTAS DEL JUEGO
PREGUNTAS = [
    # Nivel 1: Búsqueda Lineal
    {
        "nivel": 1,
        "texto": "Tienes la siguiente lista: [5, 3, 8, 2, 9, 1]. \nDebes buscar el número 8 recorriéndola elemento por elemento. ¿Qué algoritmo utilizarías?",
        "opciones": ["Búsqueda lineal", "Búsqueda binaria"],
        "respuesta_correcta": "1"
    },
    # Nivel 2: Búsqueda Binaria /// Fede
    # Nivel 3: Bubble Sort (Ordenamiento por burbuja)
     {
        "nivel": 3,
        "texto": "Tienes la seguiente lista: [19, 32, 71, 13, 4, 58]. \n¿Cuál de los siguientes algoritmos usarías para compar cada elemento de la lista con el siguiente y luego intercambiarlos si no están en el orden correcto?",
        "opciones": ["Selection Sort", "Bubble Sort" "Insertion Sort", "Quick Sort"],
        "respuesta_correcta": "2"
    },
    # Nivel 4: Selection Sort (Ordenamiento por selección)
    {
        "nivel": 4,
        "texto": "Tienes la seguiente lista: [66, 23, 17, 4, 33]. \n¿Qué algoritmo utilizarías para encontrar el elemento menor de la lista y luego colocarlo en el primer elemento, repitiendo este proceso con todos los elementos?",
        "opciones": ["Insertion Sort", "Quick Sort", "Selection Sort", "Bubble Sort"],
        "respuesta_correcta": "3"
    },
    # Nivel 5: Insertion Sort (Ordenamiento por inserción) /// Fede
    # Nivel 6: Quick Sort (Ordenamiento rápido)  /// Fede
]

# FUNCIONES DE BÚSQUEDA
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
# funcion busqueda binaria /// Fede

# FUNCIONES DE ORDENAMIENTO
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

# funcion insertion_sort /// Fede
# funcion quick_sort /// Fede

# FUNCION RESOLVER ALGORÍTMO (cuando la respuesta es correcta)
def resolver_algoritmo(nivel):
    # Búsqueda lineal
    if nivel == 1:
        lista = [5, 3, 8, 2, 9, 1]
        print("Buscando el número 8 en", lista)
        print("Resultado:", busqueda_lineal(lista, 8))
    # Bubble Sort
    elif nivel == 3:
        lista = [19, 32, 71, 13, 4, 58]
        print("Ordenando con Burbuja:", lista)
        print("Resultado:", bubble_sort(lista))
    # Selection_ sort
    elif nivel == 4:
        lista = [66, 23, 17, 4, 33]
        print("Ordenando con Selección:", lista)
        print("Resultado:", selection_sort(lista))

# función para preguntar /// Fede

# MENÚ PRINCIPAL DEL JUEGO
def jugar():
    print("\nBIENVENIDO/A AL QUIZZ DE ALGORITMOS DE BÚSQUEDA Y ORDENAMIENTO")
    aciertos = 0
    for pregunta in PREGUNTAS:
        if hacer_pregunta(pregunta):
            aciertos += 1
    print(f"\nJuego terminado. Aciertos: {aciertos}")
    if aciertos == 6:
        print("¡Perfecto! Has respondido correctamente todas las preguntas.")
    elif aciertos >= 4:
        print("¡Muy bien! Has respondido bien más de la mitad de las preguntas.")
    else:
        print("Debes practicar un poco más.")
## ///// podemos preguntar si quiere salir o volver a jugar

# ENTRADA AL JUEGO
if __name__ == "__main__":  # Ejecuta el juego solo si el archivo se ejecuta directamente
    jugar()