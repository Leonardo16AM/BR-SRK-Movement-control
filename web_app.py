# This code creates a  Flask app and runs a webpage
# It works as a socket client and send information
# to the port 1234 with the buttons pressed (W,A,S,D,E).

# In case of error try installing flask and termcolor
# or change the port number.

# 2021 - Leonardo16AM


from flask import Flask,request,session,render_template
import time
import socket
from termcolor import colored

app=Flask(__name__)

        
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':    
        return render_template('index.html')
    else:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), 12332))
        if request.form.get('w')=='W':
            s.send(b'w')
            return render_template('index.html')

        elif request.form.get('a')=='A':
            s.send(b'a')
            return render_template('index.html')
        elif request.form.get('s')=='S':
            s.send(b's')
            return render_template('index.html')

        elif request.form.get('d')=='D':
            s.send(b'd')
            return render_template('index.html')

        elif request.form.get('auto')=='Automatic':
            s.send(b'e')
            return render_template('index.html')
    return render_template('index.html')




app.run(debug=True)