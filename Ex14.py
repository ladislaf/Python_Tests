from sys import argv

script, user_name, user_surname = argv
prompt = '> '

print "Welcome user named: %s %s, this is your script named %s" % (user_name, user_surname, script)
print "How do You like me %s" % user_name
likes = raw_input(prompt)

print """
So as %s %s indicated, he likes this program 
(using his own words): %s
""" % (user_name, user_surname, likes)

open("Ex15.py", "w")