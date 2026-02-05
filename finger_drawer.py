import cv2
import mediapipe as mp  
import numpy as np
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils 
prev_x = 0
prev_y = 0
canvas = None 

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if canvas is None:
        canvas = np.zeros_like(img) 
    img = cv2.add(img, canvas)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB) 
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                x1, y1 = int(handLms.landmark[8].x * w), int(handLms.landmark[8].y * h)
                x2, y2 = int(handLms.landmark[6].x * w), int(handLms.landmark[6].y * h) 

                if id == 8:
                    if y2 > y1:
                        cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
                        if prev_x == 0 and prev_y == 0:
                            prev_x, prev_y = cx, cy

                        cv2.line(canvas, (prev_x, prev_y), (cx, cy), (255, 0, 255), 5)

                        prev_x, prev_y = cx, cy
                if y2 < y1:
                    if prev_x != 0 and prev_y != 0:

                        cv2.line(canvas, (prev_x, prev_y), (cx, cy), (0, 0, 0), 5)

                    prev_x, prev_y = cx, cy 



    cv2.imshow("Hand Tracker", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break