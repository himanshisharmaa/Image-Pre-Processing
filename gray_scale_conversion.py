import cv2
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,default="./wallpaper/images.jpeg",help="Path to the input image")
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
grayscale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",image)
cv2.imshow("GrayScale",grayscale)
cv2.waitKey()
cv2.destroyAllWindows()

