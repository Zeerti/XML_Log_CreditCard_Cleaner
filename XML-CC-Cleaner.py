import glob
import os
import pprint

os.chdir(os.curdir) #change directory to current directory where script is located
fileNames = list() # All discovered files in directory
bigList = list() # All found matches

# Get Keywords for search and extensions to open
def _get_UserInput():
    global extensionKeys
    global splitKeys

    searchExtension = input("Input all file extensions to open and search. E.G \"xml txt csv\" with spaces as a delimiter: ").lower()
    extensionKeys = searchExtension.split(' ')
    searchKey = input("Input keys to search by. Use spaces for multiple keywords(cAsE SeNsiTivE):  ")
    splitKeys = searchKey.split(' ')

#Get list of Files
def _get_List_Of_Files():
    for key in extensionKeys:
        for file in glob.glob("*." + str(key)):
             fileNames.append(file)
             
    ",".join(str(x) for x in fileNames)
    print(fileNames)

# Search all files in fileNames for key "splitKeys"
def _find_UserInput():
    for file in fileNames:
        print("Opening file: {}".format(file))
        with open(file, "r") as file:
            line = file.readline()

            while line:
                for key in splitKeys:
                    if(line.find(key) != -1): #-1 = failure
                        bigList.append(line) # Append entire line for future reference
                line = file.readline()# Read in next line
            



_get_UserInput()
_get_List_Of_Files() #  Find all files in current directory and save them
_find_UserInput() # 
pprint.pprint(bigList) # Output all search matches to console
