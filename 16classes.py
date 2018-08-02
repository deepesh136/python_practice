"""
 Self , it is the extra parameter that Python creates so you can type a.some_function () and then
 will translate that to really be some_function (a). Why use self? Your function has no idea what
 you are calling any one instance of TheThing or another, you just use a generic name self.
 __init__():
    That is how you set up a Python class with internal variables. You can set them on
 self with the . (period) just like I ll show you here. See also how we then use this in add_me_u
 p () later which lets you add to the self.number you created.
"""

class TheThing(object):
    def __init__(self):
        self.number = 0
        
    def some_function(self):
        print "I got called."
        
    def add_me_up(self, more):
        self.number += more
        return self.number
        
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print a.add_me_up(20)
print b.add_me_up(30)
print b.add_me_up(30)

print a.number
print b.number


