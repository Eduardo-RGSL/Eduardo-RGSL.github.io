'''Iterables con Loop for'''
# Iterables
for n in "Administración de sistemas informáticos en red":
    print(n)

for caracter in "Administración de sistemas informáticos en red":
    print(caracter)

with open("iterables.txt", "a") as fichero:
    for n in "Programación con Python":
        fichero.write(f'{n}\n')
