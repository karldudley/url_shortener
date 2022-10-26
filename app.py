from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import random
import string
from datetime import datetime


# create app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db' # flask sqlite db

# Initialise the db
db = SQLAlchemy(app)

# RESET = "yes"
# if RESET == "yes":
#     with app.app_context():
#         db.drop_all()    
#         db.create_all()

# create db model
class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), unique=True, nullable=False)
    short_url = db.Column(db.String(200), unique=True, nullable=False)

    #create a function to return a string when we add something
    def __repr__(self):
        return '<Urls %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirm', methods=["POST"])
def confirm():
    full_url = request.form.get("url")
    # create a random string
    random = get_random_string(6)

    # create new instance of Urls class
    new_url = Urls(url=full_url, short_url=random)

    # store random string and url in db
    try:
        db.session.add(new_url)
        db.session.commit()
        return render_template("confirm.html", url=full_url, short_url=random)
    except:
        return "There was an error shortening your url"

@app.route('/<path>')
def short(path):
    link = Urls.query.filter_by(short_url=path).first()
    if link:
        return redirect(link.url)
    else:
        return redirect("/")
    
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str

## Main
if __name__ == "__main__":
    app.run(debug=True)
