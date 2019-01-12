import cv2

img_path = 'image_input.png'

img = cv2.imread(img_path,flags=cv2.IMREAD_UNCHANGED)
for i in range(img.shape[1]):
    if i % 2 == 0:
        img[i][1] = [0,255,0]


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()