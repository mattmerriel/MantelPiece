import click
import logging

from .locations import config_file

logger = logging.getLogger('main')

def create_config_file() -> None:
    f = config_file()
    if f.exists():
        return

    try:
        f.touch()
    except OSError:
        pass

@click.group(invoke_without_command=True)
def cli():
    logger.debug('Mantelware cli Started')
    print(f'This is a test!')

@cli.command()
def validate():
    logger.info('Validating Date!')