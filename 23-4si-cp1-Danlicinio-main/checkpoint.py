
import cv2
import os,sys, os.path
import numpy as np


def image_da_webcam(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    #definição dos valores minimo e max da mascara
    #laranja
    image_lower_hsv = np.array([0, 180, 160])  
    image_upper_hsv = np.array([40, 255, 255])

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
        if (M['m00'] != 0):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            cv2.line(contornos_img,(cx - size,cy),(cx + size,cy),color,5)
            cv2.line(contornos_img,(cx,cy - size),(cx, cy + size),color,5)

            font = cv2.FONT_HERSHEY_SIMPLEX
            text = cy , cx
            origem = (cx-80,cy-100)

            cv2.putText(contornos_img, str(text), origem, font,1,(200,50,0),2,cv2.LINE_AA)
    return contornos_img

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    
    img = image_da_webcam(frame)


    cv2.imshow("preview", img)

    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()