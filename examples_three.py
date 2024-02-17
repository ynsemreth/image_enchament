import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from scipy.signal import correlate2d

def rescale(photo):
    S = photo.astype(np.float64)
    S -= S.min()
    S /= S.max()
    return S*255

photo = cv2.imread("./photos/12.jpg" , 0)

gauss_kernel = cv2.getGaussianKernel(ksize=19, sigma=3)
gauss_kernel = np.dot(gauss_kernel, gauss_kernel.T)

blur_photo = correlate2d(photo, gauss_kernel, mode="same")

mask = photo - blur_photo
mask = rescale(mask)

figure(figsize=(8, 10), dpi=160)

plt.subplot(2, 2, 1)
plt.imshow(photo, cmap="gray")
plt.title("Original Photo")

saved_image_paths = []

for k in [2,3,4,5,6]:
    sharpening_photo = photo + k * mask
    plt.subplot(3, 3, k + 2)
    plt.imshow(sharpening_photo, cmap="gray")
    plt.title(f"k = {k}")


    image_path = f'./photos/ayrık{k}.jpg'
    plt.imsave(image_path, sharpening_photo, cmap='gray')
    saved_image_paths.append(image_path)

mask_path = './photos/mask2.png'
plt.imsave(mask_path, mask, cmap='gray')
saved_image_paths.append(mask_path)

plt.show()