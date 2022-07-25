from datetime import datetime
from project import db

class Blog_post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    upvotes = db.Column(db.Integer, primary_key = False, nullable=True)
    downvotes = db.Column(db.Integer, primary_key = False, nullable=True)

    def __init__(self, title, body, author, pub_date):
        self.title = title
        self.body = body
        self.author = author
        self.pub_date = pub_date