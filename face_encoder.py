import cv2
import face_recognition
import pickle
import os

folderPath = "Data"
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
characterNames = []
for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    imgList.append(img)
    characterNames.append(os.path.splitext(path)[0])
print(characterNames)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        print(f"Image shape: {img.shape}")
        
        face_locations = face_recognition.face_locations(img)
        print(f"Face locations: {face_locations}")
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encode Started ...")
encodeListKnowm = findEncodings(imgList)
encodeListKnowmwithNames = [encodeListKnowm, characterNames]
print(encodeListKnowmwithNames)
print("Encoding completed.")

file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnowmwithNames, file)
file.close()
print("File saved")