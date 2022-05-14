import cv2 as cv
import numpy as np
import os

haarClassifier = cv.CascadeClassifier("F:\Python Vscode\haarClassifier.xml")

# making a list of people (folders in the pics data)
people = ["Manas", "Namita", "Satwik"]
# Storing path of file as a string
DIR = r"F:\Python Vscode\Face_recognition_opencv\Pics_data"

labels = []
features = []


def create_train_set():  # Function to create the training set
    for person in people:
        # Accessing path of folder of each feature
        path = os.path.join(DIR, person)
        label = people.index(person)  # Creating label for this person (folder)

        for img in os.listdir(path):  # Accessing each pic in the folder
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Now we get the coordinates of detected face
            faces_rect = haarClassifier.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=20)

            # We input the part of image that has the face detexted into the features list
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

 # Function to call the training set prep function
create_train_set()
print("-------Training set prepared------")

# Converting feature lists to np arrays
features = np.array(features)
labels = np.array(labels)

print(f'Length of features = {len(features)}')
print(f"Length of labels = {len(labels)}")

# Insantiating the inbuilt opencv face recognizer
face_recogn = cv.face.LBPHFaceRecognizer_create()

# Training on our training set
face_recogn.train(features, labels)
print("-------Training done--------")


# Saving this as a yml file to be used later.
face_recogn.save('face_trained.yml')
np.save('feauture.npy', features)
np.save('labels.npy', labels)
print("Done")
