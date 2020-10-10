#!/usr/bin/env python
import pynput.keyboard

def key_press(key):
	print(key)

keyboard_listner = pynput.keyboard.Listener(on_press=key_press)
with keyboard_listner:
	keyboard_listner.join()
