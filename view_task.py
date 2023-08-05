import click
import sqlite3 

@click.command()
def view():
    conexion = sqlite3.connect("task-manager.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        if tasks == []:
            click.echo("You don't have any task created")
        else:
            for task in tasks:
                click.echo()
                click.echo(f"Task ID:".ljust(20) + f"{task[0]}")
                click.echo(f"Name:".ljust(20) + f"{task[1]}")
                click.echo(f"Description:".ljust(20) + f"{task[2]}")
                click.echo(f"Priority:".ljust(20) + f"{task[3]}")
                click.echo(f"Status:".ljust(20) + f"{task[4]}")
                click.echo("\n")
    except sqlite3.OperationalError:
        click.echo("You have not created the DB and the table tasks, please use the command: 'create-db' ")
    conexion.close()

