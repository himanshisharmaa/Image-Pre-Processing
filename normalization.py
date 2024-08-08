import argparse
import cv2
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',type=str,default="./wallpaper/images.jpeg",help="Path to the input image")
args=vars(ap.parse_args())
image=cv2.imread(args['image'])
normalized_image=image/255.0
cv2.imshow("Image",image)
cv2.imshow("Normalized Image",normalized_image)
cv2.waitKey()
print(f"Image shape: {image.shape}")
# standardization
mean,std=cv2.meanStdDev(image)
mean=mean.reshape((1,1,3))
std=std.reshape((1,1,3))
print(mean,std)
std_img=(image-mean)/std
std_img=cv2.normalize(std_img,None,0,255,cv2.NORM_MINMAX).astype(np.uint8)
cv2.imshow("Standardized Image",std_img)
cv2.waitKey()