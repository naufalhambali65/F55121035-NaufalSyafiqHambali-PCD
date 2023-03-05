import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('aa.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# Calculate the cumulative distribution function (CDF)
cdf = hist.cumsum()
cdf_normalized = cdf / cdf.max()

# Calculate the new intensity values using the CDF
img_equalized = np.interp(img.flatten(), bins[:-1], cdf_normalized).reshape(img.shape)

# Convert the image back to 8-bit grayscale
img_equalized = (img_equalized * 255).astype(np.uint8)

# Display the original and equalized images
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(img_equalized, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')
plt.show()
