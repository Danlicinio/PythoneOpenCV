import cv2
import numpy as np
import os.path

vc = cv2.VideoCapture(0)
while True:
    ret, frame = vc.read()
    if ret == False:
        print("Sem frame")
        break
    else:
        cv2.imshow('Video', frame)
        
         if cv2.waitKey(1) & 0xFF == ord('q'):
            break
vc.release()
cv2.destroyAllWindows()