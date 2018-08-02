# script to load files. Use argv and raw_input to ask the user what file they want instead of "hard coding the file's name."
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#playing with text file file_sample.txt
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C.",
print "If you do want that hit RETURN."

raw_input("?.. ") #can use any prompt like > , *, ?.

print "Opening the file..."
target = open(filename, 'w') #w to give permission to write file

print "Truncating the file. Goodbye!."
target.truncate() #deleting complete file

print "Now I am going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Dne editing file now closing it."
target.close() # close file after use to save it.

