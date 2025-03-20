import random
import sys 


questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

correct_answers_index = [1, 2, 0, 3, 1]


def respuesta_permitida(respuesta, valores):
    return respuesta in valores

puntaje = 0

questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)
#print (questions_to_ask[0][])
#print (questions_to_ask[1][1])


for i in range(3):

    j=i
    print(questions_to_ask[i][0])  # Imprime la pregunta

    for i, respuesta in enumerate(questions_to_ask[i][1], start=1):
        print(f"{i}. {respuesta}")  # Imprime respuestas con índice desde 1
    
    for intento in range(2):

        try:
           
            user_answer = int(input("Respuesta (1-4): ")) - 1
            if respuesta_permitida(user_answer, {0, 1, 2, 3}):
                if user_answer == questions_to_ask[j][2]:
                    print("¡Correcto!")
                    puntaje +=1
                    break  
                else:
                    print("Incorrecto. Intenta de nuevo.")
                    if puntaje  > 0:
                            puntaje -=0.5
            else:
                print("Respuesta NO válida*")
                sys.exit(1)  

        except ValueError:
            print("Respuesta NO valida")
            sys.exit(1)  
        
    print("La respuesta correcta es:")
    print(questions_to_ask[j][1][questions_to_ask[j][2]])

    print()  

print (f"el puntaje total obtenido es:{puntaje}")


