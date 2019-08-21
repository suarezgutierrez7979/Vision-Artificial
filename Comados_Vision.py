# Siempre que usemos matplotlib en Jupyter es necesario poner esta línea antes de cualquier otra
%matplotlib inline

# Importamos las bibliotecas necesarias y les asignamos un alias
import skimage                           # Biblioteca para la manipulación de imágenes
import numpy as np                       # Biblioteca para la manipulación de matrices

# Importamos algunos paquetes específicos
from matplotlib import pyplot as plt     # Biblioteca para crear graficas y mostrar las imágenes en pantalla
from skimage import data                 # Paquete con imágenes de prueba
from skimage import io                   # Paquete para lectura/escritura de imágenes


#Como ejemplo básico, partimos de una matriz que representa un tablero de ajedrez, 
#como el de la práctica anterior. Dicha matriz no es más que una imagen en blanco y negro. 3
#En este caso, el blanco está representado por el valor 255 y el negro por el valor 0.

tablero= np.zeros ((8,8), dtype='uint8')
tablero [::2, 1::2] = 255
tablero [1::2, ::2] = 255

#Se muestra la matriz numerica
print (tablero)

# Se visualiza la imagen que representa la matriz
plt.imshow (tablero, cmap='gray')

# Generamos una matriz de 500X500 con contenido aleatorio 
random_img= np.random.random ([500,500])
plt.imshow (random_img, cmap='gray')
#Agregamos la paleta de color
plt.colorbar();

print ("Tipo de imagen del tablero de ajedrez:", tablero.dtype)
print ("Tipo de imagen aleatoria: ", random_img.dtype)

#Ahora, usemos una de las imágenes de prueba de Scikit-Image. Es aquí donde usamos el paquete data de skimage.
#Analice la información que se muestra y las funciones que usamos para mostrar dicha información.

coins = data.coins()
#Mostramos su informacion 
print ("Tipo:", type(coins))
print ("Tipo NumPy:" , coins.dtype)
print ("Dimensiones" , coins.shape)

#Mostramos la imagen 
plt.imshow (coins, cmap='gray')

#Usemos ahora una imagen llamada chelsea del repositorio de Scikit-image. Esta imagen es a color, 
#así que preste atención a la información de la misma.

cat = data.chelsea();
#Mostramos su informacion 
print ("Tipo:", type(cat))
print ("Tipo NumPy:" , cat.dtype)
print ("Dimensiones:" , cat.shape)
print ("Valor Minimo:", cat.min())
print ("Valor Maximo:", cat.max())

plt.imshow(cat)

cat_ubyte= skimage.img_as_ubyte(cat)
print('\ncat_ubyte\nTipo NumPy:', cat_ubyte.dtype)
print ("Valor minimo:", cat.min())
print ("Valor maximo:", cat.max())

#convierte la imagen a una representacion usando float
cat_float= skimage.img_as_float(cat)
print('\ncat_ubyte\nTipo NumPy:', cat_float.dtype)
print ("Valor minimo:", cat.min())
print ("Valor maximo:", cat.max())

# En la imagen, de la fila 10 a la fila 110 (dimensión 0 del arreglo 3D)
# En la imagen, de la columna 210 a la columna 310 (dimensión 1 del arreglo 3D)
# En los 3 canales (RGB) se asigna la tripleta 255, 0, 0: máximo valor al canal rojo y mínimo valor al azul y verde

cat[10:110, 210:310, 0] = 255
cat[10:110, 210:310, 1]= 0
cat[10:110, 210:310, 2]= 0

plt.imshow (cat); #Dibuja un cuadrado rojo en la imagen actual

#Recuerde que para una imagen a color se deben usar tres índices que en su orden son: filas, columnas y canales, así la instrucción:

#cat[10:110, 210:310, 0] = 255

#Está accediendo a los píxeles tales que están:

#Entre las filas 10 y 110 (excluida esta última)
#Entre las columnas 210 y 310 (excluida esta última)
#En el canal 0, que en el formato RGB es el canal Rojo


#Como hemos visto de los ejemplos anteriores, para mostrar una imagen se usa el comando imshow de la biblioteca de matplotlib. 
#Veamos una variación de este comando.

# Cargamos la imagen chelsea en la variable img0
img0 = data.chelsea() 

#Cargamos la imagen rocket en la variable img1

img1= data.rocket()

# La función subplots divide el espacio de la figura en subfiguras
# Los dos primeros parámetros que usamos aquí son el número de filas y columnas del subplot
# el tercer parámetro, figsize, es un parámetro que define el tamaño relativo de los subplots

f, ax = plt.subplots(1, 2, figsize=(20,10))

# Se muestra en el primer subplot la imagen 0, se le asigna un título y se eliminan los ejes del gráfico
ax[0].imshow(img0) # se muestra el primer subplot de la imagen 0
ax[0].set_title('Cat', fontsize=18) # se le asigna un titulo a la imagen y un tamaño
ax[0].axis ('off') # se le eliminan los ejes al grafico


# Se muestra en el primer subplot la imagen 0, se le asigna un título y se eliminan los ejes del gráfico
ax[1].imshow(img1) # se muestra el primer subplot de la imagen 0
ax[1].set_title('Rocket', fontsize=18) # se le asigna un titulo a la imagen y un tamaño
ax[1].set_xlabel(r'lauching position $\alpha=320$') # se le agregan los ejes al grafico




# Así de fácil se lee una imagen de disco
img = io.imread("imagenes/img1.jpg")

print('Información de la Imagen:')
print('Tipo:', type(img))
print('Tipo de dato:', img.dtype)
print("Dimensiones:", img.shape)
print("Valor min:", img.min())
print("Valor max:", img.max())

plt.imshow(img)
plt.axis('off')


#Una funcionalidad adicional consiste en cargar múltiples imágenes que están en un directorio. 
# Vea cómo hacerlo en el siguiente ejemplo:

# Se leen todas las imágenes con extensión JPG
ic = io.ImageCollection('imagenes/*.jpg')
​
print('Type:', type(ic))
ic.files
​
​
print("Cantidad de imágenes leídas: ", len(ic))

# Para mostrar la colección de imágenes requerimos un paquete para administrar lo comando del sistema operativo
import os

# Se crea el subplot. Note que son 3 columnas, pero el número de filas depende del número de imágenes
f, axes = plt.subplots(ncols=3, nrows=len(ic) // 3, figsize=(20,15))

# La función revel se usa para aplanar el arreglo y tratarlo como un arreglo 1D. Esto facilita el uso de ciclos
axes = axes.ravel()

# Se eliminan los ejes de cada subplot
for ax in axes:
    ax.axis('off')

# Se muestra cada imagen y se le agrega un título
for i,image in enumerate(ic):
    axes[i].imshow(image, cmap='gray')
    axes[i].set_title(os.path.basename(ic.files[i]))


#Además de leer una imagen, en los proyectos de visión también se hace necesario almacenar una 
#imagen que es el resultado de una operación. Para ello usamos el comando io.imsave, tal como lo hacemos a continuación:

# Modificamos la imagen en la variable img
# La modificación consiste en dibujar un cuadro verde 100x100 en el centro de la imagen
w,h,c = img.shape

img[w//2-50:w//2+50, h//2-50:h//2+50, :] = [0, 255, 0]

plt.imshow(img)
plt.axis('off')

io.imsave('imagenes/img1_modificada.jpg', img)

# Modificamos la imagen en la variable img
# La modificación consiste en dibujar un cuadro verde 100x100 en el centro de la imagen
w,h,c = img.shape
​
img[w//2-50:w//2+50, h//2-50:h//2+50, :] = [0, 255, 0]
​
plt.imshow(img)
plt.axis('off')
​
io.imsave('imagenes/img1_modificada.jpg', img)

