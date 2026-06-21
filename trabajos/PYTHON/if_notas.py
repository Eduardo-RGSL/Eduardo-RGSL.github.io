'''Ejercicio de nota'''
nota = float(input("Introduce la nota:"))
print(nota)
mensaje = "nada"
if nota > 10:
    mensaje = "Fuera Rango"
elif nota == 10:
    mensaje = "Matrícula de honor"
elif nota >= 9:
    mensaje = "Sobresaliente"
elif nota >= 7:
    mensaje = "Notable"
elif nota >= 6:
    mensaje = "Bien"
elif nota >= 5:
    mensaje = "Aprobado"
elif nota >= 0:
    mensaje = "Suspenso"
else:
    mensaje = "No es una nota"  # Para números negativos
print(mensaje)
