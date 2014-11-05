import web
from session import MongoStore
import pymongo
import datetime


from pymongo import Connection
connection = Connection()

db = connection['CookWithMe']
conversation = db['conversation']
db = c.webpy

#Create a new session object, passing the db and collection name to the MongoStore object
session = web.session.Session(app, MongoStore(db, 'sessions'))

#If you want to do user authentication and stuff aswell, add these two lines
users.session = session
users.collection = db.users
users.SALTY_GOODNESS = u'RANDOM_SALT'


def make_text(string):
	dialog = {"date": datetime.datetime.utcnow(), 
			  "speech": string}
	conversation.insert(dialog);
	connection.close();
	print string;
	return string.upper();

urls = ('/', 'tutorial')
render = web.template.render('templates/')

app = web.application(urls, globals())

my_form = web.form.Form(
                web.form.Textbox('', class_='textfield', id='textfield'),
                )

class tutorial:
    def GET(self):
        form = my_form()
        return render.tutorial(form, "Your text goes here.")
        
    def POST(self):
        form = my_form()
        form.validates()
        s = form.value['textfield']
        return make_text(s)

if __name__ == '__main__':
    app.run()

