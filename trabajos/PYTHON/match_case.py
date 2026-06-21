'''match case estructura'''

while True:
    try:
        nota = input("Introduce la nota: ")
        nota = float(nota)
        break
    except ValueError:
        print("Introduce un valor numérico, por favor")

print(nota)
mensaje = "nada"
match nota:
    case n if n > 10:
        mensaje = "Nota fuera de rango"
    case n if n == 10:
        mensaje = "Matrícula de honor"
    case n if n >= 9:
        mensaje = "Sobresaliente"
    case n if n >= 7:
        mensaje = "Notable"
    case n if n >= 6:
        mensaje = "Bien"
    case n if n >= 5:
        mensaje = "Aprobado"
    case n if n >= 0:
        mensaje = "Suspenso"
    case n if n < 0:
        mensaje = "No es una nota"  # Para números negativos
print(mensaje)

# El codigo anterior es incorrecto porque no se pueden usar comparaciones directas en los casos de match case. En su lugar, se deben usar patrones de guardia para evaluar las condiciones. El código corregido sería:
# Lo correcto sería:
while True:
    try:
        nota = input("Introduce la nota: ")
        nota = float(nota)
        break
    except ValueError:
        print("Introduce un valor numérico, por favor")

print(nota)
mensaje = "nada"
match nota:
    case n if n > 10:
        mensaje = "Nota fuera de rango"
    case n if n == 10:
        mensaje = "Matrícula de honor"
    case n if n >= 9:
        mensaje = "Sobresaliente"
    case n if n >= 7:
        mensaje = "Notable"
    case n if n >= 6:
        mensaje = "Bien"
    case n if n >= 5:
        mensaje = "Aprobado"
    case n if n >= 0:
        mensaje = "Suspenso"
    case n if n < 0:
        mensaje = "No es una nota"  # Para números negativos
print(mensaje)

