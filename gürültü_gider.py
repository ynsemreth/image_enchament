import numpy as np
import matplotlib.pyplot as plt
import cv2

from utils import konvolusyon , median_filtreleme , gauss_kernel_olustur

photo = cv2.imread("./photos/ayrık6.jpg" , 0)

sigmalar = [ 1, 3 ,5 ]
gauss_cikis = []
for sigma in sigmalar:
    m = n = 6*sigma+1
    gauss_kernel = gauss_kernel_olustur(m , n , K=1 , sigma=sigma)
    gauss_cikis.append(konvolusyon(photo, gauss_kernel))

median_filtre_boyutları = [3,5 , 7]
medyan_cikis = []
for median_filtre_boyutu in median_filtre_boyutları:
    m = n = median_filtre_boyutu
    medyan_cikis.append(median_filtreleme(photo , m , n))

photo_len = (448,448)

first = np.hstack([cv2.resize(cikis , photo_len) for cikis in [photo , *gauss_cikis]])
second = np.hstack([cv2.resize(cikis , photo_len) for cikis in [photo , *medyan_cikis]])
pop = np.vstack((first,second))

plt.imshow(pop,cmap="gray")
plt.show()


