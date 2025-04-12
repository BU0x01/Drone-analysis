from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()
tello.streamon()

frame_read = tello.get_frame_read()
cv2.imwrite("campus_image.jpg", frame_read.frame)

tello.streamoff()
tello.end()
