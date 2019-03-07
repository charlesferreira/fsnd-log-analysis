#!/usr/bin/env python3
#
# A simple reporting tool for the Full Stack Web Developer Nanodegree @ Udacity

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    ''' Starting page '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

