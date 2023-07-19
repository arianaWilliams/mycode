#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   A simple Flask server. Responds to HTTP 'GET /' requests
   with a 'Hello World' attached to a 200 response"""

# an object of flask class is our WSGI application
from flask import Flask

# flask constuctor takes the name of current
# module(__name__) as argument
app = Flask(__name__)

# route() function of the flask class is a decorator, tells the app which url should call the func
@app.route("/")
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 2224) # runs the app
