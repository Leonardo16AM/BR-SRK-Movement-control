import cv2
import socket
from termcolor import colored
from time import sleep
import base64
import zmq

context=zmq.Context()
client_socket=context.socket(zmq.PUB)
client_socket.connect('tcp://localhost:5555')




print(colored("Starting....","cyan"))




if __name__=='__main__':

    camera=input("Select the number of the camera ( 0 if error ) :")
    camera=int(camera)

    try:
        vid=cv2.VideoCapture(camera)
        print( colored(f"Camera number {camera} activated",'cyan') )
    except Exception:
        print( colored(f"Error activating camera number {camera}. We will try to activate camera number 0",'orange'))
        try:
            vid=cv2.VideoCapture(0)
            print( colored(f"Camera number {0} activated",'cyan') )
        except Exception:
            print( colored(f"No camera connected",'red'))


    fps=input("Select the number of frames per second (between 10 and 60):")
    fps=int(fps)
    if fps<30 or fps>60:
        fps=60

    print(colored(f"Using {fps} fps",'blue'))

    print(colored("Starting streaming","green"))

    while 1:
        try:
            success,img=vid.read()
            encoded,buffer=cv2.imencode('.jpg',img)
            package=base64.b64encode(buffer)
            client_socket.send(package)
            sleep(1/fps)
        except Exception as e:
            print(e)
            break
else:
    camera=int(0)
    vid=cv2.VideoCapture(camera)    
    print( colored(f"Camera number {camera} activated",'cyan') )
    fps=int(60)
    print(colored(f"Using {fps} fps",'blue'))
    print(colored("Starting streaming","green"))

    while 1:
        try:
            success,img=vid.read()
            encoded,buffer=cv2.imencode('.jpg',img)
            package=base64.b64encode(buffer)
            client_socket.send(package)
            sleep(1/fps)
        except Exception as e:
            print(e)
            break