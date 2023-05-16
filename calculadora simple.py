print("calculadora simple")

numero_1 = str(input("ingrese un numero:"))
numero_2 = str(input("ingrese otro numero:"))

if numero_1.isnumeric() and numero_2.isnumeric():
    numero_1 = int(numero_1)
    numero_2 = int(numero_2)
else:
    raise ValueError("incorrecto, no se permiten letras solo numeros")
opcion_1 = 0

while opcion_1 != 4:

    print("""
    indique la opcion que desee realizar:
    1) suma
    2) resta
    3) multiplicacion
    4) division
    """)

    opcion_1 = int(input()) 

    if opcion_1 == 1:
        print(" ")
        print("el resultados es:", numero_1, "+", numero_2, "=",  numero_1 + numero_2)
    if opcion_1 == 2:
        print(" ")
        print("el resultado es:", numero_1, "-", numero_2, "=", numero_1 - numero_2)
    if opcion_1 == 3:
        print(" ")
        print("el resultado es:", numero_1, "*", numero_2, "=", numero_1 * numero_2)
    elif opcion_1 == 4:
     if numero_2 > 0:
        print(" ")
        print("el resultado es:", numero_1, "/", numero_2, "=", numero_1 / numero_2)
     else:
         raise ZeroDivisionError("no se puede dividir entre cero, intente otro datos")