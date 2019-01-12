import cv2

img_path = 'image_input.png'

img = cv2.imread(img_path, flags=cv2.IMREAD_UNCHANGED)
print(img)
cv2.line(img, (0,0), (7,0), (0,255,0), 1)
cv2.imwrite('img_output.png', img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
