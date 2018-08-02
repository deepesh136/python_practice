# dict let you use anything, not just no. for index.

things = ['a', 'b', 'c', 'd']
stuff = {'name': 'Zed', 'age': 23, 'height': '6feet'}

print stuff['name']

print things[1]

# you can add things to list later also or replace elements.
things[2] = "z" # use quote to fill string in list. "", ''
stuff['city'] = "kgp"

print stuff
print things

# to delete things from list.

del stuff['height']
print stuff

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap: # check if input is in list or not.
        return themap[state]
    else:
        return "Not found."
        
cities['_find'] = find_city # function added to the list.Why?
print cities

while True: # creating infinte loop
    print "State? (Enter to quit)",
    state = raw_input("> ")
    
    if not state: # if not state means when no input by user just enter quit.
        print "quit."
        break
    city_found = cities['_find'](cities, state) # function called here.First python finds the dict than the index given than it knows its a function to call with parameter cities, state.
    print city_found
