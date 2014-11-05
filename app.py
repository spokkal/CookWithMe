import web
from text_processing import*

web.config.debug = False

processing = Text_Processing()

urls = ('/', 'tutorial')
render = web.template.render('templates/')

app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'context': None})
        

my_form = web.form.Form(
                web.form.Textbox('', class_='textfield', id='textfield'),
                )
	
def make_text(string, context):
	toReturn = ""
	print(string)
	if "CHEF" in string.upper(): toReturn = processing.process(string.upper(), context)
	return toReturn
	
class tutorial:
		
    def GET(self):
    	session.context = Initial_State()
        form = my_form()
    	return render.tutorial(form, "Your text goes here.")
        
    def POST(self):
        form = my_form()
        form.validates()
        s = form.value['textfield']
        return make_text(s, session.context)

if __name__ == '__main__':
    app.run()
