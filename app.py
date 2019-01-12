#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 00:15:18 2019

@author: takanori
"""

from flask import Flask, render_template, request, redirect, url_for
import numpy as np




app = Flask(__name__)

@app.route('/v1/get_message',methods=["GET"])
def index():
    
    message = picked_up()
                
    return message

def picked_up():
    message = ['大吉','小吉','中吉','末吉']
    return np.random.choice(message)



if __name__ == "__main__":
    #app.run(host='0.0.0.0',debug=True)
    app.run()
