import sqlite3
import hashlib

#Iniciar a conexão com o banco de dados podendo assim fazer o CRUD.
def connect():
    conexao = sqlite3.connect("banco/senhas.db")
    return conexao


#Essa função implementa a criação das tabelas no banco de dados.
#A tabela user e a logins_user, onde uma guardará o username e a senha.
#e a outra guardará o local onde o username, o email e senha estão
#cadastrados.
def criar():
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
                    site TEXT NOT NULL,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    usuario_id INTEGER NOT NULL,
                   
                    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
                   );
                """)
    conn.commit()
    conn.close()


#Essa função faz a seleção de tudo dentro da tabela e mostra.
def listar_user():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
                SELECT * FROM user
                """)
    print(*cursor.fetchall())
    conn.close()


#Essa função faz a inserção dos dados na tabela user
def inserir_user():

    valor_user = input("Informe o nome do usuário: ")
    valor_senha = int(input("informe a senha: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
                INSERT INTO user (user,password) 
                VALUES (?,?)
                """,(valor_user,valor_senha))
    conn.commit()
    conn.close()


#essa função deleta a tabela da tabela user
def deletar_user():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
                DELETE FROM user WHERE id = 1
                """)
    conn.commit()
    conn.close()

#essa função atualiza os dados da tabela user
# def update_user():
#     conn = connect()
#     cursor = conn.cursor()

#     cursor.execute("""
#                 UPDATE user 
#                 SET 
#                 """)