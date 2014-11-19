import dbInteface
import intro_state

class IngredientState:

	def __init__(self, name):
		self.recipe_name = name
		recipe = dbInteface.RecipeInfo(name)
		self.text = "YOU WILL NEED; "
		ingredients = recipe.getIngredients()
		count = 0
		for ingredient in ingredients:
			count += 1
			if (len(ingredients) - 1) == count:
				self.text += str(ingredient["qty"]) + " " + ingredient["measure"] + " " + ingredient["name"] + ", and "
			elif len(ingredients) == count:
				self.text += str(ingredient["qty"]) + " " + ingredient["measure"] + " " + ingredient["name"] + "."
			else:
				self.text += str(ingredient["qty"]) + " " + ingredient["measure"] + " " + ingredient["name"] + ", "
		
	def update(self, text):
		if "RETURN" in text:
			return intro_state.IntroState()
		else:
			return self
	
	def getText(self):
		return self.text