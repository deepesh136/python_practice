print "Let's practice everything." # single quote ' used inside double "
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'    # \ used to escape single quote under single quote. \\ escapes single \ and \n newline character , \t tab character.

# triple quote string used.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five # math output

# use of function.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
start_point = 10000
# giving start_point value to started variable in secret_formula and returning functions values to three script variables.
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

