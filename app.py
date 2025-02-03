from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import datetime

app = Flask(__name__)

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

@app.route("/")
def index():
    # Fetch the latest 5 articles from MongoDB (dummy data for now)
    articles = collection.find().sort("publication_date", -1).limit(5)
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
