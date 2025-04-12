import cv2
import numpy as np

image = cv2.imread("campus_image.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define green range
lower_green = np.array([35, 40, 40])
upper_green = np.array([90, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)

green_ratio = np.sum(mask > 0) / (image.shape[0] * image.shape[1])
print(f"Green area percentage: {green_ratio:.2%}")

cv2.imshow("Vegetation Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
