print "How old are you?",
age = int(raw_input())		# Converts string input into an int
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = int(raw_input()) 	# Converts string input into an int
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	