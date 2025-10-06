import cv2
import matplotlib.pyplot as plt
image = cv2.imread("input.jpg")   
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
mean_filtered = cv2.blur(image, (5, 5))  
gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  
laplacian_filtered = cv2.Laplacian(gray, cv2.CV_64F)
laplacian_filtered = cv2.convertScaleAbs(laplacian_filtered) 
titles = ["Original", "Mean Filter", "Gaussian Filter", "Laplacian Filter"]
images = [image, mean_filtered, gaussian_filtered, laplacian_filtered]
plt.figure(figsize=(10,8))
for i in range(4):
    plt.subplot(2, 2, i+1)
    if i == 3:
        plt.imshow(images[i], cmap='gray')  
    else:
        plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")
plt.show()
