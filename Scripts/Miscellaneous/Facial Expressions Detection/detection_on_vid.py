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


# LOADING HAAR CASCADE CLASSIFIER

cascade_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# CAPTURE VIDEO (ON WEBCAM)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()

    try:
        faces = cascade_model.detectMultiScale(
            frame, 1.1, 5
        )  # Detect faces in a frame

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            prediction = detect_expressions(frame, model)

            font = cv2.FONT_ITALIC

            if prediction == [0]:
                cv2.putText(frame, "Angry", (x, y), font, 1, (0, 0, 255), 2)

            elif prediction == [1]:
                cv2.putText(frame, "Happy", (x, y), font, 1, (0, 0, 255), 2)

            elif prediction == [2]:
                cv2.putText(frame, "Sad", (x, y), font, 1, (0, 0, 255), 2)

            else:
                cv2.putText(
                    frame, "Surprised", (x, y), font, 1, (0, 0, 255), 2
                )

            cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    except Exception:
        break


# Cleaning
cap.release()
cv2.destroyAllWindows()
