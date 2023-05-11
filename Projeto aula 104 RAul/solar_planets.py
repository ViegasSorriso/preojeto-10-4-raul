import cv2

img = cv2.imread("solar-System.jpg")

rocket = img[120:360, 400:500]
img[0:240, 500:600] = rocket

text = "Eu amo programar na Byjus"
cv2.putText(img, "Sol", (100, 80), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL 2, fontScale=0.6, color = (0,0,255))

cv2.imshow("resultado", img)
cv2.waitKey(0)
