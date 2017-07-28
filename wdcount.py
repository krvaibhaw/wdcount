
# Importing Libraries

import os
import sys

# Chech for command line arguments
# If not available then exit

if len(sys.argv) != 2:
        sys.exit("Usage: python wdcount.py test.txt")


# Else take the argument as path
 
else:
    path = sys.argv[1]


# Open the file in read mode

f = open(path, "r")

# Read from file

data = f.read()

# Close the file

f.close()

# Split contents of the file into a list of words

l = data.split()

# Print size of the list

print("\nTotal word count :", len(l))