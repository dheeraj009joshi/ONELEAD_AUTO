import certifi
from pymongo import MongoClient
import ssl
uri = "mongodb+srv://dlovej009:Dheeraj2006@cluster0.dnu8vna.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri,tlsCAFile=certifi.where())
db = client['CRM_USER']
collection = db['USERS']