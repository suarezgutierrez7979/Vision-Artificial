# Espacios de Color¶
# Aunque el espacio de color RGB es bastante fácil de entender, cuando este se desea usar para detectar un color específico 
# (que no sea rojo, verde o azul) puede ser doloroso.

# En las tareas específicas de visión artificial en las que el color juega un papel importante, 
# se suelen usar otros espacios de color en los que se usa un solo componente para la intensidad (luminancia o luminosidad) 
# de los píxeles y dos componentes adicionales para representar el color, como por ejemplo en los canales tono y saturación 
# de los espacios [HSL y HSV] (http://en.wikipedia.org/wiki/HSL_and_HSV)).

# Skimage provee diferentes funciones para convertir una imagen en RGB a otros espacios de color. 
# Estas funciones se encuentran en el paquete color de skimage.


# Siempre que usemos matplotlib en Jupyter es necesario poner esta línea antes de cualquier otra
%matplotlib inline

# Importamos las bibliotecas necesarias y les asigamos un alias
import skimage                           # Biblioteca para la manipulación de imágenes
import numpy as np                       # Biblioteca para la manipulación de matrices

# Importamos algunos paquetes específicos
from matplotlib import pyplot as plt     # Biblioteca para crear graficas y mostrar las imágenes en pantalla

from skimage import data                 # Paquete con imágenes de prueba
from skimage import io                   # Paquete para lectura/escritura de imágenes
from skimage import color                # Paquete con las operaciones de transformaciones entre espacios de color
from skimage import exposure             # Paquete con las funciones para calcular y alterar el histograma
from skimage import filters              # Paquete que contiene las máscaras y filtros de suavizado y realzado
from skimage import util                 # Paquete que contiene las funciones para cambiar el tipo de dato de las imágenes

from scipy import ndimage                # Usamos esta biblioteca para realizar la operación de convolución

import skdemo                            # Paquete ESPECIAL ADJUNTO con algunas funciones extra de visualización

##################

from skimage import morphology           # Para crear el kernel de convolución en los filtros no lienales

# Con este nos aseguramos que las imagenes en niveles de gris, se vean como tal siempre.
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'none'

# Leemos una de las imágenes de prueba de la practica
color_image = io.imread('imagenes/balloon.jpg')

# Pasamos la imagen al espacio de color Lab: L=luminancia, a y b definen el color real o tono
lab_image = color.rgb2lab(color_image)
lab_image.shape

#Observe que al cambiar el espacio de color, las dimensiones de la imagen no cambian en absoluto. 
# Sin embargo, visualicemos la imagen ...
skdemo.imshow_all(color_image, lab_image, titles=["Imagen Original", "Imagen Lab"])

# La función imshow visualiza una imagen en RGB, sin embargo, las matrices de la imagen en el espacio Lab no 
# se parecen en nada a las matrices de una imagen RGB.

# Dicho esto, hay un cierto parecido con la imagen en RBG. Observe, la información de cada canal:
skdemo.imshow_all(lab_image[..., 0], lab_image[..., 1], lab_image[..., 2],
                 titles=['L', 'a', 'b'])
                
# Parte de la gama de colores RGB en el espacio Lab se pueden visualizar a continuación, para valores específicos de luminancia.
# Note que la información de color es más uniforme en el espacio Lab que en el espacio RGB. Es más, estos se aproximan más a 
# la forma como el ojo humano percibe los colores.         

# En Skimage las funciones para los espacios de color son las siguientes:

# rgb2yiq: Convierte de RGB a YIQ
# rgb2yuv: Convierte de RGB a YUV
# rgb2hsv: Convierte de RGB a HSV
# rgb2xyz: Convierte de RGB a XYZ de CIE-1931
# rgb2lab: Convierte de RGB a Lab* de CIE-1976
# rgb2ycbcr: Convierte de RGB al espacio YCbCr       