import click

from .locations import config_file

def create_config_file() -> None:
    f = config_file()
    if f.exists():
        return

    try:
        f.touch()
    except OSError:
        pass

@click.command()
def cli():

   pass 