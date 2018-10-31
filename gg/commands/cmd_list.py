import click
from gg.cli import pass_context
from gg.db import list_from_db


@click.command("list", short_help="List all available scrapers.")
@pass_context
def cli(ctx):
    """
    For now, this simply spits out the routes route, but @TODO: I think it
    would be good to enumerate the routes as they go into the database. (e.g.
    use a GET requester at `/routes` to get all routes, then they would simply
    be listed back here.)
    """
    ctx.log("Listing all registered scrapers!\n")
    all_docs = list_from_db()
    for doc in all_docs:
        ctx.log("Name: {}".format(doc['name']))
        ctx.log("Routes: {}\n".format(doc['routes']))
