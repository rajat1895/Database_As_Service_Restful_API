import ssl

import certifi
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://rajat1895:Liv1895@mydb.o3ja5gs.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)