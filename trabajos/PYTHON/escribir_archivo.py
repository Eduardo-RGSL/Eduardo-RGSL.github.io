'''Escribir en archivo'''

# Modo 'a' (Append): Añade la línea al final del archivo, sin borrar lo que ya estaba escrito.

with open("append.txt", "a") as fichero:
    print("a")
    fichero.write("Hola, este es un texto de prueba\n")
    print("a")
    fichero.write("Esto es la segunda línea\n")

día = "Jueves"
with open("escribe.txt", "w") as fichero:
    print("b")
    fichero.write(f'La variable {día}\n')
    print("b")
    fichero.write("Segunda\n")
