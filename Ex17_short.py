from sys import argv
from os.path import exists

# long version
script, file_from, file_to = argv

print "Copying from %s to %s." % (file_from, file_to)
indata = open(file_from).read()
print indata

print "Input file is %d bytes long." % len(indata)

print "Does the outputfile exist? %r" % exists(file_to)
print "Ready? Otherwise CTRL+C aka break"
raw_input()

out_file = open(file_to, 'w')
out_file.write(indata)
out_file = open(file_to, 'r')
print "Allright, content of output file now looks like: \n%s" % out_file.read()
out_file.close()