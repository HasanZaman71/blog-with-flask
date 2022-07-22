from flask import render_template
from project import app

@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_post')
def create_post():
    return 'Success'

@app.route('/read_post')
def read_post():
    return 'Success'

@app.route('/update_post')
def update_post():
    return 'Success'

@app.route('/delete_post')
def delete_post():
    return 'Success'