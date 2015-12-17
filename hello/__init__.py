#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Hello!</h2></body></html>"

if __name__ == '__main__':
    app.run()
