import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("input.jpg", 0)
def sp_noise(image, prob=0.05):
    noisy = np.copy(image)
    rnd = np.random.rand(*image.shape)
    noisy[rnd < prob/2] = 0
    noisy[rnd > 1 - prob/2] = 255
    return noisy
sp_noisy = sp_noise(img)
sp_denoised = cv2.medianBlur(sp_noisy, 3)
def speckle_noise(image):
    row,col = image.shape
    noise = np.random.randn(row,col) * 0.2
    noisy = image + image * noise
    return np.clip(noisy,0,255).astype(np.uint8)
speckle_noisy = speckle_noise(img)
speckle_denoised = cv2.GaussianBlur(speckle_noisy,(3,3),0)
plt.figure(figsize=(12,6))
plt.subplot(2,3,1), plt.imshow(img,cmap='gray'), plt.title("Original")
plt.axis("off")
plt.subplot(2,3,2), plt.imshow(sp_noisy,cmap='gray'), plt.title("Salt & Pepper Noise")
plt.axis("off")
plt.subplot(2,3,3), plt.imshow(sp_denoised,cmap='gray'), plt.title("Denoised (Median)")
plt.axis("off")
plt.subplot(2,3,4), plt.imshow(speckle_noisy,cmap='gray'), plt.title("Speckle Noise")
plt.axis("off")
plt.subplot(2,3,5), plt.imshow(speckle_denoised,cmap='gray'), plt.title("Denoised (Gaussian)")
plt.axis("off")w
plt.show()
