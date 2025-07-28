from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Conexão com o banco de dados PostgreSQL
user = 'postgres'
password = 'Neo@2025*'
host = 'localhost'
database = 'blog'

DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'

# Engine de conexão
engine = create_engine(DATABASE_URI, echo=True)

# Criando a sessão
Session = sessionmaker(bind=engine)
session = Session()

# Base para as classes ORM
Base = declarative_base()