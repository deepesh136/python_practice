#comma used so print doesn't end the line with a newline and go to the next line
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()
# raw_input() coverts input to string.eg: in height u can't give in put as 6'2"" but you can give it to raw_input().

y = raw_input("Name? ")
print "So, youre %r old, %r tall, %r heavy.And your name is: %r" % (age, height, weight, y)
