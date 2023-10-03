# IMPORTS

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# LOADING THE MODEL

model = load_model("detection_model.h5")


def face_extraction(frame):
    """Detect faces in a frame and extract them"""

    faces = cascade_model.detectMultiScale(frame, 1.1, 5)

    for x, y, w, h in faces:
        cropped_img = frame[y : y + h, x : x + w]

    return cropped_img


def image_processing(frame):
    """Preprocessing of the image for predictions"""

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (48, 48))
    frame = image.img_to_array(frame)
    frame = frame / 255
    frame = np.expand_dims(frame, axis=0)

    return frame


def detect_expressions(frame, detection_model):
    """Detect final expressions and return the predictions
    done by the detection_model"""

    cropped_frame = face_extraction(frame)

    test_frame = image_processing(cropped_frame)

    prediction = np.argmax(model.predict(test_frame), axis=-1)

    return prediction


# LOAD IMAGE

img = cv2.imread("./test_images/Swift2.jpg")


# LOADING HAAR CASCADE CLASSIFIER

cascade_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = cascade_model.detectMultiScale(img, 1.1, 10)


font = cv2.FONT_ITALIC
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    prediction = detect_expressions(img, model)

    if prediction == [0]:
        cv2.putText(img, "Angry", (x, y), font, 2, (0, 0, 255), 2)

    elif prediction == [1]:
        cv2.putText(img, "Happy", (x, y), font, 2, (0, 0, 255), 2)

    elif prediction == [2]:
        cv2.putText(img, "Sad", (x, y), font, 2, (0, 0, 255), 2)

    else:
        cv2.putText(img, "Surprised", (x, y), font, 2, (0, 0, 255), 2)

    cv2.imshow("img", img)


# Cleaning

cv2.waitKey(0)
cv2.destroyAllWindows()
