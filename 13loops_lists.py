"""Before you can use a for-loop, you need a way to store the results of loops somewhere. The best way to do this is with a list. A list is exactly what its name says, a container of things that are organized in order."""

the_count = [1, 2, 3, 4, 5] #way to initialize list.
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Printing list with numbers.
for numbers in the_count:
    print "The count : %d" % numbers
    
# printing strings in list
for fruit in fruits:
    print "fruits = %s" % fruit
    
# list with numbers and strings.
for i in change:
    print "change : %r" % i
    
elements = [] # initializing empty list.

# using range function.
for j in range(0, 6):
    print "Adding %d to list." % j
    elements.append(j) #apend() used for adding things to empty list.

print elements


"""
A while-loop will keep executing the code block under it as long as a boolean expression is True."""

k = 0
number = []

while k<6:
    print "At the top i is %d" % k
    number.append(k)
    
    k = k +1
    print "now number: ", number
    print "At the bottom i is %d" % k
    
#printing numbers.
for num in number:
    print num
