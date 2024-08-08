import argparse
import cv2
import numpy as np
import imutils

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',type=str,default='./wallpaper/images.jpeg',help="Path to the input image")
args=vars(ap.parse_args())
image=cv2.imread(args['image'])


#rotation 
## grab the dimensions and calculate the center of the image
cv2.imshow("Original",image)
(h,w)=image.shape[:2]
(cx,cy)=(w//2,h//2)
## rotate the image by 45 degrees around the center of the image
## cv2.getRotationMatrix2D(center,angle,scale) function is used to make the transformation
## matrix M which will be used for rotating a image. returns 2x3 matrix M
M=cv2.getRotationMatrix2D((cx,cy),45,1.0)
## in affine transformation, all parallel lines in the original image will still be
## parallel in the output image.cv2.warpAffine(src, M, dsize, dst, flags, borderMode, borderValue)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated by 45 degrees",rotated)
## rotate our image around an arbitrary point rather than the center
M=cv2.getRotationMatrix2D((10,25),-45,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated by -45 degrees",rotated)
cv2.waitKey()
cv2.destroyAllWindows()


#Flipping
cv2.imshow("Original",image)
## horizontally
flipped=cv2.flip(image,1)
cv2.imshow("Horizontally",flipped)
## Vertically
flipped=cv2.flip(image,0)
cv2.imshow("Vertically",flipped)
##Both
flipped=cv2.flip(image,-1)
cv2.imshow("BOTH",flipped)
cv2.waitKey()
cv2.destroyAllWindows()


# Cropping
cv2.imshow("Original",image)
crop=image[67:123,93:187]
crop2=image[17:178,32:229]
cv2.imshow("Cropped",crop)
cv2.imshow("Flower",crop2)
cv2.waitKey()
cv2.destroyAllWindows()


# Scaling
cv2.imshow("Original",image)
scaled=cv2.resize(image,None,fx=1.52,fy=1.52,interpolation=cv2.INTER_LINEAR)
cv2.imshow("Scaled",scaled)
cv2.waitKey()
cv2.destroyAllWindows()


# Translation
cv2.imshow("Original",image)
## shift the image 25 pixels right and 50 px down
M=np.float32([[1,0,25],[0,1,50]])
shifted1=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Shifted1",shifted1)
## let's shift the image 50 pixels to the left and 90 pixels up
M=np.float32([[1,0,-50],[0,1,-90]])
shifted2=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Shifted2",shifted2)
## imutils
shifted_imutils=imutils.translate(image,30,100)
cv2.imshow("Shifted Imutils",shifted_imutils)
cv2.waitKey()
cv2.destroyAllWindows()


# Shearing
## horizontal sheer: [[1,shear_factor,0],[0,1,0]]
## vertical sheer: [[1,0,0],[shear_factor,1,0]]
cv2.imshow("Original",image)
M=np.float32([[1,0,0],[0.2,1,0]])
sheared=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Sheared",sheared)
cv2.waitKey()
cv2.destroyAllWindows()

# Brightness , Contrast, Saturation Adjustment
cv2.imshow("Original",image)
## Brightness
M=np.ones(image.shape,dtype='uint8')*100
added=cv2.add(image,M)
cv2.imshow("Brighter By Adding",added)
###############OR########################
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
v=cv2.add(v,100)
v=np.clip(v,0,255)
final_hsv=cv2.merge((h,s,v))
bright_image=cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
cv2.imshow("HSV Brightness",bright_image)
cv2.waitKey()
cv2.destroyAllWindows()
## Contrast
### to change the contrast and brightness of an image we 
### could use cv2.convertScaleAbs(image, alpha, beta).
### alpha -> contrast value 0<alpha<1
### beta -> brightness value [-127,127]
cv2.imshow("Original",image)
contrast_image=cv2.convertScaleAbs(image,alpha=1.5,beta=0)
cv2.imshow("Contrast",contrast_image)
cv2.waitKey()
cv2.destroyAllWindows()
## Saturation
cv2.imshow("Original",image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
s = cv2.add(s, 70)
s = np.clip(s, 0, 255)
final_hsv = cv2.merge((h, s, v))
saturated = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Saturation",saturated)
cv2.waitKey()
cv2.destroyAllWindows()


# Hue Adjustment
cv2.imshow("Original",image)
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
h=cv2.add(h,10)
h=np.clip(h,0,179)
final_hsv=cv2.merge((h,s,v))
hue_adjusted = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Hue Adjustment",hue_adjusted)
cv2.waitKey()
cv2.destroyAllWindows()


# Gaussian Noise
cv2.imshow("Original",image)
gauss=np.random.normal(0,2,image.shape).astype('uint8')
noisy_image=cv2.add(image,gauss)
cv2.imshow("Noisy Image",noisy_image)
cv2.waitKey()
cv2.destroyAllWindows()


# Blur

kernelSizes=[(3,3),(9,9),(15,15)]
## Average Blur,Gaussian Blur, Median blur
for (kx,ky) in kernelSizes:
    cv2.imshow("Original",image)
    blurred=cv2.blur(image,(kx,ky))
    cv2.imshow(f"Average {(kx,ky)}",blurred)
    blurred=cv2.GaussianBlur(image,(kx,ky),0)
    cv2.imshow(f"Gaussian {(kx,ky)}",blurred)
    blurred=cv2.medianBlur(image,(kx))
    cv2.imshow(f"Median {kx}",blurred)
    cv2.waitKey()
    cv2.destroyAllWindows()


# Cutout/Random Erasing
cv2.imshow("Original",image)
cutout_image=image.copy()
cutout_image[50:100,50:100]=0
cv2.imshow("CutOut",cutout_image)
cv2.waitKey()
cv2.destroyAllWindows()


# MixUp
## Steps:
## 1. Load the images
## 2. Generate a random mixing Coefficient
## 3. Combine the images
## 4. Combining the Labels
## 5. Display the result
image2=cv2.imread("./wallpaper/122.jpg")
image = cv2.resize(image, (224, 224))
image2 = cv2.resize(image2, (224, 224))

### Generate mixing coefficient from beta distribution
alpha=0.2
lam=np.random.beta(alpha,alpha)
### Combine the images
mixed_image=(lam*image+(1-lam)*image2).astype(np.uint8)
cv2.imshow("Mixed image",mixed_image)
cv2.waitKey()
cv2.destroyAllWindows()
