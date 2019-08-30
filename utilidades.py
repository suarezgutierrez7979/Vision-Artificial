# Importamos las bibliotecas necesarias y les asigamos un alias
import skimage                           # Biblioteca para la manipulación de imágenes
import numpy as np                       # Biblioteca para la manipulación de matrices

# Importamos algunos paquetes específicos
from matplotlib import pyplot as plt     # Biblioteca para crear graficas y mostrar las imágenes en pantalla
from skimage import data                 # Paquete con imágenes de prueba
from skimage import io                   # Paquete para lectura/escritura de imágenes

from skimage import color
from skimage import exposure

import matplotlib.colors as colors


def show_img_and_hist(img):

    d = img.shape
    plt.figure()
    
    if len(d) <= 2:
        # Calculamos la distribución de los niveles de intensidad (el histograma)
        hist, bins = exposure.histogram(img)
        
        # Mostramos la imagen junto con su histograma
        f, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 5))
        
        # Se muestra la imagen en el primer subplot
        if (img.dtype == "uint8"):
            ax0.imshow(img, cmap='gray', norm=colors.Normalize(vmin=0, vmax=255))
        else:
            ax0.imshow(img, cmap='gray', norm=colors.Normalize(vmin=0, vmax=1))
            
        ax0.set_title('Imagen Original', fontsize=16)
        ax0.axis('off')
        
        # Se muestra el histograma en el segundo subplot
        ax1.set_xlabel('Nivel de Gris');
        ax1.set_ylabel('Cantidad de Pixeles');
        ax1.set_title('Histograma de la Imagen', fontsize=16)
        ax1.fill_between(bins, hist, alpha=0.3, color='black');
        l, r = ax1.set_xlim()
        
        m = img.min()
        M = img.max()
        
        #Para que el gráfico incie en 0 y termine en 1 o 255
        if (m >= 0):
            if (M > 1):
                l = -10
            else:
                l = -0.025
        
        if (M >= 0 and M <= 1):
            r = 1.025
        elif(M > 1 and M <= 255):
            r = 265

        ax1.set_xlim(l, r)
        #ax1.set_ylim(bottom=0)

        
    else:
        # Calculamos la distribución de los niveles de intensidad de cada canal
        hist_R, bins_R = exposure.histogram(img[:,:,0])
        hist_G, bins_G = exposure.histogram(img[:,:,1])
        hist_B, bins_B = exposure.histogram(img[:,:,2])
        
        # Mostramos la imagen junto con su histograma
        f, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 5))
        
        # Se muestra la imagen en el primer subplot
        ax0.imshow(img)
        ax0.set_title('Imagen Original', fontsize=16)
        ax0.axis('off')        
        
        
        # Se muestra el histograma en el segundo subplot
        ax1.set_xlabel('Nivel de Gris');
        ax1.set_ylabel('Cantidad de Pixeles');
        ax1.set_title('Histograma de la Imagen', fontsize=16)
        ax1.fill_between(bins_R, hist_R, alpha=0.3, color='r');
        ax1.fill_between(bins_G, hist_G, alpha=0.3, color='g');
        ax1.fill_between(bins_B, hist_B, alpha=0.3, color='b');
        l, r = ax1.set_xlim()
        
        m = img.min()
        M = img.max()
        
        #Para que el gráfico incie en 0 y termine en 1 o 255
        if (m >= 0):
            if (M > 1):
                l = -10
            else:
                l = -0.025
        
        if (M >= 0 and M <= 1):
            r = 1.025
        elif(M > 1 and M <= 255):
            r = 265

        ax1.set_xlim(l, r)
        #ax1.set_ylim(bottom=0)
