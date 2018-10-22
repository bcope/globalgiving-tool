# import pymongo

# from pymongo import MongoClient

# import datetime

# client = MongoClient()

# client = MongoClient('localhost', 27017)

# client = MongoClient('mongodb://localhost:27017/')

# db = client.test_database
# print(db)
# db = client['test-database']

# collection = db.test_collection

# collection = db['test-collection']


# # post = {"author": "Mike",
# #     "text": "My first blog post!",
# #     "tags": ["mongodb", "python", "pymongo"],
# #     "date": datetime.datetime.utcnow()}

# # print(db.posts)

# # posts = db.posts
# # post_id = posts.insert_one(post).inserted_id

# # print(post_id)

# db.my_collection.insert_one({"x": 10}).inserted_id

import pymongo

SEED_DATA = [
    {
        'decade': '1970s',
        'artist': 'Debby Boone',
        'song': 'You Light Up My Life',
        'weeksAtOne': 10
    },
    {
        'decade': '1980s',
        'artist': 'Olivia Newton-John',
        'song': 'Physical',
        'weeksAtOne': 10
    },
    {
        'decade': '1990s',
        'artist': 'Mariah Carey',
        'song': 'One Sweet Day',
        'weeksAtOne': 16
    }
]

uri = "mongodb://aria:malkani28@ds139243.mlab.com:39243/gg-db"
client = pymongo.MongoClient(uri)
db = client.get_default_database()
print(db)
songs = db['songs']
songs.insert_many(SEED_DATA)

query = {'song': 'One Sweet Day'}
cursor = songs.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)
print(cursor)
for doc in cursor:
    print ('In the %s, %s by %s topped the charts for %d straight weeks.' %
            (doc['decade'], doc['song'], doc['artist'], doc['weeksAtOne']))

db.drop_collection('songs')