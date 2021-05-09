import cv2

# harcascades variables
haarcascade = r"./haarcascade_frontalface_default.xml"
model = cv2.CascadeClassifier(haarcascade)
# using a webcam

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# cap.set(10,0)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detecting faces
    faces = model.detectMultiScale(img)

    # drawing rectangles around detected faces
    for face in faces:
        x, y, w, h = face

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 3)

    cv2.imshow("WebCam", img)

    # quit on pressing q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
