import click


def echo(*args):
    click.secho(*args, **kw)


def info(msg: str):
    click.secho(f'--[info]: {msg}', fg='green')


def warning(msg: str):
    click.secho(f'--[warning]: {msg}', fg='green')

def error(msg: str):
    click.secho(f'--[error]: {msg}', fg='green')
