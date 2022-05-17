import cv2 as cv
import mediapipe as mp
import time

capture = cv.VideoCapture(0)

mpHands = mp.solutions.hands  # instantiating
hands = mpHands.Hands()
# used to draw lines on hand points (the 21 key points)
mpDraw = mp.solutions.drawing_utils

while True:
    isRead, img = capture.read()  # reading the frame
    img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # converting to RGB from BGR
    # Storing the results of hand detection in 'hands'
    results = hands.process(img_RGB)
    print(results.multi_hand_landmarks)
    cv.imshow("Frame", img)

    if results.multi_hand_landmarks:
        for hlms in results.multi_hand_landmarks:
            # mpDraw.draw_landmarks(img, hlms) #makrs the key points on the image
            # marks the key points and adds lines between them
            mpDraw.draw_landmarks(img, hlms, mpHands.HAND_CONNECTIONS)


cv.waitKey()
cv.destroyAllWindows()
