from flask import Flask, render_template
import socket


app = Flask(__name__)

get_hostname = socket.gethostname()
                   

@app.route('/')
def index():
    return "hello " + get_hostname + " is me"




