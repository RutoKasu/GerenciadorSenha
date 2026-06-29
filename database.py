import sqlite3, hashlib, os





#Iniciar a conexão com o banco de dados podendo assim fazer o CRUD.
def connect():
    conexao = sqlite3.connect("banco/senhas.db")
    return conexao







#Essa função implementa a criação das tabelas no banco de dados.
#A tabela user e a logins_user, onde uma guardará o username e a senha.
#e a outra guardará o local onde o username, o email e senha estão
#cadastrados.
def criar():

    if os.path.exists('banco/senhas.db'):
        print("Não foi possivel criar o banco de dados.\nBanco de Dados já existente.")
    else:
        print("Banco de dados criado com sucesso!")


        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT NOT NULL,
                    password TEXT NOT NULL
                    );
                    """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS login(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        servico TEXT NOT NULL,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        user_id INTEGER NOT NULL,
                    
                        FOREIGN KEY(user_id) REFERENCES user(id)
                    );
                    """)
        conn.commit()
        conn.close()










#Essa função faz a seleção de tudo dentro da tabela (user) e mostra.
def listar_user():
    if os.path.exists('banco/senhas.db'):
        print("===== LISTAGEM =====")
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
                    SELECT * FROM user
                    """)
        print(*cursor.fetchall())
        conn.close()
    else:
        print("Banco de dados não existe.")


#Essa função faz a seleção de tudo dentro da tabela de senhas (login) e mostra
def listar_login():
    if os.path.exists('banco/senha.db'):
        print("===== LISTAGEM ======")
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM login")
        print(cursor.fetchall())
        conn.close()
    else:
        print("Banco de Dados não existe")





#Essa função faz a inserção dos dados na tabela user
def inserir_user():
    if os.path.exists('banco/senhas.db'):
        print("===== INSERÇÃO DE DADOS =====")

        valor_user = input("Informe o nome do usuário: ")
        valor_senha = input("informe a senha: ")

        senha_hash = hashlib.sha256(valor_senha.encode('utf-8')).hexdigest()

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
                    INSERT INTO user (user,password) 
                    VALUES (?,?);
                    """,(valor_user,senha_hash,))
        conn.commit()
        conn.close()
    else:
        print("Banco de dados inexistente!\nCriei o banco de dados.")







def inserir_login(user_id_logado):
    if os.path.exists('banco/senhas.db'):
        print("===== INSERÇÃO DE DADOS =====")

        valor_servico = input("Informe o serviço: ")
        valor_user = input("Informe o username: ")
        valor_email = input("Informe o email: ")
        valor_password = input("Informe a senha: ")

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("""
                     INSERT INTO login (servico,username,email,password,user_id) 
                     VALUES (?,?,?,?)
                     """,(valor_servico,valor_user,valor_email,valor_password,user_id_logado))
        
        conn.commit()
        conn.close()





#essa função deleta a tabela da tabela user
def deletar_user():
    if os.path.exists("banco/senhas.db"):
        valor_id = input("Qual o id da tabela user você deseja apagar: ")

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
                    DELETE FROM user WHERE id = ?
                    """,(valor_id,))
        conn.commit()
        conn.close()

        print(f"O usuário com ID {valor_id} foi deletado com sucesso!")
    else:
        print("Banco de dados não foi encontrado!")






#função para deletar todo o banco de dados
def deletar_banco():
    if os.path.exists("banco/senhas.db"):
        os.remove("banco/senhas.db")
        print("O banco de dados foi deletado com sucesso.")
    else:
        print("Banco de dados não foi encontrado!")