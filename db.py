# Database code for the Log Analysis

import psycopg2

DBNAME = 'news'

def run_select_query(query):
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def get_top_articles():
    return run_select_query("SELECT * FROM article_views ORDER BY views DESC LIMIT 3")

def get_authors_rank():
    return run_select_query("SELECT * FROM author_views ORDER BY views DESC")
