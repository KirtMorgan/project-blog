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


@app.route('/blog')
def articles():
    return render_template('articles.html', articles_data_db = articles_with_data)


def show_article(id):
    if int(id) > len(articles):
        return 'article doesnt exist'
    else:
        article = articles[int(id)]
        return article

@app.route('/articles/<string:id>')
def show_article_page(id):
    result = show_article(id)
    return render_template('display_article_page.html', id=id, article=result)


if __name__== '__main__':
    app.run(debug=True)
