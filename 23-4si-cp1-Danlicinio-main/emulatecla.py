#!/usr/bin/python
# -*- coding: utf-8 -*-



import cv2
from cv2 import vconcat
from matplotlib import lines, pyplot as plt
import numpy as np
import math
import os
import os.path

def image_da_webcam(img):
    """
    ->>> !!!! FECHE A JANELA COM A TECLA ESC !!!! <<<<-
        deve receber a imagem da camera e retornar uma imagems filtrada.
    """

img = cv2.imread('circulo.PNG')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


#definição dos valores minimo e max da mascara
#ciano
image_lower_hsv = np.array([80, 165, 127])  
image_upper_hsv = np.array([90, 230, 230])

mask_hsv = cv2.inRange(img_hsv, image_lower_hsv, image_upper_hsv)

#magenta
image_lower_hsv2 = np.array([0, 165, 127]) 
image_upper_hsv2 = np.array([30, 255, 255])

mask_hsv2 = cv2.inRange(img_hsv, image_lower_hsv2, image_upper_hsv2)

#juntar as duas imagens
mask_juntar = cv2.bitwise_or(mask_hsv, mask_hsv2)

#encontrar contornos e calcular massa
mask_rgb = cv2.cvtColor(mask_juntar, cv2.COLOR_GRAY2RGB) 
contornos_img = mask_rgb.copy()
contornos, _ = cv2.findContours(mask_juntar, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

cv2.drawContours(contornos_img, contornos, -1, [255, 0, 0], 5)
size = 20
color = (128,128,0)

for contorno in contornos:
    M = cv2.moments(contorno)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv2.line(contornos_img,(cx - size,cy),(cx + size,cy),color,5)
    cv2.line(contornos_img,(cx,cy - size),(cx, cy + size),color,5)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = cy , cx
    origem = (cx-80,cy-100)

    cv2.putText(contornos_img, str(text), origem, font,1,(200,50,0),2,cv2.LINE_AA)
    

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.subplot(1, 2, 2)
plt.imshow(contornos_img, cmap="Greys_r", vmin=0, vmax=255)
plt.show()