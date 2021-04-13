"""Blogly application."""

from flask import Flask,request,render_template,redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,User

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'is so secret keys'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def home_page():
    return redirect("/users")

@app.route("/users")
def all_users():
    all_user = User.query.all()
    return render_template("all_user.html",users=all_user)

@app.route('/users/new')
def add_user_form():
    return render_template("add_user.html")

@app.route('/users/new',methods=["POST"])
def post_user_form():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["user_url"]

    new_user = User(first_name=first_name,last_name=last_name,image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    target_user = User.query.get(user_id)
    return render_template("user_detail.html",user = target_user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    target_user = User.query.get(user_id)
    return render_template("edit_user.html",user=target_user)


@app.route('/users/<int:user_id>/edit',methods=["POST"])
def save_edit(user_id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['user_url']

    target_user = User.query.get(user_id)

    target_user.first_name = first_name
    target_user.last_name = last_name
    target_user.image_url = image_url

    db.session.commit()

    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/delete',methods=["POST"])
def delete_user(user_id):
    get_user_info = User.query.get(user_id)
    delete_user = User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return render_template('delete_user.html',user=get_user_info)
