ten_things = "Apple Oranges Crows Telephone Light Sugar"

print "Wait there's %d things in that list, let's fix it." % len(ten_things.split(' '))
# splitting string in to list of characters..
stuff = ten_things.split(" ") # telling to split after space.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# list used after while so that when list gets empty it will return False and loop will stop. we could use len(stuff) != 10.
while len(stuff) !=10: 
    next_one = more_stuff.pop() #Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There is %d item now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do something with the stuff."

print stuff[1] # returns Oranges(2nd elemnt in list. list start with 0.)
print stuff[-1] # returns last element of list i.e corn
print stuff.pop(2) # returns 3rd element of list i.e crows.
print ' '.join(stuff) # converts list to string with space after each element in list. (crows removed by pop.)
print "#".join(stuff[3:5]) # pick 4th and 6th element from stuff list after Crows removed and returns with # between them.
 
    
