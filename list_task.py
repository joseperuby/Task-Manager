import click
import sqlite3

def list_by_id(task_id):
    conexion = sqlite3.connect("task-manager.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?",(task_id,))
    task = cursor.fetchone()
    try:
        click.echo()
        click.echo(f"Task ID:".ljust(20) + f"{task[0]}")
        click.echo(f"Name:".ljust(20) + f"{task[1]}")
        click.echo(f"Description:".ljust(20) + f"{task[2]}")
        click.echo(f"Priority:".ljust(20) + f"{task[3]}")
        click.echo(f"Status:".ljust(20) + f"{task[4]}")
        click.echo("\n")
    except TypeError:
        click.echo(f"ID incorrect, there is no such task with the ID: {task_id}")
        click.echo("Please verify if you have any task created")
    conexion.close()

def list_by_name(task_name):
    conexion = sqlite3.connect("task-manager.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE name = ?",(task_name,))
    tasks = cursor.fetchall()
    for task in tasks:
            click.echo()
            click.echo(f"Task ID:".ljust(20) + f"{task[0]}")
            click.echo(f"Name:".ljust(20) + f"{task[1]}")
            click.echo(f"Description:".ljust(20) + f"{task[2]}")
            click.echo(f"Priority:".ljust(20) + f"{task[3]}")
            click.echo(f"Status:".ljust(20) + f"{task[4]}")
            click.echo("\n")

    conexion.close()

def list_by_priority(task_priority):
    conexion = sqlite3.connect("task-manager.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE priority = ?",(task_priority,))
    tasks = cursor.fetchall()
    for task in tasks:
            click.echo()
            click.echo(f"Task ID:".ljust(20) + f"{task[0]}")
            click.echo(f"Name:".ljust(20) + f"{task[1]}")
            click.echo(f"Description:".ljust(20) + f"{task[2]}")
            click.echo(f"Priority:".ljust(20) + f"{task[3]}")
            click.echo(f"Status:".ljust(20) + f"{task[4]}")
            click.echo("\n")

    conexion.close()

def list_by_status(task_status):
    conexion = sqlite3.connect("task-manager.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks WHERE status = ?",(task_status,))
    tasks = cursor.fetchall()
    for task in tasks:
            click.echo()
            click.echo(f"Task ID:".ljust(20) + f"{task[0]}")
            click.echo(f"Name:".ljust(20) + f"{task[1]}")
            click.echo(f"Description:".ljust(20) + f"{task[2]}")
            click.echo(f"Priority:".ljust(20) + f"{task[3]}")
            click.echo(f"Status:".ljust(20) + f"{task[4]}")
            click.echo("\n")

    conexion.close()

@click.command()
def list():
    conexion = sqlite3.connect("task-manager.db")
    cursor = conexion.cursor()
    click.echo("Choose an option to list tasks:")
    click.echo("1: List all tasks")
    click.echo("2: List task by ID")
    click.echo("3: List task by name")
    click.echo("4: List task by priority")
    click.echo("5: List task by status")
    option = input("\n>")

    if option == "1":
        alphabetic = input("Sort by alphabetic order (Y/N)\n>")
        if alphabetic == "N":
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
        elif alphabetic == "Y":
            cursor.execute("SELECT * FROM tasks ORDER by name ASC")
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
        else:
             click.echo("I dont undestand, sorry")

    elif option == "2":
        list_by_id(task_id=input("Enter the ID of the task you want to view: "))

    elif option == "3":
        list_by_name(task_name=input("Enter the name of the task you want to view: "))

    elif option == "4":
        list_by_name(task_name=input("Enter the priority of the task you want to view: "))

    elif option == "5":
        list_by_name(task_name=input("Enter the status of the task you want to view: "))

    
    conexion.close()
    

