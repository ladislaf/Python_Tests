#functions returning and printing variable
print "Please define your number:"
your_number = int(raw_input("> "))
def add_one(a):
	#print "Adding 1 to your number %d" % a
	return a + 1

print "I have added one to your number:", add_one(your_number), "."