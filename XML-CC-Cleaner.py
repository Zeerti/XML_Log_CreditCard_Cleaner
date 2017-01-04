import glob
import os

os.chdir(os.curdir) #change directory to current directory where script is located
fileNames = list() #file list
bigList = list() #

#Get list of Files
def _get_List_Of_Files():
	for file in glob.glob("*.txt"):
		fileNames.append(file)
		
	for file in glob.glob("*.log"):
		fileNames.append(file)

	#Convert list array to string
	",".join(str(x) for x in fileNames)



def _find_Credit_Data(currentFile):
	with open(currentFile, "r") as file:
		line = file.readline()
	
		for line in file:
			if(line.find("<SwipeData>") != -1): #-1 = Failure
				bigList.append(line)
	
			if(line.find("<SubTotAmt>") != -1): #-1 = Failure
				bigList.append(line)
				
			if(line.find("<ApprovalCode>") != -1): #-1 = Failure
				bigList.append(line)
				bigList.append("\n\n\n") #Approval code is always last to be found (should be at least) this creates a seperation for readability


#Appears to miss the last thing in the bigList() OR is failing to save the last item found into the bigList()
def _write_cleaned_to_file(currentFile): 
	if not bigList: #No hits found.
		print("UNABLE TO LOCATE SHIT")
		return 0
	else:

		print("WRITING TO CURRENT FILE: {}".format(fileNames[currentFile]))
		cleanedFile = "Updated "+ fileNames[currentFile] #Get last file in list and set updated list
		with open(cleanedFile, "w") as writeFile: #Write to file and delete entry when completed
			for o in range(len(bigList), 0, -1):
				print(o)
				print("ITEM LIST: {}".format(len(bigList)))

				writeFile.write(bigList[o-1])
				bigList.pop(o-1)
				
	
	

#####################
##START SCRIPT HERE##
#####################

_get_List_Of_Files()#Find all files in current directory and save them

for i in range(len(fileNames), 0, -1): 

	_find_Credit_Data(fileNames[i-1]) #open and search file for matches
	_write_cleaned_to_file(i-1) #Write newly cleaned files
	







