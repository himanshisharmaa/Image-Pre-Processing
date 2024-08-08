import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,default="./wallpaper/images.jpeg",help="Path to the input image")
ap.add_argument("-c", "--clip", type=float, default=2.0,
	help="threshold for contrast limiting")
ap.add_argument("-t", "--tile", type=int, default=8,
	help="tile grid size -- divides image into tile x time cells")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Simple Equalization
equalized=cv2.equalizeHist(gray)
cv2.imshow("Original",image)
cv2.imshow("Histogram Equalization",equalized)
cv2.waitKey()
cv2.destroyAllWindows()

#Adaptive Equalization
'''
    We have two more command line arguments, one which is required, useful
    to tune and play with when experimenting with CLAHE:

    --clip: the threshold for contrast limiting. we'll typically want to 
    leave this value in the range of 2-5. If we set the value too large, then
    effectively, what we're doing is maximizing local contrast, which will, in turn
    maximize noise(which is opposite of what we want)

    --tile: the tile grid size for CLAHE. Conceptually, here we are dividing
    the input image into tile x tile cells and then applying histogram eqaulization
    to each cell.
'''
cv2.imshow("Original",image)
clahe=cv2.createCLAHE(clipLimit=args['clip'],tileGridSize=(args['tile'],args['tile']))
equalized=clahe.apply(gray)
cv2.imshow("Adaptive",equalized)
cv2.waitKey()
cv2.destroyAllWindows()