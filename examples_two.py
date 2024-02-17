import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from scipy.signal import correlate2d

matplotlib.rcParams["figure.figsize"] = (8,10)
def rescale(photo):
    S = photo.astype(np.float64)
    S -= S.min()
    S /= S.max()
    return S*255

photo = cv2.imread("./photos/ayrık6.jpg" , 0)

kernel1 = np.array([
    [0 , -1 , 0],
    [-1 , 8, -1],
    [0 , -1 , 0]
])
kernel2 = np.array([
    [-2 , 1, -2],
    [-3 , 8, -3],
    [-2 , 1, -2]
])

kernel1_filter = correlate2d(photo , kernel1 , mode="same")
kernel2_filter = correlate2d(photo , kernel2, mode="same")

figure(figsize=(8,10) , dpi = 160)

kernel1_filter = rescale(kernel1_filter)
kernel2_filter = rescale(kernel2_filter)

sharpening_photo = photo + kernel1_filter
sharpening_photo1 = photo + kernel2_filter

plt.subplot(2,2,1)
plt.imshow(photo , cmap="gray")
plt.title("Original Photo")

plt.subplot(2,2,2)
plt.imshow(sharpening_photo , cmap="gray")
plt.title("4")

plt.subplot(2,2,3)
plt.imshow(sharpening_photo1 , cmap="gray")
plt.title("8")

plt.show()