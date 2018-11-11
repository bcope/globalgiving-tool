import click, requests
from gg.db import list_from_db, delete_ngo
from gg.cli import pass_context


@click.command("delete", short_help="Test a scraper")
@click.argument("name", required=True, type=str)
@pass_context
def cli(ctx, name):
    search = "Finding scraper {} from list of registered scrapers..."
    ctx.log(search.format(name))
    try:
        scrapers = list_from_db()
        ngo_id = list(filter(lambda scraper: scraper["name"] == str(name), scrapers))[
            0
        ]["_id"]
        ctx.log("Scraper {} found!".format(name))
    except StopIteration:
        ctx.log("Scraper {} not found.".format(name))
        return
    except IndexError:
        ctx.log("Scraper {} not found.".format(name))
        return
    ctx.log("Deleting scraper {} . . . ".format(name))
    return delete_ngo(ngo_id)
