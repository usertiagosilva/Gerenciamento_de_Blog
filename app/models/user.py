from sqlalchemy import Column, Integer, String
from app.core.conexao_orm import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    def __repr__(self):
        return f'<User(name={self.name}, email={self.email})>'
