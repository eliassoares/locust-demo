from api.app import db
from sqlalchemy import Column, Integer, Text


class Access(db.Model):
    __tablename__ = 'access'
    id = Column(Integer, primary_key=True)
    path = Column(Text, nullable=False)
