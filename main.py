# Modules
import sqlite3
import click

# Local imports
from commands.delete_task import delete
from commands.welcome import welcome
from commands.add_task import add
from commands.create_db import create_db
from commands.list_task import list_task
from commands.view_task import view
from commands.update_task import update

# Functions
@click.group(help="Welcome to your favorite tasks manager app!")
def menu():
    pass

menu.add_command(delete)
menu.add_command(welcome)
menu.add_command(add)
menu.add_command(create_db)
menu.add_command(update)
menu.add_command(list_task)
menu.add_command(view)

if __name__ == "__main__":
    menu()
