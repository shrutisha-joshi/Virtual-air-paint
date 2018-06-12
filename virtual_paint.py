#virtual air painting

import cv2
import numpy as np
res=0
paint=0
erase=0
cap = cv2.VideoCapture(0)
_, fr = cap.read()
mask_black = np.zeros_like(fr, np.uint8)
mask1 = np.zeros_like(fr, np.uint8)
mask1[:] = [101,50,50]
final=0

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    j=0
    lower_limit = np.array([101,50,50])
    upper_limit = np.array([150,255,255])
    mask = cv2.inRange(hsv, lower_limit, upper_limit)
    maska = cv2.inRange(hsv,lower_limit, upper_limit)
    maska = cv2.medianBlur(maska,7)
    mask = cv2.medianBlur(mask,7)#purple detecting
    kernel = np.ones((7,7),np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)

    paint=paint + mask    #white paint on black due to purple detection
    new = cv2.bitwise_and(mask1,mask1,mask=paint)
    
    lower_limit_erase = np.array([0,0,0])
    upper_limit_erase = np.array([30,20,20])
    mask_erase = cv2.inRange(frame, lower_limit_erase, upper_limit_erase)
    mask_erase = cv2.medianBlur(mask_erase,7) #black detection
    
    
    erase = erase + mask_erase
    ret,thresh2 = cv2.threshold(erase,220,255,cv2.THRESH_BINARY_INV)
    new_erase = cv2.bitwise_and(new,new,mask=erase)
    new = new - erase
##    final = new - new_erase
    cv2.imshow('frame',frame)
    cv2.imshow('new',new)
    #cv2.imshow('black',thresh2)
    #cv2.imshow('final',final)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
