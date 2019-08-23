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

    posts = db.relationship('Post')

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(
        db.String(200),
        nullable=False,
        server_default=
        'https://cdn3.iconfinder.com/data/icons/avatars-15/64/_Ninja-2-512.png'
    )


class Post(db.Model):
    """ POST """

    __tablename__ = 'posts'

    user = db.relationship('User')
    posts_tags = db.relationship('PostTag')
    tags = db.relationship('Tag', secondary='posts_tags')

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(10000), nullable=True)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Tag(db.Model):
    """ TAG """

    __tablename__ = 'tags'

    # posts_tags = db.relationship('PostTag', backref='tags')
    posts_tags = db.relationship('PostTag')
    posts = db.relationship('Post', secondary='posts_tags')

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    posts = db.relationship('Post', secondary='posts_tags')


class PostTag(db.Model):
    """ POST TAG RELATIONSHIP """

    __tablename__ = 'posts_tags'

    tags = db.relationship('Tag')
    posts = db.relationship('Post')

    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'),
                        primary_key=True)
