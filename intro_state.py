import ingredient_state
from pymongo import*

#Intro state will provide for the initial interaction with the user.
#This will include things like saying hello and selection of a recipe.

class IntroState:

	def __init__(self):
		self.text = "HELLO, I AM CHEF. WHAT WOULD YOU LIKE TO COOK TODAY?"
		self.names_list = {"Grilled Cheese", "Roasted Chicken", "Roasted Vegetables", "Brownies", "Loaf Cake"} 
				
	def update(self, text):
	
		client = MongoClient()
		for name in self.names_list:
			if name.upper() in text:
				return ingredient_state.IngredientState(name)
		
		return self
	
	def getText(self):
		return self.text