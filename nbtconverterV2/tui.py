#!/bin/python3
import subprocess
import pathlib
import nbtlib
import sys



#function definitons 
def queryOptions():
	data = [-1,-1]
	inputFile = input("Please enter the path to your level.dat file. Press enter to use level.dat in the current directory.\n(Press q to quit)\n?) ")
	if inputFile.lower() == "q":
		print("Exiting...")
		exit()
	if inputFile:	
		data[0] = inputFile.replace("\\","")
	else:
		data[0] = "level.dat"
	print("\n=================================================\n")
	versionUserInput = input("Which version would you like to convert to?\n(Press q to quit)\n12w49a -> 1\nBeta 1.7.3 -> 2\n?) ")
	if versionUserInput.lower() == "q":
		print("Exiting...")
		exit()
	try:
		intUserInput = int(versionUserInput)
		data[1] = intUserInput
	except:
		data[1] = 0
	return data
	

def validateInput(dataInput):
	validated = [False,False]
	# check the function is being fed the correct data
	if type(dataInput[0]) != str:
		print("Invalid data type. If you're seeing this, the code is probably broken. Please open a GitHub issue ASAP.")
		validated[0] = False
	if type(dataInput[1]) != int:
		print("Invalid data type. If you're seeing this, the code is probably broken. Please open a GitHub issue ASAP.")
		validated[1] = False
	# check it's a real file and that it's an actual level.dat file
	filePath = dataInput[0]
	pathCheck = pathlib.Path(filePath)
	if pathCheck.is_file():
		try:
			nbtlib.load(filePath)
			validated[0] = True
		except:
			validated[0] = False
	# check the version input is either 1 or 2
	version = dataInput[1]
	if version == 1 or version == 2:
		validated[1] = True
	return validated





if __name__ == "__main__":
	while True:
		userInput = queryOptions()
		validated = validateInput(userInput)
		if validated[0]:
			if validated[1]:
				print("Running converter.......")
				subprocess.run([sys.executable, "main.py", userInput[0], "--versionChoice", str(userInput)]) # need to set up arguments on cookie's code and rewrite file opening
				break
			else:
				print("Invalid version. \nPlease try again:\n")
				continue
		else:
			print("Invalid level.dat file. Please check the path and make sure it's actually a level.dat file. \nTry again:\n")
			continue







