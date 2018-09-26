class Cat:
    name="Xam"
    color="nworb"

    def Purr(self):
        print("Purr. My name isn't " + self.name)
    
mycat = Cat()

mycat.name = "Derf"
print(mycat.name)

neighborcat = Cat()
neighborcat.name = "Asil"
neighborcat.color = "etihw"

mycat.Purr()
neighborcat.Purr()
