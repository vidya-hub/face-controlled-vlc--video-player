import math
import cv2
import numpy as np
import dlib
import pyautogui
detector=dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks")
cap=cv2.VideoCapture(0)
frames=0
frames_f=0
frames_b=0
frames_u=0
frames_d=0
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=detector(frame)
    for face in faces:
        x1=face.left()
        y1=face.top()
        x2=face.right()
        y2=face.bottom()
        landmarks=predictor(gray,face)
        x=landmarks.part(30).x
        y=landmarks.part(30).y
        cv2.circle(frame,(x,y),4,(255,255,255),-2)
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,255,255),2)
        up_x,up_y=landmarks.part(51).x,landmarks.part(51).y
        dn_x,dn_y=landmarks.part(57).x,landmarks.part(57).y 
        dist=math.sqrt((dn_x-up_x)**2+(dn_y-up_y)**2)
        if dist>25:
            frames+=1
            if frames==10:
                pyautogui.hotkey("space")
                frames=0
                continue
        try:
            if x<270:
                frames_b+=1
                if frames_b==3:
                    pyautogui.hotkey("ctrl","left")
                    frames_b=0
                    continue
            elif x>320:
                frames_f+=1
                if frames_f==3:
                    pyautogui.hotkey("ctrl","right")
                    frames_f=0
                    continue
            elif y<220:
                frames_u+=1
                if frames_u==3:
                    pyautogui.hotkey("ctrl","up")
                    frames_u=0
                    continue 
            elif y>240:
                frames_d+=1
                if frames_d==3:
                    pyautogui.hotkey("ctrl","down")
                    frames_d=0
                    continue
        except:
            pass 
    cv2.imshow("original",frame)
    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()