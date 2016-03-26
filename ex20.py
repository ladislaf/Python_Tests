from sys import argv

script, input_file = argv

#script will read file and then rewind it...?
def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print line_count, f.readline(2)

current_file = open(input_file)

#REWIND whatever that means?
rewind(current_file)

# print "Let's print whole file"
#print_all(current_file)
print_a_line(1,current_file)
print_a_line(2,current_file)