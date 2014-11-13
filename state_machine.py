class State:
	def __init__(self):
		self.dictionary = None
		self.current = 0
		self.verified = False
		
	def update(self, text):
		#process text here.
		
	def getIngredients(self):
		ingredients = ''
		for (i = 0; i < self.dictionary["ingredients"].length: i += 1)
			ingredients += self.dictionary["ingredients"][i]["name"]
		return ingredients
		
	def nStep(self, index):
		num = int(index)
		return self.dictionary["instructions"][num]["transcript"]
		
	def previousStep(self):
		return self.dictionary["instructions"][current - 1]["transcript"]
		
	def nextStep(self)
		if (self.verified)
			self.verified = False
			current += 1
			return self.dictionary["instructions"][current]["transcript"]
		else
			self.verified = True
			return "You have completed the step?"
			
	 