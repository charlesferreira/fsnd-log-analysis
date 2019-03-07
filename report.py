#!/usr/bin/env python3
#
# A simple reporting tool for the Full Stack Web Developer Nanodegree @ Udacity

from flask import Flask

app = Flask(__name__)

# HTML template for the starting page
HTML = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Log analysis</title>
  </head>
  <body>
    <h1>Log analysis</h1>
    <ul>
        <li><a href="#">Most popular articles</a></li>
        <li><a href="#">Most popular authors</a></li>
        <li><a href="#">Most error requests</a></li>
    </ul>    
  </body>
</html>
'''

@app.route('/', methods=['GET'])
def main():
    ''' Starting page '''
    return HTML

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

