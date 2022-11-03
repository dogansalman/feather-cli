import click

from app import application, repository

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-db', '--dbname', type= str, help='Name of database.')
@click.option('-u', '--user', type= str, help='Name of database user.')
@click.option('-p', '--userpass', type= str, help='Password of database user.')
@click.option('-h', '--host', type= str, default="localhost", help='Database address. default is localhost.')
@click.option('-lp', '--port', type= str, default=5432, help='Port of database. default is 5432')
@click.option('-pt', '--path', type= str, default=repository.default_to_path, help='Feather application installation path.')

def new(dbname, user, userpass, host, port, path):
    logo = """
    +--------------------------------------------+
    | Feather CLI Thank you for using featherERP |
    +--------------------------------------------+
    """
    click.echo(logo)
    application.new(user, userpass, dbname, host, port)
    repository.feather_clone_repo(path)
    