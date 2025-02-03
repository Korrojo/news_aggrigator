import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB connection details from environment variables
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')
cluster = os.getenv('MONGODB_CLUSTER')
database = os.getenv('MONGODB_DATABASE')

# Construct the connection string
connection_string = f"mongodb+srv://{username}:{password}@{cluster}/{database}?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(connection_string)
db = client['news_db']
collection = db['news_articles']

dummy_data = [
    {"title": "News 1", "content": "Content for news 1", "publication_date": datetime.datetime.utcnow()},
    {"title": "News 2", "content": "Content for news 2", "publication_date": datetime.datetime.utcnow()},
    {"title": "News 3", "content": "Content for news 3", "publication_date": datetime.datetime.utcnow()}
]

collection.insert_many(dummy_data)
print("Dummy data inserted.")
