import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="./wallpaper/car.png",
	help="path to input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("Original", image)
cv2.imshow("Blurred",blurred)

'''
1. Wide Thresholds:
High upper threshold and low lower threshold.
Detects more edges, including weak and possibly noisy edges.
Useful for scenarios where you want to capture as many edges as possible,
 even at the risk of including noise.
Example: lower_threshold = 50, upper_threshold = 150.

2. Mid Thresholds:
Moderate upper and lower thresholds.
A balance between detecting edges and reducing noise.
Suitable for general-purpose edge detection.
Example: lower_threshold = 100, upper_threshold = 200.

3.Tight Thresholds:
High lower threshold and even higher upper threshold.
Detects only the most prominent edges, ignoring weak edges and noise.
Useful for scenarios where you want very clean and prominent edges.
Example: lower_threshold = 150, upper_threshold = 250.
'''
wide=cv2.Canny(blurred,10,250)
mid=cv2.Canny(blurred,30,150)
tight=cv2.Canny(blurred,240,250)
cv2.imshow("Wide Edge Map",wide)
cv2.imshow("Mid Edge Map",mid)
cv2.imshow("Tight Edge Map",tight)
cv2.waitKey()
cv2.destroyAllWindows()


