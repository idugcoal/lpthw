name = 'Doug H. Cole'
age = 35 # not a lie
height = 70 # inches
weight = 160 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That is %d centimeters." % (height * 2.54)
print "He's %d pounds heavy." % weight
print "That is %d kilograms." % (weight * .453592)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print round(1.7333)