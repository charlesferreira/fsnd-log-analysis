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
```

## Usage

Run the following command to start the server:

```
$ python report.py
```

The reports will be available at <http://localhost:8000>

## Contact

Charles Ferreira <charles.dev@live.com>
