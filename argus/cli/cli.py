import click


@click.group()
@click.version_option()
@click.pass_context
def cli(ctx: click.Context):
    """Aplicação para auditorar as convocações da SEDUC"""
    ...
