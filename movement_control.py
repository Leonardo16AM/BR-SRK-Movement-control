# from pynput import keyboard
# import RPi.GPIO as GPIO
import termcolor
import time
# import board
# from adafruit_motorkit import MotorKit
import subprocess as sp

# kit = MotorKit(i2c=board.I2C())

# servoPIN1 = 6
# servoPIN2 = 5
# GPIO.setmode(GPIO.BCM)

# GPIO.setup(servoPIN1, GPIO.OUT)
# GPIO.setup(servoPIN2, GPIO.OUT)

# m1 = GPIO.PWM(servoPIN1, 50) 
# m1.start(2.5) 
# m2 = GPIO.PWM(servoPIN2, 50) 
# m2.start(2.5) 

# GPIO_TRIGGER = 23
# GPIO_ECHO = 22
# GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
# GPIO.setup(GPIO_ECHO, GPIO.IN)


# def distance():
#     GPIO.output(GPIO_TRIGGER, True)
#     time.sleep(0.5)
#     GPIO.output(GPIO_TRIGGER, False)
 
#     StartTime = time.time()
#     StopTime = time.time()
 
#     while GPIO.input(GPIO_ECHO) == 0:
#         StartTime = time.time()
 
#     while GPIO.input(GPIO_ECHO) == 1:
#         StopTime = time.time()
 
#     TimeElapsed = StopTime - StartTime
#     distance = (TimeElapsed * 34300) / 2
 
#     return distance

# def pulsa_w():
#     m1.ChangeDutyCycle(5)
#     m2.ChangeDutyCycle(10)
#     print('Se ha pulsado W')

# def pulsa_s():
#     m1.ChangeDutyCycle(10)
#     m2.ChangeDutyCycle(5)
#     print('Se ha pulsado S')

# def pulsa_a():
    
#     m1.ChangeDutyCycle(5)
#     m2.ChangeDutyCycle(5)
#     print('Se ha pulsado A')
    

# def pulsa_d():
    
#     m1.ChangeDutyCycle(10)
#     m2.ChangeDutyCycle(10)
#     print('Se ha pulsado D')
    
# def pulsa_q(): 
#     m1.ChangeDutyCycle(0)
#     m2.ChangeDutyCycle(0)
#     print('Se ha pulsado Q')
    
# def pulsa_e():
#     m1.ChangeDutyCycle(5)
#     m2.ChangeDutyCycle(10)
#     print('Se ha activado el modo automatico (Beta)')
#     while True:
#         d=distance()
#         if d<50:
#             if d<5:
#                 return
#             m1.ChangeDutyCycle(10)
#             m2.ChangeDutyCycle(10)
#             print("Objeto encontrado a menos de 35cm")
#             time.sleep(1)
#             m1.ChangeDutyCycle(5)
#             m2.ChangeDutyCycle(10)
            
             


if __name__=='__main__':
    order=input(termcolor.colored("Do you want to bouild a webpage to control(Y/N)?\n","blue"))

    if order=='Y' or order =='y':
        print(termcolor.colored("Starting webpage","blue"))
        sp.run(['& py "c:/Users/Usuario/Desktop/BR-SRK Movement control/web_app.py"'])
        print(termcolor.colored("HTTP Server started on port 5000",cyan))
        while True:
            time.sleep(0.1)
            with open('socket.txt','r') as socket:
                val=socket.read()    
                if val=='e':
                    pulsa_e()
                if val=='a':
                    pulsa_a()
                if val=='s':
                    pulsa_s()
                if val=='d':
                    pulsa_d()
                if val=='w':
                    pulsa_w()
    else:
        print(termcolor.colored("Controling by keyboard","blue"))
        hotkeys = { 'w': pulsa_w ,'s': pulsa_s,'a': pulsa_a,'d': pulsa_d,'e': pulsa_e,'q': pulsa_q}

        with keyboard.GlobalHotKeys(hotkeys) as escuchadYor:
            print(termcolor.colored("Iniciando...",green))
            escuchador.join()
                


