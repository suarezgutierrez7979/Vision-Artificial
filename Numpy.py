import numpy as np

arr = np.array([1, 2, 3])

print ("Contenido del arreglo:", arr)
print ("Tipo de datos del arreglo:", type(arr))

#Los arrays de NumPy son homogéneos, es decir, todos sus elementos son del mismo tipo.
# Si le pasamos a np.array una secuencia con objetos de tipos diferentes, promocionará todos 
# al tipo con más información. 
# Para acceder al tipo del array, podemos usar el atributo dtype.

a = np.array([1, 2, 3.0])
print(a.dtype)

#NumPy intentará automáticamente construir un array con el tipo adecuado teniendo 
# en cuenta los datos de entrada, aunque nosotros podemos forzarlo.

np.array([1, 2, 3], dtype=float)
np.array([1, 2, 3], dtype=complex)

#También podemos convertir un array de un tipo a otro utilizando el método .astype.
a.astype(int)

a = np.array([
    [1, 2, 3],
    [4, 5, 6]])

# Se especifica la fila y la columna en 2 corchetes 
print (a[0][1])

# Se simplifica la notación usando solo un corchete y los 2 índices (Esta es la más usada)
print (a[0,1])

# Obtenga la fila 0, columnas 1 y 2
a[0, 1:3]
# Obtenga las filas 0 y 1 y las columnas 0 y 1
a[0:2, 0:2]

#Unos y Ceros
# Es muy común que se requiera crear arreglos especiales cuyo contenido sean unos y ceros. Estas son las formas más comunes para hacerlo:
# zeros(shape) y ones(shape) crean arreglos de ceros y unos, respectivamente. EL parámetro shape es una tupla con el número de filas y columnas del arreglo.
# empty(shape) crea un array con «basura», equivalente a no inicializarlo, ligeramente más rápido que zeros o ones
# eye(N, M=None, k=0) crea un array con unos en una diagonal y ceros en el resto
# identity(n) devuelve la matriz identidad
# full(shape, fill_value) crea una matriz cuyo contenido está especificado por el valor fill_value
# Las funciones *_like(a) construyen arrays con el mismo tamaño que uno dado

# Se crea una matriz de 2 filas y 3 columnas de ceros. Note que el tamaño se especifica en una tupla (fila, columna)
A = np.zeros((2,3))
print ("Matriz de ceros reales:\n", A)

# Note que el tipo es real. Si se requiere algún tipo específico este deber especificado en la creación
A = np.zeros((2,3), dtype=int)
print ("\nMatriz de ceros enteros:\n", A)

# Crea una matriz diagonal de 4x4. Si la matriz es cuadrada esta función solo requiere un parámetro
A = np.eye(4)
A

# Arreglos con Rangos
# En algunas ocasiones es necesario crear arreglos conciertos rangos específicos:

# arange(start, stop, step) devuelve números equiespaciados dentro de un intervalo
# linspace(start, stop, num=50) devuelve números equiespaciados dentro de un intervalo
# logspace(start, stop, num=50, base=10.0) devuelve números equiespaciados según una escala logarítmica
# meshgrid(x1, x2, ...) devuelve matrices de n-coordenadas

# Crea un arreglo con 5 valores en el rango entre 0 y 10 (sin incluirlo) saltando de a 2
A = np.arange(0,10,2).astype(float)

# Crea un arreglo con 5 valores equiespacidos en el rango entre 0 y 1
B = np.linspace(0,1, num=5)

print ("A=",A, "\nB=",B)

# La función np.meshgrid se utiliza mucho a la hora de representar funciones en dos dimensiones, 
# y crea dos arrays: uno varía por filas y otro por columnas. Combinándolos, podemos evaluar la función en un cuadrado.

x = np.linspace(1, 5, num=5)
y = np.linspace(1, 5, num=5)

xx, yy = np.meshgrid(x, y)
print(xx,"\n\n",yy)

#Comparando Arreglos¶
#Algunas veces es necesario realizar comparaciones entre arreglos. Esta es una forma de hacerlo:

# Crea un arreglo del 0 al 6
A = np.arange(6)

# Crea un arreglo de unos
B = np.ones(6).astype(int)

print ("A=",A, "\nB=",B)

# Comparación elemento a elemento
A <= B

# Determina si ALGÚN elemento cumple la condición
np.any(A < B)

# Determina si TODOS elemento cumple la condición
np.all(A < B)


# Operaciones básicas
# Veamos ahora algunos ejemplos con opearaciones básicas entre arreglos:

# Se crean dos matrices de 3x3 con contenido aleatorio en el rango [-9, 10) de tipo entero
A = np.random.randint(-9,10, size=16).reshape(4, 4)
B = np.random.randint(-9,10, size=16).reshape(4, 4)

print (A, "\n\n",B)

# Se suma un valor a toda la matriz
A = A+10
A

# Se multiplica por un valor todos los elementos de la matriz
B = B*2
B

# Se resta 5 los elementos entre las filas 1 y 3(excluida) y columnas 0 y 2(excluida)
A[1:3, 0:2] = A[1:3, 0:2] - 5
A

# Se suma el contenido de las 2 matrices, elemento a elemento
C = A + B
C