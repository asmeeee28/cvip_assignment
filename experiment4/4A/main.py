import cv2
import sys

path = "input.jpg"  
img = cv2.imread(path)
if img is None:
    sys.exit(f"Could not read {path}")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
b, g, r = cv2.split(img)
gray_manual = (0.114*b + 0.587*g + 0.299*r).astype("uint8")
cv2.imshow("Original", img)
cv2.imshow("Gray (cv2)", gray)
cv2.imshow("Gray (manual)", gray_manual)
cv2.imwrite("output_gray.jpg", gray)  
cv2.waitKey(0)
cv2.destroyAllWindows()
