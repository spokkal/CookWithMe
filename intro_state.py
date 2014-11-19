import ingredient_state
import dbInteface
from pymongo import*

#Intro state will provide for the initial interaction with the user.
#This will include things like saying hello and selection of a recipe.

class IntroState:

	def __init__(self):
		self.text = "HELLO <n>, I AM CHEF. WHAT WOULD YOU LIKE TO COOK TODAY?"
		filter = dbInteface.Filter("recipe_names")
		self.names_list = filter.getFilter()
				
	def update(self, text):
		client = MongoClient()
		for name in self.names_list:
			if name.upper() in text:
				return ingredient_state.IngredientState(name)
		return self
	
	def getText(self):
		return self.text