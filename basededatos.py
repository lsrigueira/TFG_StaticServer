from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI)
db = client['TFG']
usuario = db['DIRECCIONES']
usuario.insert_one({"_id":"ejemplo","IPPrivada":"192.168.0.5","IPPublica":"1.1.1.1"})
