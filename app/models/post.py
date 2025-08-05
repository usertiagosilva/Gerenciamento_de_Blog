from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.conexao_orm import Base
from app.models.user import User

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))

    usuario = relationship("User", back_populates="posts")

User.posts = relationship("Post", back_populates="usuario")
