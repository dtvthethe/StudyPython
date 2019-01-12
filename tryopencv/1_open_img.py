import cv2

img_path = 'image_output.png'

img = cv2.imread(img_path,flags=cv2.IMREAD_UNCHANGED)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()