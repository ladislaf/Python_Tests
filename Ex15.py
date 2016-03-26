from sys import argv

script, filename = argv

txt = open(filename)
print "This is your file %r: " % filename
print txt.read()

print "Type the file name again"
file_name_again = raw_input("> ")

txt_again = open(file_name_again)

print txt_again.read()

txt.close()
txt_again.close()