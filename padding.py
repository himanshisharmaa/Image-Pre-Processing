import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,default="./wallpaper/car.png",help="Path to the input Image")
args=vars(ap.parse_args())
image=cv2.imread(args['image'])
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
top,bottom,left,right=50,50,50,50

# Constant Border
constant_border = cv2.copyMakeBorder(image_rgb, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 0, 0])

# Reflect Border
reflect_border = cv2.copyMakeBorder(image_rgb, top, bottom, left, right, cv2.BORDER_REFLECT)

# Replicate Border
replicate_border = cv2.copyMakeBorder(image_rgb, top, bottom, left, right, cv2.BORDER_REPLICATE)

# Wrap Border
wrap_border = cv2.copyMakeBorder(image_rgb, top, bottom, left, right, cv2.BORDER_WRAP)

# Reflect 101 Border
reflect101_border = cv2.copyMakeBorder(image_rgb, top, bottom, left, right, cv2.BORDER_REFLECT_101)


cv2.imshow("Original",image)
cv2.imshow("Constant Border",image)
cv2.imshow("Reflect Border",image)
cv2.imshow("Replicate Border",image)
cv2.imshow("Wrap Border",image)
cv2.imshow("Reflect 101 Border",image)
cv2.waitKey()
cv2.destroyAllWindows()