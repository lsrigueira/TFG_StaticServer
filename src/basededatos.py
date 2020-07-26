from pymongo import MongoClient
class mybd:
    MONGO_URI = "mongodb://localhost"
    client = MongoClient(MONGO_URI)
    db = client['TFG']
    usuario = db['DIRECCIONES']
    ##usuario.insert_one({"_id":"MAC","IPPrivada":"192.168.0.5","IPPublica":"1.1.1.1"})
    def __init__(self, MONGO_URI = "mongodb://localhost"):
        super().__init__()
        self.MONGO_URI = MONGO_URI

    def insertIp(self, mac, ipPrivada, ipPublica):
        self.usuario.insert_one({"_id":mac,"IPPrivada":ipPrivada,"IPPublica":ipPublica})

    def listAllIps(self):
        for document in self.usuario.find({}):
            print(document)

    def findByPublicIp(self, ipPublica):
        doc = self.usuario.find_one({
            "IPPublica" : ipPublica
        })
        return doc.get("IPPrivada")

    def updateIp(self, mac, ipPrivada, ipPublica):
        self.usuario.update_one({
            "_id":mac
            }, {
            "$set":{
                "IPPrivada":ipPrivada, "IPPublica":ipPublica
            }
            })

    #insertIp("MACdonals", "BURGER", "king")
    #listAllIps()
    #updateIp("MACdonals", "Masto", "king")
    #findByPublicIp("king")
