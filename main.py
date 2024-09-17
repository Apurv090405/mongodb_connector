from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://apurvchudasamaedu:vt7dqUuHUqqlzYIs@cluster0.m3uju.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Define the database and collection
db = client['test_database']  # Replace 'test_database' with your database name
collection = db['test_collection']  # Replace 'test_collection' with your collection name

# Data to insert
data = {
    "name": "Apurv Chudasama",
    "age": 20,
    "email": "apurv@chudasama.com"
}

# Insert data into the collection
try:
    result = collection.insert_one(data)
    print(f"Data inserted with ID: {result.inserted_id}")
except Exception as e:
    print(f"Insert Error: {e}")

# Fetch data from the collection
try:
    data_fetched = collection.find()  # Use .find() to get all documents or you can use .find_one() for one document
    for doc in data_fetched:
        print(doc)
except Exception as e:
    print(f"Fetch Error: {e}")
