from flask import Flask, render_template, request, redirect, url_for
import numpy as np




app = Flask(__name__)



@app.route('/')
def index():
    return "HELLO"


@app.route('/v1/get_message',methods=["GET"])
def get_message():
    
    message = picked_up()
                
    return message

def picked_up():
    message = ['大吉','小吉','中吉','末吉']
    return np.random.choice(message)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888,debug=True)
