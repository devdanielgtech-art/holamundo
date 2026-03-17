# Funciones Son bloques de codigo que realiza una tarea especifica y que son reutilizables

# Funcion sin parámetros ni devolución de valor
def saludar():
    print("Hola, bienvenidos al curso de Python")

# Funcion con parámetros
def saludo(nombre):
    print("Hola " + nombre + " bienvenido a clases")

# Llamada a la funcion
saludo("Daniel")
saludo("Juana")

# Funcion que devuelve valores
def suma(a, b):
    return a + b

# Llamada a la funcion
resultado = suma(10, 4)
print("La suma es:", resultado)

# Establecer valores por defecto para los parametros de una funcion
def bienvenida(nombre="Estudiante"):
    print("Bienvenido", nombre)

# Llamada a la funcion
bienvenida()
bienvenida("Susana")


# Funcion con argumentos variables
def sumador(*args):
    return sum(args)

# Llamada a la funcion
print(sumador(1,2,3,4,5))
print(sumador(4,5,6))