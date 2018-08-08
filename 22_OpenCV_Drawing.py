import numpy as np
import cv2

def drawing():
    img = np.zeros((512,512, 3), np.uint8)

    #다양한 색상과 선두꼐를 가진 도형 그리기
    cv2.line(img, (0,0), (511, 511), (255, 0, 0), 5)
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255), 3)
    cv2.circle(img, (477, 63), 63, (0, 0, 255), -1)
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0,180, (255, 0, 0), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'sess', (10, 500), font, 6, (255, 255, 255), 5)

    cv2.imshow('drawing', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

drawing()