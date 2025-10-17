#Escribir un programa para calcular la nota final de un examen, considerando que:

# cada respuesta correcta suma 5 puntos
# cada respuesta incorrecta suma -1 puntos
# cada respuesta en blanco suma 0 puntos.
#Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
#¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes
# tipos de respuestas puedan cambiar en el futuro?
# Puntos configurables (fácil de modificar en el futuro)

PUNTOS_CORRECTA = 5
PUNTOS_INCORRECTA = -1
PUNTOS_BLANCO = 0

resultado = 0

preguntas = {
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
for pregunta, respuesta_correcta in preguntas.items():
    respuesta = input(pregunta + " ")

    if respuesta.strip() == "":
        print("Respuesta en blanco.")
        resultado += PUNTOS_BLANCO

    elif respuesta.strip().lower() == respuesta_correcta.lower():
        print("✅ Pregunta correcta.")
        resultado += PUNTOS_CORRECTA

    else:
        print(f"❌ Pregunta incorrecta. La respuesta correcta era: {respuesta_correcta}.")
        resultado += PUNTOS_INCORRECTA

    print(f"Puntuación actual: {resultado}\n")

# Calcular nota normalizada entre 0 y 10
maximo_posible = len(preguntas) * PUNTOS_CORRECTA
nota_normalizada = max(0, (resultado / maximo_posible) * 10)

print("=====================================")
print(f"Puntuación total: {resultado}")
print(f"Nota normalizada (0-10): {nota_normalizada:.2f}")
