import click, requests
from globalgiving.db import list_from_db
from globalgiving.cli import pass_context


@click.command("test", short_help="Test a scraper")
@click.argument("n", required=True, type=str)
@pass_context
def cli(ctx, n):
    search = "Finding scraper {} from list of registered scrapers..."
    ctx.log(search.format(n))
    try:
        scrapers = list_from_db()
        route = list(filter(lambda scraper: scraper["name"] == str(n), scrapers))[0][
            "routes"
        ]["Test"]
        ctx.log("Scraper {} found!".format(n))
    except StopIteration:
        ctx.log("Scraper {} not found.".format(n))
        return
    contents = requests.get(route).text
    print(contents)
