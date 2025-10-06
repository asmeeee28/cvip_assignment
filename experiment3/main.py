import cv2
import numpy as np
import matplotlib.pyplot as plt
def shapes_demo():
    image = np.zeros((500, 700, 3), dtype=np.uint8)
    image.fill(255)  
    cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), -1)
    cv2.putText(image, "Rectangle", (60, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)   
    cv2.circle(image, (400, 150), 80, (0, 255, 0), -1)
    cv2.putText(image, "Circle", (370, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
    cv2.line(image, (100, 300), (500, 450), (0, 0, 255), 5)
    cv2.putText(image, "Line", (120, 290), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (15, 15), 0)
    edges = cv2.Canny(grayscale, 50, 150)
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes[0,0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0,0].set_title('Original with Shapes')
    axes[0,1].imshow(grayscale, cmap='gray')
    axes[0,1].set_title('Grayscale')
    axes[1,0].imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
    axes[1,0].set_title('Gaussian Blur')
    axes[1,1].imshow(edges, cmap='gray')
    axes[1,1].set_title('Edge Detection')
    for ax in axes.ravel():
        ax.axis("off")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    shapes_demo()
