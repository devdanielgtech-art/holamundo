##################################################################
########          UNIVERSIDAD PUBLICA DE EL ALTO              ####
########          CARRERA:INGENIERIA DE SISTEMAS              ####
########        ESTUDIANTE: DANIEL QUISPE GUTIERREZ           ####
##################################################################
##################################################################
##################################################################
# SE TIENE TODOS LOS CODIGOS DEL VIDEO EN ESTE MISMO ARCHIVO .PY##
##################################################################
# SE REALIZO DE MANERA APARTE CADA CODIGO PARA QUE SE PUEDA     ##
# VERIFICAR SU FUNCIONAMIENTO DE LOS CODIGOS ,ENUMERADOS EN EL  ##
# ORDEN DEL VIDEO                                               ##
##################################################################
                      ####
                      ####
                      ####
                    ########
                     ######
                      ####
                       ##

    #EN LA PARTE DE ABAJO SE ENCUENTRA TODCOMPLETO EL CODIGO JUNTO PERO PARA 
    #SU PRUEBA Y VERIFICACION EJECUTE LOS DEMAS CODIGOS.
    





print ("Hola mundo desde Python!!")
# Variables en Python 
# Enteros
edad = 20
# Float 
precio = 50.5
# Str
nombre = "Bruno Diaz"
# Bool
bandera = True

# SALIDA
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Precio:"+ str(precio))

# ENTRADA
nombre= input("Introduce tu nombre: ")
print("Hola "+nombre)

#######################3
# ENTRADA 
num1 = input("Ingresa el primer número: ")
num2 = input("Ingrese el segundo número: ")

# Conversion de str a int, str a float, str a float 
suma = float(num1) + float(num2)

print("La suma es:", suma)

###########################
curso ="Python para iniciantes"
#METODOS

print(curso.upper())
print(curso)
print(curso.lower())
print(curso.capitalize())

# Busquedas
print(curso.find("h"))
print(curso.find("cia"))

# Reemplazos
print(curso.replace("para", "FOR"))
print(curso)

# Operador
print("para" in curso)

####################
# Operadores matematicos
print(10 + 5)
print(105)
print(10 * 5)
print(10 / 4)

# Division entera
print(10 // 4)

# Modulo residuo
print(10 % 3)

# Exponente
print(2 ** 4)

x = 10
x = x + 5
print(x)

# Operador de asignacion compacto
y = 20
y += 5
print(y)

# Operador de asignacion compacto *
y = 20
y *= 5
print(y)

# Precedencia
x = 10 + (3 * 2)
print(x)



####################3
# Expresiones booleanas True o False
# >, >=, <, <=, ==, !=   OP . Relacionales
x = 3 > 2
print(x)

x = 5 == 3
print(x)

x = 5 != 3
print(x)

# and, or not Op. logicos
precio = 25
print(precio > 20 and precio < 30)

precio = 5
print(precio > 20 or precio < 30)
print(not precio > 10)



#################

# Sentencis
temperatura = 18

if temperatura > 28:
    print("Esta haciendo calor")
else:
    print("hace frio")
    
if temperatura > 28:
    print("Esta haciendo calor")
elif temperatura > 20:
    print("Es un dia agradable")
elif temperatura > 10:
    print("Hace un poco de frio")
else:
    print("hace frio, brrrr")

print("Proceso concluido")


############
# Sentencis
temperatura = int(input("Indica la tpetemperatura : "))


if temperatura > 28:
    print("Esta haciendo calor")
else:
    print("hace frio")
    
if temperatura > 28:
    print("Esta haciendo calor")
elif temperatura > 20:
    print("Es un dia agradable")
elif temperatura > 10:
    print("Hace un poco de frio")
else:
    print("hace frio, brrrr")

print("Proceso concluido")


####################3
# Bucles
contador = 12
while (contador <= 20):
    print(contador)
    contador += 1

i = 1
while (i <= 10):
    print(i * "#")
    i += 1
    
####################33
# Listas
frutas = ['Manzana', 'Fresa', 'naranjas', 'Pera', 'Maracuyá']

print(frutas)
print(frutas[0])
print(frutas[4])
print(frutas[-2])
print(frutas[1:4])
    
    
    
######################

# Metdos de listas
numeros = [1,2,3,4,5]

# Adicionar elementos a una lista
numeros.append(6)
print(numeros)

# Insertar ELEMEMTOS en una posision determinada
numeros.insert(0,-1)
print(numeros)

numeros.insert(1,0)
print(numeros)

# Elimina un elemento en su primera aparicion
numeros.remove(1)
print(numeros)

# Verificar si un elemento se encuentra en la lista
print(4 in numeros)

# Tamanño de la lista
print(len(numeros))

# Elimina el contenido de la lista
numeros.clear()

# Elimina el contenido de la lista
numeros.clear()
print(numeros)


##########################
# Objeto range
numeros = range(5)

print(numeros)

for item in numeros:
    print(item)

for item in range(5,10):
    print(item)

for item in range(10,20,2):
    print(item)
    
################

# Tuplas (inmutables)
numeros = (1,2,5,4,5,6)

# Imprimiento un elemento
print(numeros[3])

# Ocurrencia
print(numeros.count(5))
print(numeros.index(5))

####################
# Diccionarios -> Almacen a pares de clave-valor
mi_diccionario = {'nombre': 'Daniel', 'edad': 21, 'ciudad': 'La Paz'}
print(mi_diccionario)

# Acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])

# Agregar elementos
mi_diccionario['profesion'] = 'Ingeniero'
print(mi_diccionario)

# Eliminar un elemento
del mi_diccionario['ciudad']
print(mi_diccionario)

# Obtener claves del diccionario
print(mi_diccionario.keys())

# Obtener valores del diccionario
print(mi_diccionario.values())

# Verificar si una clave existe
if 'ciudad' in mi_diccionario:
    print("Clave encontrada")

# Recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[Clave: ]", clave, "[Valor: ]", valor)
    
    
###############

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
