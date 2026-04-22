import argparse
import subprocess
import sys

#INITIALISER - takes file arguments and processes them
parser = argparse.ArgumentParser(description="Takes a level.dat input file and asks details on what to do with it, then passes the information on to main.py.")
parser.add_argument("inputFile", type = str, help = "A Minecraft level.dat file (1.21.11 or older), to be downgraded")
inputArgs=parser.parse_args()


#function definitons 
def queryOptions():
	versionUserInput = input("Which version would you like to convert to?\n12w49a -> 1\nBeta 1.7.3 -> 2\n?) ")
	try:
		intUserInput = int(versionUserInput)
		return intUserInput
	except:
		return 0
	

def validateInput(dataInput):
	if type(dataInput) != int:
		print("Invalid data type. If you're seeing this, the code is probably broken. Please open a GitHub issue ASAP.")
		return False
	version = dataInput
	if version != 1 and version != 2:
		return False
	else:
		return True


if __name__ == "__main__":
	while True:
		userInput = queryOptions()
		if validateInput(userInput):
			print("Running converter.......")
			subprocess.run([sys.executable, "main.py", inputArgs.inputFile, "--versionChoice", str(userInput)]) # need to set up arguments on cookie's code and rewrite file opening
			break
		else:
			print("Invalid version. Please try again:")
			continue
