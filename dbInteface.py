from pymongo import*

class RecipeInfo(object):
	""" This class has the methods to access the database CookWithMe(MongoDB) 
		and returns the information regarding the recipe, such as the ingredients, 
		instructions etcetera.
	"""
	
	def __init__(self, recipeName):
		self.client = MongoClient()					#Creata MongoClient objects
		self.db = self.client.CookWithMe					#Create instance of the CookWithMe  database
		self.col = self.db.recipes						#Use the collection recipes 
		self.recipeName = 	recipeName
		self.recipe		=	self.col.find_one({"name":recipeName})	#if the recipe is None then there is no such and inform the user.
		
		
	def get(self):
		return self.recipe;
		
	def getIngredients(self):
		return self.recipe['ingredients']
		
	def getInstructions(self):
		return self.recipe['instructions']
	
	def getInstructionsAt(self, number):
		if (number > len(self.recipe['instructions'])):
			return "Error2"
		elif(number >= 1):
			return self.recipe['instructions'][number-1]['transcript']
		elif (number < 1):
			return "Error1"
		return None
	
class Filter(object):

	def __init__(self, filterType):
		self.client = MongoClient()					#Creata MongoClient objects
		self.db = self.client.CookWithMe					#Create instance of the CookWithMe  database
		self.col = self.db.filters						#Use the collection recipes 
		self.filterType = 	filterType
		self.filter		=	self.col.find_one({"name":filterType})	#if the recipe is None then there is no such and inform the user.
	
	def getFilter(self):
		return self.filter['filter']
		