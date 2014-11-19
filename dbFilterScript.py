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

"filter" : ["Done", "Complete", "Finished", "Continue"]
}	

filters.insert(filter)