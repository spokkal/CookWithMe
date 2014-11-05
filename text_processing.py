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
			
			
			
class Text_Processing:
	
	def process(self, text, context):
  		context.check_state(text)
		if "HELLO" in text: 
			text = "HELLO WHAT WOULD YOU LIKE TO COOK TODAY"
			print(context.name + "Name")
 			if context.complete:
 				text = "HELLO " + context.name + " WHAT WOULD YOU LIKE TO COOK TODAY"
		text = text.replace("CHEF", "")
		return text