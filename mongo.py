import os
import pymongo
if os.path.exists("env.py"):
    import env


    MONGO_URI = os.environ.get("MONGO_URI")
    DATABASE = "iSandwichDB"
    COLLECTION = "sandwiches"


    def mongo_connect(url):
        try:
            conn = pymongo.MongoClient(url)
            print("Mongo is connected")
            return conn
        except pymongo.errors.ConnectionFailure as e:
            print("Could not connect to MongoDB %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

new_doc = {"name": "BBQ Sandwich", "ingridients": "Bread, butter, bbq sauce from Kentucky, cheese", "instructions": "Just make it juicy and delicious"}

coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)