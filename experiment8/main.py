import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("input.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
transpose_img = cv2.transpose(img_rgb)
crop_img = img_rgb[50:250, 100:300]   
flip_vertical = cv2.flip(img_rgb, 0)
(h, w) = img_rgb.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img = cv2.warpAffine(img_rgb, M, (w, h))
M_shear = np.float32([[1, 0.5, 0],
                      [0.5, 1, 0]])
shear_img = cv2.warpAffine(img_rgb, M_shear, (w + 100, h + 100))
plt.figure(figsize=(12,8))
plt.subplot(2,3,1), plt.imshow(img_rgb), plt.title("Original")
plt.axis("off")
plt.subplot(2,3,2), plt.imshow(transpose_img), plt.title("Transpose")
plt.axis("off")
plt.subplot(2,3,3), plt.imshow(crop_img), plt.title("Cropping")
plt.axis("off")
plt.subplot(2,3,4), plt.imshow(flip_vertical), plt.title("Vertical Flip")
plt.axis("off")
plt.subplot(2,3,5), plt.imshow(rotated_img), plt.title("Rotation (45°)")
plt.axis("off")
plt.subplot(2,3,6), plt.imshow(shear_img), plt.title("Shearing")
plt.axis("off")
plt.show()
