from Apps.app import db
from datetime import datetime
from uuid import uuid4

# USER TABLE과 맵핑될 Class
class User(db.Model):
    # TABLE의 컴럼 정의하는 클래스 변수
    uuid = db.Column(db.String(100),primary_key =True)
    username = db.Column(db.String(10),nullable=False)
    email = db.Column(db.String(100),unique=True,nullable=False)
    password = db.Column(db.String(100),nullable=False)
    created_at = db.Column(db.DateTime,default = datetime.now)
    updated_at = db.Column(db.DateTime,default = datetime.now,onupdate=datetime.now)

class Chat(db.Model):
    idx = db.Column(db.Integer,primary_key= True)
    uuid = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    chat = db.Column(db.String(300),nullable=False)
    classification = db.Column(db.Integer)
    created_at = db.Column(db.DateTime,default = datetime.now)
    updated_at = db.Column(db.DateTime,default = datetime.now,onupdate=datetime.now)
