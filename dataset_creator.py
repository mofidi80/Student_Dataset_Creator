import cv2
import numpy as np
import sqlite3
import os

file_path = dir_path = os.path.dirname(os.path.realpath(__file__))
face_detect = cv2.CascadeClassifier(file_path + r"\haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)   #0 is for the webcam

def insert_or_update(Id, Name, age):    #function for sqlite database
    conn = sqlite3.connect(file_path + r"\face detection database.db")    #connect to databse
    cmd = "SELECT * FROM STUDENTS WHERE Id=" + str(Id)
    ###
    """to create the table mentioned above use the code below
    CREATE TABLE STUDENTS(
    Id INT,
    Name VARCHAR(20),
    age INT
    );"""
    ###
    cursor = conn.execute(cmd)  #cursor to execute statement(command=cmd)
    isRecordExist = False   #assume there is no record
    for row in cursor:
        isRecordExist = True
    if isRecordExist:   #if a record with the Id exists update name and age
        conn.execute("UPDATE STUDENTS SET Name=? WHERE Id=?", (Name,Id))
        conn.execute("UPDATE STUDENTS SET age=? WHERE Id=?", (age,Id))
    else:   #if a record with the Id does not exist create(insert)
        conn.execute("INSERT INTO STUDENTS(Id,Name,age) VALUES(?,?,?)", (Id,Name,age))
        
    conn.commit()
    conn.close()

#get user data
Id=input("Enter user Id: ")
Name=input('Enter user Name: ')
age=input("Enter user age: ")

insert_or_update(Id, Name, age)

sample_num = 0  #assume there is no sample in the dataset
while(True):
    ret, img = cam.read()   #open camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert image to grayscale, maybe instead of . it shoul be ,
    faces = face_detect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for x,y,width,height in faces:
        sample_num = sample_num + 1 #if face detected increments
        cv2.imwrite("dataset/user."+str(Id)+"."+str(sample_num)+".jpg", gray[y:y+height, x:x+width])
        cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)    #show green rectangle around face
        cv2.waitKey(100)    #delay time

    cv2.imshow("Face", img)
    cv2.waitKey(1)

    if sample_num > 1: #if dataset >1 : break the loop
        break

#quit:
cam.release()
cv2.destroyAllWindows()