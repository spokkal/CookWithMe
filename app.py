import web
from text_processing import*
from state_machine import StateMachine

import pymongo
import datetime

from pymongo import Connection
connection = Connection()

db = connection['CookWithMe']
conversation = db['conversation']

web.config.debug = False

processing = Text_Processing()

urls = ('/', 'tutorial')
render = web.template.render('templates/')

app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'context': None})
        

my_form = web.form.Form(
                web.form.Textbox('', class_='textfield', id='textfield'),
                )
flag = False	
def make_text(string, context):
	global flag
	toReturn = ""
	
	print(string)
	if "CHEF" in string.upper(): 
		toReturn = processing.process(string.upper(), context)
		flag = True
	elif flag:
		toReturn = processing.process(string.upper(), context)
	else:
		toReturn = "I am sorry, I didn't understand you. Please say Chef to start cooking."
	
	dialog = {"date": datetime.datetime.utcnow(), 
			  "user": string, "Chef": toReturn}
	conversation.insert(dialog);
	connection.close();

	return toReturn
	
class tutorial:
		
	def GET(self):
		global flag
		flag = False
		session.context = StateMachine(None)
		form = my_form()
		return render.tutorial(form, "Your text goes here.")
        
	def POST(self):
		form = my_form()
		form.validates()
		s = form.value['textfield']
		return make_text(s, session.context)

if __name__ == '__main__':
    app.run()

