# Imports
import cv2

# Read image
img = cv2.imread("./Data/test_img.jpg")

# Convert to Grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the model and make the detections
model = cv2.CascadeClassifier("haarcascade_car.xml")
cars = model.detectMultiScale(img_gray, 1.1, 2)

# Draw rectangles
for x, y, w, h in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#  Show the results
cv2.imshow("image", img)
cv2.imwrite("car_detection.jpg", img)

# Cleaning
cv2.waitKey(0)
cv2.destroyAllWindows()
