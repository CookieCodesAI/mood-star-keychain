from machine import Pin, PWM
from time import sleep

red = PWM(Pin(23), freq=5000)
green = PWM(Pin(22),freq=5000)
blue = PWM(Pin(21),freq=5000)

color_change = Pin(18, Pin.IN, Pin.PULL_UP)
send = Pin(19, Pin.IN, Pin.PULL_UP)

colors = ["red","yellow","green","cyan","blue", "purple", "pink","white"]
curr = 0

def set_color(r,g,b):
    r_bit = int((r/255)*65535)
    b_bit = int((b/255)*65535)
    g_bit = int((g/255)*65535)
    
    red.duty_u16(r_bit)
    green.duty_u16(g_bit)
    blue.duty_u16(b_bit)
    

def display():
    print(colors[curr])
    if colors[curr] == "red":
        set_color(255,0,0)
    elif colors[curr] == "yellow":
        set_color(255,255,0)
    elif colors[curr] == "green":
        set_color(0,255,0)
    elif colors[curr] == "cyan":
        set_color(0,255,255)
    elif colors[curr] == "blue":
        set_color(0,0,255)
    elif colors[curr] == "pink":
        set_color(255,0,255)
    elif colors[curr] == "white":
        set_color(255,255,255)
    elif colors[curr] == "purple":
        set_color(111, 3, 252)

display()
while True:
    if color_change.value() == 0:
        if (curr == 6):
            curr= 0;
        else:
            curr+=1
        display()
    while color_change.value() == 0:
        pass

    
