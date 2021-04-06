import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while(True):

    successs, img = cap.read()
    for barcode in decode(img):
        mydata = barcode.data.decode('utf-8')
        print(mydata)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(img,[pts],True,(0,0,255),1)
        pts2 = barcode.rect
        cv2.putText(img,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)
    cv2.imshow("result", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()