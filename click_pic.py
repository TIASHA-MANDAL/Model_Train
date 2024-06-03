import cv2
import os 
import time
from PIL import Image
import numpy as np
import shutil

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
name=input("enter your name  ")

path= "C:\\Users\\Model_trail\\ImagesAttendence"
os.chdir(path) 
isExist = os.path.exists(name+'.jpg')

if(isExist==False):

    directory = name+""
    os.mkdir(directory)
    print("Directory '% s' created" % directory) 

    cam = cv2.VideoCapture(0)
    #cv2.namedWindow("Clicking Pic For training")

    img_counter = 0
    f=0
   
    while True:
        ret, frame = cam.read()

        if not ret:
            print("failed to grab frame")
            break
        #cv2.imshow("Clicking Pic For training", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            print("Escape hit, closing...")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y , w ,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0 , 0), 1)
            
            cv2.imshow('Clicking pic for training', frame)
            path2=path+'\\'+directory 
            os.chdir(path2)
            time.sleep(1)
            img_name = name+"({}).jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            faces = frame[y:y + h, x:x + w]
            #cv2.imshow("face",faces)
            cv2.imwrite(str(img_counter)+name+'.jpg', faces)
            os.remove(img_name)#<-
            if (img_counter==4):
                f=1
                break
        if(f==1):
            break

        #cv2.imwrite('n+str(counter)+".jpg"', img) 
    
    cam.release()
    cv2.destroyAllWindows()

   

    os.chdir(path+'\\'+directory)
    image1=cv2.imread("1"+name+".jpg")
    image2=cv2.imread("2"+name+".jpg")
    image3=cv2.imread("3"+name+".jpg")
    image4=cv2.imread("4"+name+".jpg")

    # make all the images of same size 
    #so we will use resize function
    image1=cv2.resize(image1,(400,400))
    image2=cv2.resize(image2,(400,400))
    image3=cv2.resize(image3,(400,400))
    image4=cv2.resize(image4,(400,400))

    
    Horizontal1=np.hstack([image1,image2])
    Horizontal2=np.hstack([image3,image4])

    # Now the horizontal attachment is done
    # noe vertical attachment
    Vertical_attachment=np.vstack([Horizontal1,Horizontal2])

    # Show the final attachment
    #cv2.imshow("Final Collage",Vertical_attachment)
    os.chdir(path)
    cv2.imwrite(name+'.jpg', Vertical_attachment)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    shutil.rmtree(path+'\\'+directory)

else:
    print("Person already exsits")
