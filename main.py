import cv2 as cv
import numpy as np
cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
else:
    try:
        old_point= []
        
        while True:
            ret, frame = cap.read()
            frame = cv.flip(frame,1)
            if not ret:
                print("No suchcapture")
                break

            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            lower_blue =np.array([110,50,50])
            upper_blue= np.array([130,255,255])
            mask = cv.inRange(hsv, lower_blue,upper_blue)

      
            contours, hierarcy= cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)


            for c in contours:
                if cv.contourArea(c)>500:
                    x,y,w,h = cv.boundingRect(c)
                    cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
                    circle_x= x+(w//2)
                    circle_y= y+(h//2)
                    old_point.append((circle_x,circle_y))
                    cv.circle(frame,(circle_x,circle_y),5,(0,0,255),-1)
                    cv.putText(frame,str(f"X:{circle_x}, Y:{circle_y}"), (5,25), cv.FONT_HERSHEY_SIMPLEX,0.6, (0,255,0),2,cv.LINE_AA)
                    old_point = old_point[-100:]
            for i in range(1, len(old_point)):
                cv.line(frame,old_point[i],old_point[i-1],(0,0,255),2)
           
            cv.imshow("Normal Camera", frame)
            
            if cv.waitKey(1) & 0xFF == ord('q'): 
                break
            elif cv.waitKey(1) & 0XFF == ord('c'):
                old_point =[]

    finally:
        cap.release()
        cv.destroyAllWindows()
        for i in range(5):
            cv.waitKey(1)