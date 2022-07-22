from flask import redirect, render_template, url_for
from project import app, db
from project.model import Blog_post

@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/create-post')
# def create_post():

#     new_post = Blog_post(title=title, body = body, pub_date=pub_date)
#     db.session.add(new_post)
#     db.session.commit()
#     return redirect(url_for('show-post'))

@app.route('/show-list')
def show_post_list():
    
    posts = Blog_post.query.all()
    return render_template('blog-list.html', posts = posts)

@app.route('/show-post/<title>')
def show_post(title):
    blog_post = Blog_post.query.filter_by(title=title).first()
    return render_template('blog-post.html', blog_post = blog_post)

@app.route('/read-post')
def read_post():
    return 'Success'

@app.route('/update-post')
def update_post():
    return 'Success'

@app.route('/delete_post')
def delete_post():
    return 'Success'