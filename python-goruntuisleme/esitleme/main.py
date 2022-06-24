
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("abss.jpg", 0)
cv2.imshow("original", image )


#formülü ve dönüşümü ÖGREN

c = 1
log_image =c*np.log(1+image)
log_image = np.array(log_image, dtype = np.uint8)
cv2.imshow("logaritmik dönüşüm", log_image)
log_image = 255/(c*np.log(1+image))
log_image = np.array(log_image, dtype= np.uint8)
cv2.imshow("logaritmik dönüşüm 255", log_image)
cv2.waitKey()

#image = cv2.medianBlur(image, 0)


#ret, thresh1 = cv2.threshold(image, 99, 255, cv2.THRESH_BINARY)
#thresh2 = cv2.adaptiveThreshold(image, 120, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3,2)
#thresh3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3, 2)

#titles = ["orijinal Image", "global threshold = 90", "adaptif ortalama  eşitleme ", "Adaptif gaussian eşitleme"]
#image1 = [image,thresh1,thresh2,thresh3]
#for i in range(4):
    #plt.subplot(2,2,i+1),plt.imshow(image1[i],'gray ')
    #plt.title(titles[i])
    #plt.xticks([]), plt.yticks([])

#plt.show()

