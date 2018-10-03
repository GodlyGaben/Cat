import random
from tkinter import *
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class pirate():

    fullList = ["Amory 'Squealer' Addington", "Mr. Sir", "Twinkie", "Twinkletoes" ,  "Stereotypical Irish Man", "The Dapper Cadaver"]
    def __init__ (self, fullname):
        self.fullname = fullname

    def CreateName(self):
        x = random.randint(0, len(self.fullList) - 1)
        return self.fullList[x]

#mypirate = pirate("Andrew")
#print(mypirate.CreateName())

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def showName():
    full = ftext.get()
    ftext.config(text="")
    ftext.delete(0, "end")
    mygen = pirate(full)
    pirateOutput = mygen.CreateName()
    output.config(text=pirateOutput)
   
root = Tk()
myfont = "SegoeScript 14"

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
title = Label(root, text="A life of scurvy awaits ye!", font="Script 40")
flabel = Label(root, text="Fullname", font=myfont)
bshow = Button(root, text="Generate a new name.", font=myfont, command=showName)
output = Label(root)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
title.grid(row=0, column=0, columnspan=2)
flabel.grid(row=1, column=2)
ftext = Entry (root, font=myfont)
bshow.grid(row = 1, column = 5)
output.grid(row = 3, column = 2)
root.mainloop ()
