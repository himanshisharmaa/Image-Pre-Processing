# Image-Pre-Processing

# Image Pre-Processing Toolkit

This repository contains a collection of Python scripts that demonstrate **common image preprocessing techniques** used in computer vision and deep learning pipelines. These techniques help enhance image quality, remove noise, and prepare data for better model training and analysis.

---

## What is Image Preprocessing?

**Image preprocessing** refers to the set of techniques applied to raw image data to improve its quality and make it suitable for downstream tasks like object detection, classification, or segmentation. These operations include:
- Removing noise
- Standardizing pixel values
- Enhancing features (like edges)
- Augmenting data to improve model robustness

---

## Folder Structure

| File                      | Description                              |
|---------------------------|------------------------------------------|
| `gray_scale_conversion.py` | Converts RGB images to grayscale         |
| `edge_detection.py`        | Applies edge detection (Sobel, Canny)    |
| `denoising.py`             | Removes noise using filtering methods    |
| `colorSpace.py`            | Converts between different color spaces  |
| `data_augmentation.py`     | Applies random flips, rotations, etc.    |
| `data_augmentation2.py`    | Additional augmentation techniques       |

---

## 🔧 Requirements

Make sure you have Python 3.6+ and the following libraries:

```bash
pip install opencv-python numpy matplotlib
