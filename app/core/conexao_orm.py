from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from urllib.parse import quote_plus

user = 'postgres'
password = quote_plus('Neo@2025*')  # encode especial para caracteres
host = 'localhost'
database = 'blog'

DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'

# Cria o engine de conexão com banco
engine = create_engine(DATABASE_URI, echo=True)

# Define a base para os modelos
Base = declarative_base()

# Configura a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar uma sessão pronta para usar no seu código
session = SessionLocal()
