import cv2
import matplotlib.pyplot as plt
import numpy as np


foto = cv2.imread("842542.jpg")
cv2.imshow("resim", foto)
B = foto[:, :, 0]
G = foto[:, :, 1]
R = foto[:, :, 2]
cv2.imshow("resimmavi", B)
cv2.imshow("resimyeşil", G)
cv2.imshow("resimKIRMIZI", R)
cv2.waitKey()
print(foto.shape)
print(R.shape)

x = 45
y = 46
kanal =0
yogunluk_rgb = foto[y, x, kanal]
print("yogunluk ", yogunluk_rgb)
yogunluk_r = R[y, x]
print("yogunlukgray", yogunluk_r)
print("merhaba")


renkli = cv2.imread("842542.jpg")
gri = cv2.imread("842542.jpg", 0 )

hist_color = cv2.calcHist([renkli], [0], None,[256], [0,256])
hist_gray = cv2.calcHist([gri], [0], None , [256], [0,256])

plt.figure(1)
plt.plot(hist_color)

plt.figure(2)
plt.plot(hist_gray)
#plt.show()

B = renkli[:, :, 0]
hist_B=cv2.calcHist([B], [0], None, [256], [0,256])
print(np.sum(hist_B))
plt.plot(hist_B)
#plt.show()

CM = (np.max(gri) - np.min(gri))/(np.max(gri) + np.min(gri))
yeni = CM * gri
plt.imshow(yeni, cmap = 'gray')
plt.show()