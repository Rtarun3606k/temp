from flask import render_template,request,Flask,redirect
from conversion import celsius_to_fahrenheit,celsius_to_kelvin,kelvin_to_celsius,fahrenheit_to_celsius,fahrenheit_to_kelvin,kelvin_to_fahrenheit

app = Flask(__name__)

def get_converted(convert,conversion,value):
               #         <option selected>Open this select menu</option>
            # <option value="1">fahrenheit</option>
            # <option value="2">celsius</option>
            # <option value="3">kelvin</option>
    if convert==conversion:
        return f'{value} you have selected same'
    if convert==1 and conversion==2: #f to c
        return fahrenheit_to_celsius(value)
    if convert==1 and conversion==3: #f to k
        return fahrenheit_to_kelvin(value)
    if convert==2 and conversion==1: #c to f
        return celsius_to_fahrenheit(value)
    if convert==2 and conversion==3: #c to k
        return celsius_to_kelvin(value)
    if convert==3 and conversion==1: #k to f
        return kelvin_to_fahrenheit(value)
    if convert==3 and conversion==2: #k to c
        return kelvin_to_celsius(value)
    else:
        return 'select something'
    



@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def index():
    if request.method=='POST':
        convert=int(request.form['from'])
        conversion=int(request.form['to'])
        value=int(request.form['number'])
        # print(convert,conversion,value) 
        # print(type(convert),type(conversion),type(value)) 
        output = get_converted(convert,conversion,value)
        # return redirect('/')
        return render_template('index.html',output=output)
    output='your answer'
    return render_template('index.html',output=output)

