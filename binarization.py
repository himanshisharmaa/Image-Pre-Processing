import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,default="./wallpaper/car.png",help="Path to the input Image")
args=vars(ap.parse_args())
image=cv2.imread(args['image'])

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(7,7),0)

'''
    apply basic thresholding- the first parameter is the image we want to 
    threshold. the second value is our threshold check if a pixel value is
    greater than our threshold(in this case 200),we set it to black otherwise
    it is white
'''
cv2.imshow("Original",image)
(T,threshInv)=cv2.threshold(blurred,200,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary inverse",threshInv)
cv2.waitKey()
cv2.destroyAllWindows()

#using normal thresholding (rather than inverse thresholding)
cv2.imshow("Original",image)
(T,thresh)=cv2.threshold(blurred,200,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary",thresh)
masked=cv2.bitwise_and(image,image,mask=threshInv)
cv2.imshow("Output",masked)
cv2.waitKey()
cv2.destroyAllWindows()

# Otsu's thresholding
cv2.imshow("Original",image)
(T,threshInv)=cv2.threshold(blurred,200,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
cv2.imshow("Threshold Binary OTSU",threshInv)
masked=cv2.bitwise_and(image,image,mask=threshInv)
cv2.imshow("Output Otsu's masked",masked)
cv2.waitKey()
cv2.destroyAllWindows()