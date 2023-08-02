import click
import sqlite3

def get_priority():
    click.echo("\nSelect a priority for the task:")
    while True:
        click.echo("\nO:\tOptional")
        click.echo("L:\tLow")
        click.echo("M:\tMedium")
        click.echo("H:\tHigh")
        click.echo("C:\tCrucial")
        priority = input(">")
        if priority not in ["O", "L", "M", "H", "C"]:
            click.echo("ERROR: You must select between these letters:")
        else:
            return priority

def get_status():
    click.echo("\nSelect a status for the task:")
    while True:
        click.echo("\nPending:\tThe task has been created but work has not started yet.")
        click.echo("Started:\tWork on the task has begun but it is not yet completed.")
        click.echo("Completed:\tThe task has been finished and meets all requirements.")
        click.echo("Revision:\tThe task has been completed, but it requires review and approval before being considered fully finished.")
        click.echo("Canceled:\tThe task has been canceled and will not be continued.")
        click.echo("Paused:\tThe task has been temporarily stopped and is not currently being worked on.")
        click.echo("Rejected:\tThe task is considered unfeasible or unnecessary after a review.")
        status = input(">")
        if status not in ["Pending", "Started", "Completed", "Revision", "Canceled", "Paused", "Rejected"]:
            click.echo("ERROR: You must select between these status:")
        else:
            return status

@click.command()
def add():
    task = input("Name of the new task\n\n>")
    description = input("Add a description for the task\n\n>")
    priority = get_priority()
    status = get_status()

    # Usar manejo de contexto para la conexión a la base de datos
    with sqlite3.connect("task-manager.db") as conexion:
        cursor = conexion.cursor()
        try:
            # Usar parámetros en la consulta SQL para evitar interpolación de cadenas
            cursor.execute("INSERT INTO tasks (name, description, priority, status) VALUES (?, ?, ?, ?)", (task, description, priority, status))
        except sqlite3.IntegrityError:
            print("The category '{}' already exists, please try another one.".format(task))
        else:
            print("Category '{}' created".format(task))
