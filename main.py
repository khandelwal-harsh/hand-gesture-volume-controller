import cv2 
from volumecontrol import VolumeControl

video = cv2.VideoCapture(0)
while True:
    _,input_frame = video.read()    
    vcObject = VolumeControl(input_frame)
    output_frame = vcObject.calculate_volume_and_set_volume()
    cv2.imshow('Image',output_frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break


