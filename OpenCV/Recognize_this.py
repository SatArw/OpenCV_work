import cv2 as cv
import numpy as np

haarClassifier = cv.CascadeClassifier(
    "F:\Python Vscode\haarClassifier.xml")  # Loading the haar face detector

people = ["Manas", "Namita", "Satwik"]
# features = np.load('features.npy')
# labels = np.load('labels.npy')

# Instantiating the face recognizer
face_recogn = cv.face.LBPHFaceRecognizer_create()
# read the yml file we saved during training the model
face_recogn.read(
    "F:\\Python Vscode\\Face_recognition_opencv\\face_trained.yml")

img = cv.imread(
    "D:\\Users\SatArw\Downloads\WhatsApp Image 2022-05-12 at 1.29.29 PM (1).jpeg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces_rect = haarClassifier.detectMultiScale(gray, 1.1, 20)

for(x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]  # identify the roi in test image

    label, confidence = face_recogn.predict(
        faces_roi)  # Recognize the face in roi
    print(f'Label = {people[label]} with a cofidence of {confidence}')

    # cv.putText(img, str(people[label]), (20, 20),
    #            cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected faces', img)

cv.waitKey(0)
