import psycopg2

DBNAME = "news"

title_one = "\nThe three most popular articles of all time"
title_two = "\nThe three most popular authors of all time"
title_three = "\nThe days with more than one percent of" +
"requests that leads to an error"

query_one = "select title, count(*) as views from articles a," +
"log l where a.slug=substring(l.path, 10) group by" +
"title order by views desc limit 3;"
query_two = "select name, sum(views) from title_views_author" +
"group by name order by sum desc limit 3;"
query_three = "select * from error_view where \"percentage error\">1;"


def get_query_result(query):
    """Gets query results from database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_query_result(query_result):
    """Prints query result from first and second queries"""
    print (query_result[1])
    for results in (query_result[0]):
        print (str(results[0]) + ' - ' + str(results[1]) + ' views')


def print_error_result(error_result):
    """Print query result for third query"""
    print (error_result[1])
    for results in error_result[0]:
        print (str(results[0]) + ' - ' + str(results[1]) + '%')


if __name__ == '__main__':
    most_popular_articles = get_query_result(query_one), title_one
    most_popular_authors = get_query_result(query_two), title_two
    highest_error_days = get_query_result(query_three), title_three

    print_query_result(most_popular_articles)
    print_query_result(most_popular_authors)
    print_error_result(highest_error_days)
