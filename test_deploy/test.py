import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--left", type=int)
@click.option("--right", type=int)
def sum(left, right):
    print(f"{left + right}")


@cli.command()
@click.option("--text", type=str)
def echo(text):
    print(text)
