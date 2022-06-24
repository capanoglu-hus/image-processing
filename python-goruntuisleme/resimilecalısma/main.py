import cv2
import numpy as np

image = cv2.imread("abss.jpg",0)

x_filtre = np.array([[-1, -1, -1,], [0, 0, 0], [1, 1, 1]])
y_filtre = np.array([[-1, 0, 1,], [-1, 0, 1], [-1, 0, 1]])

image_x = cv2.filter2D(image, -1, x_filtre)
image_y = cv2.filter2D(image, -1, y_filtre)


laplace = cv2.Laplacian(image, cv2.CV_16S, ksize=5)
laplace2 = cv2.Laplacian(image, cv2.CV_32F)

cv2.imshow('orijinal', image)
cv2.imshow('yatay yön', image_x)
cv2.imshow('dikey yön', image_y)

cv2.imshow('laplace ', laplace)
cv2.imshow('laplace2', laplace2)
cv2.waitKey(0)

ret,esik_image= cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)

kernel = np.ones((2,2),dtype=np.uint8)

erode_result = cv2.erode(esik_image,kernel,iterations=1)

cv2.imshow("eşikleme giriş görüntüsü",esik_image)
cv2.imshow("erozyon",erode_result)

cv2.waitKey()
