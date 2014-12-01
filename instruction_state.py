import intro_state
import ingredient_state
import dbInteface
import re

class InstructionState:

	def __init__(self, name, position, ing_state):
		
		if ing_state:
			self.ing_state = ing_state
		
		self.recipe_name = name
		recipe = dbInteface.RecipeInfo(name)
		self.step = position;
		instruction = recipe.getInstructionsAt(position)
		self.done = False
		
		if (instruction == "Error1"):
			self.text = "Sorry, there is no previous step."
			self.step = position + 1
		elif (instruction == "Error2"):
			self.text = "The recipe is complete. Thank you"
			self.step = position - 1
			self.done = True
		else :
			self.step = position  #boundary check missing
			self.text = "Ok, step " + str(position) + " " + instruction + ". " + "Let me know when you are ready to continue <n>."
		
	def update(self, text):
		if (self.done == True):
			#seld.done = False
			return intro_state.IntroState("NotNone")
			
		confirmations = dbInteface.Filter("confirmations").getFilter()
		for affirm in confirmations:
			if affirm.upper() in text:
				return InstructionState(self.recipe_name, self.step + 1, None)

		
		previous = dbInteface.Filter("previous").getFilter()
		for affirm in previous:
			if affirm.upper() in text:
				return InstructionState(self.recipe_name, self.step - 1, None)
		
		matchobj = re.search(r'INGREDIENTS',text)
		if matchobj:
			self.ing_state = self.ing_state.update(text)
			self.text = self.ing_state.getText()

		return self

		
	def getText(self):
		return self.text
		