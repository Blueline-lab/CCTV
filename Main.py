"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

from time import time
import cv2
import random
import datetime




def find_face(img):

    facecascade = cv2.CascadeClassifier("haarcascade_face.xml")
    imggray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                  #Transforming the img in gray for dectection
    faces = facecascade.detectMultiScale(imggray, 2, 2)
    if faces != ():
        print("Alert")
        
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
        cv2.imshow('CCTV', img)

        out_videosaving.write(img)
        
        
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    Video_capture(mirror=True)


if __name__ == '__main__':
    main()
