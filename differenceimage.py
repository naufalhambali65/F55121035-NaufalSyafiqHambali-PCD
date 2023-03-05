import cv2
import numpy as np
from matplotlib import pyplot as plt
# input gambar
img = cv2.imread('Lena.png', 0)
diff_img = cv2.imread('Lena.png', 0)

# perbaikan kontras
diff_img = cv2.equalizeHist(diff_img)

# Perbaikan noise
diff_img = cv2.medianBlur(diff_img, 3)

# output
plt.subplot(121),plt.imshow(img, cmap='gray'),plt.title('before')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(diff_img, cmap='gray'),plt.title('after')
plt.xticks([]), plt.yticks([])
plt.show()

