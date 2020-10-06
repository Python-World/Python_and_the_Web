import cv2
import numpy as np

cap = cv2.VideoCapture("./Data/cars.avi")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"XVID")
saved_frame = cv2.VideoWriter("car_detection.avi", fourcc, 20.0, (frame_width, frame_height))

model = cv2.CascadeClassifier("haarcascade_car.xml")

while cap.isOpened():
    _, frame = cap.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = model.detectMultiScale(gray_frame, 1.1, 2)

    for x, y, w, h in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    saved_frame.write(frame)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
saved_frame.release()
cv2.destroyAllWindows()



