import click
import sqlite3

@click.command()
def update():
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
            click.echo("What do you want to change?\n>")
            click.echo("1: ID")
            click.echo("2: Name")
            click.echo("3: Description")
            click.echo("4: Priority")
            click.echo("5: Status")
            click.echo("6: All")
            option = input(">")
            if option == "1":
                new_id = input("Insert the new ID\n>")
                cursor.execute("UPDATE tasks SET id= ? WHERE id= ?", (new_id, task_id))
                conexion.commit()
                click.echo("Task updated successfully.")
                break

            