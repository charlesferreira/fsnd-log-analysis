# Log Analysis

This reporting tool was created as part of the Full Stack Web Developer
Nanodegree at Udacity.

## Setup

Execute the following queries in Postgres to create the required database views:

```sql
-- Return the view count for each article 
CREATE VIEW article_views AS SELECT title, COUNT(*) AS views FROM log, articles WHERE path=CONCAT('/article/', slug) GROUP BY articles.id;

-- Return the view count for each article's author
CREATE VIEW author_views AS SELECT name, COUNT(*) AS views FROM log, articles ar, authors au WHERE path=CONCAT('/article/', slug) AND ar.author=au.id GROUP BY name;

-- Count requests and errors by date
CREATE VIEW request_count AS SELECT DATE(time), COUNT(*) FROM log GROUP BY date;
CREATE VIEW request_errors AS SELECT DATE(time), COUNT(*) FROM log WHERE status LIKE '4%' GROUP BY date;
CREATE VIEW error_rates AS SELECT e.date, CAST(e.count AS FLOAT)/c.count AS rate FROM request_errors e, request_count c WHERE e.date = c.date;

```

## Usage

Run the following command to start the server:

```
$ python main.py
```

The reports will be available at <http://localhost:8000>

## Contact

Charles Ferreira <charles.dev@live.com>