import pymongo
import certifi

con_str = "mongodb+srv://notphilyoder93:KarmasABitch1993!@cluster0.99aarj1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(con_str, tlsCAFile  = certifi.where())
db = client.get_database("107test")