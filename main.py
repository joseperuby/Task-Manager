# Modules
import sqlite3
import click

# Local imports
from delete_task import delete
from welcome import welcome
from add_task import add
from create_db import create_db
from list_task import list_task
from view_task import view
from update_task import update

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
