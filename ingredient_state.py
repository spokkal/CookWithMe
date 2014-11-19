import dbInteface
import intro_state
import instruction_state

class IngredientState:

	def __init__(self, name):
		self.recipe_name = name
		recipe = dbInteface.RecipeInfo(name)
		ingredients = recipe.getIngredients()
		self.text = "OK <n>, YOU WILL NEED; "
		count = 0
		for ingredient in ingredients:
			count += 1
			if (len(ingredients) - 1) == count:
				self.text += str(ingredient["qty"]) + " " + ingredient["measure"] + " " + ingredient["name"] + ", and "
			elif len(ingredients) == count:
				self.text += str(ingredient["qty"]) + " " + ingredient["measure"] + " " + ingredient["name"] + "."
			else:
				self.text += str(ingredient["qty"]) + " " + ingredient["measure"] + " " + ingredient["name"] + ", "
		self.text += " WOULD YOU LIKE TO CONTINUE?"
		
	def update(self, text):
		if "RETURN" in text:
			return intro_state.IntroState()
		elif "YES" in text:
			return instruction_state.InstructionState(self.recipe_name, 1)
		else:
			return self
	
	def getText(self):
		return self.text