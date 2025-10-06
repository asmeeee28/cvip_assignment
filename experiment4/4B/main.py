import cv2
import numpy as np
def rgb_to_cmyk(image):
    rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB).astype(float) / 255.0
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    K = 1 - np.max(rgb, axis=2)
    C = (1 - R - K) / (1 - K + 1e-8)
    M = (1 - G - K) / (1 - K + 1e-8)
    Y = (1 - B - K) / (1 - K + 1e-8)
    C[K == 1] = 0
    M[K == 1] = 0
    Y[K == 1] = 0
    cmyk = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
    return cmyk
image = cv2.imread("input.jpg")  
cmyk_image = rgb_to_cmyk(image)
C, M, Y, K = cv2.split(cmyk_image)
cv2.imshow("Original BGR", image)
cv2.imshow("Cyan", C)
cv2.imshow("Magenta", M)
cv2.imshow("Yellow", Y)
cv2.imshow("Black", K)
cv2.waitKey(0)
cv2.destroyAllWindows()
