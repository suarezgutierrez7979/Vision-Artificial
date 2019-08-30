%matplotlib inline

#Importamos las bibliotecas necesarias y les asignamos el alias 
import skimage
import numpy as np

from matplotlib import pyplot as plt
from skimage import data
from skimage import io

from skimage import color
from skimage import exposure
from matplotlib import colors as cl

#Lo primero que haremos será construir el histograma de una imagen en niveles de gris. Para ello debemos:

# 1.Cargamos la imagen
# 2.Calculamos la distribución de los niveles de intensidad (el histograma)
# 3.Mostramos el histograma junto con su imagen

#cargamos la imagen 
img= data.camera()

# Calculamos la distribucion de los niveles de intensidad en el histograma 
hist, bins = exposure.histogram(img)

#Mostramos la imagen junto con su histograma 

f, (ax0, ax1) = plt.subplots (1, 2, figsize=(15,5))

#Se muestra la primera imagen en el primer subplot
ax0.imshow(img, cmap='gray')
ax0.set_title ('Imagen Original', fontsize=16)
ax0.axis('off')

#Se muestra la imagen en el segundo subplot
ax1.set_xlabel('Nivel de gris')
ax1.set_ylabel('Cantidad de pixeles')
ax1.set_title('Histograma de la Imagen', fontsize=16)
ax1.fill_between(bins, hist, alpha=0.3, color='black' )

#El histograma de una imagen de color
#Ahora, veamos el histograma de una imagen a color. En este caso el histograma no se puede visualizar directamente, sino que debemos descomponer la imagen en sus canales y visualizar los tres histogramas en un sólo gráfico. Para este caso:

# 1.Cargamos la imagen a color
# 2.Calculamos la distribución de los niveles de intensidad para cada canal de la imagen
# 3.Mostramos la imagen y su histograma compuesto

# Cargamos la imagen a color de las imagenes preinstalas en la biblioteca skimage de python
img = data.chelsea()

# Calculamos los niveles de intensidad de cada canal RGB 
hist_R, bins_R = exposure.histogram (img [:,:,0])
hist_G, bins_G = exposure.histogram (img [:,:,1])
hist_B, bins_B = exposure.histogram (img [:,:,2])

#Mostramos la imagen junto con sus subplots
f, (ax0, ax1) = plt.subplots (1, 2, figsize=(15,5))

#Mostramos la imagen en el primer Subplot
ax0.imshow(img)
ax0.set_title('Imagen Original', fontsize=16)
ax0.axis('off')

#Mostramos la imagen en el segundo subplot
ax1.set_xlabel('Nivel de gris')
ax1.set_ylabel('Cantidad de pixeles')
ax1.set_title('Histograma de la imagen', fontsize=16)

ax1.fill_between(bins_R, hist_R, alpha=0.3, color='r')
ax1.fill_between(bins_G, hist_G, alpha=0.3, color='g')
ax1.fill_between(bins_B, hist_B, alpha=0.3, color='b')

#Aumento de brillo de una imagen a color 
img = io.imread("imagenes/img3.jpg")
out = img + 100

plt.imshow(out)
hist_R, bins_R = exposure.histogram(out[:,:,0])
hist_G, bins_G = exposure.histogram(out[:,:,1])
hist_B, bins_B = exposure.histogram(out[:,:,2])

# Mostramos el valor máximo de la imagen, solo para efectos de análisis
print("Valor máximo de intensidad en la imagen original: ",img.max())

img_c = skimage.img_as_float64(img)
print("Valor del máximo despues de la converion a entero: ",img_c.max())

# Aumentamos el brillo de la imagen, sumando un valor entre 0 y 1
img_c2 = img_c + 0.4

# Observe que los valroes de salida están por fuera del rango [0,1], por el aumento de brillo
print("Valor del máximo despues del aumento de brillo: ",img_c2.max())

# Para devolver la imagen al rango [0,1] usamos la función clip de NumPy
img_c2 = np.clip(img_c2, 0, 1);

# Mostramos el valor máximo de la imagen de salida, solo para efectos de análisis
print("Valor del máximo despues del aumento de brillo: ",img_c2.max())

plt.imshow(img_c2)
hist_R, bins_R = exposure.histogram(img_c2[:,:,0])
hist_G, bins_G = exposure.histogram(img_c2[:,:,1])
hist_B, bins_B = exposure.histogram(img_c2[:,:,2])


#Disminucion del brillo
#Leemos una de las imágenes de prueba, en este caso img5.png
img = io.imread("imagenes/img5.png")

# Cambiamos la representación de la imagen a real:
img = skimage.img_as_float64(img)

# Aplicamos la operación de disminución del brillo imagen
img_2 = img - 0.2

# Devolvemos la imagen al rango [0,1] usamos la función clip de NumPy
img_2 = np.clip(img_2, 0, 1)

plt.imshow(img_2)
hist_R, bins_R = exposure.histogram(img_2[:,:,0])
hist_G, bins_G = exposure.histogram(img_2[:,:,1])
hist_B, bins_B = exposure.histogram(img_2[:,:,2])

#Estiramientos de niveles de gris Multiplicacion
#Leemos una de las imágenes de prueba, en este caso tint2.jpg
img = io.imread("imagenes/tint2.jpg")

# Cambiamos la representación de la imagen a real:
img = skimage.img_as_float32(img)

# Aplicamos la operación de "estiramiento"
img_2 = img * 2

# Devolvemos la imagen al rango [0,1] usamos la función clip de NumPy
img_2 = np.clip(img_2, 0, 1)

plt.imshow(img_2)
hist_R, bins_R = exposure.histogram(img_2[:,:,0])
hist_G, bins_G = exposure.histogram(img_2[:,:,1])
hist_B, bins_B = exposure.histogram(img_2[:,:,2])

#Negativo de Una imagen
# Leemos una de las imágenes de prueba asegurandonos que su tipo sea real
img = skimage.img_as_float32(io.imread("imagenes/img1.jpg"))

# Obtenemos la versión en escala de grises de la imagen
img_g = color.rgb2gray(img)

# Calulamos el negativo de ambas imágenes
img_neg = 1 - img
img_g_neg = 1 - img_g

# Mostramos las imágenes y sus negativos
f, ax = plt.subplots(2, 2, figsize=(20, 10))

ax[0,0].imshow(img_g, cmap="gray", norm=cl.Normalize(vmin=0.0, vmax=1.0))
ax[0,0].set_title('Imagen en gris', fontsize=18)
ax[0,0].axis('off')

ax[0,1].imshow(img_g_neg, cmap="gray", norm=cl.Normalize(vmin=0.0, vmax=1.0))
ax[0,1].set_title('Negativo en gris', fontsize=18)
ax[0,1].axis('off')

# Se muestra en el segundo subplot la imagen 1, se le asigna un título y se pone el nombre al eje X
ax[1,0].imshow(img)
ax[1,0].set_title('Imagen a Color', fontsize=18)
ax[1,0].axis('off')

ax[1,1].imshow(img_neg)
ax[1,1].set_title('Negativo a Color', fontsize=18)
ax[1,1].axis('off')



