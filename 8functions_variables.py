#this one is like your scripts with argv
# *args lot like argv parameter but for functions.
def print_two(*args):
    arg1, arg2 = args #unpacking the arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# without *args
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
#taking 1 argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
#this takes no argument.
def print_none():
    print "I got nothin'."
    
# calling functions and assigning them values.
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#the variables in above function are not connected to variables in script.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enought for party!"
    print "Get a blanket.\n"
    
print "We can just give the functions number directly"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script."
amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese, amount_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_cheese + 100, amount_crackers + 1000)

#function is called 4 times every time assigning different values to function varibales by different methods.

# use = and a new Python word return to set variables to be a value from a function.

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# giving output from one function in another.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
