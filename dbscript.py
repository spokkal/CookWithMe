from pymongo import MongoClient

cl = MongoClient()
db = cl.CookWithMe
recipes = db.recipes
recipes.remove()

###############Grilled Cheese#################

recipe = {"name" : "Grilled Cheese",

"feeds" : 1,

"ingredients" : [ { "name": "sandwich bread", "qty" : 2, "measure": "slices"},
{ "name": "american cheese", "qty" : 2, "measure": "slices" },
{ "name": "butter", "qty" : 1, "measure" : "tablespoons"},
{ "name": "salt", "qty": "a pinch of", "measure" : "" } ],

"instructions": [ { "transcript": "Melt a half of the butter in a non-stick or cast iron pan over relatively low heat"},
{  "transcript": "Toast the slices of bread on one side until they are an even pale golden brown and remove from the pan"},
{  "transcript": "Add the cheese slices to the bread on the toasted side and close the sandwich, toasted-side-in"},
{  "transcript": "Add the other half of the butter to the pan and melt it over low to medium-low heat" },
{  "transcript": "Add the sandwich to the pan and swirl it around to collect the butter, then cook low and slow till it gets even color for about five minutes", "time": "5", "measure" : "minutes"},
{  "transcript": "Remove the sandwich once it is golden brown, and season with a sprinkle of salt"}],

"cooktime" : 15
}	

recipes.insert(recipe)


#############Roasted Chicken###################

recipe = {"name" : "Roasted Chicken",

"feeds" : 4,

"ingredients" : [ { "name": "whole chicken", "qty" : 1, "measure": ""},
{ "name": "ground pepper", "qty" : "a pinch of", "measure": "" },
{ "name": "salt", "qty": "a pinch of", "measure" : "" } ],

"instructions": [ { "transcript": "Let your chicken come to room temperature before you roast it. Cold chicken takes longer to cook and will not be tender"},
{  "transcript": "Wash your chicken a little"},
{  "transcript": "Preheat the oven to 450 degrees Fahrenheit"},
{  "transcript": "Dry the chicken really well both on the outside and inside"},
{  "transcript": "Sprinkle salt and pepper inside the chicken cavity as much as you prefer" },
{  "transcript": "Truss the chicken using a butcher's knife. Tie the legs together and tie the wings close to the body"},
{  "transcript": "Season the outside of your chicken with lots of salt and some pepper"},
{  "transcript": "Place the chicken, breast side up on a rack over a roasting pan"},
{  "transcript": "Put it in the 450 degrees Fahrenheit oven for 50-60 minutes. Do not flip, blast or open the oven unless necessary"},
{  "transcript": "Your chicken is done when its internal temperature is 165 degrees. Serve it after 15 minutes"} ],

"cooktime" : 70
}	

recipes.insert(recipe)


#############Roasted Vegetables##################

recipe = {"name" : "Roasted Vegetables",

"feeds" : 2,

"ingredients" : [ { "name": "broccoli", "qty" : 1, "measure": "head"},
{ "name": "yellow squash", "qty" : "1", "measure": "" },
{ "name": "cherry tomatoes", "qty" : "1", "measure": "cup" },
{ "name": "carrots", "qty" : "3", "measure": "" },
{ "name": "olive oil", "qty" : "quarter", "measure": "cup" },
{ "name": "ground pepper", "qty" : "2", "measure": "tablespoons" },
{ "name": "salt", "qty": "3", "measure" : "tablespoons" } ],

"instructions": [ { "transcript": "Chop the broccoli and carrots in to small pieces. Remove the stalk of broccoli"},
{  "transcript": "Chop the yellow squash into half moons"},
{  "transcript": "Slice cherry tomatoes in half"},
{  "transcript": "Preheat oven to 425 degrees Fahrenheit"},
{  "transcript": "In a large bowl, toss all the vegetables together with olive oil, salt, and pepper" },
{  "transcript": "Divide the vegetables among two jelly roll pans"},
{  "transcript": "Roast vegetables for 35-40 minutes, removing the vegetables from the oven every 15 minutes to stir around"},
{  "transcript": "You can add any vegetable to the recipe and adjust the salt and pepper as per your preference"} ],

"cooktime" : 60
}	

recipes.insert(recipe)


##############Brownies#################

recipe = {"name" : "Brownies",

"feeds" : 2,

"ingredients" : [ { "name": "unsweetened chocolate", "qty" : "2", "measure": "ounces" },
{ "name": "butter", "qty" : "4", "measure": "tablespoons" },
{ "name": "eggs", "qty" : "4", "measure": "" },
{ "name": "sugar", "qty" : "two", "measure": "cups" },
{ "name": "all-purpose flour", "qty" : "two", "measure": "cups" },
{ "name": "salt", "qty": "half", "measure" : "teaspoon" } ],

"instructions": [ { "transcript": "Preheat your oven to 350 degrees. Spray a pan with cooking spray and set aside" }, 
{	"transcript": "Boil a little more than half a cup of water"},
{  "transcript": "Finely chop the chocolate"},
{  "transcript": "Melt the butter"},
{  "transcript": "Extract yolks from two of the four eggs"},
{  "transcript": "Stir in the unsweetened chocolate to the boiling water and mix until melted"},
{  "transcript": "Add the butter, eggs, yolks. Whisk until the batter is smooth"},
{  "transcript": "Combine the flour, sugar, and salt in a small bowl. Gently combine the dry ingredients with the wet. Fold until fully incorporated"},
{  "transcript": "Spread your batter into your prepared pan. Smooth out with the back of a spoon"},
{  "transcript": "Bake for 30 to 35 minutes"}
],

"cooktime" : 45
}	

recipes.insert(recipe)


##############Loaf Cake#################


recipe = {"name" : "Loaf Cake",

"feeds" : 8,

"ingredients" : [ { "name": "baking powder", "qty" : "one", "measure": "teaspoon"},
{ "name": "canola oil", "qty" : "half", "measure": "cup" },
{ "name": "eggs", "qty" : "3", "measure": "" },
{ "name": "sugar", "qty" : "1", "measure": "cup" },
{ "name": "all-purpose flour", "qty" : "two", "measure": "cups" },
{ "name": "salt", "qty": "half", "measure" : "teaspoon" } ],

"instructions": [ { "transcript": "Preheat your oven to 350 degrees. Oil a loaf pan and set aside" }, 
{	"transcript": "In a bowl, whisk together the flour, baking powder, and salt"},
{  "transcript": "In another bowl, whisk the eggs, sugar and vanilla together until well blended"},
{  "transcript": "Add the dry ingredients and stir until smooth"},
{  "transcript": "Pour in the oil and use the whisk to gently but thoroughly fold it into the batter"},
{  "transcript": "Put the batter in the loaf pan and bake 50 to 55 minutes"},
{  "transcript": "Cool on a rack for 5 minutes, then unmould and cool to room temperature right-side up"},
],

"cooktime" : 70
}	

recipes.insert(recipe)
###############################
						