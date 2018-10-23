class Pirate:
    name = " "
    ship = " "
    badass = True
    real = True

    def getDict(self):
        d = {"name":  self.name, "ship": self.ship, "real": self.real, "badass": self.badass}
        return d
    def loadFromDict (self, d):
        self.name = d["name"]
        self.ship = d["ship"]
        self.badass = d["badass"]
        self.real = d["real"]
class FileManager:
    path = "pirateDB.json"

    def writeToFile(self, idNm, obj):
        try:
            f = open(self.patth, "r")
            d = json.load(f)
            f.close()
        except:
            d = ()
            d[idNum] = obj
            f = open(self.path, "w")
            json.dump(d, f)
            f.close ()
        
