-how to run this application-

First the user should open a terminal of their choice and navigate to the folder that they downloaded. The terminal should have git installed to be able to clone my repository.
E.g. cd Documents/course-project-zaledejong
git clone https://github.com/zaledejong/course-project-zaledejong

Then the user should have the Docker Desktop application and be able to run docker commands, inputting into the terminal:
docker-compose up -d

This starts the 5 Hadoop containers in Docker. At this point the user should place the files they want to parse in the data folder. The three .tar.gz files used as examples are already in this folder, and can be replaced.

From there, the user should have python3 installed in their terminal, and should run:
python3 setup.py

This installs python in the three containers datanode, nodemanager, and namenode. (Note, if the next step of loading the engine does not work, the user may have to install python in the other two containers as well and decomment the two commands that perform this action.)

If the user has not placed their text files in the data folder, they can enter n at this point. After entering Y to load the engine, the script copies the data folder into the namenode container and performs both an inverted index MapReduce and a word count MapReduce. At this point, the user no longer has to use the setup.py file. (Note, the user should not change the data files at this point. When docker copies the data folder into the namenode, if this operation is performed again, the new data folder is copied into the existing data folder, resulting in a data folder inside of a data folder.)

Now, the user should run:
python3 application.py

This program asks the user if they want to search for a term or return the top-n words from the files. The reason why both an inverted index and word count MapReduce was performed is because searching for a term uses the results from the inverted index MapReduce, and the top-n words uses the output from the word count MapReduce. The word count MapReduce uses a stoplist to replace any common words such as and or the. However, the user may want to search for these common words, and would do so using the results from the inverted index.