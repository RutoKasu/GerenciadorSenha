import sqlite3

def connect():
    conexao = sqlite3.connect("banco/senhas.db")
    return conexao



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
        CREATE TABLE IF NOT EXISTS logins_user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    app TEXT NOT NULL,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                   );
                """)
    conn.commit()



def update():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
                SELECT * FROM user
                """)
    print(*cursor.fetchall())



def inserir():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
                INSERT INTO user (user,password) VALUES ("Eliam Rainier","Soufoda360@_")
                """)
    conn.commit()



def deletar():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
                DELETE FROM user WHERE id = 1
                """)
    conn.commit()