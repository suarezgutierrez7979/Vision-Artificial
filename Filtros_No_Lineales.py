#Filtros NO Lineales¶
# Los filtros no lineales por excelencia son 3: la mediana, el mínimo y el máximo. Este tipo de filtros, 
# también conocidos como filtros de orden estadístico, reemplazan el píxel central del kernel de convolución 
# por la mediana, el máximo o el mínimo valor entre los valores que cubre la ventana en la imagen original.

# Veamos como utilizar estos filtros en Skimage:

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

# Filtro Mediana¶
# Este es uno de los filtros más usados para suavizar una imagen dado que preserva los bordes de la misma mientras elimina el ruido.

# Al igual que con los filtros espaciales tradicionales, el filtro mediana centra el kernel de convolución en cada 
# pixel de la misma, reemplazando su valor por la mediana entre todos los valores que cubre el kernel. 
# Este filtro funciona muy bien para eliminar el ruido, especialmente el ruido de tipo impulsivo. 
# El siguiente ejemplo muestra cómo usar el filtro mediana en una imagen con ruido "sal y pimienta". 
# Además, la imagen se filtra usando un filtro gaussiano para fines de comparación.

# Cargamos la imagen y le agregamos ruido
img = skimage.img_as_ubyte(data.camera())
img_noisy = util.random_noise(img, "s&p")

# Mostramos las imágenes
skdemo.imshow_all(img, img_noisy, titles=["Imagen Original", "Imagen con Ruido S&P"])

# Kernel de convolución
k = morphology.square(3)

# Se aplica el filtro mediana
img_median = filters.rank.median(img_noisy, k)

# Se aplica el filtro gaussiano
img_gauss = filters.gaussian(img_noisy, sigma=1.0)

skdemo.imshow_all(img_median, img_gauss, titles=["Filtro Mediana", "Filtro Gaussiano"]);

#Visualizando los detalles
skdemo.imshow_all(img_median[100:200, 200:400], img_gauss[100:200, 200:400]);

# Filtro Máximo¶
# Este tipo de filtro reemplaza el píxel central del kernel con el píxel más claro (valor máximo de intensidad) 
# de entre los píxeles en el kernel.

# Aplicamos el filtro máximo
img_max = filters.rank.maximum(img_noisy, k)

# Visualizamos la matriz de la imagen
skdemo.imshow_all(img, img_noisy, img_max)

# Como se puede observar, el filtro máximo aclara la imagen. Sin embargo, este filtro 
# no suele ser una buena opción para eliminar el ruido sal ya que empeora dicho 
# ruido en la imagen.

# Veamos un ejemplo con otra imagen ...
# Leemos la imagen
img_manzana = io.imread("imagenes/CloseF.png")

# Aplicamos el filtro máximo a cada canal
R = filters.rank.maximum(img_manzana[:,:,0], k)
G = filters.rank.maximum(img_manzana[:,:,1], k)
B = filters.rank.maximum(img_manzana[:,:,2], k)

# Componemos la imagen RGB en la imagen de salida
img_manzana_max = color.gray2rgb(R)
img_manzana_max[:,:,1] = G
img_manzana_max[:,:,2] = B

# Visualizamos las imágenes
skdemo.imshow_all(img_manzana, img_manzana_max, titles=["Imagen Original", "Filtro Máximo"]);

# Filtro Mínimo¶
# Este tipo de filtro reemplaza el píxel central del kernel con el píxel más oscuro (valor mínimo de intensidad) 
# de entre los píxeles en el kernel.

# Aplicamos el filtro mínimo
img_min = filters.rank.minimum(img_noisy, k)

# Visualizamos la matriz de la imagen
skdemo.imshow_all(img, img_noisy, img_min)

# Contrario al filtro máximo, el filtro mínimo oscurece la imagen. También se debe notar que este tipo de 
# filtro no es bueno para eliminar el ruido tipo pimienta en una imagen, pues al tomar el valor mínimo del kernel,
# se agudiza el ruido.
# Veamos ahora la aplicación del filtro mínimo en la imagen de la manzana. Observe y compare las imágenes de resultado.
# Aplicamos el filtro máximo a cada canal
R = filters.rank.minimum(img_manzana[:,:,0], k)
G = filters.rank.minimum(img_manzana[:,:,1], k)
B = filters.rank.minimum(img_manzana[:,:,2], k)

# Creamos la imagen RGB a partir del canal R
img_manzana_min = color.gray2rgb(R)
img_manzana_min[:,:,1] = G
img_manzana_min[:,:,2] = B

# Visualizamos las imágenes
skdemo.imshow_all(img_manzana, img_manzana_max, img_manzana_min, titles=["Imagen Original", "Filtro Máximo", "Filtro Mínimo"]);