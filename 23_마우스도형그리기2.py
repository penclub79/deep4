from random import shuffle
import numpy as np
import cv2
import math

mode, drawing = True, False
ix, iy = -1, -1
R = [i for i in range(256)]
G = [i for i in range(256)]
B = [i for i in range(256)]

def onMouse(event, x, y, flags, param):
    global ix, iy, drawing, mode, R, G, B
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        shuffle(R), shuffle(G), shuffle(B)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(param, (ix, iy), (x, y), (R[0], G[0], B[0]), -1)
            else:
                r = (ix-x)**2 + (iy-y)**2
                r = int(math.sqrt(r))
                cv2.circle(param, (ix, iy), r, (R[0], G[0], B[0]), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(param, (ix, iy), (x, y), (R[0], G[0], B[0]), -1)
        else:
            r = (ix-x)**2 + (iy-y)**2
            r = int(math.sqrt(r))
            cv2.circle(param, (ix, iy), r, (R[0], G[0], B[0]), -1)

def mouseBrush():
    global mode

    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('paint')
    cv2.setMouseCallback('paint', onMouse, param=img)

    while True:
        cv2.imshow('paint', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break
        elif k == ord('m'):
            mode = not mode

    cv2.destroyAllWindows()

mouseBrush()