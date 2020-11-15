import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.png')

d = input("Please input diameter:\n")
sig_color = input("Please input Sigma Color:\n")
sig_space = input("Please input Sigma Space:\n")

cv2.imshow('input', img)
# Bilateral Filtering
out = cv2.bilateralFilter(img,int(d),int(sig_color),int(sig_space))
cv2.imshow('Bilateral Filter Output', out)
cv2.waitKey(0)
cv2.destroyAllWindows()

