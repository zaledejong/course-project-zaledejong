#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys
import os


# reading entire line from STDIN (standard input)
for line in sys.stdin:

    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    # we are looping over the words array and printing the word
    # with the count of 1 to the STDOUT
    for word in words:
        # get the file name
        try:
            fileName = os.environ["mapreduce_map_input_file"]
        except KeyError:
            fileName = os.environ["map_input_file"]
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        print('%s\t%s\t%s' % (word, fileName, 1))
