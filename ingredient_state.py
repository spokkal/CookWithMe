import dbInteface
import intro_state
import instruction_state

class IngredientState:
	def __init__(self, name):
		self.recipe_name = name
		recipe = dbInteface.RecipeInfo(name)
		r = recipe.get()
		self.ingredients = recipe.getIngredients()
		self.text = self.getIngredients()
		self.text += "Would you like to continue?"
		
		
	def update(self, text):
		filter = dbInteface.Filter("confirmations")
		self.conf_list = filter.getFilter()
		
		if "RETURN" in text:
			return intro_state.IntroState()			
		for conf in self.conf_list:
			if conf.upper() in text:
				return instruction_state.InstructionState(self.recipe_name, 1, self, None, None)
		if self.getOneIngredient(text) != None:
			self.text = self.getOneIngredient(text)
		elif "REPEAT" in text or "AGAIN" in text:
			self.text = self.getIngredients()
		else:
			self.text = "Please say Repeat to hear the ingredients, Return to go back or Continue to start cooking."
		return self
	
	def getIngredients(self):
		text = "OK <n>, for "+self.recipe_name+" you will need: "
		count = 0
		for ingredient in self.ingredients:
			count += 1
			if (len(self.ingredients) - 1) == count:
				text += str(ingredient["qty"]) + " " + ingredient["measure"] + " " + ingredient["name"] + ", and "
			elif len(self.ingredients) == count:
				text += str(ingredient["qty"]) + " " + ingredient["measure"] + " " + ingredient["name"] + "."
			else:
				text += str(ingredient["qty"]) + " " + ingredient["measure"] + " " + ingredient["name"] + ", "
		return text
		
	def getOneIngredient(self, ingredient):
		text = None
		for i in self.ingredients:
			if i["name"].upper() in ingredient:
				text = "You will need: "
				text += str(i["qty"]) + " " + i["measure"] + " " + i["name"]
		return text
	
	def getText(self):
		return self.text