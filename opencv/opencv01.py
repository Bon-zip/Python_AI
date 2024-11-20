import cv2
# đọc ảnh
img = cv2.imread("thumuc/anh.jpg", 1)

# resize image 
# img = cv2.resize(img, (200, 200))  # rộng , dài
img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)
# xoay ảnh
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# xuất ảnh
cv2.imshow("cua so hien thi", img)
k = cv2.waitKey()
if k == ord("s"):
    cv2.imwrite("thumuc/anhmoi5.png", img)
