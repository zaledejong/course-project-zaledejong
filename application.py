import subprocess

userInput = input("To search for term, enter 1. To search for top-n words, enter 2. To quit, enter exit. ")
while(userInput != "1" or userInput != "2" or userInput != "exit"):
    if(userInput == "1"):
        term = input("Please enter word: ")
        with open("script3.sh", "w") as file:
            file.write("#! /bin/sh\n\n"+"grep -a -w "+term+ " invertedindex-output")
            file.close
        subprocess.run('docker exec -i namenode bash < script3.sh', shell=True)
        userInput = "0"
        continue
    if(userInput == "2"):
        number = input("Please enter number of top-n results: ")
        with open("script4.sh", "w") as file:
            file.write("#! /bin/sh\n\n"+"cat wordcount-output | sort -n -k2 -r | head -"+number)
            file.close
        subprocess.run('docker exec -i namenode bash < script4.sh', shell=True)
        userInput = "0"
        continue
    if(userInput == "exit"):
        break
    userInput = input("To search for term, enter 1. To search for top-n words, enter 2. To quit, enter exit. ")
