from pynput import keyboard
from termcolor import colored

import time
import os
import board
import subprocess as sp
import socket

import RPi.GPIO as GPIO
from adafruit_motorkit import MotorKit



kit = MotorKit(i2c=board.I2C())

servoPIN1 = 6
servoPIN2 = 5
GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)

m1 = GPIO.PWM(servoPIN1, 50) 
m1.start(2.5) 
m2 = GPIO.PWM(servoPIN2, 50) 
m2.start(2.5) 

GPIO_TRIGGER = 23
GPIO_ECHO = 22
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.5)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance

def press_w():
    m1.ChangeDutyCycle(5)
    m2.ChangeDutyCycle(10)

def press_s():
    m1.ChangeDutyCycle(10)
    m2.ChangeDutyCycle(5)

def press_a():
    m1.ChangeDutyCycle(5)
    m2.ChangeDutyCycle(5)
    

def press_d():
    m1.ChangeDutyCycle(10)
    m2.ChangeDutyCycle(10)
    
def press_q(): 
    m1.ChangeDutyCycle(0)
    m2.ChangeDutyCycle(0)
    
def press_e():
    m1.ChangeDutyCycle(5)
    m2.ChangeDutyCycle(10)
    while True:
        d=distance()
        if d<50:
            if d<5:
                return
            m1.ChangeDutyCycle(10)
            m2.ChangeDutyCycle(10)
            print("Objeto encontrado a menos de 35cm")
            time.sleep(1)
            m1.ChangeDutyCycle(5)
            m2.ChangeDutyCycle(10)
            


if __name__=='__main__':
    order=input(colored("Do you want to build a webpage to control(Y/N)?\n","blue"))

    if order=='Y' or order =='y':
        print(colored("Starting webpage","blue"))

        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(),1234))
        
        '''Only Linux:'''
        os.system( 'python3 web_app.py &')
        
        print(colored("HTTP Server started on port 5000","cyan"))
        
        prev=None
        while True:
            s.listen(1)
            client_socket,adress=s.accept()
            val=client_socket.recv(100)
            val=val.decode("utf-8")

            if val=='e':
                if val!=prev:
                    print( colored("Pressed: Auto","cyan") )
                    prev=val
                # press_e()
            if val=='a':
                if val!=prev:
                    print( colored("Pressed: A","cyan") )
                    prev=val
                # press_a()
            if val=='s':
                if val!=prev:
                    print( colored("Pressed: S","cyan") )
                    prev=val
                # press_s()
            if val=='d':
                if val!=prev:
                    print( colored("Pressed: D","cyan") )
                    prev=val
                # press_d()
            if val=='w':
                if val!=prev:
                    print( colored("Pressed: W","cyan") )
                    prev=val
                # press_w()
    else:
        print(colored("Controling by keyboard","blue"))
        hotkeys = { 'w': press_w ,'s': press_s,'a': press_a,'d': press_d,'e': press_e,'q': press_q}

        with keyboard.GlobalHotKeys(hotkeys) as escuchador:
            print(colored("Starting...","green"))
            escuchador.join()
                


