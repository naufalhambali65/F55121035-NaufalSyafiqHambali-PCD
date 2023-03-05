import cv2
import numpy as np

# load citra input pertama dan kedua dalam grayscale
img1 = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# lakukan pengurangan citra
result = cv2.subtract(img1, img2)

# tampilkan hasil
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
