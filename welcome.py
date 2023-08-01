import click

@click.command()
@click.option("--name", prompt="Enter your name: ", help="The name of the user")
def welcome(name):
    click.echo("Welcome {} to your favorite tasks manager app!".format(name))
    click.echo("This application allows you to manage your tasks and projects.")
    click.echo("Use the following commands to start managing:")
    click.echo("  add - Add a new task")
    click.echo("  delete - Delete a task")
    click.echo("  list - List all tasks")
    click.echo("  update - Update the status of a task")
    click.echo("  view - View details of a task")