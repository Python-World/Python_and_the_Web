import cv2
import numpy as np


# Define ROI
def roi(image, vertices):
    mask = np.zeros_like(image)
    mask_color = 255
    cv2.fillPoly(mask, vertices, mask_color)
    masked_img = cv2.bitwise_and(image, mask)
    return masked_img


# Draw Hough Lines on image
def draw_lines(lines, image):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return image


# Preprocess the frames for detections
def process(img):
    try:
        # Define roi vertices
        h, w, _ = img.shape
        roi_vertices = [(200, h), (w / 2, 2 * h / 3), (w - 100, h)]

        # Convert to GRAYSCALE
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply dilation (morphology)
        kernel = np.ones((3, 3), np.uint8)
        gray_img = cv2.dilate(gray_img, kernel=kernel)

        # Canny edge detection
        canny = cv2.Canny(gray_img, 60, 255)

        # ROI
        roi_image = roi(canny, np.array([roi_vertices], np.int32))

        # Hough Lines
        hough_lines = cv2.HoughLinesP(
            roi_image, 1, np.pi / 180, 40, minLineLength=10, maxLineGap=5
        )
        final_img = draw_lines(hough_lines, img)
        return final_img

    except Exception:
        return img


# Capture the video file
cap = cv2.VideoCapture("./Data/Manhattan_Trim.mp4")

# PropIDs of the video frame
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# FourCC Codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
saved_frame = cv2.VideoWriter(
    "Manhattan_detection.avi", fourcc, 30.0, (frame_width, frame_height)
)


while cap.isOpened():
    _, frame = cap.read()

    try:
        frame = process(frame)
        saved_frame.write(frame)
        cv2.imshow("final", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    except Exception:
        break


cap.release()
saved_frame.release()
cv2.destroyAllWindows()
