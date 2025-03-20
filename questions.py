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



for i in range(3):

    j=i
    print(questions_to_ask[i][0]) 

    for i, respuesta in enumerate(questions_to_ask[i][1], start=1):
        print(f"{i}. {respuesta}")  
    
    for intento in range(2):

           
            user_answer = input("Respuesta (1-4): ") 
            if user_answer.isnumeric():
                if respuesta_permitida(user_answer, {"1", "2", "3", "4"}):
                    answer = int(user_answer) -1 
                    if answer  == questions_to_ask[j][2]:
                        print("¡Correcto!")
                        puntaje +=1
                        break  
                    else:
                        print("Incorrecto. Intenta de nuevo.")
                        if puntaje  > 0 and intento == 0 : 
                            puntaje -=0.5
                        """
                            Si la persona vuelve a responder mal la misma pregunta , no decrementa el puntaje.
                            Esto lo hago para evitar distintos resultados para la misma cantidad de aciertos.
                        """
                else:
                        print("Respuesta NO válida*")
                        sys.exit(1)  

            else:       
                    print("Respuesta NO valida")
                    sys.exit(1)  
            if (intento==1):  #Si la persona respondia mal dos veces ,se muestra cual era la respuesta correcta.  
                print("La respuesta correcta es:")
                print(questions_to_ask[j][1][questions_to_ask[j][2]])

    print()  

print (f"el puntaje total obtenido es:{puntaje}")


