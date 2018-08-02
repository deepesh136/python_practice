# script that also accepts arguments.
# add festures to your script from Python feature set.
from sys import argv
# argv variable holds the arguments you pass to your Python script when you run it.
'''
script, first, second, third = argv #unpacking argv to assign arguments to four variables.

print "the script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
'''
#to run this script type on terminal as python more_input_practice.py first 2nd third . this will take script = more_input_practice, first = first, second = 2nd and so on.Called Passing command line arguments.
script, user_name = argv #
prompt = '> ' #after print question ask input as > (input) with newline

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)
print "where do you live %s." % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

