import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)


# address = 'https://192.168.198.105:8080/video'
# cap.open(address)


cap.set(3, 640)
cap.set(4, 480)

scanned = []

while True:
    success, img = cap.read()
    for barcode in decode(img):
        scanned.append(barcode.data)
    cv2.imshow("result", img)
    cv2.waitKey(1)

    print(scanned)
