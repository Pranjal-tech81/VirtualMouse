import cv2
import HandTrackingModule as htm
import mouse
import time
import autopy

import numpy as np
import pyautogui

# ===============================================================

wCam = 740
hCam = 780
pTime = 0
frameR = 20
smoothening = 7
plocX, plocY = 0, 0
clocX, clocY = 0, 0
detector = htm.handDetector(maxHands=1)
wScr, hScr = 1537, 865
#print(autopy.screen.size())
# =================================================================
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bBox = detector.findPosition(img)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
#     cv2.putText(img,str(int(fps)),(10,50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),3)

    if (len(lmList)) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR),
                      (wCam-frameR, hCam-frameR), (1, 0, 0), 2)

# MOVEMENT OF MOUSE
# ==================================================================

        
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:

            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            clocX = plocX+(x3-plocX)/smoothening
            clocY = plocY+(y3-plocY)/smoothening

            if(wScr-x3 < 1560 and y3 < 870):
                autopy.mouse.move(wScr-(x3), (y3))

            cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
            plocX, plocY = clocX, clocY

# Left Click
# ===================================================================
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if(length < 30):
                cv2.putText(img, "LEFT CLICK  "+str(int(length)),
                            (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (255, 255, 255), cv2.FILLED)
                autopy.mouse.click()
                print("left")


# Rigth Click
# ===================================================================
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            length, img, lineInfo = detector.findDistance(4, 8, img)
            if(length < 50):
                cv2.putText(img, "RIGHT CLICK  "+str(int(length)),
                            (10, 80), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (255, 255, 255), cv2.FILLED)
                mouse.click('right')
                print("right")


# Scroll Up
# ====================================================================

        if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            value = 20
            val = 0
            print("up")
            while True:
                cv2.putText(img, "scroll up activate", (10, 150),
                            cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 3)
                pyautogui.scroll(10)
                val += 1
                if(val == value):
                    break

# Scroll Down
# ======================================================================

        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:
            print("down")
            value = 20
            val = 0
            while True:
                cv2.putText(img, "scroll down activate", (10, 210),
                            cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 3)
                pyautogui.scroll(-10)
                val += 1
                if val == value:
                    break

# Exiting
# =======================================================================
    cv2.imshow("WINDOW", img)
    if cv2.waitKey(30) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
