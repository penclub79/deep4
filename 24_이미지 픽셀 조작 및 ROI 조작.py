import numpy as np
import cv2
from random import shuffle
import math

img = cv2.imread('images/hallstatt.jpg')

B = img.item(340, 200, 0)
G = img.item(340, 200, 1)
R = img.item(340, 200, 2)

BGR = [B, G, R]
print(BGR)
px = img[340, 200]
print(px)

print(img.shape)
print(img.size)
print(img.dtype)

# def addImage(imgfile1, imgfile2):
#     img1 = cv2.imread(imgfile1)
#     img2 = cv2.imread(imgfile2)
#
#     cv2.imshow('img1', img1)
#     cv2.imshow('img2', img2)
#
#     add_img1 = img1 + img2
#     add_img2 = cv2.add(img1, img2)
#
#     cv2.imshow('img1+img2', add_img1)
#     cv2.imshow('add(img1, img2)', add_img2)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# addImage('images/hallstatt.jpg', 'images/ho.jpg')

def onMouse(x):
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     shuffle(B), shuffle(G), shuffle(R)
    #     cv2.circle(param, (x,y), 50, (B[0], G[0], R[0], -1))
    pass
def imgBlending(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.namedWindow('ImgPane')
    cv2.createTrackbar('MIXING', 'ImgPane', 0, 100, onMouse)
    mix = cv2.getTrackbarPos('MIXING', 'ImgPane')

    while True:
        img = cv2.addWeighted(img1, float(100-mix)/100, img2, float(mix)/100, 0)
        cv2.imshow('ImgPane', img)
        k = cv2.waitKey(1) & 0xFF
        mix = cv2.getTrackbarPos('MIXING', 'ImgPane')

        if k == 27:
            break
        elif k == ord('m'):
            mode = not mode

cv2.destroyAllWindows()
imgBlending('images/hallstatt.jpg', 'images/suji.jpg')


def bitOperation(hpos, vpos):
    img1 = cv2.imread('images/suji.jpg')
    img2 = cv2.imread('images/ho.jpg')

    rows, cols, channels = img2.shape
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos:rows+vpos, hpos:cols+hpos] = dst

    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitOperation(10, 10)
