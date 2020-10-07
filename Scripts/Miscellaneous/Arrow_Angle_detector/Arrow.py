import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX
cap = cv2.VideoCapture(0)
cv2.namedWindow("Adjust") #Adjust help us to find the right threshold values for better accuracy using slider window.
cv2.createTrackbar("min","Adjust",110,255,nothing)

text = 'Left'
while True:
	ret ,frame = cap.read() #Reading each frame.
	frame = cv2.resize(frame, (640,480), interpolation=cv2.INTER_AREA)
	cropped = frame[100:400,100:500]
	cropped = cv2.flip(cropped,1)
	temp = cropped
	cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
	mi = cv2.getTrackbarPos("min","Adjust")

	_,threshold = cv2.threshold(cropped,mi,255,cv2.THRESH_BINARY)
	kernal = np.zeros([10,10],np.uint8)
	threshold = cv2.erode(threshold,kernal)
	contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours :
		area = cv2.contourArea(cnt)
		if area > 400 : #Selecting Contours only with area greater then 400
			approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
			approx_area = cv2.contourArea(approx)
			if(len(approx)==7): #As an arrow has seven edges, hence we are selecting the polygon with 7 edges
					n = approx.ravel()
					x1 = n[0] #First Co-ordinate always point to the topmost vertex
					y1 = n[1] 
					x2 = n[2]
					y2 = n[3]
					x3 = n[6]
					y3 = n[7]
					distance1 = (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2) 
					distance2 = (x1 - x3)*(x1 - x3) + (y1 - y3)*(y1 - y3)
					ratio = distance1/distance2 #Ratio will help us to determine the orientation or angle of the arrow
					if(2500<approx_area<25000 and (0.2<ratio<0.3 or ratio <0.1)):
						cv2.drawContours(temp,[approx],0,(0,0,255),5)

						x = approx.ravel()[0]
						y = approx.ravel()[1]
						
						if(0.2 < distance1/distance2 < 0.3): #Finding the tip of the arrow with the help of the ratios
							cv2.putText(temp,"Arrow tip",(x,y),font,0.5,(0,0,255))
							endx = (n[6]+n[8])/2
							endy = (n[7]+n[9])/2
							topx = x1
							topy = y1
							length = np.sqrt((topx-endx)*(topx-endx) + (topy-endy)*(topy-endy))
							y_v = endy-length
							if((topx-endx)==0):
								print(0)
							else:
								tan = (topy - y_v)/(topx - endx)
								print(np.arctan(tan)*57.3*2) #Basic cirle property to print the angles ( between 90 and -90)
							
						else :
							cv2.putText(temp,"Arrow end",(x,y),font,0.5,(0,0,255))
							if(distance1/distance2 <0.1):
								endx = (n[2]+n[0])/2
								endy = (n[3]+n[1])/2
								topx = n[8]
								topy = n[9]
								length = np.sqrt((topx-endx)*(topx-endx) + (topy-endy)*(topy-endy))
								y_v = endy - length
								if((topx-endx)==0):
									print(180)
								else:
									tan = (topy - y_v)/(topx - endx)
									print(np.arctan(tan)*57.3*2)
							else:
								topx = n[6]
								topy = n[7]
								endx = (n[12]+n[0])/2
								endy = (n[13]+n[1])/2
								length = np.sqrt((topx-endx)*(topx-endx) + (topy-endy)*(topy-endy))
								y_v = endy - length
								if((topx-endx)==0):
									print(180)
								else:
									tan = (topy - y_v)/(topx - endx)
									print(np.arctan(tan*57.3)*2)

	cv2.imshow('temp',temp)
	cv2.imshow('threshold',threshold)
	#print(text)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
