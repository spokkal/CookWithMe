from state_machine import StateMachine

context = StateMachine(None)

while 1==1:
	text = raw_input()
	if "CHEF" in text.upper():
		reply = context.update(text.upper())
		print reply
