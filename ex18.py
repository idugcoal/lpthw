# This one is like the scripts with argv
# *args receives all input parameters as a list
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# This takes no arguments
def print_none():
	print "I got nothin."

print_two("Doug", "Cole")
print_two_again("Douglas", "Cole")
print_one("Champion")
print_none()
