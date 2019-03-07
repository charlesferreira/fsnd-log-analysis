# Log Analysis

This reporting tool was created as part of the Full Stack Web Developer
Nanodegree at Udacity.

## Setup

Create the database views by running the following commands:

```sql
CREATE VIEW article_views AS SELECT title, COUNT(*) AS views FROM log, articles WHERE path=CONCAT('/article/', slug) GROUP BY articles.id;
```

## Usage

## Contact

Charles Ferreira <charles.dev@live.com>
