from PIL import ImageGrab
import pyautogui
import numpy
import time
import cv2
import os


timeA = time.time()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
name = f"Recording{len(os.listdir())-2}.mp4"
out = cv2.VideoWriter(name, fourcc, 14.0, (1920, 1080))

white = (255, 255, 255)
black = (0, 0, 0)

while True:
    frame = ImageGrab.grab()
    data = frame.load()

    (x, y) = pyautogui.position()

    mouseFrame = numpy.array(frame)
    finalFrame = cv2.cvtColor(mouseFrame, 4)

    cv2.circle(finalFrame, (x, y), 7, (0, 0, 0), -1)
    cv2.circle(finalFrame, (x, y), 6, (255, 255, 255), -1)

    cv2.imshow("Recoding", finalFrame)
    out.write(finalFrame)

    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break

out.release()
cv2.destroyAllWindows()
print("Time:", str(time.time() - timeA)[:4]+"s")