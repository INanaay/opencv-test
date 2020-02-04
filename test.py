import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider



cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")

    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        break


cam.release()
cv2.destroyAllWindows()


minvalue = 100
maxvalue = 100

edges = cv2.Canny(frame, minvalue, maxvalue)

plt.subplot(121), plt.imshow(frame, cmap='gray')

plt.title('original Image'), plt.xticks([], plt.yticks([]))

plt.subplot(122), plt.imshow(edges, cmap='gray')

plt.title('Edge image'), plt.xticks([]), plt.yticks([])

min_value_slider = Slider(plt.axes([0.25, .1, 0.50, 0.02]), 'minValue', 0, 1000, valinit=100)

max_value_slider = Slider(plt.axes([0.25, .05, 0.50, 0.02]), 'maxValue', 0, 1000, valinit=500)


def updatemin(val):
    new_edges = cv2.Canny(frame, val, maxvalue)
    plt.subplot(122), plt.imshow(new_edges, cmap='gray')
    plt.title('edge Image'), plt.xticks([], plt.yticks([]))

def updatemax(val):
    new_edges = cv2.Canny(frame, minvalue, val)
    plt.subplot(122), plt.imshow(new_edges, cmap='gray')
    plt.title('edge Image'), plt.xticks([], plt.yticks([]))


min_value_slider.on_changed(updatemin)

max_value_slider.on_changed(updatemin)


plt.show()
