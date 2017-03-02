
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    binary_image = cv2.inRange(frame, (70,70,100), (100, 100, 255))

    cv2.imshow('Binary', binary_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
