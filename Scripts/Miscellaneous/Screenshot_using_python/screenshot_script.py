import time
import cv2 
import numpy as np 
import pyautogui
   
print("Taking a screenshot in 3 seconds, navigate to desired screen...")  
time.sleep(3)

# taking a screenshot
image = pyautogui.screenshot() 
   
# pyautogui returns a PIL image in RGB format
# Convert it to BGR for saving
image = cv2.cvtColor(np.array(image), 
                     cv2.COLOR_RGB2BGR) 
   
# save image
cv2.imwrite("Screenshot.png", image) 