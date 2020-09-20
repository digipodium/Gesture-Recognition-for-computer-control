import cv2
import numpy as np
import pyautogui

cap=cv2.VideoCapture(0)
yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])
upper_limit=200
lower_limit=300
left_limit=270-50
right_limit=370+50
actions={'space':False,'left':False,'down':False,'right':False}
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,yellow_lower,yellow_upper)
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    frame = cv2.line(frame,(0,198),(640,198),(0,255,0),4)
    frame = cv2.line(frame,(0,298),(640,298),(0,255,0),4)
    frame = cv2.line(frame,(218,0),(218,480),(255,255,255),4)
    frame = cv2.line(frame,(368+50,0),(368+50,480),(0,0,0),4)
    for c in contours:
        area=cv2.contourArea(c)
        if area>300:
            x,y,w,h=cv2.boundingRect(c)
#           cv2.drawContours(frame,c,-1,(0,255,0),2)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            if y<upper_limit and x<left_limit:
                if actions.get('space')==False:
                    pyautogui.press('space')
                    actions['space']=True
                    print(actions)
                    
            elif y<upper_limit and x>left_limit and x<right_limit:
                if actions.get('up')==False:
                    pyautogui.press('up')
                    actions['up']=True
                    print(actions)
            elif y>lower_limit and x>left_limit and x<right_limit:
                if actions.get('down')==False:
                    pyautogui.press('down')
                    actions['down']=True
                    print(actions)
            elif y>upper_limit and y<lower_limit and x<left_limit:
                if actions.get('left')==False:
                    pyautogui.press('left')
                    actions['left']=True
                    print(actions)
            elif y>upper_limit and y<lower_limit and x>right_limit:
                if actions.get('right')==False:
                    pyautogui.press('right')
                    actions['right']=True
                    print(actions)



            elif y>upper_limit and y<lower_limit and x>left_limit and x<right_limit:
                if actions.get('space') or actions.get('up') or actions.get('down') or actions.get('left') or actions.get('right'):
                    actions['space']=False
                    actions['up']=False
                    actions['down']=False
                    actions['left']=False
                    actions['right']=False
                    print(actions)
                
                
                
                
                
                
           # print("y:",y,"prev_y:",upper_limit)
    
    cv2.imshow('frame',frame)
    
    
    
    if cv2.waitKey(10)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
