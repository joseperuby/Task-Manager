import click
import sqlite3

def update_name(task_id):
    with sqlite3.connect("task-manager.db") as conexion:
        cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    new_id = input("Insert the new Name\n>")
    cursor.execute("UPDATE tasks SET name= ? WHERE id= ?", (new_id, task_id))
    conexion.commit()
    conexion.close()
    click.echo("Task updated successfully.")

def update_id(task_id):
    with sqlite3.connect("task-manager.db") as conexion:
        cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    new_id = input("Insert the new ID\n>")
    try:
        cursor.execute("UPDATE tasks SET id= ? WHERE id= ?", (new_id, task_id))
        conexion.commit()
        conexion.close()
        click.echo("Task updated successfully.")
    except sqlite3.IntegrityError:
        click.echo("ERROR: You must insert a number!")


def update_description(task_id):
    with sqlite3.connect("task-manager.db") as conexion:
        cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    new_id = input("Insert the new Description\n>")
    cursor.execute("UPDATE tasks SET description= ? WHERE id= ?", (new_id, task_id))
    conexion.commit()
    conexion.close()
    click.echo("Task updated successfully.")

def update_priority(task_id):
    with sqlite3.connect("task-manager.db") as conexion:
        cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    priorities = ["O", "L", "M", "H", "C"]
    while True:
        new_id = input("Insert the new Priority\n>")
        if new_id in priorities:
            cursor.execute("UPDATE tasks SET priority= ? WHERE id= ?", (new_id, task_id))
            conexion.commit()
            conexion.close()
            click.echo("Task updated successfully.")
            break
        else:
            click.echo("ERROR: You must select between these letters:")
            click.echo("\nO:\tOptional")
            click.echo("L:\tLow")
            click.echo("M:\tMedium")
            click.echo("H:\tHigh")
            click.echo("C:\tCrucial")

def update_status(task_id):
    with sqlite3.connect("task-manager.db") as conexion:
        cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    statuses = ["Pending", "Started", "Completed", "Revision", "Canceled", "Paused", "Rejected"]
    while True:
        new_id = input("Insert the new Status\n>")
        if new_id in statuses:
            cursor.execute("UPDATE tasks SET status= ? WHERE id= ?", (new_id, task_id))
            conexion.commit()
            conexion.close()
            click.echo("Task updated successfully.")
            break
        else:
            click.echo("ERROR: You must select between these letters:")
            click.echo("\nPending:\tThe task has been created but work has not started yet.")
            click.echo("Started:\tWork on the task has begun but it is not yet completed.")
            click.echo("Completed:\tThe task has been finished and meets all requirements.")
            click.echo("Revision:\tThe task has been completed, but it requires review and approval before being considered fully finished.")
            click.echo("Canceled:\tThe task has been canceled and will not be continued.")
            click.echo("Paused:\t\tThe task has been temporarily stopped and is not currently being worked on.")
            click.echo("Rejected:\tThe task is considered unfeasible or unnecessary after a review.")

def update_all(task_id):
    with sqlite3.connect("task-manager.db") as conexion:
        cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    statuses = ["Pending", "Started", "Completed", "Revision", "Canceled", "Paused", "Rejected"]
    priorities = ["O", "L", "M", "H", "C"]
    new_id = input("Insert the new ID\n>")
    new_name = input("Insert the new Name\n>")
    new_description = input("Insert the new Description\n>")
    new_priority = input("Insert the new Priority\n>")
    if new_priority in priorities:
        new_status = input("Insert the new Status\n>")
        if new_status in statuses:
            try:
                cursor.execute("UPDATE tasks SET id= ?, name= ?, description = ?, priority = ?, status = ? WHERE id= ?", (new_id, new_name, new_description, new_priority, new_status, task_id))
                conexion.commit()
                conexion.close()
                click.echo("Task updated successfully.")
            except sqlite3.IntegrityError:
                click.echo("ERROR: Your ID must be a number!")
        else:
            click.echo("ERROR: You must select between these letters:")
            click.echo("\nPending:\tThe task has been created but work has not started yet.")
            click.echo("Started:\tWork on the task has begun but it is not yet completed.")
            click.echo("Completed:\tThe task has been finished and meets all requirements.")
            click.echo("Revision:\tThe task has been completed, but it requires review and approval before being considered fully finished.")
            click.echo("Canceled:\tThe task has been canceled and will not be continued.")
            click.echo("Paused:\t\tThe task has been temporarily stopped and is not currently being worked on.")
            click.echo("Rejected:\tThe task is considered unfeasible or unnecessary after a review.")

    else:
        click.echo("ERROR: You must select between these letters:")
        click.echo("\nO:\tOptional")
        click.echo("L:\tLow")
        click.echo("M:\tMedium")
        click.echo("H:\tHigh")
        click.echo("C:\tCrucial")

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
                update_id(task_id)
                break
            elif option == "2":
                update_name(task_id)
                break
            elif option == "3":
                update_description(task_id)
                break
            elif option == "4":
                update_priority(task_id)
                break
            elif option == "5":
                update_status(task_id)
                break
            elif option == "6":
                update_all(task_id)
                break
            else:
                click.echo("Error, please choose a number")

            