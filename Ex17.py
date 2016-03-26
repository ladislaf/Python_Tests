from sys import argv
from os.path import exists

# long version
script, file_from, file_to = argv
#oneliner to copy from file_from to file_to

open(file_to, 'w').write(open(file_from).read())
