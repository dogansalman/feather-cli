import click

from app import application

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type= str, help='Name of feather applicatin')
@click.option('-db', '--dbname', type= str, help='Name of database')
@click.option('-u', '--user', type= str, help='Name of database user')
@click.option('-p', '--userpass', type= str, help='Password of database user')
@click.option('-h', '--host', type= str, default="localhost", help='Database address. default is localhost')
@click.option('-pt', '--port', type= int, default=5432, help='Port of database. default is 5432')

def new(name, dbname, user, userpass, host, port):
    logo = """
    +--------------------------------------------+
    | Feather CLI Thank you for using featherERP |
    +--------------------------------------------+
    """
    click.echo(logo)
    application.new(user, userpass, dbname, host, port)
    