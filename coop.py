from enum import unique
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#Create a flask instance
app = Flask(__name__)
#Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#Secret Key!
app.config['SECRET_KEY'] = "Goop123"

#Initialize the database
db = SQLAlchemy(app)
#Create a model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #Create a String
    def __repr__(self):
        return '<Name %r>' % self.name

# Create a form Class
class Userrform(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired()])
    submit = SubmitField("Submit")


#Create a route decorator
@app.route('/')

#safe, capitalize, lower, upper, title, trim, striptags,   -- jinja filters

def index():
    return render_template("index.html")

#localhost5000:/user/macawile
@app.route('/register/add', methods=['GET', 'POST'])
def register():
    name = None
    form = Userrform()
    #validators
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User Registered Succesfully Please Login!")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("register.html", name = name, form = form, our_users = our_users)

# Create Custom Error pages
# Create Invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500




