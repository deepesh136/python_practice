cars = 100
space_in_a_car =4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
#to put variables between print string
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
#strings that have variables embedded in them.
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print "Let's talk about %s." % my_name #no comma and leave space too.
print "He's is %d inches tall." % my_height #%s for strings and %d for integer.
print "He's %d pounds heavy." % my_weight
print "He's got %s eyes and %s hair." % (my_eyes, my_hair) #for two variables in one string use bracket.
print "His teeth are usually %s depending on the coffee." % my_teeth
print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
#use of %r: print it no matter what is in it
i = 10
j = 'Hello'
print "integr=%r string=%r" % (i, j)
#string practice
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)
print x, y
print "I said: %r." % x
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't that joke so funny! %r"
print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."
print w + e
