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

import skdemo                            # Paquete ESPECIAL ADJUNTO con algunas funciones extra de visualización

####################
from skimage import filters              # Paquete que contiene las máscaras y filtros de suavizado y realzado
from skimage import util                 # Paquete que contiene las funciones para cambiar el tipo de dato de las imágenes

from scipy import ndimage                # Usamos esta biblioteca para realizar la operación de convolución


# Con este nos aseguramos que las imagenes en niveles de gris, se vean como tal siempre.
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'none'

#Convolucion de Imagenes 
# creamos una imagen de tipo FLOTANTE
img = np.zeros((7, 7), dtype=float)
img[1:6, 1:6] = 0.5
img[2:5, 2:5] = 1

plt.imshow(img)

# Creamos el kernel de convolución
# Nota: si no recuerda esto, revise nuevamente la Práctica 0
k = np.full((3,3), 1/9)

# Visualizamos la matriz de la imagen. Note como se hace el print ...
print ("Imagen Original: ")
print (np.array_str(img, precision=2))

# Visualizamos la matriz del kernel. Note como se hace el print ...
print ("\nKernel de Convolución:")
print (np.array_str(k, precision=2))

# Aplicamos la convolución
# Note que la función de convolución está en el paquete ndimage de scipy
out = ndimage.convolve(img, k, mode='constant', cval=0.0)

# Visualizamos la matriz de la imagen resultante
print ("Imagen Resultado:")
print (np.array_str(out, precision=2))

# Visualizamos la imagen de salida
plt.imshow(out)

#Filtros de Suavizado

# Los filtros de suavizado son aquellos que permiten suavizar los cambios en la imagen por lo que suelen tener un efecto de 
# desenfoque en las imágenes.
# A este tipo de filtros también se les conoce como filtros paso bajo, esto debido a que dejan pasar las bajas frecuencias 
# de la imagen (que representan los cambios suaves) pero eliminan o atenúan las altas frecuencias, que son los cambios bruscos
#  y que normalmente representan el ruido y los bordes de la imagen.
# Skimage proporciona principalmente tres tipo de filtros de suavizado: El Filtro Promedio y 
# el Filtro Gaussiano que son filtros lineales y el Filtro Mediana que es un filtro de orden estadístico.

# Filtro de Suavizado Promedio¶
# En el ejemplo incial aplicamos a la imagen un filtro promedio de 3x3:

# Con base en los resultados que obtuvimos se pueden hacer dos observaciones importantes cuando se aplica 
# un filtro de suavizado promedio:

# La intensidad de los píxeles más brillantes disminuyó
# La intensidad de los píxeles oscuros, rodeados de píxeles más claros aumentó
# Veamos la aplicación del filtro promedio en Skimage:

# Cargamos una de las imágenes en niveles de gris
cat = color.rgb2gray(data.chelsea())

# Revisamos el tipo de la imagen
print ("Tipo de dato de la imagen Original: ", img.dtype)

# Como la imagen es floante debemos pasarla a uint8 o untin16
# El tipo de la imagen debe cambiar porque la función solo recibe imágenes enteras
cat = util.img_as_ubyte(cat)
print ("Tipo de dato de la imagen convertida: ", img.dtype)

# Aplicamos el filtro promedio de 5x5 usando skimage
avg = filters.rank.mean(cat, np.ones((5,5)))

# Mostramos las imágenes
skdemo.imshow_all(cat, avg, titles=["Imagen Original", "Imagen Promedio"])


# Filtro de Suavizado Gaussiano¶
# El filtro Gaussiano es el filtro clásico de suavizado y es muy similar al filtro promedio. Sin embargo, 
# el filtro Gaussiano no pondera de igual manera a todos los píxeles en el vecindario: los píxeles qué 
# están más cerca al píxel central tienen mayor peso que aquellos que están más alejados de este.

# Creamos una matriz de zeros y cambiamos el valor del píxel central
m = np.zeros((5,5))
m[2,2] = 1

# Usamos la función del paquete filters para generar la máscara
k_gauss = filters.gaussian(m, sigma=0.5)
print("Kernel con sigma = 0.5:\n", np.array_str(k_gauss, precision=3,  suppress_small=True))

# Variamos el tamaño de sigma
k_gauss = filters.gaussian(m, sigma=1)
print("\n\nKernel con sigma = 1:\n", np.array_str(k_gauss, precision=3, suppress_small=True))

# Creamos la imagen de prueba
img = np.zeros((7, 7), dtype=float)
img[2:5, 2:5] = 0.5

# Filtramos la imagen usando un sigma=0.5
out_1 = filters.gaussian(img, sigma=0.5)

# Filtramos la imagen usando un sigma=1.0
out_2 = filters.gaussian(img, sigma=1.0)

# Visualizamos las imágenes
skdemo.imshow_all(img, out_1, out_2, titles=["Original", "Filtro Gauss con Sigma=0.5", "Filtro Gauss con Sigma=1.0"])

# Aplicamos el filtro Gaussiano en la imagen del gato
gauss = filters.gaussian(cat, sigma=1.0)

# Mostramos las imágenes
skdemo.imshow_all(cat, avg, gauss, titles=["Original", "Filtro Promedio", "Filtro Promedio"])


#Probemos ahora en una imagen con ruido añadido:
# Cargamos la imagen astronauta
ast = color.rgb2gray(data.astronaut())

# Agregamos ruido normal
ast_noised = util.random_noise(ast, mode="speckle")

# Filtramos la imagen con ruido usando un filtro promedio de 5x5
ast_avg = filters.rank.mean(ast_noised, np.ones((5,5)))

# Filtramos la imagen con ruido usando un filtro gaussiano
ast_gauss = filters.gaussian(ast_noised, sigma=1.0)

# Mostramos las imágenes
skdemo.imshow_all(ast, ast_noised, titles=["Original", "Con Rudio Agregado"])
skdemo.imshow_all(ast_avg, ast_gauss, titles=["Filtro Promedio", "Filtro Gaussiano"])

#Hagamos una prueba más para comparar los resultados entre el filtro promedio y el filtro gaussiano:
# Cargamos la imagen del fotografo y hacemos un remuestreo a lo "bruto"
cam = data.camera()

sigma = 15
k = np.ones((3*sigma, 3*sigma))
fot_px_mean = filters.rank.mean(cam, k)
fot_px_gauss = filters.gaussian(cam, sigma)
titles = ['Filtro Promedio', 'Filtro Gaussiano']
skdemo.imshow_all(fot_px_mean, fot_px_gauss, titles=titles)

# Filtros de Realzado
# Los Filtros de Realzado (o filtros Paso Alto) se usan para resaltar los detalles “finos” de la imagen y/o 
# para recuperar cierto detalle perdido durante su captura. Es por esta razón que estos filtros están asociados, 
# con la detección de bordes.

# En este sentido, los filtros de realzado acentúan los bordes en la imagen, aunque también suelen resaltan 
# cualquier ruido o imperfección que haya en la misma.

# Máscara Unsharp
# La máscara unsharp es un filtro lineal que permite resaltar los bordes de la imagen. Para ello, 
# el filtro identifica los bordes a partir de una resta entre la imagen original y su versión suavizada. 
# A continuación, dichos bordes son intensificados y sumados a la imagen original.

# Al igual que otro tipo de filtros, si se va a aplicar a imágenes en color, la aplicación se debe hacer 
# a cada canal de manera independiente.
# Debe ter cuidado con la aplicación de los filtros basados en los bordes de las imágenes puesto que estos
# pueden generar valores de intensidad negativos. En este sentido se recomienda usar siempre imágenes de tipo real, 
# además que se debe usar la función clip de NumPy para reestablecer los niveles de gris de la imagen al rango [0,1], 
# una vez se realcen los bordes.
# Ahora sí, veamos la aplicación de este filtro en Skimage:

# Cargamos una de las imagenes de la práctica
eye = util.img_as_float(io.imread("imagenes/eye_vesels.png"))

# Aplicamos el filtro a cada canal por separado (la versión 1.5 tiene la funcion, la 1.4 NO!!!)
#R = filters.unsharp_mask(eye[:,:,0], radius=5, amount=2)
#G = filters.unsharp_mask(eye[:,:,1], radius=5, amount=2)
#B = filters.unsharp_mask(eye[:,:,2], radius=5, amount=2)

# Si tiene instalada la versión 1.4 el camino es más largo ...
radius = 2 # Radio del filtro gaussiano 
amount = 1 # Cantidad de veces que se suman los bordes a la imagen original

# Como la imagen es a color, el proceso debe hacerse en cada canal
b_R = filters.gaussian(eye[:,:,0], sigma=radius, mode='reflect')
R = eye[:,:,0] + (eye[:,:,0] - b_R) * amount

b_G = filters.gaussian(eye[:,:,1], sigma=radius, mode='reflect')
G = eye[:,:,1] + (eye[:,:,1] - b_G) * amount

b_B = filters.gaussian(eye[:,:,2], sigma=radius, mode='reflect')
B = eye[:,:,2] + (eye[:,:,2] - b_B) * amount

# La función np.clip corrige los valores de la imagen para que queden en el rango adecuado [0, 1]
eye_unsharp = np.zeros(eye.shape)
eye_unsharp[:,:,0] = np.clip(R, 0, 1)
eye_unsharp[:,:,1] = np.clip(G, 0, 1)
eye_unsharp[:,:,2] = np.clip(B, 0, 1)

# Recuerde que el borde es: original - suavizada
# Además, para visualizar los bordes sumamos el valor 0.5 (o 128 en imágenes uint8) a esos bordes
edges = np.zeros(eye.shape)
edges[:,:,0] = np.clip(eye[:,:,0] - b_R, 0, 1)+0.5
edges[:,:,1] = np.clip(eye[:,:,1] - b_G, 0, 1)+0.5
edges[:,:,2] = np.clip(eye[:,:,2] - b_B, 0, 1)+0.5

# Visualizamos las imágenes
skdemo.imshow_all(eye, edges, eye_unsharp, titles=["Original", "Bordes", "Imagen Realzada"])

# Filtro Laplaciano
# Como se mencionó, el Filtro Laplaciano es un filtro basado en segunda derivada. Es así que este filtro 
# busca los píxeles de la imagen en los que hay un mínimo o máximo relativo 
# (al principio o al final de un cambio tipo rampa o escalón).

# En skimage este tipo de filtro se puede aplicar usando la función filters.laplace o bien definiendo 
# la máscara y usando la función ndimage.convolve de scipy.

# Al igual que con la Máscara Unsharp, se debe tener cuidado de volver a llevar al rango [0,1] 
# los valores de intensidad para imágenes de tipo real y al rango [0, 255] para imágenes de tipo entero.
# Trabejemos ahora solo con un solo canal
eye_gray = color.rgb2gray(eye)

# Aplicamos el operador laplaciano usando la función de skimage
eye_lp1 = filters.laplace(eye_gray)
eye_1 = np.clip(eye_gray + eye_lp1, 0, 1)

# Este kernel es el mismo usado en la función filters.laplace
k1 = np.array([[0, -1, 0], 
               [-1, 4, -1], 
               [0, -1, 0]])

eye_lp2 = ndimage.convolve(eye_gray, k1)
eye_2 = np.clip(eye_gray + eye_lp2, 0, 1)

k2 = np.array([[-1, -1, -1], 
               [-1, 8, -1], 
               [-1, -1, -1]])

eye_lp3 = ndimage.convolve(eye_gray, k2)
eye_3 = np.clip(eye_gray + eye_lp3, 0, 1)

plt.imshow(eye_gray, cmap="gray")
skdemo.imshow_all(eye_lp1, eye_lp2, eye_lp3, titles=["Laplaciano skimage", "Laplaciano 4", "Laplacinao 8"])
skdemo.imshow_all(eye_1, eye_2, eye_3, titles=["Imagen Realzada skimage", "Imagen Realzada Lap 4", "Imagen Realzada Lap 8"])

#Note que si bien el Filtro Laplaciano mejora los bordes, al ser un operdaor de segunda derivada hace que este aumente 
#considerablemente el ruido en la imagen.
