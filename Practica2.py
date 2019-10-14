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

#Ejercicio 1. Eliminación del fondo en una Imagen
#Existe una gran variedad de problemas en Visión Artificial en los que es necesario eliminar el fondo de la imagen 
# con el fin de aislar los objetos de interés de la misma. Uno de esos problemas consiste en la extracción de las 
# venas en imágenes del nervio óptico. En la imagen siguiente, por ejemplo, se tiene una imagen del nervio óptico y 
# las venas tras extraer el fondo de la imagen. (OJO: las imágenes no corresponden pero pretenden ilustrar la idea de 
# lo que se debe hacer).

# Una forma para hacer esto consiste en estimar una imagen del fondo de la escena, es decir, una imagen sin las venas para luego restar esta imagen de la imagen original.

# Desarrolle una función que dada una imagen (en niveles de gris) retorne una imagen que represente el fondo de la escena, y una imagen sin el fondo calculado. La función debe recibir 3 parámetros: la imagen original, el tipo de filtro a usar para estimar el fondo y el tamaño del filtro. Dicha función debe:

# Estimar una imagen que represente el fondo de la escena. Esto se hace aplicando bien sea aplicando:

# Un filtro promedio
# Un filtro mediana
# Un filtro máximo con dirección vertical
# Un filtro máximo con dirección horizontal
# Una vez estimado el fondo debe tomar la imagen original y restar la imagen del fondo (o viceversa)

# La imagen resultante debe volver poner en el rango adecuado de valores de una imagen, según su tipo

# *NOTA: * tenga cuidado con los tipos de las imágenes al realizar estas operaciones!


# Desarrollo del Ejercicio 1

# img = Imagen de entrada
# filtro = Tipo de filtro a usar para la estimación del fondo
# n = número de vecinos considerados en cada dirección para aplicar el filtro
def img_without_bck(img, filtro=1, n=3):

    #Si la imagen es a color se convierte a niveles de gris
    if (len(img.shape)  > 2):
        img = color.rgb2gray(img)

    #Imagen del fondo estimado
    bck = np.zeros(img.shape)

    #Imagen sin el fondo
    out = np.zeros(img.shape)
        
    #AQUÍ: Empice su código
    
    #Convierte la imagen original a float    
    img = util.img_as_ubyte(img);
    
    #Aplica el filtro para estimar el fondo
    if (filtro == 1):
        bck = filters.rank.mean(img, np.ones((n,n)));
    elif (filtro == 2):
        bck = filters.rank.median(img, np.ones((n,n)));
    elif (filtro == 3):
        bck = filters.rank.maximum(img, np.ones((1,n)));
    elif (filtro == 4):
        bck = filters.rank.maximum(img, np.ones((n,1)));
    else:
        print("debe ingresar un filtro valido");
        return;
    
    #Convierte la imagen original y el fondo a float
    bck = util.img_as_float(bck);
    img = util.img_as_float(img);
    
    #Los valores que estén en negativos los setea como 0 y los que estén sobre 1 les pone 1
    out = np.clip((bck - img), 0, 1);
    
    #Convierte la imagen a blanco y negro
    out2 = np.zeros(out.shape);
    out2[out >= 0.05] = 1;
    
    #Mostramos el resultado
    skdemo.imshow_all(img, bck, out2, size=7, titles=["Original", "Fondo", "Bordes"] )
    
    return bck, out

img_without_bck(io.imread("imagenes/Retina_1.jpg"), 2, 10);
img_without_bck(io.imread("imagenes/Retina_2.jpg"), 2, 10);

# Discusión de los resultados obtenidos:
# ¿Cuál es el mejor filtro y de qué tamaño?
# El filtro promedio de tamaño 10
# ¿La forma del filtro influye en el resultado?, ¿Por qué?
# Si
# ¿El tamaño del filtro influye en el resultado?, ¿Por qué?
# Si, porque mientras mayor sea el filtro el resultado de los bordes será más preciso.

# Ejercicio 2. Realzando una imagen
# Como vimos antes, la base para realzar una imagen son los bordes que se puedan extraer de la misma. En este punto usted debe desarrollar una función que realce una imagen. Para ello:

# Primero debe suavizar la imagen usando un filtro mediana de 3x3
# Calcule la imagen de bordes horizontales usando la máscara de la segunda derivada. Para esto use la función scipy.signal.convolve2d
# Calcule la imagen de bordes verticales usando la máscara de la segunda derivada. Para esto use la función scipy.signal.convolve2d
# Genere una imagen de bordes que corresponda al máximo entre las dos imágenes anteriores
# Sume la última imagen obtenida a la imagen original para realzar los bordes
# La función debe mostrar (en un subplot) la imagen original, los bordes horizontales, los bordes verticales, 
# el máximo entre los bordes y la imagen realzada.
# *NOTA: tenga cuidado con los tipos de las imágenes al realizar estas operaciones!

# Desarrollo del Ejercicio 2

def img_enhance(img):
    #AQUÍ: Empice su código
    
    #Si la imagen es a color se convierte a niveles de gris
    if (len(img.shape)  > 2):
        img = color.rgb2gray(img)
        
    #Convierte la imagen original a float    
    img = util.img_as_float(img);
    
    #Aplicamos el filtro de la mediana con una mascara de 3*3
    img2 = filters.rank.median(img, np.ones((3,3), dtype=float));
    #Convertimos la imagen a float
    img2 = np.clip(util.img_as_float(img2), 0, 1);
    
    #Obtener los bordes horizontales    
    # Creamos la mascara kernel    
    k1 = np.array([[1, -2, 1]]);
    
    # Aplicamos el filtro para obtener los bordes horizontales
    img3 = scipy.signal.convolve2d(img2, k1, mode='same', boundary='fill', fillvalue=0);
    img3 = np.clip(img3, 0, 1);    
    
    #Obtener los bordes verticales    
    # Creamos la mascara kernel    
    k2 = np.array([[1],
                   [-2],
                   [1]]);
    
    # Aplicamos el filtro para obtener los bordes verticales
    img4 = scipy.signal.convolve2d(img2, k2, mode='same', boundary='fill', fillvalue=0);
    img4 = np.clip(img4, 0, 1);
    
    # Obtiene los pixel maximos entre las imágenes de bordes verticales y horizontales
    img5 = np.maximum(img3, img4);        
    
    # Suma los bordes a la imagen original
    img6 = np.clip(img + img5, 0, 1);
    
    #Mostramos el resultado
    titles = ["Original", "bordes horizontales", "bordes verticales", "Máximos entre bordes", "imagen resaltada"];
    skdemo.imshow_all(img, img3, img4, img5, img6, size=7, titles=titles);
    
# Pruebe la función usando las imágenes rice, retina_3 y taj_orig
import scipy.signal

img_enhance(io.imread("imagenes/rice.png"));
img_enhance(io.imread("imagenes/Retina_3.jpg"));
img_enhance(io.imread("imagenes/taj_orig.jpg"));