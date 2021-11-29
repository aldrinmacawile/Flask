from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired


#Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "Goop123"

# Create a form Class
class Namerform(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    submit = SubmitField("Submit")




#Create a route decorator
@app.route('/')

#def index():
    #return "<h1>Hello World!</h1>"

#safe, capitalize, lower, upper, title, trim, striptags,   -- jinja filters

def index():
    return render_template("index.html")

#localhost5000:/user/macawile
@app.route('/register', methods=['GET', 'POST'])

def register():
    #return "<h1>Hello {}!!!</h1>".format(name)
    name = None
    form = Namerform()
    #validators
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Succesfully Please Login!")

    return render_template("register.html", name = name, form = form)

# Create Custom Error pages
# Create Invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500




