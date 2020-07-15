from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI)
db = client['TFG']
usuario = db['DIRECCIONES']
##usuario.insert_one({"_id":"MAC","IPPrivada":"192.168.0.5","IPPublica":"1.1.1.1"})

def insertIp(mac, ipPrivada, ipPublica):
    usuario.insert_one({"_id":mac,"IPPrivada":ipPrivada,"IPPublica":ipPublica})

def listAllIps():
    for document in usuario.find({}):
        print(document)

def findByPublicIp(ipPublica):
    doc = usuario.find_one({
        "IPPublica" : ipPublica
    })
    print(doc)

def updateIp(mac, ipPrivada, ipPublica):
    usuario.update_one({
        "_id":mac
        }, {
        "$set":{
            "IPPrivada":ipPrivada, "IPPublica":ipPublica
        }
        })

#insertIp("MACdonals", "BURGER", "king")
listAllIps()
updateIp("MACdonals", "Masto", "king")
findByPublicIp("king")
