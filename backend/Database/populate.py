import sqlite3
import pandas as pd

def init_messages_database():
    conn = sqlite3.connect('chat_messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def populate_vehicles_database(csv_file_path, db_file_path, table_name = "vehicles"):
    conn = None
    try:
        df = pd.read_csv(csv_file_path)
        conn = sqlite3.connect(db_file_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        print(f"Tabela '{table_name}' criada e populada com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        if conn:
            conn.close()
