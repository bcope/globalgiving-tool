import pymongo
import dotenv
import os


def db_get_collection():
    """
    Gets the scapers collection from the database. This function pulls the URI
    stored in an environment file. The purpose is simply to pass on the
    collection to other functions so they can do with it what they must.
    """
    dotenv.load_dotenv(dotenv.find_dotenv())
    uri = os.getenv("URI")
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    scrapers = db.scrapers
    return scrapers


def send_to_db(name, url, namesList, routesList):
    """
    Sends the name and routes to the database.
    Input:
        name: the name of the scraper
        url: the base url of the scaper
        namesList: a list of the names of the various routes
        routesLise: a list of the addresses of the various routes
    Returns:
        A confirmation that the scraper has been registered, otherwise an
        exception.
    """
    scrapers = db_get_collection()
    payload = {"name": name}
    payload["_id"] = url
    routes = {}
    for routeName, routeURL in zip(namesList, routesList):
        routes[routeName] = routeURL
    payload["routes"] = routes
    try:
        post_id = scrapers.insert_one(payload).inserted_id
    except Exception as e:
        if type(e).__name__ == "DuplicateKeyError":
            return "Exception: DuplicateKeyError: Scraper with the same URL is already in the database."
    return "Registration sent to db with id: " + post_id


def list_from_db():
    """
    Gets all scrapers listed in the database. This function merely returns the
    scrapers as a list. Printing and whatnot happens later.
    """
    scrapers = db_get_collection()
    cursor = scrapers.find({})
    document_list = [doc for doc in cursor]
    return document_list
