#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
current_file = None

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # splitting the data on the basis of tab we have provided in mapper.py
    word, fileName, count = line.split('\t', 2)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word and current_file == fileName:
        current_count += count
    else:
        if current_word and current_file:
            # write result to STDOUT
            print('%s\t%s\t%s' % (current_word, current_file, current_count))
        current_count = count
        current_word = word
        current_file = fileName

# do not forget to output the last word if needed!
if current_word == word and current_file == fileName:
    print('%s\t%s\t%s' % (current_word, current_file, current_count))
