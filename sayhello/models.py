from datetime import datetime

from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
    # 注意，这里设置的默认值是方法名称now，不是方法的调用now()
