# initial setup

# user runs the following commands
# git clone https://github.com/zdejong/docker-hadoop.git
# cd /docker-hadoop
# docker-compose up -d

import subprocess

# docker initialization
subprocess.run('docker exec -i datanode bash < script.sh', shell=True)
subprocess.run('docker exec -i nodemanager bash < script.sh', shell=True)
subprocess.run('docker exec -i namenode bash < script.sh', shell=True)

# may need to execute these as well
# subprocess.run('docker exec -i historyserver bash < script.sh', shell=True)
# subprocess.run('docker exec -i resourcemanager bash < script.sh', shell=True)

subprocess.run('docker cp wordcount_mapper.py namenode:/wordcount_mapper.py', shell=True)
subprocess.run('docker cp wordcount_reducer.py namenode:/wordcount_reducer.py', shell=True)
subprocess.run('docker cp invertedindex_mapper.py namenode:/invertedindex_mapper.py', shell=True)
subprocess.run('docker cp invertedindex_reducer.py namenode:/invertedindex_reducer.py', shell=True)

userInput = input("Load engine? [Y/n] ")
while(userInput != "Y"):
    if(userInput == "n"):
        quit()
    print("Please enter Y to continue or n to quit. ")
    userInput = input("Load engine? [Y/n] ")


subprocess.run('docker cp data/ namenode:/input', shell=True)
subprocess.run('docker exec -i namenode bash < script2.sh', shell=True)
