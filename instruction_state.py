import intro_state
import ingredient_state
import dbInteface
import re

class InstructionState:

	def __init__(self, name, position, ing_state, savepos):
		
		if ing_state:
			self.ing_state = ing_state
		
		self.recipe_name = name
		recipe = dbInteface.RecipeInfo(name)
		if savepos == None:
			self.step = position;
		else:
			self.step = savepos
		instruction = recipe.getInstructionsAt(position)
		self.done = False
		
		if (instruction == "Error1"):
			self.text = "Sorry, there is no previous step."
			if savepos == None:
				self.step = position + 1
		elif (instruction == "Error2"):
			self.text = "The recipe is complete. Thank you"
			if savepos == None:
				self.step = position - 1
			self.done = True
		else :
			if savepos == None:
				self.step = position  #boundary check missing
			self.text = "Ok, step " + str(position) + " " + instruction + ". " + "Let me know when you are ready to continue <n>."

	def update(self, text):
		
		numberdict = {"ONE":1, "1":1,"TWO":2,"2":2,"THREE":3,"3":3,
		"FOUR":4,"4":4,"FIVE":5,"5":5,"5":5,"SIX":6,"6":6,
		"SEVEN":7, "7":7,"EIGHT":8, "8":8,"NINE":9,"9":9,"TEN":10,"10":10}
	
		if (self.done == True):
			#seld.done = False
			return intro_state.IntroState("NotNone")
			
		confirmations = dbInteface.Filter("confirmations").getFilter()
		for affirm in confirmations:
			if affirm.upper() in text:
				return InstructionState(self.recipe_name, self.step + 1, self.ing_state, None)

		
		previous = dbInteface.Filter("previous").getFilter()
		for affirm in previous:
			if affirm.upper() in text:
				return InstructionState(self.recipe_name, self.step - 1, self.ing_state, None)
		
		
		step = dbInteface.Filter("step").getFilter()
		for affirm in step:
			if affirm.upper() in text:
				print(text)
				split_text = text.split()
				sno = split_text[split_text.index(affirm.upper()) + 1]
				stepNo = numberdict[sno]
				print(stepNo)
				if type(stepNo) is int:
					return InstructionState(self.recipe_name, stepNo, self.ing_state, self.step)
						
		
		
		matchobj = re.search(r'INGREDIENT',text)
		if matchobj:
			self.ing_state = self.ing_state.update(text)
			self.text = self.ing_state.getText()

		return self

		
	def getText(self):
		return self.text
		