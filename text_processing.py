from state_machine import *

class Initial_State:

	def __init__(self):
		self.name = ''
		self.complete = False
		
	def check_state(self, text):
		split_text = text.split()
		if "MY NAME" in text: 
			self.name = split_text[split_text.index('IS') + 1] 
			self.complete = True
			return
		if "THEY CALL ME" in text:
			self.name = split_text[split_text.index('ME') + 1] 
			self.complete = True
			return
		if "I AM" in text:
			self.name = split_text[split_text.index('AM') + 1] 
			self.complete = True
			return
		if "I'M" in text:
			self.name = split_text[split_text.index("I'M") + 1]
			self.complete = True
			return
			
			
			
class Text_Processing:
	
	def process(self, text, context):
  		context.check_state(text)
		if "HELLO" in text: 
			text = "HELLO WHAT WOULD YOU LIKE TO COOK TODAY"
			print(context.name + "Name")
 			if context.complete:
 				text = "HELLO " + context.name + " WHAT WOULD YOU LIKE TO COOK TODAY"
		text = text.replace("CHEF", "")

		if "CHOCOLATE MILK" in text:
			text = "Chocolate Milk. Step 1: Pour milk into a glass. Step 2: Add cocoa powder to the glass and stir well. Chocolate milk is ready."

		return text