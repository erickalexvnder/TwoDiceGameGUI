# Must install pip playsound module

# Erick Romero
# Final project
# 4/28/2021

from breezypythongui import EasyFrame
import random
from playsound import playsound
playsound('jigsaw.mp3')


class TwoDiceGame(EasyFrame):
    

	def __init__(self):
	
		EasyFrame.__init__(self, title = "Two Dice Game", resizable = False, background = "orangered4")
		
		self.addLabel(text = "Roll the die. Win or Die!", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "orangered4", foreground = "black").config(font = ("Deadly claws", 40))

        # Player Number

		self.addLabel(text = "You", row = 1, column = 0, sticky = "NSEW", background = "white", foreground = "black").config(font = ("deadlyclaws", 20))
		self.rollOne = self.addIntegerField(value = 0, row = 2, column = 0, rowspan = 2, sticky = "NW")
		self.rollOne["background"] = "white"
		self.rollOne["foreground"] = "black"
		self.rollOne["font"] = 78

        # Jigsaw's Number
		self.addLabel(text = "JIGSAW", row = 1, column = 1, sticky = "NSEW", background ="white", foreground = "black").config(font =("heartless", 35))
		self.rollTwo = self.addIntegerField(value = 0, row = 2, column = 1, rowspan = 2)
		self.rollTwo["background"] = "white"
		self.rollTwo["foreground"] = "black"
		self.rollTwo["font"] = 78

		self.button = self.addButton(text = "Lets play.", row = 4 , column = 0, columnspan = 2, command = self.roll)
		self.button["background"] = "white"
		self.button["foreground"] = "black"
		self.button["font"] = 20

		self.resultArea = self.addLabel(text = "", row = 5 , column = 0, columnspan = 2, rowspan = 3, sticky = "NSEW")
		self.resultArea["background"] = "orangered4"
		self.resultArea["foreground"] = "black"	
		self.resultArea["font"] = 100



	def roll(self):
		roll1 = random.randint(1, 6)
		roll2 = random.randint(1, 6)
		result = ""

		if roll1 > roll2:
			result = "You Live."
		elif roll1 < roll2:
			result = "Jigsaw wins!"
		else:
			 roll1 == roll2
			 result = "Not good enough. No draws. Try Again?"

		self.rollOne.setNumber(roll1)
		self.rollTwo.setNumber(roll2)
		self.resultArea["text"] = result

        

def main():
		TwoDiceGame().mainloop()
main()
