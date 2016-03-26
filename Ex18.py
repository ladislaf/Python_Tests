#kinda like with argv
def print_two_strings(*args):
	arg1, arg2 = args
	print "Argument 1: %r, Argument 2: %r" % (arg1, arg2)

#beware of the intendation(!)
print_two_strings("Lada", "Vlcek")

#empty function
def print_dummy_text():
	print "Dummy text"
	
print_dummy_text()

#function with one argument
print_me = raw_input("please input some text \n > ")
def print_me_one_string_please(argument1):
	print "This is your \"some text:\" %s" % argument1

print_me_one_string_please(print_me)

