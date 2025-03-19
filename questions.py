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

for _ in range(3):
    
    question_index = random.randint(0, len(questions) - 1)
    print(questions[question_index])
    
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")
    
    for intento in range(2):
        user_answer = input("Respuesta (1-4): ")

        try:
           
            user_answer = int(user_answer) - 1
            
            if respuesta_permitida(user_answer, {0, 1, 2, 3}):
                if user_answer == correct_answers_index[question_index]:
                    print("¡Correcto!")
                    puntaje +=1
                    break  
                else:
                    print("Incorrecto. Intenta de nuevo.")
                    puntaje -=0.5
            else:
                print("Respuesta NO válida")
                sys.exit(1)  

        except ValueError:
            print("Respuesta NO valida")
            sys.exit(1)  
        
    else:
        print("La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])

    print()  

print (f"el puntaje total obtenido es:{puntaje}")


