import argparse
import cv2
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,default="./wallpaper/car.png",help="Path to the input Image")
args=vars(ap.parse_args())
image=cv2.imread(args['image'])
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
means = []
stds = []

for channel in range(image_rgb.shape[2]):
    mean, std = cv2.meanStdDev(image_rgb[:, :, channel])
    means.append(mean[0][0])
    stds.append(std[0][0])

# Normalize each channel
normalized_img = np.zeros(image_rgb.shape, dtype=np.float32)
for channel in range(image_rgb.shape[2]):
    normalized_img[:, :, channel] = (image_rgb[:, :, channel] - means[channel]) / stds[channel]

# Clip the values to be in the range [0, 1]
normalized_img = np.clip(normalized_img, 0, 1)

# Convert back to uint8
normalized_img = (normalized_img * 255).astype(np.uint8)
cv2.imshow("Original",image_rgb)
cv2.imshow("Normalized",normalized_img)

cv2.waitKey()
cv2.destroyAllWindows()