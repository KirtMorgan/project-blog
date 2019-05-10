from flask import Flask, render_template

from articles import articles


# app is the instance of the Flask object that has a method
app = Flask(__name__)

# meothod calling the articles db
articles_with_data = articles()

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles_data_db = articles_with_data)

def show_article(dict_id):
    if int(dict_id) > len(articles):
        return 'article doesnt exist'
    else:
        article = articles[int(dict_id)]
        return article

@app.route('/articles/<string:id>')
def show_article_page(dict_id):
    result = show_article(dict_id)
    return render_template('display_article_page.html', dict_id=dict_id, article=result)


if __name__== '__main__':
    app.run(debug=True)
