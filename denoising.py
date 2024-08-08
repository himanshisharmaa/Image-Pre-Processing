import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,default="./wallpaper/car.png",help="Path to the input Image")
args=vars(ap.parse_args())
image=cv2.imread(args['image'])

# for denoising we can use blurring too that we have already used 
# apart from that we have following methods

# Bilateral filtering
cv2.imshow("Original",image)
params=[(11,21,7),(11,41,21),(11,61,39)]

## loop over the diameter, sigma color and sigma space
for (diameter,sigmaColor,sigmaSpace) in params:
    #apply bilateral filtering to the image
    blurred=cv2.bilateralFilter(image,diameter,sigmaColor,sigmaSpace)
    title=f"BilateralFilter d={diameter}, sc={sigmaColor},ss={sigmaSpace}"
    cv2.imshow(title,blurred)
    cv2.waitKey()
cv2.destroyAllWindows()

# Non-Local Means Denoising
cv2.imshow("Original",image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
nlm_denoised=cv2.fastNlMeansDenoising(gray,None,30,7,21)
cv2.imshow('NLM Denoised Image', nlm_denoised)
cv2.waitKey()
cv2.destroyAllWindows()
