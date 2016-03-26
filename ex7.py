print "Marry had a little lamb."
print "Its fleece was whit as %s." % "Snow"
print "And everywhere that Marry went."
print ".aa.." * 10 #what will that do?

print "a" +"b" + "c ",
print "e" + "f ", "g"

#ex8

formater = "%r %r %r %r"
print formater % (1,2,3,4)

print formater % ("one", 2, 3.00, 4/6)

print formater % (True, False, 1000/5.6565, formater)

print formater % (
"first line of ",
"multiline",
"text",
4
)

# ex9 - printing, printing, printing
months = "\nJan \nFeb\nMar"

multiline_text = """
this is a multiline text




"""
print "text %r" % months #ugly
print "text %s" % months #beautiful!
print multiline_text

# ex10 playing with text!
print "lets insert TAB \there"
print "don't know what \\this \\ does?" #escapes escape character
print "\t* I can has \n\t* stars!"

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,

open("Ex8.py",'w')