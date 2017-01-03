bigList = list()
fileName = "2016-12-27_AR005779.log"
cleanedFile = "Updated "+ fileName

with open(fileName, "r") as file:
	line = file.readline()

	for line in file:
		if(line.find("<SwipeData>") != -1):
			bigList.append(line)

		if(line.find("<SubTotAmt>") != -1):
			bigList.append(line)
			
		if(line.find("<ApprovalCode>") != -1):
			bigList.append(line)
			bigList.append("\n\n\n")

with open(cleanedFile, "w") as writeFile:
	for i in range(len(bigList)):
		writeFile.write(bigList[i])
