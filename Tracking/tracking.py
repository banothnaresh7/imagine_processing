import cv2

cap = cv2.VideoCapture(0)
#####Tracking#######
#tracker = cv2.TrackerKCF_create()
#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMIL_create()
tracker = cv2.TrackerMOSSE_create()
#tracker = cv2.TrackerCSRT_create()
#tracker = cv2.TrackerMedianFlow_create()

####################

##### TRACKER INITIALIZATION
success,img= cap.read()
bbox= cv2.selectROI("Tracking",img,False)
tracker.init(img,bbox)

def drawbbox(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,0,255),1)
    cv2.putText(img, "Tracking", (90, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

while(True):

    timer = cv2.getTickCount()
    success,img= cap.read()
    success,bbox= tracker.update(img)

    if success:
        drawbbox(img,bbox)
    else:
        cv2.putText(img, "LOST", (90, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer)
    if fps > 60:
        myColor = (20, 230, 20)
    elif fps > 20:
        myColor = (230, 20, 20)
    else:
        myColor = (20, 20, 230)

    cv2.putText(img,str(int(fps)),(90,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.imshow("Tracking", img)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
