# Keylogger
A keylogger that -<br>
1. Captures your input in any window
2. Save them to a file
3. Quits automatically on an exit signal
4. Saves load on CPU when special keys are pressed<br>


## Prerequisites
Pyxhook -><br>
`pip3 install pyxhook`<br>
Python-xlib -><br>
`pip3 install python-xlib`<br>


## Usage
Before running the program, set the <b>END SIGNAL</b> & <b>LOG FILE</b> path in line number 11 & 12 in keylogger.py<br>
Then you can either run it with -><br>
`python3 keylogger.py`<br>
Or if you want it in background -><br>
`nohup python3 keylogger.py`<br>
<br>
The temporary buffer is reset everytime, if it doesn't matches the end signal<br>
The script goes to sleep for 1 second when a special key is pressed (to reduce load on CPU)


## Screenshots
![image not found](img.png)


## Author name
#### Ritik Malik

