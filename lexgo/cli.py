import click


@click.group()
@click.version_option()
def cli():
    "A lexicon search tool for language teachers and students. Explore word patterns in any language. "


@cli.command(name="command")
@click.argument(
    "example"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
