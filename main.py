import pymongo

# Provide the mongoDB localhost url to connect to mongodb
client = pymongo.MongoClient()

# Database Name
database = client[""]

# Collection Name
collection = database['Products']

