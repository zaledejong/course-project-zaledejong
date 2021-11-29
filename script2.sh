#! /bin/sh

hadoop fs -mkdir -p tmp
hadoop fs -put input

mapred streaming \
-file wordcount_mapper.py -mapper 'python wordcount_mapper.py' \
-file wordcount_reducer.py -reducer 'python wordcount_reducer.py' \
-input input/* \
-output wordcount_output

mapred streaming \
-file invertedindex_mapper.py -mapper 'python invertedindex_mapper.py' \
-file invertedindex_reducer.py -reducer 'python invertedindex_reducer.py' \
-input input/* \
-output invertedindex_output

hadoop fs -getmerge wordcount_output wordcount-output
hadoop fs -getmerge invertedindex_output invertedindex-output
