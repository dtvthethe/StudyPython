import cv2
import numpy as np
#import time

# cv2.namedWindow('HienThi', cv2.WINDOW_NORMAL)
#
# vid = cv2.VideoCapture('video_exp.avi')
# print(vid.get(5))
# while vid.isOpened():
#     ret, frame = vid.read()
#     cv2.imshow('HienThi', frame)
#     time.sleep(1/50)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# vid.release()
img1 = cv2.create

img = cv2.imread('bc_den-trang.png',)
red = np.sum(img == 0)
print('Tong mau do:', red)