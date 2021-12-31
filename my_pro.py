import cv2
import numpy as np
from  pyzbar.pyzbar import decode

cam=cv2.VideoCapture(0)
while True:
    _,frame=cam.read()
    for barcode in decode(frame):
        bra_data=barcode.data.decode('utf-8')
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(0,0,255),5)
        pts2=barcode.rect
        cv2.putText(frame,bra_data,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    # frame=cv2.flip(frame,1)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)


