"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

from email import message
from time import time
import cv2
import random
import datetime
import os 

#local import 
import com



def find_face(img):
    
    facecascade = cv2.CascadeClassifier("haarcascade_face.xml")
    imggray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                  #Transforming the img in gray for dectection
    faces = facecascade.detectMultiScale(imggray, 2, 2)
    if faces != () and com.messagedelay == True :
        
        com.telegram_bot("Alert face detected on video _1_")
        com.messagedelay = False
        
       
        

        
        
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)
    
        
        cv2.imwrite(f'images/{random.randint(1, 300)}.png',img)
    




def Video_capture(mirror=False):
    format_towrite = cv2.VideoWriter_fourcc(*'XVID')
    out_videosaving = cv2.VideoWriter(f'./VideoDATA/{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.avi',format_towrite, 20.0, (640,  480))
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
            
        face = find_face(img)
        com.time += 1
        if com.time > 300:
            com.messagedelay = True
            com.time = 0
        cv2.namedWindow("CCTV", cv2.WND_PROP_AUTOSIZE)
        cv2.setWindowProperty("CCTV",cv2.WND_PROP_AUTOSIZE,cv2.WINDOW_AUTOSIZE)
        cv2.imshow('CCTV', img,)

        out_videosaving.write(img)
        
        
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    Video_capture(mirror=True)


if __name__ == '__main__':
    main()
