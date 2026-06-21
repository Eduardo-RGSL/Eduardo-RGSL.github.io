'''Formato de variables tipo string'''
nombre = "Pedro"
Apellido1 = "Guerrero"
Apellidos2 = "López"

# Vamos a concatenar (unir) strings usando el operador +
# que si está rodeado de string, los concatena

nombre_completo = nombre + Apellido1 + Apellidos2
print(nombre_completo)

nombre_completo = nombre + " " + Apellido1 + " " + Apellidos2
print(nombre_completo)

# Se usa f "{}espacio en blanco()" format()

nivel = "Funddamentos de"
tipo = "Programación"
lenguaje = "Python"
nombre_módulo = f"{nivel} {tipo} {lenguaje}"
print(nombre_módulo)

# Conseguir el siguiente texto GBD = 6 horas por semana
módulo = "Gestión de Bases de Datos"
día1 = 1
día2 = 3
día3 = 2
datos_módulos = f"{módulo[0]}{módulo[11]}{módulo[20]} {"="} {día1 + día2 + día3} {"horas por semana"}"
print(datos_módulos)
