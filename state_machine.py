from ingredient_state import*
from intro_state import*

class StateMachine:
	def __init__(self):
		self.state = IntroState()
		
	#This is going to filter the text input and pass it to the current state.
	#The current state will determine the correct transition to make
	#and will return the correct state.
	def update(self, text):
		text = self.filter(text)
		self.state = self.state.update(text) #We update the state. This will transition if needed.
		return self.state.getText() #Now we can return the resulting text for the current state.
 
 	def filter(self, text):
 		#This is where we can perform filtering and word replacement
 		#on the input text.
 		return text