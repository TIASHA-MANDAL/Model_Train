import shutil
import os

print("Enter the person u want to delete")
name=input()

isExist_train = os.path.exists("C:\\Users\\Model_trail\\ImagesAttendence"+"\\"+name+".jpg")

if(isExist_train==True ):
    print("Deleting....")
    os.remove("C:\\Users\\Model_trail\\ImagesAttendence"+"\\"+name+".jpg")
else:
    print("Person do not exist")