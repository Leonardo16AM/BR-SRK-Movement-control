from flask import Flask,request,session,render_template
import asyncio
import movement_control as car


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':    
        return render_template('index.html')
    else:
        print(request.form)
        if request.form.get('w')=='W':
            car.pulsa_w()
        elif request.form.get('a')=='A':
            car.pulsa_a()
        elif request.form.get('s')=='S':
            car.pulsa_s()
        elif request.form.get('d')=='D':
            car.pulsa_d()
        elif request.form.get('auto')=='Automatic':
            car.pulsa_e()

        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)