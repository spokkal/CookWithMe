from pymongo import MongoClient

cl = MongoClient()
db = cl.CookWithMe
filters = db.filters
filters.remove()

###############name filter#################

filter = {"name" : "recipe_names",

"filter" : ["Grilled Cheese", "Roasted Chicken", "Roasted Vegetables", "Brownies", "Loaf Cake"]
}	

filters.insert(filter)

###############confirmations filter#################

filter = {"name" : "confirmations",

"filter" : ["Done", "Complete", "Finished", "Continue", "Ok", "Next", "Yes"]
}	

filters.insert(filter)

###############previous filter#################
filter = {"name" : "previous",

"filter" : ["previous", "earlier", "last", "back"]
}	

filters.insert(filter)

###############Step filter#################
filter = {"name" : "step",

"filter" : ["step", "instruction"]
}	

filters.insert(filter)

###############Explain filter#################
filter = {"name" : "explain",

"filter" : {"toast":"Toasting means to cook or brown food, generally bread, by exposure to a grill, fire, or other source of radiant heat.",
			"whisk":"Whisking means to beat or stir a substance, especially cream or eggs with a light, rapid movement.",
			"swirl":"Swirling means to move a substance in a twisting or spiralling pattern",
			"truss":"Trussing means to tie up the wings and legs of a chicken or other bird before cooking",
			}
			
}	

filters.insert(filter)
