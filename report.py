#!/usr/bin/env python3
#
# A simple reporting tool for the Full Stack Web Developer Nanodegree @ Udacity

from flask import Flask, render_template

from db import get_top_articles, get_authors_rank

app = Flask(__name__)


@app.route('/')
def home():
    ''' Home page '''
    return render_template('index.html')

@app.route('/articles')
def articles():
    ''' Most popular articles '''
    title = 'Top articles'
    articles = get_top_articles()
    return render_template('reports/articles.html', title=title, data=articles)

@app.route('/authors')
def authors():
    ''' Most popular articles '''
    title = 'Authors rank'
    authors = get_authors_rank()
    return render_template('reports/authors.html', title=title, data=authors)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

