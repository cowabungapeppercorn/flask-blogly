"""Blogly application."""

import pdb
import datetime
from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'we need secrets'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/users/new', methods=['GET'])
def show_user_form():

    return render_template('add-user.html')


@app.route('/users/new', methods=['POST'])
def add_new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url'] or None
    new_user = User(first_name=first_name,
                    last_name=last_name,
                    image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user_info(user_id):
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter(user_id == user_id).all()
    return render_template('user-info.html', user=user, posts=posts)


@app.route('/users/<int:user_id>/edit')
def show_user_edit_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('update-user.html', user=user)


@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    flash(f'User {user.first_name} deleted')
    return redirect('/users')


@app.route('/users/<int:user_id>/posts/new')
def new_post(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('new_post.html', user=user)


@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def create_post(user_id):
    user = User.query.get_or_404(user_id)
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title,
                    content=content,
                    created_at=datetime.datetime.now(),
                    user_id=user_id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/users/{user.id}')


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    return render_template('post_display.html', post=post, user=user)


@app.route('/posts/<int:post_id>/edit')
def show_edit(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    return render_template('post_edit.html', post=post, user=user)


@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title,
                    content=content,
                    created_at=datetime.datetime.now(),
                    user_id=post.user_id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/posts/{post_id}')
