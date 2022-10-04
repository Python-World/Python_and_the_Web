import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX
cap = cv2.VideoCapture(0)
cv2.namedWindow(
    "Adjust"
)  # Adjust help us to find the right threshold values for better accuracy using slider window.
cv2.createTrackbar("min", "Adjust", 110, 255, lambda x: None)


def distance(x1, x2, y1, y2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)


def terminate():
    cap.release()
    cv2.destroyAllWindows()


text = "Left"
while True:
    ret, frame = cap.read()  # Reading each frame.
    frame = cv2.resize(
        frame, (640, 480), interpolation=cv2.INTER_AREA
    )  # Resizing
    cropped = frame[100:400, 100:500]  # Cropping the frame
    cropped = cv2.flip(cropped, 1)  # Flipping the frame vertically
    temp = cropped  # Temp is our original image
    cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    mi = cv2.getTrackbarPos(
        "min", "Adjust"
    )  # Getting the values from the trackbar

    _, threshold = cv2.threshold(
        cropped, mi, 255, cv2.THRESH_BINARY
    )  # Converting image to binary (1's and 0's only)
    kernal = np.zeros(
        [10, 10], np.uint8
    )  # creating a square of 10X10 of zeroes
    threshold = cv2.erode(
        threshold, kernal
    )  # using this square to remove noise from the threshold
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )  # Finding contours or areas with same color

    for cnt in contours:  # iterating through each contour
        area = cv2.contourArea(cnt)
        if area > 400:  # Selecting Contours only with area greater then 400
            approx = cv2.approxPolyDP(
                cnt, 0.01 * cv2.arcLength(cnt, True), True
            )  # Reducing the number of edges/vertices or approximating the contour
            approx_area = cv2.contourArea(approx)
            if (
                len(approx) == 7
            ):  # As an arrow has seven edges, hence we are selecting the polygon with 7 edges
                n = approx.ravel()  # Converts 2d array into 1d array
                x1 = n[
                    0
                ]  # First Co-ordinate always point to the topmost vertex
                y1 = n[1]
                x2 = n[2]
                y2 = n[3]
                x3 = n[6]
                y3 = n[7]
                distance1 = distance(x1, x2, y1, y2)
                distance2 = distance(x1, x3, y1, y3)
                ratio = (
                    distance1 / distance2
                )  # Ratio will help us to determine the orientation or angle of the arrow
                if 2500 < approx_area < 25000 and (
                    0.2 < ratio < 0.3 or ratio < 0.1
                ):
                    cv2.drawContours(
                        temp, [approx], 0, (0, 0, 255), 5
                    )  # Outlining the detected arrow with red color

                    x = approx.ravel()[
                        0
                    ]  # x co-ordinate of the top-most vertex (could be the tip or the end of the arrow)
                    y = approx.ravel()[
                        1
                    ]  # y co-ordinate of the top-most vertex (could be the tip or the end of the arrow)

                    if (
                        0.2 < distance1 / distance2 < 0.3
                    ):  # Finding the tip of the arrow with the help of the ratios of the distances
                        cv2.putText(
                            temp, "Arrow tip", (x, y), font, 0.5, (0, 0, 255)
                        )
                        topx = x1
                        topy = y1
                        endx = (n[6] + n[8]) / 2
                        endy = (n[7] + n[9]) / 2
                        length = np.sqrt(distance(topx, endx, topy, endy))
                        y_v = endy - length
                        if (topx - endx) == 0:  # Denominator becomes zero
                            print(0)
                        else:
                            tan = (topy - y_v) / (topx - endx)
                            print(
                                np.arctan(tan) * 57.3 * 2
                            )  # Basic cirle property to print the angles ( between 90 and -90)

                    else:
                        cv2.putText(
                            temp, "Arrow end", (x, y), font, 0.5, (0, 0, 255)
                        )
                        if distance1 / distance2 < 0.1:
                            topx = n[8]
                            topy = n[9]
                            endx = (n[2] + n[0]) / 2
                            endy = (n[3] + n[1]) / 2
                            length = np.sqrt(distance(topx, endx, topy, endy))
                            y_v = endy - length
                            if (topx - endx) == 0:  # Denominator becomes zero
                                print(180)
                            else:
                                tan = (topy - y_v) / (topx - endx)
                                print(np.arctan(tan) * 57.3 * 2)
                        else:
                            topx = n[6]
                            topy = n[7]
                            endx = (n[12] + n[0]) / 2
                            endy = (n[13] + n[1]) / 2
                            length = np.sqrt(distance(topx, endx, topy, endy))
                            y_v = endy - length
                            if (topx - endx) == 0:  # Denominator becomes zero
                                print(180)
                            else:
                                tan = (topy - y_v) / (topx - endx)
                                print(np.arctan(tan * 57.3) * 2)

    cv2.imshow("temp", temp)  # Displaying original image
    cv2.imshow("threshold", threshold)  # Displaying threshold image
    if cv2.waitKey(1) & 0xFF == ord(
        "q"
    ):  # Program will quite when q is pressed
        break
terminate()
