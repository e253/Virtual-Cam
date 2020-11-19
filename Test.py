import pyvirtualcam
import cv2



with pyvirtualcam.Camera(1280, 720, 30, 0, print_fps=True) as cam:
    while True