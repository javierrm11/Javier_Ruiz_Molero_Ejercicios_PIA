"""
Date: 20/10/2025
@author: Javier Ruiz Molero

Ejercicio 6
Escribir un programa para calcular la nota final de un examen, considerando que:

cada respuesta correcta suma 5 puntos
cada respuesta incorrecta suma -1 puntos
cada respuesta en blanco suma 0 puntos.
Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes
tipos de respuestas puedan cambiar en el futuro?
Puntos configurables (fácil de modificar en el futuro)
"""

POINTS_CORRECT = 5
POINTS_INCORRECT = -1
POINTS_BLANC = 0

result = 0

quenstions = {
    "¿Cómo se llama la provincia?": "Córdoba",
    "¿En qué comunidad autónoma se encuentra Córdoba?": "Andalucía",
    "¿Qué famoso monumento combina elementos islámicos y cristianos?": "La Mezquita-Catedral",
    "¿Qué río atraviesa la ciudad de Córdoba?": "Guadalquivir",
    "¿Qué fiesta popular cordobesa fue declarada Patrimonio Inmaterial de la Humanidad?": "Los Patios de Córdoba",
    "¿Qué filósofo cordobés fue una de las grandes figuras del pensamiento árabe?": "Averroes",
    "¿Qué poeta romano famoso nació en Córdoba?": "Séneca",
    "¿Cómo se llama el casco antiguo declarado Patrimonio de la Humanidad?": "Centro histórico de Córdoba",
    "¿Qué plato típico cordobés está hecho con pan, tomate, ajo y aceite de oliva?": "Salmorejo",
    "¿Qué nombre recibe el famoso puente de piedra que cruza el Guadalquivir?": "Puente Romano"
}

# Recorrer preguntas
for quenstion, answer_correct in quenstions.items():
    answer = input(quenstion + " ")

    if answer.strip() == "":
        print("Respuesta en blanco.")
        result += POINTS_BLANC

    elif answer.strip().lower() == answer_correct.lower():
        print("Pregunta correcta.")
        result += POINTS_CORRECT

    else:
        print(f"Pregunta incorrecta. La respuesta correcta era: {answer_correct}.")
        result += POINTS_INCORRECT

    print(f"Puntuación actual: {result}\n")

# Calcular nota normalizada entre 0 y 10
max_posible = len(quenstions) * POINTS_CORRECT
note_normal = max(0, (result / max_posible) * 10)

print("=====================================")
print(f"Puntuación total: {result}")
print(f"Nota normalizada (0-10): {note_normal:.2f}")
