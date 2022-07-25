from datetime import datetime
from flask import jsonify, redirect, render_template, request, url_for
from project import app, db
from project.model import Blog_post

@app.route('/home')
@app.route('/')
def index():
    posts = Blog_post.query.all()
    return render_template('index.html', posts = posts)

@app.route('/create-post')
def create_post():
    #  print(request.get_data())
     return render_template('create-post.html')

    

@app.route('/add-post', methods=['POST'])
def add_post():
    # print(request.get_data())
    
    title = request.form.get('title')
    body = request.form.get('body')
    author = request.form.get('author')
    pub_date = datetime.now()
    new_post = Blog_post(title=title, body=body, author=author, pub_date=pub_date)
    db.session.add(new_post)
    db.session.commit()

    return redirect(url_for('show_post_list'))



@app.route('/show-list')
def show_post_list():
    
    posts = Blog_post.query.all()
    return render_template('blog-list.html', posts = posts)

@app.route('/show-post/<title>')
def show_post(title):
    blog_post = Blog_post.query.filter_by(title=title).first()
    return render_template('blog-post.html', blog_post = blog_post)

@app.route('/about')
def show_about():
    return render_template('about.html')

@app.route('/read-post')
def read_post():
    return 'Success'

@app.route('/update-post')
def update_post():
    return 'Success'

@app.route('/delete_post')
def delete_post():
    return 'Success'