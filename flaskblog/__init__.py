from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flaskblog.forms import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='acc590d5f6c84066479477aef4590cdd'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

from flaskblog import routes 