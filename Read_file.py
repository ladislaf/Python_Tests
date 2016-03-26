#takes filename as input, prints its content
from sys import argv

scriptname, filename = argv

file_open = open(filename)
print "Content of file is:"
print file_open.read()
file_open.close()
