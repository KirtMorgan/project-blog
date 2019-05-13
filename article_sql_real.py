from sql_db_connection import *

def article_sql_db():
    query = 'SELECT * FROM ArticlesData;'
    cursor.execute(query)
    article_results = cursor.fetchall()
    return article_results