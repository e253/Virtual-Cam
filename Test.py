import pyvirtualcam
import cv2
import numpy as np


video  = cv2.VideoCapture("C:\\Users\\Ethan\\Videos\\Transformers\\Transformers (2009 ) Revenge Of The Fallen.mp4")
webcam = cv2.VideoCapture(0)
INPUT = webcam
width = int(INPUT.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(INPUT.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps_in = int(INPUT.get(cv2.CAP_PROP_FPS))
print(height, width, fps_in)

with pyvirtualcam.Camera(width, height, fps_in, 0) as cam:
    while True:
        status, frame = INPUT.read()
        print(frame)
        out_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        print(out_frame)
        out_frame_rgba = np.zeros((height, width, 4), np.uint8)
        out_frame_rgba[:,:,:3] = out_frame
        out_frame_rgba[:,:,3] = 255
        print(out_frame_rgba)
        cam.send(frame)
        cam.sleep_until_next_frame()