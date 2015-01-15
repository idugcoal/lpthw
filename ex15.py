# Import the argv module from sys
from sys import argv

# Get the script name and the filename from argv
script, filename = argv

# Store the contents of filename into txt
txt = open(filename)

# Output the filename
print "Here's your file %r: " % filename
# Output the contents of txt
print txt.read()

# Prompt for the filename again
print "Type the filename again:"
# Store user input into file_again
file_again = raw_input("> ")

# Store the contents of file_again into txt_again
txt_again = open(file_again)

# Print the contents of txt_again
print txt_again.read()

# Close txt
txt.close()
# Close txt_again
txt_again.close()