from api.app import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

