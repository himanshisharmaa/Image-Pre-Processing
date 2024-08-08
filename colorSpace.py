import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,default="./wallpaper/images.jpeg",help="Path to the input Image")
args=vars(ap.parse_args())
image=cv2.imread(args['image'])
cv2.imshow("RGB",image)
for (name,chan) in zip(("B","G","R"),cv2.split(image)):
    cv2.imshow(name,chan)
cv2.waitKey()
cv2.destroyAllWindows()

#convert the image to the HSV color space and shw it
cv2.imshow("RGB",image)
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)
for (name,chan) in zip(("H","S","V"),cv2.split(hsv)):
    cv2.imshow(name,chan)
cv2.waitKey(0)
cv2.destroyAllWindows()

#convert the image to the L*a*b* color space and shw it
cv2.imshow("RGB",image)
lab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB",lab)
for (name,chan) in zip(("L*","a*","b*"),cv2.split(lab)):
    cv2.imshow(name,chan)
cv2.waitKey(0)
cv2.destroyAllWindows()


#show the original and grayscal version of the img
cv2.imshow("RGB",image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",image)
cv2.imshow("GrayScale",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()