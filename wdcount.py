
import os
import sys

if len(sys.argv) != 2:
        sys.exit("Usage: python wdcount.py test.txt")

else:
    path = sys.argv[1]

f = open(path, "r")
data = f.read()
f.close()

l = data.split()
print("\nTotal word count :", len(l))