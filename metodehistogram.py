import cv2
import numpy as np
import matplotlib.pyplot as plt

# load gambar grayscale
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# hitung histogram gambar
hist, bins = np.histogram(img.flatten(), 256, [0,256])

# tampilkan histogram
plt.hist(img.flatten(), 256, [0,256], color = 'r')
plt.xlim([0,256])
plt.show()
