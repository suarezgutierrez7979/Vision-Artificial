# Siempre que usemos matplotlib en Jupyter es necesario poner esta línea antes de cualquier otra
%matplotlib inline

# Importamos las bibliotecas necesarias y les asignamos un alias
import skimage                           # Biblioteca para la manipulación de imágenes
import skimage.transform as tf
import numpy as np                       # Biblioteca para la manipulación de matrices

# Importamos algunos paquetes específicos
from matplotlib import pyplot as plt     # Biblioteca para crear graficas y mostrar las imágenes en pantalla
from skimage import data                 # Paquete con imágenes de prueba
from skimage import io                   # Paquete para lectura/escritura de imágenes


#Ejercicio 1. Pixelar una Imagen
#La idea de este punto consiste en desarrollar una función que dada una imagen, 
# obtenga una versión pixelada de la misma. Como ejemplo, a continaución se muestra una imagen (la versión original) 
# y su versión pixelada con un parámetro de n=10.

#Pista: para realizar esto escoja grupos de píxeles a interválos regulares en la imagen original y use el color de ese píxel 
# para colorear una región más grande en la imagen de salida.

# Función que pixela una imagen img usando "pixeles" de tamaño n
def pixelar_imagen(img, n=10):

    # En Python se debe trabajar sobre una copia para no alterar la imagen original
    out = img.copy()

    # TODO: Implemente su código aquí
    for i in range(10, out.shape[0], 10):
        for j in range(10, out.shape[1], 10):
            out[i-10:i,j-10:j] = out[i,j]

    return out

# Cargue la imagen img7.jpg de la carpeta imágenes de esta práctica
img7 = io.imread("imagenes/img6.jpg")

# Se invoca la función recientemente implementada
out_img7 = pixelar_imagen(img7)

# Muestre la imagen de salida
io.imshow(out_img7)

# Cargue la imagen img3.png de la carpeta imágenes de esta práctica
img3 = io.imread("imagenes/img3.png")

# Se invoca la función recientemente implementada
out_img3 = pixelar_imagen(img3)

# Muestre la imagen de salida
io.imshow(out_img3)

# Cargue la imagen img4.jpg de la carpeta imágenes de esta práctica
img4 = io.imread("imagenes/img4.jpg")

# Se invoca la función recientemente implementada
out_img4 = pixelar_imagen(img4)

# Muestre la imagen de salida
io.imshow(out_img4)

# Ejercicio 2. Generar un Calidoscopio
# Con esta función lo que se pretende es generar un calidoscopio a partir de la imagen original. 
# Como ejemplo, a continuación se muestra una imagen y su versión calidoscopio usando un parámetro de n=2 y n=4

#Pista: para poder realizar este ejercicio se debe investigar como escalar y cómo hacer un espejo (o voltear) 
# una imagen usando skimage.

# Función que genera una imagen calidoscopio de la imagen original. 
# El parámetro n determina cuantas veces se repite la imagen original en filas y columnas
# Función que genera una imagen calidoscopio de la imagen original. 
# El parámetro n determina cuantas veces se repite la imagen original en filas y columnas
# Función que genera una imagen calidoscopio de la imagen original. 
# El parámetro n determina cuantas veces se repite la imagen original en filas y columnas
def calidoscopio_imagen(img, n=2):
    
    # En Python se debe trabajar sobre una copia para no alterar la imagen original
    out = img.copy()
    
    # TODO: Implemente su código aquí    
    for i in range(0, n, 2):
        out = np.concatenate([np.flipud(out),out], axis=0)     
        out = np.concatenate([out, np.fliplr(out)], axis=1) 
        
    return out 

# Cargue la imagen img4.png de la carpeta imágenes de esta práctica
img4 = io.imread("imagenes/img4.jpg")


# Se invoca la función recientemente implementada
out_img4 = calidoscopio_imagen(img4)


# Cargue la imagen img6.jpg de la carpeta imágenes de esta práctica
img6 = io.imread('imagenes/img6.jpg')


# Se invoca la función recientemente implementada
out_img6 = calidoscopio_imagen(img6)

# Muestre las imagenes originales y las imágenes resultantes
f, ax = plt.subplots(2, 2, figsize=(20, 10))

ax[0,0].imshow(img4, cmap="gray")
ax[0,0].set_title('Imagen Original', fontsize=18)
ax[0,0].axis('off')

ax[0,1].imshow(out_img4, cmap="gray")
ax[0,1].set_title('Imagen Calidoscopio', fontsize=18)
ax[0,1].axis('off')

ax[1,0].imshow(img6, cmap="gray")
ax[1,0].set_title('Imagen Original', fontsize=18)
ax[1,0].axis('off')

ax[1,1].imshow(out_img6, cmap="gray")
ax[1,1].set_title('Imagen Calidoscopio', fontsize=18)
ax[1,1].axis('off')
