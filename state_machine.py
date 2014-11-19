class State:
	def __init__(self):
		self.dictionary = None
		self.current = 0
		self.verified = False
		
	def update(self, text):
		if "BACK" in text:
			return previousStep(text)
		
	def getIngredients(self):
		ingredients = ''
		for i in range (0,self.dictionary["ingredients"].length):
			ingredients += self.dictionary["ingredients"][i]["name"]
		return ingredients
		
	def nStep(self, index):
		num = int(index)
		return self.dictionary["instructions"][num]["transcript"]
		
	def previousStep(self):
		return self.dictionary["instructions"][current - 1]["transcript"]
		
	def nextStep(self):
		if self.verified:
			self.verified = False
			current += 1
			return self.dictionary["instructions"][current]["transcript"]
		else:
			self.verified = True
			return "Have you completed the step?"	 