import random
from tkinter import *

class pirate():

    fullList = ["Amory 'Squealer' Addington", "Mr. Sir", "Twinkie", "Twinkletoes" ,  "Stereotypical Irish Man"]
    def __init__ (self, fullname):
        self.fullname = fullname

    def CreateName(self):
        x = random.randint(0, len(self.fullList) - 1)
        return self.fullList[x]

#mypirate = pirate("Andrew")
#print(mypirate.CreateName())

root = Tk()
myfont = "SegoeScript 14"
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
banner = PhotoImage(file="paper.gif")
banner = banner.subsample(2,2)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
title = Label(root, text="A life of scurvy awaits ye!", font="Script 40")

flabel = Label(root, text="Fullname", font=myfont)

bshow = Button(root, text="Generate a new name.", font=myfont)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
title.grid(row=0, column=0, columnspan=2)

flabel.grid(row=1, column=2)

ftext = Entry (root, font=myfont)

bshow.grid(row = 1, column = 5)

ftext.grid(row = 2, column = 2)

root.mainloop ()
