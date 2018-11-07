import json
from tkinter import *
from random import randint
from firebase import firebase as fb
class Pirate:
    name = ""
    ship = ""
    fictional = False

    def getDict(self):
        d = {"name": self.name,
             "ship":self.ship,
             "fictional":self.fictional}
        return d
    def loadFromDict(self, d):
        self.name = d["name"]
        self.name = d["ship"]
        self.fictional = d["fictional"]

class FirebasManager:
    app = fb.FirebaseApplication("https://pirate-to-the-db.firebaseio.com/", None)
    
    def writeToFile(self, idNum, obj):
        result = self.app.put("",idNum,obj)

def addNew():
    p = Pirate()
    p.name = namebox.get()
    p.ship = shipbox.get()
    p.fictional = optionString.get()

    namebox.delete(0,"end")
    shipbox.delete(0,"end")

    d = p.getDict()
    fm = FirebaseManager()
    idNum = randint(11111, 99999)
    fm.writeToFile(idNum, d)
        
root = Tk()
root.title("Pirate Database")
title = Label(root, text="Pirate Database", font="fixedsys 25 bold")
nametext = Label(root, text="Name", font="fixedsys 15")
namebox = Entry(root, font="fixedsys 15")
shiptext = Label(root, text="Ship", font="fixedsys 15")
shipbox = Entry(root, font="fixedsys 15")
fictext = Label(root, text="Fictional", font="fixedsys 15")
savebtn = Button(root, text="SAVE", font="fixedsys 15", command=addNew)

title.grid(row=0, column=0, columnspan=3)
nametext.grid(row=1, column=0)
namebox.grid(row=1, column=1)
shiptext.grid(row=2, column=0)
shipbox.grid(row=2, column=1)
fictext.grid(row=3, column=0)
savebtn.grid(row=4, column=0, columnspan=2)

optionString = StringVar(root)
optionString.set("True")
dropdown = OptionMenu(root, optionString, "True", "False")
dropdown.config(font = "fixedsys 15", width="10")
dropdown.nametowidget(dropdown.menuname).config(font="fixedsys 15")
dropdown.grid(row=3, column=1)

root.mainloop()

