import cv2
import numpy as np
import albumentations as A
from albumentations import (HorizontalFlip, Rotate, RandomCrop, Resize, RandomBrightnessContrast,
                            RandomGamma, HueSaturationValue, GaussNoise, Blur, ElasticTransform,
                            RandomGridShuffle, ShiftScaleRotate)
from albumentations.pytorch import ToTensorV2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('path_to_your_image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define augmentation pipeline
transform = A.Compose([
    HorizontalFlip(p=0.5),
    Rotate(limit=45, p=0.5),
    RandomCrop(height=200, width=200, p=0.5),
    Resize(height=224, width=224, p=1.0),
    RandomBrightnessContrast(p=0.5),
    RandomGamma(p=0.5),
    HueSaturationValue(p=0.5),
    GaussNoise(p=0.5),
    Blur(blur_limit=3, p=0.5),
    ElasticTransform(p=0.5),
    ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.1, rotate_limit=45, p=0.5),
])

# Apply transformations
augmented_image = transform(image=image)['image']

# Display the original and augmented images
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(image)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(augmented_image)
ax[1].set_title('Augmented Image')
ax[1].axis('off')

plt.show()
