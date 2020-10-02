import cv2 as cv
from random import randrange

# Load some pre-trained data on face frontals from OpenCV (Haar Cascade Algorithm)
trained_face_data = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces
# img = cv2.imread('Tom_Cruise.jpg')

# To capture video from webcam
webcam = cv.VideoCapture(0)

# Iterate forever over the frames
while True:

    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert to GrayScale
    grayscaled_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_image)

    # Highlight the faces using rectangles
    for (x, y, w, h) in face_coordinates:
        cv.rectangle(frame, (x,y), (x+w,y+h), (randrange(256),randrange(256),randrange(256)), 5)

    # Display the image with the faces
    cv.imshow('Face Detector', frame)
    key = cv.waitKey(1)

    # Stop when the Q key is pressed
    if key == 81 or key == 113:     # ASCII codes for Q and q
        break

# Release the Webcam VideoCapture object
webcam.release()

print('Code Completed')