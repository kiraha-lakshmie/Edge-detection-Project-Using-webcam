import cv2
import numpy as np

image = cv2.imread("test.jpg")

if image is None:
    print("Image not found!")
    exit()

image = cv2.resize(image, (640, 480))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blur, 50, 150)

# Dilate edges to close gaps
kernel = np.ones((5,5), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=2)

# Find contours
contours, _ = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

mask = np.zeros_like(gray)

if contours:
    largest = max(contours, key=cv2.contourArea)
    cv2.drawContours(mask, [largest], -1, 255, thickness=cv2.FILLED)

cv2.imshow("Original", image)
cv2.imshow("Edges", edges)
cv2.imshow("Final Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()