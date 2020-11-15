import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image_Lena512rgb.png')
b,g,r = cv2.split(img)

value = input("Please input channel(r / g / b):\n")

if value == 'r':
    hist, bins = np.histogram(r.flatten(), 256, [0, 256])
    plt.hist(r.flatten(), 256, [0, 256], color='r')
    equ = cv2.equalizeHist(r)
elif value == 'g':
    hist, bins = np.histogram(g.flatten(), 256, [0, 256])
    plt.hist(g.flatten(), 256, [0, 256], color='g')
    equ = cv2.equalizeHist(g)
elif value == 'b':
    hist, bins = np.histogram(b.flatten(), 256, [0, 256])
    plt.hist(b.flatten(), 256, [0, 256], color='b')
    equ = cv2.equalizeHist(b)
else:
    print('Entered wrong values')

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')


cv2.imshow('input', img)
cv2.imshow('Equalization channel output', equ)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
