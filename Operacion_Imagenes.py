# Siempre que usemos matplotlib en Jupyter es necesario poner esta línea antes de cualquier otra
%matplotlib inline

# Importamos las bibliotecas necesarias y les asigamos un alias
import skdemo
import numpy as np
from matplotlib import pyplot as plt
from skimage import data
from skimage import color
from skimage import exposure
from skimage import io


# Ejercicio 1. Operaciones Entre Múltiples Imágenes
# Las operaciones entre múltiples imágenes son comunes en la etapa de preprocesamiento. 
# Una aplicación frecuente de este tipo de operaciones se presenta en el proceso de extracción del background (o fondo) 
# de una imagen para segmentar los objetos de interés en la misma, por ejemplo, para extraer los objetos en movimiento 
# de un video.

# Siga los pasos a continuación para segmentar los objetos en movimiento en una vía rápida:

# 1. Creee un vector de ceros de 240x320x3x100 llamado imagenes
imagenes = np.zeros((240,320,3,100))

# 2. Almacene en dicho vector las primeras 100 imágenes del vídeo en la carpeta highway, saltando de dos en dos
#    Para realizar este punto revise como dar formato a enteros con la función format
#    Cree una lista con la url de las imagenes a cargar
lista = []
for i in range(0,100):
    lista.append("highway/in{:0>6d}.jpg".format((i*2+1)))

# 3. Lea las imagenes como una colección
ic = io.imread_collection(lista)

# 4. Concatene las imágenes en un arreglo de 100x240x320x3
imagenes = io.concatenate_images(ic)

# 5. Visualice 4 de las imágenes cargadas en un subplot de 4x4
f, axes = plt.subplots(2, 2, figsize=(20,10))
axes = axes.ravel()

for ax in axes:
    ax.axis('off')

(ax_1, ax_2, ax_3, ax_4) = axes
 
ax_1.imshow(imagenes[0,:,:,:])
ax_2.imshow(imagenes[25,:,:,:])
ax_3.imshow(imagenes[50,:,:,:])
ax_4.imshow(imagenes[75,:,:,:])

# 6. Estime el background de la escena, para ello promedie las imágenes leídas anteriormente
background = np.mean(imagenes, axis=0).astype('uint8')

# 7. Muestre el background calculado
plt.imshow(background)
plt.axis("off")

# 8. Lea la imagen de prueba (in001637.jpg)  en la variable test 
test = io.imread("highway/in001637.jpg")

# 9. Restar las imagenes de test y background, haciendoq ue la suma sea entera
out = (test.astype(int) - background.astype(int))

# 10. Sature los píxeles con valores <0 y >255
out[out < 0] = 0
out[out > 255] = 255

# 11. Cambie el tipo de la imagen a uint8
out = out.astype(np.uint8)

# 12. Muestre la imagen resultante y su histograma
skdemo.imshow_with_histogram(out)

# 13. Haga una expansión de la imagen en el rango 0, 180
out2 = exposure.rescale_intensity(out, in_range=(0, 180))

# 14. Umbralice cada canal por separado mantenga los píxeles >= 128
Ro = out2[:,:,0] >= 128;
Go = out2[:,:,1] >= 128;
Bo = out2[:,:,2] >= 128;

# 15. Genere una imagen de salida que corresponda al OR entre los canales
out3 = np.logical_or(Ro, Go)
out3 = np.logical_or(out3, Bo)

# 16. Muestre los objetos de interés en la imagen (out3)
plt.imshow(Bo, cmap="gray")
plt.axis("off")
