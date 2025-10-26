"""
Ejercicio 1
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar, multiplicar, dividir y terminar.
Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. Si se introduce una opción incorrecta se
muestra un mensaje de error. El menú se volverá a mostrar, a menos que no se de a la opción terminar.

- Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera). Las variables se inicializan a cero.
- Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente no se puedan ejecutar el resto de las opciones.
- Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción (por su número) y devuelve la opción escogida.
  Modifica el último programa para que use esta función.
"""

# pedir datos
# num1 = int(input("Introduce un numero: "))
# num2 = int(input("Introduce un numero: "))
num1 = 0
num2 = 0

# menu
while True:
    """
    opcion = int(input(
        "¿Qué opción eliges?\n"
        "1 - Añadir numeros\n"
        "2 - Sumar\n"
        "3 - Restar\n"
        "4 - Multiplicar\n"
        "5 - Dividir\n"
        "6 - Terminar\n"
        "👉 Elige una opción: "
    ))
    """
    opcionesMenu = ["Anadir numeros", "Sumar", "Restar", "Multiplicar","Dividir","Terminar"]

    # funciones
    def anadirmenu(menu):
        for i, opcion in enumerate(menu, start=1):
            print(f"{i}. {opcion}")

            # Pedir opción al usuario
        opcion = int(input("Elige una opción (número): "))
        return opcion

    def anadirNumeros():
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce un numero: "))
        return num1, num2
    def suma(num1, num2):
        print(f"La suma de {num1} y {num2} es {num1 + num2}. \n")


    def resta(num1, num2):
        print(f"La resta de {num1} y {num2} es {num1 - num2}.\n")


    def multiplicar(num1, num2):
        print(f"La multiplicacion de {num1} y {num2} es {num1 * num2}.\n")


    def dividir(num1, num2):
        print(f"La division de {num1} y {num2} es {num1 / num2}.\n")

    opcion = anadirmenu(opcionesMenu)
    # comprobar opciones
    match opcion:
        case 1:
            numeros = anadirNumeros()
            num1 = numeros[0]
            num2 = numeros[1]
        case 2:
            if num1 == 0 and num2 == 0:
                print("Debes de introducir los numeros primero\n")
                continue
            suma(num1, num2)
        case 3:
            if num1 == 0 and num2 == 0:
                print("Debes de introducir los numeros primero\n")
                continue
            resta(num1, num2)
        case 4:
            if num1 == 0 and num2 == 0:
                print("Debes de introducir los numeros primero\n")
                continue
            multiplicar(num1, num2)
        case 5:
            if num1 == 0 and num2 == 0:
                print("Debes de introducir los numeros primero\n")
                continue
            dividir(num1, num2)
        case 6:
            exit()
        case _:
            print("Error: Introduce un numero valido\n")





