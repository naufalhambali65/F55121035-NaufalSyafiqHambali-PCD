import cv2
import numpy as np

# load the input images
img1 = cv2.imread('aa.jpg')
img2 = cv2.imread('aa.jpg')
img3 = cv2.imread('aa.jpg')

# convert the images to floating point
img1 = img1.astype(np.float32)
img2 = img2.astype(np.float32)
img3 = img3.astype(np.float32)

# compute the average image
avg_img = (img1 + img2 + img3) / 3

# convert the average image back to uint8 format
avg_img = avg_img.astype(np.uint8)

# display the result
cv2.imshow('Average Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
