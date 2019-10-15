# Métodos de Segmentación¶
# En Visión Artificial la segmentación consiste en el proceso de dividir una imagen en partes o 
# grupos de píxeles que representan los diferentes objetos en la escena. En este sentido, la segmentación 
# busca simplificar la representación de la imagen para facilitar su análisis.

# En general, los algoritmos de segmentación o bien buscan las discontinuidades en la 
# imagen (representadas por puntos, líneas o bordes) 
# o agrupan los píxeles que tienen cierta similitud.

# Veamos como usar diferentes métodos de segmentacióna en Skimage.

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
from skimage import transform            # Esta biblioteca es la que contiene la implementación de Hough
from skimage import measure              # Esta biblioteca contiene el método de etiquetado de regiones
from skimage import feature              # Esta biblioteca es la que contiene la implementación del canny

# Con este nos aseguramos que las imagenes en niveles de gris, se vean como tal siempre.
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'none'

#Segmentación por Umbral Simple¶
#Este es el tipo de segmentación más simple y consiste en utilizar el histograma para determinar 
#el nivel de intensidad que permite separar a los objetos del fondo de la imagen.

# Cargamos la imagen de prueba
img_1 = io.imread('imagenes/rice.png')

img_1 = color.rgb2gray(img_1)
      
# Visualizamos la imagen de prueba y su histograma
skdemo.imshow_with_histogram(img_1)

img_1.shape

# Al analizar el histograma se puede observar que los objetos de interés, cuyo color predominante es muy claro, 
# tienen valores por encima del valor 125. Ese valor es el que se utilza como umbral.

# En Python, cuando se usa NumPy, el proceso de umbralización es muy simple:

# La umbralización consiste en simplmente comparar los píxeles de la imagen con el valor definido
img_BW = img_1 >= 125

plt.imshow(img_BW)

# Note que a pesar de que los objetos son más claros que el fondo de la imagen, este método no funciona muy bien con la imagen 
# de los arroces. Esto sucede porque la iluminación en la imagen es no homogenea. Cuando esto sucede al aumentar el valor del
# umbral podemos perder objetos. Por el contrario, si disminuímos el umbral aparecerán todos los objetos pero
# también aparecerán objetos no deseados del fondo (ruido).

# Cargamos la imagen de prueba
img_2 = data.coins()
      
# Visualizamos la imagen de prueba y su histograma
skdemo.imshow_with_histogram(img_2)

# La umbralización consiste en simplmente comparar los píxeles de la imagen con el valor definido
img_BW = img_2 >= 128

plt.figure()
plt.imshow(img_BW)

# Apesar de que las monedas parecieran ser más claras que el fondo, el histograma nos muestra que estás no 
# tienen un nivel de intensidad que nos permitan separarlas fácilmente del fondo.
# En este caso el uso de un método de umbralización simple no es adecuado.

# Segmentación por Umbral Adaptativo¶
# Los métodos de umbralización adaptativos calculan de manera automática el umbral de acuerdo a la información 
# contenida en la imagen. En consecuencia, cuando se tienen ambientes con condiciones de iluminación no adecuadas 
# el umbral adaptativo obtiene mejores resultados que un método de umbralización simple. Existen diferentes métodos 
# de umbralización de este tipo, entre ellos:

# Método Adaptativo Local
# método ISODATA
# Método Otsu
# Método de Yen
# Método de Li (basado en entreopía)
# Veamos como usar los tres primeros y veamos los resultados en ambas imágenes:

# Método Adaptativo

# Revise la documentación a fin de que conozca los parámetros de la función
t1 = filters.threshold_local(img_1, 15, 'mean')
t2 = filters.threshold_local(img_2, 81, 'gaussian')

img_BW_1 = img_1 > t1
img_BW_2 = img_2 > t2

skdemo.imshow_all(img_BW_1, img_BW_2, titles=["Arroz umbral Adaptativo - Mean", "Coins umbral Adaptativo - Mean"])

# Método ISODATA

# Revise la documentación a fin de que conozca los parámetros de la función
t1 = filters.threshold_isodata(img_1)
t2 = filters.threshold_isodata(img_2);

img_BW_1 = img_1 > t1;
img_BW_2 = img_2 > t2;

skdemo.imshow_all(img_BW_1, img_BW_2, titles=["Arroz umbral isodata", "Coins umbral isodata"])

# Método yen

# Revise la documentación a fin de que conozca los parámetros de la función
t1 = filters.threshold_yen(img_1)
t2 = filters.threshold_yen(img_2)

img_BW_1 = img_1 > t1;
img_BW_2 = img_2 > t2;

skdemo.imshow_all(img_BW_1, img_BW_2, titles=["Arroz umbral Yen", "Coins umbral Yen"])

# Para efectos prácticos skiimage tiene una función que nos permite comparar los resultados de diferentes 
# métodos de umbralización: isodata,li, mean, minimum, otsu, triangle, yen

fig, ax = filters.try_all_threshold(img_1, figsize=(20, 20), verbose=False)

# Métodos de Extracción de Bordes¶
# Como se explicó en la clase, estos métodos usan máscaras de convolución para obtener los bordes horizontales y 
# verticales de una imagen, siendo las máscaras más usadas: Sobel, Prewitt y Roberts.

# Veamos como usarlas:

# Filtro Sobel
gradiente = filters.sobel(img_1)
skdemo.imshow_all(img_1, gradiente)


# Note que esta función integra tanto los bordes verticales como horizontales (calculando el gradiente), 
# no obstante el resultado es una imagen en escala de grises que, específicamente, nos indica la probabilidad 
# de que un píxel esté en el borde de un objeto. No obstante, para obtener los bordes de los objetos (imagen binaria) 
# debemos umbralizar el gradiente. Por ejemplo:

# Obtenga los bordes con un gradiente maypr a 0.1
img_bordes = gradiente > 0.1

skdemo.imshow_all(img_1, img_bordes)

# Observe que este enfoque no es muy bueno ya que a pesar de que se obtienen 
# los bordes de los objetos estos pueden contener ruido y además pueden ser gruesosm, 
# cuando estos deben ser delgados y conectados.

# Probemos las otras máscaras con la imagen de las monedas.

# Filtro Sobel
g_sobel = filters.sobel(img_2)
g_scharr = filters.scharr(img_2)
g_prewitt = filters.prewitt(img_2)
g_roberts = filters.roberts(img_2)

skdemo.imshow_all(g_sobel > 0.1, g_scharr > 0.1, titles=["Sobel", "Scharr"])
skdemo.imshow_all(g_prewitt > 0.1, g_roberts > 0.1, titles=["Prewitt", "Roberts"])

# Detector de Bordes Canny¶
# Canny es un detector de bordes que utiliza un filtro basado en la derivada de una gaussiana para calcular 
# la intensidad de los gradientes. Es decir, se empeiza aplicando un filtro gaussiano que reduce el efecto del 
# ruido presente en la imagen. Luego, se encuentran los posibles bordes en la imagen usando un filtro sobel, 
# después los bordes potenciales se reducen a curvas de 1 píxel, eliminando aquellos píxeles que no tienen un 
# máximo en la magnitud del gradiente (resultado del filtro sobel). Finalmente, los píxeles del borde 
# se mantienen o se eliminan utilizando la histéresis.

# En Skimage, Canny tiene tres parámetros ajustables: el desviación estándar del filtro gaussiano 
# (cuanto más ruidosa es la imagen, mayor debe ser este parámetro), y el umbral minimo y máximo para la histéresis.

# Veamos como usar el detector de bordes Canny:
# Cargamos la imagen en escala de grises
img_3 = skimage.img_as_float(io.imread("imagenes/bicho.jpg"))
img_3 = color.rgb2gray(img_3)

# Aplicamos el detector de bordes Canny
# Revise la documentación para tener más información sobre los parámetros
img_3_bordes = feature.canny(img_3, sigma=1, low_threshold=0.2, high_threshold=0.5)

skdemo.imshow_all(img_3, img_3_bordes, titles=["Origial", "Bordes Canny"], size=8)

# Transformada de Hough¶
# Las transformadas de Hough son una serie de algoritmos para detectar ciertos tipos de figuras 
# geométricas en una imagen. Al igual que con los detectores de bordes, las transformadas de Hough 
# producen una imagen binaria que contiene el tipo de 
# figura geométrica particular que se busca en la imagen

#Transformada de Hought para líneas¶
# Este tipo de transformada debe partir de una imagen con las líneas candidatas

#Aplicamos la transformada de Hough para líneas sobre los bordes de la imagen 3
lines = transform.probabilistic_hough_line(img_3_bordes, threshold=10, line_length=30, line_gap=1)

fig, axes = plt.subplots(1, 2, figsize=(20,5))
ax = axes.ravel()

ax[0].imshow(img_3_bordes)
ax[1].imshow(img_3)

for line in lines:
    p0, p1 = line
    ax[1].plot((p0[0], p1[0]), (p0[1], p1[1]))
ax[1].set_title('Líneas con Transformda de Hough')

# Transformada de Hough para Círculos¶
# La transformada Hough en su forma más simple es un método para detectar líneas rectas, p
# ero también se puede usar para detectar círculos o elipses. Este método es robusto contra el ruido 
# o los puntos que faltan en el borde los círculos.
from skimage import draw

# En este caso usamos la imagen de las monedas
img_2_bordes = feature.canny(img_2, sigma=3, low_threshold=10, high_threshold=50)

# Detecte círculos de diferentes radios radios
hough_radii = np.arange(10, 40, 2)
hough_res = transform.hough_circle(img_2_bordes, hough_radii)

# Seleccione the 24 círculos más prominentes
accums, cx, cy, radii = transform.hough_circle_peaks(hough_res, hough_radii, total_num_peaks=40)

# Se pintan los círculos en la imagen
image = color.gray2rgb(img_2)
for center_y, center_x, radius in zip(cy, cx, radii):
    circy, circx = draw.circle_perimeter(center_y, center_x, radius)
    image[circy, circx] = (220, 20, 20)

skdemo.imshow_all(img_2_bordes, image, size=8)

# Métodos de Segmentación basados en Regiones
# Una región consiste en una parte de la imagen que satisface un cierto criterio de uniformidad. Así, l
# a segmentación por regiones considera que cada región se forma a partir de píxeles considerados semillas y 
# evoluciona, mediante un algoritmo recursivo, incorporando aquellos píxeles vecinos que satisfacen una condición 
# establecida. Comúnmente, los criterios utilizados se refieren a propiedades de proximidad y homogeneidad. 
# El proceso de segmentación finaliza cuando no se encuentran más píxeles que cumplan la condición especificada.

# Como vimos en clase, existen diferentes métodos de segmentación basada en regiones, a continuación, 
# vamos a usar algunos de ellos usando Skimage.


# Segmentación por Watershed
# El nombre de watershed proviene de una analogía con la hidrología. El uso de este método de segmentación consiste en "inundar" 
# una imagen para determinar los puntos en los que se unen las cuencas, las cuales se determinan a partir de ciertos marcadores. 
# Las líneas que separan las cuencas hidrográficas corresponden a la segmentación de la imagen.

# En este sentido, el mapa de elevación incial es fundamental para una buena segmentación. Por ejemplo, para el problema de 
# las monedas, la amplitud del gradiente proporciona un buen mapa de elevación inicial.

# Usamos el operador Sobel para calcular la amplitud del gradiente:

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Volvemos a calcular el gradiente de la imagen usando el operador sobel
img_2_bordes = filters.sobel(img_2)

# Visualizamos el mapa de elevacion, es decir el gradiente como una imagen 3D
xx, yy = np.mgrid[0:img_2_bordes.shape[0], 0:img_2_bordes.shape[1]]
fig = plt.figure(figsize=(15,10))
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, img_2_bordes, cmap="jet")
ax.view_init(70, 10)
ax.set_title("Mapa de Elevación")
plt.show()

# Creamos los marcadores que serán usados para inundar el mapa de elevación
markers = np.zeros_like(img_2)
markers[img_2 < 30] = 1
markers[img_2 > 150] = 2

# Aplicamos el método de segmentación
segmentation = morphology.watershed(img_2_bordes, markers)

#Etiquetamos las regiones y las mostramos
#etiqeutas = measure.label(segmentation)
#plt.imshow(etiqeutas, cmap="jet")
plt.imshow(segmentation)
