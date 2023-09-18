import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--text", type=str)
def echo(text):
    print(text)
