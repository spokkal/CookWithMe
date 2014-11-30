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
		instruction = recipe.getInstructionsAt(position)
		self.step = position  #boundary check missing
		self.text = "Ok, step " + str(position) + " " + instruction + ". " + "Let me know when you are ready to continue <n>."
		
	def update(self, text):
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
		