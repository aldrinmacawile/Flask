from flask import Flask, render_template

#Create a flask instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')

#def index():
    #return "<h1>Hello World!</h1>"

#safe, capitalize, lower, upper, title, trim, striptags,   -- jinja filters

def index():
    first_name = "Aldrin"
    stuff = "This is bold text"

    favorite_pizza = ["Pepperoni", "Cheese", "Mushroom", 41]
    return render_template("index.html", first_name=first_name, stuff=stuff, favorite_pizza = favorite_pizza)

#localhost5000:/user/macawile
@app.route('/user/<name>')

def user(name):
    #return "<h1>Hello {}!!!</h1>".format(name)
    return render_template("user.html", user_name=name)

# Create Custom Error pages
# Create Invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500