from flask import Flask, g, render_template
from auth import views
import sqlite3

app = Flask(__name__)
app.register_blueprint(views.bp)

DATABASE = ':memory:' 

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route('/')
def hello_world():
    return render_template('home.html', name='Felix')

