'''calculadora_operacionesd_v2'''

print("Bienvenido a la calculadora de ASIR")
num1 = float(input("Introduce el primer número: "))
while True:
    operacion = input("Introduce la operación a realizar (suma, resta, multiplicación, división) o FIN para salir: ").upper()
    if operacion == "FIN":
        print("Se cerró la calculadora.")
        break
    num2 = float(input("Introduce el segundo número: "))
    
    if operacion == "SUMA":
        resultado = num1 + num2
    elif operacion == "RESTA":
        resultado = num1 - num2
    elif operacion == "MULTIPLICACIÓN":
        resultado = num1 * num2
    elif operacion == "DIVISIÓN":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: Indeterminación.")
    else:
        print("Operación no válida. Por favor, introduce una operación correcta.")
    
    print(f"La {operacion.lower()} de {num1} y {num2} es: {resultado}")
    num1 = resultado

