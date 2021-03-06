# Database code for the Log Analysis

import psycopg2
import sys


DBNAME = 'news'


def run_select_query(query):
    try:
        conn = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)

    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


def get_top_articles():
    query = "SELECT * FROM article_views ORDER BY views DESC LIMIT 3"
    return run_select_query(query)


def get_authors_rank():
    query = "SELECT * FROM author_views ORDER BY views DESC"
    return run_select_query(query)


def get_errors():
    query = "SELECT * FROM error_rates WHERE rate > 0.01 ORDER BY rate DESC"
    return run_select_query(query)
