from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True, index=True)
    bio = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    expenditure = db.Column(db.Integer)

class FinanceLiteracy(db.Model):
    __tablename__ = 'financesLiteracy'
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(255))
    content =db.Column(db.String)

class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer,primary_key = True)
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255),nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

	#create string

    def __repr__(self):
        return '<Task %r>'%self.id
	

    