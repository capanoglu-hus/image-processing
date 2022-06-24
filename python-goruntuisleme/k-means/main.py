import matplotlib as plt
import numpy as np
import cv2

path ='abss.jpg'

img =cv2.imread(path)
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
two0image = img.reshape((-1,3))
two0image = np.float32(two0image)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
K = 2
attempts=10
ret, label, center = cv2.kmeans(two0image, K, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))
cv2.imshow("orijinal",img)
cv2.imshow("k=2", result_image)
cv2.waitKey()