print "Mary had a little lamb." #printing normal string.
print "Its fleece was white as %s" % 'snow' #printing string in string.
print "And everywhere that Mary went."
print "." * 10 # prints '.' 10 times.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# comma used to print words with space i.e cheese burger not cheese \n(next line) burger
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# using comma puts space between two strings.
print formatter % (
    "I had this thing.",
    "That could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ", days # prints days string as it is.
print "Here are the months: ", months # \n used for giving space.
# printing strings with next line as it is us triple quote.note no comma used as in formatter one.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much we like
Every 4 lines if want.
"""
# """ , \, \\ use.
tabby_cat = "\tI'm tabbed in." # \t used to give tab space.
persian_cat = "I'm split\n on a line." #\n used for next line
backslash_cat = "I'm \\a \\ cat." # prints one \ insted of \\
double_quote = "I am 6'2\" tall." # \used to consider " as part of string and not end
single_quote = 'I am 6\'2 tall.'
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat 
print backslash_cat 
print fat_cat
print single_quote 
print double_quote
