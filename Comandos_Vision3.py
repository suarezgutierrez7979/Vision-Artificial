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

####################

import skdemo                            # Paquete ESPECIAL ADJUNTO con algunas funciones extra de visualización

# Cargamos la imagen
img = data.camera()

# Calcula y muestra el histograma de la imagen
skdemo.imshow_with_histogram(img)

# Expansión del Histograma
# Como vimos en clase, mejorar el contraste de una imagen nos permite identificar más fácilmente los objetos de interés en la imagen, además que facilita el proceso de su segmentación y la extracción de sus características, esto bien sea a ojo o utilizando diferentes tipos de algoritmos.

# Eche un vistazo a la imagen del fotógrafo y a su histograma:

# Observe detenidamente el histograma: dado que la imagen es de tipo uint8, los valores de niveles de intensidad van de 0 a 255.
# Advierta que hay algunos pocos píxeles hacia el valor 255 y otros pocos por debajo del 10. Esto nos indica que la imagen no 
# tiene una distribución adecuada de los píxeles cercanos al blanco.
# En este caso, podemos aplicar una Expansión del Histograma:



# Los puntos que se están moviendo son m=10 y M=180, de acuerdo a la ecuación presentada en las diapositivas
img_contraste = exposure.rescale_intensity(img, in_range=(10, 180))

# Mostramos el histograma usando la biblioteca skdemo
skdemo.imshow_with_histogram(img_contraste);


# En este caso apliquemos la expansión a la imagen 3 de la práctica
img3 = io.imread("imagenes/img3.jpg")

# Visualizamos la imagen y su histograma
skdemo.imshow_with_histogram(img3);

# En el resultado vemos que los histogramas están concentrados en valores por debajo al nivel de gris 100, que es un nivel 
# de gris oscuro, lo que hace que la imagen esté oscura. Apliquemos una expansión al histograma con valores de salida 
# de los niveles de gris entre el 20 y el 220:


# Los puntos que se están moviendo son m=0 y M=180, de acuerdo a la ecuación presentada en las diapositivas
img3_contraste = exposure.rescale_intensity(img3, in_range=(0, 180), out_range=(20,220))

​
# Mostramos el histograma usando la biblioteca skdemo
skdemo.imshow_with_histogram(img3_contraste);

#Note que el contraste de la imagen mejoró, pero no lo suficiente. Tratemos ahora haciendo una #expansión completa del histograma, es decir, con un rango de salida del 0 al 255 (el cual no se #especifica en la transformación).
# Los puntos que se están moviendo son m=0 y M=180, de acuerdo a la ecuación presentada en las diapositivas
img3_contraste = exposure.rescale_intensity(img3, in_range=(0, 180))

# Mostramos el histograma usando la biblioteca skdemo
skdemo.imshow_with_histogram(img3_contraste);

# Los puntos que se están moviendo son m=0 y M=180, de acuerdo a la ecuación presentada en las diapositivas
img3_contraste = exposure.rescale_intensity(img3, in_range=(0, 180))

​
# Mostramos el histograma usando la biblioteca skdemo
skdemo.imshow_with_histogram(img3_contraste);

# Ecualización del Histograma
# Si bien, la expansión del histograma suele funcionar, hay funciones un poco más "inteligentes" que logran mejores resultados. 
# Una de ellas es la ecualización del histograma la cual busca generar una imagen cuyo histograma tenga una distribución 
# uniforme entre los valores de intensidad.

#Empecemos entonces viendo la función de distribución acumulada (CDF) de las intensidades de la imagen del fotógrafo:

ax_image, ax_hist = skdemo.imshow_with_histogram(img)
skdemo.plot_cdf(img, ax=ax_hist.twinx())

ax_image, ax_hist = skdemo.imshow_with_histogram(img)

skdemo.plot_cdf(img, ax=ax_hist.twinx())

# Se ecualiza la imagen
img_ecualizada = exposure.equalize_hist(img)


# OJO Use esta instrucción para cambiar el tamaño de visualización de las imágenes de aquí en adelante!
plt.rcParams['figure.figsize'] = [8, 6]

# Se calcula y muestra el histograma y la CDF de la imagen ecualizada
ax_image, ax_hist = skdemo.imshow_with_histogram(img_ecualizada)
skdemo.plot_cdf(img_ecualizada, ax=ax_hist.twinx())

# Ecualización Adaptativa del Histograma
# Un problema de la ecualización del histograma es que esta tiende generar imágenes cuyo contraste es artificialmente alto. 
# No obstante, la ecualización se puede mejorar solamente si se aplica localmente a ciertas partes de la imagen, en lugar 
# de aplicarla a la imagen completa. Note que, en el ejemplo anterior, el contraste en la capa del fotógrafo es mucho mejor, 
# pero el contraste en la hierba se reduce.

#La ecualización adaptativa del histograma con limitaciones de contraste (CLAHE) aborda estos problemas. 
# Los detalles de implementación no se presentan, pero ver el resultado es muy útil:

img_ecualizada = exposure.equalize_adapthist(img)

ax_image, ax_hist = skdemo.imshow_with_histogram(img_ecualizada)
skdemo.plot_cdf(img_ecualizada, ax=ax_hist.twinx())