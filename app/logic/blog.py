from app.core.conexao_orm import Base, engine, session
from app.models.user import User
from app.models.post import Post

def criar_tabelas():
    Base.metadata.create_all(engine)

def add_user(name, email):
    novo_usuario = User(name=name, email=email)
    session.add(novo_usuario)
    session.commit()
    print("Usuário adicionado com sucesso!")

def add_post(title, content, author_id):
    post = Post(title=title, content=content, author_id=author_id)
    session.add(post)
    session.commit()
    print("Post adicionado com sucesso!")

def query_users_posts():
    users = session.query(User).all()
    for user in users:
        print(f'{user.name} ({user.email}):')
        for post in user.posts:
            print(f'  - {post.title}: {post.content}')

def show_menu():
    criar_tabelas()

    while True:
        print("\n[1] Adicionar usuário\n[2] Adicionar post\n[3] Ver usuários e posts\n[0] Sair")
        op = input("Escolha uma opção: ")

        if op == "1":
            name = input("Nome: ")
            email = input("Email: ")
            add_user(name, email)
        elif op == "2":
            title = input("Título: ")
            content = input("Conteúdo: ")
            author_id = int(input("ID do usuário: "))
            add_post(title, content, author_id)
        elif op == "3":
            query_users_posts()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
