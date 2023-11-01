import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    comment_id = Column(Integer(), ForeignKey="comment.id")
    post_id = Column(Integer(), ForeignKey="post.id")
    user_followers = relationship("User_Followers", uselist=True, backref='user')


class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    user_followers = relationship("User_Followers", uselist=True, backref="followers")

class User_Followers(Base):
    __tablename__ = 'user_followers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id'))
    followers_id = Column(Integer(), ForeignKey('followers.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_post = relationship("User", uselist=True, backref='post')
    comment_id = Column(Integer(), ForeignKey='commet')
    media_id = Column(Integer(), ForeignKey('media.id'))
  

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    user_comments = relationship("User", uselist=True, backref='comment')
    post_comments  = relationship("Post", uselist=True, backref='comment')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(LargeBinary)
    url = Column(String(250))
    post = relationship("Post", uselist=False, backref='media')
  



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
