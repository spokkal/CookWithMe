from ingredient_state import*
from intro_state import*

class StateMachine:
	def __init__(self, text):
		self.state = IntroState(text)
		self.name = ''
		
	#This is going to filter the text input and pass it to the current state.
	#The current state will determine the correct transition to make
	#and will return the correct state.
	def update(self, text):
		
		self.name = self.getName(text)
			
		toReturn = self.filter(text)
		self.state = self.state.update(toReturn) #We update the state. This will transition if needed.
		print self.state
		toReturn = self.state.getText() #Now we can return the resulting text for the current state.
 		toReturn = self.postProcess(toReturn)
 		return toReturn
 		
 		
 	def filter(self, text):
 		toReturn = text
 		#This is where we can perform filtering and word replacement
 		#on the input text.
 		return toReturn
 		
 	def postProcess(self, text):
 		toReturn = text
 		#We can do some post processing on the returned text here.
 		toReturn = toReturn.replace("<n>", self.name) #One post process will be adding the users name to the return text.
 		return toReturn
 		
 	def getName(self, text):
 		split_text = text.split()
		if "MY NAME" in text: 
			return split_text[split_text.index('IS') + 1] 
		elif "THEY CALL ME" in text:
			return split_text[split_text.index('ME') + 1] 
		elif "I AM" in text and "DONE" not in text and "READY" not in text:
			return split_text[split_text.index('AM') + 1] 
		elif "I'M" in text and "DONE" not in text and "READY" not in text:
			return split_text[split_text.index("I'M") + 1]
		else:
			return self.name 
		