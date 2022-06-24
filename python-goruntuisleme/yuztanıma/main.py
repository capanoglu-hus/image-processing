import cv2
import numpy as np

image= cv2.imread("happy-kids-1.jpg")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for gama in [2,3]:
    gama_corrected = np.array(255 * (image_gray / 255 ) ** gama, dtype='uint8')
    cv2.imshow("gama", gama_corrected)
    cv2.waitKey()

face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

yuzler = face_cascade.detectMultiScale(image_gray)

print("görüntüdeki yüz sayısı= ", f"{len(yuzler)}")

for x, y, width, height in yuzler:
    cv2.rectangle(image, (x,y ), (x+ width, y+ height), color=(0, 0, 255),thickness=2)
    cv2.imshow("sonuc",image)
cv2.waitKey()
#tuz biber gürültüsü ekleyip onun üzerinde yüz bul haarcascade metotlarına bak