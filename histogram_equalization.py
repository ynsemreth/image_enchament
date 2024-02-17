import cv2
import matplotlib.pyplot as plt
import numpy as np



def cv2_main():
    foto = cv2.imread("./photos/unnamed (2).jpg", 0)
    hist_es_foto = cv2.equalizeHist(foto)

    yanyana = np.hstack((foto, hist_es_foto))

    plt.imshow(yanyana, cmap="gray")
    plt.show()


def fotografin_histogramini_olustur(foto, L):
    histogram, bins = np.histogram(foto, bins=L, range=(0, L))
    return histogram


def normallestirilmis_histogram_olustur(foto, L):
    histogram = fotografin_histogramini_olustur(foto, L)
    return histogram / foto.size


def kumulatif_dagilimi_olustur(p_r_r):
    return np.cumsum(p_r_r)


def histogram_esitleme(foto, L):
    p_r_r = normallestirilmis_histogram_olustur(foto, L)
    kumulatif_dagilim = kumulatif_dagilimi_olustur(p_r_r)
    donusum_fonksiyonu = (L-1) * kumulatif_dagilim
    shape = foto.shape
    ravel = foto.ravel() # (800x600) -> 480000
    hist_es_foto = np.zeros_like(ravel)
    for i, pixel in enumerate(ravel):
        hist_es_foto[i] = donusum_fonksiyonu[pixel]
    return hist_es_foto.reshape(shape).astype(np.uint8)


def main():
    L = 2**8
    acik = cv2.imread("./photos/ayrık6.jpg", 0)

    hist_es_acik = histogram_esitleme(acik, L)
    yanyana_acik = np.hstack((acik, hist_es_acik))

    grid = np.vstack((yanyana_acik))

    plt.imshow(grid, cmap="gray")
    plt.show()

    cv2.imwrite("./photos/yeni_islemci.jpg" , hist_es_acik)

if __name__ == "__main__":
    # cv2_main()
    main()