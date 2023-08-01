import sqlite3
import click

@click.command()
def create_db():
    conexion = sqlite3.connect("task-manager.db")
    cursor = conexion.cursor()
    
    try:
        cursor.execute('''CREATE TABLE tasks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(100) NOT NULL,
                    description TEXT NOT NULL,
                    priority CHAR(1) NOT NULL,
                    status VARCHAR(100) NOT NULL
                    )
                    ''')
    
    except sqlite3.OperationalError:
        print("The table 'tasks' has already been created.")
    else:
        print("The table 'tasks' was successfully created.")
    conexion.commit()
    conexion.close()
