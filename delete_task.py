import click
import sqlite3

@click.command()
def delete():
    while True:
        task_id = input("Enter the ID: \n\n>")
        try:
            with sqlite3.connect("task-manager.db") as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        except sqlite3.OperationalError:
            click.echo("You have not created the DB and the table tasks, please use the command: 'create-db' ")
            break
        task = cursor.fetchone()
        click.echo(task)
        if task is None:
            click.echo("ID does not match with a task from from the Table.")
            answer = input("Do you want to try again? (Y/N)\n\n>")
            if answer == "Y":
                pass
            elif answer == "N":
                break
            else:
                click.echo("Sorry I dont understand you, Good bye.")
                break
        else:
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conexion.commit()
            click.echo("Task deleted successfully.")
            break

