from sys import argv

script, filename = argv

print "Actual content of file is: "
target = open(filename)
print target.read()

# print "We're going to erase %r." % filename
# print "If you don't want it, press CTRL+C (^C)."
# print "If you want it, press return."

# raw_input("?")	

# print "Opening the target file..."
# print "Erasing content of file. Goodbye!"
# target = open(filename,'w')
# target.truncate()

target_file = open(filename)
print "file should be empty, showing content:"
print target_file.read()
target_file = open(filename)
target_file.close()

print "Please insert three lines:"

line1 = raw_input("Please insert line 1: \n")
line2 = raw_input("Please insert line 2: \n")
line3 = raw_input("Please insert line 3: \n")
line_break = "\n"

print ("Im going to write it to file!")
mode_of_writing = raw_input('Please choose a/w/r: \n > ')
target = open(filename,mode_of_writing)
target.write(line1 + line_break + line2 + line_break + line3)

target = open(filename)
print target.read()
target.close()

