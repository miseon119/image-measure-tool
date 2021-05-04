import cv2
import numpy as np
from skimage.measure import compare_ssim

src2 = cv2.imread("sample2.jpg")
src = cv2.imread("sample3.jpg")

gray1 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)

crop1 = cv2.medianBlur(gray1,5)
crop2 = cv2.medianBlur(gray2,5)

score = compare_ssim(crop1, crop2, gaussian_weights=True, full=False)
# (score, diff) = compare_ssim(gray1, gray2, full=False)

print("score = ",score)
