from conexao_orm import Base, engine, session
from user import User
from post import Post

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)