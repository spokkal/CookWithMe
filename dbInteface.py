from pymongo import MongoClient

client = MongoClient()					#Creata MongoClient objects
db = client.CookWithMe					#Create instance of the CookWithMe  database
col = db.recipes						#Use the collection recipes 

class RecipeInfo(object):
	""" This class has the methods to access the database CookWithMe(MongoDB) 
		and returns the information regarding the recipe, such as the ingredients, 
		instructions etcetera.
	"""
	
	def __init__(self, recipeName):
		self.recipeName = 	recipeName
		self.recipe		=	col.find({"name":recipeName})	#if the recipe is None then there is no such and inform the user.
		
		
	def get(self):
		return self.recipe;
		
	def getIngredients(self):
		return self.recipe["ingredients"]
		
	def getInstructions(self):
		return self.recipe["instructions"]
	
	def getInstructions(self, number):
		if(number < 1):
			return self.recipe["instructions"][number-1]
		return None
		