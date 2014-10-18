import os

from flask import Flask, render_template, send_file
from HogOnline import HogOnline

app = Flask(__name__)

#@app.route('/YOUR BEAUTIFUL URL HERE')
#def HANDLER_FUNCTION():
    #return OUTPUT OF YOUR SERVER CODE
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
