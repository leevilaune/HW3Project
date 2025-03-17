import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
import framebuf

button = Pin(9, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

left_btn = Pin(9,Pin.IN,Pin.PULL_UP)
right_btn = Pin(7,Pin.IN,Pin.PULL_UP)
mid_btn = Pin(8,Pin.IN,Pin.PULL_UP)

#ex1 working
def ex1():
    index = 0
    ufo_str = "<=>"
    x=0
    while True:
        oled.fill(0)
        if(left_btn.value()==0 and x<=128-3*8):
            x+=1
        if(right_btn.value()==0 and x>=0):
            x-=1   
        oled.text(ufo_str,x,48,1)
        oled.show()

        index+=1

#ex2 working
def ex2():
    word_list = []
    screen_max_draw = 8
    y = 0

    while True:
        word = input("gib mir: ")
        word_list.append(word)

        oled.fill(0)
        y = 0

        for word in word_list[-screen_max_draw:]:
            oled.text(word, 0, y, 1)
            y += 8

        oled.show()

#ex3 working
def ex3():
    x=0
    y=32
    while True:
        x+=1
        if(x==128):
            x=0
        if(left_btn.value()==0):
            y+=1
        elif(right_btn.value()==0):
            y-=1
        elif(mid_btn.value()==0):
            oled.fill(0)
            x=0
            y=32
        oled.pixel(x,y,4)
        oled.show()
        time.sleep(0.05)
ex3()

