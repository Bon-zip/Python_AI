import cv2
image = cv2.imread("lienbuoi.jpg")
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invert , (25, 25,), 0)

invertedblur = cv2.bitwise_not(blur)

sketch = cv2.divide(grey_img , invertedblur , scale=242.4)

cv2.imwrite("builien.jpg", sketch)
