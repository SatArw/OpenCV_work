# OpenCV_basics

This is a repository containing all my work on OpenCV. 

So far, 

1. I have worked on face detection using [haar cascades](https://github.com/opencv/opencv/tree/4.x/data/haarcascades) that I found on the opencv github repository. I detected faces on a few of my images and screenshots of online meets to check the results and play around with the features. I attempted changing few parameters of the haar cascades like the minNeighbors parameter and studied the changes in face detection. 

2. Afterwards, I attempted to classify a few of mine, my brother's and my mother's images using the haar cascades and [LBPHFaceRecognizer](https://docs.opencv.org/4.x/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html).You can find the code in [Feature_train.py](https://github.com/SatArw/OpenCV_basics/blob/main/OpenCv/Feature_train.py) and [Recognize_this.py](https://github.com/SatArw/OpenCV_basics/blob/main/OpenCv/Recognize_this.py). The accuracy is not great, a maximum of 60%, this is mostly due to the small dataset I have used. 

3. I wrote a basic program to recognize the hand gestures using the standard 21 landmark points on the arm. I have used mediapipe and an instance of mediapipe.solutions.hands() to detect the hands and an instance of mediapipe.solutions.drawing_utils() to draw the points and connecting lines on the video frame where the hand is detected. The code is here, [Hand_gesture.py](https://github.com/SatArw/OpenCV_work/blob/main/OpenCv/Hand_gesture.py).

I will keep updating this repository as I accomplish more projects. 
