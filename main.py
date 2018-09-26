#!/usr/bin/env python3
import psycopg2

db = psycopg2.connect(dbname="news")
c = db.cursor()

# First Question : What are the most popular three articles of all time?
query1 = "select articles.title,count(log.id) as cnt from articles left join log on log.path=concat('/article/',articles.slug) group by articles.title order by cnt desc limit 3"
c.execute(query1)
result1 = c.fetchall()
print("Solution for 1st Question")
for x in result1:
    print(x)
print("\n")

# Second Question : Who are the most popular article authors of all time?
query2 = "select authors.name, count(log.id) as cnt from authors left join articles on authors.id=articles.author left join log on log.path=concat('/article/',articles.slug) group by authors.name order by cnt desc"
c.execute(query2)
result2 = c.fetchall()
print("Solution for 2nd Question")
for x in result2:
    print(x)
print("\n")

# Third Question : On which days did more than 1% of requests lead to errors?
# select date_trunc('day',log.time) "day", count(*) as cnt from log where status='404 NOT FOUND' group by 1;
# select date_trunc('day',log.time) "day",100.0*(sum(case when status='404 NOT FOUND'then 1 else 0 end))/count(time) as percent from log group by 1;
query3 = '''select to_char(day,'Month DD,YYYY') as day,percent as percentage from (select date_trunc('day',log.time) "day",100.0*(sum(case when status='404 NOT FOUND'then 1 else 0 end))/count(time) as percent from log group by 1) as foo where percent>1.0'''
c.execute(query3)
result3 = c.fetchall()
print("Solution for 3rd Question")
for x in result3:
    print(x)
print("\n")
