#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

stoplist = ["a", "about", "above", "after", "again", "against", "all", "am",
            "an", "and", "any", "are", "aren't", "as", "at", "be", "because",
            "been", "before", "being", "below", "between", "both", "but",
            "by", "can't", "cannot", "could", "couldn't", "did", "didn't",
            "do", "does", "doesn't", "doing", "don't", "down", "during",
            "each", "few", "for", "from", "further", "had", "hadn't", "has",
            "hasn't", "have", "haven't", "having", "he", "he'd", "he'll",
            "he's", "her", "here", "here's", "hers", "herself", "him",
            "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm",
            "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its",
            "itself", "let's", "me", "more", "most", "mustn't", "my",
            "myself", "no", "nor", "not", "of", "off", "on", "once", "only",
            "or", "other", "ought", "our", "ours", "ourselves", "out",
            "over", "own", "same", "shan't", "she", "she'd", "she'll",
            "she's", "should", "shouldn't", "so", "some", "such", "than",
            "that", "that's", "the", "their", "theirs", "them", "themselves",
            "then", "there", "there's", "these", "they", "they'd", "they'll",
            "they're", "they've", "this", "those", "through", "to", "too",
            "under", "until", "up", "very", "was", "wasn't", "we", "we'd",
            "we'll", "we're", "we've", "were", "weren't", "what", "what's",
            "when", "when's", "where", "where's", "which", "while", "who",
            "who's", "whom", "why", "why's", "will", "with", "won't", "would",
            "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your",
            "yours", "yourself", "yourselves"]

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    # we are looping over the words array and printing the word
    # with the count of 1 to the STDOUT
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        if word.lower() not in stoplist:
            print('%s\t%s' % (word, 1))
