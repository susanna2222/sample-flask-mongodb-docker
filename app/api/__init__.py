import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
# mongoClient = pymongo.MongoClient("mongodb://mongodb:27017/")
mongoDB = mongoClient["mhm_app"]
dblist = mongoClient.list_database_names()

if "mhm_app" in dblist:
  print("mhm_app database exists.")
else:
  print("mhm_app database not exists.")

# collist = mongoDB.list_collection_names()
# if "users" in collist:
#   print("Collection: users exists.")
# else:
#   print("Collection: users not exists.")