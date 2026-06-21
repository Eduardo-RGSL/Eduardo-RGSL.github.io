'''calculadora_operaciones_v1'''

print("Bienvenido a la calculadora de ASIR")
num1 = float(input("Introduce el primer número: "))
operacion = input(
    "Introduce la operación a realizar (suma, resta, multiplicación o división): ").lower()
num2 = float(input("Introduce el segundo número: "))
if operacion == "suma":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif operacion == "resta":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif operacion == "multiplicación":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif operacion == "división":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: Indeterminación.")
else:
    print("Operación no válida. Por favor, introduce una operación correcta.")



with open("calculadora.txt", "w") as calcu:
    print("Bienvenido a la calculadora de ASIR")
    num1 = float(input("Introduce el primer número: "))
    operacion = input(
        "Introduce la operación a realizar (suma, resta, multiplicación o división): ").lower()
    num2 = float(input("Introduce el segundo número: "))
    if operacion == "suma":
        resultado = num1 + num2
        print("El resultado de la suma es:", resultado)
    elif operacion == "resta":
        resultado = num1 - num2
        print("El resultado de la resta es:", resultado)
    elif operacion == "multiplicación":
        resultado = num1 * num2
        print("El resultado de la multiplicación es:", resultado)
    elif operacion == "división":
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)
        else:
            print("Error: Indeterminación.")
    else:
        print("Operación no válida. Por favor, introduce una operación correcta.")
    calcu.write(f'El resultado de la operación es {resultado}')


