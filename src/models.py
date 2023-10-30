import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


# Definir las tablas user, post, media, comment y follower/ Listo
# Llenar el contenido de las tablas segun lo solicitado/ Listo
# Establecer las relaciones entre tablas de manera correcta:
# 1ra Relacion User-Follower relacion one to many de ambas partes (Porque un usurio puede tener muchos seguidores y los seguidores son muchos usurios) / Listo
# 2da Reclacion User-Comment relacion one to many (Un usurio puede tener muchos comentarios pero un comentario no puede tener muchos usurios) /Listo
# 3ra Relacion User-Post relacion one to many (Un usurio puede hacer muchas publicaciones pero esas publicaciones pertenecen a un solo usurio) /Listo
# 4ta Relacion Post-Comment relacion one to many (Una publicacion puede tener muchos cometarios pero un comentario pertenece a una publicacion) /Listo
# 5ta Relacion Post-Media relacion one to one /Listo

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(30), nullabble=False, unique=True)
    password = Column(String(250), nullabble=False)
    email = Column(String(100), nullabble=False, unique=True)
    birth_date = Column(DateTime(), nullabble=False)
    followers = relationship("Followers", uselist=True, backref='user')
    followers_id = Column(Integer(), ForeignKey='followers.id')
    commets_id = Column(Integer(), ForeignKey='comment.id')
    post_id =   Column(Integer(), ForeignKey='post.id')


class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullabble=False)
    username = Column(String(30), nullabble=False, unique=True)
    followers_of_follower = Column(Integer())
    users = relationship("User", uselist=True, backref='followers')
    users_id = Column(Integer(), ForeignKey='user.id')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_post = relationship("User", uselist=True, backref='post')
    comment_id = Column(Integer(), ForeignKey='commet')
    media = relationship("Media", uselist=False, backpopulates="post")

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
    post_id = Column(Integer, ForeignKey='post.id')
    post = relationship("Post", backpopulates="media")



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
