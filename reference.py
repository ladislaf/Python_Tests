###Ladas reference to python:###

#import z modulu
#command line ARGument Variables
from sys import argv
#import exists
from os.path import exists

#argv assigment
script_name = argv

#print
string = "String"
cislo = 1
raw = "i s uvozovkami"
print "Text %s, Cislo %d, Raw %r" % (string, cislo, raw)

#vstup od usera:
user_input = raw_input ("tohle uvidi uzivatel> ")

#file open and read and close(!)
file_open = open("reference.py")
print file_open.read()
file_open.close()

#file open and write newline and close(!)
file_open = open("reference.py", "a")
print file_open.write("\n#newline")
file_open = open("reference.py")
print file_open.read()
file_open.close()

#length of text
file_open = open("reference.py")
print (len(file_open.read()))
file_open.close()

#does file exist in path?
file_to_check_for_existance = "Ex21.py"
print "Is is it true that file %s exists in current folder?" %file_to_check_for_existance, exists(file_to_check_for_existance)

#function to return logic after called
def gather_status(weekday):
	return "Weekday:" + weekday
print gather_status("Tue")
#newline
#newline
#newline