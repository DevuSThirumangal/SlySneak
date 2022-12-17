import cv2
import os
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
name = str(input("Name : "))
path = 'images/'+name
count = 0
while os.path.exists(path):
    print("name already exists")
    name = str(input("Enter name again: "))
    path = 'images/'+name
os.makedirs(path)
while True:
    ret,frame = video.read()
    faces = facedetect.detectMultiScale(frame,1.3,5)
    for x,y,w,h in faces:
        count = count+1
        nameloc = './images/'+name+'/'+str(count)+'.jpg'
        cv2.imwrite(nameloc, frame[y:y+h,x:x+h])
    cv2.imshow("WindowFrame",frame)
    cv2.waitKey(1)
    if count==100:
        break
video.release()
cv2.destroyAllWindows()
