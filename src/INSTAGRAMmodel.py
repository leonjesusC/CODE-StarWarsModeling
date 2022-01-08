import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    created = Column(DateTime, nullable=False)
    last_active = Column(DateTime, nullable=False)
    post = relationship("Post", backref="users")
    user_post = relationship("User_Post", backref="users")
    comments = relationship("Comment", backref="users")
    likes = relationship("Like", backref="users")
    
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    image_url = Column(String(250), nullable=False)
    like_number = Column(Integer, nullable=False)
    comment_number = Column(Integer, nullable=False)
    user_post = relationship("User_Post", backref="post")
    comments = relationship("Comment", backref="post")
    likes = relationship("Like", backref="post")
    

class User_Post(Base):
    __tablename__ = 'user_post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_content = Column(String(250), nullable=False)

class Like(Base):
    __tablename__ = 'like'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    liked = Column(Boolean, nullable=False)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagramINSTAGRAM.png')