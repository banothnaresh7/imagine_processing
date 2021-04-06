import cv2

path = 'E:/python codes/textdection/haarcascade_frontalface_default.xml'
objectName= 'FACE'

def empty(a):
    pass

cv2.namedWindow("Result")
cv2.resizeWindow("Result",640,580)

#Trackbar

"""
cv2.createTrackbar("scale", "Result", 400, 1000,empty)
cv2.createTrackbar("neig", "Result", 5, 50,empty)
cv2.createTrackbar("min", "Result", 0, 100250,empty)
"""
cascade = cv2.CascadeClassifier(path)

#Image Reading
img = cv2.imread("C:\\Users\\Naresh\\Pictures\\Camera Roll\\1580913321992.jpg")
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


while(True):
    #DETECT THE FACE

    #scaleval = cv2.getTrackbarPos("scale","Result")
    #neigh = cv2.getTrackbarPos("neig", "Result")
    objects = cascade.detectMultiScale(imggray)
    print(objects)

    #Drawing Rectangle
    for (x,y,w,h) in objects:
        area= w*h
        minarea= cv2.getTrackbarPos("min","Result")
        minarea=0
        if area>minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
            cv2.putText(img,objectName,(x,y-5),1,cv2.FONT_HERSHEY_SIMPLEX,(0,0,255),3)
            roi_color = img[y:y + h, x:x + w]
    cv2.imshow("Result", img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

