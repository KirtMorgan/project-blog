from sql_db_connection import *

def article_db():
    query = 'SELECT * FROM ArticlesData;'
    cursor.execute(query)
    article_results = cursor.fetchall()
    return article_results

# hi = {}
# red = []
# for article in article_results:
#     red.append(article)
#
# print(red)
