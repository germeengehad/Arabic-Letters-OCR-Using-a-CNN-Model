# Arabic Letters OCR Uing A CNN Model : Projct Overview
![Image](https://github.com/germeengehad/Arabic-Letters-OCR-Using-a-CNN-Model/blob/main/1_rYZoGtsO1HqsqX-UhlbXuA.png)
- This project aims to apply OCR to recognize Arabic letters using a CNN model trained on a collection of Arabic letter images. Additionally.

# Data Set
- Traditional OCR algorithms and techniques assume we’re working with a fixed font of some sort. In the early 1900s, that could have been the font used by microfilms.
In the 1970s, specialized fonts were explicitly developed for OCR algorithms, thereby making them more accurate. By the 2000s, we could use the fonts pre-installed on our computers to automatically generate training data and use these fonts to train our OCR models.
Each of these fonts had something in common:
i. They were engineered in some manner.
ii. There was a predictable and assumed space between each character (thereby making segmentation easier).
iii. The styles of the fonts were more conducive to OCR.
This Dataset Consist of Images of Arabic letters and numbers , but we will work on letters only

#  Data Augmentation And Data Preprossing
- Rescaling: Normalizes pixel values to the [0, 1] range.
- Rotation: Randomly rotates images by up to 10 degrees.
- Fill Mode: Fills in new pixels using the nearest pixel values.
- Featurewise Centering and Normalization: Normalizes images by centering them and scaling by standard deviation.
- Flipping: Randomly flips images vertically and horizontally.
- Shearing: Applies shear transformations with an intensity of 0.2.
- Zooming: Zooms in or out on images by 20%.
- Brightness Adjustment: Adjusts brightness to 40%-60% of the original.
- Validation Split: Reserves 30% of images for validation.
