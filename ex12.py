from sys import argv

script, first, second, third = argv

first = raw_input("What is the name of first variable?")
second = int(raw_input("Please type in your favourite number"))
print "This script is called", script
print "First variable is called: ", first , " ."
print "Second variable is called: ", second , " ."
print "Third variable is called: ", third , " ."

open("Ex14.py",'w')