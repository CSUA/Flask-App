import os

from flask import Flask, render_template, send_file
from HogOnline import HogOnline

hog = HogOnline()
app = Flask(__name__)

@app.route('/')
def home():
    return static_proxy("index.html")
  
@app.route('/static/<path>')
def static_proxy(path):
    return send_file(os.path.join('static', path))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
