from turtle import Turtle
from gpiozero import Button, MotionSensor
from time import sleep
gary = Turtle(shape = 'turtle')
ms = MotionSensor('BOARD16', queue_len = 1, threshold = .7)
up = Button('BOARD37')
down = Button('BOARD33')
left = Button('BOARD22')
right = Button('BOARD35')
while not down.is_pressed:
    if up.is_pressed:
        gary.forward(10)
    elif left.is_pressed:
        gary.left(90)
    elif right.is_pressed:
        gary.right(90)
    if ms.motion_detected:
        gary.clear()
    sleep(.2)
