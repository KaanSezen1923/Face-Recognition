import cv2 
import face_recognition
import pickle 
import numpy as np 
import pyttsx3 
import cvzone

cap=cv2.VideoCapture(0)

def audio(character_name):
    engine=pyttsx3.init()
    engine.say(f" Welcome {character_name}")
    engine.runAndWait()


print("Loading encoding file")
file=open("EncodeFile.p","rb")
encodeListKnowmwithNames=pickle.load(file)
file.close()
encodeListKnowm,characterNames=encodeListKnowmwithNames
print(characterNames)
print("Loaded encoding file")

while True:
    ret,frame=cap.read()
    imgS=cv2.resize(frame,(0,0),None,fx=0.25,fy=0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    faceCurFrame=face_recognition.face_locations(imgS)
    encodeCurFrame=face_recognition.face_encodings(imgS,faceCurFrame)


    for encodeface,faceloc in zip(encodeCurFrame,faceCurFrame):
        facedis=face_recognition.face_distance(encodeListKnowm,encodeface)
        print("facedis",facedis)
        matchIndex=np.argmin(facedis)
        if facedis[matchIndex] < 0.70:
            charactername=characterNames[matchIndex]
        else :
            charactername="Unknown"

        y1,x2,y2,x1=faceloc
        y1, x2, y2, x1=y1*4,x2*4,y2*4,x1*4
        bbox=x1,y1,x2-x1,y2-y1
        cvzone.cornerRect(frame,bbox)
        cvzone.putTextRect(frame,charactername,(x1, y1 - 15))
        audio(charactername)
    cv2.imshow("Face Recognition",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break 
    
cap.release()
cv2.destroyAllWindows()