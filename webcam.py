"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2
import random


def find_face(img):

    facecascade = cv2.CascadeClassifier("haarcascade_face.xml")
    imggray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                  #Transforming the img in gray for dectection
    faces = facecascade.detectMultiScale(imggray, 2, 2)
    if faces != ():
        print("find")
        
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)
    
        
        cv2.imwrite(f'images/{random.randint(1, 300)}.png',img)
    




def show_webcam(mirror=False):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
            
        face = find_face(img)
        cv2.imshow('my webcam', img)
        out.write(img)
        
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()
