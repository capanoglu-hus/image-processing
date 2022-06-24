import cv2
import numpy as np

img = cv2.imread("abss.jpg")

for gama in [0.1, 0.5, 1.2, 2.2]:
    gama_corrected = np.array(255 * (img / 255 ) ** gama, dtype='uint8')
    cv2.imshow("gama", gama_corrected)
    cv2.waitKey()

#filtreler
blur_filter1 = np.ones((3, 3), np.float64)/(9.0)
blur_filter2 = np.ones((8, 8), np.float64)/(9.0)
blur_filter3 = np.ones((12, 12), np.float64)/(9.0)

img_blur1 = cv2.filter2D(img, -1, blur_filter1)

img_blur2 = cv2.filter2D(img, -1, blur_filter2)

img_blur3 = cv2.filter2D(img, -1, blur_filter3)

cv2.imshow("abss", img)
cv2.imshow("abss1", img_blur1)
cv2.imshow("abss2", img_blur2)
cv2.imshow("abss3", img_blur3)

cv2.waitKey()


gaussian_blur = cv2.GaussianBlur(img, (15, 15), 0)         #boyut büyüynce bulanıklaşma artıyor

median_filtre = cv2.medianBlur(img, 5)
cv2.imshow("orijinal ", img)
cv2.imshow("gaussian filtre sonucu ", gaussian_blur)
cv2.imshow("medyan filtre", median_filtre)
cv2.waitKey()
