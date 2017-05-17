print "Exercise 5: More Variables and Printing\n"

print "CODE\n"

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
height_in_cm = height * 2.54
weight = 180 #lbs
weight_in_kg = weight * 0.45
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "Thats %r in cm" %height_in_cm
print "He's %d pounds heavy." % weight
print "or %d four our friends across the pound" % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usally %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)

print "\nSTUDY DRILLS\n"

print "(1): Change all the cariables so there is no my_ in front of each one. Make sure you change the name everwhere, not just where you used = to set them.\n"

print "(2): Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.\n"

print "(3): Search online for all of the Python format characters.\n"

print "(4): Try more format characters. %r is very useful one. It's like saying 'print this no matter what.'"
