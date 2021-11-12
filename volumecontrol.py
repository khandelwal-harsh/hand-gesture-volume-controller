import cv2 
import mediapipe as mp
from math import hypot
import numpy as np
import alsaaudio


class VolumeControl:

    def __init__(self,frame) -> None:
        """
        Initialize Frame and Hand landmark model
        """
        self.frame = frame
        self.mpHands = mp.solutions.hands 
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.volMin,self.volMax = [0,100]

    def set_volume(self,volume) -> None:
        """
        Set System's Volume
        """
        m = alsaaudio.Mixer()
        m.setvolume(int(volume))    

    def calculate_volume_and_set_volume(self) -> np.ndarray:
        """
        Return Calculate Volume
        """
        imgRGB = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        lmList = []
        if results.multi_hand_landmarks:
            for handlandmark in results.multi_hand_landmarks:
                for id,lm in enumerate(handlandmark.landmark):
                    h,w,_ = self.frame.shape
                    cx,cy = int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy]) 
                self.mpDraw.draw_landmarks(self.frame,handlandmark,self.mpHands.HAND_CONNECTIONS)
        volume = -1
        if lmList != []:
            x1,y1 = lmList[4][1],lmList[4][2]
            x2,y2 = lmList[8][1],lmList[8][2]

            cv2.circle(self.frame,(x1,y1),4,(255,0,0),cv2.FILLED)
            cv2.circle(self.frame,(x2,y2),4,(255,0,0),cv2.FILLED)
            cv2.line(self.frame,(x1,y1),(x2,y2),(255,0,0),3)

            length = hypot(x2-x1,y2-y1)
            volume = round(np.interp(length,[15,220],[self.volMin,self.volMax]))
            self.set_volume(volume)
        return self.frame
