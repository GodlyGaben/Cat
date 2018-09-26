import random

class pirate():
    firstname = "Amory"
    nickname = "Squealer"
    lastname = "Addington"
    fullname = "Amory 'Squealer' Addington"

    fullList = ["Amory 'Squealer' Addington", "Mr. Sir", "Twinkie", "Twinkletoes" ,  "Stereotypical Irish Man"]
    def __init__ (self, fullname):
        self.fullname = fullname

    def CreateName(self):
        x = random.randint(0, (self.fullList) - 1)
        return self.fullList[x]

mypirate = pirate("Andrew")
print(mypirate.CreateName())
