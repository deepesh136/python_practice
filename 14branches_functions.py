from sys import exit

def gold_room():
    print "This room is full of gold.How much do you want?"
    
    next = raw_input("> ")
    # another way for writing if statemnent. or used so true whether 0 or 1.
    if "0" in next or "1" in next:
        how_much = int(next) #next a string(raw input)
    else:
        dead("Man, learn to type a number") #calling function dead
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard")
 # called when start input is left       
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False  #value for bear_moved set to False by deafult its True.
    
 # it is an infinite loop however we are calling dead function so it will stop when function gets called.
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:  # enters if condition when input = taunt bear. True and True = True.
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True # converting value to true to exit the loop.
        elif next == "Taunt bear" and bear_moved: # enters after above condition by again checking the input.
            dead("The bear gets pissed off and chews your leg off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
# based on the input flee or head it either goes back to function start or to function dead() with some another strings.if anyother input function gets called again.          
def cthulu_room():
    print "How you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty.")
    else:
        cthulu_room()
        
# whenever it is called it will print the passes string plus goodjob. and exit the code.        
def dead(why):
    print why, "Good job!"
    exit(0) #exiting the loop
  
# first it gets called.and print below three lines.  
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"    
    
    next = raw_input("< ") #based on input following condition works.
    
    if next == "left": #if input is "left" bear_room() called.
        bear_room()
    elif next == "right": # if right tha cthulu_room().
       cthulu_room()
    else:  # if any other input than dead() called with string paased as argument.
        dead("You stumble around the room until you starve.")
        
        
start()  #first this function will be called when we run the program.
