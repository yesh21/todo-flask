from app import db
from datetime import datetime

  
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    complete = db.Column(db.Boolean)
    descript = db.Column(db.Text)
    date = db.Column(db.DateTime,default=datetime.utcnow)
  
