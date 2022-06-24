import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("abss.jpg", 0)
#inverted = np.invert(image)
#cv2.imshow("orijinal", image )
#cv2.imshow("inverted", inverted  )

#negimage = 255- image

#cv2.imshow("negatıf", negimage)
#cv2.waitKey()

# img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(image, 99, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(image, 120, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3,2)
thresh3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3, 2)
#ret, thresh4 = cv2.threshold(image, 120, 255, cv2.THRESH_TOZERO)
#ret, thresh5 = cv2.threshold(image, 120, 255, cv2.THRESH_TOZERO_INV)
titles = ["orijinal Image", "global threshold = 90","adaptif ortalama  eşitleme ", "Adaptif gaussian eşitleme"]
image1 = [image,thresh1,thresh2,thresh3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(image1[i],'gray ')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
#cv2.imshow("binary thresh ", thresh1)
#cv2.imshow("binaryınv thresh ", thresh2)
#cv2.imshow("trunc thresh ", thresh3)
#cv2.imshow("tozero thresh ", thresh4)
#cv2.imshow("tozeroınv thresh ", thresh5)
#cv2.waitKey()


myResult = cv2.inRange(image, 100, 130)
cv2.imshow("eşikleme", myResult)
cv2.waitKey()