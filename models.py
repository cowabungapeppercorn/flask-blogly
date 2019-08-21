"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """ Connect to Database """

    db.app = app
    db.init_app(app)


class User(db.Model):
    """ USER """

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                           nullable=False)
    last_name = db.Column(db.String(50),
                          nullable=False)
    image_url = db.Column(db.String(200),
                          nullable=True,
                          default=('https://cdn3.iconfinder.com/data/icons/avatars-15/64/_Ninja-2-512.png'))
