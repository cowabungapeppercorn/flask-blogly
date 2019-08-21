"""Blogly application."""

import pdb
from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'we need secrets'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


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
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    
    db.session.add(new_user)
    db.session.commit()
    
    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user_info(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user-info.html', user=user)


@app.route('/users/<int:user_id>/edit')
def show_user_edit_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('update-user.html', user=user)


@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    
    pdb.set_trace()
    
    # user.query.delete()
    db.session.delete(user)
    db.session.commit()
    
    flash(f'User {user.first_name} deleted')
    return redirect('/users')
 