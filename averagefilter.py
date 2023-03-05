import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('aa.jpg')

img = np.float32(img)/255.0

kernel = np.ones((5,5),np.float32)/25

filtered_img = cv2.filter2D(img, -1, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(filtered_img),plt.title('Filtered')
plt.xticks([]), plt.yticks([])
plt.show()
