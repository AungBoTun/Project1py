from models import *
from flask import Flask, session, render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_login import login_user, logout_user, login_required,LoginManager

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.urandom(12)
#Session(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Set up database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_id(str(user_id))

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        if not request.form['user_id'] or not request.form['email'] or not request.form["DOB"] or not request.form["Nationlaity"]:
            return render_template("error.html", message="Invalid flight number.")
        else:
            users.add_users(request.form['user_id'],request.form['email'],request.form["DOB"])
    return render_template("index.html")

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/book")
def book():
    return render_template("book.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route('/login')
def login():
     return render_template("login.html")

@app.route('/login', methods=['GET','POST'])
def login_post():
        user_id = str(request.form.get("user_id"))
        email = str(request.form.get("email"))     

        user=users.query.filter_by(user_id=user_id,email=email).first()
        if not user:
            return render_template("error.html", message="No such flight with that id.")
        else:
            login_user(user)
            return render_template("book.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template("login.html")
