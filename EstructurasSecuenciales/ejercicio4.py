# 11. Dado un número de dos cifras, diseñe un programa que
# permita obtener el número invertido.

num = int(input("Ingresa un numero de dos cifras: "))
# Convertir a cadena para poder invertirlo
convertirNumAString = str(num)
# Invertir el número usando slicing
numInvertido = convertirNumAString[::-1]

#mostramos el numero invertido
print(f"El numero invertido: {numInvertido}")