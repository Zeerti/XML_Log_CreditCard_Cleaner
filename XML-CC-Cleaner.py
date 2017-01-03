bigList = list()
fileName = "2016-12-27_AR005779.log"
cleanedFile = "Updated "+ fileName

with open(fileName, "r") as file:
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
with open(cleanedFile, "w") as writeFile:
	for i in range(len(bigList)):
		writeFile.write(bigList[i])


