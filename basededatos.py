from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI)
db = client['TFG']
usuario = db['DIRECCIONES']
##usuario.insert_one({"_id":"MAC","IPPrivada":"192.168.0.5","IPPublica":"1.1.1.1"})


#mostrar todos
for document in usuario.find({}):
    print(document)

#mostar o buscado
doc = usuario.find_one({
    "IPPublica": "1.1.1.1"
})
print(doc)

##update
usuario.update_one({
    "IPPublica":"1.1.1.1"
    }, {
    "$set":{
        "IPPrivada":"This IP bitch"
    }
    })

#mostar o buscado
doc = usuario.find_one({
    "IPPublica": "1.1.1.1"
})
print(doc)