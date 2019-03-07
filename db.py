# Database code for the Log Analysis

import psycopg2

DBNAME = 'news'

def get_top_articles():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM article_views ORDER BY views DESC LIMIT 3")
    articles = cursor.fetchall()
    db.close()
    return articles

def get_authors_rank():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM author_views ORDER BY views DESC")
    authors = cursor.fetchall()
    db.close()
    return authors
