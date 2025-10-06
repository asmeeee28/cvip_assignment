import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("input.jpg", cv2.IMREAD_COLOR)
contrast_img = cv2.convertScaleAbs(image, alpha=1.5, beta=50)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist_eq = cv2.equalizeHist(gray)
smoothed = cv2.GaussianBlur(image, (9, 9), 0)
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
titles = ['Original', 'Contrast + Brightness', 'Histogram Equalization',
          'Smoothed (Gaussian Blur)', 'Thresholded']
images = [image, contrast_img, hist_eq, smoothed, thresholded]
plt.figure(figsize=(12,8))
for i in range(5):
    plt.subplot(2, 3, i+1)
    if len(images[i].shape) == 2:
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis("off")
plt.show()
