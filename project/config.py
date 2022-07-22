import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:1234@localhost:5432/blog_posts_db'  
        #  'sqlite:///' + os.path.join(basedir, 'app.db')
        
    # Postgres db connection format: 'postgresql://username:password@hostname:port/dbname'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
