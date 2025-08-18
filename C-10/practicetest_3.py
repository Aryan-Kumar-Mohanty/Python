from random   import randint

class Train:
    def __init__(self,trainno):
        self.trainno=trainno
        pass
    def book(self,fro,to):
        print(f"Ticket is booked in{self.trainno} from {fro} to {to}")
        pass
    def getstatux(self):
        print(f"Train no {self.trainno}is running successfully")
        pass
    def getfare(self,fro,to):
        print(f"Ticket fare in {self.trainno} from {fro} to {to} is {randint(222,5555)}")
        pass

t=Train(12234)
t.book("Bhubanewar","puri")
t.getfare("Bhubaneswar","puri") 
t.getstatux()  