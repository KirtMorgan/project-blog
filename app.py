from flask import Flask, render_template
from articles import chef_pick

app = Flask(__name__)

@app.route('/story')

def story():
    return render_template('story.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__== '__main__':
    app.run(debug=True)
