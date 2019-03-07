#!/usr/bin/env python3
#
# A simple reporting tool for the Full Stack Web Developer Nanodegree @ Udacity

from flask import Flask, render_template

from db import get_popular_articles

app = Flask(__name__)


@app.route('/')
def home():
    ''' Home page '''
    return render_template('index.html')

@app.route('/articles')
def articles():
    ''' Most popular articles '''
    title = 'Popular articles'
    articles = get_popular_articles()
    return render_template('report.html', title=title, data=articles, columns=['title', 'views'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

