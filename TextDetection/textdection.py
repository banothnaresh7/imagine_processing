import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('C:\\Users\\Naresh\\Pictures\\Screenshots\\Screenshot (8).png')
#img = cv2.imread('color.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

"""
#print(pytesseract.image_to_string(img))



###Detecting characters

hImg, wImg, _ = img.shape    # it img.shape gives us the number of rows and colu and color
boxes= pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),3)  #cv2.rectangle(img,start_pt,end_pt,color,thickness)
    cv2.putText(img, b[0], (x, hImg-y+40), 1,cv2.FONT_HERSHEY_COMPLEX, (50, 50, 255), 3)

"""
### Detecting words
hImg,wImg,_= img.shape

#cong = r'--oem 3 --psm 6 outputbase digits'
boxes= pytesseract.image_to_data(img)
"""
boxes contains a list of values like linenum,pagenum,block num, text and many
of 12 values  and at 0 pos we get this information
"""
prevBlock_num = 0
for x,b in enumerate(boxes.splitlines()):
    print(b)
    if x!= 0:
        b= b.split()
        if len(b)== 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]),int (b[9])
            cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255),2)
            #cv2.putText(img, b[11], (x,y), 1, cv2.FONT_HERSHEY_COMPLEX, (50,50,255),2)
            with open('C:/Users/Naresh/Desktop/text/append.txt','a') as f:
                if prevBlock_num == b[2]:
                    f.writelines(f' {b[11]}')
                else:
                    f.writelines(f'\n{b[11]}')
                    prevBlock_num = b[2]



###resize of window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',800,800)

cv2.imshow("image",img)
cv2.waitKey(0)