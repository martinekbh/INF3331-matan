import sys
import os


#Check for right number of args from command line
if len(sys.argv) != 3:
    print("You need to provide 2 arguments - the searchword and the directory to search in")
    exit()

#Proceed to search for right files in the given directory
searchword = sys.argv[1]
directory = sys.argv[2]

if os.path.exists(directory):
    #print("SEARCHING IN " + directory + " FOR FILES WITH " + searchword + " IN THE FILENAME...\n")
    
    for root, dirs, files in os.walk(directory):
        for name in files:
            if searchword in name:
                print(os.path.join(root, name))
else:
    print(directory + " is not a path to any directory. Check your input.")
