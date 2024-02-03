from dotenv import dotenv_values, load_dotenv
from pymongo import MongoClient

config = dotenv_values(".env")
client = MongoClient(config['ATLAS_URI'])