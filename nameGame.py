"""
    nameGame.py
    The Name Game

    Dylan Grandjean
    September 7th, 2016

    This program manipulates strings.

    Enter a person's name and you will get back
    (X), (X), bo-b(X[1:])
    Banana-fana fo-f(X[1:])
    Fee-fi-mo-m(X[1:])
    X!
"""

name = raw_input("What's your name? ")

# Checks the first letter of the name in order to determine how it will use given name
# If begins with a vowel, keep the whole name in lower case
if name[0] == ("A" or "a" or "E" or "e" or "I" or "i" or "O" or "o" or "U" or "u" or "Y" or "y"):
    name_b = name.lower()
# Else remove the first letter and proceed
else:
    name_b = name[1:]

# Print formatted output
print "%s, %s, bo-b%s" %(name, name, name_b)
print "Banana-fana fo-f%s" %name_b
print "Fee-fi-mo-m%s" %name_b
print "%s!" %name

