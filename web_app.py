from flask import Flask,request,session,render_template
import time

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    global big_thread
    if request.method=='GET':    
        return render_template('index.html')
    else:

        with open("socket.txt","r+") as socket:
            if request.form.get('w')=='W':
                socket.write('w')
                return render_template('index.html')

            elif request.form.get('a')=='A':
                socket.write('a')
                return render_template('index.html')
            elif request.form.get('s')=='S':
                socket.write('s')
                return render_template('index.html')

            elif request.form.get('d')=='D':
                socket.write('d')
                return render_template('index.html')

            elif request.form.get('auto')=='Automatic':
                socket.write('e')
                return render_template('index.html')

            return render_template('index.html')


app.run(debug=True)