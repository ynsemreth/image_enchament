import numpy as np
import cv2
import matplotlib.pyplot as plt

def stack(*args):
    return np.hstack(args)

def negative(photo):
    L = np.max(photo)
    negative_photo = L - photo
    return negative_photo

def rescale(photo):
    s = photo.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)

def log_transformation(r,c):  # s = c.log(1+r)
    r = r.astype(float)
    s = c*np.log(1+r)
    s = rescale(s)
    return s

def gamma_transformation(r,c,gamma):
    r = r.astype(float)
    s = c*r**gamma # s = c.r**gamma
    s = rescale(s)
    return s
def main():

    image = cv2.imread("./photos/fourier_spectrum.tif" , 0)
    image_gamma = cv2.imread("./photos/fourier_spectrum.tif" , 0)
    negative_image = negative(image)
    image_log = log_transformation(image , c=1)
    neighboor_image = stack(image,negative_image)

    gamma_force = [3, 4, 5]
    force_transform = []
    for gamma in gamma_force:
        force = gamma_transformation(image_gamma , c=1 , gamma=gamma)
        force_transform.append(force)

    vertical_1 = stack(image_gamma , force_transform[0])
    vertical_2 = stack(*force_transform[1:])
    grid = np.vstack((vertical_1,vertical_2))
    plt.imshow(grid , cmap="gray")
    plt.show()

if __name__ == "__main__":
    main()
