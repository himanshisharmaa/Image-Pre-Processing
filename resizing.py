import argparse
import cv2
import imutils
from PIL import Image

ap=argparse.ArgumentParser()
ap.add_argument("-i",'--img',type=str,default="./wallpaper/images.jpeg",help="path of the input image")
args=vars(ap.parse_args())
image=cv2.imread(args['img'])
cv2.imshow("Images",image)

# resize the image to be the 150 pixel wide, but in order to prevent the 
# resized image from being skewed/distorted, we must first calculate the ratio
# of the "new" width to the "old"

r=150.0/image.shape[1]
dim=(150,int(image.shape[0]*r))
resized_inter_area=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
resized_inter_nearest=cv2.resize(image,dim,interpolation=cv2.INTER_NEAREST)
resized_inter_linear=cv2.resize(image,dim,interpolation=cv2.INTER_LINEAR)
resized_inter_cubic=cv2.resize(image,dim,interpolation=cv2.INTER_CUBIC)
resized_inter_LANCZOS4=cv2.resize(image,dim,interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("inter_area",resized_inter_area)
cv2.imshow("inter_nearest",resized_inter_nearest)
cv2.imshow("inter_linear",resized_inter_linear)
cv2.imshow("inter_cubic",resized_inter_cubic)
cv2.imshow("inter_LANCZOS4",resized_inter_LANCZOS4)

cv2.waitKey()
cv2.destroyAllWindows()


#imutils

resized=imutils.resize(image,width=250)
cv2.imshow('Resized Width',resized)
cv2.waitKey()

## pil
img=Image.open('./wallpaper/images.jpeg')
resized=img.resize((224,224))