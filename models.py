import sqlite3

def init_db():
    """Função para inicializar o banco de dados SQLite"""
    with sqlite3.connect('database.db') as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS books(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        category TEXT NOT NULL,
                        author TEXT NOT NULL,
                        img TEXT NOT NULL
                    )""")
        print("Banco de dados criado!")