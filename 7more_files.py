from sys import argv
#exists returns True if a file exists, based on its name in a string as an argument. It returns False if not.
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "the input file is %d bytes long" %len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("> ")

output = open(to_file, 'w')
output.write(indata)

print "Alright, All done."

output.close()
input.close()

