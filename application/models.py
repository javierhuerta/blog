from sqlalchemy import Column, Integer, String, Text, Date
from application.database import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    body = Column(Text(), nullable=False)
    pub_date = Column(Date(), nullable=False)

    def __init__(self, title=title, body=body, pub_date=pub_date):
        self.title = title
        self.body = body
        self.pub_date = pub_date

    def __repr__(self):
        return '<Post %r>' % (self.title)