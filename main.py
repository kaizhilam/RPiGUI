from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(14)
led2 = LED(15)
led3 = LED(18)

root = Tk()
root.title("LED toggler")

myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

def ledToggle():
    if v.get() == "Off":
        led1.off()
        led2.off()
        led3.off()
    elif v.get() == "Red":
        led1.off()
        led2.off()
        led3.on()
    elif v.get() == "Green":
        led1.off()
        led2.on()
        led3.off()
    elif v.get() == "Blue":
        led1.on()
        led2.off()
        led3.off()


MODES = ["Red","Green","Blue","Off"]

v = StringVar()
v.set("Off")
for text in MODES:
    b = Radiobutton(root, text=text, variable=v, value=text, command = ledToggle)
    b.pack(anchor=W)

mainloop()

