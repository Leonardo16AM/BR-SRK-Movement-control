from flask import Flask,request,session,render_template
import movement_control as car
import threading
import time

app=Flask(__name__)


class Thread (threading.Thread):
    def __init__(self,ch):
        threading.Thread.__init__(self)
        self.ch=ch
    def run(self):
        if(self.ch=='W'):
            car.pulsa_w()
            
        if(self.ch=='A'):
            car.pulsa_a()
            
        if(self.ch=='S'):
            car.pulsa_s()
            
        if(self.ch=='D'):
            car.pulsa_d()

        if(self.ch=='Auto'):
            car.pulsa_e()
        while 1:pass
        return



big_thread=123

@app.route('/',methods=['GET','POST'])
def index():
    global big_thread
    if request.method=='GET':    
        print(threading.activeCount() )
        print(threading.currentThread() )
        print(threading.enumerate())
        return render_template('index.html')
    else:
        if request.form.get('w')=='W':
            big_thread=Thread('W')
            big_thread.start()
            return render_template('index.html')

        elif request.form.get('a')=='A':
            big_thread=Thread('A')
            big_thread.start()
            return render_template('index.html')

        elif request.form.get('s')=='S':
            big_thread=Thread('D')
            big_thread.start()
            return render_template('index.html')

        elif request.form.get('d')=='D':
            big_thread=Thread('D')
            big_thread.start()
            return render_template('index.html')

        elif request.form.get('auto')=='Automatic':
            big_thread=Thread('Auto')
            big_thread.start()
            return render_template('index.html')

        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)