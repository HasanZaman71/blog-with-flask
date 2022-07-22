import os

from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:1234@localhost:port/blog_posts_db'
     SQLALCHEMY_TRACK_MODIFICATIONS = False